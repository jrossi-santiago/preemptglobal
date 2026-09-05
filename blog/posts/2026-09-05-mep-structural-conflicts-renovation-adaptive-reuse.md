---
title: "MEP/Structural Coordination Conflicts on Renovation and Adaptive Reuse Projects: Why Existing Conditions Raise the Risk"
slug: mep-structural-conflicts-renovation-adaptive-reuse
date: 2026-09-05
description: "MEP/structural drawing coordination conflicts are already the most common clash category on any set. Renovation and adaptive reuse projects compound that risk — here's why."
deck: "Structural-MEP conflicts are already the highest-frequency clash category on a new-construction set. On a renovation or adaptive reuse project, the same conflict has a second way to happen — and the drawings alone won't show you which one you're looking at."
tags: [Coordination, MEP, Structural]
---

!lede MEP/structural drawing coordination conflicts are already the single most common clash category on any multi-discipline set, new construction included. Renovation and adaptive reuse projects don't just inherit that baseline risk — they add a second failure mode on top of it, one that has nothing to do with whether the mechanical and structural engineers coordinated with each other on this project at all.

On new construction, a structural-MEP conflict means two disciplines drew against each other badly: a duct routed through a beam, a hanger load the framing wasn't sized for, a penetration nobody sleeved. Fix that by reading both sheets together before the set is issued, and the conflict goes away. On a renovation or adaptive reuse project, that same category of conflict can happen even when both disciplines drew perfectly against the existing-conditions documentation they were handed — because the building the mechanical and structural drawings were coordinated against isn't necessarily the building that's actually there.

## Why Structural-MEP Risk Doesn't Just Carry Over — It Compounds

Published clash-detection research already identifies structural-versus-MEP as the single most frequent discipline-pairing in coordination data, ahead of any other combination measured — a baseline true of [any set, on any project type](/blog/mep-structural-interface-points-fail-most-often/). Renovation and adaptive reuse work stacks three additional constraints on top of that baseline that new construction doesn't have to solve for at all.

First, plenum space is fixed. A new building's ceiling void, riser, and shaft dimensions get set by the design team specifically to fit the MEP scope planned for it. An existing building's plenum space was sized for whatever occupied it originally — often decades before the current program was contemplated — and every duct, cable tray, sprinkler line, and conduit competing for that same fixed volume has less room to avoid each other than a new-construction set would give them.

Second, structural members are fixed too, in a way that changes what a coordination conflict actually costs to fix. On new construction, a duct-versus-beam clash caught during design is a redline — move the line, done. On a renovation, the beam in conflict may be existing structure that can't simply be relocated or resized without a separate engineering scope, which means a coordination conflict that would be a two-minute fix on a new set can require its own analysis, its own retrofit detail, and its own line item before the mechanical drawing can even be corrected.

Third, and least visible on the drawings themselves: existing structural and MEP capacity was sized for the building's original use, not the one going in now. A change of occupancy — office to residential, warehouse to flex/light-industrial — routinely asks existing framing, electrical service, and HVAC infrastructure to carry a load path or capacity nobody originally designed them for.

<div class="callout">
  <div class="cl-label">Worth knowing</div>
  <p>Laser-scan point cloud data can capture existing plenum, shaft, and structural geometry at millimeter-level accuracy — a meaningful upgrade over inherited as-built drawings, which frequently reflect assumptions rather than field-verified conditions. The gap between what a point cloud shows and what an older as-built shows is exactly where a coordination review needs to check its source before trusting either the mechanical or the structural sheet drawn against it.</p>
</div>

## Two Ways the Same Conflict Can Happen — and Only One Shows Up in a Drawing-Only Read

A document-level coordination review normally works by reading one discipline's sheets against another's, looking for the point where their assumptions about shared space or shared structure disagree. That catches the first failure mode on a renovation set just as well as it does on new construction: mechanical and structural drawn against each other badly, on the same existing-conditions baseline.

