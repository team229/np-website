"""Shop hub, category pages and product pages."""
from __future__ import annotations

from components import (
    crumb_bar, cta_block, disclaimer_box, faq_block, page_hero, product_card,
    section_head, service_card, trust_bar,
)
from layout import (
    Page, attr, breadcrumb_schema, e, faq_schema, product_schema, wa, wa_btn,
)
from urllib.parse import quote

C = ("Shop", "/shop/")
OILS = ("Ritual Oils", "/shop/ritual-oils/")
CRYSTALS = ("Crystals & Bracelets", "/shop/crystals/")

PRODUCT_DISCLAIMER = (
    "<strong>Important.</strong> This is an intention-based spiritual product for personal ritual practice. "
    "It is not medicine and makes no medical, psychological or supernatural claim. For external use only. "
    "Patch-test before first use, keep away from children, and avoid contact with eyes. If you are pregnant, "
    "nursing or managing a health condition, speak to your doctor before use."
)


def product_page(
    *,
    path: str,
    url: str,
    name: str,
    meta_title: str,
    meta_desc: str,
    lede: str,
    price_main: str,
    price_note: str,
    variants: list,
    img: str,
    tag: str,
    description_html: str,
    howto_html: str,
    faqs: list,
    related: list,
    crumbs: list,
    category: str,
) -> Page:
    from components import crumb_bar
    from layout import breadcrumbs
    crumb_html = breadcrumbs(crumbs)

    variant_rows = ""
    if len(variants) > 1:
        opts = "".join(
            f'<option value="{attr(label)}">{e(label)} — {e(price)}</option>'
            for label, price in variants
        )
        variant_rows = f"""
        <label class="small muted" for="variant" style="display:block;margin-bottom:6px">Size</label>
        <select id="variant" name="variant"
          style="width:100%;max-width:260px;background:var(--ink);border:1px solid var(--line);color:var(--parchment);
                 padding:11px 12px;border-radius:3px;font-family:inherit;font-size:15px;margin-bottom:18px">
          {opts}
        </select>"""

    order_msg = f"Hi Nisha, I'd like to order the {name}"
    order_link = wa(order_msg, "product-order")

    body = crumb_bar(crumb_html)
    body += f"""
<section class="section">
  <div class="wrap">
    <div class="product-layout">
      <div class="product-gallery">
        <div class="main-img" style="background-image:url('{img}')"
             role="img" aria-label="{attr(name)}"></div>
      </div>

      <div>
        <span class="product-badge">{e(tag)}</span>
        <h1 class="product-title">{e(name)}</h1>
        <div class="product-price">₹{price_main} <small>incl. of all taxes</small></div>
        <p class="product-desc">{lede}</p>

        {variant_rows}

        <form class="product-actions" onsubmit="return false">
          <div class="qty-row">
            <span class="small muted">Quantity</span>
            <div class="qty">
              <button type="button" data-qty="down" aria-label="Decrease quantity">−</button>
              <input type="number" name="qty" value="1" min="1" max="20" aria-label="Quantity">
              <button type="button" data-qty="up" aria-label="Increase quantity">+</button>
            </div>
          </div>
          <a class="btn btn-gold btn-lg btn-block" href="{order_link}" target="_blank" rel="noopener"
             data-wa-service="{attr(name)}" data-wa-placement="product">
            Order on WhatsApp
          </a>
          <a class="btn btn-outline btn-block" href="{wa(f"a question about {name}", "product-question")}"
             target="_blank" rel="noopener">Ask a question first</a>
        </form>

        <div class="product-meta">
          <div><span class="k">Delivery</span><span>Pan-India, 3–7 working days</span></div>
          <div><span class="k">Payment</span><span>UPI or bank transfer, confirmed on WhatsApp</span></div>
          <div><span class="k">Ships from</span><span>India</span></div>
          <div><span class="k">Use</span><span>External ritual use only</span></div>
        </div>

      </div>
    </div>

    {disclaimer_box(PRODUCT_DISCLAIMER)}

    <div class="tabs">
      <div class="tab-buttons" role="tablist">
        <button class="tab-btn" role="tab" aria-selected="true" aria-controls="tab-desc" id="tabbtn-desc">Description</button>
        <button class="tab-btn" role="tab" aria-selected="false" aria-controls="tab-how" id="tabbtn-how">How to use</button>
        <button class="tab-btn" role="tab" aria-selected="false" aria-controls="tab-ship" id="tabbtn-ship">Shipping &amp; returns</button>
        <button class="tab-btn" role="tab" aria-selected="false" aria-controls="tab-dis" id="tabbtn-dis">Disclaimer</button>
      </div>
      <div class="tab-panel active" id="tab-desc" role="tabpanel" aria-labelledby="tabbtn-desc">
        {description_html}
      </div>
      <div class="tab-panel" id="tab-how" role="tabpanel" aria-labelledby="tabbtn-how">
        {howto_html}
      </div>
      <div class="tab-panel" id="tab-ship" role="tabpanel" aria-labelledby="tabbtn-ship">
        <p>Orders are confirmed on WhatsApp before payment. Once confirmed, dispatch is usually within 2 working
           days and delivery takes 3–7 working days depending on your location.</p>
        <p>Shipping is included in the price for addresses within India. For international delivery, message first
           and I'll quote the additional cost.</p>
        <p><strong>Returns:</strong> for hygiene and safety reasons, opened oils and worn crystals cannot be
           returned. If a parcel arrives damaged or the wrong item is sent, message within 48 hours with a photo
           and it will be replaced or refunded.</p>
      </div>
      <div class="tab-panel" id="tab-dis" role="tabpanel" aria-labelledby="tabbtn-dis">
        <p>This is an intention-based spiritual product for personal ritual practice. It is not medicine, and no
           medical, psychological or supernatural outcome is claimed or guaranteed.</p>
        <p>For external use only. Patch-test on a small area before first use. Keep away from children. Avoid
           contact with eyes and broken skin. If you are pregnant, nursing, or managing a health condition, speak
           to your doctor before use.</p>
        <p>By purchasing, you confirm you are 18 or older and using the product for personal spiritual practice.</p>
      </div>
    </div>
  </div>
</section>
"""
    body += f"""
<section class="section-tight">
  <div class="wrap">
    <h2 style="font-size:24px;margin-bottom:20px">Questions about this product</h2>
    {faq_block(faqs)}
  </div>
</section>
"""
    body += f"""
<section class="section-tight">
  <div class="wrap">
    <h2 style="font-size:24px;margin-bottom:20px">You might also like</h2>
    <div class="grid grid-3">
      {''.join(product_card(*r) for r in related)}
    </div>
  </div>
</section>
"""
    body += cta_block(
        "Not sure which one you need?",
        "Tell me what you're working on and I'll point you to the right oil or stone — or tell you if you don't "
        "need one at all.",
        service=f"question about {name}",
        secondary_label="Browse all products",
        secondary_href="/shop/",
    )

    schema_price = price_main.replace(",", "")
    return Page(
        path=path,
        url=url,
        title=meta_title,
        description=meta_desc,
        body=body,
        nav="shop",
        crumbs=crumbs,
        og_image=img,
        schema=[
            product_schema(name, meta_desc, url, schema_price, img),
            faq_schema(faqs),
            breadcrumb_schema(crumbs),
        ],
    )


