---
title: "MEP/Structural Coordination Conflicts in High-Rise Residential: Where Shaft and Riser Stacking Fails"
slug: mep-structural-conflicts-high-rise-residential-shaft-riser-stacking
date: 2026-09-29
description: "MEP/structural drawing coordination conflicts in high-rise residential cluster where shafts and risers must stack floor after floor. Here is where the stack breaks."
deck: "A residential tower asks every riser, shaft, and stack to line up across dozens of floors. The stacking logic is simple. The drawings that have to prove it rarely are."
tags: [Coordination, MEP, Structural, Multifamily]
---

!lede In a high-rise residential tower, MEP/structural drawing coordination conflicts rarely start as dramatic clashes. They start as a shaft that is a few inches short, a riser that shifts sideways at a transfer level, or a column that lands where a stack was supposed to run. Each is small on paper. Each repeats on every floor it touches.

This post looks at one narrow question: where does shaft and riser stacking actually fail on a high-rise residential set, and what can a reviewer check on the drawings before the first shaft wall is framed?

## Why Stacking Is the Core Coordination Problem in a Residential Tower

A residential tower repeats a unit layout. Kitchens and bathrooms sit back to back, and units stack directly above each other so that plumbing, exhaust, and electrical can run vertically through a small number of shafts. That is efficient, and it is also unforgiving. A vertical path has to be clear from the lowest floor it serves to the highest, and every discipline draws its piece of that path on its own sheets.

The architect draws the shaft. The structural engineer draws the columns, shear walls, and slab edges. The mechanical, plumbing, electrical, and fire protection engineers each draw what runs through it. A shaft is coordinated only when all of those drawings agree on the same footprint, on every floor, at the same time. On a typical set they are produced by different firms on different schedules.

For the broader picture of where structural-versus-MEP conflicts originate, see [where coordination conflicts originate on a set](/blog/structural-vs-mep-where-coordination-conflicts-originate/). This post narrows it to the tower's vertical distribution.

<div class="callout">
  <div class="cl-label">Worth knowing</div>
  <p>A conflict that lives in the typical floor plate does not happen once. It repeats on every floor built from that plate. The cheapest place to catch it is before the plate becomes the template.</p>
</div>

## The Five Places Shaft and Riser Stacking Fails

### 1. Shaft size versus what is actually routed through it

The shaft is often drawn early, at a size set by a schematic-level allowance. The systems that go into it keep growing: a larger plumbing stack after fixture counts change, a bigger exhaust riser, added electrical or low-voltage pathways, a fire-rated enclosure that eats interior dimension. The shaft outline on the architectural plan can stay frozen while the contents outgrow it. A reviewer compares the shaft footprint against the sum of what each discipline shows inside it, including clearances for insulation, hangers, and access.

### 2. Risers versus columns and shear walls

Shafts want the same locations as structure. Cores and corners are where the structural engineer wants shear walls, and where MEP wants shafts. When the structural set is revised late, a wall thickens or a column moves, and the shaft footprint on the MEP and architectural sheets is not always updated to match. The stack still looks continuous on each discipline's own drawing. It only fails when the sheets are laid over each other.

### 3. Transfer levels and podium interfaces

Many residential towers sit on a podium of parking or retail, with a transfer slab or transfer beams where the unit grid above stops matching the column grid below. Risers that stack cleanly through the residential floors have to jog, offset, or drop through the transfer structure, where member depth and reinforcing leave little room to move. The stack that was continuous for twenty floors is discontinuous at exactly the level where structure is least flexible. For the podium-specific version of this, see [catching design errors in multifamily podium construction](/blog/catching-design-errors-before-construction-multifamily-podium/).

### 4. Slab penetrations, sleeves, and openings

Every riser that crosses a floor needs an opening or sleeve in the slab. Structural drawings show the openings they were told about. If a plumbing stack moves by a foot in a later revision, the sleeve location on the structural set may not follow, and the slab is placed with the opening in the wrong spot. Post-tensioned slabs raise the stakes, since cutting or coring after placement has to avoid tendons, so openings need to be resolved on the drawings before the pour.

### 5. Fire-rated shaft enclosures and penetrations

Rated shaft walls run the full height of the stack, and the penetrations through them are a documentation issue as much as a physical one. The architectural sheets show the rated enclosure. The MEP sheets show what passes through. Whether the assembly and the penetration firestopping details agree is something that only shows up when both are read together. Fire-rated penetration gaps are one of the [interface points that fail most often](/blog/mep-structural-interface-points-fail-most-often/).

