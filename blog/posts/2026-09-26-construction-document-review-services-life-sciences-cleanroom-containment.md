---
title: "Construction Document Review Services for Life Sciences and Lab Buildings: What Cleanroom and Containment Sets Add to Scope"
slug: construction-document-review-services-life-sciences-cleanroom-containment
date: 2026-09-26
description: "How construction document review services scope differently for life sciences buildings — ISO 14644 cleanroom classification, USP 797/800 compounding rooms, and BSL containment pressure cascades a standard review doesn't check."
deck: "A cleanroom or containment lab doesn't just add equipment to a building — it adds a performance requirement the drawings have to prove on paper before anyone pours concrete. A document review scoped for a standard commercial set will miss where that proof breaks down."
tags: [Document Review, Life Sciences, Coordination]
---

!lede A standard commercial building's construction document review checks whether the disciplines agree with each other — does the structural grid match the architectural plan, do the MEP risers land where the shafts are sized for them, does the spec section match what's drawn. A life sciences building with cleanroom or containment space needs all of that, plus something a standard review doesn't have to check at all: whether the drawings actually deliver a stated, numeric performance requirement — an ISO particle class, a pressure differential in pascals, a room that stays negative even when a fan fails. Construction document review services for this building type aren't a bigger version of a standard review. They're a standard review plus a second, harder question: does this set prove the room will perform the way its classification says it has to, not just that the walls and ducts are drawn consistently.

## Why Cleanroom and Containment Space Changes the Review's Job

A typical document review confirms internal consistency — sheet A agrees with sheet M, the spec doesn't contradict the drawing, the shaft has room for what's routed through it. That's necessary but not sufficient once a room carries an ISO cleanliness class or a biosafety containment level, because those classifications are performance requirements, not descriptions. A room labeled "ISO 7" or "BSL-3" on the life-safety plan is making a claim about air changes, pressure differential, and filtration that has to be traceable through the mechanical design, not just typed onto a room-finish schedule. A [construction document review checklist for higher education lab and classroom buildings](/blog/document-review-checklist-higher-education-lab-classroom-hybrid/) already has to check occupancy classification and fume hood exhaust; a life sciences cleanroom or containment set raises the bar again, because the room's classification is a number the mechanical system either hits or doesn't — and a document review is one of the few places that gets checked before the room exists to test.

## Cleanroom Classification: What ISO 14644-1 Actually Requires the Drawings to Show

ISO 14644-1 sets nine cleanroom classes, from ISO Class 1 (the cleanest) down to ISO Class 9, based on the maximum particle count allowed per cubic meter of air at specified particle sizes. Pharmaceutical and life sciences buildings typically operate in ISO Classes 5, 7, and 8, which map to the Grade A–D cleanroom grades defined in EU GMP Annex 1. None of those classes are achieved by a room's shape or finish — they're achieved by HEPA filtration, air change rate, and a pressure cascade between rooms of different cleanliness, and all three of those are things a document review can and should verify are actually drawn, not just labeled.

<div class="callout">
  <div class="cl-label">Worth knowing</div>
  <p>ISPE guidance calls for a minimum 10-pascal pressure differential between cleanroom grades and at least 5 pascals between two rooms of the same classification, cleaner space staged at higher pressure than less-clean space around it. A document review should confirm that cascade is shown room-by-room on the mechanical drawings — not assumed from the room-finish schedule's ISO label.</p>
</div>

A set that assigns an ISO class on the architectural room schedule but doesn't show the air change rate, HEPA filter placement, and pressure differential needed to hit that class on the mechanical sheets is making a claim the drawings haven't backed up. That gap is exactly what a document review exists to catch before it becomes a commissioning failure — discovered with the room built, finished, and the air balance not matching the number on the door.

## USP 797 and USP 800: Two Compounding Rooms With Opposite Pressure Requirements

Life sciences buildings that include pharmacy compounding space add a coordination risk that's easy to get backward. USP 797 governs sterile, non-hazardous compounding: the buffer room around the compounding hood has to run positive pressure — at least 0.02 inches of water column — with a minimum of 30 air changes per hour and HEPA-filtered supply, keeping outside contamination from migrating in. USP 800 governs hazardous drug compounding, and the requirement inverts: the room has to run negative pressure — 0.01 to 0.03 inches of water column — externally vented, at a minimum of 12 air changes per hour, so contamination is contained and removed rather than kept out. One protects the product from the room; the other protects the room and the people in it from the product.

