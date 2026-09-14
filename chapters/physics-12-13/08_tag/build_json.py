# -*- coding: utf-8 -*-
"""Stage 8 tagging script for physics-12-13 (Nuclei / नाभिक).

Parses 07_format/structured.hi.md's container tree (via pipeline.tag._parse)
and walks it into the JSON shape step_8/PROMPT.md specifies: one object per
item with prompt/topic/parts/solution_blocks/answer/figures, each solution's
blocks carrying a "stage" of given/key_formula/substitute/conclusion.

This chapter's stage 7 pass (07_format/structured.hi.md) already assigned the
fixed vocabulary explicitly to every :::concept/:::formula/:::step it added
(concept="given" always, formula="key_formula" always, step labelled either
"मान रखो" (substitute) or "निष्कर्ष" (conclusion) - no step was left
unlabelled in this chapter), so the per-item judgment call is mostly a direct
label->stage lookup rather than positional inference. The one exception is
ex_13.4's three qualitative prose parts (a/b/c), deliberately left as plain
unwrapped text at stage 7 (no concept/formula/step at all - a purely
discursive discussion doesn't fit the numeric given/formula/substitute/
conclusion mold, per step_9/PROMPT.md's own guidance) - each becomes a single
synthetic "step" block with no label, and the positional-inference rule
("a solution with only one stageable block is entirely conclusion") applies.

No :::table anywhere in this chapter. Exactly one :::note (ex_13.1's
neutron-star remark, type="tip", already labelled). Zero figures (confirmed
at stage 2 - this chapter's 2 mathpix images are never referenced inside any
example/exercise).
"""
import sys, os, json, re, io

sys.path.insert(0, r"C:\Users\ajayr\Downloads\ncert-pipeline")
from pipeline import tag as _tag

ROOT = r"C:\Users\ajayr\Downloads\ncert-pipeline"
CH = os.path.join(ROOT, "chapters", "physics-12-13")

STAGE_LABEL_MAP = {
    "जानकारी": "given",
    "मुख्य सूत्र": "key_formula",
    "मान रखो": "substitute",
    "निष्कर्ष": "conclusion",
}

NOTE_DEFAULT_LABEL = {"caution": "सावधानी", "recall": "याद रखें", "tip": "सुझाव"}

_SOLUTION_OPENER_RE = re.compile(r"^\s*(?:हल\s*:?\s*|\\text\s*\{\s*हल\s*:\s*\})", re.M)


def _child_dicts(children, name):
    return [c for c in children if isinstance(c, dict) and c["name"] == name]


def _flow_from_text(text):
    text = text.strip()
    if not text:
        return []
    return [{"type": "text", "text": text}]


def _flow_from_container(node):
    """Walk a container's direct children (strings and nested :::figure/
    :::table) into an ordered flow list. A :::figure nested inside e.g. a
    :::step's own flow (not just a bare top-level figure) must still show up
    in the flow at its right position - not exercised by this chapter's own
    content (no figures at all), but implemented for correctness."""
    flow = []
    for c in node["children"]:
        if isinstance(c, str):
            flow.extend(_flow_from_text(c))
        elif isinstance(c, dict) and c["name"] == "figure":
            flow.append({"type": "figure", "src": c["attrs"].get("src", ""),
                         "caption": _text_of(c)})
        elif isinstance(c, dict) and c["name"] == "table":
            flow.append({"type": "table", "html": _text_of(c)})
    return flow


def _text_of(node):
    return "\n\n".join(c.strip() for c in node["children"] if isinstance(c, str) and c.strip())


def _strip_solution_opener(blocks):
    """Strip a leading 'हल'/'हल:'/'हल :' opener from the very first block's
    first text segment, once. Not exercised by this chapter's own content
    (the textbook's own 'हल' opener is already carried as the :::solution
    container's own `label` attribute, never embedded as literal flow text)
    but implemented defensively per step_8/PROMPT.md."""
    if not blocks:
        return
    first = blocks[0]
    flow = first.get("flow")
    if not flow:
        return
    for seg in flow:
        if seg["type"] == "text":
            new_text = _SOLUTION_OPENER_RE.sub("", seg["text"], count=1)
            if new_text != seg["text"]:
                seg["text"] = new_text.strip()
            break
        else:
            break


