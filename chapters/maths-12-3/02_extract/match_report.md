# Match report — maths-12-3

- **chapter:** maths-12-3 (आव्यूह / Matrices)
- **language:** Hindi-only (no chapter.en.pdf / solutions.en.pdf supplied)
- **examples_extracted:** 24 (ex_3.1–ex_3.24)
- **prashnavali_3.1_extracted:** 10 (q_3.1.1–q_3.1.10)
- **prashnavali_3.2_extracted:** 22 (q_3.2.1–q_3.2.22)
- **prashnavali_3.3_extracted:** 12 (q_3.3.1–q_3.3.12)
- **misc_exercise_extracted:** 11 (q_3.9.1–q_3.9.11)
- **total_items:** 79
- **gate_counts:** PASS (0 failures)
- **gate_solutions_present_hi:** PASS (0 failures, every item has a non-empty solution)
- **gate_bilingual:** N/A as expected for Hindi-only — all 79 items flagged missing a language (by design)

## Worked examples (ex_3.1–ex_3.24)

All 24 examples' solutions taken directly from chapter.hi.md itself (the textbook's own worked solution), never matched against solutions.hi.md, per standard convention — NCERT worked examples always carry their own textbook solution and the separate solutions manual only covers exercises (प्रश्नावली). Example 12 is spelled "उदहारण 12" in the source OCR (missing आ) — a genuine transcription variant, transcribed as printed, not corrected here.

## प्रश्नावली 3.1 — clean 1:1 number match (no drift)

All 10 items (q_3.1.1..q_3.1.10) matched solutions.hi.md's own प्रश्नावली 3.1, प्रश्न 1-10 directly by number; content-verified — no drift.

## प्रश्नावली 3.2 — clean 1:1 number match (no drift)

All 22 items (q_3.2.1..q_3.2.22) matched solutions.hi.md's own प्रश्नावली 3.2, प्रश्न 1-22 directly by number; spot-checked items 1, 10, 12, 20, 22 plus a full re-verification during transcription of every item in this range — no drift found anywhere in this exercise.

## प्रश्नावली 3.3 — clean 1:1 number match (no drift)

All 12 items (q_3.3.1..q_3.3.12) matched solutions.hi.md's own प्रश्नावली 3.3, प्रश्न 1-12 directly by number; spot-checked items 11, 12 plus full transcription-time verification — no drift.

## प्रश्नावली 3.4 — ENTIRE EXERCISE DISCARDED (Rule 5: genuine old-edition-only content)

