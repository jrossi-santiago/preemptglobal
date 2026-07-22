# CRM Outreach Guide

Reference doc for the daily CRM outreach agent. This file is the source of truth for field
mapping, filtering rules, channel selection, and report formatting. If this file and the agent
prompt ever disagree, this file wins.

See `PREEMPT_CONTEXT.md` (repo root) for business facts, voice, and guardrails — this doc
covers CRM-specific logic only.

---

## 1. Data source

Airtable base `app41M1klIruYKXuW`, table `tbl6vr7FbZK28kIVJ` ("Contacts"). Fetch all records,
paginating with `list_records_for_table` until done.

### Field mapping

Map each record's `cellValuesByFieldId` into this shape (missing fields → `null`):

| Output field | Source field ID | Notes |
|---|---|---|
| `id` | record id | |
| `name` | `fldKVamMNCYI0jIIZ` | |
| `company` | `fld5CNYAk4k7zCkhv` | |
| `title` | `fldvaIF9ZA7uGTBPy` | |
| `linkedin_url` | `fldcpY13MQPOYrU5n` | |
| `source_signal` | `fldGBxkEUUYnc1eRD` | |
| `date_first_contacted` | `fldHxF13ifBGzphV1` | |
| `contact_method` | `fld5RAse52MawpUjT.name` | or null |
| `status` | `fldXQRy1UM5eNhnKk.name` | or null |
| `followup_date` | `fldD3nWhAu6ppj0PN` | |
| `followup_done` | `fldJw4UHZnWFDhhzw` | boolean, default false |
| `notes` | `fldhx728EoxPG02wa` | |

---

## 2. Calendar cross-check

Fetch today's events from Google Calendar `josephrossi613@gmail.com`:
- `startTime` = TODAY 00:00:00 (America/New_York offset: `-04:00` if EDT, `-05:00` if EST)
- `endTime` = TODAY+1 00:00:00, same offset

Map each event to `{summary, description, start, attendee_emails: []}`.

If this fetch fails for any reason, use an empty event list — never fail the whole run over
calendar access.

---

## 3. Who's due today

A contact needs outreach if:
- `followup_date` is set, **and**
- `followup_date <= TODAY`, **and**
- `status` is not `"Dead"`

Everyone else is excluded from today's report entirely.

---

## 4. Calendar match → "scheduled today" group

For each due contact, check if their name (case-insensitive; try both the full name and just
the last token/surname — e.g. "Sage Olsen" should match an event titled "Follow up: Sage
Olsen") appears in any today-event's `summary`, `description`, or `attendee_emails`.

If it matches, move that contact to a separate **"scheduled today"** group instead of the
outreach group — they don't need a separate nudge since it's already on the calendar.

---

## 5. Channel selection

For everyone left in the outreach group, pick a channel in this priority order:

1. **Email** — if an email address (regex-shaped, e.g. `name@domain.tld`) appears anywhere in
   `title`, `notes`, or `source_signal`, use that address.
2. **LinkedIn** — else if `linkedin_url` is set, use it.
3. **Call/Text** — else if a US-style phone number (e.g. `904-580-0585`, `(904) 580-0585`)
   appears in `title`, `notes`, or `source_signal`, use it.
4. **Other** — else, no contact info found.

---

## 6. Timeline per contact

Build a chronological mini-history from:
- `source_signal` as an unlabeled first line, plus
- `notes` split on newlines — if a note line starts with a date marker like `7/15 — ...`,
  `7/15 - ...`, or `7/15: ...`, split it into `(date label, text)`; otherwise keep the whole
  line as unlabeled text.

---

## 7. Due phrase

`days_over = TODAY - followup_date` (in days).

- `days_over <= 0` → "due today"
- `days_over == 1` → "a day overdue"
- else → "`{days_over}` days overdue"

---

## 8. Report format (Markdown)

File name: `crm/{TODAY}.md` (e.g. `crm/2026-07-22.md`), one new file per day.

### Title

```
# Daily Outreach List — {Month Day, Year}
```
e.g. `# Daily Outreach List — July 22, 2026`

### Intro line

> Morning — N person/people to reach out to today.

(singular/plural on "person"/"people"). If there's a scheduled-today group, append:

> Also flagging M person/people already on your calendar, so no separate nudge needed there.

### Zero-contacts variant

If zero contacts are due and zero are scheduled today, skip everything else and use just:

```
# Daily Outreach List — {Month Day, Year}

Morning — nothing on your outreach list today. No follow-ups are due, and nothing's overdue.

_(Just confirming the routine ran fine this morning — no action needed from you.)_
```

### Outreach sections

One `##` section per channel that has contacts, in this fixed order: **Email, LinkedIn,
Call/Text, Other** (skip empty ones):

```
## {Channel} · {count}

### {Name} ({Company})
- {date label or nothing} — {timeline text}
- {date label or nothing} — {timeline text}
- **{TODAY as M/D} — {action sentence}** _({due phrase})_
```

- Omit `({Company})` entirely if there's no company.
- Timeline lines with no date label are just `- {text}`.

**Action sentence by channel:**
- Email → `Reach out by email — {email}`
- LinkedIn → `Reach out on LinkedIn — {linkedin_url}`
- Call/Text → `Reach out by call or text — {phone}`
- Other → `No direct contact info on file — check LinkedIn or your notes`

### Scheduled-today section

Only if there's a scheduled-today group:

```
## Already on your calendar

- **{Name} ({Company})** — already on your calendar today at {h:mm AM/PM} ("{event summary}").
  No outreach needed.
```

- Omit "at `{time}`" if the event has no start time.
- Omit `({Company})` if none.

### Escaping

Escape markdown special characters (`*`, `_`, `[`, `]`, `` ` ``) anywhere user-supplied text is
inserted (name, company, notes, etc.) so stray characters don't break rendering.

---

## 9. Failure mode

If any step throws in a way that can't be routed around (calendar failures do **not** count —
those just use an empty event list), write `crm/{TODAY}.md` with this content instead:

```
# Daily Outreach List — RUN FAILED — {Month Day, Year}

Heads up — this morning's outreach run didn't finish, so there's no list today.

​```
{error message}
​```
```

Always commit and push this failure file too — never end the run without a committed,
verified report file for TODAY.
