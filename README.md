# MGI v7 — Luxury Miami Edition (Lounge Music)
- Hero line: “Empowering Global Growth from Miami, Florida.”
- Instagram icon (header & footer)
- Book Now in Travel (WhatsApp)
- Sam — Founder / Matt — Co‑Founder
- Contact: WhatsApp, emails, Instagram, Sunbiz, Google Map (no forms)
- Local images in /assets/images and music in /assets/audio (no external links)
- Vercel-ready static site

---
## v7.1 — Real HD Photos (Unsplash Source)
This build pulls REAL HD photos from Unsplash **via `source.unsplash.com`** URLs:
- Skyline, Resort, Skyscrapers (night), Business meeting, Executive coaching, Miami office.

### Make images local later (optional)
1) Download 6 photos you like and save them to `/assets/images/` with these exact names:
   - hero-miami-skyline.jpg
   - travel-luxury-resort.jpg
   - realestate-miami-towers.jpg
   - consulting-meeting.jpg
   - coaching-executive.jpg
   - miami-office.jpg
2) Replace the Unsplash URLs in `index.html` with the local paths above (or just ask me to package a local build).

---
## v7.2 — Local HD Edition (web‑fast, good quality)
This build now uses local image paths in `/assets/images/` for maximum reliability and speed.

### Upgrade to REAL HD photos (one step)
Run this from your laptop (Python 3):
```
pip install pillow
python fetch_images.py
```
This will download and optimize 6 real Unsplash photos into `/assets/images/` with the correct filenames.
Then redeploy on Vercel.
