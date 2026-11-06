/* KaziBora site script: navigation, saved jobs, job search & filters, forms helpers, consent-gated analytics. No dependencies. */
(function () {
  'use strict';
  var KB = window.KB || {};
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var store = {
    get: function (k, d) { try { var v = localStorage.getItem(k); return v ? JSON.parse(v) : d; } catch (e) { return d; } },
    set: function (k, v) { try { localStorage.setItem(k, JSON.stringify(v)); } catch (e) { /* private mode */ } }
  };
  function toast(msg) {
    var t = document.createElement('div'); t.className = 'toast'; t.setAttribute('role', 'status'); t.textContent = msg;
    document.body.appendChild(t); setTimeout(function () { t.remove(); }, 2200);
  }
  window.KBToast = toast;

  /* ---------- navigation ---------- */
  var toggle = $('.nav-toggle'), nav = $('#site-nav');
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open);
      toggle.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
      var hdr = $('.site-header'); if (hdr) nav.style.top = Math.max(hdr.getBoundingClientRect().bottom, 0) + 'px';
      document.body.style.overflow = open ? 'hidden' : '';
    });
  }
  $$('.sub-toggle').forEach(function (b) {
    b.addEventListener('click', function () {
      var li = b.parentElement, open = !li.classList.contains('open');
      $$('.has-sub.open').forEach(function (x) { if (x !== li) { x.classList.remove('open'); x.firstElementChild.setAttribute('aria-expanded', 'false'); } });
      li.classList.toggle('open', open); b.setAttribute('aria-expanded', open);
    });
  });
  document.addEventListener('click', function (e) {
    if (!e.target.closest('.has-sub')) $$('.has-sub.open').forEach(function (x) { x.classList.remove('open'); });
  });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') $$('.has-sub.open').forEach(function (x) { x.classList.remove('open'); }); });

  /* ---------- demo date rolling (only when the site ships demo data) ---------- */
  var MONTHS = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
  function fmt(d) { return d.getDate() + ' ' + MONTHS[d.getMonth()] + ' ' + d.getFullYear(); }
  function shift(n) { var d = new Date(); d.setDate(d.getDate() + n); return d; }
  function agoText(n) { return n === 0 ? 'today' : n === 1 ? 'yesterday' : n + ' days ago'; }
  function leftText(n) { return n <= 0 ? 'today' : n === 1 ? 'tomorrow' : 'in ' + n + ' days'; }
  function rollDates(root) {
    if (!KB.demo) return;
    $$('.job-card', root).forEach(function (c) {
      var a = +c.dataset.ago, l = +c.dataset.left, p = $('[data-posted]', c), cl = $('[data-closes]', c);
      if (p) p.textContent = 'Posted ' + agoText(a);
      if (cl) cl.textContent = 'Closes ' + leftText(l);
    });
    $$('[data-posted-long]', root).forEach(function (el) { el.textContent = fmt(shift(-(+el.dataset.ago))); });
    $$('[data-closes-long]', root).forEach(function (el) { el.textContent = fmt(shift(+el.dataset.left)); });
  }
  rollDates(document);

  /* ---------- saved jobs ---------- */
  var saved = store.get('kb_saved', []);
  function paintSaved(root) {
    $$('[data-save]', root).forEach(function (b) {
      var on = saved.indexOf(b.dataset.save) > -1; b.setAttribute('aria-pressed', on);
      var s = $('span', b); if (s) s.textContent = on ? 'Saved' : 'Save job';
    });
  }
  document.addEventListener('click', function (e) {
    var b = e.target.closest('[data-save]'); if (!b) return;
    var id = b.dataset.save, i = saved.indexOf(id);
    if (i > -1) saved.splice(i, 1); else saved.push(id);
    store.set('kb_saved', saved); paintSaved(document);
    toast(i > -1 ? 'Removed from saved jobs' : 'Job saved to this device');
    if ($('#saved-list')) renderSaved();
  });
  paintSaved(document);
  document.addEventListener('click', function (e) {
    var b = e.target.closest('[data-copy]'); if (!b) return;
    var t = b.dataset.copy;
    if (navigator.clipboard) navigator.clipboard.writeText(t).then(function () { toast('Link copied'); }, function () { toast(t); });
    else toast(t);
  });

  function renderSaved() {
    var box = $('#saved-list'); if (!box) return;
    fetch('/assets/jobs.json').then(function (r) { return r.json(); }).then(function (all) {
      var list = all.filter(function (j) { return saved.indexOf(j.id) > -1; });
      $('#saved-empty').hidden = list.length > 0;
      box.innerHTML = list.map(function (j) {
        return '<article class="job-card" data-id="' + j.id + '" data-ago="' + j.ago + '" data-left="' + j.left + '"><a class="job-logo" href="' + j.url + '" tabindex="-1" aria-hidden="true"><img src="' + j.logo + '" width="56" height="56" alt=""></a>' +
          '<div class="job-main"><h3><a href="' + j.url + '">' + esc(j.title) + '</a></h3><p class="job-co">' + esc(j.company) + (j.verified ? ' <span class="badge verified">Verified</span>' : '') + '</p>' +
          '<ul class="job-meta"><li>' + esc(j.where) + '</li><li>' + esc(j.type) + '</li><li>' + esc(j.pay) + '</li></ul></div>' +
          '<div class="job-side"><button type="button" class="save" data-save="' + j.id + '" aria-pressed="true" aria-label="Remove saved job">&#10084;</button><span class="when" data-posted>Posted ' + agoText(j.ago) + '</span><a class="btn btn-sm btn-primary" href="' + j.url + '">View job</a></div></article>';
      }).join('');
      rollDates(box);
    }).catch(function () { $('#saved-empty').hidden = false; });
  }
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }
  renderSaved();

  /* ---------- job board filters ---------- */
  var results = $('#results');
  if (results) {
    var panel = $('.filters'), list = $('.job-list', results), cards = $$('.job-card', list);
    var PAGE = 20, shown = PAGE;
    var f = {
      q: $('[name=q]', panel), category: $('[name=category]', panel), location: $('[name=location]', panel), type: $('[name=type]', panel),
      salary: $('[name=salary]', panel), remote: $('[name=remote]', panel), verified: $('[name=verified]', panel), levels: $$('[name=level]', panel)
    };
    var sort = $('#sort'), count = $('#res-count'), none = $('#no-results'), more = $('#more-btn'), chips = $('#active-filters');
    var originalOrder = cards.slice();

    function readURL() {
      var p = new URLSearchParams(location.search);
      f.q.value = p.get('q') || ''; f.category.value = p.get('category') || ''; f.location.value = p.get('location') || '';
      f.type.value = p.get('type') || ''; f.salary.value = p.get('salary') || ''; f.remote.checked = p.get('remote') === '1'; f.verified.checked = p.get('verified') === '1';
      var lv = (p.get('level') || '').split(',');
      f.levels.forEach(function (c) { c.checked = lv.indexOf(c.value) > -1; });
      if (p.get('sort')) sort.value = p.get('sort');
    }
    function state() {
      return {
        q: f.q.value.trim().toLowerCase(), category: f.category.value, location: f.location.value, type: f.type.value, salary: +f.salary.value || 0,
        remote: f.remote.checked, verified: f.verified.checked, levels: f.levels.filter(function (c) { return c.checked; }).map(function (c) { return c.value; }), sort: sort.value
      };
    }
    function writeURL(s) {
      var p = new URLSearchParams();
      if (s.q) p.set('q', f.q.value.trim()); if (s.category) p.set('category', s.category); if (s.location) p.set('location', s.location);
      if (s.type) p.set('type', s.type); if (s.salary) p.set('salary', s.salary); if (s.remote) p.set('remote', '1'); if (s.verified) p.set('verified', '1');
      if (s.levels.length) p.set('level', s.levels.join(',')); if (s.sort !== 'relevance') p.set('sort', s.sort);
      var qs = p.toString(); history.replaceState(null, '', location.pathname + (qs ? '?' + qs : ''));
    }
    function match(c, s) {
      var d = c.dataset;
      if (s.category && d.cat !== s.category) return false;
      if (s.location && d.loc !== s.location) return false;
      if (s.type && d.type !== s.type) return false;
      if (s.levels.length && s.levels.indexOf(d.level) < 0) return false;
      if (s.remote && d.remote !== '1') return false;
      if (s.verified && d.verified !== '1') return false;
      if (s.salary && +d.salary < s.salary) return false;
      if (s.q) { var hay = c.textContent.toLowerCase().replace(/\s+/g, ' '); return s.q.split(/\s+/).every(function (t) { return hay.indexOf(t) > -1; }); }
      return true;
    }
    function sorted(arr, mode) {
      var a = arr.slice();
      var key = { newest: function (c) { return +c.dataset.ago; }, closing: function (c) { return +c.dataset.left; }, pay: function (c) { return -c.dataset.salary; } }[mode];
      if (mode === 'relevance') return originalOrder.filter(function (c) { return a.indexOf(c) > -1; });
      return a.sort(function (x, y) { return key(x) - key(y); });
    }
    function chipsFor(s) {
      var out = [];
      function add(label, fn) { out.push('<button type="button" data-x="' + out.length + '">' + esc(label) + ' &times;</button>'); chipFns.push(fn); }
      var chipFns = [];
      if (s.q) add('"' + f.q.value.trim() + '"', function () { f.q.value = ''; });
      if (s.category) add(f.category.options[f.category.selectedIndex].text, function () { f.category.value = ''; });
      if (s.location) add(f.location.options[f.location.selectedIndex].text, function () { f.location.value = ''; });
      if (s.type) add(s.type, function () { f.type.value = ''; });
      s.levels.forEach(function (l) { var el = f.levels.filter(function (c) { return c.value === l; })[0]; add(el.parentNode.textContent.trim(), function () { el.checked = false; }); });
      if (s.salary) add('KSh ' + s.salary.toLocaleString() + '+', function () { f.salary.value = ''; });
      if (s.remote) add('Remote only', function () { f.remote.checked = false; });
      if (s.verified) add('Verified only', function () { f.verified.checked = false; });
      chips.innerHTML = out.join(''); chips._fns = chipFns;
    }
    function apply(resetPage) {
      if (resetPage) shown = PAGE;
      var s = state(), ok = sorted(cards.filter(function (c) { return match(c, s); }), s.sort), n = 0;
      cards.forEach(function (c) { c.hidden = true; });
      ok.forEach(function (c) { list.appendChild(c); c.hidden = ++n > shown; });
      count.innerHTML = '<b>' + ok.length + '</b> job' + (ok.length === 1 ? '' : 's') + ' found';
      none.hidden = ok.length > 0; more.hidden = ok.length <= shown;
      chipsFor(s); writeURL(s);
    }
    $$('input,select', panel).forEach(function (el) { el.addEventListener(el.type === 'search' ? 'input' : 'change', function () { apply(true); }); });
    sort.addEventListener('change', function () { apply(true); });
    more.addEventListener('click', function () { shown += PAGE; apply(false); });
    chips.addEventListener('click', function (e) { var b = e.target.closest('button'); if (!b) return; chips._fns[+b.dataset.x](); apply(true); });
    $('[data-reset]', panel).addEventListener('click', function () { f.q.value = ''; f.category.value = f.location.value = f.type.value = f.salary.value = ''; f.remote.checked = f.verified.checked = false; f.levels.forEach(function (c) { c.checked = false; }); sort.value = 'relevance'; apply(true); });
    var open = $('[data-open-filters]'), close = $('[data-close-filters]');
    if (open) open.addEventListener('click', function () { panel.classList.add('open'); document.body.style.overflow = 'hidden'; });
    if (close) close.addEventListener('click', function () { panel.classList.remove('open'); document.body.style.overflow = ''; window.scrollTo({ top: results.offsetTop - 80 }); });
    readURL(); apply(true);
    window.addEventListener('popstate', function () { readURL(); apply(true); });
  }

  /* ---------- forms helpers ---------- */
  var params = new URLSearchParams(location.search);
  var planRadios = $$('input[name=plan][data-price]');
  if (planRadios.length) {
    var total = $('#plan-total'), want = params.get('plan');
    function upd() { var c = planRadios.filter(function (r) { return r.checked; })[0]; if (c && total) total.textContent = 'KSh ' + (+c.dataset.price).toLocaleString('en-KE'); }
    planRadios.forEach(function (r) { if (want && r.value === want) r.checked = true; r.addEventListener('change', upd); }); upd();
  }
  var jobField = $('#f-job'); if (jobField && params.get('job')) jobField.value = params.get('job').replace(/-/g, ' ');
  $$('[data-course]').forEach(function (a) {
    if (a.tagName === 'A') a.addEventListener('click', function () { var s = $('[data-course-select]'); if (s) s.value = a.dataset.course; });
  });
  /* Netlify forms: friendly submit state */
  $$('form[data-netlify]').forEach(function (fm) {
    fm.addEventListener('submit', function () { var b = $('button[type=submit]', fm); if (b) { b.disabled = true; b.textContent = 'Sending...'; } });
  });

  /* ---------- consent-gated analytics ---------- */
  var anyTracking = KB.ga4 || KB.gtm || KB.ads || KB.meta;
  function loadScript(src, cb) { var s = document.createElement('script'); s.async = true; s.src = src; if (cb) s.onload = cb; document.head.appendChild(s); }
  function loadTracking() {
    window.dataLayer = window.dataLayer || [];
    function gtag() { dataLayer.push(arguments); } window.gtag = gtag;
    if (KB.gtm) { dataLayer.push({ 'gtm.start': Date.now(), event: 'gtm.js' }); loadScript('https://www.googletagmanager.com/gtm.js?id=' + KB.gtm); }
    var id = KB.ga4 || KB.ads;
    if (id && !KB.gtm) { loadScript('https://www.googletagmanager.com/gtag/js?id=' + id); gtag('js', new Date()); if (KB.ga4) gtag('config', KB.ga4, { anonymize_ip: true }); if (KB.ads) gtag('config', KB.ads); }
    if (KB.meta) {
      !function (f, b, e, v, n, t, s) { if (f.fbq) return; n = f.fbq = function () { n.callMethod ? n.callMethod.apply(n, arguments) : n.queue.push(arguments); }; if (!f._fbq) f._fbq = n; n.push = n; n.loaded = !0; n.version = '2.0'; n.queue = []; t = b.createElement(e); t.async = !0; t.src = v; s = b.getElementsByTagName(e)[0]; s.parentNode.insertBefore(t, s); }(window, document, 'script', 'https://connect.facebook.net/en_US/fbevents.js');
      fbq('init', KB.meta); fbq('track', 'PageView');
    }
  }
  if (anyTracking) {
    var c = store.get('kb_consent', null);
    if (c === 'yes') loadTracking();
    else if (c === null) {
      var bar = document.createElement('div'); bar.className = 'consent'; bar.setAttribute('role', 'dialog'); bar.setAttribute('aria-label', 'Cookie consent');
      bar.innerHTML = '<p>We use cookies for analytics and to measure our adverts. You can accept or decline; the site works either way. See our <a href="/privacy/">privacy policy</a>.</p><div><button class="btn btn-primary btn-sm" data-c="yes">Accept</button><button class="btn btn-outline btn-sm" data-c="no">Decline</button></div>';
      document.body.appendChild(bar);
      bar.addEventListener('click', function (e) { var b = e.target.closest('[data-c]'); if (!b) return; store.set('kb_consent', b.dataset.c); bar.remove(); if (b.dataset.c === 'yes') loadTracking(); });
    }
  }
})();
