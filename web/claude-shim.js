/* AQ Autotest – thay window.claude (của claude.ai) khi chạy console trên localhost.
 * Cung cấp đúng phần console dùng: db, user, assets, downloads, permissions, mcp (host:aq-autotest).
 * Dữ liệu đi qua server.py (lưu file JSON trong data/). Thay đổi từ máy khác (git pull) được
 * nhận nhờ thăm dò /api/rev mỗi 2 giây. */
(function () {
  'use strict';
  var LOCAL = window.AQ_LOCAL || {};
  var H = { 'Content-Type': 'application/json', 'X-AQ': '1' };
  function err(code, message) { var e = new Error(message || code); e.code = code; e.message = message || code; return e; }
  async function api(method, url, body, headers) {
    var r = await fetch(url, { method: method, headers: headers || H, body: body === undefined ? undefined : (body instanceof Blob ? body : JSON.stringify(body)) });
    var j = null; try { j = await r.json(); } catch (e) { j = null; }
    if (!r.ok) throw err(r.status === 404 ? 'not_found' : r.status === 422 ? 'tool_error' : 'bad_request', (j && j.error) || ('HTTP ' + r.status));
    return j;
  }
  function q(o) { return Object.keys(o).map(function (k) { return k + '=' + encodeURIComponent(o[k]); }).join('&'); }
  function clone(v) { return v == null ? v : JSON.parse(JSON.stringify(v)); }

  /* ---------------- db ---------------- */
  var listeners = [];
  var rev = null;
  function refreshAll() { listeners.slice().forEach(function (l) { l.run(); }); }
  async function poll() {
    try { var r = await api('GET', '/api/rev'); if (rev !== null && r.rev !== rev) refreshAll(); rev = r.rev; } catch (e) { }
    setTimeout(poll, 2000);
  }
  setTimeout(poll, 2000);
  function bump() { setTimeout(refreshAll, 30); }

  function docSnap(id, exists, data) { return { id: id, exists: exists, data: function () { return clone(data); } }; }
  function Ref(path, id) { this.path = path; this.id = id; }
  Ref.prototype.get = async function () { var r = await api('GET', '/api/doc?' + q({ path: this.path, id: this.id })); return docSnap(this.id, r.exists, r.data); };
  Ref.prototype.set = async function (data) { await api('PUT', '/api/doc?' + q({ path: this.path, id: this.id }), data); bump(); };
  Ref.prototype.update = async function (data) { await api('PATCH', '/api/doc?' + q({ path: this.path, id: this.id }), data); bump(); };
  Ref.prototype['delete'] = async function () { await api('DELETE', '/api/doc?' + q({ path: this.path, id: this.id })); bump(); };
  Ref.prototype.onSnapshot = function (next, error) {
    var self = this, alive = true, last = null;
    var l = { run: function () { if (!alive) return; self.get().then(function (s) { var sig = JSON.stringify([s.exists, s.data()]); if (sig === last) return; last = sig; next(s); }, function (e) { if (error) error(e); }); } };
    listeners.push(l); l.run();
    return function () { alive = false; listeners = listeners.filter(function (x) { return x !== l; }); };
  };

  function Query(path, opts) { this.path = path; this.o = opts || {}; }
  Query.prototype._with = function (k, v) { var o = Object.assign({}, this.o); o[k] = v; return new Query(this.path, o); };
  Query.prototype.doc = function (id) { return new Ref(this.path, id || (Date.now().toString(36) + Math.random().toString(36).slice(2, 12))); };
  Query.prototype.orderBy = function (f, dir) { return this._with('order', [f, dir || 'asc']); };
  Query.prototype.limit = function (n) { return this._with('limit', n); };
  Query.prototype.where = function (f, op, v) { var w = (this.o.where || []).concat([[f, op, v]]); return this._with('where', w); };
  Query.prototype.add = async function (data) { var r = await api('POST', '/api/db?' + q({ path: this.path }), data); bump(); return new Ref(this.path, r.id); };
  function test(d, w) {
    var a = d[w[0]], op = w[1], b = w[2];
    switch (op) {
      case '==': return a === b; case '!=': return a !== b; case '<': return a < b; case '<=': return a <= b;
      case '>': return a > b; case '>=': return a >= b; case 'in': return (b || []).indexOf(a) >= 0;
      case 'array-contains': return Array.isArray(a) && a.indexOf(b) >= 0; default: return true;
    }
  }
  Query.prototype.get = async function () {
    var r = await api('GET', '/api/db?' + q({ path: this.path })), docs = r.docs || [], o = this.o;
    (o.where || []).forEach(function (w) { docs = docs.filter(function (d) { return test(d.data, w); }); });
    if (o.order) { var f = o.order[0], s = o.order[1] === 'desc' ? -1 : 1; docs.sort(function (x, y) { var a = x.data[f], b = y.data[f]; return a === b ? 0 : (a === undefined || a === null) ? 1 : (b === undefined || b === null) ? -1 : (a < b ? -s : s); }); }
    if (o.limit) docs = docs.slice(0, o.limit);
    var list = docs.map(function (d) { return docSnap(d.id, true, d.data); });
    return { docs: list, size: list.length, empty: !list.length, forEach: function (fn) { list.forEach(fn); } };
  };
  Query.prototype.onSnapshot = function (next, error) {
    var self = this, alive = true, last = null;
    var l = { run: function () { if (!alive) return; self.get().then(function (s) { var sig = JSON.stringify(s.docs.map(function (d) { return [d.id, d.data()]; })); if (sig === last) return; last = sig; next(s); }, function (e) { if (error) error(e); }); } };
    listeners.push(l); l.run();
    return function () { alive = false; listeners = listeners.filter(function (x) { return x !== l; }); };
  };
  var db = { collection: function (path) { return new Query(String(path).replace(/^data\/users\/me\b/, 'data/users/' + (LOCAL.userId || 'me'))); }, doc: function (p) { var s = String(p).split('/'); var id = s.pop(); return new Ref(s.join('/'), id); } };

  /* ---------------- user ---------------- */
  var user = {
    id: async function () { return LOCAL.userId || null; },
    me: async function () { return { id: LOCAL.userId, name: LOCAL.userName || '' }; },
    profiles: async function (ids) { var o = {}; (ids || []).forEach(function (id) { o[id] = { id: id, name: id === LOCAL.userId ? (LOCAL.userName || '') : '' }; }); return o; },
    search: async function () { return []; },
    isOwner: function () { return true; }, canEdit: function () { return true; }, can: async function () { return true; }
  };

  /* ---------------- assets ---------------- */
  var assets = {
    upload: async function (blob) {
      var r = await fetch('/api/assets', { method: 'POST', headers: { 'Content-Type': blob.type || 'application/octet-stream', 'X-AQ': '1' }, body: blob });
      if (!r.ok) throw err('upload_failed', 'Không lưu được file'); return r.json();
    },
    list: async function () { return { assets: [], usage: {} }; },
    'delete': async function () { }
  };

  /* ---------------- downloads ---------------- */
  var downloads = {
    save: async function (o) {
      var b = o.data instanceof Blob ? o.data : new Blob([o.data]);
      var a = document.createElement('a'); a.href = URL.createObjectURL(b); a.download = o.filename || 'file'; document.body.appendChild(a); a.click();
      setTimeout(function () { URL.revokeObjectURL(a.href); a.remove(); }, 2000); return { status: 'saved' };
    }
  };

  /* ---------------- mcp: chỉ host:aq-autotest (server.py làm trực tiếp) ---------------- */
  var mcp = {
    callTool: async function (server, tool, input) {
      if (server !== 'host:aq-autotest') throw err('server_not_connected', 'Bản localhost không có kết nối ' + server);
      var out = await api('POST', '/api/kit/' + encodeURIComponent(tool), input || {});
      return { content: [{ type: 'text', text: JSON.stringify(out) }], structuredContent: out, payload: out };
    },
    listTools: async function () { return { servers: [{ server: 'host:aq-autotest', authStatus: 'connected', tools: [] }] }; },
    server: async function (name) { return new Proxy({}, { get: function (_, t) { return function (input) { return mcp.callTool(name, t, input).then(function (r) { return r.payload; }); }; } }); }
  };

  var permissions = { state: async function () { return 'granted'; }, request: async function () { return {}; }, manage: async function () { } };
  var caps = { db: db, user: user, assets: assets, downloads: downloads, mcp: mcp, permissions: permissions };
  window.claude = { use: function (name) { return Promise.resolve(caps[name] || null); } };
})();
