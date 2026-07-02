import os
import json
import re
from datetime import datetime

# ============================================
# ABYNSS STUDIO — Static Detail Pages Generator
# Python script to generate HTML files for
# portfolio projects, blog articles, and activities.
# ============================================

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

# Helper to format dates
def get_date_string(date_str):
    try:
        dt = datetime.strptime(date_str, "%Y-%m-%d")
        months = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 
                  'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
        return f"{dt.day} {months[dt.month - 1]} {dt.year}"
    except Exception:
        return date_str

# Helper to map absolute path variables to relative paths
def get_relative_path(path):
    if path and path.startswith("/"):
        return "../../" + path[1:]
    return path

# Shared Navigation and Footer markup
# Navigation and Footer markups (Separate per page type for absolute consistency & correct paths)
PROJECT_HEADER_HTML = """  <nav class="navbar" role="navigation"><div class="container navbar-inner">
    <a href="../../" class="navbar-logo">ABYNSS <span>STUDIO</span></a>
    <div class="navbar-links">
      <a href="../../" class="navbar-link">Beranda</a><a href="../../about/" class="navbar-link">Tentang</a><a href="../../portfolio/" class="navbar-link active">Portfolio</a><a href="../../gallery/" class="navbar-link">Galeri</a><a href="../../services/" class="navbar-link">Layanan</a><a href="../../pricing/" class="navbar-link">Harga</a><a href="../../articles/" class="navbar-link">Artikel</a><a href="../../contact/" class="navbar-link">Kontak</a>
    </div>
    <a href="../../contact/" class="btn btn-primary btn-sm navbar-cta hide-below-desktop">Hubungi Kami</a>
    <div class="hamburger" aria-label="Menu" role="button" tabindex="0"><span></span><span></span><span></span></div>
  </div></nav>
  <div class="mobile-menu"><a href="../../" class="mobile-menu-link">Beranda</a><a href="../../about/" class="mobile-menu-link">Tentang</a><a href="../../portfolio/" class="mobile-menu-link">Portfolio</a><a href="../../contact/" class="mobile-menu-link">Kontak</a></div>"""

ARTICLE_HEADER_HTML = """  <nav class="navbar" role="navigation"><div class="container navbar-inner">
    <a href="../../" class="navbar-logo">ABYNSS <span>STUDIO</span></a>
    <div class="navbar-links">
      <a href="../../" class="navbar-link">Beranda</a><a href="../../about/" class="navbar-link">Tentang</a><a href="../../portfolio/" class="navbar-link">Portfolio</a><a href="../../gallery/" class="navbar-link">Galeri</a><a href="../../services/" class="navbar-link">Layanan</a><a href="../../pricing/" class="navbar-link">Harga</a><a href="../../articles/" class="navbar-link active">Artikel</a><a href="../../contact/" class="navbar-link">Kontak</a>
    </div>
    <a href="../../contact/" class="btn btn-primary btn-sm navbar-cta hide-below-desktop">Hubungi Kami</a>
    <div class="hamburger" aria-label="Menu" role="button" tabindex="0"><span></span><span></span><span></span></div>
  </div></nav>
  <div class="mobile-menu"><a href="../../" class="mobile-menu-link">Beranda</a><a href="../../about/" class="mobile-menu-link">Tentang</a><a href="../../articles/" class="mobile-menu-link">Artikel</a><a href="../../contact/" class="mobile-menu-link">Kontak</a></div>"""

ACTIVITY_HEADER_HTML = """  <nav class="navbar" role="navigation"><div class="container navbar-inner">
    <a href="../../" class="navbar-logo">ABYNSS <span>STUDIO</span></a>
    <div class="navbar-links">
      <a href="../../" class="navbar-link">Beranda</a><a href="../../about/" class="navbar-link">Tentang</a><a href="../../portfolio/" class="navbar-link">Portfolio</a><a href="../../gallery/" class="navbar-link">Galeri</a><a href="../../services/" class="navbar-link">Layanan</a><a href="../../pricing/" class="navbar-link">Harga</a><a href="../../articles/" class="navbar-link">Artikel</a><a href="../../contact/" class="navbar-link">Kontak</a>
    </div>
    <a href="../../contact/" class="btn btn-primary btn-sm navbar-cta hide-below-desktop">Hubungi Kami</a>
    <div class="hamburger" aria-label="Menu" role="button" tabindex="0"><span></span><span></span><span></span></div>
  </div></nav>
  <div class="mobile-menu"><a href="../../" class="mobile-menu-link">Beranda</a><a href="../../about/" class="mobile-menu-link">Tentang</a><a href="../../gallery/" class="mobile-menu-link">Galeri</a><a href="../../contact/" class="mobile-menu-link">Kontak</a></div>"""

