'use strict';
/**
 * Kết nối AQ Support Hub (ACS – https://acs.aqtech.io.vn) theo "cách 2": người dùng đăng nhập ACS ngay trong
 * một cửa sổ của app (phiên lưu ở partition persist:acs, giống app AQ Case Widget), app gọi chính API mà giao diện
 * ACS đang dùng (/auth/me, /cs/lookups, /cs/query, /cs/cases/{id}/history…) TỪ BÊN TRONG trang ACS (cùng origin,
 * cookie của người dùng) – chỉ thấy/sửa được những gì tài khoản đó được phép. App không lưu mật khẩu.
 *
 * IPC cho trang console (chỉ cửa sổ chính được gọi):
 *   acs-status            → { ok, me:{name,username,id} } | { needLogin } | { error }
 *   acs-login             → mở cửa sổ đăng nhập, chờ tới khi đăng nhập xong hoặc đóng cửa sổ → như acs-status
 *   acs-logout            → xoá phiên
 *   acs-call {method,path,body} → { status, data }   (path phải bắt đầu bằng /auth/me hoặc /cs/)
 *   acs-open {caseId}     → mở case trong cửa sổ ACS của app
 *   acs-upload {name,b64,mime} → tải ảnh lên ACS (/cs/attachments) → { status, data:{id} } – ảnh cho Nội dung Tester test
 *   acs-survey-start / acs-survey-stop → ghi lại các lời gọi /cs/… khi người dùng tự thao tác trên ACS (khảo sát cách
 *     ACS lưu Query và nội dung test) → { calls:[{method,path,status,req,res}] }, đồng thời lưu rieng/acs-khao-sat.json.
 *     Không ghi cookie/header; trường có tên chứa "pass"/"token" bị che.
 */
const path = require('path');
const fs = require('fs');

const BASE = 'https://acs.aqtech.io.vn';
const LIGHT_URL = BASE + '/auth/providers';   // trang JSON nhẹ cùng origin để gọi API
const PARTITION = 'persist:acs';
const PATH_OK = /^\/(auth\/me|cs\/)[A-Za-z0-9_\-./?=&%,@:+~]*$/;
const METHODS = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE'];