solutions.hi.md contains a full extra exercise, "प्रश्नावली 3.4" (18 items, प्रश्न 1-18, covering finding matrix inverses via elementary row/column transformations), immediately following प्रश्नावली 3.3 and immediately before the misc/chapter-end exercise heading in that document. **This entire section has no counterpart anywhere in the current chapter.hi.md** (rationalized edition dropped the "elementary operations to find A⁻¹" topic from this chapter's exercises entirely — no section 3.4-numbered exercise, and no trace of its content, appears in chapter.hi.md at all). All 18 items (17 matrix-inverse-by-elementary-operations problems + 1 closing MCQ on the definition of an invertible matrix, "आव्यूह A तथा B एक दूसरे के व्युत्क्रम होंगे केवल यदि...") are discarded per Rule 5 — never merged, renumbered, or invented into the current item set. Confirmed boundary: solutions.hi.md's प्रश्नावली 3.4 प्रश्न 18 (the MCQ) is followed immediately by "अध्याय 3 पर विविध प्रश्नावली / प्रश्न 1", marking exactly where the discarded exercise ends and the (kept) misc exercise begins.

## विविध प्रश्नावली (misc, kind=additional_exercise) — REJECTED plain number-match; hand-verified content mapping used

solutions.hi.md's misc section has 15 items (प्रश्न 1-15); the current chapter keeps only 11, with the offset concentrated at the front (3 old items dropped from the start) plus one more dropped from the middle. Used the id slot `q_3.9.<n>` (kind=`additional_exercise`) — deliberately unused, since content sections run 3.1-3.7 and the three numbered exercises are 3.1/3.2/3.3 (with the discarded old-edition "3.4" label reserved and unused in the current chapter), so 3.9 avoids colliding with any real number on either side. Every pairing below was confirmed by direct content comparison before use:

| chapter id | chapter content (short) | solutions प्रश्न # |
|---|---|---|
| q_3.9.1 | AB−BA विषम सममित प्रमाण (A,B सममित) | 4 |
| q_3.9.2 | B'AB सममित/विषम सममित प्रमाण | 5 |
| q_3.9.3 | A'A=I से x,y,z ज्ञात करना | 6 |
| q_3.9.4 | पंक्ति-स्तंभ-आव्यूह गुणनफल से x ज्ञात करना | 7 |
| q_3.9.5 | A²−5A+7I=O सत्यापन | 8 |
| q_3.9.6 | पंक्ति-स्तंभ-आव्यूह गुणनफल से x ज्ञात करना (दूसरा उदाहरण) | 9 |
| q_3.9.7 | निर्माता — दो बाज़ारों में आय व लाभ (आव्यूह गुणन अनुप्रयोग) | 10 |
| q_3.9.8 | X\[1 2 3;4 5 6]=... से आव्यूह X ज्ञात करना | 11 |
| q_3.9.9 | MCQ A²=I से α²+βγ का मान | 13 |
| q_3.9.10 | MCQ सममित तथा विषम सममित दोनों आव्यूह | 14 |
| q_3.9.11 | MCQ (I+A)³−7A जहाँ A²=A | 15 |

**Orphan solutions discarded (genuine old-edition-only content, per Rule 5 — not invented into placeholder questions):** प्रश्न 1 (Aⁿ सामान्य सूत्र आगमन प्रमाण, `[[1,0],[n,1]]` रूप), प्रश्न 2 (Aⁿ सामान्य सूत्र आगमन प्रमाण, `[[1,1,1],[0,1,1],[0,0,1]]` रूप), प्रश्न 3 (Aⁿ सामान्य सूत्र आगमन प्रमाण, `[[3,-4],[1,-1]]` रूप), प्रश्न 12 (AB=BA दिया हो तो गणितीय आगमन से (AB)ⁿ=AⁿBⁿ तथा ABⁿ=BⁿA का प्रमाण). All four are induction-proof problems about `Aⁿ`/`(AB)ⁿ` general formulas with no counterpart among the current chapter's 11 misc items.

## Known source-side issues transcribed verbatim (not fixed at this stage)

- q_3.9.6: solutions.hi.md's own solution for this item is itself incomplete/broken in the source — it ends abruptly at `⇒[x²-2x-40+2x-8]=[0].0` without ever isolating x (the expected resolution would simplify to x²-48=0 → x=±4√3). Transcribed exactly as printed per Rule 5/extract.md's "transcribe, don't fix" rule; flagged here for stage 5 to evaluate against the source PDF image.
- q_3.3.2 and q_3.3.8: solutions.hi.md carries a genuine copy-paste artifact in each item's part (ii) — the concluding line literally re-prints the part (i) equality (`(A+B)′=A′+B′` / `(A+A′)′=(A+A′)`) instead of the part (ii) one it should state (`(A−B)′=A′−B′` / `(A−A′)′=−(A−A′)`). Transcribed verbatim; flagged for stage 5 as a real correction candidate (the arithmetic in the body of each solution is itself correct — only the final restated equality line is mistyped in the source).
- ex_3.22: the source's Q′ matrix has one entry printed as `5/3` where the surrounding arithmetic implies it should be `5/2` (a likely source-side typo, consistent with every other entry in that row/column being expressed in halves). Transcribed exactly as printed; flagged for stage 5.
- ex_3.16: the (AB)(C) computation's raw array has a jagged trailing entry ("-4+18" on its own row before the closing bracket) that looks like a source OCR artifact from a multi-line handwritten-style computation. Transcribed as-is; flagged for stage 5 to check against the source PDF page image directly.
- q_3.2.8: chapter.hi.md's own prompt line reads "X तथा Y ज्ञात कीजिए यदि Y=...तथा 2X+Y=..." — Y is actually given outright, not solved-for symmetrically with X, a minor wording quirk present identically in both chapter.hi.md and solutions.hi.md. Transcribed as-is (Rule 5 — no invented correction at extraction stage).

## Structural fixes applied during assembly (container-syntax only, no content changed)

Two items from the delegated extraction batches used an invalid container nesting (`:::part` nested inside an unclosed `:::prompt`, rather than as a direct sibling inside the example/question with its own `:::prompt`/`:::solution`) which `pipeline.tag`/`pipeline.mdio` cannot parse (pre-stage-7 flat-item format requires `:::part` to be a direct child, not nested inside `:::prompt`/`:::solution`). Fixed by restructuring into proper sibling `:::part` blocks, each with its own prompt+solution split at the source's own existing sub-labels — no text was added, removed, or reworded, only re-containerized:
- ex_3.20 (three parts, each a one-line prompt + its own solution segment, split at the source's own "(i) यहाँ / (ii) यहाँ / (iii) यहाँ" markers).
- q_3.9.7 (two parts (a)/(b), each already had its own prompt+solution in the source batch — only needed the shared item-level `:::prompt` (the table stem) explicitly closed before the parts began).

Verified via a full container-balance check (every `:::name{...}` open matched to exactly one bare `:::` close) and an explicit `part`-nested-inside-`prompt`/`solution` scan across the whole assembled file — both clean after the fix.
