"""Vedic kundali, candle rituals and custom consultation pages."""
from __future__ import annotations

from components import (
    cta_block, disclaimer_box, faq_block, page_hero, price_table, related_links,
    section_head, steps, trust_bar,
)
from layout import Page, breadcrumb_schema, faq_schema, service_schema, wa_btn
from pages_tarot import service_page

C = ("Consultations", "/consultations/")


# ============================================================ KUNDALI

KUNDALI_FAQ = [
    ("Do I need my exact birth time?",
     "Yes — for kundali, birth time matters because the ascendant and house placements depend on it. If you don't "
     "have it, tell me what you do have and I'll tell you honestly how much can still be read."),
    ("What if my birth time is approximate?",
     "We work with it, and I'll flag which parts of the reading are less certain. Varshfal in particular is more "
     "forgiving than a full chart."),
    ("Is this the same as a kundali milan for marriage?",
     "No. Kundali milan is a separate matching process. I offer the individual chart analysis and varshfal here; "
     "for couple matching, message me and I'll tell you what's possible."),
    ("Do you recommend gemstones?",
     "Only where the chart supports it, and I'll always say when a gemstone isn't necessary. I don't sell "
     "gemstones, which means there's no incentive for me to recommend one."),
    ("How long does it take?",
     "Varshfal is usually 2–3 days. A full kundali analysis is 3–5 days depending on depth. If you have a "
     "deadline, tell me when you book."),
    ("Will you tell me about doshas?",
     "Yes, where they genuinely apply — and I'll explain what they mean in plain language rather than leaving you "
     "frightened by a term. Many 'doshas' are common and manageable, and I'll say so."),
]

KUNDALI_BODY = page_hero(
    "Vedic Kundali &amp; Varshfal",
    "Your birth chart read properly — placements, patterns, strengths and the year ahead. In plain language, "
    "without the fear-selling.",
    '<nav class="breadcrumbs" aria-label="Breadcrumb"><a href="/">Home</a>'
    '<span class="sep">/</span><a href="/consultations/">Consultations</a>'
    '<span class="sep">/</span><span aria-current="page">Vedic Kundali</span></nav>',
    badges=["From ₹300", "Delivered in 2–5 days", "Hindi &amp; English", "Plain-language report"],
) + f"""
{trust_bar()}

<section class="section">
  <div class="wrap">
    <div class="split split-wide-left" style="align-items:start">
      <div class="prose">
        <h2 style="margin-top:0">What a kundali reading actually covers</h2>
        <p>A birth chart is a map of where the planets sat at the moment you were born. Read well, it describes
           tendencies rather than events: how you handle pressure, where you tend to over-give, what kind of work
           suits you, and which areas of life require more deliberate effort.</p>
        <p>The problem with most kundali readings isn't the astrology — it's the delivery. Clients come away with
           Sanskrit terms, a list of doshas, and a shopping list of gemstones. That's not useful, and it's often
           frightening for no good reason.</p>
        <p>This reading is written in plain language. Every technical term gets explained. If something in your
           chart is genuinely difficult, you'll hear it directly — and you'll also hear what to do about it.</p>

        <h2>Two ways to work with your chart</h2>
        <h3 style="font-size:19px;margin-top:20px">Kundali Analysis — the full picture</h3>
        <p>Planetary placements, house analysis, strengths and challenges, and the life areas you asked about:
           career, relationships, finances, personal growth. Doshas are identified only where relevant and always
           explained.</p>
        <h3 style="font-size:19px;margin-top:20px">Varshfal — the year ahead</h3>
        <p>A focused annual reading. Major themes for the coming year, career and relationship trends, the periods
           worth pushing in, and the periods worth protecting. Most useful booked in December or January, but it
           works at any point in the year.</p>

        {disclaimer_box(
          "<strong>An honest note.</strong> I don't sell gemstones and I don't recommend expensive remedies. If "
          "the chart supports a simple practice — a mantra, a donation, a small ritual — I'll say so. If it "
          "doesn't, I'll say that too. Nobody should leave a reading feeling they must spend money to be safe."
        )}
      </div>
      <div>
        <div class="split-img" style="background-image:url('/images/cat-kundali.webp');aspect-ratio:1/1"></div>
        <div class="cta-block" style="padding:26px 22px;margin-top:18px">
          <h2 style="font-size:22px;margin-bottom:8px">Book a chart reading</h2>
          <p class="small" style="margin-bottom:16px">Send your date, time and place of birth to begin.</p>
          {wa_btn("Book on WhatsApp", "Vedic Kundali Analysis", "kundali-sidebar", "btn btn-gold btn-block")}
        </div>
      </div>
    </div>
  </div>
</section>

<div class="divider"></div>

<section class="section">
  <div class="wrap">
    {section_head("Pricing", "Reports are written, not read aloud from software.")}
    <div style="max-width:840px;margin:0 auto">
      {price_table(
        ["Service", "What it covers", "Price"],
        [
          ["Varshfal (Annual Horoscope)", ("Year ahead", "Themes, timing and areas needing attention"), "₹300"],
          ["Astrological Remedies &amp; Crystal Guidance", ("Guidance", "Simple practices where the chart supports them"), "₹500"],
          ["Vedic Kundali Analysis", ("Full chart", "Placements, houses, strengths, challenges"), "₹600"],
          ["Kundali + Varshfal Bundle", ("Both", "The full chart plus the year ahead"), "₹799"],
        ],
        2,
      )}
    </div>
    <p class="small muted text-center mt-3">
      Birth details required: date, exact time, and place of birth. Without a birth time, message first and I'll
      tell you what can still be read.
    </p>
  </div>
</section>

<div class="divider"></div>

<section class="section">
  <div class="wrap">
    {section_head("How it works", "")}
    {steps([
      ("01", "Send birth details", "Date, exact time, and place of birth."),
      ("02", "Confirm what you want", "Full chart, year ahead, or both. I'll quote before you pay."),
      ("03", "Receive your report", "Written analysis in plain language, usually within 3–5 days."),
    ])}
  </div>
</section>

<div class="divider"></div>

<section class="section">
  <div class="wrap">
    {section_head("Questions before you book", "")}
    {faq_block(KUNDALI_FAQ)}
  </div>
</section>
""" + related_links("Related", [
    ("/consultations/numerology/", "Numerology", "If you don't have a birth time, numbers still work"),
    ("/consultations/tarot-readings/", "Tarot Readings", "For a specific situation rather than the wider chart"),
    ("/consultations/candle-rituals/", "Candle Rituals", "Intention-based ritual support"),
]) + cta_block(
    "Book a kundali reading",
    "Send your date, time and place of birth. I'll confirm what can be read and the timeline before you pay.",
    service="Vedic Kundali Analysis",
)

