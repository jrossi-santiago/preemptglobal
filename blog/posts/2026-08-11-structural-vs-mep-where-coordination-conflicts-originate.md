---
title: "Structural vs. MEP: Where Coordination Conflicts Actually Originate on a Set"
slug: structural-vs-mep-where-coordination-conflicts-originate
date: 2026-08-11
description: "MEP/structural drawing coordination conflicts don't happen randomly across a set. They cluster at a handful of predictable interface points. Here's where to look first."
deck: "Duct-through-beam is the famous one, but it's not the only place structural and MEP fight for the same three inches. A field guide to the interface points that generate the most conflicts, sheet by sheet."
tags: [Coordination, MEP, Structural]
---

!lede MEP/structural drawing coordination conflicts don't scatter randomly across a set. They cluster at a small number of interface points — the same handful of locations where a structural engineer and a mechanical, electrical, or plumbing engineer have both drawn something into the same physical space without seeing each other's sheet. Know the interface points and a review gets faster and more targeted. Ignore them and every set eventually produces the same expensive surprises in the field.

The reason these conflicts keep originating in the same places is structural: literally. Structural drawings are produced to carry load, MEP drawings are produced to move air, water, power, and waste, and both disciplines are optimizing for their own geometry first. Nobody on either team is drawing carelessly — they're solving a different problem than the one on the sheet next to them, and the two problems happen to want the same six inches of ceiling, the same column line, or the same slab penetration.

## Ductwork and Piping Through Structural Framing

This is the interface point every superintendent already knows about, because it's the one that shows up in the field the most. A mechanical engineer routes a main supply or return duct on the shortest, most efficient path between the air handler and the space it's serving. A structural engineer places beams, girders, and joists on the grid that carries the building's load most efficiently. Those two logics don't know about each other unless someone forces them to.

The result is a duct — or a pipe, or a cable tray — drawn to run exactly where a wide-flange beam or a solid-web joist already occupies the space. On open-web steel joists, there's often room to route smaller lines through the web openings, which is why so many soft clashes on this interface are avoidable if the duct size and routing account for the joist's actual opening pattern rather than treating it as clear space. On solid beams, girders, and any joist run without adequate web openings, there's no way through — only around, which usually means a lower duct, a re-route, or a change in the ceiling plan that nobody priced.

<div class="callout">
  <div class="cl-label">Worth knowing</div>
  <p>Hard clashes — where two elements are drawn occupying the same physical space — are the most expensive to catch late, because the fix isn't a design change on paper, it's demo and re-fabrication in the field. Soft clashes, where the geometry technically fits but leaves no clearance for insulation, access, or maintenance, are cheaper individually but far more numerous, and they're the ones a quick visual scan is most likely to miss.</p>
</div>

## Vertical Risers, Shafts, and Columns

The second interface point is vertical instead of horizontal. Plumbing stacks, electrical risers, and mechanical shafts all need a continuous, unobstructed vertical path from the lowest level they serve to the highest — and structural columns, shear walls, and braced frames need to land on a consistent grid for the same reason, floor after floor. Both disciplines are competing for the same core and corner locations, because those are structurally efficient column positions and mechanically efficient riser locations at the same time.

When the structural grid and the MEP riser plan are developed on separate tracks — common on fast-moving design schedules — a shaft that reads as clear on the mechanical drawings can land squarely on a column centerline once the structural set catches up. Catching this one requires reading the structural column grid and the MEP riser plan side by side, floor by floor, not reviewing either set in isolation.

## Ceiling Plenum Stack-Up

Above every finished ceiling, there's a fixed amount of vertical space, and every discipline with something to hang in that space is drawing as if it has first claim to it: structural for beam depth and camber, mechanical for ductwork and diffusers, plumbing for piping and slope, electrical for cable tray and lighting, fire protection for sprinkler mains and branch lines. None of those drawings show the others' elements stacked in the same section.

