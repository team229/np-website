"""Numerology category and individual numerology service pages."""
from __future__ import annotations

from components import (
    cta_block, disclaimer_box, faq_block, page_hero, price_table, related_links,
    section_head, service_card, steps, trust_bar,
)
from layout import Page, breadcrumb_schema, faq_schema, service_schema, wa_btn

from pages_tarot import service_page

C = ("Consultations", "/consultations/")
N = ("Numerology", "/consultations/numerology/")


# ============================================================ CATEGORY

CAT_FAQ = [
    ("Do I need my exact birth time for numerology?",
     "No. Numerology needs your full date of birth and the name as it's written. Birth time is only required for "
     "Vedic kundali, which is a different service."),
    ("How is the report delivered?",
     "As a written report sent on WhatsApp or email within 24–48 hours. Each report is written for your specific "
     "numbers — it isn't a template with your name inserted."),
    ("Can numerology tell me my future?",
     "No. Numerology describes tendencies, cycles and timing patterns. It's a lens for reflection, not a "
     "prediction engine. You'll get the most from it if you treat it as a way of organising what you already sense."),
    ("Is numerology useful if I don't believe in it?",
     "Many clients are sceptical when they start. The useful part is usually the discipline of looking at your "
     "patterns from a structured angle — which works whether or not you take the metaphysics literally."),
    ("Can I change my numbers?",
     "Only your name number, and only by changing how the name is written. Date-derived numbers don't change. "
     "That's why name correction is a real service and 'changing your destiny' isn't."),
    ("Which numerology service should I start with?",
     "The Life Path reading (₹299) is the entry point. If you want everything at once, the Complete Chart (₹799) "
     "covers life path, psychic, destiny and personal year together."),
]

CAT_BODY = page_hero(
    "Online Numerology Consultations",
    "Your date of birth and your name, read as patterns — not predictions. Written reports in 24–48 hours, "
    "with an optional call to talk it through.",
    '<nav class="breadcrumbs" aria-label="Breadcrumb"><a href="/">Home</a>'
    '<span class="sep">/</span><a href="/consultations/">Consultations</a>'
    '<span class="sep">/</span><span aria-current="page">Numerology</span></nav>',
    badges=["From ₹299", "Reports in 24–48 hours", "Hindi &amp; English", "Written, not generic"],
    cta_service="Numerology Consultation",
) + f"""
{trust_bar()}

<section class="section">
  <div class="wrap">
    <div class="prose" style="max-width:78ch">
      <h2 style="margin-top:0">Why numerology is often the better entry point</h2>
      <p>Tarot asks you to bring a question. Numerology doesn't. It works from what you already have — your date
         of birth, your name, the number on your house or your vehicle — and describes the patterns that show up
         around those things.</p>
      <p>That makes it a gentler place to start if you're not sure what to ask, or if the idea of a live reading
         feels intense. You get a written report you can read at your own pace, and come back with questions
         afterwards if you want to.</p>
      <p>In practice, the most useful sections are almost always the <strong>personal year</strong> (what phase
         you're in right now) and the <strong>name number</strong> (how the name you use lands on other people).
         Those two explain a surprising amount of the "why does this keep happening" feeling.</p>
    </div>

    <div class="grid grid-2 mt-4">
      {service_card("/consultations/numerology/name/", "Name Numerology &amp; Correction",
                    "How your name reads numerically, spelling variations, and whether a correction is worth making.",
                    "From ₹399", "/images/cat-numerology.webp")}
      {service_card("/consultations/numerology/house/", "House &amp; Nameplate Numerology",
                    "The number on your home, flat or nameplate — and what it tends to support or work against.",
                    "From ₹399", "/images/cat-numerology.webp")}
      {service_card("/consultations/numerology/vehicle/", "Vehicle Number Numerology",
                    "Existing registration numbers, or choosing a number for a new vehicle.",
                    "From ₹299", "/images/cat-numerology.webp")}
      {service_card("/consultations/numerology/marriage/", "Marriage &amp; Compatibility",
                    "Relationship numbers, couple compatibility, and marriage timing guidance.",
                    "From ₹499", "/images/cat-numerology.webp")}
      {service_card("/consultations/numerology/baby-name/", "Baby Name Numerology",
                    "Choosing an auspicious name, or checking one you've already shortlisted.",
                    "From ₹699", "/images/cat-numerology.webp")}
      {service_card("/consultations/vedic-kundali/", "Vedic Kundali Analysis",
                    "When you want the full birth chart rather than numbers alone.",
                    "From ₹600", "/images/cat-kundali.webp")}
    </div>
  </div>
</section>

<div class="divider"></div>

<section class="section">
  <div class="wrap">
    {section_head("Core numerology readings", "Start here if you're new. These cover the numbers that matter most.")}
    <div style="max-width:840px;margin:0 auto">
      {price_table(
        ["Reading", "What it covers", "Price"],
        [
          ["Life Path Number", ("Your primary number", "The core pattern you keep returning to"), "₹299"],
          ["Psychic &amp; Destiny Number", ("Two numbers", "How you operate day-to-day vs. what you're moving toward"), "₹399"],
          ["Personal Year &amp; Month", ("Current cycle", "What phase you're in and when it shifts"), "₹399"],
          ["Complete Numerology Chart", ("Everything above", "Life path, psychic, destiny, personal year"), "₹799"],
          ["Detailed Life Blueprint", ("Full written report", "All numbers plus timing and practical guidance"), "₹999"],
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
      ("01", "Send your details", "Full date of birth and the name exactly as it's written. No birth time needed."),
      ("02", "Pay and confirm", "You'll get a receipt and a delivery window — usually 24–48 hours."),
      ("03", "Read your report", "Written for your numbers specifically. Optional 20-minute call to discuss it."),
    ])}
  </div>
</section>

<div class="divider"></div>

<section class="section">
  <div class="wrap">
    {section_head("Before you book", "")}
    {faq_block(CAT_FAQ)}
  </div>
</section>
""" + related_links("Related", [
    ("/consultations/tarot-readings/", "Tarot Readings", "For a specific situation rather than a pattern"),
    ("/consultations/vedic-kundali/", "Vedic Kundali", "The full birth chart, planetary placements and remedies"),
    ("/resources/guides/tarot-vs-numerology/", "Tarot vs Numerology", "Which reading fits your question"),
    ("/resources/guides/", "All Guides", "Plain-language explainers"),
]) + cta_block(
    "Not sure which numerology reading?",
    "Send your date of birth and what you're hoping to understand. I'll tell you which report fits — the ₹299 "
    "one is often enough.",
    service="Numerology Consultation",
)

