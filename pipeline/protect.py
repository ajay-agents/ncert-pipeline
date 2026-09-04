"""Mask everything a language model must not rewrite, then put it back verbatim.

Used before stages 5 and 6. If a single token fails to come back, the stage
fails loudly instead of shipping a mangled equation.
"""
from __future__ import annotations

import re

OPEN, CLOSE = "\u27e6", "\u27e7"   # ⟦ ⟧ — absent from NCERT text and from Devanagari

# Order matters: longest / outermost constructs first.
PATTERNS: list[tuple[str, re.Pattern]] = [
    ("D", re.compile(r"\$\$.+?\$\$", re.S)),                    # display math
    ("C", re.compile(r"\\ce\{(?:[^{}]|\{[^{}]*\})*\}")),        # mhchem
    ("T", re.compile(r"(?:^[ \t]*\|.*\|[ \t]*$\n?)+", re.M)),   # markdown table
    ("I", re.compile(r"!\[[^\]]*\]\([^)]*\)")),                 # image
    ("M", re.compile(r"(?<!\$)\$(?!\$)[^$\n]+?\$(?!\$)")),      # inline math
    ("U", re.compile(r"\b\d+(?:\.\d+)?\s*(?:×\s*10\^?-?\d+\s*)?"
                     r"(?:m/s|km/h|N|J|W|Pa|kg|g|mol|L|mL|cm|mm|km|m|s|K|°C|eV|Hz|Ω|V|A|C)\b")),
]


class ProtectionError(RuntimeError):
    pass


def freeze(text: str) -> tuple[str, dict[str, str]]:
    """Replace protected spans with ⟦K0⟧ tokens. Returns (masked_text, mapping)."""
    mapping: dict[str, str] = {}
    counter = {k: 0 for k, _ in PATTERNS}

    for kind, pattern in PATTERNS:
        def _sub(m: re.Match) -> str:
            tok = f"{OPEN}{kind}{counter[kind]}{CLOSE}"
            counter[kind] += 1
            mapping[tok] = m.group(0)
            return tok
        text = pattern.sub(_sub, text)

    return text, mapping


def restore(text: str, mapping: dict[str, str]) -> str:
    """Put every span back. Raises if the model dropped or duplicated a token."""
    missing = [t for t in mapping if text.count(t) != 1]
    if missing:
        raise ProtectionError(
            f"{len(missing)} protected token(s) lost or duplicated: {missing[:5]}"
        )
    for tok, original in mapping.items():
        text = text.replace(tok, original)
    stray = re.findall(rf"{OPEN}[A-Z]\d+{CLOSE}?", text)
    if stray:
        raise ProtectionError(f"invented tokens in model output: {stray[:5]}")
    return text


def parity(before: str, after: str) -> list[str]:
    """Cheap structural diff used by gates.py when freezing is not in play."""
    problems = []
    for name, pattern in [("display math", PATTERNS[0][1]),
                          ("inline math", PATTERNS[4][1]),
                          ("tables", PATTERNS[2][1]),
                          ("images", PATTERNS[3][1])]:
        a, b = len(pattern.findall(before)), len(pattern.findall(after))
        if a != b:
            problems.append(f"{name}: {a} -> {b}")
    return problems
