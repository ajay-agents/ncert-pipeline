### ex_2.7 — solution (en)
- **Confidence:** high
- **Reason:** Mathpix OCR rendered the sulfate ion's element symbol with a lowercase 'o' instead of the capital 'O' the PDF clearly shows. (promoted past the medium hold after explicit user sign-off)
- **Found:**
  > \lambda_{\mathrm{So}_{4}^{2-}}^{o}
- **Should be:**
  > \lambda_{\mathrm{SO}_{4}^{2-}}^{o}

### q_2.1 — solution (en)
- **Confidence:** high
- **Reason:** OCR misread 'Al' as 'AI' (capital I) - same list correctly rendered as 'Al' in this item's own question field, and the solutions-manual page confirms 'Al'.
- **Found:**
  > Mg, AI, Zn, Fe, Cu
- **Should be:**
  > Mg, Al, Zn, Fe, Cu

### q_2.1 — final_answer (en)
- **Confidence:** high
- **Reason:** Same OCR error repeated in the answer restatement.
- **Found:**
  > Mg, AI, Zn, Fe, Cu
- **Should be:**
  > Mg, Al, Zn, Fe, Cu

### q_2.5 — parts[3].question (en)
- **Confidence:** high
- **Reason:** OCR misread the liquid-state marker '(l)' as digit '(1)' - confirmed against both the English question page and the solutions manual's independent restatement.
- **Found:**
  > \mathrm{Br}_{2}(1)
- **Should be:**
  > \mathrm{Br}_{2}(l)

### it_2.1 — solution (en)
- **Confidence:** high
- **Reason:** OCR misread digit '1' as letter 'l' in the cell notation - solutions manual page clearly shows '1M'.
- **Found:**
  > \mathrm{Mg}^{2+}(\mathrm{aq}, \mathrm{lM})
- **Should be:**
  > \mathrm{Mg}^{2+}(\mathrm{aq}, 1 \mathrm{M})

### it_2.5 — solution (en)
- **Confidence:** high
- **Reason:** Scrambled OCR reading order - the manual's own layout puts 'Applying Nernst equation we have:' before the derivation, not after it as trailing fragments; 'Given that' duplicates context already in the prompt field and isn't part of the worked derivation. (promoted past the medium hold after explicit user sign-off)
- **Found:**
  > $$
  > \begin{aligned}
  > & \mathrm{Ni}_{(s)}+2 \mathrm{Ag}^{+}(0.002 \mathrm{M}) \rightarrow \mathrm{Ni}^{2+}(0.160 \mathrm{M})+2 \mathrm{Ag}_{(s)} \\
  > & E_{(\text {cell) }}^{\ominus}=1.05 \mathrm{~V} \\
  > & E_{\text {(cell) }}=E_{\text {(cell) }}^{\ominus}-\frac{0.0591}{n} \log \frac{\left[\mathrm{Ni}^{2+}\right]}{\left[\mathrm{Ag}^{+}\right]^{2}} \\
  > & =1.05-\frac{0.0591}{2} \log \frac{(0.160)}{(0.002)^{2}} \\
  > & =1.05-0.02955 \log \frac{0.16}{0.000004} \\
  > & =1.05-0.02955 \log 4 \times 10^{4} \\
  > & =1.05-0.02955(\log 10000+\log 4) \\
  > & =1.05-0.02955(4+0.6021) \\
  > & =0.914 \mathrm{~V}
  > \end{aligned}
  > $$
  > 
  > Given that
  > Applying Nernst equation we have:
- **Should be:**
  > Applying Nernst equation we have:
  > 
  > $$
  > \begin{aligned}
  > & \mathrm{Ni}_{(s)}+2 \mathrm{Ag}^{+}(0.002 \mathrm{M}) \rightarrow \mathrm{Ni}^{2+}(0.160 \mathrm{M})+2 \mathrm{Ag}_{(s)} \\
  > & E_{(\text {cell) }}^{\ominus}=1.05 \mathrm{~V} \\
  > & E_{\text {(cell) }}=E_{\text {(cell) }}^{\ominus}-\frac{0.0591}{n} \log \frac{\left[\mathrm{Ni}^{2+}\right]}{\left[\mathrm{Ag}^{+}\right]^{2}} \\
  > & =1.05-\frac{0.0591}{2} \log \frac{(0.160)}{(0.002)^{2}} \\
  > & =1.05-0.02955 \log \frac{0.16}{0.000004} \\
  > & =1.05-0.02955 \log 4 \times 10^{4} \\
  > & =1.05-0.02955(\log 10000+\log 4) \\
  > & =1.05-0.02955(4+0.6021) \\
  > & =0.914 \mathrm{~V}
  > \end{aligned}
  > $$

