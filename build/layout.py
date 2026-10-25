"""
Shared layout, navigation and schema builders for the Tarot with Nisha site.

Every page is rendered through `render()` so the header, footer, CTA blocks and
structured data stay identical across the site. Never hand-write a <html> shell.
"""
from __future__ import annotations

import html
import json
from dataclasses import dataclass, field

SITE_URL = "https://www.tarotwithnisha.com"
BRAND = "Tarot with Nisha"
PRACTITIONER = "Nisha Pathak"
WHATSAPP = "918796590763"
EMAIL = "nishak1410@gmail.com"
INSTAGRAM = "https://www.instagram.com/tarotwithnisha/"

DEFAULT_OG = "/images/og-image.jpg"
LOGO_SVG = (
    '<svg width="25" height="25" viewBox="0 0 100 100" fill="none" aria-hidden="true">'
    '<path d="M62 20a32 32 0 1 0 0 60 26 26 0 1 1 0-60Z" fill="#C9A15A"/></svg>'
)


def e(text: str) -> str:
    """Escape text for HTML."""
    return html.escape(text, quote=False)


def attr(text: str) -> str:
    return html.escape(text, quote=True)


def wa(service: str = "", placement: str = "generic") -> str:
    """Build a WhatsApp deep link with a pre-filled message."""
    service = html.unescape(service)  # content files may pass &amp; entities
    if service:
        msg = f"Hi Nisha, I'm interested in {service}. Could you share availability and pricing?"
    else:
        msg = "Hi Nisha, I'd like to know more about a reading. Could you share availability?"
    from urllib.parse import quote
    return f"https://wa.me/{WHATSAPP}?text={quote(msg)}"


def wa_btn(
    label: str,
    service: str = "",
    placement: str = "generic",
    cls: str = "btn btn-gold",
    extra: str = "",
) -> str:
    clean = html.unescape(service)
    return (
        f'<a class="{cls}" href="{wa(service, placement)}" target="_blank" rel="noopener" '
        f'data-wa-service="{attr(clean)}" data-wa-placement="{attr(placement)}"{extra}>{label}</a>'
    )


@dataclass
class Page:
    path: str  # output file path relative to site root, e.g. "consultations/index.html"
    url: str  # canonical path, e.g. "/consultations/"
    title: str
    description: str
    body: str
    h1: str = ""
    og_image: str = DEFAULT_OG
    schema: list = field(default_factory=list)
    nav: str = ""  # which top-level nav item is current
    crumbs: list = field(default_factory=list)  # [(label, url|None)]
    noindex: bool = False


# ---------------------------------------------------------------- navigation

CONSULTATIONS = [
    ("/consultations/tarot-readings/", "Tarot Readings", "Sessions, questions & specialised"),
    ("/consultations/numerology/", "Numerology", "Name, house, vehicle, marriage"),
    ("/consultations/vedic-kundali/", "Vedic Kundali & Varshfal", "Birth chart and annual reading"),
    ("/consultations/candle-rituals/", "Candle Rituals", "Intention-based ritual work"),
    ("/consultations/custom/", "Custom Consultation", "For situations that don't fit"),
]

SHOP = [
    ("/shop/ritual-oils/", "Ritual Oils", "Intention-based anointing oils"),
    ("/shop/crystals/", "Crystals & Bracelets", "Pyrite, tourmaline, quartz"),
    ("/shop/", "All Products", "The full collection"),
]

RESOURCES = [
    ("/resources/guides/", "Guides", "Practical reading on tarot & numerology"),
    ("/resources/faqs/", "FAQs", "Answers before you book"),
]


def _dropdown(items: list, with_desc: bool = True) -> str:
    out = ['<div class="dropdown">']
    for url, label, desc in items:
        if with_desc:
            out.append(f'<a href="{url}">{e(label)}<small>{e(desc)}</small></a>')
        else:
            out.append(f'<a href="{url}">{e(label)}</a>')
    return "\n".join(out) + "</div>"


