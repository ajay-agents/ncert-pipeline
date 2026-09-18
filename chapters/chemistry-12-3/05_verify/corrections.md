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

### q_3.20 — solution (hi)
- **Confidence:** high
- **Reason:** The question's own table gives pressure in mm Hg (confirmed via mathpix and the item's own :::prompt), but the k1/k2 derivation labelled the same 35/54/63/70 values as 'atm'. Traced to a genuine error in solutions.hi.pdf page 107 (confirmed by direct 200dpi render - the source itself prints 'atm'). Does not change the numeric k value (a ratio of same-unit pressures), but the unit label is factually wrong and could mislead a student checking units. Corrected to mm Hg throughout.
- **Found:**
  > हल $\left(\mathrm{CH}_{3}\right)_{2} \mathrm{CHN}=\mathrm{NCH}\left(\mathrm{CH}_{3}\right)_{2}(g) \longrightarrow \mathrm{N}_{2}(g)+\mathrm{C}_{6} \mathrm{H}_{14}(g)$
  > 
  > | प्रारम्भिक दाब | $p_{i}$ | $0$ | $0$ |
  > | :--- | :--- | :--- | :--- |
  > | $t$ समय पश्चात् | $p_{i}-p$ | $p$ | $p$ |
  > 
  > $t$ समय पश्चात् कुल दाब अर्थात् $\left(p_{i}\right)=\left(p_{i}-p\right)+p+p=p_{i}+p$
  > अथवा
  > 
  > $$
  > p=p_{t}-p_{i}
  > $$
  > 
  > $a=p_{i} ;(a-x)=p_{i}-p$;समी (i) से $p$ का मान रखने पर
  > 
  > $$
  > (a-x)=p_{i}-\left(p_{t}-p_{i}\right), \text { i.e., }(a-x)=2 p_{i}-p_{t}
  > $$
  > 
  > अपघटन अभिक्रिया गैसीय प्रकृति की है अतः वेग स्थिरांक $k$ की निम्न प्रकार गणना कर सकते हैं
  > 
  > $$
  > k=\frac{2.303}{t} \log \frac{a}{a-x}
  > $$
  > 
  > $a$ तथा $(a-x)$ का मान रखने पर
  > 
  > $$
  > k=\frac{2.303}{t} \log \left(\frac{p_{i}}{2 p_{i}-p_{t}}\right)
  > $$
  > 
  > (i) माना $360 \mathrm{~s}$ के पश्चात् वेग स्थिरांक $=k_{1}$
  > $$
  > \begin{aligned}
  > k_{1} & =-\frac{2.303}{(360 \mathrm{~s})} \log \frac{(35 \mathrm{~atm})}{(70-54) \mathrm{atm}} \\
  > & =\frac{2.303}{(360 \mathrm{~s})} \log \frac{35}{16} \\
  > & =\frac{2.303}{(360 \mathrm{~s})} \log 2.1875 \\
  > & =\frac{2.303 \times 0.33995}{(360 \mathrm{~s})} \\
  > & =2.17 \times 10^{-3} \mathrm{~s}^{-1}
  > \end{aligned}
  > $$
  > (ii) माना $720 \mathrm{~s}$ के पश्चात् वेग स्थिरांक $=k_{2}$
  > $$
  > \begin{aligned}
  > k_{2} & =-\frac{2.303}{(720 \mathrm{~s})} \log \frac{(35 \mathrm{~atm})}{(70-63) \mathrm{atm}} \\
  > & =-\frac{2.303}{(720 \mathrm{~s})} \log 5=\frac{2.303 \times 0.6990}{(720 \mathrm{~s})} \\
  > & =2.24 \times 10^{-3} \mathrm{~s}^{-1}
  > \end{aligned}
  > $$
  > अत: औसत वेग स्थिरांक, $k=\frac{(2.17+2.24) \times 10^{-3} \mathrm{~s}^{-1}}{2}$.
  > $$
  > k=2.21 \times 10^{-3} \mathrm{~s}^{-1}
  > $$