FOOTER_HTML = """  <!-- ========== FOOTER ========== -->
  <footer class="footer" role="contentinfo">
    <div class="container">
      <div class="footer-grid">
        <!-- Brand -->
        <div class="footer-brand">
          <div class="footer-brand-name">ABYNSS <span>STUDIO</span></div>
          <p>Studio fotografi & videografi profesional yang menghadirkan pengalaman visual sinematik kelas dunia. Momen terbaik Anda, kualitas terbaik kami.</p>
          <div class="footer-social">
            <a href="https://instagram.com/abynsstudio" target="_blank" rel="noopener" class="footer-social-link" aria-label="Instagram">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><rect x="2" y="2" width="20" height="20" rx="5"/><circle cx="12" cy="12" r="5"/><circle cx="17.5" cy="6.5" r="1.5" fill="currentColor" stroke="none"/></svg>
            </a>
            <a href="https://tiktok.com/@abynsstudio" target="_blank" rel="noopener" class="footer-social-link" aria-label="TikTok">
              <svg viewBox="0 0 24 24" fill="currentColor"><path d="M19.59 6.69a4.83 4.83 0 01-3.77-4.25V2h-3.45v13.67a2.89 2.89 0 01-2.88 2.5 2.89 2.89 0 01-2.89-2.89 2.89 2.89 0 012.89-2.89c.28 0 .54.04.79.1v-3.5a6.37 6.37 0 00-.79-.05A6.34 6.34 0 003.15 15.2a6.34 6.34 0 006.34 6.34 6.34 6.34 0 006.34-6.34V9.17a8.16 8.16 0 003.76.92V6.69z"/></svg>
            </a>
            <a href="https://youtube.com/@abynsstudio" target="_blank" rel="noopener" class="footer-social-link" aria-label="YouTube">
              <svg viewBox="0 0 24 24" fill="currentColor"><path d="M23.498 6.186a3.016 3.016 0 00-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 00.502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 002.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 002.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/></svg>
            </a>
          </div>
        </div>

        <!-- Navigation -->
        <div>
          <h4 class="footer-heading">Navigasi</h4>
          <a href="../../" class="footer-link">Beranda</a>
          <a href="../../about/" class="footer-link">Tentang Kami</a>
          <a href="../../portfolio/" class="footer-link">Portfolio</a>
          <a href="../../gallery/" class="footer-link">Galeri</a>
          <a href="../../services/" class="footer-link">Layanan</a>
          <a href="../../pricing/" class="footer-link">Harga</a>
        </div>

        <!-- More Links -->
        <div>
          <h4 class="footer-heading">Lainnya</h4>
          <a href="../../articles/" class="footer-link">Artikel</a>
          <a href="../../activities/" class="footer-link">Aktivitas</a>
          <a href="../../testimonials/" class="footer-link">Testimoni</a>
          <a href="../../faq/" class="footer-link">FAQ</a>
          <a href="../../contact/" class="footer-link">Kontak</a>
          <a href="../../privacy/" class="footer-link">Kebijakan Privasi</a>
        </div>

        <!-- Newsletter -->
        <div>
          <h4 class="footer-heading">Newsletter</h4>
          <p class="caption" style="margin-bottom: var(--space-sm);">Dapatkan tips fotografi dan promo eksklusif langsung ke email Anda</p>
          <div class="footer-newsletter">
            <form class="footer-newsletter-form" onsubmit="event.preventDefault(); alert('Terima kasih telah berlangganan!');">
              <input type="email" class="footer-newsletter-input" placeholder="Email Anda" required>
              <button type="submit" class="footer-newsletter-btn">Kirim</button>
            </form>
          </div>
        </div>
      </div>

      <div class="footer-bottom">
        <p class="footer-copy">&copy; 2024 ABYNSS STUDIO. Seluruh hak cipta dilindungi.</p>
        <div class="footer-bottom-links">
          <a href="../../privacy/" class="footer-bottom-link">Kebijakan Privasi</a>
          <a href="../../faq/" class="footer-bottom-link">FAQ</a>
        </div>
      </div>
    </div>
  </footer>"""

