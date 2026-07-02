/* ============================================
   ABYNSS STUDIO — WhatsApp Floating Button
   ============================================ */

import { fetchData, whatsappUrl } from '../utils.js';

export async function initWhatsAppFloat() {
  const btn = document.querySelector('.whatsapp-float');
  if (!btn) return;

  const siteData = await fetchData('site');
  if (!siteData) return;

  const phone = siteData.whatsapp || '6285973729267';
  const message = 'Halo ABYNSS Studio, saya tertarik dengan layanan fotografi/videografi Anda. Boleh info lebih lanjut?';

  btn.href = whatsappUrl(phone, message);
  btn.target = '_blank';
  btn.rel = 'noopener noreferrer';
}
