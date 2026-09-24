---
title: "Spec vs. Drawing Conflicts on Healthcare Projects: Where Equipment Specs and Room Data Sheets Diverge"
slug: spec-vs-drawing-conflicts-healthcare-equipment-room-data-sheets
date: 2026-09-24
description: "On healthcare projects, spec vs drawing conflicts concentrate around equipment specs and room data sheets — the two documents most likely to drift apart before a set goes out to bid."
deck: "A general spec vs. drawing conflict check misses the pattern that's specific to healthcare work: equipment specifications and room data sheets, maintained on separate tracks by separate teams, describing the same room without ever being checked against each other."
tags: [Document Review, Coordination, MEP]
---

!lede Spec vs. drawing conflicts show up on every asset class, but healthcare work has a failure mode most commercial projects don't: a room data sheet and an equipment specification that each describe the same clinical space completely on their own terms, maintained by different people on different schedules, never checked side by side until something doesn't fit in the field. Knowing that this is where the divergence concentrates changes where a pre-bid review needs to look first.

## Why healthcare sets have an extra document to reconcile

A standard commercial set already has to reconcile two documents describing the same physical thing: the drawings (geometry — where something sits, how big it is, how it connects) and the spec book (performance and product requirements — what it's made of, how it's installed, what standard it meets). [The field guide to spec vs. drawing conflicts](/blog/spec-vs-drawing-conflicts/) covers how that basic two-document mismatch plays out and who has authority to resolve it once it reaches the field.

Healthcare work adds a third document into that same reconciliation problem: the room data sheet. A room data sheet catalogs everything a clinical space needs — finishes, fixtures, MEP connections, environmental parameters like temperature, humidity, and pressurization, and the equipment that room is built to hold — room by room, department by department. It's produced early, often by a different team than the one writing Division 11 equipment specs or coordinating the architectural and MEP drawings, and it's meant to be the single source of truth for what a room requires. In practice, it's a third independently maintained description of the same space, which means there are now three documents that all have to agree instead of two.

## Where the divergence actually shows up

### Equipment specs written before the equipment is selected

Division 11 healthcare equipment — sterilization equipment, OR lighting, scrub sinks, narcotics lockers, imaging systems, lab equipment like fume hoods and controlled environment cabinets — routinely needs its utility requirements locked in early, because medical gas lines, dedicated electrical circuits, and structural accommodations have to be built into the drawings well before the equipment itself is procured. That timing pressure is exactly where the conflict originates: a room data sheet gets written against a preliminary or basis-of-design piece of equipment, the drawings get coordinated and issued against that same assumption, and then the actual equipment selection changes late — a different manufacturer, a different footprint, a different utility connection point — without every document that referenced the earlier assumption getting updated in lockstep. The room data sheet, the equipment spec, and the drawings can each be internally consistent and still describe three slightly different rooms.

<div class="callout">
  <div class="cl-label">Worth knowing</div>
  <p>The fix isn't picking which of the three documents is "right." It's confirming, before bid, which equipment selections in the room data sheets are actually final versus still a placeholder the drawings were coordinated against — because a placeholder that never gets flagged as a placeholder is exactly what turns into a field conflict.</p>
</div>

### Room data sheets that outlive a drawing revision

A room data sheet is meant to stay synchronized with the drawings, models, and specs it describes as those documents evolve — but it's a separate deliverable, usually maintained in its own database or spreadsheet rather than inside the CAD or BIM model itself. When a room gets revised late in design — a door swing changes, a fixed casework layout shifts, a mechanical diffuser moves — the drawing update doesn't automatically propagate back into the room data sheet's finish schedule, clearance notes, or equipment list. The result is the same pattern Division 08 hardware schedules show on a standard commercial set: two documents, each edited correctly by the person responsible for it, that quietly stop agreeing with each other because neither editor is checking the other's document as part of their own revision. [The five spec sections most likely to disagree with the drawings](/blog/spec-vs-drawing-five-sections-most-likely-to-disagree/) covers that same failure pattern in a non-healthcare context — the mechanism is identical, healthcare work just adds a third document that can silently fall out of sync.

