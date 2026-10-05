# Hans van Gorp — academic website

Jekyll site built by GitHub Pages from `master` and served at https://hansvangorp.github.io.
It started as the academicpages template (a fork of Minimal Mistakes) and has since been
customized: dark theme, Inter font, structured publications, generated link-preview cards
and a generated CV PDF. Unused template content was removed on purpose; don't re-add it.

## Running locally

```
bundle install                      # gems go to vendor/bundle (see .bundle/config, gitignored)
bundle exec jekyll serve --config _config.yml,_config.dev.yml --livereload
```

Open http://localhost:4000. `_config.dev.yml` makes links point to localhost. Restart the
server after editing `_config.yml`. The `Gemfile` uses the `github-pages` gem, so the
local build matches GitHub's (Jekyll 3.10).

## Content

- `_pages/`: About (homepage, `about.md`), Publications, Patents, Teaching, CV.
- `_publications/*.md` and `_patents/*.md`: one file per item. The page body is only the
  abstract; everything else is in the front matter:

  ```yaml
  ---
  title: "Paper title"
  collection: publications           # or patents
  permalink: /publication/YYYY-MM-DD # patents: /patent/...; must be unique
  date: YYYY-MM-DD
  venue: 'Journal or conference'     # patents: 'US Patent Application 2025/0072825'
  authors: 'A. Author, Hans van Gorp, and B. Author'
  paperurl: 'https://doi.org/...'    # optional, shown as "Paper" button
  pdfurl: '/files/YYYY-MM-DD.pdf'    # optional, local PDFs live in files/
  codeurl: 'https://github.com/...'  # optional
  reference: 'Full citation text'    # optional, shown in the Citation box
  ---
  ```

  "Hans van Gorp", "H. van Gorp" and "H. Van Gorp" are automatically bolded in author lists.
- Rendering: `_includes/publication-meta.html` (authors, venue/year, link pills),
  `_includes/archive-single-pub.html` (list entry), `_includes/archive-single-cv.html`
  (CV entry). The Publications page groups entries by year.

## Design

Colors are defined once in `_sass/_variables.scss`:

| Role | Variable | Value |
|---|---|---|
| Background | `$background-color` | `#0A1628` |
| Body text | `$text-color` | `#CBD5E1` |
| Highlight/accent (sparingly: nav underline, selection, CV headings rule) | `$highlight-color` | `#FFC000` |
| Links | `$link-color` | `#A5B4FC` (periwinkle) |
| Muted text | `$gray` | `#94A3B8` |

The font is Inter (Google Fonts, loaded in `_includes/head/custom.html`). The owner found
gold links too loud; keep gold as a small accent only. Buttons are outline pills, not
filled gold. Print styles (`_sass/_print.scss`) turn the CV page into an A4 document in the
same dark theme (owner's choice). `@page { background }` paints the page margins navy and
`print-color-adjust: exact` stops Chrome from dropping the backgrounds.
The CV web page (`classes: cv-page`, styles in `_sass/_archive.scss`) deliberately mirrors
the PDF: compact text, `$heading-color` headings with a gold rule, two-column research areas.
Section headings with a thin gold rule are opt-in per page via `classes: ruled-headings`
(CV, Publications, Patents, Teaching). Screen-only CV/heading rules are wrapped in
`@media screen` so they never leak into the PDF; check the PDF after styling the CV page.

## Generated assets (do not edit by hand)

### Profile photos: `images/profile-*.jpg`

`images/prof_pic_square.png` (1500×1500) is the original, and the only photo to edit or replace.
`scripts/make_photos.py` derives the other two:

| File | Size | Used by |
|---|---|---|
| `prof_pic_square.png` | 1500×1500 original | `scripts/make_cards.py` (site card) |
| `profile-print.jpg` | 600×600, q92 | CV PDF header (`_pages/cv.md`) |
| `profile-web.jpg` | 400×400, q85 | sidebar (`author.avatar` in `_config.yml`) |

Never point pages at the original: it is 2 MB and made the CV PDF 4 MB.

The GitHub Action `.github/workflows/generated-assets.yml` regenerates these on push and
commits them:

### Link-preview cards: `images/cards/*.png`

Made by `scripts/make_cards.py` (1200×630 PNG, the Open Graph size LinkedIn uses).

- `site.png`: profile card (photo `images/prof_pic_square.png`, name, role,
  affiliations, topics, URL). Set as `og_image` in `_config.yml`; used for all regular pages.
- `<permalink slug>.png`, one per publication/patent: `/publication/2026-08-13` gives
  `publication-2026-08-13.png`. `_includes/seo.html` derives the same name from `page.url`.
- Paper card design (approved by the owner; don't change without being asked):
  - navy background with a 12px gold bar on the left edge;
  - no header or logo;
  - the title in Inter Bold white, largest of 64/58/52/46/42px that fits in 3 lines;
  - one line of authors (26px, muted gray, own name in bold white, truncated with "…");
  - `venue · year` in gold, 26px semibold;
  - a footer rule with `hansvangorp.github.io` in periwinkle;
  - the text block is vertically centered above the footer rule.

**Reproducing them exactly.** The output is pixel-identical on any OS as long as these are unchanged:
- the font `scripts/fonts/Inter.ttf` (variable Inter from google/fonts, OFL licence, sha256
  checked by the script);
- Pillow's basic text layout engine (`layout_engine=ImageFont.Layout.BASIC`). Without it,
  Pillow uses libraqm when it is installed, as on GitHub's Linux runners, and glyphs shift;
- the Pillow version pinned in `scripts/requirements.txt` (the script refuses to run with
  another version unless `--any-pillow`).

```
pip install -r scripts/requirements.txt
python scripts/make_photos.py       # derived profile photos (run first)
python scripts/make_cards.py        # only rewrites cards whose pixels changed
```

Cards are regenerated automatically when a paper is added or edited. Cards for deleted
papers are removed. To change the profile card text, edit `SITE_CARD` in the script.

### CV PDF: `files/cv.pdf`

`scripts/cv-pdf.sh` prints http://localhost:4000/cv/ to PDF with headless Chrome, using the
print styles. The PDF starts with a header that only appears in print (`.cv-print-header` in
`_pages/cv.md`): name, role in gold and contact line flush left, round profile photo on
the right, and a thin light grey line (0.5pt `$gray`) along the bottom of the band. It is currently 3 pages.
The header is a full-width band in `$lighter-gray` (#13223A) on page 1 only (`@page :first`
has no top margin). Pages have no side margins; `.archive` is padded 16mm instead, so the
band can bleed to the edges without Chrome shrinking the page to fit. Band padding is equal
top and bottom (12mm) so the photo is vertically centred. The site must be served first, then run `bash scripts/cv-pdf.sh`. The CV page
links to it with the "Download CV (PDF)" button.

## Conventions

- Shell scripts must keep LF line endings (`.gitattributes`); the Action runs them on Linux.
- `scripts/`, `CLAUDE.md`, `vendor/` and `Gemfile.lock` are excluded from the built site
  (`exclude:` in `_config.yml`).