# ----------------------------------------------------
# TEMPLATE 1: PORTFOLIO/PROJECT DETAIL
# ----------------------------------------------------
PROJECT_TEMPLATE = """<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{{TITLE}} — ABYNSS STUDIO</title>
  <meta name="description" content="{{SUBTITLE}}. Detail proyek, cerita, tantangan, dan solusi visual dari ABYNSS Studio.">
  <link rel="canonical" href="https://abynsstudio.com/portfolio/{{SLUG}}/">
  <meta property="og:title" content="{{TITLE}} — ABYNSS STUDIO">
  <meta property="og:description" content="{{SUBTITLE}}">
  <meta property="og:image" content="{{COVER}}">
  <meta property="og:url" content="https://abynsstudio.com/portfolio/{{SLUG}}/">
  <link rel="stylesheet" href="../../assets/css/main.css?v=2.2">
  <link rel="stylesheet" href="../../assets/css/pages/portfolio.css?v=2.2">
  <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect fill='%230D0D0D' width='32' height='32' rx='8'/%3E%3Ctext x='16' y='22' text-anchor='middle' fill='%23C7A66A' font-family='serif' font-size='18' font-weight='bold'%3EA%3C/text%3E%3C/svg%3E">
</head>
<body class="loading noise-overlay">
  <div id="loader"><div class="loader-logo">ABYNSS <span>STUDIO</span></div><div class="loader-bar-track"><div class="loader-bar"></div></div><div class="loader-percent">0%</div></div>
  <div class="scroll-progress"><div class="scroll-progress-bar"></div></div>

  {{HEADER}}

  <main>
    <!-- Project Hero -->
    <section class="project-hero">
      <img src="{{COVER}}" alt="{{TITLE}}">
      <div class="project-hero-overlay"></div>
      <div class="project-hero-content">
        <div class="breadcrumb" style="justify-content:center;"><a href="../../">Beranda</a><span class="separator">/</span><a href="../">Portfolio</a><span class="separator">/</span><span class="current">{{TITLE}}</span></div>
        <span class="overline" style="color:var(--accent);"><span class="accent-dot"></span>Proyek {{CATEGORY}}</span>
        <h1 data-split>{{TITLE}}</h1>
        <p class="body-lg">{{SUBTITLE}}</p>
      </div>
    </section>

    <!-- Project Info Details -->
    <section class="section">
      <div class="container">
        <div class="project-details-layout">
          <!-- Main Story -->
          <div class="project-main-story" data-animate="fade-right">
            <span class="overline">Cerita Proyek</span>
            <h2>Konsep & Visi</h2>
            <p>{{STORY}}</p>

            <div class="project-challenge-grid mt-xl">
              <div class="challenge-box">
                <h4>⚠️ Tantangan</h4>
                <p>{{CHALLENGE}}</p>
              </div>
              <div class="solution-box">
                <h4>💡 Solusi</h4>
                <p>{{SOLUTION}}</p>
              </div>
            </div>

            <div class="result-box mt-lg">
              <h4>🏆 Hasil</h4>
              <p>{{RESULT}}</p>
            </div>
          </div>

          <!-- Sidebar Metadata -->
          <div class="project-meta-sidebar" data-animate="fade-left">
            <div class="meta-sidebar-widget">
              <h4>Detail Informasi</h4>
              <div class="meta-item"><span>Klien</span><strong>{{CLIENT}}</strong></div>
              <div class="meta-item"><span>Tanggal</span><strong>{{DATE}}</strong></div>
              <div class="meta-item"><span>Lokasi</span><strong>{{LOCATION}}</strong></div>
              <div class="meta-item"><span>Peralatan</span><strong>{{EQUIPMENT}}</strong></div>
              <div class="meta-item"><span>Kategori</span><strong style="text-transform:capitalize;">{{CATEGORY}}</strong></div>
            </div>
            <a href="../../contact/?interest={{TITLE}}" class="btn btn-primary w-full mt-lg">Tanyakan Proyek Serupa</a>
          </div>
        </div>
      </div>
    </section>

    <!-- Media Section -->
    <section class="section" style="background:var(--bg-secondary);">
      <div class="container">
        <div class="section-header">
          <span class="overline">Media Proyek</span>
          <h2>Dokumentasi Visual</h2>
        </div>
        
        {{VIDEO_EMBED}}

        <div class="masonry-grid mt-xl" data-animate-children>
          {{GALLERY_IMAGES}}
        </div>
      </div>
    </section>

    <!-- Related Projects -->
    <section class="section">
      <div class="container">
        <div class="section-header">
          <span class="overline">Lihat Lainnya</span>
          <h2>Proyek Terkait</h2>
        </div>
        <div class="featured-grid" id="related-projects-container" data-animate-children>
          <!-- Populated by JS dynamic fallback -->
        </div>
      </div>
    </section>
  </main>

  {{FOOTER}}

  <a class="whatsapp-float" href="https://wa.me/6285973729267" target="_blank" rel="noopener"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg></a>
  <button class="back-to-top" aria-label="Kembali ke atas"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="18 15 12 9 6 15"></polyline></svg></button>

  <script src="https://cdn.jsdelivr.net/npm/gsap@3.12.5/dist/gsap.min.js" defer></script>
  <script src="https://cdn.jsdelivr.net/npm/gsap@3.12.5/dist/ScrollTrigger.min.js" defer></script>
  <script src="https://unpkg.com/lenis@1.1.18/dist/lenis.min.js" defer></script>
  <script src="https://unpkg.com/split-type@0.3.4/umd/index.min.js" defer></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/vanilla-tilt/1.8.1/vanilla-tilt.min.js" defer></script>
  <script type="module" src="../../assets/js/app.js"></script>

  <script type="module">
    import { fetchData, getBasePath } from '../../assets/js/utils.js';
    import { initTilts } from '../../assets/js/components/tilt.js';

    document.addEventListener('loaderComplete', async () => {
      const data = await fetchData('projects');
      if (!data) return;

      const container = document.getElementById('related-projects-container');
      const basePath = getBasePath();
      const currentCategory = "{{CATEGORY}}";
      const currentSlug = "{{SLUG}}";

      const related = data.projects.filter(p => p.category === currentCategory && p.slug !== currentSlug).slice(0, 3);

      if (related.length) {
        container.innerHTML = related.map(p => `
          <a href="${basePath}/portfolio/${p.slug}/" class="featured-card" data-animate="fade-up" data-tilt>
            <img src="${basePath}${p.cover}" alt="${p.title}" loading="lazy">
            <div class="featured-card-overlay">
              <span class="featured-card-category">${p.category}</span>
              <h3 class="featured-card-title">${p.title}</h3>
            </div>
          </a>
        `).join('');
      } else {
        const fallback = data.projects.filter(p => p.slug !== currentSlug).slice(0, 3);
        container.innerHTML = fallback.map(p => `
          <a href="${basePath}/portfolio/${p.slug}/" class="featured-card" data-animate="fade-up" data-tilt>
            <img src="${basePath}${p.cover}" alt="${p.title}" loading="lazy">
            <div class="featured-card-overlay">
              <span class="featured-card-category">${p.category}</span>
              <h3 class="featured-card-title">${p.title}</h3>
            </div>
          </a>
        `).join('');
      }
      initTilts();
    });
  </script>
</body>
</html>"""