NUMEROLOGY = Page(
    path="consultations/numerology/index.html",
    url="/consultations/numerology/",
    title="Numerology Consultation India | Name, House, Marriage | ₹299",
    description=(
        "Numerology consultations with Nisha Pathak — life path, name correction, house, vehicle and marriage. "
        "Written reports in 24–48 hours. From ₹299."
    ),
    h1="Online Numerology Consultations",
    body=CAT_BODY,
    nav="consultations",
    crumbs=[C, N],
    og_image="/images/cat-numerology.webp",
    schema=[
        service_schema("Numerology Consultation",
                       "Online numerology readings covering life path, name, house, vehicle, marriage and baby names.",
                       "/consultations/numerology/", price_low="299", category="Numerology Consultation"),
        faq_schema(CAT_FAQ),
        breadcrumb_schema([C, N]),
    ],
)


# ============================================================ NAME

NAME_FAQ = [
    ("Should I change my name if the number isn't good?",
     "Usually not. A name change is disruptive and rarely necessary. In most cases a spelling variation used "
     "professionally — not a legal change — is enough. I'll tell you honestly if I think it's worth doing at all."),
    ("Does the spelling I use matter, or the legal spelling?",
     "Both, in different ways. Your legal name is what documents and formal contexts carry. The name you actually "
     "use — on Instagram, in business, with friends — is what people respond to. We look at both."),
    ("Can you check a business or brand name?",
     "Yes. Business name analysis is ₹699 and looks at how the name reads numerically alongside what the business "
     "does. It's most useful before you print anything."),
    ("What about a baby's name?",
     "That's a separate service — baby name numerology starts at ₹699 and works from the expected date of birth."),
    ("How long does it take?",
     "24–48 hours for the report. New name selection consultations include a 20–30 minute call and take a little "
     "longer."),
    ("Will a name correction change my life?",
     "No — and I'd be suspicious of anyone who says it will. A name number is one influence among many. It's "
     "worth aligning if it's easy to do, but it isn't a substitute for the actual work."),
]

