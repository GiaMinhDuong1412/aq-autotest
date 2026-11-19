'use strict';
/**
 * Cầu nối ACS cho MCP (Claude Desktop → aq_mcp.py → server.py → đây): server.py gọi POST http://127.0.0.1:<cổng>/acs
 * kèm X-AQ-Token để đọc ACS bằng phiên người dùng đã đăng nhập trong app (acs.js). CHỈ ĐỌC: GET /auth/me, GET /cs/…, POST /cs/query.
 * Cổng ngẫu nhiên, token ngẫu nhiên mỗi lần mở app – truyền cho server.py qua biến môi trường AQ_ACS_RELAY / AQ_ACS_TOKEN.
 */
const http = require('http');
const crypto = require('crypto');

const READ_PATH = /^\/(auth\/me|cs\/)[A-Za-z0-9_\-./?=&%,@:+~]*$/;

function allowed(method, p) {
  method = String(method || 'GET').toUpperCase();
  p = String(p || '');
  if (!READ_PATH.test(p) || p.includes('..')) return false;
  if (method === 'GET') return true;
  return method === 'POST' && p.split('?')[0] === '/cs/query';   // chạy Query = đọc
}

module.exports = function startRelay({ acs, log }) {
  const token = crypto.randomBytes(24).toString('base64url');
  const srv = http.createServer((req, res) => {
    const end = (code, obj) => { const b = Buffer.from(JSON.stringify(obj)); res.writeHead(code, { 'Content-Type': 'application/json', 'Content-Length': b.length }); res.end(b); };
    const tok = String(req.headers['x-aq-token'] || '');
    if (req.method !== 'POST' || req.url !== '/acs' || tok.length !== token.length || !crypto.timingSafeEqual(Buffer.from(tok), Buffer.from(token))) return end(403, { error: 'forbidden' });
    let raw = '';
    req.on('data', (c) => { raw += c; if (raw.length > 200000) req.destroy(); });
    req.on('end', async () => {
      let a;
      try { a = JSON.parse(raw || '{}'); } catch { return end(400, { error: 'JSON lỗi' }); }
      if (!allowed(a.method, a.path)) return end(403, { error: 'MCP chỉ được ĐỌC ACS (GET /cs/…, POST /cs/query) – không ghi lên ACS.' });
      try { end(200, await acs.call(a.method, a.path, a.body)); } catch (e) { end(200, { status: 0, error: String((e && e.message) || e) }); }
    });
  });
  return new Promise((resolve) => {
    srv.on('error', (e) => { log('Không mở được cầu nối ACS cho MCP:', e.message); resolve(null); });
    srv.listen(0, '127.0.0.1', () => resolve({ url: `http://127.0.0.1:${srv.address().port}`, token, close: () => srv.close() }));
  });
};
module.exports.allowed = allowed;