def header(current: str = "") -> str:
    def cls(key: str) -> str:
        return ' data-current="true"' if current == key else ""

    return f"""
<div class="offer-banner">
  ✦ New here? First readings this week are 20% off — <a href="{wa()}" target="_blank" rel="noopener">book on WhatsApp</a> to claim it
</div>

<header class="site-header">
  <nav class="nav" aria-label="Primary">
    <a href="/" class="logo">{LOGO_SVG}<span>Tarot&nbsp;With&nbsp;Nisha</span></a>

    <ul class="navlinks">
      <li{cls("home")}><a href="/">Home</a></li>
      <li{cls("consultations")}>
        <button type="button" aria-expanded="false" aria-haspopup="true">Consultations <span class="chev"></span></button>
        {_dropdown(CONSULTATIONS)}
      </li>
      <li{cls("shop")}>
        <button type="button" aria-expanded="false" aria-haspopup="true">Shop <span class="chev"></span></button>
        {_dropdown(SHOP)}
      </li>
      <li{cls("resources")}>
        <button type="button" aria-expanded="false" aria-haspopup="true">Resources <span class="chev"></span></button>
        {_dropdown(RESOURCES)}
      </li>
      <li{cls("about")}><a href="/about/">About</a></li>
    </ul>

    <a href="{wa()}" class="btn btn-gold btn-sm navcta" target="_blank" rel="noopener"
       data-wa-service="" data-wa-placement="nav">Book on WhatsApp</a>

    <button class="hamburger" id="hamBtn" aria-label="Open menu" aria-expanded="false" aria-controls="mobileMenu">
      <span></span><span></span><span></span>
    </button>
  </nav>

  <div class="mobile-menu" id="mobileMenu">
    <a href="/">Home</a>
    <div class="mm-label">Consultations</div>
    {''.join(f'<a href="{u}">{e(l)}</a>' for u, l, _ in CONSULTATIONS)}
    <div class="mm-label">Shop</div>
    {''.join(f'<a href="{u}">{e(l)}</a>' for u, l, _ in SHOP)}
    <div class="mm-label">Resources</div>
    {''.join(f'<a href="{u}">{e(l)}</a>' for u, l, _ in RESOURCES)}
    <div class="mm-label">More</div>
    <a href="/about/">About</a>
    <a href="/consultations/">All consultations</a>
    <a href="/disclaimer/">Disclaimer</a>
    <a href="{wa()}" class="btn btn-gold" target="_blank" rel="noopener">Book on WhatsApp</a>
  </div>
</header>
"""


def breadcrumbs(crumbs: list) -> str:
    if not crumbs:
        return ""
    parts = ['<nav class="breadcrumbs" aria-label="Breadcrumb">',
             '<a href="/">Home</a>']
    for i, (label, url) in enumerate(crumbs):
        parts.append('<span class="sep">/</span>')
        if url and i < len(crumbs) - 1:
            parts.append(f'<a href="{url}">{e(label)}</a>')
        else:
            parts.append(f'<span aria-current="page">{e(label)}</span>')
    parts.append("</nav>")
    return "".join(parts)