NAME = service_page(
    path="consultations/numerology/name/index.html",
    url="/consultations/numerology/name/",
    nav="consultations",
    crumbs=[C, N, ("Name Numerology", "/consultations/numerology/name/")],
    h1="Name Numerology & Correction",
    meta_title="Name Numerology India | Correction & Business Names | ₹399",
    meta_desc=("Name numerology and name correction online with Nisha Pathak. Check your name number, compare "
               "spellings, analyse a business name. Written report in 24–48 hours. From ₹399."),
    lede=("How the name you use reads numerically — and whether a spelling variation is genuinely worth making. "
          "Honest recommendations, including when to leave it alone."),
    img="/images/cat-numerology.webp",
    price_from="₹399",
    price_note="Report in 24–48 hours",
    who=[
        "You've been told your name number is wrong and want a calmer second opinion",
        "You use a different spelling professionally than on your documents",
        "You're naming a business, brand or creative project",
        "You've married and are deciding whether to change your surname",
        "You're choosing the spelling of your child's name",
        "Something about your name has never quite felt like you",
    ],
    includes=[
        "Your current name number, from the spelling you actually use",
        "How it sits against your life path and psychic numbers",
        "Specific spelling variations that shift the number, where they exist",
        "A clear recommendation — including 'leave it alone' when that's the honest answer",
        "Optional 20-minute call to talk it through",
    ],
    process=[
        ("01", "Send your details", "Full name as written, the spelling you use, and your date of birth."),
        ("02", "Pay and confirm", "Report delivered within 24–48 hours by WhatsApp or email."),
        ("03", "Read and ask", "Add a call if you want to talk through the recommendation."),
    ],
    pricing_headers=["Service", "What it covers", "Price"],
    pricing_rows=[
        ["Name Number Calculation", ("Core report", "Your name number and what it emphasises"), "₹399"],
        ["Name Spelling Analysis", ("Detailed", "Two or three variants compared side by side"), "₹499"],
        ["Business / Brand Name Analysis", ("For founders", "How the name reads commercially"), "₹699"],
        ["Baby Name Numerology", ("For parents", "Checked against expected date of birth"), "₹699"],
        ["Personal Name Correction", ("Recommendations", "Variants plus guidance on whether to use them"), "₹799"],
        ["New Name Selection Consultation", ("Includes a call", "20–30 minutes working through options"), "₹999"],
    ],
    popular=4,
    faqs=NAME_FAQ,
    related=[
        ("/consultations/numerology/", "All Numerology", "Life path, personal year and complete charts"),
        ("/consultations/numerology/baby-name/", "Baby Name Numerology", "Choosing a name for a child"),
        ("/consultations/numerology/marriage/", "Marriage Numerology", "Surname decisions and compatibility"),
    ],
    schema_name="Name Numerology",
    schema_desc=("Online name numerology and name correction consultation including business name analysis and "
                 "spelling variants."),
    schema_low="399",
    disclaimer=("<strong>An honest note.</strong> I don't recommend legal name changes. Most of the value is in "
                "understanding the pattern, not changing documents. If a variation is easy and useful, I'll say "
                "so — if it isn't, I'll say that too."),
    cta_title="Check your name number",
    cta_text=("Send your full name as you actually use it and your date of birth. I'll confirm the right option "
              "and the delivery time."),
)
# ============================================================ HOUSE

HOUSE_NUMBERS = [
    ("1", "Independence and self-direction", "Good for people starting out alone. Can feel solitary if you want a busy home.", "Strong for founders, freelancers, anyone building something."),
    ("2", "Partnership and sensitivity", "Warm and relational. Emotions run high and small conflicts linger.", "Good for couples. Less good if you need quiet separation of work and home."),
    ("3", "Expression and social energy", "Guests, conversation, creativity. Rarely tidy, rarely boring.", "Great for entertainers, creatives and people who host often."),
    ("4", "Structure and stability", "Practical, grounded, sometimes rigid. Rules form easily here.", "Strong for families and anyone needing routine. Watch for stubbornness."),
    ("5", "Movement and change", "Frequent shifts, travel, restlessness. Nothing stays put for long.", "Good for renters and the transient. Difficult if you crave permanence."),
    ("6", "Care and responsibility", "The household tends to become the centre of gravity. Comfortable and demanding.", "Excellent for families. Watch for over-responsibility."),
    ("7", "Reflection and solitude", "Quiet, inward, sometimes isolating. Deep rest happens here.", "Good for writers, researchers, anyone needing retreat."),
    ("8", "Ambition and material focus", "Work bleeds into home. Money matters get attention.", "Strong for business owners. Watch for home feeling like an office."),
    ("9", "Completion and release", "Endings, generosity, and a slightly transitional feel.", "Good for short stays and turning points. Not ideal for long-term settling."),
]

