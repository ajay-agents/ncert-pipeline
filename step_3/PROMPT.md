Stage 3 — split the matched chapter into examples-only and Q&A-only markdown.

Read `chapters/$ARGUMENTS/02_extract/chapter.en.md`/`chapter.hi.md`
(whichever exist) via `pipeline.mdio.markdown_to_chapter()` +
`pipeline.mdio.merge_by_id()`, then render each kind-filtered subset with
`pipeline.render.render()`. Pure function, no model call.

Before starting: check `manifest.unchanged_since(chapters/$ARGUMENTS/,
"split", *the chapter.<lang>.md files present)`. If true, stop and report.

Produce, for each of `en` and `hi`:
- `03_split/examples.<lang>.md`  (kind: example)
- `03_split/qa.<lang>.md`        (kinds: exercise, additional_exercise)

Then verify the round trip: parse each file with `tag._parse` and confirm every
container balances. Report file sizes and item counts (the two files'
counts must sum to the merged chapter's total item count — nothing gained,
nothing lost in the split).

Append a `manifest.py` entry: stage `"split"`, inputs the chapter.<lang>.md
hash(es), counts = file sizes and item counts per output, model_calls = 0.
