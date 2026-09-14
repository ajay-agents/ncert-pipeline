# -*- coding: utf-8 -*-
"""LaTeX -> hand-rendered HTML converter for physics-12-9's stage 9 page.
Modeled closely on chapters/physics-12-8/09_design/latex.py (itself modeled
on physics-12-7/physics-12-6's own converters) - fractions as .s31/.s32/.s33,
sqrt as &radic;+overline span, multi-row aligned blocks as .s92/.s93, "="
glued to a following frac/sqrt via .s90, non-breaking spaces around ~/×/·/=,
degree signs as <sup>°</sup>.

This chapter's own LaTeX vocabulary (grepped from 08_tag/structured.hi.json,
per the documented "grep before trusting a reused converter" discipline --
Ray Optics is arithmetic-heavy like physics-12-6/12-7/12-8, but its own
derivations lean much more heavily on explicit logical-step connectives than
any prior chapter did): \\Rightarrow \\rightarrow \\infty \\approx \\geq
\\leq \\therefore \\because \\sin \\tan \\circ \\theta \\pi \\sqrt \\frac
\\left \\right \\mathrm \\text \\prime \\times \\cdot \\quad \\begin{aligned}
\\max. physics-12-8's inherited table already covers therefore/because/sin/
tan/circ/theta/pi/sqrt/frac/left/right/mathrm/text/prime/times/cdot/quad/
aligned -- but NONE of \\Rightarrow, \\rightarrow, \\infty, \\approx, \\geq,
\\leq were in its NOARG_SYMBOL table (that chapter's own EM-wave content
never happened to need an implication arrow, an infinity symbol, or an
inequality/approx sign). This chapter's solutions use "$\\Rightarrow$" as
their single most common connective (every "इसलिए/अतः" step-to-step jump is
written this way, not spelled out in words) and "$v=\\infty$"/"$u
\\rightarrow \\infty$" constantly (a real image forming at infinity is a
recurring physical situation in lens/mirror/telescope problems) -- left
unhandled, these would all fall through to the generic "unknown command:
render its bare name" path and print the literal words "Rightarrow",
"rightarrow", "infty", "approx", "geq", "leq" on the page instead of their
symbols, on nearly every line of nearly every item. Exactly the
cross-chapter (here: cross-content-shape-within-the-same-subject) gap
step_9/PROMPT.md warns a reused converter can silently have. \\max (e.g.
"f_{\\max}") is deliberately left unhandled -- it already falls through to
the same "print the bare command name" path, which is the CORRECT rendering
for it (the word "max" is exactly what should appear, just not in upright
font -- a purely cosmetic, non-content-loss gap not worth a special case).
"""
import re

NBSP = "\u00a0"

GREEK = {
    "omega": "ω", "Omega": "Ω", "phi": "φ", "Phi": "Φ", "pi": "π",
    "mu": "μ", "nu": "ν", "theta": "θ", "varepsilon": "ε", "epsilon": "ε",
    "Delta": "Δ", "delta": "δ", "lambda": "λ",
    "gamma": "γ", "Gamma": "Γ", "sigma": "σ", "Sigma": "Σ",
}

NOARG_SYMBOL = {
    "circ": "°", "times": NBSP + "×" + NBSP, "cdot": NBSP + "·" + NBSP,
    "therefore": "∴", "because": "∵", "prime": "&prime;", "quad": NBSP + NBSP,
    "AA": "Å",
    # Added for physics-12-9 -- see module docstring: this chapter's
    # derivations lean on these as their primary step-to-step connectives
    # far more than any prior chapter did, and none were in the inherited
    # table (a real, chapter-content-dependent gap, not a hypothetical one).
    "Rightarrow": NBSP + "⇒" + NBSP, "rightarrow": NBSP + "→" + NBSP,
    "infty": "∞", "approx": NBSP + "≈" + NBSP,
    "geq": NBSP + "≥" + NBSP, "leq": NBSP + "≤" + NBSP,
}
# Italicized, not upright - two independent reasons. (1) Standard math
# typesetting convention: a Greek letter standing for a physical quantity
# (an angle theta, a wavelength lambda) is set in italic, same as a Latin
# variable, while an upright Greek letter is reserved for a unit/operator
# use this chapter never has. (2) A real legibility bug caught for real on
# this chapter: at this page's actual rendered size (font-size ~17.5px
# inside a container zoomed to 0.63, i.e. an effective ~11px), upright
# theta's (θ) thin horizontal crossbar anti-aliases away almost
# completely in every font tested (the declared Noto Serif Devanagari /
# STIX Two Text stack, and also Times New Roman / Cambria Math / Segoe UI
# Symbol / DejaVu Serif / Liberation Serif as fallback probes) - confirmed
# with a Playwright screenshot at 1x device scale and pixel-level zoom:
# "cos^2θ" rendered as "cos^20", theta visually identical to the digit
# 0, not merely similar. The same crossbar survives clearly at a normal
# reading size or a high device-pixel-ratio screenshot (4x), which is what
# made this easy to miss on a quick look - it only collapses at this
# page's own actual effective font size. None of this chapter's other
# Greek letters (λ/μ/π/φ, all checked against the same
# rendered page) have a same-shape collision with a digit, so this could
# have been fixed for theta alone - italicizing the whole GREEK table
# instead is both the typographically correct choice and a defensive
# safety net if a future chapter reuses this table with a Greek letter
# that turns out to have the same problem at this size.
NOARG_SYMBOL.update({k: f"<i>{v}</i>" for k, v in GREEK.items()})


