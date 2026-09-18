# -*- coding: utf-8 -*-
"""Stage 9 render script for maths-12-3 (Matrices), adapted from
maths-12-2's own working render_page.py/latex.py (the most recent, most
similar prior chapter), plus every trap documented in step_9/PROMPT.md.
Section list rewritten for this chapter's three exercises (प्रश्नावली
3.1/3.2/3.3) instead of maths-12-2's two; table-flow rendering added for
q_3.9.7's two nested tables (the only tables in this chapter); matrix
rendering lives in latex.py (see its own module docstring)."""
import json
import re
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))
from latex import convert_math_spans

CH = os.path.dirname(__file__) + r'\..'
with open(CH + r'\08_tag\structured.hi.json', encoding='utf-8') as f:
    DATA = json.load(f)

ITEMS = DATA['items']

# ============================================================
# text helpers
# ============================================================

_SENT_SPLIT_RE = re.compile(r'(?<!\d)([।])|(?<![0-9])(\.)(?!\d)(?=\s|$)')


def text_to_lines(text):
    """Split flowing prose into one line per sentence: on existing newlines,
    and on sentence-ending punctuation (Devanagari । always; ASCII . only
    when not a decimal point) outside any $...$ span."""
    if text is None:
        return []
    # protect math spans so we never split inside one
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
        # split on । or a non-decimal .
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

    # restore protected spans
    def restore(s):
        return re.sub(r'\x00(\d+)\x00', lambda m: spans[int(m.group(1))], s)

    return [restore(l) for l in lines]


def render_prose_lines(text):
    lines = text_to_lines(text)
    return ''.join(f'<div class="s27">{convert_math_spans(l)}</div>' for l in lines)


_TABLE_LINE_RE = re.compile(r'^\s*\|.*\|\s*$')
_TABLE_SEP_RE = re.compile(r'^\s*\|?[\s:|-]+\|?\s*$')


def render_prompt(text):
    """Render an item/part prompt as one or more <p class="s21"> paragraphs
    - but first split out any embedded markdown pipe-table. Exam question
    text is immutable (Rule 4), so stage 7 was never allowed to wrap a
    table living inside a :::prompt in :::table the way it could for a
    solution's own content; it survives as bare pipe-syntax lines, and a
    naive single-paragraph join-then-convert prints them as literal
    "| | ... |" text instead of a table. Caught for real: ex_3.1's own
    factory worker-count table, sitting directly in its question text.
    Returns the full wrapped HTML (callers must NOT wrap this in another
    <p> - a <table> can't legally nest inside one)."""
    if not text:
        return ''
    lines = text.split('\n')
    n = len(lines)
    chunks = []  # ('prose'|'table', [lines])
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
    """Render a flow's raw markdown pipe-table as a real HTML <table> -
    this chapter's only such content is q_3.9.7's price/production tables
    (one in the item-level prompt, one per part's own concept block); a
    flow-reader that only ever joins type:"text" segments (flow_text()
    above) silently drops these, the same documented blind spot as a
    dropped mid-solution figure."""
    lines = [l for l in table_md.strip().split('\n') if l.strip()]
    if len(lines) < 2:
        return ''
    sep_re = re.compile(r'^\s*\|?[\s:|-]+\|?\s*$')
    data_lines = [lines[0]] + [l for l in lines[1:] if not sep_re.match(l)]
    rows_html = []
    for line in data_lines:
        cells = [c.strip() for c in line.strip().strip('|').split('|')]
        cells_html = ''.join(f'<td class="s100">{convert_math_spans(c)}</td>' for c in cells)
        rows_html.append(f'<tr>{cells_html}</tr>')
    return f'<table class="s99">{"".join(rows_html)}</table>'


