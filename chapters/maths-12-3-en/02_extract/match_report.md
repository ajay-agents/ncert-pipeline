# Match report - maths-12-3-en

English-only build; no Hindi alignment needed.

## Numbering mismatch between current chapter and solutions manual

The solutions manual restarts its own local numbering per exercise section (1-10, 1-22, 1-12, 1-18, 1-15) rather than using the flat chapter-wide numbering this pipeline assigns. Exercises 3.1/3.2/3.3 (sections A/B/C, local counts 10/22/12) match the current chapter exactly and were joined by plain number match - spot-checked byte-for-byte correct on three distinctive items (A#1's specific matrix elements, B#5's fraction matrices, C#7's specific symmetric/skew-symmetric matrices) before trusting the rest.

**Section D (18 items) does not correspond to the current Exercise 3.4 at all** - the current chapter keeps only 1 item in Exercise 3.4 (a single MCQ about matrix inverses), but the solutions manual's own 4th section has 18 items, 17 of which are an entirely different "elementary transformation" (row-reduction) exercise for finding matrix inverses - a topic absent from the current rationalised textbook chapter altogether (confirmed: no such section exists anywhere in chapter.en.md). Only the LAST item (D#18) matches the current Exercise 3.4's own MCQ text ("Matrices A and B will be inverse of each other only if...") - verified by exact phrase match ("inverse of each other" appears exactly once in the whole solutions document, at this position). D#1-17 are kept as orphaned additional_exercise items (sol_3.d.1 - sol_3.d.17, number="EX3.OLD-1".."EX3.OLD-17"), not discarded, per Rule 5.

**Section E (15 items) has orphans interspersed, not just appended.** The current chapter's Miscellaneous Exercise has 11 items; the solutions manual's Misc section has 15. Every one of the 15 was individually read and matched by content (not position): E#1 ("(aI+bA)^n" induction), E#2 (all-ones matrix power induction) and E#3 (a specific 2x2 matrix power induction) are three orphaned induction-proof questions that come BEFORE any of the current chapter's own Misc items; E#4-E#11 then match the current chapter's Misc items 1-8 exactly, in order; E#12 ("AB=BA implies AB^n=B^nA by induction") is a FOURTH orphan interspersed in the middle, between what would otherwise be a contiguous run; E#13-E#15 then match the current chapter's Misc items 9-11 exactly. All 4 orphans kept as additional_exercise items (sol_3.misc.1, sol_3.misc.2, sol_3.misc.3, sol_3.misc.12 - id suffix preserves the solutions manual's own original local number for traceability), number="MISC-1"/"MISC-2"/"MISC-3"/"MISC-12".

## Items with empty solution

None - all 56 real exercise items have a matched, non-empty solution.
