---
title: "A Document Review Checklist for Cleanroom and Containment Lab Buildings: What Classification-Driven Detail Adds to Scope"
slug: document-review-checklist-cleanroom-containment-lab-buildings
date: 2026-10-09
description: "A document review checklist for cleanroom and containment lab buildings: trace ISO class and BSL claims from the room schedule to pressure, exhaust, finishes, and controls."
deck: "On a cleanroom or containment lab, the classification on the room schedule is a promise the rest of the set has to keep. This checklist walks the sheets where that promise gets made, and where it quietly breaks."
tags: [Document Review, Life Sciences, Coordination]
---

!lede A document review checklist for a standard building asks whether the sheets agree with each other. A document review checklist for a cleanroom or containment lab asks that, then asks a harder question: when the room schedule says ISO 7 or BSL-3, can you follow that label through every discipline until you reach the equipment, the pressure, and the sequence that make it true? Each classification pulls detail out of architectural, mechanical, electrical, plumbing, and controls sheets at once. If one of them leaves its piece out, the label is still on the door, but nothing in the set backs it up.

## How to Use This Checklist

Start from the classification, not the discipline. For every room carrying an ISO cleanliness class, a biosafety level, or a USP compounding designation, pick the room and trace it through the sheets below. A conflict found this way is usually a missing piece, not a disagreement: the architectural plan promises something the mechanical set never provides. That kind of gap doesn't show up in a sheet-to-sheet comparison, because there is nothing on the second sheet to compare against.

