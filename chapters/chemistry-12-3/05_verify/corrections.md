### ex_3.2 — solution (hi)
- **Confidence:** high
- **Reason:** OCR attached a spurious ^{-1} exponent to "min" in the denominator; the PDF (p.68) shows plain "184 min" there (the -1 is already accounted for by the leading -1/2 and the later mol L^-1).
- **Found:**
  > 184 \mathrm{~min}^{-1}
- **Should be:**
  > 184 \mathrm{~min}

### ex_3.2 — solution (hi)
- **Confidence:** medium
- **Reason:** The PDF (p.68) has these as two separate derivation lines: "= 6.79 × 10⁻⁴ mol L⁻¹/min" and, on the next line, "= (6.79 × 10⁻⁴ mol L⁻¹ min⁻¹) × (60 min/1h)". Extraction merged them, giving the first line a spurious "min^{-1}" exponent (PDF shows plain "/min" there) and appending the "×(60 min/1h)" factor that actually belongs to the next line.
- **Found:**
  > / \mathrm{min}^{-1} \times(60 \mathrm{~min} / 1 \mathrm{~h})
- **Should be:**
  > / \mathrm{min}

### ex_3.2 — solution (hi)
- **Confidence:** medium
- **Reason:** Continuation of the same reflow error above: the "×(60 min/1h)" factor that belongs on this line was instead misplaced onto the previous line, leaving this line with the garbled fragment "(60 a)" instead of "(60 min/1h)" as shown in the PDF (p.68).
- **Found:**
  > \times(60 \mathrm{a})
- **Should be:**
  > \times(60 \mathrm{~min} / 1 \mathrm{~h})

