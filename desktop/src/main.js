'use strict';
/**
 * AQ Auto Test – app Windows (Electron) của console kịch bản test Edusoft/Netweb.
 * App chạy server.py (Python nhúng ở resources/python, mã ở resources/app) trên 127.0.0.1 rồi mở console trong cửa sổ riêng.
 * Dữ liệu của máy ở %APPDATA%\AQ Auto Test: du-lieu\ (kịch bản, lượt chạy…), rieng\ (cấu hình, tài khoản), nhat-ky.txt.
 * Đóng cửa sổ = thoát app (server tắt theo). Cập nhật: updater.js (repo public aq-autotest-releases, không cần token).
 *
 * Chạy thử từ mã nguồn (không đóng gói): cd desktop && npm install && npm start  – dùng server.py ở thư mục repo và python3/python.
 * Kiểm tra nhanh bản build: "AQ Auto Test.exe" --smoke  (mở server + trang đăng nhập rồi thoát, mã 0 = đạt).
 */
const { app, BrowserWindow, ipcMain, shell, Notification, Menu, dialog, session } = require('electron');
const path = require('path');
const fs = require('fs');
const os = require('os');
const http = require('http');
const net = require('net');
const { spawn, execFileSync } = require('child_process');
const { createUpdater } = require('./updater');

const APP_ID = 'vn.aqtech.autotest';
const APP_NAME = 'AQ Auto Test';
const SMOKE = process.argv.includes('--smoke');
if (SMOKE) app.setPath('userData', fs.mkdtempSync(path.join(os.tmpdir(), 'aq-autotest-smoke-')));

const RES = process.resourcesPath;
const CODE = app.isPackaged ? path.join(RES, 'app') : path.resolve(__dirname, '..', '..');
const PYTHON = app.isPackaged && process.platform === 'win32' ? path.join(RES, 'python', 'pythonw.exe')
  : (process.env.AQ_PYTHON || (process.platform === 'win32' ? 'python' : 'python3'));
const ICON = path.join(__dirname, '..', 'build', 'icon.ico');
const HOME = app.getPath('userData');
const DATA = path.join(HOME, 'du-lieu');
const RIENG = path.join(HOME, 'rieng');
const LOG = path.join(HOME, 'nhat-ky.txt');
const CFG_FILE = path.join(HOME, 'app.json');
const UPDATE_CHECK_MS = 4 * 60 * 60 * 1000;

let cfg = { port: 8788, bounds: null, maximized: false };
let win = null;
let server = null;
let port = 0;
let quitting = false;
let updater = null;
let splash = null;
let launch = { version: '', prev: null, fresh: false };

function log(...a) {
  try { fs.appendFileSync(LOG, new Date().toISOString().replace('T', ' ').slice(0, 19) + ' ' + a.join(' ') + '\n'); } catch { /* bỏ qua */ }
}
function loadCfg() { try { cfg = { ...cfg, ...JSON.parse(fs.readFileSync(CFG_FILE, 'utf8')) }; } catch { /* lần đầu */ } }
function saveCfg() { try { fs.writeFileSync(CFG_FILE, JSON.stringify(cfg, null, 1)); } catch { /* bỏ qua */ } }

// ---------------- dữ liệu ----------------
/** Lần đầu: chuyển dữ liệu từ bản app đời đầu (cài bằng Inno Setup ở %LOCALAPPDATA%\Programs\AQ-AutoTest). */
function chuyenDuLieuCu() {
  if (fs.existsSync(DATA) || !process.env.LOCALAPPDATA) return;
  const old = path.join(process.env.LOCALAPPDATA, 'Programs', 'AQ-AutoTest');
  try {
    if (fs.existsSync(path.join(old, 'du-lieu'))) {
      fs.cpSync(path.join(old, 'du-lieu'), DATA, { recursive: true });
      log('Đã chuyển dữ liệu từ', old);
    }
    if (fs.existsSync(path.join(old, 'rieng', 'config.json'))) {   // cổng, thư mục bộ test, người dùng (không lấy token cũ)
      fs.mkdirSync(RIENG, { recursive: true });
      fs.copyFileSync(path.join(old, 'rieng', 'config.json'), path.join(RIENG, 'config.json'));
    }
  } catch (e) { log('Không chuyển được dữ liệu cũ:', e.message); }
}