HOUSE_FAQ = [
    ("I'm renting — does the house number still matter?",
     "It matters less than for a home you own, but it isn't irrelevant. If you're staying more than a year, the "
     "number still describes the atmosphere you're living in."),
    ("My building has a flat number and a door number. Which one counts?",
     "The number on the door you actually use is primary. Building and society numbers are secondary context. "
     "If they conflict, we look at which is more present in daily life."),
    ("Can a bad house number be fixed?",
     "You can't change the number, but you can change how it's written — adding a letter, using a nameplate, or "
     "adjusting how the entrance is presented. I'll tell you honestly whether it's worth doing."),
    ("Should I reject a house because of its number?",
     "No. Number is one factor among many — location, light, neighbours, rent and commute matter more. Use this "
     "to understand the atmosphere, not to veto a good home."),
    ("Do you check the nameplate name too?",
     "Yes, that's included in the nameplate analysis. The name on the door and the number on the door are read "
     "together."),
]

HOUSE_BODY = page_hero(
    "House &amp; Nameplate Numerology",
    "The number on your door describes the atmosphere you come home to. Useful if a home has never quite felt "
    "settled — or if you're choosing between two.",
    '<nav class="breadcrumbs" aria-label="Breadcrumb"><a href="/">Home</a>'
    '<span class="sep">/</span><a href="/consultations/">Consultations</a>'
    '<span class="sep">/</span><a href="/consultations/numerology/">Numerology</a>'
    '<span class="sep">/</span><span aria-current="page">House &amp; Nameplate</span></nav>',
    badges=["From ₹399", "Report in 24–48 hours", "Hindi &amp; English", "Buying or renting"],
    cta_service="House &amp; Nameplate Numerology",
) + f"""
{trust_bar()}

<section class="section">
  <div class="wrap">
    <div class="prose" style="max-width:78ch">
      <h2 style="margin-top:0">Why a house number reads differently from a person's number</h2>
      <p>A person's number describes a life. A house number describes an atmosphere — the mood of the space, the
         kind of behaviour it encourages, and the friction it tends to produce. Two people can live at the same
         address and experience it differently, but the pattern is usually recognisable.</p>
      <p>The most common thing this reading explains: why a home that looks perfect on paper never quite feels
         calm. Usually it's a mismatch between the number's natural rhythm and what the occupants need. A number
         5 house is wonderful if you travel constantly and miserable if you want stillness.</p>
    </div>

    <div class="mt-4">
      {section_head("The nine house numbers", "A short orientation — your report goes much deeper.")}
      <div class="table-scroll">
        <table class="price-table">
          <thead><tr><th>Number</th><th>Core quality</th><th>How it tends to feel</th><th>Best suited to</th></tr></thead>
          <tbody>
            {''.join(f'<tr><td class="amount">{n}</td><td><strong>{q}</strong></td><td>{f}</td><td>{b}</td></tr>' for n, q, f, b in HOUSE_NUMBERS)}
          </tbody>
        </table>
      </div>
      <p class="small muted mt-3">Note: 11, 22 and 33 are master numbers and are read differently rather than reduced. Your report will explain this if it applies.</p>
    </div>
  </div>
</section>

<div class="divider"></div>

<section class="section" id="pricing">
  <div class="wrap">
    {section_head("Pricing", "All reports delivered within 24–48 hours.")}
    <div style="max-width:820px;margin:0 auto">
      {price_table(
        ["Service", "What it covers", "Price"],
        [
          ["House / Flat Number Analysis", ("Core report", "The atmosphere and patterns of your address"), "₹399"],
          ["House Nameplate Name Analysis", ("Name + number", "For homes with a name rather than only a number"), "₹499"],
          ["Nameplate Name &amp; Number Review", ("Combined", "Both elements read together"), "₹699"],
          ["New House Number Consultation", ("Before you commit", "Compare two or three addresses you're considering"), "₹799"],
          ["Combined Home &amp; Family Numerology", ("Household", "Every occupant's numbers against the address"), "₹999"],
        ],
        2,
      )}
    </div>
  </div>
</section>

<div class="divider"></div>

<section class="section">
  <div class="wrap">
    {section_head("Questions before you book", "")}
    {faq_block(HOUSE_FAQ)}
  </div>
</section>
""" + related_links("Related", [
    ("/consultations/numerology/vehicle/", "Vehicle Numerology", "The number on your car or scooter"),
    ("/consultations/numerology/name/", "Name Numerology", "Your personal name number"),
    ("/consultations/vedic-kundali/", "Vedic Kundali", "Traditional chart-based guidance for the home"),
    ("/resources/guides/house-number-numerology/", "House Number Guide", "What numbers 1–9 actually mean"),
]) + cta_block(
    "Check your house number",
    "Send your flat or house number, the nameplate name if there is one, and who lives there.",
    service="House &amp; Nameplate Numerology",
)