# ============================================================ SHOP HUB

SHOP_FAQ = [
    ("How do I order?",
     "Message on WhatsApp with the product and quantity. I'll confirm availability, total and delivery time, then "
     "share payment details. Your order is dispatched after payment is confirmed."),
    ("Do you ship across India?",
     "Yes, pan-India. Delivery is usually 3–7 working days after dispatch. Shipping is included in the listed price."),
    ("Are these products safe to use on skin?",
     "They're formulated for external ritual use — typically a drop on the wrists, pulse points, or to dress a "
     "candle. Patch-test first. They are not for ingestion, and should be kept away from eyes and broken skin."),
    ("Can you guarantee the oil will work?",
     "No, and I won't pretend otherwise. These are intention-based products for personal practice. What they do is "
     "support focus and ritual — not produce guaranteed outcomes."),
    ("Do you offer bundles?",
     "Yes. Reading + oil bundles are the most popular and are listed on the individual service pages. Custom "
     "bundles can be arranged on WhatsApp."),
]

SHOP_BODY = page_hero(
    "Ritual Oils &amp; Crystals",
    "Intention-based products for your own practice — made in small batches, shipped pan-India. Not magic "
    "solutions; tools for focus and ritual.",
    '<nav class="breadcrumbs" aria-label="Breadcrumb"><a href="/">Home</a>'
    '<span class="sep">/</span><span aria-current="page">Shop</span></nav>',
    badges=["Pan-India delivery", "3–7 working days", "Small batch", "Intention-based"],
    cta_service="Ritual Oils enquiry", cta_label="Ask about a product", cta_secondary_href="",
) + f"""
{trust_bar()}

<section class="section">
  <div class="wrap">
    {section_head("Two collections", "Twenty ritual oils for anointing and candle work. Twelve crystal pieces for wearing and grounding.")}
    <div class="grid grid-2">
      {service_card("/shop/ritual-oils/", "Ritual Oils",
                    "Twenty intention oils — protection, money, love, cleansing, career and more. 10 ml and 20 ml.",
                    "From ₹799", "/images/cat-oils.webp", "Shop oils")}
      {service_card("/shop/crystals/", "Crystals &amp; Bracelets",
                    "Pyrite, rose quartz, black tourmaline, amethyst, selenite. Twelve pieces, honestly described.",
                    "From ₹599", "/images/cat-crystals.webp", "Shop crystals")}
    </div>
  </div>
</section>

<div class="divider"></div>

<section class="section">
  <div class="wrap">
    {section_head("All products", "")}
    <div class="grid grid-3">
      {product_card("/shop/ritual-oils/protection-oil/", "Protection Oil", "₹799", "/images/products/protection-oil.webp")}
      {product_card("/shop/ritual-oils/money-oil/", "Money Oil", "₹799", "/images/products/money-oil.webp")}
      {product_card("/shop/ritual-oils/love-attraction-oil/", "Love Attraction Oil", "₹799", "/images/products/love-oil.webp")}
      {product_card("/shop/crystals/pyrite-bracelet/", "Pyrite Bracelet", "₹599", "/images/products/pyrite-bracelet.webp", "Crystal")}
      {product_card("/shop/crystals/rose-quartz-bracelet/", "Rose Quartz Bracelet", "₹599", "/images/products/rose-quartz-bracelet.webp", "Crystal")}
      {product_card("/shop/ritual-oils/personalised-intention-oil/", "Personalised Intention Oil", "From ₹799", "/images/cat-oils.webp", "Custom blend")}
    </div>
  </div>
</section>

<div class="divider"></div>

<section class="section">
  <div class="wrap">
    {section_head("Before you order", "")}
    {faq_block(SHOP_FAQ)}
  </div>
</section>
""" + disclaimer_box(
    "<strong>A note on how these are described.</strong> Every product here is sold as an intention-based "
    "spiritual item for personal practice. Nothing is claimed to cure, treat or guarantee any outcome. If a "
    "seller tells you otherwise about a ritual oil, be careful."
) + cta_block(
    "Not sure what you need?",
    "Tell me what you're working on. I'll recommend something — or tell you that a reading would serve you better "
    "than a product.",
    secondary_label="See consultations",
)

SHOP = Page(
    path="shop/index.html",
    url="/shop/",
    title="Ritual Oils & Crystal Bracelets Online India | Tarot with Nisha",
    description=(
        "Intention-based ritual oils and crystal bracelets from Tarot with Nisha. Small batch, honestly described, "
        "shipped pan-India in 3–7 working days. From ₹599."
    ),
    h1="Ritual Oils & Crystals",
    body=SHOP_BODY,
    nav="shop",
    crumbs=[C],
    og_image="/images/cat-oils.webp",
    schema=[faq_schema(SHOP_FAQ), breadcrumb_schema([C])],
)


# ============================================================ OIL CATALOGUE

