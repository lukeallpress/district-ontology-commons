# The question bank

The generic questions to ask any role, organized by the record field each answer fills. Ask them with a
draft in hand ("here is what I think happens; tell me where I am wrong"), record the session, and extract
roles and dates only. Each answer that cannot be given becomes a ledger row.

The live, growing version of this bank is intended to be a public site; this file is the bank until then.

## For a process (fifteen minutes, one record)

| Fills | Ask |
|---|---|
| `purpose` | Why does this exist? What goes wrong if nobody does it? Which policy or goal does it serve? |
| `trigger` | What tells you it is time to do it: a number, a date, something that happened, someone asking? |
| `trigger` (the real one) | And if the meeting were cancelled, what would still make you do it? |
| `signal` | Where do you look to know? Which screen, report, email, spreadsheet? |
| `actor` | Who actually does it? Who does it when they are out? |
| `steps` | Walk me through it, start to finish, as you did it **the last time**. |
| `steps` (the workaround) | Which step do you do differently from the written procedure, and why? |
| `output` | When it is done, what exists that did not before? |
| `evidence.location` | And where is that kept? Could someone count how many times it happened last month? |
| `cadence` | How often, and when in the year? Is there a window when it piles up? |
| `follows`, `escalates_to` | What happens next? What came before? When does it become someone else's? |
| `systems` | Which systems do you touch, and which one would stop you if it were down? |
| `owner` | Who owns the rule, if not you? Who could change the threshold or the step? |
| `vendor`, `automated` | Does a paid tool do part of this? Does a job or a script? Which part? |
| `findings` | What would you change about it if you could? |
| `sop` | Is there a written how-to? Where? When was it last right? |

## For a role (thirty minutes, once per role)

| Fills | Ask |
|---|---|
| `purpose` | What is this role for, in one sentence, to someone who has never met you? |
| `owns` | What do you own: processes, systems, lists, documents, relationships, recurring reports? |
| `decides` | What do you get to decide without asking anyone? |
| `does_not_decide` | What do you have to ask about, and whom? |
| `cadences` | What happens on your calendar every week, month, year that is really work and not just a meeting? (Have the calendar audit open; go series by series.) |
| `standing_rules` | What rules do you hold other people to? |
| `how_to_work_with.ask` | How should someone bring you a question? A request? Something urgent? |
| `how_to_work_with.approve` | What needs your yes, and what does your yes look like: an email, a meeting, a signature, a merge? |
| `how_to_work_with.never` | What do you wish people would stop doing when they work with you? |
| `how_to_work_with.prefers` | What makes a request easy to say yes to? |
| `handoff` | If you left tomorrow, what would nobody know how to do? What would you tell your replacement on day one? |
| `handoff` | What breaks when you are out for a week? Who notices first? |
| the ledger | What do people ask you that they should be able to find out without you? |
| `titles`, `classification` | What does the directory call you, and what did it call the last person in this role? |

## For a decision (five minutes, when you meet a "we always")

| Fills | Ask |
|---|---|
| `decision` | What exactly is the rule, in one sentence? |
| `decided_by`, `decided_on` | Who decided, in what role, and roughly when? |
| `reason` | Why? What was the problem it solved? |
| `scope` | What does it apply to: every campus, one program, one system? |
| `would_reopen` | What would have to change for this to be reconsidered? |
| `applies_to` | Which processes obey it? |
| `confidence` | Did the decider tell you this, or did you see it once? |

## For a department (the first meeting, five minutes at a meeting they already attend)

1. What do you do every Monday? Every first of the month? Every August?
2. What do people from other departments ask you for most?
3. What do you send out on a schedule, and who reads it?
4. Which of your procedures is written down, and where? Which is only in someone's head?
5. When the last person left your team, what did you discover nobody else could do?
6. Which system, if it went down for a day, would stop your work?
7. What do you do the same way at every campus, and what differs by campus?

## For the sponsor (the first record of all)

Everything in the role section, plus:

- Which rulings have you made in the last three months that people still obey? (Each is a decision record.)
- Which repositories, jobs, dashboards and systems do you own, and which do you merely touch?
- Which standing meetings are yours, and what is each one's output?
- What do you refuse, and why? (The `never` list is the most useful part of a sponsor's record for an agent.)
- What is the one thing you would want an agent to be able to answer about your role without asking you?

## The questions a district new to this asks

Collected from conversations with other districts; the answers are in `references/`.

- What is the back-end data structure, and should it be a database? → `storage-and-review.md`
- How do we keep staff trusting this when their email could be referenced? → `privacy.md`
- How did you get into a departed director's files, and what did you do with them? → `rollout.md` (the vacancy), `privacy.md` (consent is per source)
- We have many ways of doing the same thing; how do we capture the practice side when the policy side is done? → `convert-an-sop.md`, then the ledger
- We have a form that asks "what is the process, who needs to know, who is the expert"; is that enough? → it fills `steps`, `actor`/`notifies` and `owner`; add `trigger`, `evidence.location` and `source` and it is a process record
- Should we use a standard vocabulary? → `roles-not-people.md` (Ed-Fi StaffClassification for roles; nothing standard exists for processes or decisions)
- Which format: YAML, Markdown, a database? → the format is the least important choice; `storage-and-review.md`
