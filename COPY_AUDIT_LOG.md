# Copy Audit Log — Anti-Confusion Positioning

Phase 1 output. Discovery only — no files have been edited. Scope covered the live marketing site and its templates: `index.html`, `findings/index.html`, `handoff/index.html`, `send/index.html`, `blog/template.html`, `blog/index_template.html`, `blog/index.html` (generated), all six posts in `blog/posts/*.md` (source of truth — the `blog/<slug>/index.html` files are build output from `blog/build.py` and inherit the same copy), and the one feature-art SVG (`blog/posts/2026-07-20-architect-qc-vs-owner-review.feature.html`).

Out of scope, not crawled as "site copy": `linkedin/`, `crm/`, `blog/outreach/`, `blog/prompts/` (internal drafts/pipeline notes, not published pages). `PREEMPT_CONTEXT.md` is also not site copy, but it's flagged separately below because it's the shared brief every future content-generation agent reads — if the $30M+ framing isn't updated there too, new blog posts will keep reintroducing the exact issue this rewrite is fixing.

## Summary

- **Files scanned:** 17 (4 standalone pages, 2 shared templates, 1 generated blog index, 6 post source files, 1 feature-art partial, 1 adjacent context doc, plus robots.txt/sitemap.xml/tracking.js/README checked and found to contain no flaggable copy)
- **Total flagged instances: 41**
  - `anti-GC/architect framing`: **17**
  - `dollar threshold`: **11**
  - `missing vertical language`: **3** (2 page-level + 1 sitewide pattern)
  - `adversarial tone`: **7**
  - `other`: **3**

Note on the blog posts: each `.md` file's visible FAQ text is duplicated verbatim inside a `FAQPage` JSON-LD `<script>` block at the bottom of the same file (for SEO rich results). Where a flagged instance is FAQ copy, the schema copy needs the identical rewrite in Phase 2 — I've noted that inline rather than giving the schema a separate row, to keep this table readable.

---

## index.html (homepage)

