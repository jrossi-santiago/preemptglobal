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
from datetime import date, datetime

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


DATE_LINE_RE = re.compile(r"(\d{1,2}/\d{1,2})\s*[—\-:]\s*(.+)$")


def parse_timeline(contact):
    """Turns Source Signal + Notes into a chronological (date_label, text) log.

    Notes are typically written as dated lines already (e.g. "7/15 — Messaged
    Ray..."); this just splits on those markers instead of dumping the raw
    blob, so the email reads as a history instead of a paragraph.
    """
    entries = []
    source_signal = (contact.get("source_signal") or "").strip()
    if source_signal:
        entries.append((None, source_signal))

    notes = (contact.get("notes") or "").strip()
    for raw_line in notes.split("\n"):
        raw_line = raw_line.strip()
        if not raw_line:
            continue
        match = DATE_LINE_RE.search(raw_line)
        if match:
            entries.append((match.group(1), match.group(2).strip()))
        else:
            entries.append((None, raw_line))
    return entries


def short_today(today):
    d = date.fromisoformat(today)
    return f"{d.month}/{d.day}"


def html_escape(text):
    if text is None:
        return ""
    return (
        str(text)
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )


def due_phrase(followup_date, today):
    days_over = (date.fromisoformat(today) - date.fromisoformat(followup_date)).days
    if days_over <= 0:
        return "due today"
    if days_over == 1:
        return "a day overdue"
    return f"{days_over} days overdue"


def format_time(iso_str):
    try:
        return datetime.fromisoformat(iso_str).strftime("%-I:%M %p")
    except (ValueError, TypeError):
        return iso_str or ""


def channel_sentence(channel, value, linkedin):
    if channel == "Email":
        return f"Reach out by email — {value}"
    if channel == "LinkedIn":
        return f"Reach out on LinkedIn — {linkedin}"
    if channel == "Call/Text":
        return f"Reach out by call or text — {value}"
    return "No direct contact info on file — check LinkedIn or your notes"


def render_contact_row(contact, channel, value, today):
    name = html_escape(contact.get("name") or "Unknown")
    company = html_escape(contact.get("company"))
    linkedin = contact.get("linkedin_url")

    header = name
    if company:
        header += f" <span style=\"font-weight:400;color:#777;\">({company})</span>"

    history_lines = ""
    for date_label, text in parse_timeline(contact):
        label = html_escape(date_label) if date_label else "&nbsp;&nbsp;&nbsp;"
        history_lines += f"""
        <div style="font-size:13px;color:#666;margin-top:3px;"><span style="display:inline-block;width:38px;color:#999;">{label}</span>&mdash; {html_escape(text)}</div>"""

    due = due_phrase(contact.get("followup_date"), today)
    action = channel_sentence(channel, value, linkedin)
    action_line = f"""
        <div style="font-size:14px;color:#111;font-weight:600;margin-top:6px;"><span style="display:inline-block;width:38px;color:#999;font-weight:400;">{short_today(today)}</span>&mdash; {html_escape(action)} <span style="font-weight:400;color:#999;">({due})</span></div>"""

    return f"""
    <div style="margin-bottom:20px;">
      <div style="font-weight:600;font-size:15px;">{header}</div>
      {history_lines}
      {action_line}
    </div>"""


def render_scheduled_row(contact, event):
    name = html_escape(contact.get("name") or "Unknown")
    company = html_escape(contact.get("company"))
    summary = html_escape(event.get("summary") or "a meeting")
    time_str = html_escape(format_time(event.get("start")))
    who = name
    if company:
        who += f" ({company})"
    when = f" at {time_str}" if time_str else ""
    return f"""
    <div style="font-size:14px;color:#333;margin-bottom:6px;">
      <strong>{who}</strong> &mdash; already on your calendar today{when} ("{summary}"). No outreach needed.
    </div>"""


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
        grouped[channel].append((contact, channel, value))

    total_outreach = sum(len(v) for v in grouped.values())

    if total_outreach == 0 and not scheduled_today:
        html = f"""
        <div style="font-family:-apple-system,Segoe UI,Arial,sans-serif;max-width:600px;font-size:15px;color:#222;">
          <p>Morning — nothing on your outreach list today. No follow-ups are due, and nothing's overdue.</p>
          <p style="color:#999;font-size:12px;">(Just confirming the routine ran fine this morning — no action needed from you.)</p>
        </div>"""
        log_line = "contacts_due=0 scheduled_today=0"
        return subject, html, log_line

    people_word = "person" if total_outreach == 1 else "people"
    intro = f"Morning — {total_outreach} {people_word} to reach out to today."
    if scheduled_today:
        cal_word = "person" if len(scheduled_today) == 1 else "people"
        intro += f" Also flagging {len(scheduled_today)} {cal_word} already on your calendar, so no separate nudge needed there."

    sections_html = ""
    for channel in CHANNEL_ORDER:
        items = grouped[channel]
        if not items:
            continue
        rows = "".join(render_contact_row(c, ch, v, today) for c, ch, v in items)
        sections_html += f"""
        <h3 style="margin:20px 0 8px;font-size:14px;color:#555;text-transform:uppercase;letter-spacing:0.03em;border-bottom:1px solid #eee;padding-bottom:6px;">{channel} &middot; {len(items)}</h3>
        {rows}"""

    scheduled_html = ""
    if scheduled_today:
        rows = "".join(render_scheduled_row(c, e) for c, e in scheduled_today)
        scheduled_html = f"""
        <h3 style="margin:24px 0 8px;font-size:14px;color:#777;">Already on your calendar</h3>
        {rows}"""

    html = f"""
    <div style="font-family:-apple-system,Segoe UI,Arial,sans-serif;max-width:600px;font-size:15px;color:#222;">
      <p style="margin-top:0;">{intro}</p>
      {sections_html}
      {scheduled_html}
      <p style="color:#999;font-size:12px;margin-top:24px;">That's everything for today.</p>
    </div>"""

    log_line = f"contacts_due={total_outreach} scheduled_today={len(scheduled_today)}"
    return subject, html, log_line


def build_error_email(error_message, today):
    today_display = date.fromisoformat(today).strftime("%B %-d, %Y")
    subject = f"Daily Outreach List — RUN FAILED — {today_display}"
    html = f"""
    <div style="font-family:-apple-system,Segoe UI,Arial,sans-serif;max-width:600px;font-size:15px;color:#222;">
      <p>Heads up — this morning's outreach run didn't finish, so there's no list today.</p>
      <p style="background:#f5f5f5;padding:10px;border-radius:4px;font-family:monospace;font-size:13px;color:#333;">{html_escape(error_message)}</p>
      <p style="color:#777;font-size:13px;">Details are in logs/daily_outreach.log if you want to dig in.</p>
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
