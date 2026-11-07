# Harvest: collecting how-we-operate knowledge from staff

The builder's draft comes from code, documents and calendars. It is wrong in ways only the people doing the
work can see, and it is silent about everything the systems do not record. Harvesting is the part of the
practice that gets the truth out of staff without wasting their time, without asking them things they cannot
know, and without retaining anything personal. This is what we did, what failed, and what we do now.

Everything here is a pattern. Our implementation is an internal site; yours can be a form, a chat bot, a sheet,
or a weekly fifteen minutes at a meeting people already attend. The rules are the same.

## (a) The review game

Records are made of **claims**: one statement each, small enough to be right or wrong on its own ("the
registrar posts the transfer transcript", "the trigger is the fifth unexcused absence"). Staff do not review
records; they answer claims.

- **One card at a time.** The claim is the only heading on the page, with one line of context (the process's
  purpose, or the decision itself) and a link to the whole record. Three large buttons under it, each a colour
  and a glyph, never colour alone: **Yes, that's right** (green), **Not quite** (amber, opens an optional note),
  **Not sure** (blue). Keys 1, 2, 3 work. Answering advances to the next card.
- **Skip for now.** No points, no penalty; the card comes back tomorrow at the back of the queue. A skip is not
  an answer and is not counted as one.
- **Points and a leaderboard.** Every button says what it is worth before it is pressed; a short "+5! Nice."
  follows each answer. Answering a question in words is worth more than confirming a claim; a dispute with a
  note is worth more than a bare tap; "not sure" is worth nothing (it is an honest answer and still recorded,
  but the board rewards what moves a record). The leaderboard is the home page: top twenty, your own line
  always visible, the school year and this week as windows, a streak of days with at least one answer. The
  point values live in one table and are printed from it on every page, so nobody mistakes them for policy.
- **Each person gets their own order.** Within a band, cards are shuffled by a hash of the person and the card,
  so one person sees the same order every visit and two people see different orders. Coverage spreads instead
  of everyone answering the same first ten.
- **Ask only what you are not sure of.** A claim is never queued when the record is already verified, the
  decision is already confident, the claim is already confirmed by enough people, or a person cannot check it
  on a card. Band the rest: claims whose record names the person's role first, then the ones that reach them
  through their group or campus; within a band, lowest confidence first (single-source records, decisions seen
  once, then recurring, then the rest). The player sees only "We only ask about things we're not sure of yet";
  the administrator sees the counts behind it.
- **Standing is computed, never stored, and never sets `verified`.** From the current responses: *confirmed*
  (enough agree weight and no disagree), *disputed* (any disagree), *thin* (one agree, nothing else),
  *unanswered*. A response from someone the record names outweighs one from someone merely near the work. The
  reviewer reads the confirmed claims and sets `verified` in the record, dated. Nothing on the site edits a
  record; promotion stays a pull request by a person.
- **"Not my area" is an answer.** Our next slice: a fourth button worth nothing that excludes that card for
  that person from then on and feeds two admin lists: coverage (claims nobody left can answer) and a rewrite
  list (claims many people could not understand). Without it, "not sure" carries two meanings and you cannot
  tell a thin record from a badly routed one.

Where it stands for us (2026-11-07, pattern numbers): about 6,700 claims of which about 4,500 were askable on
day one; about 1,600 questions of which about 960 were askable. The rest were kept off the cards by the rules
below, which is the point: the game is only as good as what it refuses to ask.

## (b) Human-friendly language

The first time our own sponsor played, he could not tell whether claims about systems he oversees were true,
because the cards were raw field text: record keys, backticks, pointer notes, analysts' findings first in the
queue. Then the first outside group met a wall of technical findings and answered nothing. The fix is a gate,
not a style guide.

**The askability gate.** A claim or question is kept off every card when, after cleaning, it still carries a
code, file, table or path shape, a keyed system reference or a placeholder, or runs past about forty words (the
ledger's median question is twenty-four). Cleaning turns record keys into record names and drops backticks,
parenthetical pointers and transcript stamps. The site rewrites nothing: the count per kind is on the
administrators' help page, and the fix is at the source, in the record or the ledger. A card is one thing: one
claim, one question, one answer.

**Before and after** (generic):

> Before: `process:transfer-transcript-intake#steps[2]`: registrar runs `post_transfer.py` against
> `course_history` after the `STU_IMPORT` job (see ledger #41, "still true?").
>
> After: **Transfer transcript intake**, step 3. *The registrar posts the transfer courses once the morning
> student import has run.* Is that right?

**Address the role, not the system.** Fit the question to the field ("Is this what starts it?", "Does this
role do this?", "Is this still the rule?") and put the record's purpose as the context line. A finding written by
an analyst ("the evidence location is null") is for the record's owner, in an interview; on a card to anyone
else it is noise, and it goes last or not at all.

## (c) Routing: ask only the roles the record names

Records name their actors and owners; the directory knows people's titles, groups and sites. Routing matches
those, in this order, and the first match is enough: the person's **title words** in the actor or owner phrase
(a one-word title matches only that exact role, so "Director" never reaches "director of innovation"; the most
specific known title wins, so "principal" never takes "assistant principal"'s claims); an editable **synonym
table** (human resources and HR; site administrator and the campus principals); a **group** (campus
administrators, district office leadership); a **location** (a record that names a campus goes to that campus's
matching titles only); and **self-claimed roles** ("I also do this", offered on the card itself and on the
person's own page, accepted only for phrases the records use).

**Named or near.** The first two and the last of those *name* the person's role; a group or a location match
only says they are near the work. A **question** (an answer in words) goes only to people whose role is named.
A **claim** (a tap) may still reach the group, but after the claims that name the person.

**What went wrong when we routed by directory title.** Our first staff session was the academic leadership
team. Every district-office leader was handed about 300 question cards, 283 of them analysts' findings on the
sponsor's own records, because a synonym for the sponsor's title pointed at the whole district-office group, and
findings were banded first. They could answer nothing and said so. Two fixes, both structural: questions route
only by named role, and the askability gate above. Lesson for anyone starting: a directory title is not a role;
"Executive Director" tells you nothing about what the person oversees.

**Coverage gaps are a report.** A claim with no respondent at all is listed for the administrator with the
phrase that matched nothing; that list is how the synonym table grows. Routing is computed on read from the
current directory, never stored, so a new hire sees their cards on first sign-in and a leaver's disappear.

## (d) The five intake routes

1. **The review game**, above. Best for confirming what is already drafted and for the questions the ledger
   already holds. Worst for anything that needs a paragraph.
2. **A role hands its own assistant the question list.** The person opts in; the administrator generates a
   plain-text brief: the questions and claims routed to that role, by id, the rules (roles not people, no
   student data, say "don't know", confidence and evidence kind per answer) and a structured reply block. The
   person's assistant answers from their mailbox and documents; the person pastes the block back, signed in as
   themselves, and sees exactly what was recorded. Answers land as *assistant-inferred* with the person's title,
   group and location, never a username. Opting out purges everything. `questions/agent-intake-prompt.md` is the
   prompt.
3. **A backup account for a vacant role.** When a role is empty, a colleague answers for it from a second
   sign-in bound to the vacant title, so the records keep moving and the answers are tied to the role, not to
   the colleague's own.
4. **Interview with the draft in hand.** Fifteen minutes, one record, "tell me where I am wrong". Far better
   than "tell me what you do". The drafted record is the agenda; the ledger rows for that role are the second
   half. `questions/question-bank.md` has the questions by field.
5. **Transcripts of training and handover sessions**, mined for operational facts only: a cadence, a trigger,
   a threshold, where the evidence lands, a standing rule and its reason. Nothing about any person. The output
   is candidate records for a human to promote, never records written directly.

A sixth route exists on paper for us and is off until it is built: replies by mail to the brief, parsed by the
same contract. Document it, do not pretend you have it.

## (e) Consent and privacy while harvesting

- **Nothing personal is retained.** Operational facts only, from any source. No opinion, nothing about an
  individual or a reputation, not even a count. This outranks every other rule here and must hold mechanically
  (headers-only tools, roles-only output, a validator that refuses names), not by judgment.
- **The person sees only what their role may see.** Visibility tiers apply to the game as they apply to the
  export: a card never shows a `source` or a `signal` field, and a staff-tier record names no infrastructure.
- **Answers are tied to title, group and location, never a username, in anything that leaves the site.** The
  export for promotion is a candidate bundle grouped by record and question: each line carries title, group,
  location, confidence, evidence kind, date and the claim text at the time, and no username. The administrator
  can see who claimed what; the records never do.
- **A mailbox or calendar instrument is run only by the owner of that mailbox or calendar**, on their own
  account, and bulk material with people in it goes through a local model, not a hosted one. A departed
  colleague's shared work folders may be read with an explicit decision recorded; their mailbox needs a separate
  one.
- **Opt-in for anything an assistant does on a person's behalf**, with the consent text on their own page: what
  the brief asks, what the answers are tied to, that they see everything sent, that opting out purges it.
- **Say what the game is for, on the game.** Ours says: "Every answer makes the map of how we work a little
  truer" and "We only ask about things we're not sure of yet". People answer honestly when they know why.

## (f) What to measure

| Measure | Why it matters |
|---|---|
| Coverage per role: claims routed, answered, with no respondent | the gaps are where the synonym table and the role records are wrong |
| Askable share: claims and questions on cards versus kept off, per kind | the kept-off list is the rewrite list; a falling share means records are getting more technical |
| Standing counts: confirmed, disputed, thin, unanswered, per record and overall | disputed is where the draft was wrong; thin is where you need a second person |
| Time to first answer for a new record | the real test of routing: a record nobody is asked about is a record nobody owns |
| Answers by evidence kind: I do this, I saw it, told by a role, document, assistant-inferred | the mix tells you how much of the ontology rests on first-hand knowledge |
| Streaks and daily answered counts | engagement; also the early warning that the queue has run dry or gone stale |

Report these to the sponsor weekly, and put the askable share and the coverage gaps in front of whoever
writes records. The game is a measuring instrument for the records before it is a game for the staff.
