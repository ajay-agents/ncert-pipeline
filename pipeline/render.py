"""Chapter JSON -> markdown with container markup. Pure function, no model call."""
from __future__ import annotations

from .schema import Chapter, Item, Lang

LABELS = {
    "en": {"example": "Example", "exercise": "Question",
           "additional_exercise": "Additional Question",
           "solution": "Solution", "answer": "Answer"},
    "hi": {"example": "\u0909\u0926\u093e\u0939\u0930\u0923", "exercise": "\u092a\u094d\u0930\u0936\u094d\u0928",
           "additional_exercise": "\u0905\u0924\u093f\u0930\u093f\u0915\u094d\u0924 \u092a\u094d\u0930\u0936\u094d\u0928",
           "solution": "\u0939\u0932", "answer": "\u0909\u0924\u094d\u0924\u0930"},
}

# Section headings. Hindi has no plural suffix, so never build one by adding "s".
SECTIONS = {
    "en": {"example": "Examples", "exercise": "Questions and Solutions",
           "additional_exercise": "Additional Questions"},
    "hi": {"example": "\u0909\u0926\u093e\u0939\u0930\u0923",
           "exercise": "\u092a\u094d\u0930\u0936\u094d\u0928 \u0914\u0930 \u0939\u0932",
           "additional_exercise": "\u0905\u0924\u093f\u0930\u093f\u0915\u094d\u0924 \u092a\u094d\u0930\u0936\u094d\u0928"},
}


def _attrs(**kw) -> str:
    # A stray literal `"` in model-written text (e.g. topic) would break the
    # single-line {k="v"} attribute syntax tag.py parses — never emit one.
    clean = lambda v: str(v).replace('"', "'").replace("\n", " ")
    pairs = " ".join(f'{k}="{clean(v)}"' for k, v in kw.items() if v not in (None, "", []))
    return "{" + pairs + "}" if pairs else ""


def render_item(item: Item, lang: Lang) -> str:
    L = LABELS[lang]
    out: list[str] = []
    container = "example" if item.kind == "example" else "question"
    out.append(f":::{container}{_attrs(number=item.number, kind=item.kind, id=item.id, topic=item.topic.get(lang), verified=item.verified or None, simplified=item.simplified or None, corrections_applied=item.corrections_applied or None)}")
    out.append(f"#### {L[item.kind]} {item.number}\n")

    q = item.question.get(lang).strip()
    if q:
        out.append(":::prompt")
        out.append(q)
        out.append(":::\n")

    for fig in item.figures:
        out.append(f":::figure{_attrs(src=fig.src, id=fig.id)}")
        cap = fig.caption.get(lang).strip()
        if cap:
            out.append(cap)
        out.append(":::\n")

    if item.parts:
        for p in item.parts:
            out.append(f":::part{_attrs(label=p.label)}")
            pq = p.question.get(lang).strip()
            if pq:
                out.append(f":::prompt\n{pq}\n:::\n")
            ps = p.solution.get(lang).strip()
            if ps:
                out.append(f":::solution\n{ps}\n:::\n")
            pa = p.final_answer.get(lang).strip()
            if pa:
                out.append(f":::answer\n**{L['answer']}:** {pa}\n:::\n")
            out.append(":::\n")

    sol = item.solution.get(lang).strip()
    if sol:
        out.append(f":::solution{_attrs(label=L['solution'])}")
        out.append(sol)
        out.append(":::\n")

    ans = item.final_answer.get(lang).strip()
    if ans:
        out.append(":::answer")
        out.append(f"**{L['answer']}:** {ans}")
        out.append(":::\n")

    out.append(":::\n")
    return "\n".join(out)


def render(chapter: Chapter, lang: Lang, kinds: tuple[str, ...] | None = None) -> str:
    kinds = kinds or ("example", "exercise", "additional_exercise")
    title = chapter.title.get(lang) or f"Chapter {chapter.chapter_number}"
    head = [
        "---",
        f"subject: {chapter.subject}",
        f"class: {chapter.class_level}",
        f"chapter: {chapter.chapter_number}",
        f"lang: {lang}",
        f'title: "{title}"',
        "---",
        "",
        f"# {title}",
        "",
    ]
    body: list[str] = []
    for kind in kinds:
        items = chapter.by_kind(kind)
        if not items:
            continue
        body.append(f"## {SECTIONS[lang][kind]}\n")
        body.extend(render_item(i, lang) for i in items)
    return "\n".join(head + body).rstrip() + "\n"