# ----------------------------------------------------
# TEMPLATE 2: ARTICLES/BLOG DETAIL
# ----------------------------------------------------
ARTICLE_TEMPLATE = """<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{{TITLE}} — ABYNSS STUDIO</title>
  <meta name="description" content="{{EXCERPT}}">
  <link rel="canonical" href="https://abynsstudio.com/articles/{{SLUG}}/">
  <meta property="og:title" content="Artikel: {{TITLE}} — ABYNSS STUDIO">
  <meta property="og:description" content="{{EXCERPT}}">
  <meta property="og:image" content="{{COVER}}">
  <meta property="og:url" content="https://abynsstudio.com/articles/{{SLUG}}/">
  <link rel="stylesheet" href="../../assets/css/main.css?v=2.2">
  <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect fill='%230D0D0D' width='32' height='32' rx='8'/%3E%3Ctext x='16' y='22' text-anchor='middle' fill='%23C7A66A' font-family='serif' font-size='18' font-weight='bold'%3EA%3C/text%3E%3C/svg%3E">
</head>
<body class="loading noise-overlay">
  <div id="loader"><div class="loader-logo">ABYNSS <span>STUDIO</span></div><div class="loader-bar-track"><div class="loader-bar"></div></div><div class="loader-percent">0%</div></div>
  <div class="scroll-progress"><div class="scroll-progress-bar"></div></div>

  {{HEADER}}

  <main>
    <!-- Article Hero -->
    <section class="project-hero">
      <img src="{{COVER}}" alt="{{TITLE}}">
      <div class="project-hero-overlay"></div>
      <div class="project-hero-content">
        <div class="breadcrumb" style="justify-content:center;"><a href="../../">Beranda</a><span class="separator">/</span><a href="../">Artikel</a><span class="separator">/</span><span class="current">{{TITLE}}</span></div>
        <span class="overline" style="color:var(--accent);"><span class="accent-dot"></span>{{CATEGORY}}</span>
        <h1 data-split>{{TITLE}}</h1>
        <p class="body-lg">Diterbitkan pada {{DATE}} • {{READING_TIME}} menit baca</p>
      </div>
    </section>

    <!-- Article Content -->
    <section class="section">
      <div class="container" style="max-width:800px; margin-inline:auto;">
        <!-- Author info -->
        <div class="article-author-info mb-xl" data-animate="fade-up" style="display:flex; align-items:center; gap:var(--space-md);">
          <img src="{{AUTHOR_AVATAR}}" alt="{{AUTHOR_NAME}}" class="author-avatar" style="width:48px; height:48px; border-radius:50%; object-fit:cover;"
               onerror="this.src='data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2248%22 height=%2248%22 rx=%2224%22%3E%3Crect fill=%22%23181818%22 width=%2248%22 height=%2248%22/%3E%3Ctext x=%2224%22 y=%2229%22 text-anchor=%22middle%22 fill=%22%23C7A66A%22 font-size=%2214%22%3EA%3C/text%3E%3C/svg%3E'">
          <div>
            <strong>Oleh {{AUTHOR_NAME}}</strong>
            <p class="caption" style="color:var(--text-muted); margin-bottom:0;">Tim Storyteller ABYNSS Studio</p>
          </div>
        </div>

        <div class="rich-text-content" data-animate="fade-up" style="line-height:var(--lh-relaxed); color:var(--text-secondary);">
          {{CONTENT_HTML}}
        </div>

        <!-- Tags -->
        <div class="article-tags mt-xl" data-animate="fade-up" style="display:flex; gap:var(--space-xs); flex-wrap:wrap;">
          {{TAGS}}
        </div>
      </div>
    </section>
  </main>

  {{FOOTER}}

  <a class="whatsapp-float" href="https://wa.me/6285973729267" target="_blank" rel="noopener"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg></a>
  <button class="back-to-top" aria-label="Kembali ke atas"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="18 15 12 9 6 15"></polyline></svg></button>

  <script src="https://cdn.jsdelivr.net/npm/gsap@3.12.5/dist/gsap.min.js" defer></script>
  <script src="https://cdn.jsdelivr.net/npm/gsap@3.12.5/dist/ScrollTrigger.min.js" defer></script>
  <script src="https://unpkg.com/lenis@1.1.18/dist/lenis.min.js" defer></script>
  <script src="https://unpkg.com/split-type@0.3.4/umd/index.min.js" defer></script>
  <script type="module" src="../../assets/js/app.js"></script>
</body>
</html>"""

