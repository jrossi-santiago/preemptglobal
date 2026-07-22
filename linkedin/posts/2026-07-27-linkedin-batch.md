# LinkedIn Posts — Week of 2026-07-27

## Day 1 (Mon) — Growth

You probably read a bid set cover sheet first. I stopped doing that two years ago.

The cover sheet tells you what the design team wants you to see — code summary, project data, the neat version of the story. Read it first and you carry that version into every sheet after it. You start looking for confirmation instead of contradiction.

Now I start in the middle. Structural framing plan, then the MEP sheet that touches the same bay, then back to the code summary last — as the thing I'm checking everyone else's work against, not the thing that sets my expectations.

It changes what you catch. A 2-hour shaft wall on the code summary reads as settled fact if you see it first. Read the structural and architectural sheets cold, then check them against the summary, and a mismatch jumps out instead of getting explained away by a document you already trusted.

Small habit. Different results. Most reviews confirm what the cover sheet already told them to expect. Independent ones don't get to assume the story is true yet.

Send me your next bid set — I'll review it cold, no cover-sheet-first bias. Findings back in 5 business days, sheet reference and dollar range attached. Under $50K in exposure found, you don't pay.

---

## Day 2 (Tue) — Nurture

Your riser diagram says the conduit run goes from the basement switchgear to the roof-level mechanical penthouse. Has anyone actually traced it, floor by floor, against the plans for each level in between?

Most reviews check the riser diagram against itself — does it look internally consistent — and stop there. That's not the same as confirming the routing survives contact with every individual floor plan it has to pass through.

Here's the framework I run on every data center set, three passes:

Pass 1 — Anchor points. Confirm the riser's stated start and end points match the equipment shown on those floor plans exactly, not approximately.

Pass 2 — Continuity. Walk the riser through every intermediate level. Does the shaft exist on that floor's plan? Is it sized the same? A riser that's 4" on level 2 and 6" on level 5 has a gap somewhere nobody drew.

Pass 3 — Penetrations. Check that each floor penetration shown on the riser has a matching fire-rated assembly detail on that floor's architectural sheet.

I've found risers that vanish for two floors and reappear like nothing happened. Run this before your set goes to permit — send it over, I'll trace it for you. Findings in 5 business days, dollar range attached, $50K guarantee, NDA available.

---

## Day 3 (Wed) — Nurture

Your equipment schedule says the CRAC units run 480V, 3-phase. The submittal your vendor sent back says something close, but not identical. Who's checking that the two actually match before the submittal gets stamped "approved"?

Most coordination review stops at "does the submittal look complete." It rarely asks "does the submittal match the design intent, line by line."

The Submittal Match — three checks I run on every piece of long-lead equipment:

Electrical — voltage, phase, and full-load amps on the submittal against the schedule and the one-line. Not close. Identical.

Physical — dimensions and weight on the submittal against the structural and architectural sheets showing where the unit lands. A unit 4" wider than scheduled doesn't fit the curb it was designed for.

Connections — inlet and outlet sizes and locations against the piping and ductwork already drawn to meet it.

I caught a chiller last month spec'd for a 6" supply connection where the submittal showed 8". Nobody flagged it, because the submittal "looked right" — full spec sheet, clean formatting, vendor letterhead. Looking right and matching are different things.

Send me the schedule and the submittals together. I'll run the match. Findings in 5 business days, sheet reference and dollar range, $50K guarantee or you don't pay.

---

## Day 4 (Thu) — Conversion

Your switchgear is rated for less fault current than your generators can actually deliver. Here's what that costs when it's caught in the field instead of at bid.

Reviewed a data center bid set two weeks ago. Two 2MW generators, paralleled, feeding a switchgear lineup spec'd at 65kAIC. Ran the fault current calc with both units contributing simultaneously: 71kA available at that bus. The switchgear was under-rated by 6kA.