It does not, by itself, catch the second failure mode: mechanical and structural drawn *consistently* with each other, and both wrong about the building. If the existing-conditions survey the design team worked from understated a beam's actual depth, missed an undocumented duct bank from a prior tenant fit-out, or simply predates several rounds of unrecorded alterations, the mechanical and structural sheets can agree with each other completely and still conflict with the real condition behind the ceiling. A 2020 peer-reviewed study in the *Journal of Construction Engineering and Management*, analyzing 517 change orders across 27 renovation projects, found that change orders driven by unforeseen existing conditions carried significantly higher mean cost than change orders from other causes — and identified HVAC as the trade with the single highest cost impact per change order in that category, even though concrete generated the highest overall volume. That's the second failure mode showing up in real cost data: an MEP conflict nobody could see on the sheet, because the sheet was drawn against a version of the building that wasn't accurate to begin with.

<div class="mini-report">
  <div class="rh"><span class="title">RENOVATION MEP/STRUCTURAL RISK — TWO FAILURE MODES</span><span class="meta">what a review has to check for each</span></div>
  <div class="mini-row"><span class="k">Design-vs-design conflict</span><span class="v">Same as new construction — read MEP and structural sheets against each other</span></div>
  <div class="mini-row"><span class="k">Design-vs-existing-building conflict</span><span class="v hot">Unique to reuse — verify existing-conditions source before trusting either sheet</span></div>
  <div class="mini-row"><span class="k">Trade generating the most unforeseen-condition change orders</span><span class="v">Concrete (JCEM study)</span></div>
  <div class="mini-row"><span class="k">Trade with highest cost impact per change order</span><span class="v hot">HVAC (JCEM study)</span></div>
</div>

## Where Existing Structural Capacity Becomes the Constraint on the MEP Design

A structural-MEP conflict on new construction is almost always a routing or clearance problem — the duct is in the wrong place relative to the beam. On a reuse project, it's just as often a capacity problem: the existing member is in the *right* place, but wasn't sized to carry what the new MEP scope is now asking of it. New rooftop condensing units landing on existing roof framing sized for a lighter original load. New hanger points added to bar joists that already have manufacturer-set limits on attached load, with no record of how much of that allowance prior tenant work already used. A new penetration through an existing shear wall or transfer beam that reads as routine on the mechanical sheet and as a life-safety structural issue the moment someone checks what that member is actually doing in the lateral system.

None of those show up as a clash in the geometric sense — nothing overlaps on the drawing. They show up as an omission: a structural capacity check that either happened and isn't documented in the set, or never happened at all, because the mechanical drawing treated the existing member as available space rather than as a load-bearing element with a documented (or undocumented) history of prior modification.

## Undocumented Modifications: The Conflict a New-Construction Review Never Has to Consider

Every occupied building older than a few years has usually been touched by work that predates the current project — a prior tenant's ceiling-mounted equipment, an electrical panel upgrade, a partial re-route of plumbing that never made it back onto an as-built. None of that history is necessarily wrong to leave undocumented at the time; it's just rarely reconciled before the next design team inherits the drawings and treats them as current. That's a category of coordination risk a [document review checklist for renovation and adaptive reuse work](/blog/document-review-checklist-renovation-adaptive-reuse/) has to check for that a new-construction checklist simply doesn't need — there's no equivalent "undocumented history" to verify on a clean site.

The practical implication for a reviewer reading a renovation or adaptive reuse set: cross-discipline coordination between mechanical and structural sheets is necessary but not sufficient. It closes the design-vs-design gap the same way it always does — the same interface points that [fail most often on any set](/blog/mep-structural-interface-points-fail-most-often/) still fail most often here. But closing the design-vs-existing-building gap requires a separate check: verifying how the existing-conditions information was captured, how recently, and against what portion of the building's actual modification history — before treating anything drawn against it as settled fact. Skip that second check, and a set can pass a fully coordinated cross-discipline review and still put a mechanical sub in the same position [a single missed clash always creates](/blog/missed-mep-clash-change-order-cost/): standing in front of a structural member that isn't where, or isn't what, the drawings said it was.

