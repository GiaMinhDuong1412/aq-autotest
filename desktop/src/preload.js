'use strict';
// Cầu nối trang console (http://localhost:<cổng>) ↔ app: phiên bản, cập nhật, thoát.
const { contextBridge, ipcRenderer } = require('electron');

contextBridge.exposeInMainWorld('aqDesktop', {
  onUpdate: (cb) => ipcRenderer.on('update', (_e, u) => cb(u)),
  getUpdate: () => ipcRenderer.invoke('update-get'),
  updateAct: () => ipcRenderer.send('update-act'),
  quit: () => ipcRenderer.send('quit'),
  getInfo: () => ipcRenderer.invoke('app-info'),               // { version, prev, fresh } – popup "Có gì mới" / hướng dẫn lần đầu
  pickFile: (o) => ipcRenderer.invoke('pick-file', o || {}),     // hộp chọn file của Windows → đường dẫn ('' = huỷ)
  acs: {                                                          // AQ Support Hub – đăng nhập trong app, gọi API cùng phiên (acs.js)
    status: () => ipcRenderer.invoke('acs-status'),
    login: () => ipcRenderer.invoke('acs-login'),
    logout: () => ipcRenderer.invoke('acs-logout'),
    call: (method, path, body) => ipcRenderer.invoke('acs-call', { method, path, body }),
    image: (path, max) => ipcRenderer.invoke('acs-image', { path, max }),      // ảnh trong case → {status, mime, b64}
    upload: (name, b64, mime) => ipcRenderer.invoke('acs-upload', { name, b64, mime }),   // ảnh → /cs/attachments → {status, data:{id}}
    open: (caseId) => ipcRenderer.invoke('acs-open', { caseId }),
    surveyStart: () => ipcRenderer.invoke('acs-survey-start'),
    surveyStop: () => ipcRenderer.invoke('acs-survey-stop'),
    onEvent: (cb) => ipcRenderer.on('acs', (_e, p) => cb(p)),
  },
});
