# -*- coding: utf-8 -*-
"""LaTeX -> hand-rendered HTML converter for physics-12-13's stage 9 page.
Copied from chapters/physics-12-12/09_design/latex.py (the most recently
proven and complete of this pipeline's stage-9 scripts) - fractions as
.s31/.s32/.s33, sqrt as &radic;+overline span, multi-row aligned/array/
gathered blocks as .s92/.s93, "=" glued to a following frac/sqrt via .s90,
non-breaking spaces around ~/x/./=, degree signs as <sup>&deg;</sup>.

This chapter's own LaTeX vocabulary (grepped from 07_format/
structured.hi.md, per the documented "grep before trusting a reused
converter" discipline - Nuclei is binding-energy/mass-defect/Q-value
arithmetic, one nuclear-reaction equation, one radius-ratio proportionality):
\\Delta \\approx \\because \\begin \\cdot \\end \\frac \\left \\longrightarrow
\\mathrm \\pi \\propto \\right \\rightarrow \\text \\therefore \\times
\\varepsilon, plus \\begin{aligned} (no \\array/\\gathered/\\cases this time).

Three real gaps found and fixed here, none inherited unmodified from
physics-12-12 (whose own Atoms content never happened to need them):

1. \\longrightarrow (q_13.6's decay/fission equation "{ }_{26}^{56}\\mathrm{Fe}
   \\longrightarrow 2{ }_{13}^{28}\\mathrm{Al}") and \\propto (q_13.4's
   "R \\propto A^{1/3}") were both missing from the inherited NOARG_SYMBOL
   table and would have fallen through to the generic "unknown command:
   print its bare name" path, rendering the literal words "longrightarrow"/
   "propto" instead of an arrow/proportionality sign.

2. \\mathrm{MeV} / c^{2} (ex_13.3's mass-energy-equivalence unit, used four
   times in that one item plus once more in its own answer) is a genuine
   UNIT expression (a compound unit "MeV per c-squared", conventionally
   written compact and inline, never as a stacked value/value fraction) -
   but the inherited _is_unit_division() only recognizes a unit slash when
   BOTH sides are wrapped in \\mathrm{...}/\\text{...}/etc; here the right
   side is a bare, un-wrapped "c^{2}" with no such wrapper at all. Without a
   fix this falls through to the ordinary division-rewrite path and turns
   "931.5 MeV/c^2" into a two-row stacked fraction, which reads as a value
   computation, not a unit - visually wrong for the same reason a stacked
   m/s^2 or N/C would be. Fixed by recognizing a bare single-letter symbol
   (optionally with its own exponent, e.g. "c^{2}") as a valid unit-like
   right side whenever the left side is already a real \\mathrm/\\text unit.

3. The flat-slash rewrite's own boundary search (in _rewrite_flat_slashes'
   inner boundaries()) only stops a numerator/denominator search at a
   depth-0 "=" or "\\times"/"x" - not at \\approx. q_13.4's own boxed answer
   echo, "$R_{\\text{स्वर्ण}}/R_{\\text{रजत}} \\approx 1.23$", has a genuine
   top-level division (R_gold/R_silver, correctly meant to become a stacked
   fraction, matching the exemplar's own display equation for the same
   ratio two lines above it) immediately followed by "\\approx 1.23" with no
   "=" or "\\times" in between anywhere in the whole span - so without a fix
   the denominator search runs all the way to the end of the string and
   swallows " \\approx 1.23" into the fraction's own denominator, producing
   a nonsensical "R_gold over (R_silver \\approx 1.23)". Fixed by adding
   \\approx as a third depth-0 boundary token, exactly like "=" and
   "\\times" already are.
"""
import re

NBSP = "\u00a0"

GREEK = {
    "omega": "ω", "Omega": "Ω", "phi": "φ", "Phi": "Φ", "pi": "π",
    "mu": "μ", "nu": "ν", "theta": "θ", "varepsilon": "ε", "epsilon": "ε",
    "Delta": "Δ", "delta": "δ", "lambda": "λ",
    "gamma": "γ", "Gamma": "Γ", "sigma": "σ", "Sigma": "Σ",
    "rho": "ρ", "varphi": "φ",
    "alpha": "α",
    # Added for physics-12-13 (Nuclei): \beta is standard nuclear-decay
    # vocabulary (beta decay/particle) - not present in this chapter's own
    # 14-item final content (confirmed by the grep in this module's
    # docstring - the actual items are binding-energy/mass-defect/Q-value
    # arithmetic, no explicit beta-decay numeric item made the final cut),
    # but added defensively since a future re-run of this same converter on
    # a chapter that does use it should not silently print the bare word
    # "beta" the way an unhandled command otherwise would.
    "beta": "β",
}

