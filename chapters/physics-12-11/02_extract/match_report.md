# Match report — physics-12-11 (Hindi-only)

## Summary

- Language: Hindi only (`chapter.hi.pdf` / `solutions.hi.pdf`; no English source).
- Examples extracted from `chapter.hi.md`: **3** (उदाहरण 11.1–11.3).
- Exercises extracted from `chapter.hi.md` ("## अभ्यास" section only — this
  rationalised chapter has no separate "अतिरिक्त प्रश्न"/additional-exercises
  block): **11** (11.1–11.11).
- Raw solutions-document entries extracted from `solutions.hi.md`
  ("प्रश्नावली" प्रश्न 1–19 + "विविध प्रश्नावली" प्रश्न 20–37): **37**.
- Matched (hand-verified by content): **11**.
- Orphaned solutions-manual entries (discarded, not part of this chapter's
  item set): **26**.

## The automated `join_solutions()` result was wrong and was not used

`solutions.hi.md` numbers its entries bare ("1", "2", … "37"), which
`match.norm_num()` chapter-prefixes to `"11.1"`–`"11.37"` since none of
those bare numbers contain a `.`. The chapter's own exercises are already
numbered `"11.1"`–`"11.11"`. A naive number join therefore "matches" every
single chapter exercise — but from `11.5` onward every one of those
matches is wrong, because the solutions manual is an older, un-rationalised
edition whose problem set does not line up 1:1 with the numbers the
current (rationalised) chapter kept. Concretely, running
`match.join_solutions()` produced 11 apparently-clean matches with **zero**
`needs_review` entries for the exercise/solution number collisions
themselves — every number found *something* to pair with, which is exactly
the "eleven consecutive items silently mismatched" failure mode
`step_2/PROMPT.md` warns about.

