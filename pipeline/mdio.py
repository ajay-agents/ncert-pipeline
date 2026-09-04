"""Markdown <-> Chapter/Item/Correction serialization - the on-disk format
used at every stage from stage 2 onward.

`render.py` already writes Chapter/Item -> container markdown (`:::example`,
`:::prompt`, `:::solution`, ...) for stages 4 and 7; `tag.py`'s `_parse()`
already turns that markup into a tree. This module is the missing read
direction, so that same container format can be the on-disk format at
*every* stage, not just the later ones - no separate JSON layer. Every
gate/match/verify function keeps operating on Chapter/Item objects exactly
as before; only how those objects reach/leave disk changes.
"""
from __future__ import annotations

import re

from . import render as _render
from . import tag as _tag
from .schema import Chapter, Correction, Figure, Item, Lang, Part, SourceRef, Text

# Stage 2's three un-merged lists, matching the old JSON dict's keys exactly
# (`{"examples": [...], "exercises": [...], "solutions": [...]}`). Fixed,
# English, structural markers - parsed by code, not shown to a student, so
# they don't need to be per-language the way render.py's SECTIONS are.
_SECTION_HEADINGS = {
    "examples": "## Examples",
    "exercises": "## Exercise Questions",
    "solutions": "## Raw Solutions",
}


def _heading_section(line: str) -> str | None:
    line = line.strip()
    for section, heading in _SECTION_HEADINGS.items():
        if line == heading:
            return section
    return None


def _child_dicts(children: list, name: str) -> list[dict]:
    return [c for c in children if isinstance(c, dict) and c["name"] == name]


def _node_text(node: dict) -> str | None:
    """Join a leaf container's own direct string children into one text
    blob. Prompt/solution/answer/figure-caption content is always flat
    markdown at these stages - stage 7 is what introduces nested
    :::step/:::formula containers, so a nested dict here means this text
    was pointed at a structured.<lang>.md (post-stage-7) file by mistake."""
    for c in node["children"]:
        if isinstance(c, dict):
            raise ValueError(
                f"unexpected nested container '{c['name']}' inside "
                f"'{node['name']}' - markdown_to_items/markdown_to_chapter "
                "only understand pre-stage-7 (flat) item structure"
            )
    parts = [c.strip() for c in node["children"] if isinstance(c, str)]
    text = "\n\n".join(p for p in parts if p)
    return text or None


_ANSWER_PREFIX_CACHE: dict[Lang, re.Pattern] = {}


def _answer_prefix_re(lang: Lang) -> re.Pattern:
    if lang not in _ANSWER_PREFIX_CACHE:
        label = _render.LABELS[lang]["answer"]
        _ANSWER_PREFIX_CACHE[lang] = re.compile(rf"^\*\*{re.escape(label)}:\*\*\s*")
    return _ANSWER_PREFIX_CACHE[lang]


def _strip_answer_prefix(text: str | None, lang: Lang) -> str | None:
    """render_item() bakes '**{Answer label}:** ' into the answer body
    (unlike :::solution, which correctly carries its label as an attr) -
    undo that here rather than changing render.py's already-working output
    shape, which stage 7/8 render on unchanged."""
    if text is None:
        return None
    stripped = _answer_prefix_re(lang).sub("", text, count=1)
    return stripped or None


