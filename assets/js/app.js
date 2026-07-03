/* ============================================
   ABYNSS STUDIO — Main App Entry Point
   Initializes all global components
   ============================================ */

import { initLoader } from './core/loader.js';
import { initCursor } from './core/cursor.js';
import { initSmoothScroll } from './core/smooth-scroll.js';
import { initScrollAnimations } from './core/scroll-animations.js';
import { initNavbar } from './components/navbar.js';
import { initCounters } from './components/counter.js';
import { initScrollProgress } from './components/scroll-progress.js';
import { initBackToTop } from './components/back-to-top.js';
import { initWhatsAppFloat } from './components/whatsapp-float.js';
import { initMagneticButtons } from './components/magnetic-btn.js';
import { initMarquee } from './components/marquee.js';
import { initLightbox } from './components/lightbox.js';
import { initAccordion } from './components/accordion.js';
import { initLazyLoad, getBasePath } from './utils.js';

import { initPageTransitions } from './core/transitions.js';
import { initTilts } from './components/tilt.js';

// ---- App initialization ----
// ES6 modules are deferred by default, meaning they run after the DOM is parsed.
// Initializing directly avoids race conditions where DOMContentLoaded has already fired.
initLoader();

document.addEventListener('loaderComplete', async () => {
  // Core systems
  initSmoothScroll();
  // initCursor(); // Disabled custom cursor as per user request to avoid stuck elements and visual clutter
  initPageTransitions();

  // Global components
  initNavbar();
  initScrollProgress();
  initBackToTop();
  initWhatsAppFloat();
  initMagneticButtons();
  initMarquee();
  initLightbox();
  initAccordion();
  initCounters();
  initLazyLoad();

  // Page-specific initialization (await dynamic content loads)
  const path = window.location.pathname;
  
  if (isDynamicListPage(path)) {
    document.addEventListener('contentReady', () => {
      initScrollAnimations();
      initTilts();
    }, { once: true });
    
    await initCurrentPage();
  } else {
    // Initialize immediately for static detail pages
    initScrollAnimations();
    initTilts();
  }
});

// ---- Page-specific initialization ----
async function initCurrentPage() {
  const path = window.location.pathname;

  try {
    // Determine which page we're on
    if (isPage(path, '/') || path.endsWith('/index.html')) {
      const m = await import('./pages/home.js');
      if (m.initHomePage) {
        await m.initHomePage();
      }
    }
  } catch (err) {
    console.error('Error loading page-specific logic:', err);
  }
}

function isDynamicListPage(path) {
  const basePath = getBasePath();
  const normalized = path
    .replace(basePath, '')
    .replace(/\/index\.html$/, '')
    .replace(/\/+$/, '') || '/';
  const dynamicPaths = [
    '/',
    '/portfolio',
    '/gallery',
    '/services',
    '/pricing',
    '/articles',
    '/activities',
    '/testimonials'
  ];
  return dynamicPaths.includes(normalized);
}

function isPage(currentPath, targetPath) {
  const basePath = getBasePath();
  const normalized = currentPath.replace(basePath, '').replace(/\/+$/, '') || '/';
  return normalized === targetPath;
}
