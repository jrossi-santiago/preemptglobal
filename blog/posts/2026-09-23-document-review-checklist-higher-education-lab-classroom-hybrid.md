---
title: "A Document Review Checklist for Higher Education Lab and Classroom Hybrid Buildings"
slug: document-review-checklist-higher-education-lab-classroom-hybrid
date: 2026-09-23
description: "A document review checklist for higher education buildings that mix labs and classrooms under one roof — occupancy splits, fume hood exhaust, structural vibration, and utility coordination a standard checklist misses."
deck: "A STEM building that puts wet labs and lecture rooms in the same footprint isn't one building for code and coordination purposes — it's two, sharing a structure and a set of shafts. A document review checklist built for either half alone will miss where they meet."
tags: [Document Review, Coordination, Bid Documents]
---

!lede A hybrid lab-and-classroom building at a college or university reads as one project on the cover sheet and functions as two on every sheet after it. The classroom wing needs flexible, open floor plates, movable furniture, and nothing more exotic than power and data. The lab wing needs fume hood exhaust that can't be cross-connected to anything, vibration control the classroom side never has to think about, and a fire-separation strategy the building code treats as its own problem. A document review checklist written for a standard academic building checks whether the drawings agree with each other. A checklist for this building type has to check whether two different sets of requirements were coordinated at the line where they meet — and that line runs through the structure, the shafts, and the mechanical rooms, not around them.

## Why a Hybrid Building Needs Its Own Checklist

Most document review checklists assume one governing use drives the building's systems. A hybrid lab-classroom building doesn't have one governing use — it has two, occupying the same floor plate and sharing risers and, often, a mechanical penthouse. That forces decisions a purely instructional or purely research building never has to make: which occupancy classification applies to which zone, where the fire-rated separation between them actually sits, and whether the shafts serving the lab side were sized and routed without stealing space the classroom side's HVAC also needs. A [document review checklist for renovation and adaptive reuse projects](/blog/document-review-checklist-renovation-adaptive-reuse/) has to reconcile new design intent against an existing structure; a hybrid lab-classroom checklist has to reconcile two design intents against each other inside one new structure — a different coordination problem even when both halves are being built from scratch.

## Occupancy Classification: Where the Code Splits the Building in Two

Under the International Building Code, colleges and universities are generally classified as Group B (business) occupancy, even though the use is instructional. A classroom itself stays within that B classification as long as its occupant load stays at 49 or fewer; cross that threshold — a large lecture hall serving a hybrid STEM building often does — and the space reclassifies to Group A-3 (assembly), which carries its own egress and exiting requirements.

The lab side runs on a separate track. Historically, a teaching or research lab using hazardous chemicals above the code's maximum allowable quantities would trigger reclassification to Group H (high-hazard), with the far more restrictive structural, egress, and separation requirements that classification carries. Section 428 of the IBC, introduced for higher education laboratories, changes that calculus: a lab that meets Section 428's control-area and quantity provisions, together with Chapter 38 of the International Fire Code, can exceed the ordinary maximum allowable quantities for hazardous materials while remaining in Group B. That exception is exactly the kind of code-compliance detail a document review needs to confirm explicitly — not assumed from the drawings' cover sheet, but checked against the actual chemical inventory and control-area layout the lab was designed around.

<div class="callout">
  <div class="cl-label">Worth knowing</div>
  <p>IBC Section 428 lets a higher education laboratory hold more hazardous chemicals than the code's default limits without being pushed into Group H occupancy — but only if the control areas, quantities, and fire protection actually satisfy Section 428 and IFC Chapter 38. A set that assumes the Section 428 exception applies without the underlying control-area design to support it is carrying an occupancy classification the drawings haven't actually earned.</p>
</div>

A document review scoped for this building type should confirm, zone by zone: which spaces are B, which are A-3, whether any lab space is relying on the Section 428 exception and whether the control-area design actually supports that reliance, and — critically — where the fire-rated separation between the classroom zones and the lab zones is drawn, since a mixed-occupancy building lives or dies on whether that separation is continuous through the structure, not just shown correctly in one section cut.

## Fume Hood Exhaust: The System With No Room for a Coordination Miss

Fume hood exhaust is governed by NFPA 45, and the standard is unambiguous about what the ductwork can and can't do: air exhausted from a chemical fume hood may not be recirculated into the building, the ductwork serving the hood has to be dedicated to laboratory exhaust only — no mixing with general building return or exhaust — and fire dampers are not permitted inside fume hood exhaust ducts, since a damper that closes during a fire is a damper that traps hazardous fumes exactly where they shouldn't collect. Where flammable vapors are involved, the exhaust fan itself has to be spark-resistant construction. NFPA 45 also sets the lab's hazard classification (A through D based on the quantity and flammability of materials present), which in turn determines the fire-rated separation required around the lab space — a Class A lab up to 10,000 square feet needs 2-hour-rated walls, a Class B lab of the same size needs 1-hour walls, and Class C and D labs carry no area limit or special wall requirement at all.

