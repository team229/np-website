"""Consultation hub, category pages and individual service pages."""
from __future__ import annotations

from components import (
    cta_block, disclaimer_box, faq_block, page_hero, price_table, related_links,
    section_head, service_card, steps, trust_bar,
)
from layout import Page, breadcrumb_schema, faq_schema, service_schema, wa, wa_btn


def service_page(
    *,
    path: str,
    url: str,
    nav: str,
    crumbs: list,
    h1: str,
    meta_title: str,
    meta_desc: str,
    lede: str,
    img: str,
    price_from: str,
    price_note: str,
    who: list,
    includes: list,
    process: list,
    pricing_headers: list,
    pricing_rows: list,
    popular: int | None,
    faqs: list,
    related: list,
    schema_name: str,
    schema_desc: str,
    schema_price: str | None = None,
    schema_low: str | None = None,
    extra: str = "",
    disclaimer: str = "",
    cta_title: str = "",
    cta_text: str = "",
) -> Page:
    crumb_html = ""
    from layout import breadcrumbs
    crumb_html = breadcrumbs(crumbs)

    body = page_hero(h1, lede, crumb_html,
                     badges=[f"From {price_from}", price_note],
                     cta_service=schema_name)
    body += f"""
<section class="section">
  <div class="wrap">
    <div class="split split-wide-left" style="align-items:start">
      <div class="prose">
        <h2 style="margin-top:0">Who this is for</h2>
        <ul class="checklist">
          {''.join(f'<li>{w}</li>' for w in who)}
        </ul>
        <h2>What's included</h2>
        <ul class="checklist">
          {''.join(f'<li>{i}</li>' for i in includes)}
        </ul>
        {disclaimer_box(disclaimer) if disclaimer else ''}
      </div>
      <div>
        <div class="split-img" style="background-image:url('{img}');aspect-ratio:1/1"></div>
        <div class="cta-block" style="padding:26px 22px;margin-top:18px">
          <h2 style="font-size:22px;margin-bottom:8px">Book this consultation</h2>
          <p class="small" style="margin-bottom:16px">Message with your situation and I'll confirm availability.</p>
          {wa_btn("Book on WhatsApp", schema_name, "service-sidebar", "btn btn-gold btn-block")}
        </div>
      </div>
    </div>
  </div>
</section>

<div class="divider"></div>

<section class="section">
  <div class="wrap">
    {section_head("How it works", "Simple, private, and built around your actual question.")}
    {steps(process)}
  </div>
</section>

<div class="divider"></div>

<section class="section" id="pricing">
  <div class="wrap">
    {section_head("Pricing", "Confirmed before you pay. No add-ons afterwards.")}
    <div style="max-width:820px;margin:0 auto">
      {price_table(pricing_headers, pricing_rows, popular)}
      <p class="small muted text-center mt-3">
        Prices in INR. Sessions are by phone or video. Payment confirms your slot.
      </p>
    </div>
  </div>
</section>

{extra}

<div class="divider"></div>

<section class="section">
  <div class="wrap">
    {section_head("Questions about this reading", "")}
    {faq_block(faqs)}
  </div>
</section>
"""
    body += related_links("You might also consider", related)
    body += cta_block(
        cta_title or "Ready when you are",
        cta_text or "Send a couple of lines about your situation. I'll confirm the right reading and the "
                    "next available slot.",
        service=schema_name,
    )

    return Page(
        path=path,
        url=url,
        title=meta_title,
        description=meta_desc,
        body=body,
        nav=nav,
        crumbs=crumbs,
        og_image=img,
        schema=[
            service_schema(schema_name, schema_desc, url, schema_price, schema_low),
            faq_schema(faqs),
            breadcrumb_schema(crumbs),
        ],
    )


# ============================================================ HUB

HUB_FAQ = [
    ("How do I know which consultation to book?",
     "Message on WhatsApp with a couple of sentences about your situation. I'll point you to the right one — "
     "and if a reading isn't the right tool for what you're facing, I'll tell you that instead."),
    ("Can I combine two services?",
     "Yes. Tarot plus numerology, or kundali plus a candle ritual, are common combinations. Bundled pricing is "
     "available and I'll quote it before you commit to anything."),
    ("Are consultations available outside India?",
     "Yes. Sessions are online, so clients join from the US, UK, Canada, UAE and Singapore regularly. Pricing "
     "stays in INR; your bank handles the conversion."),
    ("What language are sessions in?",
     "Hindi, English, or a mix of both. Tell me your preference when booking and the whole session — including "
     "the follow-up — will be in that language."),
    ("How long does a consultation take?",
     "Tarot readings are 20–60 minutes depending on what you book. Numerology is a written report delivered in "
     "24–48 hours, with an optional call. Kundali analysis takes 2–4 days. Candle rituals run 3–21 days with a "
     "consultation before and a summary after."),
]

