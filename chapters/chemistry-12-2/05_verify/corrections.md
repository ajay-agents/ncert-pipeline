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

### q_2.4 — solution (en)
- **Confidence:** high
- **Reason:** Table value for E(Cr3+/Cr) is -0.74 V; the very next line's cell-potential subtraction already uses -0.74, confirmed against this chapter's own reliably-extracted standard-potential table and the extract_match manifest note.
- **Found:**
  > E_{\mathrm{Cr}^{3+} / \mathrm{Cr}}^{\ominus}=0.74 \mathrm{~V}
- **Should be:**
  > E_{\mathrm{Cr}^{3+} / \mathrm{Cr}}^{\ominus}=-0.74 \mathrm{~V}

### q_2.6 — final_answer (en)
- **Confidence:** high
- **Reason:** Leaked internal reviewer/annotator commentary ('as stated'...'see report') is not source content and must not render on the page. The underlying 1.104/1.04 V self-contradiction is the source's own (confirmed against solutions.en.md) and is reported separately, not silently corrected.
- **Found:**
  > $E^{\ominus} = 1.104 \mathrm{~V}$ (as stated); $\Delta_{r}G^{\ominus} = -213.04 \mathrm{~kJ}$ (calculation shown uses $1.04$, not $1.104$ — see report)
- **Should be:**
  > $E^{\ominus} = 1.104 \mathrm{~V}$; $\Delta_{r}G^{\ominus} = -213.04 \mathrm{~kJ}$

### q_2.7 — solution (en)
- **Confidence:** high
- **Reason:** Literal markdown heading syntax leaked into solution prose (heading-bleed artifact); render as a bold inline label, not a raw '##'.
- **Found:**
  > ## Molar conductivity:
- **Should be:**
  > **Molar conductivity:**

### q_2.7 — solution (en)
- **Confidence:** high
- **Reason:** OCR ell-vs-capital-I confusion; this item's own earlier line correctly uses lowercase l ('Since a=1, l=1').
- **Found:**
  > Now, $I=1$ and $A=\mathrm{V}$
- **Should be:**
  > Now, $l=1$ and $A=\mathrm{V}$

