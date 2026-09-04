Stage 6 — simplify solution language for student readability.

Simplify `chapters/$ARGUMENTS/05_verify/chapter.verified.en.md`/
`chapter.verified.hi.md`. Read each language via
`pipeline.mdio.markdown_to_chapter()`.

Before starting: check `manifest.unchanged_since(chapters/$ARGUMENTS/, "simplify",
*the chapter.verified.<lang>.md files present)`. If true, stop and report.

Follow `step_6/simplify.md`. Non-negotiable:

- **Freeze first.** Run every field through `protect.freeze()` before the model
  sees it, and `protect.restore()` after. If restore raises, retry that item
  once, then leave it unsimplified and log it.
- **Exercise question text is never touched.** Simplify solutions, explanations
  and example prose only.
- Final numeric answers are never rephrased, rounded or re-derived.
- Hindi follows the house style: Devanagari for English technical terms, no
  hyphens, short sentences.

Write `06_simplify/chapter.simplified.en.md`/`chapter.simplified.hi.md` via
`pipeline.render.render()` per language.

Gates, all against the merged `chapter.verified.*.md`
(`pipeline.mdio.merge_by_id()`):
`gate_question_text_frozen`, `gate_answers_unchanged`, `gate_math_parity`,
`gate_bilingual`. Any failure means the stage output is discarded, not patched.

Append a `manifest.py` entry regardless of outcome: stage `"simplify"`, inputs
the chapter.verified.<lang>.md hash(es), counts = items simplified vs. left
unchanged vs. restore-failed, gate_results from all four gates, model_calls =
number of items/batches sent. A failed gate still gets an entry — the record
that this run was discarded is itself part of the audit trail.

Run `python3 CALIBRATION/calibrate.py chapters/$ARGUMENTS` once this stage
is done.
