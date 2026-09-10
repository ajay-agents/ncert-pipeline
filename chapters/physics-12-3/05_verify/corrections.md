# Corrections — physics-12-3

**8 high/medium-confidence corrections applied**, all fixing the same
underlying OCR failure: the solutions-manual PDF prints the current
variable I (and the length variable l) as a plain, mostly serif-less
vertical stroke, and Mathpix's OCR resolved that ambiguous glyph
inconsistently — sometimes as the Greek letter phi, sometimes as a bare
division slash, sometimes as the digit "1", and once fused with an
adjacent "n" into the LaTeX `\ln` command. Every correction below was
verified directly against the actual solutions-manual PDF page (not
assumed from the pattern alone) both by the dispatched verification
sub-agent and independently re-confirmed by the coordinator via a second,
high-dpi render of the same pages.

### q_3.1 — solution (hi)
- **Confidence:** high
- **Found:** `\varphi_{\max }`
- **Should be:** `I_{\max }`
- **Reason:** PDF page index 0 clearly prints `I_{\max}=\frac{E}{r}=\frac{12}{0.4}=30\ \mathrm{A}` — matching the correctly-transcribed "I" used two lines earlier and in the answer block. Only this one occurrence was corrupted to phi.

### q_3.6 — solution (hi)
- **Confidence:** high
- **Found:** `$t^{\circ} \mathrm{C}=4^{\circ} \mathrm{C}=2.8 \mathrm{~A}$`
- **Should be:** `$t^{\circ} \mathrm{C}=I_{t^{\circ} \mathrm{C}}=2.8 \mathrm{~A}$`
- **Reason:** PDF page index 3 prints "अन्त में t ताप पर धारा $t^{\circ}\mathrm{C}=I_{t^{\circ}\mathrm{C}}=2.8\ \mathrm{A}$ हो जाती है।" — the italic I was OCR'd as the digit "4".

### q_3.7 — solution (hi), 4 corrections
- **Confidence:** high (2), medium (2)
- Kirchhoff's loop rule: `\Sigma V=\Sigma / R` → `\Sigma V=\Sigma I R` (PDF page index 4 prints ΣV=ΣIR; the "I" was dropped and a stray slash rendered instead).
- `2=\frac{17}{5} / \text { अथवा } /=\frac{10}{17} \mathrm{~A}` → `2=\frac{17}{5} I \text { अथवा } I=\frac{10}{17} \mathrm{~A}` (PDF page index 5, same failure mode, both instances).
- `I_{1}=\frac{2 l}{5} \text { तथा } I_{2}=-\frac{1}{5}` → `I_{1}=\frac{2 l}{5} \text { तथा } I_{2}=-\frac{l}{5}` (medium confidence — the print glyph is inherently ambiguous between I/l/1; inferred from consistency with the adjacent unambiguous occurrence and later use).
- `I_{2}=-\frac{1}{5}=-\frac{2}{17} \mathrm{~A}` → `I_{2}=-\frac{l}{5}=-\frac{2}{17} \mathrm{~A}` (medium confidence, same reasoning).

### q_3.9 — solution (hi), 2 corrections
- **Confidence:** medium, high
- `v_{d}=\frac{1}{n e A}` → `v_{d}=\frac{l}{n e A}` (medium confidence — inferred from the immediately preceding equation `I=neAv_d`, same glyph ambiguity).
- `t=\frac{\ln e A}{l}=...` → `t=\frac{l n e A}{l}=...` (high confidence — Mathpix fused "I" and "n" into the LaTeX `\ln` command, producing a nonsensical logarithm; there is no logarithm anywhere in this derivation).

### q_3.3 — solution (hi) — applied after explicit user sign-off
- **Confidence:** high (source confirmed, correction applied only on the user's explicit go-ahead — see below)
- **Found:** `$1027^{\circ} \Omega$` (in the concluding sentence)
- **Should be:** `$1027^{\circ} \mathrm{C}$`
- **Reason:** concluding sentence read "अतः पदार्थ का $1027^{\circ} \Omega$ ताप पर प्रतिरोध $117 \Omega$ है।" — using °Ω instead of °C for a temperature, directly under a derivation that correctly computed $t=1000+27=1027^{\circ}\mathrm{C}$. Confirmed via a direct high-dpi render of the solutions-manual PDF page (index 2) that the source itself prints this exact typo — not an OCR/transcription fault. Per `step_5/verify.md`'s narrow same-page self-contradiction exception, this is **not** an ordinary correction the pipeline applies silently — the user was shown the finding and explicitly chose to correct it for this chapter (rather than preserve the source's own error) before this fix was applied.

## Summary

- All 16 items checked (7 examples against `00_raw/chapter.hi.pdf`, 9
  exercise solutions against `00_raw/solutions.hi.pdf`).
- 9 corrections applied total (8 OCR-error corrections, all `high`/
  `medium` confidence; 1 same-page unit self-contradiction applied only
  after the user's explicit sign-off) — all in `solution` fields, all
  `hi`.
- 1 other genuine textbook errata already known and confirmed not to need
  correction (ex_3.7's leftover formula fragment from a different
  example, and q_3.9's prompt-side missing negative exponent on m³/m⁻³ —
  both source-printed, not OCR faults, both left as-is per the same rule).
- `gate_math_parity` and `gate_counts` re-verified clean after applying
  these corrections and propagating them through 06_simplify and
  07_format (all three files had the exact same garbled substrings,
  byte-identical, since they sit inside frozen/protected math spans that
  simplification and formatting never touch).