NOARG_SYMBOL = {
    "circ": "°", "times": NBSP + "×" + NBSP, "cdot": NBSP + "·" + NBSP,
    "therefore": "∴", "because": "∵", "prime": "&prime;", "quad": NBSP + NBSP,
    "AA": "Å",
    "Rightarrow": NBSP + "⇒" + NBSP, "rightarrow": NBSP + "→" + NBSP,
    "infty": "∞", "approx": NBSP + "≈" + NBSP,
    "geq": NBSP + "≥" + NBSP, "leq": NBSP + "≤" + NBSP,
    # Added for physics-12-13 - see module docstring point 1: q_13.6's own
    # nuclear-decay equation ("Fe \longrightarrow 2 Al") and q_13.4's radius
    # proportionality ("R \propto A^{1/3}") both use commands missing from
    # every prior chapter's inherited table (neither Atoms nor any earlier
    # chapter's own content happened to need an equation-arrow or a
    # proportionality sign). \longrightarrow reuses the same glyph as
    # \rightarrow (the visual distinction between the two LaTeX commands is
    # spacing, not shape, and this page hand-renders both as one fixed-width
    # arrow character either way).
    "longrightarrow": NBSP + "→" + NBSP,
    "propto": NBSP + "∝" + NBSP,
    # Added for physics-12-14 (Semiconductor Electronics): \sim ("of order" /
    # "approximately", e.g. "$n_i \sim 10^{16}$", "$\sim 4.5\times10^9$") is
    # genuinely used repeatedly in this chapter's own content (grepped and
    # diffed against this table before writing the render script, per the
    # established discipline - a Physics chapter's own test content doesn't
    # automatically exercise every command a later Physics chapter needs).
    # No prior chapter's own content happened to need it, so it was missing
    # here; without this, \sim would silently degrade to a bare space via the
    # unhandled-command fallback, dropping a real "approximately" marker with
    # no error. Rendered the same way \approx is - a tilde operator (distinct
    # glyph from \approx's "≈", per standard math typesetting) with
    # non-breaking spaces on both sides, same reasoning as \approx's own.
    "sim": NBSP + "∼" + NBSP,
}
# Italicized, not upright - two independent reasons (standard math-typesetting
# convention for a Greek letter standing for a physical quantity, and a real
# legibility bug at this page's actual rendered size where upright theta's
# thin crossbar anti-aliases away and reads as the digit 0 - see
# physics-12-11/12-12's own latex.py for the full caught-for-real writeup).
NOARG_SYMBOL.update({k: f"<i>{v}</i>" for k, v in GREEK.items()})


# ============================================================
# Step 1: protect \begin{env}...\end{env} blocks as opaque placeholders so
# the division-rewrite pass (and its depth/boundary tracking) never has to
# reason about them; each row's own content still goes through the full
# convert() pipeline (division-rewrite included) independently, inside
# _render_env below.
# ============================================================

_ENV_TOKEN = "\u27ea{}\u27eb"  # ⟪N⟫ - absent from this chapter's real content


_ENV_TOKEN_SCAN_RE = re.compile(r"\\(begin|end)\{([a-zA-Z]+)\}")


def _protect_envs(s):
    """Find every TOP-LEVEL \\begin{env}...\\end{env} block and replace it
    with an opaque placeholder token, by depth all the way through (not by a
    same-name backreference regex - see physics-12-12's own latex.py for the
    caught-for-real nested-same-name-environment bug this guards against;
    this chapter's own content never nests an aligned inside another aligned,
    but the depth-based scan costs nothing extra and stays correct either
    way)."""
    stash = []
    out = []
    pos = 0
    depth = 0
    top_start = None
    top_name = None
    top_body_start = None

    for m in _ENV_TOKEN_SCAN_RE.finditer(s):
        kind, name = m.group(1), m.group(2)
        if kind == "begin":
            if depth == 0:
                top_start = m.start()
                top_name = name
                top_body_start = m.end()
            depth += 1
        else:
            if depth == 0:
                continue
            depth -= 1
            if depth == 0:
                body = s[top_body_start:m.start()]
                out.append(s[pos:top_start])
                stash.append((top_name, body))
                out.append(_ENV_TOKEN.format(len(stash) - 1))
                pos = m.end()
                top_start = None

    out.append(s[pos:])
    return "".join(out), stash


