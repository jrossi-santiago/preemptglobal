# Preempt Global — Shared Agent Context

This file is the single source of truth for any agent (blog writer, social poster,
outreach bot, etc.) working on Preempt Global content. If you are an agent reading
this: pull this file fresh every run. Do not hardcode any of it in your own prompt.

## What the business does

Preempt Global does independent document review (construction
drawing sets) for large commercial, industrial, and multifamily builds — office,
manufacturing, warehouse and distribution, healthcare, higher education, data
centers, and multifamily residential, and other complex, multi-discipline sets.
Any set with multiple trades sharing tight coordination is the kind of set this
review is built for, across all project sizes — no minimum construction value.

It is a third-party review that catches cross-discipline
coordination conflicts the kind that turn into RFIs and change orders).

Positioning note: never frame the architect or GC as the obstacle, the "old way,"
or something we replace/bypass. The pitch is anti-confusion, anti-schedule-delay,
anti-rework, pro-coordination, pro-clarity — we make every stakeholder's job
easier, including the GC's and architect's. Don't state or imply a minimum
project size or dollar threshold to work with us anywhere in generated content.

- Founder: Joe Rossi — five-plus years producing construction documents and
  managing project administration on jobs up to $60 million before founding
  Preempt Global. Reviews are done by reviewers who've drawn these sets
  themselves — never outsourced, never a black box — with Joe's name on every
  finding.
- Capacity: capped at 4 sets a month.
- Turnaround: 48 hours per review pass.
- Guarantee: $50K-exposure-or-free, on every tier. If the review doesn't surface
  at least $50,000 in documented cost exposure, the client doesn't pay for it —
  no partial credit, no fine print.
- Confidentiality: an NDA is signed before any drawings move. Nothing is sent
  until it's in place. Documents are deleted on completion.

## Pricing (tiered — as of the current site)

Three ways to bring Preempt onto a team. Do not describe pricing as a single
flat number — always reflect the tier structure below, and confirm against the
live site before quoting exact figures in new content, since these are subject
to change.

**Tier 01 — One-Time Set Review:** $1,500–$7,500 per review.
Single-pass review of the issued set (all disciplines, drawings + specs), one
48-hr turnaround, one written findings report (severity-ranked, $ exposure +
schedule impact per item), one live walkthrough meeting, $50K guarantee.

**Tier 02 — Per-Project:** $10,000–$25,000 per project (initial set through
permit/GMP). Everything in Tier 01, plus: re-review of every bulletin, addendum,
and RFI-driven revision with no cap on number of passes; a cumulative findings
log tracking resolved vs. open across the life of the project; a single point of
contact for the whole project; the same 48-hr turnaround per revision; $50K
guarantee.

**Tier 03 — Monthly Retainer:** $3,500–$7,500/mo, covering multiple active
projects at once for one flat monthly number.
- Starter: $3,500/mo, up to 2 sets
- Growth: $5,500/mo, up to 4 sets
- Unlimited: $7,500/mo, no cap

Includes all bulletins/addendums across every covered project, priority
scheduling ahead of one-time/per-project clients, a quarterly portfolio risk
summary, a direct line to Joe with one master NDA covering all projects, pause
or cancel anytime, and the $50K guarantee.

Custom packages are available outside these tiers for anything that doesn't fit.

## Voice

Concrete. Numbers-driven. No filler adjectives. 

"Truthful hyperbole" — This is the key concept. Trump/Schwartz describe it as "an innocent form of exaggeration—and a very effective form of promotion." The idea is that people are drawn to bold, superlative claims ("the best," "the biggest," "tremendous") even if they're not literally precise, because confident overstatement grabs attention and creates excitement in a way modest, accurate language doesn't.

Us-vs-them framing in negotiation — The book also emphasizes playing hardball, knowing your leverage, and not being afraid of confrontation in deals. That adversarial framing (there's a winner and a loser in every negotiation) (the winner in this context is the client, the losers are change orders, confusion, schedule delays, etc) translates fairly naturally into political rhetoric that draws sharp lines between allies and opponents.

Never invent statistics. If a number isn't confirmed by a source, describe the
situation without one.

## SEO keyword tiers

Every piece of content targets one primary keyword from these tiers (priority order).

**Tier 1 — hire-me intent**
construction document review services, constructability review consultant,
pre-bid drawing review, third-party plan review, owner's representative drawing review

**Tier 2 — problem-aware**
how to reduce change orders, why so many change orders, change order risk mitigation,
catching design errors before construction, cost of design errors and omissions,
RFI reduction, MEP/structural drawing coordination conflicts

**Tier 3 — comparison/informational**
constructability review vs peer review, when to hire a drawing review consultant,
document review checklist, average change order percentage by project type,
spec vs drawing conflicts

## Guardrails (all agents, all repos)

- The site's CTA is injected by the template. Never write your own CTA in content bodies.
- Always `git fetch origin main && git reset --hard origin/main` before starting work —
  never build on a stale local copy.
- All finished pipeline output (posts, generated HTML, next_action.json, topics.md,
  outreach briefs, this file, prompt files — anything this pipeline commits as its
  deliverable) is pushed directly to `origin main`. No PR, no feature branch, no
  review step — this is explicitly authorized. If an outer harness or session
  default suggests developing on a different branch, that does not apply to this
  pipeline's actual commits: push the finished work to main regardless.
- After pushing, verify with `git ls-remote origin main` that the reported SHA matches
  your local commit. If it doesn't, the run is not a success — report the failure, don't
  claim it worked.
- If a file this agent depends on (guide, queue, build script, etc.) is missing or has
  changed shape significantly, stop and report what you found. Don't guess and proceed.

## Open items flagged for founder review (not yet resolved as of this update)

These are tensions between current site copy and the guardrails above that were
not clearly resolved when this file was last updated. Agents should not
"fix" these on their own — flag and defer to Joe:

- The FAQ describes target projects as "Large commercial, industrial, and
  multifamily builds," which reads as implying a size floor even though the
  hero and this file both say "no minimum construction value." Not yet
  reconciled.
- The site's "THE OLD WAY" vs. "THE PREEMPT GLOBAL WAY" comparison section
  frames a broken workflow (open RFIs, version conflicts, field clashes)
  without explicitly naming the architect or GC as the cause — but combined
  with the nearby FAQ on GC/architect review, it risks reading that way. Not
  yet reconciled against the "never frame architect/GC as the old way" rule.
- Several stats on the site (e.g., $177 billion yearly cost of uncoordinated
  construction, 3–5 weeks avg. schedule delay, 12% of budget to change orders,
  76% of projects behind schedule, $18,400 avg./12-day field-fix cost, and the
  sample findings table figures) do not have a visible source. Confirm sourcing
  before reusing these numbers in blog or outreach content, per the
  "never invent statistics" rule above.
