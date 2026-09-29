# -*- coding: utf-8 -*-
"""Stage 9 render script for economics-12-1 (Introductory Macroeconomics,
Chapter 1: Introduction) - the first Economics chapter this pipeline has
ever designed. Adapted from maths-12-5's own render_page_en.py/latex.py
(the most recent, most feature-complete prior chapter's own working
script) since none of its accumulated bug fixes are Economics-specific,
but heavily simplified for this chapter's own much simpler shape:

- 4 exercise items total, 0 examples - a single 'Exercises' section, no
  Examples heading, no per-exercise-number subsections (5.1/5.2/... the
  way a multi-exercise Maths chapter needs), no Miscellaneous section.
- No multi-part items, no case-split solutions, no notes/concepts - every
  item's own solution stayed a single flat block at stage 7 (see that
  stage's own manifest note: an essay-style definitional answer doesn't
  have a genuine given/key-formula/substitute/conclusion shape, so none
  was forced onto it). group_blocks()/render_solution_stack() are kept
  as general-purpose logic anyway (same proven code as every other
  chapter), just never exercise their step/note branches here.
- 1 genuine :::table (q_1.1's own micro-vs-macro comparison) and 1
  genuine mid-solution :::figure (q_1.4's own Great Depression flow
  chart) - both real exercises of render_solution_stack's own bare-block
  branches, same as maths-12-5's own first use of them.
- All 4 items are single-digit numbers (q_1.1-q_1.4) - no BADGE_VARIANT_38
  need ever triggers, but the check is kept for parity/future chapters.

latex.py is reused completely unmodified - this chapter's only real math
content is one inline '$15 \\%$' span, well within what it already
handles; none of its matrix/determinant/piecewise-function machinery is
exercised here, but keeping it does no harm."""
import json
import re
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))
from latex import convert_math_spans

CH = os.path.dirname(__file__) + r'\..'
with open(CH + r'\08_tag\structured.en.json', encoding='utf-8') as f:
    DATA = json.load(f)

ITEMS = DATA['items']

# ============================================================
# text helpers (identical to every other chapter's own proven logic)
# ============================================================

_SENT_SPLIT_RE = re.compile(r'(?<!\d)([।])|(?<![0-9])(\.)(?!\d)(?=\s|$)')


def text_to_lines(text):
    """Split flowing prose into one line per sentence: on existing newlines,
    and on sentence-ending punctuation (Devanagari । never appears in this
    English chapter, kept for parity; ASCII . only when not a decimal
    point) outside any $...$ span."""
    if text is None:
        return []
    spans = []

    def protect(m):
        spans.append(m.group(0))
        return f"\x00{len(spans) - 1}\x00"

    protected = re.sub(r'\$\$.+?\$\$|\$[^$]+\$', protect, text, flags=re.S)

    lines = []
    for raw_line in protected.split('\n'):
        raw_line = raw_line.strip()
        if not raw_line:
            continue
        parts = []
        buf = []
        i = 0
        n = len(raw_line)
        while i < n:
            c = raw_line[i]
            buf.append(c)
            if c == '।':
                parts.append(''.join(buf))
                buf = []
            elif c == '.':
                prev = raw_line[i - 1] if i > 0 else ''
                nxt = raw_line[i + 1] if i + 1 < n else ''
                if not (prev.isdigit() and nxt.isdigit()) and not prev.isdigit():
                    parts.append(''.join(buf))
                    buf = []
            i += 1
        if buf:
            parts.append(''.join(buf))
        lines.extend(p.strip() for p in parts if p.strip())

    def restore(s):
        return re.sub(r'\x00(\d+)\x00', lambda m: spans[int(m.group(1))], s)

    return [restore(l) for l in lines]


def render_prose_lines(text):
    lines = text_to_lines(text)
    return ''.join(f'<div class="s27">{convert_math_spans(l)}</div>' for l in lines)


_TABLE_LINE_RE = re.compile(r'^\s*\|.*\|\s*$')
_TABLE_SEP_RE = re.compile(r'^\s*\|?[\s:|-]+\|?\s*$')


def render_prompt(text):
    if not text:
        return ''
    lines = text.split('\n')
    n = len(lines)
    chunks = []
    i = 0
    while i < n:
        if (_TABLE_LINE_RE.match(lines[i]) and i + 1 < n
                and _TABLE_SEP_RE.match(lines[i + 1]) and '|' in lines[i + 1]):
            j = i
            while j < n and lines[j].strip() and _TABLE_LINE_RE.match(lines[j]):
                j += 1
            chunks.append(('table', lines[i:j]))
            i = j
        else:
            j = i
            prose = []
            while j < n and not (_TABLE_LINE_RE.match(lines[j]) and j + 1 < n
                                  and _TABLE_SEP_RE.match(lines[j + 1])):
                prose.append(lines[j])
                j += 1
            chunks.append(('prose', prose))
            i = j

    out = []
    for kind, chunk_lines in chunks:
        if kind == 'table':
            out.append(render_table_html('\n'.join(chunk_lines)))
        else:
            joined = ' '.join(l.strip() for l in chunk_lines if l.strip())
            if joined:
                out.append(f'<p class="s21">{convert_math_spans(joined)}</p>')
    return ''.join(out)