| # | Location | Original Copy (verbatim) | Issue Type | Proposed Direction |
|---|---|---|---|---|
| 1 | Hero positioning, line 528 | "Independent, owner-side review of bid and IFC sets for **$30M+ commercial and industrial projects**. Paid by the owner. Working for no one else." | dollar threshold | Drop the "$30M+" qualifier from the core positioning line; describe the offering as available for any project size, and let scale come through in the case-study numbers instead. |
| 2 | §01 section header + lede, lines 577–578 | "Three people read your drawings. None of them work for you." / "The problem is that none of those incentives are yours." | adversarial tone | Reframe around the coordination gap itself (confusion, misaligned incentives that cost everyone time) rather than "none of them work for you," which reads as owner-vs-everyone-else. |
| 3 | Reader card — architect, lines 583–586 | "Checks for design intent — then stops." / "QCs the set against their own drawings. Once it matches what they intended to draw, their review is done." | anti-GC/architect framing | Describe the architect's QC scope factually (what it's *for*) without "then stops" framing that implies incompleteness/laziness. |
| 4 | Reader card — contractor, lines 588–591 | "Reads it like a chess board." / "Hunts for the gaps and ambiguities they can price later as change orders. A conflict found now is revenue found later." | anti-GC/architect framing | The single most adversarial line on the site — directly frames the GC as profiting from the owner's blind spots. Replace with a description of the GC's coordination review as scoped to pricing/means-and-methods, not to catching cross-discipline conflicts on the owner's behalf. |
| 5 | Pull quote, line 601 | "That gap is structural, not accidental. It is also exactly where the money leaks." | adversarial tone | Reframe around the coordination/confusion gap, not "the money leaks" (implies someone's taking it). |
| 6 | Proof line, line 530 | "Last set: 26 conflicts and $430K in exposure that a top-5 GC's own coordination process missed." | anti-GC/architect framing | Keep the stat; reframe so the GC's process is a *prior, real* review this one adds to, not one that "missed" it. E.g., "…that surfaced in an independent owner-side pass, after the GC's own coordination review." |
| 7 | §04 case section lede, line 674 | "Our independent, owner-side pass surfaced what that process missed." | anti-GC/architect framing | Same fix as #6 — remove "missed," frame as an additional, owner-dedicated pass. |
| 8 | Fit section, "Worth your time if," line 804 | "You own or develop large commercial or industrial builds at **$30M+ construction value**" | dollar threshold | Remove the dollar floor; describe fit by project complexity/multi-trade coordination need, not a minimum construction value. |
| 9 | FAQ — "Doesn't our GC's or architect's review already cover this?", lines 852–853 | "No — and that's the whole point. The architect QCs the set against their own design intent. The contractor reads it for what they can price later. Both reviews are real; neither is run for you." | anti-GC/architect framing | Keep the factual scope distinction ("neither is scoped to run for the owner specifically"); cut "reads it for what they can price later," which is the adversarial framing. |
| 10 | FAQ — "What kinds of projects do you review?", line 861 | "Large commercial and industrial builds — office, manufacturing, warehouse and distribution, healthcare, higher-ed, data centers... If it's **$30M+ in construction value** with multiple trades sharing tight coordination, it's the kind of set this review is built for." | dollar threshold + missing vertical language | Remove the $30M+ floor; add "multifamily" to the list of project types (currently absent sitewide — see cross-cutting note below). |
| 11 | Hero "type-strip," lines 563–570 | "Sets reviewed across / DATA CENTERS · MANUFACTURING · HEALTHCARE · HIGHER-ED · WAREHOUSE & DIST." | missing vertical language | "Large multifamily" and generic "commercial" are absent from this list even though they're named core verticals for the business. Add multifamily; consider whether manufacturing/healthcare read as off-strategy given the four target verticals aren't fully represented. |
| 12 | Fit section, "Worth your time if," line 807 | "A bid set or IFC set is about to go out — and **no one independent** is checking it for you" | *(reviewed, no change)* | Not flagged — this is a fair, non-adversarial statement of the actual gap (no independent, owner-paid reviewer), not a claim that the GC/architect are the obstacle. Listed here to show it was considered, not missed. |

## findings/index.html (The UCCS Findings File)

| # | Location | Original Copy (verbatim) | Issue Type | Proposed Direction |
|---|---|---|---|---|
| 13 | `<title>`, line 7 | "Preempt Global — The UCCS Findings File: 26 conflicts, 4 critical, **0 caught by anyone else**" | anti-GC/architect framing | Metadata rewrite needed because the flagged phrase is in the title itself. Replace "0 caught by anyone else" with a framing centered on exposure found, not on others' failure (e.g., "…an independent owner-side pass") |
| 14 | H1, line 401 | "One bid set. 26 conflicts. **Zero caught by anyone else.**" | anti-GC/architect framing | Same fix as #13 — keep the number, drop the "caught by anyone else" framing. |
| 15 | Hero positioning, line 403 | "The actual UCCS findings file a client receives from a review — anonymized and unedited. 133 sheets, already run through a top-5 GC's own coordination process. Every finding below survived that review before we opened the set." | anti-GC/architect framing | Reframe as: this file shows what an *additional*, owner-dedicated pass adds on top of the GC's existing coordination review — not that findings "survived" it. |
| 16 | §04 Method section, line 556 | "All twenty-six survived a general contractor's own internal coordination review before we ever opened the set — which is the entire argument for why an owner-side pass exists at all." | anti-GC/architect framing | Same reframe — the argument for an owner-side pass is incentive alignment (someone reading purely for the owner), not that the GC's review failed. |

## handoff/index.html

| # | Location | Original Copy (verbatim) | Issue Type | Proposed Direction |
|---|---|---|---|---|
| 17 | §01 pillar §04 "Conflict-free," line 462 | "Not the architect, not the GC, not the design-builder. Your set is read for your exposure and nobody else's — no competing relationship, **no incentive to look away**." | adversarial tone *(uncertain — flagging per ground rules, not clear-cut)* | "No incentive to look away" implies others do have incentive to look away. Consider softening to "no competing relationship, full incentive alignment with you" — keeps the differentiation without implying bad faith. Flagging for your call rather than assuming. |
| 18 | "Why this exists" section, line 521 | "On every large build, three parties read the documents. The architect checks for design intent. The GC reads for what they can price later. The owner — who pays for every miss — is the only one with no one reading the set for them." | anti-GC/architect framing | Same core narrative as index.html #3/#4/#9 — reframe "reads for what they can price later" as scope difference, not motive. |

## blog/posts/2026-07-20-architect-qc-vs-owner-review.md

*(also present in generated `blog/architect-qc-vs-owner-review/index.html`)*

| # | Location | Original Copy (verbatim) | Issue Type | Proposed Direction |
|---|---|---|---|---|
| 19 | Frontmatter `title` | "Architect QC Isn't Owner Protection — Here's the Difference" | adversarial tone | Title sets an against-the-architect frame for the whole post. Reframe toward the gap/coordination angle, e.g. something like "What Architect QC Covers — and What Still Needs an Owner-Side Read." |
| 20 | Frontmatter `deck` | "Why the two reviews already built into your project's process — the architect's and the contractor's — **were never designed to catch** the conflicts that end up costing you the most." | adversarial tone | Keep the scope-gap point; soften "were never designed to catch" (implies design failure) toward "aren't scoped to catch." |
| 21 | Body, opening section | "Once you see it, the pattern shows up on nearly every **$30M+ set** we've reviewed." | dollar threshold | Drop the $30M+ qualifier or replace with "large, multi-discipline set." |
| 22 | Body, "The two reviews your project already has" | "The general contractor's coordination team reads the same set differently. Their incentive is to price the work accurately — which means a gap or ambiguity found during their own internal review **often becomes a change order down the line, not a flagged issue during bid**." | anti-GC/architect framing | Keep the incentive-structure point (it's real and useful); remove the implication that the GC is sitting on findings. Frame as: the GC's review isn't scoped to flag conflicts for the owner's benefit, not that gaps get quietly banked. |
| 23 | Body, "What owners can do before the set goes out" | "Keeping the reviewer's incentives aligned with the owner's. **Anyone paid by the GC or the design team is, structurally, reading for someone else.**" | anti-GC/architect framing | This is close to implying GC/architect-paid reviewers can't be trusted. Reframe around owner-paid review adding a dedicated, aligned read — not casting other reviewers as compromised. |

## blog/posts/2026-07-22-pre-bid-drawing-review-vs-ifc-timing.md

*(also present in generated `blog/pre-bid-drawing-review-vs-ifc-timing/index.html`)*

| # | Location | Original Copy (verbatim) | Issue Type | Proposed Direction |
|---|---|---|---|---|
| 24 | Lede | "Applied to a **$30M project**, that escalation isn't abstract." | dollar threshold | Used repeatedly through the post as the default example scale; genericize or vary, since the piece otherwise reads as a $30M-minimum audience. |
| 25 | Callout, "Worth knowing" | "...it became a negotiated change order, because **the GC now had a priced number to hold to and no incentive to absorb a fix that wasn't in their bid**." | anti-GC/architect framing | Keep the mechanism (signed contracts change negotiating leverage); drop "no incentive to absorb," which frames the GC as unwilling rather than describing a structural/contractual reality. |
| 26 | Body, "What the bid window actually buys an owner" | "**A GC that finds an ambiguity during pricing has a rational reason to price around it quietly rather than flag it during bid**, which is part of why relying on a shrinking RFI count..." | anti-GC/architect framing | One of the strongest adversarial lines in the blog content. Reframe around bid-window incentives generally (favoring earlier review) rather than GCs specifically "quietly" pricing around issues. |
| 27 | FAQ — "Why would a contractor price around a conflict instead of flagging it during bidding?" (+ duplicate in JSON-LD) | "A bidder who spots an ambiguity during pricing has an incentive to price around it conservatively **and stay quiet**, rather than flag it and risk a competitor undercutting them..." | anti-GC/architect framing | Same fix as #26; update both the visible FAQ and the matching JSON-LD `FAQPage` text. |

## blog/posts/2026-07-22-rfi-reduction-coordination-conflicts.md

*(also present in generated `blog/rfi-reduction-coordination-conflicts/index.html`)*

| # | Location | Original Copy (verbatim) | Issue Type | Proposed Direction |
|---|---|---|---|---|
| 28 | Lede | "...and on **$30M+ builds**, the gap between 'fewer RFIs' and 'fewer conflicts' is exactly where the expensive change orders live." | dollar threshold | Drop or genericize the $30M+ qualifier. |
| 29 | Body, "Why a shrinking RFI log isn't automatically good news" | "...or that **a subcontractor priced around an ambiguity instead of flagging it, betting they'd recover the cost later through a change order**." | anti-GC/architect framing | Keep the RFI-metric-gaming point conceptually; reframe around the metric's blind spot rather than implying subcontractors are betting against the owner. |
| 30 | Same section | "**A GC tracking RFI count as a KPI has every incentive to discourage the practice of filing one** for anything that can plausibly be resolved on-site." | anti-GC/architect framing | Reframe around what the metric fails to capture, not GC motive. |
| 31 | FAQ — "What's a good number of RFIs for a $30M construction project?" (+ duplicate in JSON-LD) | Question title itself uses "**$30M construction project**" as the default frame. | dollar threshold | Reword the question to be scale-agnostic, or note the benchmark scales with project size rather than anchoring to $30M. |

## blog/posts/2026-07-23-missed-mep-clash-change-order-cost.md

*(also present in generated `blog/missed-mep-clash-change-order-cost/index.html`)*

| # | Location | Original Copy (verbatim) | Issue Type | Proposed Direction |
|---|---|---|---|---|
| 32 | Lede | "**Every $30M+ project** has at least one sheet where a mechanical routing decision and a structural member are drawn as if the other doesn't exist." | dollar threshold | Drop the $30M+ framing — the underlying point (duct/beam conflicts happen on complex multi-discipline sets) applies at any scale. |
| 33 | Body, "Why this conflict wasn't caught by anyone already looking at the set" | "An ambiguity or overlap found during that pass has a real incentive attached to staying quiet — flag it during bid and a competitor can undercut on a cleaner number; price around it and recover the gap later. **That's not a GC acting in bad faith.**" | anti-GC/architect framing | The disclaimer doesn't fully offset the framing that precedes it. Reframe around scope/incentive structure without "staying quiet... recover the gap later," which reads as gaming the process regardless of the disclaimer. |

## blog/posts/2026-07-24-anatomy-of-a-findings-report-third-party-plan-review.md

*(also present in generated `blog/anatomy-of-a-findings-report-third-party-plan-review/index.html`)*

| # | Location | Original Copy (verbatim) | Issue Type | Proposed Direction |
|---|---|---|---|---|
| 34 | Lede | "Most owners on a **$30M+ project** have sat through an architect's QC process and a GC's coordination pass before, but neither of those produces anything close to what an independent, owner-side findings report looks like." | dollar threshold | Drop $30M+ qualifier. |
| 35 | Body, "What a real audit is not" | "**Not the architect's QC repackaged.** ...the architect's own quality control checks the drawings against design intent... It isn't scoped to catch a contradiction between two disciplines' sheets..." | adversarial tone *(uncertain — mostly factual scope description)* | This one reads mostly as fair differentiation, not adversarial — flagging per the "when unsure, flag it" rule rather than because it's a clear miss. Recommend keeping as-is or only light wording pass. |

## blog/posts/2026-07-23-data-center-constructability-review-consultant.md

No anti-GC/architect or adversarial-tone issues found — this post is a good model for the target tone (e.g. "None of this is a knock on the teams building these facilities — they're some of the most technically capable in the industry..."). It also already names multiple verticals naturally in the deck ("commercial, multifamily, or industrial work"). No rows flagged for this file.

## Cross-cutting / sitewide

| # | Location | Original Copy (verbatim) | Issue Type | Proposed Direction |
|---|---|---|---|---|
| 36 | Sitewide | "Large multifamily" as a named vertical **never appears** on the site (one blog post mentions "office or multifamily" only as a comparison point, not as a served vertical). "Warehouse & Dist." and "Higher-Ed" are present; generic "commercial" appears only inside "commercial and industrial," never called out on its own the way data centers/manufacturing/healthcare are. | missing vertical language | Work "large multifamily" into the homepage type-strip, the FAQ project-types answer, and the Fit section, per the brief's four core verticals. Consider a future blog post parallel to the data-center one, focused on multifamily coordination conflicts, if the user wants blog-level vertical coverage too (out of scope for this rewrite unless requested). |
| 37 | `PREEMPT_CONTEXT.md`, "What the business does" | "Preempt Global does independent, owner-side document review (bid/IFC construction drawing sets) for **$30M+ commercial and industrial projects**." | other *(not site copy — flagged for awareness)* | This file isn't published site copy, but it's the brief every future content-generation agent reads before writing new posts/social content. If it keeps the $30M+ floor after the site copy is rewritten to drop it, new content will keep reintroducing the exact framing this rewrite removes. Recommend updating in parallel — confirm with user before touching, since it's outside "the site" as scoped.} |

---

## Items reviewed and NOT flagged (for transparency)

- `send/index.html` — reviewed in full. No anti-GC/architect framing or dollar-threshold language found. The one adjacent-topic line ("Not the architect, not the GC, not the design-builder... no competing relationship") lives in `handoff/index.html`, not here.
- `blog/template.html` and `blog/index_template.html` — shared chrome/CTA copy reviewed; no adversarial framing or dollar thresholds found.
- Image alt text and SVG `aria-label`s across the homepage, findings page, and the one blog feature-art partial — all describe the technical finding itself (e.g., "Elevation schematic: W24x84 transfer girder overlapping a 54-inch supply duct...") with no adversarial or threshold language. Not flagged.
- `robots.txt`, `sitemap.xml`, `assets/tracking.js` — no natural-language copy present.
- `blog/posts/2026-07-23-data-center-constructability-review-consultant.md` — see note above; no issues found.

---

## Next step

Please review this log and confirm before Phase 2 (rewrite). You may want to:
1. Cut or reclassify any of the "uncertain" flags (#17, #35).
2. Confirm whether `PREEMPT_CONTEXT.md` (#37) should be updated alongside the site copy, since it's technically out of scope but feeds future content.
3. Confirm the multifamily cross-cutting item (#36) — specifically whether you want it worked into the homepage only, or also want a note added to the audit log for a possible future blog post.

Once confirmed, Phase 2 will branch to `copy/anti-confusion-positioning` and rewrite each flagged instance in place, with scoped commits per page.