A structural drawing that shows adequate beam depth for span and load doesn't show whether there's still room below it for the MEP stack-up the mechanical and plumbing drawings assume is available. This is one of the conflicts that a plan-view-only read of the set will never catch — it only shows up when someone builds the section and stacks every trade's elements in the actual available depth.

<div class="mini-report">
  <div class="rh"><span class="title">STACK-UP INTERFACE</span><span class="meta">what competes for plenum depth</span></div>
  <div class="mini-row"><span class="k">Structural</span><span class="v">Beam/joist depth, camber</span></div>
  <div class="mini-row"><span class="k">Mechanical</span><span class="v">Ductwork, diffusers, VAV boxes</span></div>
  <div class="mini-row"><span class="k">Plumbing</span><span class="v">Piping, required slope</span></div>
  <div class="mini-row"><span class="k">Fire protection</span><span class="v hot">Sprinkler mains, branch lines</span></div>
  <div class="mini-row"><span class="k">Electrical</span><span class="v">Cable tray, conduit, lighting</span></div>
</div>

## Embeds, Anchor Bolts, and Underslab Routing

Below the finished floor and inside the foundation, the same fight happens with concrete instead of ceiling tile. Structural drawings call out embeds, anchor bolts, and reinforcing that need to land in specific locations to do their job — and MEP drawings route underslab plumbing, conduit, and drainage through the same footprint, often on a separate sheet set with a separate revision history. A plumbing line routed straight through a footing, or a conduit run that conflicts with reinforcing steel that's already been detailed, is a conflict that's far more expensive to catch once concrete has been placed than it is on paper.

Post-tensioned slabs raise the stakes further. PT cable layouts are unforgiving — a sleeve or penetration placed where a tendon was supposed to run isn't a redesign, it's a structural engineer of record sign-off and, in the worst cases, a rework of cured concrete.

## Structural Connections Blocking MEP Paths

The last interface point is the one that's easiest to miss on a plan-view review: structural connections themselves. Moment connections, gusset plates, cross-bracing, and other structural steel connection details occupy space beyond the nominal beam or column footprint shown on a simplified plan. An MEP route that reads as clear against the structural member's centerline can still run directly into a connection detail that only shows up on the structural drawings' enlarged connection sheets — sheets an MEP-focused reviewer may never open.

## Why These Conflicts Survive Individual Discipline QC

Each discipline's own QA/QC process checks that its own drawings are internally consistent — that the duct sizes are right, that the beam sizes carry the load, that the plumbing meets code. None of that QC is built to catch a conflict that only exists when two disciplines' drawings are read together. That's a structural review question and an MEP review question at the same time, and it's exactly the kind of conflict [a missed clash between a duct and a beam](/blog/missed-mep-clash-change-order-cost/) turns into a change order with no natural ceiling on its cost — because by the time it's found, the fix isn't a redline, it's demo.

It's also why RFI count is a misleading signal here. A team can run a clean RFI log through the entire structural and MEP coordination phase and still have every one of these interface points unresolved, because [a low RFI count reflects how few questions got asked, not how few conflicts exist](/blog/rfi-reduction-coordination-conflicts/) in the set.

<div class="takeaways">
  <h3>Key takeaways</h3>
  <ul>
    <li>MEP/structural drawing coordination conflicts cluster at five predictable interface points: horizontal framing, vertical risers/shafts, ceiling plenum stack-up, embeds and underslab routing, and structural connection details.</li>
    <li>Hard clashes are rarer but costlier to fix in the field; soft clashes are more numerous and easier to miss on a quick pass.</li>
    <li>Plenum stack-up conflicts don't show up in plan view — they require reading a section with every trade's elements stacked together.</li>
    <li>Structural connection details (moment connections, gusset plates) occupy more space than the simplified member shown on a basic plan, and MEP routing that clears the member centerline can still hit the connection.</li>
    <li>Each discipline's individual QA/QC checks internal consistency, not cross-discipline fit — catching these conflicts requires a review built to read both sets together.</li>
  </ul>
