# -*- coding: utf-8 -*-
"""LaTeX -> HTML converter for physics-12-11/-1-style stage 9 pages,
adapted for maths-12-2 (Inverse Trigonometric Functions). Modeled on the
established stage-9 pattern (see step_9/PROMPT.md for every documented
trap this implementation defends against): division-rewrite for bare
`/`, unit/exponent bypass of that rewrite, non-breaking spaces around
~/×/·/=, `=`-glued fraction/sqrt chains, \left(\right) as its own unit,
\begin{aligned}/\begin{array}/\begin{gathered} row splitting, inline
\begin{cases}/\begin{array} via the generic \begin handler.
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
    (\\mathrm{...} / \\mathrm{...})."""
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
        # does the wrapper group (with any trailing ^{}/_{}) reach the end?
        _, after = _read_group(text, text.index("{", m.start()))
        tail = text[after:]
        # allow trailing ^{...} or _{...} chains
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

        # find numerator start: nearest depth-0 =, \times/× (not gluing 10^),
        # \text{...} end, or start of `before`
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

        # find denominator end: nearest depth-0 =, \times/×, \text{ start, end of string
        den_end_rel = len(after_full)
        j = 0
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
                # skip following whitespace for arg-taking commands
                if cmd == "frac":
                    num, j = _read_arg(s, j)
                    den, j = _read_arg(s, j)
                    num_html = _convert_inner(num)
                    den_html = _convert_inner(den)
                    out.append(f'<span class="s31"><span class="s32">{num_html}</span><span class="s33">{den_html}</span></span>')
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
                if cmd in ("text", "mathrm", "mbox", "operatorname"):
                    arg, j = _read_arg(s, j)
                    inner_html = _convert_inner(arg, bypass_division=True)
                    inner_html = inner_html.replace("~", NBSP)
                    if cmd == "operatorname":
                        out.append(inner_html)
                    else:
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
                    end_marker = "\\end{%s}" % envname
                    end_idx = s.find(end_marker, k)
                    if end_idx == -1:
                        i = j2
                        continue
                    body = s[k:end_idx]
                    j = end_idx + len(end_marker)
                    rows = body.split("\\\\")
                    row_htmls = []
                    for row in rows:
                        row = row.strip()
                        if not row:
                            continue
                        cells = row.split("&")
                        cell_htmls = [_convert_inner(cell.strip()) for cell in cells]
                        row_htmls.append("".join(cell_htmls))
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
                    else:
                        out.append(label)
                    i = j2
                    continue
                if cmd in NOARG_SYMBOL:
                    out.append(NOARG_SYMBOL[cmd])
                    i = j
                    continue
                # unrecognized command - drop silently (no known chapter use)
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
                # glue this = and every following = <frac/sqrt> into one span
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
        if c in "×·÷":
            out.append(NBSP + c + NBSP)
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
    html = _convert_inner(text)
    html = _collapse_space_runs(html)
    return html


def convert_math_spans(text):
    """Replace every $$...$$ and $...$ span in `text` with converted HTML;
    prose outside spans is HTML-escaped (and gets the same bare-brace fix
    documented in step_9/PROMPT.md, though this chapter has no such case)."""
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
