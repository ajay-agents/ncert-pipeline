"""Stage 8. Walk a structured.<lang>.md container tree (tag._parse) into the
JSON shape stage 9 renders from: prompt/answer/flow are ordered text+figure
segment lists, and every stageable solution block gets a given/key_formula/
substitute/conclusion `stage`.

The given/key-formula/substitute/conclusion call is documented in
step_8/PROMPT.md as a fully mechanical rule once stage 7's own labelling
call is taken as authoritative (an explicit :::concept is always "given", an
explicit :::formula is always "key_formula" regardless of position; an
unlabelled plain :::step or bare-text block is "given" if first among the
solution's stageable blocks, "conclusion" if last, "substitute" otherwise,
and "conclusion" outright if it is the only one) - so it is implemented here
as code, not re-decided per chapter. `:::note`/`:::figure`/`:::table` never
carry a stage and are excluded from the position count.
"""
from __future__ import annotations

import re
from typing import Any

from . import render as _render
from . import tag as _tag

_STAGE_EXCLUDED = {"note", "figure", "table"}
_ANSWER_PREFIX_CACHE: dict[str, re.Pattern] = {}
_SOLUTION_OPENER_RE = re.compile(
    r'^(?:\\text\{)?(?:हल|उत्तर)\s*[:：]?\s*\}?\s*'  # हल/उत्तर, with or
    # without a colon, with or without \text{...} wrapping. Different
    # solutions-manual publishers use different Hindi words for "Solution:" -
    # हल is the chemistry/physics-manual convention already handled here;
    # उत्तर ("answer") is a biology-manual convention that surfaced for real
    # on biology-12-4 (every one of its 16 items opens "उत्तर : ...", and
    # none were stripped because this regex only knew हल). biology-12-1/2/3
    # never hit this same gap only because those chapters' own solution text
    # was built by hand-typing clean content directly rather than
    # transcribing the source verbatim - the underlying source documents
    # likely use "उत्तर :" too and would show the same leak if re-extracted
    # verbatim. Extend this list again if a future chapter's own solutions
    # manual uses yet another convention (e.g. "समाधान").
)
_NOTE_TYPE_LABELS_HI = {"caution": "सावधानी",
                         "recall": "याद रखें",
                         "tip": "सुझाव"}
_NOTE_TYPE_LABELS_EN = {"caution": "Caution", "recall": "Recall", "tip": "Tip"}


def _child_dicts(children: list, name: str) -> list[dict]:
    return [c for c in children if isinstance(c, dict) and c["name"] == name]


def _strip_hal_opener(flow: list[dict]) -> list[dict]:
    """Strip a leading हल/उत्तर opener (with or without a colon) from the
    very first text segment of a solution's flow - the source solutions
    manual's own redundant "Solution:"/"Answer:" opener, whichever word that
    particular manual happens to use."""
    if not flow or flow[0]["type"] != "text":
        return flow
    text = flow[0]["text"]
    stripped = _SOLUTION_OPENER_RE.sub("", text, count=1).lstrip()
    if stripped == text:
        return flow
    out = list(flow)
    if stripped:
        out[0] = {**out[0], "text": stripped}
    else:
        out = out[1:]
    return out


def build_flow(children: list, lang: str) -> list[dict[str, Any]]:
    """Ordered text/figure/table segments from a container's direct
    children, recursing into a nested :::figure wherever it occurs so a
    figure placed inside a :::step still shows up in that step's own flow,
    in position - and likewise a :::table (a data table given alongside a
    question's own prompt, e.g. "the following data was obtained-", is a
    real and common shape, not just a solution-side occurrence).

    Used for prompt/answer/caption flows, and for a "step" block's own flow
    after `_flatten_children` has already promoted any nested concept/
    formula/note/table/figure out of it - so in practice this only ever sees
    plain strings (and, for prompt/answer, a bare figure or table) by the
    time it runs on solution content."""
    out: list[dict[str, Any]] = []
    for c in children:
        if isinstance(c, str):
            t = c.strip()
            if t:
                out.append({"type": "text", "text": t})
        elif isinstance(c, dict) and c["name"] == "figure":
            cap_segs = build_flow(c["children"], lang)
            caption = " ".join(s["text"] for s in cap_segs if s["type"] == "text").strip()
            out.append({"type": "figure", "src": c["attrs"].get("src", ""), "caption": caption})
        elif isinstance(c, dict) and c["name"] == "table":
            out.append({"type": "table", "html": _table_markdown(c)})
    return out


_LEAF_PROMOTABLE = {"concept", "formula", "note", "table", "figure"}
_ALL_CONTAINERS = _LEAF_PROMOTABLE | {"step"}


