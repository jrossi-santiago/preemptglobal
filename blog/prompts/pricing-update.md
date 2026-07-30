You are handling a pricing-intent buy-intent topic for Preempt Global,
at github repo jrossi-santiago/preemptglobal (main branch is the live
site, auto-deployed — generated static HTML is committed directly, no
build step beyond blog/build.py).

First: read PREEMPT_CONTEXT.md at the repo root in full. It contains
the current, real pricing (a monthly retainer for unlimited set
reviews, and a one-time set review as the secondary offer) and the
$50K-exposure-or-free guarantee. If it conflicts with this prompt,
PREEMPT_CONTEXT.md wins.

GATE CHECK — do this before anything else:
Read blog/next_action.json. If route_to is NOT
"blog/prompts/pricing-update.md", stop immediately and reply with
exactly: "Not my topic — routed to <route_to> instead. No action
taken." Do not proceed past this point in that case.

If route_to IS "blog/prompts/pricing-update.md", continue below. Use
the topic and keyword from next_action.json — do not re-read
topics.md for the topic.

IMPORTANT CONTEXT — read before doing anything:
Unlike a typical B2B SaaS comparison blog, Preempt Global's own topic
bank never asks about a competitor's pricing — DECISION_TYPES.md's
rule 3 only matches a keyword that names a specific product/vendor's
price. In practice that means this routine fires when the keyword is
genuinely asking about Preempt Global's own price or cost (e.g.
"preempt global pricing," "how much does a document review cost").
Before writing anything, confirm that's actually the case. If the
keyword is really a generic industry cost/impact topic with no
pricing-lookup intent (the exact failure this rule was patched to
avoid — see DECISION_TYPES.md rule 3's non-match example), stop and
reply: "This looks miscategorized as pricing — <keyword> reads as
informational, not a pricing lookup. No action taken; flag for
reclassification." Do not guess at a workaround.

Do this, fully autonomously, no confirmation needed:

1. git fetch origin main && git reset --hard origin/main.

2. Read blog/POST_GUIDE.md in full for frontmatter/markdown rules.

3. Scan blog/posts/ for an existing page that already targets this
   same pricing/cost decision. If one exists, you will be updating it
   in place rather than creating a new file — open it, read it fully,
   and update rather than duplicate (matches next_action.json's
   existing_page value, if set).

4. Confirm the real, current figures before writing anything:
   - Never invent a number. Pull pricing straight from
     PREEMPT_CONTEXT.md's pricing section (retainer $7,000/mo for
     unlimited set reviews, one-time review $9,000 per review — both
     start with every deliverable included, and specific add-ons can be
     removed to lower the price), and cross-check against the live
     pricing page (pricing/index.html, id="tiers") since
     PREEMPT_CONTEXT.md itself notes pricing is subject to change.
   - If the two sources disagree, trust the live pricing page and note
     the discrepancy in your reply so PREEMPT_CONTEXT.md can be
     corrected.
   - State pricing as the two-offer structure it actually is (default
     to leading with the retainer as the lower cost per review) —
     do not invent a third tier or a per-project package.
   - Never call the retainer a "subscription" — it's B2B professional
     services language, not a SaaS plan.
   - Do not describe retainer capacity or client count as capped
     or limited in any way — that language was intentionally removed
     from the live site and should not be reintroduced.

5. Write or update the page as blog/posts/YYYY-MM-DD-slug.md (new) or
   in place (existing), 800–1,500 words. Complete frontmatter per
   POST_GUIDE.md. Primary keyword in title, slug, and first 100 words
   where natural. Cover: what's included in the core review (locked,
   non-removable), which add-ons can be unchecked to adjust price, the
   48-hour turnaround, the $50K-exposure-or-free guarantee (no partial
   credit, no fine print), and how a buyer should decide between the
   retainer and the one-time review. No invented discounts, no
   invented "starting at" figures beyond what the two offers actually
   state.

6. End the body with an FAQ section: 3–5 real searcher questions
   (check "People Also Ask"-style phrasings during research), each
   with a 2–4 sentence answer. Use the guide's FAQ/schema component if
   it defines one; otherwise render as H2 "Frequently Asked Questions"
   with H3 questions, and additionally emit valid FAQPage JSON-LD in a
   <script type="application/ld+json"> block if the guide's supported
   HTML allows raw script tags — if it doesn't, use plain headings
   only and note that in your reply.

7. Scan blog/posts/ for the 2–3 most topically related published
   posts and link to them contextually in the body (real anchor text,
   not "click here"). If nothing is related, skip rather than force it.

8. Do not write your own CTA — the template appends it automatically.

9. Run python3 blog/build.py from the repo root. Confirm zero errors
   and that blog/<slug>/index.html has no leftover {{ template }}
   tokens, and that the page appears correctly in the regenerated
   blog/index.html and sitemap.xml.

10. In blog/topics.md, check off the topic used (- [ ] → - [x]),
    append slug + today's date (or "(updated existing page: <path>)"
    if you updated rather than created), matching the "Already
    published" format. If fewer than 10 unchecked topics remain, add
    6–8 new topics per PREEMPT_CONTEXT.md's pricing offers, spread
    across the retainer and one-time review.

11. Commit all changes (new/updated post .md, generated
    blog/<slug>/index.html, regenerated blog/index.html, sitemap.xml,
    robots.txt, updated topics.md) with a clear commit message and
    push directly to origin main. No PR, no review — explicitly
    authorized.

12. Verify: run git ls-remote origin main and confirm the SHA matches
    the commit you just made. If the push is rejected (e.g.
    non-fast-forward) or fails, run
    git fetch origin main && git rebase origin/main (keep both your
    changes and any other changes when resolving straightforward
    conflicts) and retry the push once. Do not proceed to the reply
    step until the verified remote SHA matches your local commit.

Reply with a short confirmation: page title, whether it was a new
page or an update to an existing one, target keyword, live URL
(https://preemptglobal.com/blog/<slug>/), and any pricing discrepancy
noted in step 4.

If step 12's verification never succeeded, do NOT report success —
reply with exactly what failed (the git error text, and whether any
content was left uncommitted/unpushed) so it can be recovered
manually.

If PREEMPT_CONTEXT.md, blog/POST_GUIDE.md, blog/topics.md, or
blog/build.py don't exist or the repo structure has changed
significantly, stop and report what you found instead of guessing.
