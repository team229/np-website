# Build system

The site is **plain static HTML** committed to the repo — there is no build step at
deploy time. This folder exists only so that the 32 pages share one header, footer,
CTA blocks and schema layer instead of duplicating them 32 times.

## Why a generator

Before this, the site was a single 878-line `index.html` with inline `<style>` and
`<script>`. That doesn't scale past a handful of pages. Now:

- **One stylesheet** (`assets/site.css`) — every page links it
- **One script** (`assets/site.js`) — nav, menus, tabs, accordion, sticky CTA
- **One layout** (`build/layout.py`) — head, meta, OG, schema, header, footer
- **One components file** (`build/components.py`) — cards, tables, FAQs, CTA blocks
- **One module per section** — home, tarot, numerology, rituals, shop, resources, misc

Changing the nav or footer is now a one-line edit in `layout.py`, followed by a
regenerate.

## Commands

```bash
cd websites/np-website/build

python3 generate.py    # writes all 32 pages + sitemap.xml + robots.txt
python3 check.py       # QA: broken links, missing images, duplicate/missing meta,
                       #     H1 count, sitemap coverage
```

There are no third-party dependencies — Python 3 standard library only.

## How a page is defined

Each page is a `Page` dataclass:

```python
PAGE = Page(
    path="consultations/numerology/house/index.html",   # output file
    url="/consultations/numerology/house/",             # canonical
    title="House Number Numerology India | Flat & Nameplate | ₹399",
    description="...",                                  # <=175 chars
    body=BODY,                                          # rendered HTML
    nav="consultations",                                # highlights nav item
    crumbs=[("Consultations", "/consultations/"), ...], # breadcrumbs + schema
    og_image="/images/cat-numerology.webp",
    schema=[service_schema(...), faq_schema(...)],
)
```

`layout.render(PAGE)` wraps it with the head, schema JSON-LD, header, footer and
sticky CTA. The `ProfessionalService` organisation node is added to every page
automatically.

## Adding a page

1. Write the body using the helpers in `components.py`
2. Append a `Page(...)` to the relevant `pages_*.py` module
3. Add it to `collect()` in `generate.py`
4. Run `generate.py` then `check.py`
5. Commit the generated `.html` alongside the source

## Rules for content

- `check.py` must pass before committing — no broken links, no duplicate titles
- One `<h1>` per page (product pages put the H1 in the product detail, not the hero)
- Titles ≤ 65 chars, descriptions 70–175 chars
- Every service page needs: price, who it's for, what's included, how it works, FAQ
- Every ritual or product page needs the disclaimer block
- Images go in `images/`, always `.webp`, referenced with a root-relative path
- Never hotlink an external image

## Image pipeline

Images are generated at high resolution and converted once:

```python
from PIL import Image
im = Image.open(src).convert("RGB")
im.thumbnail((1600, 1600), Image.LANCZOS)
im.save(dst.with_suffix(".webp"), "WEBP", quality=82, method=6)
```

Category images: 1600px wide. Product images: 1100px square. Portrait: 900px.
Total image weight is ~1.2 MB for the whole site.

## Known constraints

- **No shopping cart.** Products use an "Order on WhatsApp" flow with a quantity
  selector. This is deliberate: real payment integration (Razorpay/Stripe) needs a
  backend, GST details and a refund policy Nisha has to sign off on. WhatsApp
  ordering is how the business already closes sales.
- **No testimonials.** The site explains why (readings are private) and links to the
  Instagram highlights. When Nisha supplies quotes with permission, add a
  `.test-grid` block and `Review` schema.
- **No Hindi pages yet.** The language signal is present throughout
  ("Hindi & English"). A full `hreflang` build should wait until Search Console
  shows real Hindi-language query volume.
