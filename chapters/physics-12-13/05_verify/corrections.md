### q_13.9 — solution (hi)
- **Confidence:** high
- **Reason:** Same-page arithmetic self-contradiction, confirmed against the actual solutions.hi.pdf page image (p.90): 9x10^9 x (1.6x10^-19)^2 / (2x10^-15) correctly equals 1.152x10^-13 J, not the printed 5.76x10^-14 J (exactly half). The printed intermediate value contradicts both the computation directly above it and the division immediately following it on the same line (5.76e-14 / 1.6e-19 = 360000, not the printed 720000; only 1.152e-13 / 1.6e-19 = 720000 matches). The final answer (720000 eV -> 360 keV) was already correct and is left untouched; only the self-contradictory intermediate number is corrected.
- **Found:**
  > \frac{5.76 \times 10^{-14}}{1.6 \times 10^{-19}}=720000 \mathrm{eV}
- **Should be:**
  > \frac{1.152 \times 10^{-13}}{1.6 \times 10^{-19}}=720000 \mathrm{eV}

## Additional findings from this stage's full read-back + arithmetic re-derivation
(documented here per CLAUDE.md/step_5 - not applied as Correction objects,
either because the fix already landed upstream at extraction time, or
because the rule for a genuine cross-document disagreement is to leave both
values exactly as printed, not resolve unilaterally)

- **q_13.4 (Au/Ag nuclear radius ratio), same-page self-contradiction already
  resolved upstream**: solutions.hi.pdf (p.84, प्रश्न 11 in that document's own
  numbering) literally prints the exponent as `(197/107)^13 = 1.225` -
  confirmed against the actual page image, not an OCR artifact. `1.225` is
  only consistent with an exponent of `1/3` (verified: (197/107)^(1/3) =
  1.2258...), never `13`. This chapter's own `02_extract/chapter.hi.md`
  already used the correct `1/3` (the extraction pass silently normalised
  this obvious slip rather than transcribing it verbatim, which deviates
  from the usual "transcribe as-is, fix at stage 5" discipline - flagged
  here for the record) - confirmed correct, no further action needed.
  Also on the same solutions.hi.pdf page: the question header prints the
  gold isotope as `{}^{197}_{78}Au` (Z=78), while this chapter's own
  chapter.hi.pdf (exercise 13.4) and main text both print `{}^{197}_{79}Au`
  (Z=79, gold's real atomic number). This is a CROSS-DOCUMENT disagreement,
  not a same-page contradiction (each source is internally consistent with
  itself) - per standing instructions, left unresolved; note that Z never
  actually enters this item's rendered solution text (only the mass numbers
  197/107 are used in the R ∝ A^(1/3) ratio), so no value in the
  deliverable is actually affected either way. Documented here only, per
  instructions for a genuine cross-source disagreement.

- **q_13.6 (Fe-56 -> 2 Al-28 fission), same-page self-contradiction already
  resolved upstream**: solutions.hi.pdf (p.87, प्रश्न 16) prints its own
  "दिया है" restatement of the data with `m({}^{66}_{26}Fe) = 55.93494 u`
  (A=66) - confirmed against the actual page image, a genuine print error,
  not OCR noise - while the very next line's reaction equation on the same
  page, `{}^{56}_{26}Fe -> 2{}^{28}_{13}Al`, and every other use of Fe in the
  same solution (and this chapter's own exercise 13.6) correctly use A=56.
  55.93494 u is the real Fe-56 atomic mass. This chapter's extraction never
  carried the standalone "दिया है" restatement into q_13.6's solution text at
  all (it started directly from the reaction equation, using the chapter's
  own correctly-printed A=56 statement) - so the deliverable was never
  affected; confirmed already correct, no further action needed.

- **q_13.7 (Pu-239 fission energy), same-page self-contradiction already
  resolved upstream**: solutions.hi.pdf (p.88, प्रश्न 17) prints its final
  result line as `= 4.53 x 10^26 MW`, where every preceding step computes in
  MeV and the question explicitly asks "kitni MeV urja" - confirmed against
  the actual page image, a genuine unit slip in the printed source (MW is
  dimensionally a power unit, not energy - cannot be what a per-fission
  energy total is measured in). This chapter's extraction already recorded
  the corrected unit (MeV) rather than transcribing "MW" verbatim - flagged
  here for the record, confirmed correct, no further action needed.

- **q_13.10 (nuclear matter density is A-independent), genuine
  CROSS-DOCUMENT disagreement - left exactly as printed in both sources,
  not resolved**: this chapter's own main text (section 13.3, chapter.hi.pdf
  p.3-4) and exercise 13.10's own given constant both state
  R0 = 1.2 x 10^-15 m (= 1.2 fm). solutions.hi.pdf's own density derivation
  (p.90, प्रश्न 21) substitutes R0 = 1.1 x 10^-15 m instead - confirmed
  against the actual page image, and the printed final answer
  (2.97 x 10^17 kg/m^3) is arithmetically consistent with 1.1, not 1.2 (a
  value of 1.2 would give ~2.30 x 10^17 kg/m^3 instead). Both sources are
  internally self-consistent (chapter uses 1.2 throughout; solutions manual
  uses 1.1 throughout this one derivation and its own printed answer
  matches it) - this is exactly the "two different stated values, either
  could be what the source means" shape the standing instructions say to
  leave alone, not the same-page shape this session had standing
  authorisation to fix. q_13.10's solution in chapter.verified.hi.md keeps
  the solutions-manual's own R0 = 1.1 x 10^-15 m and 2.97 x 10^17 kg/m^3
  exactly as printed there. Flagged prominently here and in the stage
  progress report for the user's attention.
