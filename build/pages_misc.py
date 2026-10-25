"""About, disclaimer, resources hub and 404."""
from __future__ import annotations

from components import (
    cta_block, faq_block, page_hero, service_card, steps, trust_bar,
)
from layout import (
    Page, breadcrumb_schema, faq_schema, wa_btn,
)

R = ("Resources", "/resources/")


# ============================================================ ABOUT

ABOUT_FAQ = [
    ("How long have you been reading?",
     "Seven years, and more than 1,600 clients across India and internationally. The practice started as a personal "
     "interest and became a full-time one."),
    ("Do you read for international clients?",
     "Yes. Sessions are online, so clients join from the US, UK, Canada, UAE and Singapore regularly. Pricing stays "
     "in INR and your bank handles conversion."),
    ("What disciplines do you work in?",
     "Tarot, numerology, Vedic kundali and varshfal, and intention-based candle rituals. I also make ritual oils and "
     "curate crystal pieces for clients' own practice."),
    ("Are you available for in-person sessions?",
     "No — everything is online by phone or video. That's deliberate: it means someone in a small town has the same "
     "access as someone in Mumbai."),
]

ABOUT_BODY = page_hero(
    "About Nisha Pathak",
    "Seven years of practice, more than 1,600 clients, and one consistent approach: tell people the truth about "
    "what the cards, numbers or chart actually show.",
    '<nav class="breadcrumbs" aria-label="Breadcrumb"><a href="/">Home</a>'
    '<span class="sep">/</span><span aria-current="page">About</span></nav>',
    badges=["7+ years", "1,600+ clients", "Hindi &amp; English", "Pan-India"],
) + f"""
{trust_bar()}

<section class="section">
  <div class="wrap">
    <div class="split split-wide-right" style="align-items:start">
      <div class="split-img" style="background-image:url('/images/nisha-portrait.webp');background-position:center 38%;aspect-ratio:1/1"></div>
      <div class="prose">
        <h2 style="margin-top:0">How this started</h2>
        <p>My introduction to tarot wasn't dramatic. It was curiosity that turned into study, and study that turned
           into something I couldn't put down. Over time it became clear that the useful part wasn't prediction —
           it was the way a reading could take something tangled and make it speakable.</p>
        <p>Seven years and more than 1,600 clients later, that's still the part I care about. People arrive with a
           situation they've been carrying for months. Often they already know what they need to do. What they
           don't have is language for it, or permission to trust it.</p>

        <h2>What I actually do</h2>
        <p>I read tarot, numerology and Vedic charts. Over the years I've also built a practice around
           intention-based rituals — candle work, and the oils and crystals that support it. Those exist because
           clients kept asking what they could do between sessions, and I wanted the answer to be something
           disciplined rather than a shopping list.</p>

        <h2>What I won't do</h2>
        <ul>
          <li><strong>Promise outcomes.</strong> No reading can guarantee what another person will do.</li>
          <li><strong>Sell fear.</strong> If something in your chart is difficult, you'll hear it plainly — but
              you won't be told you're in danger and need to pay to fix it.</li>
          <li><strong>Push remedies.</strong> I don't sell gemstones, which means I have no reason to recommend
              one.</li>
          <li><strong>Take bookings that won't help.</strong> If a lawyer, therapist or financial adviser is what
              you need, I'll say so.</li>
          <li><strong>Influence another person's will.</strong> Relationship work is about your side of it, always.</li>
        </ul>

        <h2>How I work</h2>
        <p>Every session is one-on-one, private, and in Hindi or English — whichever you think in. It's online, by
           phone or video, which means the same access whether you're in a metro or a small town.</p>
        <p>I keep the number of sessions per day limited. A reading given when I'm rushed is worse than no reading,
           and I'd rather turn down a booking than deliver one badly.</p>

        <blockquote><p>My job isn't to tell you what will happen. It's to make the situation clear enough that you
        can decide.</p></blockquote>
      </div>
    </div>
  </div>
</section>

<div class="divider"></div>

<section class="section-tight">
  <div class="wrap">
    <div class="link-card" style="cursor:default;display:grid;gap:10px;padding:24px 26px">
      <div><strong style="display:inline;font-size:15px;color:var(--gold)">WhatsApp</strong>
        <span style="display:inline;margin-left:10px">+91 87965 90763 — fastest, for bookings and questions</span></div>
      <div><strong style="display:inline;font-size:15px;color:var(--gold)">Email</strong>
        <span style="display:inline;margin-left:10px"><a href="mailto:nishak1410@gmail.com">nishak1410@gmail.com</a></span></div>
      <div><strong style="display:inline;font-size:15px;color:var(--gold)">Instagram</strong>
        <span style="display:inline;margin-left:10px"><a href="https://www.instagram.com/tarotwithnisha/" target="_blank" rel="noopener">@tarotwithnisha</a></span></div>
    </div>
  </div>
</section>

<div class="divider"></div>

<section class="section">
  <div class="wrap">
    <h2 style="font-size:28px;margin-bottom:24px">What I work with</h2>
    <div class="grid grid-4">
      {service_card("/consultations/tarot-readings/", "Tarot", "Love, career and full readings.", "From ₹599", "/images/cat-tarot.webp")}
      {service_card("/consultations/numerology/", "Numerology", "Name, house, vehicle and marriage.", "From ₹299", "/images/cat-numerology.webp")}
      {service_card("/consultations/vedic-kundali/", "Vedic Kundali", "Birth chart and year ahead.", "From ₹300", "/images/cat-kundali.webp")}
      {service_card("/consultations/candle-rituals/", "Candle Rituals", "Intention-based ritual work.", "From ₹999", "/images/cat-candles.webp")}
    </div>
  </div>
</section>

<div class="divider"></div>

<section class="section">
  <div class="wrap">
    <h2 style="font-size:28px;margin-bottom:8px">Questions people ask</h2>
    {faq_block(ABOUT_FAQ)}
  </div>
</section>
""" + cta_block(
    "Book a session",
    "Message with a couple of lines about your situation. I'll tell you which consultation fits — or if none does.",
)