# (slug, name, subtitle, description, intention chips)
OIL_ITEMS = [
    ("protection-oil", "Protection Oil", "Protection &amp; Energetic Boundaries",
     "For those who want to bring spiritual protection into their personal rituals, meditation and "
     "intention-setting practice.",
     ["Personal protection rituals", "Energetic boundaries", "Spiritual grounding"]),
    ("negativity-removal-oil", "Negativity Removal Oil", "Cleansing &amp; Release",
     "For intentions centred on releasing unwanted emotional heaviness, letting go of stagnant energy and "
     "creating a fresh spiritual atmosphere.",
     ["Release and renewal", "Emotional reset", "Spiritual cleansing"]),
    ("love-attraction-oil", "Love Attraction Oil", "Love &amp; Connection",
     "For rituals focused on welcoming healthy love, emotional openness, self-love and meaningful romantic "
     "connection.",
     ["Love attraction intentions", "Self-love rituals", "Openness to connection"]),
    ("love-binding-oil", "Love Binding Oil", "Commitment &amp; Relationship Intentions",
     "A specialised oil for practices centred on commitment, devotion, relationship harmony and "
     "strengthening an existing bond. Intention-based spiritual practice — not a means of controlling "
     "another person's feelings or choices.",
     ["Commitment-focused rituals", "Relationship harmony", "Devotion and connection"]),
    ("money-oil", "Money Oil", "Wealth &amp; Financial Growth",
     "For prosperity rituals focused on financial opportunity, abundance, business growth and developing "
     "a mindset of possibility.",
     ["Money attraction intentions", "Business prosperity", "Financial opportunity"]),
    ("luck-oil", "Luck Oil", "Good Fortune &amp; New Opportunities",
     "For rituals centred on favourable opportunities, positive beginnings, confidence and welcoming good "
     "fortune.",
     ["Good luck rituals", "New beginnings", "Opportunity and success"]),
    ("charm-oil", "Charm Oil", "Personal Magnetism &amp; Charisma",
     "For rituals focused on confidence, personal presence, charm and feeling more comfortable and "
     "magnetic in social situations.",
     ["Personal magnetism", "Confidence and charisma", "Social and romantic appeal"]),
    ("fame-recognition-oil", "Fame &amp; Recognition Oil", "Visibility &amp; Public Recognition",
     "For intentions related to recognition, reputation, creative expression and being seen for your work "
     "and talents.",
     ["Public recognition", "Career visibility", "Creative success"]),
    ("peace-harmony-oil", "Peace &amp; Harmony Oil", "Calm &amp; Harmony at Home",
     "For intentions involving calm, harmony at home and more peaceful day-to-day interactions.",
     ["Household calm", "Peaceful interactions", "Emotional steadiness"]),
    ("success-career-oil", "Success &amp; Career Oil", "Professional Growth",
     "For professional growth, interviews, promotions, business ambitions and achievement-focused rituals.",
     ["Interviews and promotions", "Business ambition", "Achievement"]),
    ("opportunity-opener-oil", "Opportunity Opener Oil", "Fresh Starts &amp; New Possibilities",
     "For setting intentions around fresh starts, moving past perceived obstacles and noticing new "
     "possibilities.",
     ["Fresh starts", "Overcoming obstacles", "Noticing opportunity"]),
    ("self-love-beauty-oil", "Self-Love &amp; Beauty Oil", "Self-Worth &amp; Self-Care",
     "For self-worth, self-appreciation, confidence and personal-care rituals.",
     ["Self-worth", "Self-appreciation", "Personal care"]),
    ("intuition-oil", "Intuition &amp; Psychic Awareness Oil", "Meditation &amp; Intuition",
     "For meditation, tarot preparation, reflection and spiritual-intuition rituals.",
     ["Meditation", "Tarot preparation", "Reflection"]),
    ("aura-cleansing-oil", "Aura Cleansing Oil", "Cleansing &amp; Grounding",
     "For symbolic aura-cleansing rituals, grounding and setting a fresh personal intention. Distinct "
     "from Protection Oil, which comes after the clearing.",
     ["Aura cleansing", "Grounding", "Fresh intentions"]),
    ("business-client-attraction-oil", "Business &amp; Client Attraction Oil", "Growth &amp; Client Engagement",
     "For entrepreneurs, creators and service providers setting intentions around business growth and "
     "customer engagement.",
     ["Business growth", "Client engagement", "Visibility"]),
    ("reconciliation-oil", "Reconciliation &amp; Healing Bonds Oil", "Repair &amp; Forgiveness",
     "For reflection on repairing relationships, forgiveness, open communication and rebuilding trust "
     "where both people are willing.",
     ["Repairing relationships", "Forgiveness", "Open communication"]),
    ("confidence-courage-oil", "Confidence &amp; Courage Oil", "Self-Belief &amp; Assertiveness",
     "For intentions involving self-belief, courage, assertiveness and facing important decisions.",
     ["Self-belief", "Courage", "Assertiveness"]),
    ("victory-competition-oil", "Victory &amp; Competition Oil", "Competition &amp; Achievement",
     "For competitive situations, examinations, important presentations and achieving personal goals.",
     ["Exams and competitions", "Presentations", "Personal goals"]),
    ("dream-connection-oil", "Dream &amp; Spiritual Connection Oil", "Dreamwork &amp; Reflection",
     "For pre-meditation rituals, dream journaling and setting intentions for spiritual reflection.",
     ["Dream journaling", "Pre-meditation", "Spiritual reflection"]),
    ("abundance-blessings-oil", "Abundance &amp; Blessings Oil", "Gratitude &amp; Receiving",
     "For gratitude, a sense of abundance, receiving opportunities and welcoming positive developments.",
     ["Gratitude practice", "Receiving", "Welcoming good fortune"]),
]


OIL_PAGES = {"protection-oil", "money-oil", "love-attraction-oil", "personalised-intention-oil"}


def oil_card(slug, name, sub, desc, chips, priced=True) -> str:
    price = ('₹799 <small>10 ml · ₹1,299 for 20 ml</small>' if priced
             else 'From ₹1,499 <small>quoted after consultation</small>')
    title = (f'<a href="/shop/ritual-oils/{slug}/">{name}</a>'
             if slug in OIL_PAGES else name)
    return f"""
    <div class="cat-item" id="{slug}">
      <h3>{title}</h3>
      <span class="cat-sub">{sub}</span>
      <p>{desc}</p>
      <div class="chips">{''.join(f'<span class="chip">{c}</span>' for c in chips)}</div>
      <div class="cat-foot">
        <span class="cat-price">{price}</span>
        {wa_btn("Order", name, "catalogue", "btn btn-gold btn-sm")}
      </div>
    </div>"""


CRYSTAL_PAGES = {"pyrite-bracelet", "rose-quartz-bracelet"}


def crystal_card(slug, name, desc, price) -> str:
    title = (f'<a href="/shop/crystals/{slug}/">{name}</a>'
             if slug in CRYSTAL_PAGES else name)
    return f"""
    <div class="cat-item" id="{slug}">
      <h3>{title}</h3>
      <p>{desc}</p>
      <div class="cat-foot">
        <span class="cat-price">₹{price}</span>
        {wa_btn("Order", name, "catalogue", "btn btn-gold btn-sm")}
      </div>
    </div>"""


