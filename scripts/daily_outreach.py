#!/usr/bin/env python3
"""Daily outreach summary generator.

Pure logic only: filtering, channel selection, calendar cross-check, and HTML
rendering. It does not talk to Airtable, Google Calendar, or Gmail directly --
those require the account-linked connectors that only the Claude agent
running the daily Trigger can reach. The Trigger prompt fetches the raw data
via MCP tools, writes it to JSON, and calls this script to turn it into the
actual email.

Usage:
    python3 daily_outreach.py --records records.json --events events.json \
        --today 2026-07-21 --out email.json

    python3 daily_outreach.py --error "Airtable fetch failed: 401 Unauthorized" \
        --today 2026-07-21 --out email.json

Input formats
-------------
records.json: list of objects with keys
    id, name, company, title, linkedin_url, source_signal,
    date_first_contacted, contact_method, status, followup_date,
    followup_done, notes

events.json: list of objects with keys
    summary, description, start (ISO string), attendee_emails (list[str])
    (today's Google Calendar events; omit/empty if Calendar isn't connected)

Output (--out): JSON with keys subject, html, log_line
"""

import argparse
import json
import re
import sys
from datetime import date

EMAIL_RE = re.compile(r"[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}")
PHONE_RE = re.compile(r"(\+?1[\s\-.])?\(?\d{3}\)?[\s\-.]\d{3}[\s\-.]\d{4}")

DEAD_STATUS = "Dead"

CHANNEL_ORDER = ["Email", "LinkedIn", "Call/Text", "Other"]


def find_email(*texts):
    for text in texts:
        if not text:
            continue
        match = EMAIL_RE.search(text)
        if match:
            return match.group(0)
    return None


def find_phone(*texts):
    for text in texts:
        if not text:
            continue
        match = PHONE_RE.search(text)
        if match:
            return match.group(0).strip()
    return None


def pick_channel(contact):
    """Returns (channel, contact_value) per Email > LinkedIn > Call/Text > Other."""
    searchable = (contact.get("title"), contact.get("notes"), contact.get("source_signal"))
    email = find_email(*searchable)
    if email:
        return "Email", email
    linkedin = contact.get("linkedin_url")
    if linkedin:
        return "LinkedIn", linkedin
    phone = find_phone(*searchable)
    if phone:
        return "Call/Text", phone
    return "Other", None


def needs_outreach(contact, today):
    followup_date = contact.get("followup_date")
    if not followup_date:
        return False
    if followup_date > today:
        return False
    if (contact.get("status") or "").strip() == DEAD_STATUS:
        return False
    return True


def matches_contact(name, *texts):
    if not name:
        return False
    name_lower = name.lower()
    # also try last token (surname) for loose matches like "Follow up: Sage Olsen"
    tokens = [t for t in re.split(r"[\s,]+", name_lower) if len(t) > 1]
    for text in texts:
        if not text:
            continue
        text_lower = text.lower()
        if name_lower in text_lower:
            return True
        if tokens and all(tok in text_lower for tok in tokens):
            return True
    return False


def find_calendar_match(contact, events):
    for event in events:
        haystacks = [event.get("summary"), event.get("description")]
        haystacks.extend(event.get("attendee_emails") or [])
        if matches_contact(contact.get("name"), *haystacks):
            return event
    return None


def context_for(contact):
    parts = []
    if contact.get("notes"):
        parts.append(contact["notes"].strip())
    if contact.get("source_signal"):
        parts.append(contact["source_signal"].strip())
    return " — ".join(parts) if parts else "(no notes on file)"


def html_escape(text):
    if text is None:
        return ""
    return (
        str(text)
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )


def render_contact_row(contact, channel_value):
    name = html_escape(contact.get("name") or "Unknown")
    company = html_escape(contact.get("company"))
    linkedin = contact.get("linkedin_url")
    notes = html_escape(context_for(contact))
    followup_date = html_escape(contact.get("followup_date"))

    header = name
    if company:
        header += f" &mdash; {company}"

    links = []
    if linkedin:
        links.append(f'<a href="{html_escape(linkedin)}">LinkedIn profile</a>')
    links_html = f'<div style="margin:2px 0;">{" | ".join(links)}</div>' if links else ""

    contact_value_html = ""
    if channel_value and channel_value != linkedin:
        contact_value_html = f'<div style="margin:2px 0;color:#333;">{html_escape(channel_value)}</div>'

    return f"""
    <li style="margin-bottom:14px;">
      <div style="font-weight:600;">{header}</div>
      <div style="font-size:12px;color:#888;">Follow-up due: {followup_date}</div>
      {contact_value_html}
      {links_html}
      <div style="font-size:13px;color:#444;margin-top:2px;">{notes}</div>
    </li>"""


