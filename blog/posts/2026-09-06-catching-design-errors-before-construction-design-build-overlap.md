---
title: "Catching Design Errors Before Construction on a Design-Build Schedule: What Changes When Design and Construction Overlap"
slug: catching-design-errors-before-construction-design-build-overlap
date: 2026-09-06
description: "Catching design errors before construction gets harder once earlier packages are already built. Here's what actually changes when design and construction overlap."
deck: "On a design-bid-build job, 'before construction' is one clear window. On a design-build schedule, part of the building is already built while the rest is still being drawn — and that changes what catching a design error actually requires."
tags: [Design-Build, Coordination, Quality Control]
---

!lede Catching design errors before construction assumes there's a "before" — a point where the whole set exists on paper and nothing has been built yet. A design-build schedule, where early packages break ground while later ones are still in design, doesn't give you that point. Part of the project is already poured, framed, or roughed-in while the rest is still a drawing. Catching a design error in that environment means catching it against something more complicated than another sheet in the same set: a physical condition that already exists and can't be quietly revised.

## Why "before construction" isn't one moment here

On a traditional schedule, catching design errors before construction is a checklist problem — read the full set, every discipline against every other, before it goes out to bid. [That checklist](/blog/catching-design-errors-before-construction-checklist/) works because the set is finished and nothing has been built yet. Every conflict it finds is still a redline.

Design-build breaks that premise on purpose. The entire value of the delivery method, for an owner chasing schedule, is that site work and structure can be under construction while mechanical, electrical, and finish packages are still being designed. That's not a side effect to manage around — it's the reason the delivery method gets chosen. But it means the "before" in "before construction" no longer applies to the project as a whole. It applies, package by package, to whichever piece hasn't been built yet — and for the pieces that have, the standard for catching an error changes from "does this contradict another sheet" to "does this contradict something that's already in the ground."

## The moving target: designing against a structure that can't be revised

A design error caught on paper, before anything is built, gets fixed on paper. A design error caught after the package it belongs to is already under construction doesn't have that option — the fix has to work around whatever is physically there, not around what the drawings originally said should be there. On a design-build schedule, that second category isn't rare. It's the normal condition for every package that designs after an earlier one has already broken ground.

That creates a specific failure mode a design-bid-build schedule doesn't have: the later package's designer is working from the record of what the earlier package was supposed to be, not necessarily what it actually became in the field. Field conditions routinely diverge from the issued drawings during construction — buried MEP routing gets adjusted around an unforeseen obstruction, a structural connection gets field-modified, a duct run shifts a few inches to clear something the original drawing didn't account for — and the paper record of those changes doesn't always keep pace with the changes themselves. A mechanical package designed three months later against the original structural drawings, instead of against what was actually built, is designing against information that may already be wrong.

<div class="callout">
  <div class="cl-label">Worth knowing</div>
  <p>On a rolling-release schedule, the biggest source of a "surprise" design error usually isn't a mistake made by either designer — it's a later package trusting an earlier package's issued drawings instead of verifying what that earlier package actually became once it was built. The paper and the field diverge quietly, and neither discipline's own QA/QC is positioned to catch the gap between them.</p>
</div>

This is a different problem from cross-discipline coordination in the ordinary sense — it's not two disciplines contradicting each other on the same set of drawings at the same moment. It's a discipline designing in the present against a record of the past that may no longer be accurate, because the thing it's designing against has already been physically altered since the drawings that describe it were issued.

## Where the risk actually concentrates

Academic research on fast-track activity overlapping — projects where design and construction run concurrently rather than sequentially — has looked directly at which risks concentrate where. A 2023 study on construction professionals' perceptions of fast-track overlapping risk (published in *Eng*, MDPI) found four risk types accounting for most of what practitioners flagged: construction error, design change, crew interference, and poor construction productivity. Design change specifically — a later design decision reacting to, or contradicting, something already committed earlier — showed up as one of the dominant categories, and the study found risk was perceived most acutely in moderate degrees of overlap and in activities occurring earlier in the schedule, not in the packages released last.

