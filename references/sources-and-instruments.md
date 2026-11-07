# Where the facts come from, and how they stay true

## The `source` entry

Every record carries a list of places its facts were learned, one entry per place:

```yaml
source:
- where: the attendance procedure document in the student services shared folder (the grace weeks per campus)
  kind: document        # code, job, data, document, web, meeting, conversation, email, observation
  learned: '2026-09-30' # the day it was read or heard; quoted
  supports: [trigger]   # optional: the fields this source backs
  link: https://...     # optional: how to re-open it, when `where` is not already findable
  checked: '2027-02-01' # optional: re-read on this day and it still said the same
  recheck_by: '2027-06-01'  # optional: a deadline that overrides the kind's interval
```

`where` is specific enough for someone else to find again: a file and its lines, a document's title and
folder, a meeting and its date, or **the role** that said it. Never a person's name. A record with no source
is a guess, and the validator requires at least one.

Two rules that are easy to get wrong:

- **Never move `learned`.** It is the day the fact first came from that place. Re-reading an unchanged source
  sets `checked`; finding it changed corrects the record and adds a new source entry.
- **A migration must say what it did.** When we converted 910 free-text sources into this shape, each got a
  `dated_by: text` or `dated_by: commit` so a reader knows whether the date came from the text or from when
  the line entered the repository (an upper bound).

## The source review

A script lists, every week: sources whose file has a commit since they were learned or checked; sources
whose file is gone; sources past their kind's interval (we use 90 days for `job` and `observation`, 180 for
`code`, `data`, `document` and `web`, 365 for `meeting`, `conversation` and `email`); and any undated source.
A person works the due ones; a scheduled run re-reads the changed files first. This is what keeps a record
honest a year later without anyone remembering to check.

## Mine the code and documents before you ask anyone

Most of an organization's thresholds and calendars are already written down somewhere a machine can read:

| Trace | What it yields |
|---|---|
| scheduled jobs and their configuration | thresholds, calendars, recipients, the automated step of a human process |
| letters and emails a system sends | the trigger and the actor of the human process that follows |
| forms | the request-triggered processes and their fields |
| existing SOPs, checklists, handbooks, board policy | steps, owners, rules in force, the decision records hiding in "we always" sentences |
| the strategic plan's action steps | declared projects with an owner role and a definition of done |
| incident write-ups, proposals, review logs, handoffs | the standing decisions people obey, with their date and reason |

Write the record as `drafted` from these, then interview. Thirty minutes with drafts in hand beats two hours
from a blank page, and the holder sees that the point is to spare them explaining.

## The instruments for what the code does not hold

Each turns one kind of trace into **candidates**: half-filled records with a `source` line and a confidence
word, written to the ignored intake folder for a person to promote. Nothing an instrument produces becomes a
record without that step.

| Instrument | Trace | Yields | Rule |
|---|---|---|---|
| Calendar audit | recurring events in one person's calendar export | cadences (the meeting is the heartbeat), actor roles from attendees, windows | only for the person who asked; attendees resolved to roles |
| Mail mining | subjects, senders and dates of one mailbox | recurring reports nobody wrote down (a subject that repeats weekly is a process), who asks whom for what | **headers only, never bodies**; only the mailbox owner runs it |
| Interview | fifteen minutes with a role holder, drafts in hand | trigger, steps, evidence location; the "what nobody wrote down" list | recorded; dates and roles only in what is committed |
| Recording extraction | a meeting transcript or auto-generated notes | decisions, commitments, cadences, process mentions, each with the speaker's role | only when the meeting owner handed it over; the prompt replaces every person with a role |
| Decision mining | incident notes, proposals, handoffs, an assistant's memory of rulings | standing decisions with date, reason, what would reopen them | |
| Role self-audit | everything above pointed at one person, plus what they own in code and systems | a role record | the sponsor first |
| Department folders | what a department already has, read-only | the existing written practice | the folder stays the department's |
| Agent brief | an opt-in role holder's own assistant answers the questions routed to the role from what it can see of their work | the interview at scale, with a confidence and an evidence kind per answer | roles only, no student data, withdraw at any time; see `questions/agent-intake-prompt.md` |
| The question ledger | every "how do we..." nobody could answer | the gaps, ranked by how often asked | an agent adds a row instead of guessing |

Confidence is a word, not a number: `seen-once`, `recurring`, `stated-by-owner`, `verified`. A scheduled run
may raise `seen-once` to `recurring` when a second trace agrees; only a person reaches `stated-by-owner`.

## The order to run them for a new role

1. Calendar audit (an afternoon, no interview needed): the cadences and the roles around them.
2. Mail mining on the same mailbox: the requests the role fields and the reports it sends.
3. Decision mining over the documents the role owns.
4. Draft the role record and the process candidates from 1 to 3.
5. **Then** the interview, with the drafts in hand: confirm, correct, fill the evidence locations.
6. Recordings as they happen: each meeting the role owns is extracted the week it occurs.

## Three things that will bite in the interview

- **"Where is that kept?" gets a shrug more often than any other question.** The shrug is the finding. Write
  `evidence.location: null` and the words they used. Do not invent a location.
- **People describe the ideal, not the last time.** "Walk me through it as you did it last time" is the wording
  that gets the real steps, including the workaround.
- **The trigger they name first is often the calendar, and the real trigger is a person.** "The meeting is
  Tuesday" versus "the assistant principal messages me when a student hits ten". Ask "and if the meeting were
  cancelled?"
