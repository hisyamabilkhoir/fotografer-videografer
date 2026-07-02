/* ============================================
   ABYNSS STUDIO — Scroll Animations
   GSAP + ScrollTrigger powered
   ============================================ */

import { prefersReducedMotion } from '../utils.js';

export function initScrollAnimations() {
  if (prefersReducedMotion()) {
    // Just show everything immediately
    document.querySelectorAll('[data-animate]').forEach(el => {
      el.classList.add('is-visible');
    });
    return;
  }

  // Check if GSAP is loaded
  if (typeof gsap !== 'undefined' && typeof ScrollTrigger !== 'undefined') {
    gsap.registerPlugin(ScrollTrigger);
    initGSAPAnimations();
  } else {
    // Fallback: Intersection Observer
    initObserverAnimations();
  }
}

function initGSAPAnimations() {
  // ---- Page Hero Entrance Animation (Immediate on Load) ----
  const hero = document.querySelector('.page-hero');
  if (hero) {
    const breadcrumb = hero.querySelector('.breadcrumb');
    const overline = hero.querySelector('.overline');
    const title = hero.querySelector('h1[data-split]');
    const desc = hero.querySelector('p');

    const heroTl = gsap.timeline();

    if (breadcrumb) {
      gsap.set(breadcrumb, { opacity: 0 });
      heroTl.fromTo(breadcrumb, { y: 15, opacity: 0 }, { y: 0, opacity: 1, duration: 0.5, ease: 'power2.out' });
    }
    if (overline) {
      gsap.set(overline, { opacity: 0 });
      heroTl.fromTo(overline, { y: 15, opacity: 0 }, { y: 0, opacity: 1, duration: 0.5, ease: 'power2.out' }, '-=0.35');
    }
    if (title) {
      gsap.set(title, { opacity: 0 });
      heroTl.fromTo(title, { y: 15, opacity: 0 }, { y: 0, opacity: 1, duration: 0.7, ease: 'power3.out' }, '-=0.35');
    }
    if (desc) {
      gsap.set(desc, { opacity: 0 });
      heroTl.fromTo(desc, { y: 15, opacity: 0 }, { y: 0, opacity: 1, duration: 0.5, ease: 'power2.out' }, '-=0.35');
    }
  }

  // ---- Grid items stagger entrance (Immediate on Load) ----
  const gridItems = gsap.utils.toArray('.masonry-grid .masonry-item-wrapper, .gallery-grid .gallery-item, #activities-grid .article-card');
  if (gridItems.length > 0) {
    gsap.fromTo(gridItems, 
      { y: 25, opacity: 0 },
      { y: 0, opacity: 1, duration: 0.6, stagger: 0.04, ease: 'power3.out' }
    );
  }

  // ---- Fade Up elements ----
  gsap.utils.toArray('[data-animate="fade-up"]:not(.masonry-item-wrapper):not(.gallery-item):not(#activities-grid .article-card):not(.pricing-card):not(.addon-card)').forEach((el, i) => {
    const delay = el.dataset.delay ? parseFloat(el.dataset.delay) * 0.1 : 0;
    gsap.fromTo(el, 
      { y: 40, opacity: 0 },
      {
        y: 0,
        opacity: 1,
        duration: 0.8,
        delay: delay,
        ease: 'power3.out',
        scrollTrigger: {
          trigger: el,
          start: 'top 85%',
          toggleActions: 'play none none none'
        }
      }
    );
  });

  // ---- Fade elements ----
  gsap.utils.toArray('[data-animate="fade"]').forEach(el => {
    const delay = el.dataset.delay ? parseFloat(el.dataset.delay) * 0.1 : 0;
    gsap.fromTo(el, 
      { opacity: 0 },
      {
        opacity: 1,
        duration: 0.8,
        delay: delay,
        ease: 'power2.out',
        scrollTrigger: {
          trigger: el,
          start: 'top 85%',
          toggleActions: 'play none none none'
        }
      }
    );
  });

  // ---- Fade Left ----
  gsap.utils.toArray('[data-animate="fade-left"]').forEach(el => {
    gsap.fromTo(el, 
      { x: -40, opacity: 0 },
      {
        x: 0,
        opacity: 1,
        duration: 0.8,
        ease: 'power3.out',
        scrollTrigger: {
          trigger: el,
          start: 'top 85%',
          toggleActions: 'play none none none'
        }
      }
    );
  });

  // ---- Fade Right ----
  gsap.utils.toArray('[data-animate="fade-right"]').forEach(el => {
    gsap.fromTo(el, 
      { x: 40, opacity: 0 },
      {
        x: 0,
        opacity: 1,
        duration: 0.8,
        ease: 'power3.out',
        scrollTrigger: {
          trigger: el,
          start: 'top 85%',
          toggleActions: 'play none none none'
        }
      }
    );
  });

  // ---- Scale ----
  gsap.utils.toArray('[data-animate="scale"]').forEach(el => {
    gsap.fromTo(el, 
      { scale: 0.9, opacity: 0 },
      {
        scale: 1,
        opacity: 1,
        duration: 0.8,
        ease: 'power3.out',
        scrollTrigger: {
          trigger: el,
          start: 'top 85%',
          toggleActions: 'play none none none'
        }
      }
    );
  });

  // ---- Reveal (clip-path) ----
  gsap.utils.toArray('[data-animate="reveal"]').forEach(el => {
    gsap.fromTo(el, 
      { clipPath: 'inset(0 100% 0 0)' },
      {
        clipPath: 'inset(0 0 0 0)',
        duration: 1,
        ease: 'power3.inOut',
        scrollTrigger: {
          trigger: el,
          start: 'top 85%',
          toggleActions: 'play none none none'
        }
      }
    );
  });

  // ---- Staggered children ----
  gsap.utils.toArray('[data-animate-children]').forEach(parent => {
    const children = Array.from(parent.children);
    if (!children.length) return;
    gsap.fromTo(children, 
      { y: 30, opacity: 0 },
      {
        y: 0,
        opacity: 1,
        duration: 0.6,
        stagger: 0.1,
        ease: 'power3.out',
        scrollTrigger: {
          trigger: parent,
          start: 'top 85%',
          toggleActions: 'play none none none'
        }
      }
    );
  });

  // ---- Split text animation ----
  if (typeof SplitType !== 'undefined') {
    gsap.utils.toArray('[data-split]:not(.page-hero [data-split])').forEach(el => {
      const split = new SplitType(el, { types: 'words,chars' });
      if (!split.chars || !split.chars.length) return;
      gsap.fromTo(split.chars, 
        { y: 20, opacity: 0 },
        {
          y: 0,
          opacity: 1,
          duration: 0.5,
          stagger: 0.02,
          ease: 'power3.out',
          scrollTrigger: {
            trigger: el,
            start: 'top 85%',
            toggleActions: 'play none none none'
          }
        }
      );
    });
  }

  // ---- Parallax images ----
  gsap.utils.toArray('[data-parallax]').forEach(el => {
    const speed = parseFloat(el.dataset.parallax) || 0.3;
    gsap.to(el, {
      y: () => -(ScrollTrigger.maxScroll(window) * speed * 0.1),
      ease: 'none',
      scrollTrigger: {
        trigger: el.parentElement || el,
        start: 'top bottom',
        end: 'bottom top',
        scrub: true
      }
    });
  });

  // ---- Section headers ----
  gsap.utils.toArray('.section-header').forEach(header => {
    const overline = header.querySelector('.overline');
    const heading = header.querySelector('h2');
    const desc = header.querySelector('p');

    const tl = gsap.timeline({
      scrollTrigger: {
        trigger: header,
        start: 'top 85%',
        toggleActions: 'play none none none'
      }
    });

    if (overline) tl.fromTo(overline, { y: 20, opacity: 0 }, { y: 0, opacity: 1, duration: 0.5 });
    if (heading) tl.fromTo(heading, { y: 20, opacity: 0 }, { y: 0, opacity: 1, duration: 0.6 }, '-=0.3');
    if (desc) tl.fromTo(desc, { y: 20, opacity: 0 }, { y: 0, opacity: 1, duration: 0.5 }, '-=0.3');
  });
}

/**
 * Fallback: Intersection Observer for browsers without GSAP
 */
function initObserverAnimations() {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('is-visible');
        observer.unobserve(entry.target);
      }
    });
  }, {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
  });

  document.querySelectorAll('[data-animate]').forEach(el => {
    observer.observe(el);
  });
}
