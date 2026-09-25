# -*- coding: utf-8 -*-
"""LaTeX -> HTML converter for maths-12-3-en (Matrices, English medium),
adapted from two lineages: maths-12-4's own working converter (सारणिक /
Determinants, itself descended from maths-12-3's Hindi-medium converter for
THIS SAME chapter) supplies the matrix/determinant-bar CSS-grid rendering
this chapter needs constantly; physics-12-5-en's converter (the most
recently built in this repo) supplies general fixes accumulated since then
(non-breaking hyphen on a wrapped negative sign, \\dfrac as a \\frac alias,
a "fail visibly" fallback for any still-uncovered command instead of
silently dropping it). See step_9/PROMPT.md for every documented trap this
implementation defends against: division-rewrite for bare `/`, unit/
exponent bypass of that rewrite, non-breaking spaces around ~/x/./=,
`=`-glued fraction/sqrt chains, \\left(\\right) as its own unit,
\\begin{aligned}/\\begin{array}/\\begin{gathered}/\\begin{cases} row
splitting via the generic \\begin handler, genuine bracketed-matrix
rendering as a real CSS grid with drawn brackets.

Re-checked for THIS chapter by grepping 06_simplify/chapter.simplified.en.md
for every `\\[a-zA-Z]+` command actually used: begin/end/left/right (1195x
each - this chapter's dominant shape by far)/frac (462x)/mathrm (413x)/
Rightarrow (283x)/prime (260x)/alpha/cos/sin/theta/text/times/rightarrow/
quad/sqrt/cdot/tan/beta/gamma/in/neq/pm/binom/because/pi/mathbf/qquad, plus
\\begin{array} (1088x) and \\begin{aligned} (187x) - no \\begin{cases}, no
\\begin{gathered}, no \\oint, no \\sum, no bare (non-\\left-wrapped) \\{ set-
builder brace. Three real gaps found against both inherited converters and
fixed here, none of them cosmetic:
  - **\\prime (260 occurrences) was entirely unhandled by BOTH maths-12-3's
    and maths-12-4's own converters** (neither has a "prime" entry anywhere
    in NOARG_SYMBOL) - every `A^{\\prime}` transpose notation in those two
    finished chapters' own converters would have silently rendered as an
    EMPTY superscript, since the unhandled-command path there drops silently
    and this chapter's Hindi twin (maths-12-3) uses \\prime for transpose
    288 times over. Added "prime": U+2032 here; this is the single most
    consequential fix in this file for a chapter that is fundamentally about
    transposes.
  - **\\binom{a}{b} (8 occurrences, ex_3.7-style "solve by matrix method"
    simultaneous-equation setup, e.g. x\\binom{2}{3}+y\\binom{-1}{1}=
    \\binom{10}{5})** - a genuine 2-row column vector in parentheses, not a
    binomial-coefficient stack and not a division; neither inherited
    converter has ANY \\binom handling at all (dropped silently). Added a
    dedicated handler rendering it as a small parenthesised two-row stack
    (.s94b-.s97b), reusing the same "flanks + inner grid" shape as the
    bracketed-matrix renderer below but for exactly two stacked cells.
  - **\\mathbf{N} (2 occurrences, "n \\in \\mathbf{N}" - the induction-proof
    natural-numbers set)** - present in physics-12-5-en's converter (bold)
    but absent from maths-12-3/maths-12-4's; added here (simple bold, no
    special meaning beyond the textbook's own upright-bold set notation).
  - **\\pm was referenced by no chapter content here (0 occurrences) but
    was ALSO simply missing from both inherited NOARG_SYMBOL tables** -
    added defensively since it is such a common, cheap, easily-missed gap
    (a future correction pass to this chapter's own content could
    plausibly introduce a "+/-" case without anyone re-auditing this file).

New in this chapter's own converter (beyond what maths-12-4 already had):
**round-paren matrices** (`\\left(\\begin{array}{colspec}...\\end{array}
\\right)`) are actually the MAJORITY shape here (687 occurrences vs. 377
square-bracket ones per the same grep) - this chapter's own textbook
solutions write "let A = (matrix)" with round parens far more often than
"[matrix]" square brackets, the opposite emphasis from maths-12-4's own
determinant-heavy content. The matrix-span finder below now recognizes
BOTH `\\left[...\\right]` and `\\left(...\\right)` wrapping a `\\begin{array}`
as a genuine matrix (never a bare `|A|`-style single-symbol case, which the
plain \\left/\\right handler already renders correctly with no grid needed),
picking round-corner flank CSS for the paren form and the original
square-bracket flank CSS for the bracket form, so the two remain visually
distinct exactly as the source itself distinguishes them. Also hardened the
matrix/generic-array body finder to be nesting-depth-aware (matching same-
name \\begin/\\end pairs rather than the first literal "\\end{array}"
string found) rather than a naive `str.find` - this chapter has ~13 places
where an outer plain \\begin{array} (a row-reduction step's own alignment
column, or an induction proof's justification column) wraps one or more
complete bracket/paren matrices as sibling cells within its own rows; a
naive first-match end-finder risks truncating the OUTER array's body at the
INNER matrix's own closing tag if ever a matrix genuinely nested inside
another array's cell (not exercised for real in this chapter's own content,
checked, but cheap to make robust against regardless).
"""
import re

