# Copy Changes Summary — Anti-Confusion Positioning

Branch: `copy/anti-confusion-positioning` (off `claude/run-prompt-u9yut9`). All 41 items from `COPY_AUDIT_LOG.md` were rewritten, plus 6 additional instances found during Phase 2 (noted below), plus a sync update to `PREEMPT_CONTEXT.md` (out of site-copy scope, but requested). **Nothing has been merged to main or pushed to a deploy branch — this is the approval gate.**

---

## index.html (homepage)

| Location | Before | After | Rationale |
|---|---|---|---|
| Hero positioning | "…for $30M+ commercial and industrial projects." | "…for large multifamily, warehouse and industrial, higher-ed, and commercial projects." | dollar threshold + missing vertical language |
| Hero proof line | "…that a top-5 GC's own coordination process missed." | "…surfaced by an independent owner-side pass after a top-5 GC's own coordination review." | anti-GC framing |
| Hero type-strip | DATA CENTERS / MANUFACTURING / HEALTHCARE / HIGHER-ED / WAREHOUSE & DIST. | + MULTIFAMILY added | missing vertical language |
| §01 header | "Three people read your drawings. None of them work for you." | "Three people read your drawings. Only one of them is reading for you." | adversarial tone |
| §01 lede | "…Everyone is doing their job exactly as their incentives ask them to. The problem is that none of those incentives are yours." | "…Every one of those reviews does its job well. None of them is scoped to catch cross-discipline coordination conflicts specifically for the owner." | adversarial tone |
| Architect card | "Checks for design intent — then stops." / "…Once it matches what they intended to draw, their review is done." | "Checks the set against design intent." / "…a real, necessary review, scoped to design intent rather than cross-discipline coordination." | anti-GC/architect framing |
| Contractor card | "Reads it like a chess board." / "Hunts for the gaps and ambiguities they can price later as change orders. A conflict found now is revenue found later." | "Reads it to price the work." / "Reviews the set to scope and price the job accurately — a coordination pass aimed at bid accuracy, not at flagging every cross-discipline conflict for the owner." | anti-GC/architect framing (most severe on site) |
| §01 pull quote | "…It is also exactly where the money leaks." | "…and it's exactly where coordination conflicts turn into change orders." | adversarial tone |
| §04 case lede | "Our independent, owner-side pass surfaced what that process missed." | "Our independent, owner-side pass added a dedicated read for the owner's specific exposure — the kind that process isn't scoped to catch." | anti-GC framing |
| Fit — "Worth your time if" | "…large commercial or industrial builds at $30M+ construction value" | "…large commercial, industrial, multifamily, or higher-ed builds" | dollar threshold + vertical language |
| FAQ — GC/architect review | "No — and that's the whole point. The architect QCs…The contractor reads it for what they can price later." | "…The contractor's coordination review is scoped to pricing the work accurately. Both are real, necessary reviews — neither is scoped to run for the owner specifically…still had 26 conflicts worth flagging." | anti-GC framing |
| FAQ — project types | "…If it's $30M+ in construction value with multiple trades sharing tight coordination…" | "…multifamily residential…If it's a set with multiple trades sharing tight coordination…" | dollar threshold + vertical language |

## findings/index.html

| Location | Before | After | Rationale |
|---|---|---|---|
| `<title>` | "…26 conflicts, 4 critical, 0 caught by anyone else" | "…26 Conflicts, 4 Critical, Documented in Full" | anti-GC framing (metadata — title itself carried the issue) |
| H1 | "One bid set. 26 conflicts. Zero caught by anyone else." | "One bid set. 26 conflicts. Every one documented in full." | anti-GC framing |
| Hero positioning | "…Every finding below survived that review before we opened the set." | "…Every finding below is what an independent, owner-side pass adds on top of that review." | anti-GC framing |
| §04 Method | "All twenty-six survived a general contractor's own internal coordination review…which is the entire argument for why an owner-side pass exists at all." | "…turned up on a set that had already been through a general contractor's own internal coordination review — which is the case for why a dedicated, owner-side pass is worth running alongside it, not instead of it." | anti-GC framing |

## handoff/index.html

| Location | Before | After | Rationale |
|---|---|---|---|
| §01 pillar §04 | "…no competing relationship, no incentive to look away." | "…no competing relationship, full incentive alignment with you." | adversarial tone (uncertain flag, resolved per confirmation) |
| "Why this exists" | "The GC reads for what they can price later." | "The GC's coordination review is scoped to pricing the work." | anti-GC framing |

