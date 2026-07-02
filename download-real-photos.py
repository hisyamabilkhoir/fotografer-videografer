import urllib.request
import os
import ssl

# Bypass SSL certificate verification for standard Python urllib
ssl._create_default_https_context = ssl._create_unverified_context

BASE_DIR = r"c:\xampp\htdocs\abynsstudio\fotografer-videografer\assets\images"

# Unsplash Curated Luxury/Aesthetic Photo URLs (1200x800 for main, 800x800 for square gallery, 200x200 for avatars)
UNSPLASH_PHOTOS = {
    # Hero / OG
    "hero/hero-poster.jpg": "https://images.unsplash.com/photo-1492691527719-9d1e07e534b4?auto=format&fit=crop&w=1920&h=1080&q=80",
    "og/og-home.jpg": "https://images.unsplash.com/photo-1492691527719-9d1e07e534b4?auto=format&fit=crop&w=1200&h=630&q=80",
    
    # Portfolio Wedding
    "portfolio/wedding-01.jpg": "https://images.unsplash.com/photo-1519741497674-611481863552?auto=format&fit=crop&w=1200&h=800&q=80",
    "portfolio/wedding-01-2.jpg": "https://images.unsplash.com/photo-1511285560929-80b456fea0bc?auto=format&fit=crop&w=1200&h=800&q=80",
    "portfolio/wedding-01-3.jpg": "https://images.unsplash.com/photo-1583939003579-730e3918a45a?auto=format&fit=crop&w=1200&h=800&q=80",
    "portfolio/wedding-01-4.jpg": "https://images.unsplash.com/photo-1465495976277-4387d4b0b4c6?auto=format&fit=crop&w=1200&h=800&q=80",
    "portfolio/wedding-01-5.jpg": "https://images.unsplash.com/photo-1519225495810-7517c5000916?auto=format&fit=crop&w=1200&h=800&q=80",
    "portfolio/wedding-01-6.jpg": "https://images.unsplash.com/photo-1507504038482-7621c51871be?auto=format&fit=crop&w=1200&h=800&q=80",
    
    # Portfolio Commercial / Products
    "portfolio/commercial-01.jpg": "https://images.unsplash.com/photo-1523275335684-37898b6baf30?auto=format&fit=crop&w=1200&h=800&q=80",
    "portfolio/commercial-01-2.jpg": "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?auto=format&fit=crop&w=1200&h=800&q=80",
    "portfolio/commercial-01-3.jpg": "https://images.unsplash.com/photo-1572635196237-14b3f281503f?auto=format&fit=crop&w=1200&h=800&q=80",
    
    # Portfolio Cinematic Wedding Film (Widescreen cinematic stills)
    "portfolio/wedding-film-01.jpg": "https://images.unsplash.com/photo-1494959764136-6be9eb3c261e?auto=format&fit=crop&w=1200&h=800&q=80",
    "portfolio/wedding-film-01-2.jpg": "https://images.unsplash.com/photo-1519671482749-fd09be7ccebf?auto=format&fit=crop&w=1200&h=800&q=80",
    "portfolio/wedding-film-01-3.jpg": "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?auto=format&fit=crop&w=1200&h=800&q=80",
    
    # Portfolio Fashion Editorial
    "portfolio/fashion-01.jpg": "https://images.unsplash.com/photo-1490481651871-ab68de25d43d?auto=format&fit=crop&w=1200&h=800&q=80",
    "portfolio/fashion-01-2.jpg": "https://images.unsplash.com/photo-1469334031218-e382a71b716b?auto=format&fit=crop&w=1200&h=800&q=80",
    "portfolio/fashion-01-3.jpg": "https://images.unsplash.com/photo-1509631179647-0177331693ae?auto=format&fit=crop&w=1200&h=800&q=80",
    
    # Portfolio Food
    "portfolio/food-01.jpg": "https://images.unsplash.com/photo-1504674900247-0877df9cc836?auto=format&fit=crop&w=1200&h=800&q=80",
    "portfolio/food-01-2.jpg": "https://images.unsplash.com/photo-1476224203421-9ac39bcb3327?auto=format&fit=crop&w=1200&h=800&q=80",
    "portfolio/food-01-3.jpg": "https://images.unsplash.com/photo-1498837167922-ddd27525d352?auto=format&fit=crop&w=1200&h=800&q=80",
    
    # Portfolio Corporate
    "portfolio/corporate-01.jpg": "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?auto=format&fit=crop&w=1200&h=800&q=80",
    "portfolio/corporate-01-2.jpg": "https://images.unsplash.com/photo-1497366216548-37526070297c?auto=format&fit=crop&w=1200&h=800&q=80",
    "portfolio/corporate-01-3.jpg": "https://images.unsplash.com/photo-1497215728101-856f4ea42174?auto=format&fit=crop&w=1200&h=800&q=80",
    
    # Portfolio Graduation
    "portfolio/graduation-01.jpg": "https://images.unsplash.com/photo-1523050854058-8df90110c9f1?auto=format&fit=crop&w=1200&h=800&q=80",
    "portfolio/graduation-01-2.jpg": "https://images.unsplash.com/photo-1541339907198-e08756dedf3f?auto=format&fit=crop&w=1200&h=800&q=80",
    
    # Portfolio Prewedding
    "portfolio/prewedding-01.jpg": "https://images.unsplash.com/photo-1492691527719-9d1e07e534b4?auto=format&fit=crop&w=1200&h=800&q=80",
    "portfolio/prewedding-01-2.jpg": "https://images.unsplash.com/photo-1482575003355-12a73a8ccd15?auto=format&fit=crop&w=1200&h=800&q=80",
    "portfolio/prewedding-01-3.jpg": "https://images.unsplash.com/photo-1522673607200-164d1b6ce486?auto=format&fit=crop&w=1200&h=800&q=80",
    
    # About
    "about/author.jpg": "https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=600&h=600&q=80",
    "about/studio.jpg": "https://images.unsplash.com/photo-1542038784456-1ea8e935640e?auto=format&fit=crop&w=1200&h=1500&q=80",
    "about/photographer.jpg": "https://images.unsplash.com/photo-1492691527719-9d1e07e534b4?auto=format&fit=crop&w=1200&h=1500&q=80",
    
    # Services
    "services/photography.jpg": "https://images.unsplash.com/photo-1516035069371-29a1b244cc32?auto=format&fit=crop&w=1200&h=800&q=80",
    "services/videography.jpg": "https://images.unsplash.com/photo-1492691527719-9d1e07e534b4?auto=format&fit=crop&w=1200&h=800&q=80",
    "services/wedding.jpg": "https://images.unsplash.com/photo-1519741497674-611481863552?auto=format&fit=crop&w=1200&h=800&q=80",
    "services/corporate.jpg": "https://images.unsplash.com/photo-1497366216548-37526070297c?auto=format&fit=crop&w=1200&h=800&q=80",
    "services/drone.jpg": "https://images.unsplash.com/photo-1527977966376-1c8408f9f108?auto=format&fit=crop&w=1200&h=800&q=80",
    "services/editing.jpg": "https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?auto=format&fit=crop&w=1200&h=800&q=80",
    
    # Articles
    "articles/article-01.jpg": "https://images.unsplash.com/photo-1452780212940-6f5c0d14d848?auto=format&fit=crop&w=1200&h=800&q=80",
    "articles/article-02.jpg": "https://images.unsplash.com/photo-1492691527719-9d1e07e534b4?auto=format&fit=crop&w=1200&h=800&q=80",
    "articles/article-03.jpg": "https://images.unsplash.com/photo-1506157786151-b8491531f063?auto=format&fit=crop&w=1200&h=800&q=80",
    
    # Activities
    "activities/activity-01.jpg": "https://images.unsplash.com/photo-1515187029135-18ee286d815b?auto=format&fit=crop&w=1200&h=800&q=80",
    "activities/activity-01-2.jpg": "https://images.unsplash.com/photo-1528605248644-14dd04022da1?auto=format&fit=crop&w=1200&h=800&q=80",
    "activities/activity-02.jpg": "https://images.unsplash.com/photo-1511578314322-379afb476865?auto=format&fit=crop&w=1200&h=800&q=80",
    "activities/activity-02-2.jpg": "https://images.unsplash.com/photo-1540575467063-178a50c2df87?auto=format&fit=crop&w=1200&h=800&q=80",
    "activities/activity-03.jpg": "https://images.unsplash.com/photo-1505373877841-8d25f7d46678?auto=format&fit=crop&w=1200&h=800&q=80",
    "activities/activity-03-2.jpg": "https://images.unsplash.com/photo-1517457373958-b7bdd4587205?auto=format&fit=crop&w=1200&h=800&q=80",
    
    # Testimonials
    "testimonials/avatar-01.jpg": "https://images.unsplash.com/photo-1494790108377-be9c29b29330?auto=format&fit=crop&w=200&h=200&q=80",
    "testimonials/avatar-02.jpg": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&w=200&h=200&q=80",
    "testimonials/avatar-03.jpg": "https://images.unsplash.com/photo-1438761681033-6461ffad8d80?auto=format&fit=crop&w=200&h=200&q=80",
    "testimonials/avatar-04.jpg": "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?auto=format&fit=crop&w=200&h=200&q=80",
    "testimonials/avatar-05.jpg": "https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=200&h=200&q=80",
    "testimonials/avatar-06.jpg": "https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?auto=format&fit=crop&w=200&h=200&q=80",
    
    # Gallery
    "gallery/gallery-01.jpg": "https://images.unsplash.com/photo-1519741497674-611481863552?auto=format&fit=crop&w=800&h=800&q=80",
    "gallery/gallery-02.jpg": "https://images.unsplash.com/photo-1490481651871-ab68de25d43d?auto=format&fit=crop&w=800&h=800&q=80",
    "gallery/gallery-03.jpg": "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?auto=format&fit=crop&w=800&h=800&q=80",
    "gallery/gallery-04.jpg": "https://images.unsplash.com/photo-1527977966376-1c8408f9f108?auto=format&fit=crop&w=800&h=800&q=80",
    "gallery/gallery-05.jpg": "https://images.unsplash.com/photo-1504674900247-0877df9cc836?auto=format&fit=crop&w=800&h=800&q=80",
    "gallery/gallery-06.jpg": "https://images.unsplash.com/photo-1516035069371-29a1b244cc32?auto=format&fit=crop&w=800&h=800&q=80",
    "gallery/gallery-07.jpg": "https://images.unsplash.com/photo-1506157786151-b8491531f063?auto=format&fit=crop&w=800&h=800&q=80",
    "gallery/gallery-08.jpg": "https://images.unsplash.com/photo-1511578314322-379afb476865?auto=format&fit=crop&w=800&h=800&q=80",
    "gallery/gallery-09.jpg": "https://images.unsplash.com/photo-1505373877841-8d25f7d46678?auto=format&fit=crop&w=800&h=800&q=80",
    "gallery/gallery-10.jpg": "https://images.unsplash.com/photo-1519671482749-fd09be7ccebf?auto=format&fit=crop&w=800&h=800&q=80",
    "gallery/gallery-11.jpg": "https://images.unsplash.com/photo-1497366216548-37526070297c?auto=format&fit=crop&w=800&h=800&q=80",
    "gallery/gallery-12.jpg": "https://images.unsplash.com/photo-1469334031218-e382a71b716b?auto=format&fit=crop&w=800&h=800&q=80",
}

print("Starting to download high-quality luxury photos...")

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

downloaded = 0
failed = 0

for relative_path, url in UNSPLASH_PHOTOS.items():
    dest_path = os.path.join(BASE_DIR, relative_path.replace('/', os.sep))
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    
    print(f"Downloading {relative_path}...")
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=15) as response, open(dest_path, 'wb') as out_file:
            out_file.write(response.read())
        downloaded += 1
    except Exception as e:
        print(f"Failed to download {relative_path}: {e}")
        failed += 1

print(f"\nDownload finished! Successfully downloaded: {downloaded}, Failed: {failed}")
