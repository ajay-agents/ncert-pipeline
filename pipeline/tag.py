"""Container-markdown parser: `:::name{attr="value"}...:::` -> a tree of
nested nodes, leaves are raw markdown strings.

This used to also render that tree straight to HTML (a fixed-code fallback
for stage 8, driven by css/component_map.json). That path is gone - stage 8
is hand-designed only now, matching solutions-chapter-1.html/.css. `_parse()`
stays because `pipeline/mdio.py` depends on it for every stage's markdown ->
Chapter/Item read direction, not just stage 8's.
"""
from __future__ import annotations

import re

OPEN_RE = re.compile(r"^:::(?P<name>[a-z][a-z0-9_-]*)\s*(?P<attrs>\{.*\})?\s*$")
CLOSE_RE = re.compile(r"^:::\s*$")
ATTR_RE = re.compile(r'(\w+)="([^"]*)"')


class TagError(RuntimeError):
    pass


def _parse(lines: list[str]):
    """Build a nested tree of container nodes; leaves are raw markdown strings."""
    root = {"name": "_root", "attrs": {}, "children": []}
    stack = [root]
    buf: list[str] = []

    def flush():
        if buf and "".join(buf).strip():
            stack[-1]["children"].append("\n".join(buf))
        buf.clear()

    for lineno, line in enumerate(lines, 1):
        m = OPEN_RE.match(line)
        if m:
            flush()
            node = {"name": m.group("name"),
                    "attrs": dict(ATTR_RE.findall(m.group("attrs") or "")),
                    "children": [], "line": lineno}
            stack[-1]["children"].append(node)
            stack.append(node)
            continue
        if CLOSE_RE.match(line):
            flush()
            if len(stack) == 1:
                raise TagError(f"line {lineno}: ':::' closes nothing")
            stack.pop()
            continue
        buf.append(line)

    flush()
    if len(stack) > 1:
        unclosed = ", ".join(f"{n['name']}@{n['line']}" for n in stack[1:])
        raise TagError(f"unclosed containers: {unclosed}")
    return root
