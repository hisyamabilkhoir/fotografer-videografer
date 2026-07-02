/* ============================================
   ABYNSS STUDIO — Loading Screen
   ============================================ */

export function initLoader() {
  const loader = document.getElementById('loader');
  if (!loader) return;

  const percentEl = loader.querySelector('.loader-percent');
  let progress = 0;

  // Animate percentage counter
  const interval = setInterval(() => {
    progress += Math.random() * 15;
    if (progress >= 100) {
      progress = 100;
      clearInterval(interval);
      // Hide loader after completion
      setTimeout(() => {
        loader.classList.add('hidden');
        document.body.classList.remove('loading');
        // Trigger hero animations after loader disappears
        document.dispatchEvent(new CustomEvent('loaderComplete'));
      }, 400);
    }
    if (percentEl) percentEl.textContent = `${Math.floor(progress)}%`;
  }, 80);
}