- **Should be:**
  > हल $\left(\mathrm{CH}_{3}\right)_{2} \mathrm{CHN}=\mathrm{NCH}\left(\mathrm{CH}_{3}\right)_{2}(g) \longrightarrow \mathrm{N}_{2}(g)+\mathrm{C}_{6} \mathrm{H}_{14}(g)$
  > 
  > | प्रारम्भिक दाब | $p_{i}$ | $0$ | $0$ |
  > | :--- | :--- | :--- | :--- |
  > | $t$ समय पश्चात् | $p_{i}-p$ | $p$ | $p$ |
  > 
  > $t$ समय पश्चात् कुल दाब अर्थात् $\left(p_{i}\right)=\left(p_{i}-p\right)+p+p=p_{i}+p$
  > अथवा
  > 
  > $$
  > p=p_{t}-p_{i}
  > $$
  > 
  > $a=p_{i} ;(a-x)=p_{i}-p$;समी (i) से $p$ का मान रखने पर
  > 
  > $$
  > (a-x)=p_{i}-\left(p_{t}-p_{i}\right), \text { i.e., }(a-x)=2 p_{i}-p_{t}
  > $$
  > 
  > अपघटन अभिक्रिया गैसीय प्रकृति की है अतः वेग स्थिरांक $k$ की निम्न प्रकार गणना कर सकते हैं
  > 
  > $$
  > k=\frac{2.303}{t} \log \frac{a}{a-x}
  > $$
  > 
  > $a$ तथा $(a-x)$ का मान रखने पर
  > 
  > $$
  > k=\frac{2.303}{t} \log \left(\frac{p_{i}}{2 p_{i}-p_{t}}\right)
  > $$
  > 
  > (i) माना $360 \mathrm{~s}$ के पश्चात् वेग स्थिरांक $=k_{1}$
  > $$
  > \begin{aligned}
  > k_{1} & =-\frac{2.303}{(360 \mathrm{~s})} \log \frac{(35 \mathrm{~mm} \mathrm{Hg})}{(70-54) \mathrm{mm} \mathrm{Hg}} \\
  > & =\frac{2.303}{(360 \mathrm{~s})} \log \frac{35}{16} \\
  > & =\frac{2.303}{(360 \mathrm{~s})} \log 2.1875 \\
  > & =\frac{2.303 \times 0.33995}{(360 \mathrm{~s})} \\
  > & =2.17 \times 10^{-3} \mathrm{~s}^{-1}
  > \end{aligned}
  > $$
  > (ii) माना $720 \mathrm{~s}$ के पश्चात् वेग स्थिरांक $=k_{2}$
  > $$
  > \begin{aligned}
  > k_{2} & =-\frac{2.303}{(720 \mathrm{~s})} \log \frac{(35 \mathrm{~mm} \mathrm{Hg})}{(70-63) \mathrm{mm} \mathrm{Hg}} \\
  > & =-\frac{2.303}{(720 \mathrm{~s})} \log 5=\frac{2.303 \times 0.6990}{(720 \mathrm{~s})} \\
  > & =2.24 \times 10^{-3} \mathrm{~s}^{-1}
  > \end{aligned}
  > $$
  > अत: औसत वेग स्थिरांक, $k=\frac{(2.17+2.24) \times 10^{-3} \mathrm{~s}^{-1}}{2}$.
  > $$
  > k=2.21 \times 10^{-3} \mathrm{~s}^{-1}
  > $$

### q_3.22 — solution (hi)
- **Confidence:** high
- **Reason:** The second, duplicate 'A = 1.585 x 10^6 ...' line dropped the 's' unit ('collisions^-1' instead of 'collisions s^-1') - an extraction-stage artifact, since solutions.hi.pdf page 110 (confirmed by direct 200dpi render) shows 'collisions s^-1' on BOTH the first and duplicate lines. Corrected to match.
- **Found:**
  > हल (a) $\log k$ एवं $1 / T$ के मध्य ग्राफ खींचने के लिए हम आँकड़ों को निम्नलिखित रूप में दोबारा लिखते हैं
  > 
  > | T(K) | $273$ | $293$ | $313$ | $333$ | $353$ |
  > | :--- | :--- | :--- | :--- | :--- | :--- |
  > | $1 / T$ | $0.003663$ | $0.003413$ | $0.003213$ | $0.003003$ | $0.002833$ |
  > | logk | - $6.1040$ | - $4.7696$ | - $3.5900$ | -2.7496 | - $1.6996$ |
  > 
  > 
  >     (b) ग्राफ की सहायता से ढाल को ज्ञात करते हैं।
  > $$
  > \text { ढाल }=\frac{-2.4}{0.00047}=\frac{-E_{\mathrm{a}}}{2.303 R}
  > $$
  >     ∴
  > $$
  > \text { सक्रियण ऊर्जा } \begin{aligned}
  > \left(E_{a}\right) & =\frac{2.4 \times 2.303 \times 8.314 \mathrm{~J} \mathrm{~mol}^{-1}}{0.00047} \\
  > & =97875 \mathrm{~J} \mathrm{~mol}^{-1} \\
  > & =97.875 \mathrm{~kJ} \mathrm{~mol}^{-1}
  > \end{aligned}
  > $$
  >     (c) हम जानते हैं कि
  > $$
  > \log k=\log A-\frac{E_{a}}{2.303 R T}
  > $$
  > 
  > इसकी $y=m x+c$ से तुलना करने पर, चूँकि यह अंतःखण्ड रूप में रेखा की समीकरण है।
  > 
  > $$
  > \log k=\left(-\frac{E_{a}}{2.303 R T}\right) \frac{1}{T}+\log A
  > $$
  > 
  > $\log A=$ रुअक्ष अर्थात् $\log k$ अक्ष पर अंतःखण्ड का मान
  > 
  > $$
  > \begin{aligned}
  > &=(-1+7.2) \\
  > &=6.2\left[y_{2}-y_{1}=-1-(7.2)\right] \\
  > & \text { आवृत्ति गुणक, } A=\text { Antilog } 6.2=1585000 \\
  > &=1.585 \times 10^{6} \mathrm{collisions} \mathrm{~s}^{-1} \\
  > & A=1.585 \times 10^{6} \text { collisions }^{-1}
  > \end{aligned}
  > $$
  > 
  > (d) ग्राफ के अध्ययन द्वारा वेग नियतांक $k$ का मान ज्ञात करते हैं।
  > 
  > | T(K) | 1/T | ग्राफ से $\log k$ का मान | $k$ का मान |
  > | :--- | :--- | :--- | :--- |
  > | $303$ | $0.003300$ | - $4.2$ | $6.31 \times 10^{-5} \mathrm{~s}^{-1}$ |
  > | $323$ | $0.003096$ | -2.8 | $1.585 \times 10^{-3} \mathrm{~s}^{-1}$ |
