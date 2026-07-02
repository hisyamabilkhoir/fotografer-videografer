/* ============================================
   ABYNSS STUDIO — Page Transitions
   Smooth fade-out/curtain transition on exit
   ============================================ */

import { getBasePath } from '../utils.js';

export function initPageTransitions() {
  const links = document.querySelectorAll('a:not([target="_blank"]):not([href^="#"]):not([href^="mailto:"]):not([href^="tel:"]):not([href^="javascript:"])');
  
  links.forEach(link => {
    link.addEventListener('click', (e) => {
      const href = link.getAttribute('href');
      if (!href) return;

      // Verify it's an internal link
      const isInternal = href.startsWith('.') || href.startsWith('/') || href.startsWith(window.location.origin);
      if (!isInternal) return;

      e.preventDefault();

      // Create transition overlay element dynamically
      const overlay = document.createElement('div');
      overlay.className = 'page-transition-overlay';
      overlay.style.position = 'fixed';
      overlay.style.inset = '0';
      overlay.style.backgroundColor = '#0D0D0D';
      overlay.style.zIndex = '99999';
      overlay.style.transform = 'translateY(100%)';
      overlay.style.transition = 'transform 0.6s cubic-bezier(0.85, 0, 0.15, 1)';
      document.body.appendChild(overlay);

      // Trigger slide up
      requestAnimationFrame(() => {
        overlay.style.transform = 'translateY(0)';
      });

      // Redirect after animation completes
      setTimeout(() => {
        window.location.href = href;
      }, 600);
    });
  });
}
