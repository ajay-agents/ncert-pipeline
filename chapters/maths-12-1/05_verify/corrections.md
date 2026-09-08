### q_1.1.1 — parts[0].solution (hi)
- **Confidence:** high
- **Reason:** Extraction silently "corrected" a labeling swap present in the solutions-manual PDF itself. The source's first bullet for part (i) argues via pairs (1,1),(2,2)...(14,14) — a reflexivity argument — but the printed label is "सममित" (symmetric), not "स्वतुल्य" (reflexive). Verified against the PDF at 500 DPI, unambiguous. The extraction pass replaced the source's actual (apparently erroneous) label with the mathematically-fitting one, violating transcribe-don't-fix. Restoring the PDF's literal wording per stage 5 rules — the source's own inconsistency is not ours to fix.
- **Found:**
  > R स्वतुल्य नहीं है क्योंकि $(1,1),(2,2) \ldots(14,14) \notin \mathrm{R}$.
- **Should be:**
  > R सममित नहीं है क्योंकि $(1,1),(2,2) \ldots(14,14) \notin \mathrm{R}$.

### q_1.2.3 — solution (hi)
- **Confidence:** high
- **Reason:** OCR dropped the negation "नहीं" — the extracted text says f IS injective, contradicting both the question (which asks to prove f is neither injective nor surjective) and the extracted solution's own preceding reasoning (f(1.2)=f(1.9) but 1.2≠1.9, which proves f is NOT injective). Confirmed against solutions.hi.pdf page 11 (उत्तर 3), which reads "∴ f एकैकी फलन नहीं है।"
- **Found:**
  > $\therefore f$ एकैकी फलन है।
- **Should be:**
  > $\therefore f$ एकैकी फलन नहीं है।

### q_1.5.4 — final_answer (hi)
- **Confidence:** high
- **Reason:** the solutions manual's own text (page "उत्तर 10", solutions_p31.png) ends its derivation with "= n", describing the count as equal to the number of permutations of 1,2,...,n — it never writes a factorial symbol. The extracted final_answer added a "!" that is not in the source.
- **Found:**
  > $n$ !
- **Should be:**
  > $n$
