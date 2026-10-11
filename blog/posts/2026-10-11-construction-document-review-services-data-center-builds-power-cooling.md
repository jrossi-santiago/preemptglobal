---
title: "Construction Document Review Services for Data Center Builds: What Changes When Power and Cooling Drive the Set"
slug: construction-document-review-services-data-center-builds-power-cooling
date: 2026-10-11
description: "Construction document review services for data centers have to start with power and cooling, not the building. Here's what a review checks first when MEP drives the set."
deck: "On most buildings the architecture sets the frame and the systems fit inside it. On a data center it runs the other way: electrical and mechanical systems set the frame, and the building has to hold them. A document review scoped for a standard commercial set starts in the wrong place."
tags: [Data Centers, Document Review, Coordination]
---

!lede Construction document review services for a standard commercial building start with the architecture: does the structural grid match the plan, do the risers land in the shafts, does the spec match the drawing. On a data center, that order flips. Power and cooling decide the footprint, the floor loads, the ceiling heights, and the yard layout, and the architecture is drawn to hold what the electrical and mechanical engineers need. A review that starts with the architectural sheets and works outward is starting at the wrong end of the set.

## Why the Review Starts With Power and Cooling

In a typical office or warehouse set, a coordination conflict is usually one trade's work running into another's. In a data center the same conflicts exist, but they sit on top of something else: a capacity requirement. The set has to deliver a stated amount of power and a stated amount of heat rejection, to every hall, with a stated amount of redundancy. If one sheet quietly shrinks a pad, a duct bank, or a chilled water pipe, the building may still be coordinated on paper and still miss its capacity target.

That changes what a document review has to trace. Beyond "do these two sheets agree," the question becomes "does the path from utility to rack, and from rack back out to heat rejection, show up complete and consistent across every discipline that touches it?" We covered why this asset class generates more conflicts than most in [why data centers need a constructability review](/blog/data-center-constructability-review-consultant/). This post is about what that means for the scope of a review.

## Follow the Power Path Sheet by Sheet

The electrical path runs from the utility service through switchgear, generators, and UPS to the distribution in each hall. A review follows that path across the electrical one-lines, the site plan, the architectural plans, and the structural sheets, and checks that every piece shows up in each place it should.

- **Equipment rooms and yards.** Switchgear, generator, and UPS rooms or pads should have clearances, door sizes, and structural supports that match the equipment shown on the electrical sheets. A one-line that calls for a larger lineup than the room was drawn for is a finding.
- **Redundancy paths.** If the design calls for redundant feeds (N+1 or 2N), a review checks that the two paths are physically separate where the design says they are. Duct banks, cable trays, and shafts that look independent on the one-line can end up sharing a route on the plans.
- **Generator and fuel systems.** Exhaust routing, fuel storage, fill locations, and the structural support for tanks and pads cross three or four disciplines. Each discipline's sheet tends to be right on its own terms. The conflict shows up in the overlay.
- **Owner-furnished or long-lead equipment.** Where the owner buys major equipment directly, the set often carries an assumed size and weight from an earlier submittal. A review checks that the room, the pad, and the access path were drawn to the equipment actually selected, not a placeholder.

## Cooling Is Now a Structural Question Too

Cooling used to be a mechanical coordination problem: ducts, pipes, and units that had to fit in the space. With higher rack densities and liquid cooling, it has become a structural and architectural problem as well.

