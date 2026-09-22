# Match report

- **examples:** 7
- **exercise_questions:** 31
- **exercise_solutions_extracted:** 32
- **exercise_matched_by_number:** 31
- **exercise_content_verified_mismatches_found_and_fixed:** 3
## exercise_orphan_solutions_discarded (2)
- orig 9.25 (stability of a coordination compound - no chapter counterpart)
- orig 9.30 (oxidation number of Co in K[Co(CO)4] - no chapter counterpart)

## exercise_genuine_content_gap (1)
- q_5.25: no solution exists anywhere in this solutions manual for the chapter's actual 5.25 (violet colour of [Ti(H2O)6]3+ via crystal field theory) - left empty per Rule 5, reported here explicitly

- **intext_questions:** 10
- **intext_solutions_extracted:** 11
- **intext_matched_by_number:** 10
## intext_orphan_solutions_discarded (1)
- orig 9.11 (overall complex dissociation equilibrium constant for [Cu(NH3)4]2+ - no chapter counterpart, a genuine 11th intext question the rationalised chapter dropped)

## flagged_for_stage5_verification (14)
- ex_5.1: source's own 5-item answer list is printed out of order (i, iii, ii, iv, v) - transcribed as printed, not resequenced
- ex_5.2 parts: source's own answer list order is (a, b, d, e, c) - each part still got its correct matching answer by label, but flagging the odd source ordering
- ex_5.6: prompt part (a) uses 'OX' (uppercase) vs 'ox' (lowercase, standard) everywhere else - likely an OCR capitalisation glitch, transcribed as printed
- q_5.3 part (i): unbalanced LaTeX - opens with \left[ but closes with a bare \right. instead of \right] (missing closing bracket)
- q_5.24 part (ii): '$\left[\mathrm{Co}\left(\mathrm{NH}_{3}\right)_{5} \mathrm{Cl}_{-}\right] \mathrm{Cl}_{2}$' - the '\mathrm{Cl}_{-}' is almost certainly a mis-OCR'd 'Cl]', i.e. should read [Co(NH3)5Cl]Cl2
- q_5.1 solution: '(In modern terminology...' has an unclosed opening parenthesis, looks like a mis-OCR'd sub-point marker
- q_5.2 solution: ends abruptly with a trailing lone '-' character - looks like a page-break/truncation artifact
- q_5.3 solution: the part answering 'coordination polyhedron' is labelled '(vi)' instead of the expected '(iv)', and '(vi)' is then reused again for 'heteroleptic complexes' - duplicate/misnumbered labels in the source
- q_5.8 solution: isomerism list runs (a)-(f) but (d) and (e) labels are glued oddly into the preceding sentence/equation rather than starting their own line
- q_5.25 (orphan, discarded - see genuine_content_gap above) and q_5.30's correct source text ('Question 9.31' in the original) ends with a stray trailing 'Then,' immediately before the page break into the next question - looks like truncated/cut-off content, kept as printed with nothing added
- it_5.1 solution: sub-part labels print as (i)(ii)(iii)(vi)(v)(vi) - '(iv)' is missing entirely and '(vi)' appears twice
- it_5.8 solution: looks like a two-column side-by-side comparison table (Co complex vs Ni complex) that mathpix flattened into one interleaved, internally-contradictory stream ('Ni... Hence, it is an inner orbital complex' - inner-orbital should describe the Co complex, not Ni)
- it_5.9 solution: text says 'electronic configuration of Pd(+2) is 5d^8' where it should almost certainly say 'Pt(+2)' (the question and rest of the answer are about a Pt complex)
- it_5.10 solution: another apparent two-column interleave (Mn-aquo vs Mn-cyano comparison); '[Mn(CN)6]^4' is missing its expected negative charge (should read 4-)

- **notes:** This chapter's solutions manual ("(Chapter 9)(Coordination compounds)") uses a numbering scheme that is NOT a uniform chapter-number offset from the textbook's own "Unit 5" numbering (unlike a simple '9.N -> 5.N' substitution) - it silently carries TWO extra, chapter-dropped exercise questions interspersed near the end of its own sequence (orig 9.25 and orig 9.30), each with no counterpart in the current rationalised chapter's 31 exercises. Per step_2/PROMPT.md's explicit warning that a pure number-based join can match every number to *something* while still being wrong, needs_review stayed empty for exercises even though 3 items (q_5.25, q_5.30, q_5.31) were initially mismatched by the naive '9.N -> 5.N' relabelling. Caught by manually reading and comparing every one of the 31 chapter exercise stems against all 32 solutions-manual question stems side by side (not trusting the automated join's clean report) - found solutions 'Question 9.25' and 'Question 9.30' each match no chapter exercise at all, while solutions 'Question 9.31' and 'Question 9.32' are verbatim matches for the chapter's own 5.30 and 5.31 respectively (not 5.31/5.32 as naive relabelling assumed). Fixed by hand: cleared q_5.25's wrongly-attached content, reassigned q_5.30 and q_5.31 to their correct content, and discarded the two genuine orphans. The intext-questions side (10 questions, 11 raw solutions) had no such hidden mismatch - verified all 11 solutions-manual stems against the 10 chapter stems directly; 9.1-9.10 are clean 1:1 matches and only 9.11 (dissociation constant question) is a genuine, simple trailing orphan with no chapter counterpart. One genuine, unfixable content gap remains: q_5.25 (violet colour of [Ti(H2O)6]3+ via crystal field theory) has NO answer anywhere in this solutions manual under any number - confirmed by searching the whole document for 'violet' and 'crystal field theory' and finding no match to this specific question. Left empty per Rule 5 (nothing invented); will need stage 5's attention (or acceptance as a permanent gap). Separately, gate_solutions_present initially flagged ex_5.2 and ex_5.3 (both split into :::part blocks) as having no solution: each part had only a :::answer (a direct formula/IUPAC name, no narrative), which the gate does not count as a 'solution'. This is not a real gap - the source's own 'Solution' heading for these two examples contains nothing but these direct results (no derivation) - so each part's solution field was set equal to its own answer field (10 parts total), faithfully representing that the answer IS the solution for this kind of direct lookup question, not an invention of new content.