def _node_to_item(node: dict, lang: Lang) -> Item:
    attrs = node["attrs"]
    children = node["children"]

    prompt_nodes = _child_dicts(children, "prompt")
    question = _node_text(prompt_nodes[0]) if prompt_nodes else None

    figures = []
    for fig_node in _child_dicts(children, "figure"):
        figures.append(Figure(
            id=fig_node["attrs"].get("id", ""),
            src=fig_node["attrs"].get("src", ""),
            caption=Text(**{lang: _node_text(fig_node)}),
        ))

    parts = []
    for part_node in _child_dicts(children, "part"):
        pc = part_node["children"]
        p_prompt = _child_dicts(pc, "prompt")
        p_solution = _child_dicts(pc, "solution")
        p_answer = _child_dicts(pc, "answer")
        parts.append(Part(
            label=part_node["attrs"].get("label", ""),
            question=Text(**{lang: _node_text(p_prompt[0]) if p_prompt else None}),
            solution=Text(**{lang: _node_text(p_solution[0]) if p_solution else None}),
            final_answer=Text(**{lang: _strip_answer_prefix(
                _node_text(p_answer[0]) if p_answer else None, lang)}),
        ))

    solution_nodes = _child_dicts(children, "solution")
    solution = _node_text(solution_nodes[0]) if solution_nodes else None

    answer_nodes = _child_dicts(children, "answer")
    final_answer = _strip_answer_prefix(
        _node_text(answer_nodes[0]) if answer_nodes else None, lang)

    default_kind = "example" if node["name"] == "example" else "exercise"
    return Item(
        id=attrs.get("id", ""),
        kind=attrs.get("kind", default_kind),
        number=attrs.get("number", ""),
        question=Text(**{lang: question}),
        topic=Text(**{lang: attrs.get("topic") or None}),
        parts=parts,
        solution=Text(**{lang: solution}),
        final_answer=Text(**{lang: final_answer}),
        figures=figures,
        source=SourceRef(),
        verified=attrs.get("verified") == "True",
        simplified=attrs.get("simplified") == "True",
        corrections_applied=int(attrs.get("corrections_applied") or 0),
    )


def items_to_markdown(items_by_section: dict[str, list[Item]], lang: Lang) -> str:
    """Stage 2's shape - {"examples": [...], "exercises": [...],
    "solutions": [...]} - as three headed sections of item blocks. Inverse
    of markdown_to_extraction()."""
    out: list[str] = []
    for section, heading in _SECTION_HEADINGS.items():
        items = items_by_section.get(section) or []
        if not items:
            continue
        out.append(heading)
        out.append("")
        out.extend(_render.render_item(i, lang) for i in items)
    return "\n".join(out).rstrip() + "\n"


def markdown_to_extraction(text: str, lang: Lang) -> dict[str, list[Item]]:
    """Inverse of items_to_markdown()."""
    tree = _tag._parse(text.splitlines())
    result: dict[str, list[Item]] = {s: [] for s in _SECTION_HEADINGS}
    current: str | None = None
    for child in tree["children"]:
        if isinstance(child, str):
            for line in child.splitlines():
                section = _heading_section(line)
                if section:
                    current = section
            continue
        if isinstance(child, dict) and child["name"] in ("example", "question"):
            if current is None:
                raise ValueError("item block found before any section heading")
            result[current].append(_node_to_item(child, lang))
    return result


def markdown_to_items(text: str, lang: Lang) -> list[Item]:
    """Parse a flat sequence of :::example/:::question blocks (no section
    headings to track - each item's own `kind` attr is enough once the
    three stage-2 lists have been merged, from stage 3 onward)."""
    tree = _tag._parse(text.splitlines())
    return [
        _node_to_item(child, lang)
        for child in tree["children"]
        if isinstance(child, dict) and child["name"] in ("example", "question")
    ]


def markdown_to_chapter(text: str, lang: Lang) -> Chapter:
    """Inverse of render.render(): parse its YAML-ish front matter for
    chapter metadata, then markdown_to_items() for the body."""
    meta: dict[str, str] = {}
    body = text
    if text.startswith("---"):
        _, front, body = text.split("---", 2)
        for line in front.strip().splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                meta[k.strip()] = v.strip().strip('"')

    items = markdown_to_items(body, lang)
    return Chapter(
        subject=meta.get("subject", "physics"),
        class_level=int(meta.get("class") or 0),
        chapter_number=meta.get("chapter", ""),
        title=Text(**{lang: meta.get("title")}),
        items=items,
    )


