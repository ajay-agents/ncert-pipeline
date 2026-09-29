# Match report

- **questions_in_chapter:** 11
- **solutions_in_manual:** 14
- **matched:** 11
- **hand_matched_due_to_numbering_drift:** True
- **drift_explanation:** Solutions manual inserts 3 extra questions (its own Q4: bond-price calculation; Q5: why speculative demand is inversely related to interest rate; Q6: liquidity trap) immediately after its own Q3, none of which exist among the chapter's own current 11 exercises. From that point on the solutions manual's own printed numbering runs exactly 3 ahead of the chapter's own exercise numbers: chapter Q4-Q11 correspond to solutions manual Q7-Q14, not solutions Q4-Q11. A plain number-based join would have silently produced 8 wrong pairings (q_3.4 through q_3.11) while needs_review would show only solutions Q12/13/14 as 'orphans' - confirmed by running match.join_solutions() on hand-typed stand-ins as a diagnostic before building this chapter's own merge by hand, content-verified pair by pair.
## hand_verified_pairs (11)
- q_3.1 <- solutions Q1 (barter system)
- q_3.2 <- solutions Q2 (functions of money) + fig_3_1 (Functions of Money flowchart)
- q_3.3 <- solutions Q3 (transaction demand for money)
- q_3.4 <- solutions Q7 (alternative definitions of money supply)
- q_3.5 <- solutions Q8 (legal tender / fiat money)
- q_3.6 <- solutions Q9 (high powered money)
- q_3.7 <- solutions Q10 (functions of a commercial bank)
- q_3.8 <- solutions Q11 (money multiplier)
- q_3.9 <- solutions Q12 (instruments of monetary policy)
- q_3.10 <- solutions Q13 (commercial bank as creator of money) + final_answer
- q_3.11 <- solutions Q14 (lender of last resort)

## orphan_solutions_discarded (3)
- solutions Q4: bond-price calculation (Rs 500 bond, 5% interest, 2 years) - no matching exercise in the chapter's current 11
- solutions Q5: why speculative demand for money is inversely related to the rate of interest - no matching exercise
- solutions Q6: what is 'liquidity trap' - no matching exercise

- **orphan_disposition:** Discarded, not fabricated into new exercise items - these 3 solutions-manual entries answer questions that do not exist anywhere in the chapter's own current (rationalised) 11 exercises; inventing a :::question item not actually printed in chapter.en.pdf would violate Rule 4 (exercise question text must be transcribed from the textbook itself, never authored). Same established practice as physics-12-3/physics-12-5's own documented cases in step_2/PROMPT.md. Their content thematically echoes Box 3.1's own bond-pricing/speculative-demand/liquidity-trap narrative, suggesting the solutions manual added its own practice questions covering that optional box - but the box itself poses no formal numbered question, so there is genuinely no textbook question for these solutions to attach to.
## excluded_non_item_content (5)
- 'Key Concepts' glossary (term-pair table, e.g. 'Barter exchange / Double coincidence of wants') - same exclusion pattern as economics-12-1's own Key Concepts glossary, no item home.
- Box 3.1 'Demand and Supply for Money: A Detailed Discussion' - narrative content with embedded present-value calculations (Rs 109.29, Rs 107.33) and fig_3_0 (Fig 3.1, Speculative Demand for Money), but no textbook 'Example:' label anywhere - matches this pipeline's own established rule of only extracting what the source itself formally demarcates as a worked example.
- Box No. 3.2 'Demonetisation' - purely descriptive narrative, no question or worked calculation.
- Appendix 3.1 (Sum of an Infinite Geometric Series derivation), Appendix 3.2 (Table 3.4, M1/M3 money supply data through 2024-25), Appendix 3.3 (Table 3.5, monetary base sources data through 2024-25) - all three explicitly labelled 'Appendix' in the printed page margin (confirmed via direct PDF page-16/17 text extraction), same updated-data-reprint-appendix pattern already established and excluded in economics-12-1/12-2.
- 2 footnote blocks ([^0], [^1]) - confirmed neither falls inside any of the 11 exercises.

## needs_review (0)
