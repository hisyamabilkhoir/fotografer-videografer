/* ============================================
   ABYNSS STUDIO — Accordion Component
   ============================================ */

export function initAccordion() {
  const accordionItems = document.querySelectorAll('.accordion-item');
  if (!accordionItems.length) return;

  accordionItems.forEach(item => {
    const header = item.querySelector('.accordion-header');
    const body = item.querySelector('.accordion-body');
    const inner = item.querySelector('.accordion-body-inner');

    if (!header || !body || !inner) return;

    header.addEventListener('click', () => {
      const isActive = item.classList.contains('active');

      // Close all other items (optional: remove this for multi-open)
      accordionItems.forEach(otherItem => {
        if (otherItem !== item) {
          otherItem.classList.remove('active');
          const otherBody = otherItem.querySelector('.accordion-body');
          if (otherBody) otherBody.style.maxHeight = '0';
        }
      });

      // Toggle current item
      if (isActive) {
        item.classList.remove('active');
        body.style.maxHeight = '0';
      } else {
        item.classList.add('active');
        body.style.maxHeight = inner.scrollHeight + 'px';
      }
    });
  });
}