def merge_by_id(en: Chapter | None, hi: Chapter | None) -> Chapter:
    """Reassemble a bilingual Chapter from two per-language Chapters whose
    items already share the same `id` (true from stage 3 onward). Simpler
    than match.align_languages(), which does first-time fuzzy alignment;
    this is a plain id-keyed merge, and handles a chapter that only ever
    had one language (e.g. the existing Hindi-only physics-12-1)."""
    if en is None and hi is None:
        raise ValueError("merge_by_id needs at least one language")
    if en is None:
        return hi
    if hi is None:
        return en

    hi_index = hi.index()
    for item in en.items:
        partner = hi_index.get(item.id)
        if partner is None:
            continue
        item.question.hi = partner.question.get("hi") or None
        item.topic.hi = partner.topic.get("hi") or None
        item.solution.hi = partner.solution.get("hi") or None
        item.final_answer.hi = partner.final_answer.get("hi") or None
        for a, b in zip(item.parts, partner.parts):
            a.question.hi = b.question.get("hi") or None
            a.solution.hi = b.solution.get("hi") or None
            a.final_answer.hi = b.final_answer.get("hi") or None
        for a, b in zip(item.figures, partner.figures):
            a.caption.hi = b.caption.get("hi") or None
        item.verified = item.verified or partner.verified
        item.simplified = item.simplified or partner.simplified
        item.corrections_applied = max(item.corrections_applied, partner.corrections_applied)
    en.title.hi = hi.title.get("hi") or en.title.get("hi")
    return en


# --- corrections: flat records, no nesting, so a small line-based format
# (not the container-tag machinery) is simpler and just as robust. ---

_CORRECTION_HEADING_RE = re.compile(
    r"^###\s+(?P<item_id>\S+)\s+—\s+(?P<field>\S+)\s+\((?P<lang>en|hi)\)\s*$"
)


def corrections_to_markdown(corrections: list[Correction]) -> str:
    out: list[str] = []
    for c in corrections:
        out.append(f"### {c.item_id} — {c.field} ({c.lang})")
        out.append(f"- **Confidence:** {c.confidence}")
        out.append(f"- **Reason:** {c.reason}")
        out.append("- **Found:**")
        # split("\n") (not splitlines()) so "\n".join(...) on the read side
        # reconstructs the original string exactly, trailing newlines
        # included - splitlines() silently drops that information.
        for line in c.found.split("\n"):
            out.append(f"  > {line}")
        out.append("- **Should be:**")
        for line in c.should_be.split("\n"):
            out.append(f"  > {line}")
        out.append("")
    return "\n".join(out).rstrip() + "\n"


def markdown_to_corrections(text: str) -> list[Correction]:
    corrections: list[dict] = []
    current: dict | None = None
    # Collect each field's blockquote lines in a list and join once at the
    # end - NOT by concatenating onto a string as pieces arrive, which
    # breaks the instant the first piece happens to be an empty line (an
    # empty accumulator is indistinguishable from "no piece seen yet").
    current_lines: dict[str, list[str]] = {}
    field_buf: str | None = None

    def _flush():
        if current is not None:
            current["found"] = "\n".join(current_lines.get("found") or [""])
            current["should_be"] = "\n".join(current_lines.get("should_be") or [""])
            corrections.append(Correction(**current))

    for line in text.splitlines():
        m = _CORRECTION_HEADING_RE.match(line)
        if m:
            _flush()
            current = {"item_id": m["item_id"], "field": m["field"], "lang": m["lang"],
                       "confidence": "medium", "reason": ""}
            current_lines = {}
            field_buf = None
            continue
        if current is None:
            continue
        stripped = line.strip()
        if stripped.startswith("- **Confidence:**"):
            current["confidence"] = stripped.split("**Confidence:**", 1)[1].strip()
        elif stripped.startswith("- **Reason:**"):
            current["reason"] = stripped.split("**Reason:**", 1)[1].strip()
        elif stripped.startswith("- **Found:**"):
            field_buf = "found"
            current_lines[field_buf] = []
        elif stripped.startswith("- **Should be:**"):
            field_buf = "should_be"
            current_lines[field_buf] = []
        elif stripped.startswith(">") and field_buf:
            current_lines[field_buf].append(stripped[1:].strip())
    _flush()
    return corrections


def match_report_to_markdown(report: dict) -> str:
    """Write-only human/model-readable report - nothing downstream re-parses
    this as a typed object, so no matching reader is needed."""
    out = ["# Match report", ""]
    for key, value in report.items():
        if isinstance(value, list):
            out.append(f"## {key} ({len(value)})")
            for v in value:
                out.append(f"- {v}")
            out.append("")
        else:
            out.append(f"- **{key}:** {value}")
    return "\n".join(out).rstrip() + "\n"
