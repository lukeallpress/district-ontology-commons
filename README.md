# sop-to-ontology

A shareable skill for turning a school district's SOPs, how-to documents and tribal knowledge into an
**organizational ontology**: records of the recurring work, the roles that run it, the standing decisions
people obey, and the questions nobody has answered yet, kept in git, reviewed in pull requests, exported by
audience, and readable by people and agents alike.

Written by Luke Allpress, Director of Innovation at a public high school district in Arizona, from the first
two months of building that district's own ontology (about 450 records across 280 processes, 24 roles and 146
decisions, in daily use by staff through a review game and by agents through an export). The working ontology
is a private repository, `AFUHSD/af-ontology`; this folder is what can be distilled from it for anyone else.
The prompt to write the shareable version came from a November 2026 conversation with UniqLearn and Cajon
Valley Union School District about how districts should structure and serve this kind of knowledge.

## What you get

- `SKILL.md`: the ten lessons and the order to do things in. Start here. It is an Agent Skill, so Claude Code,
  Codex and other agents that read `SKILL.md` frontmatter can load it directly.
- `references/`: the reasoning behind each lesson, including what went wrong for us.
- `templates/`: a copyable repository skeleton: three JSON schemas, one valid example of each record kind, the
  question ledger and a validator (`validate.py`, Python 3.11+, `pyyaml` and `jsonschema`). Copy its contents
  into a new private repository and you have a working, validated ontology with three records.
- `questions/`: the generic questions to ask any role, organized by the record field each one fills, and the
  prompt a role holder can hand their own assistant to answer them with nothing personal.

## Install as a skill

Clone or copy this folder into your agent's skills directory (for Claude Code, `~/.claude/skills/sop-to-ontology`).
The skill triggers on requests like "turn our SOPs into an ontology" or "document how our district operates".

## Start a new ontology

```
mkdir our-ontology && cd our-ontology && git init
cp -r <this folder>/templates/* .
python -m venv .venv && .venv/bin/pip install pyyaml jsonschema   # Scripts\pip on Windows
.venv/bin/python validate.py
```

Then write the sponsor's own role record first (see `questions/question-bank.md`, the role section), convert
five SOPs with `references/convert-an-sop.md`, and open a pull request for each.

## The three rules you will be tempted to break

1. **Roles, never people.** The validator refuses a bare personal name. Keep it that way.
2. **Nothing personal is retained.** Only operational facts leave a mailbox, a calendar or a transcript.
3. **`verified` is set only by the owning role, in a conversation.** Never by an agent, a vote or a headless run.

## License and contributions

Use it, fork it, improve it. If you build an ontology with it, the most useful thing you can send back is the
question that your staff could not answer and how you resolved it; that goes in the question bank.