<div class="mini-report">
  <div class="rh"><span class="title">USP 797 VS. USP 800 — PRESSURE AND VENTILATION</span><span class="meta">what the mechanical drawings have to show for each room type</span></div>
  <div class="mini-row"><span class="k">Room pressure</span><span class="v">Positive (USP 797) vs. negative (USP 800)</span></div>
  <div class="mini-row"><span class="k">Minimum air changes/hour</span><span class="v">30 ACH (797 buffer room) vs. 12 ACH (800)</span></div>
  <div class="mini-row"><span class="k">Exhaust</span><span class="v hot">Recirculated HEPA-filtered supply (797) vs. externally vented (800)</span></div>
  <div class="mini-row"><span class="k">Design intent</span><span class="v">Product protection vs. hazard containment</span></div>
</div>

Because both room types often sit in the same pharmacy suite, a document review has to confirm which pressure regime applies to which room on the actual mechanical drawings — not just on the pharmacy layout — and that the ductwork serving a USP 800 negative-pressure room isn't sharing a return path with a USP 797 positive-pressure buffer room next door. A mechanical set that reverses which room is positive and which is negative, or routes both off a shared air handler without independent control, is a finding that belongs on a findings report before the ductwork is fabricated, not after.

## Biocontainment: Where a Pressure Cascade Has to Survive a Fan Failure

Biosafety level containment labs — BSL-2 and BSL-3 space in particular — push the same pressure-cascade logic further, because the requirement isn't just a steady-state number, it's a requirement that the direction of airflow can't reverse even when equipment fails. The CDC/NIH Biosafety in Microbiological and Biomedical Laboratories manual (BMBL, 6th edition) requires BSL-3 space to run a minimum of 6 air changes per hour with directional airflow, moving from clean, non-laboratory areas into the lab — and requires the air handling system to be designed so that under failure conditions, airflow does not reverse. The NIH Design Requirements Manual takes that further and calls for N+1 redundancy on the critical components that maintain the cascade: air handlers, exhaust fans, and HEPA filters, so a single equipment failure doesn't turn a negative-pressure lab positive.

That redundancy requirement is a document review question, not a commissioning question, because it has to be visible in the mechanical design before a single fan is installed: are the exhaust fans shown as a redundant N+1 pair or a single unit, is there a control sequence that shuts down supply air if exhaust fails rather than letting the room go positive, and does the airlock or anteroom between the corridor and the lab have an interlock that keeps both doors from opening at once. A review that only confirms the BSL classification is labeled correctly on the life-safety plan, without checking whether the mechanical system was actually designed to hold that classification through a failure scenario, has answered the easy half of the question.

## What a Life Sciences Document Review Adds to a Standard Scope

The disciplines being checked don't change for a life sciences building — it's still drawings against specs, mechanical against structural, one sheet against another. What changes is the number of performance claims embedded in those drawings that have to be traced to a specific system, not taken on the labeled classification alone. A [checklist covering MEP and structural interface points](/blog/mep-structural-interface-points-fail-most-often/) already treats shaft routing and utility coordination as places where a set fails quietly; a cleanroom or containment set adds pressure cascades, redundant exhaust, and airlock interlocks to that same list of places a document review has to trace room by room rather than trust the schedule.

<div class="takeaways">
  <h3>Key takeaways</h3>
  <ul>
    <li>An ISO cleanroom class or BSL containment level on the room schedule is a performance claim — confirm the mechanical drawings show the air change rate, filtration, and pressure cascade actually needed to hit it, not just the label.</li>
    <li>USP 797 (sterile, non-hazardous) compounding rooms run positive pressure; USP 800 (hazardous drug) rooms run negative and externally vented — verify which regime applies to which room on the mechanical set, especially where both sit in the same suite.</li>
    <li>BSL-3 containment requires directional airflow that can't reverse under failure — check for N+1 redundant exhaust fans and a control sequence that shuts down supply if exhaust fails, not just a correctly labeled life-safety plan.</li>
    <li>Airlocks and anterooms between corridor and containment space need a door interlock preventing both from opening simultaneously — confirm it's shown in the control sequence, not assumed from the floor plan.</li>
    <li>A pressure cascade shared across rooms with different classifications (or opposite pressure requirements) on one air handler without independent control is a coordination finding, not a design preference.</li>
  </ul>
</div>

## Frequently Asked Questions