OILS_FAQ = [
    ("How do I choose between the oils?",
     "By intention, not by strength. If something feels heavy and unnamed, start with Negativity Removal or "
     "Aura Cleansing. Once it's clear, use Protection to hold the space. For money, career or love, pick the "
     "oil that names the thing you're actually working on. If you're torn, message me — I'd rather point you "
     "to one than sell you three."),
    ("What sizes are the oils available in?",
     "Every standard oil comes in 10 ml (₹799) and 20 ml (₹1,299). A 10 ml bottle lasts roughly two to three "
     "months with regular use."),
    ("Can I use more than one oil at a time?",
     "Yes, but not on the same area at once. Most people keep one for daily practice and use another for "
     "specific ritual work."),
    ("Do you make custom blends?",
     "Yes. The Personalised Intention Oil is blended around your situation after a short consultation — ₹799 "
     "for 10 ml, ₹1,299 for 20 ml, or ₹1,499 for a full situation-based blend."),
    ("Are these oils safe on skin?",
     "They're for external ritual use — a drop on the wrists, pulse points, or to dress a candle. Patch-test "
     "first. Not for ingestion, and keep away from eyes and broken skin."),
]

OILS_BODY = page_hero(
    "Ritual Oils",
    "Twenty intention-based oils, dressed for specific purposes. 10 ml ₹799 · 20 ml ₹1,299. Made in small "
    "batches, shipped pan-India.",
    '<nav class="breadcrumbs" aria-label="Breadcrumb"><a href="/">Home</a>'
    '<span class="sep">/</span><a href="/shop/">Shop</a>'
    '<span class="sep">/</span><span aria-current="page">Ritual Oils</span></nav>',
    badges=["20 oils", "10 ml ₹799", "20 ml ₹1,299", "Pan-India delivery"],
    cta_service="Ritual Oils enquiry", cta_label="Ask about an oil", cta_secondary_href="",
) + f"""
{trust_bar()}

<section class="section">
  <div class="wrap">
    {section_head("The collection", "Each oil is dressed for one intention. Order any of them on WhatsApp — "
                                    "or ask me which one fits.")}
    <div class="catalogue">
      {''.join(oil_card(*item) for item in OIL_ITEMS)}
    </div>
  </div>
</section>

<div class="divider"></div>

<section class="section">
  <div class="wrap">
    {section_head("Personalised blends", "For situations that don't fit a standard oil.")}
    <div class="catalogue">
      {oil_card(
        "personalised-intention-oil",
        "Personalised Intention Oil",
        "Custom Blend",
        "A custom intention blend built around your particular situation — relationships, career, confidence "
        "or a new chapter. Intentions are selected after a short personal consultation.",
        ["Chosen after consultation", "Blended to your situation", "10 ml or 20 ml"],
        priced=False,
      )}
    </div>
    <p class="small muted text-center mt-3">
      Personalised Intention Oil — 10 ml ₹799 · 20 ml ₹1,299 · Situation-Based Ritual Oil ₹1,499
    </p>
  </div>
</section>

<div class="divider"></div>

<section class="section">
  <div class="wrap">
    <div class="prose" style="max-width:76ch">
      <h2 style="margin-top:0">A note on how these are described</h2>
      <p>Every oil here is an intention-based spiritual product for personal ritual practice. None of them is "
         "claimed to produce a guaranteed outcome, and none is a substitute for medical care.</p>
      <p><strong>Love Binding Oil</strong> in particular is offered for commitment, devotion and harmony within "
         "an existing bond. It is not a means of influencing another person against their will, and I will "
         "decline any request framed that way.</p>
      <p>If you're working with a situation none of these names quite fit, the personalised blend exists for "
         "exactly that.</p>
    </div>
  </div>
</section>

<div class="divider"></div>

<section class="section">
  <div class="wrap">
    {section_head("Questions before you order", "")}
    {faq_block(OILS_FAQ)}
  </div>
</section>
""" + disclaimer_box(PRODUCT_DISCLAIMER) + cta_block(
    "Not sure which oil?",
    "Tell me what you're working on. I'll recommend one — or tell you that a reading would serve you better.",
    service="Ritual Oils enquiry",
)

OILS_CAT = Page(
    path="shop/ritual-oils/index.html",
    url="/shop/ritual-oils/",
    title="Ritual Oils Online India | 20 Intention Oils | From ₹799",
    description=(
        "Twenty intention-based ritual oils — protection, money, love, cleansing and more. 10 ml ₹799, 20 ml "
        "₹1,299. Small batch, shipped pan-India."
    ),
    h1="Ritual Oils",
    body=OILS_BODY,
    nav="shop",
    crumbs=[C, OILS],
    og_image="/images/cat-oils.webp",
    schema=[faq_schema(OILS_FAQ), breadcrumb_schema([C, OILS])],
)


# ============================================================ CRYSTALS CATALOGUE

CRYSTAL_ITEMS = [
    ("pyrite-bracelet", "Pyrite Bracelet",
     "Natural pyrite cube beads on elastic cord. Metallic gold facets that catch light — the most-worn piece "
     "for work and business contexts.", "599"),
    ("pyrite-anklet", "Pyrite Anklet",
     "The same natural pyrite, strung as an anklet. Worn for grounding through the day.", "699"),
    ("money-magnet-bracelet", "Money Magnet Bracelet",
     "A mixed-stone piece built around abundance intentions — pyrite and citrine-toned stones.", "899"),
    ("protection-bracelet", "Protection Bracelet",
     "A grounding combination for boundary intentions. Worn when you need to feel less affected by other "
     "people's energy.", "799"),
    ("black-tourmaline-bracelet", "Black Tourmaline Bracelet",
     "Matte black tourmaline beads. The simplest piece in the collection, and the one most people keep on "
     "daily.", "699"),
    ("tigers-eye-bracelet", "Tiger's Eye Bracelet",
     "Golden-brown chatoyant stones. Worn for steadiness before something that requires nerve.", "599"),
    ("tourmaline-tigers-eye-bracelet", "Black Tourmaline + Tiger's Eye",
     "Two stones in one piece — grounding and steadiness together. A common pairing for work weeks.", "799"),
    ("rose-quartz-bracelet", "Rose Quartz Bracelet",
     "Polished rose quartz in soft translucent pink. Worn for self-worth and openness, not for attracting a "
     "specific person.", "599"),
    ("amethyst-bracelet", "Amethyst Bracelet",
     "Violet amethyst beads, varied in translucency. Used in meditation and pre-reading rituals.", "699"),
    ("seven-chakra-bracelet", "Seven Chakra Bracelet",
     "Seven stones in one bracelet, one for each chakra. A broader piece for general practice.", "699"),
    ("selenite-door-hanging", "Selenite + Black Tourmaline Door Hanging",
     "A hanging piece for an entrance. Selenite with black tourmaline, on a natural cord.", "799"),
    ("selenite-charging-plate", "Selenite Charging Plate",
     "A flat selenite plate used to rest and cleanse other stones overnight.", "799"),
]