HOUSE = Page(
    path="consultations/numerology/house/index.html",
    url="/consultations/numerology/house/",
    title="House Number Numerology India | Flat & Nameplate | ₹399",
    description=(
        "House and flat number numerology with Nisha Pathak. Understand the atmosphere of your address or compare "
        "homes before you commit. Report in 24–48 hours. From ₹399."
    ),
    h1="House & Nameplate Numerology",
    body=HOUSE_BODY,
    nav="consultations",
    crumbs=[C, N, ("House & Nameplate", "/consultations/numerology/house/")],
    og_image="/images/cat-numerology.webp",
    schema=[
        service_schema("House & Nameplate Numerology",
                       "Online numerology analysis of a house, flat or nameplate number.",
                       "/consultations/numerology/house/", price_low="399", category="Numerology Consultation"),
        faq_schema(HOUSE_FAQ),
        breadcrumb_schema([C, N, ("House & Nameplate", "/consultations/numerology/house/")]),
    ],
)


# ============================================================ VEHICLE

VEHICLE_NUMBERS = [
    ("1", "Fast, independent, decisive", "Good for solo drivers and daily commuters. Watch for impatience in traffic."),
    ("2", "Smooth, cooperative, steady", "Comfortable for family use and long drives. Less suited to aggressive driving."),
    ("3", "Expressive, social, busy", "A car that gets used a lot and carries people. Watch for distraction."),
    ("4", "Solid, practical, reliable", "The safest-feeling option. Excellent for long ownership and high mileage."),
    ("5", "Mobile, restless, quick", "Great for people who travel constantly. Higher tendency toward sudden trips and minor niggles."),
    ("6", "Comfortable, caring, heavy", "Good for family vehicles. Watch for the car becoming a shared responsibility."),
    ("7", "Quiet, inward, unusual", "Fine for low-mileage personal use. Can feel 'detached' if the car is used for work."),
    ("8", "Powerful, ambitious, demanding", "Strong for business vehicles and commercial use. Higher maintenance attention needed."),
    ("9", "Completion, transition, generous", "Suits vehicles nearing the end of their life or used for service. Not ideal for a brand-new long-term purchase."),
]

VEHICLE_FAQ = [
    ("Does the full registration number matter, or just the last digits?",
     "The full number is read, but the total reduced value carries most of the weight. The last four digits are "
     "also looked at as a secondary layer — which is why people often notice patterns there."),
    ("I'm buying a new car. Can you help me choose the number?",
     "Yes. That's the new-vehicle option (₹599). Send me the numbers you're being offered and your date of birth, "
     "and I'll rank them for you."),
    ("Can a number cause accidents?",
     "No. I won't tell you a number causes accidents — that's fear-selling. What a number describes is a driving "
     "style tendency and a general energy. Your driving habits matter infinitely more."),
    ("Is this useful for a two-wheeler?",
     "Yes, the same analysis applies to scooters and motorcycles."),
    ("My number has a letter in it. How is that handled?",
     "Letters convert to numbers using the standard chart, then the whole registration is reduced. I'll show you "
     "the working so it doesn't feel arbitrary."),
]