# ----------------------------------------------------
# TEMPLATE 3: ACTIVITIES DETAIL
# ----------------------------------------------------
ACTIVITY_TEMPLATE = """<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{{TITLE}} — ABYNSS STUDIO</title>
  <meta name="description" content="{{EXCERPT}}">
  <link rel="canonical" href="https://abynsstudio.com/activities/{{SLUG}}/">
  <meta property="og:title" content="Aktivitas: {{TITLE}} — ABYNSS STUDIO">
  <meta property="og:description" content="{{EXCERPT}}">
  <meta property="og:image" content="{{COVER}}">
  <meta property="og:url" content="https://abynsstudio.com/activities/{{SLUG}}/">
  <link rel="stylesheet" href="../../assets/css/main.css?v=2.2">
  <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect fill='%230D0D0D' width='32' height='32' rx='8'/%3E%3Ctext x='16' y='22' text-anchor='middle' fill='%23C7A66A' font-family='serif' font-size='18' font-weight='bold'%3EA%3C/text%3E%3C/svg%3E">
</head>
<body class="loading noise-overlay">
  <div id="loader"><div class="loader-logo">ABYNSS <span>STUDIO</span></div><div class="loader-bar-track"><div class="loader-bar"></div></div><div class="loader-percent">0%</div></div>
  <div class="scroll-progress"><div class="scroll-progress-bar"></div></div>

  {{HEADER}}

  <main>
    <!-- Activity Hero -->
    <section class="project-hero">
      <img src="{{COVER}}" alt="{{TITLE}}">
      <div class="project-hero-overlay"></div>
      <div class="project-hero-content">
        <div class="breadcrumb" style="justify-content:center;"><a href="../../">Beranda</a><span class="separator">/</span><a href="../">Aktivitas</a><span class="separator">/</span><span class="current">{{TITLE}}</span></div>
        <span class="overline" style="color:var(--accent);"><span class="accent-dot"></span>{{CATEGORY}}</span>
        <h1 data-split>{{TITLE}}</h1>
        <p class="body-lg">{{DATE}} • {{LOCATION}}</p>
      </div>
    </section>

    <!-- Activity Content -->
    <section class="section">
      <div class="container" style="max-width:800px; margin-inline:auto;">
        <div class="rich-text-content" data-animate="fade-up">
          <p class="body-lg" style="color:var(--text-secondary); margin-bottom:var(--space-md); font-style:italic;">{{EXCERPT}}</p>
          {{CONTENT_HTML}}
        </div>

        <!-- Activity stats if any -->
        {{STATS}}
      </div>
    </section>

    <!-- Gallery of the activity -->
    <section class="section" style="background:var(--bg-secondary);">
      <div class="container">
        <div class="section-header">
          <span class="overline">Dokumentasi</span>
          <h2>Galeri Kegiatan</h2>
        </div>
        <div class="masonry-grid mt-xl" data-animate-children>
          {{GALLERY_IMAGES}}
        </div>
      </div>
    </section>
  </main>

  {{FOOTER}}

  <a class="whatsapp-float" href="https://wa.me/6285973729267" target="_blank" rel="noopener"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg></a>
  <button class="back-to-top" aria-label="Kembali ke atas"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="18 15 12 9 6 15"></polyline></svg></button>

  <script src="https://cdn.jsdelivr.net/npm/gsap@3.12.5/dist/gsap.min.js" defer></script>
  <script src="https://cdn.jsdelivr.net/npm/gsap@3.12.5/dist/ScrollTrigger.min.js" defer></script>
  <script src="https://unpkg.com/lenis@1.1.18/dist/lenis.min.js" defer></script>
  <script src="https://unpkg.com/split-type@0.3.4/umd/index.min.js" defer></script>
  <script type="module" src="../../assets/js/app.js"></script>
</body>
</html>"""