/** Sau khi đổi phiên bản: đưa dữ liệu mẫu (kịch bản, kế hoạch…) của bản mới vào du-lieu/ – chưa có thì chép, có rồi chỉ thay khi updatedAt mới hơn. */
function gopDuLieuMau() {
  const seed = path.join(CODE, 'data');
  const mark = path.join(DATA, '.phien-ban-du-lieu');
  const ver = app.getVersion();
  try { if (fs.readFileSync(mark, 'utf8').trim() === ver) return; } catch { /* chưa có */ }
  let n = 0;
  const walk = (dir) => {
    for (const e of fs.readdirSync(dir, { withFileTypes: true })) {
      const f = path.join(dir, e.name);
      if (e.isDirectory()) { walk(f); continue; }
      const d = path.join(DATA, path.relative(seed, f));
      if (fs.existsSync(d)) {
        if (!f.endsWith('.json')) continue;
        try {
          const a = String(JSON.parse(fs.readFileSync(f, 'utf8')).updatedAt || '');
          const b = String(JSON.parse(fs.readFileSync(d, 'utf8')).updatedAt || '');
          if (a <= b) continue;
        } catch { continue; }
      }
      fs.mkdirSync(path.dirname(d), { recursive: true });
      fs.copyFileSync(f, d);
      n++;
    }
  };
  try {
    if (fs.existsSync(seed)) walk(seed);
    fs.mkdirSync(DATA, { recursive: true });
    fs.writeFileSync(mark, ver);
    log('Gộp dữ liệu mẫu bản', ver, ':', n, 'file');
  } catch (e) { log('Lỗi gộp dữ liệu mẫu:', e.message); }
}

// ---------------- server Python ----------------
function portFree(p) {
  return new Promise((res) => {
    const s = net.createServer();
    s.once('error', () => res(false));
    s.once('listening', () => s.close(() => res(true)));
    s.listen(p, '127.0.0.1');
  });
}

async function choosePort() {
  const base = Number(cfg.port) || 8788;
  for (let p = base; p < base + 20; p++) if (await portFree(p)) return p;
  throw new Error('Không có cổng trống từ ' + base + ' tới ' + (base + 19));
}

function startServer() {
  const out = fs.openSync(LOG, 'a');
  const env = { ...process.env, AQ_APP_HOME: HOME, AQ_APP_VERSION: app.getVersion(), PYTHONIOENCODING: 'utf-8', PYTHONUTF8: '1' };
  const args = [path.join(CODE, 'server.py'), '--port', String(port), '--data', DATA, '--local', RIENG, '--no-browser'];
  log('Chạy server', PYTHON, 'cổng', port, 'bản', app.getVersion());
  server = spawn(PYTHON, args, { cwd: CODE, env, windowsHide: true, stdio: ['ignore', out, out] });
  server.on('exit', (code) => {
    log('Server dừng, mã', code);
    server = null;
    if (!quitting) {
      quitting = true;
      if (!SMOKE) dialog.showErrorBox(APP_NAME, 'Server của AQ Auto Test dừng bất ngờ (mã ' + code + ').\nXem nhật ký: ' + LOG);
      app.exit(1);
    }
  });
  server.on('error', (e) => log('Không chạy được Python:', e.message));
}

function stopServer() {
  if (!server) return;
  const pid = server.pid;
  server.removeAllListeners('exit');
  try {
    if (process.platform === 'win32') execFileSync('taskkill', ['/pid', String(pid), '/t', '/f'], { windowsHide: true, stdio: 'ignore' });
    else server.kill();
  } catch { /* đã tắt */ }
  server = null;
}

