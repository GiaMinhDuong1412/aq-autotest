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
});
