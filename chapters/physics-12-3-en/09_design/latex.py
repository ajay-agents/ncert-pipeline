# -*- coding: utf-8 -*-
"""LaTeX -> HTML converter for physics-12-2-en's stage 9 page, adapted from
physics-12-1-en's own working converter (same subject, same language, the
most recent prior chapter - see step_9/PROMPT.md for every documented trap
this implementation defends against): division-rewrite for bare `/`,
unit/exponent bypass of that rewrite, non-breaking spaces around ~/x/./=,
`=`-glued fraction/sqrt chains, \\left(\\right) as its own unit,
\\begin{aligned}/\\begin{array}/\\begin{gathered} row splitting via the
generic \\begin handler.

Re-checked for THIS chapter (physics-12-2, Electrostatic Potential and
Capacitance) by grepping 06_simplify/chapter.simplified.en.md for every
`\\[a-zA-Z]+` command actually used: \\circ/\\cos/\\dfrac/\\epsilon/\\in/
\\left/\\mathbf/\\mathrm/\\mu/\\pi/\\prime/\\propto/\\quad/\\right/\\sqrt/
\\text/\\therefore/\\theta/\\times/\\varepsilon, plus \\begin{aligned}/
\\begin{array} (no \\begin{gathered}/\\begin{cases}, no \\oint, no \\sum -
none of those appear in this chapter's own 21 used items, only possibly in
discarded orphan additional-exercises that never reached 06_simplify).
Everything physics-12-1-en's own converter already carries (epsilon/
varepsilon/circ-as-degree/in-as-epsilon-OCR-artifact, all already needed
there too since Coulomb's-law permittivity is common to both chapters)
covers this chapter directly. Two gaps found and fixed: \\dfrac (display
fraction, used in ex_2.4/ex_2.8's answers) was entirely unhandled - now an
alias of \\frac; \\propto (V \\propto 1/r, example 2.2's potential-falloff
remark) was entirely unhandled - now maps to "\u221d" with non-breaking
padding, same convention as \\times/\\cdot.

Dropped from maths-12-5: bracketed-matrix and determinant-bar rendering
(.s94-.s98/.sD1-.sD3) - genuine determinant/matrix content never appears in
this chapter's electrostatics arithmetic, so that code is dead weight here,
not a defensive keep.

Per step_9/PROMPT.md's own explicit warning ("a converter built against one
chapter's own content will only handle the notation that chapter happened
to use"), this chapter's own 06_simplify/chapter.simplified.en.md was
grepped for every `\\[a-zA-Z]+` command actually used before trusting this
adaptation, turning up several gaps a Maths (Continuity/Differentiability)
chapter's own converter never needed:
  - \\epsilon (38x) / \\varepsilon (20x) - the permittivity symbol
    epsilon-zero, this chapter's single most common Greek letter after pi -
    entirely missing from the source converter's GREEK table.
  - \\rho (5x, charge density), \\sigma (5x, surface charge density),
    \\tau (1x, torque) - likewise missing.
  - \\Delta (19x, "the area element DS") and \\Phi (7x, flux) - the
    CAPITAL Greek letters; only lowercase phi was covered.
  - \\hat (16x) and \\vec (4x) - accent commands for unit vectors
    (r-hat, n-hat) and vector arrows (E-vec, F-vec), pervasive in this
    chapter's force/field notation, entirely unhandled by the source
    converter (never needed on a Maths chapter).
  - \\sim (3x), \\gg (2x), \\approx (2x), \\AA (1x, the angstrom unit
    symbol), \\angle (1x) - all missing.
Also two chapter-specific overrides of symbols the source converter DOES
map, but to the wrong meaning for THIS chapter's content:
  - \\circ: the source maps it to the function-composition symbol (a
    Maths-chapter need). Every one of this chapter's own 9 \\circ
    occurrences is a degree sign (30^\\circ, 180^\\circ, ...) - confirmed
    by grepping every instance in 07_format/structured.en.md before
    overriding, per step_9/PROMPT.md's own "don't disambiguate
    speculatively" guidance. Mapped to the degree sign here instead.
  - \\in: the source maps it to the set-membership symbol. This chapter
    has zero set-theory content; its 4 occurrences (all "\\in_{0}") are a
    mathpix OCR artifact misreading the permittivity symbol epsilon-zero
    (confirmed by checking each of the 4 occurrences directly - all read
    "Permittivity of free space" right next to them). Mapped to epsilon
    here instead, matching \\epsilon/\\varepsilon.
"""
import re

