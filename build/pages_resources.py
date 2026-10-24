"""Resources: guides index, FAQ hub and articles."""
from __future__ import annotations

from components import (
    cta_block, faq_block, page_hero, related_links, section_head, trust_bar,
)
from layout import (
    Page, article_schema, breadcrumb_schema, faq_schema, wa_btn,
)

R = ("Resources", "/resources/")
G = ("Guides", "/resources/guides/")


def article_page(*, path, url, crumbs, h1, meta_title, meta_desc, lede, img,
                 published, modified, body_html, faqs, related) -> Page:
    from layout import breadcrumbs
    body = page_hero(h1, lede, breadcrumbs(crumbs),
                     badges=[f"Updated {modified}", "By Nisha Pathak", "8 min read"])
    body += f"""
<section class="section">
  <div class="wrap-narrow">
    <div class="prose">
      {body_html}
    </div>
    <div class="mt-4" style="padding:24px 0;border-top:1px solid var(--line)">
      {wa_btn("Ask me a question on WhatsApp", "Reading enquiry", "article-cta", "btn btn-gold")}
    </div>
  </div>
</section>

<section class="section-tight">
  <div class="wrap-narrow">
    <h2 style="font-size:24px;margin-bottom:16px">Related questions</h2>
    {faq_block(faqs)}
  </div>
</section>
"""
    body += related_links("Keep reading", related)
    body += cta_block(
        "Want this applied to your own situation?",
        "A reading takes the general and makes it specific. If something here resonated, that's usually the sign.",
        service="Reading enquiry",
    )
    return Page(
        path=path, url=url, title=meta_title, description=meta_desc, body=body,
        nav="resources", crumbs=crumbs, og_image=img,
        schema=[article_schema(meta_title, meta_desc, url, published, modified),
                faq_schema(faqs), breadcrumb_schema(crumbs)],
    )


# ============================================================ GUIDES INDEX

GUIDES_FAQ = [
    ("Do I need to read these before booking?",
     "No. They exist because a lot of people want to understand how this works before spending money — which is "
     "reasonable. Read if it helps; skip if you'd rather just talk."),
    ("Are these written by you or generated?",
     "Written by me, based on seven years of readings and roughly 1,600 clients. Where I'm uncertain about "
     "something, the article says so."),
]

GUIDES_BODY = page_hero(
    "Guides",
    "Plain-language explanations of tarot, numerology and the things clients ask before booking. No jargon, no "
    "fear-selling.",
    '<nav class="breadcrumbs" aria-label="Breadcrumb"><a href="/">Home</a>'
    '<span class="sep">/</span><a href="/resources/">Resources</a>'
    '<span class="sep">/</span><span aria-current="page">Guides</span></nav>',
    badges=["Written by Nisha", "Practical", "No jargon"],
) + f"""
{trust_bar()}

<section class="section">
  <div class="wrap">
    <div class="grid grid-2">
      <a class="card" href="/resources/guides/house-number-numerology/">
        <div class="card-img" style="background-image:url('/images/cat-numerology.webp')"></div>
        <div class="card-body">
          <h3>House Number Numerology: What Numbers 1–9 Actually Mean</h3>
          <p>Why a house that looks perfect on paper can feel unsettled — and how to read the number on your door.</p>
          <span class="card-link">Read the guide →</span>
        </div>
      </a>
      <a class="card" href="/resources/guides/baby-name-numerology/">
        <div class="card-img" style="background-image:url('/images/cat-kundali.webp')"></div>
        <div class="card-body">
          <h3>Baby Name Numerology: A Sensible Approach</h3>
          <p>How to use numerology when choosing a name without turning it into a source of anxiety.</p>
          <span class="card-link">Read the guide →</span>
        </div>
      </a>
      <a class="card" href="/resources/guides/questions-to-ask-in-a-tarot-reading/">
        <div class="card-img" style="background-image:url('/images/cat-tarot.webp')"></div>
        <div class="card-body">
          <h3>12 Questions That Make a Tarot Reading Useful</h3>
          <p>Why "will he text me" wastes a reading — and what to ask instead.</p>
          <span class="card-link">Read the guide →</span>
        </div>
      </a>
      <a class="card" href="/resources/guides/tarot-vs-numerology/">
        <div class="card-img" style="background-image:url('/images/cat-crystals.webp')"></div>
        <div class="card-body">
          <h3>Tarot vs Numerology: Which Should You Choose?</h3>
          <p>An honest comparison, including when neither is the right tool.</p>
          <span class="card-link">Read the guide →</span>
        </div>
      </a>
    </div>
  </div>
</section>

<div class="divider"></div>

<section class="section">
  <div class="wrap">
    {section_head("Questions readers ask", "")}
    {faq_block(GUIDES_FAQ)}
  </div>
</section>
""" + cta_block(
    "Prefer to just ask?",
    "You don't need to read anything first. Send a couple of lines about your situation and I'll tell you "
    "whether a reading will help.",
)

