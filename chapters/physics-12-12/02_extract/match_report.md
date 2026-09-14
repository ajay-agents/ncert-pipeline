# Match report

- **chapter_exercises_found:** 12.1-12.9 (9 items) -- this rationalised edition's own '## अभ्यास' section; no additional/miscellaneous-exercises block exists in chapter.hi.md
- **solutions_manual_raw_entries:** प्रश्न 1-17 (17 items) -- प्रश्नावली 1-10 + विविध प्रश्नावली (मिस्सेलेनियस) 11-17
- **naive_number_join_would_have_been_wrong:** join_solutions() with chapter='12' prefixes bare solutions-manual numbers '1'..'17' to '12.1'..'12.17'. This DOES match 1<->1, 2<->2 correctly, but प्रश्न 3 (Paschen-series shortest-wavelength question) is an EXTRA question interspersed in the solutions manual with NO counterpart anywhere in this chapter's own 9 exercises -- naive prefixing would normalise it to '12.3' and silently steal the slot of the chapter's REAL 12.3 (the '2.3 eV gap' question, which is actually प्रश्न 4 in the solutions manual), cascading a growing one-off misattachment through every remaining exercise (12.4<-प्रश्न 5 wrongly instead of प्रश्न 4, ... 12.9<-प्रश्न 10 wrongly instead of प्रश्न 9-position content) -- exactly the failure mode step_2/PROMPT.md warns about (physics-12-3/12-5 precedent), just with the extra item near the START of the run instead of scattered through the middle.
## content_verified_pairing_used (9)
- q_12.1 <- प्रश्न 1 (MCQ a-e, identical wording+options)
- q_12.2 <- प्रश्न 2 (solid-hydrogen thought experiment, identical wording)
- q_12.3 <- प्रश्न 4 (NOT प्रश्न 3 -- '2.3 eV' gap, matches q_12.3's own de-glued text)
- q_12.4 <- प्रश्न 5 (ground-state KE/PE, identical wording)
- q_12.5 <- प्रश्न 6 (n=4 photon absorption, identical wording)
- q_12.6 <- प्रश्न 7 (parts a/b speed+period at n=1,2,3, identical wording)
- q_12.7 <- प्रश्न 8 (innermost radius given, n=2/3 radii, identical wording)
- q_12.8 <- प्रश्न 9 (12.5eV electron beam, identical wording)
- q_12.9 <- प्रश्न 10 (earth-orbit quantum number, identical wording)

## orphans_excluded_not_invented (2)
- प्रश्न 3 -- Paschen-series shortest-wavelength question. Genuinely interspersed extra question in the solutions manual with no counterpart in this rationalised chapter's own exercises. Full text + solution preserved below for the record but NOT added to chapter.hi.md as a fabricated item.
- प्रश्न 11-17 -- entire 'विविध प्रश्नावली' (miscellaneous/additional exercises) block. This rationalised chapter.hi.md has NO additional-exercises section at all (confirmed by reading the full file end-to-end) -- matches the physics-12-5 precedent of a whole prior-edition problem set the current rationalisation dropped outright. 7 entries discarded, not force-matched, not fabricated into an additional_exercise section.

- **orphan_solution_3_full_text:** प्रश्न 3. पाश्चन श्रेणी में विद्यमान स्पेक्ट्रमी रेखाओं की लघुतम तरंगदैर्घ्य क्या है? हल पाश्चन श्रेणी हेतु, n1=3 तथा n2=∞; परिणाम: λ ≈ 822.65 nm.
- **gate_counts:** PASS
- **gate_solutions_present_hi:** PASS
- **gate_bilingual:** FAIL (expected, hi-only chapter, no English source): 24 item-checks
- **flag_for_stage5_q12.8:** q_12.8's own solutions-manual text computes lambda=993 Angstrom in the derivation, then its concluding sentence states 'लाइमन श्रेणी 933 Angstrom की तरंगदैर्घ्य ... उत्सर्जित करेगी' -- 933 vs the derived 993 is a same-page self-contradiction (likely a digit-transposition typo in the source), matching the recurring pattern flagged in every prior chapter (ex_2.3/q_5.7(ii)/etc precedent). Transcribed VERBATIM as printed (both numbers, unresolved) at this stage per 'extract, do not fix' -- flagged here for stage 5 to check against the actual solutions.hi.pdf page image and correct with explicit sign-off, not silently.
- **flag_for_stage5_q12.9:** q_12.9's solutions-manual text ends with an apparently unrelated trailing remark ('अत: इलेक्ट्रॉन n=1 से n=3 में उद्वेलित होगा ... लाइमन श्रेणी से सम्बन्धित है') about an electron transition and the Lyman series, which has no logical connection to the earth-orbiting-the-sun quantum-number question actually asked. Left OUT of this item's final_answer/solution text entirely here (not invented, not silently merged) since it reads as either a genuine authoring error in the (non-official, guide-book-style) solutions manual or a page-boundary content bleed from an adjacent, unrelated problem; flagged for stage 5 to check against the actual solutions.hi.pdf page.
