/* Interview trainer, scam checker and course enquiry helpers. */
(function () {
  'use strict';
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };

  /* ----- interview trainer ----- */
  var list = $('#iq-list');
  if (list) {
    var items = $$('.iq', list), chips = $('#iq-chips'), cur = '';
    chips.addEventListener('click', function (e) {
      var b = e.target.closest('[data-iq-cat]'); if (!b) return;
      cur = b.dataset.iqCat; $$('.chip', chips).forEach(function (c) { c.classList.toggle('is-on', c === b); });
      items.forEach(function (i) { i.hidden = cur && i.dataset.cat !== cur; });
    });
    var pr = $('#practice'), q = $('#pr-q'), tip = $('#pr-tip'), timerEl = $('#pr-timer'), t = null, left = 120, order = [], idx = -1;
    function pool() { return items.filter(function (i) { return !cur || i.dataset.cat === cur; }); }
    function show() {
      var p = pool(); if (!p.length) return;
      if (!order.length || idx >= order.length - 1) { order = p.slice().sort(function () { return Math.random() - .5; }); idx = -1; }
      var it = order[++idx];
      q.textContent = it.querySelector('summary').childNodes[1].textContent;
      tip.textContent = it.querySelector('p').textContent; tip.hidden = true; stop(); left = 120; paint();
      $('#pr-start').textContent = 'Start timer';
    }
    function paint() { var m = Math.floor(left / 60), s = left % 60; timerEl.textContent = (m < 10 ? '0' : '') + m + ':' + (s < 10 ? '0' : '') + s; }
    function stop() { if (t) { clearInterval(t); t = null; } }
    $('#pr-open').addEventListener('click', function () { pr.hidden = false; order = []; idx = -1; show(); pr.scrollIntoView({ behavior: 'smooth', block: 'center' }); });
    $('#pr-close').addEventListener('click', function () { pr.hidden = true; stop(); });
    $('#pr-next').addEventListener('click', show);
    $('#pr-reveal').addEventListener('click', function () { tip.hidden = !tip.hidden; });
    $('#pr-start').addEventListener('click', function () {
      if (t) { stop(); this.textContent = 'Resume'; return; }
      var self = this; self.textContent = 'Pause';
      t = setInterval(function () { left--; paint(); if (left <= 0) { stop(); self.textContent = 'Restart'; left = 120; if (window.KBToast) window.KBToast('Time is up. Review the tip and try again.'); } }, 1000);
    });
  }

  /* ----- scam checker ----- */
  var form = $('#scam-form');
  if (form) {
    var card = $('#scam-result'), bar = $('#scam-bar'), title = $('#scam-title'), text = $('#scam-text'), act = $('#scam-actions');
    var boxes = $$('input[type=checkbox]', form);
    function run() {
      var score = 0, max = 0, severe = false, n = 0;
      boxes.forEach(function (b) { var w = +b.dataset.w; max += w; if (b.checked) { score += w; n++; if (w >= 5) severe = true; } });
      card.className = 'result-card';
      if (!n) { title.textContent = 'Tick the boxes that apply'; text.textContent = 'We will assess the risk as you go.'; bar.style.width = '0'; act.innerHTML = ''; return; }
      var pct = Math.min(100, Math.round(score / 14 * 100));
      bar.style.width = Math.max(pct, 8) + '%';
      if (severe || score >= 7) {
        card.classList.add('high'); title.textContent = 'High risk: likely a scam';
        text.textContent = 'This offer matches serious scam patterns. Do not pay any money or share ID, bank or M-Pesa details.';
        act.innerHTML = '<ul><li>Stop communicating and do not send money.</li><li>Keep screenshots, numbers and receipts.</li><li>If you paid, contact your payment provider or bank immediately and report to the police.</li></ul><p><a class="btn btn-primary btn-sm" href="/report-scam/">Report this job</a></p>';
      } else if (score >= 3) {
        card.classList.add('med'); title.textContent = 'Medium risk: be careful';
        text.textContent = 'Several warning signs are present. Verify the employer independently before going further.';
        act.innerHTML = '<ul><li>Find the company\'s official website and call its published number.</li><li>Ask for a proper interview at the company\'s office or on its official video link.</li><li>Do not share ID or bank details until you have a written offer.</li></ul><p><a class="btn btn-outline btn-sm" href="/report-scam/">Report if unsure</a></p>';
      } else {
        card.classList.add('low'); title.textContent = 'Lower risk, stay alert';
        text.textContent = 'Only minor warning signs so far. Keep checking and never pay to get a job.';
        act.innerHTML = '<ul><li>Confirm the employer on its official channels.</li><li>Never pay for applications, training or uniforms.</li></ul><p><a class="btn btn-outline btn-sm" href="/jobs/">Browse verified jobs</a></p>';
      }
    }
    boxes.forEach(function (b) { b.addEventListener('change', run); });
  }
})();
