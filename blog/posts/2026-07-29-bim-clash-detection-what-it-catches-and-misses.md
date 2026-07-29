---
title: "BIM Clash Detection: What It Catches (and Misses)"
slug: bim-clash-detection-what-it-catches-and-misses
date: 2026-07-29
description: "BIM clash detection catches geometry — two modeled elements overlapping. Here's exactly what it catches, what it misses, and where paper clash detection picks up."
deck: "Clash detection is real and it works — for what it's built to check. Here's the line between what a coordinated model catches and what only reading the issued set catches."
tags: [BIM, Coordination, MEP]
---

!lede BIM clash detection is the industry's default answer to "how do we know the trades won't collide before we build it" — and for what it's built to do, it's a good answer. Run clash detection construction coordination correctly, on a model built to the right level of development, and it will find the duct routed through the beam every time. What it won't find is everything sitting outside the model: the spec section that contradicts the drawing it's paired with, the general note that quietly prohibits what a detail three sheets over requires, or the conflict that never got modeled because that discipline hasn't caught up yet.

None of that is a knock on the technology. It's a scope question, and scope questions matter more than they get credit for, because a team that assumes clash detection means "the set has been fully checked" is carrying risk it doesn't know it's carrying.

## What BIM Clash Detection Actually Checks

Clash detection software — Navisworks, Revizto, and similar coordination tools are the common examples — runs rule-based tests between linked discipline models: architectural, structural, mechanical, electrical, plumbing, fire protection. It's looking for three specific things:

- **Hard clashes.** Two objects occupying the same physical space — a duct routed through a structural beam, a pipe running through a column. Purely geometric, and the easiest category for software to catch reliably.
- **Soft (clearance) clashes.** An object intruding on the required access or maintenance clearance around another — equipment placed too close to an electrical panel to meet code-required working clearance, for instance.
- **Workflow (4D) clashes.** Not a physical overlap at all, but a sequencing conflict — two trades scheduled into the same space at the same time.

All three are real problems worth catching, and a model that's been properly coordinated will surface them before anyone breaks ground. That's exactly why any team running full BIM coordination should keep running it.

## What It Doesn't Check

The limitation isn't a flaw in the software — it's a limitation of what geometry can represent. A few categories of conflict live entirely outside what a 3D model checks, no matter how mature the BIM process is:

- **Spec-vs-drawing contradictions.** A written spec section that calls for one assembly while the drawing it's paired with shows another. Nothing about that disagreement is geometric — it's two documents disagreeing with each other in words, not in space.
- **General notes that contradict a detail.** A note on one sheet prohibiting exactly what a detail on another sheet requires. Both can be individually "correct" and still be un-buildable together, and neither is a modeled object clashing with another modeled object.
- **Non-overlapping conflicts that still stop work.** A door schedule that doesn't match the hardware set spec. A fire-rated assembly called out in one place and dropped in another. None of these show up as two elements sharing the same coordinates — they show up as a sub standing in the field holding two documents that disagree.
- **Anything that hasn't been modeled yet.** Clash detection is only as good as what's been drawn in 3D, to a coordination-ready level of development, by every discipline, and kept current. Early in design, on smaller trades, on renovation work, or anywhere one discipline is behind on modeling, there's simply no coordinated model yet to run the software against.

## The Real Prerequisite: A Coordination-Ready Model

That last point is worth sitting with, because it's the part that gets skipped in most conversations about clash detection ROI. The technology works — genuinely well — when the inputs are right. A widely cited case study on a $230 million design-build project found that a $200,000 investment in BIM coordination produced more than $2.5 million in verified savings, a return that makes the case for running clash detection on its own. But that return depended on every discipline actually modeling to the level of development clash detection needs, on a schedule that kept the model current enough to trust.

<div class="callout">
  <div class="cl-label">Worth knowing</div>
  <p>The US construction industry loses an estimated $177 billion a year to rework and field inefficiency, per FMI's widely cited industry study. Clash detection closes part of that gap. It was never built to close all of it — the written spec and general notes sit outside a model no matter how well that model is coordinated.</p>
</div>

## Clash Detection vs. Document Review: Two Different Layers

This is where the comparison usually gets flattened into "which one do we need," when the more useful question is "which layer does each one check." Clash detection vs document review isn't really a competition — it's two passes at the same set, scoped to different things. Clash detection reads geometry inside a coordinated model. A construction document review reads the issued set itself: the drawings and the specs, cross-checked against each other and across every trade, whether or not that content has been modeled yet.

That's also a difference in who it's for. BIM coordination is typically run by the design team's or GC's VDC group, scoped to keep the model buildable. A construction document review is paid by the owner and reports to no one else. Neither replaces the other — see the [full point-by-point comparison](/vs-bim-clash/) for how the two actually run side by side, and [what a construction document review is](/construction-document-review/) if the distinction between the underlying terms itself needs unpacking first.

## What "Paper Clash Detection" Actually Means

"Paper clash detection" isn't an industry term of art, but it's a useful way to describe what a document-level review is actually doing: catching the same category of conflict clash detection catches — two things that shouldn't coexist — without needing a 3D model as a prerequisite. It's reading the issued set the way a coordinated model gets read, except the "model" is the drawings and specs as issued, checked sheet against sheet and discipline against discipline.