def parse_markdown_content(content_str):
    lines = content_str.split("\n")
    content_html = []
    in_list = False
    list_items = []

    for line in lines:
        line = line.strip()
        if not line:
            if in_list:
                content_html.append(f"<ul class='mb-md' style='padding-left:var(--space-md); list-style-type:disc;'>{''.join(list_items)}</ul>")
                list_items = []
                in_list = False
            continue

        if line.startswith("## "):
            if in_list:
                content_html.append(f"<ul class='mb-md' style='padding-left:var(--space-md); list-style-type:disc;'>{''.join(list_items)}</ul>")
                list_items = []
                in_list = False
            content_html.append(f'<h2 class="h3 mt-xl mb-md">{line[3:]}</h2>')
        elif line.startswith("# "):
            if in_list:
                content_html.append(f"<ul class='mb-md' style='padding-left:var(--space-md); list-style-type:disc;'>{''.join(list_items)}</ul>")
                list_items = []
                in_list = False
            content_html.append(f'<h2 class="h2 mt-2xl mb-md">{line[2:]}</h2>')
        elif line.startswith("- ") or line.startswith("* "):
            in_list = True
            list_items.append(f"<li>{line[2:]}</li>")
        else:
            if in_list:
                content_html.append(f"<ul class='mb-md' style='padding-left:var(--space-md); list-style-type:disc;'>{''.join(list_items)}</ul>")
                list_items = []
                in_list = False
            content_html.append(f"<p class='mb-md'>{line}</p>")

    if in_list:
        content_html.append(f"<ul class='mb-md' style='padding-left:var(--space-md); list-style-type:disc;'>{''.join(list_items)}</ul>")

    return "\n".join(content_html)