def _flatten_children(children: list) -> list[tuple[str, dict]]:
    """Flatten a :::solution/:::part's children into a flat, ordered list of
    (kind, node) pairs, promoting any :::concept/:::formula/:::note/:::table/
    :::figure nested inside ANOTHER container - a :::step, or a :::concept/
    :::formula/:::note wrapping one in turn - to its own top-level entry.

    Stage 7 sometimes nests these for narrative flow: a step's own text
    leading into a formula, then continuing after it; a concept whose
    definition itself sets a formula apart mid-explanation. Real cases from
    this pipeline's own chapters: a step wrapping a formula, a step wrapping
    a concept, and (the one a step-only fix would still miss) a concept
    wrapping a formula. The JSON schema keeps every stageable/note/table/
    figure block as its own flat solution_blocks entry (step_8/PROMPT.md:
    "keep each source block as its own JSON entry"), and `build_flow` only
    understands plain text and a bare figure - so any wrapper swallowing a
    nested formula/concept/note/table would silently drop it. Splitting the
    wrapper's own text around each promoted block, in original order, and
    keeping the wrapper's own kind (a concept split around a nested formula
    yields two "concept" fragments, not "step" ones) is the fix.

    kind is the (possibly synthetic) block's own name - "step"/"concept"/
    "formula"/"note" for a text-bearing block (dict with "attrs"/"children"),
    or "table"/"figure" for a leaf with no further splitting.
    """
    out: list[tuple[str, dict]] = []

    def has_nested(items: list) -> bool:
        return any(isinstance(c, dict) and c["name"] in _ALL_CONTAINERS for c in items)

    def emit_run(kind: str, buf: list, attrs: dict) -> None:
        if buf:
            out.append((kind, {"attrs": attrs, "children": buf}))

    def walk(items: list, wrapper_kind: str, attrs_for_first: dict | None) -> None:
        buf: list = []
        attrs = attrs_for_first or {}
        for c in items:
            if isinstance(c, dict) and c["name"] in _ALL_CONTAINERS:
                emit_run(wrapper_kind, buf, attrs); buf = []; attrs = {}
                if c["name"] in ("table", "figure") or not has_nested(c["children"]):
                    out.append((c["name"], c))
                else:
                    walk(c["children"], c["name"], c["attrs"])
            else:
                buf.append(c)
        emit_run(wrapper_kind, buf, attrs)

    walk(children, "step", None)
    return out


def _table_markdown(node: dict) -> str:
    return "\n".join(c for c in node["children"] if isinstance(c, str)).strip()


def _note_label(node: dict, lang: str) -> str | None:
    label = node["attrs"].get("label") or None
    if label:
        return label
    note_type = node["attrs"].get("type", "")
    table = _NOTE_TYPE_LABELS_HI if lang == "hi" else _NOTE_TYPE_LABELS_EN
    return table.get(note_type)


def build_solution_blocks(children: list, lang: str) -> list[dict[str, Any]]:
    raw = _flatten_children(children)

    stageable_idxs = [i for i, (kind, _) in enumerate(raw) if kind not in _STAGE_EXCLUDED]

    def infer_stage(i: int) -> str:
        if len(stageable_idxs) == 1:
            return "conclusion"
        pos = stageable_idxs.index(i)
        if pos == 0:
            return "given"
        if pos == len(stageable_idxs) - 1:
            return "conclusion"
        return "substitute"

    blocks: list[dict[str, Any]] = []
    for i, (kind, node) in enumerate(raw):
        if kind == "step":
            label = node["attrs"].get("label")
            stage = label if label in ("given", "key_formula", "substitute", "conclusion") else infer_stage(i)
            block = {"type": "step", "stage": stage, "flow": build_flow(node["children"], lang)}
            if label and label not in ("given", "key_formula", "substitute", "conclusion"):
                block["label"] = label
            blocks.append(block)
        elif kind == "concept":
            block = {"type": "concept", "stage": "given", "flow": build_flow(node["children"], lang)}
            if node["attrs"].get("label"):
                block["label"] = node["attrs"]["label"]
            blocks.append(block)
        elif kind == "formula":
            block = {"type": "formula", "stage": "key_formula", "flow": build_flow(node["children"], lang)}
            if node["attrs"].get("label"):
                block["label"] = node["attrs"]["label"]
            blocks.append(block)
        elif kind == "note":
            blocks.append({
                "type": "note",
                "note_type": node["attrs"].get("type", ""),
                "label": _note_label(node, lang),
                "flow": build_flow(node["children"], lang),
            })
        elif kind == "figure":
            cap_segs = build_flow(node["children"], lang)
            caption = " ".join(s["text"] for s in cap_segs if s["type"] == "text").strip()
            blocks.append({"type": "figure", "src": node["attrs"].get("src", ""), "caption": caption})
        elif kind == "table":
            blocks.append({"type": "table", "html": _table_markdown(node)})

    if blocks and blocks[0]["type"] in ("step", "concept") and blocks[0].get("flow"):
        blocks[0]["flow"] = _strip_hal_opener(blocks[0]["flow"])
    return blocks


def _answer_prefix_re(lang: str) -> re.Pattern:
    if lang not in _ANSWER_PREFIX_CACHE:
        label = _render.LABELS[lang]["answer"]
        _ANSWER_PREFIX_CACHE[lang] = re.compile(rf"^\*\*{re.escape(label)}:\*\*\s*")
    return _ANSWER_PREFIX_CACHE[lang]