None of that is a system a document review can verify by reading the mechanical sheet in isolation. It has to be checked against the structural and architectural sheets together: does the dedicated exhaust shaft actually run clean from hood to roof without ducking through a shared chase, is the roof-level exhaust discharge point far enough from any fresh-air intake serving the classroom side, and does the NFPA 45 class assigned on the life-safety plan match the fire-rated wall thickness actually drawn around that lab. A shaft that shares a chase with classroom-side return air, or a fume hood duct that was value-engineered into a shared vertical run to save floor space, is exactly the kind of finding this checklist exists to catch before it's a field problem instead of a redline.

## Structural and Vibration Coordination: What the Classroom Side Doesn't Need

A classroom floor plate is designed for people and furniture — a uniform, modest live load with no unusual sensitivity to how it performs. A lab floor plate serving analytical instrumentation, microscopy, or balance work is designed against a vibration criterion, not just a load number, and that criterion typically has to be satisfied by the structural bay itself — slab thickness, span, and column spacing — not corrected after the fact with an isolation pad under one piece of equipment. A hybrid building that puts vibration-sensitive lab space over or adjacent to a mechanical room, elevator, or high-traffic classroom corridor is asking the structure to solve a problem that's easiest to fix at the layout stage and hardest to fix once it's built.

<div class="mini-report">
  <div class="rh"><span class="title">STRUCTURAL & SYSTEM DEMANDS — CLASSROOM ZONE VS. LAB ZONE</span><span class="meta">what a hybrid-building review should confirm are resolved on paper</span></div>
  <div class="mini-row"><span class="k">Live load basis</span><span class="v">uniform occupant/furniture load vs. equipment-specific loading</span></div>
  <div class="mini-row"><span class="k">Vibration criterion</span><span class="v hot">none required vs. instrument-specific limit set at structural bay design</span></div>
  <div class="mini-row"><span class="k">Exhaust ductwork</span><span class="v">general return air vs. dedicated, non-recirculating fume hood exhaust</span></div>
  <div class="mini-row"><span class="k">Fire separation basis</span><span class="v">standard occupancy rules vs. NFPA 45 hazard class (A–D)</span></div>
</div>

A document review should flag any vibration-sensitive lab space whose structural bay wasn't explicitly designed to a stated vibration criterion, and any lab located directly above, below, or adjacent to a mechanical room, loading dock, or high-traffic classroom corridor without a documented vibration analysis addressing that adjacency.

## Utility Distribution: Where Fixed Casework Meets Movable Furniture

Lab casework is fixed infrastructure — benches plumbed for gas, vacuum, compressed air, and often reverse-osmosis or deionized water, positioned to keep emergency eyewash and safety showers within the code-required travel distance of any point where hazardous materials are used. Classroom furniture is the opposite: movable and dependent on power and data delivered flexibly enough to follow whatever layout that semester's instructor wants. A hybrid building's utility distribution plan has to serve both without either side compromising the other, and the document review should confirm the lab-side utility drops are actually routed to where the fixed casework plan shows them — not a generic grid that assumes furniture will move to meet the utilities, which is backward for a lab and the kind of miss a [checklist covering MEP and structural interface points](/blog/mep-structural-interface-points-fail-most-often/) is built to catch.

## The Flexibility Trap: "Convertible" Space Is a Documentation Problem, Not Just a Design Goal

Many hybrid buildings are programmed with classrooms designed to convert to lab space later, as departmental needs shift. That flexibility is a legitimate design goal, and it creates a specific document review blind spot: a set that shows a space as classroom occupancy today but was structurally and mechanically oversized "for future lab conversion" needs that intent documented and reviewed against actual code requirements now, not deferred to whenever the conversion happens. A document review should confirm the drawings state clearly which occupancy classification and system capacity the space is being reviewed and permitted for today, and treat any future-conversion capacity as a stated design allowance — verified for structural and shaft capacity — rather than an assumption that a later renovation will sort out compliance on its own. That same discipline matters on any building with a phased or uncertain end use, the same way it matters on [projects built for change-order risk in healthcare and life sciences work](/blog/change-order-risk-mitigation-healthcare-life-sciences/), where a space's eventual use can carry code consequences the initial design doesn't fully account for.

