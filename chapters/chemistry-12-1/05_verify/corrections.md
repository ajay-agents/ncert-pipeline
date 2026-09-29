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

## Follow-up pass (post-hoc review fixes, 2026-09-25)

### ex_1.9 — solution (en)
- **Confidence:** high
- **Reason:** OCR misread the Greek capital Delta as a diaeresis-A plus stray glyph merge ('Ä T f' for 'Δ T_f').
- **Found:**
  > \ddot{\mathrm{A}} T_{\mathrm{f}}
- **Should be:**
  > \Delta T_{\mathrm{f}}

### q_1.14 — solution (en)
- **Confidence:** high
- **Reason:** Third-party solutions manual answers with Delta_sol H (enthalpy of solution) throughout, but the question (verified verbatim against chapter.en.pdf's own exercise 1.14 text) asks about Delta_mix H (enthalpy of mixing) -- the quantity actually tied to Raoult's-law deviations. Corrected to match the question's own, textbook-verified terminology.
- **Found:**
  > \Delta_{\mathrm{sol}} H=0
- **Should be:**
  > \Delta_{\text{mix}} H=0

### q_1.14 — solution (en)
- **Confidence:** high
- **Reason:** Same Delta_sol -> Delta_mix terminology fix as above.
- **Found:**
  > \Delta_{\text {sol }} H=\text { Positive }
- **Should be:**
  > \Delta_{\text {mix }} H=\text { Positive }

### q_1.14 — solution (en)
- **Confidence:** high
- **Reason:** Same Delta_sol -> Delta_mix terminology fix as above.
- **Found:**
  > \Delta_{\text {sol }} H=\text { Negative }
- **Should be:**
  > \Delta_{\text {mix }} H=\text { Negative }

### q_1.17 — solution (en)
- **Confidence:** high
- **Reason:** Same-page self-contradiction: the defining sentence says 100 g, but the very next line's own arithmetic (1000/18 = 55.56 mol) already commits to 1000 g -- the correct definition of molality. Confirmed via direct page image (00_raw/solutions.en.pdf) that the source itself prints '100 g' here.
- **Found:**
  > 1 molal solution means 1 mol of the solute is present in 100 g of the solvent (water).
- **Should be:**
  > 1 molal solution means 1 mol of the solute is present in 1000 g of the solvent (water).

### it_1.2 — solution (en)
- **Confidence:** high
- **Reason:** Dropped decimal point in the atomic mass of Cl (35.5 written as 355); the immediately following result (154 g/mol) already assumes 35.5, confirming this is a transcription slip, not the intended value.
- **Found:**
  > 1 \times 12+4 \times 355
- **Should be:**
  > 1 \times 12+4 \times 35.5

### it_1.4 — solution (en)
- **Confidence:** high
- **Reason:** Mislabeled; the question (immutable) says 'molal', and the entire calculation that follows uses the per-1000-g-solvent (molal) convention, not molar. Confirmed via direct page image that the source itself prints 'molar' here despite its own question and math using molal.
- **Found:**
  > 0.25 molar aqueous solution of urea means:
- **Should be:**
  > 0.25 molal aqueous solution of urea means:

### it_1.8 — solution (en)
- **Confidence:** high
- **Reason:** Missing derivation line dropped during extraction (mathpix's own '[Omitted long context line]' marker sits at this exact spot in 01_mathpix/solutions.en.md); restored verbatim from the source PDF page (00_raw/solutions.en.pdf), confirmed via direct page image read.
- **Found:**
  > \Rightarrow 600=(450-700) x_{\mathrm{A}}+700
  > \end{aligned}
- **Should be:**
  > \Rightarrow 600=(450-700) x_{\mathrm{A}}+700 \\
  > & \Rightarrow -100=-250 x_{\mathrm{A}} \\
  > & \Rightarrow x_{\mathrm{A}}=0.4
  > \end{aligned}

### q_1.22 — solution (en)
- **Confidence:** high
- **Reason:** Font-substitution artifact in the source PDF itself (Greek capital Pi, the osmotic-pressure symbol, rendered as the geometric/Cyrillic-looking glyph the extraction preserved as \sqcap); normalized to \Pi, matching how this same symbol is written elsewhere in this chapter (e.g. ex_1.11).
- **Found:**
  > T=300 \mathrm{~K} \sqcap \\
  > & =1.52 \mathrm{bar}
- **Should be:**
  > T=300 \mathrm{~K} \\
  > & \Pi=1.52 \mathrm{bar}

### q_1.22 — solution (en)
- **Confidence:** high
- **Reason:** Same Pi font-substitution artifact as above (Cyrillic-looking glyph for capital Pi).
- **Found:**
  > Applying the relation, $п=$
- **Should be:**
  > Applying the relation, $\Pi=$

### q_1.23 — parts[0].solution (en)
- **Confidence:** high
- **Reason:** Spelling correction of standard chemistry terminology (Van der Waals) -- present verbatim in the source PDF but an unambiguous typo, not a content/values judgment call.
- **Found:**
  > Van der Wall's forces of attraction.
- **Should be:**
  > Van der Waals' forces of attraction.

### q_1.23 — parts[1].solution (en)
- **Confidence:** high
- **Reason:** Same spelling correction as part (i).
- **Found:**
  > Van der Wall's forces of attraction.
- **Should be:**
  > Van der Waals' forces of attraction.

### q_1.23 — parts[2].solution (en)
- **Confidence:** high
- **Reason:** Spelling correction of standard chemistry terminology (ion-dipole) -- present verbatim in the source PDF but an unambiguous typo.
- **Found:**
  > Ion-diople interaction.
- **Should be:**
  > Ion-dipole interaction.

### q_1.25 — parts[3].solution (en)
- **Confidence:** high
- **Reason:** Removes leaked internal pipeline commentary that was mistakenly written into the content field itself instead of the stage report; replaced with the actual structure in inline notation, since the source's own embedded SVG drawing cannot be reproduced as an image in this markdown pipeline.
- **Found:**
  > [structural formula shown inline in source as an embedded SVG image of HO-CH2-CH2-OH; omitted here, see note in stage report]
- **Should be:**
  > $\mathrm{HO-CH_2-CH_2-OH}$

### q_1.31 — solution (en)
- **Confidence:** high
- **Reason:** Same leaked-internal-note defect as q_1.25(iv); replaced with the actual named structures.
- **Found:**
  > [Source shows structural-formula images for acetic acid, trichloroacetic acid and trifluoroacetic acid inline here, before the explanation; omitted, see note in stage report]
- **Should be:**
  > $\mathrm{CH_3COOH}$ (acetic acid), $\mathrm{CCl_3COOH}$ (trichloroacetic acid), $\mathrm{CF_3COOH}$ (trifluoroacetic acid)

### q_1.36 — final_answer (en)
- **Confidence:** high
- **Reason:** The question asks for two values; the final answer previously echoed only the first, even though the second (32 torr) was already derived earlier in this same solution. Completed using that already-derived value -- no new computation invented.
- **Found:**
  > Hence, the vapour pressure of pure liquid A is 280.7 torr.
- **Should be:**
  > Hence, the vapour pressure of pure liquid A is 280.7 torr. Vapour pressure of liquid A in the solution, $p_A = 32$ torr.

### q_1.37 — solution (en)
- **Confidence:** high
- **Reason:** Corrupted table header ('Ptota') already present in the extracted data; corrected against the question's own clean header for the same row two lines above.
- **Found:**
  > | Ptota $\boldsymbol{(} \mathbf{m m ~ H g} \boldsymbol{)}$ |
- **Should be:**
  > | $P_{\text{total}}$ (mm Hg) |

### q_1.37 — solution (en)
- **Confidence:** high
- **Reason:** Corrupted table header (duplicated multiplication sign, dropped the x_acetone variable) already present in the extracted data; corrected against the question's own clean header for the same row.
- **Found:**
  > | 100 × × acetone |
- **Should be:**
  > | $100 \times x_{\text{acetone}}$ |

### q_1.38 — solution (en)
- **Confidence:** high
- **Reason:** Duplicated line not present in the source (confirmed against 00_raw/solutions.en.pdf); removed the repeat.
- **Found:**
  > And, partial vapour pressure of toluene, $p_{t}=x_{t} \times p_{t}$
  > And, partial vapour pressure of toluene, $p_{t}=x_{t} \times p_{t}$
- **Should be:**
  > And, partial vapour pressure of toluene, $p_{t}=x_{t} \times p_{t}$

### ex_1.5 — solution (en)
- **Confidence:** high
- **Reason:** Mismatched \left[...\right. bracket construct (valid LaTeX but fragile) rendered as a stray literal period in stage 9's hand-written converter ('p CH2Cl2 O = . 415'); rewritten as a clean, self-contained expression at the data layer so the bug cannot recur if the chapter is re-rendered.
- **Found:**
  > $\left[p_{\mathrm{CH}_{2} \mathrm{Cl}_{2}}^{O}=\right.$ 415 mm Hg and $p_{\mathrm{CHCl}_{3}}^{o}=200 \mathrm{~mm} \mathrm{Hg}$ ]
- **Should be:**
  > $p_{\mathrm{CH}_{2} \mathrm{Cl}_{2}}^{O}=415 \mathrm{~mm} \mathrm{Hg}$ and $p_{\mathrm{CHCl}_{3}}^{o}=200 \mathrm{~mm} \mathrm{Hg}$

### q_1.41 — solution (en)
- **Confidence:** high
- **Reason:** Typo, unambiguous.
- **Found:**
  > Appling the following relation,
- **Should be:**
  > Applying the following relation,

### ex_1.4 — solution (en)
- **Confidence:** high
- **Reason:** The much-less-than symbol was left outside math delimiters, so stage 9's LaTeX-to-HTML converter (which only converts LaTeX commands inside $...$) showed the literal command text '\ll' on the page instead of '≪'. Wrapped it in math delimiters at the data layer instead of patching only the rendered HTML, so the fix survives any future re-render.
- **Found:**
  > it is \ll 55.5
- **Should be:**
  > it is $\ll$ 55.5
