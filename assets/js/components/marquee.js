/* ============================================
   ABYNSS STUDIO — Marquee Component
   Infinite horizontal scrolling text
   ============================================ */

export function initMarquee() {
  const marquees = document.querySelectorAll('.marquee-track');
  marquees.forEach(track => {
    // Clone content for seamless loop
    const content = track.innerHTML;
    track.innerHTML = content + content;
  });
}
