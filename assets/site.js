/* ============================================================
   Tarot with Nisha — shared site behaviour
   ============================================================ */
(function () {
  'use strict';

  /* ---------- mobile menu ---------- */
  var ham = document.getElementById('hamBtn');
  var mobile = document.getElementById('mobileMenu');
  if (ham && mobile) {
    ham.addEventListener('click', function () {
      var open = mobile.classList.toggle('open');
      ham.setAttribute('aria-expanded', String(open));
    });
    mobile.querySelectorAll('a').forEach(function (a) {
      a.addEventListener('click', function () {
        mobile.classList.remove('open');
        ham.setAttribute('aria-expanded', 'false');
      });
    });
  }

  /* ---------- dropdown navigation ---------- */
  var navItems = Array.prototype.slice.call(
    document.querySelectorAll('.navlinks > li')
  ).filter(function (li) { return li.querySelector('.dropdown'); });

  function closeAll(except) {
    navItems.forEach(function (li) {
      if (li === except) return;
      li.classList.remove('open');
      var b = li.querySelector('button');
      if (b) b.setAttribute('aria-expanded', 'false');
    });
  }

  navItems.forEach(function (li) {
    var btn = li.querySelector('button');
    var dd = li.querySelector('.dropdown');
    if (!btn || !dd) return;

    function open() {
      closeAll(li);
      li.classList.add('open');
      btn.setAttribute('aria-expanded', 'true');
    }
    function close() {
      li.classList.remove('open');
      btn.setAttribute('aria-expanded', 'false');
    }

    btn.addEventListener('click', function (ev) {
      ev.preventDefault();
      // On hover-capable desktops the menu is already open from mouseenter;
      // the click that follows must not immediately close it again.
      if (li.dataset.hoverOpened === '1') {
        delete li.dataset.hoverOpened;
        return;
      }
      if (li.classList.contains('open')) close(); else open();
    });

    li.addEventListener('mouseenter', function () {
      if (window.matchMedia('(min-width: 980px)').matches) {
        if (!li.classList.contains('open')) li.dataset.hoverOpened = '1';
        open();
      }
    });
    li.addEventListener('mouseleave', function () {
      if (window.matchMedia('(min-width: 980px)').matches) {
        delete li.dataset.hoverOpened;
        close();
      }
    });

    li.addEventListener('keydown', function (ev) {
      if (ev.key === 'Escape') { close(); btn.focus(); }
      if (ev.key === 'ArrowDown') { ev.preventDefault(); open(); var f = dd.querySelector('a'); if (f) f.focus(); }
    });
  });

  document.addEventListener('click', function (ev) {
    if (!ev.target.closest('.navlinks')) closeAll(null);
  });

  /* ---------- FAQ accordion ---------- */
  document.querySelectorAll('.faq-item').forEach(function (item) {
    var q = item.querySelector('.faq-q');
    var a = item.querySelector('.faq-a');
    if (!q || !a) return;

    function sync() {
      if (item.classList.contains('open')) {
        a.style.maxHeight = a.scrollHeight + 'px';
        q.setAttribute('aria-expanded', 'true');
      } else {
        a.style.maxHeight = '0px';
        q.setAttribute('aria-expanded', 'false');
      }
    }
    sync();
    q.addEventListener('click', function () {
      item.classList.toggle('open');
      sync();
    });
    window.addEventListener('resize', sync);
  });

  /* ---------- product tabs ---------- */
  var tabButtons = document.querySelectorAll('.tab-btn');
  tabButtons.forEach(function (btn) {
    btn.addEventListener('click', function () {
      var group = btn.closest('.tabs');
      if (!group) return;
      group.querySelectorAll('.tab-btn').forEach(function (b) {
        b.setAttribute('aria-selected', 'false');
      });
      group.querySelectorAll('.tab-panel').forEach(function (p) {
        p.classList.remove('active');
      });
      btn.setAttribute('aria-selected', 'true');
      var panel = group.querySelector('#' + btn.getAttribute('aria-controls'));
      if (panel) panel.classList.add('active');
    });
  });

  /* ---------- quantity selector ---------- */
  document.querySelectorAll('.qty').forEach(function (wrap) {
    var input = wrap.querySelector('input');
    var minus = wrap.querySelector('[data-qty="down"]');
    var plus = wrap.querySelector('[data-qty="up"]');
    if (!input) return;
    function set(v) {
      var n = Math.max(1, Math.min(20, parseInt(v, 10) || 1));
      input.value = String(n);
      var form = wrap.closest('form');
      if (form) {
        var hidden = form.querySelector('input[name="qty"]');
        if (hidden) hidden.value = String(n);
      }
    }
    if (minus) minus.addEventListener('click', function () { set(parseInt(input.value, 10) - 1); });
    if (plus) plus.addEventListener('click', function () { set(parseInt(input.value, 10) + 1); });
    input.addEventListener('change', function () { set(input.value); });
  });

  /* ---------- sticky mobile CTA ---------- */
  var sticky = document.getElementById('stickyCta');
  if (sticky) {
    var shown = false;
    function onScroll() {
      var y = window.scrollY || document.documentElement.scrollTop;
      var shouldShow = y > 420;
      if (shouldShow !== shown) {
        shown = shouldShow;
        sticky.classList.toggle('visible', shown);
        document.body.classList.toggle('has-sticky-cta', shown);
      }
    }
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
  }

  /* ---------- year ---------- */
  var y = document.getElementById('year');
  if (y) y.textContent = String(new Date().getFullYear());

  /* ---------- mark real conversions for analytics ---------- */
  document.querySelectorAll('[data-wa-service], .float-wa').forEach(function (el) {
    el.addEventListener('click', function () {
      var payload = {
        event: 'wa_click',
        service: el.getAttribute('data-wa-service') || 'unspecified',
        placement: el.getAttribute('data-wa-placement') || 'unknown',
        page: window.location.pathname
      };
      if (typeof window.gtag === 'function') window.gtag('event', 'wa_click', payload);
    });
  });
})();
