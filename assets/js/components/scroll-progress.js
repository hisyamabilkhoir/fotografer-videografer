/* ============================================
   ABYNSS STUDIO — Scroll Progress Bar
   ============================================ */

import { throttle } from '../utils.js';

export function initScrollProgress() {
  const progressBar = document.querySelector('.scroll-progress-bar');
  if (!progressBar) return;

  const updateProgress = throttle(() => {
    const scrollTop = window.scrollY;
    const docHeight = document.documentElement.scrollHeight - window.innerHeight;
    const progress = docHeight > 0 ? scrollTop / docHeight : 0;
    progressBar.style.transform = `scaleX(${progress})`;
  }, 16);

  window.addEventListener('scroll', updateProgress);
}
