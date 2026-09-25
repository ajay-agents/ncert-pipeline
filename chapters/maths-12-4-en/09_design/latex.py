# -*- coding: utf-8 -*-
"""LaTeX -> HTML converter for maths-12-4-en (Determinants, English medium),
adapted from maths-12-3-en's own converter (Matrices, English medium, built
this same session - the most evolved lineage: nesting-aware row/cell
splitting, \\prime/\\binom/\\mathbf support, non-breaking hyphen on a
wrapped negative sign, a "fail visibly" fallback for any still-uncovered
command instead of silently dropping it). See step_9/PROMPT.md for every
documented trap this implementation defends against: division-rewrite for
bare `/`, unit/exponent bypass of that rewrite, non-breaking spaces around
~/x/./=, `=`-glued fraction/sqrt chains, \\left(\\right) as its own unit,
\\begin{aligned}/\\begin{array}/\\begin{gathered}/\\begin{cases} row
splitting via the generic \\begin handler, genuine bracketed-matrix
rendering as a real CSS grid with drawn brackets.

Re-checked for THIS chapter by grepping 06_simplify/chapter.simplified.en.md
for every `\\[a-zA-Z]+` command actually used (see step_9/PROMPT.md's own
coverage grep, reproduced/re-verified here): begin/end/left/right (1193x
each)/frac (334x)/mathrm (275x)/Rightarrow (139x)/text (137x)/sin (136x)/
alpha (133x)/cos (119x)/Delta (110x)/operatorname (104x)/beta (81x)/
rightarrow (77x)/theta (75x)/quad (48x)/gamma (44x)/delta (34x)/neq (31x)/
times (20x)/leq (14x)/cdot (12x)/pm (11x)/in (7x)/leftrightarrow (6x)/
pi (3x)/sqrt (2x)/infty (2x)/mp (1x)/ldots (1x)/mid (1x)/binom (1x).
Display environments: \\begin{array} (950x, the large majority wrapped in
\\left|...\\right| as genuine determinant bars - see below), \\begin{aligned}
(236x), \\begin{gathered} (7x, always used bare/unbracketed as an ad-hoc
column stack for a system-of-equations column vector - rendered correctly
already by the generic \\begin handler below, which doesn't special-case by
env name at all beyond the bracket/paren/bar matrix-span detector's own
`\\begin{array}` check).

Gaps found against maths-12-3-en's own converter and fixed here:
  - **\\Delta (110 occurrences - this chapter's single most-used symbol,
    always meaning "the value of this determinant") was silently DROPPED by
    every converter this one otherwise descends from** - checked directly:
    maths-12-3-en's own GREEK dict only has lowercase "delta" (03B4), never
    uppercase "Delta"; the sibling Hindi maths-12-4 converter (this
    chapter's own closest precedent, same subject) has the exact same gap -
    confirmed for real by grepping ITS rendered final.hi.html for "Delta":
    zero matches, despite 25 occurrences in ITS OWN chapter.simplified.hi.md
    - every \\Delta in that finished, already-shipped chapter renders as
    nothing at all (falls through the "unrecognized command" path, which in
    that older converter drops silently rather than failing visibly). Not
    replicated here: added "Delta": U+0394, italicized the same way every
    other Greek letter used as a variable name is (Delta is assigned,
    subscripted (Delta_1, Delta_2) and combined (Delta_1+Delta_2=Delta)
    exactly like an ordinary variable in this chapter's own content, not
    used as a named-but-fixed physical quantity the way \\Delta S is in the
    physics chapters' own converters, which is why those chose upright
    instead - different chapter, different usage, different choice).
  - **\\leftrightarrow (6x, row/column-swap notation for an elementary
    operation, e.g. "R_1 \\leftrightarrow R_3")**, **\\mp (1x, "k=\\mp 2")**,
    **\\ldots (1x, equation-numbering "\\quad\\ldots(1)")** and **\\mid (1x -
    see note below) were all simply missing from NOARG_SYMBOL** - added:
    U+2194, U+2213 (NBSP-padded like \\pm), U+2026, and a bare "|" for \\mid
    respectively.
    \\mid's own single occurrence ("$A \\mid$ & 0 & 0" inside a determinant
    cell, evidently an OCR artefact that misplaced a determinant bar - the
    intended cell almost certainly reads "$|A|$") is rendered literally as
    the source has it (a bare "|" glued after "A", no reordering) - Rule 1
    says fix content via the data/stage's own logic, never by reshaping it
    silently at render time, so this stays exactly as the JSON has it and
    is flagged in the read-back report instead.
  - \\leq/\\geq/\\neq/\\in/\\binom/\\sqrt/\\pm were already present in
    maths-12-3-en's own tables and needed no changes; \\operatorname already
    renders correctly via the existing \\text/\\mathrm/\\mbox/\\operatorname
    branch (confirmed against this chapter's 104 \\operatorname{adj} uses -
    plain upright "adj", not literal "operatorname" or a stray brace).

New in this chapter's own converter (beyond what maths-12-3-en already had):
**determinant-bar matrices** (`\\left|\\begin{array}{colspec}...\\end{array}
\\right|`) are this chapter's own dominant content shape (376 occurrences -
more than square-bracket (247) and round-paren (282) matrices combined),
since a determinant chapter constantly writes out the array between two
vertical bars rather than in brackets/parens. The matrix-span finder
(`_find_matrix_spans`) now recognizes THREE wrapping delimiters -
`\\left[...\\right]`, `\\left(...\\right)` and `\\left|...\\right|` - around
a `\\begin{array}`, picking bracket-corner flank CSS (.s94/.s95/.s96),
round-corner flank CSS (.s94p/.s95p/.s96p) or plain vertical-line flank CSS
(.s94d/.s95d/.s96d, new here) respectively, so a determinant bar renders as
two straight vertical lines rather than a bracket or a paren - visually
distinct exactly as the source itself distinguishes the three. A bare
`|A|`/`|A-\\lambda I|`-style single-symbol determinant reference (no
`\\begin{array}` immediately inside) is untouched by this and still falls
through to the ordinary `\\left`/`\\right` handler, which already renders a
literal "|" character with no grid needed - exactly the same disambiguation
maths-12-3-en's own bracket/paren detection already relied on.
"""
import re

