### ex_2.1 — solution (hi)
- **Confidence:** high
- **Reason:** Lost exponent — the Nernst-equation denominator in the PDF shows [Ag⁺]² (consistent with the reaction's 2 e⁻ / 2Ag⁺ stoichiometry, and with the same squared-Ag⁺ denominator used in the general Ni/Ag Nernst equation printed just above this example on the same page), but the extracted text has only Ag⁺ with no exponent.
- **Found:**
  > \ln \frac{\mathrm{Mg}^{2+}}{\mathrm{Ag}^{+}}
- **Should be:**
  > \ln \frac{\mathrm{Mg}^{2+}}{\left(\mathrm{Ag}^{+}\right)^{2}}

### ex_2.5 — solution (hi)
- **Confidence:** high
- **Reason:** Lost exponent — the PDF shows the molar conductivity result as S cm² mol⁻¹ (the correct unit for molar conductivity, and consistent with the parallel "m" version of the same calculation a few lines later which correctly has S m² mol⁻¹), but the extracted text drops the exponent, giving the wrong unit S cm mol⁻¹.
- **Found:**
  > =229.6 \mathrm{~S} \mathrm{~cm} \mathrm{~mol}^{-1}
- **Should be:**
  > =229.6 \mathrm{~S} \mathrm{~cm}^{2} \mathrm{~mol}^{-1}

### it_2.1 — solution (hi)
- **Confidence:** high
- **Reason:** OCR garbled "दूसरे" (second) into a nonsense syllable
- **Found:**
  > इसी प्रकार मानक हाइड्रोजन इलेक्ट्रोड स्सरे अर्द्धसेल
- **Should be:**
  > इसी प्रकार मानक हाइड्रोजन इलेक्ट्रोड दूसरे अर्द्धसेल

### it_2.1 — solution (hi)
- **Confidence:** high
- **Reason:** OCR garbled the "सेल" (cell) subscript into "सेस" in the inline reference to E°(cell)
- **Found:**
  > वोल्टमीटर के पाठ्यांक द्वारा $E_{\text {सेस }}^{\circ}$ के मान प्राप्त होते हैं
- **Should be:**
  > वोल्टमीटर के पाठ्यांक द्वारा $E_{\text {सेल }}^{\circ}$ के मान प्राप्त होते हैं

### it_2.1 — solution (hi)
- **Confidence:** high
- **Reason:** OCR garbled the "सेल" (cell) subscript into "सेता" in the displayed equation
- **Found:**
  > E_{\text {सेता }}^{\circ} & =E_{\left(\mathrm{H}^{+} / \frac{1}{2} \mathrm{H}_{2}\right)}^{\circ}-E_{\left(\mathrm{Mg}^{2+} / \mathrm{Mg}\right)}^{\circ} \\
- **Should be:**
  > E_{\text {सेल }}^{\circ} & =E_{\left(\mathrm{H}^{+} / \frac{1}{2} \mathrm{H}_{2}\right)}^{\circ}-E_{\left(\mathrm{Mg}^{2+} / \mathrm{Mg}\right)}^{\circ} \\

### it_2.1 — solution (hi)
- **Confidence:** high
- **Reason:** OCR misread the "+" superscript on Mg²⁺ as a division sign
- **Found:**
  > & =0-E_{\left(\mathrm{Mg}^{2} \div / \mathrm{Mg}\right)}^{\circ}
- **Should be:**
  > & =0-E_{\left(\mathrm{Mg}^{2+} / \mathrm{Mg}\right)}^{\circ}

### it_2.5 — solution (hi)
- **Confidence:** high
- **Reason:** OCR garbled the "सेल" (cell) subscript into "सेत" in E°(cell)
- **Found:**
  > E_{\text {सेल }} & =E_{\text {सेत }}^{\circ}-\frac{0.0591}{n} \log \frac{\left[\mathrm{Ni}^{2+}\right]}{\left[\mathrm{Ag}^{+}\right]^{2}} \\
- **Should be:**
  > E_{\text {सेल }} & =E_{\text {सेल }}^{\circ}-\frac{0.0591}{n} \log \frac{\left[\mathrm{Ni}^{2+}\right]}{\left[\mathrm{Ag}^{+}\right]^{2}} \\

### it_2.6 — solution (hi)
- **Confidence:** high
- **Reason:** OCR misread "RT" (gas constant times temperature) as "RI" in the log Kc formula
- **Found:**
  > \log K_{c} & =-\frac{\Delta G^{\circ}}{2.303 \mathrm{RI}} \\
- **Should be:**
  > \log K_{c} & =-\frac{\Delta G^{\circ}}{2.303 \mathrm{RT}} \\

### it_2.13 — solution (hi)
- **Confidence:** high
- **Reason:** OCR misread ध (dha) as घ (gha); "वैद्युत घारा" is not a word, the solutions manual clearly shows "वैद्युत धारा" (electric current), consistent with the same phrase used throughout this chapter.
- **Found:**
  > वैद्युत घारा बाह्य स्रोत से प्रदान की जाती है
- **Should be:**
  > वैद्युत धारा बाह्य स्रोत से प्रदान की जाती है

### it_2.13 — solution (hi)
- **Confidence:** high
- **Reason:** OCR error dropped the correct plural form; the solutions manual shows "अभिक्रियाएँ" (reactions), not "अभिक्रियाई" which is not a valid word.
- **Found:**
  > समस्त रासायनिक अभिक्रियाई, सेल के प्रयोग के समय की व्युत्क्रम होती है
- **Should be:**
  > समस्त रासायनिक अभिक्रियाएँ, सेल के प्रयोग के समय की व्युत्क्रम होती है

### it_2.15 — solution (hi)
- **Confidence:** high
- **Reason:** OCR misread भ as म; the solutions manual clearly shows "प्रारम्भ" (begin/start), not "प्रारम्म" which is not a valid word.
- **Found:**
  > फेरस आयन बनाना प्रारम्म कर देता है
- **Should be:**
  > फेरस आयन बनाना प्रारम्भ कर देता है

### q_2.2 — solution (hi)
- **Confidence:** high
- **Reason:** OCR misread ध (dha) as घ (gha) in "धातुओं" (metals); the solutions-manual PDF clearly shows "जिन धातुओं का अपचयन विभव निम्न..."
- **Found:**
  > जिन घातुओं
- **Should be:**
  > जिन धातुओं

### q_2.3 — solution (hi)
- **Confidence:** medium
- **Reason:** The standalone word "कैथोड" (cathode) is set in a font in the solutions-manual PDF where the था-ligature renders as a corrupted glyph; the extraction read it as "कैयोड". The same document spells the word correctly and legibly as "कैथोड" in the smaller subscript instances on the same and adjacent pages (e.g. E°_कैथोड in q_2.4 and q_2.6), which is why this is not full "high" confidence — the glyph itself is visually ambiguous even under zoom, but no legible instance anywhere in this document actually reads "य" in this word.
- **Found:**
  > कैयोड
- **Should be:**
  > कैथोड

### q_2.4 — solution (hi)
- **Confidence:** high
- **Reason:** OCR misread ड (da) as ढ (dha) in "ऐनोड" (anode). The PDF clearly shows "E°_सेल = E°_केथोड − E°_ऐनोड" with ड, and the same word is spelled correctly ("ऐनोड") elsewhere in this same extracted solution (part ii).
- **Found:**
  > ऐनोढ
- **Should be:**
  > ऐनोड

### q_2.5 — question (hi)
- **Confidence:** high
- **Reason:** OCR misread the digit "1" as the letter "l" and inserted a space. The chapter PDF clearly shows "H₂(g)(1bar)" with no space, for cell (ii).
- **Found:**
  > l bar
- **Should be:**
  > 1bar

### q_2.6 — solution (hi)
- **Confidence:** medium
- **Reason:** Same font-rendering issue as in q_2.3: the standalone word "कैथोड" (cathode) is corrupted by the PDF's bold font and was read by OCR as "कैयोड". The same document renders the word legibly as "कैथोड" in the E°_कैथोड subscript a few lines above this exact occurrence.
- **Found:**
  > कैयोड
- **Should be:**
  > कैथोड

### q_2.7 — solution (hi)
- **Confidence:** high
- **Reason:** OCR misread थ (tha) as य (ya) in "अनुप्रस्थ" (cross-section/transverse). The PDF clearly shows "A = अनुप्रस्थ काट का क्षेत्रफल", and the same extracted solution spells the word correctly ("अनुप्रस्थ") twice more later in the same field.
- **Found:**
  > अनुप्रस्य काट
- **Should be:**
  > अनुप्रस्थ काट

### q_2.8 — solution (hi)
- **Confidence:** high
- **Reason:** The PDF shows two separate lines — "मोलर सान्द्रता (C) = 0.20 mol L⁻¹" and then, as its own equation, "(0.2 mol)/(1000 cm³) = 2.0×10⁻⁴ mol cm⁻³" — but the extraction fused these into one fraction and put the wrong quantity in the denominator ("0.2 mol⁻¹" instead of the PDF's "1000 cm³"), which also doesn't match its own stated unit of the result (mol cm⁻³).
- **Found:**
  > \left(0.2 \mathrm{~mol}^{-1}\right)
- **Should be:**
  > \left(1000 \mathrm{~cm}^{3}\right)

### q_2.9 — solution (hi)
- **Confidence:** high
- **Reason:** OCR misread the Greek letter κ (kappa, conductivity) as the Latin letter "x" in "प्रश्नानुसार, R=1500Ω; κ=0.146×10⁻³". The PDF clearly shows κ, and the same extracted solution correctly uses \kappa two lines later in "सेल स्थिरांक = R × κ".
- **Found:**
  > \mathrm{x}=0.146
- **Should be:**
  > \kappa=0.146

### q_2.13 — solution (hi)
- **Confidence:** high
- **Reason:** OCR replaced an equals sign with a minus sign in the final Ca calculation; PDF shows "= 1F", not "− 1F".
- **Found:**
  > \frac{2 \times 20}{40}-1 \mathrm{~F}
- **Should be:**
  > \frac{2 \times 20}{40}=1 \mathrm{~F}

### q_2.14 — solution (hi)
- **Confidence:** high
- **Reason:** The "2F" annotation and the electron term got swapped/duplicated: the extracted text attaches "2F" under "2Fe³⁺" and repeats "2e⁻" as its own annotation. The PDF shows no annotation under 2Fe³⁺, and "2F" annotated under 2e⁻ instead.
- **Found:**
  > \underset{2 \mathrm{~F}}{2 \mathrm{Fe}^{3+}}+\underset{2 \mathrm{e}^{-}}{2 \mathrm{e}^{-}}
- **Should be:**
  > 2 \mathrm{Fe}^{3+}+\underset{2 \mathrm{~F}}{2 \mathrm{e}^{-}}

### q_2.12 — solution (hi)
- **Confidence:** medium
- **Reason:** In the MnO₄⁻ → Mn²⁺ electrode reaction, the main/annotation positions are swapped and the electron symbol "e⁻" was misread as "O⁻" (there is no oxide species in this reaction — it is a 5-electron reduction). The PDF shows MnO₄⁻ (annotated "Mn की आ०स०=7") + 5e⁻ (annotated "5mol") → Mn²⁺ (annotated "Mn की आ०स०=2"), but the extracted text has an empty main symbol carrying MnO₄⁻ as its own annotation, "5mol" as the main symbol with "5 O⁻" annotated beneath it, and the Mn²⁺ annotation missing its "Mn की" prefix.
- **Found:**
  > \underset{\substack{\mathrm{MnO}_{4}^{-} \\ \mathrm{Mn} \text { की } \\ \text { आ०स० }=7}}{ }+\underset{\text { 5 } \mathrm{O}^{-}}{5 \mathrm{~mol}} \longrightarrow \underset{\text { आ०स० }=2}{\mathrm{Mn}^{2+}}
- **Should be:**
  > \underset{\substack{\mathrm{Mn} \text { की } \\ \text { आ०स० }=7}}{\mathrm{MnO}_{4}^{-}}+\underset{5 \mathrm{~mol}}{5 e^{-}} \longrightarrow \underset{\mathrm{Mn} \text { की } \text { आ०स० }=2}{\mathrm{Mn}^{2+}}

### q_2.17 — solution (hi)
- **Confidence:** high
- **Reason:** "सम्भव" (possible/feasible) is consistently OCR'd as "सम्मव" in every part's concluding sentence, even though the opening rule sentence of this same solution correctly spells it "सम्भव". Fixing spelling only — the feasibility verdict itself ("है"/"नहीं है") is left exactly as printed.
- **Found:**
  > 0.23 \mathrm{~V}
- **Should be:**
  > 0.23 \mathrm{~V}

### q_2.17 — solution (hi)
- **Confidence:** high
- **Reason:** Same "सम्मव"→"सम्भव" OCR error, part (ii)'s concluding sentence. Note: per the batch instructions, the "नहीं है" verdict itself is a confirmed genuine textbook self-contradiction (E°cell computes to +0.46 V, positive, yet the book concludes not feasible) and is intentionally left untouched — only the spelling of "सम्भव" is corrected here.
- **Found:**
  > 0.46 \mathrm{~V}
- **Should be:**
  > 0.46 \mathrm{~V}

### q_2.17 — solution (hi)
- **Confidence:** high
- **Reason:** Same "सम्मव"→"सम्भव" OCR error, part (iii)'s concluding sentence.
- **Found:**
  > -0.32 \mathrm{~V}
- **Should be:**
  > -0.32 \mathrm{~V}

### q_2.17 — solution (hi)
- **Confidence:** high
- **Reason:** Same "सम्मव"→"सम्भव" OCR error, part (iv)'s concluding sentence.
- **Found:**
  > -0.03 \mathrm{~V}
- **Should be:**
  > -0.03 \mathrm{~V}

### q_2.17 — solution (hi)
- **Confidence:** high
- **Reason:** Same "सम्मव"→"सम्भव" OCR error, part (v)'s concluding sentence. Note: the PDF's part (v) has the identical self-contradiction pattern as part (ii) — E°cell computes to +0.32 V (positive) yet concludes "सम्भव नहीं है" (not feasible) — confirmed genuinely printed that way; left untouched here (only the spelling is corrected), and flagged separately in the stage summary since it was not among the batch's pre-identified known errors.
- **Found:**
  > +0.32 \mathrm{~V}
- **Should be:**
  > +0.32 \mathrm{~V}

### q_2.18 — solution (hi)
- **Confidence:** high
- **Reason:** OCR corrupted "सिल्वर" (silver) to "सित्वर" in part (i)'s solution heading.
- **Found:**
  > सित्वर इलेक्ट्रोडों के साथ
- **Should be:**
  > सिल्वर इलेक्ट्रोडों के साथ

### q_2.18 — solution (hi)
- **Confidence:** high
- **Reason:** OCR corrupted "प्लैटिनम" (platinum) to "दैटिनम" in part (iv)'s solution heading.
- **Found:**
  > दैटिनम इलेक्ट्रोडों के साथ
- **Should be:**
  > प्लैटिनम इलेक्ट्रोडों के साथ

### q_2.18 — solution (hi)
- **Confidence:** high
- **Reason:** OCR corrupted "कैथोड" (cathode) to "कैयोड" in part (i)'s discussion of where silver collects; the PDF clearly reads "कैथोड" here.
- **Found:**
  > सिल्वर कैयोड पर एकत्रित होगा
- **Should be:**
  > सिल्वर कैथोड पर एकत्रित होगा

### q_2.18 — solution (hi)
- **Confidence:** high
- **Reason:** Same "कैथोड"→"कैयोड" OCR error, part (ii)'s statement that Ag deposits at the cathode.
- **Found:**
  > कैयोड पर Ag निक्षेपित होती है
- **Should be:**
  > कैथोड पर Ag निक्षेपित होती है

### q_2.17 — solution (hi)
- **Confidence:** high
- **Reason:** Reconstructed fix for a corrections_F.md entry that degraded to a no-op: its multi-line Found/Should-be block only had a '>' prefix on the first line, so mdio.markdown_to_corrections() silently dropped the rest, making found==should_be. Part (i)'s conclusion.
- **Found:**
  > =0.77-0.54=0.23 \mathrm{~V}
  > \end{aligned}
  > $$
  > अतः अभिक्रिया सम्मव है।
- **Should be:**
  > =0.77-0.54=0.23 \mathrm{~V}
  > \end{aligned}
  > $$
  > अतः अभिक्रिया सम्भव है।

### q_2.17 — solution (hi)
- **Confidence:** high
- **Reason:** Same reconstruction, part (ii)'s conclusion (the genuine self-contradiction verdict itself is left untouched).
- **Found:**
  > =0.80-0.34=0.46 \mathrm{~V}
  > $$
  > अतः अभिक्रिया सम्मव नहीं है।
- **Should be:**
  > =0.80-0.34=0.46 \mathrm{~V}
  > $$
  > अतः अभिक्रिया सम्भव नहीं है।

### q_2.17 — solution (hi)
- **Confidence:** high
- **Reason:** Same reconstruction, part (iii)'s conclusion.
- **Found:**
  > =0.77-1.09=-0.32 \mathrm{~V}
  > $$
  > अतः अभिक्रिया सम्मव नहीं है।
- **Should be:**
  > =0.77-1.09=-0.32 \mathrm{~V}
  > $$
  > अतः अभिक्रिया सम्भव नहीं है।

### q_2.17 — solution (hi)
- **Confidence:** high
- **Reason:** Same reconstruction, part (iv)'s conclusion.
- **Found:**
  > =0.77-0.80=-0.03 \mathrm{~V}
  > $$
  > अतः अभिक्रिया सम्मव नहीं है।
- **Should be:**
  > =0.77-0.80=-0.03 \mathrm{~V}
  > $$
  > अतः अभिक्रिया सम्भव नहीं है।

### q_2.17 — solution (hi)
- **Confidence:** high
- **Reason:** Same reconstruction, part (v)'s conclusion (also a genuine self-contradiction verdict, +0.32 V yet 'not feasible' - left untouched, only the spelling fixed).
- **Found:**
  > =1.09-0.77=+0.32 \mathrm{~V}
  > $$
  > अतः अभिक्रिया सम्मव नहीं है।
- **Should be:**
  > =1.09-0.77=+0.32 \mathrm{~V}
  > $$
  > अतः अभिक्रिया सम्भव नहीं है।

### q_2.5 — solution (hi)
- **Confidence:** high
- **Reason:** Part (iv) used E deg(Br2/Br-) = 1.08 V, but chapter.hi.pdf's own Table 2.1 (page 37, confirmed by direct 200dpi render) states 1.09 V for this exact half-cell, and this same chapter's own q_2.17 solution already correctly uses 1.09 V for the identical couple - an internal self-contradiction. The 1.08 V value traces to a genuine error in solutions.hi.pdf page 76 (confirmed by direct render, not an OCR artifact). Corrected to 1.09 V throughout, giving emf = -1.298 V (was -1.288 V).
- **Found:**
  > हल (i) सेल समीकरण $\mathrm{Mg}(s)+\mathrm{Cu}^{2+}(\mathrm{aq}) \longrightarrow \mathrm{Mg}^{2+}(\mathrm{aq})+\mathrm{Cu}(\mathrm{s}) \quad(n=2)$
  > नेर्न्स्ट समीकरण
  > $$
  > E_{\text {सेल }}=E_{\text {सेल }}^{\circ}-\frac{0.0591}{2} \log \frac{\left[\mathrm{Mg}^{2+}\right]}{\left[\mathrm{Cu}^{2+}\right]}
  > $$
  > सेल का emf,
  > $$
  > \begin{aligned}
  > E_{\text {सेल }} & =[0.34-(-2.37)]-\frac{0.0591}{2} \log \frac{\left[10^{-3}\right]}{\left[10^{-4}\right]} \\
  > & =2.71-0.02955=2.68 \mathrm{~V}
  > \end{aligned}
  > $$
  > अत:
  > $$
  > \text { emf }=2.68 \mathrm{~V}
  > $$
  > (ii) सेल समीकरण $\mathrm{Fe}(\mathrm{s})+2 \mathrm{H}^{+}(\mathrm{aq}) \longrightarrow \mathrm{Fe}^{2+}(\mathrm{aq})+\mathrm{H}_{2}(\mathrm{~g}) \quad(n=2)$
  > नेर्न्स्ट समीकरण $E_{\text {सेल }}=E_{\text {सेल }}^{\circ}-\frac{0.0591}{2} \log \frac{\left[\mathrm{Fe}^{2+}\right]}{\left[\mathrm{H}^{+}\right]^{2}}$
  > सेल का emf,
  > $$
  > \begin{aligned}
  > E_{\text {सेल }} & =[0-(-0.44)]-\frac{0.0591}{2} \log \frac{\left[10^{-3}\right]}{[1]^{2}} \\
  > & =0.44-\frac{0.591}{2} \times(-3) \\
  > & =0.44+0.0887 \\
  > & =0.5287 \mathrm{~V} \\
  > & \approx 0.53 \mathrm{~V}
  > \end{aligned}
  > $$
  > अत:
  > $$
  > \text { emf }=0.53 \mathrm{~V}
  > $$
  > (iii) सेल समीकरण $\mathrm{Sn}(s)+2 \mathrm{H}^{+}(a q) \longrightarrow \mathrm{Sn}^{2+}(a q)+\mathrm{H}_{2}(g) \quad(n=2)$
  > नेर्न्स्ट समीकरण $E_{\text {सेल }}=E_{\text {सेल }}^{\circ}-\frac{0.0591}{2} \log \frac{\left[\mathrm{Sn}^{2+}\right]}{\left[\mathrm{H}^{+}\right]^{2}}$
  > सेल का emf
  > $$
  > \begin{aligned}
  > E_{\text {सेल }} & =[0-(-0.14)]-\frac{0.0591}{2} \log \frac{[0.05]}{[0.02]^{2}} \\
  > & =0.14-\frac{0.0591}{2} \times(2.097) \\
  > & =0.14-0.0620=0.08 \mathrm{~V}
  > \end{aligned}
  > $$
  > अत:
  > $$
  > \text { emf }=0.08 \mathrm{~V}
  > $$
  > (iv) सेल समीकरण $2 \mathrm{Br}^{-}(l)+2 \mathrm{H}^{+}(\mathrm{aq}) \longrightarrow \mathrm{Br}_{2}(l)+\mathrm{H}_{2}(g)$ $(n=2)$
  > नेर्न्स्ट समीकरण
  > $$
  > E_{\text {सेल }}=E_{\text {सेल }}^{\circ}-\frac{0.0591}{2} \log \frac{1}{\left[\mathrm{Br}^{-}\right]^{2}\left[\mathrm{H}^{+}\right]^{2}}
  > $$
  > सेल का emf
  > $$
  > \begin{aligned}
  > E_{\text {सेल }} & =[0-1.08]-\frac{0.0591}{2} \log \frac{1}{(0.01)^{2} \times(0.03)^{2}} \\
  > & =-1.08-\frac{0.0591}{2} \log \left(1.111 \times 10^{7}\right) \\
  > & =-1.08-\frac{0.0591}{2}(7.0457) \\
  > & =-1.08-0.208 \\
  > & =-1.288 \mathrm{~V}
  > \end{aligned}
  > $$
  > अत:
  > $$
  > e m f=-1.288 \mathrm{~V}
  > $$
- **Should be:**
  > हल (i) सेल समीकरण $\mathrm{Mg}(s)+\mathrm{Cu}^{2+}(\mathrm{aq}) \longrightarrow \mathrm{Mg}^{2+}(\mathrm{aq})+\mathrm{Cu}(\mathrm{s}) \quad(n=2)$
  > नेर्न्स्ट समीकरण
  > $$
  > E_{\text {सेल }}=E_{\text {सेल }}^{\circ}-\frac{0.0591}{2} \log \frac{\left[\mathrm{Mg}^{2+}\right]}{\left[\mathrm{Cu}^{2+}\right]}
  > $$
  > सेल का emf,
  > $$
  > \begin{aligned}
  > E_{\text {सेल }} & =[0.34-(-2.37)]-\frac{0.0591}{2} \log \frac{\left[10^{-3}\right]}{\left[10^{-4}\right]} \\
  > & =2.71-0.02955=2.68 \mathrm{~V}
  > \end{aligned}
  > $$
  > अत:
  > $$
  > \text { emf }=2.68 \mathrm{~V}
  > $$
  > (ii) सेल समीकरण $\mathrm{Fe}(\mathrm{s})+2 \mathrm{H}^{+}(\mathrm{aq}) \longrightarrow \mathrm{Fe}^{2+}(\mathrm{aq})+\mathrm{H}_{2}(\mathrm{~g}) \quad(n=2)$
  > नेर्न्स्ट समीकरण $E_{\text {सेल }}=E_{\text {सेल }}^{\circ}-\frac{0.0591}{2} \log \frac{\left[\mathrm{Fe}^{2+}\right]}{\left[\mathrm{H}^{+}\right]^{2}}$
  > सेल का emf,
  > $$
  > \begin{aligned}
  > E_{\text {सेल }} & =[0-(-0.44)]-\frac{0.0591}{2} \log \frac{\left[10^{-3}\right]}{[1]^{2}} \\
  > & =0.44-\frac{0.591}{2} \times(-3) \\
  > & =0.44+0.0887 \\
  > & =0.5287 \mathrm{~V} \\
  > & \approx 0.53 \mathrm{~V}
  > \end{aligned}
  > $$
  > अत:
  > $$
  > \text { emf }=0.53 \mathrm{~V}
  > $$
  > (iii) सेल समीकरण $\mathrm{Sn}(s)+2 \mathrm{H}^{+}(a q) \longrightarrow \mathrm{Sn}^{2+}(a q)+\mathrm{H}_{2}(g) \quad(n=2)$
  > नेर्न्स्ट समीकरण $E_{\text {सेल }}=E_{\text {सेल }}^{\circ}-\frac{0.0591}{2} \log \frac{\left[\mathrm{Sn}^{2+}\right]}{\left[\mathrm{H}^{+}\right]^{2}}$
  > सेल का emf
  > $$
  > \begin{aligned}
  > E_{\text {सेल }} & =[0-(-0.14)]-\frac{0.0591}{2} \log \frac{[0.05]}{[0.02]^{2}} \\
  > & =0.14-\frac{0.0591}{2} \times(2.097) \\
  > & =0.14-0.0620=0.08 \mathrm{~V}
  > \end{aligned}
  > $$
  > अत:
  > $$
  > \text { emf }=0.08 \mathrm{~V}
  > $$
  > (iv) सेल समीकरण $2 \mathrm{Br}^{-}(l)+2 \mathrm{H}^{+}(\mathrm{aq}) \longrightarrow \mathrm{Br}_{2}(l)+\mathrm{H}_{2}(g)$ $(n=2)$
  > नेर्न्स्ट समीकरण
  > $$
  > E_{\text {सेल }}=E_{\text {सेल }}^{\circ}-\frac{0.0591}{2} \log \frac{1}{\left[\mathrm{Br}^{-}\right]^{2}\left[\mathrm{H}^{+}\right]^{2}}
  > $$
  > सेल का emf
  > $$
  > \begin{aligned}
  > E_{\text {सेल }} & =[0-1.09]-\frac{0.0591}{2} \log \frac{1}{(0.01)^{2} \times(0.03)^{2}} \\
  > & =-1.09-\frac{0.0591}{2} \log \left(1.111 \times 10^{7}\right) \\
  > & =-1.09-\frac{0.0591}{2}(7.0457) \\
  > & =-1.09-0.208 \\
  > & =-1.298 \mathrm{~V}
  > \end{aligned}
  > $$
  > अत:
  > $$
  > e m f=-1.298 \mathrm{~V}
  > $$

### q_2.16 — solution (hi)
- **Confidence:** high
- **Reason:** 863.7 s / 60 = 14.395 min = 14 min 23.7 s, not '14 min 39 s' as both solutions.hi.pdf page 84 (confirmed by direct render) and this pipeline's own solution stated - a genuine arithmetic error in the official solutions manual, not an OCR artifact. The charge/current-derived 863.7 s figure itself, and the downstream Cu/Zn mass calculations (which use 1295.6 C directly, not the time), are unaffected.
- **Found:**
  > हल (a)
  > $$
  > \mathrm{Ag}^{+}(\mathrm{aq})+\underset{1 \mathrm{~mol}}{\mathrm{e}^{-}} \longrightarrow \underset{\substack{1 \mathrm{~mol} \\(108 \mathrm{~g})}}{\mathrm{Ag}(\mathrm{~s})}
  > $$
  > $\because 108 \mathrm{~g}$ वैद्युत द्वारा सिल्वर निक्षेपित होता है $=96500 \mathrm{C}$ वैद्युत द्वारा
  > $\therefore 1.45 \mathrm{~g}$ वैद्युत द्वारा सिल्वर निक्षेपित होता है $=\frac{(96500 \mathrm{C}) \times(1.45 \mathrm{~g})}{(108 \mathrm{~g})}$ $=1295.6 \mathrm{C}$ वैद्युत द्वारा
  > $\because$ धारा $(i)=1.5 \mathrm{~A}$
  > $$
  > \begin{aligned}
  > \therefore \text { समय }(t)=\frac{Q}{i}=\frac{(1295.6 \mathrm{C})}{(1.5 \mathrm{~A})} & =863.7 \mathrm{~s} \\
  > & =14 \mathrm{~min} 39 \mathrm{~s}
  > \end{aligned}
  > $$
  > (b)
  > $$
  > \mathrm{Cu}^{2+}(\mathrm{aq})+\underset{(2 \times 96500 \mathrm{C})}{2 \mathrm{e}^{-}} \longrightarrow \underset{63.5 \mathrm{~g}}{\mathrm{Cu}(\mathrm{~s})}
  > $$
  > $\because(2 \times 96500 \mathrm{C})$ वैद्युत प्रवाहित करने पर निक्षेपित $\mathrm{Cu}=63.5 \mathrm{~g}$
  > $\therefore 1295.6 \mathrm{C}$ वैद्युत प्रवाहित करने पर निक्षेपित $\mathrm{Cu}=\frac{(63.5) \times(1295.6 \mathrm{C})}{(2 \times 96500 \mathrm{C})}=0.426 \mathrm{~g}$
  > $$
  > \mathrm{Zn}^{2+}(\mathrm{aq})+\underset{(2 \times 96500 \mathrm{C})}{2 \mathrm{e}^{-}} \longrightarrow \underset{65.3 \mathrm{~g}}{\mathrm{Zn}(\mathrm{~s})}
  > $$
  > $\because(2 \times 96500) \mathrm{C}$ वैद्युत प्रवाहित करने पर निक्षेपित $\mathrm{Zn}=65.3 \mathrm{~g}$
  > $\therefore 1295.6 \mathrm{C}$ वैद्युत प्रवाहित करने पर निक्षेपित $\mathrm{Zn}=\frac{(65.3 \mathrm{~g}) \times(12956 \mathrm{C})}{(2 \times 96500 \mathrm{C})}$
  > $$
  > =0.438 \mathrm{~g}
  > $$
  > अतः निक्षेपित Cu की मात्रा $=0.426 \mathrm{~g}$
  > तथा निक्षेपित Zn की मात्रा = $0.438 \mathrm{~g}$
- **Should be:**
  > हल (a)
  > $$
  > \mathrm{Ag}^{+}(\mathrm{aq})+\underset{1 \mathrm{~mol}}{\mathrm{e}^{-}} \longrightarrow \underset{\substack{1 \mathrm{~mol} \\(108 \mathrm{~g})}}{\mathrm{Ag}(\mathrm{~s})}
  > $$
  > $\because 108 \mathrm{~g}$ वैद्युत द्वारा सिल्वर निक्षेपित होता है $=96500 \mathrm{C}$ वैद्युत द्वारा
  > $\therefore 1.45 \mathrm{~g}$ वैद्युत द्वारा सिल्वर निक्षेपित होता है $=\frac{(96500 \mathrm{C}) \times(1.45 \mathrm{~g})}{(108 \mathrm{~g})}$ $=1295.6 \mathrm{C}$ वैद्युत द्वारा
  > $\because$ धारा $(i)=1.5 \mathrm{~A}$
  > $$
  > \begin{aligned}
  > \therefore \text { समय }(t)=\frac{Q}{i}=\frac{(1295.6 \mathrm{C})}{(1.5 \mathrm{~A})} & =863.7 \mathrm{~s} \\
  > & =14 \mathrm{~min} 23.7 \mathrm{~s} \approx 14 \mathrm{~min} 24 \mathrm{~s}
  > \end{aligned}
  > $$
  > (b)
  > $$
  > \mathrm{Cu}^{2+}(\mathrm{aq})+\underset{(2 \times 96500 \mathrm{C})}{2 \mathrm{e}^{-}} \longrightarrow \underset{63.5 \mathrm{~g}}{\mathrm{Cu}(\mathrm{~s})}
  > $$
  > $\because(2 \times 96500 \mathrm{C})$ वैद्युत प्रवाहित करने पर निक्षेपित $\mathrm{Cu}=63.5 \mathrm{~g}$
  > $\therefore 1295.6 \mathrm{C}$ वैद्युत प्रवाहित करने पर निक्षेपित $\mathrm{Cu}=\frac{(63.5) \times(1295.6 \mathrm{C})}{(2 \times 96500 \mathrm{C})}=0.426 \mathrm{~g}$
  > $$
  > \mathrm{Zn}^{2+}(\mathrm{aq})+\underset{(2 \times 96500 \mathrm{C})}{2 \mathrm{e}^{-}} \longrightarrow \underset{65.3 \mathrm{~g}}{\mathrm{Zn}(\mathrm{~s})}
  > $$
  > $\because(2 \times 96500) \mathrm{C}$ वैद्युत प्रवाहित करने पर निक्षेपित $\mathrm{Zn}=65.3 \mathrm{~g}$
  > $\therefore 1295.6 \mathrm{C}$ वैद्युत प्रवाहित करने पर निक्षेपित $\mathrm{Zn}=\frac{(65.3 \mathrm{~g}) \times(12956 \mathrm{C})}{(2 \times 96500 \mathrm{C})}$
  > $$
  > =0.438 \mathrm{~g}
  > $$
  > अतः निक्षेपित Cu की मात्रा $=0.426 \mathrm{~g}$
  > तथा निक्षेपित Zn की मात्रा = $0.438 \mathrm{~g}$

### q_2.16 — final_answer (hi)
- **Confidence:** high
- **Reason:** Propagates the seconds-to-minutes correction above into the final answer line.
- **Found:**
  > समय = 863.7 s (14 min 39 s); निक्षेपित Cu = 0.426 g; निक्षेपित Zn = 0.438 g
- **Should be:**
  > समय = 863.7 s (≈ 14 min 24 s); निक्षेपित Cu = 0.426 g; निक्षेपित Zn = 0.438 g
