# Match report

- **chapter:** maths-12-2
- **lang:** en
- **items_total:** 49
- **examples:** 6
- **exercise_2_1:** 14
- **exercise_2_2:** 15
- **miscellaneous_exercise:** 14
- **figures:** 0
- **method:** HAND-BUILT merge, not match.join_solutions(). EXAMPLES and EXERCISE 2.1 are clean 1:1 matches by printed number (content-verified). EXERCISE 2.2 and MISCELLANEOUS EXERCISE ON CHAPTER 2 each have MORE solutions-manual questions than chapter items, with the extra orphaned questions from an older/unrationalised edition INTERSPERSED (not trailing) throughout the numbering - the same 'physics-12-3/12-5' trap step_2/PROMPT.md warns about. A plain number-based join would have silently mispaired every item from the first orphan onward in each section. Instead, every solutions-manual entry in both sections was read and content-matched against the chapter's own text one at a time; the verified mapping is recorded in stage 1's manifest entry and in this pipeline's memory file (chapter_maths_12_2.md).
- **id_scheme_note:** EXERCISE 2.1 and EXERCISE 2.2 are both printed 1..N within this chapter, so ids use a section-scoped scheme (q_2.1.N for EXERCISE 2.1, q_2.2.N for EXERCISE 2.2, q_2.3.N for the Miscellaneous Exercise) to avoid collision; each item's own number= field still holds its true printed number within its own section, unaffected by the id.
## orphaned_solutions_not_extracted (9)
- EXERCISE 2.2 solutions Q3: tan^-1(2/11)+tan^-1(7/24) - no chapter counterpart
- EXERCISE 2.2 solutions Q4: 2*tan^-1(1/2)+tan^-1(1/7) - no chapter counterpart
- EXERCISE 2.2 solutions Q6: tan^-1(1/sqrt(x^2-1)) - no chapter counterpart
- EXERCISE 2.2 solutions Q12: cot(tan^-1 a + cot^-1 a) - no chapter counterpart
- EXERCISE 2.2 solutions Q14: sin(sin^-1(1/5)+cos^-1 x)=1 - no chapter counterpart
- EXERCISE 2.2 solutions Q15: tan^-1((x-1)/(x-2))+tan^-1((x+1)/(x+2))=pi/4 - no chapter counterpart
- MISC EXERCISE solutions Q8: tan^-1(1/5)+tan^-1(1/7)+tan^-1(1/3)+tan^-1(1/8)=pi/4 - no chapter counterpart
- MISC EXERCISE solutions Q12: 9pi/8 - (9/4)sin^-1(1/3) = (9/4)sin^-1(2sqrt2/3) - no chapter counterpart (also flagged at stage 1 as possibly truncated in mathpix output; worth a direct PDF re-check at stage 5 regardless)
- MISC EXERCISE solutions Q17: tan^-1(x/y)-tan^-1((x-y)/(x+y)) multiple choice - no chapter counterpart

## flagged_for_stage_5 (5)
- q_2.1.11 (EXERCISE 2.1 item 11): mathpix dropped the \left(...\right) wrapping around a negated fraction in the question text (\tan^{-1}(1)+\cos^{-1}-\frac{1}{2}+\sin^{-1}-\frac{1}{2} instead of the correctly-parenthesized form) - preserved verbatim per extract discipline, needs correction at stage 5
- q_2.2.1 solution (EXERCISE 2.2 item 1, from sol.Q1): genuinely garbled mathpix OCR ('x=8in', 'sin4(sinsin-', 'sin3' etc. are not valid math) - needs full reconstruction from the source PDF page at stage 5
- q_2.2.2 solution (EXERCISE 2.2 item 2, from sol.Q2): same class of garbled OCR ('x=theta_os', 'tos^-1(x)=', etc.) - needs full reconstruction from the source PDF page at stage 5
- q_2.2.10 solution (from sol.Q16) and q_2.2.11 solution (from sol.Q17): each has one garbled opening line ('Since, theta_in sin(theta-)' / 'Since, tan tan(theta-)') before the derivation continues correctly - needs a source-PDF check at stage 5
- q_2.3.8 solution (Misc Exercise item 8, from sol.Q9): final line reads '=I.HS' where it should read '=LHS' - minor OCR glyph confusion, needs correction at stage 5

## needs_review (0)
