# Match report

- **lang:** hi
- **intext_join:** {'questions': 10, 'solutions': 11, 'matched': 10, 'unmatched_questions': [], 'orphan_solutions': ['5.11'], 'duplicate_solutions': [], 'needs_review': ['5.11']}
- **exercise_join:** {'questions': 32, 'solutions': 32, 'matched': 32, 'unmatched_questions': [], 'orphan_solutions': [], 'duplicate_solutions': [], 'needs_review': []}
## gate_counts (0)

## gate_solutions_present (2)
- q_5.16: no solution (hi)
- q_5.25: no solution (hi)

- **gate_bilingual_note:** expected - Hindi-only chapter, no English source
## manual_fixes (2)
- it_sol_5.11 ([Cu(NH3)4]2+ beta4 dissociation-constant question): orphan solution, no matching in-text question anywhere in the current chapter (only 10 genuine in-text questions, 5.1-5.10, exist) - discarded per Rule 5, not attached to anything.
- q_5.25 / sol_5.25: join_solutions() matched these by number alone, but content is unrelated - q_5.25 asks for a crystal-field-theory explanation of [Ti(H2O)6]3+'s violet color; the solutions manual's own entry 25 is about stability of coordination compounds in solution (a 'Rationalised' curriculum edition mismatch - confirmed no other numbered entry in the manual answers q_5.25's real topic either). q_5.25's solution field was manually cleared (was wrongly holding sol_5.25's stability-discussion text) rather than keep a confidently wrong answer; sol_5.25's real content has no home and was discarded.
