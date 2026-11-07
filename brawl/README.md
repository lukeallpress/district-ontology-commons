# The brawl: comparing ontologies across districts

"A year from now, fifteen of us throw our ontologies in the middle and let the best ideas win." That is the
goal. Nothing here is decided. This page states the design question so the
[Discussion](https://github.com/lukeallpress/district-ontology-commons/discussions) can decide it.

## What must be common for a comparison to run at all

| Common | Why |
|---|---|
| The three record kinds and their required fields (process, role, decision) and the ledger | you cannot diff a process against a paragraph |
| The role classification vocabulary: Ed-Fi `StaffClassification` as `classification` on every role record | "assistant principal" and "vice principal" and "AP" must land on the same thing |
| The four visibility tiers, and the rule that only the public tier leaves the district | otherwise nobody shares anything |
| A public-tier export shape: one folder of records in the common schemas, validated | the brawl runs on exports, never on live repositories |
| The `source` entry shape and the status ladder (drafted, verified, measured) | a verified record and a drafted one are not the same evidence |

## What stays local

Record keys, local titles and aliases, the processes themselves (every district runs attendance differently; that
is the point), the systems named in `systems` edges (an atlas key means nothing outside the district), the
synonym table, everything below the public tier.

## Candidate comparison questions

- Which processes do you have for this role classification that we do not have for the same classification?
- Where do our standing decisions differ for the same trigger ("fifth unexcused absence", "a staff member
  leaves", "a vendor asks for student data")?
- Which processes are automated for you and manual for us?
- Which of your verified records cover a ledger question we have had open for months?
- What does your role record for a classification say it decides alone that ours says it escalates?
- Which decisions have you reopened, and why, that we still hold as standing?

## Storage options on the table

| Option | For | Against |
|---|---|---|
| **Git per district, shared index here.** Each district keeps its own repository; this commons holds each district's public-tier export folder and an index that joins them by classification and trigger. | Zero new infrastructure; every district already has git; the pull request is the review; the commons stays public by construction. | Comparison is a script somebody runs; no live query; exports go stale unless each district automates its own push. |
| **A shared graph store.** Records from every public tier loaded into one graph database, queried across districts by role classification, trigger, system class. | Live cross-district queries; agents can answer "who else does this" directly. | Somebody hosts it, secures it and pays for it; a second copy of every record to keep in sync; the first security question is who may query what. |
| **Federated exports, each district hosts its own.** Every district publishes its public tier at a URL in the common shape; the commons holds only the list of URLs and the comparison tooling. | Each district controls its own publication and revocation; no shared store to secure. | Availability is whatever each district's hosting is; a comparison needs all of them up at once; the smallest district carries the same hosting burden as the largest. |

A fourth question sits under all three: whether the serving layer for agents is the same thing as the
comparison layer for people. We think not. Serving an agent inside one district is a file plus a small query
tool today; comparing across districts is a batch job over exports until proven otherwise.

## What we do not know

- Whether Ed-Fi's staff classification is fine-grained enough for the roles that matter most (a registrar, a
  federal programs director, an instructional coach) or whether the commons needs a shared extension list.
- Whether process triggers can be normalised enough to join on. "Fifth unexcused absence" is a threshold; "a
  parent calls" is an event; "every Monday" is a cadence.
- How to compare decisions whose reasons are local law or local board policy with decisions whose reasons are
  convenience.
- Whether anyone will publish a public tier that is more than ten records, and what makes them willing.

Take all of it to the Discussion. The first district folder with a public export settles more than this page can.