NBSP = "\u00a0"

GREEK = {
    "pi": "\u03c0", "theta": "\u03b8", "alpha": "\u03b1", "beta": "\u03b2",
    "phi": "\u03c6", "varphi": "\u03c6", "lambda": "\u03bb", "mu": "\u03bc",
    "delta": "\u03b4", "gamma": "\u03b3",
}
# Capital Delta (110x - this chapter's single heaviest-used symbol, always
# "the value of this determinant") - italicized the same as every other
# Greek letter used as a variable name here (assigned, subscripted, combined
# just like an ordinary variable - see module docstring for why this
# chapter's own usage differs from the physics chapters' upright \Delta S).
GREEK_UPPER = {
    "Delta": "\u0394",
}

NOARG_SYMBOL = {
    "times": NBSP + "\u00d7" + NBSP, "cdot": NBSP + "\u00b7" + NBSP,
    "div": NBSP + "\u00f7" + NBSP,
    "therefore": "\u2234", "because": "\u2235",
    "quad": NBSP + NBSP, "qquad": NBSP + NBSP + NBSP + NBSP,
    "Rightarrow": NBSP + "\u21d2" + NBSP, "rightarrow": NBSP + "\u2192" + NBSP,
    "leftrightarrow": NBSP + "\u2194" + NBSP,
    "leq": NBSP + "\u2264" + NBSP, "geq": NBSP + "\u2265" + NBSP,
    "neq": NBSP + "\u2260" + NBSP, "in": NBSP + "\u2208" + NBSP,
    "notin": NBSP + "\u2209" + NBSP, "infty": "\u221e",
    "circ": "\u00b0",
    # inherited from maths-12-3-en - transpose notation (A^{\prime}), not
    # exercised by this chapter's own content (0 occurrences, checked) but
    # kept for parity/robustness against a future correction.
    "prime": "\u2032",
    "pm": NBSP + "\u00b1" + NBSP,
    # added for this chapter (see module docstring): \mp (1x, "k=\mp 2"),
    # \ldots (1x, equation-numbering "\quad\ldots(1)").
    "mp": NBSP + "\u2213" + NBSP,
    "ldots": "\u2026",
    # \mid (1x) - rendered as a bare vertical bar, same glyph a genuine
    # \left|/\right| delimiter already produces; see module docstring for
    # why this single occurrence is very likely an OCR artefact, rendered
    # as-is rather than silently reordered.
    "mid": "|",
}
# Greek letters are italicized, matching standard math typesetting (a
# variable name), same convention as every prior chapter's converter.
NOARG_SYMBOL.update({k: f"<i>{v}</i>" for k, v in GREEK.items()})
NOARG_SYMBOL.update({k: f"<i>{v}</i>" for k, v in GREEK_UPPER.items()})