def _build_stageable_blocks(solution_node):
    """Walk a :::solution (or :::part > :::solution) container's direct
    children into an ordered list of block dicts, each already carrying its
    "stage" (given/key_formula/substitute/conclusion) for concept/formula/
    step/bare-text blocks, or note/figure/table blocks with no stage."""
    raw_blocks = []  # (kind, node_or_text)
    for c in solution_node["children"]:
        if isinstance(c, str):
            if c.strip():
                raw_blocks.append(("bare", c))
        elif isinstance(c, dict):
            raw_blocks.append((c["name"], c))

    blocks = []
    stageable_idx = []  # indices into `blocks` that are stageable
    for kind, payload in raw_blocks:
        if kind == "concept":
            blocks.append({"type": "concept", "stage": "given",
                            "label": payload["attrs"].get("label") or "जानकारी",
                            "flow": _flow_from_container(payload)})
            stageable_idx.append(len(blocks) - 1)
        elif kind == "formula":
            blocks.append({"type": "formula", "stage": "key_formula",
                            "label": payload["attrs"].get("label") or "मुख्य सूत्र",
                            "flow": _flow_from_container(payload)})
            stageable_idx.append(len(blocks) - 1)
        elif kind == "step":
            label = payload["attrs"].get("label")
            stage = STAGE_LABEL_MAP.get(label)  # None if unlabelled/non-fixed
            blocks.append({"type": "step", "stage": stage, "label": label,
                            "flow": _flow_from_container(payload)})
            stageable_idx.append(len(blocks) - 1)
        elif kind == "bare":
            blocks.append({"type": "step", "stage": None, "label": None,
                            "flow": _flow_from_text(payload)})
            stageable_idx.append(len(blocks) - 1)
        elif kind == "note":
            note_type = payload["attrs"].get("type", "tip")
            label = payload["attrs"].get("label") or NOTE_DEFAULT_LABEL.get(note_type, "सुझाव")
            blocks.append({"type": "note", "note_type": note_type, "label": label,
                            "flow": _flow_from_container(payload)})
        elif kind == "figure":
            blocks.append({"type": "figure", "src": payload["attrs"].get("src", ""),
                            "caption": _text_of(payload)})
        elif kind == "table":
            blocks.append({"type": "table", "html": _text_of(payload)})

    # Positional fallback for any stageable block whose stage is still None.
    n = len(stageable_idx)
    for pos, bi in enumerate(stageable_idx):
        if blocks[bi]["stage"] is not None:
            continue
        if n == 1:
            blocks[bi]["stage"] = "conclusion"
        elif pos == 0:
            blocks[bi]["stage"] = "given"
        elif pos == n - 1:
            blocks[bi]["stage"] = "conclusion"
        else:
            blocks[bi]["stage"] = "substitute"

    _strip_solution_opener(blocks)
    return blocks


def _build_answer(answer_node):
    if answer_node is None:
        return []
    return _flow_from_container(answer_node)


def _build_part(part_node):
    pc = part_node["children"]
    prompt_nodes = _child_dicts(pc, "prompt")
    solution_nodes = _child_dicts(pc, "solution")
    answer_nodes = _child_dicts(pc, "answer")
    return {
        "label": part_node["attrs"].get("label", ""),
        "prompt": _flow_from_container(prompt_nodes[0]) if prompt_nodes else [],
        "solution_blocks": _build_stageable_blocks(solution_nodes[0]) if solution_nodes else [],
        "answer": _build_answer(answer_nodes[0] if answer_nodes else None),
    }


def _build_item(node):
    attrs = node["attrs"]
    children = node["children"]

    prompt_nodes = _child_dicts(children, "prompt")
    figure_nodes = _child_dicts(children, "figure")
    part_nodes = _child_dicts(children, "part")
    solution_nodes = _child_dicts(children, "solution")
    answer_nodes = _child_dicts(children, "answer")

    figures = [{"src": f["attrs"].get("src", ""), "caption": _text_of(f)} for f in figure_nodes]
    parts = [_build_part(p) for p in part_nodes]

    # Known duplicate-solution artifact: when parts is non-empty, an
    # item-level trailing :::solution is either genuine shared data (keep)
    # or a re-narration duplicate (drop). Neither ex_13.4 nor q_13.5 (this
    # chapter's only two multi-part items) HAS an item-level :::solution at
    # all - confirmed at stage 7 - so this branch is a defensive no-op here,
    # not exercised by this chapter's actual content.
    if parts:
        solution_blocks = []
    else:
        solution_blocks = _build_stageable_blocks(solution_nodes[0]) if solution_nodes else []

    default_kind = "example" if node["name"] == "example" else "exercise"
    return {
        "id": attrs.get("id", ""),
        "kind": attrs.get("kind", default_kind),
        "number": attrs.get("number", ""),
        "topic": attrs.get("topic", ""),
        "prompt": _flow_from_container(prompt_nodes[0]) if prompt_nodes else [],
        "figures": figures,
        "parts": parts,
        "solution_blocks": solution_blocks,
        "answer": _build_answer(answer_nodes[0] if answer_nodes else None),
    }


def build():
    path = os.path.join(CH, "07_format", "structured.hi.md")
    text = io.open(path, encoding="utf-8").read()

    meta = {}
    body = text
    if text.startswith("---"):
        _, front, body = text.split("---", 2)
        for line in front.strip().splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                meta[k.strip()] = v.strip().strip('"')

    tree = _tag._parse(body.splitlines())
    items = []
    for child in tree["children"]:
        if isinstance(child, dict) and child["name"] in ("example", "question"):
            items.append(_build_item(child))

    return {
        "front": {"title": meta.get("title", ""), "chapter": meta.get("chapter", "")},
        "items": items,
    }


if __name__ == "__main__":
    data = build()
    out_path = os.path.join(CH, "08_tag", "structured.hi.json")
    with io.open(out_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print("wrote", out_path, len(data["items"]), "items")
