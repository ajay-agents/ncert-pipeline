### q_11.10 — parts[1].solution (hi)
- **Confidence:** high
- **Reason:** Same-page self-contradiction: the question states the ball's speed as 1.0 km/s (same as part (a)'s bullet), but the solution's own restatement drops 'km' and computes with v=1 m/s, giving a wavelength three orders of magnitude too large. Confirmed against solutions.hi.pdf p.49 -- genuinely printed this way in the source, not an OCR artifact. Fixed per explicit user decision (same-page self-contradiction precedent), not silently.
- **Found:**
  > बॉल का द्रव्यमान, $m=0.060 \mathrm{~kg}$ तथा बॉल की चाल, $v=1 \mathrm{~m} / \mathrm{s}$
  > 
  > $$
  > \begin{aligned}
  > \lambda & =\frac{h}{m v}=\frac{6.63 \times 10^{-34}}{0.060 \times 1} \\
  > & =1.1 \times 10^{-32} \mathrm{~m}
  > \end{aligned}
  > $$
- **Should be:**
  > बॉल का द्रव्यमान, $m=0.060 \mathrm{~kg}$ तथा बॉल की चाल, $v=1.0 \mathrm{~km} / \mathrm{s}=1000 \mathrm{~m} / \mathrm{s}$
  > 
  > $$
  > \begin{aligned}
  > \lambda & =\frac{h}{m v}=\frac{6.63 \times 10^{-34}}{0.060 \times 1000} \\
  > & =1.1 \times 10^{-35} \mathrm{~m}
  > \end{aligned}
  > $$

### q_11.10 — parts[1].final_answer (hi)
- **Confidence:** high
- **Reason:** Same fix as parts[1].solution above -- the final answer must match the corrected derivation.
- **Found:**
  > $\lambda = 1.1 \times 10^{-32} \mathrm{~m}$
- **Should be:**
  > $\lambda = 1.1 \times 10^{-35} \mathrm{~m}$