CRYSTALS_FAQ = [
    ("Are these natural stones?",
     "Yes. Colour, inclusions and shape vary from piece to piece — that's normal and is part of what makes each "
     "one different. No two are identical."),
    ("What size are the bracelets?",
     "Elasticated, roughly 16–19 cm, which fits most adult wrists. Message before ordering if you need a "
     "specific measurement."),
    ("How do I cleanse a stone?",
     "Cool water, pat dry, and rest it on a selenite plate or in indirect light. Avoid prolonged direct sun on "
     "amethyst and rose quartz, which can fade."),
    ("Do crystals have healing properties?",
     "They're used in spiritual practice for focus and intention. I won't claim they cure anything, and if "
     "you're managing a health condition you should see a doctor."),
]

CRYSTALS_BODY = page_hero(
    "Crystals &amp; Bracelets",
    "Twelve natural stone pieces for wearing, grounding and cleansing. Honestly described — no miracle claims.",
    '<nav class="breadcrumbs" aria-label="Breadcrumb"><a href="/">Home</a>'
    '<span class="sep">/</span><a href="/shop/">Shop</a>'
    '<span class="sep">/</span><span aria-current="page">Crystals &amp; Bracelets</span></nav>',
    badges=["12 pieces", "From ₹599", "Natural stone", "Pan-India delivery"],
    cta_service="Crystal enquiry", cta_label="Ask about a piece", cta_secondary_href="",
) + f"""
{trust_bar()}

<section class="section">
  <div class="wrap">
    {section_head("The collection", "Natural stone, simply described. Order on WhatsApp — or ask which one fits.")}
    <div class="catalogue">
      {''.join(crystal_card(*item) for item in CRYSTAL_ITEMS)}
    </div>
  </div>
</section>

<div class="divider"></div>

<section class="section">
  <div class="wrap">
    <div class="prose" style="max-width:76ch">
      <h2 style="margin-top:0">A note on how crystals actually get used</h2>
      <p>Crystals work best as physical reminders. A pyrite bracelet won't change your bank balance — but "
         "catching sight of it before a meeting can remind you to hold your nerve, and that's a real effect.</p>
      <p>That framing matters, because you'll find sellers promising a stone will fix a marriage or cure an "
         "illness. That isn't how this works, and I won't describe these pieces that way.</p>
      <h3>Common pairings</h3>
      <ul>
        <li><strong>Pyrite</strong> — work and business contexts, for focus and confidence.</li>
        <li><strong>Rose quartz</strong> — self-worth and openness; often paired with a love reading.</li>
        <li><strong>Black tourmaline</strong> — when you need to feel less affected by other people's energy.</li>
        <li><strong>Selenite</strong> — cleansing and resting other stones.</li>
      </ul>
    </div>
  </div>
</section>

<div class="divider"></div>

<section class="section">
  <div class="wrap">
    {section_head("Questions before you order", "")}
    {faq_block(CRYSTALS_FAQ)}
  </div>
</section>
""" + disclaimer_box(PRODUCT_DISCLAIMER) + cta_block(
    "Pair it with a reading",
    "Most clients buy a crystal to hold an intention set in a session. If that's what you're after, start with a "
    "reading and I'll suggest the right piece.",
    service="Crystal &amp; Reading Bundle",
    secondary_label="See consultations",
)

CRYSTALS_CAT = Page(
    path="shop/crystals/index.html",
    url="/shop/crystals/",
    title="Crystal Bracelets India | Pyrite, Quartz & More | ₹599",
    description=(
        "Natural crystal bracelets and stones — pyrite, rose quartz, black tourmaline, amethyst, selenite. "
        "Honestly described, shipped pan-India. From ₹599."
    ),
    h1="Crystals & Bracelets",
    body=CRYSTALS_BODY,
    nav="shop",
    crumbs=[C, CRYSTALS],
    og_image="/images/cat-crystals.webp",
    schema=[faq_schema(CRYSTALS_FAQ), breadcrumb_schema([C, CRYSTALS])],
)


# ============================================================ PRODUCTS

PROTECTION_FAQ = [
    ("When should I use protection oil instead of cleansing?",
     "Cleansing comes first. If something feels heavy or stagnant, clear it. Protection is for afterwards — holding "
     "your energy steady once the space is clear."),
    ("How do I apply it?",
     "A drop on each wrist or behind the ears before you go into a situation that drains you. Some people dress a "
     "candle with it instead. Either is fine."),
    ("Does it smell strong?",
     "It's a subtle, resinous blend — noticeable but not overpowering. If you're sensitive to fragrance, patch-test "
     "first."),
    ("Can I use it on children?",
     "No. These are adult products. For a child's room, a drop on a candle you burn yourself is more appropriate."),
]