VEHICLE_BODY = page_hero(
    "Vehicle Number Numerology",
    "The registration number on your car or scooter, read as a pattern. Useful when buying, or when a vehicle has "
    "never quite felt right.",
    '<nav class="breadcrumbs" aria-label="Breadcrumb"><a href="/">Home</a>'
    '<span class="sep">/</span><a href="/consultations/">Consultations</a>'
    '<span class="sep">/</span><a href="/consultations/numerology/">Numerology</a>'
    '<span class="sep">/</span><span aria-current="page">Vehicle Numerology</span></nav>',
    badges=["From ₹299", "Delivered within 24 hours", "Hindi &amp; English", "Buying or existing"],
    cta_service="Vehicle Number Numerology",
) + f"""
{trust_bar()}

<section class="section">
  <div class="wrap">
    <div class="prose" style="max-width:78ch">
      <h2 style="margin-top:0">A practical way to use this</h2>
      <p>Vehicle numerology is the least mystical of the readings and the most immediately useful, because it
         often informs a purchase you're about to make anyway. If you're choosing between three registration
         numbers, knowing which one suits your own numbers is genuinely useful information — and it costs far
         less than most people assume.</p>
      <p>For an existing vehicle, the reading is more reflective: it describes the kind of relationship you tend
         to have with that vehicle — how much you use it, how it behaves, whether it feels like yours. Most
         clients find it recognisable rather than surprising.</p>
      <p><strong>What it won't do:</strong> predict accidents, guarantee safety, or replace servicing. If a
         number could prevent a crash, insurance companies would be out of business.</p>
    </div>

    <div class="mt-4">
      {section_head("The nine vehicle numbers", "A short orientation — your report includes the full working.")}
      <div class="table-scroll">
        <table class="price-table">
          <thead><tr><th>Number</th><th>Character</th><th>What it tends to mean in practice</th></tr></thead>
          <tbody>
            {''.join(f'<tr><td class="amount">{n}</td><td><strong>{q}</strong></td><td>{f}</td></tr>' for n, q, f in VEHICLE_NUMBERS)}
          </tbody>
        </table>
      </div>
      <p class="small muted mt-3">Master numbers (11, 22, 33) are read in full rather than reduced. Your report explains this where relevant.</p>
    </div>
  </div>
</section>

<div class="divider"></div>

<section class="section" id="pricing">
  <div class="wrap">
    {section_head("Pricing", "Existing numbers within 24 hours. New-vehicle guidance the same day where possible.")}
    <div style="max-width:820px;margin:0 auto">
      {price_table(
        ["Service", "What it covers", "Price"],
        [
          ["Vehicle Registration Analysis", ("Existing number", "Full reading of your current registration"), "₹299"],
          ["Vehicle &amp; Birth Number Compatibility", ("Comparison", "How the number sits against your own numbers"), "₹399"],
          ["New Vehicle Number Selection", ("Before you buy", "Two or three candidate numbers ranked for you"), "₹599"],
          ["Vehicle &amp; Owner Compatibility Report", ("Detailed", "Full report including timing notes"), "₹699"],
        ],
        2,
      )}
    </div>
  </div>
</section>

<div class="divider"></div>

<section class="section">
  <div class="wrap">
    {section_head("Questions before you book", "")}
    {faq_block(VEHICLE_FAQ)}
  </div>
</section>
""" + related_links("Related", [
    ("/consultations/numerology/house/", "House Numerology", "The number on your home"),
    ("/consultations/numerology/name/", "Name Numerology", "Your personal name number"),
    ("/consultations/numerology/", "All Numerology", "Life path, personal year and complete charts"),
]) + cta_block(
    "Check a vehicle number",
    "Send the registration number and your date of birth. If you're choosing between numbers, send all of them.",
    service="Vehicle Number Numerology",
)

VEHICLE = Page(
    path="consultations/numerology/vehicle/index.html",
    url="/consultations/numerology/vehicle/",
    title="Vehicle Number Numerology Online | Car & Bike Registration | ₹299",
    description=(
        "Vehicle number numerology with Nisha Pathak. Analyse your registration number or rank candidate numbers "
        "before buying. Delivered within 24 hours. From ₹299."
    ),
    h1="Vehicle Number Numerology",
    body=VEHICLE_BODY,
    nav="consultations",
    crumbs=[C, N, ("Vehicle", "/consultations/numerology/vehicle/")],
    og_image="/images/cat-numerology.webp",
    schema=[
        service_schema("Vehicle Number Numerology",
                       "Online numerology analysis of vehicle registration numbers, including new vehicle number selection.",
                       "/consultations/numerology/vehicle/", price_low="299", category="Numerology Consultation"),
        faq_schema(VEHICLE_FAQ),
        breadcrumb_schema([C, N, ("Vehicle", "/consultations/numerology/vehicle/")]),
    ],
)


