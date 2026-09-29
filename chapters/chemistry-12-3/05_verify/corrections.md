### ex_3.1 — question (en)
- **Confidence:** high
- **Reason:** The extraction merged a stylized sidebar heading label ('Example 3.1') into the running sentence text - the page shows the label positioned beside the paragraph, not part of it.
- **Found:**
  > at different times given Example 3.1 below, calculate the average rate of the reaction:
- **Should be:**
  > at different times given below, calculate the average rate of the reaction:

### ex_3.1 — solution (en)
- **Confidence:** high
- **Reason:** Genuine truncation - the sentence ends mid-equation, dropping the actual numeric result 'L^-1 = 5.12x10^-5 mol L^-1 s^-1' which the source page clearly shows.
- **Found:**
  > \text { So, } r_{\text {inst }} \text { at } 600 \mathrm{~s}=-\left(\frac{0.0165-0.037}{(800-400) \mathrm{s}}\right) \mathrm{mol}
- **Should be:**
  > \text { So, } r_{\text {inst }} \text { at } 600 \mathrm{~s}=-\left(\frac{0.0165-0.037}{(800-400) \mathrm{s}}\right) \mathrm{mol} \mathrm{~L}^{-1}=5.12 \times 10^{-5} \mathrm{~mol} \mathrm{~L}^{-1} \mathrm{~s}^{-1}

### ex_3.2 — solution (en)
- **Confidence:** high
- **Reason:** Unit/exponent error - the page shows the denominator as plain '184 min' (a duration), not '184 min^-1'.
- **Found:**
  > \frac{(2.08-2.33) \mathrm{mol} \mathrm{~L}^{-1}}{184 \mathrm{~min}^{-1}}
- **Should be:**
  > \frac{(2.08-2.33) \mathrm{mol} \mathrm{~L}^{-1}}{184 \mathrm{~min}}

### ex_3.10 — solution (en)
- **Confidence:** high
- **Reason:** The source page prints the units with an inserted 'L' ('J mol L^-1', an unusual but clearly legible printing) in both the numerator and denominator of this step - the extraction silently dropped it to the more 'normal-looking' J mol^-1.
- **Found:**
  > \frac{209000 \mathrm{~J} \mathrm{~mol}^{-1}}{2.303 \times 8.314 \mathrm{~J} \mathrm{~mol}^{-1} \mathrm{~K}^{-1}}
- **Should be:**
  > \frac{209000 \mathrm{~J} \mathrm{~mol} \mathrm{~L}^{-1}}{2.303 \times 8.314 \mathrm{~J} \mathrm{~mol} \mathrm{~L}^{-1} \mathrm{~K}^{-1}}

### q_3.20 — solution (en)
- **Confidence:** high
- **Reason:** OCR garbled the hexane product formula; the solutions-manual page clearly prints 'C6H14(g)', not 'C6H1+(g)'.
- **Found:**
  > \mathrm{C}_{6} \mathrm{H}_{1+(g)}
- **Should be:**
  > \mathrm{C}_{6} \mathrm{H}_{14(g)}

### q_3.22 — solution (en)
- **Confidence:** high
- **Reason:** Table row label swap - the page shows this row (the 3.66e-3... values) headed '1/T / K^-1', not 'ln k'.
- **Found:**
  > $\ln k \longrightarrow$
- **Should be:**
  > $10^{3} \times \frac{1}{T}\left(\mathrm{~K}^{-1}\right) \longrightarrow$

### q_3.22 — solution (en)
- **Confidence:** medium
- **Reason:** Missing row label - the page's own row header for this row is '10^5 x k/s^-1'. [Coordinator note: this was originally reported as medium confidence by the verifying agent but mistakenly applied at high-confidence bookkeeping - the correction itself was already verified against the source page directly and is not in question, only this confidence label was miscopied. Recorded accurately here for the audit trail.]
- **Found:**
  > | 0.0787 | 1.70 | 25.7 | 178 | 2140 |
- **Should be:**
  > $10^{5} \times k/\mathrm{s}^{-1}$ | 0.0787 | 1.70 | 25.7 | 178 | 2140 |

### q_3.22 — solution (en)
- **Confidence:** high
- **Reason:** Missing row label - this unlabeled row genuinely holds the ln k values, matching the page's third table row headed 'ln k'.
- **Found:**
  > | -7.147 | - 4.075 | -1.359 | -0.577 | 3.063 |
- **Should be:**
  > $\ln k$ | -7.147 | - 4.075 | -1.359 | -0.577 | 3.063 |

### q_3.22 — solution (en)
- **Confidence:** high
- **Reason:** Redundant malformed row with no data cells - an artifact of the mislabeling above; the page's own table has only three rows, not four.
- **Found:**
  > | $10^{3} \times \frac{1}{T}\left(\mathrm{~K}^{-1}\right) \longrightarrow$ |  |  |  |  |  |