<div class="mini-report">
  <div class="rh"><span class="title">SHAFT STACKING CHECKS</span><span class="meta">what a reviewer compares across sheets</span></div>
  <div class="mini-row"><span class="k">Shaft footprint</span><span class="v">Architectural outline vs. sum of all systems inside it</span></div>
  <div class="mini-row"><span class="k">Structure at the shaft</span><span class="v">Columns and shear walls vs. shaft edges, every floor</span></div>
  <div class="mini-row"><span class="k">Transfer level</span><span class="v hot">Riser offsets vs. transfer member depth</span></div>
  <div class="mini-row"><span class="k">Slab openings</span><span class="v">Structural sleeve locations vs. current riser locations</span></div>
  <div class="mini-row"><span class="k">Rated enclosure</span><span class="v">Shaft wall assembly vs. penetration details</span></div>
</div>

## Why These Conflicts Survive Discipline-by-Discipline QC

Each of these failures passes a single-discipline check. The architect's plan shows a clean shaft. The structural plan shows clean columns. The plumbing riser diagram shows a clean stack. Every sheet is internally consistent. The conflict lives in the space between the sheets, and that is where a coordination review has to look. It is why a set can pass its own QC and still not be coordinated, a theme covered in [why "it passed QA/QC" doesn't mean the set is coordinated](/blog/qa-qc-passed-doesnt-mean-set-coordinated/).

BIM clash detection helps with physical overlaps in the model, but it does not read the notes, schedules, and rated assembly details where several of the failures above live. What it catches and misses is covered in [BIM clash detection: what it catches and misses](/blog/bim-clash-detection-what-it-catches-and-misses/).

## How to Review a Stack Before It Is Built

A practical sequence for a high-rise residential set:

1. **Pick the typical floor first.** Confirm every shaft on the typical plate against all disciplines before the plate repeats.
2. **Trace each stack top to bottom.** Follow each riser from the roof to the lowest level it serves, noting every floor where its location or size changes.
3. **Overlay structure on the shafts.** Lay current structural revisions over the shaft footprints, not the revisions that were current when the shafts were drawn.
4. **Isolate the transfer level.** Give the transfer slab or beams their own pass, since it is where continuous stacks are forced to jog.
5. **Reconcile slab openings against risers.** Match structural sleeve and opening locations to the latest MEP riser drawings.
6. **Read the rated assemblies with the penetrations.** Check shaft wall types against firestopping details.

<div class="takeaways">
  <h3>Key takeaways</h3>
  <ul>
    <li>Shaft and riser stacking fails between disciplines, not within one, so single-discipline QC tends to pass it.</li>
    <li>The typical floor plate is the highest-leverage review target, because an error in it repeats on every floor.</li>
    <li>Transfer levels and slab openings are the two places a continuous stack is most likely to break.</li>
    <li>Late structural revisions are a common source of drift, since shaft footprints on other sheets do not always follow.</li>
  </ul>
</div>

## Frequently Asked Questions

### What is shaft and riser stacking in a high-rise?

Stacking is the practice of aligning shafts, plumbing stacks, exhaust risers, and electrical pathways vertically from floor to floor so systems can run straight through the building. It depends on every discipline drawing the same path in the same place on every level.

### Why do MEP and structural conflicts happen so often in residential towers?

Shafts and structural elements compete for the same core and corner locations, and the two are drawn by different firms on different timelines. A late change to either one can leave the other set out of date without any single sheet looking wrong.

### Where in a high-rise residential set should a coordination review focus first?

Start with the typical floor plate, because errors there repeat on every floor. Then focus on the transfer level between the podium and the residential floors, where continuous risers are forced to offset around structure.

### Is BIM clash detection enough to catch riser stacking problems?

It catches physical overlaps in the model, but not every failure sits in the model. Slab opening locations, rated assembly details, and notes on different sheets can disagree without any geometric clash. A cross-discipline document review covers those.

<script type="application/ld+json">
{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
{"@type":"Question","name":"What is shaft and riser stacking in a high-rise?","acceptedAnswer":{"@type":"Answer","text":"Stacking is the practice of aligning shafts, plumbing stacks, exhaust risers, and electrical pathways vertically from floor to floor so systems can run straight through the building. It depends on every discipline drawing the same path in the same place on every level."}},
{"@type":"Question","name":"Why do MEP and structural conflicts happen so often in residential towers?","acceptedAnswer":{"@type":"Answer","text":"Shafts and structural elements compete for the same core and corner locations, and the two are drawn by different firms on different timelines. A late change to either one can leave the other set out of date without any single sheet looking wrong."}},
{"@type":"Question","name":"Where in a high-rise residential set should a coordination review focus first?","acceptedAnswer":{"@type":"Answer","text":"Start with the typical floor plate, because errors there repeat on every floor. Then focus on the transfer level between the podium and the residential floors, where continuous risers are forced to offset around structure."}},
{"@type":"Question","name":"Is BIM clash detection enough to catch riser stacking problems?","acceptedAnswer":{"@type":"Answer","text":"It catches physical overlaps in the model, but not every failure sits in the model. Slab opening locations, rated assembly details, and notes on different sheets can disagree without any geometric clash. A cross-discipline document review covers those."}}
]}
</script>
