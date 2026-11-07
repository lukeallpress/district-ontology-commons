# The three record kinds and the question ledger

Three kinds of record and one ledger are enough for an organization. Each kind answers one question a
newcomer, a successor or an agent asks; resist adding a fourth until a year of records demands it.

| Kind | Answers | Key shape | File |
|---|---|---|---|
| process | "When does X happen, what starts it, who does it, where is it recorded?" | `process:<slug>` | `processes/<slug>.yaml` |
| role | "What is this role for, what does it own and decide, how do I work with it?" | `role:<slug>` | `roles/<slug>.yaml` |
| decision | "Why do we do it this way, who decided, and what would change it?" | `decision:<slug>` | `decisions/<slug>.yaml` |
| the ledger | "Has anyone asked this, and did anyone answer?" | row number | `questions/LEDGER.md` |

**The key is the file name.** `processes/five-absence-conversation.yaml` holds `key: process:five-absence-conversation`
and nothing else may claim that key. References between records are keys, and the validator refuses a reference
to a record that does not exist unless it is marked `(not yet drafted)`. That is the whole coordination
mechanism: no index file, no registry, no database. The folder is the index.

## The process record

One recurring piece of human work with a purpose. Everything else hangs off it.

| Field | What it holds | Why it is there |
|---|---|---|
| `key`, `name` | the id and the name people actually use | search works on the name people say |
| `status` | `drafted`, `verified`, `measured`, `retired` | so no reader mistakes a draft for policy |
| `visibility` | `public`, `staff`, `internal`, `restricted` | who may see it (see `privacy.md`) |
| `source` | one entry per place a fact was learned | so it can be re-read when the place changes |
| `purpose` | why it exists; the policy or goal it serves | the first thing a successor needs |
| `trigger` | `kind` (`threshold`, `event`, `window`, `request`, `schedule`) and the `rule` in words | the trigger is what a tool or an agent would watch for |
| `signal` | the system fact the trigger reads, and the screen or report that surfaces it | the data path; technical, hidden below `internal` |
| `actor` | the roles that act, by key, never by name | a person leaving changes nothing |
| `steps` | what is done, in order, in plain words, as it was done last time | the real steps include the workaround |
| `output` | the artifact produced | "what exists afterwards that did not before" |
| `evidence.location` | where completion is recorded; `null` means nowhere | a process with no evidence cannot be counted or triaged; `null` is a finding, not a gap to paper over |
| `cadence` | `continuous`, `daily`, `weekly`, `per-event`, or a dated window | the heartbeat |
| `follows`, `escalates_to` | the process before and the one after | the chain |
| `systems` | edges to the systems map, each with a mechanism: `informs`, `facilitates`, `notifies`, `records-in` | outage triage in human terms: which processes does a broken system block |
| `owner` | the role accountable for the rule, if not the actor | who can change it |
| `automated` | which step a job does, or `nothing` | the build-versus-buy case starts here |
| `findings` | what the record's author saw wrong | so they are not re-reported as new |
| `sop` | where the human how-to lives; `null` means none exists | the record is the model; the SOP is the manual |

## The role record

A role, never a person: the holder changes, the record stays. It is the record a successor reads on day one.

| Field | What it holds |
|---|---|
| `purpose` | one sentence to someone who has never met the role |
| `classification` | the Ed-Fi `StaffClassification` value this role falls under (see `roles-not-people.md`) |
| `titles` | the local directory titles that map to this role, as aliases |
| `reports_to` | a role key or a title |
| `owns` | `processes` (keys), `systems`, `repos`, `other` |
| `decides`, `does_not_decide` | decision rights in plain words |
| `cadences` | `what`, `when`, `with` (roles), `evidence` |
| `standing_rules` | rules the role holds others to; each should also be a decision record |
| `how_to_work_with` | `ask`, `approve`, `never`, `prefers` |
| `handoff` | what a successor would need on day one; usually the richest field |
| `open_questions`, `findings` | what the author could not learn, and what looked wrong |

## The decision record

A decision people still obey. The reason matters more than the ruling: a successor who knows the reason can
tell when it no longer applies.

| Field | What it holds |
|---|---|
| `title`, `decision` | what was decided |
| `status` | `standing`, `superseded`, `proposed`, `retired` |
| `decided_on`, `decided_by` | a month or a day; a role, never a name |
| `reason` | why, in the decider's words if you have them |
| `scope` | what it applies to: every app, one campus, one job |
| `would_reopen` | the condition under which it should be reconsidered |
| `applies_to` | keys of the records it governs |
| `confidence` | `seen-once`, `recurring`, `stated-by-owner`, `verified`: a word, never a number |
| `superseded_by` | the decision that replaced it |

## The question ledger

One line per question nobody could answer: the question in the asker's words, `asked_by` (a role or `agent`),
the first date, a count that goes up when it returns, a status, and the answer or next step. A question closes
when a record answers it, and the closing line names the record.

The ledger is the learning mechanism. An agent that cannot answer from the records adds a line instead of
guessing. An interview starts from the rows routed to that role. A row that has sat open for a month is the
next thing to write. Number rows once and never reuse a number: two branches that each append rows can pick
the same number, and a repeated number is a repeated key wherever the ledger is read.

## The status ladder

| Status | Meaning | Who sets it |
|---|---|---|
| `drafted` | written from code, documents or a transcript | anyone, including an agent |
| `verified` | the owning role confirmed it in a conversation, dated in `last_verified` | the owning role only, through a person |
| `measured` | the evidence is counted and the count is reported somewhere | a person, once the count exists |
| `retired` | the work stopped; the record stays as history | a person |

A record half-confirmed stays `drafted` with a note saying which half. A staff review game, a vote, an agent
or a headless run never sets `verified`; they produce candidates and findings that a person reads before
touching the record. Say the status every time you answer from a record.
