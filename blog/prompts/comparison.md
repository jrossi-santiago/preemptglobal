You are writing a buy-intent comparison or alternatives page for
Preempt Global, at github repo jrossi-santiago/preemptglobal (main
branch is the live site, auto-deployed — generated static HTML is
committed directly, no build step beyond blog/build.py).

First: read PREEMPT_CONTEXT.md at the repo root in full. It defines
the business, voice, SEO keyword tiers, competitors, and cross-agent
guardrails. If it conflicts with this prompt, PREEMPT_CONTEXT.md wins.

GATE CHECK — do this before anything else:
Read blog/next_action.json. If route_to is NOT
"blog/prompts/comparison.md", stop immediately and reply with exactly:
"Not my topic — routed to <route_to> instead. No action taken."
Do not proceed past this point in that case.

If route_to IS "blog/prompts/comparison.md", continue below. Use the
topic, keyword, and decision_type values from next_action.json — do
not re-read topics.md.

Do this, fully autonomously, no confirmation needed:

1. git fetch origin main && git reset --hard origin/main.

2. Read blog/POST_GUIDE.md in full — exact frontmatter schema and
   supported markdown/HTML. Follow it exactly.

3. Check decision_type from next_action.json — it will be either
   "alternatives" or "comparison". The two are close but not
   identical:

   IF "alternatives" (e.g. "asana alternatives"):
   - The reader already knows the named product and wants a reason
     to switch.
   - Research and list 3-5 real alternatives, using web search for
     current pricing, features, and positioning — never invent a
     price or feature you can't confirm from a source.
   - For each alternative, cover: why someone would switch to it,
     price/contract differences vs. the named product, features the
     named product lacks, migration effort, and who it's the best
     fit for.
   - End with a clear "who should choose what" verdict — do not just
     summarize each competitor's homepage.

   IF "comparison" (e.g. "asana vs monday"):
   - This is a head-to-head between exactly two named products.
   - Research current pricing and features for both, using web
     search — never invent numbers.
   - Compare both products using the SAME criteria for each (pricing,
     core features, ease of use, integrations, support, etc.) —
     do not use different categories for each product.
   - Explicitly state where each product wins, including where our
     product (if one of the two is Preempt Global's own) loses or
     falls short. If your product wins every single row, stop and
     rewrite — that means you wrote an ad, not a comparison.
   - End with a verdict broken out by buyer type (e.g. "best for
     small teams," "best for agencies") and the correct next step for
     each.

4. Write the full page, 1,500–2,500 words, as
   blog/posts/YYYY-MM-DD-slug.md (today's date, URL-safe slug from
   the title, primary keyword in title and slug where it reads
   naturally). Complete frontmatter per the guide. Primary keyword in
   the first 100 words, at least one H2, and the meta description —
   natural, never stuffed.

5. Required evidence — do not publish without these:
   - Current, sourced pricing for every product named (not
     estimated).
   - A comparison table or clearly structured criteria section (same
     criteria applied to every product).
   - A named verdict/recommendation section — never end on "it
     depends" with no guidance.

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
   tokens, and that the new post appears in the regenerated
   blog/index.html and sitemap.xml.

10. In blog/topics.md, check off the topic used (- [ ] → - [x]),
    append slug + today's date matching the "Already published"
    format. If fewer than 10 unchecked topics remain, add 6–8 new
    topics to the bottom, each mapped to a specific keyword from
    PREEMPT_CONTEXT.md's tiers, spread across tiers rather than all
    Tier 3.

11. Commit all changes (new post .md, generated blog/<slug>/index.html,
    regenerated blog/index.html, sitemap.xml, robots.txt, updated
    topics.md) with a clear commit message and push directly to
    origin main. No PR, no review — explicitly authorized.

12. Verify: run git ls-remote origin main and confirm the SHA matches
    the commit you just made. If the push is rejected (e.g.
    non-fast-forward) or fails, run
    git fetch origin main && git rebase origin/main (keep both your
    new post and any other changes when resolving straightforward
    conflicts) and retry the push once. Do not proceed to the reply
    step until the verified remote SHA matches your local commit.

Reply with a short confirmation: page title, decision_type used
(alternatives or comparison), target keyword, live URL
(https://preemptglobal.com/blog/<slug>/), and which internal links
were added.

If step 12's verification never succeeded, do NOT report success —
reply with exactly what failed (the git error text, and whether any
content was left uncommitted/unpushed) so it can be recovered
manually.

If PREEMPT_CONTEXT.md, blog/POST_GUIDE.md, blog/topics.md, or
blog/build.py don't exist or the repo structure has changed
significantly, stop and report what you found instead of guessing.