On paper, that's a rounding error. In the field, it's switchgear that can't safely interrupt a fault it's actually exposed to — which means re-engineering the gear, a change order, and every trade waiting on that electrical room to close in getting resequenced.

Caught at bid review: a redline to the spec section and a note to the switchgear vendor. An afternoon.
Caught after the gear ships: $96K–$180K in re-manufacture and freight, plus 10–14 weeks added to a schedule already tight on the generator lead time.

Nobody missed this because they're careless. The fault current calc lives in a different submittal than the switchgear spec, and nobody's job is to hold both at once and check the math between them.

Send me your set before it goes to bid. Findings in 5 business days, dollar range attached. Under $50K found, you don't pay.

---

## Day 5 (Fri) — Growth

The cleanest bid set I ever reviewed had the worst mistake buried in it.

Every sheet formatted the same. Consistent title blocks, consistent line weights, a code summary that read like it had been proofread three times. The kind of set that makes you relax a little before you've checked anything.

That's exactly the problem. A messy set puts you on alert. A polished one lulls you. I almost signed off on that review in under two hours because nothing looked off — until I cross-checked the fire-rated assembly on one sheet against the structural detail on another out of habit, not suspicion. Two different ratings for the same wall. One hour on structural, two hours on architectural.

Nothing about the formatting told me to look there. The formatting told me not to bother.

I've started treating a clean-looking set as a reason to slow down, not speed up. Polish is a production value. It's not evidence the coordination underneath actually happened.

If your set looks buttoned-up and hasn't had an outside pass on it, that's exactly the profile I'd want to check. Send it over — findings in 5 business days, dollar range attached, $50K guarantee, NDA available.

---

## Day 6 (Sat) — Nurture

Your panel schedule shows 42 circuits at 20A each. Your one-line has a main breaker sized for a load that doesn't add up to that. Which one is wrong — and has anyone done the arithmetic to find out?

Panel schedules and one-lines get drawn by different people, sometimes on different days, and reconciling them against each other isn't anybody's explicit job. It falls into the gap between disciplines.

The Panel Schedule Cross-Check, two passes:

Pass 1 — Load math. Add up the connected load on the panel schedule. Compare it against the main breaker size and the feeder on the one-line. If the math doesn't support the breaker size, one of the two documents is wrong.

Pass 2 — Circuit count. Count the circuits on the panel schedule against the spaces available in the panel called out in the spec. A 42-circuit schedule in a panel spec'd for 30 spaces doesn't fit, and nobody catches that until the panel shows up.

Found this exact gap on a project two months ago — panel schedule assumed a 400A main, one-line showed 350A feeding it. Caught before permit, it's a correction. Caught after, it's a panel swap.

Run this before your set goes out. Send it to me — findings in 5 business days, $50K guarantee, NDA available.

---

## Day 7 (Sun) — Conversion

Your mechanical schedule puts a 4,000-lb rooftop unit on a mezzanine platform. Your structural drawings don't show a connection detail for how that load transfers into the frame below it.

Reviewed a large commercial set last month with exactly this gap. The mechanical schedule and equipment plan were clear on the unit, its weight, and its location. The structural sheets showed the mezzanine framing in general terms — beam sizes, column grid — but no connection detail where a 4,000-lb load was supposed to land.

That's not a drafting oversight you can wave off. Without a checked connection detail, nobody has confirmed the frame was designed for that load in that location, as opposed to a generic uniform load across the platform.

Caught at bid review: a coordination note to the structural engineer, a detail added before award. A few days.
Caught during steel fabrication: re-engineering the connection, possible re-fabrication of affected members, and $122K–$310K in cost with 8–12 weeks added to a schedule already sequencing steel against everything above it.

The mechanical schedule and the structural set get reviewed by different people who never compare notes. That's the seam this fell through.

Send me your set before steel gets released for fabrication. Findings in 5 business days, dollar range attached, $50K guarantee or you don't pay.