def flow_text(flow):
    return '\n'.join(seg['text'] for seg in flow if seg.get('type') == 'text')


def render_table_html(table_md):
    lines = [l for l in table_md.strip().split('\n') if l.strip()]
    if len(lines) < 2:
        return ''
    sep_re = re.compile(r'^\s*\|?[\s:|-]+\|?\s*$')
    data_lines = [lines[0]] + [l for l in lines[1:] if not sep_re.match(l)]
    rows_html = []
    for idx, line in enumerate(data_lines):
        cells = [c.strip() for c in line.strip().strip('|').split('|')]
        tag = 'th' if idx == 0 else 'td'
        cells_html = ''.join(f'<{tag} class="s100">{convert_math_spans(c)}</{tag}>' for c in cells)
        rows_html.append(f'<tr>{cells_html}</tr>')
    return f'<table class="s99">{"".join(rows_html)}</table>'


def render_flow_html(flow, text_renderer):
    out = []
    for seg in flow:
        if seg.get('type') == 'text':
            out.append(text_renderer(seg['text']))
        elif seg.get('type') == 'table':
            out.append(render_table_html(seg.get('html', '')))
    return ''.join(out)


# ============================================================
# stage pill classes (cycle by section color index 0..3: teal/orange/pink/purple)
# ============================================================
PILL = {
    'given': ['s24'] * 4,
    'key_formula': ['s28'] * 4,
    'substitute': ['s34'] * 4,
    'conclusion': ['s35'] * 4,
}
LABEL_EN = {'given': 'Given', 'key_formula': 'Key formula', 'substitute': 'Substitute', 'conclusion': 'Conclusion'}
BOX_BLOB = ['s37', 's44', 's50', 's56']
BOX_PLAIN = ['s86', 's87', 's88', 's89']
ARROW_COLOR = ['#10989e', '#f5820b', '#e42a63', '#7a3df0']

NOTE_PILL = {'recall': 's74', 'caution': 's75', 'tip': 's74'}

DOODLE_ARROW = '<svg width="44" height="86" viewBox="0 0 44 118" class="s25" aria-hidden="true"><path d="M36 6 C 12 26, 6 62, 15 102" fill="none" stroke="{c}" stroke-width="2.2" stroke-linecap="round"></path><path d="M9 92 L15 103 L22 94" fill="none" stroke="{c}" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"></path></svg>'
CHECK_DOODLE = '<svg width="30" height="28" viewBox="0 0 30 28" class="s38" aria-hidden="true"><path d="M3 22 L11 12 M13 26 L18 13 M22 22 L28 14" fill="none" stroke="{c}" stroke-width="2.4" stroke-linecap="round"></path></svg>'

ITEM_DOODLES = [
    '<svg width="30" height="30" viewBox="0 0 30 30" class="s20"><path d="M15 3 C15.5 10.5 19.5 14.5 27 15 C19.5 15.5 15.5 19.5 15 27 C14.5 19.5 10.5 15.5 3 15 C10.5 14.5 14.5 10.5 15 3 Z" fill="none" stroke="#10989e" stroke-width="1.8" stroke-linejoin="round"></path></svg>',
    '<svg width="30" height="30" viewBox="0 0 30 30" class="s20"><path d="M15 2 L18.5 11 L28 11.5 L20.5 17.5 L23 27 L15 21.5 L7 27 L9.5 17.5 L2 11.5 L11.5 11 Z" fill="none" stroke="#f5820b" stroke-width="1.8" stroke-linejoin="round"></path></svg>',
    '<svg width="36" height="28" viewBox="0 0 36 28" class="s20"><path d="M7 4 C 3 10, 3 18, 8 25 M18 2 C 15 10, 15 18, 18 26 M29 5 C 33 11, 33 18, 28 24" fill="none" stroke="#e42a63" stroke-width="2.1" stroke-linecap="round"></path></svg>',
    '<svg width="32" height="30" viewBox="0 0 32 30" class="s20"><circle cx="16" cy="15" r="10" fill="none" stroke="#7a3df0" stroke-width="1.8" stroke-dasharray="4 3"></circle><path d="M16 1 L16 4 M16 26 L16 29 M2 15 L5 15 M27 15 L30 15" stroke="#7a3df0" stroke-width="1.8" stroke-linecap="round"></path></svg>',
]

