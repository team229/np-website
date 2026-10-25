"""Reusable HTML components for the Tarot with Nisha site."""
from __future__ import annotations

from html import unescape

from layout import attr, e, wa, wa_btn


def txt(value: str) -> str:
    """Normalise a label that may already contain entities, then escape once.

    Lets content files write either "&" or "&amp;" without double-escaping.
    """
    return e(unescape(value))


def trust_bar() -> str:
    items = [
        ("✦", "7+ years of practice"),
        ("✦", "1,600+ clients served"),
        ("✦", "Hindi &amp; English"),
        ("✦", "Pan-India · phone or video"),
    ]
    return (
        '<div class="trust-bar"><ul>'
        + "".join(f'<li><span class="glyph">{g}</span>{t}</li>' for g, t in items)
        + "</ul></div>"
    )


def hero(
    h1: str,
    sub: str = "",
    desc: str = "",
    primary_label: str = "Book on WhatsApp",
    primary_service: str = "",
    secondary_label: str = "See consultations",
    secondary_href: str = "/consultations/",
    eyebrow: str = "Astrologer &amp; Psychic — Nisha Pathak",
    tags: list | None = None,
    bg: str = "/images/cat-tarot.webp",
    media_alt: str = "Tarot cards and candles on a reading table",
) -> str:
    tags_html = ""
    if tags:
        tags_html = '<div class="hero-tags">' + "".join(
            f'<span><i class="dot"></i>{t}</span>' for t in tags
        ) + "</div>"
    sub_html = f'<p class="sub">{sub}</p>' if sub else ""
    desc_html = f'<p class="desc">{desc}</p>' if desc else ""
    return f"""
<section class="hero">
  <div class="wrap hero-grid">
    <div class="hero-copy">
      <span class="eyebrow"><span class="rule"></span>{eyebrow}<span class="rule"></span></span>
      <h1>{h1}</h1>
      {sub_html}
      {desc_html}
      <div class="hero-ctas">
        {wa_btn(primary_label, primary_service, "hero")}
        <a href="{secondary_href}" class="btn btn-outline">{secondary_label}</a>
      </div>
      {tags_html}
    </div>
    <div class="hero-media" style="background-image:url('{bg}')"
         role="img" aria-label="{attr(media_alt)}"></div>
  </div>
</section>
"""


def page_hero(h1: str, lede: str, crumbs: str = "", badges: list | None = None,
              cta_service: str = "", cta_label: str = "Book on WhatsApp",
              cta_placement: str = "page-hero",
              cta_secondary_href: str = "#pricing") -> str:
    badge_html = ""
    if badges:
        badge_html = (
            '<div class="hero-tags" style="justify-content:flex-start;margin-top:16px">'
            + "".join(f'<span><i class="dot"></i>{b}</span>' for b in badges)
            + "</div>"
        )
    cta_html = ""
    if cta_service:
        secondary = ""
        if cta_secondary_href:
            secondary = f'<a href="{cta_secondary_href}" class="btn btn-outline">See pricing</a>'
        cta_html = (
            '<div class="hero-ctas" style="justify-content:flex-start;margin-top:24px">'
            + wa_btn(cta_label, cta_service, cta_placement)
            + secondary
            + "</div>"
        )
    return f"""
<section class="page-hero">
  <div class="wrap">
    {crumbs}
    <h1 style="margin-top:14px">{h1}</h1>
    <p class="lede">{lede}</p>
    {badge_html}
    {cta_html}
  </div>
</section>
"""


def crumb_bar(crumbs_html: str) -> str:
    """Slim breadcrumb strip for pages where the H1 lives further down."""
    return f'<div class="wrap" style="padding-top:18px">{crumbs_html}</div>'


def service_card(url: str, title: str, desc: str, price: str, img: str = "",
                 link_label: str = "Learn more") -> str:
    img_html = f'<div class="card-img" style="background-image:url(\'{img}\')"></div>' if img else ""
    return f"""
<a class="card" href="{url}">
  {img_html}
  <div class="card-body">
    <h3>{txt(title)}</h3>
    <p>{desc}</p>
    <div class="card-price">{price}</div>
    <span class="card-link">{link_label} <span aria-hidden="true">→</span></span>
  </div>
</a>"""


def product_card(url: str, title: str, price: str, img: str, tag: str = "Ritual oil") -> str:
    return f"""
<a class="product-card" href="{url}">
  <div class="thumb" style="background-image:url('{img}')"></div>
  <div class="p-body">
    <div class="p-tag">{txt(tag)}</div>
    <h3>{txt(title)}</h3>
    <div class="p-price">{price}</div>
  </div>
</a>"""