## Blog posts (source `.md`, rebuilt to matching `blog/<slug>/index.html`, `blog/index.html`, sitemap.xml, robots.txt via `blog/build.py`)

### architect-qc-vs-owner-review.md
| Location | Before | After | Rationale |
|---|---|---|---|
| Title | "Architect QC Isn't Owner Protection — Here's the Difference" | "What Architect QC Covers — and Where an Owner-Side Review Picks Up" | adversarial tone |
| Deck | "…were never designed to catch the conflicts…" | "…aren't scoped to catch the conflicts…" | adversarial tone |
| Lede | "The contractor reads it for what can be priced later…neither one is built to protect the party writing the checks." / "…the pattern shows up on nearly every $30M+ set we've reviewed." | "The contractor's coordination review is scoped to pricing the work accurately…neither one is scoped to protect the party writing the checks." / "…nearly every large, multi-discipline set we've reviewed — commercial, multifamily, industrial, or higher-ed." | anti-GC framing + dollar threshold + vertical language |
| Body | "…a gap or ambiguity found during their own internal review often becomes a change order down the line, not a flagged issue during bid." | "…not to flagging cross-discipline conflicts on the owner's behalf, which is a different task with a different objective." | anti-GC framing |
| Body bullet | "Anyone paid by the GC or the design team is, structurally, reading for someone else." | "A dedicated, owner-paid read…run alongside the architect's QC and the GC's coordination review — not instead of them." | anti-GC framing |

### pre-bid-drawing-review-vs-ifc-timing.md
| Location | Before | After | Rationale |
|---|---|---|---|
| Body | "Applied to a $30M project…" | "Applied to a large capital project…" | dollar threshold |
| Callout | "…the GC now had a priced number to hold to and no incentive to absorb a fix that wasn't in their bid." | "…the GC now had a signed, priced contract — and any fix outside that scope was, by definition, a change to the deal both sides had already agreed to." | anti-GC framing |
| Body | "…it's that the bid window specifically is the last point where a contractor has no leverage over the fix." | "…the last point where no one yet has contractual leverage over the fix." | anti-GC framing (found in Phase 2) |
| Body | "A GC that finds an ambiguity during pricing has a rational reason to price around it quietly rather than flag it during bid…" | "An ambiguity found during pricing is easy for a bidder to price around rather than flag — competitive bidding rewards a clean number, not a raised hand…" | anti-GC framing |
| FAQ + JSON-LD | "…has an incentive to price around it conservatively and stay quiet, rather than flag it…" | "…has every reason to price around it conservatively rather than flag it…once a contract is signed and the fix is no longer free for anyone to catch." | anti-GC framing |

### rfi-reduction-coordination-conflicts.md
| Location | Before | After | Rationale |
|---|---|---|---|
| Lede | "…on $30M+ builds, the gap…" | "…on large, multi-discipline builds, the gap…" | dollar threshold |
| Body | "…a subcontractor priced around an ambiguity instead of flagging it, betting they'd recover the cost later through a change order." | "…a subcontractor priced around an ambiguity instead of flagging it, and the conflict simply never generated a formal question." | anti-GC framing |
| Body | "A GC tracking RFI count as a KPI has every incentive to discourage the practice of filing one…" | "When RFI count gets tracked as a KPI, there's a natural pull toward resolving anything…informally…" | anti-GC framing |
| FAQ + JSON-LD | "What's a good number of RFIs for a $30M construction project?" / "A $30M project generating well outside that range…" | "…for a large construction project?" / "A project generating well outside that range…" | dollar threshold |
| Body (found in Phase 2) | "…meaning a $30M project should expect somewhere in the range of 450–600 RFIs…" | "…meaning a large project should expect a proportional volume of RFIs…" | dollar threshold |
| Body (found in Phase 2) | "On a $30M project, even the lower end of that range is $900,000–$1.5M in exposure…" | "On a project this size, even the lower end of that range can mean $900,000–$1.5M in exposure…" | dollar threshold |