BADGE_VARIANT = [
    ('s15', 's16', 's17', 's19'),
    ('s40', 's41', 's42', 's43'),
    ('s46', 's47', 's48', 's49'),
    ('s52', 's53', 's54', 's55'),
]
BADGE_VARIANT_38 = [
    ('s15', 's16', 's68', 's19'),
    ('s40', 's41', 's65', 's43'),
    ('s46', 's47', 's66', 's49'),
    ('s52', 's53', 's67', 's55'),
]
DIVIDER_CLASS = {0: 's57', 1: 's39', 2: 's58', 3: 's51'}


def group_blocks(blocks):
    groups = []
    for b in blocks:
        if b['type'] == 'note':
            groups.append({'kind': 'note', 'note': b})
            continue
        if b['type'] == 'figure':
            groups.append({'kind': 'figure', 'figure': b})
            continue
        if b['type'] == 'table':
            groups.append({'kind': 'table', 'table': b})
            continue
        stage = b.get('stage')
        if stage is None:
            continue
        if groups and groups[-1].get('kind') == 'stage' and groups[-1]['stage'] == stage:
            groups[-1]['blocks'].append(b)
        else:
            groups.append({'kind': 'stage', 'stage': stage, 'blocks': [b]})
    return groups


def render_solution_stack(blocks, answer_text, color_idx):
    if not blocks:
        return ''
    groups = group_blocks(blocks)
    stage_group_indices = [i for i, g in enumerate(groups) if g.get('kind') == 'stage']
    conclusion_idx = None
    for i in stage_group_indices:
        if groups[i]['stage'] == 'conclusion':
            conclusion_idx = i
    echo_idx = conclusion_idx if conclusion_idx is not None else (
        stage_group_indices[-1] if stage_group_indices else None)

    parts = []
    for i, g in enumerate(groups):
        if g.get('kind') == 'note':
            note = g['note']
            note_type = note.get('note_type', '')
            pill_class = NOTE_PILL.get(note_type, 's74')
            label = note.get('label') or ''
            label_html = f'<div class="s23"><span class="{pill_class}">{label}</span></div>'
            body_html = render_flow_html(note.get('flow', []), render_prose_lines)
            content_html = f'<div class="s91"><div class="s26">{body_html}</div></div>'
            parts.append(f'<div class="s82">{label_html}{content_html}</div>')
            continue
        if g.get('kind') == 'figure':
            fig = g['figure']
            src = fig.get('src', '')
            cap = fig.get('caption', '')
            parts.append(
                f'<div class="s76"><figure class="s77"><img src="{src}" alt="" class="s78">'
                f'<figcaption class="s79">{cap}</figcaption></figure></div>'
            )
            continue
        if g.get('kind') == 'table':
            parts.append(f'<div class="s80">{render_table_html(g["table"].get("html", ""))}</div>')
            continue

        stage = g['stage']
        pill_class = PILL[stage][color_idx]
        label = LABEL_EN[stage]
        needs_doodle = stage in ('given', 'key_formula')
        doodle = DOODLE_ARROW.format(c=ARROW_COLOR[color_idx]) if needs_doodle else ''
        label_html = f'<div class="s23"><span class="{pill_class}">{label}</span>{doodle}</div>'

        body_html = ''.join(
            render_flow_html(b['flow'], render_prose_lines) for b in g['blocks']
        )
        content_inner = f'<div class="s26">{body_html}</div>'

        if i == echo_idx and answer_text:
            plain_len = len(re.sub(r'\$[^$]*\$|\\[a-zA-Z]+|[{}\\]', '', answer_text))
            box_class = (BOX_PLAIN if plain_len > 30 else BOX_BLOB)[color_idx]
            answer_html = convert_math_spans(answer_text)
            echo = (f'<div class="s36"><div class="s27"><span class="{box_class}">{answer_html}</span></div>'
                    f'{CHECK_DOODLE.format(c=ARROW_COLOR[color_idx])}</div>')
            content_inner += echo

        content_html = f'<div class="s91">{content_inner}</div>'
        parts.append(f'<div class="s82">{label_html}{content_html}</div>')

    return f'<div class="s81">{"".join(parts)}</div>'


def strip_redundant_enumeration(item_prompt, parts):
    if not parts or not item_prompt:
        return item_prompt
    stripped = item_prompt.strip()
    for p in parts:
        p_text = (p.get('prompt_text') or '').strip()
        p_text_nomark = re.sub(r'^\([a-zA-Z0-9]+\)\s*', '', p_text)
        if stripped == p_text or stripped == p_text_nomark:
            return None
    return item_prompt


