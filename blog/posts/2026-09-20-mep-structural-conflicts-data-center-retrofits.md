---
title: "MEP/Structural Coordination Conflicts on Data Center Retrofits: Why Existing Infrastructure Raises the Stakes"
slug: mep-structural-conflicts-data-center-retrofits
date: 2026-09-20
description: "MEP/structural drawing coordination conflicts are already the top clash category on any set. Retrofitting an existing building into a data center stacks new risk on top of that baseline — here's why."
deck: "A data center retrofit inherits two already-elevated risk profiles at once: the coordination load of a MEP-dominant building, and the uncertainty of building against a structure nobody designed for this program. Together they change what a coordination review has to check first."
tags: [Data Centers, MEP, Structural]
---

!lede MEP/structural drawing coordination conflicts are already the most common clash category on any multi-discipline set, and data centers already generate more of that risk than almost any other asset class. A retrofit — converting an existing warehouse, shell office building, or legacy data hall into a modern, high-density facility — doesn't average those two risk factors together. It stacks them, because the retrofit adds a category of conflict neither a new-build data center nor a standard renovation has to solve on its own: MEP and structural systems both being redesigned against a building whose real capacity was never verified against a data center program in the first place.

The retrofit market exists because it's often the faster, cheaper path to capacity. Industry cost analyses put a retrofit at roughly a fifth of new-construction cost per megawatt — a real advantage in a market where utility interconnection queues alone can run 30 to 60-plus weeks for switchgear and generators. The economics are real. So is the coordination problem that comes with them.

## Why a Retrofit Doesn't Just Inherit Data Center Risk — It Compounds It

A ground-up data center is already a MEP-heavy building by design: industry estimates put mechanical, electrical, and plumbing systems at 60-75% of total construction cost, roughly double the 30-40% typical for standard commercial work, because MEP effectively *is* the building at that point. That baseline risk doesn't change on a retrofit. What changes is that the structural and spatial envelope those systems have to fit into wasn't designed for them — it was designed for whatever the building's original use was, often years before a data center program was ever contemplated.

That's the same failure mode we've written about on [renovation and adaptive reuse projects generally](/blog/mep-structural-conflicts-renovation-adaptive-reuse/): two disciplines can draw a fully coordinated set against each other and still conflict with the real building, because the existing-conditions information both sheets were drawn against wasn't accurate to begin with. A data center retrofit runs that same risk, but with a MEP load several times denser than the renovation projects that failure mode is usually discussed against — office-to-residential conversions, adaptive reuse of a warehouse into flex space. Here, the new program isn't just heavier than the old one; it's a different order of magnitude in power density, cooling load, and structural demand than almost anything the building was likely built to carry.

<div class="callout">
  <div class="cl-label">Worth knowing</div>
  <p>Roof and floor structures on a purpose-built data center are typically engineered to carry several times the load of a standard warehouse roof, specifically to support rooftop mechanical plant and raised-access-floor equipment loads. A retrofit candidate building was very likely engineered to none of that — which is why a structural capacity assessment is usually the first item in retrofit due diligence, before layout or equipment selection even begins.</p>
</div>

## The Floor-Loading Problem AI Retrofits Are Creating

The clearest version of this risk right now is happening at the rack level. Rack power density has climbed from roughly 10 kW a few years ago to well over 100 kW for the newest high-density AI hardware platforms — and every kilowatt of added compute density brings proportional weight with it once liquid cooling enters the picture. A fully equipped liquid-cooled rack, coolant manifolds included, can run three to five times heavier than the air-cooled rack it's replacing, and the coolant distribution units that support it can weigh several tons apiece when flooded. Engineering analysis of liquid-cooling retrofits shows the effective floor loading for the same footprint of compute rising from roughly 12-15 kilopascals under traditional air cooling to 20 kilopascals or more under liquid cooling.

<div class="mini-report">
  <div class="rh"><span class="title">WHAT AN AI RETROFIT ADDS TO THE STRUCTURAL LOAD</span><span class="meta">air-cooled vs. liquid-cooled, same footprint</span></div>
  <div class="mini-row"><span class="k">Rack density, several years ago</span><span class="v">~10 kW/rack</span></div>
  <div class="mini-row"><span class="k">Rack density, current high-density AI hardware</span><span class="v hot">100+ kW/rack</span></div>
  <div class="mini-row"><span class="k">Rack weight, liquid-cooled vs. air-cooled</span><span class="v hot">3-5x heavier</span></div>
  <div class="mini-row"><span class="k">Floor loading, air-cooled vs. liquid-cooled (same compute footprint)</span><span class="v">~12-15 kPa → 20+ kPa</span></div>
