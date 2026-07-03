/* ============================================
   ABYNSS STUDIO — Navbar Component
   ============================================ */

import { throttle } from '../utils.js';

export function initNavbar() {
  const navbar = document.querySelector('.navbar');
  const hamburger = document.querySelector('.hamburger');
  const mobileMenu = document.querySelector('.mobile-menu');
  const mobileLinks = document.querySelectorAll('.mobile-menu-link');

  if (!navbar) return;

  // Scroll effect — glass background on scroll
  const onScroll = throttle(() => {
    if (window.scrollY > 50) {
      navbar.classList.add('scrolled');
    } else {
      navbar.classList.remove('scrolled');
    }
  }, 100);

  window.addEventListener('scroll', onScroll);

  // Hamburger toggle
  if (hamburger && mobileMenu) {
    hamburger.addEventListener('click', () => {
      hamburger.classList.toggle('active');
      mobileMenu.classList.toggle('active');
      document.body.style.overflow = mobileMenu.classList.contains('active') ? 'hidden' : '';

      // Stagger animation for mobile links
      mobileLinks.forEach((link, i) => {
        if (mobileMenu.classList.contains('active')) {
          link.style.transitionDelay = `${0.1 + i * 0.05}s`;
        } else {
          link.style.transitionDelay = '0s';
        }
      });
    });

    // Close menu on link click
    mobileLinks.forEach(link => {
      link.addEventListener('click', () => {
        hamburger.classList.remove('active');
        mobileMenu.classList.remove('active');
        document.body.style.overflow = '';
      });
    });
  }

  // Active link highlighting
  highlightActiveLink();
}

function highlightActiveLink() {
  const currentPath = window.location.pathname;
  const navLinks = document.querySelectorAll('.navbar-link, .mobile-menu-link');

  navLinks.forEach(link => {
    const href = link.getAttribute('href');
    if (!href) return;

    // Remove trailing slashes for comparison
    const normalizedPath = currentPath.replace(/\/+$/, '') || '/';
    const normalizedHref = new URL(href, window.location.href).pathname.replace(/\/+$/, '') || '/';

    if (normalizedPath === normalizedHref) {
      link.classList.add('active');
    } else {
      link.classList.remove('active');
    }
  });
}