### Utility and clearance requirements that don't match what got drawn

Division 11 equipment often carries specific clearance, utility, and structural requirements that exist to satisfy a code or a manufacturer's installation standard, not just a room layout preference — a fixed x-ray unit's structural mounting requirement, a sterilizer's utility rough-in, a medical gas outlet's required clearance from a headwall. Coordinating vendors, contractors, and equipment planners are all supposed to confirm that connections match flow meters, suction regulators, and structural provisions, but that confirmation loop runs on its own schedule, separate from the architectural and MEP drawing coordination. When it lags, the room data sheet and the equipment spec can each correctly state a requirement that the issued drawings never actually built in — a clearance nobody drew, a utility rough-in sized for the wrong connection.

<div class="mini-report">
  <div class="rh"><span class="title">WHERE HEALTHCARE SPEC VS. DRAWING CONFLICTS CONCENTRATE</span><span class="meta">Three documents, one room</span></div>
  <div class="mini-row"><span class="k">Room data sheet</span><span class="v">Early source of truth for finishes, MEP connections, equipment — maintained separately from the model</span></div>
  <div class="mini-row"><span class="k">Equipment spec (Division 11)</span><span class="v hot">Often locked before equipment is finalized — utility and clearance requirements change with late substitutions</span></div>
  <div class="mini-row"><span class="k">Drawings (architectural + MEP)</span><span class="v">Coordinated against whichever version of the equipment assumption was current at issue</span></div>
</div>

## Why this matters more on healthcare work than a standard commercial set

On a typical commercial build, a spec vs. drawing conflict is a correction — expensive if it's found in the field, cheap if it's caught before bid, but rarely a code or life-safety issue on its own. On healthcare work, the FGI Guidelines for Design and Construction of Hospitals and Outpatient Facilities set minimum requirements for space, infection prevention, and MEP systems that are frequently more restrictive than general building code, and where a discrepancy exists, the more stringent standard applies. A room data sheet, equipment spec, and drawing set that disagree with each other on a clinical space aren't just internally inconsistent — one of those three descriptions may not actually satisfy the FGI requirement the room is supposed to meet, which raises the stakes of catching the mismatch on paper rather than during inspection or commissioning. [Change order risk mitigation on healthcare and life sciences work](/blog/change-order-risk-mitigation-healthcare-life-sciences/) covers the broader pattern of why exposure concentrates differently on this asset class — equipment lead times and infection control requirements that don't show up on a standard commercial set at all.

## What a pre-bid review checks for specifically

Catching this before bid means checking the room data sheet, the equipment spec, and the drawings against each other as a matched set for every clinical space — not reading each document independently and assuming agreement. That means confirming which equipment listed on a room data sheet is a finalized selection versus a basis-of-design placeholder, verifying that utility rough-ins and clearances shown on the MEP drawings match what the equipment spec actually requires rather than an earlier version of it, and flagging any room where the finish or dimensional information on the room data sheet doesn't match what the current drawing revision shows. None of that is a different skill from a standard spec vs. drawing check — it's the same cross-check, applied to three documents instead of two, on the spaces where healthcare work concentrates the highest equipment and utility complexity.

<div class="takeaways">
  <h3>Key takeaways</h3>
  <ul>
    <li>Healthcare projects add a third document — the room data sheet — to the standard two-document spec vs. drawing reconciliation problem.</li>
    <li>Division 11 equipment specs are often locked before equipment is finalized, so a late substitution can leave the room data sheet, the spec, and the drawings each describing a slightly different room.</li>
    <li>Room data sheets are typically maintained outside the drawing model, so a late drawing revision doesn't automatically propagate back into the room data sheet's finish or equipment listing.</li>
    <li>FGI Guidelines often set more restrictive requirements than general code for clinical spaces, which raises the stakes of a three-document mismatch beyond a routine field correction.</li>
    <li>A pre-bid review needs to check the room data sheet, equipment spec, and drawings against each other as a matched set, not read each in isolation.</li>
  </ul>
</div>