def footer() -> str:
    return f"""
<footer class="site-footer">
  <div class="foot-grid">
    <div>
      <div class="foot-logo">Tarot With Nisha</div>
      <p>Private online tarot readings, numerology and intention-based rituals with {PRACTITIONER}.
         7+ years, 1,600+ clients. Hindi &amp; English, phone or video, pan-India.</p>
    </div>
    <div>
      <h4>Consultations</h4>
      <ul>
        <li><a href="/consultations/tarot-readings/">Tarot Readings</a></li>
        <li><a href="/consultations/numerology/">Numerology</a></li>
        <li><a href="/consultations/vedic-kundali/">Vedic Kundali &amp; Varshfal</a></li>
        <li><a href="/consultations/candle-rituals/">Candle Rituals</a></li>
        <li><a href="/consultations/custom/">Custom Consultation</a></li>
      </ul>
    </div>
    <div>
      <h4>Shop</h4>
      <ul>
        <li><a href="/shop/ritual-oils/">Ritual Oils</a></li>
        <li><a href="/shop/crystals/">Crystals &amp; Bracelets</a></li>
        <li><a href="/shop/">All Products</a></li>
      </ul>
    </div>
    <div>
      <h4>Connect</h4>
      <ul>
        <li><a href="{INSTAGRAM}" target="_blank" rel="noopener">Instagram — @tarotwithnisha</a></li>
        <li><a href="{wa()}" target="_blank" rel="noopener">WhatsApp — +91 87965 90763</a></li>
        <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
        <li><a href="/about/">About Nisha</a></li>
        <li><a href="/disclaimer/">Disclaimer</a></li>
      </ul>
    </div>
  </div>
  <div class="foot-bottom">
    <span>© <span id="year">2026</span> Tarot with Nisha. All rights reserved.</span>
    <span>Readings and rituals are offered as guidance and reflection. They are not a substitute for
    medical, legal or financial advice, and no outcome is guaranteed.</span>
  </div>
</footer>

<div class="sticky-cta" id="stickyCta">
  <a class="btn btn-outline" href="/consultations/">Consultations</a>
  {wa_btn("Book on WhatsApp", "", "sticky")}
</div>

<a href="{wa()}" class="float-wa" target="_blank" rel="noopener" aria-label="Chat on WhatsApp"
   data-wa-service="" data-wa-placement="float">
  <svg width="28" height="28" viewBox="0 0 32 32" fill="#fff" aria-hidden="true"><path d="M16.01 3C9.38 3 4 8.38 4 15.01c0 2.39.63 4.63 1.72 6.57L4 29l7.6-1.66a11.94 11.94 0 0 0 4.41.84h.01c6.63 0 12-5.38 12-12.01C28.02 8.38 22.65 3 16.01 3zm0 21.8h-.01a9.8 9.8 0 0 1-4.99-1.37l-.36-.21-4.51.99.98-4.4-.23-.37a9.78 9.78 0 0 1-1.51-5.23c0-5.41 4.4-9.81 9.82-9.81 2.62 0 5.09 1.02 6.94 2.88a9.75 9.75 0 0 1 2.87 6.94c0 5.41-4.4 9.58-9.99 9.58zm5.38-7.34c-.29-.15-1.75-.87-2.02-.96-.27-.1-.47-.15-.67.15-.2.29-.77.96-.94 1.16-.17.2-.35.22-.64.07-.29-.15-1.23-.46-2.35-1.47-.87-.78-1.45-1.74-1.62-2.03-.17-.29-.02-.45.13-.6.13-.13.29-.35.44-.52.15-.17.2-.29.29-.49.1-.2.05-.37-.02-.52-.07-.15-.67-1.63-.92-2.23-.24-.58-.49-.5-.67-.51-.17-.01-.37-.01-.57-.01-.2 0-.52.07-.79.37-.27.29-1.04 1.02-1.04 2.5s1.07 2.9 1.22 3.1c.15.2 2.1 3.21 5.09 4.5.71.31 1.27.49 1.7.62.71.23 1.36.2 1.87.12.57-.08 1.75-.71 2-1.4.25-.68.25-1.27.17-1.4-.07-.12-.26-.2-.55-.35z"/></svg>
</a>
"""


# ---------------------------------------------------------------- schema

def org_schema() -> dict:
    return {
        "@context": "https://schema.org",
        "@type": "ProfessionalService",
        "@id": SITE_URL + "/#business",
        "name": BRAND,
        "founder": {"@type": "Person", "name": PRACTITIONER, "jobTitle": "Tarot Reader & Numerologist"},
        "description": (
            "Online tarot readings, numerology consultations and intention-based candle rituals "
            "with Nisha Pathak. Private, one-on-one, by phone or video across India."
        ),
        "url": SITE_URL + "/",
        "image": SITE_URL + DEFAULT_OG,
        "telephone": "+91-87965-90763",
        "email": EMAIL,
        "priceRange": "₹299 - ₹7999",
        "currenciesAccepted": "INR",
        "areaServed": {"@type": "Country", "name": "India"},
        "availableLanguage": ["en", "hi"],
        "sameAs": [INSTAGRAM],
        "address": {"@type": "PostalAddress", "addressCountry": "IN"},
    }