NBSP = "\u00a0"

GREEK = {
    "pi": "\u03c0", "theta": "\u03b8", "alpha": "\u03b1", "beta": "\u03b2",
    "phi": "\u03c6", "varphi": "\u03c6", "lambda": "\u03bb", "mu": "\u03bc",
    "delta": "\u03b4", "gamma": "\u03b3",
    # added for this chapter (see module docstring) - permittivity/charge
    # density/torque symbols a Maths chapter never needed.
    "epsilon": "\u03b5", "varepsilon": "\u03b5",
    "rho": "\u03c1", "sigma": "\u03c3", "tau": "\u03c4",
}

NOARG_SYMBOL = {
    "times": NBSP + "\u00d7" + NBSP, "cdot": NBSP + "\u00b7" + NBSP,
    "div": NBSP + "\u00f7" + NBSP,
    "therefore": "\u2234", "because": "\u2235",
    "quad": NBSP + NBSP, "qquad": NBSP + NBSP + NBSP + NBSP,
    "Rightarrow": NBSP + "\u21d2" + NBSP, "rightarrow": NBSP + "\u2192" + NBSP,
    "leq": NBSP + "\u2264" + NBSP, "geq": NBSP + "\u2265" + NBSP,
    "neq": NBSP + "\u2260" + NBSP,
    # \in overridden below (this chapter's own OCR-artifact meaning, not
    # set membership - see module docstring).
    "notin": NBSP + "\u2209" + NBSP, "infty": "\u221e",
    # \circ overridden below (degree sign, not function composition, for
    # this chapter - see module docstring).
    "pm": NBSP + "\u00b1" + NBSP,
    "cup": NBSP + "\u222a" + NBSP,
    "prime": "\u2032",
    "ldots": "\u2026",
    "propto": NBSP + "\u221d" + NBSP,  # V \propto 1/r (potential falls off notation)
    # --- added for this chapter (see module docstring) ---
    "Delta": "\u0394",           # capital delta, upright (not italicized
                                  # like a variable name - matches how
                                  # \Delta S is printed in the source)
    "Phi": "\u03a6",              # capital phi, upright (flux symbol)
    "Omega": "\u03a9",            # capital omega, upright - the ohm unit
                                  # symbol (resistance), not a variable name;
                                  # entirely missing from physics-12-1-en's/
                                  # physics-12-2-en's converter since neither
                                  # chapter's own content used \Omega at all -
                                  # a Current Electricity chapter uses it on
                                  # nearly every line ($100 \Omega$ etc.).
    "sim": NBSP + "\u223c" + NBSP,      # "order of" / "approximately", e.g. r \sim 10^{-15} m
    "approx": NBSP + "\u2248" + NBSP,
    "gg": NBSP + "\u226b" + NBSP,        # much-greater-than, e.g. r \gg a
    "AA": "\u00c5",                # \AA - the angstrom unit symbol
    "angle": "\u2220",
    "circ": "\u00b0",               # override: degree sign, not composition -
                                    # see module docstring.
}
# Greek letters are italicized, matching standard math typesetting (a
# variable name), same convention as every prior chapter's converter.
NOARG_SYMBOL.update({k: f"<i>{v}</i>" for k, v in GREEK.items()})
# \in override: this chapter's \in is always the epsilon-zero OCR artifact,
# never set membership (see module docstring) - italicized the same way as
# \epsilon/\varepsilon, since it renders the same variable, added after the
# GREEK-italics pass above so it isn't overwritten by it.
NOARG_SYMBOL["in"] = f"<i>{GREEK['epsilon']}</i>"

OPERATOR_NAMES = {"sin", "cos", "tan", "cot", "sec", "cosec", "csc", "ln", "log", "lim"}


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

    def _simple_paren_repl(m):
        start = m.start()
        end = m.end()
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


