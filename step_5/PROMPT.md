Stage 5 — verify content against the source PDFs and apply corrections.

Verify `chapters/$ARGUMENTS/04_combined/combined.en.md`/`combined.hi.md`
against `00_raw/*.pdf`. Read each language via
`pipeline.mdio.markdown_to_chapter()` and merge with
`pipeline.mdio.merge_by_id()` before verifying.

Before starting: check `manifest.unchanged_since(chapters/$ARGUMENTS/, "verify",
*the combined.<lang>.md files present, *the four raw PDFs)`. If true, stop and report.

Everything downstream (simplify, format, tag, the final hand-designed
page) treats what leaves this stage as ground truth — stage 9 has no code
gate at all, so a number this stage misses has no later chance of being
caught except by a human reading the finished page. Batch generously
enough, and read the attached PDF pages closely enough, that this stage
is where accuracy actually gets decided.

Follow `step_5/verify.md`. Key constraints:

- Attach the **original PDF pages** as document blocks alongside each batch of
  items. Verification against the Mathpix markdown alone is worthless — that is
  the artefact you are checking.
- Batch by 5–8 items so the relevant pages fit alongside them.
- Return corrections as the markdown blocks `step_5/verify.md` shows.
  **Do not return rewritten text.** Every correction needs `found`,
  `should_be`, `reason` and `confidence`.
- Parse them with `pipeline.mdio.markdown_to_corrections()`, then apply with
  `pipeline.verify.apply_corrections()` — do not edit the chapter markdown by
  hand. It applies `high` confidence corrections and returns the rest in
  `held` (medium/low, or a `found` that no longer matches exactly once). Show
  `held` to the user; only re-run with a lower `min_confidence` once they've
  approved specific items.

Write `05_verify/corrections.md` via `pipeline.mdio.corrections_to_markdown()`
(the full list returned by the model) and `05_verify/chapter.verified.en.md`/
`chapter.verified.hi.md` via `pipeline.render.render()` per language (the
chapter after `apply_corrections`).

Gates: `gate_math_parity(before, after)` for both languages, `gate_counts`.
`apply_corrections()` mutates and returns the SAME chapter object it's given
— snapshot `before = chapter.model_copy(deep=True)` first, or the gate
compares the chapter against itself and vacuously "passes" no matter what
changed (this happened once already; caught by re-checking from freshly
re-read files, not by the gate itself).
Report the correction count by type — OCR errors, dropped subscripts, wrong
question numbers, missing sub-parts.

Append a `manifest.py` entry: stage `"verify"`, inputs the chapter.<lang>.md +
four PDF hashes, counts = corrections applied/held by confidence, gate_results
from both gates above, model_calls = number of batches sent.

Run `python3 CALIBRATION/calibrate.py chapters/$ARGUMENTS` once this stage
is done.
