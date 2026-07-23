You are handling a trial or discount buy-intent topic for Preempt
Global, at github repo jrossi-santiago/preemptglobal (main branch is
the live site, auto-deployed — generated static HTML is committed
directly, no build step beyond blog/build.py).

First: read PREEMPT_CONTEXT.md at the repo root in full. If it
conflicts with this prompt, PREEMPT_CONTEXT.md wins.

GATE CHECK — do this before anything else:
Read blog/next_action.json. If route_to is NOT
"blog/prompts/conversion-check.md", stop immediately and reply with
exactly: "Not my topic — routed to <route_to> instead. No action
taken." Do not proceed past this point in that case.

If route_to IS "blog/prompts/conversion-check.md", continue below.
Use the topic and keyword from next_action.json — do not re-read
topics.md for the topic.

IMPORTANT CONTEXT — read before doing anything:
Trial intent ("free trial") and discount intent ("discount", "coupon")
are different buying decisions and should almost never be answered by
the same page. Trial intent asks "can I use it?" Discount intent asks
"can I buy it for less, and what's the catch?" Determine which one
this topic is from the keyword itself before proceeding.

Do this, fully autonomously, no confirmation needed:

1. git fetch origin main && git reset --hard origin/main.

2. Read blog/POST_GUIDE.md in full for frontmatter/markdown rules.

3. Determine intent from the keyword: does it contain "trial" or
   "discount"/"coupon"/"promo"? Set your working intent accordingly
   (trial or discount). If genuinely ambiguous, default to trial.

4. Scan blog/posts/ and any existing site pages for a page that
   already covers this exact intent for this product. If one exists,
   you will be updating it in place rather than creating a new file
   — treat this the same way pricing-update.md treats an existing
   page (open it, read it fully, update rather than duplicate).

5. Research, using web search: the product's real, current trial or
   discount terms. Never invent an offer, amount, or duration that
   isn't confirmed by a source. If this is a discount topic and no
   real, currently-active offer exists, do NOT invent one because the
   keyword has search volume — write the page around whatever real
   trial/pricing options do exist instead, and note this substitution
   in your reply.

   IF intent is TRIAL, the page's first screen (opening section) must
   answer, in this order:
   - How long is the trial?
   - What is included?
   - Is a card required?
   - What happens when it ends?
   - Where do I start? (this should be the clearest, earliest CTA
     placement on the page — above the fold per the PDF's finding
     that 89% of ranking trial pages do this)

   IF intent is DISCOUNT, the page must cover:
   - The amount.
   - Eligibility.
   - Expiration.
   - Exclusions.
   - Renewal price (what it costs after the discount ends).
   - Redemption instructions.

6. Write or update the page as blog/posts/YYYY-MM-DD-slug.md (new) or
   in place (existing), 800-1,500 words — shorter than a standard
   post, since this is a conversion page, not a narrative one.
   Complete frontmatter per POST_GUIDE.md. Primary keyword in title,
   slug, and first 100 words where natural.

7. End the body with an FAQ section: 3-5 real searcher questions,
   each with a 2-4 sentence answer. Use the guide's FAQ/schema
   component if it defines one; otherwise H2 "Frequently Asked
   Questions" with H3 questions, plus FAQPage JSON-LD if raw script
   tags are supported — otherwise plain headings, note this in your
   reply.

8. Scan blog/posts/ for 2-3 related published posts and link
   contextually (real anchor text). Skip if nothing fits.

9. Do not write your own CTA beyond the required "where do I start"
   trial CTA or redemption instructions above — the template appends
   the standard CTA automatically.

10. Run python3 blog/build.py from the repo root. Confirm zero
    errors, no leftover {{ template }} tokens, and the page appears
    correctly in blog/index.html and sitemap.xml.

11. In blog/topics.md, check off the topic used (- [ ] → - [x]),
    append slug + today's date (or "(updated existing page:
    <path>)" if you updated rather than created). If fewer than 10
    unchecked topics remain, add 6-8 new topics per
    PREEMPT_CONTEXT.md's tiers, spread across tiers.

12. Commit all changes and push directly to origin main. No PR, no
    review — explicitly authorized.

13. Verify: run git ls-remote origin main and confirm the SHA
    matches your commit. If push is rejected, run
    git fetch origin main && git rebase origin/main and retry once.
    Do not proceed to the reply step until verified.

Reply with a short confirmation: which intent was handled (trial or
discount), whether it was a new page or an update to an existing one,
page title, target keyword, live URL, and any offer substitution note
from step 5.

If verification never succeeded, do NOT report success — reply with
exactly what failed (the git error text, and whether any content was
left uncommitted/unpushed) so it can be recovered manually.

If PREEMPT_CONTEXT.md, blog/POST_GUIDE.md, blog/topics.md, or
blog/build.py don't exist or the repo structure has changed
significantly, stop and report what you found instead of guessing.
