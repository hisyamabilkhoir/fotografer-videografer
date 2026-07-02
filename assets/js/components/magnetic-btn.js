/* ============================================
   ABYNSS STUDIO — Magnetic Button
   Buttons attracted to cursor on hover
   ============================================ */

import { isTouch } from '../utils.js';

export function initMagneticButtons() {
  if (isTouch()) return;

  const buttons = document.querySelectorAll('[data-magnetic]');
  buttons.forEach(btn => {
    btn.addEventListener('mousemove', (e) => {
      const rect = btn.getBoundingClientRect();
      const x = e.clientX - rect.left - rect.width / 2;
      const y = e.clientY - rect.top - rect.height / 2;
      const strength = parseFloat(btn.dataset.magnetic) || 0.3;

      btn.style.transform = `translate(${x * strength}px, ${y * strength}px)`;
    });

    btn.addEventListener('mouseleave', () => {
      btn.style.transform = 'translate(0, 0)';
      btn.style.transition = 'transform 0.4s cubic-bezier(0.16, 1, 0.3, 1)';
    });

    btn.addEventListener('mouseenter', () => {
      btn.style.transition = 'none';
    });
  });
}
