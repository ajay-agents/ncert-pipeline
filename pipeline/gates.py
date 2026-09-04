"""Gates run between stages. A failing gate halts the pipeline — Claude must not
'work around' one, it must fix the data or escalate to you.
"""
from __future__ import annotations

import re

from .protect import parity
from .schema import Chapter, Lang

NUMERIC = re.compile(r"-?\d+(?:\.\d+)?(?:\s*[×x]\s*10\^?-?\d+)?")


def gate_counts(chapter: Chapter, expected: dict[str, int] | None = None) -> list[str]:
    fails = []
    if not chapter.items:
        fails.append("chapter has zero items")
    for kind, n in (expected or {}).items():
        got = len(chapter.by_kind(kind))
        if got != n:
            fails.append(f"{kind}: expected {n}, got {got}")
    seen = set()
    for i in chapter.items:
        if i.id in seen:
            fails.append(f"duplicate item id {i.id}")
        seen.add(i.id)
        if not i.number:
            fails.append(f"{i.id}: empty number")
    return fails


def gate_solutions_present(chapter: Chapter, lang: Lang) -> list[str]:
    return [f"{i.id}: no solution ({lang})"
            for i in chapter.items
            if not i.solution.get(lang).strip()
            and not any(p.solution.get(lang).strip() for p in i.parts)]


def gate_bilingual(chapter: Chapter) -> list[str]:
    fails = []
    for i in chapter.items:
        if not i.question.has_both():
            fails.append(f"{i.id}: question missing a language")
        if (i.solution.en or i.solution.hi) and not i.solution.has_both():
            fails.append(f"{i.id}: solution missing a language")
    return fails


def gate_math_parity(before: Chapter, after: Chapter, lang: Lang) -> list[str]:
    """Run after stages 5, 6 and 7. Catches equations eaten by a rewrite."""
    fails = []
    b_index, a_index = before.index(), after.index()
    for item_id, b in b_index.items():
        a = a_index.get(item_id)
        if a is None:
            fails.append(f"{item_id}: dropped by stage")
            continue
        for field in ("question", "solution"):
            problems = parity(getattr(b, field).get(lang), getattr(a, field).get(lang))
            if problems:
                fails.append(f"{item_id}.{field}: {'; '.join(problems)}")
        if len(b.parts) != len(a.parts):
            fails.append(f"{item_id}: part count changed {len(b.parts)} -> {len(a.parts)}")
        for bp, ap in zip(b.parts, a.parts):
            for field in ("question", "solution"):
                problems = parity(getattr(bp, field).get(lang), getattr(ap, field).get(lang))
                if problems:
                    fails.append(f"{item_id} part {bp.label}.{field}: {'; '.join(problems)}")
    return fails


def gate_answers_unchanged(before: Chapter, after: Chapter, lang: Lang) -> list[str]:
    """Simplification may reword explanations. It may never move a number."""
    fails = []
    a_index = after.index()
    for item_id, b in before.index().items():
        a = a_index.get(item_id)
        if a is None:
            continue
        nb = NUMERIC.findall(b.final_answer.get(lang))
        na = NUMERIC.findall(a.final_answer.get(lang))
        if nb != na:
            fails.append(f"{item_id}: final answer changed {nb} -> {na}")
        for bp, ap in zip(b.parts, a.parts):
            pnb = NUMERIC.findall(bp.final_answer.get(lang))
            pna = NUMERIC.findall(ap.final_answer.get(lang))
            if pnb != pna:
                fails.append(f"{item_id} part {bp.label}: final answer changed {pnb} -> {pna}")
    return fails


def gate_question_text_frozen(before: Chapter, after: Chapter, lang: Lang) -> list[str]:
    """Question text is immutable in stage 6 — for exercises AND examples.

    CLAUDE.md Rule 4: 'example solutions may be simplified; example questions
    may not.' Only an example's solution is fair game for simplification.
    """
    fails = []
    a_index = after.index()
    for item_id, b in before.index().items():
        a = a_index.get(item_id)
        if a is None:
            continue
        if a.question.get(lang).strip() != b.question.get(lang).strip():
            fails.append(f"{item_id}: question text was modified")
        for bp, ap in zip(b.parts, a.parts):
            if ap.question.get(lang).strip() != bp.question.get(lang).strip():
                fails.append(f"{item_id} part {bp.label}: question text was modified")
    return fails


def report(name: str, fails: list[str], hard: bool = True) -> None:
    if not fails:
        print(f"PASS  {name}")
        return
    print(f"FAIL  {name}  ({len(fails)})")
    for f in fails[:20]:
        print(f"      - {f}")
    if len(fails) > 20:
        print(f"      ... and {len(fails) - 20} more")
    if hard:
        raise SystemExit(1)