### What is ISO 14644-1 and why does it matter for a document review?

ISO 14644-1 defines nine cleanroom classes, from ISO Class 1 to ISO Class 9, based on maximum allowable particle counts in the air. Life sciences buildings typically use Classes 5, 7, and 8. A document review should confirm the mechanical drawings show the air change rate, HEPA filtration, and pressure cascade needed to actually achieve the ISO class assigned on the room schedule, not just that the room is labeled with that class.

### What's the difference between USP 797 and USP 800 compounding rooms?

USP 797 governs sterile, non-hazardous compounding and requires positive pressure with HEPA-filtered supply air to keep contamination out and protect the product. USP 800 governs hazardous drug compounding and requires negative pressure with external venting to contain and remove contamination and protect the people in the room. The two requirements are opposites, which makes a mechanical set that mixes them up on adjacent rooms in the same suite a common coordination failure.

### Does a document review check whether a BSL-3 lab's HVAC system is redundant?

It should. The NIH Design Requirements Manual calls for N+1 redundancy on critical components — air handlers, exhaust fans, and HEPA filters — in BSL-3 and higher containment space, so a single equipment failure doesn't reverse the room's negative pressure. A document review should confirm the mechanical drawings show that redundancy and the control sequence that keeps airflow directional even if one exhaust fan fails, not just the BSL classification on the life-safety plan.

### Why can't a life sciences building rely on the room schedule alone to confirm cleanroom or containment compliance?

Because the room schedule states a classification without proving the mechanical system was designed to deliver it. The air change rate, filtration, and pressure differential that actually produce an ISO class or BSL containment level live on the mechanical drawings and control sequences, not the architectural room-finish schedule — and those are the sheets a document review has to trace the claim through.

### Do airlocks between containment space and the corridor need anything shown beyond the floor plan?

Yes. BMBL guidance calls for controlled, directional airflow and interlocked doors between an airlock or anteroom and the containment space it protects, so both doors can't open at the same time and break the pressure cascade. A document review should confirm that interlock appears in the control sequence, not just as two doors drawn on the floor plan.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What is ISO 14644-1 and why does it matter for a document review?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "ISO 14644-1 defines nine cleanroom classes, from ISO Class 1 to ISO Class 9, based on maximum allowable particle counts in the air. Life sciences buildings typically use Classes 5, 7, and 8. A document review should confirm the mechanical drawings show the air change rate, HEPA filtration, and pressure cascade needed to actually achieve the ISO class assigned on the room schedule, not just that the room is labeled with that class."
      }
    },
    {
      "@type": "Question",
      "name": "What's the difference between USP 797 and USP 800 compounding rooms?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "USP 797 governs sterile, non-hazardous compounding and requires positive pressure with HEPA-filtered supply air to keep contamination out and protect the product. USP 800 governs hazardous drug compounding and requires negative pressure with external venting to contain and remove contamination and protect the people in the room. The two requirements are opposites, which makes a mechanical set that mixes them up on adjacent rooms in the same suite a common coordination failure."
      }
    },
    {
      "@type": "Question",
      "name": "Does a document review check whether a BSL-3 lab's HVAC system is redundant?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "It should. The NIH Design Requirements Manual calls for N+1 redundancy on critical components, including air handlers, exhaust fans, and HEPA filters, in BSL-3 and higher containment space, so a single equipment failure doesn't reverse the room's negative pressure. A document review should confirm the mechanical drawings show that redundancy and the control sequence that keeps airflow directional even if one exhaust fan fails, not just the BSL classification on the life-safety plan."
      }
    },
    {
      "@type": "Question",
      "name": "Why can't a life sciences building rely on the room schedule alone to confirm cleanroom or containment compliance?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Because the room schedule states a classification without proving the mechanical system was designed to deliver it. The air change rate, filtration, and pressure differential that actually produce an ISO class or BSL containment level live on the mechanical drawings and control sequences, not the architectural room-finish schedule, and those are the sheets a document review has to trace the claim through."
      }
    },
    {
      "@type": "Question",
      "name": "Do airlocks between containment space and the corridor need anything shown beyond the floor plan?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. BMBL guidance calls for controlled, directional airflow and interlocked doors between an airlock or anteroom and the containment space it protects, so both doors can't open at the same time and break the pressure cascade. A document review should confirm that interlock appears in the control sequence, not just as two doors drawn on the floor plan."
      }
    }
  ]
}
</script>