KUNDALI = Page(
    path="consultations/vedic-kundali/index.html",
    url="/consultations/vedic-kundali/",
    title="Online Kundali Analysis & Varshfal India | Vedic Astrology | ₹600",
    description=(
        "Vedic kundali and varshfal with Nisha Pathak. Birth chart, placements, doshas and the year ahead, "
        "explained plainly. Hindi & English. From ₹300."
    ),
    h1="Vedic Kundali & Varshfal",
    body=KUNDALI_BODY,
    nav="consultations",
    crumbs=[C, ("Vedic Kundali", "/consultations/vedic-kundali/")],
    og_image="/images/cat-kundali.webp",
    schema=[
        service_schema("Vedic Kundali Analysis",
                       "Online Vedic birth chart analysis and annual varshfal reading.",
                       "/consultations/vedic-kundali/", price_low="300", category="Astrology Consultation"),
        faq_schema(KUNDALI_FAQ),
        breadcrumb_schema([C, ("Vedic Kundali", "/consultations/vedic-kundali/")]),
    ],
)


# ============================================================ CANDLE RITUALS

RITUAL_CATEGORIES = [
    ("Healing &amp; Self-Worth", "For emotional recovery, self-acceptance, and moving through a difficult transition."),
    ("Love &amp; Openness", "For opening to healthy connection and self-love. Never to influence a specific person."),
    ("Relationship Harmony", "For communication, mutual understanding, and rebuilding trust where both people are willing."),
    ("Money &amp; Abundance", "For financial intention-setting, business focus, and a less fearful relationship with money."),
    ("Career, Recognition &amp; Success", "For visibility, interviews, promotion intentions, and creative work."),
    ("Protection &amp; Boundaries", "For grounding, energetic boundaries, and a sense of personal security."),
    ("Release &amp; Cleansing", "For letting go of what has ended, and creating a fresher atmosphere."),
    ("Peace &amp; Emotional Balance", "For calm, resilience, and steadiness during a turbulent period."),
    ("Confidence &amp; Personal Power", "For self-belief, courage, and preparing for something that matters."),
    ("New Beginnings", "For transitions, fresh starts, and setting direction after a change."),
    ("Home &amp; Household Peace", "For a calmer living environment and easier day-to-day interactions."),
    ("Business &amp; Client Attraction", "For founders and practitioners setting intentions around growth and visibility."),
]