PROTECTION = product_page(
    path="shop/ritual-oils/protection-oil/index.html",
    url="/shop/ritual-oils/protection-oil/",
    name="Protection Oil",
    meta_title="Protection Ritual Oil | Energetic Boundaries | 10ml & 20ml | ₹799",
    meta_desc=(
        "Protection ritual oil for boundary and grounding intentions. Small batch, 10ml ₹799 and 20ml ₹1,299. "
        "Pan-India delivery. Intention-based spiritual product."
    ),
    lede="An anointing oil dressed for boundary and grounding intentions — for the days you need to hold your "
         "energy steady rather than absorb everything around you.",
    price_main="799",
    price_note="10ml or 20ml",
    variants=[("10ml", "₹799"), ("20ml", "₹1,299")],
    img="/images/products/protection-oil.webp",
    tag="Ritual oil",
    description_html="""
      <p>Protection Oil is for the after, not the before. Once a space or a situation has been cleared, protection
         is what holds it steady — the difference between cleaning a room and locking the door.</p>
      <p>It's dressed with resinous, grounding botanicals in a base oil, and comes in a brass-capped dropper bottle.
         The scent is warm and slightly smoky — closer to incense than perfume.</p>
      <h3>Common intentions</h3>
      <ul>
        <li>Holding boundaries around a demanding workplace or family situation</li>
        <li>Grounding before or after a difficult conversation</li>
        <li>Feeling less affected by other people's moods</li>
        <li>Closing a ritual or cleansing practice</li>
      </ul>
      <p><strong>Sizes:</strong> 10ml (roughly 2–3 months of regular use) and 20ml.</p>
    """,
    howto_html="""
      <p><strong>Before you start:</strong> patch-test a small amount on your inner wrist and wait an hour.</p>
      <ol>
        <li><strong>Anoint:</strong> one drop on each wrist, or behind the ears, before entering a situation that
            tends to drain you.</li>
        <li><strong>Or dress a candle:</strong> a thin line down the candle, away from you, then light it and hold
            your intention for a few minutes.</li>
        <li><strong>Set the intention out loud.</strong> The oil is a cue, not the mechanism — naming what you're
            holding steady is the part that does the work.</li>
      </ol>
      <p>Store away from direct sunlight. External use only. Do not ingest.</p>
    """,
    faqs=PROTECTION_FAQ,
    related=[
        ("/shop/ritual-oils/money-oil/", "Money Oil", "₹799", "/images/products/money-oil.webp", "Ritual oil"),
        ("/shop/crystals/rose-quartz-bracelet/", "Rose Quartz Bracelet", "₹599", "/images/products/rose-quartz-bracelet.webp", "Crystal"),
        ("/shop/ritual-oils/love-attraction-oil/", "Love Attraction Oil", "₹799", "/images/products/love-oil.webp", "Ritual oil"),
    ],
    crumbs=[C, OILS, ("Protection Oil", "/shop/ritual-oils/protection-oil/")],
    category="Ritual Oil",
)

MONEY_FAQ = [
    ("Will this make money appear?",
     "No. It's an intention tool. What it does is keep your attention on opportunity and financial focus — which "
     "is a real thing, but not magic."),
    ("When should I use it?",
     "Commonly before work, before a negotiation, or during a ritual focused on a business goal. Some people dress "
     "a candle with it at the start of a new month."),
    ("Can I use it with the pyrite bracelet?",
     "Yes — that pairing is common. The bracelet is the reminder you wear; the oil is what you use deliberately."),
    ("Is it safe for sensitive skin?",
     "Patch-test first. If you react, stop using it on skin and use it to dress a candle instead."),
]

MONEY = product_page(
    path="shop/ritual-oils/money-oil/index.html",
    url="/shop/ritual-oils/money-oil/",
    name="Money Oil",
    meta_title="Money Ritual Oil | 10ml & 20ml | ₹799",
    meta_desc=(
        "Money ritual oil for abundance and financial-focus intentions. Small batch, 10ml ₹799 and 20ml ₹1,299. "
        "Pan-India delivery. Intention-based spiritual product."
    ),
    lede="An anointing oil dressed for financial focus and opportunity intentions. Not a money magnet — a "
         "deliberate pause before you make decisions about money.",
    price_main="799",
    price_note="10ml or 20ml",
    variants=[("10ml", "₹799"), ("20ml", "₹1,299")],
    img="/images/products/money-oil.webp",
    tag="Ritual oil",
    description_html="""
      <p>Money Oil is the most misunderstood product in the collection, so let's be precise: it does not attract
         money. What it does is create a deliberate moment around financial decisions — which, for most people, is
         exactly the missing piece.</p>
      <p>It's dressed with warm, resinous botanicals and a touch of citrus in a golden base oil. The scent is bright
         and slightly sweet.</p>
      <h3>Common intentions</h3>
      <ul>
        <li>Starting a new month or a new financial cycle deliberately</li>
        <li>Before a negotiation, pitch or pricing conversation</li>
        <li>Business rituals around client attraction and growth</li>
        <li>Shifting out of a scarcity mindset that's driving bad decisions</li>
      </ul>
      <p><strong>Sizes:</strong> 10ml and 20ml.</p>
    """,
    howto_html="""
      <p><strong>Before you start:</strong> patch-test on your inner wrist.</p>
      <ol>
        <li><strong>Anoint:</strong> a drop on each wrist before a workday, a negotiation, or a financial decision.</li>
        <li><strong>Or dress a candle:</strong> a thin line down the candle, then set one specific financial
            intention — a number, a goal, a conversation you've been avoiding.</li>
        <li><strong>Name it concretely.</strong> "More money" does nothing. "Send the invoice I've been putting off"
            does something.</li>
      </ol>
      <p>Store away from direct sunlight. External use only. Do not ingest.</p>
    """,
    faqs=MONEY_FAQ,
    related=[
        ("/shop/crystals/pyrite-bracelet/", "Pyrite Bracelet", "₹599", "/images/products/pyrite-bracelet.webp", "Crystal"),
        ("/shop/ritual-oils/protection-oil/", "Protection Oil", "₹799", "/images/products/protection-oil.webp", "Ritual oil"),
        ("/shop/ritual-oils/love-attraction-oil/", "Love Attraction Oil", "₹799", "/images/products/love-oil.webp", "Ritual oil"),
    ],
    crumbs=[C, OILS, ("Money Oil", "/shop/ritual-oils/money-oil/")],
    category="Ritual Oil",
)

LOVE_OIL_FAQ = [
    ("Will this attract a specific person?",
     "No. This is an oil for your own openness and self-worth — not for influencing someone else's feelings. If "
     "that's what you're looking for, I'd rather be upfront now."),
    ("Can I use it during a love reading?",
     "Yes. Some clients anoint a candle during a love-focused ritual, or wear it on the day of a reading to feel "
     "more settled."),
    ("Is it suitable if I'm already in a relationship?",
     "Yes. Many people use it for self-worth within an existing relationship, rather than for attraction."),
    ("How strong is the scent?",
     "Soft and floral — rose and a hint of something resinous. If you're sensitive to fragrance, patch-test first."),
]

