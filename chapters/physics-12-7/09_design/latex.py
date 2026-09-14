# -*- coding: utf-8 -*-
"""LaTeX -> hand-rendered HTML converter for physics-12-7's stage 9 page.
Modeled on the conventions documented in step_9/PROMPT.md and observed in
chapters/physics-12-6/09_design/final.hi.html (fractions as .s31/.s32/.s33,
sqrt as &radic;+overline span, multi-row aligned blocks as .s92/.s93, "="
glued to a following frac/sqrt via .s90, non-breaking spaces around ~/×/·/=,
degree signs as <sup>°</sup>).

This chapter's own LaTeX vocabulary (grepped from 08_tag/structured.hi.json):
\\Omega \\because \\begin{aligned} \\cdot \\circ \\cos \\frac \\left \\right
\\mathbf \\mathrm \\mu \\nu \\omega \\phi \\pi \\prime \\quad \\sqrt \\tan
\\text \\therefore \\times - no set-theory/sum/oint/langle, only one begin
environment (aligned). Not a generic all-subjects converter - built for what
this chapter actually uses, per the documented "grep before trusting a
reused converter" lesson.
"""
import re

NBSP = "\u00a0"

GREEK = {
    "omega": "ω", "Omega": "Ω", "phi": "φ", "Phi": "Φ", "pi": "π",
    "mu": "μ", "nu": "ν", "theta": "θ", "varepsilon": "ε", "epsilon": "ε",
    "Delta": "Δ", "delta": "δ", "lambda": "λ",
}

NOARG_SYMBOL = {
    "circ": "°", "times": NBSP + "×" + NBSP, "cdot": NBSP + "·" + NBSP,
    "therefore": "∴", "because": "∵", "prime": "&prime;", "quad": NBSP + NBSP,
}
NOARG_SYMBOL.update({k: v for k, v in GREEK.items()})


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
    # restore env placeholders (their own rows are converted independently
    # later, inside _render_env - at this stage we just need the token
    # back in place so _convert_inner's \begin handler never actually
    # sees it; instead we hand the raw env body forward via a side table)
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
                if s[i:i + 2] == "\\\\":
                    out.append("<br>")
                    i += 2
                    continue
                i += 1
                continue
            cmd = m.group(0)[1:]
            i += len(m.group(0))

            if cmd == "frac":
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
    radical = (f'&radic;<span style="text-decoration:overline; '
               f'text-decoration-thickness:1px;">{inner}</span>')
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
# ============================================================

_GLUE_RE = re.compile(
    r'(?:\u00a0=\u00a0(?:<span class="s31">(?:(?!</span></span>).)*?</span></span>'
    r'|<span class="s90">&radic;(?:(?!</span></span>).)*?</span></span>))+',
    re.S,
)


def glue_equals_to_frac(html):
    return _GLUE_RE.sub(lambda m: f'<span class="s90">{m.group(0)}</span>', html)


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
                if not (prev_digit and next_digit):
                    buf.append(para[start:i + 1].strip())
                    start = i + 1
            i += 1
        rest = para[start:].strip()
        if rest:
            buf.append(rest)
        lines.extend(b for b in buf if b)
    return lines