# ============================================================ MARRIAGE

MARRIAGE_FAQ = [
    ("Do you match kundalis, or only numbers?",
     "This service is numbers-based — relationship numbers, couple compatibility and timing. If you want a "
     "traditional kundali milan with planetary analysis, book the Vedic Kundali service instead, or add it."),
    ("Can numerology tell me if we're compatible?",
     "It describes how two people's patterns interact — where they reinforce each other and where they'll "
     "friction. It doesn't issue a pass/fail. Couples who understand their friction points handle them better "
     "than couples who don't."),
    ("Can you tell me the best date to get married?",
     "I can suggest periods that align numerically. For a traditionally chosen muhurat you'd want a purohit or "
     "an astrologer working from the full chart — that's a different discipline and I'll say so rather than "
     "pretend otherwise."),
    ("My family wants a compatibility check before agreeing. Can this help?",
     "It can give everyone a shared framework and language for the conversation. That's often the most useful "
     "outcome — not a verdict, but a structure."),
    ("Is this only for people getting married?",
     "No. It's also used by couples already together who want to understand a recurring pattern."),
]

MARRIAGE = service_page(
    path="consultations/numerology/marriage/index.html",
    url="/consultations/numerology/marriage/",
    nav="consultations",
    crumbs=[C, N, ("Marriage & Compatibility", "/consultations/numerology/marriage/")],
    h1="Marriage & Compatibility Numerology",
    meta_title="Marriage Numerology India | Couple Compatibility | ₹499",
    meta_desc=("Marriage numerology and couple compatibility analysis online with Nisha Pathak. Relationship "
               "numbers, compatibility and timing guidance. Report in 24–48 hours. From ₹499."),
    lede=("How two people's numbers interact — where you reinforce each other, where you'll friction, and what "
          "phase the relationship is currently in."),
    img="/images/cat-numerology.webp",
    price_from="₹499",
    price_note="Report in 24–48 hours",
    who=[
        "You're deciding whether to move forward with a marriage",
        "Your family wants a compatibility check and you want a calmer framing",
        "You're already together and keep hitting the same friction",
        "You want to understand the timing of the next phase",
        "You're choosing a wedding period and want a numerical view",
    ],
    includes=[
        "Both partners' relationship numbers, calculated and compared",
        "Where the patterns reinforce each other",
        "The recurring friction points, named plainly",
        "Personal year cycles for the coming 12–24 months",
        "A written report you can share with your partner or family",
    ],
    process=[
        ("01", "Send both dates of birth", "And full names as written. That's all that's needed."),
        ("02", "Pay and confirm", "Report delivered within 24–48 hours."),
        ("03", "Read together", "Optional call if you'd like to talk through it as a couple."),
    ],
    pricing_headers=["Service", "What it covers", "Price"],
    pricing_rows=[
        ["Individual Relationship Number", ("One person", "Your relationship patterns and tendencies"), "₹499"],
        ["Couple Compatibility Report", ("Two people", "Compared patterns and friction points — most booked"), "₹799"],
        ["Marriage Date Selection Guidance", ("Timing", "Numerically aligned periods for the ceremony"), "₹799"],
        ["Marriage Compatibility Numerology", ("Detailed", "Compatibility plus personal year timing"), "₹999"],
        ["Detailed Couple Numerology Chart", ("Full report", "Everything, plus 24-month outlook"), "₹1,299"],
    ],
    popular=1,
    faqs=MARRIAGE_FAQ,
    related=[
        ("/consultations/tarot-readings/love/", "Love Tarot", "For a specific relationship situation"),
        ("/consultations/vedic-kundali/", "Vedic Kundali", "Traditional kundali milan with planetary analysis"),
        ("/consultations/numerology/name/", "Name Numerology", "Including surname-change considerations"),
    ],
    schema_name="Marriage & Compatibility Numerology",
    schema_desc=("Online marriage numerology and couple compatibility analysis, including relationship numbers and "
                 "timing guidance."),
    schema_low="499",
    disclaimer=("<strong>An honest note.</strong> This is a numbers-based compatibility reading, not a kundali "
                "milan. It describes patterns and friction — it does not issue a verdict on whether you should "
                "marry. For a traditional muhurat, consult a purohit or astrologer working from the full chart."),
    cta_title="Check compatibility",
    cta_text="Send both dates of birth and full names. I'll confirm which option fits and when you'll have the report.",
)


