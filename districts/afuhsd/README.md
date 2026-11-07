# Agua Fria Union High School District (AFUHSD), Arizona

A public high school district (six campuses plus an online academy) west of Phoenix. The commons started here.
Contact: the Director of Innovation, GitHub `lukeallpress`.

## Where we are (2026-11-07)

| | |
|---|---|
| Records | about 450: 280 processes, 24 roles, 146 decisions |
| Status | almost all `drafted` from code, documents, calendars and the sponsor's own rulings; `verified` is set by the owning role in conversation and is still rare |
| Question ledger | growing weekly; the ledger is where agents record what they could not answer |
| Review game | live internally since late October 2026; day one offered about 4,500 askable claims and about 960 askable questions, with the rest kept off the cards by the askability gate |
| Public tier | exists as a visibility level; zero records set to `public` yet. The first export here is the next step. |

## What we adopted as-is

Everything in `skill/`, because it was written from this repository. In particular: one record per file in
git with a JSON schema and a validator on every pull request; roles never people, enforced by the validator;
nothing personal retained, written as a standing decision with an owner and a reason; four visibility tiers
with the technical fields hidden below `internal`; a structured `source` entry on every fact with a periodic
source review; `verified` only by the owning role.

## What we changed, and why

- **Actors and owners were free text for the first two months** (355 distinct actor phrasings, 80 owner
  phrasings). That made routing in the review game a matching problem and caused our first failed session. We
  are keying every actor and owner to a role record and adding the Ed-Fi staff classification to each role;
  the commons' templates already require it, so a new district starts where we are ending up.
- **Findings are not claims.** An analyst's note on a record ("evidence location is null") was first shown to
  staff as a card. It now goes to the record's owner in an interview, or last in the queue as a question in
  words, and never to people the record does not name.
- **Questions route only by named role.** Group and location matches still carry claims (a tap), after the
  named ones, but never a question (an answer in words).

## Failures we learned from

- Routing by directory title alone handed every district-office leader about 300 cards, 283 of them technical
  findings on the sponsor's records; nobody could answer anything. Fix: named-role routing plus the askability
  gate (`harvest/README.md`).
- Raw field text on cards: record keys, backticks, pointer notes. The sponsor could not judge claims about his
  own systems. Fix: clean every claim before it gets an id, and tie each verdict to the text shown.
- A gamified "not sure" worth points rewards the wrong thing. It is now worth nothing and still recorded.
- A one-word title ("Director") matched every phrase containing the word and routed over a thousand claims to
  one person. Fix: a one-word title matches only that exact role.

## Next

Key every actor to a role; publish a first public-tier export in this folder; add the "not my area" answer to
the game; bring a second district's folder in and run the first comparison from `brawl/`.