### ex_3.5 — solution (hi)
- **Confidence:** high
- **Reason:** OCR wrapped the final "k" in a `\mathcal{}` macro, rendering it as a calligraphic/script glyph instead of the plain italic $k$ used everywhere else in this same solution and in the PDF (page 77, उदाहरण 3.5's final line reads plainly "k = 0.0304 min⁻¹").
- **Found:**
  > \mathcal{k}=0.0304 \mathrm{~min}^{-1}
- **Should be:**
  > k=0.0304 \mathrm{~min}^{-1}

### it_3.2 — solution (hi)
- **Confidence:** high
- **Reason:** Solutions manual (प्रश्न 2, page 89) shows the time in the denominator as plain "10 min" with no exponent; the extracted text attached a spurious ^{-1} to the minute unit, turning a time-in-the-denominator into "per minute" a second time (on top of the division already shown), which is not what the source shows or what the arithmetic requires.
- **Found:**
  > 10 \mathrm{~min}^{-1}
- **Should be:**
  > 10 \mathrm{~min}

### it_3.8 — solution (hi)
- **Confidence:** high
- **Reason:** OCR garbled "J mol⁻¹" into "dmol⁻¹" inside the final substitution step; sol_04.png clearly shows "(J mol⁻¹)".
- **Found:**
  > \left(\mathrm{dmol}^{-1}\right)
- **Should be:**
  > \left(\mathrm{~J} \mathrm{~mol}^{-1}\right)

### q_3.1 — solution (hi)
- **Confidence:** high
- **Reason:** sol_05.png part (iv) shows k की इकाई = वेग/[C2H5Cl] = mol L⁻¹s⁻¹/mol L⁻¹ = s⁻¹ as three separate terms. The extracted text instead merges the denominator with the RHS units into one garbled fraction and states the final unit as "mol L⁻¹" instead of "s⁻¹".
- **Found:**
  > k \text { की इकाई }=\frac{\text { वेग }}{\left[\mathrm{C}_{2} \mathrm{H}_{5} \mathrm{Cl}\right]-\mathrm{mol} \mathrm{~L}^{-1} \mathrm{~s}^{-1}}=\mathrm{mol} \mathrm{~L}^{-1}
- **Should be:**
  > k \text { की इकाई }=\frac{\text { वेग }}{\left[\mathrm{C}_{2} \mathrm{H}_{5} \mathrm{Cl}\right]}=\frac{\mathrm{mol} \mathrm{~L}^{-1} \mathrm{~s}^{-1}}{\mathrm{mol} \mathrm{~L}^{-1}}=\mathrm{s}^{-1}

### q_3.1 — final_answer (hi)
- **Confidence:** high
- **Reason:** Follows from the same part (iv) unit error above — sol_05.png's final unit for part (iv) is s⁻¹, not mol L⁻¹. The current field even self-flags this with "(as printed)", but the PDF's actual printed result is s⁻¹, so this should be corrected rather than left as the wrong value.
- **Found:**
  > (iv) कोटि $=1$, $k$ की इकाई (as printed) $=\mathrm{mol} \mathrm{~L}^{-1}$
- **Should be:**
  > (iv) कोटि $=1$, $k$ की इकाई $=\mathrm{s}^{-1}$

### q_3.3 — solution (hi)
- **Confidence:** high
- **Reason:** sol_06.png shows the rate expression as three separate equal terms, $-\dfrac{d[\mathrm{NH_3}]}{dt} = \dfrac{2\,d[\mathrm{N_2}]}{dt} = \dfrac{2}{3}\dfrac{d[\mathrm{H_2}]}{dt}$. The extracted text instead merges the N2 and H2 terms into a single fraction with a subtraction, which is not what the source shows and does not match the correct stoichiometric rate relation for 2NH3 → N2 + 3H2 (confirmed by the solution's own later steps, which use rate(N2)=k/2 and rate(H2)=3k/2).
- **Found:**
  > \text { अभिक्रिया वेग }=\frac{-d\left[\mathrm{NH}_{3}\right]}{d t}=+\frac{2 d\left[\mathrm{~N}_{2}\right]-2 d\left[\mathrm{H}_{2}\right]}{d t}
- **Should be:**
  > \text { अभिक्रिया वेग }=\frac{-d\left[\mathrm{NH}_{3}\right]}{d t}=+\frac{2 d\left[\mathrm{~N}_{2}\right]}{d t}=\frac{2}{3} \frac{d\left[\mathrm{H}_{2}\right]}{d t}

### q_3.3 — solution (hi)
- **Confidence:** medium
- **Reason:** Same equation restated a second time (sol_06.png, just below "शून्य कोटि अभिक्रिया के लिए, वेग = k"); the extracted text drops the "/dt" denominator on the N2 term and lacks the equals sign, making it read as a single unbalanced expression. Legibility of the exact "=" placement in this particular scanned line is imperfect, so medium rather than high confidence, but the missing dt is clear from the correctly-rendered version of the same term elsewhere in this same solution.
- **Found:**
  > \frac{-d\left[\mathrm{NH}_{3}\right]}{d t} & \quad 2 d\left[\mathrm{~N}_{2}\right]=\frac{2}{3} \frac{d\left[\mathrm{H}_{2}\right]}{d t}
- **Should be:**
  > \frac{-d\left[\mathrm{NH}_{3}\right]}{d t}=\frac{2 d\left[\mathrm{~N}_{2}\right]}{d t}=\frac{2}{3} \frac{d\left[\mathrm{H}_{2}\right]}{d t}

### q_3.5 — solution (hi)
- **Confidence:** high
- **Reason:** sol_07.png clearly reads "निम्नलिखित कारक प्रभावित करते हैं" (the factors that affect...); the extracted text has "प्रमावित", a non-word from a भ/म OCR confusion.
- **Found:**
  > निम्नलिखित कारक प्रमावित करते हैं
- **Should be:**
  > निम्नलिखित कारक प्रभावित करते हैं

### q_3.15 — solution (hi)
- **Confidence:** high
- **Reason:** OCR misspelled "प्रारम्भिक" (initial) as "प्रारम्मिक" — the correct spelling appears two lines later in the same solution ("प्रारम्भिक सान्द्रता का आधा")
- **Found:**
  > $\mathrm{N}_{2} \mathrm{O}_{5}$ की प्रारम्मिक सान्द्रता $=1.63 \times 10^{-2} \mathrm{M}$
- **Should be:**
  > $\mathrm{N}_{2} \mathrm{O}_{5}$ की प्रारम्भिक सान्द्रता $=1.63 \times 10^{-2} \mathrm{M}$

### q_3.17 — solution (hi)
- **Confidence:** high
- **Reason:** OCR misread the Roman numeral "I" (as in "चरण I", step I) as the Devanagari full-stop danda "।"; the source page (solutions manual) clearly reads "चरण I", and the second step in the same solution is correctly rendered "चरण II"
- **Found:**
  > चरण । यदि
- **Should be:**
  > चरण I यदि

### q_3.18 — solution (hi)
- **Confidence:** high
- **Reason:** Same Roman-numeral-I-to-danda OCR confusion as q_3.17; the source reads "चरण I", and the second step in this same solution is correctly rendered "चरण II"
- **Found:**
  > हल चरण। यदि
- **Should be:**
  > हल चरण I यदि

### q_3.20 — solution (hi)
- **Confidence:** high
- **Reason:** OCR letter substitution — "दाब" (pressure) misread as "दाव" (not a word in this context); the source table header reads "प्रारम्भिक दाब"
- **Found:**
  > प्रारम्भिक दाव
- **Should be:**
  > प्रारम्भिक दाब

### q_3.20 — solution (hi)
- **Confidence:** high
- **Reason:** OCR letter substitution — "पश्चात्" (after) misread as "पश्वात्" (not a word); every other occurrence of this word in the same solution is spelled correctly
- **Found:**
  > पश्वात्
- **Should be:**
  > पश्चात्

### q_3.21 — solution (hi)
- **Confidence:** high
- **Reason:** OCR/render glyph confusion — the Latin variable "p" (pressure) was rendered as the Greek letter "\rho" in this line only; the source and the rest of this same solution use plain "p" (e.g. "$a-x=p_i-(p_t-p_i)$" two lines below)
- **Found:**
  > \rho_{t}=\rho_{i}-\rho+\rho+\rho=\rho_{i}+\rho
- **Should be:**
  > p_{t}=p_{i}-p+p+p=p_{i}+p

### q_3.21 — solution (hi)
- **Confidence:** high
- **Reason:** Same "p" rendered as "\rho" glyph confusion, immediately below the previous instance
- **Found:**
  > a=\rho_{i}
- **Should be:**
  > a=p_{i}

### q_3.21 — solution (hi)
- **Confidence:** high
- **Reason:** Same "p" rendered as "\rho" glyph confusion; the source reads "$p_i = 0.5$ atm; $p_t = 0.6$ atm"
- **Found:**
  > प्रश्नानुसार, $\rho_{i}=0.5 \mathrm{~atm} ; \rho_{t}=0.6 \mathrm{~atm}$,
- **Should be:**
  > प्रश्नानुसार, $p_{i}=0.5 \mathrm{~atm} ; p_{t}=0.6 \mathrm{~atm}$,

### q_3.21 — solution (hi)
- **Confidence:** high
- **Reason:** Stray period inserted before the exponent — OCR artifact; the source reads "$k = 2.23 \times 10^{-3}$ s$^{-1}$" and every other occurrence of this value in the same solution is written without the stray period
- **Found:**
  > k & =2.23 \times .10^{-3} \mathrm{~s}^{-1}
- **Should be:**
  > k & =2.23 \times 10^{-3} \mathrm{~s}^{-1}

### q_3.24 — solution (hi)
- **Confidence:** high
- **Reason:** Formula garbled during extraction — the ratio [A]₀/[A] lost its denominator "[A]" (replaced with a stray "\_") and the division by 2.303 was folded incorrectly into the numerator fraction, obscuring the equation's meaning. PDF page sol_23 shows a clean two-fraction equation.
- **Found:**
  > \log \frac{[A]_{0} \_\left(2.0 \times 10^{-2} \mathrm{~s}^{-1}\right) \times(100 \mathrm{~s})}{2.303}=0.8684
- **Should be:**
  > \log \frac{[A]_{0}}{[A]}=\frac{\left(2.0 \times 10^{-2} \mathrm{~s}^{-1}\right) \times(100 \mathrm{~s})}{2.303}=0.8684

### q_3.26 — solution (hi)
- **Confidence:** high
- **Reason:** The comparison step "$-E_a/(RT) = -28000K/T$" was garbled into three disconnected lines ("E_a = -28000 K", "RT", "E_a = (28000 K) × R"), losing the fraction structure. PDF page sol_24 shows this as one clean equation before the next line (which is already correct and unchanged here).
- **Found:**
  > E_{a} & =-28000 \mathrm{~K} \\
  > R T & \\
  > E_{a} & =(28000 \mathrm{~K}) \times R \\
- **Should be:**
  > -\frac{E_{a}}{R T} & =\frac{-28000 \mathrm{~K}}{T} \\
  > E_{a} & =(28000 \mathrm{~K}) \times R \\

### q_3.28 — solution (hi)
- **Confidence:** high
- **Reason:** The Arrhenius two-temperature equation was garbled: "2.303" became a stray superscript base "a^{-1.303...}", the "J mol⁻¹" unit on 8.314 was dropped, and the numerator "(T₂-283)" lost its subtraction, collapsing to "283 T₂". PDF page sol_26 (top line) shows the intact equation.
- **Found:**
  > \log \frac{1.5 \times 10^{4}}{4.5 \times 10^{3}} & =\left(6000 \mathrm{~J} \mathrm{~mol}^{-1}\right) \mathrm{a}^{-1.303 \times\left(8.314 \mathrm{~mol}^{-1}\right)}\left(283 T_{2}\right) \\
- **Should be:**
  > \log \frac{1.5 \times 10^{4}}{4.5 \times 10^{3}} & =\frac{6000 \mathrm{~J} \mathrm{~mol}^{-1}}{2.303 \times\left(8.314 \mathrm{~J} \mathrm{~mol}^{-1}\right)} \times\left(\frac{T_{2}-283}{283 T_{2}}\right) \\

### q_3.29 — solution (hi)
- **Confidence:** high
- **Reason:** The 298 K rate-constant line dropped its "/t" denominator — "k₁ = 2.303/t log(100/90)" was extracted as "k₁ = {}^{2.303} log(100/90)", turning the fraction into a stray superscript. The very next line (k₂, 308 K) has the same formula and correctly kept "/t", confirming this is an extraction slip, not a book error. PDF page sol_26 (bottom) shows both k₁ and k₂ with the same "2.303/t" form.
- **Found:**
  > k_{1}={ }^{2.303} \log \frac{100}{90}
- **Should be:**
  > k_{1}=\frac{2.303}{t} \log \frac{100}{90}

### q_3.26 — solution (hi)
- **Confidence:** high
- **Reason:** User-approved fix (per step_5's unit-slip exception rule): the derivation directly above correctly computes 232792 J mol⁻¹, but this concluding line inverts the unit to kJ⁻¹ mol⁻¹, a same-page self-contradiction confirmed printed that way in the PDF itself.
- **Found:**
  > E_{a} & =232.792 \mathrm{~kJ}^{-1} \mathrm{~mol}^{-1}
- **Should be:**
  > E_{a} & =232.792 \mathrm{~kJ} \mathrm{~mol}^{-1}

### q_3.26 — final_answer (hi)
- **Confidence:** high
- **Reason:** Same user-approved unit fix, mirrored in the boxed answer field.
- **Found:**
  > $E_a=232.792 \mathrm{~kJ}^{-1} \mathrm{~mol}^{-1}$ (unit as printed in source, likely OCR error for $\mathrm{kJ}\ \mathrm{mol}^{-1}$)
- **Should be:**
  > $E_a=232.792 \mathrm{~kJ} \mathrm{~mol}^{-1}$