</div>

## Frequently Asked Questions

### Why do MEP and structural conflicts keep happening if both disciplines use BIM?

A federated BIM model can catch a modeled geometric clash between a duct and a beam, but only if both elements are modeled to a level of development that includes their actual geometry — and only if the model is actually run and reviewed before the set is issued. Sequencing gaps, late design changes on one discipline's model, and elements that were never modeled at the right level of detail (like structural connection geometry) all let conflicts through a clash-detection pass.

### Which interface point causes the most expensive change orders?

Hard clashes between ductwork or piping and structural framing tend to generate the highest per-incident cost, because the fix in the field usually means demo and re-fabrication rather than a design revision. Conflicts caught in embeds or post-tensioned slabs can be even costlier when they aren't caught until after concrete placement.

### Can a plan-view review catch a plenum stack-up conflict?

Not reliably. A plenum stack-up conflict only becomes visible in section, once every trade's elements — structural depth, ductwork, piping, cable tray, sprinkler mains — are drawn stacked in the same available space. A reviewer working only from plan views can miss a stack-up conflict even when every individual plan sheet looks clean.

### Whose responsibility is it to catch a structural-MEP conflict before bid?

It depends on the delivery method and contract, but in practice, no single discipline's QA/QC process is built to catch a conflict that only exists across two disciplines' drawings. That's why an independent, cross-discipline document review — reading structural and MEP sheets side by side rather than in isolation — exists as a distinct step from either discipline's own quality control.

### Does clash detection replace the need for a document review?

No. Clash detection catches modeled geometry conflicts in a federated BIM model, but it doesn't catch spec-versus-drawing contradictions, general notes that conflict with a detail, or conflicts involving elements that were never modeled at the right level of development. A document review reads the actual issued set — drawings and specs together — which is a different check than running a clash report against a model.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Why do MEP and structural conflicts keep happening if both disciplines use BIM?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "A federated BIM model can catch a modeled geometric clash between a duct and a beam, but only if both elements are modeled to a level of development that includes their actual geometry — and only if the model is actually run and reviewed before the set is issued. Sequencing gaps, late design changes on one discipline's model, and elements that were never modeled at the right level of detail (like structural connection geometry) all let conflicts through a clash-detection pass."
      }
    },
    {
      "@type": "Question",
      "name": "Which interface point causes the most expensive change orders?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Hard clashes between ductwork or piping and structural framing tend to generate the highest per-incident cost, because the fix in the field usually means demo and re-fabrication rather than a design revision. Conflicts caught in embeds or post-tensioned slabs can be even costlier when they aren't caught until after concrete placement."
      }
    },
    {
      "@type": "Question",
      "name": "Can a plan-view review catch a plenum stack-up conflict?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Not reliably. A plenum stack-up conflict only becomes visible in section, once every trade's elements — structural depth, ductwork, piping, cable tray, sprinkler mains — are drawn stacked in the same available space. A reviewer working only from plan views can miss a stack-up conflict even when every individual plan sheet looks clean."
      }
    },
    {
      "@type": "Question",
      "name": "Whose responsibility is it to catch a structural-MEP conflict before bid?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "It depends on the delivery method and contract, but in practice, no single discipline's QA/QC process is built to catch a conflict that only exists across two disciplines' drawings. That's why an independent, cross-discipline document review — reading structural and MEP sheets side by side rather than in isolation — exists as a distinct step from either discipline's own quality control."
      }
    },
    {
      "@type": "Question",
      "name": "Does clash detection replace the need for a document review?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No. Clash detection catches modeled geometry conflicts in a federated BIM model, but it doesn't catch spec-versus-drawing contradictions, general notes that conflict with a detail, or conflicts involving elements that were never modeled at the right level of development. A document review reads the actual issued set — drawings and specs together — which is a different check than running a clash report against a model."
      }
    }
  ]
}
</script>
