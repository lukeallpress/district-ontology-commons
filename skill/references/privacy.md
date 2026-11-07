# What to keep private

Two rules and a tier model. The first rule outranks everything else in this skill.

## 1. Nothing personal is retained

When an instrument or an agent reads a mailbox, a calendar, a transcript, a chat log or any other personal
trace to build the ontology, **nothing about personal opinions, individuals or their reputations is retained,
recorded, summarized, counted, remembered or used to train or tune anything.** Only operational facts leave the
source: a cadence, a process name, a role, a threshold, a date, a decision and its stated reason. When in doubt
it is personal, and it stays where it was.

What that excludes, concretely: a view of a colleague, a complaint, a performance matter, a family situation,
a grievance, a health or legal matter, gossip, tone, who is good at their job, who is not. Not the fact of it,
not a paraphrase, not a count, not a memory in an agent, not a log line.

Why it is absolute: email and meetings carry personal material by nature; the ontology is about how the
organization operates, not about people; a single retained remark about a person would make the whole
repository unsafe to hand to any agent; and a model that learned from it could not unlearn it. The rule is
written as a decision record (see `templates/decisions/nothing-personal-is-retained.yaml`) so it has an owner and a reason.

It must hold **mechanically**, not by judgment:

- The mail instrument reads **headers only** (subjects, senders, dates). A tool that would need to read a body
  to work is not built.
- Every instrument's output is **roles only**; the validator refuses a personal name in a record.
- Raw material lives in an **ignored intake folder** that never lands in git.
- **Consent is per source.** A calendar or mailbox is read only for the person who asked, and only by them or
  with their explicit hand-over. A transcript is extracted only when the meeting owner handed it over.
  Interviews are offered, not imposed. A departed employee's shared work folders may be read by the role
  covering the vacancy; their mailbox is a separate, explicit decision by the organization, not a default.
- **Bulk personal material goes through a model you host**, not a hosted one. Clustering subjects and
  calendar series needs no model at all; write those tools in plain code.

The middle ground staff worry about ("will my emails be quoted at my successor?") has a clean answer: a
record may say "the campus administrator checks in with direct reports every two weeks" (operational,
role-level, from a pattern). It may never say how a named person wrote, decided or behaved. If the only
way to state a fact is about a person, it is not a fact for the ontology.

## 2. Students are not in it, ever

No student identifier, no case, no example row, no screenshot of a record, anywhere in the repository or the
intake folder. A record describes the work ("the five-absence conversation"), never an instance of it. The
validator refuses any six-or-more-digit number for exactly this reason. Student data is handled by the systems
the records point at, under their own rules; the ontology holds the pointer.

## 3. Four visibility tiers

Every record carries `visibility`, widest first:

| Level | Who sees it | Typical use |
|---|---|---|
| `public` | anyone, including vendors and other districts | cross-district comparison, vendor onboarding, cookbook examples; set only by a person, never by a migration or an agent |
| `staff` | any signed-in staff member | the staff site, the staff FAQ, the hosted assistant |
| `internal` | the technology, data and records team | the team's own agents |
| `restricted` | the owning role and the sponsor's office | open security work, exposures, personnel-adjacent processes |

Two rules hold at every level:

- **The technical fields are never shown below `internal`.** `source` (servers, paths, mailboxes, meetings) and
  `signal` (the tables and reports a process reads) are replaced in a `staff` or `public` export by the *kinds*
  of source only, so "how well is this supported" survives and no infrastructure leaves.
- **A `staff` or `public` record names no infrastructure anywhere else either.** No server, address, path,
  database object, account or connection string outside those two fields. The validator refuses one that does;
  rewrite the field in plain words ("the attendance table in the reporting warehouse") or make the record
  `internal`. Keep the infrastructure word list in the private repository.

A ledger row takes the strictest of: a leading `[internal]` or `[restricted]` mark, `internal` if it names
infrastructure, and the level of every record it names.

**Nobody widens a level but the director** (or whoever sponsors the ontology). A record without a level is
treated as `internal`: unknown is never widened. Assign the first levels with a script that marks anything
naming infrastructure `internal` and everything else `staff`, then review the `internal` ones by hand: most
can be rewritten in plain words and returned to `staff`; a few are infrastructure in substance and stay.

## 4. What this makes possible

Because the tiers exist from the first record, "a slightly public version I can send to anyone who asks" is
not a project later. It is `export --audience public`. The public tier is also how a district tells another
district "here is how we actually do X" without a legal review of every sentence: the review happened when a
person set `public` on the record.

## 5. What never enters any record at any level

A person's name. A student identifier. A case. An example row. A credential, key or password. A security
finding that is still open (a `restricted` record may describe the process of handling it, not the exposure).
Anything that is *about* a person rather than about the work.
