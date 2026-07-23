# Decision Types

Used by blog/prompts/triage.md to classify each topic from topics.md
before any content gets written.

Check the topic's target keyword against these rules, in order.
First match wins. If nothing matches, it's informational.

## 1. alternatives
Keyword contains: "alternatives", "alternative to"
Example: "asana alternatives"
Route to: blog/prompts/comparison.md
Target: new_post

## 2. comparison
Keyword contains: "vs", "versus", "or" (between two product names)
Example: "asana vs monday"
Route to: blog/prompts/comparison.md
Target: new_post

## 3. pricing
Keyword contains: "pricing", "cost", "price", "how much"
Example: "asana pricing"
Route to: blog/prompts/pricing-update.md
Target: update_existing (check blog/posts/ and any pricing page first —
if one already exists for this product, update it instead of writing a new post)

## 4. review
Keyword names a specific product/vendor and asks whether it's good or
worth using: "[product] review", "[product] reviews", "is [product]
good", "[product] worth it".
Does NOT match generic service-category terms that merely contain the
word "review" (e.g. "constructability review consultant",
"construction document review services") — those are hire-me intent,
not review-checking intent. If the keyword doesn't name a specific
product/vendor, this rule does not match; fall through to rule 6.
Example match: "asana review"
Example non-match: "constructability review consultant"
Route to: blog/prompts/review-brief.md
Target: new_post

## 5. trial_or_discount
Keyword contains: "free trial", "discount", "coupon", "promo code"
Example: "asana free trial"
Route to: blog/prompts/conversion-check.md
Target: new_post

## 6. informational (default)
Everything else — how-to, guides, "what is", listicles not matching above.
Route to: blog/prompts/daily-post.md
Target: new_post