OPERATOR_NAMES = {"sin", "cos", "tan", "cot", "sec", "cosec", "csc", "ln", "log"}


def _read_group(s, i):
    """s[i] == '{'; return (inner_text, index_after_closing_brace)."""
    assert s[i] == "{"
    depth = 0
    j = i
    while j < len(s):
        if s[j] == "{":
            depth += 1
        elif s[j] == "}":
            depth -= 1
            if depth == 0:
                return s[i + 1:j], j + 1
        j += 1
    return s[i + 1:], len(s)


def _read_arg(s, i):
    """Read one LaTeX argument at s[i:] - a {group} or a single token/char."""
    while i < len(s) and s[i] == " ":
        i += 1
    if i < len(s) and s[i] == "{":
        return _read_group(s, i)
    if i < len(s) and s[i] == "\\":
        j = i + 1
        while j < len(s) and s[j].isalpha():
            j += 1
        return s[i:j], j
    if i < len(s):
        return s[i], i + 1
    return "", i


def _find_matching_env_end(s, k, envname):
    """k points right after \\begin{envname}'s own opening tag (and any
    {colspec} that follows it). Return the index of the \\end{envname} that
    actually matches - accounting for the SAME env name nesting inside its
    own body (e.g. a matrix cell that itself contains another \\begin{array})
    - rather than a naive str.find, which would stop at the first
    \\end{array} found, truncating the outer body if any genuine same-name
    nesting occurs anywhere inside it. Returns -1 if unmatched (caller
    already has a documented fail-safe for this - treat the remainder of
    the string as the implicit body)."""
    begin_marker = "\\begin{%s}" % envname
    end_marker = "\\end{%s}" % envname
    depth = 1
    pos = k
    while True:
        nb = s.find(begin_marker, pos)
        ne = s.find(end_marker, pos)
        if ne == -1:
            return -1
        if nb != -1 and nb < ne:
            depth += 1
            pos = nb + len(begin_marker)
        else:
            depth -= 1
            pos = ne + len(end_marker)
            if depth == 0:
                return ne


# ============================================================
# Division rewrite: bare `/` -> \frac{num}{den} before the main convert.
# ============================================================

def _bracket_depths(s):
    depth = 0
    depths = []
    i = 0
    while i < len(s):
        c = s[i]
        if c in "{[(":
            depths.append(depth)
            depth += 1
        elif c in "}])":
            depth -= 1
            depths.append(depth)
        else:
            depths.append(depth)
        i += 1
    return depths


def _find_left_right_spans(s):
    """Return list of (start, end) exclusive spans covering \\left...\\right...
    as one opaque unit, so the bare-paren/division logic never looks inside
    or steals half of one."""
    spans = []
    i = 0
    while True:
        m = re.search(r"\\left", s[i:])
        if not m:
            break
        start = i + m.start()
        j = start + 5
        depth = 1
        while j < len(s) and depth > 0:
            if s[j:j + 5] == "\\left":
                depth += 1
                j += 5
            elif s[j:j + 6] == "\\right":
                depth -= 1
                j += 6
            else:
                j += 1
        spans.append((start, j))
        i = j
    return spans


def _in_any_span(pos, spans):
    return any(a <= pos < b for a, b in spans)


