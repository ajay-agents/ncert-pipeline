### ex_2.4 — parts[0].solution (hi)
- **Confidence:** high
- **Reason:** PDF page 56 (index 12) step (iii) shows the factor `(1 - 1/√2)` wrapped in parentheses after the `-q²/4πε₀d` coefficient; the extracted text dropped the parentheses, leaving the multiplication ambiguous/incorrect as written.
- **Found:**
  > \frac{-q^{2}}{4 \pi \varepsilon_{o} d} 1-\frac{1}{\sqrt{2}}
- **Should be:**
  > \frac{-q^{2}}{4 \pi \varepsilon_{o} d}\left(1-\frac{1}{\sqrt{2}}\right)

### ex_2.4 — parts[0].solution (hi)
- **Confidence:** high
- **Reason:** Same page, step (iv): PDF shows `(2 - 1/√2)` in parentheses after the coefficient; extraction dropped the parentheses here too. (Applied after the correction above, against the once-again-unique remaining `2-` occurrence.)
- **Found:**
  > \frac{-q^{2}}{4 \pi \varepsilon_{o} d} 2-\frac{1}{\sqrt{2}}
- **Should be:**
  > \frac{-q^{2}}{4 \pi \varepsilon_{o} d}\left(2-\frac{1}{\sqrt{2}}\right)