GUIDES = Page(
    path="resources/guides/index.html",
    url="/resources/guides/",
    title="Tarot & Numerology Guides | Plain-Language Explainers",
    description=(
        "Practical guides to tarot, numerology and Vedic astrology written by Nisha Pathak. Plain language, no "
        "jargon — for people who want to understand before they book."
    ),
    h1="Guides",
    body=GUIDES_BODY,
    nav="resources",
    crumbs=[R, G],
    schema=[faq_schema(GUIDES_FAQ), breadcrumb_schema([R, G])],
)


# ============================================================ FAQ HUB

FAQ_ALL = [
    ("Readings &amp; sessions", [
        ("How is a session delivered?",
         "By phone call or video call — whichever you prefer. You'll get the joining details on WhatsApp once your "
         "slot is confirmed. Everything is one-on-one with Nisha, never with a team."),
        ("How long is a session?",
         "A single-question tarot reading is 20 minutes. A focused reading is 45 minutes. A full reading is 60 "
         "minutes. Numerology and kundali are delivered as written reports."),
        ("Do you speak Hindi?",
         "Yes. Sessions are available in Hindi, English, or a mix of both. Tell me when booking and the entire "
         "session will be in that language."),
        ("Can I record the session?",
         "You're welcome to record it for your own use. I'd ask that you don't publish it, since it contains "
         "personal details."),
        ("What if I need to reschedule?",
         "Message at least 4 hours before your slot and we'll move it at no extra cost. Less than 4 hours and it "
         "depends on the day — ask and I'll try."),
        ("Do you offer refunds?",
         "Sessions are non-refundable once delivered. If you're unhappy with a session, tell me — I'd rather "
         "understand what went wrong than leave it."),
    ]),
    ("What readings can and can't do", [
        ("Can tarot predict the future?",
         "It can show you the dynamics of a situation as they stand, and where they're trending. It cannot "
         "guarantee events, and anyone who claims otherwise is guessing."),
        ("Are readings accurate?",
         "They're useful rather than accurate. A reading gives you language and structure for something you're "
         "already sensing. Its value is in the clarity it produces, not in a hit rate."),
        ("Will you tell me what I want to hear?",
         "No. That's the main reason clients stay. If the honest read is uncomfortable, you'll hear it — kindly, "
         "but plainly."),
        ("Can you make someone come back?",
         "No. I don't do work designed to override another person's choices. I can help you understand the "
         "situation and decide what you want to do."),
        ("Is this a substitute for therapy?",
         "No, and I'll say so if it seems relevant. A reading can give clarity; it can't treat anxiety, depression "
         "or trauma. If you're in distress, please also speak to a professional."),
    ]),
    ("Booking &amp; payment", [
        ("How do I book?",
         "Message on WhatsApp with your situation and preferred time window. I'll confirm the right reading, the "
         "price and the available slots."),
        ("When do I pay?",
         "Before the session — payment confirms the slot. For rituals, 50% upfront and 50% before the final day."),
        ("What payment methods do you accept?",
         "UPI and bank transfer. You'll get the details on WhatsApp after we confirm the booking."),
        ("Do you offer packages?",
         "Yes. Reading-plus-product bundles are listed on each service page. Custom combinations can be arranged "
         "on WhatsApp."),
        ("Are prices negotiable?",
         "No. The prices are already set for the amount of time and attention each service takes. What I will do "
         "is tell you honestly if a cheaper option would serve you just as well."),
    ]),
    ("Products &amp; shipping", [
        ("How long does delivery take?",
         "Dispatch within 2 working days, delivery 3–7 working days depending on location. Shipping within India "
         "is included."),
        ("Can I return a product?",
         "Opened oils and worn crystals can't be returned for hygiene reasons. Damaged or incorrect items are "
         "replaced or refunded if you message within 48 hours with a photo."),
        ("Are the products safe on skin?",
         "They're for external ritual use. Patch-test first, keep away from eyes and broken skin, and don't ingest "
         "them. If pregnant or managing a condition, check with your doctor."),
    ]),
]


