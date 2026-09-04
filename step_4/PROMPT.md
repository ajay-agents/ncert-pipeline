Stage 4 — combine the split examples/Q&A markdown into one file.

Read `chapters/$ARGUMENTS/03_split/examples.<lang>.md` +
`qa.<lang>.md` (whichever languages exist) via
`pipeline.mdio.markdown_to_chapter()` + `pipeline.mdio.merge_by_id()` (the
two files' items merge back into one `Chapter` — they were split from the
same source in stage 3, so this is a plain reunion, not a fresh match),
then render the combined chapter with `pipeline.render.render()`. Pure
function, no model call.

Before starting: check `manifest.unchanged_since(chapters/$ARGUMENTS/,
"combine", *the examples.<lang>.md and qa.<lang>.md files present)`. If
true, stop and report.

Produce, for each of `en` and `hi`:
- `04_combined/combined.<lang>.md`  (all kinds, in original order)

Then verify the round trip: parse each file with `tag._parse` and confirm
every container balances, and that its item count equals stage 3's two
files' combined count exactly (nothing gained, nothing lost recombining).
Report file sizes and item counts.

Append a `manifest.py` entry: stage `"combine"`, inputs the
examples.<lang>.md/qa.<lang>.md hashes, counts = file sizes per output,
model_calls = 0.