# ============================================================
# Step 1: protect \begin{env}...\end{env} blocks as opaque placeholders so
# the division-rewrite pass (and its depth/boundary tracking) never has to
# reason about them; each row's own content still goes through the full
# convert() pipeline (division-rewrite included) independently, inside
# _render_env below.
# ============================================================

_ENV_TOKEN = "\u27ea{}\u27eb"  # ⟪N⟫ - absent from this chapter's real content


def _protect_envs(s):
    stash = []

    def repl(m):
        stash.append((m.group("env"), m.group("body")))
        return _ENV_TOKEN.format(len(stash) - 1)

    pattern = re.compile(r"\\begin\{(?P<env>[a-zA-Z]+)\}(?P<body>.*?)\\end\{(?P=env)\}", re.S)
    while True:
        new_s = pattern.sub(repl, s, count=1)
        if new_s == s:
            break
        s = new_s
    return s, stash


_ENV_TOKEN_RE = re.compile(r"\u27ea(\d+)\u27eb")


# ============================================================
# Division rewrite: bare "/" -> \frac{a}{b}, except a unit-division
# (between/inside \mathrm{...}/\text{...}) and except a "\times 10^" glue.
# ============================================================

def _is_unit_division(s, slash_pos):
    before = s[:slash_pos].rstrip()
    after = s[slash_pos + 1:].lstrip()
    before_is_unit = bool(re.search(r"\\(?:mathrm|text|mbox|operatorname)\s*\{[^{}]*\}\s*$", before))
    after_is_unit = bool(re.match(r"^\\(?:mathrm|text|mbox|operatorname)\s*\{", after))
    return before_is_unit and after_is_unit


def _rewrite_divisions(s):
    s, envs = _protect_envs(s)
    s = _rewrite_left_right(s)
    s = _rewrite_bare_parens(s)
    s = _rewrite_flat_slashes(s)
    return s, envs


def _rewrite_left_right(s):
    out = []
    i, n = 0, len(s)
    while i < n:
        if s.startswith("\\left(", i):
            depth = 1
            j = i + 6
            while j < n and depth > 0:
                if s.startswith("\\left(", j):
                    depth += 1
                    j += 6
                    continue
                if s.startswith("\\right)", j):
                    depth -= 1
                    j += 7
                    continue
                j += 1
            inner = s[i + 6:j - 7]
            out.append("\\left(" + _rewrite_flat_slashes(_rewrite_bare_parens(inner)) + "\\right)")
            i = j
            continue
        out.append(s[i])
        i += 1
    return "".join(out)


