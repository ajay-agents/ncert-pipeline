### q_1.33 — question (en)
- **Confidence:** high
- **Reason:** Verified against chapter.en.pdf page 30: the source clearly prints '19.5 g' with no space/period artifact. The mathpix extraction had glued the question number '1.33' directly onto the start of the sentence and mis-OCR'd '19.5' as '19. 5' (spurious period+space) - confirmed as a pure OCR artifact, not the source's own text, now that the actual page is legible.
- **Found:**
  > 19. 5 g of $\mathrm{CH}_{2} \mathrm{FCOOH}$
- **Should be:**
  > 19.5 g of $\mathrm{CH}_{2} \mathrm{FCOOH}$

### ex_1.5 — solution (en)
- **Confidence:** high
- **Reason:** Mathpix mis-parsed a two-column derivation into a scrambled array (page 11): dropped units, truncated 25.5g to 25g, dropped the CHCl3-moles and total-moles intermediate results entirely. Verified against the source page.
- **Found:**
  > $$
  > \begin{array}{ll}
  > \text { Moles of } \mathrm{CH}_{2} \mathrm{Cl}_{2} & =\frac{40}{85 \mathrm{~g} \mathrm{r}} \\
  > & =\frac{25}{119.5} \\
  > \text { Moles of } \mathrm{CHCl}_{3} & \\
  > \text { Total number of moles } & =0.47+ \\
  > x_{\mathrm{CH}_{2} \mathrm{Cl}_{2}}=\frac{0.47 \mathrm{~mol}}{0.683 \mathrm{~mol}} & =0.688 \\
  > x_{\mathrm{CHCl}_{3}}=1.00-0.688 & =0.312
  > \end{array}
  > $$
- **Should be:**
  > $$
  > \begin{aligned}
  > \text { Moles of } \mathrm{CH}_{2} \mathrm{Cl}_{2} & =\frac{40 \mathrm{~g}}{85 \mathrm{~g} \mathrm{~mol}^{-1}}=0.47 \mathrm{~mol} \\
  > \text { Moles of } \mathrm{CHCl}_{3} & =\frac{25.5 \mathrm{~g}}{119.5 \mathrm{~g} \mathrm{~mol}^{-1}}=0.213 \mathrm{~mol} \\
  > \text { Total number of moles } & =0.47 \mathrm{~mol}+0.213 \mathrm{~mol}=0.683 \mathrm{~mol} \\
  > x_{\mathrm{CH}_{2} \mathrm{Cl}_{2}}=\frac{0.47 \mathrm{~mol}}{0.683 \mathrm{~mol}} & =0.688 \\
  > x_{\mathrm{CHCl}_{3}}=1.00-0.688 & =0.312
  > \end{aligned}
  > $$

### ex_1.7 — solution (en)
- **Confidence:** high
- **Reason:** Genuinely truncated in the mathpix extraction - the source (pages 17-18) continues with the full delta-Tb calculation and final boiling point, confirmed against the actual page images.
- **Found:**
  > For water, change in boiling point
- **Should be:**
  > For water, change in boiling point $\Delta T_{\mathrm{b}}=K_{\mathrm{b}} \times m=0.52 \mathrm{~K} \mathrm{~kg} \mathrm{~mol}^{-1} \times 0.1 \mathrm{~mol} \mathrm{~kg}^{-1}=0.052 \mathrm{~K}$
  > 
  > Since water boils at 373.15 K at 1.013 bar pressure, therefore, the boiling point of solution will be $373.15+0.052=373.202 \mathrm{~K}$.

### it_1.5 — solution (en)
- **Confidence:** high
- **Reason:** User-approved: solutions manual page 4 shows part (a)'s molality as one compound stacked fraction (20/166 over 0.08) = 1.506 m; the extraction garbled the second line into a division-by-zero that matches no real intermediate value.
- **Found:**
  > & \frac{20}{166} \mathrm{~m} \\
  > = & \frac{16.08}{0} \mathrm{~m} \\
- **Should be:**
  > = & \frac{\frac{20}{166}}{0.08} \mathrm{~m} \\

### q_1.32 — solution (en)
- **Confidence:** high
- **Reason:** Solution's own delta-Tf derivation stops right after the multiplication without ever writing the numeric result - source page 40 completes the same aligned block with a final '= 0.65 K' line (the item's separate answer field already states 0.65 K, so nothing is invented, just restoring the missing last derivation line).
- **Found:**
  > & =1.0655 \times 1.86 \mathrm{~K} \mathrm{~kg} \mathrm{~mol}^{-1} \times 0.3264 \mathrm{~mol} \mathrm{~kg}^{-1}
  > \end{aligned}
- **Should be:**
  > & =1.0655 \times 1.86 \mathrm{~K} \mathrm{~kg} \mathrm{~mol}^{-1} \times 0.3264 \mathrm{~mol} \mathrm{~kg}^{-1} \\
  > & =0.65 \mathrm{~K}
  > \end{aligned}

### ex_1.1 — solution (en)
- **Confidence:** high
- **Reason:** Discovered during stage 9 design (not caught at stage 5): mathpix mis-OCR'd the x_glycol mole-fraction formula's numerator as 'moles of_{2} H_{6} O_{2}' (dropping the leading C) and left a stray superscript degree sign after 'moles' in the denominator. Verified against chapter.en.pdf page 4 (Example 1.1): the printed formula is x_glycol = (moles of C2H6O2) / (moles of C2H6O2 + moles of H2O) = 0.322 mol / (0.322 mol + 4.444 mol) = 0.068 - the numeric result (0.068) was already correct and unaffected; only the symbolic display of the formula itself was garbled.
- **Found:**
  > \mathrm{x}_{\text {glycol }}=\frac{\mathrm{moles} \mathrm{of}_{2} \mathrm{H}_{6} \mathrm{O}_{2}}{\text { moles of } \mathrm{C}_{2} \mathrm{H}_{6} \mathrm{O}_{2}+\mathrm{moles}^{\circ} \text { of } \mathrm{H}_{2} \mathrm{O}}
- **Should be:**
  > \mathrm{x}_{\text {glycol }}=\frac{\text { moles of } \mathrm{C}_{2} \mathrm{H}_{6} \mathrm{O}_{2}}{\text { moles of } \mathrm{C}_{2} \mathrm{H}_{6} \mathrm{O}_{2}+\text { moles of } \mathrm{H}_{2} \mathrm{O}}