def _faq_groups() -> str:
    out = []
    for group, items in FAQ_ALL:
        out.append(f'<h2 style="font-size:24px;margin:36px 0 6px">{group}</h2>')
        out.append(faq_block(items, open_first=False))
    return "".join(out)


FAQ_BODY = page_hero(
    "Frequently Asked Questions",
    "Everything clients ask before booking — pricing, delivery, what a reading can and can't do, and how the "
    "products work.",
    '<nav class="breadcrumbs" aria-label="Breadcrumb"><a href="/">Home</a>'
    '<span class="sep">/</span><a href="/resources/">Resources</a>'
    '<span class="sep">/</span><span aria-current="page">FAQs</span></nav>',
    badges=["Pricing", "Delivery", "Confidentiality", "Honest answers"],
) + f"""
<section class="section">
  <div class="wrap-narrow">
    {_faq_groups()}
  </div>
</section>
""" + cta_block(
    "Still have a question?",
    "Message me directly. I answer before you pay anything — including when the answer is that a reading won't help.",
)

_all_faqs = [item for _, items in FAQ_ALL for item in items]

FAQS = Page(
    path="resources/faqs/index.html",
    url="/resources/faqs/",
    title="FAQs | Tarot, Numerology, Pricing & Delivery | Tarot with Nisha",
    description=(
        "Answers to the questions clients ask most — how sessions work, what readings can and can't do, pricing, "
        "payment, product delivery and safety."
    ),
    h1="Frequently Asked Questions",
    body=FAQ_BODY,
    nav="resources",
    crumbs=[R, ("FAQs", "/resources/faqs/")],
    schema=[faq_schema(_all_faqs), breadcrumb_schema([R, ("FAQs", "/resources/faqs/")])],
)


# ============================================================ ARTICLE 1

A1_FAQ = [
    ("What if my house number adds to 11, 22 or 33?",
     "These are master numbers and are read in full rather than reduced to 2, 4 or 6. They tend to describe a more "
     "intense version of the underlying number — more pressure, more potential."),
    ("Does the flat number or the building number matter more?",
     "The number on the door you actually use is primary. Building and society numbers are secondary context."),
    ("Should I move because of a number?",
     "No. Location, light, neighbours, rent and commute matter far more. Use this to understand the atmosphere, not "
     "to veto a good home."),
]