def generate_all():
    # 1. Projects
    with open(os.path.join(ROOT_DIR, "data", "projects.json"), 'r', encoding='utf-8') as f:
        projects_data = json.load(f)
        
    for p in projects_data["projects"]:
        slug = p["slug"]
        out_dir = os.path.join(ROOT_DIR, "portfolio", slug)
        os.makedirs(out_dir, exist_ok=True)
        
        html = PROJECT_TEMPLATE
        html = html.replace("{{TITLE}}", p["title"])
        html = html.replace("{{SUBTITLE}}", p["subtitle"])
        html = html.replace("{{SLUG}}", p["slug"])
        html = html.replace("{{COVER}}", get_relative_path(p["cover"]))
        html = html.replace("{{STORY}}", p["story"])
        html = html.replace("{{CHALLENGE}}", p["challenge"])
        html = html.replace("{{SOLUTION}}", p["solution"])
        html = html.replace("{{RESULT}}", p["result"])
        html = html.replace("{{CLIENT}}", p["client"])
        html = html.replace("{{DATE}}", get_date_string(p["date"]))
        html = html.replace("{{LOCATION}}", p["location"])
        html = html.replace("{{CATEGORY}}", p["category"])
        html = html.replace("{{EQUIPMENT}}", ", ".join(p["equipment"]))
        
        # Video embed
        if p.get("video"):
            video_html = f'<div class="project-video-wrapper mt-lg" data-animate="fade-up"><iframe src="{p["video"]}" allowfullscreen title="{p["title"]} Video"></iframe></div>'
            html = html.replace("{{VIDEO_EMBED}}", video_html)
        else:
            html = html.replace("{{VIDEO_EMBED}}", "")
            
        # Gallery Images
        imgs_html = []
        for img in p["images"]:
            rel_img = get_relative_path(img)
            imgs_html.append(f'<div class="masonry-item" data-lightbox="project-gallery" data-src="{rel_img}" data-animate="fade-up" style="cursor:pointer;"><img src="{rel_img}" alt="{p["title"]} Gallery Image" loading="lazy"></div>')
        html = html.replace("{{GALLERY_IMAGES}}", "\n".join(imgs_html))
        
        # Header / Footer
        html = html.replace("{{HEADER}}", PROJECT_HEADER_HTML)
        html = html.replace("{{FOOTER}}", FOOTER_HTML)
        
        # Write file with proper UTF-8 encoding (non-BOM)
        with open(os.path.join(out_dir, "index.html"), 'w', encoding='utf-8') as out_f:
            out_f.write(html)
        print(f"Generated portfolio project: {slug}")

    # 2. Articles
    with open(os.path.join(ROOT_DIR, "data", "articles.json"), 'r', encoding='utf-8') as f:
        articles_data = json.load(f)
        
    for a in articles_data["articles"]:
        slug = a["slug"]
        out_dir = os.path.join(ROOT_DIR, "articles", slug)
        os.makedirs(out_dir, exist_ok=True)
        
        html = ARTICLE_TEMPLATE
        html = html.replace("{{TITLE}}", a["title"])
        html = html.replace("{{EXCERPT}}", a["excerpt"])
        html = html.replace("{{SLUG}}", a["slug"])
        html = html.replace("{{COVER}}", get_relative_path(a["cover"]))
        html = html.replace("{{CATEGORY}}", a["category"])
        html = html.replace("{{DATE}}", get_date_string(a["date"]))
        html = html.replace("{{READING_TIME}}", str(a["reading_time"]))
        html = html.replace("{{AUTHOR_NAME}}", a["author"]["name"])
        html = html.replace("{{AUTHOR_AVATAR}}", get_relative_path(a["author"]["avatar"]))
        
        # Parse content properly
        parsed_content = parse_markdown_content(a["content"])
        html = html.replace("{{CONTENT_HTML}}", parsed_content)
        
        # Tags
        tags_html = []
        for tag in a["tags"]:
            tags_html.append(f'<span class="badge badge-outline">#{tag}</span>')
        html = html.replace("{{TAGS}}", " ".join(tags_html))
        
        # Header / Footer
        html = html.replace("{{HEADER}}", ARTICLE_HEADER_HTML)
        html = html.replace("{{FOOTER}}", FOOTER_HTML)
        
        with open(os.path.join(out_dir, "index.html"), 'w', encoding='utf-8') as out_f:
            out_f.write(html)
        print(f"Generated article: {slug}")

    # 3. Activities
    with open(os.path.join(ROOT_DIR, "data", "activities.json"), 'r', encoding='utf-8') as f:
        activities_data = json.load(f)
        
    for ac in activities_data["activities"]:
        slug = ac["slug"]
        out_dir = os.path.join(ROOT_DIR, "activities", slug)
        os.makedirs(out_dir, exist_ok=True)
        
        html = ACTIVITY_TEMPLATE
        html = html.replace("{{TITLE}}", ac["title"])
        html = html.replace("{{EXCERPT}}", ac["excerpt"])
        html = html.replace("{{SLUG}}", ac["slug"])
        html = html.replace("{{COVER}}", get_relative_path(ac["cover"]))
        html = html.replace("{{CATEGORY}}", ac["category"])
        html = html.replace("{{DATE}}", get_date_string(ac["date"]))
        html = html.replace("{{LOCATION}}", ac["location"])
        
        # Parse content properly
        parsed_content = parse_markdown_content(ac["content"])
        html = html.replace("{{CONTENT_HTML}}", parsed_content)
        
        # Stats
        if ac.get("participants"):
            stats_html = f"<div class='activity-stats-box mt-lg' data-animate='fade-up'><strong>Jumlah Peserta:</strong> <span>{ac['participants']} orang</span></div>"
            html = html.replace("{{STATS}}", stats_html)
        else:
            html = html.replace("{{STATS}}", "")
            
        # Gallery Images
        imgs_html = []
        for img in ac["images"]:
            rel_img = get_relative_path(img)
            imgs_html.append(f'<div class="masonry-item" data-lightbox="activity-gallery" data-src="{rel_img}" data-animate="fade-up" style="cursor:pointer;"><img src="{rel_img}" alt="{ac["title"]} Gallery Image" loading="lazy"></div>')
        html = html.replace("{{GALLERY_IMAGES}}", "\n".join(imgs_html))
        
        # Header / Footer
        html = html.replace("{{HEADER}}", ACTIVITY_HEADER_HTML)
        html = html.replace("{{FOOTER}}", FOOTER_HTML)
        
        with open(os.path.join(out_dir, "index.html"), 'w', encoding='utf-8') as out_f:
            out_f.write(html)
        print(f"Generated activity: {slug}")

if __name__ == '__main__':
    generate_all()
    print("Static detail pages generated successfully!")