That maps onto the design-build sequence directly. The packages released earliest — site work, foundations, structural steel — are the ones every later package has to design around, and they're also the packages most likely to have field-modified since their drawings were issued. An error introduced against an early package doesn't stay contained to that package; it propagates into every later package designed against it, which is exactly the mechanism the research describes as concentrating risk at the earlier end of the schedule rather than the later one.

<div class="mini-report">
  <div class="rh"><span class="title">FOUR RISK TYPES IN OVERLAPPING SCHEDULES</span><span class="meta">From MDPI research on fast-track activity overlapping perception</span></div>
  <div class="mini-row"><span class="k">Construction error</span><span class="v">Field execution deviating from what was issued</span></div>
  <div class="mini-row"><span class="k">Design change</span><span class="v hot">Later packages reacting to or contradicting earlier ones</span></div>
  <div class="mini-row"><span class="k">Crew interference</span><span class="v">Overlapping trades working the same footprint</span></div>
  <div class="mini-row"><span class="k">Poor construction productivity</span><span class="v">Sequencing inefficiency from concurrent work</span></div>
</div>

Separately, research on rework in construction has consistently attributed the largest share of avoidable cost to design-related errors and omissions rather than construction-phase mistakes — reinforcing why catching a design problem specifically, and catching it early, carries more leverage than catching a field execution problem after the fact. On an overlapping schedule, "early" for a given package means before that package's design is finalized against whatever's already built around it — not before the project as a whole is finished, which never happens as a single event.

## What actually has to change to catch these errors

Three things change, practically, compared to catching design errors on a schedule with a real "before":

**The check has to run against field-verified conditions, not just issued drawings, for anything already under construction.** If a later package's design assumes a structural or MEP condition from an earlier package, that assumption needs to be checked against what's actually been built — not just what the earlier package's drawings said — because the two can have already diverged by the time the later package is designed. That's a field-verification step a design-bid-build review doesn't usually need, since nothing has been built yet when the review happens.

**The review has to repeat at each package's release, not once for the project.** [That package-by-package cadence](/blog/how-to-reduce-change-orders-fast-tracked-design-build-schedule/) is the same shift a fast-tracked schedule requires generally — there's no single moment to hold for, so the check has to happen every time a new package reaches the point where it's about to be locked in.

**Every finding needs to be traced to which package it originated in and which packages it touches downstream.** On a single-set project, a conflict is just a conflict — there's one document to correct. On an overlapping schedule, the same conflict might mean redlining a package still in design, or it might mean the later package has to be redesigned around a condition the earlier package can no longer change. Knowing which situation applies determines whether the fix is a paper correction or a field problem, which is the same distinction that governs [where a pre-bid-style review actually lands on a design-build job with no separate bid set](/blog/pre-bid-drawing-review-design-build-no-separate-bid-set/).

<div class="takeaways">
  <h3>Key takeaways</h3>
  <ul>
    <li>A design-build schedule removes the single "before construction" moment a traditional error-catching checklist assumes — part of the project is usually already built while the rest is still being designed.</li>
    <li>The distinct risk this creates is a later package designing against an earlier package's issued drawings instead of what that earlier package actually became once built, since field conditions and paper records can diverge during construction.</li>
    <li>Research on fast-track activity overlapping identifies design change as one of the top risk categories, concentrated most in earlier-released packages — the ones every later package has to design around.</li>
    <li>Catching design errors on this kind of schedule requires field-verified conditions for anything already under construction, a review cadence that repeats at every package release, and traceability back to which package a conflict originated in.</li>
    <li>The underlying economics don't change: a design error is still cheaper to fix the earlier it's caught relative to when its package is built — overlap just means "earlier" has to be evaluated per package, not once for the whole project.</li>
  </ul>
</div>

