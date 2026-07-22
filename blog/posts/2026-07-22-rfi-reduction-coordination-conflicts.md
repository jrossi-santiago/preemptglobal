---
title: "RFI Reduction Won't Save You From Coordination Conflicts"
slug: rfi-reduction-coordination-conflicts
date: 2026-07-22
description: "RFI reduction sounds like progress, but a low RFI count doesn't mean a coordinated set. Here's the metric owners should track instead — and why."
deck: "Every project management dashboard tracks RFI count going down. Almost none of them track the conflicts that never became an RFI at all — because they became a change order instead."
tags: [Coordination, RFIs, Change Orders]
---

!lede RFI reduction has become the metric everyone on a project claims credit for. The GC points to a lower RFI log than last quarter's job. The design team cites it as proof the drawings were clean. The owner sees a shrinking number and assumes the project is running smoother than the last one. None of that is necessarily true, and on $30M+ builds, the gap between "fewer RFIs" and "fewer conflicts" is exactly where the expensive change orders live.

An RFI count is a count of questions asked, not a count of problems that existed. A drawing set can generate very few RFIs and still be full of unresolved cross-discipline conflicts — because nobody in the field happened to notice the girder and the duct were fighting for the same six inches until the steel was already up. At that point there's no RFI. There's a change order, a schedule hit, and a much more expensive version of the same conversation.

## What RFI count actually measures

A 2013 Navigant Construction Forum study, still the most-cited benchmark in the industry, analyzed roughly one million RFIs across 1,300 major construction projects and found an average of 796 RFIs per project, at an average processing cost of $1,080 each (in 2013 dollars) with a median response time of 9.7 days. Industry estimates for the fully-loaded cost per RFI today — factoring in the design team's review time, the GC's coordination time, and downstream schedule effects — put the number closer to $2,000–$3,000. Separately, benchmark data on RFI volume puts typical generation in the range of 15–20 RFIs per $1 million of project value, meaning a $30M project should expect somewhere in the range of 450–600 RFIs as a matter of course, independent of how well-coordinated the set actually is.

That's the first problem with treating RFI count as a health metric: a large chunk of it is just the size of the project talking, not the quality of the documents.

<div class="mini-report">
  <div class="rh"><span class="title">RFI BENCHMARKS</span><span class="meta">Navigant Construction Forum, 2013; industry updates since</span></div>
  <div class="mini-row"><span class="k">Avg. RFIs per project studied</span><span class="v">796</span></div>
  <div class="mini-row"><span class="k">Avg. cost to process (2013 $)</span><span class="v">$1,080</span></div>
  <div class="mini-row"><span class="k">Median response time</span><span class="v">9.7 days</span></div>
  <div class="mini-row"><span class="k">Current est. fully-loaded cost</span><span class="v hot">$2,000–$3,000</span></div>
</div>

The second problem is worse: RFI count can go down for reasons that have nothing to do with better coordination.

## Why a shrinking RFI log isn't automatically good news

Zero RFIs on a set that size isn't a sign of a perfectly coordinated project — it's usually a sign that people in the field have stopped asking questions and started making field calls on their own, or that a subcontractor priced around an ambiguity instead of flagging it, betting they'd recover the cost later through a change order. Either way, the conflict didn't disappear. It just moved out of the RFI log and into a line item nobody sees until the pay application.

This is the same dynamic that shows up whenever a single metric gets optimized in isolation from what it's supposed to represent. Superintendents under schedule pressure have every incentive to resolve small field conflicts informally rather than route them through a formal RFI that takes 9.7 days to answer. A GC tracking RFI count as a KPI has every incentive to discourage the practice of filing one for anything that can plausibly be resolved on-site. Neither of those behaviors makes the drawings more coordinated. They just make the dashboard look better.

<div class="callout">
  <div class="cl-label">Worth knowing</div>
  <p>On a mid-rise mixed-use set we reviewed pre-bid, the RFI log from a nearly identical project the same design team had completed the year before showed unusually few coordination-related RFIs. When we ran an independent pass on the current set, we found 19 cross-discipline conflicts that matched patterns from the earlier project almost exactly — they just hadn't been logged as RFIs the first time. They'd been field-resolved and quietly change-ordered instead.</p>
</div>

## The conflicts that never become RFIs at all

Some of the most expensive conflicts in a document set never generate an RFI in the first place, because nobody with authority to write one is looking at the sheets specifically for contradictions between disciplines. The architect's QC checks the design against its own intent. The GC's coordination team reads the set to price it accurately, which — as we've written about [why the architect's QC and owner-side review aren't the same thing](/blog/architect-qc-vs-owner-review/) — creates an incentive to price around an ambiguity rather than flag it during bid. Neither of those reviews is scoped to catch a spec section that contradicts a detail, or a structural note that quietly conflicts with an MEP routing decision on a different sheet.

Those are exactly the conflicts that skip the RFI process entirely. They show up as change orders with no RFI trail behind them, which means an owner looking only at RFI count as a leading indicator has no visibility into them until the invoice.

Design-related change orders are a meaningful share of total cost exposure on projects this size. Industry estimates put change order costs due specifically to architectural and engineering errors and omissions at roughly 3–5% of the total construction budget, and total change order costs on major projects at 10–15% of contract value, with some projects running well past that. On a $30M project, even the lower end of that range is $900,000–$1.5M in exposure that a shrinking RFI count would never have predicted.

## A better metric: conflicts caught before they cost anything

The right question isn't "how many RFIs did we generate this month." It's "how many of the cross-discipline conflicts in this set were caught while they were still free to fix." A conflict caught at design is a redline. Caught at permit, it's a coordination note. Caught at bid, someone has already priced around it. Caught in the field, it's an RFI at best and a change order at worst — and by then, the fix costs what it costs regardless of what the RFI log says.

