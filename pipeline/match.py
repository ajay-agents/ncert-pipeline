"""Joining is arithmetic, not judgement. Claude only sees what fails to join."""
from __future__ import annotations

import re
from difflib import SequenceMatcher

from .schema import Chapter, Item, Text

_PREFIX = re.compile(
    r"^\s*(?:q\.?|question|ex\.?|example|प्रश्न|उदाहरण|अभ्यास)\s*[:.\-]?\s*",
    re.I,
)


def norm_num(raw: str, chapter: str | None = None) -> str:
    """'Q. 3', '10.3', 'प्रश्न 3.' -> '10.3' when chapter='10'."""
    s = _PREFIX.sub("", str(raw).strip().lower())
    s = s.strip(" .:)(]}[")
    s = re.sub(r"[^\d.]", "", s)
    s = re.sub(r"\.+", ".", s).strip(".")
    if not s:
        return ""
    if chapter and "." not in s:
        s = f"{chapter}.{s}"
    return s


def _similar(a: str, b: str) -> float:
    norm = lambda t: re.sub(r"\s+", " ", re.sub(r"[^\w\s]", "", t.lower())).strip()
    return SequenceMatcher(None, norm(a)[:400], norm(b)[:400]).ratio()


def join_solutions(questions: list[Item], solutions: list[Item],
                   chapter: str, lang: str = "en",
                   fuzzy_threshold: float = 0.72) -> tuple[list[Item], dict]:
    """Attach solutions to questions by number, then by text similarity.

    Returns (merged_items, report). Anything in report['needs_review'] is what
    stage 3 hands to Claude — never the whole set.
    """
    sol_by_num: dict[str, Item] = {}
    duplicate_sols: list[str] = []
    for s in solutions:
        key = norm_num(s.number, chapter)
        if key in sol_by_num:
            duplicate_sols.append(key)
            continue
        sol_by_num[key] = s

    merged: list[Item] = []
    unmatched_q: list[str] = []
    used: set[str] = set()

    for q in questions:
        n = norm_num(q.number, chapter)
        q.number = n
        hit = sol_by_num.get(n)
        if hit is None:
            best, score = None, 0.0
            for key, cand in sol_by_num.items():
                if key in used:
                    continue
                sc = _similar(q.question.get(lang), cand.question.get(lang))
                if sc > score:
                    best, score = cand, sc
            if best is not None and score >= fuzzy_threshold:
                hit = best
        if hit is None:
            unmatched_q.append(n)
            merged.append(q)
            continue

        used.add(norm_num(hit.number, chapter))
        setattr(q.solution, lang, hit.solution.get(lang) or None)
        setattr(q.final_answer, lang, hit.final_answer.get(lang) or None)
        if hit.figures:
            existing_ids = {f.id for f in q.figures}
            q.figures.extend(f for f in hit.figures if f.id not in existing_ids)
        if hit.parts and len(hit.parts) == len(q.parts):
            for qp, sp in zip(q.parts, hit.parts):
                setattr(qp.solution, lang, sp.solution.get(lang) or None)
                setattr(qp.final_answer, lang, sp.final_answer.get(lang) or None)
        elif hit.parts and not q.parts:
            q.parts = hit.parts
        merged.append(q)

    orphan_sols = [n for n in sol_by_num if n not in used]
    report = {
        "questions": len(questions),
        "solutions": len(solutions),
        "matched": len(questions) - len(unmatched_q),
        "unmatched_questions": unmatched_q,
        "orphan_solutions": orphan_sols,
        "duplicate_solutions": duplicate_sols,
        "needs_review": unmatched_q + orphan_sols + duplicate_sols,
    }
    return merged, report


def align_languages(en: Chapter, hi: Chapter) -> tuple[Chapter, dict]:
    """Merge the English and Hindi extractions of the same chapter into one Chapter."""
    hi_index = {norm_num(i.number, hi.chapter_number): i for i in hi.items}
    only_en, only_hi, kind_mismatch = [], [], []

    for item in en.items:
        n = norm_num(item.number, en.chapter_number)
        partner = hi_index.pop(n, None)
        if partner is None:
            only_en.append(n)
            continue
        if partner.kind != item.kind:
            # Merge anyway — the Hindi text is still real content; a kind-label
            # disagreement between two independent extraction passes is a
            # labeling question, not a reason to throw away a translation.
            kind_mismatch.append({"number": n, "en_kind": item.kind, "hi_kind": partner.kind})
        item.question.hi = partner.question.get("hi") or None
        item.topic.hi = partner.topic.get("hi") or None
        item.solution.hi = partner.solution.get("hi") or None
        item.final_answer.hi = partner.final_answer.get("hi") or None
        if len(item.parts) == len(partner.parts):
            for a, b in zip(item.parts, partner.parts):
                a.question.hi = b.question.get("hi") or None
                a.solution.hi = b.solution.get("hi") or None
                a.final_answer.hi = b.final_answer.get("hi") or None
        for a, b in zip(item.figures, partner.figures):
            a.caption.hi = b.caption.get("hi") or None

    only_hi = list(hi_index.keys())
    report = {"aligned": len(en.items) - len(only_en),
              "only_en": only_en, "only_hi": only_hi,
              "kind_mismatch": kind_mismatch,
              "needs_review": only_en + only_hi + [m["number"] for m in kind_mismatch]}
    return en, report
