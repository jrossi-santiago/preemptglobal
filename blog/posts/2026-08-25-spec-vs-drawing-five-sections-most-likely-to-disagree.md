---
title: "Spec vs. Drawing Conflicts: The Five Sections Most Likely to Disagree With the Plans"
slug: spec-vs-drawing-five-sections-most-likely-to-disagree
date: 2026-08-25
description: "Which CSI spec sections most often contradict the drawings — openings, finishes, fire-rated assemblies, mechanical equipment, and structural reinforcing — and why each one drifts from the plans in a predictable way."
deck: "Not every spec section is equally likely to fight the drawings. Five of them account for most of the contradictions a document review actually finds — and each drifts out of sync for its own specific reason."
tags: [Document Review, Coordination, Bid Documents]
---

!lede Ask a reviewer which spec section is most likely to contradict the drawings on a given set, and they won't say "it varies." A handful of divisions account for most of the real contradictions, and they're not random — each one has a specific, repeatable reason its section drifts out of sync with the plans. Knowing which five to check first is the difference between a document review that finds the expensive conflicts and one that just skims the whole set hoping to get lucky.

## Why conflicts cluster instead of spreading evenly

A drawing set and a spec book aren't produced by the same hand at the same time. The drawings are geometry — where things sit, how big they are, how they connect. The specs are performance and product requirements — what something is made of, how it's installed, what standard it has to meet. Different disciplines, sometimes different firms, maintain each one on its own schedule, and both have to describe the same physical thing without ever directly checking against each other until someone reads them side by side.

That's why conflicts aren't spread evenly across a 50-division spec book. They concentrate wherever a detail gets revised late, gets value-engineered on one document without a matching update on the other, or depends on a schedule that has to stay in sync with a drawing schedule maintained by someone else. Five sections hit that pattern more than any others.

## 1. Openings (Division 08) — the schedule that gets value-engineered alone

Door and hardware schedules are the textbook case, because the failure mode is so specific: late in design, someone swaps a hardware set to hit a budget number, edits Division 08, and the door schedule on the architectural sheets — a different file, on a different sheet, often touched by a different person — never gets the matching revision. The drawing and the spec each describe a real, buildable hardware set. They just don't describe the same one.

<div class="callout">
  <div class="cl-label">Worth knowing</div>
  <p>The fix for a Division 08 conflict isn't picking a winner — it's catching that the schedule and the spec were edited independently in the first place, before a submittal reviewer or a crew in the field has to guess which version is current.</p>
</div>

## 2. Finishes (Division 09) — schedules that outlive the assembly beneath them

Division 09 fails the same way Division 08 does, for the same structural reason: a finish schedule on the drawings and a spec section describing the same flooring, wall finish, or ceiling system, maintained on separate tracks. The added wrinkle with finishes is that the conflict often isn't just cosmetic — a floor finish schedule can call for an assembly whose actual thickness doesn't match the slab depression the structural drawings built in for it, which turns a finish selection into a framing problem discovered only once the substrate is already poured.

## 3. Fire-rated assemblies (Division 07 and structural) — a tested system, not a description

Fire-rated wall and floor assemblies are a different kind of conflict entirely, because a UL design number isn't a general description — it's a tested system with a fixed list of components: specific studs, specific board type and thickness, specific fasteners, specific spacing. If the drawings call out a wall type that doesn't match the exact UL design referenced in the spec — a Type X board dropped to plain 5/8-inch, a load-bearing U-design substituted where the drawings show a non-load-bearing partition, a rated wall assembly shown without its matching head-of-wall joint system — the assembly on paper isn't a buildable version of the listed design. An inspector or AHJ checking the installed work against the listed design, not the drawn intent, is exactly why this category of conflict gets expensive to fix once it's built rather than caught on paper.

## 4. Mechanical equipment (Division 23) — schedules that assume clearance nobody drew

Mechanical equipment schedules are prone to a specific mismatch: the spec's basis-of-design equipment requires a service clearance — around an air handler, a rooftop unit, a piece of gear that needs room to pull a coil or swing a door — that the architectural or structural drawings never allocated space for. The equipment on the schedule and the equipment room on the drawings are each internally consistent; they just weren't checked against each other's real-world footprint. The same pattern shows up when a specified basis-of-design product goes out of production or hits a long lead time and a substitution changes a footprint or connection point that the drawings still show as the original unit — a coordination gap covered in more depth in [where coordination conflicts actually originate between structural and MEP](/blog/structural-vs-mep-where-coordination-conflicts-originate/).

## 5. Structural reinforcing and masonry (Divisions 03 and 04) — detail vs. requirement

The last recurring pattern is a structural drawing that shows a wall or slab detail without the reinforcing the corresponding spec section requires — a masonry wall drawn without visible rebar callouts while Division 04 specifies bar size and spacing at that wall type, or a concrete detail that's missing a reinforcing schedule reference the spec assumes is coordinated elsewhere. These are quieter than a hardware mismatch because nothing about the drawing looks obviously wrong on its own — the omission only shows up when someone checks the drawn detail against the spec's actual requirement line by line.

<div class="mini-report">
  <div class="rh"><span class="title">WHY EACH SECTION DRIFTS</span><span class="meta">Root cause by division</span></div>
  <div class="mini-row"><span class="k">Div. 08 — Openings</span><span class="v">Hardware set value-engineered in spec, schedule not updated</span></div>
  <div class="mini-row"><span class="k">Div. 09 — Finishes</span><span class="v">Finish schedule outlives the substrate/assembly it sits on</span></div>
  <div class="mini-row"><span class="k">Div. 07 / Structural — Fire-rated assemblies</span><span class="v hot">Drawn wall type doesn't match the listed UL design exactly</span></div>
  <div class="mini-row"><span class="k">Div. 23 — Mechanical equipment</span><span class="v">Basis-of-design clearance or footprint not reflected on drawings</span></div>
  <div class="mini-row"><span class="k">Div. 03 / 04 — Structural, masonry</span><span class="v">Reinforcing requirement in spec not shown in the drawn detail</span></div>