</div>

None of that weight was in the original building's design load, whatever it was originally built to hold. A raised access floor, a slab designed for warehouse racking, or a floor plate sized for standard office live load each carries a different — and usually lower — rated capacity than a room full of liquid-cooled AI racks and their coolant distribution units requires. That's not a routing conflict between two drawn systems; it's a capacity conflict between the MEP design and a structural element that can't simply be redrawn, which is the same distinction [we've made about renovation risk generally](/blog/mep-structural-conflicts-renovation-adaptive-reuse/) — except here the gap between what the MEP design wants and what the existing structure can carry tends to be far larger, because the retrofit program is usually a bigger jump from the building's original use than a typical office renovation ever asks for.

## What the Existing Building Wasn't Designed to Carry

Floor loading is the most visible version of the problem, but it's not the only one. Three other interfaces carry outsized risk on a data center retrofit specifically because the building predates the program now being asked of it:

- **Rooftop and mezzanine equipment support.** Adding chillers, CRAH units, or backup generation to a roof or mezzanine that was framed for a lighter original load — office mechanical penthouse, warehouse skylights, minimal rooftop equipment — repeats the [rooftop-equipment coordination risk we've written about on large-footprint buildings generally](/blog/mep-structural-conflicts-vertical-vs-horizontal-construction/), but starting from a structure that has less reserve capacity to begin with than a purpose-built industrial shell would.
- **Floor-to-floor and plenum height.** A data center's air- or liquid-distribution systems need clearance that the original building's floor-to-floor height and raised-floor plenum may not provide, and unlike a new-build set where plenum depth is a design input, an existing building's floor-to-floor dimension is fixed. Undersized plenum height is a documented cause of cooling underperformance specifically in facilities retrofitted from a lower-density original design.
- **Electrical service and switchgear space.** The building's original electrical service, transformer vault, and switchgear room were sized for its original occupancy load, not for a data center's power density — and expanding that capacity on an occupied or partially built site runs into the same interconnection queue delays affecting new construction, compounding a schedule that's often already compressed to make the retrofit's cost advantage pencil out.

## Why the As-Built Set Can't Be Taken at Face Value

The same problem that makes renovation coordination harder generally — an existing-conditions survey that doesn't reflect the building's real, current condition — applies here with a specific data center wrinkle: many retrofit candidates are legacy data halls or industrial buildings that have already been modified once, sometimes multiple times, by prior tenants or a prior generation of IT equipment. A structural member that was already loaded up for a previous fit-out, an electrical panel upgraded off-record, or a raised floor whose actual load rating was never re-verified after earlier work — none of that shows up as a clash on a coordinated MEP-versus-structural read unless the existing-conditions information itself gets checked first. Point-cloud laser scanning of the actual building, rather than relying on inherited as-built drawings, is increasingly treated as a prerequisite step precisely because it catches this gap before the mechanical and electrical design teams draw against a version of the building that isn't there anymore.

## The Schedule Pressure Doesn't Ease Up Just Because It's a Retrofit

It's tempting to assume a retrofit, working with an existing building rather than a from-scratch design, gives a project more breathing room to catch this kind of conflict. In practice the opposite is often true. Retrofits are frequently chosen specifically because they're faster to occupy than a ground-up build, which means the same fast-track pressure driving new data center schedules — [design and procurement overlapping, model-freeze dates set to protect long-lead equipment orders](/blog/data-center-constructability-review-consultant/) — applies here too, on top of a structural verification step a new-build project doesn't have to do at all. A team racing to hit an occupancy date has less incentive to slow down and re-verify existing conditions, which is exactly the moment a document-level review that checks both the cross-discipline coordination and the existing-conditions assumptions underneath it earns its keep.

<div class="takeaways">
  <h3>Key takeaways</h3>
  <ul>
    <li>Data center retrofits combine two already-elevated coordination risks: a MEP-dominant building program and an existing structure that wasn't designed for it, rather than averaging the two.</li>
    <li>Rack density has climbed from roughly 10 kW to well over 100 kW on current high-density AI hardware, and liquid-cooled racks can weigh three to five times more than the air-cooled racks they replace — a load most retrofit candidate buildings were never designed to carry.</li>
    <li>Floor loading for the same compute footprint can rise from roughly 12-15 kPa under air cooling to 20+ kPa under liquid cooling, turning a MEP equipment decision into a structural capacity question that the drawings alone won't answer.</li>
    <li>Fixed floor-to-floor height, undersized plenum depth, and undersized original electrical service are all constraints a retrofit inherits from the existing building and can't design around the way a new build can.</li>
    <li>An existing-conditions survey that doesn't reflect the building's real current condition — especially on a site already modified by a prior tenant or earlier IT fit-out — can leave a fully coordinated MEP/structural set still wrong about the building underneath it.</li>
  </ul>
</div>

Retrofitting an existing building into a data center is a sound economic decision on its own terms. But the coordination review has to account for what makes a retrofit different from both a standard renovation and a new-build data center: verifying that the existing structure, floor system, and building envelope can actually carry a MEP program built around today's rack densities, not just checking that the mechanical and electrical drawings agree with each other.

## Frequently Asked Questions

### Are data center retrofits riskier than new-construction data centers from a coordination standpoint?

They carry a different kind of risk, not simply more of the same. A new-build data center's coordination risk comes mostly from how MEP-dense the program is. A retrofit adds a second layer: whether the existing structure, floor system, and building envelope can actually support that MEP program, since none of it was originally designed with a data center's power density or cooling loads in mind.

### Why does liquid cooling make retrofit structural risk worse than it used to be?

Liquid-cooled AI racks, including their coolant distribution units, can weigh three to five times more than the air-cooled racks they replace, and floor loading for the same compute footprint can rise from roughly 12-15 kPa to 20 kPa or more. Most retrofit candidate buildings — former warehouses, office shells, or legacy data halls — weren't structurally designed for that load, which turns an equipment selection decision into a structural capacity question.

### Can a fully coordinated MEP/structural set still be wrong on a retrofit project?

Yes. If the mechanical and structural drawings agree with each other but were both drawn against an existing-conditions survey that doesn't reflect the building's real, current condition — including any undocumented work from a prior tenant or earlier IT fit-out — the set can look coordinated and still conflict with the actual building once construction starts.

### What structural elements are most likely to be undersized on a data center retrofit?

Floor and raised-access-floor loading, roof and mezzanine framing for added mechanical equipment, and the building's original electrical service and switchgear space are the three that most often come in under what a modern data center program requires, because all three were sized for the building's original occupancy rather than for high-density IT and cooling loads.

### Does the fast-track schedule common to data center projects apply to retrofits too?

Yes, often more so. Retrofits are frequently chosen specifically because they're faster to bring online than a ground-up build, which keeps the same design-procurement overlap and long-lead equipment pressure seen on new data center projects — but now stacked on top of an existing-conditions verification step that a new-build project doesn't need to do at all.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Are data center retrofits riskier than new-construction data centers from a coordination standpoint?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "They carry a different kind of risk, not simply more of the same. A new-build data center's coordination risk comes mostly from how MEP-dense the program is. A retrofit adds a second layer: whether the existing structure, floor system, and building envelope can actually support that MEP program, since none of it was originally designed with a data center's power density or cooling loads in mind."
      }
    },
    {
      "@type": "Question",
      "name": "Why does liquid cooling make retrofit structural risk worse than it used to be?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Liquid-cooled AI racks, including their coolant distribution units, can weigh three to five times more than the air-cooled racks they replace, and floor loading for the same compute footprint can rise from roughly 12-15 kPa to 20 kPa or more. Most retrofit candidate buildings, former warehouses, office shells, or legacy data halls, weren't structurally designed for that load, which turns an equipment selection decision into a structural capacity question."
      }
    },
    {
      "@type": "Question",
      "name": "Can a fully coordinated MEP/structural set still be wrong on a retrofit project?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. If the mechanical and structural drawings agree with each other but were both drawn against an existing-conditions survey that doesn't reflect the building's real, current condition, including any undocumented work from a prior tenant or earlier IT fit-out, the set can look coordinated and still conflict with the actual building once construction starts."
      }
    },
    {
      "@type": "Question",
      "name": "What structural elements are most likely to be undersized on a data center retrofit?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Floor and raised-access-floor loading, roof and mezzanine framing for added mechanical equipment, and the building's original electrical service and switchgear space are the three that most often come in under what a modern data center program requires, because all three were sized for the building's original occupancy rather than for high-density IT and cooling loads."
      }
    },
    {
      "@type": "Question",
      "name": "Does the fast-track schedule common to data center projects apply to retrofits too?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes, often more so. Retrofits are frequently chosen specifically because they're faster to bring online than a ground-up build, which keeps the same design-procurement overlap and long-lead equipment pressure seen on new data center projects, but now stacked on top of an existing-conditions verification step that a new-build project doesn't need to do at all."
      }
    }
  ]
}
</script>
