# -*- coding: utf-8 -*-
"""Stage 9 render script for economics-12-2 (Introductory Macroeconomics,
Chapter 2: National Income Accounting) - second Economics chapter, same
textbook as economics-12-1. Adapted directly from economics-12-1's own
render_page_en.py (itself adapted from maths-12-5's), since this chapter's
own content, while richer, needs no new rendering machinery beyond what
that script already proves out:

- 13 items total: 1 example (ex_2.1) + 12 exercises (q_2.1-q_2.12) - two
  sections (Examples, then Exercises forcing a page break), unlike
  economics-12-1's own single flat Exercises-only section (0 examples).
- 1 genuine multi-part item (q_2.10, 5 parts a-e) - exercises the parts
  branch for the first time in this subject.
- 3 genuine :::table blocks (ex_2.1's own Table 2.2/2.3, q_2.3's own
  stock-vs-flow comparison) - same bare-table-block handling already
  proven on economics-12-1's own q_1.1.
- 0 figures - confirmed at stage 2, every chapter image is untethered
  narrative illustration with no item to attach to; the figure-rendering
  code paths are kept (same proven logic as every other chapter) but never
  exercised here.
- q_2.6/2.7/2.8/2.11 use the fixed given/key-formula/substitute/conclusion
  labels (stage 8 already resolved this); ex_2.1's own 3 parallel-method
  steps and q_2.9's own 2 sequential-calculation steps were deliberately
  left unlabelled at stage 7 and so carry POSITIONAL stage tags from
  stage 8's mechanical fallback - see chapters/economics-12-2/manifest.json's
  own stage-8 entry for why this is expected, not a bug to fix here.
- q_2.10's own item-level prompt telescopes all 5 part labels into one
  combined enumeration sentence ("...(a) Gross Domestic Product (b) NNP
  at market price (c) ... (e) Personal disposable income") - the "related
  but distinct" telescoping shape step_9/PROMPT.md documents (distinct
  from the simpler exact-duplicate case economics-12-1 never needed to
  handle, since it had no multi-part items at all). Implemented here for
  the first time: strip_telescoped_enumeration() finds each part's own
  (label) marker in the item prompt, in order, and only strips the whole
  enumerated span from the DISPLAYED prompt if every single clause between
  markers is confirmed (after whitespace normalization, since q_2.10's own
  prompt carries a genuine PDF-page-break "\\n\\n" splitting "NNP" from
  "at market price" - already confirmed at stage 5, left as-is in the
  data) as a substring of that same-labelled part's own prompt text. Falls
  back to the full, untouched prompt on any uncertainty (a marker missing,
  a clause that doesn't verify) - never guesses.

latex.py and final.en.css are reused byte-for-byte from economics-12-1 -
this chapter's own math content (subscripted variables like NNP_{FC},
GDP_{MP}, a handful of $$\\begin{aligned}...\\end{aligned}$$ blocks, one
genuine bare "/" division inside math - "(2500 / 3000)" in q_2.11's own
GNP-deflator calculation) is well within what that converter already
handles; none of its matrix/determinant machinery is exercised here but
carrying it does no harm. Note: "Nominal GNP/Real GNP" in q_2.11's own
prose lead-in is NOT inside a $...$ span in the source (mathpix split the
surrounding parenthesis/multiplier into their own math spans and left the
division itself as plain prose) - left as plain text with a literal
slash, not force-converted to a stacked fraction, since it's genuinely
outside any math span and this is how the source itself presents it.
"""
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
    point) outside any $...$ span.

    RETROACTIVE FIX (2026-09-29, found on economics-12-3, confirmed
    already shipping here too): "Rs." (Rupees) has no abbreviation guard,
    so the plain "ASCII . only when not a decimal point" rule above treats
    it as ending a sentence - it doesn't, it's always immediately followed
    by the amount itself ("Rs. 500"). This chapter's own already-published
    final.en.html had 18 separate instances of "Rs." stranded on its own
    line, split from the amount that gives it any meaning (e.g. "So,
    depreciation is Rs." above "200 crores." on the next line) -
    economics-12-1 never exposed this bug only because that chapter is
    entirely math-free and never once writes a currency amount. Also
    guarding "i.e."/"e.g." and "Mr./Mrs./Ms./Dr." (with an optional
    trailing single-capital-letter initial) for the same reason, even
    though this specific chapter's own content doesn't currently use any
    of them - matching the more robust converter now used on every later
    chapter rather than leaving this copy stale. Protected the same way a
    $...$ math span already is, before any line-splitting logic runs."""
    if text is None:
        return []
    spans = []

    def protect(m):
        spans.append(m.group(0))
        return f"\x00{len(spans) - 1}\x00"

    protected = re.sub(
        r'\$\$.+?\$\$|\$[^$]+\$|\b[ie]\.[eg]\.,?|\bRs\.'
        r'|\b(?:Mr|Mrs|Ms|Dr)\.\s*[A-Z]\.|\b(?:Mr|Mrs|Ms|Dr)\.',
        protect, text, flags=re.S)

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
                # RETROACTIVE FIX (2026-09-29, from economics-12-3): a
                # single lowercase letter marking a lettered sub-list
                # ("a.", "b.", ...) is not a sentence end - not currently
                # exercised by this chapter's own content, but matching
                # the more robust converter now used on every later
                # chapter rather than leaving this copy stale.
                is_list_marker = bool(re.fullmatch(r'[a-z]\.', ''.join(buf)))
                if not (prev.isdigit() and nxt.isdigit()) and not prev.isdigit() and not is_list_marker:
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
    """Exact-duplicate case: the item-level prompt is nothing but one
    part's own question again (possibly missing its own leading marker).
    Never triggers on q_2.10 (its item prompt is much longer than any
    single part's), kept for parity with every other chapter's script."""
    if not parts or not item_prompt:
        return item_prompt
    stripped = item_prompt.strip()
    for p in parts:
        p_text = (p.get('prompt_text') or '').strip()
        p_text_nomark = re.sub(r'^\([a-zA-Z0-9]+\)\s*', '', p_text)
        if stripped == p_text or stripped == p_text_nomark:
            return None
    return item_prompt


_WS_RE = re.compile(r'\s+')


def _norm_ws(s):
    return _WS_RE.sub(' ', s).strip()


def strip_telescoped_enumeration(item_prompt, parts):
    """The item-level prompt telescopes every part's own ask into one
    combined enumeration sentence ('...(a) X (b) Y ... (e) Z.') rather
    than being purely one part's own question repeated. Only strip the
    enumerated tail from the DISPLAYED prompt if every single clause
    between consecutive (label) markers is confirmed, after whitespace
    normalization, as a substring of that same-labelled part's own prompt
    text - falls back to the full, untouched prompt on any uncertainty."""
    if not parts or not item_prompt or len(parts) < 2:
        return item_prompt

    labels = [p['label'].strip('()') for p in parts]
    markers = [f'({lab})' for lab in labels]

    positions = []
    search_from = 0
    for marker in markers:
        idx = item_prompt.find(marker, search_from)
        if idx == -1:
            return item_prompt  # a marker is missing - don't guess
        positions.append(idx)
        search_from = idx + len(marker)

    clause_spans = []
    for k in range(len(positions) - 1):
        start = positions[k] + len(markers[k])
        end = positions[k + 1]
        clause_spans.append((start, end))

    # last clause: from its own marker to the first non-decimal sentence
    # terminator, or end of string if none found.
    last_start = positions[-1] + len(markers[-1])
    end = len(item_prompt)
    i = last_start
    while i < len(item_prompt):
        c = item_prompt[i]
        if c in '।?':
            end = i
            break
        if c == '.':
            prev = item_prompt[i - 1] if i > 0 else ''
            nxt = item_prompt[i + 1] if i + 1 < len(item_prompt) else ''
            if not (prev.isdigit() and nxt.isdigit()) and not prev.isdigit():
                end = i
                break
        i += 1
    clause_spans.append((last_start, end))

    for (start, end), part in zip(clause_spans, parts):
        clause = _norm_ws(item_prompt[start:end])
        part_text = _norm_ws((part.get('prompt_text') or ''))
        if not clause or clause not in part_text:
            return item_prompt  # unverified - fail safe, keep full prompt

    return item_prompt[:positions[0]].rstrip()


def render_item(item, color_idx, badges):
    (badge_cls, q_cls, num_cls, topic_cls) = badges
    number_disp = item['number'].split('.')[-1]
    label_prefix = 'question' if item['kind'] == 'exercise' else 'example'

    prompt_text = flow_text(item['prompt'])
    parts_list = item.get('parts') or []
    for p in parts_list:
        p['prompt_text'] = flow_text(p['prompt'])
    if parts_list:
        prompt_text_use = strip_redundant_enumeration(prompt_text, parts_list)
        if prompt_text_use is not None:
            prompt_text_use = strip_telescoped_enumeration(prompt_text_use, parts_list)
    else:
        prompt_text_use = prompt_text
    skip_item_prompt = parts_list and prompt_text_use is None

    body = []
    if not skip_item_prompt and prompt_text_use:
        body.append(render_prompt(prompt_text_use))
        for seg in item['prompt']:
            if seg.get('type') == 'table':
                body.append(render_table_html(seg.get('html', '')))
    elif not skip_item_prompt and item['prompt']:
        for seg in item['prompt']:
            if seg.get('type') == 'table':
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
    sections = [
        ('Examples', [it for it in ITEMS if it['kind'] == 'example']),
        ('Exercises', [it for it in ITEMS if it['kind'] == 'exercise']),
    ]

    total_section_items = sum(len(items) for _, items in sections)
    assert total_section_items == len(ITEMS), (
        f'section list drops items: {total_section_items} != {len(ITEMS)}'
    )

    out.append('<div class="s2">\n  <div class="s3">National Income Accounting</div>\n  <div class="s4">Chapter 2 · All Questions and Complete Solutions</div>\n  <div class="s5"><span class="s6"></span><span class="s7"></span><span class="s8"></span><span class="s9"></span></div>\n</div>\n')

    first_section_rendered = False
    for label, section_items in sections:
        if not section_items:
            continue
        if not first_section_rendered:
            out.append(f'<div class="s10"><div class="s11"></div><div class="s12">{label}</div><div class="s11"></div></div>\n')
            first_section_rendered = True
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
<title>National Income Accounting &middot; Chapter 2 &mdash; Questions and Solutions</title>
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
