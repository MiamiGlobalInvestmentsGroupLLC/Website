#!/bin/bash
set -e
which python3 >/dev/null 2>&1 || { echo "Please install Python 3"; exit 1; }
python3 -m pip install --quiet pillow
python3 fetch_images.py
echo "Done. Images saved to assets/images/"
