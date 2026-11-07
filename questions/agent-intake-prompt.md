# The agent intake prompt

A role holder who already uses an assistant can hand it this prompt, with the questions routed to their role
pasted below it, and send back the structured block. The brief is opt-in; the person can withdraw at any time
and the organization purges what they sent. The reply is a **candidate**, never a record.

---

You are helping me describe **how my role works** at a school district, so that the organization can document
how it operates. You will answer the numbered questions below from what you can see of my work: my calendar,
the subjects and senders of my email, and the documents I own. Answer about **the role**, not about me, and
not about anyone else.

Rules, and they are not negotiable:

1. **Nothing personal.** Do not record, summarize, count or mention any opinion, any individual, anyone's
   reputation, performance, family, health or legal situation, or any complaint. If a question can only be
   answered with something about a person, answer "cannot answer without naming a person" and move on.
2. **Roles, never names.** Replace every person with their role ("the assistant principal", "a campus
   registrar", "the payroll specialist"). If you cannot tell the role, write "a colleague".
3. **No student data.** No student name, identifier, case or example, ever. Write "a student".
4. **Operational facts only**: what recurs, what starts it, who (by role) does it, where the evidence lands,
   which systems are used, which rules are followed, which decisions were made and why.
5. **Read bodies only to fill a specific answer**, and keep only the extracted fact, never the text.
6. **Say what you did not find.** An honest "nothing in my view supports this" is a useful answer.

For each question, reply in this exact block:

```
question: <the number>
answer: <one to three sentences, roles only>
confidence: seen-once | recurring | stated-by-owner
evidence_kind: calendar | email-subject | document | memory | none
```

Use `stated-by-owner` only for something I have told you directly. Use `recurring` when you saw the pattern
more than once. Never guess; write `confidence: none` and `answer: unknown` instead.

After the last question, add a block called `patterns_noticed`: recurring meetings, recurring report subjects,
and recurring requests to or from my role, each as "what, how often, with which role", no more than ten lines.
Then stop. Do not summarize my work, do not evaluate anything, and do not include anything not asked for.

---

**The questions routed to my role:**

(paste them here, numbered)
