#!/usr/bin/env python3
"""
Builds blog/<slug>/index.html and blog/index.html from blog/posts/*.md,
plus regenerates the root sitemap.xml and robots.txt.

Usage: python3 blog/build.py
No third-party dependencies beyond PyYAML (already available in this environment).
See blog/POST_GUIDE.md for the frontmatter schema and supported markdown.
"""
import json
import math
import re
import sys
from datetime import date, datetime
from pathlib import Path
from urllib.parse import quote

import yaml

BLOG_DIR = Path(__file__).resolve().parent
SITE_DIR = BLOG_DIR.parent
POSTS_DIR = BLOG_DIR / "posts"
SITE_URL = "https://preemptglobal.com"
DEFAULT_OG_IMAGE = "https://preemptglobal.com/preempt_global_logo.jpg"


# ---------- frontmatter + markdown parsing ----------

def parse_post(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.DOTALL)
    if not m:
        raise ValueError(f"{path.name}: missing YAML frontmatter (--- ... ---)")
    meta = yaml.safe_load(m.group(1)) or {}
    body = m.group(2).strip()

    required = ["title", "slug", "date", "description", "deck", "tags"]
    missing = [f for f in required if not meta.get(f)]
    if missing:
        raise ValueError(f"{path.name}: missing required frontmatter field(s): {', '.join(missing)}")

    d = meta["date"]
    if isinstance(d, (date, datetime)):
        meta["date"] = d.isoformat()[:10]
    meta["_source"] = path
    meta["_body"] = body
    return meta


def convert_inline(text: str) -> str:
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a class="inline-link" href="\2">\1</a>', text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", text)
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    return text


def convert_block(block: str) -> str:
    block = block.strip("\n")
    stripped = block.strip()

    if stripped.startswith("<"):
        return block  # raw HTML passthrough (pull-quote/callout/mini-report/takeaways snippets)

    img = re.match(r"^!\[([^\]]*)\]\(([^)]+)\)$", stripped)
    if img:
        alt, src = img.groups()
        return f'<img src="{src}" alt="{alt}">'

    lines = block.split("\n")

    if all(l.startswith("> ") or l == ">" for l in lines):
        joined = " ".join(l[2:] if l.startswith("> ") else "" for l in lines).strip()
        return f'<div class="pull-quote">{convert_inline(joined)}</div>'

    if all(re.match(r"^[-*]\s+", l) for l in lines):
        stripped_items = [re.sub(r"^[-*]\s+", "", l) for l in lines]
        items = "\n".join(f"    <li>{convert_inline(s)}</li>" for s in stripped_items)
        return f"  <ul>\n{items}\n  </ul>"

    if all(re.match(r"^\d+\.\s+", l) for l in lines):
        stripped_items = [re.sub(r"^\d+\.\s+", "", l) for l in lines]
        items = "\n".join(f"    <li>{convert_inline(s)}</li>" for s in stripped_items)
        return f"  <ol>\n{items}\n  </ol>"

    if stripped.startswith("### "):
        return f"  <h3>{convert_inline(stripped[4:])}</h3>"
    if stripped.startswith("## "):
        return f"  <h2>{convert_inline(stripped[3:])}</h2>"

    joined = " ".join(l.strip() for l in lines)
    cls = ' class="lede-p"' if block.startswith("!lede ") else ""
    if cls:
        joined = joined[len("!lede "):]
    return f"  <p{cls}>{convert_inline(joined)}</p>"


def markdown_to_html(body: str) -> str:
    blocks = re.split(r"\n\s*\n", body.strip())
    return "\n\n".join(convert_block(b) for b in blocks)


def strip_tags(html: str) -> str:
    return re.sub(r"<[^>]+>", " ", html)


def read_time(html: str) -> str:
    words = len(strip_tags(html).split())
    minutes = max(1, math.ceil(words / 225))
    return f"{minutes} min read"


def date_display(iso: str) -> str:
    return datetime.strptime(iso, "%Y-%m-%d").strftime("%B %-d, %Y") if sys.platform != "win32" \
        else datetime.strptime(iso, "%Y-%m-%d").strftime("%B %#d, %Y")


# ---------- rendering ----------

def inject_between(html: str, start_marker: str, end_marker: str, content: str) -> str:
    pattern = re.compile(re.escape(start_marker) + r".*?" + re.escape(end_marker), re.DOTALL)
    return pattern.sub(lambda _m: content, html, count=1)


