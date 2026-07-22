# Personal LinkedIn Framework

Reference doc for the "personal" LinkedIn agent (posts_personal). This agent runs in parallel
to the pillar-based LinkedIn agent (`linkedin/posts/`) but writes on a different topic axis and
under a different content framework. The two agents never share calendars or topic pools.

See `PREEMPT_CONTEXT.md` (repo root) for business facts and guardrails, `linkedin/context/BRAND_VOICE.md`
for voice, and `linkedin/context/SWIPE_PATTERNS.md` for hook/CTA mechanics. This doc covers only
what's specific to this agent: post types, the weekly mix, and the topic bank.

---

## Audience

Preempt Global, targeting construction/construction-ownership and project-delivery clients.

---

## Post types

Every post is one of these 7 types, each doing a specific job:

- **Conviction** — a belief stated with zero hedging. Filters the audience; unfollows are fine.
- **Story** — one specific moment with a lesson the reader can steal. Reader sees themselves in it.
- **Midas** — a result first (numbers, outcome), explanation after. Teach through the win, don't flex.
- **Doc** — a named framework or system, presented as a shareable reference. Problem it kills, then walkthrough.
- **Hot Take** — a contrarian critique of how the industry does something, backed by receipts, not just opinion.
- **Transformation** — before vs. after. Reader identifies with the "before."
- **Vulnerability** — a real failure and what it taught you. Rare — only use if it's been 3+ weeks since the last one.

Hook should fit the type — e.g. Conviction posts open with the stated belief, Doc posts open by
naming the framework and the problem it kills.

---

## This week's mix (fixed default)

7 posts:
- 2× Doc
- 2× Story
- 1× Midas
- 1× Conviction **or** Hot Take (choose based on topic fit)
- 1× Transformation

**Exception:** if no Vulnerability post has run in the last 3 weeks (check `linkedin/CALENDAR_PERSONAL.md`),
swap one Story or Transformation slot for a Vulnerability post instead.

---

## Topic bank

Pull topics from here only — do not invent unrelated topics.

**Documentation & Process:** RFIs (writing them, response-time tracking, common mistakes),
change orders (pricing disputes, scope creep, documentation, markup negotiation), submittals
(review turnaround, approval bottlenecks, log tracking), document control (version control,
addenda distribution, set-of-record disputes)

**Construction Administration:** owner's rep role, site visit reports, punch lists, pay
applications (AIA G702/G703, retainage disputes)

**Cost & Schedule:** critical path scheduling (float, look-aheads, delay claims), budget
tracking/cost codes, long-lead procurement, value engineering

**Risk & Disputes:** claims (differing site conditions, delay claims, documentation), contracts
(AIA documents, indemnification, risk allocation), insurance & bonding basics

**Technology:** BIM coordination/clash detection, AI in document review, construction PM
software adoption (Procore, PlanGrid, Autodesk Build), drone site surveys

**Closeout & Quality:** as-builts and O&M manuals, QA/QC processes, warranty tracking

---

## Post mechanics

- 165–215 words per post.
- No links in the post body — note "[link in first comment]" instead if one is needed.
- Apply `linkedin/context/SWIPE_PATTERNS.md`: direct-address hooks (not "I found/reviewed X"),
  a named framework or clear structure where relevant, concrete specific numbers, and always
  end with a real CTA (never "DM me if interested").
- Match `linkedin/context/BRAND_VOICE.md` exactly.