The economics are identical to why clash detection pays for itself, just applied one layer up. A conflict caught on paper costs a redline and a few minutes. The same conflict caught in the field averages $18,400 and a 12-day schedule slip, based on industry delay data. Paper clash detection and model-based clash detection are chasing the same goal — catch it before the crew does — from two different starting points.

<div class="mini-report">
  <div class="rh"><span class="title">SAME GOAL, DIFFERENT LAYER</span><span class="meta">illustrative, not a specific project</span></div>
  <div class="mini-row"><span class="k">Caught on paper or in the model</span><span class="v">Redline — near-zero cost</span></div>
  <div class="mini-row"><span class="k">Caught in the field</span><span class="v hot">$18,400 avg. / 12-day slip</span></div>
  <div class="mini-row"><span class="k">Average RFI generated in the meantime</span><span class="v">~$1,080 / ~10 business days</span></div>
</div>

That RFI figure is worth pausing on, since it's the step that usually happens before a conflict becomes a change order. The Navigant Construction Forum's widely referenced study puts the average RFI at roughly $1,080 to process and about ten business days to resolve — real money and real schedule spent on a question that a document-level review, run before the set went out, would have answered in advance. As covered separately, [RFI count itself is the wrong thing to track](/blog/rfi-reduction-coordination-conflicts/) — but every RFI that does get filed still carries that cost, whether or not the underlying conflict ever gets fully resolved.

## Where This Leaves You

If your project is running full BIM coordination, the answer isn't to replace it — it's to keep running it and recognize what it doesn't cover. If the model isn't coordination-ready yet, or won't be for a discipline that's behind, that's not a reason to wait; the issued set can be reviewed for cross-discipline conflicts today, independent of modeling status. Either way, the conflicts that get missed at this stage don't disappear. They resurface later, usually as an RFI first and a change order after that.

<div class="takeaways">
  <h3>Key takeaways</h3>
  <ul>
    <li>BIM clash detection catches hard clashes, soft/clearance clashes, and workflow (4D) clashes — all genuinely geometric, all worth catching.</li>
    <li>It doesn't catch spec-vs-drawing contradictions, conflicting general notes, or anything in a discipline that hasn't reached coordination-ready modeling yet.</li>
    <li>Clash detection ROI is real, but it depends on every discipline modeling to the right level of development and keeping it current — a prerequisite that isn't always met.</li>
    <li>"Paper clash detection" — reading the issued set itself — catches the same category of conflict without needing a model as a prerequisite.</li>
    <li>Whatever gets missed doesn't vanish — it shows up later as an RFI, and if it's still unresolved, as a change order. See <a href="/blog/construction-change-order-costs/">the real cost of construction change orders</a> for what that escalation actually looks like in dollars.</li>
  </ul>
</div>

## Frequently Asked Questions

### Does BIM clash detection replace a construction document review?

No. Clash detection checks geometry inside a coordinated model. A construction document review checks the issued set itself — drawings and specs, cross-referenced against each other — whether or not that content has reached coordination-ready modeling yet. Projects running both get two independent passes at different layers of the same set.

### What's the difference between a hard clash and a soft clash?

A hard clash is two modeled objects physically occupying the same space, like a duct through a beam. A soft (clearance) clash is an object intruding on the required access or maintenance space around another object, without actually overlapping it. Both are geometric; neither is a written-document conflict.

### Can clash detection catch a spec that contradicts the drawings?

No. That's a conflict between two written documents, not between two modeled objects, so it falls entirely outside what geometry-based clash detection is scoped to check. It's the kind of conflict a document-level review is specifically built to catch.

### Do we need a finished BIM model to catch coordination conflicts?

Not for every category of conflict. Clash detection needs a coordination-ready model. A construction document review works directly from the issued drawings and specs, so it can run even when modeling isn't complete or a discipline is behind.

### Is "paper clash detection" a real industry term?

Not formally — it's a useful shorthand for what a document-level review does: catching conflicting elements the same way clash detection does, but by reading the issued set itself rather than a 3D model.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Does BIM clash detection replace a construction document review?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No. Clash detection checks geometry inside a coordinated model. A construction document review checks the issued set itself — drawings and specs, cross-referenced against each other — whether or not that content has reached coordination-ready modeling yet. Projects running both get two independent passes at different layers of the same set."
      }
    },
    {
      "@type": "Question",
      "name": "What's the difference between a hard clash and a soft clash?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "A hard clash is two modeled objects physically occupying the same space, like a duct through a beam. A soft (clearance) clash is an object intruding on the required access or maintenance space around another object, without actually overlapping it. Both are geometric; neither is a written-document conflict."
      }
    },
    {
      "@type": "Question",
      "name": "Can clash detection catch a spec that contradicts the drawings?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No. That's a conflict between two written documents, not between two modeled objects, so it falls entirely outside what geometry-based clash detection is scoped to check. It's the kind of conflict a document-level review is specifically built to catch."
      }
    },
    {
      "@type": "Question",
      "name": "Do we need a finished BIM model to catch coordination conflicts?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Not for every category of conflict. Clash detection needs a coordination-ready model. A construction document review works directly from the issued drawings and specs, so it can run even when modeling isn't complete or a discipline is behind."
      }
    },
    {
      "@type": "Question",
      "name": "Is \"paper clash detection\" a real industry term?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Not formally — it's a useful shorthand for what a document-level review does: catching conflicting elements the same way clash detection does, but by reading the issued set itself rather than a 3D model."
      }
    }
  ]
}
</script>
