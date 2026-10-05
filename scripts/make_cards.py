#!/usr/bin/env python3
"""Generate the 1200x630 link-preview cards (Open Graph images) in images/cards/.

  images/cards/site.png                  profile card, used by all regular pages
  images/cards/<permalink slug>.png      one per publication/patent, e.g.
                                         /publication/2026-08-13 -> publication-2026-08-13.png

The output is pixel-for-pixel reproducible because the font file (sha256 checked)
and the Pillow version are pinned. Run from the repository root:

  pip install -r scripts/requirements.txt
  python scripts/make_cards.py

A card is only rewritten when its pixels change, so re-running is a no-op in git.
The design (layout, sizes, colors) is documented in CLAUDE.md; change it only on purpose.
"""
import glob
import hashlib
import os
import sys

import PIL
import yaml
from PIL import Image, ImageChops, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_DIR = os.path.join(ROOT, 'images', 'cards')
FONT = os.path.join(ROOT, 'scripts', 'fonts', 'Inter.ttf')
FONT_SHA256 = '29160a80ff49ddcab2c97711247e08b1fab27a484a329ce8b813d820dc559031'
PILLOW_VERSION = '10.4.0'  # keep in sync with scripts/requirements.txt
PHOTO = os.path.join(ROOT, 'images', 'prof_pic_square.png')

# Site palette (same as _sass/_variables.scss)
NAVY = (10, 22, 40)          # #0A1628 background
GOLD = (255, 192, 0)         # #FFC000 highlight
TEXT = (203, 213, 225)       # #CBD5E1 body text
WHITE = (241, 245, 249)      # #F1F5F9 headings
MUTED = (148, 163, 184)      # #94A3B8 secondary text
PERI = (165, 180, 252)       # #A5B4FC links
LINE = (36, 52, 76)          # #24344C rules / photo ring

W, H = 1200, 630

# Text on the profile card
SITE_CARD = {
    'name': 'Hans van Gorp',
    'role': 'Postdoctoral Researcher',
    'affiliation': 'Eindhoven University of Technology  ·  NXP Semiconductors',
    'topics': 'Signal processing  ·  Deep learning  ·  Radar  ·  Ultrasound',
    'url': 'hansvangorp.github.io',
}
OWN_NAME = 'van Gorp'  # author names containing this are drawn in bold white


def font(size, weight):
    f = ImageFont.truetype(FONT, size)
    f.set_variation_by_axes([32, weight])  # Inter axes: optical size, weight
    return f


def wrap(d, text, f, width):
    lines, cur = [], ''
    for w in text.split():
        t = (cur + ' ' + w).strip()
        if d.textlength(t, font=f) <= width:
            cur = t
        else:
            lines.append(cur)
            cur = w
    return lines + [cur]


def new_card():
    card = Image.new('RGB', (W, H), NAVY)
    d = ImageDraw.Draw(card)
    d.rectangle([0, 0, 12, H], fill=GOLD)  # gold accent bar on the left edge
    return card, d


def site_card():
    card, d = new_card()

    # round profile photo with a thin ring
    D = 300
    photo = Image.open(PHOTO).convert('RGB').resize((D, D), Image.Resampling.LANCZOS)
    mask = Image.new('L', (D * 4, D * 4), 0)
    ImageDraw.Draw(mask).ellipse([0, 0, D * 4 - 1, D * 4 - 1], fill=255)
    mask = mask.resize((D, D), Image.Resampling.LANCZOS)
    px, py = 100, (H - D) // 2
    d.ellipse([px - 6, py - 6, px + D + 6, py + D + 6], fill=LINE)
    card.paste(photo, (px, py), mask)

    x = px + D + 70
    d.text((x, 168), SITE_CARD['name'], font=font(68, 700), fill=WHITE)
    d.text((x, 258), SITE_CARD['role'], font=font(34, 600), fill=GOLD)
    d.text((x, 310), SITE_CARD['affiliation'], font=font(24, 400), fill=TEXT)
    d.line([x, 368, x + 560, 368], fill=LINE, width=2)
    d.text((x, 390), SITE_CARD['topics'], font=font(22, 500), fill=MUTED)
    d.text((x, 432), SITE_CARD['url'], font=font(24, 600), fill=PERI)
    return card