<div class="takeaways">
  <h3>Key takeaways</h3>
  <ul>
    <li>Structural-MEP conflicts are already the highest-frequency clash category on any set; renovation and adaptive reuse work adds fixed plenum space, fixed structural members, and unverified original-use capacity limits on top of that baseline.</li>
    <li>A 2020 study of 517 change orders across 27 renovation projects found unforeseen-existing-conditions change orders cost significantly more on average, with HVAC carrying the highest per-change-order cost impact of any trade.</li>
    <li>Two distinct failure modes exist on a reuse set: mechanical and structural drawn badly against each other (same as new construction), and mechanical and structural drawn consistently but against inaccurate existing-conditions information (unique to reuse).</li>
    <li>Existing structural capacity for new MEP loads — rooftop equipment, hanger points, new penetrations through load-bearing members — is often the real constraint, and it doesn't show up as a geometric clash on the drawing.</li>
    <li>A cross-discipline coordination read alone isn't sufficient on reuse work; the existing-conditions survey's source and recency need their own verification before either discipline's sheet can be trusted.</li>
  </ul>
</div>

## Frequently Asked Questions

### Are MEP/structural conflicts really worse on renovation projects than new construction?

The underlying clash category is the same — structural-versus-MEP is already the most common discipline-pairing on any set. Renovation and adaptive reuse projects add constraints new construction doesn't have: fixed plenum space sized for the building's original use, existing structural members that can't simply be relocated, and existing capacity that was never verified against the new program. Those constraints don't create a new clash category, but they raise both the frequency and the cost of the conflicts already in that category.

### Can a coordinated set still have MEP/structural conflicts on a renovation project?

Yes — this is the failure mode unique to reuse work. If the mechanical and structural drawings are consistent with each other but were both drawn against inaccurate or outdated existing-conditions information, the set can look fully coordinated and still conflict with the real building once construction starts.

### Why does HVAC carry the highest cost impact in unforeseen-condition change orders?

A peer-reviewed study of renovation change orders found HVAC had the highest cost impact per change order tied to unforeseen existing conditions, even though concrete generated more change orders overall. HVAC systems typically require continuous routing through plenum and shaft space that's fixed by the existing building, so a single unforeseen obstruction can cascade into a longer re-route or capacity fix than a more localized structural or concrete correction.

### Does a structural capacity check belong in an MEP coordination review, or is that a separate scope?

It has to be part of the same review on reuse work, even though it's a different kind of check than a geometric clash search. Verifying that existing framing, hangers, and penetrable members were checked against new MEP loads — not just routed around them — is the piece of a renovation coordination review that a new-construction review doesn't need, because new-construction structure is sized for its final MEP scope from the start.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Are MEP/structural conflicts really worse on renovation projects than new construction?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The underlying clash category is the same, structural-versus-MEP is already the most common discipline-pairing on any set. Renovation and adaptive reuse projects add constraints new construction doesn't have: fixed plenum space sized for the building's original use, existing structural members that can't simply be relocated, and existing capacity that was never verified against the new program. Those constraints don't create a new clash category, but they raise both the frequency and the cost of the conflicts already in that category."
      }
    },
    {
      "@type": "Question",
      "name": "Can a coordinated set still have MEP/structural conflicts on a renovation project?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes, this is the failure mode unique to reuse work. If the mechanical and structural drawings are consistent with each other but were both drawn against inaccurate or outdated existing-conditions information, the set can look fully coordinated and still conflict with the real building once construction starts."
      }
    },
    {
      "@type": "Question",
      "name": "Why does HVAC carry the highest cost impact in unforeseen-condition change orders?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "A peer-reviewed study of renovation change orders found HVAC had the highest cost impact per change order tied to unforeseen existing conditions, even though concrete generated more change orders overall. HVAC systems typically require continuous routing through plenum and shaft space that's fixed by the existing building, so a single unforeseen obstruction can cascade into a longer re-route or capacity fix than a more localized structural or concrete correction."
      }
    },
    {
      "@type": "Question",
      "name": "Does a structural capacity check belong in an MEP coordination review, or is that a separate scope?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "It has to be part of the same review on reuse work, even though it's a different kind of check than a geometric clash search. Verifying that existing framing, hangers, and penetrable members were checked against new MEP loads, not just routed around them, is the piece of a renovation coordination review that a new-construction review doesn't need, because new-construction structure is sized for its final MEP scope from the start."
      }
    }
  ]
}
</script>