HUB_BODY = page_hero(
    "Consultations",
    "Every session is private, one-on-one, and built around a real question. Choose a discipline — or start "
    "with your situation and I'll point you to the right one.",
    '<nav class="breadcrumbs" aria-label="Breadcrumb"><a href="/">Home</a>'
    '<span class="sep">/</span><span aria-current="page">Consultations</span></nav>',
    badges=["7+ years", "1,600+ clients", "Hindi &amp; English", "Phone or video"],
) + f"""
{trust_bar()}

<section class="section">
  <div class="wrap">
    {section_head("Choose a discipline", "Not sure? Send your situation on WhatsApp and I'll recommend one.")}
    <div class="grid grid-2">
      {service_card("/consultations/tarot-readings/", "Tarot Readings",
                    "Sessions with unlimited questions, per-question voice notes, and specialised readings.",
                    "From ₹51", "/images/cat-tarot.webp")}
      {service_card("/consultations/numerology/", "Numerology",
                    "Name, house, vehicle, marriage and baby-name analysis. Delivered as a written report.",
                    "From ₹299", "/images/cat-numerology.webp")}
      {service_card("/consultations/vedic-kundali/", "Vedic Kundali &amp; Varshfal",
                    "Birth chart analysis, doshas, remedies, and a year-ahead reading.",
                    "From ₹300", "/images/cat-kundali.webp")}
      {service_card("/consultations/candle-rituals/", "Candle Rituals",
                    "Intention-based ritual work over 3, 5, 7 or 21 days, planned around your situation.",
                    "From ₹999", "/images/cat-candles.webp")}
    </div>
    <div class="grid grid-2 mt-4">
      {service_card("/consultations/custom/", "Custom Consultation",
                    "For situations that don't fit a standard reading — transitions, decisions, or several things at once.",
                    "Quoted after a short conversation", "/images/cat-tarot.webp")}
      {service_card("/shop/", "Ritual Oils &amp; Crystals",
                    "Products for your own practice — oils, bracelets, and cleansing tools. Pan-India delivery.",
                    "From ₹599", "/images/cat-crystals.webp", "Shop now")}
    </div>
  </div>
</section>

<div class="divider"></div>

<section class="section">
  <div class="wrap">
    {section_head("How consultations work", "The same three steps for every service.")}
    {steps([
      ("01", "Message first", "Tell me what's going on in a couple of lines. No forms, no questionnaires."),
      ("02", "Get a recommendation", "I'll suggest one service and quote the exact price. You decide from there."),
      ("03", "Book and connect", "Pay to confirm your slot, then join a private call or video at the agreed time."),
    ])}
  </div>
</section>

<div class="divider"></div>

<section class="section">
  <div class="wrap">
    {section_head("Before you book", "")}
    {faq_block(HUB_FAQ)}
  </div>
</section>
""" + cta_block(
    "Tell me what's going on",
    "One message is usually enough for me to point you to the right consultation — and to tell you honestly "
    "if a reading won't help.",
)

HUB = Page(
    path="consultations/index.html",
    url="/consultations/",
    title="Online Consultations | Tarot, Numerology & Kundali | Pan India",
    description=(
        "Private online consultations with Nisha Pathak — tarot readings, numerology, Vedic kundali and "
        "intention-based candle rituals. Hindi & English, pan-India. From ₹299."
    ),
    h1="Consultations",
    body=HUB_BODY,
    nav="consultations",
    crumbs=[("Consultations", "/consultations/")],
    schema=[faq_schema(HUB_FAQ), breadcrumb_schema([("Consultations", "/consultations/")])],
)


# ============================================================ TAROT CATEGORY

TAROT_FAQ = [
    ("What does 'unlimited questions' actually mean?",
     "It means you can bring as many questions as you can fit into your booked time. A 15-minute reading "
     "usually covers one or two; a 60-minute reading often covers five or more. The limit is the clock, not a "
     "question count."),
    ("Should I book a session or a per-question reading?",
     "If your situation has several strands, or you want to talk it through, book a session — you can react to "
     "what comes up. If you have one specific question and just want the answer, the voice-note reading is "
     "cheaper and faster."),
    ("How are voice-note readings delivered?",
     "As a voice note on WhatsApp, or a DM on Instagram if you prefer. You'll have it within 24–48 hours, "
     "depending on how full the schedule is. You can reply with a follow-up question about the same reading."),
    ("Do you read in Hindi?",
     "Yes — Hindi, English, or a mix. Tell me when you book and the whole reading will be in that language."),
    ("What if I don't know what to ask?",
     "Very common. Send me a couple of lines about what's going on and I'll help you shape it into a question "
     "that will actually produce something useful. That shaping is often half the value."),
    ("Will you tell me exactly what's going to happen?",
     "No. A reading shows where a situation stands, what you might be avoiding, and what your realistic options "
     "are. It doesn't give you a guaranteed outcome, and I won't pretend otherwise."),
    ("Can I get a refund if the reading doesn't resonate?",
     "Readings are non-refundable once delivered. If something isn't landing, tell me — I'd rather understand "
     "what went wrong than leave it. Rescheduling a live session is free with 4 hours' notice."),
    ("Are the specialised readings different from a session?",
     "They're focused readings on a defined theme — love, career, or personal guidance. Each has a set price "
     "and can be delivered as a voice note or as a live session, whichever suits you."),
]