RITUAL_FAQ = [
    ("What actually happens during a candle ritual?",
     "We start with a consultation so I understand exactly what you're setting the intention for. Then I work the "
     "ritual daily for the agreed number of days, usually at a consistent time. At the end you get a short written "
     "summary of what came up during the work."),
    ("Do you guarantee a result?",
     "No. These are intention-based practices, and nobody can honestly guarantee an outcome. What I can promise is "
     "that the work is done properly, consistently, and with your specific situation in mind."),
    ("Can you do a ritual to bring a specific person back?",
     "No. I don't do work designed to override another person's choices. I do offer rituals for self-worth, "
     "release, and opening to healthy connection — which is often what people actually need."),
    ("How do I know it's working?",
     "Usually through shifts in your own clarity rather than dramatic external events. People often report "
     "sleeping better, feeling less stuck, or finally making a decision they'd been avoiding. If nothing shifts, "
     "I'll tell you honestly."),
    ("Is there a best day to start?",
     "Some people prefer to start on a new moon, a Tuesday, or a personally significant date. It isn't required. "
     "If timing matters to you, mention it during the consultation."),
    ("Do I need to do anything during the ritual days?",
     "You'll be given a simple daily practice — usually a few minutes of intention-setting. It isn't obligatory, "
     "but people who do it tend to get more from the process."),
    ("Are these rituals religious?",
     "No. They're intention-based spiritual practice, not tied to a specific religion. People of any faith — or "
     "none — use them."),
]