def render_scheduled_row(contact, event):
    name = html_escape(contact.get("name") or "Unknown")
    company = html_escape(contact.get("company"))
    summary = html_escape(event.get("summary") or "")
    start = html_escape(event.get("start") or "")
    header = name
    if company:
        header += f" &mdash; {company}"
    return f"""
    <li style="margin-bottom:8px;">
      <div style="font-weight:600;">{header}</div>
      <div style="font-size:13px;color:#444;">Already on calendar: "{summary}" at {start}</div>
    </li>"""


def build_email(contacts, events, today):
    today_display = date.fromisoformat(today).strftime("%B %-d, %Y")
    subject = f"Daily Outreach List — {today_display}"

    due = [c for c in contacts if needs_outreach(c, today)]

    grouped = {ch: [] for ch in CHANNEL_ORDER}
    scheduled_today = []

    for contact in due:
        event = find_calendar_match(contact, events) if events else None
        if event:
            scheduled_today.append((contact, event))
            continue
        channel, value = pick_channel(contact)
        grouped[channel].append((contact, value))

    total_outreach = sum(len(v) for v in grouped.values())

    if total_outreach == 0 and not scheduled_today:
        html = f"""
        <div style="font-family:-apple-system,Segoe UI,Arial,sans-serif;max-width:600px;">
          <h2 style="margin-bottom:4px;">Daily Outreach List &mdash; {html_escape(today_display)}</h2>
          <p style="color:#555;">Nothing on deck today. No contacts have a follow-up due, and nothing overdue is unresolved.</p>
          <p style="font-size:12px;color:#999;">(This confirms the routine ran successfully this morning.)</p>
        </div>"""
        log_line = f"contacts_due=0 scheduled_today=0"
        return subject, html, log_line

    sections_html = ""
    for channel in CHANNEL_ORDER:
        items = grouped[channel]
        if not items:
            continue
        rows = "".join(render_contact_row(c, v) for c, v in items)
        sections_html += f"""
        <h3 style="margin-bottom:6px;border-bottom:2px solid #eee;padding-bottom:4px;">{channel} ({len(items)})</h3>
        <ul style="list-style:none;padding-left:0;margin-top:0;">{rows}</ul>"""

    scheduled_html = ""
    if scheduled_today:
        rows = "".join(render_scheduled_row(c, e) for c, e in scheduled_today)
        scheduled_html = f"""
        <h3 style="margin-top:24px;margin-bottom:6px;color:#777;">Already scheduled today ({len(scheduled_today)})</h3>
        <ul style="list-style:none;padding-left:0;">{rows}</ul>"""

    html = f"""
    <div style="font-family:-apple-system,Segoe UI,Arial,sans-serif;max-width:600px;">
      <h2 style="margin-bottom:4px;">Daily Outreach List &mdash; {html_escape(today_display)}</h2>
      <p style="color:#555;margin-top:0;">{total_outreach} contact(s) need outreach today.</p>
      {sections_html}
      {scheduled_html}
    </div>"""

    log_line = f"contacts_due={total_outreach} scheduled_today={len(scheduled_today)}"
    return subject, html, log_line


def build_error_email(error_message, today):
    today_display = date.fromisoformat(today).strftime("%B %-d, %Y")
    subject = f"Daily Outreach List — RUN FAILED — {today_display}"
    html = f"""
    <div style="font-family:-apple-system,Segoe UI,Arial,sans-serif;max-width:600px;">
      <h2 style="color:#b00020;">Daily outreach routine failed this morning</h2>
      <p>The 4am run on {html_escape(today_display)} did not complete. No outreach list was generated.</p>
      <p style="background:#f5f5f5;padding:10px;border-radius:4px;font-family:monospace;font-size:13px;">{html_escape(error_message)}</p>
      <p style="color:#777;font-size:13px;">Check the log at logs/daily_outreach.log for details.</p>
    </div>"""
    log_line = f"run=fail error={error_message!r}"
    return subject, html, log_line


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--records", help="Path to Airtable records JSON")
    parser.add_argument("--events", help="Path to today's Calendar events JSON")
    parser.add_argument("--today", required=True, help="ISO date, e.g. 2026-07-21")
    parser.add_argument("--out", required=True, help="Path to write output JSON")
    parser.add_argument("--error", help="If set, generate a failure email instead")
    args = parser.parse_args()

    if args.error:
        subject, html, log_line = build_error_email(args.error, args.today)
    else:
        if not args.records:
            print("--records is required unless --error is set", file=sys.stderr)
            sys.exit(1)
        with open(args.records) as f:
            contacts = json.load(f)
        events = []
        if args.events:
            with open(args.events) as f:
                events = json.load(f)
        subject, html, log_line = build_email(contacts, events, args.today)

    with open(args.out, "w") as f:
        json.dump({"subject": subject, "html": html, "log_line": log_line}, f, indent=2)

    print(log_line)


if __name__ == "__main__":
    main()