A1 = article_page(
    path="resources/guides/house-number-numerology/index.html",
    url="/resources/guides/house-number-numerology/",
    crumbs=[R, G, ("House Number Numerology", "/resources/guides/house-number-numerology/")],
    h1="House Number Numerology: What the Numbers 1–9 Actually Mean",
    meta_title="House Number Numerology India | Meaning of Numbers 1–9 | Guide",
    meta_desc=(
        "What your house or flat number means in numerology — numbers 1 to 9 explained, plus why a home that looks "
        "perfect can feel unsettled. By Nisha Pathak."
    ),
    lede="A house number describes an atmosphere, not an outcome. Here's how to read yours without turning it into "
         "something to be afraid of.",
    img="/images/cat-numerology.webp",
    published="2026-10-24",
    modified="2026-10-24",
    body_html="""
      <p>Almost everyone who asks me about house numerology is really asking one of two things: <em>is my house
      number bad?</em> or <em>why does this home not feel like mine?</em></p>

      <p>The second question is more useful. A house number doesn't determine whether good or bad things happen to
      you. What it describes is the <strong>atmosphere of the space</strong> — the kind of behaviour the address
      tends to encourage, and the friction it tends to produce.</p>

      <p>Two people can live at the same address and experience it differently. But the pattern is usually
      recognisable, and that's what makes it useful.</p>

      <h2>How to calculate your house number</h2>
      <p>Take the number on the door you actually use and reduce it to a single digit. So 214 becomes 2+1+4 = 7.
      If you live at 11, 22 or 33, stop — these are master numbers and are read in full.</p>
      <p>If your address includes letters, the letters convert to numbers first. If you have both a flat number and
      a building number, the door number is primary and the building number is context.</p>

      <h2>The nine numbers, briefly</h2>

      <h3>1 — Independence</h3>
      <p>Self-directed and often solitary. Good for people starting something alone. If you want a busy, bustling
      home, this number can feel quiet.</p>

      <h3>2 — Partnership</h3>
      <p>Warm and relational. Emotions run higher here and small conflicts linger longer. Excellent for couples;
      harder if you need clear separation between work and home.</p>

      <h3>3 — Expression</h3>
      <p>Social, creative, rarely tidy. Guests, conversation, and a lot of coming and going. Great if you host
      often; tiring if you need silence to recharge.</p>

      <h3>4 — Structure</h3>
      <p>Practical and grounded. Routines form easily here, which is either a support or a rut depending on what
      you need. Strong for families; watch for rigidity.</p>

      <h3>5 — Movement</h3>
      <p>Restless and changeable. Travel, shifting plans, things not staying put. Lovely if you're transient;
      difficult if you're craving permanence.</p>

      <h3>6 — Care</h3>
      <p>The household becomes the centre of gravity. Comfortable, warm, and quietly demanding. Excellent for
      families; watch for over-responsibility.</p>

      <h3>7 — Reflection</h3>
      <p>Quiet and inward. Deep rest happens here. Good for writers, researchers, and anyone who needs retreat.
      Can tip into isolation if you're already prone to it.</p>

      <h3>8 — Ambition</h3>
      <p>Work bleeds into home. Money and status get attention. Strong for business owners; watch for the home
      feeling like an office.</p>

      <h3>9 — Completion</h3>
      <p>Endings, generosity, and a transitional quality. Suits short stays and turning points; less suited to
      long-term settling.</p>

      <h2>The mismatch is usually the answer</h2>
      <p>In my experience, the "problem" with a house number is almost never the number itself. It's the mismatch
      between what the number naturally supports and what the occupants need.</p>
      <p>A 5 house is wonderful for someone who travels constantly and miserable for someone who works from home
      and needs stillness. A 7 house is a gift to a writer and lonely for a family with young children.</p>
      <p>So before deciding your number is bad, ask what it's actually suited to — and whether that's what you
      need right now.</p>

      <h2>What you can and can't change</h2>
      <p>You can't change the number. You can change how it's written — adding a letter, using a nameplate, or
      adjusting how the entrance is presented. Sometimes that shifts the reading meaningfully. Sometimes it
      doesn't, and I'll tell you when it doesn't.</p>
      <p>What I won't do is tell you to move house because of a number. That would be irresponsible. Location,
      light, neighbours, rent and commute matter far more than any of this.</p>

      <blockquote><p>Use numerology to understand the atmosphere you're living in. Not to decide whether you're
      allowed to be happy there.</p></blockquote>

      <h2>When a proper reading helps</h2>
      <p>A full house analysis looks at the number, the nameplate if there is one, and how the occupants' own
      numbers interact with the address. That last part is where most of the useful insight sits — the same house
      genuinely does affect two people differently.</p>
      <p>If you're choosing between two homes, it's also worth doing before you commit rather than after.</p>
    """,
    faqs=A1_FAQ,
    related=[
        ("/consultations/numerology/house/", "House Number Reading", "A full analysis of your address"),
        ("/consultations/numerology/vehicle/", "Vehicle Numerology", "The number on your car"),
        ("/resources/guides/tarot-vs-numerology/", "Tarot vs Numerology", "Which one to choose"),
    ],
)


# ============================================================ ARTICLE 2

A2_FAQ = [
    ("Should the name match the birth date exactly?",
     "It doesn't need to match perfectly, and chasing a perfect match usually causes more anxiety than it resolves. "
     "A reasonable alignment is enough."),
    ("Does the surname count?",
     "Yes. The full name as it will be used is what's read, including the surname."),
    ("Can we change the name later if it doesn't work out?",
     "You can, but I'd gently suggest not treating the name as something to be optimised indefinitely. At some "
     "point the child has to just have a name."),
]

