# Rollout: the order, the review game, and what went wrong for us

## The order

1. **The sponsor's own role.** The Director of Innovation (or whoever sponsors this) writes their own role
   record first, from what they own in code, repositories, systems, calendars and three months of rulings.
   They can be wrong in public cheaply, and every rule in this skill gets tested on a willing subject.
2. **A vacancy.** A role whose holder has just left is the case the ontology exists for: deadlines do not wait
   for the rollout order. Read the departed role's shared work folders (not their mailbox, without a separate
   explicit decision), draft the processes and the role, and name in a decision record who confirms those
   records while the role is empty.
3. **Three teams and one front end.** Pick the team that owns the plumbing every other process rides on
   (technology, accounts, data flow), one team with one application and one owner, and the team where the
   knowledge is thinnest. Each gets the same four steps: a five-minute role-based question session at a
   meeting they already attend; the agent brief to anyone who opts in; one shared folder for what they already
   have; a review of the drafted records with the owning role, which is what moves a record to `verified`.
4. **Departments in the order your own champions rank them.** Ask the people who already field "how do I"
   questions which groups ask most.

Lead with a small proof, not "the ontology is everything". Done for the proof looks like: the three teams'
records reviewed by the owning roles with `verified` on the right ones and findings on the wrong ones; three
role sessions recorded and promoted; the intake folder in use; a search that answers "how do we..." for those
teams from the export, naming the record and its status; a weekly staleness check whose reminders reach owners.

## Five routes in, one landing

Every route produces **candidates**, never records. Candidates land in one place, a person reviews them, and
a pull request promotes them.

| Route | Who it suits |
|---|---|
| drop a document in the department's intake folder | most people, most of the time |
| answer the ledger questions routed to your role, by email or five minutes at a meeting | anyone with a role on a row |
| the agent brief: your own assistant drafts the answers from your work | staff who already use an assistant |
| the issue form in the repository | people who live in GitHub anyway |
| a "map your work" conversation with starters per role | staff who will not fill a form |

Promotion: a person reads the candidate, resolves names to roles, writes or amends the record, opens the pull
request; the validator and a second reviewer run; the sponsor merges; the export is rebuilt. A candidate that
has sat two weeks with no record and no question back is a finding against the promoter, not the contributor.

## The review game

Once records exist, staff validate them: each record's fields become **claims** ("the registrar posts the
transfer transcript"), routed to the people whose role the record names, shown **one card at a time** with
agree / not quite / not sure, points and a leaderboard, and the open ledger questions routed the same way for
an answer in words. A claim's standing (confirmed, disputed, thin, unanswered) is computed from responses and
**never sets `verified`**: the reviewer reads the confirmed claims and sets it in the record, dated.

Ask only what you are not sure of. Never queue a claim when the record is already verified, the decision is
already confident, people have already confirmed it, or a person cannot check it on a card.

## What went wrong for us, and the fix

**First staff session, November 2026: the academic leadership team could answer nothing.** Two causes.

1. **Routing by directory title alone.** Records named actors in free text; the site matched phrases to
   titles with a synonyms table; a synonym for the sponsor's own title pointed at the whole district-office
   leadership group. Every district-office leader was handed about 300 question cards, 283 of them findings on
   the sponsor's own records, about systems they do not oversee. Fix: a **question** (an answer in words) goes
   only to people whose role the record **names**; a group or campus match may still carry a claim (a tap),
   after the named ones. Better still, key your actors to role records from the first record
   (`roles-not-people.md`) and routing becomes a lookup.
2. **Technical findings shown to non-technical staff.** Analysts' findings ("the job logs the address", "no
   deadline exists for posting the transcript") were asked before what people themselves asked, and many
   carried a code, file, table or path shape or ran past forty words. Fix: an **askability filter** (no
   code-shaped text, under forty words for a question and fifty for a claim, every `applies_to` line off the
   cards), findings after what people asked, and an admin page that counts what was kept off so the rewrite
   list is visible.

Two more from earlier:

- **The sponsor could not judge claims about systems they oversee** because the cards showed raw field text
  with record keys, backticks and transcript stamps. Clean the text before it is shown; the person's verdict is
  tied to the words they saw.
- **A one-word title matched everything.** "Director" routed every record naming any director. A one-word
  title matches only that exact role; for longer titles the most specific known title wins.

## Governance, borrowed

One set of principles, three roads by what you want to do: **read it** (anyone, no approval), **contribute to
it** (any staff member through a route above; a champion promotes), **write it** (records and the front end: a
pull request, the validator, a review, the sponsor's merge). Nobody has to ask which process applies.

## Where things live

| What | Home |
|---|---|
| raw intake: transcripts, recordings, brief replies, interview notes | one managed shared folder tree, a subfolder per department, access per champion; never git |
| what a department already has | the department's own folder, linked from its records |
| the structured truth: processes, roles, decisions, the ledger | the private repository, with `build/` as the export |
| the SOP articles (the manual) | wherever staff already go for help (a knowledge base), linked from the record's `sop` field |
| what the ontology must never hold | names, student identifiers, case detail, credentials, open security findings |
