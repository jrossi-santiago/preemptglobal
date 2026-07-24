---
title: "Anatomy of a Findings Report: What a Real Third-Party Plan Review Actually Produces"
slug: anatomy-of-a-findings-report-third-party-plan-review
date: 2026-07-24
description: "What does a third-party plan review actually deliver? Inside the anatomy of a real findings report: how conflicts get classified, priced, and handed back to the owner."
deck: "Most owners commission a third-party plan review before they've ever seen one. Here's what's actually inside the deliverable — and how it differs from a punch list or a QA/QC checklist."
tags: [Document Review, Coordination, Bid Documents]
---

!lede Every owner who commissions a third-party plan review has some version of the same question once the engagement letter is signed: what actually comes back? Not the sales pitch — the document. Most owners on a $30M+ project have sat through an architect's QC process and a GC's coordination pass before, but neither of those produces anything close to what an independent, owner-side findings report looks like. The report is the entire product. It's worth knowing what's actually in it before you're staring at one for the first time.

A findings report is not a punch list. It's not a marked-up set of drawings with circles and arrows. It's a structured document that names every conflict found, where it lives in the set, what it would cost if it made it to the field, and what fixing it now requires — organized so an owner with no drafting background can read it in twenty minutes and know exactly what to send back to the design team.

## What actually goes into a finding

Every individual finding in a real report follows the same skeleton, regardless of what kind of conflict it is:

- **Location** — the specific sheet numbers, detail callouts, or spec section involved. Not "the MEP drawings" — sheet M-401 against sheet S-201, or Spec Section 07 21 00 against Detail 4/A-501.
- **The contradiction, stated plainly** — what one document says versus what the other document says or shows, in language a superintendent or an owner's project manager can read without cross-referencing anything else.
- **Discipline(s) involved** — single-discipline internal inconsistencies get flagged differently than cross-discipline conflicts, because they usually have different owners on the design team.
- **Severity classification** — critical, major, or minor, based on what happens if the conflict isn't caught before bid or before construction.
- **Estimated exposure** — a dollar range if one can be reasonably estimated from the scope of the conflict, or a qualitative description of consequence if a number isn't supportable. Never a guessed figure dressed up as a real one.
- **Recommended resolution path** — who needs to weigh in (structural EOR, mechanical engineer, spec writer) and what kind of fix is likely: a redline, a coordination meeting, or a formal design revision.

That's the whole structure, repeated for every finding in the set. A review of a $30M-scale project's bid set typically turns up findings across a wide range — some sets are cleaner than others — and each one gets logged this way rather than as a general narrative comment.

<div class="callout">
  <div class="cl-label">Worth knowing</div>
  <p>A finding written as "coordinate MEP with structural" is not a finding — it's a placeholder for one. A real finding names the two specific documents in conflict, the exact contradiction between them, and what it costs if nobody catches it before the set is issued. If a report can't point to a sheet number, it isn't a document-level review; it's a general impression.</p>
</div>

## Why severity classification isn't optional

Construction QA/QC processes already use a version of this — non-conformance reports on active jobs are routinely graded critical, major, or minor, because a life-safety issue and a cosmetic inconsistency don't belong in the same triage lane. A findings report from a pre-bid or IFC review borrows the same logic, applied earlier, before anything is built:

- **Critical** — a conflict that would stop work in the field, require an engineer of record's re-stamp, or create a life-safety exposure if built as drawn. These get flagged first, regardless of how many other findings are in the report.
- **Major** — a conflict that would generate a real RFI and likely a change order, but doesn't stop the job outright. As we've written about in [why RFI count is the wrong metric to track](/blog/rfi-reduction-coordination-conflicts/), a lot of major-tier conflicts never even become a logged RFI — they get field-resolved and quietly change-ordered instead, which is exactly the blind spot a pre-bid findings report is built to close.
- **Minor** — an inconsistency worth fixing (a callout that doesn't match a schedule, a note referencing a superseded detail) but unlikely to generate real cost exposure on its own.

Severity isn't a formality. It's what lets an owner triage 15 minutes of reading time against a design team's redline turnaround before bid closes, instead of treating every finding as equally urgent — or equally ignorable.

<div class="mini-report">
  <div class="rh"><span class="title">ILLUSTRATIVE FINDING BREAKDOWN</span><span class="meta">A single cross-discipline finding, structural elevation vs. MEP routing — not a specific project</span></div>
  <div class="mini-row"><span class="k">Location</span><span class="v">Sheet M-401 vs. Sheet S-201, Grid Line D/4</span></div>
  <div class="mini-row"><span class="k">Discipline</span><span class="v">Mechanical / Structural</span></div>
  <div class="mini-row"><span class="k">Severity</span><span class="v hot">Critical</span></div>
  <div class="mini-row"><span class="k">If caught pre-bid</span><span class="v">Redline — near-zero cost</span></div>
  <div class="mini-row"><span class="k">If caught in the field</span><span class="v hot">$300,000–$400,000+</span></div>
</div>

That's not a hypothetical gap — it's the same math behind [how a single missed MEP clash turns into a $400K change order](/blog/missed-mep-clash-change-order-cost/): the conflict costs the same to describe whether it's found in week two or week twenty. What changes is what it costs to fix.

## Why the report has to name a dollar figure, not just describe the problem

A findings report that only describes conflicts qualitatively is useful to a design team. It's not enough for an owner deciding whether to push back before bid closes, because "coordination issue" and "$380,000 change order if missed" don't compete for attention the same way on an owner's desk. Where a defensible range can be estimated — based on scope of rework, likely engineering re-review, and typical schedule impact for that class of conflict — the report should include it. Where it can't be responsibly estimated, the report says so plainly rather than manufacturing a number. Design-related change orders industry-wide run an estimated 3–5% of total construction budget, and total change order costs on major projects frequently reach 10–15% of contract value — real exposure on a $30M job, not a rounding error, which is the frame every dollar figure in a findings report is meant to translate into something specific and page-referenced rather than left as an industry average.

## What a real audit is not

It's worth being explicit about what doesn't count, because the term "review" gets used loosely in construction:

- **Not a rubber stamp.** A findings report with zero or near-zero findings on a $30M+ set is a red flag about the review, not a clean bill of health for the drawings — cross-discipline conflicts of some kind are close to universal at this project scale.
- **Not a general narrative memo.** "The set appears generally coordinated with some areas warranting attention" isn't a finding. It's not actionable by anyone.
- **Not the architect's QC repackaged.** As covered in [architect QC vs. owner-side review](/blog/architect-qc-vs-owner-review/), the architect's own quality control checks the drawings against design intent — did the mechanical sheet match what the mechanical engineer meant to draw. It isn't scoped to catch a contradiction between two disciplines' sheets, or between a spec section and the detail it's supposed to govern, which is precisely the category an independent findings report exists to cover.
- **Not a substitute for BIM clash detection, or replaced by it.** Clash detection catches modeled geometry conflicts reliably. It doesn't catch a written note that contradicts a drawn detail or a spec clearance the drawing doesn't allow for — conflicts that live in the documents, not the model, and that a document-level findings report is built specifically to surface.

## Timing changes what the report can still fix

The same findings report produced against a pre-bid set and against an IFC set contains the same kind of findings, but the recommended resolution path looks different in each. As we've covered in [pre-bid vs. IFC timing](/blog/pre-bid-drawing-review-vs-ifc-timing/), a critical finding caught before the set goes to bid is a redline the design team can turn around before pricing locks in. The identical finding, caught after the set is issued for construction, comes with a resolution path that already includes a change order discussion, because the price is set and the leverage to fix it for free is largely gone. The report format doesn't change. What it can still accomplish for free does.

<div class="takeaways">
  <h3>Key takeaways</h3>
  <ul>
    <li>A real findings report logs every conflict individually — location, contradiction, discipline, severity, estimated exposure, and recommended resolution — not a general narrative comment.</li>
    <li>Findings get classified critical, major, or minor, the same triage logic used in construction QA/QC non-conformance reports, applied earlier in the process before anything is built.</li>
    <li>A dollar exposure estimate, where one is defensible, is what gets a finding read and acted on before bid closes — an industry-average change order percentage doesn't compete for an owner's attention the way a page-referenced number does.</li>
    <li>A findings report is not the architect's QC repackaged and not a substitute for BIM clash detection — it's scoped specifically to cross-discipline and document-vs-document conflicts neither of those catches.</li>
    <li>The findings in a report don't change based on timing; what a design team can still fix for free before pricing locks in does.</li>
  </ul>
</div>

None of this requires an owner to become fluent in reading construction drawings. It requires knowing what a real deliverable looks like well enough to recognize the difference between a findings report and a document that merely resembles one — before deciding whether the set in front of you has actually been checked.

## Frequently Asked Questions

### What's the difference between a findings report and a punch list?

A punch list is generated during or after construction, tracking incomplete or defective installed work against the contract documents. A findings report is generated before construction — usually pre-bid or at issued-for-construction — and tracks contradictions and coordination conflicts within the documents themselves, before anything has been built to check against.

### How many findings does a typical $30M project's drawing set have?

It varies significantly by project complexity and how coordinated the design team's own process was, so there's no single benchmark number worth quoting. What's consistent across project types is that some cross-discipline conflicts are close to universal at this scale — a report that comes back with zero findings on a set this size is more often a sign of a shallow review than a genuinely clean set of drawings.

### Does a findings report replace the need for an RFI process during construction?

No. A pre-bid or pre-construction findings report catches what's visible in the documents before the field ever gets involved, but it can't anticipate every condition that surfaces once construction starts. It reduces the volume and severity of RFIs that stem from document-level conflicts specifically — it doesn't eliminate the RFI process itself.

### Who is supposed to act on the findings in the report?

The design team — typically the architect of record and the relevant discipline engineers — resolves each finding, since they're the parties authorized to revise the documents. The owner's role is to require that resolution happen before bid closes or before the set is issued, using the report as the basis for that conversation rather than relying on the design team to self-report gaps in their own coordination.

### Is a findings report the same thing as a peer review?

They're related but scoped differently. A peer review typically evaluates whether a design meets code and engineering standards, often discipline by discipline. A findings report from an independent document review is scoped specifically to conflicts between disciplines and between the drawings and the specs — the category of issue a single-discipline peer review isn't structured to catch.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What's the difference between a findings report and a punch list?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "A punch list is generated during or after construction, tracking incomplete or defective installed work against the contract documents. A findings report is generated before construction, usually pre-bid or at issued-for-construction, and tracks contradictions and coordination conflicts within the documents themselves, before anything has been built to check against."
      }
    },
    {
      "@type": "Question",
      "name": "How many findings does a typical $30M project's drawing set have?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "It varies significantly by project complexity and how coordinated the design team's own process was, so there's no single benchmark number worth quoting. What's consistent across project types is that some cross-discipline conflicts are close to universal at this scale, a report that comes back with zero findings on a set this size is more often a sign of a shallow review than a genuinely clean set of drawings."
      }
    },
    {
      "@type": "Question",
      "name": "Does a findings report replace the need for an RFI process during construction?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No. A pre-bid or pre-construction findings report catches what's visible in the documents before the field ever gets involved, but it can't anticipate every condition that surfaces once construction starts. It reduces the volume and severity of RFIs that stem from document-level conflicts specifically, it doesn't eliminate the RFI process itself."
      }
    },
    {
      "@type": "Question",
      "name": "Who is supposed to act on the findings in the report?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The design team, typically the architect of record and the relevant discipline engineers, resolves each finding, since they're the parties authorized to revise the documents. The owner's role is to require that resolution happen before bid closes or before the set is issued, using the report as the basis for that conversation rather than relying on the design team to self-report gaps in their own coordination."
      }
    },
    {
      "@type": "Question",
      "name": "Is a findings report the same thing as a peer review?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "They're related but scoped differently. A peer review typically evaluates whether a design meets code and engineering standards, often discipline by discipline. A findings report from an independent document review is scoped specifically to conflicts between disciplines and between the drawings and the specs, the category of issue a single-discipline peer review isn't structured to catch."
      }
    }
  ]
}
</script>
