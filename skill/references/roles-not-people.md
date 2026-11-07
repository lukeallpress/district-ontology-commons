# Roles, not people

A record describes work. A person is who happens to do it this year. The moment a record names a person it
becomes a record about that person: it goes stale when they leave, it cannot be shown to everyone, and it
invites the opinions and reputations that the privacy rule forbids. So:

- `actor`, `owner`, `decided_by`, `with`, `reports_to` hold **roles**.
- A role is a **record** (`roles/<slug>.yaml`) with a key, and processes name it by key: `role: role:school-counselor`.
- The directory titles that map to that role are **aliases** on the role record (`titles`), not keys.

## The person test the validator runs

A bare capitalized pair, "Firstname Lastname", is a person and is refused. A pair containing a role word
(board, director, superintendent, principal, counselor, teacher, registrar, clerk, coach, specialist, manager,
coordinator, administrator, office, team, department, committee, council, assistant, executive, district,
campus, school, program, and so on) is a role or a body and passes: "Executive Director", "Governing Board".
An email address anywhere in an owner or actor field is refused. Extend the role-word list to your own
vocabulary; the test is deliberately simple so it can be explained in one sentence.

## What we got wrong first, so you do not

Our first 280 process records named actors in **free text**: "teacher (designs and grades the assignment)",
"the attendance clerk or the registrar". It read well and it was useless for routing: 355 distinct actor
phrasings and 80 owner phrasings for a few dozen real roles. The site that asks staff to confirm claims had to
match phrases to directory titles with a synonyms table, and a one-word title ("Director") matched everything.
The fix was the rule above: `actor` is a list of role keys, with the free text kept in a `note` if it carries
something the role record does not. Key your actors from the first record.

## The classification vocabulary: Ed-Fi StaffClassification

Two districts can only compare ontologies if their roles share a vocabulary. Local titles do not ("Data
Information Specialist" exists in one district; "Registrar" means two different jobs across our own campuses).
The Ed-Fi Unifying Data Model's `StaffClassification` descriptor is a maintained, public, education-specific
classification used by state reporting across much of the United States, so adopt it as the role record's
`classification` field. Each role record then carries three things:

| Field | Example | Who sets it |
|---|---|---|
| `key` | `role:school-counselor` | you; stable; the thing processes reference |
| `classification` | `School Counselor` | from the Ed-Fi descriptor list, verbatim |
| `titles` | `["School Counselor", "Guidance Counselor", "Counselor - Academy"]` | your directory's job titles that map to this role |

Current (non-deprecated) descriptor values include, among others: `School Administrator`,
`School Administrative Support Staff`, `School Counselor`, `Secondary School Counselor`, `Secondary Teacher`,
`Special Education Teachers`, `Paraprofessional/Instructional Aide`, `Librarian/Media Specialist`,
`School Psychologist`, `Social Workers`, `Student Support Services Staff (w/o Psychology)`, `LEA Administrator`,
`LEA Administrative Support Staff`, `Instr Coordinator and Supervisor to the Staff`, `Mentor Teacher`,
`Site Coordinator`, `All Other Support Staff`. Read the live list at the Ed-Fi data standard's descriptor
reference before you start (https://docs.ed-fi.org/reference/data-exchange/udm/ links to the staff domain).

Two things to know about the list:

1. **The familiar words are deprecated.** `Principal`, `Assistant Principal`, `Superintendent`, `Counselor`,
   `Teacher`, `Instructional Coordinator`, `School Leader` and `Other` all carry `DEPRECATED` in the current
   descriptor set; the live values are the broader classes (`School Administrator` covers a principal and an
   assistant principal; `LEA Administrator` covers district-office leadership). That is fine. `classification`
   is for comparison across districts, and the broad class is what compares. The distinction between a principal
   and an assistant principal is your **role key** and your **titles**, which stay local and precise.
2. **Many roles that matter to operations are "All Other Support Staff" or "LEA Administrative Support Staff"**
   to Ed-Fi: a registrar, a data specialist, an attendance clerk. Again fine; the key carries the precision.

Where Ed-Fi has no noun, CEDS (https://ceds.ed.gov/) has a second vocabulary of classes and properties for
people, organizations and K-12 data. Neither standard models a process, an SOP or a decision; borrow the nouns
and keep the record kinds from this skill.

## Resolving a name to a role

An instrument may read a name (a calendar attendee, a sender, a document author) in order to resolve it to a
role through the staff directory. The record keeps the role. The raw material with the name in it stays in an
ignored intake folder and never lands in git. If a name cannot be resolved, the record says "a participant"
or "a campus office role", and the gap goes to the ledger.

## Bodies, groups and "the team"

"The academics team", "the SIS team", "campus administrators" are legitimate actors. Make them role records
too (`role:academics-team`) with `classification` left to the closest class or `All Other Support Staff`,
and list the member roles under `owns.other` or in the purpose. A body that decides is a `decided_by` like any
role.
