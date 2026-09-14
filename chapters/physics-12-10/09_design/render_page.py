# -*- coding: utf-8 -*-
"""Stage 9 render script for physics-12-10 (Wave Optics / तरंग-प्रकाशिकी):
reads 08_tag/structured.hi.json, hand-templates it onto the house style
(solutions-chapter-1.html's exemplar), concretely modeled on
chapters/physics-12-9/09_design/render_page.py (the most recently proven and
complete of this pipeline's stage-9 scripts), and writes
09_design/final.hi.html + final.hi.css + images/.

This chapter has no :::note or :::table content (all 8 items are either
purely qualitative reasoning or a numeric given/formula/step derivation), so
the note/table branches below are inherited unused, kept only so this script
stays a faithful copy of the proven reference rather than a stripped-down
one that might silently diverge in behavior it does share.
"""
import sys, os, json, re, io

sys.path.insert(0, os.path.dirname(__file__))
import latex

ROOT = r"C:\Users\ajayr\Downloads\ncert-pipeline"
CH = os.path.join(ROOT, "chapters", "physics-12-10")

with io.open(os.path.join(CH, "08_tag", "structured.hi.json"), encoding="utf-8") as f:
    DATA = json.load(f)

TITLE = DATA["front"]["title"]
CHAPTER_NUM = DATA["front"]["chapter"]

# ============================================================
# Color-cycle tables (teal, orange, pink, purple - matches
# chapters/physics-12-6/09_design/final.hi.html exactly)
# ============================================================
COLORS = [
    {  # 0: teal
        "badge": "s15", "qtag": "s16", "num44": "s17", "num38": "s68", "topic": "s19",
        "divider_before": "s57", "answer_blob": "s37", "answer_plain": "s86",
    },
    {  # 1: orange
        "badge": "s40", "qtag": "s41", "num44": "s42", "num38": "s65", "topic": "s43",
        "divider_before": "s39", "answer_blob": "s44", "answer_plain": "s87",
    },
    {  # 2: pink
        "badge": "s46", "qtag": "s47", "num44": "s48", "num38": "s66", "topic": "s49",
        "divider_before": "s58", "answer_blob": "s50", "answer_plain": "s88",
    },
    {  # 3: purple
        "badge": "s52", "qtag": "s53", "num44": "s54", "num38": "s67", "topic": "s55",
        "divider_before": "s51", "answer_blob": "s56", "answer_plain": "s89",
    },
]

DOODLE_SVGS = [
    '<svg width="30" height="30" viewBox="0 0 30 30" class="s20"><path d="M15 3 C15.5 10.5 19.5 14.5 27 15 C19.5 15.5 15.5 19.5 15 27 C14.5 19.5 10.5 15.5 3 15 C10.5 14.5 14.5 10.5 15 3 Z" fill="none" stroke="#10989e" stroke-width="1.8" stroke-linejoin="round"></path></svg>',
    '<svg width="30" height="30" viewBox="0 0 30 30" class="s20"><path d="M15 2 L18.5 11 L28 11.5 L20.5 17.5 L23 27 L15 21.5 L7 27 L9.5 17.5 L2 11.5 L11.5 11 Z" fill="none" stroke="#f5820b" stroke-width="1.8" stroke-linejoin="round"></path></svg>',
    '<svg width="36" height="28" viewBox="0 0 36 28" class="s20"><path d="M7 4 C 3 10, 3 18, 8 25 M18 2 C 15 10, 15 18, 18 26 M29 5 C 33 11, 33 18, 28 24" fill="none" stroke="#e42a63" stroke-width="2.1" stroke-linecap="round"></path></svg>',
    '<svg width="32" height="30" viewBox="0 0 32 30" class="s20"><circle cx="16" cy="15" r="10" fill="none" stroke="#7a3df0" stroke-width="1.8" stroke-dasharray="4 3"></circle><path d="M16 1 L16 4 M16 26 L16 29 M2 15 L5 15 M27 15 L30 15" stroke="#7a3df0" stroke-width="1.8" stroke-linecap="round"></path></svg>',
]

GIVEN_ARROW_SVG = ('<svg width="44" height="86" viewBox="0 0 44 118" class="s25" aria-hidden="true">'
                    '<path d="M36 6 C 12 26, 6 62, 15 102" fill="none" stroke="#10989e" stroke-width="2.2" stroke-linecap="round"></path>'
                    '<path d="M9 92 L15 103 L22 94" fill="none" stroke="#10989e" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"></path></svg>')
