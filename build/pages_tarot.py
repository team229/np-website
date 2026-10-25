"""Consultation hub, category pages and individual service pages."""
from __future__ import annotations

from components import (
    cta_block, disclaimer_box, faq_block, page_hero, price_table, related_links,
    section_head, service_card, steps, trust_bar,
)
from layout import Page, breadcrumb_schema, faq_schema, service_schema, wa_btn


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
                    "Love, career and full readings. Best when you need a clear read on a specific situation.",
                    "From ₹599", "/images/cat-tarot.webp")}
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
    ("Which tarot reading should I choose?",
     "If you have one clear question, the single-question reading is enough. If the situation is tangled — "
     "several people involved, or you keep going back and forth — book the 45-minute reading. The full "
     "60-minute reading is for when you want the wider picture: work, relationships and direction together."),
    ("Can tarot tell me if someone will come back?",
     "It can show you where that person's position currently sits and what the dynamic looks like. It cannot "
     "guarantee someone's future behaviour, and I won't pretend otherwise. What you'll get is a clear read of "
     "the situation and a realistic view of your options."),
    ("Do you need my birth details for a tarot reading?",
     "No. Tarot only needs your question and a little context. Birth details are used for numerology and "
     "kundali, which are separate services."),
    ("Can I record the session?",
     "Yes, you're welcome to record it for yourself. I'd ask that you don't publish it, since it contains "
     "personal details."),
    ("What if I don't know what to ask?",
     "That's common. Tell me what's been on your mind and I'll help you shape it into a question that will "
     "actually produce something useful."),
    ("Do you offer refunds?",
     "Sessions are non-refundable once delivered. If something comes up, let me know at least 4 hours ahead "
     "and we'll reschedule at no extra cost."),
]

TAROT_BODY = page_hero(
    "Tarot Readings",
    "A private, grounded reading about one situation — love, career, family or a decision you're sitting with. "
    "No theatrics, no fear-selling, no guarantees I can't keep.",
    '<nav class="breadcrumbs" aria-label="Breadcrumb"><a href="/">Home</a>'
    '<span class="sep">/</span><a href="/consultations/">Consultations</a>'
    '<span class="sep">/</span><span aria-current="page">Tarot Readings</span></nav>',
    badges=["From ₹599", "20–60 minutes", "Phone or video", "Hindi &amp; English"],
    cta_service="Tarot Reading",
) + f"""
{trust_bar()}

<section class="section">
  <div class="wrap">
    <div class="split split-wide-left" style="align-items:start">
      <div class="prose">
        <h2 style="margin-top:0">What a tarot reading actually does</h2>
        <p>Tarot doesn't hand you a fixed future. It reads the dynamics of a situation as they stand right now —
           where the energy is stuck, what's being avoided, what the other people involved are likely carrying,
           and what your realistic options look like.</p>
        <p>In practice, that means you leave the session knowing three things: what's actually going on,
           what you've been reluctant to look at, and what to do next. Most clients say the useful part wasn't
           a prediction — it was hearing something out loud that they already half-knew.</p>

        <h2>Choose by situation</h2>
      </div>
      <div class="split-img" style="background-image:url('/images/cat-tarot.webp')"></div>
    </div>

    <div class="grid grid-2 mt-4">
      {service_card("/consultations/tarot-readings/love/", "Love &amp; Relationship Tarot",
                    "Breakups, confusion, marriage pressure, and the question of whether to stay or let go.",
                    "From ₹599", "", "See this reading")}
      {service_card("/consultations/tarot-readings/career/", "Career &amp; Decision Tarot",
                    "Job switches, offers, layoffs, interviews, business decisions and workplace stress.",
                    "From ₹599", "", "See this reading")}
    </div>
  </div>
</section>

<div class="divider"></div>

<section class="section" id="pricing">
  <div class="wrap">
    {section_head("Pricing", "All readings include a written summary of the key points.")}
    <div style="max-width:820px;margin:0 auto">
      {price_table(
        ["Reading", "What it covers", "Price"],
        [
          ["Single Question", ("20 minutes · one focused question", "Best for a clear yes/no situation"), "₹599"],
          ["Focused Reading", ("45 minutes · one area of life", "Love, career, family or direction"), "₹1,299"],
          ["Full Reading", ("60 minutes · the wider picture", "Work, relationships and personal direction"), "₹1,499"],
          ["Love Clarity Bundle", ("45-min love reading + Rose Quartz bracelet", "Shipped pan-India"), "₹1,799"],
          ["Career Clarity Bundle", ("45-min career reading + Money Oil 10ml", "Shipped pan-India"), "₹1,899"],
        ],
        1,
      )}
    </div>
  </div>
</section>

<div class="divider"></div>

<section class="section">
  <div class="wrap">
    {section_head("How it works", "")}
    {steps([
      ("01", "Send your question", "One or two lines on WhatsApp. I'll tell you which reading length fits."),
      ("02", "Confirm and pay", "Pick a slot, pay to confirm. You'll get the joining details immediately."),
      ("03", "Have the reading", "A private call or video. You'll get a written summary afterwards."),
    ])}
  </div>
</section>

<div class="divider"></div>

<section class="section">
  <div class="wrap">
    {section_head("Before you book", "")}
    {faq_block(TAROT_FAQ)}
  </div>
</section>
""" + related_links("Related", [
    ("/consultations/numerology/", "Numerology", "Numbers-based analysis delivered as a report"),
    ("/consultations/vedic-kundali/", "Vedic Kundali", "Birth chart and year-ahead reading"),
    ("/consultations/candle-rituals/", "Candle Rituals", "Intention-based ritual work"),
]) + cta_block(
    "Book a tarot reading",
    "Tell me what's going on. I'll recommend the right length and confirm the next available slot.",
    service="Tarot Reading",
)