### q_2.10 — solution (en)
- **Confidence:** high
- **Reason:** Every parallel row uses kappa; this one alone uses capital K, an OCR symbol substitution (also flagged in this chapter's own extract_match manifest note).
- **Found:**
  > Then, $\mathrm{K}=11.85 \times 10^{-4} \mathrm{~S} \mathrm{~cm}^{-1},
- **Should be:**
  > Then, $\kappa=11.85 \times 10^{-4} \mathrm{~S} \mathrm{~cm}^{-1},

### q_2.10 — solution (en)
- **Confidence:** high
- **Reason:** Every parallel row computes Lambda_m = kappa/c; this row alone has Lambda_m mis-OCR'd as kappa on the left side.
- **Found:**
  > \therefore \kappa=\frac{\kappa}{c} \\
- **Should be:**
  > \therefore \Lambda_{m}=\frac{\kappa}{c} \\

### q_2.10 — solution (en)
- **Confidence:** high
- **Reason:** Capital K used instead of kappa, same OCR symbol confusion as the other rows in this table.
- **Found:**
  > & \Lambda_{m}=\frac{K}{c} \\
  > = & \frac{106.74
- **Should be:**
  > & \Lambda_{m}=\frac{\kappa}{c} \\
  > = & \frac{106.74

### q_2.10 — solution (en)
- **Confidence:** high
- **Reason:** OCR word confusion; describing a graph's y-intercept, not an interruption.
- **Found:**
  > Since the line interrupts
- **Should be:**
  > Since the line intercepts

### q_2.11 — solution (en)
- **Confidence:** high
- **Reason:** The item's own question field states this conductivity value with units S cm^-1; the solution's restatement mistakenly drops the 'c', giving a unit 1000x too large.
- **Found:**
  > \kappa=7.896 \times 10^{-5} \mathrm{~S} \mathrm{~m}^{-1} \mathrm{c}
- **Should be:**
  > \kappa=7.896 \times 10^{-5} \mathrm{~S} \mathrm{~cm}^{-1} \mathrm{c}

### q_2.11 — solution (en)
- **Confidence:** high
- **Reason:** Capital K used instead of kappa; kappa is used correctly earlier in this same solution ('Given, kappa=...').
- **Found:**
  > \Lambda_{m}=\frac{K}{\mathrm{c}}
- **Should be:**
  > \Lambda_{m}=\frac{\kappa}{\mathrm{c}}

### ex_2.9 — solution (en)
- **Confidence:** high
- **Reason:** Lowercase k mis-OCR'd for the acid dissociation constant K_a; this item's own final_answer field already correctly uses K_a for this same value.
- **Found:**
  > \mathrm{k}=\frac{\mathrm{c} \alpha^{2}}{(1-\alpha)}
- **Should be:**
  > K_{a}=\frac{\mathrm{c} \alpha^{2}}{(1-\alpha)}

### ex_2.9 — solution (en)
- **Confidence:** high
- **Reason:** Molar conductivity's unit is always cm^2 mol^-1; the very next line re-uses this same value correctly as cm^2 mol^-1 (OCR digit confusion 2 -> 3).
- **Found:**
  > 48.15 \mathrm{~S} \mathrm{~cm}^{3} \mathrm{~mol}^{-1}
- **Should be:**
  > 48.15 \mathrm{~S} \mathrm{~cm}^{2} \mathrm{~mol}^{-1}

### it_2.9 — solution (en)
- **Confidence:** high
- **Reason:** '\propto' mis-OCR'd for alpha, with a duplicated stray 'c'; alpha is used correctly earlier in this same solution for the identical quantity.
- **Found:**
  > K & =\frac{c \propto c^{2}}{(1-\propto)} \\
- **Should be:**
  > K & =\frac{c \alpha^{2}}{(1-\alpha)} \\

### it_2.8 — solution (en)
- **Confidence:** high
- **Reason:** Missing charge on hydroxide ion; the same symbol appears correctly with its charge two lines later in this same solution.
- **Found:**
  > \lambda_{\mathrm{H}^{+}}^{0}+\lambda_{\mathrm{OH}}^{0} \\
- **Should be:**
  > \lambda_{\mathrm{H}^{+}}^{0}+\lambda_{\mathrm{OH}^{-}}^{0} \\

### it_2.8 — solution (en)
- **Confidence:** high
- **Reason:** Missing '=' and a misplaced alignment marker on this row of the aligned derivation, dropped by OCR; restores the standard Kohlrausch's-law identity chain matching the two rows immediately above it.
- **Found:**
  > \Lambda_{m(\mathrm{HCl})}^{0} & +\Lambda_{m(\mathrm{NaOH})}^{0}-\Lambda_{m(\mathrm{NaCl})}^{0}
- **Should be:**
  > & =\Lambda_{m(\mathrm{HCl})}^{0}+\Lambda_{m(\mathrm{NaOH})}^{0}-\Lambda_{m(\mathrm{NaCl})}^{0}

### q_2.13 — solution (en)
- **Confidence:** high
- **Reason:** Spurious '-1' exponent on the electron symbol; should be a bare minus (electron charge), an OCR artifact repeated several times in this chapter.
- **Found:**
  > \mathrm{Ca}^{2+}+2 \mathrm{e}^{-1} \longrightarrow
- **Should be:**
  > \mathrm{Ca}^{2+}+2 \mathrm{e}^{-} \longrightarrow

### q_2.13 — solution (en)
- **Confidence:** high
- **Reason:** OCR misread 'Al' as 'AI' (capital I), same error already fixed once elsewhere in this chapter (q_2.1).
- **Found:**
  > 27 g of AI = 3 F
- **Should be:**
  > 27 g of Al = 3 F

### q_2.14 — solution (en)
- **Confidence:** high
- **Reason:** Spurious '-1' exponent on electron symbol.
- **Found:**
  > \mathrm{Fe}^{2+} \longrightarrow \mathrm{Fe}^{3+}+\mathrm{e}^{-1}
- **Should be:**
  > \mathrm{Fe}^{2+} \longrightarrow \mathrm{Fe}^{3+}+\mathrm{e}^{-}

### it_2.3 — solution (en)
- **Confidence:** high
- **Reason:** Spurious '-1' exponent on electron symbol.
- **Found:**
  > \mathrm{Fe}^{3+}+\mathrm{e}^{-1} ; E^{\ominus}=-0.77
- **Should be:**
  > \mathrm{Fe}^{3+}+\mathrm{e}^{-} ; E^{\ominus}=-0.77

### q_2.18 — solution (en)
- **Confidence:** high
- **Reason:** Anodic oxidation of sulfate produces peroxodisulfate S2O8^2-, not dithionate S2O6^2-; independently corroborated by the identical reaction with the identical E deg=+1.96V value appearing in this chapter's own reliably-extracted chapter.en.pdf text (not OCR).
- **Found:**
  > \mathrm{S}_{2} \mathrm{O}_{6(a q)}^{2-}
- **Should be:**
  > \mathrm{S}_{2} \mathrm{O}_{8(a q)}^{2-}

### q_2.18 — solution (en)
- **Confidence:** high
- **Reason:** Spurious '-1' exponent on electron symbol; the very next aligned line's correct 4-electron water-oxidation half-reaction uses the plain form.
- **Found:**
  > \mathrm{Cl}_{(a q)}^{-} \longrightarrow 1 / 2 \mathrm{Cl}_{2(g)}+\mathrm{e}^{-1}
- **Should be:**
  > \mathrm{Cl}_{(a q)}^{-} \longrightarrow 1 / 2 \mathrm{Cl}_{2(g)}+\mathrm{e}^{-}

### q_2.18 — solution (en)
- **Confidence:** high
- **Reason:** Word order scrambled by OCR; this exact sentence appears correctly twice earlier in this same item's own solution.
- **Found:**
  > $E^{\circ}$ The reaction with a higher value of takes place at the cathode.
- **Should be:**
  > The reaction with a higher value of $E^{\circ}$ takes place at the cathode.

### q_2.17 — solution (en)
- **Confidence:** high
- **Reason:** OCR word-order scramble ('Since' displaced mid-sentence) and a line-break split inside 'reaction'; all words already present, only reordered/rejoined.
- **Found:**
  > $E^{\circ}$ for the overall reaction is positive, the rea ction between Ag Since + (aq) and $\mathrm{Cu}_{(s)}$ is feasible.
- **Should be:**
  > Since $E^{\circ}$ for the overall reaction is positive, the reaction between Ag+ (aq) and $\mathrm{Cu}_{(s)}$ is feasible.

### q_2.17 — solution (en)
- **Confidence:** high
- **Reason:** OCR spacing/charge-symbol artifacts on the ion notation.
- **Found:**
  > the reaction between Fe 3+ - (aq) and Br (aq) is not feasible.
- **Should be:**
  > the reaction between Fe3+ (aq) and Br- (aq) is not feasible.

### it_2.12 — solution (en)
- **Confidence:** high
- **Reason:** OCR reading-order scramble split one sentence across two rows out of order; all words already present, only reordered, same class of fix as this chapter's own already-applied it_2.5 correction.
- **Found:**
  > $$
  > \begin{aligned}
  > & \mathrm{Cr}_{2} \mathrm{O}_{7}^{2-}+14 \mathrm{H}^{+}+6 \mathrm{e}^{-} \rightarrow 2 \mathrm{Cr}^{3+}+7 \mathrm{H}_{2} \mathrm{O} \text {, the required quantity of electricity will } \\
  > & \text { Therefore, to reduce } 1 \text { mole of } \mathrm{Cr}_{2} \mathrm{O}_{7}^{2-}=6 \mathrm{~F} \\
  > & =6 \times 96487 \mathrm{C} \\
  > & =578922 \mathrm{C}
  > \end{aligned}
  > $$
- **Should be:**
  > $$
  > \begin{aligned}
  > & \mathrm{Cr}_{2} \mathrm{O}_{7}^{2-}+14 \mathrm{H}^{+}+6 \mathrm{e}^{-} \rightarrow 2 \mathrm{Cr}^{3+}+7 \mathrm{H}_{2} \mathrm{O} \\
  > & \text { Therefore, to reduce } 1 \text { mole of } \mathrm{Cr}_{2} \mathrm{O}_{7}^{2-} \text {, the required quantity of electricity will } =6 \mathrm{~F} \\
  > & =6 \times 96487 \mathrm{C} \\
  > & =578922 \mathrm{C}
  > \end{aligned}
  > $$

### it_2.15 — solution (en)
- **Confidence:** high
- **Reason:** Hydrate formula notation: standard convention uses a centered dot between the oxide and its water of hydration, not a comma.
- **Found:**
  > \mathrm{Fe}_{2} \mathrm{O}_{3}, x \mathrm{H}_{2} \mathrm{O}
- **Should be:**
  > \mathrm{Fe}_{2} \mathrm{O}_{3} \cdot x \mathrm{H}_{2} \mathrm{O}
