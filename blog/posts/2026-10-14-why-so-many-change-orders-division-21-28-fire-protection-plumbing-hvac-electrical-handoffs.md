---
title: "Why So Many Change Orders Start in Division 21–28 Scope: Fire Protection, Plumbing, HVAC, and Electrical Handoffs"
slug: why-so-many-change-orders-division-21-28-fire-protection-plumbing-hvac-electrical-handoffs
date: 2026-10-14
description: "Why so many change orders start in Division 21–28 scope: fire protection, plumbing, HVAC, and electrical handoffs, and the drawing checks that catch them first."
deck: "Fire protection, plumbing, HVAC, and electrical are drawn by different teams, bought as different trades, and installed in the same ceiling. The handoffs between them are where the change orders start."
tags: [Change Orders, MEP, Coordination, Specifications]
---

!lede If you are asking why so many change orders start in the mechanical, electrical, plumbing, and fire protection scope, the short answer is that those trades share the same ceiling, the same walls, and the same shafts, but they are drawn and specified separately. The handoffs between them are where nobody owns the answer.

This post looks at one slice of that question: the Division 21 through 28 scope, and the specific handoffs inside it that turn into RFIs and change orders. For the broader picture, see [why so many change orders happen at all](/blog/why-so-many-change-orders/).

## What Division 21–28 Actually Covers

In the CSI MasterFormat layout, the building systems sit in a block of divisions: Division 21 is fire suppression, 22 is plumbing, 23 is HVAC, 26 is electrical, 27 is communications, and 28 is electronic safety and security. Each has its own spec section set, its own drawing series, and usually its own engineer of record and its own subcontractor.

That separation is sensible for design and procurement. It is also the root of the problem. Each division is internally complete on its own sheets. The conflict lives where one division's output becomes another division's input, and the set rarely says who closes that gap.

<div class="callout">
  <div class="cl-label">Worth knowing</div>
  <p>A handoff is any point where one trade's work depends on a number, location, or load that another trade's drawings are responsible for. If neither set states it, both trades can price the job as complete and still be wrong.</p>
</div>

## The Handoffs Where Division 21–28 Change Orders Start

### 1. Fire protection versus everything above the ceiling

Sprinkler drawings are frequently a delegated or deferred submittal, produced after the other disciplines have settled their routing. Mains, branch lines, and heads then have to fit into space that ductwork, cable tray, and plumbing have already claimed. The sprinkler contractor finds the conflict at shop drawing stage, and the fix is either a reroute or a claim for extra material and labor. A reviewer asks a simple question of the base set: is there a coordinated ceiling zone for sprinkler piping, or is it assumed?

### 2. Plumbing slope versus ceiling height

Gravity drainage needs slope, and slope consumes vertical space over a distance. A long horizontal storm or sanitary run can drop well below the plane the architect assumed for the ceiling, particularly where it crosses ductwork. The plumbing plan shows the pipe. The reflected ceiling plan shows the ceiling. Neither shows that the pipe's invert at the far end does not fit. Compare invert elevations against the ceiling and structure on the same section.

### 3. HVAC equipment versus electrical service

Mechanical schedules list equipment loads: motors, VFDs, electric heat, and controls. The electrical set has to carry feeders, breakers, and disconnects for the same equipment. When equipment is changed or substituted during design, the mechanical schedule updates and the panel schedule does not. The result is a unit that arrives with a different voltage, phase, or amperage than the one the electrical set provides for. Cross-check every piece of equipment schedule against the panel schedule and one-line diagram.

### 4. Electrical clearances versus the room they sit in

Code requires working clearance in front of switchgear and panels, and dedicated space above and around them. Electrical rooms are often sized early and then invaded by a duct chase, a sprinkler riser, or a plumbing line passing through. Equipment on the one-line is shown correctly. The room plan shows the architectural footprint. Only a side-by-side check shows the clearance zone is occupied.

### 5. Controls, low voltage, and who provides what

Division 23 controls, Division 26 power, Division 27 communications, and Division 28 security and fire alarm all touch the same devices: door hardware, dampers, smoke control, elevators, and access control. Responsibility lines are often drawn in a single note, or not drawn at all. Each trade assumes another provides the conduit, the power, or the relay. This is a classic scope gap, and it surfaces as a change order the moment someone asks who was supposed to supply it.

