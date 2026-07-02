/* ============================================
   ABYNSS STUDIO — 3D Tilt Component
   VanillaTilt wrapper for luxury 3D card tilts
   ============================================ */

import { isMobile } from '../utils.js';

export function initTilts() {
  // Disable 3D tilt on mobile for performance
  if (isMobile()) return;

  if (typeof VanillaTilt !== 'undefined') {
    const targets = document.querySelectorAll('[data-tilt]');
    VanillaTilt.init(targets, {
      max: 15,
      speed: 400,
      glare: true,
      "max-glare": 0.2,
      scale: 1.02
    });
  }
}