def paper_card(title, authors, venue_line):
    card, d = new_card()
    X = 90

    # title: largest size that fits in 3 lines
    for size in (64, 58, 52, 46, 42):
        tf = font(size, 700)
        lines = wrap(d, title, tf, W - 2 * X)
        if len(lines) <= 3:
            break

    # centre the text block vertically above the footer rule
    block = len(lines) * int(size * 1.2) + (22 + 46) + 34
    y = (H - 90 - block) // 2
    for ln in lines:
        d.text((X, y), ln, font=tf, fill=WHITE)
        y += int(size * 1.2)

    # authors on one line, own name in bold; truncated with an ellipsis if too long
    y += 22
    af, afb = font(26, 400), font(26, 700)
    x = X
    names = [a.strip() for a in authors.replace(' and ', ', ').split(',') if a.strip()]
    for i, name in enumerate(names):
        sep = '' if i == 0 else ', '
        f = afb if OWN_NAME in name else af
        if x + d.textlength(sep, font=af) + d.textlength(name, font=f) > W - X - 40:
            d.text((x, y), ', …', font=af, fill=MUTED)
            break
        d.text((x, y), sep, font=af, fill=MUTED)
        x += d.textlength(sep, font=af)
        d.text((x, y), name, font=f, fill=WHITE if f is afb else MUTED)
        x += d.textlength(name, font=f)

    d.text((X, y + 46), venue_line, font=font(26, 600), fill=GOLD)

    # footer
    d.line([X, H - 90, W - X, H - 90], fill=LINE, width=2)
    d.text((X, H - 55), SITE_CARD['url'], font=font(22, 600), fill=PERI, anchor='lm')
    return card


def front_matter(path):
    text = open(path, encoding='utf-8').read()
    return yaml.safe_load(text.split('---', 2)[1])


def card_slug(permalink):
    # must match _includes/seo.html: page.url without slashes, joined by '-'
    return '-'.join(p for p in permalink.split('/') if p)


def save_if_changed(img, path):
    """Write img unless an identical-looking card is already there."""
    if os.path.exists(path):
        with Image.open(path) as old:
            if old.size == img.size and not ImageChops.difference(old.convert('RGB'), img).getbbox():
                return False
    img.save(path, optimize=True)
    return True


def check_environment():
    sha = hashlib.sha256(open(FONT, 'rb').read()).hexdigest()
    if sha != FONT_SHA256:
        sys.exit(f'Font {FONT} has sha256 {sha}, expected {FONT_SHA256}.')
    if PIL.__version__ != PILLOW_VERSION and '--any-pillow' not in sys.argv:
        sys.exit(f'Pillow {PIL.__version__} found, cards are pinned to {PILLOW_VERSION} '
                 '(pip install -r scripts/requirements.txt). Use --any-pillow to override.')


def main():
    check_environment()
    os.makedirs(OUT_DIR, exist_ok=True)
    expected, changed = {'site.png'}, []

    if save_if_changed(site_card(), os.path.join(OUT_DIR, 'site.png')):
        changed.append('site.png')

    for path in sorted(glob.glob(os.path.join(ROOT, '_publications', '*.md')) +
                       glob.glob(os.path.join(ROOT, '_patents', '*.md'))):
        fm = front_matter(path)
        year = str(fm['date'])[:4]
        venue = (fm.get('venue') or '').strip()
        venue_line = f'{venue} · {year}' if venue else year
        name = card_slug(fm['permalink']) + '.png'
        expected.add(name)
        img = paper_card(fm['title'], fm.get('authors') or '', venue_line)
        if save_if_changed(img, os.path.join(OUT_DIR, name)):
            changed.append(name)

    # remove cards of papers that no longer exist
    for f in os.listdir(OUT_DIR):
        if f.endswith('.png') and f not in expected:
            os.remove(os.path.join(OUT_DIR, f))
            changed.append(f + ' (removed)')

    print(f'{len(expected)} cards, {len(changed)} changed' + (': ' + ', '.join(changed) if changed else ''))


if __name__ == '__main__':
    main()