<div class="takeaways">
  <h3>Key takeaways</h3>
  <ul>
    <li>Confirm occupancy classification zone by zone — Group B by default, A-3 for classrooms and lecture halls over 49 occupants, and whether any lab space is relying on the IBC Section 428 exception with a control-area design that actually supports it.</li>
    <li>Verify fume hood exhaust ductwork is dedicated and non-recirculating, free of fire dampers, and that the NFPA 45 hazard class assigned matches the fire-rated wall construction actually drawn around the lab.</li>
    <li>Flag any vibration-sensitive lab space whose structural bay wasn't designed to a stated vibration criterion, especially adjacent to mechanical rooms or high-traffic classroom corridors.</li>
    <li>Check that fixed lab casework utility drops (gas, vacuum, compressed air, RO/DI water) are routed to match the casework plan, not a generic grid built for movable classroom furniture.</li>
    <li>Treat "future lab conversion" capacity in a classroom as a stated, structurally verified design allowance — not a deferred compliance question for whoever renovates the space later.</li>
  </ul>
</div>

## Frequently Asked Questions

### What occupancy classification applies to a hybrid lab and classroom building?

Most of the building falls under Group B, the standard classification for higher education facilities. Individual classrooms and lecture halls reclassify to Group A-3 once occupant load exceeds 49. Lab spaces can remain Group B even with hazardous chemical quantities above the code's ordinary limits if they qualify for the IBC Section 428 exception for higher education laboratories, which requires the control-area design and fire protection to meet Section 428 and IFC Chapter 38.

### Can fume hood exhaust ductwork share a chase with the classroom side's HVAC?

No. NFPA 45 requires fume hood exhaust ductwork to be dedicated to laboratory exhaust only, with no mixing or recirculation into general building air, and prohibits fire dampers inside the exhaust duct itself. A document review should confirm the exhaust shaft runs independently from hood to roof discharge, not through a chase shared with classroom-side return or supply air.

### Why does vibration matter for lab floors when it doesn't for classrooms?

Classroom floors only need to support people and furniture under a standard live-load assumption. Lab floors supporting sensitive instrumentation — microscopy, analytical balances, and similar equipment — are designed against a vibration criterion that has to be satisfied by the structural bay itself, since isolating one piece of equipment after construction is a far more limited fix than designing the slab and span for it up front.

### How does NFPA 45 affect the fire-rated separation around a lab?

NFPA 45 assigns labs a hazard classification from A through D based on the quantity and flammability of materials in use, and that classification sets the required fire-rated separation. A Class A lab up to 10,000 square feet needs 2-hour-rated walls, a Class B lab of the same size needs 1-hour walls, and Class C or D labs carry no special area limit or wall rating. A document review should confirm the classification on the life-safety plan matches the wall construction actually drawn.

### Should a document review check classroom space designed for "future lab conversion"?

Yes. That space should be reviewed against the occupancy classification and code requirements it's actually being permitted for today, with any future-conversion capacity — structural loading, shaft space, utility stub-outs — documented and verified as a stated design allowance rather than assumed to be resolved by a later renovation.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What occupancy classification applies to a hybrid lab and classroom building?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Most of the building falls under Group B, the standard classification for higher education facilities. Individual classrooms and lecture halls reclassify to Group A-3 once occupant load exceeds 49. Lab spaces can remain Group B even with hazardous chemical quantities above the code's ordinary limits if they qualify for the IBC Section 428 exception for higher education laboratories, which requires the control-area design and fire protection to meet Section 428 and IFC Chapter 38."
      }
    },
    {
      "@type": "Question",
      "name": "Can fume hood exhaust ductwork share a chase with the classroom side's HVAC?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No. NFPA 45 requires fume hood exhaust ductwork to be dedicated to laboratory exhaust only, with no mixing or recirculation into general building air, and prohibits fire dampers inside the exhaust duct itself. A document review should confirm the exhaust shaft runs independently from hood to roof discharge, not through a chase shared with classroom-side return or supply air."
      }
    },
    {
      "@type": "Question",
      "name": "Why does vibration matter for lab floors when it doesn't for classrooms?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Classroom floors only need to support people and furniture under a standard live-load assumption. Lab floors supporting sensitive instrumentation, such as microscopy or analytical balances, are designed against a vibration criterion that has to be satisfied by the structural bay itself, since isolating one piece of equipment after construction is a far more limited fix than designing the slab and span for it up front."
      }
    },
    {
      "@type": "Question",
      "name": "How does NFPA 45 affect the fire-rated separation around a lab?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "NFPA 45 assigns labs a hazard classification from A through D based on the quantity and flammability of materials in use, and that classification sets the required fire-rated separation. A Class A lab up to 10,000 square feet needs 2-hour-rated walls, a Class B lab of the same size needs 1-hour walls, and Class C or D labs carry no special area limit or wall rating. A document review should confirm the classification on the life-safety plan matches the wall construction actually drawn."
      }
    },
    {
      "@type": "Question",
      "name": "Should a document review check classroom space designed for future lab conversion?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. That space should be reviewed against the occupancy classification and code requirements it's actually being permitted for today, with any future-conversion capacity, such as structural loading, shaft space, or utility stub-outs, documented and verified as a stated design allowance rather than assumed to be resolved by a later renovation."
      }
    }
  ]
}
</script>
