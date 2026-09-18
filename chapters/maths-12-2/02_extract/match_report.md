# Match report — maths-12-2

- **chapter:** maths-12-2
- **language:** Hindi-only (no chapter.en.pdf / solutions.en.pdf supplied)
- **examples_extracted:** 6
- **prashnavali_2.1_extracted:** 14
- **prashnavali_2.2_extracted:** 15
- **misc_exercise_extracted:** 14
- **total_items:** 49
- **gate_counts:** PASS (0 failures)
- **gate_solutions_present_hi:** PASS (0 failures, every item has a non-empty solution)
- **gate_bilingual:** N/A as expected for Hindi-only - 97 items flagged missing a language (all of them, by design)

## प्रश्नावली 2.1 — clean 1:1 number match (no drift)

All 14 items (q_2.1.1..q_2.1.14) matched solutions.hi.md's प्रश्न 1-14 directly by number; content-verified by direct text comparison — no drift in this section, join_solutions() would have worked correctly here (not actually invoked; built by hand for consistency with the other two sections, which could not use it).

## प्रश्नावली 2.2 — REJECTED plain number-match; hand-verified content mapping used

solutions.hi.md's own प्रश्नावली 2.2 has 21 numbered items (an older, non-rationalised numbering); the current chapter.hi.md keeps only 15 of them, several INTERSPERSED rather than confined to a trailing block (chapter.hi.md's own items 10-12 even carry a leftover printed artifact — 'प्रश्न संख्या 16 से 18 में...' — confirming they were once numbered 16-18). A plain join_solutions() by number would have matched chapter items 1-2 correctly (coincidence) but items 3-15 to the WRONG solutions entirely (13 silent mismatches), while needs_review would have shown only the 6 trailing-looking orphans (16-21) and hidden the other 6 true orphans (3,4,6,12,14,15) inside the wrong pairings. Every one of the 15 pairings below was confirmed by direct content comparison before use:

| chapter id | chapter content (short) | solutions प्रश्न # |
|---|---|---|
| q_2.2.1 | 3sin⁻¹x=sin⁻¹(3x-4x³) प्रमाण | 1 |
| q_2.2.2 | 3cos⁻¹x=cos⁻¹(4x³-3x) प्रमाण | 2 |
| q_2.2.3 | tan⁻¹((√(1+x²)-1)/x) सरलीकरण | 5 |
| q_2.2.4 | tan⁻¹(√((1-cosx)/(1+cosx))) सरलीकरण | 7 |
| q_2.2.5 | tan⁻¹((cosx-sinx)/(cosx+sinx)) सरलीकरण | 8 |
| q_2.2.6 | tan⁻¹(x/√(a²-x²)) सरलीकरण | 9 |
| q_2.2.7 | tan⁻¹((3a²x-x³)/(a³-3ax²)) सरलीकरण | 10 |
| q_2.2.8 | tan⁻¹[2cos(2sin⁻¹½)] मान | 11 |
| q_2.2.9 | tan½[sin⁻¹(2x/(1+x²))+cos⁻¹((1-y²)/(1+y²))] मान | 13 |
| q_2.2.10 | sin⁻¹(sin2π/3) मान | 16 |
| q_2.2.11 | tan⁻¹(tan3π/4) मान | 17 |
| q_2.2.12 | tan(sin⁻¹⅗+cot⁻¹1.5) मान | 18 |
| q_2.2.13 | MCQ cos⁻¹(cos7π/6) | 19 |
| q_2.2.14 | MCQ sin(π/3-sin⁻¹(-½)) | 20 |
| q_2.2.15 | MCQ tan⁻¹√3-cot⁻¹(-√3) | 21 |

**Orphan solutions discarded (genuine old-edition-only content, per Rule 5 — not invented into placeholder questions):** प्रश्न 3 (tan⁻¹2/11+tan⁻¹7/24=tan⁻¹½), प्रश्न 4 (2tan⁻¹½+tan⁻¹1/7=tan⁻¹31/17), प्रश्न 6 (tan⁻¹1/√(x²-1) simplify), प्रश्न 12 (cot(tan⁻¹a+cot⁻¹a)), प्रश्न 14 (sin(sin⁻¹⅕+cos⁻¹x)=1, find x), प्रश्न 15 (tan⁻¹ sum equation, find x).