def _spec_card(name, desc, price, slug):
    link = wa(name, "tarot-" + slug)
    return (
        '<div class="cat-item" id="' + slug + '">'
        "<h3>" + name + "</h3>"
        "<p>" + desc + "</p>"
        '<div class="cat-foot">'
        '<span class="cat-price">₹' + price + "</span>"
        '<a class="btn btn-gold btn-sm" href="' + link + '" target="_blank" rel="noopener"'
        ' data-wa-service="' + name + '" data-wa-placement="tarot-' + slug + '">Book</a>'
        "</div></div>"
    )


def _package_card(name, what, price, featured=False):
    cls = "cat-item featured" if featured else "cat-item"
    badge = ('<span class="cat-sub">Best value</span>' if featured
             else '<span class="cat-sub">Package</span>')
    link = wa("the " + name + " tarot package", "tarot-package")
    return "".join([
        '<div class="' + cls + '">',
        "<h3>" + name + "</h3>",
        badge,
        "<p>" + what + "</p>",
        '<div class="cat-foot">',
        '<span class="cat-price">₹' + price + "</span>",
        '<a class="btn btn-gold btn-sm" href="' + link + '" target="_blank" rel="noopener"'
        ' data-wa-service="' + name + ' package" data-wa-placement="tarot-package">Book</a>',
        "</div></div>",
    ])


SPEC_LOVE = "".join([
    _spec_card("Love &amp; Relationship Reading",
               "A focused read on where the relationship currently stands and what you're actually dealing with.",
               "251", "love-relationship"),
    _spec_card("Their Thoughts, Feelings &amp; Intentions",
               "What the other person is likely carrying — their position, not a promise about their behaviour.",
               "251", "their-thoughts"),
    _spec_card("No Contact &amp; Reconciliation Guidance",
               "For the silence after a break — whether to reach out, how to hold the distance, and what to expect.",
               "351", "no-contact"),
    _spec_card("Relationship Clarity Reading",
               "A deeper 45-minute look at a tangled situation: several people, mixed signals, or a decision you keep circling.",
               "501", "relationship-clarity"),
    _spec_card("Detailed Love Life Reading",
               "The full picture — patterns across past relationships, what keeps repeating, and what to do differently.",
               "701", "detailed-love-life"),
])

SPEC_CAREER = "".join([
    _spec_card("Career Guidance Reading",
               "Where your career currently stands and what's actually holding the next step back.",
               "251", "career-guidance"),
    _spec_card("Job Change &amp; New Opportunities",
               "For the offer in hand or the move you keep postponing — trade-offs, timing, and what to check.",
               "351", "job-change"),
    _spec_card("Money &amp; Abundance Guidance",
               "For financial blocks, scarcity thinking, and decisions about money you've been avoiding.",
               "351", "money-abundance"),
    _spec_card("Career and Financial Clarity Session",
               "A 45-minute session covering work and money together, since they're rarely separate problems.",
               "501", "career-financial-clarity"),
])

SPEC_PERSONAL = "".join([
    _spec_card("Yes/No Tarot Reading",
               "One direct question, one direct answer, with a short note on what's shaping it. Per question.",
               "51", "yes-no"),
    _spec_card("Current Energy Reading",
               "What you're currently carrying — yours, and what you've picked up from other people.",
               "251", "current-energy"),
    _spec_card("General Life Guidance",
               "An open reading for when something feels off but you can't name it yet.",
               "351", "general-life"),
    _spec_card("Blockages &amp; Personal Growth Reading",
               "What keeps stopping you at the same point, and what it would take to move past it.",
               "501", "blockages"),
    _spec_card("Detailed Life Guidance Session",
               "A 60-minute session across several areas — work, relationships, direction — for a fuller picture.",
               "701", "detailed-life"),
])

