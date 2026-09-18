# Match report — maths-12-5

- **chapter:** maths-12-5 (सांतत्य तथा अवकलनीयता / Continuity and Differentiability)
- **language:** Hindi-only (no chapter.en.pdf / solutions.en.pdf supplied)
- **examples_extracted:** 42 (ex_5.1–ex_5.42, including 5 examples inside the "विविध उदाहरण" subsection)
- **prashnavali_5.1_extracted:** 34 (q_5.1.1–q_5.1.34)
- **prashnavali_5.2_extracted:** 10 (q_5.2.1–q_5.2.10)
- **prashnavali_5.3_extracted:** 15 (q_5.3.1–q_5.3.15)
- **prashnavali_5.4_extracted:** 10 (q_5.4.1–q_5.4.10)
- **prashnavali_5.5_extracted:** 18 (q_5.5.1–q_5.5.18)
- **prashnavali_5.6_extracted:** 11 (q_5.6.1–q_5.6.11)
- **prashnavali_5.7_extracted:** 17 (q_5.7.1–q_5.7.17)
- **misc_exercise_extracted:** 22 (q_5.9.1–q_5.9.22)
- **total_items:** 179 (42 examples + 137 exercise/misc items)
- **gate_counts:** PASS (0 failures)
- **gate_solutions_present_hi:** PASS (0 failures, every item has a non-empty solution)
- **gate_bilingual:** N/A as expected for Hindi-only — all 179 items flagged missing a language (by design)

This is the largest chapter built in this series so far (179 items, more than double maths-12-4's 80), and — unusually for this pipeline's recent history — **every one of the 7 numbered exercises (5.1–5.7) matched the solutions manual cleanly, 1:1 by printed number, with zero `needs_review` entries from `match.join_solutions()`.** No whole-exercise numbering shift this time (unlike maths-12-3/12-4, where every exercise after a certain point was offset by a constant). Two genuine, narrower orphan problems were found instead, both resolved by hand before the automated join ran (see below) — plus one nested-figure structural slip caught and fixed during assembly.

## Worked examples (ex_5.1–ex_5.42)

All 42 examples' solutions taken directly from chapter.hi.md itself (the textbook's own worked solution), never matched against solutions.hi.md, per standard convention. Examples 1–37 sit in the chapter's main flow across sections 5.2–5.7; examples 38–42 sit in a distinct "विविध उदाहरण" (Miscellaneous Examples) subsection between प्रश्नावली 5.7 and the misc exercise — still `kind="example"`, not exercises.

**Genuine figures found and correctly attached** (this chapter, unlike maths-12-3/12-4, has real mathematically-relevant graphs, not just decorative portraits): `fig_maths-12-5_3` → ex_5.9 (आकृति 5.3), `_4` → ex_5.10 (आकृति 5.4), `_5` → ex_5.11 (आकृति 5.5), `_6` → ex_5.12 (आकृति 5.6), `_7` → ex_5.13 (आकृति 5.7), `_8` → ex_5.15 (आकृति 5.8, fixed — see "Structural fix" below). `fig_0`/`_1`/`_2` (Newton portrait, general introductory illustrations) and `_9`/`_10`/`_11` (theory-section graphs illustrating xⁿ growth rates and logarithmic functions, not tied to any single example or exercise) are correctly excluded from every item, matching this pipeline's established convention for figures that sit in pure theory prose.

**Structural fix during assembly**: the dispatched batch covering ex_5.15 originally placed its `:::figure{...}` block *nested inside* `:::solution` (the figure is referenced mid-solution-text, with more solution content following it) — `pipeline.mdio` only understands flat, pre-stage-7 item structure and cannot parse a container nested inside `:::solution` at this stage (that nesting is introduced later, at stage 7). Fixed by moving the figure block to be a top-level sibling of `:::solution` (after it closes), the same convention already used correctly for the other 5 figures — the solution's own text is unchanged, only the figure's container position moved.

## प्रश्नावली 5.1–5.7 — clean 1:1 number match, zero needs_review

All 7 exercises matched `solutions.hi.md`'s own same-numbered प्रश्नावली directly, item-for-item, via `match.join_solutions()` (called once per exercise section with `chapter=""` to keep each section's own bare numbering — "1", "2", ... — from colliding with another section's, since this chapter's solutions manual numbers every exercise's items starting fresh at 1, not chapter-relative). Every section's question count exactly equalled its solution count, and `needs_review` was empty for every single one:

| exercise | items | needs_review |
|---|---|---|
| 5.1 | 34 | none |
| 5.2 | 10 | none |
| 5.3 | 15 | none |
| 5.4 | 10 | none |
| 5.5 | 18 | none |
| 5.6 | 11 | none |
| 5.7 | 17 | none |

Per step_2/PROMPT.md's own standing warning ("a whole run of same-numbered items can be matched to the wrong solution while `needs_review` stays empty"), a clean automated join was **not** taken on faith — 5 matched pairs across different sections (q_5.1.20, q_5.4.7, q_5.6.9, q_5.9.19, q_5.9.22) were spot-checked by reading question and solution side by side for genuine content correspondence (distinctive functions/values), not just matching numbers. All 5 checked out correctly.

