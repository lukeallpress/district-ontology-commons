# Convert an existing SOP into records

Take one how-to document. You will produce a process record, a role record for its actor if none exists, and
a decision record for every "we always / we never / the district requires" sentence in it. Budget an hour for
the first one and fifteen minutes by the fifth.

## Worked example

The SOP, as departments actually write them:

> **Attendance follow-up, step by step.** When a student reaches five absences in any class, the teacher of
> record has a conversation with the student and logs it in the SIS contact log under "Attendance". Use the
> attendance dashboard every Monday to see who has crossed the line. Do not wait for the attendance clerk to
> tell you. At ten absences the clerk sends the district letter; that is a separate procedure. We never count
> school-business absences toward the five.

### 1. The process record

Read each sentence for the field it fills.

| Sentence | Field | Record |
|---|---|---|
| "When a student reaches five absences in any class" | `trigger` | `kind: threshold`, `rule: a student reaches five absences in one class` |
| "the teacher of record" | `actor` | `role: role:secondary-teacher` |
| "has a conversation ... and logs it in the SIS contact log" | `steps`, `output`, `evidence.location` | steps in order; output "a contact-log entry"; evidence "the SIS contact log, category Attendance" |
| "Use the attendance dashboard every Monday" | `signal`, `cadence` | `signal.surfaced_by: the attendance dashboard`; `cadence: weekly check, continuous during the semester` |
| "At ten absences the clerk sends the district letter" | `escalates_to` | `process:ten-absence-letter (not yet drafted)` until you write it |
| "Do not wait for the attendance clerk" | `findings` or a decision | a rule in force: who owns the trigger (see step 3) |
| "We never count school-business absences" | a decision | see step 3 |
| the document itself | `source` | `where: the attendance follow-up SOP in the student services folder`, `kind: document`, `learned: '<today>'` |
| the document itself | `sop` | its link; the record is the model, the SOP is the manual |

What the SOP does not say becomes a ledger row, not an invention: who owns the five-absence threshold (a
campus or the district); whether the conversation has a deadline; what happens for a student in two classes
over the line. Leave `owner` as the best role you can name and set `status: drafted`.

See `templates/processes/five-absence-conversation.yaml` for the finished record, `templates/roles/secondary-teacher.yaml`
for the role, and `templates/decisions/nothing-personal-is-retained.yaml` for a decision record's shape.

### 2. The role record

If `role:secondary-teacher` does not exist yet, create it with what this SOP tells you and nothing more:
`purpose` in one sentence, `classification: Secondary Teacher`, `titles` from your directory, `owns.processes`
listing this process, one `cadences` entry (the Monday dashboard check), `how_to_work_with.ask` if the SOP
says how. Everything you do not know goes under `open_questions`. The role record will fill in as you convert
more SOPs; the interview finishes it.

### 3. The decision records

Every sentence of the form "we always", "we never", "the district requires", "do not" is a standing decision
somebody made, and the SOP usually omits the reason. Write it as a decision record with `status: standing`,
`confidence: seen-once`, `decided_by` as the role that owns the SOP, `reason: not stated in the SOP` if that
is the truth, and `would_reopen: not stated`. Then ask the owner for the reason at the interview; the reason
is what the successor needs.

From the example: `decision:school-business-absences-not-counted` ("school-business absences never count toward
the attendance ladder") and `decision:teacher-owns-the-five-absence-trigger` ("the teacher watches the
dashboard; the clerk does not notify at five").

### 4. Run the validator, open the pull request

```
python validate.py
```

Expect it to catch: a date you forgot to quote, a role you wrote as free text, an `escalates_to` pointing at
a record you have not written (mark it `(not yet drafted)`), a six-digit number you pasted from the SOP's
example. Fix, commit, open the pull request, and ask the SOP's owner to read the diff. Their "yes" in the
review is a conversation; set `status: verified` and `last_verified` in a follow-up commit if they confirm
every field, otherwise leave `drafted` with a note saying which half.

## Patterns you will meet

- **The SOP is really three processes.** A "how we close the month" document is a request-triggered process, a
  window process and a schedule-triggered report. Split them; link with `follows`.
- **The SOP names a person.** "Send it to Maria in payroll" becomes `role:payroll-specialist`; the name is
  resolved through the directory and never written.
- **The SOP names a system by its screen.** "Open the blue attendance screen" is `signal.surfaced_by: the SIS
  attendance screen`; the system itself is a `systems` edge (`node: base:sis`, `mechanism: records-in`).
- **The SOP has no evidence step.** The work ends with "and you're done". `evidence.location: null` and a
  finding: this process cannot be counted until someone decides where completion is recorded.
- **Two SOPs disagree.** Write both facts, each with its source, and a ledger row asking which governs. The
  disagreement is the most valuable thing the conversion found.
- **The SOP has a date in it.** "By September 15" is `trigger.kind: window`; quote the date and name the
  policy or calendar it comes from in `source`, so a change there shows up as a disagreement here.
