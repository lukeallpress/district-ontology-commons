---
name: district-ontology
description: Build a school district's organizational ontology (how it actually operates, policy and practice) as records people review in git and agents answer from, in the shared shape of the district-ontology-commons so it can be compared with other districts. Use when someone says "document how our district operates", "turn our SOPs into an ontology", "organizational ontology", "our agents don't know how we work", or asks what structure, vocabulary, privacy rules, harvesting method and interview questions to start with. Distilled from a working district ontology (hundreds of records, in use by staff through a review game and by agents through an export); the lessons, the schemas, the question bank and a validator you can run today.
---

# Build a district ontology, in the shape of the commons

This skill is the builder's half of the [district-ontology-commons](https://github.com/lukeallpress/district-ontology-commons):
the structure, the order of work and the rules. The other half, how to harvest the truth from staff once records
exist, is `../harvest/README.md`; the shared question bank is `../questions/`; how districts compare what they
built is `../brawl/README.md`. Install the whole repository, not this folder alone.

An SOP tells a person how to do a task. An ontology tells a person *or an agent* how the organization
operates: what recurring work exists, what starts it, which role does it, where the evidence lands, what has
been decided and why, and what nobody has answered yet. The SOP is the manual; the ontology is the model that
points at the manual. This skill is the shortest path from the first to the second, with the mistakes already
made for you.

It is written for a K-12 district but nothing in it is K-12 specific. Everything here was learned building
one district's ontology from September 2026 on; `references/` carries the reasoning, `templates/` the schemas
and a validator, `../questions/` the questions to ask, `../harvest/` the method for asking staff. Read this file
first; read a reference when you reach its step.

## The ten lessons

1. **Three kinds of record, one ledger.** A *process* (recurring human work with a purpose), a *role* (what a
   role is for, owns, decides, does on a cadence, and how to work with it), a *decision* (a standing ruling with
   its reason and what would reopen it). Plus a *question ledger*: every "how do we..." nobody could answer.
   Nothing else. Resist a fourth kind until a year of records demands it. → `references/record-kinds.md`

2. **One record per file, in git, with a schema and a validator on every pull request.** The file name is the
   key; references between records resolve by key; a pull request is the review. Not one big document (nobody
   reviews a diff of a 400-page file), and not a database first (you do not yet know the shape). The file format
   is the least important choice; YAML is fine. → `references/storage-and-review.md`

3. **Roles, never people.** Actors, owners and deciders are role keys. The validator refuses a bare
   "Firstname Lastname". A person leaving must not change a record. Classify roles with the Ed-Fi Unifying Data
   Model's `StaffClassification` vocabulary so two districts' ontologies can be compared, and keep your local
   titles as aliases on the role record. → `references/roles-not-people.md`

4. **Nothing personal is retained.** When a mailbox, calendar or transcript is read to build a record, only
   operational facts leave it: a cadence, a process, a role, a threshold, a date, a decision and its stated
   reason. No opinion, nothing about an individual or a reputation, not even a count. This rule outranks every
   other rule here and it must hold mechanically (headers-only tools, roles-only output), not by judgment.
   → `references/privacy.md`

5. **Four visibility tiers from day one**: `public`, `staff`, `internal`, `restricted`. The technical fields
   (`source`, `signal`) are never shown below `internal`. A `staff` or `public` record names no server, path,
   database object or account; the validator refuses one that does. Nobody widens a level but the director.
   Export by audience; the public tier is how you share with other districts. → `references/privacy.md`

