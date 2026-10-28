(() => {
  const toggle = document.getElementById('theme-toggle');
  if (!toggle) return;
  const applyTheme = (dark) => {
    document.documentElement.dataset.theme = dark ? 'dark' : 'light';
    toggle.setAttribute('aria-pressed', String(dark));
    toggle.setAttribute('aria-label', `Switch to ${dark ? 'light' : 'dark'} theme`);
  };
  let savedTheme;
  try { savedTheme = localStorage.getItem('theme'); } catch (_) { /* Themes also work without storage. */ }
  applyTheme(savedTheme === 'dark' || savedTheme === 'dark-mode');
  toggle.hidden = false;
  toggle.addEventListener('click', () => {
    const dark = document.documentElement.dataset.theme !== 'dark';
    applyTheme(dark);
    try { localStorage.setItem('theme', dark ? 'dark' : 'light'); } catch (_) { /* Keep the selected theme for this visit. */ }
  });
})();