FORMULA_ARROW_SVG = ('<svg width="38" height="34" viewBox="0 0 38 34" class="s29" aria-hidden="true">'
                      '<path d="M9 3 C 3 10, 3 20, 11 24 C 19 28, 26 22, 21 16 C 17 12, 10 16, 15 22 C 18 26, 25 28, 31 27" fill="none" stroke="#1d3f6e" stroke-width="2.2" stroke-linecap="round"></path>'
                      '<path d="M25 32 L33 27 L27 21" fill="none" stroke="#1d3f6e" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"></path></svg>')

PILL_CLASS = {"given": "s24", "key_formula": "s28", "substitute": "s34", "conclusion": "s35"}
NOTE_CLASS = {"tip": "s74", "recall": "s74", "caution": "s75"}
NOTE_DEFAULT_LABEL = {"caution": "सावधानी", "recall": "याद रखें", "tip": "सुझाव"}


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


# ============================================================
# Inline text (with $...$ math) -> HTML, single flowing string (used for
# prompts and answers - never split into per-sentence divs).
# ============================================================
_MATH_RE = re.compile(r"\$\$(.+?)\$\$|\$(.+?)\$", re.S)


def render_inline(text):
    if text is None:
        return ""
    out = []
    pos = 0
    for m in _MATH_RE.finditer(text):
        out.append(esc(text[pos:m.start()]))
        src = m.group(1) if m.group(1) is not None else m.group(2)
        html = latex.convert(src)
        html = latex.glue_equals_to_frac(html)
        out.append(html)
        pos = m.end()
    out.append(esc(text[pos:]))
    return "".join(out).replace("~", "\u00a0")


# ============================================================
# Flow text -> list of rendered "line" HTML strings, one per <div class="s27">.
# A $$...$$ display block is protected FIRST and always becomes its own
# atomic line; surrounding prose is inline-math-converted then split one
# sentence per line.
# ============================================================
_DISPLAY_RE = re.compile(r"\$\$(.+?)\$\$", re.S)


def render_flow_lines(text):
    if not text or not text.strip():
        return []
    lines = []
    pos = 0
    prose_buf = []

    def flush_prose():
        if not prose_buf:
            return
        chunk = "".join(prose_buf)
        prose_buf.clear()
        for sentence in latex.text_to_lines(chunk):
            html = render_inline(sentence)
            if html.strip():
                lines.append(html)

    for m in _DISPLAY_RE.finditer(text):
        prose_buf.append(text[pos:m.start()])
        flush_prose()
        inner = m.group(1)
        env_html = latex.convert(inner)
        env_html = latex.glue_equals_to_frac(env_html)
        if '<div class="s92' in env_html:
            lines.append(env_html)
        else:
            lines.append(f'<div class="s60">{env_html}</div>')
        pos = m.end()
    prose_buf.append(text[pos:])
    flush_prose()
    return lines


def render_block_flow(flow):
    """A block's flow list -> list of <div class="s27">...</div> strings
    for its .s26 wrapper. A nested figure segment becomes its own figure
    row (never dropped by a text-only join, per step_9/PROMPT.md's
    documented figure-in-flow trap); a nested table segment becomes its
    own table block."""
    parts = []
    for seg in flow:
        if seg["type"] == "text":
            for line in render_flow_lines(seg["text"]):
                parts.append(f'<div class="s27">{line}</div>')
        elif seg["type"] == "figure":
            parts.append(render_figure_row([seg]))
        elif seg["type"] == "table":
            parts.append(render_table_html(seg["html"]))
    return parts


def render_figure_row(figures):
    figs = []
    for fig in figures:
        cap = esc(fig.get("caption") or "")
        figs.append(f'<figure class="s77"><img src="{fig["src"]}" alt="" class="s78">'
                     f'<figcaption class="s79">{cap}</figcaption></figure>')
    return f'<div class="s76">{"".join(figs)}</div>'


def render_table_html(md_text):
    """A markdown pipe table (already wrapped, un-reformatted, by :::table
    at stage 7/serialized as-is at stage 8) -> a real HTML table. Reuses
    the base stylesheet's own .s61/.s62/.s63/.s64. Not exercised by this
    chapter's own content (no :::table anywhere) but kept for parity with
    the reference script."""
    header, rows = latex.parse_markdown_table(md_text)
    if not header:
        return ""
    thead = "<tr class=\"s62\">" + "".join(
        f'<th class="s63">{render_inline(c)}</th>' for c in header) + "</tr>"
    tbody = "".join(
        "<tr>" + "".join(f'<td class="s64">{render_inline(c)}</td>' for c in row) + "</tr>"
        for row in rows)
    return f'<div class="s60"><table class="s61"><thead>{thead}</thead><tbody>{tbody}</tbody></table></div>'


def answer_box_class(color, plain_text_len, threshold=30):
    return color["answer_plain"] if plain_text_len > threshold else color["answer_blob"]


