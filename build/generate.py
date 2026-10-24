#!/usr/bin/env python3
"""
Static site generator for Tarot with Nisha.

Renders every page through build/layout.py so the nav, footer, CTA blocks and
structured data stay consistent. Output is plain HTML committed to the repo —
there is no build step at deploy time.

Usage:
    cd websites/np-website/build
    python3 generate.py
"""
from __future__ import annotations

import sys
from datetime import date
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent

sys.path.insert(0, str(HERE))

import pages_home          # noqa: E402
import pages_tarot         # noqa: E402
import pages_numerology    # noqa: E402
import pages_rituals       # noqa: E402
import pages_shop          # noqa: E402
import pages_resources     # noqa: E402
import pages_misc          # noqa: E402

from layout import SITE_URL, render  # noqa: E402


def collect() -> list:
    pages = [
        pages_home.PAGE,
        # consultations
        pages_tarot.HUB,
        pages_tarot.TAROT,
        pages_tarot.LOVE,
        pages_tarot.CAREER,
        pages_numerology.NUMEROLOGY,
        pages_numerology.NAME,
        pages_numerology.HOUSE,
        pages_numerology.VEHICLE,
        pages_numerology.MARRIAGE,
        pages_numerology.BABY,
        pages_rituals.KUNDALI,
        pages_rituals.RITUALS,
        pages_rituals.CUSTOM,
        # shop
        pages_shop.SHOP,
        pages_shop.OILS_CAT,
        pages_shop.CRYSTALS_CAT,
        *pages_shop.PRODUCTS,
        # resources
        pages_misc.RESOURCES,
        pages_resources.GUIDES,
        pages_resources.FAQS,
        *pages_resources.ARTICLES,
        # misc
        pages_misc.ABOUT,
        pages_misc.DISCLAIMER,
        pages_misc.NOTFOUND,
    ]
    return pages


def sitemap(pages: list) -> str:
    today = date.today().isoformat()
    entries = []
    for p in pages:
        if p.noindex:
            continue
        entries.append(
            "  <url>\n"
            f"    <loc>{SITE_URL}{p.url}</loc>\n"
            f"    <lastmod>{today}</lastmod>\n"
            "    <changefreq>monthly</changefreq>\n"
            f"    <priority>{priority(p.url)}</priority>\n"
            "  </url>"
        )
    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "\n".join(entries)
        + "\n</urlset>\n"
    )


def priority(url: str) -> str:
    if url == "/":
        return "1.0"
    if url.count("/") <= 2 and url.endswith("/") and url != "/":
        return "0.9"
    if url.startswith("/consultations/") or url.startswith("/shop/"):
        return "0.8"
    if url.startswith("/resources/"):
        return "0.7"
    return "0.5"


def main() -> int:
    pages = collect()
    seen = set()
    for p in pages:
        if p.path in seen:
            print(f"ERROR: duplicate output path {p.path}", file=sys.stderr)
            return 1
        seen.add(p.path)

    for p in pages:
        out = ROOT / p.path
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(render(p), encoding="utf-8")
        print(f"  {p.path}")

    # sitemap + robots
    (ROOT / "sitemap.xml").write_text(sitemap(pages), encoding="utf-8")
    (ROOT / "robots.txt").write_text(
        "User-agent: *\n"
        "Allow: /\n"
        "Disallow: /404.html\n\n"
        f"Sitemap: {SITE_URL}/sitemap.xml\n",
        encoding="utf-8",
    )

    print(f"\n{len(pages)} pages written, plus sitemap.xml and robots.txt")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