RITUAL_BODY = page_hero(
    "Intention-Based Candle Rituals",
    "Sustained ritual work over 3, 5, 7 or 21 days, planned around a specific situation. Not a magic switch — a "
    "disciplined practice.",
    '<nav class="breadcrumbs" aria-label="Breadcrumb"><a href="/">Home</a>'
    '<span class="sep">/</span><a href="/consultations/">Consultations</a>'
    '<span class="sep">/</span><span aria-current="page">Candle Rituals</span></nav>',
    badges=["From ₹999", "3–21 days", "Consultation included", "Written summary"],
) + f"""
{trust_bar()}

<section class="section">
  <div class="wrap">
    <div class="split split-wide-left" style="align-items:start">
      <div class="prose">
        <h2 style="margin-top:0">What this is — and what it isn't</h2>
        <p>A candle ritual is a structured, repeated intention practice. Over a set number of days, a candle is
           dressed, lit and worked with a specific focus. The repetition is the point: it holds attention on one
           thing long enough for something to shift.</p>
        <p>It is not a switch you flip to make another person act. It is not a substitute for a decision you're
           avoiding. And it is not something anyone can honestly guarantee.</p>
        <p>What clients most often report is a change in their own clarity — sleeping better, feeling less stuck,
           finally making a call they'd been circling for months. That's the realistic outcome, and it's usually
           the one that matters.</p>

        {disclaimer_box(
          "<strong>Important.</strong> These are spiritual, intention-based practices. Outcomes are not "
          "guaranteed. Rituals involving relationships respect the autonomy and consent of everyone involved — I "
          "will decline any request to influence another person against their will. Nothing here is medical, "
          "legal or financial advice."
        )}
      </div>
      <div>
        <div class="split-img" style="background-image:url('/images/cat-candles.webp');aspect-ratio:1/1"></div>
        <div class="cta-block" style="padding:26px 22px;margin-top:18px">
          <h2 style="font-size:22px;margin-bottom:8px">Discuss a ritual</h2>
          <p class="small" style="margin-bottom:16px">Start with a short consultation so the work is planned properly.</p>
          {wa_btn("Book a consultation", "Candle Ritual Consultation", "ritual-sidebar", "btn btn-gold btn-block")}
        </div>
      </div>
    </div>
  </div>
</section>

<div class="divider"></div>

<section class="section">
  <div class="wrap">
    {section_head("Durations &amp; energy exchange", "Longer rituals are not 'stronger' — they suit different situations.")}
    <div style="max-width:820px;margin:0 auto">
      {price_table(
        ["Duration", "Best for", "Price"],
        [
          ["3-Day Ritual", ("Focused intention", "A single clear focus or a short, sharp transition"), "₹999"],
          ["5-Day Ritual", ("Extended focus", "Situations that need a little more settling"), "₹1,599"],
          ["7-Day Ritual", ("Deeper work", "The most commonly chosen length — a full week of consistent practice"), "₹2,299"],
          ["21-Day Ritual", ("Extended practice", "Deep patterns, long transitions, a full cycle of change"), "₹5,999"],
        ],
        2,
      )}
    </div>
    <p class="small muted text-center mt-3">
      Personalised rituals for situations that don't fit a standard category start at ₹1,499 after consultation.
    </p>
  </div>
</section>

<div class="divider"></div>

<section class="section">
  <div class="wrap">
    {section_head("What rituals are available", "Every ritual is planned around your situation — these are the common focuses.")}
    <div class="grid grid-2">
      {''.join(f'''
      <div class="link-card" style="cursor:default">
        <strong>{t}</strong>
        <span>{d}</span>
      </div>''' for t, d in RITUAL_CATEGORIES)}
    </div>
    <p class="small muted text-center mt-3">
      If your situation doesn't fit any of these, that's what the custom consultation is for.
    </p>
  </div>
</section>

<div class="divider"></div>

<section class="section">
  <div class="wrap">
    {section_head("How it works", "")}
    {steps([
      ("01", "Consultation", "We talk through the situation so the intention is specific, not vague."),
      ("02", "The ritual days", "I work the ritual daily for the agreed duration. You get a simple daily practice."),
      ("03", "Closing summary", "A written summary of what came up, and what to watch for next."),
    ])}
  </div>
</section>

<div class="divider"></div>

<section class="section">
  <div class="wrap">
    {section_head("Questions before you book", "")}
    {faq_block(RITUAL_FAQ)}
  </div>
</section>
""" + related_links("Related", [
    ("/shop/ritual-oils/", "Ritual Oils", "Oils to support your own practice between sessions"),
    ("/consultations/vedic-kundali/", "Vedic Kundali", "Chart-based guidance and simple remedies"),
    ("/consultations/custom/", "Custom Consultation", "For situations that don't fit a standard ritual"),
]) + cta_block(
    "Start with a conversation",
    "Rituals begin with a short consultation — the intention has to be specific for the work to mean anything.",
    service="Candle Ritual Consultation",
)

RITUALS = Page(
    path="consultations/candle-rituals/index.html",
    url="/consultations/candle-rituals/",
    title="Candle Rituals Online India | 3–21 Days | From ₹999",
    description=(
        "Intention-based candle rituals with Nisha Pathak, worked over 3, 5, 7 or 21 days. Planned around your "
        "situation. Consultation included. Pan-India, online. From ₹999."
    ),
    h1="Intention-Based Candle Rituals",
    body=RITUAL_BODY,
    nav="consultations",
    crumbs=[C, ("Candle Rituals", "/consultations/candle-rituals/")],
    og_image="/images/cat-candles.webp",
    schema=[
        service_schema("Intention-Based Candle Ritual",
                       "Intention-based candle ritual practice over 3, 5, 7 or 21 days, planned around a specific situation.",
                       "/consultations/candle-rituals/", price_low="999", category="Spiritual Ritual"),
        faq_schema(RITUAL_FAQ),
        breadcrumb_schema([C, ("Candle Rituals", "/consultations/candle-rituals/")]),
    ],
)


# ============================================================ CUSTOM

CUSTOM_FAQ = [
    ("What counts as a custom consultation?",
     "Anything that doesn't fit the standard categories: several things happening at once, a decision with an "
     "unusual constraint, a business situation, or a question you're not sure how to frame. We start with a "
     "conversation and build the session from there."),
    ("How is it priced?",
     "After the initial conversation. Most custom sessions land between ₹1,499 and ₹3,500 depending on what's "
     "involved. I'll quote before you commit to anything."),
    ("Can it combine tarot and numerology?",
     "Yes — that's one of the most common custom requests. Combining a reading with a numbers analysis often "
     "gives a more complete picture than either alone."),
    ("What if you think a reading won't help?",
     "I'll say so, and I won't take the booking. That happens occasionally, and it's better for both of us than "
     "proceeding with something that won't serve you."),
]

