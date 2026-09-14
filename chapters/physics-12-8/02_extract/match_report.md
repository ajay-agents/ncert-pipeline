# Match report

- **method:** hand-built merge (examples embed their own solutions directly in chapter.hi.md; exercises matched to solutions.hi.md by content, not join_solutions() number-matching, following physics-12-3/12-5/12-6 precedent)
- **chapter_examples:** 2
- **chapter_exercises:** 10
- **solutions_manual_entries:** 15
- **matched:** 10

## matched_pairs (10)
- q_8.1 <- प्रश्न 1 (संधारित्र 12cm त्रिज्या, 5.0cm दूरी, 0.15A आवेशकारी धारा — identical wording/numbers)
- q_8.2 <- प्रश्न 2 (संधारित्र R=6.0cm, C=100pF, 230V, 300 rad/s — identical numbers; solutions manual's own restated question has an internal typo "R=60 cm" but its own हल computes with 6 cm, matching the chapter; question text is taken from chapter.hi.md regardless, not from the solutions manual's restatement)
- q_8.3 <- प्रश्न 3 (X-किरण 10^-10 m, प्रकाश 6800 Å, रेडियो तरंग 500 m — identical wording)
- q_8.4 <- प्रश्न 4 (z-अक्ष, 30 MHz — identical wording)
- q_8.5 <- प्रश्न 5 (7.5 MHz से 12 MHz बैंड — identical wording)
- q_8.6 <- प्रश्न 6 (आवेशित कण 10^9 Hz दोलन — identical wording)
- q_8.7 <- प्रश्न 7 (B0=510 nT — identical wording)
- q_8.8 <- प्रश्न 8 (E0=120 N/C, v=50.0 MHz — identical wording)
- q_8.9 <- प्रश्न 9 (E=hv, वर्णक्रम भागों की फोटॉन ऊर्जा — identical wording, long derivation + summary table)
- q_8.10 <- प्रश्न 10 (2.0×10^10 Hz, 48 V/m आयाम — identical wording)

## orphan_solutions (5) — discarded
- प्रश्न 11 — निर्वात में E = (3.1 N/C) cos[(1.8 rad/m)y + (5.4×10^6 rad/s)t] î, 5-part question (a)-(e) about direction/wavelength/frequency/B — NOT present anywhere in current rationalised chapter.hi.md's own 10 exercises (8.1-8.10, no additional-exercises section at all in the chapter itself).
- प्रश्न 12 — 100 W बल्ब, 5% दृश्य विकिरण, तीव्रता 1m/10m पर — not in current chapter.
- प्रश्न 13 — वर्णक्रम भागों के लाक्षणिक ताप परिसर, λmT=0.29 cm·K — not in current chapter.
- प्रश्न 14 — वैद्युतचुंबकीय विकिरण से जुड़े प्रसिद्ध अंक (21 cm, 1057 MHz, 2.7 K, सोडियम द्विक् रेखाएँ, 14.4 keV) — not in current chapter.
- प्रश्न 15 — रेडियो प्रेषण/उपग्रह/X-किरण खगोलविज्ञान/ओजोन/ग्रीनहाउस/नाभिकीय शीतकाल के 6 संकल्पनात्मक उपप्रश्न — not in current chapter.

## duplicate_solutions (0)

## needs_review (0)

