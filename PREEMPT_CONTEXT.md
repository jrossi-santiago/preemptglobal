# Preempt Global — Shared Agent Context

This file is the single source of truth for any agent (blog writer, social poster,
outreach bot, etc.) working on Preempt Global content. If you are an agent reading
this: pull this file fresh every run. Do not hardcode any of it in your own prompt.

## What the business does

Preempt Global does independent, owner-side document review (bid/IFC construction
drawing sets) for large multifamily, warehouse/industrial, higher education, and
commercial projects, across all project sizes — no minimum construction value. It
is a third-party review, paid by the owner, that catches cross-discipline
coordination conflicts (the kind that turn into RFIs and change orders) —
conflicts the architect's own QC and the GC's coordination process aren't scoped
to catch, since each is doing a different, legitimate job on the project.

Positioning note: never frame the architect or GC as the obstacle, the "old way,"
or something we replace/bypass. The pitch is anti-confusion, anti-schedule-delay,
anti-rework, pro-coordination, pro-clarity — we make every stakeholder's job
easier, including the GC's and architect's. Don't state or imply a minimum
project size or dollar threshold to work with us anywhere in generated content.

- Founder: Joe Rossi
- Price: $3,000
- Turnaround: 48 hours
- Guarantee: free if the review doesn't find $50,000+ in exposure

## Voice

Concrete. Numbers-driven. Skeptical of hype. No fluff. No filler adjectives.
Match the tone of existing published posts in `blog/posts/` — read a couple before
writing anything new.

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
