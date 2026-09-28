# Match report — maths-12-5

## Hindi (chapter.hi.md / solutions.hi.md)

- **chapter:** maths-12-5 (सांतत्य तथा अवकलनीयता / Continuity and Differentiability)
- **language:** Hindi-only (no chapter.en.pdf / solutions.en.pdf supplied at the time this section was written)
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

### Worked examples (ex_5.1–ex_5.42)

All 42 examples' solutions taken directly from chapter.hi.md itself (the textbook's own worked solution), never matched against solutions.hi.md, per standard convention. Examples 1–37 sit in the chapter's main flow across sections 5.2–5.7; examples 38–42 sit in a distinct "विविध उदाहरण" (Miscellaneous Examples) subsection between प्रश्नावली 5.7 and the misc exercise — still `kind="example"`, not exercises.

**Genuine figures found and correctly attached** (this chapter, unlike maths-12-3/12-4, has real mathematically-relevant graphs, not just decorative portraits): `fig_maths-12-5_3` → ex_5.9 (आकृति 5.3), `_4` → ex_5.10 (आकृति 5.4), `_5` → ex_5.11 (आकृति 5.5), `_6` → ex_5.12 (आकृति 5.6), `_7` → ex_5.13 (आकृति 5.7), `_8` → ex_5.15 (आकृति 5.8, fixed — see "Structural fix" below). `fig_0`/`_1`/`_2` (Newton portrait, general introductory illustrations) and `_9`/`_10`/`_11` (theory-section graphs illustrating xⁿ growth rates and logarithmic functions, not tied to any single example or exercise) are correctly excluded from every item, matching this pipeline's established convention for figures that sit in pure theory prose.

**Structural fix during assembly**: the dispatched batch covering ex_5.15 originally placed its `:::figure{...}` block *nested inside* `:::solution` (the figure is referenced mid-solution-text, with more solution content following it) — `pipeline.mdio` only understands flat, pre-stage-7 item structure and cannot parse a container nested inside `:::solution` at this stage (that nesting is introduced later, at stage 7). Fixed by moving the figure block to be a top-level sibling of `:::solution` (after it closes), the same convention already used correctly for the other 5 figures — the solution's own text is unchanged, only the figure's container position moved.

### प्रश्नावली 5.1–5.7 — clean 1:1 number match, zero needs_review

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

### अध्याय 5 पर विविध प्रश्नावली (misc, kind=`additional_exercise`) — one interspersed orphan, content-verified mapping

The current chapter's misc section has 22 items (q_5.9.1–q_5.9.22). solutions.hi.md's own matching section (also titled "अध्याय 5 पर विविध प्रश्नावली" — a separate, later heading in the file, not to be confused with the whole-exercise-orphan below) has **23** items (प्रश्न 1–23). Items 1–18 matched the chapter's own misc items 1–18 directly by number, content-confirmed. **Solutions' own प्रश्न 19 is a genuine interspersed orphan** — a mathematical-induction proof of the power rule ($\frac{d}{dx}(x^n) = nx^{n-1}$), with no counterpart anywhere in the current chapter's 22-item misc list (the rationalised edition evidently dropped this specific proof). This shifts every later item by exactly +1: solutions' प्रश्न 20 ↔ chapter item 19 (sin(A+B) sum-formula-for-cosines derivation), 21↔20, 22↔21, 23↔22 — confirmed by content, not just position (e.g. chapter item 19's "sin(A+B) formula" content matches solutions' प्रश्न 20 exactly, not प्रश्न 19). Solutions' प्रश्न 19 was discarded per Rule 5 before the automated join ran (the join itself was done as a clean, orphan-free 1:1 match after renumbering solutions' items 20–23 down to 19–22 in memory) — never merged, renumbered onto a wrong item, or invented into a placeholder.

One known source-side OCR artifact transcribed verbatim: q_5.9.3's printed expression `(5x)^{3\cos x 2 x}` looks garbled (solutions.hi.md's own restatement of the same problem reads more cleanly as `3\cos 2x`) — flagged for stage 5 to check against the actual chapter.hi.pdf page image; not fixed here.

### Whole-exercise orphan: solutions' own "प्रश्नावली 5.8" (6 items, Rolle's Theorem) has NO counterpart in the current chapter

