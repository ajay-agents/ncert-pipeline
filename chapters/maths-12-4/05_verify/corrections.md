### q_4.4.12 — solution (hi)
- **Confidence:** high
- **Reason:** solutions.hi.pdf page 22 (its own internal page 5) literally prints '|A| = 54 - 56 = -2' right after defining B's cofactors - a source-side typo mislabeling B's own determinant as |A|. Prior extraction silently 'corrected' this to |B|, deviating from verbatim source transcription. Confirmed against the actual page image by the stage-5 verification batch.
- **Found:**
  > $|B|=54-56=-2 \neq 0 \quad \Rightarrow B^{-1}$ का अस्तित्व है।
- **Should be:**
  > $|A|=54-56=-2 \neq 0 \quad \Rightarrow B^{-1}$ का अस्तित्व है।

### q_4.9.2 — solution (hi)
- **Confidence:** high
- **Reason:** solutions.hi.pdf's own misc-section page (its 'प्रश्न 3') literally prints the concluding line as '= sin^2(alpha) + sin^2(alpha) = 1' (both terms sin^2), confirmed at 400dpi zoom by the stage-5 verification batch - a genuine source-side typo (mathematically it should be cos^2, but that judgment isn't this stage's call per step_5/verify.md). Prior extraction silently corrected the second term to cos^2, deviating from verbatim transcription of what's actually printed.
- **Found:**
  > & =\sin ^{2} \alpha+\cos^{2} \alpha=1
- **Should be:**
  > & =\sin ^{2} \alpha+\sin^{2} \alpha=1