Sources put the practical ceiling for air cooling at roughly 20 to 30 kW per rack, and the move to liquid cooling is generally discussed as a decision to make beyond about 20 kW ([Chatsworth](https://chatsworth.com/en-us/documents/white-papers/power_densities_dc_cabinets_wp)). AFCOM's 2026 report, as [summarized by Schneider Electric](https://www.engineeringnews.co.za/print-version/designing-the-modern-ai-cooling-stack-2026-08-21), found average rack density climbing from 16 kW to 27 kW in a single year, and AI-focused designs run well above that. Which of those densities a given project designs for is the owner's call. What matters for the review is that the set has to be consistent with whichever one was chosen.

Liquid cooling raises floor loading. JLL's analyst notes that keeping the same compute in the same footprint pushes the load from roughly 12–15 kPa to at least 20 kPa ([JLL](https://www.jll.com/en-ch/insights/liquid-cooling-enters-the-mainstream-in-data-centers)). If the structural sheets were set for an air-cooled hall and the mechanical sheets show coolant distribution units, manifolds, and liquid-cooled racks, those two sets of drawings disagree about what the floor carries, and neither one is wrong by itself.

<div class="callout">
  <div class="cl-label">Worth knowing</div>
  <p>A NASA Ames case study described a 108 kW liquid-cooled system that had to be placed on the concrete subfloor because the data center's raised floor was not rated for its weight. The load was known. The floor rating and the equipment selection had not been checked against each other.</p>
</div>

The cooling checks that belong in a data center review scope:

1. **Floor and slab loads against equipment weights.** Confirm the structural design loads cover the heaviest rack, CDU, and chiller configuration shown on the mechanical and electrical sheets, including filled-weight for liquid systems.
2. **Piping routes against structure.** Chilled water and coolant mains are large and heavy. Check that routes clear beams, trusses, and slab openings, and that penetrations are shown on the structural sheets, not just the mechanical ones.
3. **Ceiling and plenum heights.** The space above and below the white space is shared by ductwork, cable trays, piping, fire protection, and lighting. A review overlays all of them against the clear height the architectural sections show.
4. **Heat rejection on the roof or in the yard.** Dry coolers, chillers, and cooling towers need structural support, service clearance, and piping access. Check these against both the site plan and the roof framing.
5. **Leak and drainage provisions.** With liquid in the hall, floor drains, leak detection, and containment have to appear on the architectural, plumbing, and controls sheets consistently.

## Where Disciplines Hand Off Without Agreeing

Most findings on a data center set sit at handoffs. A few that come up repeatedly:

- **Fire protection and cooling.** Clean-agent or pre-action systems, smoke detection, and air handling shutdown sequences touch the fire protection, mechanical, electrical, and controls sheets. Each discipline can show its own piece correctly while the sequence of operations doesn't match across them.
- **Controls and the power path.** Monitoring points, transfer sequences, and generator start logic live in the controls and electrical specs. A review checks that the spec section and the drawings describe the same sequence.
- **Specs against drawings.** On a MEP-heavy set the spec carries a lot of the performance requirement. [Spec vs. drawing conflicts](/blog/spec-vs-drawing-conflicts/) are worth more attention here, because the equipment lists in the spec, the schedules on the drawings, and the one-line often disagree on a rating or a quantity.
- **Phasing.** Many data centers are built in halls or phases, with later phases energized while earlier ones are live. The set has to show what is built now, what is stubbed for later, and how the live and construction areas stay separate.

If the project is a conversion rather than a new building, the same scope applies with another layer on top. We wrote about that in [MEP/structural conflicts on data center retrofits](/blog/mep-structural-conflicts-data-center-retrofits/).

## What This Does to the Scope of a Review

A review scoped for a typical commercial building usually spends most of its time on architectural and structural coordination with MEP as one discipline among several. On a data center, MEP is most of the set. That affects how the review is organized: it follows systems end to end rather than disciplines one at a time, it weights electrical and mechanical sheets heavily, and it checks capacity claims instead of just checking that sheets agree. For the general picture of what a review covers, see [what's actually in scope for construction document review services](/blog/construction-document-review-services/). The data center version keeps all of that and adds the power and cooling paths as the primary thing to trace.

It also changes why the review matters commercially. Data center schedules tend to be tight, and equipment is often ordered before the set is final. A coordination error caught at document stage is a revision to a drawing. The same error found after equipment is on site can mean re-sizing a pad, re-routing a main, or re-ordering equipment. For how change order exposure compares across project types, see [average change order percentage on data centers, multifamily, and healthcare](/blog/average-change-order-percentage-data-centers-multifamily-healthcare/).

<div class="takeaways">
  <h3>Key takeaways</h3>
  <ul>
    <li>On a data center set, start the review at power and cooling and work outward to the building, not the other way around.</li>
    <li>Trace the electrical path from utility to rack across the one-lines, site plan, architectural, and structural sheets, and confirm redundant paths are physically separate where the design says they are.</li>
    <li>Liquid cooling raises floor loading, so check structural design loads against the heaviest equipment configuration shown on the mechanical sheets.</li>
    <li>Most findings sit at handoffs: fire protection, controls, and specs against drawings, plus phasing between live and under-construction halls.</li>
    <li>Check that rooms, pads, and access paths were drawn for the equipment actually selected, not a placeholder.</li>
  </ul>
</div>

## Frequently Asked Questions

### How is a data center document review different from a standard commercial review?

A standard review checks that the disciplines agree with each other. A data center review does that and also checks capacity: whether the power and cooling paths are complete and consistent from utility to rack and back out to heat rejection. Because MEP makes up most of the set, the review follows systems end to end rather than discipline by discipline.

### Does liquid cooling change what a document review checks?

Yes. Liquid cooling adds weight, piping, and leak provisions. A review checks that structural design loads cover the heaviest equipment configuration, that coolant piping routes clear the structure, and that drainage and leak detection show up on the architectural, plumbing, and controls sheets.

### When should a data center set be reviewed?

Before the set is released for bid or equipment procurement, since data center equipment is often ordered early and corrections get more expensive once equipment is purchased. A second pass on addenda and revisions catches conflicts introduced by changes after the first review.

### What are the most common coordination problems on a data center set?

Redundant power paths that share a route, equipment rooms and pads drawn smaller than the selected equipment, structural loads that don't match the cooling design, and sequences of operation that differ between the controls spec, the electrical sheets, and the mechanical sheets.

### Do I need a review if the design team already coordinates in BIM?

BIM clash detection is useful for geometry, but it doesn't check capacity, redundancy, or whether a spec and a schedule agree. A document review covers those, and it works on the issued drawings and specs as a bidder or builder will read them. We cover the difference in [BIM clash detection: what it catches and misses](/blog/bim-clash-detection-what-it-catches-and-misses/).

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "How is a data center document review different from a standard commercial review?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "A standard review checks that the disciplines agree with each other. A data center review does that and also checks capacity: whether the power and cooling paths are complete and consistent from utility to rack and back out to heat rejection. Because MEP makes up most of the set, the review follows systems end to end rather than discipline by discipline."
      }
    },
    {
      "@type": "Question",
      "name": "Does liquid cooling change what a document review checks?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. Liquid cooling adds weight, piping, and leak provisions. A review checks that structural design loads cover the heaviest equipment configuration, that coolant piping routes clear the structure, and that drainage and leak detection show up on the architectural, plumbing, and controls sheets."
      }
    },
    {
      "@type": "Question",
      "name": "When should a data center set be reviewed?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Before the set is released for bid or equipment procurement, since data center equipment is often ordered early and corrections get more expensive once equipment is purchased. A second pass on addenda and revisions catches conflicts introduced by changes after the first review."
      }
    },
    {
      "@type": "Question",
      "name": "What are the most common coordination problems on a data center set?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Redundant power paths that share a route, equipment rooms and pads drawn smaller than the selected equipment, structural loads that don't match the cooling design, and sequences of operation that differ between the controls spec, the electrical sheets, and the mechanical sheets."
      }
    },
    {
      "@type": "Question",
      "name": "Do I need a review if the design team already coordinates in BIM?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "BIM clash detection is useful for geometry, but it doesn't check capacity, redundancy, or whether a spec and a schedule agree. A document review covers those, and it works on the issued drawings and specs as a bidder or builder will read them."
      }
    }
  ]
}
</script>
