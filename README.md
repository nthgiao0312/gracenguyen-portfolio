# Grace — Portfolio Website

A minimal, editorial multi-page portfolio for **Grace (Giao) Nguyen**, showcasing work across three disciplines:

- **Digital Marketing**
- **Graphic Design**
- **Data Analytics**

## Design principles

| Principle | How it shows up |
| --- | --- |
| **Minimal** | Warm off-white canvas, a single cobalt accent, generous whitespace, hairline rules. |
| **Modern** | Fraunces serif display + Inter sans body, sticky blurred nav, soft shadows. |
| **Impressive (creative)** | Editorial hero, gradient campaign tiles, scroll-up hover reveals on cards, full-width case studies. |
| **Logical (analyst)** | Numbered portals on the home page (01 — Marketing, 02 — Design, 03 — Analytics), structured experience lists, stat tile. |

### Color palette

| Token | Hex | Use |
| --- | --- | --- |
| Canvas | `#F5F2EC` | Page background (warm off-white / paper) |
| Elevated | `#EFEADF` | Card media fallback |
| Ink | `#0E0E10` | Text, primary buttons, stat tile |
| Muted | `#6B6B6B` | Secondary text |
| Hairline | `#D9D3C7` | Rules & borders |
| Accent | `#2C4BD8` | Cobalt — italic emphasis, hover states, focus rings |

## Pages

| File | Purpose |
| --- | --- |
| `index.html` | Home — hero intro + 3 numbered portals + contact block. |
| `marketing.html` | 01 — Digital Marketing: experience, projects, case studies, skills, resume CTA. |
| `design.html` | 02 — Graphic Design: practice, projects, full-size UI case studies, skills. |
| `analytics.html` | 03 — Data Analytics: experience, projects, certifications, skills, resume CTA. |

## File structure

```
portfolio-website-project/
├── index.html
├── marketing.html
├── design.html
├── analytics.html
├── styles.css
├── script.js
├── README.md
├── .gitignore
├── certificates/
│   ├── intermediate-R.png
│   └── intermediate-SQL.png
├── portfolio/
│   ├── graphic-designs/
│   │   ├── 2.jpg
│   │   ├── 3.png
│   │   ├── 4.png
│   │   └── Picture 1.jpg
│   └── uni-projects/
│       ├── medibank-app-development-mockups.png
│       ├── yesstyle-app-improvement-mockups.pdf
│       └── yesstyle/
│           ├── page-1.png
│           ├── page-2.png
│           ├── page-3.png
│           ├── page-4.png
│           └── page-5.png
└── resume/
    ├── Grace-Business-Data-Analyst-Resume.pdf
    ├── Grace-Digital-Marketing-Resume.pdf
    ├── Grace-Front-Office-Administrator-Resume.pdf
    └── Grace-SalesAssistant.pdf
```

## Run locally

No build step. You have two options:

**Option 1 — open directly**
Double-click `index.html` in Finder. It will open in your default browser.

**Option 2 — run a tiny local server (recommended)**
From the project root in Terminal:

```bash
python3 -m http.server 8000
```

Then open <http://localhost:8000>.

A local server is better because some browsers restrict certain features (e.g. fonts, image caching) when files are opened via `file://`.

## Deploy

The site is 100% static — deploy anywhere:

- **Netlify** — drag the project folder onto <https://app.netlify.com/drop>
- **Vercel** — run `vercel` in the folder, or drag-and-drop
- **GitHub Pages** — push to a repo, enable Pages on the `main` branch

## Editing the content

- **Copy and cards** live in the four HTML files. To add a new project, duplicate an `<article class="card">` block inside `.grid` on the relevant page.
- Each card uses either an `<a class="card__media">` wrapping an `<img>` (for real assets) **or** a `<div class="card__media card__media--gradient" data-gradient="1|2|3">` (for a placeholder tile), plus an `<h3>` title, `<p>` description, and `<ul class="card__meta">` tags.
- **Full-size case studies** on `marketing.html` and `design.html` use the `.case` / `.case__frame` blocks — good for showcasing multi-screen UI work.
- **Resume PDFs** are linked from `marketing.html` and `analytics.html` via `resume/…pdf`. Update the `href` in the `.resume-cta` section to swap which résumé each page offers.
- **Palette** — edit the CSS custom properties at the top of `styles.css` (`:root { ... }`).

## What to add next (optional)

- Real screenshots for the Kiehl's and Glam Nails campaigns (currently gradient placeholders on `marketing.html`).
- A dark mode toggle — the tokens are already variable-driven, so it's a small addition.
- An Open Graph / social-share image for each page.