function waitServer(ms) {
  const end = Date.now() + ms;
  return new Promise((res, rej) => {
    const tick = () => {
      if (!server) return rej(new Error('Server không khởi động được – xem ' + LOG));
      const r = http.get({ host: '127.0.0.1', port, path: '/login', timeout: 2000 }, (x) => { x.resume(); res(); });
      r.on('error', () => (Date.now() > end ? rej(new Error('Server không trả lời sau ' + ms / 1000 + ' giây')) : setTimeout(tick, 300)));
      r.on('timeout', () => r.destroy());
    };
    tick();
  });
}

// ---------------- màn hình chờ khi mở app ----------------
const SPLASH_HTML = (ver, note) => `<!doctype html><html lang="vi"><head><meta charset="utf-8"><style>
html,body{margin:0;height:100%;background:#0b1324;color:#e2e8f0;font:14px "Segoe UI",system-ui,sans-serif;-webkit-user-select:none;user-select:none}
body{display:flex;flex-direction:column;align-items:center;justify-content:center;gap:14px;border:1px solid #1c2944;box-sizing:border-box;-webkit-app-region:drag}
.m{display:grid;place-items:center;width:64px;height:64px;border-radius:18px;background:linear-gradient(145deg,#3b82f6,#1d4ed8);font-weight:800;font-size:22px;color:#fff;box-shadow:0 12px 30px rgba(37,99,235,.45)}
h1{margin:0;font-size:19px;font-weight:700}.v{color:#8391ab;font-size:12px}.n{color:#93c5fd;font-size:12px;min-height:16px}
.bar{width:220px;height:4px;border-radius:4px;background:#1c2944;overflow:hidden}.bar i{display:block;width:40%;height:100%;border-radius:4px;background:#60a5fa;animation:go 1.1s ease-in-out infinite}
@keyframes go{0%{transform:translateX(-100%)}100%{transform:translateX(250%)}}#s{color:#c9d3e6;font-size:12.5px}
</style></head><body><div class="m">AQ</div><h1>AQ Auto Test</h1><div class="v">Phiên bản ${ver}</div><div class="n">${note}</div>
<div class="bar"><i></i></div><div id="s">Đang khởi động…</div></body></html>`;

function showSplash() {
  if (SMOKE) return;
  const note = launch.prev && launch.prev !== launch.version ? `Vừa cập nhật từ bản ${launch.prev}` : (launch.fresh ? 'Chào mừng bạn đến với AQ Auto Test' : '');
  splash = new BrowserWindow({ width: 420, height: 270, frame: false, resizable: false, maximizable: false, center: true, show: false,
    icon: ICON, title: APP_NAME, backgroundColor: '#0b1324', webPreferences: { contextIsolation: true, nodeIntegration: false } });
  splash.once('ready-to-show', () => splash && splash.show());
  splash.on('closed', () => { splash = null; });
  splash.loadURL('data:text/html;charset=utf-8,' + encodeURIComponent(SPLASH_HTML(launch.version, note)));
}
function splashText(t) { if (splash && !splash.isDestroyed()) splash.webContents.executeJavaScript(`document.getElementById('s').textContent=${JSON.stringify(t)}`).catch(() => {}); }
function closeSplash() { if (splash && !splash.isDestroyed()) splash.close(); splash = null; }

// ---------------- cửa sổ ----------------
const isLocal = (u) => { try { const x = new URL(u); return (x.hostname === 'localhost' || x.hostname === '127.0.0.1') && Number(x.port) === port; } catch { return false; } };
const send = (ch, p) => { if (win && !win.isDestroyed()) win.webContents.send(ch, p); };

function uniquePath(dir, name) {
  const ext = path.extname(name);
  const base = name.slice(0, name.length - ext.length);
  let f = path.join(dir, name);
  for (let i = 1; fs.existsSync(f); i++) f = path.join(dir, `${base} (${i})${ext}`);
  return f;
}

