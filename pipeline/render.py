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

    visible_parts = [p for p in item.parts if _part_has_content(p, lang)]
    if visible_parts:
        for p in visible_parts:
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


def _part_has_content(part, lang: Lang) -> bool:
    """A Part is real for `lang` only if it has some actual question/
    solution/answer text in that language - not merely a shared label.
    Needed for a genuine edition difference one level down from
    `_has_content()` below: one language's own official textbook can add an
    extra Part to an otherwise-shared item (political-science-12-4's Q6:
    the Hindi edition's own fill-in-the-blanks has a 5th blank, "two
    voluntary organisations active in protecting human rights", that
    English's own Q6 never had at all) - without this check, render() would
    still emit that Part's own empty container (a bare `:::part{label="e"}`
    shell, no content at all) on the language that doesn't have it, rather
    than omitting the Part entirely as it should."""
    return bool(part.question.get(lang) or part.solution.get(lang) or part.final_answer.get(lang))


def _has_content(item: Item, lang: Lang) -> bool:
    """An item is real for `lang` only if it (or one of its own Parts) has
    some actual question/solution/answer text in that language - not merely
    a shared id. Needed for a genuine edition difference where one
    language's own official textbook has an exercise the other language's
    edition simply never printed (political-science-12-3: the Hindi
    edition's own Exercises section has 11 numbered questions where
    English's has 10, with different content for several) - without this
    check, render() would still emit that item's own empty container
    (a bare heading, no content at all) on the language that doesn't have
    it, rather than omitting the item entirely as it should."""
    if item.question.get(lang) or item.solution.get(lang) or item.final_answer.get(lang):
        return True
    return any(_part_has_content(p, lang) for p in item.parts)


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
        items = [i for i in chapter.by_kind(kind) if _has_content(i, lang)]
        if not items:
            continue
        body.append(f"## {SECTIONS[lang][kind]}\n")
        body.extend(render_item(i, lang) for i in items)
    return "\n".join(head + body).rstrip() + "\n"