PACKAGE_CARDS = "".join([
    _package_card("Quick Clarity", "5 questions answered by voice note, delivered within 24–48 hours.", "251"),
    _package_card("Love Clarity", "A 30-minute personalised session, focused on one relationship situation.", "501"),
    _package_card("Life Guidance", "A 45-minute session covering multiple concerns at once.", "701"),
    _package_card("Complete Clarity", "A full 60-minute personalised session — the most time, the widest picture.", "951", featured=True),
])

TAROT_BODY = page_hero(
    "Online Tarot Readings",
    "Book a live session with unlimited questions from ₹251, or a single question answered by voice note from "
    "₹51. Hindi or English, anywhere in India.",
    '<nav class="breadcrumbs" aria-label="Breadcrumb"><a href="/">Home</a>'
    '<span class="sep">/</span><a href="/consultations/">Consultations</a>'
    '<span class="sep">/</span><span aria-current="page">Tarot Readings</span></nav>',
    badges=["From ₹51", "Phone, video or voice note", "Hindi &amp; English", "24–48h delivery"],
    cta_service="Tarot Reading",
) + f"""
{trust_bar()}

<section class="section">
  <div class="wrap">
    {section_head("Two ways to read", "Pick by how much you need to say, not by how much you want to spend.")}
    <div class="grid grid-2">
      <div class="link-card" style="cursor:default;padding:24px">
        <strong style="font-size:18px">Live session — unlimited questions</strong>
        <span style="margin-top:8px">15 to 60 minutes on a phone or video call. Bring as many questions as fit in
          the time, and follow the conversation where it goes.</span>
        <span style="margin-top:12px;color:var(--gold-bright);font-size:14px">From ₹251 · 15–60 minutes</span>
      </div>
      <div class="link-card" style="cursor:default;padding:24px">
        <strong style="font-size:18px">Per question — voice note</strong>
        <span style="margin-top:8px">One, two or five specific questions, answered in a voice note on WhatsApp or
          Instagram. No scheduling needed.</span>
        <span style="margin-top:12px;color:var(--gold-bright);font-size:14px">From ₹51 · delivered in 24–48 hours</span>
      </div>
    </div>
  </div>
</section>

<div class="divider"></div>

<section class="section" id="pricing">
  <div class="wrap">
    {section_head("Personal readings — unlimited questions", "You are booking time, not a question count. "
                  "Use it however you need.")}
    <div style="max-width:820px;margin:0 auto">
      {price_table(
        ["Session", "Best for", "Price"],
        [
          ["15-Minute Reading", ("One or two questions", "A quick, focused read"), "₹251"],
          ["30-Minute Reading", ("One situation in depth", "The most commonly booked length — most chosen"), "₹501"],
          ["45-Minute Reading", ("Several connected questions", "When the situation has more than one strand"), "₹701"],
          ["60-Minute Reading", ("The full picture", "Work, relationships and direction together"), "₹951"],
        ],
        1,
      )}
    </div>
    <p class="small muted text-center mt-3">
      Phone call or online consultation. “Unlimited questions” means questions asked within your booked session
      time. Includes personalised guidance, follow-ups related to your concerns, and room to explore different
      aspects of the situation.
    </p>
  </div>
</section>

<div class="divider"></div>

<section class="section">
  <div class="wrap">
    {section_head("Per-question readings", "For a quick answer on one situation, without booking a session.")}
    <div style="max-width:820px;margin:0 auto">
      {price_table(
        ["Reading", "Format", "Price"],
        [
          ["1 Question", ("Voice note", "One question, one focused interpretation"), "₹51"],
          ["2 Questions", ("Voice note", "Two questions answered separately"), "₹101"],
          ["5 Questions", ("Voice note", "Five questions — the best value per question"), "₹251"],
        ],
        2,
      )}
    </div>
    <p class="small muted text-center mt-3">
      Delivered as a voice note on WhatsApp or Instagram DM within 24–48 hours, subject to availability. Each
      question gets its own personalised interpretation and guidance.
    </p>
  </div>
</section>

<div class="divider"></div>

<section class="section">
  <div class="wrap">
    {section_head("Specialised readings", "Focused readings on a defined theme. Available as a voice note or a "
                  "live session, whichever suits you.")}

    <h3 style="font-size:22px;margin:8px 0 16px">Love &amp; Relationships</h3>
    <div class="catalogue">{SPEC_LOVE}</div>

    <h3 style="font-size:22px;margin:44px 0 16px">Career &amp; Finance</h3>
    <div class="catalogue">{SPEC_CAREER}</div>

    <h3 style="font-size:22px;margin:44px 0 16px">Personal &amp; Spiritual Guidance</h3>
    <div class="catalogue">{SPEC_PERSONAL}</div>
  </div>
</section>

<div class="divider"></div>

<section class="section">
  <div class="wrap">
    {section_head("Packages", "Bundled readings at a set price, when you already know what you want.")}
    <div class="catalogue">{PACKAGE_CARDS}</div>
  </div>
</section>

<div class="divider"></div>

<section class="section">
  <div class="wrap">
    {section_head("How it works", "Three steps, whichever format you choose.")}
    {steps([
      ("01", "Message your question", "One or two lines on WhatsApp. I'll tell you whether a session or a voice "
             "note fits better."),
      ("02", "Pay and confirm", "Payment confirms the booking — then we set a time, or I set to work on the "
             "voice note."),
      ("03", "Have the reading", "A private call or video, or a voice note within 24–48 hours. Either way you "
             "get something concrete to act on."),
    ])}
  </div>
</section>

<div class="divider"></div>

<section class="section">
  <div class="wrap">
    <div class="prose" style="max-width:74ch">
      <h2 style="margin-top:0">What a tarot reading will and won't do</h2>
      <p>It will show you where a situation actually stands, what you've been avoiding looking at, and what your
         realistic options are. Most people leave knowing something they already half-knew, said out loud for
         the first time.</p>
      <p>It won't give you a guaranteed outcome. It won't tell you what another person will definitely do, and it
         won't replace a lawyer, a doctor or a financial adviser. If a reading isn't the right tool for what
         you're facing, I'll say so rather than take the booking.</p>
    </div>
  </div>
</section>

<div class="divider"></div>

<section class="section">
  <div class="wrap">
    {section_head("Questions before you book", "")}
    {faq_block(TAROT_FAQ)}
  </div>
</section>
""" + related_links("Related", [
    ("/consultations/tarot-readings/love/", "Love & Relationship Tarot", "For a relationship situation in depth"),
    ("/consultations/tarot-readings/career/", "Career & Decision Tarot", "For a job change or business decision"),
    ("/consultations/numerology/", "Numerology", "Numbers-based analysis, delivered as a report"),
    ("/consultations/candle-rituals/", "Candle Rituals", "Intention-based ritual work"),
]) + cta_block(
    "Not sure which reading fits?",
    "Send a couple of lines about your situation. I'll point you to the right format — and tell you if the "
    "cheaper option would serve you just as well.",
    service="Tarot Reading",
)

