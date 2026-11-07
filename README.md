# district-ontology-commons

A shared, public place where K-12 districts build **ontologies of how they actually operate**, policy and
practice, and compare them.

An SOP tells a person how to do a task. An ontology tells a person *or an agent* how the organization operates:
what recurring work exists, what starts it, which role does it, where the evidence lands, what has been decided
and why, and what nobody has answered yet. Every district has one; almost none have written it down in a form a
newcomer, a colleague covering a vacancy, or an agent can answer from. This commons exists so that none of us has
to work that out alone, and so that what one district learns becomes something another district can use.

## Why a commons

The idea that started this: a year from now, fifteen districts sit around a table, throw their ontologies into
the middle and let the best ideas win. Today, when one district's technology leader says "we don't have HR data
entry errors any more, we changed how the request comes in", the room nods, and nobody else can operationalise
it, because the fix lives in one person's head and one department's habits. Written as records, with the same
shape and the same vocabulary across districts, it becomes a thing you can diff, adopt, and improve.

Three things make that possible, and they are the three things a contributor does here:

1. **Adopt the structure.** Three record kinds (process, role, decision) and a question ledger; one record per
   file in git; a schema and a validator on every pull request; roles never people; four visibility tiers from
   day one; the Ed-Fi staff classification vocabulary for roles so two districts can be compared.
2. **Harvest from your own staff.** The builder's first draft comes from code and documents; the truth comes from
   the people who do the work, asked only what they can answer, in words they would use, one card at a time.
3. **Share the public tier.** Export the records your district is willing to show the world and put them in your
   folder here. That is the material the comparison runs on.

## What is here

| Path | What |
|---|---|
| `skill/` | an installable Agent Skill (`SKILL.md`, ten lessons, references, templates with schemas and a validator) for building a district ontology with an agent at your side |
| `harvest/` | how to collect how-we-operate knowledge **from staff**, not just from the builder: the review game, human-friendly language, routing, the five intake routes, consent, what to measure |
| `questions/` | the shared question bank, by the record field each question fills and by role classification; the prompt a role hands its own assistant |
| `brawl/` | the open design question: how two districts' ontologies get compared, what must be common, where it lives; no decision taken yet |
| `districts/` | one folder per contributing district: what they adopted, what they changed, their public-tier export |
| `CONTRIBUTING.md` | how to add your district, and the public-content rules every contribution must pass |

## How to join

1. Read the opening Discussion first: [How do we share, store and brawl ontologies across
   districts?](https://github.com/lukeallpress/district-ontology-commons/discussions/1) It is where the shape
   of this gets decided, and a reply there counts as joining.
2. Post what you have, even if it is a folder of SOPs or a spreadsheet of who-does-what. The conversion is the
   easy part; knowing what you have is the hard part.
3. When you are ready, open a pull request that adds `districts/<your-district>/README.md` (see `CONTRIBUTING.md`).

## Install the skill

Clone this repository and point your agent at `skill/`. For Claude Code, a symlink or copy of `skill/` at
`~/.claude/skills/district-ontology-commons` is enough; the skill reads `../questions/` from the same clone, so
keep the whole repository together rather than copying `skill/` on its own. The skill triggers on requests like
"document how our district operates", "turn our SOPs into an ontology" or "our agents don't know how we work".

## Start a new ontology

```
mkdir our-ontology && cd our-ontology && git init
cp -r <this clone>/skill/templates/* .
python -m venv .venv && .venv/bin/pip install pyyaml jsonschema   # Scripts\pip on Windows
.venv/bin/python validate.py
```

Then write the sponsor's own role record first (`questions/question-bank.md`, the role section), convert five
SOPs with `skill/references/convert-an-sop.md`, and open a pull request for each. When records exist, read
`harvest/README.md` before you show anything to staff.

## The three rules you will be tempted to break

1. **Roles, never people.** The validator refuses a bare personal name. Keep it that way.
2. **Nothing personal is retained.** Only operational facts leave a mailbox, a calendar or a transcript.
3. **`verified` is set only by the owning role, in a conversation.** Never by an agent, a vote or a headless run.

## Who started it, and where the source lives

Started by Luke Allpress, Director of Innovation at Agua Fria Union High School District (AFUHSD), Arizona, from
the first two months of building that district's own ontology: about 450 records across 280 processes, 24 roles
and 146 decisions, in daily use by staff through a review game and by agents through an export. The working
ontology is a private repository, `AFUHSD/af-ontology`, and the review game is an internal site. Everything in
this commons is **public by construction**: patterns, schemas, lessons and questions, never a deployment, never
a person, never a student. The prompt to make it shareable came from a November 2026 conversation with UniqLearn
and Cajon Valley Union School District about how districts should structure and serve this kind of knowledge.

## License and contributions

Use it, fork it, improve it. The most useful thing you can send back is the question your staff could not
answer and how you resolved it; that goes in the question bank. The second most useful is your district folder.