def _split_rows_respecting_nested_env(body):
    """Split `body` on top-level \\\\ only - never inside a nested
    \\begin{...}...\\end{...} block."""
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
    \\begin{...}...\\end{...} block."""
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
                if cmd == "sqrt":
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
                if cmd == "hat":
                    # unit-vector hat accent (r-hat, n-hat, i-hat) - pervasive
                    # in this chapter's force/field direction notation.
                    # Combining circumflex (U+0302) placed right after the
                    # rendered base content - works cleanly for the
                    # single-letter (optionally bold) bases this chapter
                    # always uses.
                    arg, j = _read_arg(s, j)
                    out.append(f'{_convert_inner(arg)}\u0302')
                    i = j
                    continue
                if cmd == "vec":
                    # vector arrow accent (E-vec, F-vec). The combining
                    # right-arrow-above character (U+20D7) - the same
                    # technique \\hat uses via U+0302 - renders as a tofu
                    # box in this font stack (confirmed on a real page
                    # screenshot: STIX Two Text has no glyph for it, unlike
                    # the far more common combining circumflex \\hat uses).
                    # Draw the arrow with CSS instead: a small rightward
                    # arrow positioned just above the base content, the
                    # same "accent via absolute-positioned span" technique
                    # used nowhere else in this converter but the only
                    # reliable cross-font option for this one accent.
                    arg, j = _read_arg(s, j)
                    inner_html = _convert_inner(arg)
                    out.append(
                        '<span style="position:relative; display:inline-block; padding-top:0.55em;">'
                        '<span style="position:absolute; top:-0.05em; left:50%; transform:translateX(-50%); '
                        'font-size:0.7em; line-height:1;">\u2192</span>'
                        f'{inner_html}</span>'
                    )
                    i = j
                    continue
                if cmd in ("mathbf", "boldsymbol"):
                    # \mathbf{F}/\mathbf{E}/\mathbf{r} - this chapter's own
                    # bold-vector notation (not a Maths real-number-set
                    # symbol here) - bold, otherwise rendered like any
                    # other single-letter variable.
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
                    k = j2
                    while k < n and s[k] == " ":
                        k += 1
                    if k < n and s[k] == "{":
                        _, k = _read_group(s, k)
                    end_marker = "\\end{%s}" % envname
                    end_idx = s.find(end_marker, k)
                    if end_idx == -1:
                        body = s[k:]
                        j = n
                    else:
                        body = s[k:end_idx]
                        j = end_idx + len(end_marker)
                    rows = _split_rows_respecting_nested_env(body)
                    row_htmls = []
                    for row in rows:
                        row = row.strip()
                        if not row:
                            continue
                        cells = _split_cells_respecting_nested_env(row)
                        cell_htmls = [_convert_inner(cell.strip()) for cell in cells if cell.strip()]
                        row_htmls.append((NBSP * 2).join(cell_htmls))
                    out.append('<span class="s92">' + "".join(f'<span class="s93">{r}</span>' for r in row_htmls) + '</span>')
                    i = j
                    continue
                if cmd in OPERATOR_NAMES:
                    j2 = j
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
                # unrecognized command - fail visibly (print the bare command
                # name) rather than silently dropping it.
                out.append(cmd)
                i = j
                continue
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
            # a browser (the same rule that lets "well-known" wrap between
            # "well-" and "known") - so a negative number's own sign can
            # end up alone on one line with its digits starting the next
            # ("10^-" / "7"), which reads as a typo, not a line break.
            # Caught for real on this chapter's mobile layout (a narrow
            # column wraps far more aggressively than desktop, exposing
            # this on ordinary negative exponents/coefficients that never
            # visibly wrapped on a wide screen). Use a non-breaking hyphen
            # (U+2011) instead - visually identical, never a break point.
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
    html = _convert_inner(text)
    html = _collapse_space_runs(html)
    return html


def convert_math_spans(text):
    """Replace every $$...$$ and $...$ span in `text` with converted HTML;
    prose outside spans is HTML-escaped."""
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