NBSP = "\u00a0"

GREEK = {
    "pi": "\u03c0", "theta": "\u03b8", "alpha": "\u03b1", "beta": "\u03b2",
    "phi": "\u03c6", "varphi": "\u03c6", "lambda": "\u03bb", "mu": "\u03bc",
    "delta": "\u03b4", "gamma": "\u03b3",
}

NOARG_SYMBOL = {
    "times": NBSP + "\u00d7" + NBSP, "cdot": NBSP + "\u00b7" + NBSP,
    "div": NBSP + "\u00f7" + NBSP,
    "therefore": "\u2234", "because": "\u2235",
    "quad": NBSP + NBSP, "qquad": NBSP + NBSP + NBSP + NBSP,
    "Rightarrow": NBSP + "\u21d2" + NBSP, "rightarrow": NBSP + "\u2192" + NBSP,
    "leq": NBSP + "\u2264" + NBSP, "geq": NBSP + "\u2265" + NBSP,
    "neq": NBSP + "\u2260" + NBSP, "in": NBSP + "\u2208" + NBSP,
    "notin": NBSP + "\u2209" + NBSP, "infty": "\u221e",
    "circ": "\u00b0",
    # added for this chapter (see module docstring) - transpose notation
    # (A^{\prime}) is this chapter's single most common superscript, and was
    # missing from BOTH converters this file is descended from.
    "prime": "\u2032",
    # not used by this chapter's own content today (0 occurrences), but a
    # cheap, common gap worth closing defensively rather than leaving it to
    # silently drop if a future correction introduces a "+/-" case.
    "pm": NBSP + "\u00b1" + NBSP,
}
# Greek letters are italicized, matching standard math typesetting (a
# variable name), same convention as every prior chapter's converter.
NOARG_SYMBOL.update({k: f"<i>{v}</i>" for k, v in GREEK.items()})

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
# Bracketed/parenthesised-matrix rendering: \left[\begin{array}{colspec}
# ...\end{array}\right] OR \left(\begin{array}{colspec}...\end{array}
# \right) as a real CSS grid with drawn flanks (square brackets for the
# `[`/`]` form - .s94-.s98 - or round parens for the `(`/`)` form - reusing
# the same .s97/.s98 grid/cell classes with .s94p/.s95p/.s96p flanks) - this
# chapter's dominant content shape (1064 occurrences combined). Done as a
# text-level pre-pass (mirrors _rewrite_divisions's own shape): find every
# genuine bracketed-matrix span, render it immediately (recursing into each
# cell via _convert_inner), and swap it for an inert control-character
# marker so the main converter loop below never has to know matrices exist -
# substituted back to real HTML once that loop is done.
# ============================================================

_MATRIX_MARK = "\x02"


def _find_matrix_spans(s):
    """Find every \\left[...\\right] or \\left(...\\right) span whose content
    starts with \\begin{array} - a genuine matrix, not just any bracketed/
    parenthesised \\left...\\right use (a bare |A|-style single-symbol
    absolute-value/determinant reference has no \\begin{array} inside and is
    left untouched, to the ordinary \\left/\\right handler). Returns
    (start, end, colspec, body, delim) tuples, non-overlapping, left to
    right, `delim` one of "[" or "(" so the caller can pick the matching
    flank style."""
    spans = []
    i = 0
    pattern = re.compile(r"\\left([\[(])\s*\\begin\{array\}")
    while True:
        m = pattern.search(s, i)
        if not m:
            break
        start = m.start()
        delim = m.group(1)
        close_delim = "]" if delim == "[" else ")"
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
    return f'<span class="s94p"><span class="s95p"></span>{grid}<span class="s96p"></span></span>'


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
    outer block's own row breaks - caught for real on this chapter's Hindi
    twin (ex_3.11, ex_3.19). Track \\begin/\\end nesting depth char-by-char
    and only split at depth 0."""
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