def _rewrite_bare_parens(text):
    """A paren that wraps exactly one clean top-level division becomes the
    fraction directly (parens dropped)."""
    result = []
    i, n = 0, len(text)
    while i < n:
        c = text[i]
        if c == "(" and text[max(0, i - 5):i] != "\\left":
            depth = 1
            j = i + 1
            slash_positions = []
            bad = False
            while j < n and depth > 0:
                if text[j] == "(":
                    depth += 1
                elif text[j] == ")":
                    depth -= 1
                    if depth == 0:
                        break
                elif text[j] == "/" and depth == 1:
                    slash_positions.append(j)
                elif text.startswith("\\right", j):
                    bad = True
                j += 1
            content = text[i + 1:j]
            if not bad and len(slash_positions) == 1 and "\\begin" not in content and _ENV_TOKEN_RE.search(content) is None:
                rel = slash_positions[0] - (i + 1)
                num, den = content[:rel], content[rel + 1:]
                if num.strip() and den.strip() and not _is_unit_division(text, i + 1 + rel):
                    result.append("\\frac{" + num.strip() + "}{" + den.strip() + "}")
                    i = j + 1
                    continue
            result.append(c)
            i += 1
            continue
        result.append(c)
        i += 1
    return "".join(result)


def _rewrite_flat_slashes(s):
    def depth_at(text, pos):
        d = 0
        for ch in text[:pos]:
            if ch in "{(":
                d += 1
            elif ch in "})":
                d -= 1
        return d

    def boundaries(text):
        bounds = [0, len(text)]
        depth = 0
        i, n = 0, len(text)
        while i < n:
            c = text[i]
            if c in "{(":
                depth += 1
                i += 1
                continue
            if c in "})":
                depth -= 1
                i += 1
                continue
            if depth == 0:
                if c == "=":
                    bounds += [i, i + 1]
                    i += 1
                    continue
                if text.startswith("\\times", i):
                    if not re.match(r"\\times\s*10\^", text[i:]):
                        bounds += [i, i + 6]
                    i += 6
                    continue
                if c == "×":
                    if not re.match(r"×\s*10\^", text[i:]):
                        bounds += [i, i + 1]
                    i += 1
                    continue
            i += 1
        return sorted(set(bounds))

    result = []
    pos = 0
    i, n = 0, len(s)
    while i < n:
        c = s[i]
        if c == "/" and depth_at(s, i) == 0 and not _is_unit_division(s, i):
            bounds = boundaries(s)
            lo = max(b for b in bounds if b <= i)
            hi = min(b for b in bounds if b >= i + 1)
            num = s[lo:i].strip()
            den = s[i + 1:hi].strip()
            if num and den and "\\begin" not in num and "\\begin" not in den:
                result.append(s[pos:lo])
                result.append("\\frac{" + num + "}{" + den + "}")
                pos = hi
                i = hi
                continue
        i += 1
    result.append(s[pos:])
    return "".join(result)


# ============================================================
# Core LaTeX -> HTML character-by-character converter
# ============================================================