_ENV_TOKEN_RE = re.compile(r"\u27ea(\d+)\u27eb")


# ============================================================
# Division rewrite: bare "/" -> \frac{a}{b}, except a unit-division
# (between/inside \mathrm{...}/\text{...}, or a bare unit symbol like c^2 on
# one side - see module docstring point 2) and except a "\times 10^" glue.
# ============================================================

_BARE_UNIT_SYMBOL_RE = re.compile(
    r"^[a-zA-Z](?:\^\s*\{[^{}]*\}|\^\s*[0-9])?\s*$"
)


def _is_unit_division(s, slash_pos):
    before = s[:slash_pos].rstrip()
    after = s[slash_pos + 1:].lstrip()
    before_is_unit = bool(re.search(r"\\(?:mathrm|text|mbox|operatorname)\s*\{[^{}]*\}\s*$", before))
    after_is_unit = bool(re.match(r"^\\(?:mathrm|text|mbox|operatorname)\s*\{", after))
    if before_is_unit and after_is_unit:
        return True
    # A bare bare-letter symbol (optionally with its own exponent, e.g.
    # "c^{2}") on the right, with a real wrapped unit on the left, is also a
    # unit expression (physics-12-13's own "\mathrm{MeV} / c^{2}") - not a
    # value/value computation - and should stay compact/inline, never become
    # a stacked fraction. Only fires when the left side is already a
    # confirmed unit wrapper, so an ordinary "x / y" variable division is
    # never mistaken for this.
    if before_is_unit and _BARE_UNIT_SYMBOL_RE.match(after):
        return True
    return False


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
                # Added for physics-12-13 - see module docstring point 3:
                # \approx must also be a hard boundary, or a denominator
                # search with no "=" / "\times" anywhere after the slash
                # (q_13.4's "R_gold/R_silver \approx 1.23") runs all the way
                # to the end of the string and swallows the comparison
                # clause into the fraction's own denominator.
                if text.startswith("\\approx", i):
                    bounds += [i, i + 7]
                    i += 7
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
                if s[i:i + 2] == "\\_":
                    out.append("_")
                    i += 2
                    continue
                if s[i:i + 2] == "\\,":
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
    radical = (f'&radic;<span style="display:inline-block; border-top:1px '
               f'solid currentColor; padding-top:1px;">{inner}</span>')
    if index:
        idx_html = _convert_inner(index, envs)
        radical = f'<sup>{idx_html}</sup>{radical}'
    return f'<span class="s90">{radical}</span>'


def _render_env(env, body):
    body = re.sub(r"^\s*\{[^{}]*\}", "", body) if env == "array" else body
    protected_body, nested_envs = _protect_envs(body)
    rows = re.split(r"\\\\", protected_body)
    row_htmls = []
    for row in rows:
        row = row.strip().replace("&", " ")
        if not row:
            continue
        rewritten, _ = _rewrite_divisions(row)
        row_htmls.append(f'<span class="s93">{_convert_inner(rewritten, nested_envs)}</span>')
    return f'<div class="s92 s60">{"".join(row_htmls)}</div>'


def _collapse_ws_runs(html):
    html = re.sub(r"(?:\u00a0| ){2,}", NBSP, html)
    html = re.sub(r"^(?:\u00a0)+", "", html)
    return html


# ============================================================
# Glue "=" to a following \frac/\sqrt result, chained through repeats.
# ============================================================

_SPAN_OPEN_RE = re.compile(r"<span\b")


def _span_end(html, start):
    tag_end = html.index(">", start) + 1
    depth = 1
    i = tag_end
    close_tag = "</span>"
    while depth > 0:
        next_open = _SPAN_OPEN_RE.search(html, i)
        next_close = html.find(close_tag, i)
        if next_close == -1:
            return len(html)
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
    """Not exercised by this chapter (no :::table anywhere) - kept for parity
    with the reference script."""
    lines = [l.strip() for l in md_text.strip().splitlines() if l.strip()]
    rows = []
    for line in lines:
        if re.fullmatch(r"\|?\s*:?-+:?\s*(\|\s*:?-+:?\s*)+\|?", line):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        rows.append(cells)
    if not rows:
        return [], []
    return rows[0], rows[1:]