The standard spec vs. drawing conflict check still applies to healthcare work — it just isn't sufficient on its own. A review that only compares the spec book to the drawings will miss a room data sheet that fell out of sync with both, which on a clinical space isn't a cosmetic gap. It's a room that may not be built to hold the equipment, or meet the guideline, it was designed for.

## Frequently Asked Questions

### What's different about spec vs. drawing conflicts on healthcare projects?

Healthcare projects add a third document — the room data sheet — to the usual two-way reconciliation between the spec book and the drawings. Because the room data sheet, the equipment specification, and the drawings are typically maintained by different teams on different schedules, all three can be internally consistent while describing three slightly different versions of the same clinical space.

### Why do equipment specs conflict with room data sheets on hospital projects?

Division 11 equipment often needs its utility and clearance requirements locked into the drawings before the actual equipment is finalized, since medical gas, electrical, and structural accommodations take time to build in. When the equipment selection changes later — a different manufacturer or footprint — the room data sheet, the spec, and the drawings don't always get updated together.

### What is a room data sheet, and why does it matter for document review?

A room data sheet is a room-by-room record of everything a clinical space requires — finishes, MEP connections, environmental parameters, and equipment — usually maintained separately from the drawing model or BIM file. Because it's a separate deliverable, a late drawing revision doesn't automatically update the room data sheet, which means it can drift out of sync with the current drawings without anyone flagging the mismatch until the room is built.

### Do FGI Guidelines make these conflicts higher-stakes than on a standard commercial project?

Yes. FGI Guidelines for hospitals and outpatient facilities frequently set space, infection prevention, and MEP requirements that are more restrictive than general building code, and the more stringent standard applies where the two differ. A three-document mismatch on a clinical space can mean one of those documents doesn't actually satisfy the applicable FGI requirement, not just that the documents disagree with each other.

### How can these conflicts be caught before they reach the field?

A pre-bid document review that checks the room data sheet, the equipment specification, and the drawings against each other for every clinical space — rather than comparing the spec book to the drawings alone — catches a stale equipment assumption or an unsynchronized room data sheet while it's still a correction in the issued set, instead of a discovery made during equipment installation or commissioning.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What's different about spec vs. drawing conflicts on healthcare projects?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Healthcare projects add a third document, the room data sheet, to the usual two-way reconciliation between the spec book and the drawings. Because the room data sheet, the equipment specification, and the drawings are typically maintained by different teams on different schedules, all three can be internally consistent while describing three slightly different versions of the same clinical space."
      }
    },
    {
      "@type": "Question",
      "name": "Why do equipment specs conflict with room data sheets on hospital projects?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Division 11 equipment often needs its utility and clearance requirements locked into the drawings before the actual equipment is finalized, since medical gas, electrical, and structural accommodations take time to build in. When the equipment selection changes later, a different manufacturer or footprint, the room data sheet, the spec, and the drawings don't always get updated together."
      }
    },
    {
      "@type": "Question",
      "name": "What is a room data sheet, and why does it matter for document review?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "A room data sheet is a room-by-room record of everything a clinical space requires, finishes, MEP connections, environmental parameters, and equipment, usually maintained separately from the drawing model or BIM file. Because it's a separate deliverable, a late drawing revision doesn't automatically update the room data sheet, which means it can drift out of sync with the current drawings without anyone flagging the mismatch until the room is built."
      }
    },
    {
      "@type": "Question",
      "name": "Do FGI Guidelines make these conflicts higher-stakes than on a standard commercial project?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. FGI Guidelines for hospitals and outpatient facilities frequently set space, infection prevention, and MEP requirements that are more restrictive than general building code, and the more stringent standard applies where the two differ. A three-document mismatch on a clinical space can mean one of those documents doesn't actually satisfy the applicable FGI requirement, not just that the documents disagree with each other."
      }
    },
    {
      "@type": "Question",
      "name": "How can these conflicts be caught before they reach the field?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "A pre-bid document review that checks the room data sheet, the equipment specification, and the drawings against each other for every clinical space, rather than comparing the spec book to the drawings alone, catches a stale equipment assumption or an unsynchronized room data sheet while it's still a correction in the issued set, instead of a discovery made during equipment installation or commissioning."
      }
    }
  ]
}
</script>
