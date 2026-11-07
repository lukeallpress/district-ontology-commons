# Storage and review: files, a schema, a validator, an export

## Why one record per file in git

- **A pull request is the review.** The owner of a process can read a one-screen diff of their own record and
  say yes or no. Nobody can review a diff of a four-hundred-page document, and nobody reviews rows in a database.
- **The file name is the key.** `processes/<slug>.yaml` holds `process:<slug>`. References between records are
  keys and the validator checks that each one resolves to a file. There is no index to maintain; the folder is
  the index.
- **History for free.** Who changed a threshold, when and why is `git log` on one file.
- **Agents read files well.** An agent with the repository can answer from the records with no serving layer
  at all, which is how you start.

## Why not one big document

The first version of ours was one document. It could not be reviewed by the people whose work it described,
it could not say which parts were confirmed and which were guesses, and it could not be exported by audience.
Splitting it into records with a `status` and a `visibility` each was the moment it became usable.

## Why not a database first

You do not know the shape yet. Our process schema changed twelve times in the first six weeks (the `source`
entry alone went from a free-text line to a five-field object), and each change was a migration script over
files and a validator rule, done in an afternoon. Changing a database schema with a front end on it is a project.
Start in files; add a database when you have a reason (below).

## The file format does not matter much

We use YAML because a record is a document with lists and nested fields and people need to read the diff.
JSON works; so would TOML. The decisions that matter are the schema, the keys and the rules, not the
serialization. Converting later is one script. Two YAML traps: quote every date (`'2026-10-05'`, or YAML turns
it into a timestamp) and quote any list item that contains `: `.

## The structure review: a schema and a validator on every pull request

A JSON Schema per record kind catches shape: required fields, enumerations, key patterns. The validator
catches what a schema cannot. Ours (`templates/validate.py`) refuses:

| Rule | Why |
|---|---|
| key does not match the file name | a renamed file with a stale key breaks every reference to it |
| a reference to a record that does not exist | unless marked `(not yet drafted)`, so a plan can point ahead |
| a six-or-more-digit number anywhere in a record | the shape of a student number, a badge number, a phone number; none belongs in a record about a process |
| an actor, owner or decider that looks like a person | a bare "Firstname Lastname"; a pair containing a role word ("Executive Director") passes |
| an email address as an owner | name the role |
| a `source` entry with a bad date, a future date, or `checked` before `learned` | a future check would defer the review for years |
| a `staff` or `public` record naming infrastructure outside `source` and `signal` | servers, paths, database objects and accounts stay `internal` |
| a ledger row number used twice | a repeated key wherever the ledger is read |

The validator runs in CI on every pull request and in the tests, so the command line and CI agree. Keep the
validator's infrastructure word list in the private repository; it is itself a list of things not to publish.

## The export: one artifact per audience

Serving is a build step, not a copy of the files. An export script reads every record, drops what the
audience may not see (whole records above its level; the `source` and `signal` fields below `internal`,
replaced by the kinds of source so "how well is this supported" survives), and writes one JSON. The `staff`
export feeds the staff site and the hosted assistant; the `internal` export feeds the team's own agents; the
`public` export is what you hand another district.

## When a database or a graph store starts to pay

Records already form a graph: process to role, process to decision, process to system, decision to the records
it applies to. A graph store adds nothing until those edges are **keyed** (role keys in `actor`, not free-text
phrasings). Once they are, the questions that need a store are:

- serving many agents at once with per-agent visibility, especially across organizations ("your assistant
  sees only what my district marked `public`");
- staff responses at scale (who confirmed which claim, when; points; routing), which are rows, not records;
- cross-district comparison, where two ontologies share the Ed-Fi role vocabulary and can be joined on it.

Our staff review site keeps the records as the exported JSON on disk and uses SQL only for what people
submit. The records never live in the database; the repository stays the source of truth and the export is
rebuilt on every merge. Do the same until a query you need cannot be answered from the export.

## "Constraints as code"

Some decisions are rules a machine can check: "never schedule a reader on the quarter hour", "a record is
verified only by its owner". Give those a machine-readable predicate next to the prose when you can evaluate
it somewhere (a validator rule, a scheduler check, a test). Do not reach for a theorem prover; the validator
is already your constraints-as-code, and the decision record's `reason` and `would_reopen` are the parts a
machine cannot supply.