function createWindow() {
  const b = cfg.bounds || {};
  win = new BrowserWindow({
    width: b.width || 1440, height: b.height || 900, x: b.x, y: b.y, minWidth: 900, minHeight: 600,
    title: APP_NAME, icon: ICON, show: false, autoHideMenuBar: true, backgroundColor: '#0a0e16',
    webPreferences: { preload: path.join(__dirname, 'preload.js'), contextIsolation: true, nodeIntegration: false, spellcheck: false },
  });
  if (cfg.maximized) win.maximize();
  win.on('page-title-updated', (e) => e.preventDefault());   // tiêu đề cửa sổ luôn là "AQ Auto Test"
  win.once('ready-to-show', () => { if (!SMOKE) { win.show(); closeSplash(); } });
  const keep = () => { if (!win.isMaximized() && !win.isMinimized()) cfg.bounds = win.getBounds(); cfg.maximized = win.isMaximized(); };
  win.on('resize', keep);
  win.on('move', keep);
  win.on('close', () => { keep(); saveCfg(); });
  win.on('closed', () => { win = null; app.quit(); });

  // liên kết ra ngoài (tài liệu SharePoint, GitHub…) mở bằng trình duyệt; trang của console mở trong app
  win.webContents.setWindowOpenHandler(({ url }) => {
    if (isLocal(url)) return { action: 'allow', overrideBrowserWindowOptions: { icon: ICON, autoHideMenuBar: true } };
    if (/^https?:/i.test(url)) shell.openExternal(url);
    return { action: 'deny' };
  });
  win.webContents.on('will-navigate', (e, url) => { if (!isLocal(url)) { e.preventDefault(); if (/^https?:/i.test(url)) shell.openExternal(url); } });
  win.webContents.on('before-input-event', (e, i) => {
    if (i.type !== 'keyDown') return;
    const k = i.key.toLowerCase();
    if (k === 'f5' || (i.control && k === 'r')) { win.webContents.reload(); e.preventDefault(); }
    else if (k === 'f12' || (i.control && i.shift && k === 'i')) { win.webContents.toggleDevTools(); e.preventDefault(); }
    else if (i.control && (k === '=' || k === '+')) { win.webContents.setZoomLevel(win.webContents.getZoomLevel() + 0.5); e.preventDefault(); }
    else if (i.control && k === '-') { win.webContents.setZoomLevel(win.webContents.getZoomLevel() - 0.5); e.preventDefault(); }
    else if (i.control && k === '0') { win.webContents.setZoomLevel(0); e.preventDefault(); }
  });
  win.loadURL(`http://localhost:${port}/`);
}

function setupDownloads() {
  // file console tải về (file lệnh cho Agent, kết quả, xuất Excel…) lưu thẳng vào thư mục Tải về như trình duyệt
  session.defaultSession.on('will-download', (_e, item) => {
    const f = uniquePath(app.getPath('downloads'), item.getFilename());
    item.setSavePath(f);
    item.once('done', (_e2, st) => log('Tải về', st, f));
  });
}

function notify(title, body) {
  try {
    if (!Notification.isSupported()) return;
    const n = new Notification({ title, body, icon: ICON });
    n.on('click', () => { if (win) { if (win.isMinimized()) win.restore(); win.show(); win.focus(); } });
    n.show();
  } catch { /* bỏ qua */ }
}

// ---------------- khởi động ----------------
if (!app.requestSingleInstanceLock()) {
  app.quit();
} else {
  app.on('second-instance', () => { if (win) { if (win.isMinimized()) win.restore(); win.show(); win.focus(); } });
  app.whenReady().then(init);
}
app.on('before-quit', () => { quitting = true; });
app.on('will-quit', () => stopServer());
app.on('window-all-closed', () => app.quit());