</div>

## What these five have in common

Every one of these is a case where two documents, maintained on separate tracks by people who trust the other document is already correct, describe the same physical thing without anyone actually placing them side by side. None of it is bad faith or carelessness in the way a single obvious drafting error would be — it's what happens by default when a spec book and a 200-sheet drawing set are each internally consistent but never cross-checked against each other as a matched pair. [Anatomy of a findings report](/blog/anatomy-of-a-findings-report-third-party-plan-review/) covers what that cross-check looks like in practice: every one of these conflict types tied to a specific sheet and spec section, priced, and fixed before the set goes out to bid rather than surfacing as an RFI once a crew is standing in front of the contradiction. [The broader field guide to spec vs. drawing conflicts](/blog/spec-vs-drawing-conflicts/) covers who actually has the authority to resolve one of these once it reaches the field — this piece is about knowing where to look before it gets that far.

<div class="takeaways">
  <h3>Key takeaways</h3>
  <ul>
    <li>Spec-drawing conflicts cluster in five predictable divisions rather than spreading evenly across the spec book.</li>
    <li>Openings and finishes fail the same way: a schedule gets edited independently of the spec section describing the same item.</li>
    <li>Fire-rated assemblies fail differently — a UL design number is a fixed tested system, and any drawn deviation from its exact components breaks the listing.</li>
    <li>Mechanical equipment conflicts usually trace back to a clearance or footprint the drawings never allocated space for.</li>
    <li>Structural and masonry reinforcing conflicts are the quietest, because the drawn detail looks fine until it's checked line by line against the spec's actual requirement.</li>
  </ul>
</div>

Knowing which five sections to check first doesn't replace checking the rest of the set — it just means a reviewer with limited time knows exactly where to start, because these are the places a spec book and a drawing set are most likely to have drifted apart without anyone noticing.

## Frequently Asked Questions

### Which spec divisions have the most spec vs. drawing conflicts?

Openings (Division 08), Finishes (Division 09), fire-rated assemblies (Division 07 combined with structural drawings), mechanical equipment (Division 23), and structural reinforcing and masonry (Divisions 03 and 04) account for most of the recurring contradictions between specs and drawings, because each has a specific, repeatable reason its section tends to drift out of sync with the plans.

### Why do door hardware schedules conflict with the specifications so often?

Hardware sets frequently get value-engineered directly in the Division 08 spec section during a late-stage cost review, but the door schedule on the drawings — a separate file maintained on a different sheet, often by a different person — doesn't always get the matching update, leaving two internally consistent but contradictory descriptions of the same door.

### What makes fire-rated assembly conflicts different from other spec vs. drawing issues?

A UL fire-rated design number represents a specific tested system with a fixed set of components — exact stud type, board type and thickness, fasteners, and spacing. If the drawings show a wall assembly that doesn't match every component of the listed design referenced in the spec, the assembly isn't a buildable version of what was actually tested, which is a stricter failure than a typical schedule mismatch.

### How do mechanical equipment schedules end up conflicting with the drawings?

The equipment specified in Division 23 often requires a service clearance for maintenance access that the architectural or structural drawings never allocated space for, or a basis-of-design product gets substituted for one with a different footprint or connection point that the drawings still show as the original unit.

### How can these conflicts be caught before they reach the field as an RFI?

A cross-discipline document review that checks each of these five conflict-prone divisions against its corresponding drawings — rather than reading the spec book and the drawing set independently — catches the contradiction while it's still a correction in the issued set, producing a sheet-located, priced finding instead of a stopped crew and an RFI.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Which spec divisions have the most spec vs. drawing conflicts?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Openings (Division 08), Finishes (Division 09), fire-rated assemblies (Division 07 combined with structural drawings), mechanical equipment (Division 23), and structural reinforcing and masonry (Divisions 03 and 04) account for most of the recurring contradictions between specs and drawings, because each has a specific, repeatable reason its section tends to drift out of sync with the plans."
      }
    },
    {
      "@type": "Question",
      "name": "Why do door hardware schedules conflict with the specifications so often?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Hardware sets frequently get value-engineered directly in the Division 08 spec section during a late-stage cost review, but the door schedule on the drawings, a separate file maintained on a different sheet often by a different person, doesn't always get the matching update, leaving two internally consistent but contradictory descriptions of the same door."
      }
    },
    {
      "@type": "Question",
      "name": "What makes fire-rated assembly conflicts different from other spec vs. drawing issues?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "A UL fire-rated design number represents a specific tested system with a fixed set of components: exact stud type, board type and thickness, fasteners, and spacing. If the drawings show a wall assembly that doesn't match every component of the listed design referenced in the spec, the assembly isn't a buildable version of what was actually tested, which is a stricter failure than a typical schedule mismatch."
      }
    },
    {
      "@type": "Question",
      "name": "How do mechanical equipment schedules end up conflicting with the drawings?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The equipment specified in Division 23 often requires a service clearance for maintenance access that the architectural or structural drawings never allocated space for, or a basis-of-design product gets substituted for one with a different footprint or connection point that the drawings still show as the original unit."
      }
    },
    {
      "@type": "Question",
      "name": "How can these conflicts be caught before they reach the field as an RFI?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "A cross-discipline document review that checks each of these five conflict-prone divisions against its corresponding drawings, rather than reading the spec book and the drawing set independently, catches the contradiction while it's still a correction in the issued set, producing a sheet-located, priced finding instead of a stopped crew and an RFI."
      }
    }
  ]
}
</script>