solutions.hi.md contains a full exercise of its own, labelled "प्रश्नावली 5.8" (6 items, प्रश्न 1–6), covering **Rolle's Theorem** (रोले का प्रमेय) — verified genuinely absent from the current chapter.hi.md (both "रोले" and "माध्यमान मान प्रमेय"/Mean Value Theorem appear zero times in the current chapter's own mathpix text). This entire section was **never extracted at all** (out of scope from the start, once confirmed to have no possible match) and is discarded wholesale per Rule 5 — the rationalised 2026-27 edition evidently dropped Rolle's Theorem from this chapter entirely. This is a distinct orphan from the misc-section one above — do not conflate solutions' "प्रश्नावली 5.8" (wholly orphaned, Rolle's Theorem) with solutions' own separately-headed "अध्याय 5 पर विविध प्रश्नावली" (the chapter's real misc-exercise counterpart, 23 items, only one of which — प्रश्न 19 — is an orphan).

### Known source-side issues transcribed verbatim (not fixed at this stage)

- **q_5.9.3**: `(5x)^{3\cos x 2 x}` — likely OCR-garbled exponent, transcribed as printed in chapter.hi.md; solutions.hi.md's own restatement suggests `3\cos 2x` was intended. Flagged for stage 5.
- **सो 5.4 प्रश्न 8 / सो 5.5 प्रश्न 8**: both have a stray, unrelated copy-pasted opening derivative line before the correct computation resumes (see above) — transcribed exactly as printed.

### Per-part solution gap fixed: q_5.1.21

`CALIBRATION/calibrate.py`'s stricter empty-solution check (which, for a multi-part item, looks only at the parts' own `solution` fields, matching this pipeline's established downstream rendering convention that per-part solutions take priority over an item-level one once parts exist) flagged q_5.1.21 as having no solution at all, even though `gate_solutions_present` passed — the item's own combined solution text was present at the *item* level, but its 3 labelled parts ((a) sin x + cos x, (b) sin x − cos x, (c) sin x · cos x) each had an empty `solution` field, because solutions.hi.md answers all three sub-functions together in one shared derivation (prove sin and cos individually continuous, then invoke the sum/difference/product-of-continuous-functions theorem to conclude all three at once) rather than as three separate part-level write-ups. Fixed by copying the same shared derivation into each part's own `solution` field — honest, since the argument genuinely establishes continuity for all three functions via the identical reasoning, not an invented per-part derivation. `gate_solutions_present` and a full round-trip re-verified clean afterward (179 items, unchanged).

### Structural notes

Extraction split across 15 dispatched fork sub-agent batches (each given `step_2/extract.md` only, never `step_2/PROMPT.md`; each told its exact scope and output file, never to touch `chapters/`, gates, or `manifest.json`) plus one batch (प्रश्नावली 5.6+5.7 solutions) completed directly by the coordinator after a session-usage-limit failure took down that one dispatched agent (all 14 other dispatches succeeded). No invalid container nesting was found during final assembly except the one nested-figure slip noted above (fixed before assembly, not after). `gate_counts` and `gate_solutions_present("hi")` both pass with zero failures against the assembled 179-item chapter, and a full render→re-parse round-trip reproduces exactly 179 items.

## English (chapter.en.md / solutions.en.md)

- **chapter:** maths-12-5 (Continuity and Differentiability)
- **items_total:** 180
- **examples:** 43
- **exercise_5_1:** 34
- **exercise_5_2:** 10
- **exercise_5_3:** 15
- **exercise_5_4:** 10
- **exercise_5_5:** 18
- **exercise_5_6:** 11
- **exercise_5_7:** 17
- **miscellaneous_exercise:** 22
- **figures:** 10
- **multi_part_items:** 3 (q_5.1.3, q_5.1.21, q_5.5.17)
- **gate_counts:** PASS (0 failures)
- **gate_solutions_present:** PASS (0 failures)

Built via a parsing script rather than hand-transcribed item-by-item (unlike maths-12-2's own session) — this chapter's scale (180 items) made full manual transcription impractical, and the source markdown's consistent numbered-item boundaries made deterministic regex parsing safe, extracting verbatim LaTeX with no retyping risk. `match.join_solutions()` was still used for the actual number-based matching, run **separately per EXERCISE section** (7 calls, `chapter=None` each time) rather than once across the whole chapter's pooled items — necessary because `match.norm_num()` prepends the chapter number to any bare number (`"3"` → `"5.3"` when `chapter="5"`), which would have collided EXERCISE 5.1's own item 3 with EXERCISE 5.3's own item 3 (and so on) had a single chapter-wide join been attempted. This mirrors the exact same fix already independently applied on this chapter's own Hindi track (`chapter=""` there).

**Every finding below independently confirms the Hindi track's own documented findings for this exact chapter** — a strong cross-check that both extractions are correct:

- **Whole-exercise orphan, EXERCISE 5.8** (6 questions, Rolle's Theorem): confirmed absent from chapter.en.md via full-text search, skipped entirely — same as Hindi's own प्रश्नावली 5.8 finding.
- **Miscellaneous Exercise +1 shift**: chapter items 1-18 ← solutions Q1-18 (1:1, content-verified); solutions Q19 (mathematical induction, d/dx(xⁿ)=nxⁿ⁻¹) is an orphan with no chapter counterpart; chapter items 19-22 ← solutions Q20-23 (shifted +1) — the exact same orphan, same shift shape, as Hindi's own प्रश्न 19 finding.
- **q_5.misc.21** (the determinant-derivative-rule proof, chapter item 21): solutions.en.md's own restatement (Q22) had **no `## Solution:` heading anywhere in its block** — a mathpix heading-detection gap, discovered via `gate_solutions_present` flagging an empty solution (this specific gap-shape wasn't caught by the earlier stage-1 fullwidth/heading scan, since it sits mid-block rather than being a dropped heading line at a clean boundary). Fixed by manually splitting the block at its own natural question/derivation boundary (confirmed against chapter's own item 21, which matches the block's opening verbatim).
- **q_5.1.21**: same shape as Hindi's own flagged item — question has 3 sub-parts (sinx+cosx, sinx-cosx, sinx·cosx) but the solution is ~95% ONE shared derivation (proving sinx and cosx are each individually continuous) with only a trailing one-line conclusion per part. Matched Hindi's own resolution for consistency: split into 3 `Part` objects, with the identical shared derivation duplicated into each part's own `solution` field (honest — the same reasoning genuinely establishes continuity for all three, not an invented per-part proof).

**Two more multi-part items, not flagged by Hindi's own report** (this chapter's English extraction went through an additional systematic sub-part scan Hindi's own report doesn't mention running): `q_5.1.3` (4 independent per-part continuity proofs — labelled a/b/c/d matching the CHAPTER's own convention, not solutions.en.md's differing i/ii/iii/iv convention for the same item, per the maths-12-3 Hindi `label=`-not-`number=` lesson) and `q_5.5.17` (3 independent, fully self-contained derivations — product rule / expansion / logarithmic differentiation — each proving the same result a different way, plus a shared closing sentence kept as the item-level `final_answer`). Two further candidates from an early (pre-boundary-fix) scan, `q_5.3.15` and `q_5.7.17`, were confirmed **false positives** caused by that scan's own now-fixed section-boundary bug — neither has any real multi-part structure.

**A boundary bug found and fixed during extraction** (not present in Hindi's own report, since Hindi's own extraction used a different — dispatched sub-agent — method): the first version of the section-slicing bounded each EXERCISE only by the position of the next `## EXERCISE 5.N` heading, which silently let intervening exposition/subsection headings/worked Examples between two exercises bleed into the LAST item of the earlier exercise. Caught via a systematic content-similarity check across all 115 exercise items (comparing each chapter-side question against solutions.en.md's own restated question for the same number) — items 4.10 and 5.11 showed trailing garbage like `### 5.5. Logarithmic Differentia` and a whole extra instruction sentence meant for the next block of items. Fixed by bounding each section at the nearest of the next `### `, `## EXERCISE`, `## Miscellaneous`, or `Example N` marker instead. Re-ran the full systematic check afterward: of 115 items, 23 initially flagged as low-similarity were individually reviewed and confirmed as benign phrasing differences (chapter states an instruction once before a run of items and gives only the bare expression per item, while solutions.en.md restates the full instruction each time) or trivial inline-vs-display math delimiter differences — zero genuine content mismatches.

**A genuine cross-language example-count difference, not a bug**: English's chapter.en.md has 43 sequential, non-duplicate "Example N" markers (verified via a reliable line-anchored regex, no gaps 1-43); Hindi's own section above documents 42. Every other section (EXERCISE 5.1-5.7, Misc Exercise) matches EXACTLY between the two independently-extracted language tracks (34/10/15/10/18/11/17/22 both sides) — only Examples differ, by a clean +1 shift (English's own "Miscellaneous Examples" subsection runs 39-43, Hindi's own runs 38-42, both 5 items) meaning English's main flow has one more worked example (38) than Hindi's (37). Given every other section matches exactly, this is most likely a genuine content difference between the specific English and Hindi PDF prints supplied (different edition/reprint) rather than an extraction error. English and Hindi tracks are never field-merged for this project's Maths chapters, so this requires no reconciliation, only documentation.

**Checked for recurrence of Hindi's own flagged source-side OCR artifacts — none found in English**: Hindi's own EXERCISE 5.4/5.5 item 8 solutions each opened with a stray copy-pasted unrelated derivative line; English's own corresponding solutions are clean (correctly open with the item's own actual function). Hindi's own misc item 3 exponent `(5x)^{3\cos x 2 x}` looked OCR-garbled; English's own item 3 reads cleanly as `(5x)^{3\cos 2x}`. Both confirm these were Hindi-source-specific artifacts, not something inherent to this chapter's content that would be expected to recur.

**Topic assignment**: given the chapter's scale, topics were generated via a per-exercise-theme heuristic (each of the 7 numbered EXERCISEs has one uniform operation stated once as a shared preamble, e.g. EXERCISE 5.5 is entirely "logarithmic differentiation") plus a short, LaTeX-command-stripped excerpt of the item's own distinguishing expression, rather than fully bespoke per-item wording — consistent with RULES.md's framing of topic as a low-stakes, freeform, not-source-checked label. Verified generated topics never contain a raw LaTeX backslash command (topic is a plain container attribute, never passed through the math converter at stage 9) — added a "piecewise function" fallback for `\begin{cases}`/`\begin{array}` expressions.

**Verification**: independently round-tripped the written `chapter.en.md` back through `mdio.markdown_to_chapter()` and re-ran both gates — 180 items, correct 43/115/22 kind split, unique ids, `gate_counts` and `gate_solutions_present` both pass. Verified all 10 attached figures resolve via `os.path.exists` against the real `01_mathpix/images/` directory. `CALIBRATION/calibrate.py`'s own stricter per-part solution check (the same one that caught Hindi's q_5.1.21 gap) reports 0 items with no solution at all for English too.