A2 = article_page(
    path="resources/guides/baby-name-numerology/index.html",
    url="/resources/guides/baby-name-numerology/",
    h1="Baby Name Numerology: A Sensible Approach",
    meta_title="Baby Name Numerology India | How to Choose a Name | Guide",
    meta_desc=(
        "How to use baby name numerology when choosing a name — without turning it into a source of anxiety. "
        "A practical guide by Nisha Pathak."
    ),
    lede="Numerology can be a useful tie-breaker when you're choosing a name. It becomes a problem when it turns "
         "into a test your child has to pass.",
    img="/images/cat-numerology.webp",
    published="2026-10-24",
    modified="2026-10-24",
    crumbs=[R, G, ("Baby Name Numerology", "/resources/guides/baby-name-numerology/")],
    body_html="""
      <p>I've done a lot of baby name readings, and the pattern is consistent: parents arrive with a shortlist,
      quietly worried that choosing the wrong one will set their child back somehow.</p>

      <p>That worry is understandable, and it's also worth putting down. A name number is one small influence among
      thousands. It is not a verdict on your child's future, and treating it as one creates exactly the kind of
      pressure nobody needs in the first month of parenthood.</p>

      <h2>What the name number actually describes</h2>
      <p>Every letter maps to a number. Added and reduced, they produce a name number — a description of how that
      name tends to land: how people read the person before they know them, and which qualities the name keeps
      emphasising.</p>
      <p>That's it. It's a first-impression layer, not a destiny.</p>

      <h2>A sensible way to use it</h2>
      <p>If you have a shortlist of three or four names you genuinely love, numerology works well as a
      <strong>tie-breaker</strong>. It gives you a reason to choose between options you already like, rather than a
      reason to reject a name you love.</p>
      <p>If you're using it to reject names, you'll find that almost every name has something you could object to.
      That's the trap.</p>

      <h2>What to compare against</h2>
      <p>The name number is read against the child's date-derived numbers — usually the life path number. You're
      looking for reasonable alignment, not a perfect match.</p>
      <ul>
        <li><strong>Reasonable alignment</strong> is enough. Don't chase perfection.</li>
        <li><strong>Spelling variations</strong> can shift a number. Sometimes a small change helps; sometimes it
            makes the name harder to live with, which matters more.</li>
        <li><strong>The surname counts.</strong> Read the full name as it will actually be used.</li>
        <li><strong>Say it out loud.</strong> A name that aligns numerically but sounds wrong at a school gate is
            the wrong name.</li>
      </ul>

      <h2>What I won't do</h2>
      <p>I won't tell you a name is "inauspicious" in a way that frightens you into a decision. I won't recommend
      changing a name after the birth because the numbers aren't ideal. And I won't pretend numerology has more
      authority here than your own judgement, your family's tradition, or how the name actually sounds.</p>

      <blockquote><p>The best baby name is one the parents can say with love a thousand times. Numerology can help
      you choose between good options. It shouldn't decide for you.</p></blockquote>

      <h2>What a reading includes</h2>
      <p>A standard check covers up to five shortlisted names against the expected or actual date of birth, with
      spelling variants where useful, and a written explanation you can share with family — which is often the
      most valuable part, because naming decisions tend to involve more people than just the parents.</p>
    """,
    faqs=A2_FAQ,
    related=[
        ("/consultations/numerology/baby-name/", "Baby Name Reading", "Check your shortlist properly"),
        ("/consultations/numerology/name/", "Name Numerology", "For your own name and spelling"),
        ("/resources/guides/house-number-numerology/", "House Number Numerology", "Numbers 1–9 explained"),
    ],
)


# ============================================================ ARTICLE 3

A3_FAQ = [
    ("What if my question is about someone else's behaviour?",
     "Reframe it toward what you can act on. 'What is he likely to do' is less useful than 'what should I do "
     "while I wait, and how long am I willing to'."),
    ("Is it okay to ask a yes/no question?",
     "You can, but you'll get less from it. A yes/no collapses a situation that usually has three or four "
     "possible versions."),
    ("How many questions should I bring?",
     "One. A single question explored properly beats five questions touched briefly."),
]

