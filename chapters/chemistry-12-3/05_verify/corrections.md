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
