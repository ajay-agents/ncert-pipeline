# -*- coding: utf-8 -*-
"""Stage 9 render script for maths-12-4-en (Determinants, English medium),
adapted directly from maths-12-3-en's own render_page.py (Matrices, English
medium, built this same session - the most evolved lineage: English
wording/section titles, the `strip_redundant_enumeration` telescoped-
enumeration handling with a decimal-point guard, the `any_part_has_solution`
fallback for a multi-part item whose real solution lives only at item
level, and the note-block group-kind handling).

This chapter has ZERO figures and ZERO :::table containers anywhere
(confirmed at stage 8 - every item's `figures` is `[]` and no `:::table`
container exists in the source) - the figure/table-rendering branches
inherited from maths-12-3-en are kept for parity/robustness (a future
correction pass could in principle introduce one) but are never exercised
here; the mandatory figure-src-count check in this chapter's own stage 9
report runs and passes trivially (0 referenced == 0 resolved).

Chapter-specific structural note (see step_9/PROMPT.md's own briefing for
this chapter): 9 multi-part items (q_4.2, q_4.5, q_4.7, q_4.9, q_4.11,
q_4.12, q_4.14, q_4.15, q_4.56) have EVERY part's own solution_blocks empty,
with the entire worked solution living only at item level as one combined
narrative addressing every part together (often with inline "(i)"/"(ii)"
markers already embedded in the flow text itself). The
`any_part_has_solution` fallback below (inherited unchanged from
maths-12-3-en, itself inherited from physics-12-5-en) is exactly what
renders this correctly: every part's own prompt is shown under its own
"Part (i)" heading, then the single combined item-level solution stack is
rendered once, after all the part prompts, instead of being silently
dropped for living "one level up" from where a naive per-part loop would
look. This is NOT the "duplicate trailing whole-item solution" artifact
some other chapters have - there is no duplicate to discard, just one
shared solution to render once.

A second chapter-specific quirk handled here: the 26 "additional_exercise"
orphan items (16 `sol_4.d.*`, a properties-of-determinants exercise cut
from the current textbook edition, and 10 `sol_4.misc.*`, interspersed
older-edition Misc items) carry a `number` field that is NOT a plain digit
the way every other item's is - e.g. `"EX4.OLD-1"`, `"MISC-11"`. The plain
`.split('.')[-1]` badge-number derivation every prior chapter's converter
used (assuming a dotted "chapter.number" or bare-digit format) would put
the literal string "OLD-1" or the untouched "MISC-11" into the small round
number badge, which is sized for 1-2 digits and wasn't designed for this -
`badge_number_disp()` below extracts the trailing digit run instead (e.g.
"1" from "EX4.OLD-1", "11" from "MISC-11"), which is what every other
chapter's own badge already shows for its own items; the full original
number string is still kept, untouched, in `data-screen-label` for
traceability even though nothing in the CSS ever displays that attribute.

Two known, accepted, UNCORRECTED data issues rendered exactly as the JSON
has them (per Rule 5 - nothing invented, no cross-source disagreement
silently resolved): q_4.56's question states positive off-diagonal matrix
entries while its own solution's restated matrix uses negative entries for
the same positions (a genuine textbook-vs-solutions-manual disagreement);
q_4.16's solution has a pre-existing cofactor mislabel (calls something
M_21 where A_23 is meant) native to the solutions manual itself. Both are
flagged in the stage report, neither is touched here.
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
CHAPTER_TITLE = DATA['front']['title']
CHAPTER_NUM = DATA['front']['chapter']

# ============================================================
# text helpers
# ============================================================

# This chapter's own content was grepped directly for common abbreviations
# whose internal/trailing periods are not sentence boundaries: "i.e." occurs
# 3 times here too (the same class of bug step_9/PROMPT.md documents for an
# abbreviation the sentence-splitter doesn't know about - without this
# guard, "i.e." would split into two stray one-word "sentences", "i." then
# "e."); "e.g."/"etc."/"Fig." occur zero times here but cost nothing to
# guard against defensively (matching every prior chapter's abbreviation
# set) in case a later correction pass introduces one.
_ABBREV_RE = re.compile(r'\b(?:i\.e\.|e\.g\.|etc\.|Fig\.)', re.I)
_SENT_SPLIT_RE = re.compile(r'(?<!\d)(\.)(?!\d)(?=\s|$)')


def text_to_lines(text):
    """Split flowing prose into one line per sentence: on existing newlines,
    and on sentence-ending punctuation (ASCII '.' only when not a decimal
    point) outside any $...$ span. Also guards a handful of common
    abbreviations whose internal/trailing periods are not sentence
    boundaries either (see _ABBREV_RE above)."""
    if text is None:
        return []
    spans = []

    def protect(m):
        spans.append(m.group(0))
        return f"\x00{len(spans) - 1}\x00"

    protected = re.sub(r'\$\$.+?\$\$|\$[^$]+\$', protect, text, flags=re.S)
    protected = _ABBREV_RE.sub(protect, protected)

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
            if c == '.':
                prev = raw_line[i - 1] if i > 0 else ''
                nxt = raw_line[i + 1] if i + 1 < n else ''
                if nxt in ')]}':
                    buf.append(nxt)
                    i += 1
                    parts.append(''.join(buf))
                    buf = []
                    i += 1
                    continue
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


def render_table_html(table_md):
    """Render a flow's raw markdown pipe-table as a real HTML <table> - this
    chapter has ZERO tables anywhere (confirmed at stage 8 - a Determinants
    chapter has no tabular data), so this is never exercised here, but is
    kept for parity/robustness (a flow-reader that only ever joins
    type:"text" segments would silently drop a table living inside an
    item's own :::prompt, the same documented blind spot as a dropped
    mid-solution figure). Wrapped in a scrollable .s98 div so a wide table
    never overflows
    the page on a narrow viewport or in the printed PDF."""
    lines = [l for l in table_md.strip().split('\n') if l.strip()]
    if len(lines) < 2:
        return ''
    data_lines = [lines[0]] + [l for l in lines[1:] if not _TABLE_SEP_RE.match(l)]
    rows_html = []
    for line in data_lines:
        cells = [c.strip() for c in line.strip().strip('|').split('|')]
        cells_html = ''.join(f'<td class="s100">{convert_math_spans(c)}</td>' for c in cells)
        rows_html.append(f'<tr>{cells_html}</tr>')
    return f'<div class="s101"><table class="s99">{"".join(rows_html)}</table></div>'


def render_prompt(text):
    """Render an item/part prompt as one or more <p class="s21"> paragraphs
    - but first split out any embedded markdown pipe-table. Exam question
    text is immutable (Rule 4), so stage 7 was never allowed to wrap a table
    living inside a :::prompt in :::table the way it could for a solution's
    own content; it survives as bare pipe-syntax lines, and a naive single-
    paragraph join-then-convert prints them as literal "| | ... |" text
    instead of a table."""
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


def render_flow_html(flow, text_renderer):
    """Render an ordered text/figure/table flow, preserving order - a
    figure nested mid-solution (not just an item-level one before any part)
    must render as a real figure element in its correct position, not be
    silently dropped the way a text-only join would. (This chapter has no
    figures at all, but the branch is kept for parity/robustness.)"""
    out = []
    for seg in flow:
        if seg.get('type') == 'text':
            out.append(text_renderer(seg['text']))
        elif seg.get('type') == 'table':
            out.append(render_table_html(seg.get('html', '')))
        elif seg.get('type') == 'figure':
            src = seg.get('src', '')
            cap = seg.get('caption', '')
            out.append(
                f'<div class="s76"><figure class="s77"><img src="{src}" alt="" class="s78">'
                f'<figcaption class="s79">{convert_math_spans(cap)}</figcaption></figure></div>'
            )
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

_TRAILING_DIGITS_RE = re.compile(r'(\d+)$')


def badge_number_disp(number):
    """Derive the short digit string shown in the item's round number badge.
    Every ordinary item's own `number` field is already a bare digit string
    ("2", "56") or, same result, a dotted "chapter.number" - a plain
    `.split('.')[-1]` (the convention every prior chapter's converter used)
    handles both. This chapter's 26 orphan items break that assumption -
    their `number` is a label like "EX4.OLD-1" or "MISC-11" - so pull the
    trailing digit run instead, which is what actually identifies the item
    within its own old-edition exercise and is short enough to fit the
    badge (matches what `.split('.')[-1]` would already give for a normal
    item, since there the whole trailing segment IS the digit run)."""
    m = _TRAILING_DIGITS_RE.search(number)
    return m.group(1) if m else number.split('.')[-1]


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
    """Group consecutive blocks of the same stage, preserving order. A
    block with type "note" or "figure" gets its own group kind (checked
    BEFORE the stage dispatch) rather than being routed through the
    stage-pill branch (a bare figure/note block carries no `stage` key at
    all - conflating the two would silently drop a figure into an empty,
    contentless note pill)."""
    groups = []
    for b in blocks:
        if b['type'] == 'note':
            groups.append({'kind': 'note', 'note': b})
            continue
        if b['type'] == 'figure':
            groups.append({'kind': 'figure', 'figure': b})
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
    # fall back to the last stage group when no block reached `conclusion`
    # (a short solution ending at key_formula/substitute, with the actual
    # result only ever stated in the item's own separate `answer` field) -
    # never silently drop the answer box this way.
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
            # this chapter has none, but handled defensively - sits directly
            # in the .s81 stack, not forced through the 2-child .s82 flex
            # row a stage/note pill assumes.
            fig = g['figure']
            src = fig.get('src', '')
            cap = fig.get('caption', '')
            parts.append(
                f'<div class="s76"><figure class="s77"><img src="{src}" alt="" class="s78">'
                f'<figcaption class="s79">{convert_math_spans(cap)}</figcaption></figure></div>'
            )
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
            # Approximate the answer's own RENDERED width (strip "$"
            # delimiters and LaTeX syntax, keep the digits/letters/units
            # inside each span so they count toward the length the way
            # they visually will), not its raw source length.
            plain_len = len(re.sub(r'\$|\\[a-zA-Z]+|[{}\\^_]', '', answer_text))
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
    where every labelled clause is a substring of that part's own
    prompt)."""
    if not parts or not item_prompt:
        return item_prompt
    stripped = item_prompt.strip()
    for p in parts:
        p_text = (p.get('prompt_text') or '').strip()
        p_text_nomark = re.sub(r'^\([a-zA-Z0-9]+\)\s*', '', p_text)
        if stripped == p_text or stripped == p_text_nomark:
            return None

    # telescoped-enumeration case: every labelled clause a substring of
    # that same-labelled part's own prompt.
    markers = list(re.finditer(r'\(([a-zA-Z0-9]+)\)', stripped))
    if len(markers) >= 2:
        clauses = {}
        clause_end_pos = {}
        for idx, m in enumerate(markers):
            start = m.end()
            end = markers[idx + 1].start() if idx + 1 < len(markers) else len(stripped)
            raw_clause = stripped[start:end]
            # guard against a decimal point being mistaken for the clause's
            # own sentence-ending punctuation (never split a "."
            # immediately preceded/followed by a digit).
            m_end = re.search(r'(?<!\d)\.(?!\d)|[?!]', raw_clause)
            if m_end:
                abs_end = start + m_end.end()
                clause = raw_clause[:m_end.end()]
            else:
                abs_end = end
                clause = raw_clause
            clauses[m.group(1)] = clause.strip()
            clause_end_pos[m.group(1)] = abs_end
        all_ok = True
        for label, clause in clauses.items():
            matching_part = next((p for p in parts if p.get('label', '').strip('()') == label), None)
            if matching_part is None or clause not in (matching_part.get('prompt_text') or ''):
                all_ok = False
                break
        if all_ok and clauses:
            span_start = markers[0].start()
            last_clause_end = clause_end_pos[markers[-1].group(1)]
            remainder = stripped[:span_start].strip()
            trailing = stripped[last_clause_end:].strip()
            trailing = re.sub(r'^[,;]\s*', '', trailing)
            new_prompt = (remainder + ' ' + trailing).strip() if (remainder or trailing) else None
            return new_prompt or None

    return item_prompt


def collect_nested_figure_srcs(blocks):
    """Every figure src that appears inside a solution_blocks list's own
    flows - used to avoid re-rendering the SAME figure a second time in the
    item-level 'figures before the solution' row. (This chapter has none,
    kept for parity/robustness.)"""
    srcs = set()
    for b in blocks or []:
        if b.get('type') == 'figure' and b.get('src'):
            srcs.add(b['src'])
        for seg in b.get('flow') or []:
            if seg.get('type') == 'figure' and seg.get('src'):
                srcs.add(seg['src'])
    return srcs


def render_item(item, color_idx, badges):
    (badge_cls, q_cls, num_cls, topic_cls) = badges
    number_disp = badge_number_disp(item['number'])
    label_prefix = ('Example' if item['kind'] == 'example'
                    else ('Additional Question' if item['kind'] == 'additional_exercise' else 'Question'))

    prompt_text = flow_text(item['prompt'])
    parts_list = item.get('parts') or []
    for p in parts_list:
        p['prompt_text'] = flow_text(p['prompt'])
    prompt_text_use = strip_redundant_enumeration(prompt_text, parts_list) if parts_list else prompt_text
    skip_item_prompt = parts_list and prompt_text_use is None

    body = []
    if not skip_item_prompt:
        if parts_list:
            # multi-part item: use the (possibly enumeration-trimmed) text,
            # not the raw segments - the trimming operates on the flattened
            # text. This chapter's multi-part items have no table/figure in
            # their own item-level prompt flow.
            if prompt_text_use:
                body.append(render_prompt(prompt_text_use))
        else:
            for seg in item['prompt']:
                if seg.get('type') == 'text':
                    body.append(render_prompt(seg['text']))
                elif seg.get('type') == 'table':
                    body.append(render_table_html(seg.get('html', '')))

    # item-level figures (a :::figure sitting before any part/solution) -
    # skip any figure that's ALSO nested inside a solution-block flow (item-
    # level or any part's), or it renders twice on the page. This chapter
    # has zero figures anywhere, so `item.get('figures')` is always empty,
    # but the branch is kept for parity/robustness.
    nested_srcs = collect_nested_figure_srcs(item.get('solution_blocks'))
    for p in parts_list:
        nested_srcs |= collect_nested_figure_srcs(p.get('solution_blocks'))
    for fig in item.get('figures') or []:
        src = fig.get('src', '')
        if src in nested_srcs:
            continue
        cap = fig.get('caption', '')
        body.append(
            f'<div class="s76"><figure class="s77"><img src="{src}" alt="" class="s78">'
            f'<figcaption class="s79">{convert_math_spans(cap)}</figcaption></figure></div>'
        )

    if parts_list:
        # This chapter's 9 multi-part items (q_4.2, q_4.5, q_4.7, q_4.9,
        # q_4.11, q_4.12, q_4.14, q_4.15, q_4.56 - see module docstring) have
        # parts whose OWN solution_blocks/answer are ALL empty, with the
        # real combined solution addressing every part together living only
        # at item level (positional stage-inference only fires once,
        # item-wide, since there's no way to detect "(i)/(ii)/(iii)"
        # sub-boundaries from the flat container tree).
        # Render each part's own prompt as normal, then - only when NO part
        # actually carried its own solution - fall back to the item-level
        # solution_blocks/answer as one combined solution stack after all
        # the part prompts, so this combined answer is never silently
        # dropped just because it lives one level up from where a part loop
        # naturally looks.
        any_part_has_solution = any(p.get('solution_blocks') for p in parts_list)
        for p in parts_list:
            label = p['label']
            # label already comes wrapped in parens from stage 7 for this
            # chapter ("(i)", "(ii)") - don't wrap it again.
            label_disp = label if label.startswith('(') else f'({label})'
            body.append(f'<p class="s59">Part {label_disp}</p>')
            if p['prompt_text']:
                body.append(render_prompt(p["prompt_text"]))
            if any_part_has_solution:
                ans_text = flow_text(p.get('answer') or [])
                body.append(render_solution_stack(p.get('solution_blocks') or [], ans_text, color_idx))
        if not any_part_has_solution:
            ans_text = flow_text(item.get('answer') or [])
            body.append(render_solution_stack(item.get('solution_blocks') or [], ans_text, color_idx))
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
        ('Questions and Solutions', [it for it in ITEMS if it['kind'] == 'exercise']),
        # This chapter keeps 26 genuine orphan solutions (16 from an entire
        # properties-of-determinants exercise cut from the current textbook
        # edition, plus 10 interspersed older-edition Misc items - both
        # preserved from an older solutions manual per the "nothing
        # invented" rule) as their own additional_exercise items - a light
        # "Additional Questions" divider matching the same visual weight as
        # the other two section dividers, the same convention used for
        # physics-12-5-en's own orphan items.
        ('Additional Questions', [it for it in ITEMS if it['kind'] == 'additional_exercise']),
    ]

    total_section_items = sum(len(items) for _, items in sections)
    assert total_section_items == len(ITEMS), (
        f'section list drops items: {total_section_items} != {len(ITEMS)}'
    )

    out.append(f'<div class="s2">\n  <div class="s3">{CHAPTER_TITLE}</div>\n  <div class="s4">Chapter {CHAPTER_NUM} &middot; All Questions and Solutions</div>\n  <div class="s5"><span class="s6"></span><span class="s7"></span><span class="s8"></span><span class="s9"></span></div>\n</div>\n')

    for sec_num, (label, section_items) in enumerate(sections, start=1):
        if sec_num == 1:
            out.append(f'<div class="s10"><div class="s11"></div><div class="s12">Part {sec_num} &middot; {label}</div><div class="s11"></div></div>\n')
        else:
            out.append(f'<div class="s69"><div class="s70"></div><div class="s71">Part {sec_num} &middot; {label}</div><div class="s70"></div></div>\n')

        for i, item in enumerate(section_items):
            num_disp = badge_number_disp(item['number'])
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
<title>{CHAPTER_TITLE} &middot; Chapter {CHAPTER_NUM} &mdash; Questions and Solutions</title>
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