LOVE_OIL = product_page(
    path="shop/ritual-oils/love-attraction-oil/index.html",
    url="/shop/ritual-oils/love-attraction-oil/",
    name="Love Attraction Oil",
    meta_title="Love Attraction Ritual Oil | 10ml & 20ml | ₹799",
    meta_desc=(
        "Love Attraction ritual oil for self-worth and openness intentions. Small batch, 10ml ₹799 and 20ml "
        "₹1,299. Pan-India delivery. Intention-based spiritual product."
    ),
    lede="A soft, floral anointing oil for self-worth and openness — for your own capacity to receive, not for "
         "influencing another person.",
    price_main="799",
    price_note="10ml or 20ml",
    variants=[("10ml", "₹799"), ("20ml", "₹1,299")],
    img="/images/products/love-oil.webp",
    tag="Ritual oil",
    description_html="""
      <p>Love Attraction Oil is about your side of the equation. The premise is simple: most people who struggle in
         relationships are not short of opportunities — they're short of the belief that they deserve a good one.</p>
      <p>It's dressed with rose and soft floral botanicals in a light base oil. The scent is gentle and warm.</p>
      <h3>Common intentions</h3>
      <ul>
        <li>Working on self-worth after a relationship has ended</li>
        <li>Opening to connection rather than chasing it</li>
        <li>Softening after a period of defensiveness</li>
        <li>A daily ritual of treating yourself with some care</li>
      </ul>
      <p><strong>What it isn't:</strong> a way to make a specific person want you. That isn't how this works, and I
         won't sell it that way.</p>
      <p><strong>Sizes:</strong> 10ml and 20ml.</p>
    """,
    howto_html="""
      <p><strong>Before you start:</strong> patch-test on your inner wrist.</p>
      <ol>
        <li><strong>Anoint:</strong> a drop on each wrist, or over the heart, as part of a morning routine.</li>
        <li><strong>Or dress a candle:</strong> a thin line down a pink or white candle, then set an intention about
            what you're opening to — not about a person.</li>
        <li><strong>Keep it about you.</strong> The useful intention is "I'm willing to be seen", not "he will
            come back".</li>
      </ol>
      <p>Store away from direct sunlight. External use only. Do not ingest.</p>
    """,
    faqs=LOVE_OIL_FAQ,
    related=[
        ("/shop/crystals/rose-quartz-bracelet/", "Rose Quartz Bracelet", "₹599", "/images/products/rose-quartz-bracelet.webp", "Crystal"),
        ("/shop/ritual-oils/protection-oil/", "Protection Oil", "₹799", "/images/products/protection-oil.webp", "Ritual oil"),
        ("/shop/ritual-oils/money-oil/", "Money Oil", "₹799", "/images/products/money-oil.webp", "Ritual oil"),
    ],
    crumbs=[C, OILS, ("Love Attraction Oil", "/shop/ritual-oils/love-attraction-oil/")],
    category="Ritual Oil",
)

PYRITE_FAQ = [
    ("Is pyrite real or treated?",
     "Natural pyrite. It's a metallic gold-flecked iron sulphide, which is why the facets catch light the way they "
         "do. No dye or plating."),
    ("Will it tarnish?",
     "Pyrite can dull slightly over time with skin contact. Wipe with a dry cloth. Avoid water and perfume."),
    ("What size is it?",
     "Elasticated, roughly 16–19cm — fits most adult wrists. Message if you need a specific measurement."),
    ("Can I wear it every day?",
     "Yes. Many people wear it as a work bracelet. Avoid wearing it in water or during heavy physical activity."),
]

PYRITE = product_page(
    path="shop/crystals/pyrite-bracelet/index.html",
    url="/shop/crystals/pyrite-bracelet/",
    name="Pyrite Bracelet",
    meta_title="Pyrite Bracelet Online India | Natural Stone | ₹599",
    meta_desc=(
        "Natural pyrite bead bracelet for focus and confidence intentions. Elasticated fit, ₹599, shipped "
        "pan-India in 3–7 working days."
    ),
    lede="Natural pyrite on a dark elastic cord. A wearable reminder for work and business contexts — not a "
         "wealth charm, whatever the internet says.",
    price_main="599",
    price_note="Elasticated fit",
    variants=[("One size", "₹599")],
    img="/images/products/pyrite-bracelet.webp",
    tag="Crystal bracelet",
    description_html="""
      <p>Pyrite is the stone people buy when they want to feel more capable. That's a reasonable thing to want,
         and it's also where the honest framing matters: the bracelet doesn't make you capable. It reminds you.</p>
      <p>This is a natural pyrite bead bracelet with irregular cube-cut stones — metallic gold-flecked facets that
         catch light from across a room. The variation between beads is natural, not a defect.</p>
      <h3>Common uses</h3>
      <ul>
        <li>Worn on workdays as a focus cue</li>
        <li>Paired with Money Oil for business rituals</li>
        <li>Bought as a gift for someone starting something new</li>
      </ul>
      <p><strong>Fit:</strong> elasticated, roughly 16–19cm. Fits most adult wrists.</p>
    """,
    howto_html="""
      <ol>
        <li><strong>Wear it deliberately.</strong> Put it on with a specific intention — for example, "I'll hold my
            nerve in this meeting".</li>
        <li><strong>Cleanse occasionally.</strong> Wipe with a dry cloth. Avoid water, perfume and prolonged
            sunlight.</li>
        <li><strong>Take it off for water.</strong> Pyrite dulls with repeated moisture contact.</li>
      </ol>
      <p>Natural stone varies in colour and pattern. No two bracelets are identical.</p>
    """,
    faqs=PYRITE_FAQ,
    related=[
        ("/shop/ritual-oils/money-oil/", "Money Oil", "₹799", "/images/products/money-oil.webp", "Ritual oil"),
        ("/shop/crystals/rose-quartz-bracelet/", "Rose Quartz Bracelet", "₹599", "/images/products/rose-quartz-bracelet.webp", "Crystal"),
        ("/shop/ritual-oils/protection-oil/", "Protection Oil", "₹799", "/images/products/protection-oil.webp", "Ritual oil"),
    ],
    crumbs=[C, CRYSTALS, ("Pyrite Bracelet", "/shop/crystals/pyrite-bracelet/")],
    category="Crystal Bracelet",
)

ROSE_FAQ = [
    ("Is the colour natural?",
     "Yes. Natural rose quartz varies from pale pink to a deeper blush. Some beads are more translucent than "
         "others — that's normal."),
    ("Can it fade?",
     "Prolonged direct sunlight can fade rose quartz over time. Store it away from a windowsill."),
    ("What size is it?",
     "Elasticated, roughly 16–19cm. Message if you need a specific measurement."),
    ("Is it suitable as a gift?",
     "Yes, and it's one of the most common gifts. Let me know if you'd like it packed as a gift."),
]

