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

  /* ---------- scroll reveal ---------- */
  var revealEls = Array.prototype.slice.call(document.querySelectorAll('[data-reveal]'));
  if (revealEls.length) {
    // stagger siblings so grids cascade instead of popping together
    var seen = new Map();
    revealEls.forEach(function (el) {
      var parent = el.parentElement;
      var i = seen.get(parent) || 0;
      seen.set(parent, i + 1);
      el.style.setProperty('--d', Math.min(i, 5) * 70 + 'ms');
    });

    if ('IntersectionObserver' in window) {
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          if (!entry.isIntersecting) return;
          entry.target.classList.add('is-in');
          io.unobserve(entry.target);
        });
      }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
      revealEls.forEach(function (el) { io.observe(el); });

      // safety net: anything still hidden after 3s becomes visible
      setTimeout(function () {
        revealEls.forEach(function (el) {
          if (!el.classList.contains('is-in')) el.classList.add('is-in');
        });
      }, 3000);
    } else {
      revealEls.forEach(function (el) { el.classList.add('is-in'); });
    }
  }

  /* ---------- header shadow on scroll ---------- */
  var headerEl = document.querySelector('header.site-header');
  if (headerEl) {
    var ticking = false;
    var onHead = function () {
      if (ticking) return;
      ticking = true;
      requestAnimationFrame(function () {
        headerEl.classList.toggle('scrolled', (window.scrollY || 0) > 8);
        ticking = false;
      });
    };
    window.addEventListener('scroll', onHead, { passive: true });
    onHead();
  }

  /* ---------- video testimonials (click to load) ---------- */
  document.querySelectorAll('.video-card[data-video]').forEach(function (card) {
    card.addEventListener('click', function () {
      if (card.classList.contains('playing')) return;
      var id = card.getAttribute('data-video');
      if (!id) return;
      var frame = document.createElement('iframe');
      frame.src = 'https://www.youtube-nocookie.com/embed/' + id +
                  '?autoplay=1&rel=0&playsinline=1&modestbranding=1';
      frame.title = card.getAttribute('aria-label') || 'Client video';
      frame.allow = 'accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture';
      frame.setAttribute('allowfullscreen', '');
      card.innerHTML = '';
      card.appendChild(frame);
      card.classList.add('playing');
    });
  });

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