TAROT = Page(
    path="consultations/tarot-readings/index.html",
    url="/consultations/tarot-readings/",
    title="Online Tarot Reading India | From ₹51 | Sessions & Questions",
    description=(
        "Private online tarot readings with Nisha Pathak. Live sessions with unlimited questions from ₹251, or a "
        "single question by voice note from ₹51. Hindi & English, pan-India."
    ),
    h1="Online Tarot Readings",
    body=TAROT_BODY,
    nav="consultations",
    crumbs=[("Consultations", "/consultations/"), ("Tarot Readings", "/consultations/tarot-readings/")],
    og_image="/images/cat-tarot.webp",
    schema=[
        service_schema("Tarot Reading",
                       "Online tarot readings — live sessions with unlimited questions, per-question voice-note "
                       "readings, and specialised love, career and personal guidance readings.",
                       "/consultations/tarot-readings/", price_low="51", category="Tarot Consultation"),
        faq_schema(TAROT_FAQ),
        breadcrumb_schema([("Consultations", "/consultations/"),
                           ("Tarot Readings", "/consultations/tarot-readings/")]),
    ],
)


# ============================================================ LOVE TAROT

LOVE_FAQ = [
    ("Will you tell me if my ex is coming back?",
     "I'll tell you what the cards show about where they currently stand and what the dynamic between you "
     "looks like. I won't promise that someone will act a certain way — that isn't something a reading can "
     "honestly guarantee, and anyone who says otherwise is guessing."),
    ("Can a reading make someone contact me?",
     "No. A reading gives you clarity; it doesn't change another person's choices. What it can do is help you "
     "decide how long you want to keep waiting, and what you'd rather do instead."),
    ("Is this confidential?",
     "Completely. Names, details and anything discussed stay between us. Nothing is published or shared."),
    ("I'm in a lot of pain right now. Is a reading a good idea?",
     "It can help you feel less alone with the confusion, and it can give you structure. But it isn't therapy "
     "and it isn't a crisis service. If you're in serious distress, please also speak to a licensed counsellor "
     "or a helpline. I'm happy to do a reading alongside that, not instead of it."),
    ("Do you do love spells or rituals to bring someone back?",
     "I offer intention-based rituals — for clarity, self-worth, release and opening to healthy connection. I "
     "don't offer work designed to override another person's will or choices, and I'll decline that request "
     "if it comes up."),
    ("What if I'm not sure whether I want to stay or leave?",
     "That's the most common reason people book. The reading won't decide for you — it will make the trade-offs "
     "clear enough that the decision stops feeling like a fog."),
]

