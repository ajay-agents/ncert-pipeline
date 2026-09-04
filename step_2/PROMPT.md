Stage 2 — extract examples, exercises and solutions, then match and align them.

Build `chapters/$ARGUMENTS/02_extract/chapter.en.md` + `chapter.hi.md`
(whichever languages exist) + `match_report.md`.

Before starting: check `manifest.unchanged_since(chapters/$ARGUMENTS/,
"extract_match", *the four 01_mathpix files)`. If true, stop and report —
this stage already ran against these exact files.

## Part A — extract

Extract structured items from `chapters/$ARGUMENTS/01_mathpix/`.

Run **three separate extraction passes per language**, using
`step_2/extract.md` as the instruction and `pipeline/schema.py` as the contract:

- examples from `chapter.<lang>.md`
- exercise questions from `chapter.<lang>.md` (the EXERCISES block, plus
  ADDITIONAL EXERCISES where present)
- solutions from `solutions.<lang>.md`

Chunk each source by section heading. Never split a question across chunks —
if a heading boundary lands mid-question, extend the chunk.

Keep the three lists **separate in memory** — `{"examples": [...],
"exercises": [...], "solutions": [...]}` per language, each item validated
against `Item` (not `Chapter` — there is no single merged chapter yet,
that's what Part B builds). `exercises` carries the questions with no
`:::solution` block; `solutions` carries the raw solutions-document entries
Part B joins to them. Keeping them separate in memory is what lets
`match.join_solutions()` (a two-list function) run at all.

`examples` and `exercises` items should carry `topic` (see
`step_2/extract.md`); `solutions` items don't need one — a question's
`topic` lives on the question-side item and survives the join untouched.

Assign each item's `id` yourself: `ex_<chapter>.<n>` for examples,
`q_<chapter>.<n>` for exercise/additional_exercise items, `sol_<chapter>.<n>`
for raw solutions-document entries (a distinct prefix so a solutions-pass
id can never collide with an exercise-pass id before they're joined). Use
`match.norm_num()` on the printed number to get `<n>`.

Run `gate_counts` on two throwaway `Chapter`s per language — one from
`examples + exercises`, one from `solutions` — before moving to Part B; a
duplicate id or empty number here means something upstream is already
broken, not a threshold to relax.

## Part B — match and align

1. Run `match.join_solutions(exercises, solutions, chapter, lang)` per
   language. This is deterministic — do not match by reading the files
   yourself. Build each language's `Chapter` from `examples + merged`.
2. Read `report["needs_review"]`. **Only these items go to the model.** For each
   unmatched question and orphan solution, decide the pairing — if no pairing
   is defensible, leave the solution empty. For each `duplicate_solutions`
   entry (two solution blocks extracted under the same question number, e.g.
   a heading repeated across a page break), decide whether the second block
   belongs to this question, an adjacent one, or is genuine OCR duplication
   to discard.

   **`join_solutions()` matches by printed number only** — if the textbook
   and the separate solutions-manual document have drifted out of sync on
   numbering (e.g. a "Rationalised" curriculum edition of the textbook
   dropped an exercise the solutions manual still numbers around), a whole
   run of same-numbered items can be matched to the wrong solution while
   `needs_review` stays empty, because every number DID find a match — just
   the wrong one. This has happened for real: eleven consecutive items were
   silently mismatched this way. After the automated join, spot-check by
   reading a handful of matched question/solution pairs side by side
   (distinctive numbers — radii, charge values, anything specific) even
   when `needs_review` is empty; if the chapter's own calibration part/item
   counts look off from a prior run of the same chapter, that's a second
   signal something upstream drifted.

   Also watch `join_solutions()`'s own fallback for a matched item with no
   parts yet (`elif hit.parts and not q.parts: q.parts = hit.parts`): once a
   number-only match is wrong, this line can wholesale-replace a question's
   parts list with a wrongly-numbered solution's parts. If you re-derive a
   pairing by hand after finding a mismatch, attach part-level content by
   matching the question's OWN existing part labels against the solution's
   part labels — never by replacing the parts list outright — and confirm
   the resulting part count against a fresh `gate_counts`/calibration run,
   not just against the pairing you just fixed.
3. Run `match.align_languages(en_chapter, hi_chapter)` to merge English and
   Hindi into one `Chapter`.
4. Resolve `report["only_en"]` / `report["only_hi"]` the same way — by inspection
   of the specific items, not by re-processing everything. Also check
   `report["kind_mismatch"]`: `align_languages` already merged these (a
   kind-label disagreement between two independent extraction passes doesn't
   justify discarding a real translation), but confirm which kind is actually
   correct and fix the item's `kind` if the two passes disagreed.
5. Write `chapter.en.md`/`chapter.hi.md` via `pipeline.render.render(chapter,
   lang)` (already exists — reuse it, don't hand-format) and
   `match_report.md` via `pipeline.mdio.match_report_to_markdown(report)`.

If English and Hindi extraction counts differ (before matching), list the
numbers present in one and absent in the other in your stage report — the
alignment step above is what resolves it, not a separate fix.

Append a `manifest.py` entry: stage `"extract_match"`, inputs the four
01_mathpix file hashes, counts = examples/exercises/solutions per language
plus matched/needs_review/aligned, model_calls = 6 extraction passes (3 ×
2 languages) + however many needs_review/only_en/only_hi/kind_mismatch
items you resolved by hand.

Gates: `gate_counts`, `gate_solutions_present` for both languages,
`gate_bilingual`. Report every empty solution explicitly — a silent gap here
becomes a missing answer for a student.

Run `python3 CALIBRATION/calibrate.py chapters/$ARGUMENTS` once this stage
is done — it reads `chapter.en.md`/`chapter.hi.md` directly.