def _rewrite_divisions(s):
    """Rewrite a top-level bare `/` into \\frac{num}{den}. Depth-0 only,
    never inside \\left...\\right (handled as one opaque unit first), never
    inside a \\text{}/\\mathrm{}/\\mbox{}/\\operatorname{} wrapper (those
    bypass this entirely via their own handler), never splitting a unit
    (\\mathrm{...} / \\mathrm{...}). (This chapter's own content has zero
    bare top-level `/` occurrences - checked directly - but this pass is
    kept unconditionally, matching every prior chapter's converter, since a
    later correction to the source could introduce one.)"""
    if "/" not in s:
        return s

    lr_spans = _find_left_right_spans(s)

    # simple parenthesized case: "(a/b)" with bare parens, wrapping exactly
    # one clean division and nothing else -> direct fraction, drop parens.
    def _simple_paren_repl(m):
        start = m.start()
        end = m.end()
        # refuse if this match starts right after a \left token or overlaps
        # a \left...\right span
        if s[:start].endswith("\\left"):
            return m.group(0)
        if _in_any_span(start, lr_spans) or _in_any_span(end - 1, lr_spans):
            return m.group(0)
        inner = m.group(1)
        if "\\right" in inner or "\\left" in inner:
            return m.group(0)
        num, den = inner.split("/", 1)
        return "\\frac{%s}{%s}" % (num.strip(), den.strip())

    s = re.sub(r"\(([^()/]+/[^()/]+)\)", _simple_paren_repl, s)

    # unit-slash guard: a "/" structurally between two \mathrm{...}/\text{...}
    # wrappers (e.g. \mathrm{Nm}^{2} / \mathrm{C}^{2}) is a unit, not a value
    # division - leave those bare, the \mathrm handler renders them plainly.
    WRAP_RE = re.compile(r"\\(?:mathrm|text|mbox|operatorname)\s*\{")

    def _ends_with_wrap_group(text):
        m = None
        for mm in WRAP_RE.finditer(text):
            m = mm
        if m is None:
            return False
        _, after = _read_group(text, text.index("{", m.start()))
        tail = text[after:]
        tail2 = tail
        while True:
            tm = re.match(r"^\s*[\^_]\{[^{}]*\}", tail2)
            if not tm:
                break
            tail2 = tail2[tm.end():]
        return tail2.strip() == ""

    def _starts_with_wrap(text):
        return bool(re.match(r"^\s*" + WRAP_RE.pattern, text))

    depths = _bracket_depths(s)
    slash_positions = [i for i, c in enumerate(s) if c == "/" and depths[i] == 0]
    if not slash_positions:
        return s

    result = []
    last = 0
    for pos in slash_positions:
        if _in_any_span(pos, lr_spans):
            continue
        before = s[last:pos]
        after_full = s[pos + 1:]

        if _ends_with_wrap_group(before) and _starts_with_wrap(after_full):
            continue  # unit slash, leave bare

        num_start = 0
        i = len(before) - 1
        while i >= 0:
            if before[i] == "=" and depths[last + i] == 0:
                num_start = i + 1
                break
            if before.startswith("\\times", i) or before.startswith("\u00d7", i):
                seg_after = before[i:]
                tm = re.match(r"(\\times|\u00d7)\s*10", seg_after)
                if not tm:
                    num_start = i + (len("\\times") if before.startswith("\\times", i) else 1)
                    break
            i -= 1
        numerator = before[num_start:].strip()

        den_end_rel = len(after_full)
        depth_local = 0
        k = 0
        while k < len(after_full):
            c = after_full[k]
            if c in "{[(":
                depth_local += 1
            elif c in "}])":
                depth_local -= 1
            if depth_local == 0:
                if c == "=":
                    den_end_rel = k
                    break
                if after_full.startswith("\\times", k) or after_full.startswith("\u00d7", k):
                    tm = re.match(r"(\\times|\u00d7)\s*10", after_full[k:])
                    if not tm:
                        den_end_rel = k
                        break
                if re.match(r"\\text\s*\{", after_full[k:]):
                    den_end_rel = k
                    break
            k += 1
        denominator = after_full[:den_end_rel].strip()

        if not numerator or not denominator:
            continue

        result.append(s[last:last + num_start])
        result.append("\\frac{%s}{%s}" % (numerator, denominator))
        last = pos + 1 + den_end_rel
    result.append(s[last:])
    return "".join(result)


# ============================================================
# Bracketed/parenthesised/determinant-bar-matrix rendering: \left[\begin
# {array}{colspec}...\end{array}\right] OR \left(\begin{array}{colspec}
# ...\end{array}\right) OR \left|\begin{array}{colspec}...\end{array}\right|
# as a real CSS grid with drawn flanks (square brackets for the `[`/`]` form
# - .s94-.s98 - round parens for the `(`/`)` form - .s94p/.s95p/.s96p - or
# plain vertical-line flanks for the `|`/`|` determinant-bar form - .s94d/
# .s95d/.s96d, new for this chapter - all three reusing the same .s97/.s98
# grid/cell classes). The determinant-bar form is THIS chapter's own
# dominant content shape (376 occurrences vs. 247 square-bracket + 282
# round-paren - see module docstring). Done as a text-level pre-pass
# (mirrors _rewrite_divisions's own shape): find every genuine bracketed/
# parenthesised/barred matrix span, render it immediately (recursing into
# each cell via _convert_inner), and swap it for an inert control-character
# marker so the main converter loop below never has to know matrices exist -
# substituted back to real HTML once that loop is done.
# ============================================================