The real, content-verified mapping (confirmed by comparing distinctive
numbers — work functions, wavelengths, frequencies — in each question and
its solution's own working, not by number alone):

| Chapter exercise | Solutions-manual entry | Distinctive content confirming the pair |
|---|---|---|
| q_11.1 | sol_11.1 (प्रश्न 1) | 30 kV X-rays, same numbers, same order |
| q_11.2 | sol_11.2 (प्रश्न 2) | Cs work function 2.14 eV, 6×10¹⁴ Hz |
| q_11.3 | sol_11.3 (प्रश्न 3) | stopping voltage 1.5 V |
| q_11.4 | sol_11.4 (प्रश्न 4) | 632.8 nm He-Ne laser, 9.42 mW |
| **q_11.5** | **sol_11.6 (प्रश्न 6)**, not प्रश्न 5 | slope 4.12×10⁻¹⁵ V·s → h |
| **q_11.6** | **sol_11.8 (प्रश्न 8)**, not प्रश्न 6 | threshold 3.3×10¹⁴ Hz, incident 8.2×10¹⁴ Hz |
| **q_11.7** | **sol_11.9 (प्रश्न 9)**, not प्रश्न 7 | work function 4.2 eV, 330 nm |
| **q_11.8** | **sol_11.10 (प्रश्न 10)**, not प्रश्न 8 | 7.21×10¹⁴ Hz, max speed 6.0×10⁵ m/s |
| **q_11.9** | **sol_11.11 (प्रश्न 11)**, not प्रश्न 9 | 488 nm argon laser, stopping potential 0.38 V |
| **q_11.10** | **sol_11.15 (प्रश्न 15)**, not प्रश्न 10 | bullet 0.040 kg, ball 0.060 kg, dust particle 1.0×10⁻⁹ kg |
| **q_11.11** | **sol_11.18 (प्रश्न 18)**, not प्रश्न 11 | "show EM wavelength = photon de Broglie wavelength" proof |

From `q_11.5` onward, every naive number-match would have been wrong
(paired with a true orphan or an unrelated later problem), a growing
divergence exactly like the physics-12-3/physics-12-5 precedents in
`step_2/PROMPT.md`. The chapter was rebuilt by hand, pairing each
exercise's already-extracted question text with its content-verified
solution (never trusting `join_solutions()`'s own parts-replacement
fallback — each part's solution/final_answer was attached by matching the
question's own part label against the solution's part label, not by
replacing the parts list).

## Orphaned solutions-manual entries (26) — not part of this chapter

These are genuine problems from an older, un-rationalised edition of this
chapter's exercise set (प्रश्नावली प्रश्न 1–19 plus विविध प्रश्नावली/additional
questions प्रश्न 20–37) that the current NCERT "Rationalised 2023-24"
chapter dropped entirely. Per Rule 5 ("nothing invented"), they are not
force-matched to any surviving exercise and are not fabricated into
`additional_exercise` items (the current chapter's own text has no
"अतिरिक्त प्रश्न" section at all — inventing one from the old solutions
manual would not be transcription, it would be reconstructing a section
that doesn't exist in this edition of the textbook). They are kept only as
lightweight stub records in the stage-2 build script (id, number, a short
content excerpt) for `gate_counts` bookkeeping — never rendered into
`chapter.hi.md`.

Orphaned: प्रश्न 5, 7, 12, 13, 14, 16, 17, 19, 20, 21, 22, 23, 24, 25, 26,
27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37 (26 entries).

## OCR/layout issue found and corrected during extraction (not a content fix)

`chapter.hi.md`'s own worked examples 11.1 and 11.2 arrived from Mathpix
with their text **interleaved out of order** — the textbook page prints
them as two examples but Mathpix's reading order crossed between them
mid-solution (a two-column-page artifact). As extracted, the raw stream
reads: example 11.1's part (a) solution, then a stray sentence
("0.60 V का एक निरोधी विभव लगाकर शून्य किया जाए।" — actually the missing
tail of example 11.2's own question), then a block starting "(a) अंतक
अथवा देहली आवृत्ति के लिए..." (example 11.2's own part (a) solution,
computing cesium's threshold frequency from φ₀=2.14 eV — content that has
nothing to do with example 11.1's laser problem), then example 11.1's own
part (b) solution (N = 5.0×10¹⁵ photons/s), then example 11.2's full
question text again, then example 11.2's part (b) solution (λ = 454 nm).

This was reassembled by content match (cesium/φ₀=2.14 eV sentences →
example 11.2; laser/6.0×10¹⁴ Hz/2.0×10⁻³ W sentences → example 11.1), not
reworded or invented — every sentence is transcribed verbatim, only
re-attached to the example it actually belongs to. Flagged here per
CLAUDE.md/RULES.md Rule 4/5 spirit: this is a structural
re-attribution (which example a given, already-verbatim sentence belongs
under), not a content edit.

## Same-page issues flagged for stage 5 (not resolved here — stage 2 only transcribes)

1. **q_11.4(c) / sol_11.4(c) — mislabeled mass.** The solution computes a
   hydrogen atom's speed using `m = 1.66×10⁻²⁷ kg` (correct — that is the
   hydrogen-atom/proton mass, matching the question, which asks about "एक
   हाइड्रोजन परमाणु") but the parenthetical gloss in the source reads
   "(इलेक्ट्रॉन का द्रव्यमान)" — "(the electron's mass)". An electron's mass is
   9.1×10⁻³¹ kg, three orders of magnitude off from the value actually
   used. The arithmetic itself is fine; only the label is wrong. Recommend
   stage 5 correct the label text to "(हाइड्रोजन परमाणु का द्रव्यमान)"
   — flagged, not applied here.
2. **"तीव्रता" used where "आवृत्ति" is clearly meant**, in both sol_11.6→q_11.5
   is unaffected, but sol_11.8 (→q_11.6) and sol_11.10 (→q_11.8) both write
   "प्रकाश की तीव्रता, v = 8.2×10¹⁴ Hz" / "प्रकाश की तीव्रता, v = 7.21×10¹⁴ Hz" —
   "तीव्रता" means "intensity", but the symbol `v`/units Hz and the whole
   surrounding derivation are unambiguously about frequency. Recommend
   stage 5 correct both to "आवृत्ति" (frequency) — flagged, not applied here.
3. **q_11.8 / sol_11.10 — OCR digit-drop.** Mid-derivation: "v₀ = 721×10¹⁴ −
   2.47×10¹⁴" should read "7.21×10¹⁴" (missing decimal point; the line right
   before it and the final answer both correctly use 7.21×10¹⁴). Recommend
   stage 5 fix as a straightforward OCR correction — high confidence.
4. **q_11.10(b) / sol_11.15(b) — genuine computational error, not just a
   label slip.** The question states the ball's speed as "1.0 km/s" (same
   as the bullet in part (a)). The solution's own restatement before the
   calculation says "बॉल की चाल, v = 1 m/s" (dropping "km") and then
   computes λ = 6.63×10⁻³⁴/(0.060×1) = 1.1×10⁻³² m using that (wrong) v=1.
   Using the question's actual v = 1000 m/s gives λ ≈ 1.105×10⁻³⁵ m instead
   — three orders of magnitude smaller. This is a same-page
   self-contradiction (the solution's own stated v contradicts the
   question directly above it), of the same shape as ex_2.3/q_5.7(ii)/
   q_9.30 in this pipeline's history. **Flagged prominently for the user
   here and in the stage progress report** — recommended fix: v = 1000 m/s,
   λ = 1.1×10⁻³⁵ m. Left exactly as printed in `chapter.hi.md` for now;
   to be applied as an explicit, called-out stage-5 correction (not a
   silent high-confidence OCR fix), matching this pipeline's established
   precedent of flag-then-fix for this exact failure shape.

## Figures

Only one figure from `01_mathpix/images/` is used by this chapter's final
item set: `fig_physics-12-11_6.jpg` (the V₀ vs ν graph belonging to
q_11.5/sol_11.6's own "ढलान" derivation). The chapter's other seven images
(`fig_physics-12-11_0.jpg`–`fig_physics-12-11_5.jpg`, `fig_physics-12-11_7.jpg`)
illustrate the general chapter exposition (apparatus diagrams, the
Einstein portrait, graphs in section 11.4) or an orphaned solutions-manual
question (प्रश्न 28, image 7) — none are referenced inside any example or
exercise item, so none are carried into `chapter.hi.md`.

## Gates

- `gate_counts` (examples=3, exercise=11): PASS.
- `gate_counts` (raw solutions throwaway chapter): PASS.
- `gate_solutions_present('hi')`: PASS — all 14 items have a solution
  (item-level or part-level) in Hindi.
- `gate_bilingual`: FAILS for every item, as expected — this is a
  single-language (Hindi-only) chapter with no English source at all,
  documented rather than silently passed, matching physics-12-1's own
  precedent for this exact situation.
