"""Stage 5. Applying a correction is arithmetic, not judgement — the model
decides *what* is wrong (step_5/verify.md); this module decides *how* the
fix lands in the Chapter, so Claude never hand-edits the chapter markdown to
apply one.
"""
from __future__ import annotations

import re

from .schema import Chapter, Correction, Lang

_PART_FIELD = re.compile(r"^parts\[(\d+)\]\.(question|solution|final_answer)$")
_CONFIDENCE = {"low": 0, "medium": 1, "high": 2}


def _text_field(item, field: str):
    m = _PART_FIELD.match(field)
    if m:
        return getattr(item.parts[int(m.group(1))], m.group(2))
    return getattr(item, field)


def apply_corrections(chapter: Chapter, corrections: list[Correction],
                       min_confidence: str = "high") -> tuple[Chapter, list[str], list[str]]:
    """Apply each correction's found -> should_be replacement in place.

    Only corrections at or above min_confidence are applied; the rest come
    back in `held` for the user to review before a second, explicit pass.
    A correction whose `found` text is not an exact, unique substring of the
    current field is never guessed at — it comes back in `held` too.

    Returns (chapter, applied, held) — both lists are one line per correction.
    """
    index = chapter.index()
    applied: list[str] = []
    held: list[str] = []

    for c in corrections:
        label = f"{c.item_id}.{c.field} ({c.lang})"
        item = index.get(c.item_id)
        if item is None:
            held.append(f"{label}: item not found")
            continue
        try:
            text = _text_field(item, c.field)
        except (IndexError, AttributeError):
            held.append(f"{label}: field not found")
            continue

        if _CONFIDENCE[c.confidence] < _CONFIDENCE[min_confidence]:
            held.append(f"{label}: {c.confidence} confidence — {c.reason}")
            continue

        current = text.get(c.lang)
        count = current.count(c.found)
        if count != 1:
            held.append(f"{label}: 'found' text appears {count} time(s), expected exactly 1")
            continue

        setattr(text, c.lang, current.replace(c.found, c.should_be))
        item.corrections_applied += 1
        applied.append(f"{label}: {c.reason}")

    return chapter, applied, held
