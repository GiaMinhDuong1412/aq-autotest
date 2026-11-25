'use strict';
/**
 * Cửa sổ PR merge (TFS) – "Mức 1" (người dùng chốt 25/11): app MỞ pull request trong cửa sổ riêng, NGƯỜI TEST tự bấm Complete;
 * app chỉ THEO DÕI trạng thái PR (GET API TFS cùng phiên, 3 giây/lần) và khi PR = completed thì tự chụp cửa sổ gửi về trang
 * (trang tải ảnh lên ACS → "Đã Complete merge <link>" vào Nội dung Tester test). App KHÔNG bấm Approve / Complete, không gọi API ghi TFS.
 *
 * Đăng nhập TFS: phiên lưu ở partition persist:tfs; thử đăng nhập Windows (NTLM/Kerberos) trước, máy chủ hỏi tài khoản thì hiện
 * hộp nhập (không lưu mật khẩu, chỉ đưa cho Chromium trả lời lần hỏi đó).
 *
 * IPC (chỉ cửa sổ chính):
 *   tfs-merge-open {url, caseId}  → mở / đưa lên cửa sổ PR, bắt đầu theo dõi → { ok } | { error }
 *   sự kiện 'tfs' gửi trang: { type:'state', caseId, url, status } · { type:'merged', caseId, url, status, by, at, commit, mime, b64 }
 *                            · { type:'closed', caseId, url }
 */
