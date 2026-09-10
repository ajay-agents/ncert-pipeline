# Corrections — physics-12-4

All 25 items (12 examples against `00_raw/chapter.hi.pdf`, 13 exercise
solutions against `00_raw/solutions.hi.pdf`) verified via 3 dispatched
sub-agent batches following `step_5/verify.md`, plus 2 items found and
fixed directly by the coordinator. Every fix below was independently
re-confirmed against the actual source page before being applied — none
were taken on the sub-agent's word alone. Because these were caught
before `02_extract`'s own output was treated as finalized, they were
applied directly to the extraction and stages 2-4 were rebuilt from the
corrected version, rather than round-tripped through a separate
`Correction`/`apply_corrections()` pass (see the `extract_match`,
`split` and `combine` manifest entries for the full detail this file
summarizes).

## Applied corrections

- **ex_4.5, part (a)**: `\mathrm{d} l \times \mathbf{r}=O` → `=0` — a
  math-italic zero misread as Latin "O" (confirmed at 1200dpi zoom;
  physics context — cross product of parallel vectors — makes this
  unambiguously zero).
- **ex_4.10, part (d)**, 3 corrections: the coil's moment-of-inertia
  symbol (a script letter, `$\mathscr{I}$`, used correctly twice in this
  same derivation) was OCR-misread as "g" once and digit "9" twice.
  All three corrected to the consistent symbol.
- **ex_4.11, part (a)**: `ऊधर्वाधर` (transposed letters, not a real
  word) → `ऊर्ध्वाधर` ("vertical") — confirmed against the correct
  spelling used later in the same source sentence.
- **ex_4.6**: removed a misattached figure (चित्र 4.12 /
  `fig_physics-12-4_9.jpg`) — confirmed against the source that this
  figure belongs to section 4.6's own explanatory narrative (introducing
  Ampere's circuital law), not to Example 4.6 itself, which has no
  figure of its own.
- **ex_4.9**: restructured from one combined item into 2 parts (a)/(b) —
  the source prompt telescopes "(a) पूर्व से पश्चिम...(b) दक्षिण से
  उत्तर..." into one sentence, but the solution computes two fully
  independent numeric results; split for consistency with every other
  multi-case item in this chapter (confirmed against the source that the
  restructured content is accurate, not just re-shaped).

## Checked and confirmed clean (no correction needed)

- ex_4.1–ex_4.4, ex_4.7, ex_4.8, ex_4.9 (main body), ex_4.10 parts (a)(b)(c),
  ex_4.11 parts (b)(c), ex_4.12 — all numbers, units, sub-parts and
  figures verified against the actual chapter PDF pages, matching exactly.
- All 13 exercises (q_4.1–q_4.13), including q_4.9's and q_4.13's
  labelled sub-parts — verified against the actual solutions-manual PDF
  pages, matching exactly.

## Genuine textbook errata — confirmed, left uncorrected

Per `step_5/verify.md`'s rule ("if the textbook has an error, that is
not your call"), each of the following was independently confirmed
(via a zoomed render of the actual page) to be printed identically in
the source itself, not an extraction/OCR fault:

- **q_4.1**: given-line reads `r = 8 cm = 8 × 10⁻² cm` (should physically
  read `m`, not `cm`) — a genuine unit typo in the solutions manual.
- **q_4.6**: given-line states `B = 0.2 T` while the question and the
  rest of the derivation correctly use `0.27 T` — a genuine given-value
  discrepancy in the solutions manual (not the narrow final-answer
  unit-slip exception, since this is a given-value mismatch, not a
  concluding-sentence unit contradiction).
- **ex_4.12, part (b)**: prints a stray `- 0.02 Ω` where `≈ 0.02 Ω` is
  clearly meant — confirmed identical on the source page.

## Gates

`gate_counts` and `gate_solutions_present` both pass on the corrected,
rebuilt chapter (12 examples, 13 exercises, no item with an entirely
missing solution).
