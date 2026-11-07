"""Validate every record against its schema and the cross-record rules.

    python validate.py [root]      # root defaults to this file's folder; exit 1 listing every problem

The schema catches shape. This catches what a schema cannot: a key that does not match its file name, a
reference to a record that does not exist, an identifier-shaped number, a person named where a role belongs, a
source dated in the wrong order, infrastructure in a record that staff or the public may see, and a ledger row
number used twice. Run it in CI on every pull request and from the tests, so the two agree.

Needs Python 3.11+, pyyaml and jsonschema.
"""

from __future__ import annotations

import datetime as dt
import json
import re
import sys
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator

ROOT = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path(__file__).resolve().parent
KINDS = {  # folder: (schema file, key prefix)
    "processes": ("process.schema.json", "process"),
    "roles": ("role.schema.json", "role"),
    "decisions": ("decision.schema.json", "decision"),
}
LEDGER = ROOT / "questions" / "LEDGER.md"

# Six or more consecutive digits is the shape of a student number, a badge number or a phone number: none belongs
# in a record about a process. Years (four digits) and statute numbers (15-803) pass.
IDENTIFIER_SHAPE = re.compile(r"(?<!\d)\d{6,}(?!\d)")
# A reference to a record that is not written yet is allowed only when it says so.
NOT_YET = " (not yet drafted)"
RECORD_REF = re.compile(r"\b(?:process|role|decision):[a-z0-9]+(?:-[a-z0-9]+)*")

# Words that make a capitalised pair a role or a body, not a person ("Governing Board", "Executive Director").
# Extend with your own vocabulary.
ROLE_WORDS = {
    "board", "director", "directors", "superintendent", "committee", "office", "principal", "principals", "team",
    "lead", "department", "services", "manager", "specialist", "coordinator", "administrator", "administration",
    "council", "officer", "counselor", "counselors", "teacher", "teachers", "nurse", "registrar", "clerk", "coach",
    "staff", "desk", "chair", "secretary", "assistant", "executive", "district", "campus", "school", "program",
}

# What a staff or public record may not name outside `source` and `signal`. The generic shapes are here; add your
# own server, host, database, account and vendor-instance names to INFRASTRUCTURE_WORDS. This file lives in your
# private repository; the list is itself a list of things not to publish.
INFRASTRUCTURE_WORDS: list[str] = []
INFRASTRUCTURE = re.compile("|".join([
    r"\b10\.[0-9]+\.[0-9]+\.[0-9]+\b", r"\b192\.168\.[0-9]+\.[0-9]+\b",
    r"\b172\.(?:1[6-9]|2[0-9]|3[01])\.[0-9]+\.[0-9]+\b",
    r"Password=", r"Server=", r"\b[A-Za-z]:\\", r"\b[A-Za-z]:/", r"\\\\[A-Za-z0-9_-]+\\", r"\bdbo\.",
    *(re.escape(w) for w in INFRASTRUCTURE_WORDS),
]), re.IGNORECASE)
TECHNICAL = ("source", "signal")  # never shown below internal, so they may name infrastructure


def looks_like_a_person(text: str) -> bool:
    """A bare "Firstname Lastname" is a person; a pair containing a role word is a role or a body."""
    if "@" in text:
        return True
    m = re.fullmatch(r"\s*([A-Z][a-z]+) ([A-Z][a-z]+)\s*", text)
    return bool(m) and not ({m.group(1).lower(), m.group(2).lower()} & ROLE_WORDS)


def as_date(value) -> dt.date | None:
    try:
        return dt.date.fromisoformat(str(value)) if value else None
    except ValueError:
        return None


def source_problems(record: dict, label: str) -> list[str]:
    today = dt.date.today() + dt.timedelta(days=1)  # a day's grace for a run that crosses midnight
    problems: list[str] = []
    for i, entry in enumerate(record.get("source") or [], start=1):
        if not isinstance(entry, dict):
            continue
        for field in ("learned", "checked", "recheck_by"):
            if entry.get(field) is not None and as_date(entry.get(field)) is None:
                problems.append(f"{label}: source {i} {field} {entry.get(field)!r} is not a real date")
        learned, checked, recheck = (as_date(entry.get(k)) for k in ("learned", "checked", "recheck_by"))
        if learned and learned > today:
            problems.append(f"{label}: source {i} was learned in the future ({learned})")
        if checked and checked > today:
            problems.append(f"{label}: source {i} was checked in the future ({checked})")
        if learned and checked and checked < learned:
            problems.append(f"{label}: source {i} was checked ({checked}) before it was learned ({learned})")
        if learned and recheck and recheck <= learned:
            problems.append(f"{label}: source {i} recheck_by ({recheck}) is not after learned ({learned})")
        for field in entry.get("supports") or []:
            if field not in record:
                problems.append(f"{label}: source {i} supports {field!r}, which this record does not have")
    return problems