def _strip_answer_flow_prefix(flow: list[dict[str, Any]], lang: str) -> list[dict[str, Any]]:
    """render_item() bakes '**{Answer label}:** ' into an :::answer block's
    own text (mdio.py's markdown_to_chapter() already undoes this on the
    read-back-into-Chapter path via its own _strip_answer_prefix - this is
    the same fix for serialize.py's separate structured-markdown-to-JSON
    path, which parses the :::answer container's raw text directly and had
    no equivalent stripping, so every 'answer' flow this stage ever produced
    carried the literal '**उत्तर:**'/'**Answer:**' markdown text visible at
    stage 9. Strip only the first text segment's leading occurrence."""
    if not flow or flow[0]["type"] != "text":
        return flow
    text = flow[0]["text"]
    stripped = _answer_prefix_re(lang).sub("", text, count=1)
    if stripped == text:
        return flow
    out = list(flow)
    if stripped:
        out[0] = {**out[0], "text": stripped}
    else:
        out = out[1:]
    return out


def _collect_figures(node: dict) -> list[dict[str, str]]:
    figs = []
    for fig in _child_dicts(node["children"], "figure"):
        cap_segs = build_flow(fig["children"], "hi")
        caption = " ".join(s["text"] for s in cap_segs if s["type"] == "text").strip()
        figs.append({"src": fig["attrs"].get("src", ""), "caption": caption})
    return figs


def _part_to_json(node: dict, lang: str) -> dict[str, Any]:
    prompt_nodes = _child_dicts(node["children"], "prompt")
    solution_nodes = _child_dicts(node["children"], "solution")
    answer_nodes = _child_dicts(node["children"], "answer")
    out: dict[str, Any] = {
        "label": node["attrs"].get("label", ""),
        "prompt": build_flow(prompt_nodes[0]["children"], lang) if prompt_nodes else [],
        "solution_blocks": build_solution_blocks(solution_nodes[0]["children"], lang) if solution_nodes else [],
    }
    if answer_nodes:
        out["answer"] = _strip_answer_flow_prefix(build_flow(answer_nodes[0]["children"], lang), lang)
    return out


def _item_to_json(node: dict, lang: str) -> dict[str, Any]:
    attrs = node["attrs"]
    prompt_nodes = _child_dicts(node["children"], "prompt")
    parts = [_part_to_json(p, lang) for p in _child_dicts(node["children"], "part")]
    solution_nodes = _child_dicts(node["children"], "solution")
    answer_nodes = _child_dicts(node["children"], "answer")

    # Known duplicate-solution artifact: a multi-part item's own trailing
    # whole-item :::solution just re-narrates the parts' own working - leave
    # item-level solution_blocks empty and let the parts carry it. But this
    # only applies when the parts actually HAVE their own solution content -
    # some multi-part items (e.g. a question with (i)-(vi) sub-prompts but
    # one single flowing answer covering all of them) carry NO per-part
    # solution at all, and the item-level :::solution is the only real
    # content, not a duplicate; suppressing it there would silently drop
    # the chapter's entire worked answer for that item (caught for real via
    # this stage's own figure-count gate on chemistry-12-3's q_3.15, whose
    # two graphs live inside that item-level solution).
    parts_have_solutions = any(p.get("solution_blocks") for p in parts)
    solution_blocks = [] if (parts and parts_have_solutions) else (
        build_solution_blocks(solution_nodes[0]["children"], lang) if solution_nodes else [])

    default_kind = "example" if node["name"] == "example" else "exercise"
    out: dict[str, Any] = {
        "id": attrs.get("id", ""),
        "kind": attrs.get("kind", default_kind),
        "number": attrs.get("number", ""),
        "topic": attrs.get("topic", ""),
        "prompt": build_flow(prompt_nodes[0]["children"], lang) if prompt_nodes else [],
        "figures": _collect_figures(node),
    }
    if parts:
        out["parts"] = parts
    out["solution_blocks"] = solution_blocks
    if answer_nodes:
        out["answer"] = _strip_answer_flow_prefix(build_flow(answer_nodes[0]["children"], lang), lang)
    return out


def structured_md_to_json(text: str, lang: str, title: str, chapter: str) -> dict[str, Any]:
    tree = _tag._parse(text.splitlines())
    items = [
        _item_to_json(child, lang)
        for child in tree["children"]
        if isinstance(child, dict) and child["name"] in ("example", "question")
    ]
    return {"front": {"title": title, "chapter": chapter}, "items": items}


def count_figures_in_raw_text(text: str) -> set[str]:
    """Distinct figure src count straight from the source text, independent
    of the JSON walk above - used as the stage's fresh cross-check."""
    srcs = set(re.findall(r'src="([^"]+)"', text))
    srcs |= set(m for m in re.findall(r'!\[[^\]]*\]\(([^)]+)\)', text))
    return srcs