def service_schema(name: str, description: str, url: str, price: str | None = None,
                   price_low: str | None = None, category: str = "Consultation") -> dict:
    d = {
        "@context": "https://schema.org",
        "@type": "Service",
        "name": name,
        "serviceType": category,
        "description": description,
        "provider": {"@type": "Person", "name": PRACTITIONER},
        "areaServed": {"@type": "Country", "name": "India"},
        "availableLanguage": ["en", "hi"],
        "url": SITE_URL + url,
    }
    offer = {}
    if price:
        offer = {"@type": "Offer", "price": price, "priceCurrency": "INR"}
    elif price_low:
        offer = {"@type": "Offer", "priceCurrency": "INR",
                 "priceSpecification": {"@type": "PriceSpecification",
                                        "minPrice": price_low, "priceCurrency": "INR"}}
    if offer:
        d["offers"] = offer
    return d


def faq_schema(faqs: list) -> dict:
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q,
             "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in faqs
        ],
    }


def breadcrumb_schema(crumbs: list) -> dict:
    items = [{"@type": "ListItem", "position": 1, "name": "Home", "item": SITE_URL + "/"}]
    for i, (label, url) in enumerate(crumbs, start=2):
        items.append({"@type": "ListItem", "position": i, "name": label,
                      "item": SITE_URL + (url or "/")})
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": items}


def product_schema(name: str, description: str, url: str, price: str, image: str,
                   brand_name: str = BRAND) -> dict:
    return {
        "@context": "https://schema.org",
        "@type": "Product",
        "name": name,
        "description": description,
        "image": SITE_URL + image,
        "brand": {"@type": "Brand", "name": brand_name},
        "url": SITE_URL + url,
        "offers": {
            "@type": "Offer",
            "price": price,
            "priceCurrency": "INR",
            "availability": "https://schema.org/InStock",
            "url": SITE_URL + url,
            "seller": {"@type": "Organization", "name": brand_name},
            "areaServed": {"@type": "Country", "name": "India"},
        },
    }


def article_schema(title: str, description: str, url: str, published: str, modified: str) -> dict:
    return {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": title,
        "description": description,
        "url": SITE_URL + url,
        "datePublished": published,
        "dateModified": modified,
        "author": {"@type": "Person", "name": PRACTITIONER},
        "publisher": {"@type": "Organization", "name": BRAND},
        "mainEntityOfPage": {"@type": "WebPage", "@id": SITE_URL + url},
    }


# ---------------------------------------------------------------- render

def render(p: Page) -> str:
    canonical = SITE_URL + p.url
    schemas = p.schema if p.schema else []
    # always include the org node on every page
    all_schema = [org_schema()] + schemas
    schema_html = "\n".join(
        f'<script type="application/ld+json">{json.dumps(s, ensure_ascii=False)}</script>'
        for s in all_schema
    )
    robots = '<meta name="robots" content="noindex,follow">' if p.noindex else \
             '<meta name="robots" content="index,follow,max-image-preview:large">'

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="theme-color" content="#241b3a">
<title>{e(p.title)}</title>
<meta name="description" content="{attr(p.description)}">
<link rel="canonical" href="{canonical}">
{robots}

<meta property="og:type" content="website">
<meta property="og:site_name" content="{BRAND}">
<meta property="og:title" content="{attr(p.title)}">
<meta property="og:description" content="{attr(p.description)}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{SITE_URL}{p.og_image}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{attr(p.title)}">
<meta name="twitter:description" content="{attr(p.description)}">
<meta name="twitter:image" content="{SITE_URL}{p.og_image}">

<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Crect width='100' height='100' rx='20' fill='%23120A1E'/%3E%3Cpath d='M62 20a32 32 0 1 0 0 60 26 26 0 1 1 0-60Z' fill='%23C9A15A'/%3E%3C/svg%3E">

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500&family=Jost:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/site.css">

{schema_html}
</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>
{header(p.nav)}
<main id="main">
{p.body}
</main>
{footer()}
<script src="/assets/site.js" defer></script>
</body>
</html>
"""
