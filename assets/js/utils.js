/* ============================================
   ABYNSS STUDIO — Utility Functions
   ============================================ */

/**
 * Fetch JSON data from /data/ directory
 * @param {string} filename - JSON filename (e.g., 'site', 'projects')
 * @returns {Promise<Object>}
 */
export async function fetchData(filename) {
  try {
    // Determine base path for GitHub Pages compatibility
    const basePath = getBasePath();
    const response = await fetch(`${basePath}/data/${filename}.json`);
    if (!response.ok) throw new Error(`Failed to load ${filename}.json`);
    return await response.json();
  } catch (error) {
    console.error(`[Data] Error loading ${filename}:`, error);
    return null;
  }
}

/**
 * Get base path for the site (handles GitHub Pages subdirectory)
 * @returns {string}
 */
export function getBasePath() {
  // Check if running on GitHub Pages subdirectory
  const path = window.location.pathname;
  // For local development via XAMPP
  if (path.includes('/abynsstudio/fotografer-videografer')) {
    return '/abynsstudio/fotografer-videografer';
  }
  // For GitHub Pages subdirectory
  if (path.includes('/fotografer-videografer')) {
    return '/fotografer-videografer';
  }
  // For GitHub Pages custom domain or standard root
  return '';
}

/**
 * Resolve asset paths for subdirectory compatibility
 * @param {string} path
 * @returns {string}
 */
export function resolvePath(path) {
  if (!path) return '';
  if (path.startsWith('http') || path.startsWith('data:')) return path;
  
  const basePath = getBasePath();
  const cleanPath = path.startsWith('/') ? path : '/' + path;
  return `${basePath}${cleanPath}`;
}

/**
 * Format number to Indonesian locale
 * @param {number} num
 * @returns {string}
 */
export function formatNumber(num) {
  return new Intl.NumberFormat('id-ID').format(num);
}

/**
 * Format currency to Indonesian Rupiah
 * @param {number} amount
 * @returns {string}
 */
export function formatCurrency(amount) {
  return new Intl.NumberFormat('id-ID', {
    style: 'currency',
    currency: 'IDR',
    minimumFractionDigits: 0,
    maximumFractionDigits: 0
  }).format(amount);
}

/**
 * Format date to Indonesian locale
 * @param {string} dateStr - ISO date string
 * @returns {string}
 */
export function formatDate(dateStr) {
  const date = new Date(dateStr);
  return date.toLocaleDateString('id-ID', {
    day: 'numeric',
    month: 'long',
    year: 'numeric'
  });
}

/**
 * Debounce function
 * @param {Function} func
 * @param {number} wait
 * @returns {Function}
 */
export function debounce(func, wait = 300) {
  let timeout;
  return function executedFunction(...args) {
    clearTimeout(timeout);
    timeout = setTimeout(() => func.apply(this, args), wait);
  };
}

/**
 * Throttle function
 * @param {Function} func
 * @param {number} limit
 * @returns {Function}
 */
export function throttle(func, limit = 100) {
  let inThrottle;
  return function executedFunction(...args) {
    if (!inThrottle) {
      func.apply(this, args);
      inThrottle = true;
      setTimeout(() => inThrottle = false, limit);
    }
  };
}

/**
 * Lazy load images using Intersection Observer
 */
export function initLazyLoad() {
  const images = document.querySelectorAll('img[data-src]');
  if (!images.length) return;

  const imageObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const img = entry.target;
        img.src = img.dataset.src;
        if (img.dataset.srcset) img.srcset = img.dataset.srcset;
        img.removeAttribute('data-src');
        img.removeAttribute('data-srcset');
        img.classList.add('loaded');
        imageObserver.unobserve(img);
      }
    });
  }, { rootMargin: '100px' });

  images.forEach(img => imageObserver.observe(img));
}

/**
 * Generate WhatsApp URL with pre-filled message
 * @param {string} phone - Phone number with country code
 * @param {string} message - Pre-filled message
 * @returns {string}
 */
export function whatsappUrl(phone, message = '') {
  const encoded = encodeURIComponent(message);
  return `https://wa.me/${phone}?text=${encoded}`;
}

/**
 * Check if device is mobile
 * @returns {boolean}
 */
export function isMobile() {
  return window.innerWidth < 768;
}

/**
 * Check if device is tablet
 * @returns {boolean}
 */
export function isTablet() {
  return window.innerWidth >= 768 && window.innerWidth <= 1024;
}

/**
 * Check if device supports touch
 * @returns {boolean}
 */
export function isTouch() {
  return 'ontouchstart' in window || navigator.maxTouchPoints > 0;
}

/**
 * Check if user prefers reduced motion
 * @returns {boolean}
 */
export function prefersReducedMotion() {
  return window.matchMedia('(prefers-reduced-motion: reduce)').matches;
}

/**
 * Simple slug generator
 * @param {string} text
 * @returns {string}
 */
export function slugify(text) {
  return text
    .toLowerCase()
    .replace(/[^\w\s-]/g, '')
    .replace(/[\s_-]+/g, '-')
    .replace(/^-+|-+$/g, '');
}

/**
 * Truncate text to specified length
 * @param {string} text
 * @param {number} maxLength
 * @returns {string}
 */
export function truncate(text, maxLength = 150) {
  if (text.length <= maxLength) return text;
  return text.substr(0, text.lastIndexOf(' ', maxLength)) + '...';
}

/**
 * Get reading time estimate
 * @param {string} text
 * @returns {number} minutes
 */
export function readingTime(text) {
  const wordsPerMinute = 200;
  const words = text.trim().split(/\s+/).length;
  return Math.ceil(words / wordsPerMinute);
}

/**
 * Create element with attributes and children
 * @param {string} tag
 * @param {Object} attrs
 * @param  {...(string|HTMLElement)} children
 * @returns {HTMLElement}
 */
export function createElement(tag, attrs = {}, ...children) {
  const el = document.createElement(tag);
  Object.entries(attrs).forEach(([key, value]) => {
    if (key === 'className') el.className = value;
    else if (key === 'innerHTML') el.innerHTML = value;
    else if (key.startsWith('on')) el.addEventListener(key.slice(2).toLowerCase(), value);
    else el.setAttribute(key, value);
  });
  children.forEach(child => {
    if (typeof child === 'string') el.appendChild(document.createTextNode(child));
    else if (child instanceof HTMLElement) el.appendChild(child);
  });
  return el;
}