A3 = article_page(
    path="resources/guides/questions-to-ask-in-a-tarot-reading/index.html",
    url="/resources/guides/questions-to-ask-in-a-tarot-reading/",
    h1="12 Questions That Make a Tarot Reading Actually Useful",
    meta_title="Questions to Ask in a Tarot Reading | 12 Better Prompts | Guide",
    meta_desc=(
        "Why \"will he text me\" wastes a tarot reading — and 12 better questions for love, career and personal "
        "direction. By Nisha Pathak."
    ),
    lede="The quality of a reading is set before the cards are drawn. Here's how to ask something that will "
         "actually produce clarity.",
    img="/images/cat-tarot.webp",
    published="2026-10-24",
    modified="2026-10-24",
    crumbs=[R, G, ("Questions to Ask in a Tarot Reading", "/resources/guides/questions-to-ask-in-a-tarot-reading/")],
    body_html="""
      <p>In seven years of readings, the single biggest predictor of whether a session is useful isn't the spread,
      the deck, or the day. It's the question.</p>

      <p>"Will he come back?" produces a shallow reading, because it's a yes/no question about someone else's
      behaviour. "What am I not seeing about this relationship?" produces a deep one, because it's about something
      you can actually act on.</p>

      <h2>The reframe</h2>
      <p>A good question has three qualities: it's about something you can influence, it's specific enough to
      explore, and it's honest about what you're actually feeling.</p>
      <p>Most people arrive with a question that fails all three. That's not a criticism — it's just how anxiety
      works. It narrows attention onto the one thing you can't control.</p>

      <h2>For love and relationships</h2>
      <ol>
        <li><strong>"What am I not seeing about this situation?"</strong> — the workhorse question. Almost always
            produces something.</li>
        <li><strong>"What is this person actually able to offer right now, as things stand?"</strong> — different
            from "what do they feel", and far more useful.</li>
        <li><strong>"What am I avoiding by staying in this?"</strong> — uncomfortable, and usually the real
            question.</li>
        <li><strong>"What would it look like if I chose myself here?"</strong> — useful when you already know.</li>
        <li><strong>"How long am I willing to wait, and what would change my mind?"</strong> — turns an indefinite
            wait into a decision with edges.</li>
      </ol>

      <h2>For career and decisions</h2>
      <ol start="6">
        <li><strong>"Is the problem the role, the manager, or the industry?"</strong> — these need different exits.</li>
        <li><strong>"What am I getting from staying that I haven't admitted?"</strong> — usually safety, or
            familiarity, or avoiding a conversation.</li>
        <li><strong>"What would I need to see to feel safe leaving?"</strong> — turns fear into an actual checklist.</li>
        <li><strong>"What's the cost of another six months of this?"</strong> — the question people avoid, and the
            one that usually moves them.</li>
      </ol>

      <h2>For personal direction</h2>
      <ol start="10">
        <li><strong>"What pattern keeps repeating, and what is it asking me to learn?"</strong></li>
        <li><strong>"What am I pretending not to know?"</strong> — blunt, and effective.</li>
        <li><strong>"What would I do if I believed I deserved better?"</strong> — often the whole reading in one
            question.</li>
      </ol>

      <h2>Questions to avoid</h2>
      <p>Not because they're forbidden, but because they produce little:</p>
      <ul>
        <li>"Will he/she text me?" — reduces everything to one notification.</li>
        <li>"When exactly will X happen?" — invites false precision.</li>
        <li>"Does he love me?" — a yes/no about someone's interior state; unanswerable and unhelpful.</li>
        <li>"Is this person the one?" — outsources a decision you have to make.</li>
      </ul>

      <blockquote><p>A reading can't give you control over another person's behaviour. What it can do is show you
      where you actually have agency — which is usually more than you think, and rarely where you were looking.</p></blockquote>

      <h2>If you're not sure what to ask</h2>
      <p>That's completely fine, and it's common. Tell me what's been on your mind and we'll shape it into a
      question together at the start of the session. The shaping is often half the value.</p>
    """,
    faqs=A3_FAQ,
    related=[
        ("/consultations/tarot-readings/", "Tarot Readings", "Book a session with a better question"),
        ("/consultations/tarot-readings/love/", "Love Tarot", "Relationship-focused reading"),
        ("/resources/guides/tarot-vs-numerology/", "Tarot vs Numerology", "Which tool fits your question"),
    ],
)


# ============================================================ ARTICLE 4

A4_FAQ = [
    ("Can I do both?",
     "Yes, and it's common. A reading gives you the situation; numerology gives you the pattern underneath it. "
     "Together they're usually more useful than either alone."),
    ("Which is better for a first-timer?",
     "Numerology, usually. It's delivered as a written report you can read at your own pace, with no live "
     "conversation to manage."),
    ("Which is more accurate?",
     "Wrong frame. Neither predicts. Tarot describes a situation's dynamics; numerology describes recurring "
     "patterns and cycles. They answer different questions."),
]

