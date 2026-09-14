# Match report - physics-12-14 (Hindi-only)

## chapter

physics-12-14

## lang

hi

## questions_in_chapter_exercises

6

## raw_solutions_in_manual

19

## matched

6

## matched_pairs

- q_14.1 <- प्रश्न 1 (content-verified: n-type Si MCQ, same statements)
- q_14.2 <- प्रश्न 2 (content-verified: p-type Si MCQ referencing 14.1's options)
- q_14.3 <- प्रश्न 3 (content-verified: C/Si/Ge band-gap MCQ, identical options)
- q_14.4 <- प्रश्न 4 (content-verified: unbiased p-n junction hole diffusion MCQ)
- q_14.5 <- प्रश्न 5 (content-verified: forward-bias barrier-potential MCQ)
- q_14.6 <- प्रश्न 8, NOT प्रश्न 6 (content-verified: both ask half-wave/full-wave rectifier output frequency for 50 Hz input; a blind norm_num join on bare numbering would have wrongly paired q_14.6 with प्रश्न 6, an unrelated transistor-action MCQ - see needs_review note below)

## needs_review

- Blind number-join risk: solutions.hi.md numbers its own entries bare ('प्रश्न 6', 'प्रश्न 8', ...) which match.norm_num(chapter='14') would prefix to '14.6'/'14.8' etc. '14.6' collides directly with this chapter's own real exercise 14.6, but the actual content match is प्रश्न 8, not प्रश्न 6 - resolved here by hand, by content (see matched_pairs above), exactly the pattern CLAUDE.md/step_2 warn about.

## orphan_solutions (present in solutions manual, no counterpart in this rationalised chapter - NOT merged into any item, Rule 5)

- प्रश्न 6 - transistor action (base/emitter/collector doping) MCQ
- प्रश्न 7 - transistor-amplifier voltage-gain-vs-frequency MCQ
- प्रश्न 9 - CE-transistor amplifier calc (Rout=2k, gain=100, Rin=1k)
- प्रश्न 10 - cascaded two-stage amplifier gain calc
- प्रश्न 11 - p-n photodiode 2.8 eV band-gap / 6000 nm detection check
- प्रश्न 12 - Si doped with As+In simultaneously, electron/hole count (distinct from Example 14.2, which only dopes with As)
- प्रश्न 13 - intrinsic semiconductor conductivity ratio at 600K vs 300K
- प्रश्न 14 - p-n junction diode current equation, 4 sub-parts (I0, forward/reverse bias, dynamic resistance)
- प्रश्न 15 - OR-gate/AND-gate circuit identification from NOT+diode gates (truth tables, 2 figures)
- प्रश्न 16 - NAND-gate circuit truth table
- प्रश्न 17 - two NAND-gate circuits, logic operation identification (2 truth tables)
- प्रश्न 18 - NOR-gate circuit truth table
- प्रश्न 19 - two NOR-gate-only circuits, logic identification (2 truth tables)

## why_this_scale_of_mismatch

- This rationalised chapter.hi.md stops at section 14.7 (rectifier application) plus summary/'विचारणीय विषय' and 6 exercises (14.1-14.6). It never covers sections on Zener diode, LED/photodiode/solar cell, transistors, amplifiers, oscillators, or digital electronics/logic gates - all of which the (unrevised) solutions manual still carries answers for (प्रश्न 6,7,9-19). This matches the documented physics-12-5 pattern: an entire prior edition's worth of orphaned solutions-manual content for sections the 2023-24 rationalisation cut from the chapter outright.
- Practical consequence for later stages: the ~60 solutions.hi.md table rows flagged at stage 1 (logic-gate truth tables) belong ENTIRELY to orphaned प्रश्न 15-19 and will NOT appear anywhere in this chapter's final item set - none of the matched exercises (14.1-14.6) are logic-gate questions. Likewise 37 of this chapter's 38 mathpix images belong either to orphaned solutions content (fig indices ~19-37, all logic-gate circuit diagrams) or to general chapter exposition never tied to a specific example/exercise number - only 1 image (fig_physics-12-14_16.jpg, चित्र 14.17) is actually item-referenced, by ex_14.4.

## flags_for_stage_5

- ex_14.2's solution text reads with a scrambled sentence order (mathpix artifact) - transcribed verbatim per stage-2 rule; needs re-derivation/reordering against the source PDF page, and its final_answer (left empty here) needs to be resolved from the PDF (n_e = N_D = 5x10^22 m^-3 is implied but never stated as its own sentence in the extracted text; n_h ~= 4.5x10^9 m^-3 is explicit).
- q_14.2's matched solution (प्रश्न 2) gives descriptive reasoning but no explicit option letter, unlike every sibling MCQ item - possible dropped '(d)' in mathpix OCR (my own content check: the description given, 'electron minority + hole majority from trivalent doping', matches option (d) of the chapter's own MCQ, not (b)) - CONFIRM against the actual solutions PDF page before setting final_answer; left empty here rather than invented.
- SAME-PAGE SELF-CONTRADICTION FLAG (q_14.3, प्रश्न 3): boxed answer '(c)' states (E_g)_C > (E_g)_Si > (E_g)_Ge (Ge smallest), matching the chapter's own explicit summary data (C=5.4eV, Si=1.1eV, Ge=0.7eV) - but the solution's own explanatory sentence says 'Si के लिए न्यूनतम' (Si is smallest), contradicting both its own boxed letter and the chapter body. Per standing authorization for confidently-diagnosed same-page self-contradictions: fix 'Si के लिए न्यूनतम' -> 'Ge के लिए न्यूनतम' at stage 5, AFTER confirming against the actual solutions PDF page image (not fixed here at stage 2 - transcribed verbatim, flagged for stage 5).