_MATRIX_MARK = "\x02"


def _find_matrix_spans(s):
    """Find every \\left[...\\right], \\left(...\\right) or \\left|...\\right|
    span whose content starts with \\begin{array} - a genuine matrix/
    determinant, not just any bracketed/parenthesised/barred \\left...\\right
    use (a bare |A|-style single-symbol absolute-value/determinant reference
    has no \\begin{array} inside and is left untouched, to the ordinary
    \\left/\\right handler, which already renders a literal "|" with no grid
    needed there). Returns (start, end, colspec, body, delim) tuples,
    non-overlapping, left to right, `delim` one of "[", "(" or "|" so the
    caller can pick the matching flank style."""
    spans = []
    i = 0
    pattern = re.compile(r"\\left([\[(|])\s*\\begin\{array\}")
    close_for = {"[": "]", "(": ")", "|": "|"}
    while True:
        m = pattern.search(s, i)
        if not m:
            break
        start = m.start()
        delim = m.group(1)
        close_delim = close_for[delim]
        after_left = start + len("\\left") + 1
        bm = re.match(r"\s*\\begin\{array\}", s[after_left:])
        begin_end = after_left + bm.end()
        if begin_end < len(s) and s[begin_end] == "{":
            colspec, k = _read_group(s, begin_end)
        else:
            colspec, k = "", begin_end
        end_idx = _find_matching_env_end(s, k, "array")
        if end_idx == -1:
            i = start + 5
            continue
        body = s[k:end_idx]
        after_end = end_idx + len("\\end{array}")
        rm = re.match(r"\s*\\right" + re.escape(close_delim), s[after_end:])
        if not rm:
            i = start + 5
            continue
        span_end = after_end + rm.end()
        spans.append((start, span_end, colspec, body, delim))
        i = span_end
    return spans


def _render_matrix(colspec, body, delim):
    rows = _split_rows_respecting_nested_env(body)
    parsed_rows = [_split_cells_respecting_nested_env(r) for r in rows if r.strip()]
    parsed_rows = [[c.strip() for c in row] for row in parsed_rows]
    if colspec and colspec.strip():
        ncols = len(colspec.strip())
    else:
        ncols = max((len(r) for r in parsed_rows), default=1)
    cells_html = "".join(
        f'<span class="s98">{_convert_inner(c)}</span>'
        for row in parsed_rows for c in row
    )
    grid = (f'<span class="s97" style="grid-template-columns:'
            f'repeat({ncols}, minmax(1.6em, max-content));">{cells_html}</span>')
    if delim == "[":
        return f'<span class="s94"><span class="s95"></span>{grid}<span class="s96"></span></span>'
    if delim == "(":
        return f'<span class="s94p"><span class="s95p"></span>{grid}<span class="s96p"></span></span>'
    return f'<span class="s94d"><span class="s95d"></span>{grid}<span class="s96d"></span></span>'


def _extract_matrices(s):
    """Replace every genuine bracketed/parenthesised-matrix span with an
    inert marker token (a control character no LaTeX command/operator this
    converter recognizes ever produces, so the main loop passes it through
    unchanged) and return (masked_text, {token: rendered_html})."""
    spans = _find_matrix_spans(s)
    if not spans:
        return s, {}
    mapping = {}
    out = []
    last = 0
    for idx, (start, end, colspec, body, delim) in enumerate(spans):
        out.append(s[last:start])
        token = f"{_MATRIX_MARK}M{idx}{_MATRIX_MARK}"
        mapping[token] = _render_matrix(colspec, body, delim)
        out.append(token)
        last = end
    out.append(s[last:])
    return "".join(out), mapping