# ============================================================ BABY NAME

BABY_FAQ = [
    ("When should I book — before or after the baby is born?",
     "Either works. Before birth we use the expected date; after birth we use the actual date of birth, which is "
     "more accurate. Many parents book a shortlist check after the birth."),
    ("Can you suggest names, or only check ones I've chosen?",
     "Both. The new name selection option (₹999) includes a call where we work through options together. The "
     "standard option checks a shortlist you already have."),
    ("How many names can you check?",
     "Up to five in the standard report. More than that and it becomes a different conversation — message me and "
     "we'll work it out."),
    ("Does the surname count?",
     "Yes. The full name as it will be used is what's read, including the surname."),
    ("Is this a religious or scriptural naming process?",
     "No. This is numerology, not namkaran. If you're following a family or religious tradition for the naming "
     "ceremony, this sits alongside it rather than replacing it."),
]

BABY = service_page(
    path="consultations/numerology/baby-name/index.html",
    url="/consultations/numerology/baby-name/",
    nav="consultations",
    crumbs=[C, N, ("Baby Name Numerology", "/consultations/numerology/baby-name/")],
    h1="Baby Name Numerology",
    meta_title="Baby Name Numerology India | Auspicious Name Check | ₹699",
    meta_desc=("Baby name numerology with Nisha Pathak. Check a shortlist or choose a name against your baby's "
               "date of birth. Report in 24–48 hours. From ₹699."),
    lede=("Check the names on your shortlist, or work through options together — measured against your baby's "
          "date of birth."),
    img="/images/cat-numerology.webp",
    price_from="₹699",
    price_note="Report in 24–48 hours",
    who=[
        "You have a shortlist and want a numerical view before deciding",
        "You're choosing between family names and want a tie-breaker",
        "You've already named your baby and want to understand the pattern",
        "You want the name aligned with the birth date rather than chosen at random",
    ],
    includes=[
        "Name numbers for up to five shortlisted names",
        "Each name compared against the baby's date-derived numbers",
        "Spelling variations that shift the number, where useful",
        "A clear recommendation with reasoning you can explain to family",
        "Optional call to talk through the shortlist",
    ],
    process=[
        ("01", "Send the date of birth", "Actual or expected. Plus the shortlist, or ask for the selection call."),
        ("02", "Pay and confirm", "Report within 24–48 hours."),
        ("03", "Decide with confidence", "A written explanation you can share with your family."),
    ],
    pricing_headers=["Service", "What it covers", "Price"],
    pricing_rows=[
        ["Baby Name Numerology", ("Shortlist check", "Up to five names against the birth date"), "₹699"],
        ["Name + Full Chart for Baby", ("Combined", "Name check plus baby's core numbers"), "₹999"],
        ["New Name Selection Consultation", ("Includes a call", "20–30 minutes working through options together"), "₹999"],
    ],
    popular=0,
    faqs=BABY_FAQ,
    related=[
        ("/consultations/numerology/name/", "Name Numerology", "For your own name and spelling variations"),
        ("/consultations/numerology/", "All Numerology", "Life path, personal year and complete charts"),
        ("/consultations/vedic-kundali/", "Vedic Kundali", "Traditional chart-based naming guidance"),
        ("/resources/guides/baby-name-numerology/", "Baby Name Guide", "A sensible approach to naming"),
    ],
    schema_name="Baby Name Numerology",
    schema_desc="Online baby name numerology consultation checking a shortlist against the child's date of birth.",
    schema_low="699",
    disclaimer=("<strong>An honest note.</strong> This is numerology, not namkaran. If your family follows a "
                "religious or scriptural naming tradition, this sits alongside it rather than replacing it."),
    cta_title="Check your shortlist",
    cta_text="Send the date of birth and the names you're considering. I'll confirm the report timeline.",
)
