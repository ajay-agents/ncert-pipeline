# Match report

- **questions:** 35
- **solutions:** 74
- **matched:** 35
## unmatched_questions (0)

## orphan_solutions (3)
- sol_1.3.1..14 (EXERCISE 1.3 in the solutions manual - composition/invertibility, old-edition content; the current textbook covers this only narratively via Examples 15-17, no separate numbered exercise)
- sol_1.4.1..13 (EXERCISE 1.4 in the solutions manual - Binary Operations, a topic entirely absent from the current rationalized textbook; contains the chapter's 5 real operation tables)
- sol_1.misc.{1,2,3,6,7,9,11,12,13,14,18,19} (12 of the solutions manual's 19 Miscellaneous Exercise items - the old edition had a larger Misc Exercise; only 7 of its 19 items match the current textbook's own 7-item Miscellaneous Exercise on Chapter 1)

## duplicate_solutions (0)

## needs_review (0)

## numbering_scheme_notes (2)
- Both source documents use local numbering that restarts at 1 inside each of several named blocks (EXERCISE 1.1, EXERCISE 1.2, and in the solutions manual only, EXERCISE 1.3 and EXERCISE 1.4) - a naive global join_solutions() call would collide across blocks via norm_num()'s chapter-prefixing. Resolved by hand: real exercises got one flat global number 1.1-1.35 in textbook reading order (16 from EX1.1 + 12 from EX1.2 + 7 from the Misc Exercise); orphans kept block-qualified ids (sol_1.3.N, sol_1.4.N, sol_1.misc.N) using their own local number as the suffix, so no id collisions even though local numbers repeat across blocks.
- Miscellaneous Exercise mapping (old solutions-manual local number -> new textbook local number): old4->new1, old5->new2, old8->new3, old10->new4, old15->new5, old16->new6, old17->new7. Verified by content match, not by number - the two documents' own Misc-exercise numbering does not correspond.

## garbled_source_notes (1)
- q_1.25 (EXERCISE 1.2 item 9 in chapter.en.md): the piecewise-function definition's own lead-in line ('9. Let f: N -> N be defined by f(n)=...') is missing from the mathpix source entirely - the item jumps straight into the fraction body. Transcribed exactly as the source prints it (Rule 5 - nothing invented); flagged for stage 5 to check against the actual textbook PDF page.

## table_notes (1)
- 5 real markdown tables found in the source (all inside the orphaned EXERCISE 1.4 / Binary Operations block: sol_1.4.3, sol_1.4.4 (two page-split fragments manually rejoined into one 6x6 table - same content, nothing changed), sol_1.4.5, sol_1.4.7). All preserved; none dropped.

## image_notes (1)
- 5 images in chapter.en.md, all genuine and each directly referenced by name (Fig 1.1 attached near Example 3; Fig 1.2 near the Types-of-Functions intro/Example 7 area; Fig 1.3 near Example 9; Fig 1.4 near Example 12; Fig 1.5 near the Composition-of-Functions intro/Example 15 area). No decorative or bogus images found (unlike physics-12-4-en).
