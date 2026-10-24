"""Homepage."""
from __future__ import annotations

from components import (
    cta_block, faq_block, hero, price_table, product_card, section_head,
    service_card, steps, trust_bar,
)
from layout import Page, faq_schema, wa_btn

SITUATIONS = [
    ("/consultations/tarot-readings/love/", "A relationship I can't read clearly",
     "Should I stay, wait, or let go?"),
    ("/consultations/tarot-readings/career/", "A career decision I keep postponing",
     "Switch, stay, negotiate, or start over?"),
    ("/consultations/numerology/marriage/", "Marriage &amp; compatibility questions",
     "Timing, matching, and family pressure."),
    ("/consultations/numerology/name/", "My name or a business name",
     "Spelling, correction, and number alignment."),
    ("/consultations/vedic-kundali/", "I want to understand my birth chart",
     "Kundali analysis and the year ahead."),
    ("/consultations/candle-rituals/", "Something feels heavy and I can't name it",
     "Clearing, protection, and intention work."),
]

FAQ = [
    ("Are these readings online or in person?",
     "Everything is online — by phone call or video call, whichever you prefer. Clients join from "
     "across India and abroad. You'll get a private, one-on-one session, not a chat with a team."),
    ("Do you read in Hindi?",
     "Yes. Readings are available in Hindi, English or a mix of both. Tell me which you'd prefer when "
     "you book and the whole session will be in that language."),
    ("How much does a reading cost?",
     "A single-question tarot reading starts at ₹599. A focused 45-minute reading is ₹1,299 and a full "
     "60-minute reading is ₹1,499. Numerology reports start at ₹299, kundali analysis is ₹600, and "
     "intention-based candle rituals start at ₹999. Exact pricing is always confirmed before you pay."),
    ("How soon can I get an appointment?",
     "Most weeks there are slots within 2–3 days. Message on WhatsApp with your situation and preferred "
     "time window and I'll confirm what's available."),
    ("Will you tell me exactly what's going to happen?",
     "No — and I'd be careful of anyone who does. A reading shows you where a situation actually stands, "
     "what you might be avoiding, and what your realistic options are. The decision stays yours."),
    ("Is what I share confidential?",
     "Completely. Nothing from a session is published or shared. The client messages you see on Instagram "
     "are shared by those clients themselves, with permission."),
]

