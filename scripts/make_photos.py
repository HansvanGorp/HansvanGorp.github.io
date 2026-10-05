#!/usr/bin/env python3
"""Derive the smaller profile photos from the original in images/.

  images/prof_pic_square.png   original (1500x1500); source for these and for the site card
  images/profile-print.jpg     600x600, for the CV PDF (~550 ppi at its 28 mm print size)
  images/profile-web.jpg       400x400, for the sidebar (175 px, sharp on 2x screens)

Run from the repository root (uses the Pillow version pinned in scripts/requirements.txt):

  python scripts/make_photos.py

A photo is only rewritten when its pixels change, so re-running is a no-op in git.
To change the photo, replace the original and run this script (the GitHub Action does too).
"""
import io
import os

from PIL import Image, ImageChops

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMAGES = os.path.join(ROOT, 'images')
ORIGINAL = os.path.join(IMAGES, 'prof_pic_square.png')

VERSIONS = [
    # file name,          size, JPEG quality
    ('profile-print.jpg', 600, 92),
    ('profile-web.jpg',   400, 85),
]


def encode(img, quality):
    buf = io.BytesIO()
    img.save(buf, 'JPEG', quality=quality, optimize=True, progressive=True)
    return buf.getvalue()


def same_pixels(path, data):
    if not os.path.exists(path):
        return False
    with Image.open(path) as old, Image.open(io.BytesIO(data)) as new:
        return old.size == new.size and not ImageChops.difference(
            old.convert('RGB'), new.convert('RGB')).getbbox()


def main():
    original = Image.open(ORIGINAL).convert('RGB')
    changed = []
    for name, size, quality in VERSIONS:
        data = encode(original.resize((size, size), Image.Resampling.LANCZOS), quality)
        path = os.path.join(IMAGES, name)
        if not same_pixels(path, data):
            with open(path, 'wb') as f:
                f.write(data)
            changed.append(name)
    print(f'{len(VERSIONS)} photos, {len(changed)} changed' + (': ' + ', '.join(changed) if changed else ''))


if __name__ == '__main__':
    main()