LOVE_INTRO = """
<p>Most people who book a love reading already know something is off. What they don't have is language for
it — or permission to trust what they've noticed.</p>
<p>This reading is designed for exactly that point. Not "will he text me", but: what is actually happening
between you, what is each of you carrying into it, what have you been ignoring, and what would it look like
to move forward — with or without this person.</p>
"""

LOVE_BODY = page_hero(
    "Online Love &amp; Relationship Tarot Reading",
    "Honest clarity on the relationship question you keep circling. No false hope, no fear-selling — just a "
    "clear read and a realistic view of your options.",
    '<nav class="breadcrumbs" aria-label="Breadcrumb"><a href="/">Home</a>'
    '<span class="sep">/</span><a href="/consultations/">Consultations</a>'
    '<span class="sep">/</span><a href="/consultations/tarot-readings/">Tarot Readings</a>'
    '<span class="sep">/</span><span aria-current="page">Love &amp; Relationships</span></nav>',
    badges=["From ₹251", "Voice note or live session", "Hindi &amp; English", "Confidential"],
    cta_service="Love &amp; Relationship Tarot Reading",
) + f"""
{trust_bar()}

<section class="section">
  <div class="wrap">
    <div class="split split-wide-left" style="align-items:start">
      <div class="prose">
        <h2 style="margin-top:0">What's usually going on</h2>
        {LOVE_INTRO}
        <h2>What people bring to this reading</h2>
        <ul class="checklist">
          <li>A breakup they can't stop replaying</li>
          <li>A relationship that feels one-sided but they can't name why</li>
          <li>Marriage pressure from family when they aren't sure themselves</li>
          <li>A situationship that has been "almost something" for months</li>
          <li>Two people they care about and no clear way to choose</li>
          <li>The quiet feeling that they've already decided and are scared to admit it</li>
        </ul>

        <h2>What you'll actually get</h2>
        <ul class="checklist">
          <li>A grounded read of where the situation currently stands</li>
          <li>The other person's likely position — without pretending it's a certainty</li>
          <li>What you've been avoiding looking at</li>
          <li>Your realistic options, including the one you haven't considered</li>
          <li>Something concrete to do next, whether that's a conversation or a decision</li>
        </ul>

        {disclaimer_box(
          "<strong>An honest note.</strong> This reading will not promise reconciliation, and it won't tell you "
          "someone's feelings are guaranteed. It also won't try to control another person's choices — that "
          "isn't how I work. What it will do is make the situation clear enough for you to act on."
        )}
      </div>
      <div>
        <div class="split-img" style="background-image:url('/images/cat-tarot.webp');aspect-ratio:1/1"></div>
        <div class="cta-block" style="padding:26px 22px;margin-top:18px">
          <h2 style="font-size:22px;margin-bottom:8px">Book a love reading</h2>
          <p class="small" style="margin-bottom:16px">Private call or video, in Hindi or English.</p>
          {wa_btn("Book on WhatsApp", "Love &amp; Relationship Tarot Reading", "love-sidebar", "btn btn-gold btn-block")}
        </div>
      </div>
    </div>
  </div>
</section>

<div class="divider"></div>

<section class="section" id="pricing">
  <div class="wrap">
    {section_head("Pricing", "Payment confirms your slot. Reschedule free with 4 hours' notice.")}
    <div style="max-width:820px;margin:0 auto">
      {price_table(
        ["Reading", "What it covers", "Price"],
        [
          ["Love &amp; Relationship Reading", ("Focused read", "Where the relationship currently stands"), "₹251"],
          ["Their Thoughts, Feelings &amp; Intentions", ("Focused read", "Their position — not a promise about their behaviour"), "₹251"],
          ["No Contact &amp; Reconciliation Guidance", ("Guidance", "Whether to reach out, how to hold the distance"), "₹351"],
          ["Relationship Clarity Reading", ("45 minutes", "For a tangled situation — most booked"), "₹501"],
          ["Detailed Love Life Reading", ("60 minutes", "Patterns across relationships, and what to change"), "₹701"],
        ],
        3,
      )}
    </div>
  </div>
</section>

<div class="divider"></div>

<section class="section">
  <div class="wrap">
    {section_head("How it works", "")}
    {steps([
      ("01", "Tell me the situation", "A few lines is enough. No need to write an essay."),
      ("02", "Choose your slot", "Pay to confirm. You'll get the joining details straight away."),
      ("03", "Have the reading", "Private call or video. You'll get a written summary afterwards."),
    ])}
  </div>
</section>

<div class="divider"></div>

<section class="section">
  <div class="wrap">
    {section_head("Questions before you book", "")}
    {faq_block(LOVE_FAQ)}
  </div>
</section>
""" + related_links("Related", [
    ("/consultations/tarot-readings/career/", "Career Tarot", "For work decisions rather than relationships"),
    ("/consultations/numerology/marriage/", "Marriage Numerology", "Compatibility and timing analysis"),
    ("/consultations/candle-rituals/", "Candle Rituals", "Self-worth, release and opening to connection"),
]) + cta_block(
    "You've been overthinking this for a while",
    "Send a couple of lines. I'll tell you whether a reading is the right next step — and what it would cover.",
    service="Love &amp; Relationship Tarot Reading",
)

