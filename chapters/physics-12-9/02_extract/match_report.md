# Match report

- **language:** hi-only chapter (no English source, same as physics-12-1)
- **examples:** 8
- **exercises:** 31
- **raw_solutions_in_solutions.hi.md:** 38
## matched_1_to_1_by_number (15)
- sol1..sol17 -> q_9.1..q_9.17 (direct number match, content-verified)
- sol19 -> q_9.18 (bulb/wall/convex-lens problem)
- sol20 -> q_9.19 (screen 90cm, two lens positions 20cm apart)
- sol21 -> q_9.20 (a,b: two-lens system from Q9.10/9.20, 8cm apart)
- sol22 -> q_9.21 (60 deg prism, TIR at second face, n=1.524)
- sol29 -> q_9.22 (card-sheet squares, magnifying lens) -- SEE FLAG below
- sol30 -> q_9.23 (max angular magnification distance)
- sol31 -> q_9.24 (6.25mm^2 image area)
- sol32 -> q_9.25 (a-e conceptual: magnifying lens/microscope)
- sol33 -> q_9.26 (30X compound microscope)
- sol34 -> q_9.27 (a,b: telescope f_o=140cm f_e=5cm)
- sol35 -> q_9.28 (a,b,c: telescope separation + tower image height)
- sol36 -> q_9.29 (Cassegrain telescope, 220mm/140mm mirrors)
- sol37 -> q_9.30 (galvanometer mirror, 3.5 deg deflection) -- SEE FLAG below
- sol38 -> q_9.31 (plano-convex lens + liquid on plane mirror)

- **why_not_naive_number_join:** join_solutions() matches purely by printed number. This chapter's solutions.hi.md (an older, unrationalised solutions manual) numbers its entries 1..38 bare, while the current rationalised chapter.hi.pdf only has 31 exercises (9.1..9.31). From solutions-manual entry 18 onward, 7 extra questions are INTERSPERSED (not appended at the end) that the rationalised chapter dropped entirely -- a Human Eye subsection (accommodation range, myopia/hypermetropia corrective lens power, astigmatism) plus a crown/flint achromatic-prism-combination question and a plane/convex-mirror real-image conceptual question. A naive number-match (norm_num(chapter='9')) would have silently paired q_9.18 through q_9.31 with the WRONG solutions-manual entries (off by a growing offset), exactly the pattern already seen in physics-12-3/5/6/7's build history. Every pairing above was content-verified by hand (matching physical quantities, not just position) before building the merged Chapter -- join_solutions() was NOT used for items 9.18-9.31; they were built directly from content-verified solutions.hi.md text.
## orphan_solutions_discarded_no_home_in_rationalised_chapter (7)
- sol18: plane/convex mirror real-image conceptual Q (5 sub-parts a-e)
- sol23: crown-glass/flint-glass achromatic prism combination Q
- sol24: Human Eye - cornea/eye-lens power, accommodation range estimate
- sol25: Human Eye - does myopia/hypermetropia imply lost accommodation?
- sol26: Human Eye - myopic person's -1.0D distance + 2.0D reading lens
- sol27: Human Eye - astigmatism (vertical vs horizontal stripes)
- sol28: Human Eye - reading small print with a 5cm-focal-length magnifier

## needs_review_flags_for_stage_5 (2)
- q_9.22 (sol29): chapter.hi.pdf's own exercise text states the magnifying lens is '9 cm फ़ोकस दूरी का अभिसारी लेंस' (f=9cm), but solutions.hi.pdf's matched solution (प्रश्न 29) computes throughout with f=+10cm ('10 cm फोकस दूरी का अभिसारी लेंस') -- a genuine cross-source value disagreement between the two independent PDFs, not an OCR artifact (both renderings are internally consistent, solutions doc even bolds '10 cm'). Per standing instruction: leaving both values exactly as printed in their own source, NOT unilaterally resolved -- flagged here for stage 5 confirmation against the actual PDF pages and for the user's sign-off.
- q_9.30 (sol37): the matched solution's own final line contains a same-page self-contradiction -- it computes d = 1.5 x (7 deg x pi / 180 deg) = 0.184 m, then in the same breath restates this as '= 18.4 m' (should be 18.4 cm, since 0.184 m = 18.4 cm; '18.4 m' is off by a factor of 100 from its own preceding value). Flagged per the same-page-self-contradiction rule -- left both figures visible in the transcribed solution text, best-judgement fix noted (18.4 cm) but NOT silently substituted; needs the user's quick sign-off.

## missing_figure_flag (1)
- ex_9.1 references 'चित्र 9.5' (the concave-mirror ray diagram the mirror equation is derived from) but no distinct image file in 01_mathpix/images/ carries that caption -- only fig_physics-12-9_2/3 (चित्र 9.4 a/b) precede it and fig_physics-12-9_4 (चित्र 9.6) follows; चित्र 9.5's own image appears to be missing from the mathpix extraction. Left without a figure attached per Rule 5 (nothing invented) rather than guessing which image it might be; flagged here rather than silently dropped.

- **en_vs_hi_extraction_count_diff:** n/a -- hi-only chapter, no English source PDFs provided (00_raw/ has only chapter.hi.pdf and solutions.hi.pdf)
## gate_counts (0)

## gate_solutions_present_hi (0)

- **gate_bilingual:** 66 items flagged -- EXPECTED, single-language (Hindi-only) chapter, no English source exists
