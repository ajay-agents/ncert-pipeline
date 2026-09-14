# Stage 5 — verification notes (physics-12-10, Hindi-only)

All 8 items (ex_10.1, ex_10.2, q_10.1–q_10.6) were read against the actual
rendered pages of `00_raw/chapter.hi.pdf` and `00_raw/solutions.hi.pdf`
(image renders at 200dpi, not the mathpix text) — every question, every
solution step, every numeric value and every figure reference was checked.

**No `found`/`should_be` corrections were applied.** Extraction was accurate
everywhere it was checked. Three things surfaced during the read-back that
are documented here instead of as corrections, per `step_5/verify.md`'s
"if the textbook has an error, that is not your call":

## 1. q_10.1 — "आवर्तनांक" is NOT an OCR/mathpix slip; it is what the PDF prints

The previous agent flagged `chapter.hi.md`'s q_10.1 prompt — "जल का
आवर्तनांक 1.33 है" — as a likely OCR slip for "अपवर्तनांक" (refractive
index). Checked directly against `chapter.hi.pdf` page 18 (printed page
272) at high zoom: the source PDF itself prints "आवर्तनांक", not
"अपवर्तनांक". This is a genuine textbook-print anomaly (almost certainly a
typo in this NCERT edition), not an extraction error — mathpix transcribed
the page faithfully. Per `step_5/verify.md`, `should_be` must be what the
PDF actually shows, and a textbook's own error is not stage 5's call to
fix. **Left exactly as printed, uncorrected.** For reference,
`solutions.hi.pdf` page 1 (its own restatement of the question) prints the
correct "अपवर्तनांक" — the anomaly is specific to `chapter.hi.pdf`'s own
print of the question. Flagged prominently for the user; no action taken.

## 2. q_10.6 — the question genuinely omits slit separation (d) and screen distance (D)

The question as printed on `chapter.hi.pdf` page 19 (page 273) ends after
stating the two wavelengths (650 nm, 520 nm) and asking parts (a) and (b) —
it never states d or D. This is not a mathpix truncation: the full page
was checked and there is nothing more printed. `solutions.hi.pdf`'s worked
solution (page 6, "प्रश्न 6") nonetheless uses D = 1.2 m and d = 2×10⁻³ m
without ever stating where they came from — a gap already present in the
source solutions manual, not introduced by this pipeline. Per Rule 5
(nothing invented), the question text is left exactly as printed — no
values were fabricated into it. Flagged for the user's awareness; the
worked solution's own D/d values are themselves unverifiable against the
question as printed, though they do produce the printed final answers
(1.17×10⁻³ m and 1.56×10⁻³ mm) correctly.

## 3. q_10.6(b) — same-page self-contradiction in the source solutions manual, already resolved upstream

`solutions.hi.pdf` page 6 ("प्रश्न 6") states in prose "जो λ₁ तरंगदैर्घ्य
के कारण **(n+1)** की चमकीली फ्रिन्ज के संगत है", but the very next line's
equation uses **(n−1)**: `n·λ₂·(D/d) = (n−1)·λ₁·(D/d)`. Solving with
(n+1) gives a negative, nonsensical n; solving with (n−1) gives n = 5,
matching every subsequent step in the source's own derivation. This is a
same-page self-contradiction in the printed solutions manual itself (the
same pattern as physics-12-2's ex_2.3, q_5.7(ii), etc.), not a bilingual
or cross-source disagreement. An earlier stage (extraction/matching, before
stage 5) already resolved this silently in `combined.hi.md`, which reads
"(n−1)वीं चमकीली फ्रिंज के संगत है" — consistent with the equation and the
correct n = 5 result. No further action needed at stage 5; flagged here so
the resolution is on record and visible to the user, per the standing
instruction to always surface this pattern even when the fix already
landed correctly.