async function init() {
  app.setAppUserModelId(APP_ID);
  Menu.setApplicationMenu(null);
  fs.mkdirSync(HOME, { recursive: true });
  try { if (fs.statSync(LOG).size > 4 * 1024 * 1024) fs.writeFileSync(LOG, ''); } catch { /* chưa có */ }
  loadCfg();
  launch = { version: app.getVersion(), prev: cfg.lastVersion || null, fresh: !fs.existsSync(DATA) };
  if (!SMOKE) { cfg.lastVersion = launch.version; saveCfg(); }
  showSplash();
  chuyenDuLieuCu();
  gopDuLieuMau();
  fs.mkdirSync(RIENG, { recursive: true });
  try {
    port = await choosePort();
    splashText('Đang chạy máy chủ nội bộ…');
    startServer();
    await waitServer(60000);
    splashText('Đang mở giao diện…');
  } catch (e) {
    log('Lỗi khởi động:', e.message);
    closeSplash();
    if (SMOKE) { console.error('SMOKE FAIL', e.message); app.exit(1); return; }
    dialog.showErrorBox(APP_NAME, 'Không khởi động được AQ Auto Test.\n' + e.message + '\n\nNhật ký: ' + LOG);
    app.exit(1);
    return;
  }
  setupDownloads();
  ipcMain.handle('update-get', () => (updater ? updater.getState() : null));
  ipcMain.on('update-act', () => { if (updater) updater.act(); });
  ipcMain.on('quit', () => app.quit());
  ipcMain.handle('app-info', () => launch);
  ipcMain.handle('pick-file', async (_e, o) => {
    const r = await dialog.showOpenDialog(win, { title: o.title || 'Chọn file', defaultPath: o.defaultPath || undefined,
      filters: Array.isArray(o.filters) ? o.filters : undefined, properties: [o.dir ? 'openDirectory' : 'openFile'] });
    return r.canceled || !r.filePaths.length ? '' : r.filePaths[0];
  });
  createWindow();
  if (SMOKE) return smoke();
  updater = createUpdater({ send, notify, beforeInstall: () => { quitting = true; stopServer(); } });
  setTimeout(() => updater.check(false), 8 * 1000);
  setInterval(() => updater.check(false), UPDATE_CHECK_MS);
}

/** --smoke: trang đăng nhập mở được, đăng nhập admin/1234 thì console nạp được và có window.AQ_APP. */
function smoke() {
  const fail = (m) => { console.error('SMOKE FAIL', m); log('SMOKE FAIL', m); quitting = true; app.exit(1); };
  const timer = setTimeout(() => fail('quá 90 giây'), 90000);
  const wc = win.webContents;
  let step = 0;
  wc.on('did-fail-load', (_e, code, desc) => fail('không nạp được trang: ' + code + ' ' + desc));
  wc.on('did-finish-load', async () => {
    try {
      const url = wc.getURL();
      if (step === 0) {
        if (!/\/login$/.test(url)) return fail('chưa đăng nhập mà không về trang login: ' + url);
        step = 1;
        const ok = await wc.executeJavaScript(`fetch('login',{method:'POST',headers:{'Content-Type':'application/json','X-AQ':'1'},body:JSON.stringify({login:'admin',password:'1234'})}).then(r=>r.ok)`);
        if (!ok) return fail('đăng nhập admin/1234 không được');
        wc.loadURL(`http://localhost:${port}/`);
      } else if (step === 1) {
        step = 2;
        const r = await wc.executeJavaScript(`({app: !!window.AQ_APP && window.AQ_APP.version, auth: !!window.AQ_AUTH, desk: !!window.aqDesktop, nav: document.querySelectorAll('.nav-item').length})`);
        if (!r.app || !r.auth || !r.desk || !r.nav) return fail('console thiếu thành phần: ' + JSON.stringify(r));
        clearTimeout(timer);
        console.log('SMOKE OK', JSON.stringify(r));
        log('SMOKE OK', JSON.stringify(r));
        quitting = true;
        stopServer();
        app.exit(0);
      }
    } catch (e) { fail(e.message); }
  });
}