def _split_rows_respecting_nested_env(body):
    """Split `body` on top-level \\\\ only - never inside a nested
    \\begin{...}...\\end{...} block. A labeled-column array nested inside an
    outer \\begin{aligned}/\\begin{array} row has its own internal \\\\ row
    separators, which a naive body.split("\\\\\\\\") can't tell apart from the
    outer block's own row breaks - caught for real in maths-12-3-en (this
    converter's own immediate ancestor, ex_3.11/ex_3.19). Track \\begin/\\end
    nesting depth char-by-char and only split at depth 0."""
    rows = []
    buf = []
    i = 0
    n = len(body)
    depth = 0
    while i < n:
        if body[i:i + 6] == "\\begin":
            depth += 1
            buf.append(body[i])
            i += 1
            continue
        if body[i:i + 4] == "\\end":
            depth -= 1
            buf.append(body[i])
            i += 1
            continue
        if depth <= 0 and body[i:i + 2] == "\\\\":
            rows.append("".join(buf))
            buf = []
            i += 2
            continue
        buf.append(body[i])
        i += 1
    rows.append("".join(buf))
    return rows


def _split_cells_respecting_nested_env(row):
    """Split `row` on top-level & only - never inside a nested
    \\begin{...}...\\end{...} block, the same depth-tracking technique as
    _split_rows_respecting_nested_env's own \\\\ splitting above, applied to
    & instead - a bare (non-bracketed) \\begin{array} used purely as a
    column-aligned grid nested inside an outer aligned/array row has its own
    internal & column separators. Track \\begin/\\end nesting depth
    char-by-char and only split at depth 0."""
    cells = []
    buf = []
    i = 0
    n = len(row)
    depth = 0
    while i < n:
        if row[i:i + 6] == "\\begin":
            depth += 1
            buf.append(row[i])
            i += 1
            continue
        if row[i:i + 4] == "\\end":
            depth -= 1
            buf.append(row[i])
            i += 1
            continue
        if depth <= 0 and row[i] == "&":
            cells.append("".join(buf))
            buf = []
            i += 1
            continue
        buf.append(row[i])
        i += 1
    cells.append("".join(buf))
    return cells


# ============================================================
# Main converter
# ============================================================

ENV_ALIASES = {"aligned": "aligned", "array": "array", "gathered": "aligned", "cases": "cases"}