6. **Every fact says where it was learned.** A structured `source` entry per place: `where` (findable again,
   never a person's name), `kind`, `learned` (a quoted date), optionally `supports`, `checked`, `recheck_by`.
   A periodic review lists sources whose file changed or whose interval passed. A record with no source is a
   guess. → `references/sources-and-instruments.md`

7. **Mine the code and the documents before you interview anyone.** Scheduled jobs, forms, letters a system
   sends and the existing SOPs already encode thresholds and calendars. Draft from those, then interview with
   the draft in hand: "tell me where I am wrong" beats "tell me what you do". → `references/sources-and-instruments.md`

8. **`drafted` is honest; `verified` is earned.** A record written from code and documents is `drafted`. Only
   the owning role, in a conversation, moves it to `verified`, dated. An agent, a headless run or a crowd vote
   never does. Say the status whenever you answer from a record. → `references/record-kinds.md`

9. **Start with the director's own role, then a vacancy, then three teams.** The person who sponsors the work
   goes first because they can be wrong in public cheaply. A role whose holder has just left is the case the
   ontology exists for. Then three teams with one front end. → `references/rollout.md`

10. **Ask people only what they can answer.** Our first staff session failed because questions were routed by
    directory title alone and technical findings were shown to non-technical staff. Route by the role the record
    names, filter out anything code-shaped or over forty words, and show one claim at a time.
    → `references/rollout.md`, and the full method in `../harvest/README.md`

## Doing it

**Day one.** Copy the contents of `templates/` into a new private repository: the three schemas, the three
example records, the ledger, `validate.py`. Run the validator. Write the sponsor's own role record from what they own in
code, repositories, calendars and three months of rulings (`../questions/question-bank.md`, the role section).

**Week one.** Convert five existing SOPs with `references/convert-an-sop.md`: each becomes a process record, a
role record for its actor if none exists, and a decision record for every "we always / we never" sentence.
Every unanswerable field becomes a ledger row, not an invention.

**Month one.** Pick the first team. Calendar audit and document mining first, fifteen-minute interviews with
drafts in hand second. Set up the export by audience and put the `staff` tier somewhere staff can search it.
Add a way for staff to confirm or dispute a claim, one card at a time, routed to the role the record names.

**Ongoing.** A pull request per change, the validator on each, the source review weekly, the ledger worked
down at interviews. An agent that cannot answer from the records adds a ledger row instead of guessing; that
line is how the ontology learns what it is missing.

## Rules for an agent using this skill

- Answer from the records and cite the key and the status: "per `process:five-absence-conversation` (drafted),
  the teacher of record logs the contact". A summary with no key is a guess.
- Cannot answer? Add a ledger row with the question in the asker's words, `asked_by: agent`, today's date. Then
  say the question is open.
- Never put a person in a record. Never put a student identifier, a case or an example row anywhere in the
  repository.
- Never set `verified`. Correct a `drafted` record when the code disagrees with it, citing the file in `source`.
- Every fact you add or change gets a `source` entry with a quoted `learned` date. Re-reading an unchanged
  source sets `checked`; never move `learned`.
- Never set `public` or widen any record's visibility without the director.

## The question bank

`../questions/question-bank.md` holds the generic questions to ask any role, organized by the record field each
one fills and by role classification, and `../questions/agent-intake-prompt.md` is the prompt a role holder can
hand their own assistant to answer them from their mailbox and documents with nothing personal. The bank is a
commons asset: every district adds the questions its staff could not answer, under the same headings. A public
site that serves the bank is intended; until it exists the folder is the bank.

## What is in this folder

| Path | What |
|---|---|
| `../README.md` | the commons charter: what this is, why, how to join |
| `../harvest/README.md` | collecting from staff: the review game, human-friendly language, routing, intake routes, consent, measures |
| `../brawl/README.md` | how districts' ontologies get compared; the open design question |
| `../districts/` | one folder per contributing district |
| `references/record-kinds.md` | the three record kinds and the ledger, field by field, and the status ladder |
| `references/storage-and-review.md` | one record per file, schema plus validator, the export, when a database starts to pay |
| `references/roles-not-people.md` | the person test, role keys, titles as aliases, the Ed-Fi StaffClassification vocabulary |
| `references/privacy.md` | nothing personal is retained; the four visibility tiers; what never enters a record |
| `references/sources-and-instruments.md` | the `source` entry, the source review, the capture instruments and their consent rules |
| `references/rollout.md` | the order to roll it out, the staff review game, what went wrong for us and the fix |
| `references/convert-an-sop.md` | the walkthrough from one how-to document to three records |
| `templates/` | a copyable repository skeleton: `schema/` (the three schemas, JSON Schema 2020-12), `processes/`, `roles/`, `decisions/` (one valid example each, generic district language), `questions/LEDGER.md` (the ledger with one example row), `validate.py` (schema, key equals file name, references resolve, no identifiers, no people, no infrastructure below `internal`, ledger numbers unique) |
| `../questions/question-bank.md` | the shared questions, by the field they fill and by role classification |
| `../questions/agent-intake-prompt.md` | the prompt a role hands its own assistant |

## Related standards

- Ed-Fi Unifying Data Model: https://docs.ed-fi.org/reference/data-exchange/udm/ (the staff domain's
  `StaffClassification` descriptor is the role vocabulary this skill adopts)
- Common Education Data Standards (CEDS): https://ceds.ed.gov/ (classes and properties for people,
  organizations and K-12 data; a second source of nouns when Ed-Fi lacks one)

Neither standard models a process, an SOP or a decision. Borrow their nouns; keep the record kinds here.