def visibility_problems(record: dict, label: str) -> list[str]:
    if record.get("visibility") not in ("staff", "public"):
        return []
    body = {k: v for k, v in record.items() if k not in TECHNICAL}
    hits: list[str] = []
    for m in INFRASTRUCTURE.finditer(json.dumps(body, default=str, ensure_ascii=False)):
        if m.group(0) not in hits:
            hits.append(m.group(0))
    if not hits:
        return []
    return [f"{label}: visibility {record['visibility']} but it names {', '.join(hits[:5])} outside source and"
            " signal; rewrite those fields in plain words or make the record internal"]


def ledger_problems() -> list[str]:
    """Every ledger row number is used once; two branches that each append rows can pick the same number."""
    if not LEDGER.exists():
        return []
    seen: dict[str, int] = {}
    for line in LEDGER.read_text(encoding="utf-8").splitlines():
        m = re.match(r"\|\s*(\d+)\s*\|", line)
        if m:
            seen[m.group(1)] = seen.get(m.group(1), 0) + 1
    return [f"questions/LEDGER.md: row number {n} is used {c} times; give the newer rows the next free numbers"
            for n, c in seen.items() if c > 1]


def all_problems() -> list[str]:
    problems: list[str] = []
    known = {f"{prefix}:{p.stem}" for folder, (_, prefix) in KINDS.items() for p in (ROOT / folder).glob("*.yaml")}
    for folder, (schema_name, prefix) in KINDS.items():
        directory = ROOT / folder
        if not directory.exists():
            continue
        validator = Draft202012Validator(json.loads((ROOT / "schema" / schema_name).read_text(encoding="utf-8")))
        for path in sorted(directory.glob("*.yaml")):
            label = f"{folder}/{path.name}"
            text = path.read_text(encoding="utf-8")
            record = yaml.safe_load(text)
            if not isinstance(record, dict):
                problems.append(f"{label}: not a mapping")
                continue
            for error in sorted(validator.iter_errors(record), key=lambda e: list(e.absolute_path)):
                where = "/".join(str(x) for x in error.absolute_path) or "<root>"
                problems.append(f"{label}: {where}: {error.message}")
            if record.get("key") != f"{prefix}:{path.stem}":
                problems.append(f"{label}: key {record.get('key')!r} does not match the file name (expected {prefix}:{path.stem})")
            if IDENTIFIER_SHAPE.search(text):
                problems.append(f"{label}: a six-or-more-digit number; records carry no identifiers")
            for m in RECORD_REF.finditer(text):
                ref = m.group(0)
                if ref not in known and not text[m.end():].startswith(NOT_YET):
                    problems.append(f"{label}: {ref} is not a record; add it or mark it{NOT_YET!r}")
            for field in ("owner", "decided_by"):
                if looks_like_a_person(str(record.get(field, ""))):
                    problems.append(f"{label}: {field} {record.get(field)!r} looks like a person; name the role")
            for actor in record.get("actor") or []:
                if isinstance(actor, dict) and looks_like_a_person(str(actor.get("role", ""))):
                    problems.append(f"{label}: actor {actor.get('role')!r} looks like a person; name the role")
            for cadence in record.get("cadences") or []:
                if isinstance(cadence, dict) and looks_like_a_person(str(cadence.get("with", ""))):
                    problems.append(f"{label}: cadence with {cadence.get('with')!r} looks like a person; name the role")
            problems.extend(source_problems(record, label))
            problems.extend(visibility_problems(record, label))
    problems.extend(ledger_problems())
    return problems


def main() -> int:
    problems = all_problems()
    counts = {folder: len(list((ROOT / folder).glob("*.yaml"))) for folder in KINDS}
    summary = ", ".join(f"{n} {k}" for k, n in counts.items())
    if problems:
        print("\n".join(problems))
        print(f"\n{len(problems)} problem(s) across {summary}")
        return 1
    print(f"OK: {summary} valid")
    return 0


if __name__ == "__main__":
    sys.exit(main())