### missed-mep-clash-change-order-cost.md
| Location | Before | After | Rationale |
|---|---|---|---|
| Lede | "Every $30M+ project has at least one sheet…" | "Every large, multi-discipline project has at least one sheet…" | dollar threshold |
| Body | "An ambiguity or overlap found during that pass has a real incentive attached to staying quiet — flag it during bid and a competitor can undercut on a cleaner number; price around it and recover the gap later." | "An ambiguity or overlap found during that pass is easy to price around rather than flag — raising it during bid risks a competitor undercutting on a cleaner number." | anti-GC framing |
| Body (found in Phase 2) | "On a $30M project, the low end of just the design-error share of that range is close to $1M in exposure…" | "On a project this size, the low end…can still mean roughly $1M in exposure…" | dollar threshold |
| Takeaways (found in Phase 2) | "…a real number on a $30M job, not a rounding error." | "…a real number on a large project, not a rounding error." | dollar threshold |
| FAQ + JSON-LD | "…on a $30M-scale project routinely add up to $300,000–$400,000+…" | "…on a project at that scale routinely add up to $300,000–$400,000+…" | dollar threshold |

### anatomy-of-a-findings-report-third-party-plan-review.md
| Location | Before | After | Rationale |
|---|---|---|---|
| Lede | "Most owners on a $30M+ project…" | "Most owners on a large, multi-discipline project…" | dollar threshold |
| Body (found in Phase 2) | "A review of a $30M-scale project's bid set typically turns up…" | "A review of a large project's bid set typically turns up…" | dollar threshold |
| Body (found in Phase 2) | "…a findings report with zero or near-zero findings on a $30M+ set is a red flag…" | "…on a large, multi-discipline set is a red flag…" | dollar threshold |
| Body (found in Phase 2) | "…real exposure on a $30M job, not a rounding error…" | "…real exposure on a large project, not a rounding error…" | dollar threshold |
| FAQ + JSON-LD | "How many findings does a typical $30M project's drawing set have?" | "How many findings does a typical large project's drawing set have?" | dollar threshold |

### data-center-constructability-review-consultant.md
No changes. Reviewed in both Phase 1 and Phase 2 — no anti-GC framing, no dollar threshold, already names multiple verticals naturally.

## Non-site-copy update (requested explicitly, outside original audit scope)

### PREEMPT_CONTEXT.md
| Before | After | Rationale |
|---|---|---|
| "…for $30M+ commercial and industrial projects…conflicts the architect's own QC and the GC's coordination process are structurally not incentivized to catch." | "…for large multifamily, warehouse/industrial, higher education, and commercial projects, across all project sizes — no minimum construction value…conflicts the architect's own QC and the GC's coordination process aren't scoped to catch, since each is doing a different, legitimate job on the project." Plus a new explicit positioning note instructing future content-generation runs never to frame the GC/architect as the obstacle and never to state a dollar threshold. | This file isn't published site copy, but it's the brief every future blog/social/outreach agent reads before writing. Updating it prevents new content from reintroducing the exact framing this rewrite removes. |

---

## Uncertain calls — flagged for your review, not silently resolved

1. **handoff/index.html, "no incentive to look away."** Rewrote to "full incentive alignment with you." This was flagged uncertain in Phase 1; you confirmed the audit log as-is, so I applied the softer framing rather than leaving the original. If you'd rather keep the original phrasing, it's a one-line revert.
2. **anatomy-of-a-findings-report post, "Not the architect's QC repackaged" bullet.** Per the Phase 1 recommendation (which you confirmed), I left this mostly untouched — it reads as fair, factual scope differentiation rather than adversarial framing. No wording change was made beyond the dollar-threshold instance in the same section.
3. **Homepage type-strip ("MULTIFAMILY" added to "Sets reviewed across").** This is a factual claim about past work. I added it because the task brief describes multifamily as a core vertical, but I don't have independent confirmation of a specific multifamily engagement the way the data-center case study is documented elsewhere on the site. Worth a quick gut-check that this doesn't overstate track record — if there's no multifamily case history yet, consider a softer label like "Built for projects across" instead of "Sets reviewed across."

## Structural changes (flagging per ground rules — none required here)

No "starting at $X" badges, ceiling/floor UI elements, links, or CTAs needed to be removed or restructured. All $30M+ removals were straight text edits; no layout or component changes were required.

---

## What's next

Everything above is committed on `copy/anti-confusion-positioning`, pushed to origin, not merged. Please review and confirm before I merge to main or push anywhere further — per Phase 3, I won't do either without your explicit go-ahead.
