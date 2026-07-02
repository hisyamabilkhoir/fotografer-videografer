/* ============================================
   ABYNSS STUDIO — Lightbox Component
   Premium fullscreen image/video viewer
   ============================================ */

export function initLightbox() {
  // Create lightbox element if it doesn't exist
  let lightbox = document.querySelector('.lightbox');
  if (!lightbox) {
    lightbox = document.createElement('div');
    lightbox.className = 'lightbox';
    lightbox.innerHTML = `
      <button class="lightbox-close" aria-label="Tutup">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <line x1="18" y1="6" x2="6" y2="18"></line>
          <line x1="6" y1="6" x2="18" y2="18"></line>
        </svg>
      </button>
      <button class="lightbox-nav lightbox-prev" aria-label="Sebelumnya">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <polyline points="15 18 9 12 15 6"></polyline>
        </svg>
      </button>
      <button class="lightbox-nav lightbox-next" aria-label="Selanjutnya">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <polyline points="9 18 15 12 9 6"></polyline>
        </svg>
      </button>
      <img class="lightbox-img" src="" alt="">
      <div class="lightbox-counter"></div>
    `;
    document.body.appendChild(lightbox);
  }

  const closeBtn = lightbox.querySelector('.lightbox-close');
  const prevBtn = lightbox.querySelector('.lightbox-prev');
  const nextBtn = lightbox.querySelector('.lightbox-next');
  const img = lightbox.querySelector('.lightbox-img');
  const counter = lightbox.querySelector('.lightbox-counter');

  let currentImages = [];
  let currentIndex = 0;

  // Open lightbox
  function open(images, index = 0) {
    currentImages = images;
    currentIndex = index;
    showImage();
    lightbox.classList.add('active');
    document.body.style.overflow = 'hidden';
  }

  // Close lightbox
  function close() {
    lightbox.classList.remove('active');
    document.body.style.overflow = '';
  }

  // Show current image
  function showImage() {
    if (!currentImages.length) return;
    const src = typeof currentImages[currentIndex] === 'string' 
      ? currentImages[currentIndex] 
      : currentImages[currentIndex].src;
    img.src = src;
    img.alt = `Foto ${currentIndex + 1}`;
    counter.textContent = `${currentIndex + 1} / ${currentImages.length}`;

    // Hide nav if single image
    prevBtn.style.display = currentImages.length > 1 ? '' : 'none';
    nextBtn.style.display = currentImages.length > 1 ? '' : 'none';
  }

  // Navigation
  function next() {
    currentIndex = (currentIndex + 1) % currentImages.length;
    showImage();
  }

  function prev() {
    currentIndex = (currentIndex - 1 + currentImages.length) % currentImages.length;
    showImage();
  }

  // Event listeners
  closeBtn.addEventListener('click', close);
  prevBtn.addEventListener('click', prev);
  nextBtn.addEventListener('click', next);

  // Close on background click
  lightbox.addEventListener('click', (e) => {
    if (e.target === lightbox) close();
  });

  // Keyboard navigation
  document.addEventListener('keydown', (e) => {
    if (!lightbox.classList.contains('active')) return;
    if (e.key === 'Escape') close();
    if (e.key === 'ArrowLeft') prev();
    if (e.key === 'ArrowRight') next();
  });

  // Touch swipe support
  let touchStartX = 0;
  lightbox.addEventListener('touchstart', (e) => {
    touchStartX = e.changedTouches[0].screenX;
  }, { passive: true });

  lightbox.addEventListener('touchend', (e) => {
    const touchEndX = e.changedTouches[0].screenX;
    const diff = touchStartX - touchEndX;
    if (Math.abs(diff) > 50) {
      if (diff > 0) next();
      else prev();
    }
  }, { passive: true });

  // Make open function globally available
  window.openLightbox = open;

  // Auto-bind to [data-lightbox] elements
  document.querySelectorAll('[data-lightbox]').forEach(el => {
    el.addEventListener('click', () => {
      const group = el.dataset.lightbox;
      const items = document.querySelectorAll(`[data-lightbox="${group}"]`);
      const images = Array.from(items).map(item => item.dataset.src || item.querySelector('img')?.src || item.href);
      const index = Array.from(items).indexOf(el);
      open(images, index);
    });
  });

  return { open, close, next, prev };
}