def plain_len(html_or_text):
    return len(re.sub(r"<[^>]+>", "", html_or_text))


# ============================================================
# Solution blocks -> .s81 stack of .s82 label+content rows
# ============================================================

def render_solution_blocks(blocks, color, final_answer_flow):
    if not blocks:
        return ""
    rows = []
    for b in blocks:
        btype = b["type"]
        if btype in ("concept", "formula", "step"):
            stage = b.get("stage")
            pill_class = PILL_CLASS.get(stage, "s34")
            label_text = b.get("label") or {"given": "जानकारी", "key_formula": "मुख्य सूत्र",
                                             "substitute": "मान रखो", "conclusion": "निष्कर्ष"}.get(stage, "")
            doodle = ""
            if stage == "given":
                doodle = GIVEN_ARROW_SVG
            elif stage == "key_formula":
                doodle = FORMULA_ARROW_SVG
            content_lines = render_block_flow(b["flow"])
            content_html = "".join(content_lines)
            row = (f'<div class="s82"><div class="s23"><span class="{pill_class}">{esc(label_text)}</span>{doodle}</div>'
                   f'<div class="s91"><div class="s26">{content_html}</div>')
            rows.append(("row_open", row, stage))
        elif btype == "note":
            note_type = b.get("note_type", "tip")
            note_class = NOTE_CLASS.get(note_type, "s74")
            label_text = b.get("label") or NOTE_DEFAULT_LABEL.get(note_type, "सुझाव")
            content_lines = render_block_flow(b["flow"])
            content_html = "".join(content_lines)
            row = (f'<div class="s82"><div class="s23"><span class="{note_class}">{esc(label_text)}</span></div>'
                   f'<div class="s91"><div class="s26">{content_html}</div></div></div>')
            rows.append(("row_full", row, None))
        elif btype == "figure":
            fig_row = render_figure_row([b])
            rows.append(("row_bare", fig_row, None))
        elif btype == "table":
            rows.append(("row_bare", render_table_html(b.get("html", "")), None))

    # close concept/formula/step rows (they were left open to allow an
    # answer box to be appended into the LAST such row's .s91 content)
    stageable_indices = [i for i, r in enumerate(rows) if r[0] == "row_open"]
    last_stageable = stageable_indices[-1] if stageable_indices else None

    out = []
    for i, (kind, html, stage) in enumerate(rows):
        if kind == "row_open":
            if i == last_stageable and final_answer_flow:
                ans_text_plain = plain_len(final_answer_flow)
                cls = answer_box_class(color, ans_text_plain)
                out.append(html + f'<div class="s36"><div class="s27"><span class="{cls}">{final_answer_flow}</span></div></div></div></div>')
            else:
                out.append(html + "</div></div>")
        else:
            out.append(html)

    if final_answer_flow and last_stageable is None:
        ans_text_plain = plain_len(final_answer_flow)
        cls = answer_box_class(color, ans_text_plain)
        out.append(f'<div class="s82"><div class="s23"></div><div class="s91"><div class="s36"><div class="s27"><span class="{cls}">{final_answer_flow}</span></div></div></div></div>')

    return f'<div class="s81">{"".join(out)}</div>'


_ANSWER_LABEL_RE = re.compile(r"^\s*\*\*[^*]*:\*\*\s*")
_BOLD_RE = re.compile(r"\*\*([^*]+)\*\*")


def answer_has_table(answer_list):
    return any(seg["type"] == "table" for seg in (answer_list or []))


def render_answer_flow(answer_list):
    """Text-only join (strips any leftover leading '**उत्तर:**' markdown
    prefix, in case one survived - stage 8 already strips it, so this is a
    defensive no-op for this chapter's own data). Never called on an answer
    list that also contains a table segment."""
    if not answer_list:
        return ""
    texts = []
    for seg in answer_list:
        if seg["type"] == "text":
            raw = _ANSWER_LABEL_RE.sub("", seg["text"], count=1)
            html = render_inline(raw)
            html = _BOLD_RE.sub(r"<b>\1</b>", html)
            if html.strip():
                texts.append(html)
    return " ".join(texts)


def render_answer_table_block(answer_list):
    """An answer whose result IS a table doesn't fit the small pill-shaped
    boxed-answer echo - render it as its own labelled block below the
    solution instead. Not exercised by this chapter (no table answers)."""
    parts = [f'<div class="s59">उत्तर:</div>']
    for seg in answer_list:
        if seg["type"] == "table":
            parts.append(render_table_html(seg["html"]))
    return "".join(parts)


# ============================================================
# One item
# ============================================================