<div class="mini-report">
  <div class="rh"><span class="title">DIVISION 21–28 HANDOFF CHECKS</span><span class="meta">what a reviewer compares across sheets</span></div>
  <div class="mini-row"><span class="k">Sprinkler routing</span><span class="v">Fire protection zone vs. ductwork, tray, and piping above ceiling</span></div>
  <div class="mini-row"><span class="k">Drainage slope</span><span class="v">Plumbing inverts vs. ceiling and structure elevations</span></div>
  <div class="mini-row"><span class="k">Equipment power</span><span class="v hot">Mechanical schedules vs. panel schedules and one-line</span></div>
  <div class="mini-row"><span class="k">Electrical rooms</span><span class="v">Working clearance vs. what else is routed through</span></div>
  <div class="mini-row"><span class="k">Controls and low voltage</span><span class="v">Who provides conduit, power, and relays at shared devices</span></div>
</div>

## Why These Handoffs Survive Normal QC

Each discipline's engineer checks their own sheets, and each set passes. Spec sections are written to describe a trade's own work, so they reinforce the division boundary instead of crossing it. The drawings agree with themselves and disagree with each other.

That is why a set can clear its own review and still produce RFIs once the trades start coordinating in the field. We covered the mechanics of that in [why "it passed QA/QC" doesn't mean the set is coordinated](/blog/qa-qc-passed-doesnt-mean-set-coordinated/).

## Where the Money Goes

Handoff errors rarely cost much to fix on paper and cost a great deal after installation. A reroute drawn in review is a markup. The same reroute after rough-in is demolition, new material, resequenced labor, and a delay to whoever follows in that space. We have laid out the pattern in [the interface points that fail most often](/blog/mep-structural-interface-points-fail-most-often/) and [where structural-versus-MEP conflicts originate](/blog/structural-vs-mep-where-coordination-conflicts-originate/). The dollars depend on the project, so we do not put a generic figure on it here.

## A Practical Way to Check Before Bid

1. List every piece of equipment in the mechanical and plumbing schedules and confirm each has a matching electrical feed.
2. Identify every deferred or delegated submittal in Division 21 through 28, and confirm the base set reserves space for it.
3. Pull a ceiling zone section at the tightest corridor and trace every system through it.
4. Mark every electrical room and mechanical room and verify clearances against actual routing.
5. Find every shared device and write down which trade provides each component.

<div class="takeaways">
  <h3>Key takeaways</h3>
  <ul>
    <li>Division 21–28 change orders usually start at handoffs between trades, not inside any single trade's drawings.</li>
    <li>Deferred sprinkler design and equipment-to-panel mismatches are two of the most common sources.</li>
    <li>Spec sections divide work by trade, so scope gaps sit between sections where no one reads.</li>
    <li>Handoffs cost the least to fix on paper before bid.</li>
  </ul>
</div>

## Frequently Asked Questions

### Why do so many change orders involve MEP and fire protection?

These trades share limited space and depend on each other's numbers, yet are drawn and procured separately. When one changes, the others do not always follow, and the mismatch is found during installation.

### Which division causes the most change orders?

There is no honest single answer without a sourced study, and it varies by project type. In practice, the problem is less one division than the interfaces among Divisions 21, 22, 23, and 26.

### Are deferred fire protection submittals a risk?

They can be. If the base set does not reserve a coordinated sprinkler zone, the sprinkler contractor designs into whatever space is left, and conflicts show up at shop drawings.

### Can a drawing review catch these before bid?

Yes. Handoff conflicts are visible on the documents if the sheets are read against each other, which is the purpose of an independent cross-discipline review.

<script type="application/ld+json">
{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
{"@type":"Question","name":"Why do so many change orders involve MEP and fire protection?","acceptedAnswer":{"@type":"Answer","text":"These trades share limited space and depend on each other's numbers, yet are drawn and procured separately. When one changes, the others do not always follow, and the mismatch is found during installation."}},
{"@type":"Question","name":"Which division causes the most change orders?","acceptedAnswer":{"@type":"Answer","text":"There is no honest single answer without a sourced study, and it varies by project type. In practice, the problem is less one division than the interfaces among Divisions 21, 22, 23, and 26."}},
{"@type":"Question","name":"Are deferred fire protection submittals a risk?","acceptedAnswer":{"@type":"Answer","text":"They can be. If the base set does not reserve a coordinated sprinkler zone, the sprinkler contractor designs into whatever space is left, and conflicts show up at shop drawings."}},
{"@type":"Question","name":"Can a drawing review catch these before bid?","acceptedAnswer":{"@type":"Answer","text":"Yes. Handoff conflicts are visible on the documents if the sheets are read against each other, which is the purpose of an independent cross-discipline review."}}
]}
</script>
