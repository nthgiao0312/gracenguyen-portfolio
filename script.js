(() => {
  const $ = (sel, root = document) => root.querySelector(sel);
  const $$ = (sel, root = document) => Array.from(root.querySelectorAll(sel));

  // --- Filter: Work section ---
  const filters = $$('.filter');
  const cards = $$('.card');

  const setFilter = (value) => {
    filters.forEach((btn) => {
      const active = btn.dataset.filter === value;
      btn.classList.toggle('is-active', active);
      btn.setAttribute('aria-selected', active ? 'true' : 'false');
    });

    cards.forEach((card) => {
      const match = value === 'all' || card.dataset.category === value;
      card.classList.toggle('is-hidden', !match);
    });
  };

  filters.forEach((btn) => {
    btn.addEventListener('click', () => setFilter(btn.dataset.filter));
  });

  // --- Sticky nav shadow on scroll ---
  const navBar = $('.nav-bar');
  const onScroll = () => {
    if (!navBar) return;
    navBar.classList.toggle('is-scrolled', window.scrollY > 8);
  };
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  // --- Mobile menu ---
  const toggle = $('.nav__toggle');
  const links = $('.nav__links');

  if (toggle && links) {
    toggle.addEventListener('click', () => {
      const open = links.classList.toggle('is-open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });

    links.querySelectorAll('a').forEach((a) => {
      a.addEventListener('click', () => {
        links.classList.remove('is-open');
        toggle.setAttribute('aria-expanded', 'false');
      });
    });
  }
})();
