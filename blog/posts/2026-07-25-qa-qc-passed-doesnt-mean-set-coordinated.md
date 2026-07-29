---
title: "Passing QA/QC Doesn't Mean Coordinated"
slug: qa-qc-passed-doesnt-mean-set-coordinated
date: 2026-07-25
description: "Catching design errors before construction takes more than a passed QA/QC review. Here's exactly what QA/QC checks on a drawing set — and what it isn't scoped to catch."
deck: "A drawing set can clear every internal QA/QC check the architect runs and still ship with cross-discipline conflicts nobody caught. Here's the actual difference between \"passed QC\" and \"coordinated.\""
tags: [Coordination, Bid Documents, Quality Control]
---

!lede "It already passed QA/QC" is one of the most common reasons an owner waves off an independent review before bid. It sounds like the box has been checked. It hasn't — not the box that matters for catching design errors before construction, anyway. QA/QC and coordination are two different checks, run against two different standards, and a set can pass one completely while failing the other in ways that don't surface until a crew is standing in front of a wall that can't be built as drawn.

The confusion is understandable. Both processes involve reviewing drawings before they go out. Both catch real problems. But they're not redundant with each other, and knowing exactly where one stops and the other should start is the difference between a set that looks clean and a set that actually is.

## What QA/QC actually checks

A firm's internal QA/QC process is a real, structured review — not a formality. On a typical architecture or engineering firm's drawing set, it verifies:

- **Internal consistency against firm standards** — that the set follows the office's own drafting conventions, sheet numbering, and detail library.
- **Cross-references within the discipline** — that every detail callout on a plan points to a detail that actually exists on that sheet set, that keynote numbers match the legend, and that room names and numbers agree across that discipline's own plans.
- **Completeness against the contract scope** — that the deliverable includes everything the client agreement calls for at that phase.
- **Code compliance for that discipline's scope** — that what's drawn meets the applicable code sections the reviewing discipline is responsible for.

That's a genuinely useful check, and it catches real errors — a missing detail reference, an outdated keynote, a wall type that doesn't match its own schedule. What it checks is whether the architectural set is internally consistent with itself, and whether the structural set is internally consistent with itself, and so on, discipline by discipline.

<div class="callout">
  <div class="cl-label">Worth knowing</div>
  <p>QA/QC is run by the same firm that produced the drawings, checking its own work against its own standards. That's not a conflict of interest — it's simply a different scope than a cross-discipline conflict check, and no firm's internal QC process is set up to catch a contradiction between its own sheet and a different discipline's sheet, because that contradiction, by definition, lives outside any single firm's set.</p>
</div>

## What "coordinated" actually means

"Coordinated" describes something QA/QC was never built to check: agreement *between* disciplines, not within one. A mechanical sheet can pass every internal QA/QC check the mechanical engineer runs — correct keynotes, correct schedules, complete details — and still route a duct directly through a beam the structural set requires at that exact elevation. Neither sheet is wrong on its own terms. Neither firm's QC process failed. The conflict exists only when you hold the two sheets up against each other, which is exactly the step no single discipline's internal review is scoped to perform.

The same logic covers a written note on one sheet that contradicts a drawn detail on another, or a spec section that requires clearance a structural detail doesn't allow for. Each individual document can be internally clean. The contradiction only exists in the gap between documents — a gap that's nobody's job to check unless someone is explicitly reading the full set against itself, across every discipline, on purpose.

## Why a set can pass QA/QC and still carry serious exposure

This is the pattern that shows up on nearly every large, multi-discipline bid set: individually clean documents that were never checked against each other. As covered in [what architect QC covers and where an owner-side review picks up](/blog/architect-qc-vs-owner-review/), the architect's QC and the GC's coordination pass are both real and both scoped to a different job than protecting the owner from cross-discipline exposure specifically.

<div class="mini-report">
  <div class="rh"><span class="title">HOW ONE CONFLICT CLEARS THREE QA/QC CHECKS</span><span class="meta">Illustrative — structural vs. mechanical vs. spec, not a specific project</span></div>
  <div class="mini-row"><span class="k">Structural sheet QC</span><span class="v">Passed — internally consistent</span></div>
  <div class="mini-row"><span class="k">Mechanical sheet QC</span><span class="v">Passed — internally consistent</span></div>
  <div class="mini-row"><span class="k">Spec section QC</span><span class="v">Passed — internally consistent</span></div>
  <div class="mini-row"><span class="k">Cross-discipline conflict caught by any of the three</span><span class="v hot">No</span></div>
</div>

That's not a hypothetical. Construction Industry Institute research has attributed a majority of construction rework to design coordination errors and omissions specifically — not drafting mistakes within a single discipline's own set, but the gap between disciplines that internal QA/QC isn't positioned to close. BIM clash detection narrows part of that gap by catching modeled geometry that physically overlaps, but it doesn't catch a written note contradicting a routing decision, or a spec clearance the drawn detail doesn't allow for — conflicts that live in the documents themselves rather than in modeled geometry.

## Catching design errors before construction, not after

The reason this distinction matters isn't academic. It's timing. A cross-discipline conflict that clears every discipline's internal QA/QC and every model-based clash check doesn't disappear — it just moves downstream, to whichever phase someone finally reads the full set against itself. As we've written about in [how a single missed MEP clash turns into a $400,000 change order](/blog/missed-mep-clash-change-order-cost/), the fix for the identical conflict costs close to nothing before bid and a six-figure change order once it's discovered in the field. Passing QA/QC doesn't move that clock. Only a cross-discipline read, done before bid, does.