None of this makes catching design errors before construction impossible on a design-build schedule — it makes it a different, more frequent exercise than the single pre-bid check a traditional schedule allows for. The packages that already broke ground don't get a second chance to be caught on paper; the ones still in design still do, provided the check against what's already built actually happens before they're locked in too.

## Frequently Asked Questions

### Can you actually catch design errors before construction on a design-build schedule if construction has already started?

Yes, but the scope of "before construction" narrows to whatever hasn't broken ground yet. For packages already under construction, the goal shifts from catching an error before it's built to catching it before the *next* package locks in a design decision that depends on it — which is still a meaningfully cheaper fix than catching the conflict after both packages are built.

### Why does record drawing accuracy matter more on an overlapping schedule than a traditional one?

Because a later package on an overlapping schedule is often designed against an earlier package's drawings while that earlier package is simultaneously being built and field-modified. On a traditional schedule, nothing is under construction yet, so the drawings and the physical condition can't have diverged. On an overlapping schedule, they can — and often have, by the time a later package needs to design around them.

### Is design change really one of the bigger risks on a fast-tracked or design-build schedule?

Research on fast-track activity overlapping identifies design change as one of four dominant risk categories construction professionals report, alongside construction error, crew interference, and poor productivity, with risk concentrated more in earlier-scheduled activities than later ones. That lines up with how overlap actually works: the earliest packages are the ones every later package has to design around.

### Does this mean design-build projects have more design errors than design-bid-build projects?

Not inherently — it means the errors that do occur are harder to catch with the checklist a design-bid-build project uses, because there's no single finished set to check before anything is built. The overlap itself is a structural feature of the delivery method, not a sign the design is worse; catching errors against it just requires a review model built for rolling packages instead of one complete set.

### Who is responsible for checking a later package against what's already been built?

Nominally, whichever team is designing the later package should be verifying the conditions it's building on. In practice, that verification competes with the same schedule pressure driving the overlap in the first place, which is why an independent document review — one specifically checking each new package against both the drawings and the built condition of what came before it — tends to catch what an already-stretched design team misses.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Can you actually catch design errors before construction on a design-build schedule if construction has already started?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes, but the scope of \"before construction\" narrows to whatever hasn't broken ground yet. For packages already under construction, the goal shifts from catching an error before it's built to catching it before the next package locks in a design decision that depends on it, which is still a meaningfully cheaper fix than catching the conflict after both packages are built."
      }
    },
    {
      "@type": "Question",
      "name": "Why does record drawing accuracy matter more on an overlapping schedule than a traditional one?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Because a later package on an overlapping schedule is often designed against an earlier package's drawings while that earlier package is simultaneously being built and field-modified. On a traditional schedule, nothing is under construction yet, so the drawings and the physical condition can't have diverged. On an overlapping schedule, they can, and often have, by the time a later package needs to design around them."
      }
    },
    {
      "@type": "Question",
      "name": "Is design change really one of the bigger risks on a fast-tracked or design-build schedule?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Research on fast-track activity overlapping identifies design change as one of four dominant risk categories construction professionals report, alongside construction error, crew interference, and poor productivity, with risk concentrated more in earlier-scheduled activities than later ones. That lines up with how overlap actually works: the earliest packages are the ones every later package has to design around."
      }
    },
    {
      "@type": "Question",
      "name": "Does this mean design-build projects have more design errors than design-bid-build projects?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Not inherently, it means the errors that do occur are harder to catch with the checklist a design-bid-build project uses, because there's no single finished set to check before anything is built. The overlap itself is a structural feature of the delivery method, not a sign the design is worse; catching errors against it just requires a review model built for rolling packages instead of one complete set."
      }
    },
    {
      "@type": "Question",
      "name": "Who is responsible for checking a later package against what's already been built?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nominally, whichever team is designing the later package should be verifying the conditions it's building on. In practice, that verification competes with the same schedule pressure driving the overlap in the first place, which is why an independent document review, one specifically checking each new package against both the drawings and the built condition of what came before it, tends to catch what an already-stretched design team misses."
      }
    }
  ]
}
</script>
