'use strict';
// Cầu nối trang console (http://localhost:<cổng>) ↔ app: phiên bản, cập nhật, thoát.
const { contextBridge, ipcRenderer } = require('electron');

contextBridge.exposeInMainWorld('aqDesktop', {
  onUpdate: (cb) => ipcRenderer.on('update', (_e, u) => cb(u)),
  getUpdate: () => ipcRenderer.invoke('update-get'),
  updateAct: () => ipcRenderer.send('update-act'),
  quit: () => ipcRenderer.send('quit'),
});