- **Should be:**
  > 

### q_3.30 — solution (en)
- **Confidence:** high
- **Reason:** Truncated numerator/denominator - the page shows the full '(313-293)/(293x313)'.
- **Found:**
  > \frac{313-2}{293 \times 3}
- **Should be:**
  > \frac{313-293}{293 \times 313}

### ex_3.1 — solution (en)
- **Confidence:** medium
- **Reason:** Mathpix mis-segmented a real sentence and equation (3.3) as raster images (fig_3_16.jpg, fig_3_17.jpg), then the combine step misattributed the Fig 3.2 caption to the wrong image and duplicated the (3.3) marker. Verified by opening the raw image crops directly (fig_3_16.jpg is the "It can be seen (Table 3.1)..." text line, fig_3_17.jpg is equation (3.3), fig_3_18.jpg is the real Fig 3.2 graph) and reading the source page directly. User-approved (medium confidence - exact LaTeX spacing is best-effort reconstruction, not verbatim OCR).
- **Found:**
  > ![](images/fig_3_16.jpg)
  > Fig 3.2
  > Instantaneous rate of hydrolysis of butyl chloride $\left(\mathrm{C}_{4} \mathrm{H}_{9} \mathrm{Cl}
  > 
  > ![](images/fig_3_17.jpg)
  > (3.3)
  > 
  > (3.3)
  > ![](images/fig_3_18.jpg)
- **Should be:**
  > It can be seen (Table 3.1) that the average rate falls from $1.90 	imes 10^{-4} \mathrm{~mol} \mathrm{~L}^{-1} \mathrm{~s}^{-1}$ to $0.4 	imes 10^{-4} \mathrm{~mol} \mathrm{~L}^{-1} \mathrm{~s}^{-1}$. However, average rate cannot be used to predict the rate of a reaction at a particular instant as it would be constant for the time interval for which it is calculated. So, to express the rate at a particular moment of time we determine the instantaneous rate. It is obtained when we consider the average rate at the smallest time interval say d$t$ (i.e. when $\Delta t$ approaches zero). Hence, mathematically for an infinitesimally small d$t$ instantaneous rate is given by
  > 
  > $$
  > r_{\mathrm{av}}=
  > $$
  > 
  > As $\Delta t
  > 
  > ![](images/fig_3_18.jpg)
  > Fig 3.2
  > Instantaneous rate of hydrolysis of butyl chloride $\left(\mathrm{C}_{4} \mathrm{H}_{9} \mathrm{Cl}

### ex_3.1 — solution (en)
- **Confidence:** medium
- **Reason:** Mathpix mis-segmented a real sentence and equation (3.3) as raster images (fig_3_16.jpg, fig_3_17.jpg), then the combine step misattributed the Fig 3.2 caption to the wrong image and duplicated the (3.3) marker. Verified by opening the raw image crops directly (fig_3_16.jpg is the 'It can be seen (Table 3.1)...' text line, fig_3_17.jpg is equation (3.3), fig_3_18.jpg is the real Fig 3.2 graph) and reading the source page directly. User-approved (medium confidence - exact LaTeX spacing is best-effort reconstruction, not verbatim OCR).
- **Found:**
  > ![](images/fig_3_16.jpg)
  > Fig 3.2
  > Instantaneous rate of hydrolysis of butyl chloride $\left(\mathrm{C}_{4} \mathrm{H}_{9} \mathrm{Cl}\right)$
  > 
  > ![](images/fig_3_17.jpg)
  > (3.3)
  > 
  > (3.3)
  > ![](images/fig_3_18.jpg)
- **Should be:**
  > It can be seen (Table 3.1) that the average rate falls from $1.90 \times 10^{-4} \mathrm{~mol} \mathrm{~L}^{-1} \mathrm{~s}^{-1}$ to $0.4 \times 10^{-4} \mathrm{~mol} \mathrm{~L}^{-1} \mathrm{~s}^{-1}$. However, average rate cannot be used to predict the rate of a reaction at a particular instant as it would be constant for the time interval for which it is calculated. So, to express the rate at a particular moment of time we determine the instantaneous rate. It is obtained when we consider the average rate at the smallest time interval say d$t$ (i.e. when $\Delta t$ approaches zero). Hence, mathematically for an infinitesimally small d$t$ instantaneous rate is given by
  > 
  > $$
  > r_{\mathrm{av}}=\frac{-\Delta[\mathrm{R}]}{\Delta t}=\frac{\Delta[\mathrm{P}]}{\Delta t} \quad (3.3)
  > $$
  > 
  > As $\Delta t \rightarrow 0$ or $\quad r_{\text {inst }}=\frac{-\mathrm{d}[\mathrm{R}]}{\mathrm{d} t}=\frac{\mathrm{d}[\mathrm{P}]}{\mathrm{d} t}$
  > 
  > ![](images/fig_3_18.jpg)
  > Fig 3.2
  > Instantaneous rate of hydrolysis of butyl chloride $\left(\mathrm{C}_{4} \mathrm{H}_{9} \mathrm{Cl}\right)$


---

## Retroactive fix pass (external review, session 2026-09-25/28)

### q_3.2 — solution (en)
- **Confidence:** high
- **Reason:** User-authorized: the manual's own printed final value drops the ×10⁻⁹ magnitude (3.888×10⁻⁹ computed from its own numbers); user specified the book's intended value is 3.9×10⁻⁹, not the more-precise-looking 3.89×10⁻⁹ some reviews suggest.
- **Found:**
  > =3.89 \mathrm{~mol} \mathrm{~L}^{-1} \mathrm{~s}^{-1}
- **Should be:**
  > =3.9 \times 10^{-9} \mathrm{~mol} \mathrm{~L}^{-1} \mathrm{~s}^{-1}

### q_3.2 — final_answer (en)
- **Confidence:** high
- **Reason:** Same fix cascaded to the item's own answer-line restatement.
- **Found:**
  > rate $=3.89 \mathrm{~mol} \mathrm{~L}^{-1} \mathrm{~s}^{-1}$
- **Should be:**
  > rate $=3.9 \times 10^{-9} \mathrm{~mol} \mathrm{~L}^{-1} \mathrm{~s}^{-1}$

### q_3.4 — solution (en)
- **Confidence:** high
- **Reason:** OCR digit misread (1 for 3) in dimethyl ether's own formula subscript; every other occurrence in this same item (question and the line immediately above) correctly reads OCH3.
- **Found:**
  > p_{\mathrm{CH}_{3} \mathrm{OCH}_{1}}
- **Should be:**
  > p_{\mathrm{CH}_{3} \mathrm{OCH}_{3}}

### q_3.8 — solution (en)
- **Confidence:** high
- **Reason:** This is an AVERAGE rate over a finite 30s interval, not an instantaneous rate — every other average-rate calculation in this chapter (Example 3.1/3.2, Ex 3.1/3.2) uses -Δ[X]/Δt notation with the minus sign; the manual's own d[]/dt (differential/instantaneous) notation here is inconsistent with its own house style and the actual arithmetic performed (a finite difference, not a derivative).
- **Found:**
  > =\frac{d[\text { Ester }]}{d t}
- **Should be:**
  > =-\frac{\Delta[\text { Ester }]}{\Delta t}

### it_3.5 — solution (en)
- **Confidence:** high
- **Reason:** Missing multiplication sign glues 1.15 and 10^-3 into one token; the identical value is correctly written '1.15 \times 10^{-3}' in this same item's own question and Substitute step.
- **Found:**
  > Rate constant $=1.1510^{-3} \mathrm{~s}^{-1}$
- **Should be:**
  > Rate constant $=1.15 \times 10^{-3} \mathrm{~s}^{-1}$

### q_3.20 — solution (en)
- **Confidence:** high
- **Reason:** OCR glyph confusion (subscript 'l' for 't'); this is total pressure at time t, written correctly as P_t two lines later in the same derivation (2P0-Pt).
- **Found:**
  > \mathrm{P}_{l}=\left(\mathrm{P}_{0}-p\right)+p+p
- **Should be:**
  > \mathrm{P}_{t}=\left(\mathrm{P}_{0}-p\right)+p+p

### q_3.20 — solution (en)
- **Confidence:** high
- **Reason:** OCR glyph confusion (subscript '1' for 't'); same variable (total pressure at time t) is written P_t elsewhere in this same derivation.
- **Found:**
  > & \Rightarrow \mathrm{P}_{1}=\mathrm{P}_{0}+p \\
  > & \Rightarrow p=\mathrm{P}_{1}-\mathrm{P}_{0}
- **Should be:**
  > & \Rightarrow \mathrm{P}_{t}=\mathrm{P}_{0}+p \\
  > & \Rightarrow p=\mathrm{P}_{t}-\mathrm{P}_{0}

### q_3.21 — solution (en)
- **Confidence:** high
- **Reason:** Same P_l -> P_t OCR fix as q_3.20 (identical derivation reused for a different compound).
- **Found:**
  > \mathrm{P}_{l}=\left(\mathrm{P}_{0}-p\right)+p+p
- **Should be:**
  > \mathrm{P}_{t}=\left(\mathrm{P}_{0}-p\right)+p+p

### q_3.21 — solution (en)
- **Confidence:** high
- **Reason:** OCR glyph confusion (subscript '1' for 't'); P_t is used correctly immediately above and below this exact line in the same item.
- **Found:**
  > \mathrm{P}_{0}-p=\mathrm{P}_{0}-\left(\mathrm{P}_{1}-\mathrm{P}_{0}\right)
- **Should be:**
  > \mathrm{P}_{0}-p=\mathrm{P}_{0}-\left(\mathrm{P}_{t}-\mathrm{P}_{0}\right)

### q_3.21 — solution (en)
- **Confidence:** high
- **Reason:** SOCl2 (thionyl chloride) is a different real compound from SO2Cl2 (sulfuryl chloride), the substance this question is actually about, per its own question text and the same item's own Given block a few lines above.
- **Found:**
  > pressure of $\mathrm{SOCl}_{2}$ is
- **Should be:**
  > pressure of $\mathrm{SO}_{2}\mathrm{Cl}_{2}$ is

### q_3.21 — solution (en)
- **Confidence:** high
- **Reason:** Same SOCl2 -> SO2Cl2 fix.
- **Found:**
  > p_{\mathrm{SOCl}_{2}}=\mathrm{P}_{0}-\mathrm{p}
- **Should be:**
  > p_{\mathrm{SO}_{2}\mathrm{Cl}_{2}}=\mathrm{P}_{0}-\mathrm{p}

### q_3.21 — solution (en)
- **Confidence:** high
- **Reason:** Same SOCl2 -> SO2Cl2 fix (also fixes inconsistent capitalization 'SoCl2').
- **Found:**
  > p_{\mathrm{SoCl}_{2}}
- **Should be:**
  > p_{\mathrm{SO}_{2}\mathrm{Cl}_{2}}

### q_3.21 — solution (en)
- **Confidence:** high
- **Reason:** 'rate of equation' is not a real term; every other place in this chapter that names this quantity calls it 'rate of reaction'.
- **Found:**
  > Therefore, the rate of equation, when total pressure is 0.65 atm, is given by,
- **Should be:**
  > Therefore, the rate of reaction, when total pressure is 0.65 atm, is given by,

### q_3.24 — solution (en)
- **Confidence:** high
- **Reason:** Capital T is reserved for temperature elsewhere in this chapter; this is a time value, always lowercase t (matches the item's own use of 't' in every subsequent line).
- **Found:**
  > $k=2.0 \times 10^{-2} \mathrm{~s}^{-1} T=100 \mathrm{~s}$
- **Should be:**
  > $k=2.0 \times 10^{-2} \mathrm{~s}^{-1}, t=100 \mathrm{~s}$

### q_3.24 — solution (en)
- **Confidence:** high
- **Reason:** Missing space glues 'mol' and 'L' into 'moL'; the same unit is written correctly as 'mol L^-1' throughout the rest of this item.
- **Found:**
  > [\mathrm{A}]_{\mathrm{o}}=1.0 \mathrm{moL}^{-1}
- **Should be:**
  > [\mathrm{A}]_{\mathrm{o}}=1.0 \mathrm{~mol} \mathrm{~L}^{-1}

### q_3.26 — solution (en)
- **Confidence:** high
- **Reason:** Glyph confusion (Greek alpha for subscript 'a'); this item's own very next lines correctly use E_a throughout ('E_a/RT=28000K/T', 'E_a=R×28000K').
- **Found:**
  > k=\mathrm{Ae}^{-E_{\alpha} / \mathrm{RT}}(\mathrm{ii})
- **Should be:**
  > k=\mathrm{Ae}^{-E_{a} / \mathrm{RT}}(\mathrm{ii})

### q_3.15 — solution (en)
- **Confidence:** high
- **Reason:** 'V/s' is a garbled OCR rendering of the informal abbreviation 'vs' (versus), mis-attached as a bogus subscript on the bracket; there is no such quantity as 'V/s' in this derivation.
- **Found:**
  > (iv) The given reaction is of the first order as the plot, $\log \left[\mathrm{N}_{2} \mathrm{O}_{5}\right]_{\mathrm{V} / \mathrm{s}} t$, is a straight line.
- **Should be:**
  > (iv) The given reaction is of the first order as the plot of $\log \left[\mathrm{N}_{2} \mathrm{O}_{5}\right]$ vs $t$ is a straight line.

### q_3.15 — solution (en)
- **Confidence:** high
- **Reason:** Same 'V/s' -> 'vs' fix, second occurrence in the same item.
- **Found:**
  > Again, slope of the line of the plot $\log \left[\mathrm{N}_{2} \mathrm{O}_{5}\right]_{\mathrm{V} / \mathrm{s}} t$ is given by
- **Should be:**
  > Again, slope of the line of the plot of $\log \left[\mathrm{N}_{2} \mathrm{O}_{5}\right]$ vs $t$ is given by