Two genuine source-side transcription artifacts were flagged during extraction (not fixed here, transcribed verbatim per Rule 5 — flagged for stage 5 to check against the actual solutions.hi.pdf page image):
- **उत्तर 8 (प्रश्नावली 5.4, q_5.4.8)**: the solution's opening line reads "माना $y=\frac{e^{x}}{\sin x}$" — a stray copy-paste leftover unrelated to q_5.4.8's actual question ($\log(\log x)$, $x>1$); every line after that stray opener correctly proceeds with $y=\log(\log x)$ and reaches the right derivative ($\frac{1}{x\log x}$). Transcribed exactly as printed, including the stray first line.
- **उत्तर 8 (प्रश्नावली 5.5)**: the first derivative line is likewise a stray copy-pasted line unrelated to the item's actual function; the correct computation follows immediately after it.

## अध्याय 5 पर विविध प्रश्नावली (misc, kind=`additional_exercise`) — one interspersed orphan, content-verified mapping

The current chapter's misc section has 22 items (q_5.9.1–q_5.9.22). solutions.hi.md's own matching section (also titled "अध्याय 5 पर विविध प्रश्नावली" — a separate, later heading in the file, not to be confused with the whole-exercise-orphan below) has **23** items (प्रश्न 1–23). Items 1–18 matched the chapter's own misc items 1–18 directly by number, content-confirmed. **Solutions' own प्रश्न 19 is a genuine interspersed orphan** — a mathematical-induction proof of the power rule ($\frac{d}{dx}(x^n) = nx^{n-1}$), with no counterpart anywhere in the current chapter's 22-item misc list (the rationalised edition evidently dropped this specific proof). This shifts every later item by exactly +1: solutions' प्रश्न 20 ↔ chapter item 19 (sin(A+B) sum-formula-for-cosines derivation), 21↔20, 22↔21, 23↔22 — confirmed by content, not just position (e.g. chapter item 19's "sin(A+B) formula" content matches solutions' प्रश्न 20 exactly, not प्रश्न 19). Solutions' प्रश्न 19 was discarded per Rule 5 before the automated join ran (the join itself was done as a clean, orphan-free 1:1 match after renumbering solutions' items 20–23 down to 19–22 in memory) — never merged, renumbered onto a wrong item, or invented into a placeholder.

One known source-side OCR artifact transcribed verbatim: q_5.9.3's printed expression `(5x)^{3\cos x 2 x}` looks garbled (solutions.hi.md's own restatement of the same problem reads more cleanly as `3\cos 2x`) — flagged for stage 5 to check against the actual chapter.hi.pdf page image; not fixed here.

## Whole-exercise orphan: solutions' own "प्रश्नावली 5.8" (6 items, Rolle's Theorem) has NO counterpart in the current chapter

solutions.hi.md contains a full exercise of its own, labelled "प्रश्नावली 5.8" (6 items, प्रश्न 1–6), covering **Rolle's Theorem** (रोले का प्रमेय) — verified genuinely absent from the current chapter.hi.md (both "रोले" and "माध्यमान मान प्रमेय"/Mean Value Theorem appear zero times in the current chapter's own mathpix text). This entire section was **never extracted at all** (out of scope from the start, once confirmed to have no possible match) and is discarded wholesale per Rule 5 — the rationalised 2026-27 edition evidently dropped Rolle's Theorem from this chapter entirely. This is a distinct orphan from the misc-section one above — do not conflate solutions' "प्रश्नावली 5.8" (wholly orphaned, Rolle's Theorem) with solutions' own separately-headed "अध्याय 5 पर विविध प्रश्नावली" (the chapter's real misc-exercise counterpart, 23 items, only one of which — प्रश्न 19 — is an orphan).

## Known source-side issues transcribed verbatim (not fixed at this stage)

- **q_5.9.3**: `(5x)^{3\cos x 2 x}` — likely OCR-garbled exponent, transcribed as printed in chapter.hi.md; solutions.hi.md's own restatement suggests `3\cos 2x` was intended. Flagged for stage 5.
- **सो 5.4 प्रश्न 8 / सो 5.5 प्रश्न 8**: both have a stray, unrelated copy-pasted opening derivative line before the correct computation resumes (see above) — transcribed exactly as printed.

## Per-part solution gap fixed: q_5.1.21

`CALIBRATION/calibrate.py`'s stricter empty-solution check (which, for a multi-part item, looks only at the parts' own `solution` fields, matching this pipeline's established downstream rendering convention that per-part solutions take priority over an item-level one once parts exist) flagged q_5.1.21 as having no solution at all, even though `gate_solutions_present` passed — the item's own combined solution text was present at the *item* level, but its 3 labelled parts ((a) sin x + cos x, (b) sin x − cos x, (c) sin x · cos x) each had an empty `solution` field, because solutions.hi.md answers all three sub-functions together in one shared derivation (prove sin and cos individually continuous, then invoke the sum/difference/product-of-continuous-functions theorem to conclude all three at once) rather than as three separate part-level write-ups. Fixed by copying the same shared derivation into each part's own `solution` field — honest, since the argument genuinely establishes continuity for all three functions via the identical reasoning, not an invented per-part derivation. `gate_solutions_present` and a full round-trip re-verified clean afterward (179 items, unchanged).

## Structural notes

Extraction split across 15 dispatched fork sub-agent batches (each given `step_2/extract.md` only, never `step_2/PROMPT.md`; each told its exact scope and output file, never to touch `chapters/`, gates, or `manifest.json`) plus one batch (प्रश्नावली 5.6+5.7 solutions) completed directly by the coordinator after a session-usage-limit failure took down that one dispatched agent (all 14 other dispatches succeeded). No invalid container nesting was found during final assembly except the one nested-figure slip noted above (fixed before assembly, not after). `gate_counts` and `gate_solutions_present("hi")` both pass with zero failures against the assembled 179-item chapter, and a full render→re-parse round-trip reproduces exactly 179 items.