ROSE = product_page(
    path="shop/crystals/rose-quartz-bracelet/index.html",
    url="/shop/crystals/rose-quartz-bracelet/",
    name="Rose Quartz Bracelet",
    meta_title="Rose Quartz Bracelet Online India | Natural Stone | ₹599",
    meta_desc=(
        "Natural rose quartz bead bracelet for self-worth and openness intentions. Elasticated fit, ₹599, shipped "
        "pan-India in 3–7 working days."
    ),
    lede="Polished rose quartz on a soft elastic cord. Worn for self-worth and openness — not for making someone "
         "love you.",
    price_main="599",
    price_note="Elasticated fit",
    variants=[("One size", "₹599")],
    img="/images/products/rose-quartz-bracelet.webp",
    tag="Crystal bracelet",
    description_html="""
      <p>Rose quartz is the most over-promised stone in the market. You'll find sellers claiming it brings a soulmate
         or repairs a marriage. It doesn't do either, and describing it that way sets people up to be disappointed.</p>
      <p>What it is: a genuinely beautiful, soft pink stone that works well as a daily reminder to be less harsh
         with yourself. That's a modest claim, and it's the true one.</p>
      <h3>Common uses</h3>
      <ul>
        <li>Worn during a period of rebuilding self-worth</li>
        <li>Paired with the Love Attraction Oil or a love reading</li>
        <li>Given as a gift — it's the most-gifted piece in the collection</li>
      </ul>
      <p><strong>Fit:</strong> elasticated, roughly 16–19cm.</p>
    """,
    howto_html="""
      <ol>
        <li><strong>Wear it with a specific intention.</strong> "I'll speak to myself the way I'd speak to a
            friend" is a better intention than "I want love".</li>
        <li><strong>Cleanse gently.</strong> Cool water, pat dry. Avoid harsh chemicals.</li>
        <li><strong>Keep out of direct sun.</strong> Rose quartz fades with prolonged exposure.</li>
      </ol>
      <p>Natural stone varies in colour and translucency. No two bracelets are identical.</p>
    """,
    faqs=ROSE_FAQ,
    related=[
        ("/shop/ritual-oils/love-attraction-oil/", "Love Attraction Oil", "₹799", "/images/products/love-oil.webp", "Ritual oil"),
        ("/shop/crystals/pyrite-bracelet/", "Pyrite Bracelet", "₹599", "/images/products/pyrite-bracelet.webp", "Crystal"),
        ("/shop/ritual-oils/protection-oil/", "Protection Oil", "₹799", "/images/products/protection-oil.webp", "Ritual oil"),
    ],
    crumbs=[C, CRYSTALS, ("Rose Quartz Bracelet", "/shop/crystals/rose-quartz-bracelet/")],
    category="Crystal Bracelet",
)

PERSONALISED_FAQ = [
    ("How does the custom blend work?",
     "It starts with a short conversation about what you're working on. From that I choose the botanicals and "
     "the intention the blend is dressed for, and tell you exactly what's in it and how to use it."),
    ("How long does it take?",
     "Three to five days, because the blend is made after the consultation rather than pulled off a shelf."),
    ("What's the difference between the 10 ml, 20 ml and situation-based options?",
     "Size, mostly. The situation-based blend (₹1,499) is a larger, more involved formulation for a complex "
     "situation where more than one thing needs addressing."),
    ("Can you blend for a specific person?",
     "No. Blends are built around your own intention and practice, not for influencing someone else's choices."),
]

PERSONALISED = product_page(
    path="shop/ritual-oils/personalised-intention-oil/index.html",
    url="/shop/ritual-oils/personalised-intention-oil/",
    name="Personalised Intention Oil",
    meta_title="Personalised Intention Oil | Custom Ritual Blend | From ₹799",
    meta_desc=(
        "A custom intention oil blended around your situation after a short consultation. 10 ml ₹799, 20 ml "
        "₹1,299, situation-based ₹1,499. Shipped pan-India."
    ),
    lede="A custom blend built around your particular situation — relationships, career, confidence or a new "
         "chapter. Chosen after a short consultation, not picked from a shelf.",
    price_main="799",
    price_note="10 ml · 20 ml · situation-based",
    variants=[("10 ml", "₹799"), ("20 ml", "₹1,299"), ("Situation-based blend", "₹1,499")],
    img="/images/cat-oils.webp",
    tag="Custom blend",
    description_html="""
      <p>Most people who ask for a custom blend have already tried a standard oil and found it almost right.
         The situation has two or three strands to it, and no single intention covers all of them.</p>
      <p>This is the oil for that. We start with a short conversation — what you're working on, what you've
         already tried, and what you want the practice to actually do for you. From there I build the blend,
         tell you what's in it, and explain how to use it.</p>
      <h3>What you get</h3>
      <ul>
        <li>A blend chosen for your situation, not a generic intention</li>
        <li>A written note on what's in it and why</li>
        <li>Usage guidance — anointing, candle dressing, or both</li>
        <li>Made in 3–5 days, then shipped</li>
      </ul>
      <p><strong>Options:</strong> 10 ml ₹799 · 20 ml ₹1,299 · situation-based blend ₹1,499.</p>
    """,
    howto_html="""
      <p><strong>Before you start:</strong> patch-test on your inner wrist and wait an hour.</p>
      <ol>
        <li><strong>Read the note first.</strong> The blend is built around one intention — knowing what it is
            makes the practice more deliberate.</li>
        <li><strong>Anoint or dress a candle.</strong> A drop on each wrist, or a thin line down a candle away
            from you.</li>
        <li><strong>Name the intention.</strong> The oil is a cue. Naming what you're working toward is the part
            that does the work.</li>
      </ol>
      <p>Store away from direct sunlight. External use only. Do not ingest.</p>
    """,
    faqs=PERSONALISED_FAQ,
    related=[
        ("/shop/ritual-oils/protection-oil/", "Protection Oil", "₹799", "/images/products/protection-oil.webp", "Ritual oil"),
        ("/shop/ritual-oils/money-oil/", "Money Oil", "₹799", "/images/products/money-oil.webp", "Ritual oil"),
        ("/shop/crystals/pyrite-bracelet/", "Pyrite Bracelet", "₹599", "/images/products/pyrite-bracelet.webp", "Crystal"),
    ],
    crumbs=[C, OILS, ("Personalised Intention Oil", "/shop/ritual-oils/personalised-intention-oil/")],
    category="Ritual Oil",
)

PRODUCTS = [PROTECTION, MONEY, LOVE_OIL, PYRITE, ROSE, PERSONALISED]
