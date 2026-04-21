# Grace — Portfolio Website

A minimal, editorial one-page portfolio for **Grace (Giao) Nguyen**, showcasing work across three disciplines:

- **Digital Marketing**
- **Graphic Design**
- **Data Analytics**

## Design principles

| Principle | How it shows up |
| --- | --- |
| **Minimal** | Warm off-white canvas, a single cobalt accent, generous whitespace, hairline rules. |
| **Modern** | Fraunces serif display + Inter sans body, sticky blurred nav, soft shadows. |
| **Impressive (creative)** | Editorial hero, gradient campaign tiles, scroll-up hover reveals on cards. |
| **Logical (analyst)** | Dashboard-style filter chips for work (All / Marketing / Design / Analytics), numbered sections (01 — About, 02 — Work, 03 — Contact). |

### Color palette

| Token | Hex | Use |
| --- | --- | --- |
| Canvas | `#F5F2EC` | Page background (warm off-white / paper) |
| Elevated | `#EFEADF` | Card media fallback |
| Ink | `#0E0E10` | Text, primary buttons, stat tile |
| Muted | `#6B6B6B` | Secondary text |
| Hairline | `#D9D3C7` | Rules & borders |
| Accent | `#2C4BD8` | Cobalt — italic emphasis, hover states, focus rings |

## File structure

```
resume/
├── index.html
├── styles.css
├── script.js
├── README.md
├── certificates/
│   ├── intermediate-R.png
│   └── intermediate-SQL.png
└── portfolio/
    ├── graphic-designs/
    │   ├── 2.jpg
    │   ├── 3.png
    │   ├── 4.png
    │   └── Picture 1.jpg
    └── uni-projects/
        └── medibank-app-development-mockups.png
```

## Run locally

No build step. You have two options:

**Option 1 — open directly**
Double-click `index.html` in Finder. It will open in your default browser.

**Option 2 — run a tiny local server (recommended)**
From the `resume/` folder in Terminal:

```bash
python3 -m http.server 8000
```

Then open <http://localhost:8000>.

A local server is better because some browsers restrict certain features (e.g. fonts, image caching) when files are opened via `file://`.

## Deploy

The site is 100% static — deploy anywhere:

- **Netlify** — drag the `resume/` folder onto <https://app.netlify.com/drop>
- **Vercel** — `vercel` in the folder, or drag-and-drop
- **GitHub Pages** — push to a repo, enable Pages on the `main` branch

## Editing the content

All copy and cards live in `index.html`. To add a new project, duplicate a `<article class="card">` block inside `.grid` and set:

- `data-category="marketing" | "design" | "analytics"` — controls which filter shows it.
- Either an `<a class="card__media">` wrapping an `<img>` (for real assets) **or** a `<div class="card__media card__media--gradient" data-gradient="1|2|3">` (for a placeholder tile).
- `<h3>` title, `<p>` description, and `<ul class="card__meta">` tags.

To change the palette, edit the CSS custom properties at the top of `styles.css` (`:root { ... }`).

## What to add next (optional)

- Real screenshots for the Kiehl's and Glam Nails campaigns (currently gradient placeholders).
- A downloadable PDF resume button in the nav (one of the existing resume PDFs can be linked directly).
- A dark mode toggle — the tokens are already variable-driven, so it's a small addition.
