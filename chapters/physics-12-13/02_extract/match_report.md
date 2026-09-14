# Match report

- **questions:** 10
- **raw_solutions_in_solutions_hi_md:** 31
- **matched:** 10
## unmatched_questions (0)

## orphan_solutions (21)
- 1
- 2
- 6
- 7
- 8
- 9
- 10
- 12
- 13
- 14
- 18
- 22
- 23
- 24
- 25
- 26
- 27
- 28
- 29
- 30
- 31

## duplicate_solutions (0)

## needs_review (0)

- **bare_numbering_collision_confirmed:** solutions.hi.md numbers its questions bare (1..31, no chapter prefix); this chapter's own rationalised exercises are printed 13.1..13.10 (with a dot) so norm_num() does NOT prefix them, but a bare raw solutions number DOES get chapter-prefixed onto "13.<n>" - since raw numbers 1-10 all exist in the solutions manual, EVERY ONE of this chapter's 10 real exercises collides with an unrelated raw entry of the same bare number, not just a few of them. Concretely: exercise 13.1 (Nitrogen-14 binding energy) would silently receive raw "प्रश्न 1" (a Lithium-isotope-abundance problem)'s solution instead of its real match, raw "प्रश्न 3"; exercise 13.3 (the coin problem) would receive raw "प्रश्न 3" (Nitrogen) instead of its real match, raw "प्रश्न 5"; and so on through 13.10. needs_review would stay empty throughout, since every number "matches" something - exactly the physics-12-11/12-12 failure mode. The merge actually used in chapter.hi.md was instead built entirely by hand, one pair at a time, content-verified against both the chapter's own exercise text and the solutions manual's worked answer (matching distinctive data values - masses, mass numbers, energies) - see correct_mapping_exercise_to_raw_solutions_number below.
- **correct_mapping_exercise_to_raw_solutions_number:** {'13.1': 3, '13.2': 4, '13.3': 5, '13.4': 11, '13.5': 15, '13.6': 16, '13.7': 17, '13.8': 19, '13.9': 20, '13.10': 21}
## orphan_raw_solutions_numbers (21)
- 1
- 2
- 6
- 7
- 8
- 9
- 10
- 12
- 13
- 14
- 18
- 22
- 23
- 24
- 25
- 26
- 27
- 28
- 29
- 30
- 31

## cross_document_or_ocr_flags_for_stage_5 (6)
- q_13.4 / sol 11: solutions.hi.md prints Au as Z=78 ('{ }_{78}^{197} Au'); chapter's own exercise 13.4 and main text both print Z=79. Likely OCR digit error in the solutions PDF (or an original textbook typo) - doesn't affect the numeric answer (only mass numbers 197/107 are used in the R∝A^(1/3) ratio), but must be confirmed against the actual solutions PDF page at stage 5, not silently 'fixed' here.
- q_13.4 / sol 11: solutions.hi.md's ratio line shows the exponent as '{}^{13}' ('(197/107)^{13}=1.225') - almost certainly OCR-glued '1/3' -> '13' (matches step_10/PROMPT.md's documented superscript-merge failure mode, here happening at OCR time instead of PDF-export time). 1.225 is only consistent with an exponent of 1/3, not 13. Flagged for stage 5 correction against the source PDF, not fixed here (extraction transcribes broken LaTeX as-is).
- q_13.5 (ii) / sol 15: OCR shows a garbled CJK-like glyph before 'ंकि ऊर्जा धनात्मक है' in the source solutions.hi.md ('絜ंकि' instead of 'चूँकि'). Transcribed here as the intended 'चूँकि' (an unambiguous OCR garble of a common connector word, not a content/number field) - flag for stage 5 re-confirmation against the PDF.
- q_13.6 / sol 16: solutions.hi.md prints the Fe mass number as '{ }_{26}^{66} Fe' (A=66) in one spot while using A=56 correctly everywhere else in the same solution and matching the chapter's own exercise 13.6 (A=56 throughout). Treated as an isolated OCR digit swap (66->56), not transcribed into the extracted item - flag for stage 5 to confirm against the PDF page directly.
- q_13.7 / sol 17: solutions.hi.md's final result line gives the unit as 'MW' ('=4.53 x 10^26 MW') where every surrounding step computes in MeV and the question asks 'kitni MeV urja'. Extracted here as printed (MW) per stage-2 rule (transcribe, don't fix) - SAME-PAGE self-contradiction candidate for stage 5's standing authorization (unit wrong for the kind of quantity, derivation directly above already correct) - confirm against the source PDF page first, then correct to MeV if confirmed.
- q_13.10 / sol 21: solutions.hi.md's density derivation substitutes R0=1.1x10^-15 m, but the chapter's own main text (section 13.3) and exercise 13.10's own given constant both state R0=1.2 fm. This is a CROSS-DOCUMENT disagreement (question/chapter says 1.2, solutions manual computes with 1.1), not a same-page self-contradiction - per standing instructions, left EXACTLY as printed in each source, not resolved unilaterally, and flagged prominently here for stage 5 to document (not fix) in corrections.md.
