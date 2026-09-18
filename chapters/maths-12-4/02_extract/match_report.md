# Match report — maths-12-4

- **chapter:** maths-12-4 (सारणिक / Determinants)
- **language:** Hindi-only (no chapter.en.pdf / solutions.en.pdf supplied)
- **examples_extracted:** 19 (ex_4.1–ex_4.19)
- **prashnavali_4.1_extracted:** 8 (q_4.1.1–q_4.1.8)
- **prashnavali_4.2_extracted:** 5 (q_4.2.1–q_4.2.5)
- **prashnavali_4.3_extracted:** 5 (q_4.3.1–q_4.3.5)
- **prashnavali_4.4_extracted:** 18 (q_4.4.1–q_4.4.18)
- **prashnavali_4.5_extracted:** 16 (q_4.5.1–q_4.5.16)
- **misc_exercise_extracted:** 9 (q_4.9.1–q_4.9.9)
- **total_items:** 80
- **gate_counts:** PASS (0 failures)
- **gate_solutions_present_hi:** PASS (0 failures, every item has a non-empty solution)
- **gate_bilingual:** N/A as expected for Hindi-only — all 80 items flagged missing a language (by design)

## Worked examples (ex_4.1–ex_4.19)

All 19 examples' solutions taken directly from chapter.hi.md itself (the textbook's own worked solution), never matched against solutions.hi.md, per standard convention — NCERT worked examples always carry their own textbook solution and the separate solutions manual only covers exercises (प्रश्नावली). Exhaustively grepped chapter.hi.md to confirm the chapter has exactly 19 examples (see "known source-side issues" below re: ex_4.10's apparent self-reference to "उदाहरण 21").

## प्रश्नावली 4.1 — clean 1:1 number match (no drift)

All 8 items (q_4.1.1..q_4.1.8) matched solutions.hi.md's own प्रश्नावली 4.1, प्रश्न 1-8 directly by number and content — no drift in section numbering. (Item 6 has a sign discrepancy between the chapter's own printed matrix and the matching solution's computation — see below.)

## प्रश्नावली 4.2 (current) ↔ प्रश्नावली 4.3 (solutions) — uniform +1 exercise-number shift begins here

All 5 items (q_4.2.1..q_4.2.5, त्रिभुज क्षेत्रफल/संरेखता/रेखा-समीकरण) matched solutions.hi.md's own "प्रश्नावली 4.3" (not "4.2") content-for-content, item-for-item — confirmed by direct comparison of every problem statement, not by number alone. This is the first exercise after the point where the current (rationalized) edition's numbering diverges from the solutions manual's numbering by exactly +1 — see the "whole-exercise orphan" note below for why.

## प्रश्नावली 4.3 (current) ↔ प्रश्नावली 4.4 (solutions)

All 5 items (q_4.3.1..q_4.3.5, उपसारणिक/सहखंड) matched solutions.hi.md's own "प्रश्नावली 4.4" content-for-content — same +1 shift as above. Item 5's MCQ option (A) wording differs slightly between chapter and solutions — see below.

## प्रश्नावली 4.4 (current) ↔ प्रश्नावली 4.5 (solutions)

All 18 items (q_4.4.1..q_4.4.18, सहखंडज/व्युत्क्रम) matched solutions.hi.md's own "प्रश्नावली 4.5" content-for-content — same +1 shift. Item 11 required a reconstructed line — see below, flagged prominently.

## प्रश्नावली 4.5 (current) ↔ प्रश्नावली 4.6 (solutions)

All 16 items (q_4.5.1..q_4.5.16, संगत/असंगत निकाय + आव्यूह विधि से हल) matched solutions.hi.md's own "प्रश्नावली 4.6" content-for-content — same +1 shift. Items 10-14's question text in chapter.hi.md was OCR-scrambled (a 3-column page layout interleaved different items' equation lines); reconstructed by rendering chapter.hi.pdf pages 24-25 directly via PyMuPDF and reading the actual page image, then cross-validated against solutions.hi.md's own (non-scrambled) restatement of each item's question inside its solution — all reconstructions matched exactly, item for item.

## Whole-exercise orphan: solutions' own "प्रश्नावली 4.2" (16 items) has NO counterpart in the current chapter

solutions.hi.md contains a full exercise of its own, labelled "प्रश्नावली 4.2" (16 items, प्रश्न 1-16, covering "properties of determinants without expansion" — evaluating determinants purely via row/column operations and standard properties), positioned between solutions' प्रश्नावली 4.1 and what it itself labels प्रश्नावली 4.3. **This entire exercise has no counterpart anywhere in the current chapter.hi.md** — the rationalized 2026-27 edition dropped this exercise from the chapter entirely. This is why every subsequent solutions-side प्रश्नावली number is offset by exactly +1 relative to the current chapter's own numbering (current 4.2 ↔ solutions 4.3, current 4.3 ↔ solutions 4.4, current 4.4 ↔ solutions 4.5, current 4.5 ↔ solutions 4.6). All 16 of solutions' प्रश्नावली 4.2 items are discarded per Rule 5 — never merged, renumbered, or invented into the current item set.

## अध्याय 4 पर विविध प्रश्नावली (misc, kind=additional_exercise) — hand-verified content mapping used, NOT plain number-match

The current chapter's misc section has 9 items; solutions.hi.md's own misc section ("अध्याय 4 पर विविध प्रश्नावली") has 19 items (प्रश्न 1-19). The mapping is non-uniform (unlike the exercises above, it is not a simple offset) — every one of the current 9 items was matched to its solutions counterpart by direct content comparison, not by position. Used the id slot `q_4.9.<n>` (kind=`additional_exercise`) — deliberately unused, since content sections run 4.1-4.6 and the five numbered exercises are 4.1-4.5 (with the discarded old-edition "4.2"-in-solutions label never colliding, since it is never used as a current-chapter section number), so 4.9 avoids any collision:

| chapter id | chapter content (short) | solutions प्रश्न # |
|---|---|---|
| q_4.9.1 | सारणिक (x,sinθ,cosθ की पंक्तियों वाला) θ-स्वतंत्र सिद्ध करना | 1 |
| q_4.9.2 | cos α cos β / cos α sin β / -sin α आदि प्रविष्टियों वाले सारणिक का मान | 3 |
| q_4.9.3 | A⁻¹, B दिए हों तो (AB)⁻¹ ज्ञात करना | 7 |
| q_4.9.4 | (adj A)⁻¹=adj(A⁻¹) तथा (A⁻¹)⁻¹=A का सत्यापन | 8 |
| q_4.9.5 | \|x,y,x+y; y,x+y,x; x+y,x,y\| का मान | 9 |
| q_4.9.6 | \|1,x,y; 1,x+y,y; 1,x,x+y\| का मान | 10 |
| q_4.9.7 | 2/x+3/y+10/z=4 आदि निकाय हल करना (1/x,1/y,1/z में आव्यूह विधि) | 16 |
| q_4.9.8 | MCQ विकर्ण आव्यूह diag(x,y,z) का व्युत्क्रम | 18 |
| q_4.9.9 | MCQ sinθ वाले आव्यूह के सारणिक का परिसर | 19 |

**Orphan solutions discarded (genuine old-edition-only content, per Rule 5 — not invented into placeholder questions):** प्रश्न 2 (सारणिक-प्रसरण बिना सिद्ध करना, `[a,a²,bc;...]=[1,a²,a³;...]`), प्रश्न 4 (b+c,c+a,a+b रूप का सारणिक शून्य ⇒ a+b+c=0 या a=b=c), प्रश्न 5 (x+a,x,x रूप वाले सारणिक का समीकरण x के लिए हल करना), प्रश्न 6 (a²,bc,ac+c² रूप सिद्ध करना =4a²b²c²), प्रश्न 11 (α,α²,β+γ रूप का गुणनखंडन सिद्ध करना), प्रश्न 12 (x,x²,1+px³ रूप का गुणनखंडन सिद्ध करना), प्रश्न 13 (3a,-a+b,-a+c रूप सिद्ध करना =3(a+b+c)(ab+bc+ca)), प्रश्न 14 (1,1+p,1+p+q रूप सिद्ध करना =1), प्रश्न 15 (sinα,cosα,cos(α+δ) रूप सिद्ध करना =0), प्रश्न 17 (MCQ — a,b,c समान्तर श्रेढ़ी में हों तो सारणिक का मान). All ten are "prove without expansion" / algebraic-identity determinant problems with no counterpart among the current chapter's 9 misc items — consistent with the current edition's general removal of "properties without expansion" content from this chapter (the same topic dropped wholesale as the whole-exercise orphan above).

## Known source-side issues transcribed verbatim (not fixed at this stage)

- **ex_4.19**: the problem statement (chapter.hi.md) gives matrices with different signs than its own solution computation — problem states `[[1,1,2],[0,2,3],[3,2,4]]` × `[[2,0,1],[9,2,3],[6,1,2]]` but the solution's actual arithmetic uses `[[1,-1,2],[0,2,-3],[3,-2,4]]` × `[[-2,0,1],[9,2,-3],[6,1,-2]]`, and the stated final answer (x=0, y=5, z=3) only checks out against the negative-sign version. Transcribed the chapter's own (positive) problem text per Rule 5 and the solution's actual (negative-sign) computation as printed; flagged for stage 5 to check against both source PDFs' page images. ex_4.19 also has a `^{1}` in the source where `^{-1}` (inverse) was clearly intended — transcribed as printed, flagged.
- **q_4.1.6**: the chapter's own printed matrix A=[[1,1,2],[2,1,3],[5,4,9]] (all positive third column) does not match the solution's actual computation, which clearly operates on A=[[1,1,-2],[2,1,-3],[5,4,-9]] (negative third column) — the solution's arithmetic "1(-9+12)-1(-18+15)-2(8-5)=3+3-6=0" only works with the negative-sign version. Transcribed the chapter's own (positive) printed text for the question per Rule 5; flagged for stage 5.
- **q_4.3.5**: the MCQ's option (A) wording differs slightly between chapter.hi.md ("a₁₁A₃₁+a₁₂A₃₂+a₁₃A₃₃") and solutions.hi.md ("a₁₁A₁₁+a₁₂A₃₂+a₁₃A₃₃") — transcribed the chapter's own option text; the correct answer (D) is unaffected either way. Flagged for stage 5.
- **q_4.4.11**: solutions.hi.md's own solution has a corrupted/garbled OCR line — one of the cofactor values was replaced by unreadable characters ("A_{31}=0 住 伎 α" — literal CJK-looking glyphs in place of what should be A₃₂ and A₃₃). **Reconstructed** A₃₂=-sinα and A₃₃=cosα by cross-deriving them from the SAME solution's own immediately-following, clearly-legible restatement of adj(A) (`adj A=[[1,0,0],[0,-cosα,-sinα],[0,-sinα,cosα]]`) — not invented, but derived from the same document's own later-stated result. This is a deviation from pure "transcribe as printed" discipline; **flagged prominently for stage 5 to verify the reconstructed line against the actual solutions.hi.pdf page image** before it is trusted further downstream.
- **q_4.9.3** and **q_4.9.4** (misc items 3 and 4): same sign-discrepancy pattern as ex_4.19/q_4.1.6 above. Chapter's own printed matrices are all-positive (item 3: A⁻¹=[[3,1,1],[15,6,5],[5,2,2]], B=[[1,2,2],[1,3,0],[0,2,1]]; item 4: A=[[1,2,1],[2,3,1],[1,1,5]]), but the matching solutions (प्रश्न 7 and प्रश्न 8) both operate throughout on matrices with several negative entries in the same positions (item 3: A⁻¹=[[3,-1,1],[-15,6,-5],[5,-2,2]], B=[[1,2,-2],[-1,3,0],[0,-2,1]]; item 4: A=[[1,-2,1],[-2,3,1],[1,1,5]]). Transcribed the chapter's own printed question text per Rule 5, and the solution's actual computation (which only checks out with the negative-sign versions) verbatim. Flagged for stage 5 — this looks like the same systematic OCR sign-drop pattern affecting chapter.hi.md specifically (never solutions.hi.md), seen now in four separate items across this chapter (ex_4.19, q_4.1.6, q_4.9.3, q_4.9.4).
- **ex_4.5**: the solution text has a duplicated/garbled line ("अर्थात्\nअर्थात्") — a genuine OCR artifact, transcribed as-is.
- **ex_4.10**: the solution's own टिप्पणी (remark) contains a self-reference reading "उदाहरण $21$". After reading the surrounding context, concluded this is an OCR misread of "उदाहरण 10" (the example referring to itself), not a genuine 20th/21st example — the chapter has exactly 19 examples (exhaustively confirmed via grep). Transcribed as printed; flagged for stage 5.

## Images (out of scope for extraction, per stage-1 manifest note)

Both images extracted at stage 1 (`fig_maths-12-4_0.jpg`, a decorative P.S. Laplace portrait in the भूमिका intro; `fig_maths-12-4_1.jpg`, an adjugate-swap-rule diagram in the "4.3 सहखंडज" subsection's own टिप्पणी) sit in theory/intro sections, never inside any उदाहरण or exercise item — correctly excluded from every item extracted here, same pattern as maths-12-3.

## Structural notes

No invalid container nesting was found during assembly (unlike maths-12-3's stage 2, which needed two structural fixes) — a full container-balance check (every `:::name{...}` open matched to exactly one bare `:::` close, depth never negative, final depth 0) passed clean on the first assembly of all eight batches (ex1-10, ex11-19, q41, q42, q43, q44, q45, q49) into `chapter.hi.md`. `gate_counts` and `gate_solutions_present("hi")` both pass with zero failures against the assembled 80-item chapter.
