# Match report - maths-12-4-en

English-only build; no Hindi alignment needed.

## Numbering mismatch between current chapter and solutions manual

The solutions manual is built against a **pre-rationalisation edition** of
this chapter, which had SIX numbered exercises (4.1-4.6) plus a 19-item
Miscellaneous Exercise; the current rationalised textbook keeps only FIVE
exercises (4.1-4.5) plus a 9-item Miscellaneous Exercise. This is not a
simple "extra items appended at the end" case (like maths-12-3-en's own
Section D/E) - it's a whole-chapter **renumbering shift**, discovered by
comparing each solutions-manual section's own opening question against the
current chapter's own exercises by topic, not by number:

| current chapter | topic | old solutions-manual section | old count | current count |
|---|---|---|---|---|
| EXERCISE 4.1 | Evaluate determinants | EXERCISE 4.1 | 8 | 8 |
| *(none)* | Properties of determinants | EXERCISE 4.2 | 16 | - |
| EXERCISE 4.2 | Area of a triangle | EXERCISE 4.3 | 5 | 5 |
| EXERCISE 4.3 | Minors and cofactors | EXERCISE 4.4 | 5 | 5 |
| EXERCISE 4.4 | Adjoint and inverse | EXERCISE 4.5 | 18 | 18 |
| EXERCISE 4.5 | Consistency / solving via matrices | EXERCISE 4.6 | 16 | 16 |
| Misc Exercise | (mixed) | Misc Exercise | 19 | 9 |

Every renumbered pair above was spot-checked by content (not just count) -
first and last item of each section, plus at least one middle item for the
larger ones - before trusting the local-number-to-local-number join within
that pair. All matched cleanly.

**The old EXERCISE 4.2 (16 items, "Properties of determinants" - prove an
identity without expanding, etc.) has no counterpart anywhere in the
current chapter at all.** This whole exercise was cut in the 2023-24
rationalisation. Kept as additional_exercise items (`sol_4.d.1`-`sol_4.d.16`,
number="EX4.OLD-1".."EX4.OLD-16"), never discarded, per Rule 5.

**The Miscellaneous Exercise has 10 interspersed orphans, not a contiguous
cut block** - every one of the old section's 19 items was individually
content-matched against the current chapter's own 9 items:

- current 1 = old 1, current 2 = old 3, current 3 = old 7, current 4 = old 8,
  current 5 = old 9, current 6 = old 10, current 7 = old 16, current 8 =
  old 18, current 9 = old 19.
- Orphans (old numbers, no current counterpart): 2, 4, 5, 6, 11, 12, 13,
  14, 15, 17 - kept as `sol_4.misc.2`, `sol_4.misc.4`, ... `sol_4.misc.17`
  (id suffix preserves each orphan's own original old-manual local number
  for traceability), number="MISC-2".."MISC-17".

**A genuine rationalisation leftover, not an OCR error:** the current
textbook's own Misc Exercise still contains the sentence "Using properties
of determinants in Exercises 11 to 15, prove that:" sitting between its own
item 6 and item 7 - a stray instructional pointer to the old numbering
(items 11-15) that were cut from this edition entirely. Since it describes
no surviving item, it was treated as noise (like a stray page header) and
dropped rather than attached to item 7 (which is an unrelated "solve the
system of equations" question, not a "prove using properties" one). By
contrast, "Choose the correct answer in Exercise 17 to 19." (between items
7 and 8) genuinely still describes the two MCQs that survived as current
items 8 and 9 (old 18, old 19) - kept and prepended to both, transcribed
exactly as printed (stale old numbers and all), per "transcribe, don't fix."

## Mathpix extraction quality issues (not fixed, transcribed/flagged per Rule)

- **`chapter.en.md`'s opening epigraph and "4.1" heading line contain 41
  full-width CJK-style punctuation characters** (already flagged at stage 1)
  - confined to decorative front matter, does not affect any item's own
    content.
- **A cross-reference to "Example 21"** appears inside a Remark following
  Example 10 ("Expanding the determinant Delta, in Example 21, along R1...")
  - almost certainly a pre-rationalisation cross-reference to the OLD
    edition's own Example 21 (this chapter used to have more examples before
    some were cut), left exactly as printed per Rule 4/"transcribe, don't
    fix" - not an OCR digit error, a genuine textbook-numbering leftover
    exactly like the Misc Exercise's own stray instruction lines above.
- **EXERCISE 4.4's items 1-11 were severely garbled by mathpix** - several
  matrices lost their `\left[...\right]` delimiters entirely and mathpix
  then misread the bare matrix ROWS as numbered-list markers (e.g. raw
  mathpix text `"1.\n2.\n34\n-2 01\nVerify..."` for what should have been
  two clean 2x2/3x3 adjoint-matrix questions). Hand-reconstructed items 1-7
  directly from the actual PDF page images (textbook pages 16-17, 0-indexed)
  rather than from the unusable mathpix text - this is transcription from
  the source, not invention, the same as any other extraction; items 8-10
  were readable but also missing their brackets, fixed the same way as
  Example 15 below; item 11 was already correct.
- **A recurring bracket-drop pattern**: beyond EXERCISE 4.4's items 8-10,
  Example 15 and 6 further exercise items (EXERCISE 4.4's items 12, 13, 14,
  15, 16, and one MISC item) had a bare `\begin{array}...\end{array}`
  standing in for a matrix with no `\left[`/`\right]` around it - fixed by
  adding the missing delimiters (a meaning-preserving, mechanical fix, not
  a content change) after confirming via a general sweep across every
  extracted item, not just the ones spotted by eye. **One real bug caught
  and fixed during that sweep**: the first version of this fix's own regex
  didn't exclude determinant bars (`\left|...\right|`) as "already
  delimited", so it wrongly wrapped 3 genuine determinant expressions in an
  extra pair of square brackets (`\left|\left[...\right]\right|`) - caught
  by spot-checking q_4.1 against its own solution, fixed by excluding
  `\left|`/`\right|` from the bracket-drop detector, and reconfirmed with a
  zero-count sweep across both examples.en.md and qa.en.md before trusting
  the final assembly.
- **EXERCISE 4.4 item 15's own mathpix text has a stray garbled fragment**
  (`$$\n2-11\n$$`) immediately after its real content - kept as-is per
  "keep it broken and continue", flagged here for stage 5.
- **EXERCISE 4.4 item 16's matrix appears to be missing its first row** -
  mathpix extracted only a 2x3 array `[[-1,2,-1],[1,-1,2]]`, but the
  solutions manual's own transcription of the same matrix (old EXERCISE
  4.5's local item 16) shows a 3x3 matrix `[[2,-1,1],[-1,2,-1],[1,-1,2]]`.
  Left exactly as mathpix extracted it (a content-completeness question is
  stage 5's job, checked against the actual PDF page, not inferred here
  from the solutions manual as an unverified secondary source) - flagged
  clearly for stage 5's attention.

## Items with empty solution

None - all 61 real exercise items (across the renumbered EXERCISE
4.1-4.5 and the 9-item Misc Exercise) have a matched, non-empty solution.
All 19 examples have their own textbook-provided solution too (unlike
maths-12-3-en, this chapter has no "question and result stated as one
continuous sentence, no separate Solution" example).