- **critical_finding:** The current rationalised chapter.hi.md prints exactly 10 exercises under "अभ्यास" (8.1-8.10) with **no** "अतिरिक्त अभ्यास"/additional-exercises section at all. The separate, pre-rationalisation solutions.hi.md keeps all 15 entries under its own bare 1-15 numbering, split by its own heading into "अभ्यास प्रश्न" (प्रश्न 1-10) and "अतिरिक्त प्रश्न" (प्रश्न 11-15). Here, unlike physics-12-3/12-5/12-6, the orphaned block is a clean, CONTIGUOUS trailing range (11-15) that lines up exactly with the solutions manual's own "अतिरिक्त प्रश्न" heading — no interspersion within the 1-10 range, and no numbering collision risk from match.norm_num()'s bare-number chapter-prefixing (प्रश्न 11-15 -> "8.11".."8.15", none of which collide with any real 8.x exercise). Still resolved by hand (not via join_solutions()) and every one of the 10 real pairs was verified by content (distinctive values: 12cm/5cm/0.15A; 6cm/100pF/230V/300rad/s; 10^-10m/6800Å/500m; 30MHz; 7.5-12MHz; 10^9Hz; 510nT; 120N/C/50MHz; the eV energy table; 2×10^10Hz/48V/m) — following the mandatory spot-check discipline regardless of how clean the numbering looks, per step_2/PROMPT.md.
- **ocr_ambiguity_flags_for_stage5** (transcribed as printed in solutions.hi.md per stage 2 "do not fix" rule; each needs a PDF-page check at stage 5, listed by suspected type):
  1. q_8.1(a): solution computes "C = 8.01×10^-14 F = 8.01 pF" — internally inconsistent (8.01×10^-14 F is NOT 8.01 pF; 8.01 pF = 8.01×10^-12 F), and the very next line's dV/dt calculation correctly uses 8.01×10^-12 in the denominator. Suspected OCR/typo of the exponent (-12 misread as -14) in one line only; direct arithmetic (ε0·π·r²/d) confirms 8.01×10^-12 F = 8.01 pF is the physically correct value consistent with the rest of the same solution.
  2. q_8.4: closing sentence reads "अतः वैद्युतचुंबकीय तरंग की आवृति 10 m है" — labels the computed 10 m as "आवृत्ति" (frequency) when it is actually "तरंगदैर्घ्य" (wavelength), the quantity the question and the preceding derivation both compute. Likely a plain wording slip in the source solutions manual.
  3. q_8.5: solution's first line reads "आघूर्ण f2=12 MHz" — "आघूर्ण" (moment) is very likely OCR/typo for "आवृत्ति" (frequency); also the λ1 formula line writes "λ1 = c/t1" (t1 instead of f1) — likely an OCR substitution of f->t.
  4. q_8.9 (माइक्रो तरंगें hetu): "E=hv=6.6×10^-34×10^10=6.6×1σ^-24 J" — "1σ" is very likely an OCR misread of "10" (sigma glyph substituted for a zero); the next line's own follow-up computation already uses the correct "6.6×10^-24" value, so this looks like an isolated single-line OCR artifact.
  5. q_8.10(c): final derivation step reads "u_E = (1/4)·(B0²/μ0) = B0²/(2μ0) = u_B" — algebraically, (1/4)(B0²/μ0) equals B0²/(4μ0), not B0²/(2μ0); a factor-of-2 discrepancy in the last equality only (does not affect the qualitative conclusion "u_E = u_B" the question asks to demonstrate, but the intermediate numeric coefficient printed does not follow from the line right before it).
  None of these were corrected here — per stage 2 rules, transcribed exactly as extracted from solutions.hi.md, flagged for stage 5's PDF-page verification (which can confirm whether each is a genuine mathpix OCR artifact vs. an actual error already present in the printed solutions manual, per the "should_be must be what the PDF actually shows" rule, and per the standing "leave both as printed, document the disagreement" preference for anything that turns out to be a genuine source-book error rather than an OCR artifact).

- **figure_notes:** chapter.hi.md's own exercises 8.1 and 8.2 each carry one figure (fig_physics-12-8_7.jpg = चित्र 8.5 for 8.1, fig_physics-12-8_8.jpg = चित्र 8.6 for 8.2), both attached at item level. solutions.hi.md's own प्रश्न 1 restates the same चित्र 8.5 diagram as a separate scan (fig_physics-12-8_9.jpg) — not attached, since it is a redundant duplicate of the chapter's own figure for the same exercise and the question/figure of record comes from chapter.hi.md, not the solutions manual's restatement. The other 7 downloaded images (fig_0 Maxwell portrait, fig_1 Fig 8.1 capacitor-loop diagram, fig_2/fig_3 Fig 8.2(a)/(b), fig_4 Hertz portrait, fig_5 Fig 8.3 wave diagram, fig_6 Fig 8.4 spectrum chart) are all narrative/expository images inside the chapter's running text between examples/exercises, not attached to any example or exercise item — consistent with Part A extracting only the "Examples" and "Exercise Questions" sections, not the chapter's general narrative.
