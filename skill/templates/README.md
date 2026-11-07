# Templates: a working ontology with three records

Copy this folder's contents into a new **private** repository and you have a validated ontology to grow:

```
schema/            the process, role and decision schemas (JSON Schema 2020-12)
processes/         one record per process; the file name is the key without `process:`
roles/             one record per role
decisions/         one record per standing decision
questions/         LEDGER.md, the question ledger
validate.py        the structure review; run it on every pull request
```

```
python -m venv .venv
.venv/bin/pip install pyyaml jsonschema        # Scripts\pip on Windows
.venv/bin/python validate.py
```

The three records here are a worked example from `references/convert-an-sop.md`: one SOP about a
five-absence conversation became a process, the role that acts, and the privacy decision every ontology needs
first. Replace them with your own; keep the decision.

Two things to do before the first real record:

1. Add your own server, host, database, account and vendor-instance names to `INFRASTRUCTURE_WORDS` in
   `validate.py`, so a `staff` or `public` record that names one is refused. That list stays private.
2. Add `intake/` and `build/` to `.gitignore`. Raw material may carry names and never lands in git; the export
   is rebuilt, never committed.
