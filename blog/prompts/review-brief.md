You are handling a review-intent buy-intent topic for Preempt Global,
at github repo jrossi-santiago/preemptglobal (main branch is the live
site, auto-deployed — generated static HTML is committed directly, no
build step beyond blog/build.py).

First: read PREEMPT_CONTEXT.md at the repo root in full. If it
conflicts with this prompt, PREEMPT_CONTEXT.md wins.

GATE CHECK — do this before anything else:
Read blog/next_action.json. If route_to is NOT
"blog/prompts/review-brief.md", stop immediately and reply with
exactly: "Not my topic — routed to <route_to> instead. No action
taken." Do not proceed past this point in that case.

If route_to IS "blog/prompts/review-brief.md", continue below. Use
the topic and keyword from next_action.json — do not re-read
topics.md for the topic.

IMPORTANT CONTEXT — read before doing anything:
Review-intent searches ("is [product] good", "[product] review") are
different from every other buy-intent type. The buyer wants proof
from somebody OTHER than the company itself. A self-published "our
product is great" page on our own domain does not satisfy this intent
and should not be the main deliverable. This routine produces:
  (a) a short on-site "facts page" that makes the product easy to
      verify (real screenshots-ready facts, current pricing, real
      limitations — nothing promotional), and
  (b) an outreach brief — NOT published to the live site — listing
      where and how to pursue real third-party reviews.
The outreach brief is the primary output. The on-site page is
secondary and small.

Do this, fully autonomously, no confirmation needed:

1. git fetch origin main && git reset --hard origin/main.

2. Read blog/POST_GUIDE.md in full for frontmatter/markdown rules.

3. Research, using web search:
   - Current product facts: pricing, core features, known
     limitations. Never invent a number or feature.
   - Where competitors or comparable products get reviewed: which
     independent sites, roundups, communities, or publications
     currently review products in this category. Note real,
     currently-active outlets only — do not invent publication names.
   - What existing review coverage (if any) already exists for this
     product, positive or negative.

4. Build the on-site facts page, blog/posts/YYYY-MM-DD-slug.md,
   600-1,000 words (shorter than a normal post — this is a reference
   page, not a narrative one):
   - Complete frontmatter per POST_GUIDE.md.
   - Primary keyword in title, slug, and first 100 words where
     natural.
   - Content: current pricing, core features, honest limitations
     (do not omit real limitations — a page with no downsides reads
     as promotional and undermines the goal), and where to find
     independent coverage if any exists.
   - No sales language, no CTA-style claims. State facts plainly.
   - End with an FAQ section: 3-5 real searcher questions, each with
     a 2-4 sentence answer. Use the guide's FAQ/schema component if
     it defines one; otherwise H2 "Frequently Asked Questions" with
     H3 questions, plus FAQPage JSON-LD if raw script tags are
     supported — otherwise plain headings, note this in your reply.
   - Scan blog/posts/ for 2-3 related published posts and link
     contextually. Skip if nothing fits.
   - Do not write a CTA — the template appends it automatically.

5. Build the outreach brief as a SEPARATE file:
   blog/outreach/YYYY-MM-DD-slug-review-brief.md
   This file is NOT part of the published site and must NOT be run
   through build.py or linked from any live page. It should contain:
   - The product facts a third-party reviewer would need (pricing,
     features, limitations, screenshots-worth-taking list).
   - A list of the specific independent outlets/communities/roundups
     found in research, with a one-line note on why each is a fit.
   - A suggested named-author angle (per the PDF's finding that 89%
     of ranking reviews have a byline) — i.e., what a credible
     independent reviewer would need to write something real.
   - This is a working document for a human to act on manually (e.g.
     outreach emails, PR, product seeding) — not something to be
     auto-published or auto-sent anywhere.

6. Run python3 blog/build.py from the repo root. Confirm zero errors,
   no leftover {{ template }} tokens, and that the on-site facts page
   (not the outreach brief) appears in blog/index.html and
   sitemap.xml.

7. In blog/topics.md, check off the topic used (- [ ] → - [x]),
   append slug + today's date matching "Already published" format,
   noting "(review-brief: outreach doc created, not published)". If
   fewer than 10 unchecked topics remain, add 6-8 new topics per
   PREEMPT_CONTEXT.md's tiers, spread across tiers.

8. Commit all changes (on-site page, generated HTML, blog/index.html,
   sitemap.xml, robots.txt, updated topics.md, AND the outreach brief
   file) with a clear commit message and push directly to origin
   main. No PR, no review — explicitly authorized. (Committing the
   outreach brief to the repo is fine — it's just not published as a
   live page.)

9. Verify: run git ls-remote origin main and confirm the SHA matches
   your commit. If push is rejected, run
   git fetch origin main && git rebase origin/main and retry once.
   Do not proceed to the reply step until verified.

Reply with a short confirmation: on-site page title and URL, and a
one-line summary of what's in the outreach brief (how many outlets
identified) plus its file path so it can be reviewed manually.

If verification never succeeded, do NOT report success — reply with
exactly what failed (the git error text, and whether any content was
left uncommitted/unpushed) so it can be recovered manually.

If PREEMPT_CONTEXT.md, blog/POST_GUIDE.md, blog/topics.md, or
blog/build.py don't exist or the repo structure has changed
significantly, stop and report what you found instead of guessing.
