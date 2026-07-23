You are writing a standard informational blog post for Preempt Global,
at github repo jrossi-santiago/preemptglobal (main branch is the live
site, auto-deployed — generated static HTML is committed directly, no
build step beyond blog/build.py).

First: read PREEMPT_CONTEXT.md at the repo root in full. It defines
the business, voice, SEO keyword tiers, and cross-agent guardrails. If
it conflicts with this prompt, PREEMPT_CONTEXT.md wins.

GATE CHECK — do this before anything else:
Read blog/next_action.json. If route_to is NOT
"blog/prompts/daily-post.md", stop immediately and reply with exactly:
"Not my topic — routed to <route_to> instead. No action taken." Do
not proceed past this point in that case.

If route_to IS "blog/prompts/daily-post.md", continue below. Use the
topic and keyword from next_action.json — do not re-read topics.md
for the topic.

This is the default/fallback content type: how-to, guide, "what is",
explainer, or listicle content that isn't buy-intent (no named
product/vendor comparison, no pricing check, no review-checking, no
trial/discount). The reader is trying to understand a problem, not
choose between two named options — write to inform first; hire-me
intent follows from being useful, not from selling in the body.

Do this, fully autonomously, no confirmation needed:

1. git fetch origin main && git reset --hard origin/main.

2. Read blog/POST_GUIDE.md in full — exact frontmatter schema and
   supported markdown/HTML. Follow it exactly.

3. Research the topic as needed, using web search for any factual
   claim, statistic, or industry data point. Never invent a number,
   study, or source. If a specific figure can't be confirmed, describe
   the situation qualitatively instead of guessing a number.

4. Write the full page, 1,200–2,000 words, as
   blog/posts/YYYY-MM-DD-slug.md (today's date, URL-safe slug from
   the title, primary keyword in title and slug where it reads
   naturally). Complete frontmatter per the guide. Primary keyword in
   the first 100 words, at least one H2, and the meta description —
   natural, never stuffed. Match the voice in PREEMPT_CONTEXT.md:
   concrete, numbers-driven, no filler.

5. Structure for the reader's actual question — use the keyword and
   topic title to figure out what they're trying to learn, and answer
   that directly rather than working around to it. Use the guide's
   callout, mini-report, and takeaways components where they fit a
   concrete fact or number worth pulling out; skip them if nothing
   fits rather than forcing one in.

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

Reply with a short confirmation: page title, target keyword, live URL
(https://preemptglobal.com/blog/<slug>/), and which internal links
were added.

If step 12's verification never succeeded, do NOT report success —
reply with exactly what failed (the git error text, and whether any
content was left uncommitted/unpushed) so it can be recovered
manually.

If PREEMPT_CONTEXT.md, blog/POST_GUIDE.md, blog/topics.md, or
blog/build.py don't exist or the repo structure has changed
significantly, stop and report what you found instead of guessing.