For the background on the standards behind these rooms (ISO 14644-1, USP 797 and 800, BMBL), see our breakdown of [what cleanroom and containment sets add to a document review's scope](/blog/construction-document-review-services-life-sciences-cleanroom-containment/). This post is the working list.

## 1. Classification Inventory

- Is there one list of every classified room (ISO class, BSL level, USP designation) that the architectural, mechanical, and controls sets all reference?
- Does each room's classification match across the room schedule, life-safety plan, mechanical zone drawings, and equipment schedules?
- Are adjacent rooms of different classification ordered so the cleaner or more hazardous space sits where the pressure cascade needs it?

A room that's ISO 7 on one sheet and ISO 8 on another is the easiest finding on this list, and the one most likely to be sitting in a set that otherwise looks coordinated.

## 2. Pressure Cascade and Airflow

- Is a target pressure differential shown for every classified room, and does it run in the direction the classification requires?
- Does the mechanical set show supply, return, and exhaust quantities that can actually produce the differential, or only the target number?
- Are rooms with opposite pressure requirements (positive buffer rooms next to negative containment rooms) on independent control, not a shared air handler or return path?
- For containment space, is the exhaust shown with redundancy, and does the control sequence prevent the room from going positive if a fan fails?

<div class="callout">
  <div class="cl-label">Worth knowing</div>
  <p>A pressure differential written on a room schedule is a target. The mechanical drawings are where it either becomes a supply-versus-exhaust offset someone can verify, or stays a number nobody has to hit.</p>
</div>

## 3. Filtration and Air Handling

- Are HEPA filters shown at the terminal or in a housing where the classification needs them, with the housing accessible for testing and replacement?
- Is the physical space for filter housings, extra exhaust fans, and the ductwork they require actually available above the ceiling and in the mechanical room?
- Do the equipment schedule and the plan agree on how many air handlers serve the classified zone?

This is where cleanroom sets collide with structure. Added redundancy and filter housings need ceiling and shaft space the architectural and structural sheets may never have reserved. See the [MEP and structural conflicts that show up when equipment grows late in design](/blog/mep-structural-conflicts-data-center-retrofits/) for how that pattern plays out.

## 4. Envelope, Finishes, and Penetrations

- Do the wall, ceiling, and floor finishes in classified rooms match what the classification requires (smooth, cleanable, sealed at joints), and does the finish schedule match the spec?
- Is every penetration through a classified room's envelope (pipe, conduit, duct, sprinkler drop) shown with a seal detail, not left to field decision?
- Do door and window schedules show the hardware, interlocks, and sealing the airlocks and pass-throughs need?
- Are ceilings in classified rooms detailed so light fixtures, diffusers, and sprinkler heads can be installed without breaking the seal?

Penetrations are the most common place for an otherwise well-drawn room to fail. Every discipline sends something through the envelope, and no one discipline owns the seal.

## 5. Airlocks, Interlocks, and Access Control

- Are airlocks and anterooms drawn with the sequence of operation for their door interlocks, not only two doors on a plan?
- Do the electrical and controls sheets show the interlock wiring, alarms, and monitoring devices the architectural plan implies?
- Is emergency egress shown to work with an interlocked or access-controlled door, and is that reconciled with the life-safety plan?

Interlocks are drawn in architecture, wired in electrical, and sequenced in controls. A set can be consistent within each discipline and still leave the interlock incomplete across them.

## 6. Plumbing, Process, and Waste

- Are process gases, purified water, and vacuum shown with routing that respects the classified envelope?
- Do sinks, floor drains, and eyewash stations in classified rooms follow the cleanliness or containment rules, or are they carried over from a standard lab detail?
- For containment space, is there a waste-handling or decontamination strategy shown, and does it connect to the plumbing and mechanical sets?

## 7. Power, Controls, and Monitoring

- Is emergency or standby power shown for the equipment that keeps the pressure cascade running?
- Does the controls narrative describe alarm thresholds and failure responses, and do the points list and electrical sheets support them?
- Are pressure monitors, sensors, and alarm panels located on the architectural plan, not just listed in a spec section?

## 8. Specifications Against Drawings

- Do the specs for HVAC, finishes, and controls reference the same classification the drawings do?
- Are testing and certification requirements (airflow balancing, particle counts, containment verification) written into the spec, and does the schedule allow time for them?
- Where a spec requires equipment the drawings don't show space for, which governs?

This ties directly to the [spec versus drawing conflicts that appear in equipment-heavy healthcare sets](/blog/spec-vs-drawing-conflicts-healthcare-equipment-room-data-sheets/): specified performance with no drawn space or connection to support it.

<div class="takeaways">
  <h3>Key takeaways</h3>
  <ul>
    <li>Trace each classified room from the room schedule to the pressure, filtration, finish, and controls sheets. Sheet-to-sheet comparison alone misses promises with nothing on the other end.</li>
    <li>Rooms with opposite pressure requirements need independent control and separate return paths.</li>
    <li>Redundancy and filter housings need ceiling, shaft, and mechanical room space. Confirm it was reserved.</li>
    <li>Penetrations and interlocks cross every discipline, so no single discipline owns them. Check them explicitly.</li>
    <li>Testing and certification belong in both the spec and the schedule.</li>
  </ul>
</div>

## Frequently Asked Questions

### What should a document review checklist for a cleanroom include?

It should include a classification inventory, pressure cascade and airflow, filtration and air handling, envelope and penetration details, airlock interlocks, process plumbing, power and controls, and spec-to-drawing agreement. Each item should be traced from the room schedule to the sheets that make it true.

### How is a cleanroom checklist different from a standard building checklist?

A standard checklist confirms the disciplines agree with each other. A cleanroom checklist also confirms the set contains the pressure, filtration, sealing, and control information needed to deliver each room's stated classification. Many gaps are omissions, so there is no second sheet to disagree with.

### Which sheets matter most on a containment lab?

The mechanical airflow and control sequences, the architectural room and door schedules, and the electrical and controls sheets that wire interlocks and alarms. These are where a containment classification either becomes a buildable system or stays a label.

### When should the review happen?

Before bid, and again after major revisions. Redundant exhaust, filter housings, and sealed penetrations all take space and coordination that are cheaper to resolve on paper than in a finished ceiling.

### Does every lab need a cleanroom-level checklist?

No. The added detail applies where a room carries an ISO class, a biosafety level, or a USP compounding designation. A standard teaching or research lab is better served by a [hybrid lab and classroom checklist](/blog/document-review-checklist-higher-education-lab-classroom-hybrid/).

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What should a document review checklist for a cleanroom include?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "It should include a classification inventory, pressure cascade and airflow, filtration and air handling, envelope and penetration details, airlock interlocks, process plumbing, power and controls, and spec-to-drawing agreement. Each item should be traced from the room schedule to the sheets that make it true."
      }
    },
    {
      "@type": "Question",
      "name": "How is a cleanroom checklist different from a standard building checklist?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "A standard checklist confirms the disciplines agree with each other. A cleanroom checklist also confirms the set contains the pressure, filtration, sealing, and control information needed to deliver each room's stated classification. Many gaps are omissions, so there is no second sheet to disagree with."
      }
    },
    {
      "@type": "Question",
      "name": "Which sheets matter most on a containment lab?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The mechanical airflow and control sequences, the architectural room and door schedules, and the electrical and controls sheets that wire interlocks and alarms. These are where a containment classification either becomes a buildable system or stays a label."
      }
    },
    {
      "@type": "Question",
      "name": "When should the review happen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Before bid, and again after major revisions. Redundant exhaust, filter housings, and sealed penetrations all take space and coordination that are cheaper to resolve on paper than in a finished ceiling."
      }
    },
    {
      "@type": "Question",
      "name": "Does every lab need a cleanroom-level checklist?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No. The added detail applies where a room carries an ISO class, a biosafety level, or a USP compounding designation. A standard teaching or research lab is better served by a hybrid lab and classroom checklist."
      }
    }
  ]
}
</script>