const PARTITION = 'persist:tfs';
const PR_URL = /^https?:\/\/[^/\s]+\/tfs\/[^?#\s]*\/_git\/[^/?#\s]+\/pullrequest\/\d+/i;

module.exports = function setupTfs({ BrowserWindow, ipcMain, session, ICON, getWin, log }) {
  const wins = new Map();   // url → { win, caseId, timer, done }
  let ntlm = false;

  function send(p) {
    const w = getWin();
    if (w && !w.isDestroyed()) w.webContents.send('tfs', p);
  }
  function fromMain(e) {
    const w = getWin();
    return w && !w.isDestroyed() && e.sender === w.webContents;
  }

  /** https://host/tfs/AQ/Source.NET/_git/Source.NET/pullrequest/1004 → API GET (chỉ đọc) */
  function apiOf(url) {
    const m = String(url).match(/^(https?:\/\/[^/]+\/tfs\/[^/]+)\/([^/]+)\/_git\/([^/?#]+)\/pullrequest\/(\d+)/i);
    if (!m) return null;
    return `${m[1]}/${m[2]}/_apis/git/repositories/${m[3]}/pullRequests/${m[4]}?api-version=4.1`;
  }

  function authPrompt(parent, host) {
    return new Promise((resolve) => {
      const w = new BrowserWindow({
        parent, modal: true, width: 380, height: 250, resizable: false, minimizable: false, maximizable: false,
        title: 'Đăng nhập TFS', icon: ICON, autoHideMenuBar: true,
        webPreferences: { contextIsolation: true, nodeIntegration: false, sandbox: true },
      });
      let done = false;
      const finish = (v) => { if (!done) { done = true; resolve(v); if (!w.isDestroyed()) w.close(); } };
      w.on('closed', () => finish(null));
      // nhận kết quả qua đổi tiêu đề trang (không cần preload): "AQ-OK:<json>"
      w.webContents.on('page-title-updated', (_e, t) => {
        if (t.startsWith('AQ-OK:')) { try { finish(JSON.parse(t.slice(6))); } catch (x) { finish(null); } }
        else if (t === 'AQ-HUY') finish(null);
      });
      const esc = (s) => String(s).replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
      const html = `<!doctype html><meta charset="utf-8"><title>Đăng nhập TFS</title>
<style>body{font:14px system-ui,'Segoe UI',sans-serif;margin:16px;color:#1c2b3a}label{display:block;margin:8px 0 2px;font-size:12px;color:#506070}
input{width:100%;box-sizing:border-box;padding:7px 8px;border:1px solid #c5d0dc;border-radius:6px}.r{display:flex;gap:8px;justify-content:flex-end;margin-top:14px}
button{padding:7px 14px;border-radius:6px;border:1px solid #c5d0dc;background:#fff;cursor:pointer}.p{background:#2b5898;color:#fff;border-color:#2b5898}small{color:#708090}</style>
<div>TFS <b>${esc(host)}</b> cần đăng nhập</div><small>Tài khoản Windows / domain (vd AQ\\ten). App không lưu mật khẩu.</small>
<form id="f"><label>Tài khoản</label><input id="u" autofocus autocomplete="username"><label>Mật khẩu</label><input id="p" type="password" autocomplete="current-password">
<div class="r"><button type="button" id="h">Huỷ</button><button class="p">Đăng nhập</button></div></form>
<script>f.onsubmit=function(e){e.preventDefault();document.title='AQ-OK:'+JSON.stringify({u:u.value,p:p.value});};h.onclick=function(){document.title='AQ-HUY';};</script>`;
      w.loadURL('data:text/html;charset=utf-8,' + encodeURIComponent(html));
    });
  }

  async function poll(url) {
    const s = wins.get(url);
    if (!s || s.done || !s.win || s.win.isDestroyed()) return;
    const api = apiOf(url);
    let st = null;
    try {
      st = await s.win.webContents.executeJavaScript(`(async()=>{try{const r=await fetch(${JSON.stringify(api)},{credentials:'include',cache:'no-store',headers:{Accept:'application/json'}});
        if(!r.ok)return {http:r.status};const d=await r.json();return {status:d.status,by:d.closedBy&&d.closedBy.displayName,at:d.closedDate,
        commit:d.lastMergeCommit&&d.lastMergeCommit.commitId,title:d.title};}catch(e){
        const t=(document.body&&document.body.innerText)||'';return {dom:/\\bCompleted\\b|Đã hoàn thành/.test(t)?'completed':''};}})()`, true);
    } catch (x) { st = null; }
    if (!st) return;
    const status = st.status || st.dom || '';
    if (status && status !== s.last) { s.last = status; send({ type: 'state', caseId: s.caseId, url, status }); }
    if (/^completed$/i.test(status)) {
      s.done = true;
      clearInterval(s.timer);
      try { await s.win.webContents.reload(); } catch (x) { /* trang tự hiện Completed */ }
      await new Promise((r) => setTimeout(r, 3500));         // chờ trang vẽ lại trạng thái "Completed"
      if (s.win.isDestroyed()) return;
      let img = await s.win.webContents.capturePage();
      const { width } = img.getSize();
      if (width > 1600) img = img.resize({ width: 1600, quality: 'good' });
      send({ type: 'merged', caseId: s.caseId, url, status, by: st.by || '', at: st.at || '', commit: st.commit || '',
        mime: 'image/jpeg', b64: img.toJPEG(85).toString('base64') });
      log && log(`TFS: PR ${url} completed → đã chụp ảnh gửi trang (case ${s.caseId})`);
    } else if (/^abandoned$/i.test(status)) {
      s.done = true;
      clearInterval(s.timer);
    }
  }

  function open(url, caseId) {
    url = String(url || '').trim();
    if (!PR_URL.test(url)) return { error: 'Link merge không đúng dạng …/tfs/…/_git/…/pullrequest/<số>' };
    const cur = wins.get(url);
    if (cur && cur.win && !cur.win.isDestroyed()) { cur.caseId = caseId; cur.win.show(); cur.win.focus(); return { ok: true, again: true }; }
    const ses = session.fromPartition(PARTITION);
    if (!ntlm) { try { ses.allowNTLMCredentialsForDomains('*'); } catch (x) { /* Electron cũ */ } ntlm = true; }
    const main = getWin();
    const win = new BrowserWindow({
      width: 1280, height: 860, title: 'Merge PR – case ' + caseId, icon: ICON, autoHideMenuBar: true,
      webPreferences: { partition: PARTITION, contextIsolation: true, nodeIntegration: false, sandbox: true },
    });
    const s = { win, caseId, timer: null, done: false, last: '' };
    wins.set(url, s);
    win.webContents.setWindowOpenHandler(({ url: u }) => { win.loadURL(u).catch(() => {}); return { action: 'deny' }; });
    win.webContents.on('login', async (e, _d, info, cb) => {
      e.preventDefault();
      const r = await authPrompt(win, info.host);
      if (r && r.u) cb(r.u, r.p); else cb();
    });
    win.on('closed', () => {
      clearInterval(s.timer);
      wins.delete(url);
      if (!s.done) send({ type: 'closed', caseId: s.caseId, url });
    });
    win.loadURL(url).catch((x) => log && log('TFS: không mở được ' + url + ' – ' + x.message));
    s.timer = setInterval(() => poll(url), 3000);
    if (main && !main.isDestroyed()) { /* cửa sổ độc lập, không modal: người test thao tác TFS thoải mái */ }
    return { ok: true };
  }

  ipcMain.handle('tfs-merge-open', (e, a) => {
    if (!fromMain(e)) return null;
    a = a || {};
    try { return open(a.url, String(a.caseId || '')); } catch (x) { return { error: String((x && x.message) || x) }; }
  });

  return { open };
};