TAROT = Page(
    path="consultations/tarot-readings/index.html",
    url="/consultations/tarot-readings/",
    title="Online Tarot Reading India | Love & Career | From ₹599",
    description=(
        "Book a private online tarot reading with Nisha Pathak. Love, career and full readings by phone or "
        "video, in Hindi or English, anywhere in India. 20–60 minutes. From ₹599."
    ),
    h1="Tarot Readings",
    body=TAROT_BODY,
    nav="consultations",
    crumbs=[("Consultations", "/consultations/"), ("Tarot Readings", "/consultations/tarot-readings/")],
    og_image="/images/cat-tarot.webp",
    schema=[
        service_schema("Tarot Reading", "Private online tarot reading by phone or video, focused on love, career or general life direction.", "/consultations/tarot-readings/", price_low="599", category="Tarot Consultation"),
        faq_schema(TAROT_FAQ),
        breadcrumb_schema([("Consultations", "/consultations/"), ("Tarot Readings", "/consultations/tarot-readings/")]),
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
    badges=["From ₹599", "20–45 minutes", "Hindi &amp; English", "100% confidential"],
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
          ["Single Question", ("20 minutes", "One specific question about one person or situation"), "₹599"],
          ["Love &amp; Relationship Reading", ("45 minutes", "The full dynamic, plus next steps — most booked"), "₹1,299"],
          ["Love Clarity Bundle", ("45-min reading + Rose Quartz bracelet", "Bracelet shipped pan-India"), "₹1,799"],
        ],
        1,
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
    title="Love Tarot Reading India | Relationship Clarity | ₹599",
    description=(
        "Private online love tarot reading with Nisha Pathak. Breakups, confusion and marriage pressure. Honest "
        "clarity, no false hope. Hindi & English. From ₹599."
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
    badges=["From ₹599", "20–45 minutes", "Hindi &amp; English", "Practical next steps"],
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
          ["Single Question", ("20 minutes", "One decision — offer, resignation, interview"), "₹599"],
          ["Career &amp; Decision Reading", ("45 minutes", "Full situation, trade-offs and next steps"), "₹1,299"],
          ["Career Clarity Bundle", ("45-min reading + Money Oil 10ml", "Oil shipped pan-India"), "₹1,899"],
        ],
        1,
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
    title="Career Tarot Reading India | Job & Business | ₹599",
    description=(
        "Private online career tarot reading with Nisha Pathak. Job switches, offers, layoffs and interviews. "
        "Hindi & English, pan-India. From ₹599."
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
