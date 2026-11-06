/* CV builder and cover letter generator. Everything runs in the browser; nothing is uploaded. */
(function () {
  'use strict';
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  function esc(s) { return String(s == null ? '' : s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }
  function save(k, v) { try { localStorage.setItem(k, JSON.stringify(v)); } catch (e) { } }
  function load(k) { try { return JSON.parse(localStorage.getItem(k)); } catch (e) { return null; } }
  function toast(m) { if (window.KBToast) window.KBToast(m); }

  /* ================= CV BUILDER ================= */
  var prev = $('#cv-preview');
  if (prev) {
    var SAMPLE = {
      name: 'Wanjiru Kamau', title: 'Accounts Assistant', email: 'wanjiru.kamau@example.com', phone: '0712 345 678', location: 'Nairobi, Kenya', link: 'linkedin.com/in/wanjiru-kamau',
      summary: 'Detail-oriented accounting graduate with one year of internship experience in bookkeeping and reconciliations. Fast learner who enjoys turning messy records into clear reports, seeking an entry-level accounts role.',
      exp: [{ role: 'Accounts Intern', company: 'Savanna Ledger Advisory, Nairobi', dates: 'Jan 2026 - Jun 2026', bullets: 'Reconciled 40+ client bank statements monthly with 99% accuracy\nPrepared VAT and PAYE schedules for review by senior accountants\nCut month-end reporting time by 20% by building Excel templates' },
        { role: 'Student Treasurer', company: 'University Commerce Club', dates: '2024 - 2025', bullets: 'Managed a KSh 250,000 budget for events and kept clear records\nRaised KSh 80,000 through a community fundraising drive' }],
      edu: [{ school: 'University of Nairobi', course: 'Bachelor of Commerce (Accounting)', dates: '2021 - 2025' }, { school: 'Kenya Secondary School', course: 'KCSE, Mean grade B+', dates: '2017 - 2020' }],
      skills: 'Excel, QuickBooks, Bookkeeping, Bank reconciliation, Teamwork, Attention to detail', languages: 'English, Kiswahili', referees: '', template: 'classic', accent: '#0f6b4a'
    };
    var EMPTY = { name: '', title: '', email: '', phone: '', location: '', link: '', summary: '', exp: [{ role: '', company: '', dates: '', bullets: '' }], edu: [{ school: '', course: '', dates: '' }], skills: '', languages: '', referees: '', template: 'classic', accent: '#0f6b4a' };
    var S = load('kb_cv') || JSON.parse(JSON.stringify(SAMPLE));
    var tplSel = $('#cv-template'), accSel = $('#cv-accent');

    function bullets(t) {
      var l = String(t || '').split('\n').map(function (x) { return x.replace(/^[\s\-•*]+/, '').trim(); }).filter(Boolean);
      return l.length ? '<ul>' + l.map(function (x) { return '<li>' + esc(x) + '</li>'; }).join('') + '</ul>' : '';
    }
    function render() {
      var contact = [S.email, S.phone, S.location, S.link].filter(Boolean).map(function (x) { return '<span>' + esc(x) + '</span>'; }).join('');
      var exp = S.exp.filter(function (e) { return e.role || e.company; }).map(function (e) {
        return '<div class="item"><div class="row">' + esc(e.role) + '<span>' + esc(e.dates) + '</span></div><div class="sub">' + esc(e.company) + '</div>' + bullets(e.bullets) + '</div>';
      }).join('');
      var edu = S.edu.filter(function (e) { return e.school || e.course; }).map(function (e) {
        return '<div class="item"><div class="row">' + esc(e.course) + '<span>' + esc(e.dates) + '</span></div><div class="sub">' + esc(e.school) + '</div></div>';
      }).join('');
      var skills = S.skills.split(',').map(function (x) { return x.trim(); }).filter(Boolean).map(function (x) { return '<span>' + esc(x) + '</span>'; }).join('');
      var langs = S.languages.split(',').map(function (x) { return x.trim(); }).filter(Boolean).join(' &middot; ');
      var refs = S.referees.trim() ? '<p>' + esc(S.referees).replace(/\n/g, '<br>') + '</p>' : '<p>Available on request.</p>';
      var sec = function (h, b) { return b ? '<h2>' + h + '</h2>' + b : ''; };
      var head = '<h1>' + esc(S.name || 'Your Name') + '</h1><div class="cv-title">' + esc(S.title) + '</div><div class="cv-contact">' + contact + '</div>';
      prev.className = 'cv t-' + S.template; prev.style.setProperty('--a', S.accent);
      if (S.template === 'modern') {
        prev.innerHTML = '<div class="cv-head">' + head + '</div><div class="cv-side">' + sec('Skills', skills && '<div class="skills">' + skills + '</div>') + sec('Languages', langs && '<p>' + langs + '</p>') + sec('Education', edu) + '</div>' +
          '<div class="cv-main">' + sec('Profile', S.summary && '<p>' + esc(S.summary) + '</p>') + sec('Experience', exp) + sec('Referees', refs) + '</div>';
      } else {
        prev.innerHTML = head + sec('Profile', S.summary && '<p>' + esc(S.summary) + '</p>') + sec('Experience', exp) + sec('Education', edu) + sec('Skills', skills && '<div class="skills">' + skills + '</div>') + sec('Languages', langs && '<p>' + langs + '</p>') + sec('Referees', refs);
      }
      save('kb_cv', S);
    }
    function rep(kind, arr, fields, container) {
      container.innerHTML = '';
      arr.forEach(function (item, i) {
        var d = document.createElement('div'); d.className = 'rep';
        d.innerHTML = '<button type="button" class="rm" aria-label="Remove" title="Remove">&times;</button>' + fields.map(function (f) {
          var id = kind + '-' + f[0] + '-' + i;
          return '<div class="fld"><label for="' + id + '">' + f[1] + '</label>' + (f[2] === 'ta' ? '<textarea id="' + id + '" rows="4" data-k="' + f[0] + '" placeholder="' + (f[3] || '') + '"></textarea>' : '<input id="' + id + '" data-k="' + f[0] + '" type="text" placeholder="' + (f[3] || '') + '">') + '</div>';
        }).join('');
        $$('[data-k]', d).forEach(function (el) { el.value = item[el.dataset.k] || ''; el.addEventListener('input', function () { item[el.dataset.k] = el.value; render(); }); });
        $('.rm', d).addEventListener('click', function () { arr.splice(i, 1); if (!arr.length) arr.push({}); build(); render(); });
        container.appendChild(d);
      });
    }
    function build() {
      rep('exp', S.exp, [['role', 'Job title', 'in', 'Accounts Intern'], ['company', 'Company and town', 'in', 'Company, Nairobi'], ['dates', 'Dates', 'in', 'Jan 2026 - Jun 2026'], ['bullets', 'Achievements (one per line)', 'ta', 'Start each line with an action verb']], $('#cv-exp'));
      rep('edu', S.edu, [['course', 'Qualification', 'in', 'Diploma in ...'], ['school', 'Institution', 'in', 'University / College'], ['dates', 'Years', 'in', '2021 - 2025']], $('#cv-edu'));
    }
    function sync() {
      $$('[data-cv]').forEach(function (el) { el.value = S[el.dataset.cv] || ''; el.addEventListener('input', function () { S[el.dataset.cv] = el.value; render(); }); });
      tplSel.value = S.template; accSel.value = S.accent;
      if (accSel.value !== S.accent) { accSel.value = '#0f6b4a'; }
    }
    tplSel.addEventListener('change', function () { S.template = tplSel.value; render(); });
    accSel.addEventListener('change', function () { S.accent = accSel.value; render(); });
    $('#add-exp').addEventListener('click', function () { S.exp.push({}); build(); render(); });
    $('#add-edu').addEventListener('click', function () { S.edu.push({}); build(); render(); });
    $('#cv-print').addEventListener('click', function () { window.print(); });
    $('#cv-sample').addEventListener('click', function () { S = JSON.parse(JSON.stringify(SAMPLE)); sync(); build(); render(); toast('Sample loaded'); });
    $('#cv-clear').addEventListener('click', function () { if (confirm('Clear everything in your CV?')) { S = JSON.parse(JSON.stringify(EMPTY)); sync(); build(); render(); } });
    sync(); build(); render();
  }

  /* ================= COVER LETTER ================= */
  var form = $('#cl-form');
  if (form) {
    var out = $('#cl-out');
    var val = function (n) { var el = form.elements[n]; return el ? el.value.trim() : ''; };
    function list(a) { return a.length < 2 ? (a[0] || '') : a.slice(0, -1).join(', ') + ' and ' + a[a.length - 1]; }
    function letter() {
      var name = val('name') || '[Your name]', job = val('job') || '[Job title]', co = val('company') || '[Company]', mgr = val('manager');
      var skills = val('skills').split(',').map(function (s) { return s.trim(); }).filter(Boolean), ach = val('achievement'), tone = val('tone'), lvl = val('level');
      var d = new Date(), date = d.getDate() + ' ' + ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'][d.getMonth()] + ' ' + d.getFullYear();
      var contact = [val('phone'), val('email'), val('town')].filter(Boolean).join(' | ');
      var open = { professional: 'I am writing to apply for the position of ' + job + ' at ' + co + '. I believe my skills and commitment make me a strong candidate for this role.',
        enthusiastic: 'I was excited to see the ' + job + ' vacancy at ' + co + ' and I would love the opportunity to contribute to your team.',
        concise: 'Please accept this application for the ' + job + ' position at ' + co + '.' }[tone || 'professional'];
      var bg = { graduate: 'As a recent graduate, I bring up-to-date knowledge, a strong work ethic and a hunger to learn. Through my studies, projects and campus activities I have built the foundation to contribute from my first day.',
        some: 'With one to three years of hands-on experience, I have developed practical skills and a record of reliable delivery that I am keen to apply at ' + co + '.',
        experienced: 'With several years of experience, I bring a proven record of delivering results, working with teams and solving problems under pressure.' }[lvl || 'graduate'];
      var sk = skills.length ? 'My key strengths include ' + list(skills) + ', which I believe are directly relevant to this role.' : '';
      var ac = ach ? 'For example, ' + ach.charAt(0).toLowerCase() + ach.slice(1).replace(/\.$/, '') + '. This showed me how to take ownership and deliver results.' : '';
      var why = tone === 'concise' ? '' : '\n\nI am drawn to ' + co + ' because of its reputation and the chance to grow in a team that values integrity and results.';
      var body = [open, bg, sk, ac].filter(Boolean).join('\n\n') + why;
      var close = 'Thank you for considering my application. My CV is attached and I would welcome the chance to discuss how I can contribute. I can be reached on ' + (val('phone') || 'the number above') + '.';
      return name + '\n' + contact + '\n\n' + date + '\n\nDear ' + (mgr || 'Hiring Manager') + ',\n\nRE: APPLICATION FOR ' + job.toUpperCase() + '\n\n' + body + '\n\n' + close + '\n\nYours sincerely,\n' + name;
    }
    function draw() { out.textContent = letter(); }
    form.addEventListener('input', draw); form.addEventListener('change', draw); draw();
    $('#cl-copy').addEventListener('click', function () {
      var t = out.innerText; if (navigator.clipboard) navigator.clipboard.writeText(t).then(function () { toast('Letter copied'); }); else { var r = document.createRange(); r.selectNodeContents(out); getSelection().removeAllRanges(); getSelection().addRange(r); document.execCommand('copy'); toast('Letter copied'); }
    });
    $('#cl-print').addEventListener('click', function () { window.print(); });
  }
})();
