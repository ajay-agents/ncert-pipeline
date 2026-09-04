Stage 8 — tag each solution's structure and serialize to JSON.

Build `chapters/$ARGUMENTS/08_tag/structured.<lang>.json`.

Before starting: check `manifest.unchanged_since(chapters/$ARGUMENTS/, "tag",
structured_md_path)`. If true, stop and report.

This stage exists to do the last piece of *judgment* work — deciding how
each worked solution's blocks map onto the house style's fixed structure —
somewhere it can be checked mechanically, before stage 9's hand-design pass
has to make the same calls with no code gate at all. Get this stage right
and stage 9 becomes close to pure templating; get it wrong and every bug
resurfaces one stage later where nothing catches it automatically.

## What to serialize

Parse `07_format/structured.<lang>.md`'s container tree (`tag._parse`) and
walk it into one JSON object per language:

```json
{
  "front": {"title": "...", "chapter": "1"},
  "items": [
    {
      "id": "ex_1.1", "kind": "example", "number": "1.1", "topic": "...",
      "prompt": [{"type": "text", "text": "..."}, {"type": "figure", "src": "images/fig_1_5.jpg", "caption": "..."}],
      "figures": [{"src": "images/fig_1_5.jpg", "caption": "..."}],
      "parts": [
        {"label": "a", "prompt": [...], "solution_blocks": [...], "answer": [...] }
      ],
      "solution_blocks": [
        {"type": "step", "stage": "given", "flow": [{"type": "text", "text": "..."}]},
        {"type": "note", "note_type": "caution", "label": "सावधानी", "flow": [...]},
        {"type": "concept", "stage": "given", "label": "जानकारी", "flow": [...]},
        {"type": "formula", "stage": "key_formula", "label": "मुख्य सूत्र", "flow": [...]},
        {"type": "figure", "src": "...", "caption": "..."},
        {"type": "table", "html": "..."}
      ],
      "answer": [{"type": "text", "text": "..."}]
    }
  ]
}
```

Every text-bearing field (`prompt`, `answer`, a block's `flow`) is an
**ordered list of `{type: "text", text}` / `{type: "figure", src,
caption}` segments**, never a flat string — a figure nested inside a
`:::step` (not a direct `:::solution` child) must still show up in the
flow, in the right position. Parsing only the container's direct text
children and ignoring nested containers silently drops such a figure; this
happened for real this session and is exactly what the gate below exists
to catch.

## The given → key-formula → substitute → conclusion judgment

This is the one genuinely model-judgment part of this stage:

- An explicit `:::concept` block is always `"stage": "given"`; an explicit
  `:::formula` block is always `"stage": "key_formula"` — regardless of
  position.
- Use the block's own `label` attribute as-is when stage 7 already set it
  to the fixed vocabulary (`_shared/RULES.md`'s container-vocabulary
  section) — that's the authoritative call, already made upstream; don't
  re-derive it.
- For a plain `:::step` (or bare text) that stage 7 left unlabelled, infer
  `stage` from its position among the solution's other stageable blocks
  (excluding `:::note`/`:::figure`/`:::table`, which never carry a stage):
  the first is `"given"`, the last is `"conclusion"`, anything in between
  is `"substitute"`; a solution with only one stageable block is entirely
  `"conclusion"`.
- Merge consecutive blocks that land on the same stage into one logical
  group in your own working notes if it helps, but keep each source block
  as its own JSON entry — stage 9 does the visual merging, this stage just
  needs every block's `stage` set correctly.
- Do this same inference **independently per part** for a multi-part item
  — a part's own solution_blocks get their own given/conclusion endpoints,
  not the item's.

## Noise to strip while you're in here

- A leading "हल" / "हल:" / "हल :" (with or without a colon, with or
  without a following space) at the very start of a solution's first
  block — the textbook's own "Solution:" opener, redundant with this
  page's own presentation. Also strip the rarer case where it's embedded
  as `\text{हल :}` inside a LaTeX aligned row. Strip only the very first
  occurrence in a solution's flow, not the word "हल" anywhere else.
- A `:::note` with an empty `label` gets a sensible default for its
  `type` instead of an empty pill: `"caution"` → `"सावधानी"`, `"recall"` →
  `"याद रखें"`, `"tip"` → `"सुझाव"` (or the English equivalents for an
  English-language chapter).

## The known duplicate-solution artifact

Stage 7 may have flagged a multi-part item whose source carries a second,
whole-item solution after the labelled parts that just re-narrates the
same working (sometimes with OCR-degraded numbers that don't match the
correct per-part version). When `parts` is non-empty for an item, do
**not** also populate that item's own `solution_blocks` from this
duplicate — leave the item-level `solution_blocks` empty and let the
per-part `solution_blocks`/`answer` carry the content. The item's own
top-level `answer` (a combined summary across parts, when the source has
one) is still real and should be kept.

## Figure paths

Keep `src` in the form it already has in `structured.<lang>.md`
(`images/fig_1_5.jpg`, not a bare `fig_1_5.jpg`) — this is the path stage 9
will use verbatim as an `<img src>` relative to its own output file,
alongside the `images/` folder that already sits next to it. Stripping to
a bare filename here breaks every image at render time in a way that
isn't visible until someone actually opens the finished page — it slipped
through a whole verification pass this session before being caught.

## Gate

Re-parse the JSON you just wrote and compare, against a **fresh, direct**
count from `structured.<lang>.md` (not against numbers you already had in
memory while writing the JSON):
- item count (examples + exercises)
- part count (summed across all items)
- distinct figure `src` count (both formal `:::figure{}` containers and
  any inline image reference embedded in a solution's raw text)

Any mismatch is a hard stop — something was dropped or duplicated during
serialization; find it before writing the file, not after.

Append a `manifest.py` entry: stage `"tag"`, inputs the
`structured.<lang>.md` hash, counts = items/parts/figures + a
given/key_formula/substitute/conclusion stage-label distribution,
model_calls = however many judgment batches you sent.