- **Should be:**
  > हल (a) $\log k$ एवं $1 / T$ के मध्य ग्राफ खींचने के लिए हम आँकड़ों को निम्नलिखित रूप में दोबारा लिखते हैं
  > 
  > | T(K) | $273$ | $293$ | $313$ | $333$ | $353$ |
  > | :--- | :--- | :--- | :--- | :--- | :--- |
  > | $1 / T$ | $0.003663$ | $0.003413$ | $0.003213$ | $0.003003$ | $0.002833$ |
  > | logk | - $6.1040$ | - $4.7696$ | - $3.5900$ | -2.7496 | - $1.6996$ |
  > 
  > 
  >     (b) ग्राफ की सहायता से ढाल को ज्ञात करते हैं।
  > $$
  > \text { ढाल }=\frac{-2.4}{0.00047}=\frac{-E_{\mathrm{a}}}{2.303 R}
  > $$
  >     ∴
  > $$
  > \text { सक्रियण ऊर्जा } \begin{aligned}
  > \left(E_{a}\right) & =\frac{2.4 \times 2.303 \times 8.314 \mathrm{~J} \mathrm{~mol}^{-1}}{0.00047} \\
  > & =97875 \mathrm{~J} \mathrm{~mol}^{-1} \\
  > & =97.875 \mathrm{~kJ} \mathrm{~mol}^{-1}
  > \end{aligned}
  > $$
  >     (c) हम जानते हैं कि
  > $$
  > \log k=\log A-\frac{E_{a}}{2.303 R T}
  > $$
  > 
  > इसकी $y=m x+c$ से तुलना करने पर, चूँकि यह अंतःखण्ड रूप में रेखा की समीकरण है।
  > 
  > $$
  > \log k=\left(-\frac{E_{a}}{2.303 R T}\right) \frac{1}{T}+\log A
  > $$
  > 
  > $\log A=$ रुअक्ष अर्थात् $\log k$ अक्ष पर अंतःखण्ड का मान
  > 
  > $$
  > \begin{aligned}
  > &=(-1+7.2) \\
  > &=6.2\left[y_{2}-y_{1}=-1-(7.2)\right] \\
  > & \text { आवृत्ति गुणक, } A=\text { Antilog } 6.2=1585000 \\
  > &=1.585 \times 10^{6} \mathrm{collisions} \mathrm{~s}^{-1} \\
  > & A=1.585 \times 10^{6} \text { collisions } \mathrm{~s}^{-1}
  > \end{aligned}
  > $$
  > 
  > (d) ग्राफ के अध्ययन द्वारा वेग नियतांक $k$ का मान ज्ञात करते हैं।
  > 
  > | T(K) | 1/T | ग्राफ से $\log k$ का मान | $k$ का मान |
  > | :--- | :--- | :--- | :--- |
  > | $303$ | $0.003300$ | - $4.2$ | $6.31 \times 10^{-5} \mathrm{~s}^{-1}$ |
  > | $323$ | $0.003096$ | -2.8 | $1.585 \times 10^{-3} \mathrm{~s}^{-1}$ |

### q_3.22 — final_answer (hi)
- **Confidence:** high
- **Reason:** Contains a stray internal QC/proofreading annotation ('(as printed, "collisions")') that does not exist anywhere in solutions.hi.pdf (confirmed absent from both the mathpix text and a direct page render) and has no place in a clean answer key. Replaced with the clean 'collisions s^-1' unit, matching the source.
- **Found:**
  > $E_a=97.875 \mathrm{~kJ} \mathrm{~mol}^{-1}$; $A=1.585 \times 10^{6}$ (as printed, "collisions"); $30^{\circ}\mathrm{C}$ (303 K) पर $k=6.31 \times 10^{-5} \mathrm{~s}^{-1}$; $50^{\circ}\mathrm{C}$ (323 K) पर $k=1.585 \times 10^{-3} \mathrm{~s}^{-1}$
- **Should be:**
  > $E_a=97.875 \mathrm{~kJ} \mathrm{~mol}^{-1}$; $A=1.585 \times 10^{6} \text { collisions } \mathrm{s}^{-1}$; $30^{\circ}\mathrm{C}$ (303 K) पर $k=6.31 \times 10^{-5} \mathrm{~s}^{-1}$; $50^{\circ}\mathrm{C}$ (323 K) पर $k=1.585 \times 10^{-3} \mathrm{~s}^{-1}$