def render_post(meta: dict, template: str, related_html: str) -> str:
    slug = meta["slug"]
    url = f"{SITE_URL}/blog/{slug}/"
    tags = meta.get("tags") or []
    tag_chips = "\n".join(f'      <span class="tag-chip">{t}</span>' for t in tags)
    content_html = markdown_to_html(meta["_body"])

    feature_file = meta["_source"].with_suffix("").with_suffix(".feature.html")
    feature_block = feature_file.read_text(encoding="utf-8") if feature_file.exists() else ""

    html = template
    html = inject_between(html, "<!--FEATURE_ART_START-->", "<!--FEATURE_ART_END-->", feature_block)

    replacements = {
        "{{TITLE}}": meta["title"],
        "{{TITLE_JSON}}": json.dumps(meta["title"]),
        "{{TITLE_URL}}": quote(meta["title"]),
        "{{DESCRIPTION}}": meta["description"],
        "{{DESCRIPTION_JSON}}": json.dumps(meta["description"]),
        "{{CANONICAL_URL}}": url,
        "{{OG_IMAGE}}": meta.get("og_image") or DEFAULT_OG_IMAGE,
        "{{DATE_ISO}}": meta["date"],
        "{{DATE_DISPLAY}}": date_display(meta["date"]),
        "{{READ_TIME}}": read_time(content_html),
        "{{PRIMARY_TAG}}": tags[0] if tags else "Insights",
        "{{TAG_CHIPS}}": tag_chips,
        "{{DECK}}": meta["deck"],
        "{{CONTENT}}": content_html,
    }
    for token, value in replacements.items():
        html = html.replace(token, value)

    html = inject_between(html, "<!--RELATED_START-->", "<!--RELATED_END-->", related_html)
    return html


def render_related(all_posts: list, current_slug: str) -> str:
    others = [p for p in all_posts if p["slug"] != current_slug][:3]
    if not others:
        return ""
    cards = []
    for p in others:
        tag = (p.get("tags") or ["Insights"])[0]
        rt = read_time(markdown_to_html(p["_body"]))
        cards.append(
            f'      <a class="related-card" href="/blog/{p["slug"]}/">\n'
            f'        <span class="rc-tag">{tag}</span>\n'
            f'        <h4>{p["title"]}</h4>\n'
            f'        <span class="rc-meta">{rt}</span>\n'
            f'      </a>'
        )
    return (
        '<section class="related">\n'
        '  <div class="article-wrap">\n'
        '    <p class="kicker">Keep reading</p>\n'
        '    <h2 style="margin-top:8px;">More from the field</h2>\n'
        '    <div class="related-grid">\n'
        + "\n".join(cards) +
        '\n    </div>\n  </div>\n</section>'
    )


def render_index(all_posts: list, index_template: str) -> str:
    cards = []
    for p in all_posts:
        tag = (p.get("tags") or ["Insights"])[0]
        rt = read_time(markdown_to_html(p["_body"]))
        cards.append(
            f'      <a class="post-card" href="/blog/{p["slug"]}/">\n'
            f'        <span class="pc-tag">{tag}</span>\n'
            f'        <h3>{p["title"]}</h3>\n'
            f'        <p>{p["deck"]}</p>\n'
            f'        <span class="pc-meta"><time datetime="{p["date"]}">{date_display(p["date"])}</time> · {rt}</span>\n'
            f'      </a>'
        )
    cards_html = "\n".join(cards) if cards else '      <p class="pc-empty">First post coming soon.</p>'
    return index_template.replace("{{POST_CARDS}}", cards_html)


def build_sitemap(all_posts: list) -> str:
    static_pages = ["", "findings/", "handoff/", "send/", "blog/"]
    urls = [f"{SITE_URL}/{p}" for p in static_pages]
    urls += [f"{SITE_URL}/blog/{p['slug']}/" for p in all_posts]
    entries = "\n".join(f"  <url><loc>{u}</loc></url>" for u in urls)
    return f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{entries}\n</urlset>\n'


def build_robots() -> str:
    return f"User-agent: *\nAllow: /\nSitemap: {SITE_URL}/sitemap.xml\n"


def main():
    template = (BLOG_DIR / "template.html").read_text(encoding="utf-8")
    index_template = (BLOG_DIR / "index_template.html").read_text(encoding="utf-8")

    post_files = sorted(POSTS_DIR.glob("*.md"))
    if not post_files:
        print("No posts found in blog/posts/", file=sys.stderr)

    posts = [parse_post(p) for p in post_files]
    posts.sort(key=lambda p: p["date"], reverse=True)

    slugs = [p["slug"] for p in posts]
    if len(slugs) != len(set(slugs)):
        raise ValueError("Duplicate slug detected across posts/*.md")

    for meta in posts:
        related_html = render_related(posts, meta["slug"])
        html = render_post(meta, template, related_html)
        out_dir = BLOG_DIR / meta["slug"]
        out_dir.mkdir(parents=True, exist_ok=True)
        (out_dir / "index.html").write_text(html, encoding="utf-8")
        print(f"built blog/{meta['slug']}/index.html")

    (BLOG_DIR / "index.html").write_text(render_index(posts, index_template), encoding="utf-8")
    print("built blog/index.html")

    (SITE_DIR / "sitemap.xml").write_text(build_sitemap(posts), encoding="utf-8")
    (SITE_DIR / "robots.txt").write_text(build_robots(), encoding="utf-8")
    print("built sitemap.xml and robots.txt")


if __name__ == "__main__":
    main()