LOVE = Page(
    path="consultations/tarot-readings/love/index.html",
    url="/consultations/tarot-readings/love/",
    title="Love Tarot Reading India | From ₹251 | Tarot with Nisha",
    description=(
        "Private online love tarot reading with Nisha Pathak. Breakups, confusion and marriage pressure. Honest "
        "clarity, no false hope. Hindi & English. From ₹251."
    ),
    h1="Online Love & Relationship Tarot Reading",
    body=LOVE_BODY,
    nav="consultations",
    crumbs=[("Consultations", "/consultations/"),
            ("Tarot Readings", "/consultations/tarot-readings/"),
            ("Love & Relationships", "/consultations/tarot-readings/love/")],
    og_image="/images/cat-tarot.webp",
    schema=[
        service_schema("Love & Relationship Tarot Reading",
                       "Private online tarot reading focused on relationships, breakups and marriage questions.",
                       "/consultations/tarot-readings/love/", price_low="599", category="Tarot Consultation"),
        faq_schema(LOVE_FAQ),
        breadcrumb_schema([("Consultations", "/consultations/"),
                           ("Tarot Readings", "/consultations/tarot-readings/"),
                           ("Love & Relationships", "/consultations/tarot-readings/love/")]),
    ],
)


# ============================================================ CAREER TAROT

CAREER_FAQ = [
    ("Can tarot tell me if I'll get this job?",
     "It can show you how the situation is currently positioned and what's influencing the outcome — including "
     "things on your side you can still change. It can't guarantee a hiring decision. What it's genuinely good "
     "for is showing you whether you're pursuing the right thing in the first place."),
    ("Is this useful if I've already decided?",
     "Often more useful. A reading can surface what you're walking into, what you haven't accounted for, and "
     "whether the decision is coming from clarity or from exhaustion. Both are valid reasons to leave — but "
     "they lead to different next steps."),
    ("Do you help with layoffs and job loss?",
     "Yes. A significant share of career readings are about sudden job loss, restructuring anxiety, or the "
     "aftermath of being let go. The work is usually about separating shock from strategy."),
    ("Can you help with a business decision?",
     "Yes — partnerships, launches, hiring, pricing and whether to expand. Business readings tend to be more "
     "practical than people expect; the cards are good at exposing what the founder already senses but is "
     "talking themselves out of."),
    ("Do I need to prepare anything?",
     "No. Bring your question and, if you have one, the decision deadline. That's enough."),
    ("Will you tell me what to do?",
     "No. I'll show you the trade-offs clearly and tell you what I'd be asking in your position. The decision "
     "stays yours — that's the whole point."),
]