def _convert_inner(s, bypass_division=False):
    """Core recursive converter. bypass_division=True skips the top-level
    division rewrite (used for exponent/unit content whose braces are
    already stripped, per the documented trap)."""
    if not bypass_division:
        s = _rewrite_divisions(s)
    out = []
    i = 0
    n = len(s)
    while i < n:
        c = s[i]
        if c == "\\":
            # multi-letter or single-symbol command
            m = re.match(r"\\([a-zA-Z]+)", s[i:])
            if m:
                cmd = m.group(1)
                j = i + m.end()
                if cmd in ("frac", "dfrac"):
                    num, j = _read_arg(s, j)
                    den, j = _read_arg(s, j)
                    num_html = _convert_inner(num)
                    den_html = _convert_inner(den)
                    out.append(f'<span class="s31"><span class="s32">{num_html}</span><span class="s33">{den_html}</span></span>')
                    i = j
                    continue
                if cmd == "binom":
                    # a 2-row column vector in parentheses (this chapter's
                    # own "solve by matrix method" simultaneous-equation
                    # setup, e.g. x\binom{2}{3}+y\binom{-1}{1}=\binom{10}{5})
                    # - not a division, not a fraction; render as a small
                    # parenthesised two-cell stack, same flank/grid device
                    # as the bracketed-matrix renderer above.
                    top, j = _read_arg(s, j)
                    bot, j = _read_arg(s, j)
                    top_html = _convert_inner(top)
                    bot_html = _convert_inner(bot)
                    grid = (f'<span class="s97b">'
                            f'<span class="s98">{top_html}</span>'
                            f'<span class="s98">{bot_html}</span></span>')
                    out.append(f'<span class="s94p"><span class="s95p"></span>{grid}<span class="s96p"></span></span>')
                    i = j
                    continue
                if cmd == "sqrt":
                    # optional [n] root index (unused here, chapter has none)
                    while j < n and s[j] == " ":
                        j += 1
                    if j < n and s[j] == "[":
                        k = s.index("]", j)
                        j = k + 1
                    arg, j = _read_arg(s, j)
                    inner_html = _convert_inner(arg)
                    is_frac = "\\frac" in arg or "/" in arg
                    if is_frac:
                        out.append(f'<span class="s90">\u221a({inner_html})</span>')
                    else:
                        out.append(f'\u221a({inner_html})')
                    i = j
                    continue
                if cmd == "bar":
                    arg, j = _read_arg(s, j)
                    out.append(f'<span style="text-decoration:overline">{_convert_inner(arg)}</span>')
                    i = j
                    continue
                if cmd in ("mathbf", "boldsymbol"):
                    # \mathbf{N} - this chapter's induction-proof natural-
                    # numbers set notation ("n \in \mathbf{N}"); simple bold,
                    # no other special meaning.
                    arg, j = _read_arg(s, j)
                    out.append(f"<b>{_convert_inner(arg)}</b>")
                    i = j
                    continue
                if cmd in ("text", "mathrm", "mbox", "operatorname"):
                    arg, j = _read_arg(s, j)
                    inner_html = _convert_inner(arg, bypass_division=True)
                    inner_html = inner_html.replace("~", NBSP)
                    out.append(inner_html)
                    i = j
                    continue
                if cmd in ("left", "right"):
                    # consume delimiter: a two-char \{ \} \| token, or a
                    # single char (or '.' for an invisible delimiter)
                    while j < n and s[j] == " ":
                        j += 1
                    if j < n and s[j] == "\\" and j + 1 < n and s[j + 1] in "{}|":
                        delim = s[j + 1]
                        j += 2
                    else:
                        delim = s[j] if j < n else ""
                        j += 1
                    out.append("" if delim == "." else _escape(delim))
                    i = j
                    continue
                if cmd == "begin":
                    envname, j2 = _read_arg(s, j)
                    # consume optional {colspec}
                    k = j2
                    while k < n and s[k] == " ":
                        k += 1
                    if k < n and s[k] == "{":
                        _, k = _read_group(s, k)
                    end_idx = _find_matching_env_end(s, k, envname)
                    if end_idx == -1:
                        # missing/unmatched \end{envname} - a genuine
                        # source-side defect, not something to silently fall
                        # through on (a bare "&" with no special handling
                        # elsewhere would html-escape to a literal "&amp;").
                        # Fail safe instead: treat everything from k to the
                        # end of the string as the implicit body.
                        body = s[k:]
                        j = n
                    else:
                        body = s[k:end_idx]
                        j = end_idx + len("\\end{%s}" % envname)
                    rows = _split_rows_respecting_nested_env(body)
                    row_htmls = []
                    for row in rows:
                        row = row.strip()
                        if not row:
                            continue
                        cells = _split_cells_respecting_nested_env(row)
                        cell_htmls = [_convert_inner(cell.strip()) for cell in cells if cell.strip()]
                        # multiple real cells on one row is a genuine
                        # multi-column grid - give them a visible gap; a
                        # single cell (the common aligned-equation case)
                        # needs none.
                        row_htmls.append((NBSP * 2).join(cell_htmls))
                    out.append('<span class="s92">' + "".join(f'<span class="s93">{r}</span>' for r in row_htmls) + '</span>')
                    i = j
                    continue
                if cmd in OPERATOR_NAMES:
                    j2 = j
                    # optional ^{-1} or ^{...}
                    sup = None
                    while j2 < n and s[j2] == " ":
                        j2 += 1
                    if j2 < n and s[j2] == "^":
                        sup_arg, j2 = _read_arg(s, j2 + 1)
                        sup = sup_arg
                    label = cmd if cmd != "cosec" else "cosec"
                    if sup is not None:
                        sup_html = _convert_inner(sup, bypass_division=True)
                        out.append(f"{label}<sup>{sup_html}</sup>")
                        i = j2
                    else:
                        out.append(label)
                        i = j
                    continue
                if cmd in NOARG_SYMBOL:
                    out.append(NOARG_SYMBOL[cmd])
                    i = j
                    continue
                # unrecognized command - fail visibly (print the bare
                # command name) rather than silently dropping it. Per
                # step_9/PROMPT.md's own documented trap, a converter built
                # against one chapter's own content only covers what that
                # chapter happened to use; printing the bare name instead of
                # vanishing silently means a genuinely-missed command is
                # still visible in the manual read-back and in the rendered
                # page itself, rather than a content gap no check can catch.
                out.append(cmd)
                i = j
                continue
            # single-char command like \{ \} \, etc.
            nxt = s[i + 1] if i + 1 < n else ""
            if nxt in "{}":
                out.append(nxt)
                i += 2
                continue
            if nxt == ",":
                out.append(" ")
                i += 2
                continue
            i += 1
            continue
        if c == "^":
            arg, j = _read_arg(s, i + 1)
            html = _convert_inner(arg, bypass_division=True)
            out.append(f"<sup>{html}</sup>")
            i = j
            continue
        if c == "_":
            arg, j = _read_arg(s, i + 1)
            html = _convert_inner(arg, bypass_division=True)
            out.append(f"<sub>{html}</sub>")
            i = j
            continue
        if c in "{}":
            i += 1
            continue
        if c == "~":
            out.append(NBSP)
            i += 1
            continue
        if c == "=":
            # check for immediately following \frac or \sqrt (glue chain)
            j = i + 1
            while j < n and s[j] == " ":
                j += 1
            if s[j:j + 5] == "\\frac" or s[j:j + 5] == "\\sqrt":
                glued = ["="]
                k = j
                while True:
                    if s[k:k + 5] == "\\frac":
                        arg_start = k + 5
                        num, arg_start = _read_arg(s, arg_start)
                        den, arg_start = _read_arg(s, arg_start)
                        glued.append(f'<span class="s31"><span class="s32">{_convert_inner(num)}</span><span class="s33">{_convert_inner(den)}</span></span>')
                        k = arg_start
                    elif s[k:k + 5] == "\\sqrt":
                        arg_start = k + 5
                        arg, arg_start = _read_arg(s, arg_start)
                        glued.append(f'\u221a({_convert_inner(arg)})')
                        k = arg_start
                    else:
                        break
                    while k < n and s[k] == " ":
                        k += 1
                    if k < n and s[k] == "=":
                        glued.append(NBSP + "=" + NBSP)
                        k += 1
                        while k < n and s[k] == " ":
                            k += 1
                        if not (s[k:k + 5] == "\\frac" or s[k:k + 5] == "\\sqrt"):
                            break
                    else:
                        break
                out.append(f'<span class="s90">{"".join(glued)}</span>')
                i = k
                continue
            out.append(NBSP + "=" + NBSP)
            i += 1
            continue
        if c in "\u00d7\u00b7\u00f7":
            out.append(NBSP + c + NBSP)
            i += 1
            continue
        if c == "-" and i + 1 < n and s[i + 1].isdigit():
            # A plain ASCII hyphen-minus is a valid soft line-break point to
            # a browser - so a negative number's own sign can end up alone
            # on one line with its digits starting the next, which reads as
            # a typo on a narrow mobile column. Use a non-breaking hyphen
            # (U+2011) instead - visually identical, never a break point.
            # This chapter's matrices are full of negative entries
            # (e.g. "-1", "-5"), so this matters more here than most.
            out.append("\u2011")
            i += 1
            continue
        out.append(_escape(c))
        i += 1
    return "".join(out)