A4 = article_page(
    path="resources/guides/tarot-vs-numerology/index.html",
    url="/resources/guides/tarot-vs-numerology/",
    h1="Tarot vs Numerology: Which Should You Choose?",
    meta_title="Tarot vs Numerology | Which Reading Should You Book? | Guide",
    meta_desc=(
        "An honest comparison of tarot and numerology — what each is good for, what each can't do, and how to "
        "choose. By Nisha Pathak."
    ),
    lede="They answer different questions. Choosing the wrong one is the most common reason people feel a reading "
         "didn't help.",
    img="/images/cat-crystals.webp",
    published="2026-10-24",
    modified="2026-10-24",
    crumbs=[R, G, ("Tarot vs Numerology", "/resources/guides/tarot-vs-numerology/")],
    body_html="""
      <p>People often treat tarot and numerology as two flavours of the same thing. They're not, and the difference
      matters more than most practitioners admit — partly because admitting it would mean turning down bookings.</p>

      <h2>The short version</h2>
      <p><strong>Tarot answers: what is happening in this situation right now?</strong></p>
      <p><strong>Numerology answers: what pattern am I in, and what phase is it?</strong></p>
      <p>If you have a specific situation with moving parts — a relationship, a job offer, a decision — tarot is
      usually the better tool. If you have a recurring feeling, a sense of being stuck, or you want to understand
      your own tendencies, numerology is usually better.</p>

      <h2>What tarot is good at</h2>
      <ul>
        <li>Reading the dynamics of a live situation</li>
        <li>Surfacing what you're avoiding</li>
        <li>Describing other people's likely positions (with appropriate uncertainty)</li>
        <li>Turning a fog into three concrete options</li>
        <li>Working in real time, in conversation</li>
      </ul>

      <h2>What tarot is bad at</h2>
      <ul>
        <li>Guaranteeing outcomes — it can't, and anyone who says it can is guessing</li>
        <li>Precise dates</li>
        <li>Anything requiring specialist knowledge: salary maths, contracts, medical questions</li>
        <li>Long-term pattern analysis — that's numerology's job</li>
      </ul>

      <h2>What numerology is good at</h2>
      <ul>
        <li>Describing recurring patterns and cycles</li>
        <li>Timing personal years — "what phase am I in"</li>
        <li>Name analysis, which tarot can't touch</li>
        <li>House, vehicle and business numbers</li>
        <li>Being read at your own pace, as a written report</li>
      </ul>

      <h2>What numerology is bad at</h2>
      <ul>
        <li>Specific situations with multiple moving parts</li>
        <li>Anything requiring a live conversation to untangle</li>
        <li>Emotional nuance — it's a map, not a conversation</li>
        <li>It also can't predict, despite what some practitioners imply</li>
      </ul>

      <h2>How to choose</h2>
      <p>Ask yourself one question: <em>do I have a situation, or do I have a pattern?</em></p>
      <p>If you can name the situation — "my ex messaged me last week", "I have an offer and I don't know whether to
      take it" — book a tarot reading.</p>
      <p>If what you have is vaguer — "I keep ending up in the same relationship", "I always feel behind", "something
      feels off and I can't name it" — start with numerology.</p>

      <h2>When neither is the right tool</h2>
      <p>This is worth saying plainly. If you're dealing with a legal problem, a medical issue, a financial crisis,
      or a mental health difficulty, neither tarot nor numerology is the right first call. A reading might give you
      comfort alongside proper help, but it shouldn't substitute for it.</p>
      <p>I'll tell you that directly if it comes up. It costs me a booking and it's the right thing to do.</p>

      <blockquote><p>Choose tarot for a situation. Choose numerology for a pattern. Choose something else entirely
      if the problem has a professional solution.</p></blockquote>
    """,
    faqs=A4_FAQ,
    related=[
        ("/consultations/tarot-readings/", "Tarot Readings", "For a specific situation"),
        ("/consultations/numerology/", "Numerology", "For patterns and cycles"),
        ("/resources/guides/questions-to-ask-in-a-tarot-reading/", "Better Questions", "How to ask something useful"),
    ],
)

ARTICLES = [A1, A2, A3, A4]