CUSTOM_BODY = page_hero(
    "Custom Consultation",
    "For situations that don't fit a standard reading — several things at once, an unusual constraint, or a "
    "question you're not sure how to frame.",
    '<nav class="breadcrumbs" aria-label="Breadcrumb"><a href="/">Home</a>'
    '<span class="sep">/</span><a href="/consultations/">Consultations</a>'
    '<span class="sep">/</span><span aria-current="page">Custom Consultation</span></nav>',
    badges=["Quoted after consultation", "60–90 minutes", "Hindi &amp; English", "No obligation"],
) + f"""
{trust_bar()}

<section class="section">
  <div class="wrap">
    <div class="prose" style="max-width:78ch">
      <h2 style="margin-top:0">When a standard reading isn't the right fit</h2>
      <p>Most situations fit one of the standard services. But some don't. A few examples of what people bring here:</p>
      <ul>
        <li>A career decision tangled up with a family obligation</li>
        <li>A relationship question where the real issue is money, or a business</li>
        <li>A business partnership where two people want different things</li>
        <li>Several separate decisions that all seem connected</li>
        <li>A question they can't articulate yet and need help shaping</li>
      </ul>
      <p>For these, we start with a conversation. If a standard service covers it, I'll point you there — it's
         cheaper and faster. If it genuinely needs something custom, I'll propose a format and a price.</p>

      <h2>What a custom session can include</h2>
      <ul class="checklist">
        <li>Tarot reading combined with numerology analysis</li>
        <li>A kundali view alongside a tarot read</li>
        <li>Ritual planning for a complex situation</li>
        <li>An extended session (90 minutes) for multiple connected questions</li>
        <li>A written summary you can refer back to</li>
      </ul>

      {disclaimer_box(
        "<strong>An honest note.</strong> I won't take a booking I don't think will help. If the situation calls "
        "for a lawyer, a therapist or a financial adviser, I'll say so — and I won't dress that up as spiritual "
        "guidance."
      )}
    </div>
  </div>
</section>

<div class="divider"></div>

<section class="section">
  <div class="wrap">
    {section_head("How it works", "")}
    {steps([
      ("01", "Message with the situation", "A few lines is enough to start."),
      ("02", "Get a proposal", "I'll suggest a format and a price. No obligation to proceed."),
      ("03", "Book if it fits", "Pay to confirm, then meet for the session."),
    ])}
  </div>
</section>

<div class="divider"></div>

<section class="section">
  <div class="wrap">
    {section_head("Questions before you book", "")}
    {faq_block(CUSTOM_FAQ)}
  </div>
</section>
""" + related_links("Related", [
    ("/consultations/tarot-readings/", "Tarot Readings", "If one clear question is the main thing"),
    ("/consultations/numerology/", "Numerology", "If you want a pattern view rather than a situation view"),
    ("/consultations/candle-rituals/", "Candle Rituals", "If the work is about sustained intention"),
]) + cta_block(
    "Describe the situation",
    "Tell me what's going on. I'll tell you whether a standard reading covers it or whether something custom makes sense.",
    service="Custom Consultation",
)

CUSTOM = Page(
    path="consultations/custom/index.html",
    url="/consultations/custom/",
    title="Custom Tarot & Numerology Consultation | India",
    description=(
        "Custom online consultation for situations that don't fit a standard reading. Combined tarot, numerology "
        "and ritual planning with Nisha Pathak. Pan-India."
    ),
    h1="Custom Consultation",
    body=CUSTOM_BODY,
    nav="consultations",
    crumbs=[C, ("Custom Consultation", "/consultations/custom/")],
    og_image="/images/cat-tarot.webp",
    schema=[
        service_schema("Custom Consultation",
                       "Bespoke online consultation combining tarot, numerology and ritual planning for complex situations.",
                       "/consultations/custom/", category="Consultation"),
        faq_schema(CUSTOM_FAQ),
        breadcrumb_schema([C, ("Custom Consultation", "/consultations/custom/")]),
    ],
)