That's a fundamentally different thing to track than RFI volume, and it requires someone to actually look for conflicts before the set goes out, rather than waiting for the field to surface them. BIM coordination workflows help — projects that run structured clash detection during design report RFI reductions of up to 40% on the geometry-based conflicts that show up as physical clashes in the model. But clash detection only catches what's modeled. It doesn't catch a written note that contradicts a drawn detail, an omission where no conflicting geometry exists because no one modeled the connection at all, or a spec section that disagrees with the sheet it's supposed to govern. Those conflicts live in the issued documents, not in the model, and they need a document-level read to surface — the same kind of pass an independent, owner-side reviewer runs on a bid or IFC set before it goes out.

<div class="takeaways">
  <h3>Key takeaways</h3>
  <ul>
    <li>RFI count measures how many questions got asked — not how many conflicts exist in the set.</li>
    <li>A shrinking RFI log can reflect field workarounds and quiet change orders as easily as it can reflect better coordination.</li>
    <li>The Navigant Construction Forum benchmark puts the average project at 796 RFIs and roughly $1,080 each to process — current fully-loaded estimates run $2,000–$3,000.</li>
    <li>Design-related change orders alone run 3–5% of total construction budget on average; total change order exposure often runs 10–15%.</li>
    <li>The metric that actually predicts cost exposure is conflicts caught before bid, not RFIs filed after.</li>
  </ul>
</div>

Tracking RFI count isn't wrong — it's just incomplete. It tells you how much friction showed up in the field. It says nothing about the friction that got priced around instead of logged, or the conflicts sitting in the issued set that haven't been discovered by anyone yet. The projects that actually reduce change-order exposure aren't the ones with the fewest RFIs on the dashboard. They're the ones where someone read the set for cross-discipline conflicts before it ever reached the field — while the fix was still a redline instead of a claim.

## Frequently Asked Questions

### What's a good number of RFIs for a $30M construction project?

There isn't a universal target, because RFI volume scales with project size and complexity — industry benchmarks suggest a range of roughly 15–20 RFIs per $1 million of project value as a baseline. A $30M project generating well outside that range in either direction is worth a closer look, but the count alone doesn't tell you whether the underlying documents were coordinated.

### Does a low RFI count mean the drawing set was well-coordinated?

Not necessarily. A low count can mean the set was genuinely clean, but it can also mean field teams resolved ambiguities informally and subcontractors priced around unclear details rather than filing formal questions. Those conflicts still show up later — usually as change orders with no RFI trail explaining where they came from.

### What's the actual difference between an RFI and a change order?

An RFI is a formal question asked during construction to clarify something ambiguous or missing in the documents, typically resolved without a cost impact if caught early enough. A change order is a formal modification to the contract, usually because the RFI (or a field discovery with no preceding RFI) revealed something that requires additional scope, cost, or time to resolve. The later a conflict is caught, the more likely it becomes a change order instead of a free clarification.

### How can owners reduce RFI-driving conflicts without slowing down the schedule?

The fix isn't discouraging RFIs — it's catching the underlying conflicts before the set is issued, so fewer of them ever reach the field as questions or claims. An independent, document-level review of the bid or IFC set, run specifically to find cross-discipline conflicts before bid, typically takes 48 hours and doesn't touch the design or construction schedule at all.

### Is RFI count a fair way to evaluate a design team or GC's performance?

On its own, no — it rewards whoever is best at keeping conflicts out of the formal log, which isn't the same as keeping conflicts out of the project. A more useful evaluation combines RFI trends with first-pass response quality, the timing of when conflicts were caught relative to bid, and an independent read of how coordinated the issued documents actually were.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What's a good number of RFIs for a $30M construction project?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "There isn't a universal target, because RFI volume scales with project size and complexity — industry benchmarks suggest a range of roughly 15–20 RFIs per $1 million of project value as a baseline. A $30M project generating well outside that range in either direction is worth a closer look, but the count alone doesn't tell you whether the underlying documents were coordinated."
      }
    },
    {
      "@type": "Question",
      "name": "Does a low RFI count mean the drawing set was well-coordinated?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Not necessarily. A low count can mean the set was genuinely clean, but it can also mean field teams resolved ambiguities informally and subcontractors priced around unclear details rather than filing formal questions. Those conflicts still show up later, usually as change orders with no RFI trail explaining where they came from."
      }
    },
    {
      "@type": "Question",
      "name": "What's the actual difference between an RFI and a change order?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "An RFI is a formal question asked during construction to clarify something ambiguous or missing in the documents, typically resolved without a cost impact if caught early enough. A change order is a formal modification to the contract, usually because the RFI, or a field discovery with no preceding RFI, revealed something that requires additional scope, cost, or time to resolve."
      }
    },
    {
      "@type": "Question",
      "name": "How can owners reduce RFI-driving conflicts without slowing down the schedule?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The fix isn't discouraging RFIs, it's catching the underlying conflicts before the set is issued, so fewer of them ever reach the field as questions or claims. An independent, document-level review of the bid or IFC set, run specifically to find cross-discipline conflicts before bid, typically takes 48 hours and doesn't touch the design or construction schedule at all."
      }
    },
    {
      "@type": "Question",
      "name": "Is RFI count a fair way to evaluate a design team or GC's performance?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "On its own, no, it rewards whoever is best at keeping conflicts out of the formal log, which isn't the same as keeping conflicts out of the project. A more useful evaluation combines RFI trends with first-pass response quality, the timing of when conflicts were caught relative to bid, and an independent read of how coordinated the issued documents actually were."
      }
    }
  ]
}
</script>
