#!/usr/bin/env python3
# Download real HD photos (Unsplash) and save to /assets/images/.

import os, io
from urllib.request import urlopen, Request
from PIL import Image

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "images")
os.makedirs(OUT, exist_ok=True)

IMAGES = {
  "hero-miami-skyline.jpg": "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?q=80&w=1920&auto=format&fit=crop",
  "travel-luxury-resort.jpg": "https://images.unsplash.com/photo-1501117716987-c8eecbff15f9?q=80&w=1920&auto=format&fit=crop",
  "realestate-miami-towers.jpg": "https://images.unsplash.com/photo-1485738422979-f5c462d49f74?q=80&w=1920&auto=format&fit=crop",
  "consulting-meeting.jpg": "https://images.unsplash.com/photo-1522071820081-009f0129c71c?q=80&w=1920&auto=format&fit=crop",
  "coaching-executive.jpg": "https://images.unsplash.com/photo-1523289333742-be1143f6b766?q=80&w=1920&auto=format&fit=crop",
  "miami-office.jpg": "https://images.unsplash.com/photo-1507209696998-3c532be9b2b1?q=80&w=1920&auto=format&fit=crop",
}

def fetch_and_optimize(name, url):
    print(f"Fetching {name} ...")
    req = Request(url, headers={"User-Agent":"Mozilla/5.0"})
    with urlopen(req, timeout=30) as r:
        data = r.read()
    img = Image.open(io.BytesIO(data)).convert("RGB")
    # Resize if > 1920 px width
    max_w = 1920
    if img.width > max_w:
        ratio = max_w / img.width
        img = img.resize((max_w, int(img.height*ratio)), Image.LANCZOS)
    out_path = os.path.join(OUT, name)
    img.save(out_path, "JPEG", quality=82, optimize=True, progressive=True)
    print("Saved:", out_path)

def main():
    try:
        from PIL import Image
    except ImportError:
        print("Install Pillow: pip install pillow")
        return
    for name, url in IMAGES.items():
        try:
            fetch_and_optimize(name, url)
        except Exception as e:
            print("Failed:", name, e)
    print("Done.")

if __name__ == "__main__":
    main()