def render_item(item, color_idx, badges):
    (badge_cls, q_cls, num_cls, topic_cls) = badges
    number_disp = item['number'].split('.')[-1]
    label_prefix = 'question'

    prompt_text = flow_text(item['prompt'])
    parts_list = item.get('parts') or []
    for p in parts_list:
        p['prompt_text'] = flow_text(p['prompt'])
    prompt_text_use = strip_redundant_enumeration(prompt_text, parts_list) if parts_list else prompt_text
    skip_item_prompt = parts_list and prompt_text_use is None

    body = []
    if not skip_item_prompt and item['prompt']:
        for seg in item['prompt']:
            if seg.get('type') == 'text':
                body.append(render_prompt(seg["text"]))
            elif seg.get('type') == 'table':
                body.append(render_table_html(seg.get('html', '')))

    for fig in item.get('figures') or []:
        src = fig.get('src', '')
        cap = fig.get('caption', '')
        body.append(
            f'<div class="s76"><figure class="s77"><img src="{src}" alt="" class="s78">'
            f'<figcaption class="s79">{cap}</figcaption></figure></div>'
        )

    if parts_list:
        for p in parts_list:
            label = p['label']
            label_disp = label if label.startswith('(') else f'({label})'
            body.append(f'<p class="s59">Part {label_disp}</p>')
            if p['prompt_text']:
                body.append(render_prompt(p["prompt_text"]))
            ans_text = flow_text(p.get('answer') or [])
            body.append(render_solution_stack(p.get('solution_blocks') or [], ans_text, color_idx))
    else:
        ans_text = flow_text(item.get('answer') or [])
        body.append(render_solution_stack(item.get('solution_blocks') or [], ans_text, color_idx))

    doodle = ITEM_DOODLES[color_idx]
    html = (
        f'<div data-screen-label="{label_prefix} {item["number"]}" class="s13">\n'
        f'      <div class="s14">\n'
        f'        <div class="{badge_cls}">\n'
        f'          <div class="{q_cls}">Q</div>\n'
        f'          <div class="{num_cls}">{number_disp}<span class="s18"></span></div>\n'
        f'          <div class="{topic_cls}">{item.get("topic", "")}</div>\n'
        f'        </div>\n'
        f'        {doodle}\n'
        f'      </div>\n'
        f'      <div>\n'
        f'{"".join(body)}\n'
        f'      </div>\n'
        f'    </div>\n'
    )
    return html


def build_page():
    out = []
    color_idx = 0
    # This chapter has exactly one section - all 4 items are plain
    # Exercises, no Examples (0 exist), no per-exercise-number
    # subsections, no Miscellaneous Exercise.
    sections = [
        ('Exercises', [it for it in ITEMS if it['kind'] == 'exercise']),
    ]

    total_section_items = sum(len(items) for _, items in sections)
    assert total_section_items == len(ITEMS), (
        f'section list drops items: {total_section_items} != {len(ITEMS)}'
    )

    out.append('<div class="s2">\n  <div class="s3">Introduction</div>\n  <div class="s4">Chapter 1 · All Questions and Complete Solutions</div>\n  <div class="s5"><span class="s6"></span><span class="s7"></span><span class="s8"></span><span class="s9"></span></div>\n</div>\n')

    for sec_num, (label, section_items) in enumerate(sections, start=1):
        if not section_items:
            continue
        if sec_num == 1:
            out.append(f'<div class="s10"><div class="s11"></div><div class="s12">{label}</div><div class="s11"></div></div>\n')
        else:
            out.append(f'<div class="s69"><div class="s70"></div><div class="s71">{label}</div><div class="s70"></div></div>\n')

        for i, item in enumerate(section_items):
            num_disp = item['number'].split('.')[-1]
            badge_set = BADGE_VARIANT_38[color_idx] if len(num_disp) >= 2 else BADGE_VARIANT[color_idx]
            out.append(render_item(item, color_idx, badge_set))
            if i != len(section_items) - 1:
                out.append(f'<div class="{DIVIDER_CLASS[(color_idx + 1) % 4]}"></div>\n')
            color_idx = (color_idx + 1) % 4

    return ''.join(out)


PAGE = build_page()

HTML = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Introduction · Chapter 1 &mdash; Questions and Solutions</title>
<link rel="stylesheet" href="final.en.css">
</head>
<body>
<main class="sheet">
  <div class="s1">
{PAGE}  </div>
</main>
</body>
</html>
'''

out_path = os.path.join(os.path.dirname(__file__), 'final.en.html')
with open(out_path, 'w', encoding='utf-8') as f:
    f.write(HTML)
print('wrote', out_path, len(HTML), 'chars')