ABOUT = Page(
    path="about/index.html",
    url="/about/",
    title="About Nisha Pathak | Tarot Reader & Numerologist | 7+ Years",
    description=(
        "Meet Nisha Pathak — tarot reader, numerologist and Vedic astrologer with 7+ years of practice and 1,600+ "
        "clients across India and internationally. Hindi & English, pan-India."
    ),
    h1="About Nisha Pathak",
    body=ABOUT_BODY,
    nav="about",
    crumbs=[("About", "/about/")],
    og_image="/images/nisha-portrait.webp",
    schema=[faq_schema(ABOUT_FAQ), breadcrumb_schema([("About", "/about/")])],
)


# ============================================================ RESOURCES HUB

RES_FAQ = [
    ("Do I need to read anything before booking?",
     "No. The guides exist for people who want to understand how this works before spending money. If you'd rather "
     "just talk, message me."),
    ("Can I ask a question that isn't answered here?",
     "Yes — message on WhatsApp. I answer before you pay anything, including when the answer is that a reading "
     "won't help."),
]

RES_BODY = page_hero(
    "Resources",
    "Plain-language guides and honest answers — so you can decide whether a reading is worth your money before "
    "you spend it.",
    '<nav class="breadcrumbs" aria-label="Breadcrumb"><a href="/">Home</a>'
    '<span class="sep">/</span><span aria-current="page">Resources</span></nav>',
    badges=["Written by Nisha", "No jargon", "Practical"],
) + f"""
<section class="section">
  <div class="wrap">
    <div class="grid grid-2">
      <a class="card" href="/resources/guides/">
        <div class="card-img" style="background-image:url('/images/cat-tarot.webp')"></div>
        <div class="card-body">
          <h3>Guides</h3>
          <p>Practical explanations of tarot, numerology and Vedic astrology — including what each one can't do.</p>
          <span class="card-link">Read the guides →</span>
        </div>
      </a>
      <a class="card" href="/resources/faqs/">
        <div class="card-img" style="background-image:url('/images/cat-candles.webp')"></div>
        <div class="card-body">
          <h3>FAQs</h3>
          <p>Pricing, delivery, confidentiality, and how sessions actually work.</p>
          <span class="card-link">See the FAQs →</span>
        </div>
      </a>
    </div>
  </div>
</section>

<div class="divider"></div>

<section class="section">
  <div class="wrap">
    <h2 style="font-size:26px;margin-bottom:8px">Common questions</h2>
    {faq_block(RES_FAQ)}
  </div>
</section>
""" + cta_block(
    "Prefer to just ask?",
    "You don't need to read anything first. Send a couple of lines and I'll tell you honestly whether a reading "
    "will help.",
)

RESOURCES = Page(
    path="resources/index.html",
    url="/resources/",
    title="Resources | Tarot & Numerology Guides and FAQs | Tarot with Nisha",
    description=(
        "Guides and FAQs on tarot, numerology and Vedic astrology — pricing, delivery, and honest answers about "
        "what a reading can and can't do."
    ),
    h1="Resources",
    body=RES_BODY,
    nav="resources",
    crumbs=[R],
    schema=[faq_schema(RES_FAQ), breadcrumb_schema([R])],
)


# ============================================================ DISCLAIMER