def render_item(item, color_idx):
    color = COLORS[color_idx]
    num = item["number"]
    decimal_part = num.split(".")[-1] if "." in num else ""
    num_class = color["num38"] if len(decimal_part) >= 2 else color["num44"]

    kind_label = "उदाहरण" if item["kind"] == "example" else "प्रश्न"
    badge_html = (f'<div class="{color["badge"]}"><div class="{color["qtag"]}">Q</div>'
                  f'<div class="{num_class}">{esc(num)}<span class="s18"></span></div>'
                  f'<div class="{color["topic"]}">{esc(item["topic"] or "")}</div></div>')
    doodle_html = DOODLE_SVGS[color_idx]

    body = []
    prompt_text = render_answer_flow(item["prompt"])
    if prompt_text:
        body.append(f'<p class="s21">{prompt_text}</p>')

    if item["figures"]:
        body.append(render_figure_row(item["figures"]))

    if item["parts"]:
        for p in item["parts"]:
            body.append(f'<div class="{color["topic"]}" style="margin-top:22px">भाग ({p["label"]})</div>')
            p_prompt = render_answer_flow(p["prompt"])
            if p_prompt:
                body.append(f'<p class="s21">{p_prompt}</p>')
            p_answer = render_answer_flow(p["answer"])
            body.append(render_solution_blocks(p["solution_blocks"], color, p_answer))
    else:
        if answer_has_table(item["answer"]):
            body.append(render_solution_blocks(item["solution_blocks"], color, None))
            body.append(render_answer_table_block(item["answer"]))
        else:
            item_answer = render_answer_flow(item["answer"])
            body.append(render_solution_blocks(item["solution_blocks"], color, item_answer))

    # item-level combined answer alongside parts (this chapter's items all
    # have empty item-level "answer" whenever they have parts - kept for
    # parity with the reference script / a future rerun).
    if item["parts"] and item["answer"] and not answer_has_table(item["answer"]):
        combined = render_answer_flow(item["answer"])
        if combined:
            body.append(f'<div class="s81"><div class="s82"><div class="s23"></div><div class="s91">'
                         f'<div class="s36"><div class="s27"><span class="{color["answer_blob"] if plain_len(combined) <= 30 else color["answer_plain"]}">{combined}</span></div></div>'
                         f'</div></div></div>')

    html = (f'<div data-screen-label="{kind_label} {num}" class="s13">\n'
            f'  <div class="s14">\n{badge_html}\n{doodle_html}\n  </div>\n'
            f'  <div>\n{"".join(body)}\n  </div>\n</div>\n')
    return html


def build():
    items = DATA["items"]
    examples = [it for it in items if it["kind"] == "example"]
    exercises = [it for it in items if it["kind"] != "example"]

    out = []
    out.append('<div class="s2">\n')
    out.append(f'  <div class="s3">{esc(TITLE)}</div>\n')
    out.append(f'  <div class="s4">अध्याय {esc(CHAPTER_NUM)} · सभी प्रश्न एवं पूर्ण हल</div>\n')
    out.append('  <div class="s5"><span class="s6"></span><span class="s7"></span><span class="s8"></span><span class="s9"></span></div>\n')
    out.append('</div>\n')
    out.append('<div class="s10"><div class="s11"></div><div class="s12">भाग 1 · उदाहरण</div><div class="s11"></div></div>\n')

    color_idx = 0
    for it in examples:
        out.append(render_item(it, color_idx))
        color_idx = (color_idx + 1) % 4
        out.append(f'<div class="{COLORS[color_idx]["divider_before"]}"></div>\n')
    if out and out[-1].startswith('<div class="s'):
        out.pop()

    out.append('<div class="s69"><div class="s70"></div><div class="s71">भाग 2 · अभ्यास प्रश्न</div><div class="s70"></div></div>\n')

    for idx, it in enumerate(exercises):
        out.append(render_item(it, color_idx))
        color_idx = (color_idx + 1) % 4
        if idx != len(exercises) - 1:
            out.append(f'<div class="{COLORS[color_idx]["divider_before"]}"></div>\n')

    body_html = "".join(out)

    page = f"""<!DOCTYPE html>
<html lang="hi">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(TITLE)} &middot; अध्याय {esc(CHAPTER_NUM)} &mdash; प्रश्न एवं हल</title>
<link rel="stylesheet" href="final.hi.css">
</head>
<body>
<main class="sheet">
  <div class="s1">
{body_html}
  </div>
</main>
</body>
</html>
"""
    return page


if __name__ == "__main__":
    page = build()
    out_path = os.path.join(CH, "09_design", "final.hi.html")
    with io.open(out_path, "w", encoding="utf-8") as f:
        f.write(page)
    print("wrote", out_path, len(page), "chars")
