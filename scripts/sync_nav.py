#!/usr/bin/env python3
"""
Syncs the header nav (desktop + mobile) and footer link row across every
page from the partials in partials/ — mainly partials/comparisons.json.

Usage: python3 scripts/sync_nav.py
No third-party dependencies.

To add a new comparison page to the "Comparisons" dropdown site-wide:
  1. Add an entry to partials/comparisons.json
  2. Run this script
  3. Commit the result

The first run on a page adopts its existing nav/footer markup by wrapping
it in <!-- NAME:START --> / <!-- NAME:END --> markers; every run after
that just replaces the content between the markers, so this is safe to
re-run any time (including on brand-new pages copied from an existing one).
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PARTIALS = ROOT / "partials"

LAST_LINK = {
    "faq": {
        "desktop": '<a href="{PREFIX}#faq" class="hover-underline">FAQ</a>',
        "mobile": '<a href="{PREFIX}#faq" class="py-3.5">FAQ</a>',
    },
    "blog": {
        "desktop": '<a href="/blog" class="hover-underline text-[#FF5722]">Blog</a>',
        "mobile": '<a href="/blog" class="py-3.5 text-[#FF5722]">Blog</a>',
    },
}

MARKERS = [
    # (name, legacy_start_needle, legacy_end_tag)
    ("NAV_DESKTOP", '<nav class="hidden lg:flex items-center gap-8 mono text-[13px] tracking-wide uppercase">', "</nav>"),
    ("NAV_MOBILE", '<nav id="mobile-nav"', "</nav>"),
    ("FOOTER_LINKS", '<nav class="mono text-[11px] uppercase tracking-wide flex gap-6 text-[#1A1A1A]/60">', "</nav>"),
]


def detect_variant(rel_path: Path) -> str:
    if rel_path == Path("index.html"):
        return "home"
    if rel_path.parts[0] == "blog":
        return "blog"
    return "sub"


def render_comparisons(items: list) -> tuple[str, str]:
    desktop_parts, mobile_parts = [], []
    for i, item in enumerate(items):
        last = i == len(items) - 1
        d_cls = "block px-4 py-3 text-[13px] hover:bg-[#FF5722]/10" if last \
            else "block px-4 py-3 border-b border-[#1A1A1A]/10 text-[13px] hover:bg-[#FF5722]/10"
        m_cls = "block py-2 pb-2.5 pl-3 normal-case tracking-normal text-[13px]" if last \
            else "block py-2 pl-3 normal-case tracking-normal text-[13px]"
        desktop_parts.append(f'<a href="{item["path"]}" class="{d_cls}">{item["label"]}</a>')
        mobile_parts.append(f'<a href="{item["path"]}" class="{m_cls}">{item["label"]}</a>')
    return "".join(desktop_parts), "".join(mobile_parts)


def render_nav(templates: dict, prefix: str, lastlink_kind: str, comparisons: list) -> tuple[str, str]:
    comp_desktop, comp_mobile = render_comparisons(comparisons)
    last_desktop = LAST_LINK[lastlink_kind]["desktop"].format(PREFIX=prefix)
    last_mobile = LAST_LINK[lastlink_kind]["mobile"].format(PREFIX=prefix)

    desktop = (templates["nav_desktop"]
               .replace("{{PREFIX}}", prefix)
               .replace("{{COMPARISONS_DESKTOP}}", comp_desktop)
               .replace("{{LAST_LINK_DESKTOP}}", last_desktop))
    mobile = (templates["nav_mobile"]
              .replace("{{PREFIX}}", prefix)
              .replace("{{COMPARISONS_MOBILE}}", comp_mobile)
              .replace("{{LAST_LINK_MOBILE}}", last_mobile))
    return desktop, mobile


def apply_marker(text: str, name: str, new_content: str, legacy_start: str, legacy_end_tag: str) -> str:
    start_marker, end_marker = f"<!-- {name}:START -->", f"<!-- {name}:END -->"

    si = text.find(start_marker)
    if si != -1:
        ei = text.find(end_marker, si)
        if ei == -1:
            raise ValueError(f"unterminated {name} marker")
        return text[:si] + start_marker + new_content + end_marker + text[ei + len(end_marker):]

    ls = text.find(legacy_start)
    if ls == -1:
        return text  # this page doesn't have this element
    le = text.find(legacy_end_tag, ls)
    if le == -1:
        raise ValueError(f"couldn't find end of legacy {name} block")
    return text[:ls] + start_marker + new_content + end_marker + text[le + len(legacy_end_tag):]


def main():
    comparisons = json.loads((PARTIALS / "comparisons.json").read_text(encoding="utf-8"))
    templates = {
        "nav_desktop": (PARTIALS / "nav-desktop.html").read_text(encoding="utf-8"),
        "nav_mobile": (PARTIALS / "nav-mobile.html").read_text(encoding="utf-8"),
        "footer_links": (PARTIALS / "footer-links.html").read_text(encoding="utf-8"),
    }

    updated = []
    for path in sorted(ROOT.rglob("*.html")):
        rel = path.relative_to(ROOT)
        if rel.parts[0] == "partials" or ".feature." in path.name:
            continue

        variant = detect_variant(rel)
        prefix = "" if variant == "home" else "/"
        lastlink_kind = "blog" if variant == "blog" else "faq"
        nav_desktop, nav_mobile = render_nav(templates, prefix, lastlink_kind, comparisons)
        footer_links = templates["footer_links"].replace("{{PREFIX}}", prefix)
        rendered = {"NAV_DESKTOP": nav_desktop, "NAV_MOBILE": nav_mobile, "FOOTER_LINKS": footer_links}

        text = original = path.read_text(encoding="utf-8")
        for name, legacy_start, legacy_end_tag in MARKERS:
            text = apply_marker(text, name, rendered[name], legacy_start, legacy_end_tag)

        if text != original:
            path.write_text(text, encoding="utf-8")
            updated.append(str(rel))

    if updated:
        print(f"Synced nav/footer in {len(updated)} file(s):")
        for u in updated:
            print(f"  {u}")
    else:
        print("Nav/footer already in sync — no changes.")


if __name__ == "__main__":
    main()