DISCLAIMER_BODY = page_hero(
    "Disclaimer",
    "What these services are, what they aren't, and what you're agreeing to. Written plainly, because it matters.",
    '<nav class="breadcrumbs" aria-label="Breadcrumb"><a href="/">Home</a>'
    '<span class="sep">/</span><span aria-current="page">Disclaimer</span></nav>',
) + """
<section class="section">
  <div class="wrap-narrow">
    <div class="prose">
      <p><em>Last updated: 24 October 2026</em></p>

      <h2>Guidance, not guarantees</h2>
      <p>Tarot readings, numerology, Vedic astrology and intention-based rituals are offered as tools for
         reflection and personal insight. They are not predictions of the future, and no outcome is guaranteed.
         Any decision you make after a consultation is your own.</p>

      <h2>Not medical, legal or financial advice</h2>
      <p>Nothing on this website or in any consultation constitutes medical, psychological, legal or financial
         advice. These services are not a substitute for treatment, diagnosis, legal counsel or professional
         financial planning. If you are facing a medical, legal or financial issue, please consult a qualified
         professional.</p>

      <h2>Mental health</h2>
      <p>A reading can offer emotional clarity, but it is not therapy and does not treat any condition. If you are
         experiencing significant distress, please contact a licensed mental health professional or a crisis
         helpline in your area. In India, Tele-MANAS is available on 14416.</p>

      <h2>Rituals and consent</h2>
      <p>All ritual work is intention-based spiritual practice. Rituals involving relationships respect the
         autonomy and consent of everyone involved. Requests to influence another person against their will are
         declined.</p>
      <p>Ritual outcomes are not guaranteed. What is offered is consistent, properly conducted practice — not a
         promised result.</p>

      <h2>Products</h2>
      <p>Ritual oils and crystals are sold as items for personal spiritual practice. They are not medicines and make
         no medical, psychological or supernatural claim.</p>
      <ul>
        <li>Oils are for external use only. Do not ingest.</li>
        <li>Patch-test on a small area before first use.</li>
        <li>Keep away from children and avoid contact with eyes and broken skin.</li>
        <li>If pregnant, nursing, or managing a health condition, consult your doctor before use.</li>
        <li>Natural stones vary in colour, pattern and shape. No two pieces are identical.</li>
      </ul>

      <h2>Age</h2>
      <p>Services and products are intended for adults aged 18 and over.</p>

      <h2>Confidentiality</h2>
      <p>Everything shared in a consultation is treated as confidential. Client messages shown on Instagram are
         shared by those clients themselves, with permission, and personal details are removed. Sessions may not be
         published or redistributed without consent.</p>

      <h2>Payments, cancellations and refunds</h2>
      <ul>
        <li>Sessions are confirmed on payment.</li>
        <li>Rescheduling is free with at least 4 hours' notice.</li>
        <li>Sessions are non-refundable once delivered.</li>
        <li>Products: opened oils and worn crystals cannot be returned for hygiene reasons. Damaged or incorrect
            items are replaced or refunded if reported within 48 hours with a photograph.</li>
      </ul>

      <h2>Third-party platforms</h2>
      <p>Bookings are coordinated over WhatsApp and payments made by UPI or bank transfer. Those platforms have
         their own terms, and their availability is outside our control.</p>

      <h2>Contact</h2>
      <p>Questions about anything here can be sent to
         <a href="mailto:nishak1410@gmail.com">nishak1410@gmail.com</a> or via WhatsApp on +91 87965 90763.</p>
    </div>
  </div>
</section>
""" + cta_block(
    "Questions about any of this?",
    "Message me before booking. I'd rather answer a question now than have you book something that isn't right "
    "for you.",
)

DISCLAIMER = Page(
    path="disclaimer/index.html",
    url="/disclaimer/",
    title="Disclaimer | Guidance, Products & Consent | Tarot with Nisha",
    description=(
        "What Tarot with Nisha's readings, rituals and products are and are not — including medical, legal and "
        "financial disclaimers, consent, and refund terms."
    ),
    h1="Disclaimer",
    body=DISCLAIMER_BODY,
    nav="",
    crumbs=[("Disclaimer", "/disclaimer/")],
    schema=[breadcrumb_schema([("Disclaimer", "/disclaimer/")])],
)


# ============================================================ 404

NOTFOUND_BODY = """
<section class="section" style="padding-top:88px;padding-bottom:88px">
  <div class="wrap-narrow text-center">
    <div style="font-family:'Cormorant Garamond',serif;font-size:64px;color:var(--gold);line-height:1">404</div>
    <h1 style="margin:14px 0 12px;font-size:32px">This page isn't here</h1>
    <p class="muted" style="max-width:44ch;margin:0 auto 28px">
      The link may be old, or the page may have moved. Here are the places people usually want.
    </p>
    <div class="cta-row">
      <a href="/consultations/" class="btn btn-gold">Browse consultations</a>
      <a href="/" class="btn btn-outline">Go to homepage</a>
    </div>
    <div class="grid grid-2 mt-4" style="text-align:left">
      <a class="link-card" href="/consultations/tarot-readings/">
        <strong>Tarot Readings</strong><span>Love, career and full readings</span></a>
      <a class="link-card" href="/consultations/numerology/">
        <strong>Numerology</strong><span>Name, house, vehicle and marriage</span></a>
      <a class="link-card" href="/shop/">
        <strong>Shop</strong><span>Ritual oils and crystals</span></a>
      <a class="link-card" href="/resources/faqs/">
        <strong>FAQs</strong><span>Pricing, delivery and how it works</span></a>
    </div>
  </div>
</section>
"""

NOTFOUND = Page(
    path="404.html",
    url="/404.html",
    title="Page not found | Tarot with Nisha",
    description="The page you were looking for isn't here. Browse consultations, numerology readings, ritual oils or the FAQ instead.",
    h1="Page not found",
    body=NOTFOUND_BODY,
    nav="",
    noindex=True,
)