### it_2.8 — solution (en)
- **Confidence:** high
- **Reason:** Every other instance of the limiting-molar-conductivity symbol in this field is rendered Lambda_m^0; this one OCR'd the same superscript-naught glyph as phi. (promoted past the medium hold after explicit user sign-off)
- **Found:**
  > the $\Lambda_{m}^{\phi}$ value of water can be determined.
- **Should be:**
  > the $\Lambda_{m}^{0}$ value of water can be determined.

### q_2.13 — parts[1].question (en)
- **Confidence:** high
- **Reason:** Textbook prints the element symbol capitalized ('Al'); extraction has it lowercase.
- **Found:**
  > 40.0 g of al from molten
- **Should be:**
  > 40.0 g of Al from molten

### q_2.17 — solution (en)
- **Confidence:** high
- **Reason:** Manual's own garbled two-column wrap dropped the word 'is' between 'Fe3+(aq)' and 'not feasible' in part (iv)'s conclusion - confirmed legible on the source page. (promoted past the medium hold after explicit user sign-off)
- **Found:**
  > \text { and } \mathrm{Fe}_{3+(a q)} \\
- **Should be:**
  > \text { and } \mathrm{Fe}_{3+(a q)} \text { is } \\

### q_2.17 — solution (en)
- **Confidence:** high
- **Reason:** Part (iv)'s combined-equation line (with its own horizontal rule, matching parts (i)-(iii)'s pattern) is missing from the extraction - legible on the source page as faint/overlapping text, and the -0.03V value is independently corroborated by arithmetic (0.77V - 0.80V = -0.03V). (promoted past the medium hold after explicit user sign-off)
- **Found:**
  > \mathrm{Fe}^{3+}{ }_{(a q)}+\mathrm{e}^{-} \longrightarrow \mathrm{Fe}^{2+}(a q) & ; E^{0}=+0.77 \mathrm{~V}
  > \end{array}
- **Should be:**
  > \mathrm{Fe}^{3+}{ }_{(a q)}+\mathrm{e}^{-} \longrightarrow \mathrm{Fe}^{2+}(a q) & ; E^{0}=+0.77 \mathrm{~V} \\
  > \hline \mathrm{Ag}_{(s)}+\mathrm{Fe}^{3+}{ }_{(a q)} \longrightarrow \mathrm{Ag}_{(a q)}^{+}+\mathrm{Fe}^{2+}{ }_{(a q)} & ; E^{0}=-0.03 \mathrm{~V}
  > \end{array}

### it_2.15 — solution (en)
- **Confidence:** high
- **Reason:** Discovered during stage 9 design read-back, not caught at stage 5: mathpix mis-OCR'd the liquid-state marker '(l)' in the cathode half-reaction as '(f /)'. Verified against solutions.en.pdf page 7 (Question 3.15): the printed reaction is O2(g)+4H+(aq)+4e- -> 2H2O(l).
- **Found:**
  > \mathrm{H}_{2} \mathrm{O}_{(f /)}
- **Should be:**
  > \mathrm{H}_{2} \mathrm{O}_{(l)}

### it_2.15 — solution (en)
- **Confidence:** high
- **Reason:** Same page, the overall reaction: mathpix mis-OCR'd 'Fe(s)' as 'Fe(x)' and 'H2O(l)' as 'H2O(r)'. Verified against solutions.en.pdf page 7: the printed overall reaction is 2Fe(s)+O2(g)+4H+(aq) -> 2Fe2+(aq)+2H2O(l).
- **Found:**
  > 2 \mathrm{Fe}_{(x)}+\mathrm{O}_{2(g)}+4 \mathrm{H}_{(a q)}^{+} \longrightarrow 2 \mathrm{Fe}_{(a q)}^{2+}+2 \mathrm{H}_{2} \mathrm{O}_{(r)}
- **Should be:**
  > 2 \mathrm{Fe}_{(s)}+\mathrm{O}_{2(g)}+4 \mathrm{H}_{(a q)}^{+} \longrightarrow 2 \mathrm{Fe}_{(a q)}^{2+}+2 \mathrm{H}_{2} \mathrm{O}_{(l)}
