# Match report

- **method:** hand-built merge (examples embed their own solutions; exercises matched to solutions.hi.md by content, not join_solutions() number-matching)
- **chapter_exercises:** 8
- **solutions_manual_entries:** 17
- **matched:** 8
## matched_pairs (8)
- q_6.1 <- प्रश्न 1 (चित्र a-f दिशा प्रागुक्ति, same 6 sub-panels)
- q_6.2 <- प्रश्न 2 (अनियमित तार/वृत्ताकार लूप, identical wording)
- q_6.3 <- प्रश्न 3 (15 फेरे/cm सोलेनॉइड, 2.0 A -> 4.0 A in 0.1s, identical wording)
- q_6.4 <- प्रश्न 4 (8cm x 2cm कटा लूप, 0.3T, 1cm/s, identical wording)
- q_6.5 <- प्रश्न 5 (1.0m छड़, 400 rad/s, 0.5T, identical wording)
- q_6.6 <- प्रश्न 7 (10m तार पूर्व-पश्चिम, 0.30e-4 Wb/m^2, 5.0 m/s, identical wording)
- q_6.7 <- प्रश्न 8 (5.0A->0.0A in 0.1s, avg emf 200V, identical wording)
- q_6.8 <- प्रश्न 9 (M=1.5H, 0->20A in 0.5s, identical wording)

## orphan_solutions (9)
- प्रश्न 6 - वृत्ताकार कुंडली r=8cm, N=20, 50 rad/s, 3.0e-2 T (max/avg emf, power) - NOT present anywhere in current rationalised chapter.hi.md's 8 exercises (6.1-6.8). Old pre-rationalisation exercise, retained only in the solutions manual.
- प्रश्न 10 - जेट प्लेन पंख, dip angle 30 deg - NOT present in current chapter.
- प्रश्न 11 - प्रश्न 4 का लूप स्थिर, विद्युत चुम्बक धारा घट रही (additional exercise) - not in current chapter (no additional-exercises section at all).
- प्रश्न 12 - वर्गाकार लूप 12cm, गैर-एकसमान क्षेत्र प्रवणता - not in current chapter.
- प्रश्न 13 - search coil, ballistic galvanometer - not in current chapter.
- प्रश्न 14 - छड़ PQ पटरियों पर, (a)-(g) - not in current chapter.
- प्रश्न 15 - वायु-कोर परिनालिका, back-emf - not in current chapter.
- प्रश्न 16 - तार + वर्गाकार लूप अन्योन्य प्रेरकत्व - not in current chapter.
- प्रश्न 17 - आवेशित रिम, चुंबकीय क्षेत्र हटाने पर कोणीय वेग - not in current chapter.

## duplicate_solutions (0)

## needs_review (0)

- **critical_finding:** This chapter's own printed exercises (6.1-6.8, no additional-exercises section) are numbered 1-8 in sequence, but the separate solutions manual keeps the PRE-RATIONALISATION numbering (प्रश्न 1-17, with प्रश्न 11-17 under its own 'अतिरिक्त प्रश्न' heading). प्रश्न 6 and प्रश्न 10 are extra, ORPHANED entries INTERSPERSED among the otherwise-matching numbers (not confined to a trailing block) - exactly the physics-12-3/physics-12-5 pattern. A naive match.join_solutions() number-based join would have been actively WRONG here, not just silently short: solutions.hi.md numbers its own entries bare ('1'..'17'), so match.norm_num(raw, chapter='6') would prepend the chapter number to any bare number, normalising प्रश्न 6 -> '6.6' - directly colliding with the chapter's own real exercise 6.6 (a completely different question, the falling E-W wire, which is actually प्रश्न 7 in the solutions manual's own numbering). Every question from 6.6 onward would have silently drifted by one, with needs_review staying empty throughout since every bare number 'matches' something. Resolved by verifying all 8 pairings by content (distinctive numeric values: 15 turns/cm, 8x2cm loop, 400 rad/s, 0.30e-4 Wb/m^2, 200V avg emf, 1.5H mutual inductance) before writing anything, matching every word of each question's own wording between chapter.hi.md and solutions.hi.md.
- **ocr_flag_for_stage5:** q_6.3's solution (प्रश्न 3) computes e = A*mu0*n*dI/dt = 2e-4 * 4*pi*1e-7 * 1500 * 20 ~= 7.5e-6 V by direct arithmetic, but solutions.hi.md's own OCR text reads 'e=7.5 x 10^{6} V' (positive exponent, missing the minus sign) - transcribed here EXACTLY as printed in the mathpix output per stage 2 rules ('do not fix, transcribe as-is'); flagged for stage 5 verification against the actual solutions.hi.pdf page to confirm whether the source PDF itself has this sign error or whether it is a mathpix OCR artifact.
- **figure_notes:** chitra 6.11 (rotating-rod field diagram, ex_6.6) was rendered by Mathpix as a plain markdown table of x symbols, not as a downloaded image file - no fig_*.jpg exists for it, so no figure block was attached to ex_6.6 (nothing invented). q_6.1's four chapter-side images (fig_13/14/15/16, all captioned generically 'chitra 6.15' by the source) could not be reliably disambiguated panel-by-panel against the six lettered sub-answers (a)-(f) from OCR text alone; all four are attached at item level without per-panel claims - flagged as a known limitation, not a silent guess. solutions.hi.md's own duplicate crops of the same diagrams for q_6.1/q_6.2 (fig_18-23) were not used, to avoid attaching redundant duplicate images of content already covered by the chapter's own figures. q_6.4's fig_24 and fig_25 are near-identical duplicate scans of the same loop diagram (chapter itself has no figure for exercise 6.4); only fig_24 was attached, to avoid a duplicate.
