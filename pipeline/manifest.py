"""Append-only audit trail for one chapter's run through the pipeline.

CLAUDE.md requires every stage to append: stage name, timestamp, input
hashes, counts, gate results, model calls. Left as prose, eight independent
sessions would each invent their own field names and format. This is the one
place that format is defined, so `manifest.json` stays readable by later
tooling instead of being eight slightly-different ad hoc dumps.
"""
from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path


def input_hashes(*paths: str | Path) -> dict[str, str]:
    """{filename: short sha256} for every path that exists. Skips missing ones
    rather than raising — a stage may have fewer inputs than usual."""
    out = {}
    for p in paths:
        p = Path(p)
        if p.exists():
            out[p.name] = hashlib.sha256(p.read_bytes()).hexdigest()[:16]
    return out


def append(chapter_dir: str | Path, stage: str, *,
           inputs: dict[str, str] | None = None,
           counts: dict[str, int] | None = None,
           gate_results: dict[str, list[str]] | None = None,
           model_calls: int = 0,
           notes: str | None = None) -> None:
    """Append one entry to <chapter_dir>/manifest.json (created if absent).

    `gate_results` is {gate_name: failure_list} — pass every gate the stage
    ran, including the ones that passed (empty list). A stage whose hard gate
    failed should still call this so the failure is on record.
    """
    path = Path(chapter_dir) / "manifest.json"
    entries = json.loads(path.read_text(encoding="utf-8")) if path.exists() else []
    gate_results = gate_results or {}
    entries.append({
        "stage": stage,
        "at": datetime.now(timezone.utc).isoformat(),
        "inputs": inputs or {},
        "counts": counts or {},
        "gates_failed": {k: v for k, v in gate_results.items() if v},
        "gates_passed": [k for k, v in gate_results.items() if not v],
        "model_calls": model_calls,
        "notes": notes,
    })
    path.write_text(json.dumps(entries, indent=2, ensure_ascii=False), encoding="utf-8")


def unchanged_since(chapter_dir: str | Path, stage: str, *paths: str | Path) -> bool:
    """True if `stage`'s most recent manifest entry already ran against these
    exact input hashes — the signal a stage should skip re-running."""
    path = Path(chapter_dir) / "manifest.json"
    if not path.exists():
        return False
    entries = [e for e in json.loads(path.read_text(encoding="utf-8")) if e["stage"] == stage]
    if not entries:
        return False
    return entries[-1]["inputs"] == input_hashes(*paths)