## विविध प्रश्नावली (additional_exercise) — REJECTED plain number-match; hand-verified content mapping used

Same failure mode: solutions.hi.md's misc section has 17 items; the current chapter keeps only 14, with two old items (प्रश्न 8, प्रश्न 12) dropped from the MIDDLE of the run rather than the end, shifting every later item's true number down by 1 or 2. A plain number-match would have paired chapter items 1-7 correctly (real 1:1 range) but items 8-14 to the wrong solutions, with only प्रश्न 17 surfacing as an orphan (hiding प्रश्न 8 and प्रश्न 12 as true orphans). Verified by content:

| chapter id | chapter content (short) | solutions प्रश्न # |
|---|---|---|
| q_2.5.1 | cos⁻¹(cos13π/6) मान | 1 |
| q_2.5.2 | tan⁻¹(tan7π/6) मान | 2 |
| q_2.5.3 | 2sin⁻¹⅗=tan⁻¹24/7 प्रमाण | 3 |
| q_2.5.4 | sin⁻¹8/17+sin⁻¹⅗=tan⁻¹77/36 प्रमाण | 4 |
| q_2.5.5 | cos⁻¹⅘+cos⁻¹12/13=cos⁻¹33/65 प्रमाण | 5 |
| q_2.5.6 | cos⁻¹12/13+sin⁻¹⅗=sin⁻¹56/65 प्रमाण | 6 |
| q_2.5.7 | tan⁻¹63/16=sin⁻¹5/13+cos⁻¹⅗ प्रमाण | 7 |
| q_2.5.8 | tan⁻¹√x=½cos⁻¹((1-x)/(1+x)) प्रमाण | 9 |
| q_2.5.9 | cot⁻¹(...)=x/2 प्रमाण | 10 |
| q_2.5.10 | tan⁻¹(...)=π/4-½cos⁻¹x प्रमाण [x=cos2θ] | 11 |
| q_2.5.11 | 2tan⁻¹(cosx)=tan⁻¹(2cosecx) हल | 13 |
| q_2.5.12 | tan⁻¹((1-x)/(1+x))=½tan⁻¹x हल | 14 |
| q_2.5.13 | MCQ sin(tan⁻¹x) | 15 |
| q_2.5.14 | MCQ sin⁻¹(1-x)-2sin⁻¹x=π/2 | 16 |

**Orphan solutions discarded:** प्रश्न 8 (tan⁻¹⅕+tan⁻¹1/7+tan⁻¹⅓+tan⁻¹⅛=π/4 प्रमाण), प्रश्न 12 (9π/8-9/4·sin⁻¹⅓=9/4·sin⁻¹(2√2/3) प्रमाण), प्रश्न 17 (MCQ tan⁻¹(x/y)-tan⁻¹((x-y)/(x+y))).

## Cross-document domain-notation discrepancies (flagged for stage 5, not resolved here)

- q_2.2.4: chapter states domain '0<x<π'; solutions प्रश्न 7 states 'x<π' (no lower bound given). Same core expression.
- q_2.2.5: chapter states domain '-π/4<x<3π/4'; solutions प्रश्न 8 states '0<x<π'. Same core expression.
- q_2.2.7: solutions प्रश्न 10's own domain line has a dropped comparison operator on its right side ('a>0; -a/√3 ≤ x a/√3', missing a '≤' before the final 'a/√3') — a Mathpix OCR artifact in the source, transcribed as-is per stage 2 rules (not fixed here).

## Known OCR artifacts transcribed verbatim (not fixed at this stage)

- chapter.hi.md's own प्रश्नावली 2.2 item 8 and विविध प्रश्नावली items 8, 9, 10 print the inverse-function exponent as a bare '1' instead of '-1' (e.g. 'tan^{1}' for 'tan^{-1}') — a Mathpix superscript-minus-sign drop. solutions.hi.md's own versions of the same items (प्रश्न 11 in प्रश्नावली 2.2; प्रश्न 9,10,11 in the misc section) print these correctly with '-1', so the intended reading is unambiguous. Left exactly as printed in chapter.hi.md's own extraction (question text), per 'transcribe, don't fix' — a stage 5 concern, not stage 2's.