CAREER_BODY = page_hero(
    "Online Career &amp; Decision Tarot Reading",
    "For the job change you've been \"thinking about\" for months. A clear read of the situation, the trade-offs, "
    "and what to do next.",
    '<nav class="breadcrumbs" aria-label="Breadcrumb"><a href="/">Home</a>'
    '<span class="sep">/</span><a href="/consultations/">Consultations</a>'
    '<span class="sep">/</span><a href="/consultations/tarot-readings/">Tarot Readings</a>'
    '<span class="sep">/</span><span aria-current="page">Career &amp; Decisions</span></nav>',
    badges=["From ₹251", "Voice note or live session", "Hindi &amp; English", "Practical next steps"],
    cta_service="Career &amp; Decision Tarot Reading",
) + f"""
{trust_bar()}

<section class="section">
  <div class="wrap">
    <div class="split split-wide-left" style="align-items:start">
      <div class="prose">
        <h2 style="margin-top:0">The problem isn't the decision</h2>
        <p>Almost nobody who books a career reading is short of information. They know the salary, the commute,
           the manager, the risk. What they don't have is permission — or a way to tell the difference between
           a genuinely bad situation and their own exhaustion.</p>
        <p>That's what this reading is for. It separates the three questions people usually collapse into one:
           <strong>Is the problem the role, the manager, or the industry?</strong> They need different exits.</p>

        <h2>What people bring to this reading</h2>
        <ul class="checklist">
          <li>An offer in hand and no idea whether to take it</li>
          <li>A job that pays well and quietly drains them</li>
          <li>Layoff anxiety, restructuring, or the aftermath of being let go</li>
          <li>A promotion that keeps not happening</li>
          <li>An interview or exam where the stakes feel disproportionate</li>
          <li>Whether to leave a stable job for a business</li>
          <li>A business decision — partner, launch, pricing, expansion</li>
        </ul>

        <h2>What you'll actually get</h2>
        <ul class="checklist">
          <li>A clear read of how the situation is currently positioned</li>
          <li>What you're avoiding by staying — and by leaving</li>
          <li>The realistic timing, as far as a reading can show it</li>
          <li>Two or three concrete next actions</li>
          <li>A written summary you can refer back to when the doubt returns</li>
        </ul>

        {disclaimer_box(
          "<strong>An honest note.</strong> A reading won't replace salary maths, contract review or career "
          "advice from someone in your industry. What it does well is expose the pattern behind the hesitation. "
          "That's usually what's actually blocking the decision."
        )}
      </div>
      <div>
        <div class="split-img" style="background-image:url('/images/cat-tarot.webp');aspect-ratio:1/1"></div>
        <div class="cta-block" style="padding:26px 22px;margin-top:18px">
          <h2 style="font-size:22px;margin-bottom:8px">Book a career reading</h2>
          <p class="small" style="margin-bottom:16px">Private call or video, in Hindi or English.</p>
          {wa_btn("Book on WhatsApp", "Career &amp; Decision Tarot Reading", "career-sidebar", "btn btn-gold btn-block")}
        </div>
      </div>
    </div>
  </div>
</section>

<div class="divider"></div>

<section class="section" id="pricing">
  <div class="wrap">
    {section_head("Pricing", "Payment confirms your slot. Reschedule free with 4 hours' notice.")}
    <div style="max-width:820px;margin:0 auto">
      {price_table(
        ["Reading", "What it covers", "Price"],
        [
          ["Career Guidance Reading", ("Focused read", "Where your career stands and what's holding it back"), "₹251"],
          ["Job Change &amp; New Opportunities", ("Guidance", "Trade-offs, timing and what to check"), "₹351"],
          ["Money &amp; Abundance Guidance", ("Guidance", "Financial blocks and money decisions"), "₹351"],
          ["Career and Financial Clarity Session", ("45 minutes", "Work and money together — most booked"), "₹501"],
        ],
        3,
      )}
    </div>
  </div>
</section>

<div class="divider"></div>

<section class="section">
  <div class="wrap">
    {section_head("How it works", "")}
    {steps([
      ("01", "Describe the decision", "Where you are, what you're choosing between, and any deadline."),
      ("02", "Pick a slot", "Pay to confirm. You'll get joining details immediately."),
      ("03", "Have the reading", "Private call or video, plus a written summary afterwards."),
    ])}
  </div>
</section>

<div class="divider"></div>

<section class="section">
  <div class="wrap">
    {section_head("Questions before you book", "")}
    {faq_block(CAREER_FAQ)}
  </div>
</section>
""" + related_links("Related", [
    ("/consultations/tarot-readings/love/", "Love Tarot", "For relationship questions rather than work"),
    ("/consultations/numerology/name/", "Business Name Numerology", "For naming a company or brand"),
    ("/consultations/candle-rituals/", "Candle Rituals", "Confidence, opportunity and business intention work"),
]) + cta_block(
    "Book a career reading",
    "Tell me what you're deciding between. I'll confirm the right reading length and the next available slot.",
    service="Career &amp; Decision Tarot Reading",
)

CAREER = Page(
    path="consultations/tarot-readings/career/index.html",
    url="/consultations/tarot-readings/career/",
    title="Career Tarot Reading India | From ₹251 | Job Decisions",
    description=(
        "Private online career tarot reading with Nisha Pathak. Job switches, offers, layoffs and interviews. "
        "Hindi & English, pan-India. From ₹251."
    ),
    h1="Online Career & Decision Tarot Reading",
    body=CAREER_BODY,
    nav="consultations",
    crumbs=[("Consultations", "/consultations/"),
            ("Tarot Readings", "/consultations/tarot-readings/"),
            ("Career & Decisions", "/consultations/tarot-readings/career/")],
    og_image="/images/cat-tarot.webp",
    schema=[
        service_schema("Career & Decision Tarot Reading",
                       "Private online tarot reading focused on career decisions, job changes and business questions.",
                       "/consultations/tarot-readings/career/", price_low="599", category="Tarot Consultation"),
        faq_schema(CAREER_FAQ),
        breadcrumb_schema([("Consultations", "/consultations/"),
                           ("Tarot Readings", "/consultations/tarot-readings/"),
                           ("Career & Decisions", "/consultations/tarot-readings/career/")]),
    ],
)