Industry estimates on front-end coordination consistently point the same direction: money spent finding conflicts before construction returns multiples of that spend in avoided field costs, because a redline is inexpensive and a stop-work RFI on an active job never is. That return only exists if the check actually happens before the set is issued — a passed QA/QC review doesn't substitute for it, because it was never checking for the same thing.

## What closes the gap

None of this means QA/QC is broken or unnecessary — it's doing exactly what it's designed to do, and skipping it would be a mistake. What it means is that "the set passed QA/QC" answers a narrower question than most owners assume it does. Closing the actual gap requires a review scoped specifically to cross-discipline agreement:

- **Reading every discipline's sheets against every other discipline's sheets** — not just against that discipline's own standards.
- **Checking written notes and spec sections against drawn details**, not just details against their own detail library.
- **Running the check before bid**, while the cheapest fix — a redline — is still on the table.

That's the same distinction covered in more depth in [what is owner-side QA/QC?](/construction-qa-qc-review/) — why "passed QA/QC" and "checked for the owner" answer two different questions.
- **Naming a dollar figure for what's found**, as covered in [anatomy of a findings report](/blog/anatomy-of-a-findings-report-third-party-plan-review/), so exposure competes for attention the way a general "coordination note" doesn't.

<div class="takeaways">
  <h3>Key takeaways</h3>
  <ul>
    <li>QA/QC checks a discipline's drawings against that firm's own standards, cross-references, and code scope — it's a real check, run correctly.</li>
    <li>"Coordinated" means something different: agreement between disciplines, which no single discipline's internal QC process is scoped to verify.</li>
    <li>A set can pass every discipline's QA/QC individually and still carry six-figure cross-discipline exposure that surfaces only in the field.</li>
    <li>BIM clash detection catches modeled geometry conflicts, not contradictions between written notes, specs, and details.</li>
    <li>Catching design errors before construction requires a review scoped specifically to cross-discipline agreement, run before bid — not a repeat of QA/QC.</li>
  </ul>
</div>

"Passed QA/QC" is a true statement about a real process. It's just an answer to a narrower question than "is this set coordinated" — and the gap between those two questions is exactly where the expensive conflicts live.

## Frequently Asked Questions

### Is QA/QC the same thing as a coordination review?

No. QA/QC checks a discipline's own drawings against that firm's internal standards, cross-references, and code scope. A coordination review checks whether different disciplines' documents agree with each other. A set can pass QA/QC completely and still contain cross-discipline conflicts, because the two checks are scoped to different questions.

### Does BIM clash detection catch what QA/QC misses?

Partially. Clash detection catches modeled geometry that physically overlaps, which is a real and useful check. It doesn't catch a written note that contradicts a drawn detail on another sheet, or a spec section that requires clearance a detail doesn't allow for — conflicts that exist in the documents themselves rather than in the 3D model.

### Whose responsibility is it to catch cross-discipline conflicts if QA/QC doesn't?

On most projects, no single contracted party is scoped specifically to catch cross-discipline conflicts on the owner's behalf. The architect's QC protects design intent within their own scope, and the GC's coordination review is scoped to pricing the work accurately. An independent, owner-side review is the check specifically aligned to catching these conflicts before bid.

### Why doesn't a passed QA/QC review show up as a red flag when conflicts exist?

Because QA/QC isn't failing at its job — it's succeeding at a narrower one. Each discipline's drawings can be fully internally consistent while still contradicting another discipline's sheet, since that comparison sits outside what any single firm's QC process checks.

### When is the cheapest point to catch these conflicts?

Before the set goes to bid. A cross-discipline conflict caught pre-bid is typically a redline the design team can turn around at little or no cost. The identical conflict caught after bid or in the field usually comes with a change order, schedule impact, and a fix that costs a fraction of what it would have cost to catch earlier.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Is QA/QC the same thing as a coordination review?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No. QA/QC checks a discipline's own drawings against that firm's internal standards, cross-references, and code scope. A coordination review checks whether different disciplines' documents agree with each other. A set can pass QA/QC completely and still contain cross-discipline conflicts, because the two checks are scoped to different questions."
      }
    },
    {
      "@type": "Question",
      "name": "Does BIM clash detection catch what QA/QC misses?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Partially. Clash detection catches modeled geometry that physically overlaps, which is a real and useful check. It doesn't catch a written note that contradicts a drawn detail on another sheet, or a spec section that requires clearance a detail doesn't allow for, conflicts that exist in the documents themselves rather than in the 3D model."
      }
    },
    {
      "@type": "Question",
      "name": "Whose responsibility is it to catch cross-discipline conflicts if QA/QC doesn't?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "On most projects, no single contracted party is scoped specifically to catch cross-discipline conflicts on the owner's behalf. The architect's QC protects design intent within their own scope, and the GC's coordination review is scoped to pricing the work accurately. An independent, owner-side review is the check specifically aligned to catching these conflicts before bid."
      }
    },
    {
      "@type": "Question",
      "name": "Why doesn't a passed QA/QC review show up as a red flag when conflicts exist?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Because QA/QC isn't failing at its job, it's succeeding at a narrower one. Each discipline's drawings can be fully internally consistent while still contradicting another discipline's sheet, since that comparison sits outside what any single firm's QC process checks."
      }
    },
    {
      "@type": "Question",
      "name": "When is the cheapest point to catch these conflicts?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Before the set goes to bid. A cross-discipline conflict caught pre-bid is typically a redline the design team can turn around at little or no cost. The identical conflict caught after bid or in the field usually comes with a change order, schedule impact, and a fix that costs a fraction of what it would have cost to catch earlier."
      }
    }
  ]
}
</script>