def _html_escape(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def _find_matching_brace(s, start):
    depth = 0
    for i in range(start, len(s)):
        if s[i] == "{":
            depth += 1
        elif s[i] == "}":
            depth -= 1
            if depth == 0:
                return i
    return len(s) - 1


def _read_group(s, i, skip_ws=True):
    """Read a {...} group, or (if no brace) a single token, per LaTeX's
    'one token if no braces' rule. Skips whitespace before the group only
    (the space between a command and its argument), never after."""
    if skip_ws:
        while i < len(s) and s[i] == " ":
            i += 1
    if i < len(s) and s[i] == "{":
        j = _find_matching_brace(s, i)
        return s[i + 1:j], j + 1
    if i < len(s) and s[i] == "\\":
        m = re.match(r"\\[a-zA-Z]+", s[i:])
        if m:
            return m.group(0), i + len(m.group(0))
        return s[i:i + 2], i + 2
    if i < len(s):
        return s[i], i + 1
    return "", i


# Combining circumflex accent - placed after a single base letter (or the
# HTML span physics-12-7's \mathbf handler already produced for it) to
# render x̂/î/ĵ/k̂ without a bespoke absolutely-positioned span. Every
# \hat{...} in this chapter wraps exactly one letter (optionally itself
# wrapped in \mathbf), so appending the combining mark after the converted
# inner HTML is safe and reads correctly in every browser tested.
_COMBINING_CIRCUMFLEX = "\u0302"


def convert(latex_src, envs=None):
    """Convert one LaTeX span's inner content (without $.../$$...$$) to HTML."""
    rewritten, found_envs = _rewrite_divisions(latex_src)
    return _convert_inner(rewritten, found_envs)


def _convert_inner(s, envs=None):
    envs = envs or []
    out = []
    i, n = 0, len(s)
    while i < n:
        c = s[i]

        env_m = _ENV_TOKEN_RE.match(s, i)
        if env_m:
            idx = int(env_m.group(1))
            env_name, body = envs[idx]
            out.append(_render_env(env_name, body))
            i = env_m.end()
            continue

        if c == "\\":
            m = re.match(r"\\[a-zA-Z]+", s[i:])
            if not m:
                if s[i:i + 2] == "\\{":
                    out.append("{")
                    i += 2
                    continue
                if s[i:i + 2] == "\\}":
                    out.append("}")
                    i += 2
                    continue
                if s[i:i + 2] == "\\ ":
                    out.append(NBSP)
                    i += 2
                    continue
                if s[i:i + 2] == "\\,":
                    # LaTeX thin-space, used in this chapter to separate a
                    # unit's own factors (e.g. "m\,s^{-1}" for m s^-1) --
                    # falls through unhandled otherwise (the command regex
                    # below only matches \[a-zA-Z]+, never a bare comma) and
                    # the backslash was silently dropped, leaving a literal
                    # "," glued straight onto the unit with no space at all
                    # (caught for real: "m,s^-1" instead of "m s^-1").
                    # Non-breaking, same reasoning as "~", so the unit's two
                    # factors never split across a line either.
                    out.append(NBSP)
                    i += 2
                    continue
                if s[i:i + 2] == "\\\\":
                    out.append("<br>")
                    i += 2
                    continue
                i += 1
                continue
            cmd = m.group(0)[1:]
            i += len(m.group(0))

            if cmd in ("frac", "dfrac"):
                # physics-12-10 uses \dfrac (display-style fraction) 16 times
                # throughout - grepped from 08_tag/structured.hi.json per the
                # "grep before trusting a reused converter" discipline;
                # physics-12-9's own content never used \dfrac so this
                # converter (inherited unmodified from there) had no case
                # for it, which would have fallen through to the generic
                # "unknown command: print its bare name" path and rendered
                # the literal text "dfrac" on the page in place of every
                # such fraction. Renders identically to \frac - the only
                # difference in real LaTeX is display- vs text-style sizing,
                # which this hand-rendered .s31/.s32/.s33 stacked-fraction
                # markup doesn't distinguish anyway.
                num, i = _read_group(s, i)
                den, i = _read_group(s, i)
                out.append(_render_frac(num, den, envs))
                continue

            if cmd == "sqrt":
                idx_content = None
                j = i
                while j < n and s[j] == " ":
                    j += 1
                if j < n and s[j] == "[":
                    k = s.find("]", j)
                    idx_content = s[j + 1:k]
                    i = k + 1
                radicand, i = _read_group(s, i)
                out.append(_render_sqrt(radicand, idx_content, envs))
                continue

            if cmd == "hat":
                content, i = _read_group(s, i)
                inner_html = _convert_inner(content, envs)
                out.append(inner_html + _COMBINING_CIRCUMFLEX)
                continue

            if cmd in ("mathrm", "text", "mbox", "operatorname", "mathbf"):
                content, i = _read_group(s, i)
                inner_html = _convert_inner(content, envs)
                out.append(f"<b>{inner_html}</b>" if cmd == "mathbf" else inner_html)
                continue

            if cmd in ("left", "right"):
                if i < n:
                    if s[i] == "\\":
                        m2 = re.match(r"\\[a-zA-Z]+", s[i:])
                        if m2:
                            tok = m2.group(0)
                            i += len(tok)
                            if tok == "\\{":
                                out.append("{")
                            elif tok == "\\}":
                                out.append("}")
                            # \right. (no visible delimiter) -> nothing
                    elif s[i] == ".":
                        i += 1
                    else:
                        out.append(s[i])
                        i += 1
                continue

            if cmd in NOARG_SYMBOL:
                out.append(NOARG_SYMBOL[cmd])
                continue

            if cmd in ("sin", "cos", "tan", "log", "ln"):
                out.append(cmd)
                continue

            # unknown command: render its bare name, not silently blank
            out.append(cmd)
            continue

        if c == "^":
            i += 1
            content, i = _read_group(s, i)
            out.append(_render_sup(content, envs))
            continue

        if c == "_":
            i += 1
            content, i = _read_group(s, i)
            out.append(f"<sub>{_convert_inner(content, envs)}</sub>")
            continue

        if c == "~":
            out.append(NBSP)
            i += 1
            continue

        if c == "/":
            # any '/' surviving to here is (by construction of
            # _rewrite_divisions) a unit division (rad/s, m/s) that was
            # deliberately left un-fractioned - pad with non-breaking
            # spaces so the unit never splits across a line.
            out.append(NBSP + "/" + NBSP)
            i += 1
            continue

        if c == "=":
            out.append(NBSP + "=" + NBSP)
            i += 1
            continue

        if c in "{}":
            i += 1
            continue

        if c == "&":
            out.append(" ")
            i += 1
            continue

        out.append(_html_escape(c))
        i += 1

    html = "".join(out)
    return _collapse_ws_runs(html)


def _render_sup(content, envs):
    stripped = content.strip()
    if stripped in ("\\circ", "circ"):
        return "<sup>°</sup>"
    if re.fullmatch(r"\\mathrm\s*\{\s*o\s*\}", stripped) or stripped == "o":
        return "<sup>°</sup>"
    if stripped == "\\prime":
        return "<sup>&prime;</sup>"
    return f"<sup>{_convert_inner(content, envs)}</sup>"


def _render_frac(num, den, envs):
    num_html = _convert_inner(num, envs)
    den_html = _convert_inner(den, envs)
    return (f'<span class="s31"><span class="s32">{num_html}</span>'
            f'<span class="s33">{den_html}</span></span>')


def _render_sqrt(radicand, index, envs):
    inner = _convert_inner(radicand, envs)
    # border-top on an inline-block, NOT text-decoration:overline on a plain
    # inline span - caught for real on this chapter's q_10.5
    # ("2\sqrt{I_{1}I_{2}}", the interference-intensity cross term):
    # text-decoration:overline does not reliably span a single continuous
    # line across content whose internal boxes carry different
    # vertical-align (a <sub> shifts its own box down), so Chromium rendered
    # two short, separate overline fragments sitting only above the bare
    # "I" letters, with no line at all over either subscript or the gap
    # between them - "I_1 I_2" under one radical looked like two unrelated
    # square roots glued together, not one root over the whole product.
    # inherited unmodified from physics-12-8/12-9, whose own sqrt content
    # never happened to wrap more than one subscripted variable at a time,
    # so this was latent, not previously visible. border-top on a genuine
    # inline-block box is a box-level line, not a text run decoration, so it
    # spans the box's full width in one piece regardless of what
    # vertical-align its children use.
    radical = (f'&radic;<span style="display:inline-block; border-top:1px '
               f'solid currentColor; padding-top:1px;">{inner}</span>')
    if index:
        idx_html = _convert_inner(index, envs)
        radical = f'<sup>{idx_html}</sup>{radical}'
    return f'<span class="s90">{radical}</span>'


def _render_env(env, body):
    body = re.sub(r"^\s*\{[^{}]*\}", "", body) if env == "array" else body
    rows = re.split(r"\\\\", body)
    row_htmls = []
    for row in rows:
        row = row.strip().replace("&", " ")
        if not row:
            continue
        row_htmls.append(f'<span class="s93">{convert(row)}</span>')
    return f'<div class="s92 s60">{"".join(row_htmls)}</div>'


def _collapse_ws_runs(html):
    html = re.sub(r"(?:\u00a0| ){2,}", NBSP, html)
    html = re.sub(r"^(?:\u00a0)+", "", html)
    return html


# ============================================================
# Glue "=" to a following \frac/\sqrt result, chained through repeats.
#
# A regex built on "lazily consume characters until the first literal
# '</span></span>'" (the original, physics-12-7-inherited approach) is
# depth-blind: it stops at the FIRST double-close it finds, even when
# that's actually the end of a span NESTED inside the fraction (e.g. a
# \sqrt's own .s31/.s90 closing INSIDE a \frac numerator/denominator),
# not the outer .s31/.s90 span itself. Caught for real on this chapter:
# q_8.2(c)'s B = \frac{...\sqrt{2}...}{...} has exactly this shape (a
# \sqrt nested inside a \frac's numerator) - the naive regex truncated
# the numerator's own .s32 span right after the nested sqrt's closing
# tags, stranding "\u00d7 6.9 \u00d7 10^{-6}" outside .s32 (still inside .s31,
# before .s33) and leaving one stray unmatched </span> - garbled,
# visibly broken markup, not merely a missed glue. physics-12-7 never
# exercised this because none of ITS own fractions happened to nest a
# sqrt inside a frac's numerator/denominator at the same time as a
# leading "=" glue trigger. Fixed with a proper depth-aware span-end
# scanner instead of a fixed-lookahead regex.
# ============================================================

_SPAN_OPEN_RE = re.compile(r"<span\b")


def _span_end(html, start):
    """`start` must point at the '<' of an opening '<span ...>' tag.
    Returns the index just past its matching '</span>', correctly
    accounting for any spans nested inside it (to any depth)."""
    tag_end = html.index(">", start) + 1
    depth = 1
    i = tag_end
    close_tag = "</span>"
    while depth > 0:
        next_open = _SPAN_OPEN_RE.search(html, i)
        next_close = html.find(close_tag, i)
        if next_close == -1:
            return len(html)  # malformed input - bail out safely
        if next_open and next_open.start() < next_close:
            depth += 1
            i = html.index(">", next_open.start()) + 1
        else:
            depth -= 1
            i = next_close + len(close_tag)
    return i


def glue_equals_to_frac(html):
    NBSP_EQ = "\u00a0=\u00a0"
    out = []
    i, n = 0, len(html)
    while i < n:
        start = i
        j = i
        matched_once = False
        while True:
            advanced = False
            if html.startswith(NBSP_EQ, j) and (
                html.startswith('<span class="s31"', j + len(NBSP_EQ))
                or html.startswith('<span class="s90"', j + len(NBSP_EQ))
            ):
                j = _span_end(html, j + len(NBSP_EQ))
                matched_once = True
                advanced = True
            elif j == start and (
                html.startswith('<span class="s31"', j) or html.startswith('<span class="s90"', j)
            ):
                # a bare frac/sqrt with no leading "=" - only valid as the
                # very first element of a chain (mirrors the original
                # regex's second alternative, e.g. "\sqrt{a} = b" chains).
                j = _span_end(html, j)
                matched_once = True
                advanced = True
            if not advanced:
                break
        if matched_once and j > start:
            out.append(f'<span class="s90">{html[start:j]}</span>')
            i = j
        else:
            out.append(html[i])
            i += 1
    return "".join(out)


def text_to_lines(text):
    """Split plain text into one line per sentence - Devanagari '।' is
    unambiguous; ASCII '.' guarded against a preceding/following digit."""
    text = text.strip()
    if not text:
        return []
    paras = re.split(r"\n\s*\n|\n", text)
    lines = []
    for para in paras:
        para = para.strip()
        if not para:
            continue
        buf, start = [], 0
        n = len(para)
        i = 0
        while i < n:
            ch = para[i]
            if ch == "।":
                buf.append(para[start:i + 1].strip())
                start = i + 1
            elif ch == ".":
                prev_digit = i > 0 and para[i - 1].isdigit()
                next_digit = i + 1 < n and para[i + 1].isdigit()
                # An ellipsis ("..." used as this manual's own equation-
                # numbering marker, e.g. "... (1)") is a run of periods, not
                # a sentence end -- guard against splitting mid-run (which
                # otherwise produces a string of stray one-character "."
                # lines, caught for real on q_9.31's "...(1)" reference).
                prev_dot = i > 0 and para[i - 1] == "."
                next_dot = i + 1 < n and para[i + 1] == "."
                if not (prev_digit and next_digit) and not (prev_dot or next_dot):
                    buf.append(para[start:i + 1].strip())
                    start = i + 1
            i += 1
        rest = para[start:].strip()
        if rest:
            buf.append(rest)
        lines.extend(b for b in buf if b)
    return lines


def parse_markdown_table(md_text):
    """Parse a simple pipe-table (header row, ':---' separator, data rows)
    into (header_cells, [row_cells, ...]) - each cell still raw (un-rendered
    $...$ math). Wrap exactly as given: same rows/columns/cell text, no
    reformatting, per step_7/format.md's ':::table adds a wrapper; it does
    not reformat.'"""
    lines = [l.strip() for l in md_text.strip().splitlines() if l.strip()]
    rows = []
    for line in lines:
        if re.fullmatch(r"\|?\s*:?-+:?\s*(\|\s*:?-+:?\s*)+\|?", line):
            continue  # alignment separator row
        cells = [c.strip() for c in line.strip("|").split("|")]
        rows.append(cells)
    if not rows:
        return [], []
    return rows[0], rows[1:]
