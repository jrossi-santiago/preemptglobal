---
title: "RFI Volume Isn't a KPI: What to Track Instead"
slug: rfi-volume-not-a-kpi-what-to-track-instead
date: 2026-08-10
description: "RFI reduction alone isn't a real performance metric. Here's the leading-indicator framework owners should track instead of RFI volume — and the numbers behind it."
deck: "Every project dashboard has a line for RFI count. Almost none of them have a line for what actually predicts cost exposure: where conflicts get caught, and how much never shows up as an RFI at all."
tags: [Coordination, RFIs, Metrics]
---

!lede RFI reduction gets treated as a scorecard number on most large projects — a line on a monthly dashboard that goes down and gets read as progress. It's a lagging indicator dressed up as a leading one, and the difference matters more than the semantics suggest. A falling RFI count tells you how many formal questions got filed. It says nothing about how many cross-discipline conflicts are actually sitting in the documents, waiting to surface as a field problem instead of a paperwork one.

That gap is why "RFI reduction" as a stated goal keeps producing disappointing results even on projects where the count genuinely drops. As covered in [why RFI count doesn't measure coordination](/blog/rfi-reduction-coordination-conflicts/), a lower log can just as easily mean conflicts got field-resolved and quietly change-ordered instead of formally logged. The fix for that isn't a better RFI target. It's a different set of things to measure.

## Why a Single Number Can't Do This Job

Any team that manages by one number will eventually manage to that number instead of to the outcome it was supposed to represent. RFI count is especially prone to this because it's easy to move without moving the thing underneath it — a superintendent under schedule pressure can resolve a field ambiguity with a phone call instead of a formal RFI, and the dashboard improves while the conflict rate doesn't change at all.

The standard fix in quality management for this exact failure mode is to separate leading indicators from lagging ones. A lagging indicator records something that already happened — RFI count, change order total, punch list length. A leading indicator measures something upstream that predicts those outcomes before they're locked in — how much of the document set has been checked for cross-discipline conflicts, and when. The Construction Industry Institute uses this same distinction for safety performance, where lagging measures like incident rate are treated as too delayed and too noisy to manage against directly, in favor of leading measures of the practices that prevent incidents in the first place. Coordination quality has the identical problem, and the identical fix applies.

## The Metric Buried Inside "Cost of Quality"

Quality management has a framework for this that construction rarely applies explicitly, even though the underlying activity — reviewing documents before they cause a problem — fits it exactly. Cost of quality splits spending into two categories: cost of conformance (prevention and appraisal — catching problems before they exist) and cost of nonconformance (internal and external failure — the cost of fixing what wasn't caught). Every dollar spent on document review before bid is conformance spend. Every dollar spent on a field-discovered coordination conflict — the RFI cycle, the redesign, the change order, the schedule impact — is failure spend, and it's reliably the larger number.

The Construction Industry Institute puts average direct field rework at roughly 5% of total project cost, ranging from 2% to 20% depending on project type and how well the set was coordinated going in. That's the failure-cost side of the ledger, and it's the number a shrinking RFI count does nothing to move if the underlying conflicts are just getting caught later, in the field, instead of earlier, on paper.

<div class="mini-report">
  <div class="rh"><span class="title">COST OF QUALITY, APPLIED TO COORDINATION</span><span class="meta">CII field rework benchmark</span></div>
  <div class="mini-row"><span class="k">Avg. direct field rework (% of project cost)</span><span class="v hot">~5%</span></div>
  <div class="mini-row"><span class="k">Range by project type/coordination quality</span><span class="v">2%–20%</span></div>
  <div class="mini-row"><span class="k">Where this cost sits on the ledger</span><span class="v">Failure (nonconformance)</span></div>
  <div class="mini-row"><span class="k">What a pre-bid review adds to</span><span class="v">Prevention (conformance)</span></div>
</div>

An owner tracking RFI count alone has no visibility into which side of that ledger a project is actually on. Two projects can post identical RFI totals — one because the set was genuinely clean, the other because conflicts got absorbed into field change orders that never touched the RFI log. Only one of those projects has a real coordination problem, and RFI count can't tell them apart.

## Four Things to Track Instead

None of these require new software or a new process — they require asking a different question of the same document review and change-order data most projects already generate.

1. **Conflict origin ratio.** Of the cross-discipline conflicts identified over the life of the project, what share were caught before bid versus discovered in the field? This is the single most direct leading indicator of coordination quality, because it measures when a conflict was found, not just whether it eventually got resolved. A project catching most of its conflicts pre-bid is running conformance spend down the failure-cost curve; a project catching most of them in the field is running the reverse.

2. **Findings closure, not findings count.** A cumulative findings tracker — resolved versus still-open, logged against the sheet and discipline where it was found — says more than a raw conflict count ever could. A high number of findings closed pre-bid is a good sign. The same number sitting open at 90% construction complete is a warning, regardless of what the RFI log shows in the meantime.

<div class="callout">
  <div class="cl-label">Worth knowing</div>
  <p>A findings report that's sheet-located and severity-ranked — not just a running list — turns this into a metric instead of a document. It's the same structure covered in <a href="/blog/anatomy-of-a-findings-report-third-party-plan-review/">what a real findings report looks like</a>: every conflict tagged with where it was found, how severe it is, and what it costs if it isn't fixed before bid.</p>
</div>

3. **Rework and change-order cost as a percentage of contract value, tracked over time.** This is the lagging indicator that actually matters, as opposed to RFI count, which is a lagging indicator that doesn't. The CII's 2%–20% rework range gives a real benchmark to plot against — a project trending toward the low end after adopting a pre-bid coordination review, project over project, is the evidence a leading-indicator strategy is working. RFI count trending down in isolation is not that evidence.

4. **RFI cost and aging, as a secondary signal only.** RFI volume and response time aren't useless — a spike in either can flag a real process breakdown. The mistake is treating volume as the primary target instead of a secondary signal that needs the other three numbers next to it for context. Tracked alongside conflict origin and findings closure, RFI trends become informative. Tracked alone, they're the number a project can move without moving anything that matters, which is exactly the failure mode covered in the [change order math behind real cost exposure](/blog/change-order-math-calculating-real-exposure/).

<div class="takeaways">
  <h3>Key takeaways</h3>
  <ul>
    <li>RFI count is a lagging indicator of formal questions asked — not a leading indicator of coordination quality, and the two can move in opposite directions.</li>
    <li>The cost-of-quality framework splits spend into prevention/appraisal (conformance) and failure (nonconformance) — the CII puts average direct field rework at roughly 5% of project cost, ranging 2%–20%, which is the failure-cost number a shrinking RFI count doesn't move.</li>
    <li>Conflict origin ratio — the share of conflicts caught pre-bid versus in the field — is the most direct leading indicator available, because it measures timing, not just eventual resolution.</li>
    <li>A cumulative findings tracker, closed against resolved versus still-open, gives a real-time read on coordination status that RFI count structurally cannot.</li>
    <li>RFI volume and response time are still worth watching, but only as a secondary signal alongside these — never as the primary KPI on their own.</li>
  </ul>
</div>

The projects that actually reduce cost exposure aren't the ones instructed to reduce RFIs. They're the ones tracking when conflicts get caught, not just how many questions got asked about them — and shifting spend from the failure side of the ledger to the prevention side before the set ever reaches the field.

## Frequently Asked Questions

### If RFI count isn't a good KPI, what should replace it on a project dashboard?

Replace a single RFI number with a small set of leading and lagging indicators tracked together: the conflict origin ratio (conflicts caught pre-bid versus in the field), findings closure status from a cumulative tracker, and rework/change-order cost as a percentage of contract value over time. RFI volume can stay on the dashboard as a secondary signal, but it shouldn't be the number a team is managed against.

### What's the difference between a leading and a lagging indicator in construction quality?

A lagging indicator records something that already happened — RFI count, change order total, punch list length. A leading indicator measures an upstream activity that predicts those outcomes before they're locked in, such as how much of a document set has been independently checked for cross-discipline conflicts before bid. Leading indicators are actionable in real time; lagging indicators only confirm the result afterward.

### How much does construction rework typically cost as a percentage of project value?

The Construction Industry Institute puts average direct field rework at roughly 5% of total project cost, with a range of 2% to 20% depending on project type and how well the issued set was coordinated. That range is a useful benchmark for tracking whether a coordination review program is actually reducing failure costs over time, independent of what the RFI log shows.

### Can a project have a low RFI count and still have serious coordination problems?

Yes, and it's a common pattern. A low RFI count can reflect field teams resolving ambiguities informally or subcontractors pricing around unclear details rather than filing formal questions — in both cases the underlying conflict still exists, it just moves from the RFI log into an unlogged field change instead. Tracking conflict origin and findings closure alongside RFI count is what catches this pattern; RFI count alone cannot.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "If RFI count isn't a good KPI, what should replace it on a project dashboard?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Replace a single RFI number with a small set of leading and lagging indicators tracked together: the conflict origin ratio (conflicts caught pre-bid versus in the field), findings closure status from a cumulative tracker, and rework/change-order cost as a percentage of contract value over time. RFI volume can stay on the dashboard as a secondary signal, but it shouldn't be the number a team is managed against."
      }
    },
    {
      "@type": "Question",
      "name": "What's the difference between a leading and a lagging indicator in construction quality?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "A lagging indicator records something that already happened, RFI count, change order total, punch list length. A leading indicator measures an upstream activity that predicts those outcomes before they're locked in, such as how much of a document set has been independently checked for cross-discipline conflicts before bid. Leading indicators are actionable in real time; lagging indicators only confirm the result afterward."
      }
    },
    {
      "@type": "Question",
      "name": "How much does construction rework typically cost as a percentage of project value?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The Construction Industry Institute puts average direct field rework at roughly 5% of total project cost, with a range of 2% to 20% depending on project type and how well the issued set was coordinated. That range is a useful benchmark for tracking whether a coordination review program is actually reducing failure costs over time, independent of what the RFI log shows."
      }
    },
    {
      "@type": "Question",
      "name": "Can a project have a low RFI count and still have serious coordination problems?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes, and it's a common pattern. A low RFI count can reflect field teams resolving ambiguities informally or subcontractors pricing around unclear details rather than filing formal questions, in both cases the underlying conflict still exists, it just moves from the RFI log into an unlogged field change instead. Tracking conflict origin and findings closure alongside RFI count is what catches this pattern; RFI count alone cannot."
      }
    }
  ]
}
</script>