BODY = (
    hero(
        h1="Online Tarot, Numerology &amp; Spiritual Guidance — Pan India",
        sub="Clarity for the decision you keep circling.",
        desc="Private one-on-one consultations with Nisha Pathak — tarot, numerology, Vedic kundali and "
             "intention-based rituals. Hindi or English, by phone or video, anywhere in India.",
        primary_label="Book a Consultation",
        secondary_label="Browse all services",
        tags=["7+ years", "1,600+ clients", "Hindi &amp; English", "100% confidential"],
    )
    + trust_bar()
    + f"""
<section class="section">
  <div class="wrap">
    {section_head("Start with what's actually on your mind",
                  "Most people arrive with a situation, not a service name. Pick the one that sounds closest.")}
    <div class="grid grid-3">
      {''.join(f'''
      <a class="link-card" href="{u}" style="padding:22px 22px 20px">
        <strong style="font-size:17px;line-height:1.35">{t}</strong>
        <span style="margin-top:6px">{d}</span>
        <span style="margin-top:12px;color:var(--gold);font-size:13px">See the right reading →</span>
      </a>''' for u, t, d in SITUATIONS)}
    </div>
  </div>
</section>

<div class="divider"></div>

<section class="section">
  <div class="wrap">
    {section_head("Consultations", "Four disciplines, one private conversation. Every session is built around your question.")}
    <div class="grid grid-4">
      {service_card("/consultations/tarot-readings/", "Tarot Readings",
                    "Love, career, and full readings. A grounded look at where things stand and what to do next.",
                    "From ₹599", "/images/cat-tarot.webp")}
      {service_card("/consultations/numerology/", "Numerology",
                    "Name, house, vehicle, marriage and baby-name numerology — reports delivered in 24–48 hours.",
                    "From ₹299", "/images/cat-numerology.webp")}
      {service_card("/consultations/vedic-kundali/", "Vedic Kundali &amp; Varshfal",
                    "Birth chart analysis, planetary placements, and the themes of your coming year.",
                    "From ₹300", "/images/cat-kundali.webp")}
      {service_card("/shop/ritual-oils/", "Ritual Oils &amp; Crystals",
                    "Intention-based oils, bracelets and cleansing tools for your own practice.",
                    "From ₹599", "/images/cat-oils.webp", "Shop the collection")}
    </div>
  </div>
</section>

<div class="divider"></div>

<section class="section">
  <div class="wrap">
    <div class="split split-wide-left">
      <div>
        {section_head("Why people book with Nisha", "", center=False)}
        <div class="prose" style="margin-top:14px">
          <p>Seven years of practice and more than 1,600 clients across India and internationally — but the
             reason people come back isn't the number. It's that the reading is honest.</p>
          <p>You won't be told what you want to hear. You'll be told what the cards, the numbers or the chart
             actually show, in plain language, with something concrete to do next.</p>
        </div>
        <ul class="checklist mt-3">
          <li><strong>Grounded, not theatrical.</strong> No fear-selling, no forced remedies, no "pay more to remove a curse".</li>
          <li><strong>Personalised.</strong> Your situation gets examined on its own terms, not matched to a template.</li>
          <li><strong>Transparent pricing.</strong> You know the cost before you pay. Nothing is added afterwards.</li>
          <li><strong>Hindi or English.</strong> The whole session in the language you think in.</li>
          <li><strong>Pan-India, by phone or video.</strong> From a metro or a small town — same access.</li>
          <li><strong>Confidential.</strong> What you share stays between the two of you.</li>
        </ul>
        <div class="mt-4">{wa_btn("Ask a question on WhatsApp", "", "home-why", "btn btn-gold")}</div>
      </div>
      <div class="split-img split-img-tall" style="background-image:url('/images/nisha-portrait.webp')"></div>
    </div>
  </div>
</section>

<div class="divider"></div>

<section class="section">
  <div class="wrap">
    {section_head("How a consultation works", "Three steps. No forms to fill, no packages to decode.")}
    {steps([
      ("01", "Message on WhatsApp", "Tell me in a couple of lines what's going on. I'll suggest the right reading — not the most expensive one."),
      ("02", "Confirm your slot", "Choose a time that works. Payment confirms the booking. You'll get the details straight away."),
      ("03", "Talk it through", "A private call or video session in Hindi or English. You leave with a clear read and next steps."),
    ])}
  </div>
</section>

<div class="divider"></div>

<section class="section">
  <div class="wrap">
    {section_head("What clients say", "Readings are private — the messages clients choose to share live on Instagram.")}
    <div class="test-private">
      <p class="quote">"Everything you tell me stays between us. That's why you won't find readings published
        here — but the messages clients send me afterwards are saved in my Instagram highlights."</p>
      <p class="who">— Nisha</p>
      <a href="https://www.instagram.com/tarotwithnisha/" target="_blank" rel="noopener"
         class="btn btn-outline btn-sm">See client messages on Instagram</a>
    </div>
  </div>
</section>

<div class="divider"></div>

<section class="section">
  <div class="wrap">
    {section_head("From the ritual collection", "Intention-based oils and crystals for your own practice. Pan-India delivery.")}
    <div class="grid grid-4">
      {product_card("/shop/ritual-oils/protection-oil/", "Protection Oil", "₹799", "/images/products/protection-oil.webp")}
      {product_card("/shop/ritual-oils/money-oil/", "Money Oil", "₹799", "/images/products/money-oil.webp")}
      {product_card("/shop/ritual-oils/love-attraction-oil/", "Love Attraction Oil", "₹799", "/images/products/love-oil.webp")}
      {product_card("/shop/crystals/pyrite-bracelet/", "Pyrite Bracelet", "₹599", "/images/products/pyrite-bracelet.webp", "Crystal")}
    </div>
    <div class="text-center mt-4">
      <a href="/shop/" class="btn btn-outline">View the full collection</a>
    </div>
  </div>
</section>

<div class="divider"></div>

<section class="section">
  <div class="wrap">
    {section_head("Common questions", "If yours isn't here, message me — I'll answer honestly, before you pay anything.")}
    {faq_block(FAQ)}
    <div class="text-center mt-4">
      <a href="/resources/faqs/" class="btn btn-outline">Read all FAQs</a>
    </div>
  </div>
</section>
"""
    + cta_block(
        "Not sure which reading you need?",
        "Send a couple of lines about your situation. I'll tell you which consultation fits — and if none of "
        "them do, I'll say so.",
        service="",
        secondary_label="See all consultations",
    )
)

PAGE = Page(
    path="index.html",
    url="/",
    title="Online Tarot, Numerology & Spiritual Guidance | Pan India",
    description=(
        "Private online tarot readings, numerology and Vedic kundali consultations with Nisha Pathak. "
        "7+ years, 1,600+ clients. Hindi & English, phone or video, pan-India. From ₹299."
    ),
    h1="Online Tarot, Numerology & Spiritual Guidance — Pan India",
    body=BODY,
    nav="home",
    schema=[faq_schema(FAQ)],
)