def _escape(c):
    return {"&": "&amp;", "<": "&lt;", ">": "&gt;"}.get(c, c)


_SPACE_RUN_RE = re.compile(NBSP + r"[ " + NBSP + r"]*|[ ]+" + NBSP)


def _collapse_space_runs(html):
    def repl(m):
        return NBSP if NBSP in m.group(0) else m.group(0)
    return _SPACE_RUN_RE.sub(repl, html)


def latex_to_html(text):
    """Convert a $...$ / $$...$$-delimited math span's inner content."""
    text, matrix_map = _extract_matrices(text)
    html = _convert_inner(text)
    for token, rendered in matrix_map.items():
        html = html.replace(token, rendered)
    html = _collapse_space_runs(html)
    return html


def convert_math_spans(text):
    """Replace every $$...$$ and $...$ span in `text` with converted HTML;
    prose outside spans is HTML-escaped. (This chapter has zero occurrences
    of a bare `\\{`/`\\}` stranded in plain prose outside any $...$ span -
    checked directly - so no extra prose-side brace fix is needed here.)"""
    if not text:
        return ''
    out = []
    i = 0
    n = len(text)
    while i < n:
        if text[i:i + 2] == "$$":
            end = text.find("$$", i + 2)
            if end == -1:
                out.append(_escape(text[i]))
                i += 1
                continue
            inner = text[i + 2:end]
            out.append(f'<div class="s80">{latex_to_html(inner)}</div>')
            i = end + 2
            continue
        if text[i] == "$":
            end = text.find("$", i + 1)
            if end == -1:
                out.append(_escape(text[i]))
                i += 1
                continue
            inner = text[i + 1:end]
            out.append(latex_to_html(inner))
            i = end + 1
            continue
        out.append(_escape(text[i]))
        i += 1
    return "".join(out)
