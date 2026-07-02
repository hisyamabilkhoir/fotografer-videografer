/* ============================================
   ABYNSS STUDIO — Back to Top Button
   ============================================ */

import { throttle } from '../utils.js';

export function initBackToTop() {
  const btn = document.querySelector('.back-to-top');
  if (!btn) return;

  const toggleVisibility = throttle(() => {
    if (window.scrollY > 500) {
      btn.classList.add('visible');
    } else {
      btn.classList.remove('visible');
    }
  }, 100);

  window.addEventListener('scroll', toggleVisibility);

  btn.addEventListener('click', () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  });
}
