/* ============================================
   ABYNSS STUDIO — Home Page Logic
   ============================================ */

import { fetchData, formatDate, getBasePath, whatsappUrl, resolvePath } from '../utils.js';
import { initThreeBackground } from '../core/three-bg.js';

export async function initHomePage() {
  // Initialize Three.js background on hero
  initThreeBackground('three-bg');

  // Load data and populate sections
  const [siteData, projectsData, servicesData, articlesData, activitiesData, testimonialsData] = await Promise.all([
    fetchData('site'),
    fetchData('projects'),
    fetchData('services'),
    fetchData('articles'),
    fetchData('activities'),
    fetchData('testimonials')
  ]);

  if (siteData) {
    populateStats(siteData.stats);
  }
  if (projectsData) {
    populateFeaturedProjects(projectsData.projects.filter(p => p.featured));
  }
  if (servicesData) {
    populateServicesPreview(servicesData.services.slice(0, 4));
  }
  if (articlesData) {
    populateArticlesPreview(articlesData.articles.slice(0, 3));
  }
  if (activitiesData) {
    populateActivitiesPreview(activitiesData.activities.slice(0, 3));
  }
  if (testimonialsData) {
    populateTestimonials(testimonialsData.testimonials);
  }

  // Hero animation after content loads
  animateHero();

  // Signal that dynamic content is populated
  document.dispatchEvent(new CustomEvent('contentReady'));
}

function animateHero() {
  if (typeof gsap === 'undefined') return;

  const tl = gsap.timeline({ delay: 0.2 });

  tl.to('.hero-label', { opacity: 1, y: 0, duration: 0.6, ease: 'power3.out' })
    .to('.hero-title', { opacity: 1, y: 0, duration: 0.8, ease: 'power3.out' }, '-=0.3')
    .to('.hero-subtitle', { opacity: 1, y: 0, duration: 0.6, ease: 'power3.out' }, '-=0.4')
    .to('.hero-cta-group', { opacity: 1, y: 0, duration: 0.5, ease: 'power3.out' }, '-=0.3')
    .to('.hero-scroll-indicator', { opacity: 1, duration: 0.5 }, '-=0.2');

  // Set initial states
  gsap.set(['.hero-label', '.hero-title', '.hero-subtitle', '.hero-cta-group'], {
    y: 30
  });
}

function populateStats(stats) {
  const container = document.getElementById('stats-container');
  if (!container || !stats) return;

  container.innerHTML = stats.map(stat => `
    <div class="stat-item" data-animate="fade-up">
      <div class="stat-number" data-counter="${stat.number}" data-suffix="${stat.suffix}">${stat.number}${stat.suffix}</div>
      <div class="stat-label">${stat.label}</div>
    </div>
  `).join('');
}

function populateFeaturedProjects(projects) {
  const container = document.getElementById('featured-container');
  if (!container || !projects.length) return;

  const basePath = getBasePath();

  container.innerHTML = projects.slice(0, 5).map(project => `
    <a href="${basePath}/portfolio/${project.slug}/" class="featured-card" data-animate="fade-up" data-tilt>
      <img src="${resolvePath(project.cover)}" alt="${project.title}" loading="lazy">
      <div class="featured-card-overlay">
        <span class="featured-card-category">${project.category}</span>
        <h3 class="featured-card-title">${project.title}</h3>
      </div>
    </a>
  `).join('');
}

function populateServicesPreview(services) {
  const container = document.getElementById('services-preview-container');
  if (!container || !services.length) return;

  const basePath = getBasePath();

  container.innerHTML = services.map(service => `
    <a href="${basePath}/services/" class="service-preview-card" data-animate="fade-up">
      <img src="${resolvePath(service.cover)}" alt="${service.title}" loading="lazy">
      <div class="service-preview-content">
        <h3>${service.title}</h3>
        <p>${service.subtitle}</p>
      </div>
    </a>
  `).join('');
}

function populateArticlesPreview(articles) {
  const container = document.getElementById('articles-preview-container');
  if (!container || !articles.length) return;

  const basePath = getBasePath();

  container.innerHTML = articles.map(article => `
    <a href="${basePath}/articles/${article.slug}/" class="article-preview-card" data-animate="fade-up">
      <div class="article-preview-img">
        <img src="${resolvePath(article.cover)}" alt="${article.title}" loading="lazy">
      </div>
      <div class="article-preview-body">
        <div class="article-preview-meta">
          <span>${article.category}</span>
          <span>${formatDate(article.date)}</span>
        </div>
        <h3>${article.title}</h3>
        <p>${article.excerpt}</p>
      </div>
    </a>
  `).join('');
}

function populateActivitiesPreview(activities) {
  const container = document.getElementById('activities-preview-container');
  if (!container || !activities.length) return;

  const basePath = getBasePath();

  container.innerHTML = activities.map(activity => `
    <a href="${basePath}/activities/${activity.slug}/" class="article-preview-card" data-animate="fade-up">
      <div class="article-preview-img">
        <img src="${resolvePath(activity.cover)}" alt="${activity.title}" loading="lazy">
      </div>
      <div class="article-preview-body">
        <div class="article-preview-meta">
          <span>${activity.category}</span>
          <span>${formatDate(activity.date)}</span>
        </div>
        <h3>${activity.title}</h3>
        <p>${activity.excerpt}</p>
      </div>
    </a>
  `).join('');
}

function populateTestimonials(testimonials) {
  const container = document.getElementById('testimonials-container');
  if (!container || !testimonials.length) return;

  // Add event listener for avatar fallback (once only)
  if (!container.dataset.hasErrorListener) {
    container.addEventListener('error', (e) => {
      if (e.target.tagName === 'IMG' && e.target.classList.contains('testimonial-avatar')) {
        const name = e.target.alt || 'A';
        const initial = name.charAt(0).toUpperCase();
        e.target.src = `data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='56' height='56'%3E%3Crect fill='%23181818' width='56' height='56' rx='28'/%3E%3Ctext x='28' y='33' text-anchor='middle' fill='%23C7A66A' font-size='18' font-weight='bold'%3E${initial}%3C/text%3E%3C/svg%3E`;
      }
    }, true);
    container.dataset.hasErrorListener = 'true';
  }

  let currentIndex = 0;

  function showTestimonial(index) {
    const t = testimonials[index];
    container.innerHTML = `
      <div class="testimonial-card" style="opacity: 0;">
        <div class="testimonial-quote">${t.quote}</div>
        <div class="testimonial-author">
          <img src="${resolvePath(t.avatar)}" alt="${t.name}" class="testimonial-avatar" loading="lazy">
          <div>
            <div class="testimonial-name">${t.name}</div>
            <div class="testimonial-role">${t.role} — ${t.company}</div>
          </div>
        </div>
      </div>
    `;

    const card = container.querySelector('.testimonial-card');
    if (card) {
      if (typeof gsap !== 'undefined') {
        gsap.fromTo(card, 
          { opacity: 0, y: 15 },
          { opacity: 1, y: 0, duration: 0.6, ease: 'power2.out' }
        );
      } else {
        card.style.opacity = '1';
      }
    }
  }

  showTestimonial(0);

  // Auto-rotate every 5 seconds
  setInterval(() => {
    currentIndex = (currentIndex + 1) % testimonials.length;
    showTestimonial(currentIndex);
  }, 5000);
}