def price_table(headers: list, rows: list, popular_index: int | None = None) -> str:
    """rows: list of lists; each cell is either a string or (main, sub) tuple."""
    head = "".join(f"<th>{h}</th>" for h in headers)

    def cell(c):
        if isinstance(c, tuple):
            return f"{c[0]}<small>{c[1]}</small>"
        return c

    body = []
    for i, row in enumerate(rows):
        cls = ' class="popular"' if popular_index is not None and i == popular_index else ""
        cells = []
        for j, c in enumerate(row):
            klass = ' class="amount"' if j == len(row) - 1 else ""
            cells.append(f"<td{klass}>{cell(c)}</td>")
        body.append(f"<tr{cls}>{''.join(cells)}</tr>")
    return (
        '<div class="table-scroll"><table class="price-table">'
        f"<thead><tr>{head}</tr></thead><tbody>{''.join(body)}</tbody>"
        "</table></div>"
    )


def faq_block(faqs: list, open_first: bool = True) -> str:
    items = []
    for i, (q, a) in enumerate(faqs):
        opened = " open" if (open_first and i == 0) else ""
        items.append(f"""
    <div class="faq-item{opened}">
      <button class="faq-q" type="button" aria-expanded="{'true' if (open_first and i == 0) else 'false'}">
        <span>{e(q)}</span><span class="plus" aria-hidden="true">+</span>
      </button>
      <div class="faq-a"><p>{a}</p></div>
    </div>""")
    return f'<div class="faq">{"".join(items)}</div>'


def cta_block(title: str, text: str, service: str = "", secondary_label: str = "",
              secondary_href: str = "/consultations/") -> str:
    secondary = ""
    if secondary_label:
        secondary = f'<a href="{secondary_href}" class="btn btn-outline">{secondary_label}</a>'
    return f"""
<section class="section">
  <div class="wrap">
    <div class="cta-block">
      <h2>{title}</h2>
      <p>{text}</p>
      <div class="cta-row">
        {wa_btn("Book on WhatsApp", service, "cta")}
        {secondary}
      </div>
      <p class="small muted" style="margin-top:18px;margin-bottom:0">
        Usually replies within a few hours, 10am–8pm IST. Hindi &amp; English.
      </p>
    </div>
  </div>
</section>"""


def split_section(title: str, paras: list, img: str, bullets: list | None = None,
                  reverse: bool = False, cta: str = "", section_class: str = "section",
                  image_ratio: str = "") -> str:
    order = "split-wide-right" if reverse else "split-wide-left"
    bullet_html = ""
    if bullets:
        bullet_html = '<ul class="checklist mt-3">' + "".join(
            f"<li>{b}</li>" for b in bullets
        ) + "</ul>"
    p_html = "".join(f"<p>{p}</p>" for p in paras)
    ratio = " split-img-tall" if image_ratio == "tall" else ""
    img_el = f'<div class="split-img{ratio}" style="background-image:url(\'{img}\')"></div>'
    text_el = f"""
    <div>
      <h2>{title}</h2>
      <div class="prose" style="margin-top:14px">{p_html}{bullet_html}</div>
      {cta}
    </div>"""
    inner = (img_el + text_el) if not reverse else (text_el + img_el)
    return f"""
<section class="{section_class}">
  <div class="wrap">
    <div class="split {order}">
      {inner}
    </div>
  </div>
</section>"""


def disclaimer_box(text: str) -> str:
    return f'<div class="disclaimer-box">{text}</div>'


def section_head(title: str, sub: str = "", center: bool = True) -> str:
    if center:
        return f'<div class="sec-head"><h2>{title}</h2>' + (f"<p>{sub}</p>" if sub else "") + "</div>"
    return f'<div class="section-head-left"><h2>{title}</h2>' + (f"<p>{sub}</p>" if sub else "") + "</div>"


def steps(items: list) -> str:
    """items: list of (number, title, text)"""
    cells = "".join(f"""
      <div class="step" style="padding:22px 0;border-top:1px solid var(--line)">
        <div class="num" style="font-family:'Cormorant Garamond',serif;font-size:14px;color:var(--gold-ink);letter-spacing:.04em">{n}</div>
        <h3 style="font-size:20px;margin:8px 0 6px">{t}</h3>
        <p style="color:var(--muted);font-size:14.5px;margin:0">{d}</p>
      </div>""" for n, t, d in items)
    return f'<div class="grid grid-4" style="gap:0 28px">{cells}</div>'


def related_links(title: str, links: list) -> str:
    """links: list of (url, label, desc)"""
    cells = "".join(
        f'<a class="link-card" href="{u}"><strong>{txt(l)}</strong><span>{txt(d)}</span></a>'
        for u, l, d in links
    )
    return f"""
<section class="section-tight">
  <div class="wrap">
    <h2 style="font-size:24px;margin-bottom:20px">{title}</h2>
    <div class="grid grid-3">{cells}</div>
  </div>
</section>"""