def render_flow_html(flow, text_renderer):
    """Render an ordered text/table flow, preserving order - text segments
    via the given renderer (render_prompt for a prompt, render_prose_lines
    for a solution block's own body), a table segment as a real table
    instead of being silently dropped."""
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
LABEL_HI = {'given': 'जानकारी', 'key_formula': 'मुख्य सूत्र', 'substitute': 'मान रखो', 'conclusion': 'निष्कर्ष'}
BOX_BLOB = ['s37', 's44', 's50', 's56']
BOX_PLAIN = ['s86', 's87', 's88', 's89']
ARROW_COLOR = ['#10989e', '#f5820b', '#e42a63', '#7a3df0']

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
    """Group consecutive blocks of the same stage, preserving order; a
    block with no stage (shouldn't occur in this chapter - no notes) is
    skipped defensively."""
    groups = []
    for b in blocks:
        stage = b.get('stage')
        if stage is None:
            continue
        if groups and groups[-1]['stage'] == stage:
            groups[-1]['blocks'].append(b)
        else:
            groups.append({'stage': stage, 'blocks': [b]})
    return groups


def render_solution_stack(blocks, answer_text, color_idx):
    if not blocks:
        return ''
    groups = group_blocks(blocks)
    conclusion_idx = None
    for i, g in enumerate(groups):
        if g['stage'] == 'conclusion':
            conclusion_idx = i
    echo_idx = conclusion_idx if conclusion_idx is not None else (len(groups) - 1 if groups else None)

    parts = []
    for i, g in enumerate(groups):
        stage = g['stage']
        pill_class = PILL[stage][color_idx]
        label = LABEL_HI[stage]
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
    """Skip the item-level prompt when it's pure repetition of the parts'
    own prompts (exact duplicate, or a telescoped multi-clause enumeration
    where every labelled clause is a substring of that part's own prompt)."""
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
    label_prefix = 'उदाहरण' if item['kind'] == 'example' else ('अतिरिक्त प्रश्न' if item['kind'] == 'additional_exercise' else 'प्रश्न')

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

    if parts_list:
        for p in parts_list:
            label = p['label']
            label_disp = label if label.startswith('(') else f'({label})'
            body.append(f'<p class="s59">भाग {label_disp}</p>')
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
    sections = [
        ('उदाहरण', [it for it in ITEMS if it['kind'] == 'example']),
        ('प्रश्नावली 3.1', [it for it in ITEMS if it['id'].startswith('q_3.1.')]),
        ('प्रश्नावली 3.2', [it for it in ITEMS if it['id'].startswith('q_3.2.')]),
        ('प्रश्नावली 3.3', [it for it in ITEMS if it['id'].startswith('q_3.3.')]),
        ('विविध प्रश्नावली', [it for it in ITEMS if it['kind'] == 'additional_exercise']),
    ]

    out.append('<div class="s2">\n  <div class="s3">आव्यूह</div>\n  <div class="s4">अध्याय 3 · सभी प्रश्न एवं पूर्ण हल</div>\n  <div class="s5"><span class="s6"></span><span class="s7"></span><span class="s8"></span><span class="s9"></span></div>\n</div>\n')

    for sec_num, (label, section_items) in enumerate(sections, start=1):
        if sec_num == 1:
            out.append(f'<div class="s10"><div class="s11"></div><div class="s12">भाग {sec_num} · {label}</div><div class="s11"></div></div>\n')
        else:
            out.append(f'<div class="s69"><div class="s70"></div><div class="s71">भाग {sec_num} · {label}</div><div class="s70"></div></div>\n')

        for i, item in enumerate(section_items):
            # use the 38px badge variant when the in-section number has 2+
            # digits (matches the exemplar's own convention for longer numbers)
            num_disp = item['number'].split('.')[-1]
            badge_set = BADGE_VARIANT_38[color_idx] if len(num_disp) >= 2 else BADGE_VARIANT[color_idx]
            out.append(render_item(item, color_idx, badge_set))
            if i != len(section_items) - 1:
                out.append(f'<div class="{DIVIDER_CLASS[(color_idx + 1) % 4]}"></div>\n')
            color_idx = (color_idx + 1) % 4

    return ''.join(out)


PAGE = build_page()

HTML = f'''<!DOCTYPE html>
<html lang="hi">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>आव्यूह · अध्याय 3 &mdash; प्रश्न एवं हल</title>
<link rel="stylesheet" href="final.hi.css">
</head>
<body>
<main class="sheet">
  <div class="s1">
{PAGE}  </div>
</main>
</body>
</html>
'''

out_path = os.path.join(os.path.dirname(__file__), 'final.hi.html')
with open(out_path, 'w', encoding='utf-8') as f:
    f.write(HTML)
print('wrote', out_path, len(HTML), 'chars')