module.exports = function setupAcs({ BrowserWindow, ipcMain, session, ICON, getWin, log, RIENG }) {
  let acsWin = null;
  let workerOk = false;
  let loginWait = null;      // { resolve, poll }
  let survey = null;         // { calls: [], pending: Map }
  let quitting = false;

  const fromMain = (e) => { const w = getWin(); return !!w && !w.isDestroyed() && e.sender === w.webContents; };
  const push = (p) => { const w = getWin(); if (w && !w.isDestroyed()) w.webContents.send('acs', p); };

  function ensureWin() {
    if (acsWin && !acsWin.isDestroyed()) return acsWin;
    acsWin = new BrowserWindow({
      width: 1100, height: 800, show: false, title: 'AQ Support Hub – đăng nhập', icon: ICON, autoHideMenuBar: true,
      webPreferences: { partition: PARTITION, contextIsolation: true, sandbox: true },
    });
    acsWin.webContents.setWindowOpenHandler(() => ({
      action: 'allow', overrideBrowserWindowOptions: { autoHideMenuBar: true, icon: ICON, webPreferences: { partition: PARTITION } },
    }));
    acsWin.on('close', (e) => {
      if (quitting) return;
      e.preventDefault();
      acsWin.hide();
      if (loginWait) endLogin();
      if (survey) push({ survey: 'hidden' });
    });
    acsWin.webContents.on('did-finish-load', () => { workerOk = true; });
    acsWin.webContents.on('did-fail-load', (_e, code, _d, _u, main) => { if (main && code !== -3) workerOk = false; });
    workerOk = false;
    return acsWin;
  }

  async function ensureWorker() {
    const w = ensureWin();
    const wc = w.webContents;
    if (loginWait || survey) return wc.getURL().startsWith(BASE);   // đang đăng nhập/khảo sát: dùng trang đang mở
    if (!workerOk || !wc.getURL().startsWith(BASE) || wc.isLoading()) {
      try { await w.loadURL(LIGHT_URL); } catch (e) {
        if (!String(e && e.message).includes('ERR_ABORTED')) throw new Error('Không kết nối được acs.aqtech.io.vn (kiểm tra mạng/VPN)');
      }
    }
    return wc.getURL().startsWith(BASE);
  }

  /** fetch cùng origin bên trong trang ACS */
  async function call(method, p, body) {
    method = String(method || 'GET').toUpperCase();
    if (!METHODS.includes(method)) throw new Error('Phương thức không hợp lệ');
    if (!PATH_OK.test(String(p || ''))) throw new Error('Đường dẫn ACS không được phép: ' + p);
    if (!(await ensureWorker())) throw new Error('Không mở được trang ACS');
    const code = `(async()=>{const init={method:${JSON.stringify(method)},credentials:'same-origin',cache:'no-store',headers:{}};
      ${body !== undefined ? `init.headers['Content-Type']='application/json';init.body=${JSON.stringify(JSON.stringify(body))};` : ''}
      const r=await fetch(${JSON.stringify(p)},init);let t='';try{t=await r.text();}catch(e){}
      let d=null;try{d=t?JSON.parse(t):null;}catch(e){d=t.slice(0,2000);}return {status:r.status,data:d};})()`;
    try {
      return await acsWin.webContents.executeJavaScript(code, true);
    } catch (e) {
      const m = String((e && e.message) || e);
      if (/Failed to fetch|NetworkError|ERR_/i.test(m)) { workerOk = false; throw new Error('Không kết nối được acs.aqtech.io.vn (kiểm tra mạng/VPN)'); }
      throw e;
    }
  }

  /** tải ảnh lên ACS (POST /cs/attachments?name=…, octet-stream – như trình soạn thảo của ACS) → { status, data:{id…} }.
   *  Dùng cho ảnh trong "Nội dung Tester test": nội dung chèn <img src="/cs/att/<id>">. Chỉ nhận ảnh, tối đa 8 MB. */
  async function upload(name, b64, mime) {
    if (!/^image\/(png|jpeg|webp|gif)$/.test(String(mime || ''))) throw new Error('Chỉ tải ảnh lên ACS');
    b64 = String(b64 || '');
    if (!b64 || b64.length > 11 * 1024 * 1024) throw new Error('Ảnh rỗng hoặc quá 8 MB');
    name = String(name || 'anh.jpg').replace(/[^\w.\-]+/g, '_').slice(0, 80);
    if (!(await ensureWorker())) throw new Error('Không mở được trang ACS');
    const code = `(async()=>{const s=atob(${JSON.stringify(b64)}),u=new Uint8Array(s.length);for(let i=0;i<s.length;i++)u[i]=s.charCodeAt(i);
      const r=await fetch('/cs/attachments?name='+encodeURIComponent(${JSON.stringify(name)}),{method:'POST',credentials:'same-origin',cache:'no-store',
        headers:{'Content-Type':'application/octet-stream'},body:u});let t='';try{t=await r.text();}catch(e){}
      let d=null;try{d=t?JSON.parse(t):null;}catch(e){d=t.slice(0,2000);}return {status:r.status,data:d};})()`;
    return acsWin.webContents.executeJavaScript(code, true);
  }

  // ---------- ảnh trong case (KH / BA / Dev chụp) – chỉ GET cùng origin, chỉ nhận image/* ----------
  const IMG_PATH = /^\/[A-Za-z0-9_\-./?=&%,@:+~]*$/;
  /** buffer ảnh → JPEG/PNG thu nhỏ (cạnh dài ≤ max) để gửi cho Claude / hiện trên trang */
  function shrink(buf, mime, max) {
    max = max || 1568;
    try {
      const { nativeImage } = require('electron');
      let im = nativeImage.createFromBuffer(buf);
      if (im.isEmpty()) return { mime, b64: buf.toString('base64') };
      const { width: w, height: h } = im.getSize();
      if (Math.max(w, h) > max) im = w >= h ? im.resize({ width: max, quality: 'good' }) : im.resize({ height: max, quality: 'good' });
      const s = im.getSize();
      if (buf.length < 700000 && Math.max(w, h) <= max && /png|jpe?g/.test(mime)) return { mime, b64: buf.toString('base64'), w: s.width, h: s.height };
      return { mime: 'image/jpeg', b64: im.toJPEG(82).toString('base64'), w: s.width, h: s.height };
    } catch { return { mime, b64: buf.toString('base64') }; }
  }
  async function image(p, max) {
    p = String(p || '');
    if (p.startsWith(BASE)) p = p.slice(BASE.length);
    if (!IMG_PATH.test(p) || p.includes('..')) throw new Error('Ảnh không thuộc ACS: ' + p.slice(0, 120));
    if (!(await ensureWorker())) throw new Error('Không mở được trang ACS');
    const code = `(async()=>{const r=await fetch(${JSON.stringify(p)},{credentials:'same-origin',cache:'no-store'});
      const ct=(r.headers.get('content-type')||'').split(';')[0].trim();
      if(r.status!==200||!/^image\\//i.test(ct))return {status:r.status,mime:ct};
      const b=new Uint8Array(await r.arrayBuffer());if(b.length>15e6)return {status:413,mime:ct};
      let s='';for(let i=0;i<b.length;i+=32768)s+=String.fromCharCode.apply(null,b.subarray(i,i+32768));
      return {status:200,mime:ct,b64:btoa(s)};})()`;
    const r = await acsWin.webContents.executeJavaScript(code, true);
    if (r.status !== 200 || !r.b64) return { status: r.status, mime: r.mime, error: r.status === 200 ? 'Không phải ảnh' : 'ACS trả mã ' + r.status };
    return Object.assign({ status: 200 }, shrink(Buffer.from(r.b64, 'base64'), r.mime, max));
  }

  async function status() {
    try {
      const r = await call('GET', '/auth/me');
      if (r.status === 401 || r.status === 403) return { needLogin: true };
      if (r.status !== 200 || !r.data) return { error: 'ACS trả về mã ' + r.status };
      return { ok: true, me: { name: r.data.display_name || r.data.username || '', username: r.data.username || '', id: r.data.id != null ? String(r.data.id) : (r.data.user_id != null ? String(r.data.user_id) : '') } };
    } catch (e) { return { error: String((e && e.message) || e) }; }
  }

  function endLogin(res) {
    if (!loginWait) return;
    clearInterval(loginWait.poll);
    const w = loginWait; loginWait = null; workerOk = false;
    status().then((s) => { push({ status: s }); w.resolve(res || s); });
  }

  async function login() {
    if (loginWait) return new Promise((r) => { const old = loginWait.resolve; loginWait.resolve = (x) => { old(x); r(x); }; });
    const w = ensureWin();
    return new Promise((resolve) => {
      loginWait = { resolve, poll: null };
      w.show(); w.focus();
      w.loadURL(BASE + '/').catch(() => { /* chuyển hướng tới trang đăng nhập */ });
      loginWait.poll = setInterval(async () => {
        try {
          const wc = w.webContents;
          if (!wc.getURL().startsWith(BASE) || wc.isLoading()) return;
          const ok = await wc.executeJavaScript("fetch('/auth/me',{cache:'no-store'}).then(r=>r.ok)", true);
          if (ok) { if (w.isVisible() && !survey) w.hide(); endLogin(); }
        } catch { /* đang chuyển trang */ }
      }, 2000);
    });
  }

  async function logout() {
    try { await session.fromPartition(PARTITION).clearStorageData(); } catch { /* bỏ qua */ }
    workerOk = false;
    const s = { needLogin: true };
    push({ status: s });
    return s;
  }

  // ---------- khảo sát: ghi lại lời gọi /cs/… khi người dùng tự thao tác ----------
  const mask = (s) => String(s || '').replace(/("[^"]*(pass|token|secret)[^"]*"\s*:\s*)"[^"]*"/gi, '$1"***"').slice(0, 6000);
  async function surveyStart() {
    const w = ensureWin();
    const dbg = w.webContents.debugger;
    try { if (!dbg.isAttached()) dbg.attach('1.3'); } catch (e) { throw new Error('Không bật được khảo sát: ' + e.message); }
    survey = { calls: [], pending: new Map() };
    dbg.removeAllListeners('message');
    dbg.on('message', async (_ev, method, p) => {
      if (!survey) return;
      try {
        if (method === 'Network.requestWillBeSent') {
          const u = new URL(p.request.url);
          if (u.origin !== BASE || !/^\/(cs|auth\/me)/.test(u.pathname)) return;
          survey.pending.set(p.requestId, { at: new Date().toISOString(), method: p.request.method, path: u.pathname + u.search, req: mask(p.request.postData || '') });
        } else if (method === 'Network.responseReceived') {
          const c = survey.pending.get(p.requestId);
          if (c) c.status = p.response.status;
        } else if (method === 'Network.loadingFinished') {
          const c = survey.pending.get(p.requestId);
          if (!c) return;
          survey.pending.delete(p.requestId);
          try { const b = await dbg.sendCommand('Network.getResponseBody', { requestId: p.requestId }); c.res = mask(b.base64Encoded ? '' : b.body); } catch { c.res = ''; }
          survey.calls.push(c);
          if (survey.calls.length > 400) survey.calls.shift();
          push({ survey: 'call', n: survey.calls.length, last: c.method + ' ' + c.path });
        }
      } catch { /* bỏ qua */ }
    });
    await dbg.sendCommand('Network.enable');
    w.show(); w.focus();
    if (!w.webContents.getURL().startsWith(BASE) || w.webContents.getURL().startsWith(LIGHT_URL)) w.loadURL(BASE + '/').catch(() => {});
    return { ok: true };
  }
  function surveyStop() {
    const calls = survey ? survey.calls.slice() : [];
    survey = null;
    try { const dbg = acsWin && acsWin.webContents.debugger; if (dbg && dbg.isAttached()) dbg.detach(); } catch { /* bỏ qua */ }
    try { fs.mkdirSync(RIENG, { recursive: true }); fs.writeFileSync(path.join(RIENG, 'acs-khao-sat.json'), JSON.stringify({ at: new Date().toISOString(), calls }, null, 1)); } catch (e) { log('Không lưu được khảo sát ACS:', e.message); }
    if (acsWin && !acsWin.isDestroyed()) acsWin.hide();
    workerOk = false;
    return { calls };
  }

  ipcMain.handle('acs-status', (e) => (fromMain(e) ? status() : null));
  ipcMain.handle('acs-login', (e) => (fromMain(e) ? login() : null));
  ipcMain.handle('acs-logout', (e) => (fromMain(e) ? logout() : null));
  ipcMain.handle('acs-call', async (e, a) => {
    if (!fromMain(e)) return null;
    a = a || {};
    try { return await call(a.method, a.path, a.body); } catch (x) { return { status: 0, error: String((x && x.message) || x) }; }
  });
  ipcMain.handle('acs-image', async (e, a) => {
    if (!fromMain(e)) return null;
    a = a || {};
    try { return await image(a.path, a.max); } catch (x) { return { status: 0, error: String((x && x.message) || x) }; }
  });
  ipcMain.handle('acs-upload', async (e, a) => {
    if (!fromMain(e)) return null;
    a = a || {};
    try { return await upload(a.name, a.b64, a.mime); } catch (x) { return { status: 0, error: String((x && x.message) || x) }; }
  });
  ipcMain.handle('acs-open', (e, a) => {
    if (!fromMain(e)) return false;
    const id = String((a && a.caseId) || '');
    const w = ensureWin();
    w.show(); w.focus();
    w.loadURL(/^\d+$/.test(id) ? `${BASE}/cs-case/${id}` : BASE + '/').catch(() => {});
    workerOk = false;
    return true;
  });
  ipcMain.handle('acs-survey-start', async (e) => {
    if (!fromMain(e)) return null;
    try { return await surveyStart(); } catch (x) { return { error: String((x && x.message) || x) }; }
  });
  ipcMain.handle('acs-survey-stop', (e) => (fromMain(e) ? surveyStop() : null));

  return {
    call,                                         // cầu nối MCP (mcp-relay.js) – chỉ đọc, lọc ở đó
    image,                                        // ảnh trong case (chỉ GET, chỉ image/*)
    shrink,
    status,
    shutdown() { quitting = true; try { if (acsWin && !acsWin.isDestroyed()) acsWin.destroy(); } catch { /* bỏ qua */ } },
  };
};
