# Contributing

This is a commons. The structure, the lessons and the question bank are shared; each district's records stay
in that district's own private repository, and only its **public tier** comes here. Everything in this repository
is public the moment it is merged, so the rules below are not etiquette, they are the thing that lets a district
participate at all.

## What a district contributes

1. **A district folder: `districts/<your-district>/README.md`.** Use `districts/afuhsd/README.md` as the shape.
   Say what you adopted as-is, what you changed and why, your counts (records by kind, how many verified), the
   failures you learned from, and who to talk to (a role and a GitHub handle, not an email). Keep it to a page.
2. **Your public-tier export**, if you have one, as `districts/<your-district>/public/` holding the records your
   district is willing to show the world, in the record shapes under `skill/templates/schema/`. Run the validator
   on them first. The comparison work in `brawl/` runs on these folders.
3. **Lessons** that belong to everyone go into `skill/references/` or `harvest/`, written as the pattern, with a
   one-line attribution to your district at the point where the lesson is stated. A lesson that only makes sense
   with your deployment in view belongs in your district folder instead.
4. **Questions** your staff could not answer, and how you resolved them, go into `questions/question-bank.md`
   under the record field or the role classification they belong to. A question is the most portable thing here.

## How

Pull requests, one topic each, against `main`. Open a Discussion thread first for anything that changes the
shared structure (a schema field, a record kind, a vocabulary); the Discussion is where the shape is decided and
the pull request is how it lands. Small additions (a question, a district folder, a lesson) need no thread.

## The public-content rules

Every contribution must pass these, with no exceptions for "it's only a test environment" or "it's just an
example". Reviewers grep for them today; a validator-style check will enforce them later.

- **No infrastructure.** No hostnames, IP addresses, file paths, UNC paths, account names, service accounts,
  database, schema, table, procedure or server names, connection strings, ports, or vendor contract details.
  Write "the SIS", "the warehouse", "the reminder service", "the app host".
- **No people.** No staff names other than the contributor's own on their district folder. Roles and titles,
  never names. No opinions about anyone, no reputations, no "the previous director used to".
- **No students.** No student identifiers, no case detail, no example rows, no counts small enough to identify
  a person. Records describe the work, never a case.
- **No open security findings.** A failure mode written generically ("a shared service-account password in a
  config file is inherited by every application on the host") is a lesson. The file, the account or the host is
  an exposure. If something is valuable and unsafe, say so in the Discussion and leave it out.
- **No secrets.** Nothing that looks like a token, key or password, even revoked, even redacted in the middle.

Before you open the pull request, grep your changes for your own district's hostnames, server names, account
names, campus abbreviations and the names of people you work with. The commons' maintainers will do the same.

## Attribution

Contributions carry the contributor's district in the file (a one-line "from <district>" where the lesson is
stated) and the contributor's GitHub identity in git. Agents are welcome to draft; a person opens the pull
request and stands behind it.
