#!/usr/bin/env python3
"""
Post-build QA for the static site.

Checks:
  - every internal href/src resolves to a real file
  - every page has exactly one <h1>
  - titles and meta descriptions are unique and within length
  - descriptions exist and are within length
  - sitemap covers every indexable page
  - no external image hotlinks

Usage:
    cd websites/np-website/build
    python3 check.py
"""
from __future__ import annotations

import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent.parent

errors: list[str] = []
warnings: list[str] = []


class Head(HTMLParser):
    def __init__(self):
        super().__init__()
        self.h1 = 0
        self.title = None
        self.desc = None
        self.links: list[str] = []
        self.imgs: list[str] = []
        self._in_title = False
        self._in_desc = False
        self._buf = ""

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "h1":
            self.h1 += 1
        elif tag == "title":
            self._in_title = True
            self._buf = ""
        elif tag == "meta" and a.get("name") == "description":
            self.desc = a.get("content", "")
        elif tag in ("a", "link"):
            href = a.get("href", "")
            if href:
                self.links.append(href)
        elif tag == "img":
            src = a.get("src", "")
            if src:
                self.imgs.append(src)

    def handle_endtag(self, tag):
        if tag == "title":
            self._in_title = False
            self.title = self._buf.strip()

    def handle_data(self, data):
        if self._in_title:
            self._buf += data


def resolve(url: str) -> Path | None:
    """Map a site path to a file, or None if external/anchor."""
    if not url or url.startswith("#") or url.startswith("mailto:") or url.startswith("tel:"):
        return None
    if url.startswith("http://") or url.startswith("https://"):
        return None
    if url.startswith("data:"):
        return None
    path = urlparse(url).path
    if not path.startswith("/"):
        return ROOT / path  # relative — rare here
    target = ROOT / path.lstrip("/")
    if path.endswith("/"):
        target = target / "index.html"
    return target


def main() -> int:
    pages = sorted(ROOT.rglob("*.html"))
    pages = [p for p in pages if "build" not in p.parts]

    seen_titles: dict[str, Path] = {}
    seen_desc: dict[str, Path] = {}
    indexed: set[str] = set()

    for page in pages:
        rel = page.relative_to(ROOT)
        html = page.read_text(encoding="utf-8")
        h = Head()
        h.feed(html)

        # h1
        if h.h1 != 1:
            errors.append(f"{rel}: expected 1 <h1>, found {h.h1}")

        # title
        if not h.title:
            errors.append(f"{rel}: missing <title>")
        else:
            if len(h.title) > 65:
                warnings.append(f"{rel}: title is {len(h.title)} chars (>65)")
            if len(h.title) < 25:
                warnings.append(f"{rel}: title is only {len(h.title)} chars")
            if h.title in seen_titles:
                errors.append(f"{rel}: duplicate title also used by {seen_titles[h.title]}")
            else:
                seen_titles[h.title] = rel

        # description
        if not h.desc:
            errors.append(f"{rel}: missing meta description")
        else:
            if len(h.desc) < 70:
                warnings.append(f"{rel}: description is {len(h.desc)} chars (<70)")
            if len(h.desc) > 175:
                warnings.append(f"{rel}: description is {len(h.desc)} chars (>175)")
            if h.desc in seen_desc:
                errors.append(f"{rel}: duplicate description also used by {seen_desc[h.desc]}")
            else:
                seen_desc[h.desc] = rel

        if 'content="noindex' not in html and rel.name == "index.html":
            indexed.add("/" + str(rel).replace("index.html", ""))

        # links
        for href in h.links:
            target = resolve(href)
            if target is None:
                continue
            if not target.exists():
                errors.append(f"{rel}: broken link -> {href}")

        # images
        for src in h.imgs:
            target = resolve(src)
            if target is None:
                if src.startswith("http"):
                    errors.append(f"{rel}: external image hotlink -> {src}")
                continue
            if not target.exists():
                errors.append(f"{rel}: missing image -> {src}")

    # sitemap coverage
    sm_path = ROOT / "sitemap.xml"
    if sm_path.exists():
        sm = sm_path.read_text(encoding="utf-8")
        for url in indexed:
            if f"<loc>https://www.tarotwithnisha.com{url}</loc>" not in sm:
                errors.append(f"sitemap.xml: missing {url}")
    else:
        errors.append("sitemap.xml missing")

    print(f"Checked {len(pages)} pages\n")
    if warnings:
        print(f"{len(warnings)} warning(s):")
        for w in warnings:
            print("  ! " + w)
        print()
    if errors:
        print(f"{len(errors)} error(s):")
        for e in errors:
            print("  x " + e)
        return 1
    print("No errors.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
