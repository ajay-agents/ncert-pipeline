### it_4.2 — solution (hi)
- **Confidence:** high
- **Reason:** OCR dropped the initial "भ" of "भागीदारी", corrupting it to "मागीदारी"
- **Found:**
  > बंधन में मागीदारी नहीं
- **Should be:**
  > बंधन में भागीदारी नहीं

### it_4.2 — solution (hi)
- **Confidence:** high
- **Reason:** OCR substituted "य" for "व" in "अधात्विक", producing the non-word "अधात्यिक"; solutions PDF page 1 (सारणी/प्रश्न 2 हल) reads "अधात्विक बंध दुर्बल है"
- **Found:**
  > जिंक में अधात्यिक बंध दुर्बल है
- **Should be:**
  > जिंक में अधात्विक बंध दुर्बल है

### it_4.2 — solution (hi)
- **Confidence:** high
- **Reason:** OCR corrupted "एन्थैल्पी" (enthalpy) to the non-word "एन्यैल्पी"; solutions PDF confirms "कणन एन्थैल्पी"
- **Found:**
  > जिंक की कणन एन्यैल्पी अपनी संक्रमण श्रेणी
- **Should be:**
  > जिंक की कणन एन्थैल्पी अपनी संक्रमण श्रेणी

### it_4.4 — solution (hi)
- **Confidence:** high
- **Reason:** OCR corrupted "एन्थैल्पी" to "एन्यैल्पी" in the ΔaH label; solutions PDF (प्रश्न 4 हल, item i) reads "(कणन एन्थैल्पी)"
- **Found:**
  > (कणन एन्यैल्पी)
- **Should be:**
  > (कणन एन्थैल्पी)

### it_4.4 — solution (hi)
- **Confidence:** high
- **Reason:** Same OCR corruption ("एन्थैल्पी" → "एन्यैल्पी"); solutions PDF reads "जलयोजन एन्थैल्पी का मान कम है"
- **Found:**
  > जलयोजन एन्यैल्पी का मान कम
- **Should be:**
  > जलयोजन एन्थैल्पी का मान कम

### it_4.5 — solution (hi)
- **Confidence:** high
- **Reason:** OCR misread the exponent-bearing term "3d-विन्यास" as the digits "30-विन्यास" — a number/OCR error, not a wording change. Solutions PDF (प्रश्न 5 हल) reads "3d-विन्यास का स्थायित्व कुछ हद तक भिन्न है"
- **Found:**
  > क्योंकि 30-विन्यास का स्थायित्व
- **Should be:**
  > क्योंकि 3d-विन्यास का स्थायित्व

### it_4.5 — solution (hi)
- **Confidence:** high
- **Reason:** OCR corrupted "एन्थैल्पी" to "एन्यैल्पी"; solutions PDF reads "सामान्यतः आयनन एन्थैल्पी का मान ... बढ़ता है"
- **Found:**
  > सामान्यतः आयनन एन्यैल्पी का मान प्रभावी
- **Should be:**
  > सामान्यतः आयनन एन्थैल्पी का मान प्रभावी

### it_4.5 — solution (hi)
- **Confidence:** high
- **Reason:** Same OCR corruption ("एन्थैल्पी" → "एन्यैल्पी"); solutions PDF reads "इनके लिए आयनन एन्थैल्पी का मान उच्च होता है"
- **Found:**
  > अतः इनके लिए आयनन एन्यैल्पी का मान उच्च
- **Should be:**
  > अतः इनके लिए आयनन एन्थैल्पी का मान उच्च

### it_4.9 — solution (hi)
- **Confidence:** high
- **Reason:** Flagged Cu+/Cu2+ mixup confirmed against sol_03.png. The extracted text compares "Cu+(aq)" against "Cu+(aq)" (identical ions, meaningless comparison). The solutions PDF states Cu2+(aq) is more stable than Cu+(aq) — the second ion in the comparison must be Cu2+, matching the rest of the same solution ("Cu2+ आयन के बनने में दी जाने वाली द्वितीय आयनन एन्थैल्पी की क्षतिपूर्ति करती है ... जलीय विलयन में Cu+ आयन अधिक स्थाई Cu2+ आयन में परिवर्तित हो जाता है")
- **Found:**
  > जलीय विलयन में $\mathrm{Cu}^{+}(\mathrm{aq})$ आयन की तुलना में $\mathrm{Cu}^{+}(\mathrm{aq})$ आयन का अधिक स्थायित्व
- **Should be:**
  > जलीय विलयन में $\mathrm{Cu}^{+}(\mathrm{aq})$ आयन की तुलना में $\mathrm{Cu}^{2+}(\mathrm{aq})$ आयन का अधिक स्थायित्व

### it_4.10 — solution (hi)
- **Confidence:** high
- **Reason:** Flagged Bengali-script substitution confirmed against sol_03.png. The word for "lanthanoid" was corrupted to contain the Bengali conjunct "ন্য" instead of the correct Devanagari "लैन्थेनॉयड" — the spelling used consistently everywhere else in this chapter (e.g. it_4.10's own question line, and चित्र 4.6/4.7 captions)
- **Found:**
  > तैন্যেनॉयड आकुंचन की तुलना में
- **Should be:**
  > लैन्थेनॉयड आकुंचन की तुलना में

### it_4.10 — solution (hi)
- **Confidence:** medium
- **Reason:** "ऐक्टिनायॅड" is an inconsistent/corrupted spelling next to the correctly-spelled "ऐक्टिनॉयड" later in the very same sentence and in the question line itself; solutions PDF (प्रश्न 10 हल) uses "ऐक्टिनॉयड" throughout
- **Found:**
  > दूसरे तत्व के बीच ऐक्टिनायॅड आकुंचन अधिक होता है
- **Should be:**
  > दूसरे तत्व के बीच ऐक्टिनॉयड आकुंचन अधिक होता है

### q_4.1 — solution (hi)
- **Confidence:** high
- **Reason:** OCR misread the 3d subshell exponent notation as "3s" in the bracketed shorthand configuration for part (vii)'s parent atom Mn (the expanded configuration just before it correctly shows "3s^{2}p^{6}d^{5}4s^{2}", confirming the shorthand should use d, not s)
- **Found:**
  > या [Ar] $3 s^{5} 4 s^{2}$
- **Should be:**
  > या [Ar] $3 d^{5} 4 s^{2}$

### q_4.11 — solution (hi)
- **Confidence:** high
- **Reason:** OCR misread ध (dental dha) as घ (velar gha) in this one occurrence of "बंध" (the other two occurrences of the same word later in the same solution are correctly rendered as आबंध); the source page reads आबंध consistently throughout.
- **Found:**
  > के परमाणुओं के बीच आबंघ बनते हैं।
- **Should be:**
  > के परमाणुओं के बीच आबंध बनते हैं।

### q_4.11 — solution (hi)
- **Confidence:** high
- **Reason:** OCR misread the "3d" subshell notation (styled in italic in the source) as the Devanagari word "अठ".
- **Found:**
  > प्रथम संक्रमण श्रेणी की धातुएँ अठ- एवं
- **Should be:**
  > प्रथम संक्रमण श्रेणी की धातुएँ $3d$- एवं

### q_4.14 — solution (hi)
- **Confidence:** high
- **Reason:** OCR misread the compound name "सोडियम डाइक्रोमेट" (sodium dichromate) — the source clearly reads सोडियम (starting स), not नोडियम.
- **Found:**
  > नोडियम डाइक्रोमेंट
- **Should be:**
  > सोडियम डाइक्रोमेट

### q_4.18 — solution (hi)
- **Confidence:** high
- **Reason:** OCR misread the italic "3d" subshell notation as the digit sequence "30" (the recurring 3d→30 pattern in this chapter). The table two lines above this sentence, in the same field, correctly shows "3 d^{1}" etc., confirming this is an isolated misread.
- **Found:**
  > $30^{0}$ तथा $30^{10}$ विन्यास है
- **Should be:**
  > $3d^{0}$ तथा $3d^{10}$ विन्यास है

### q_4.20 — solution (hi)
- **Confidence:** high
- **Reason:** Script corruption — "अवस्थाएँ" was garbled to "अवस्याऍ" in the lanthanoid-column table header; PDF clearly shows "ऑक्सीकरण अवस्थाएँ".
- **Found:**
  > ऑक्सीकरण अवस्याऍ
- **Should be:**
  > ऑक्सीकरण अवस्थाएँ

### q_4.20 — solution (hi)
- **Confidence:** high
- **Reason:** Script corruption — "अवस्थाएँ" was garbled to "अवस्याएँ" in the actinoid-column table header; PDF clearly shows "ऑक्सीकरण अवस्थाएँ".
- **Found:**
  > ऑक्सीकरण अवस्याएँ
- **Should be:**
  > ऑक्सीकरण अवस्थाएँ

### q_4.20 — solution (hi)
- **Confidence:** high
- **Reason:** Duplicated row-header text in the lanthanoid column of row (iv) — the PDF prints "रांसायनिक अभिक्रियाशीलता" once before the (a)-(d) list (matching the single occurrence in the actinoid column), not twice.
- **Found:**
  > रांसायनिक अभिक्रियाशीलता <br> रांसायनिक अभिक्रियाशीलता<br>(a) संकुल
- **Should be:**
  > रांसायनिक अभिक्रियाशीलता<br>(a) संकुल

### q_4.20 — solution (hi)
- **Confidence:** high
- **Reason:** Script corruption — Devanagari "ध" misread as "घ" ("ऑक्सोघनायन" for "ऑक्सोधनायन"); the PDF's own lanthanoid-column entry for the same row correctly uses "ऑक्सोधनायन", confirming the intended word.
- **Found:**
  > ऑक्सोघनायन
- **Should be:**
  > ऑक्सोधनायन

### q_4.23 — solution (hi)
- **Confidence:** high
- **Reason:** Recurring OCR pattern in this chapter — "3d" (the 3d subshell) misread as "30". The PDF clearly shows "स्थाई विन्यास, 3d^10 सहित Cu+ आयन बनाता है", matching the earlier "[Ar] 3d^10 4s^1" in the same sentence.
- **Found:**
  > $30^{10}$
- **Should be:**
  > $3d^{10}$

### q_4.22 — solution (hi)
- **Confidence:** high
- **Reason:** Duplicated digit — the PDF shows the coefficient "2" appearing once before MnO4- (with the (+7) oxidation-state label above only "MnO4-"), not twice.
- **Found:**
  > 2 \stackrel{(+7)}{2 \mathrm{MnO}_{4}^{-}}
- **Should be:**
  > \stackrel{(+7)}{2 \mathrm{MnO}_{4}^{-}}

### q_4.27 — solution (hi)
- **Confidence:** high
- **Reason:** Script corruption — "ध" misread as "घ" ("मिश्र-घातुएँ" for "मिश्र-धातुएँ"); PDF shows "मिश्र-धातुएँ एक महत्वपूर्ण मिश्र-धातुएँ है".
- **Found:**
  > मिश्र-घातुएँ एक महत्वपूर्ण
- **Should be:**
  > मिश्र-धातुएँ एक महत्वपूर्ण

### q_4.27 — solution (hi)
- **Confidence:** high
- **Reason:** Script corruption — "थ" dropped and "ध" misread as "घ" ("लैन्येनॉयड घातु" for "लैन्थेनॉयड धातु"); PDF clearly reads "लैन्थेनॉयड धातु (~95%)".
- **Found:**
  > लैन्येनॉयड घातु
- **Should be:**
  > लैन्थेनॉयड धातु

### q_4.27 — solution (hi)
- **Confidence:** high
- **Reason:** OCR letter confusion — the chemical symbol for aluminium, "Al", was misread as "AI" (capital I instead of lowercase l).
- **Found:**
  > व AI से बनी
- **Should be:**
  > व Al से बनी

### q_4.27 — solution (hi)
- **Confidence:** high
- **Reason:** Script corruption — "ध" misread as "घ" a second time ("मिश्र-घातुएँ" for "मिश्र-धातुएँ") in part (iii); PDF shows "आधारित मिश्र-धातुएँ में प्रयुक्त होती है".
- **Found:**
  > आधारित मिश्र-घातुएँ में
- **Should be:**
  > आधारित मिश्र-धातुएँ में

### q_4.27 — solution (hi)
- **Confidence:** high
- **Reason:** Script corruption — stray anusvara inserted ("बंदूंक" for "बंदूक"); PDF clearly shows "जो बंदूक की गोली".
- **Found:**
  > जो बंदूंक की गोली
- **Should be:**
  > जो बंदूक की गोली

### q_4.27 — solution (hi)
- **Confidence:** high
- **Reason:** Script corruption — "तथा" (and) was garbled into the non-word "तभ्या". PDF context ("कवच या खोल तथा हल्के ... उत्पादन में") confirms "तथा" is correct.
- **Found:**
  > तभ्या हल्के
- **Should be:**
  > तथा हल्के

### q_4.27 — solution (hi)
- **Confidence:** medium
- **Reason:** The PDF glyph for this word carries an anusvara ("फिंलट") that the extraction dropped ("फिलट"). Word is unclear/possibly a printing artifact in the source itself, but the anusvara is visible on close inspection of the page image.
- **Found:**
  > हल्के फिलट उत्पादन
- **Should be:**
  > हल्के फिंलट उत्पादन

### q_4.32 — question (hi)
- **Confidence:** high
- **Reason:** OCR dropped the word "जो" before the first oxidation state, breaking the sentence's grammar/meaning ("...उल्लेख कीजिए जो +4 तथा जो +2..." in the PDF, vs "...उल्लेख कीजिए +4 तथा जो +2..." extracted)
- **Found:**
  > उल्लेख कीजिए $+4$ तथा जो + $2$
- **Should be:**
  > उल्लेख कीजिए जो $+4$ तथा जो $+2$

### q_4.33 — solution (hi)
- **Confidence:** high
- **Reason:** Solution-swap between q_4.33 and q_4.34. The official solutions booklet mislabels its answers ("प्रश्न 33" holds the answer to the electronic-configuration question, and "प्रश्न 34" holds the answer to the actinoid/lanthanoid comparison question) — the reverse of the textbook's own exercise numbering. The extraction paired solutions by the booklet's (mislabeled) number instead of by content, so q_4.33 (actinoid vs lanthanoid comparison) ended up with the Z=61/91/101/109 electronic-configuration answer that actually belongs to q_4.34, and q_4.34 ended up with the "see Q20" pointer that belongs to q_4.33. Confirmed against sol_17.png/sol_18.png: the page labelled "प्रश्न 33" shows "61, 91, 101 तथा 109 परमाणु क्रमांक वाले तत्वों के इलेक्ट्रॉनिक विन्यास लिखिए। हल प्रोमिथियम या Pm (Z=61)=[Xe]4f⁵5d⁰6s²..." while the page labelled "प्रश्न 34" shows "निम्नलिखित के सन्दर्भ में ऐक्टिनॉयड श्रेणी के तत्वों तथा लैन्थेनॉयड श्रेणी के तत्वों के रसायन की तुलना कीजिए... हल अभ्यास के प्रश्न 20 का हल देखें।"
- **Found:**
  > प्रोमिथियम या $\mathrm{Pm}(Z=61)=[\mathrm{Xe}] 4 f^{5} 5 d^{0} 6 s^{2}$
  > प्रोटैक्टिनियम या $\quad \mathrm{Pa}(Z=91)=[R n] 5 f^{2} 6 d^{1} 7 s^{2}$
  > मेन्डेलीवियम या $\quad M d(Z=101)=[R n] 5 f^{13} 6 d^{0} 7 s^{2}$
  > मेटनीरियम या $\quad \mathrm{Mt}(\mathrm{Z}=109)=[\mathrm{Rn}] 5 f^{14} 6 d^{7} 7 s^{2}$
- **Should be:**
  > अभ्यास के प्रश्न $20$ का हल देखें।

### q_4.34 — solution (hi)
- **Confidence:** high
- **Reason:** Other half of the same solution-swap described for q_4.33 — this item (Z=61/91/101/109 electronic configurations) currently carries the "see Q20" pointer that belongs to q_4.33, while its own correct answer (the Pm/Pa/Md/Mt configurations, confirmed on sol_17.png under the booklet's mislabeled "प्रश्न 33") is currently attached to q_4.33 instead.
- **Found:**
  > अभ्यास के प्रश्न $20$ का हल देखें।
- **Should be:**
  > प्रोमिथियम या $\mathrm{Pm}(Z=61)=[\mathrm{Xe}] 4 f^{5} 5 d^{0} 6 s^{2}$
  > प्रोटैक्टिनियम या $\quad \mathrm{Pa}(Z=91)=[R n] 5 f^{2} 6 d^{1} 7 s^{2}$
  > मेन्डेलीवियम या $\quad M d(Z=101)=[R n] 5 f^{13} 6 d^{0} 7 s^{2}$
  > मेटनीरियम या $\quad \mathrm{Mt}(\mathrm{Z}=109)=[\mathrm{Rn}] 5 f^{14} 6 d^{7} 7 s^{2}$

### q_4.36 — solution (hi)
- **Confidence:** high
- **Reason:** Table header cell corrupted — "व" misread as "प" (क्रमांक abbreviation should read "विन्यास", not "पिन्यास")
- **Found:**
  > पिन्यास
- **Should be:**
  > विन्यास

### q_4.36 — solution (hi)
- **Confidence:** high
- **Reason:** Table header cell has stray non-Devanagari (Tamil) characters mixed in from OCR, and "3d" was misread as "30" — PDF header reads "3d इलेक्ट्रॉनों की संख्या"
- **Found:**
  > 30 தக்கங் in की संख्या
- **Should be:**
  > 3d इलेक्ट्रॉनों की संख्या

### q_4.36 — solution (hi)
- **Confidence:** high
- **Reason:** Table header cell has stray non-Devanagari (Tamil) characters mixed in from OCR, and "3d" was misread as "30" — PDF header reads "3d-कक्षक में इलेक्ट्रॉनों का जाना"
- **Found:**
  > 30-கसक में इलेक्ट्रॉनों का जाना
- **Should be:**
  > 3d-कक्षक में इलेक्ट्रॉनों का जाना

### q_4.36 — solution (hi)
- **Confidence:** high
- **Reason:** Table header abbreviation lost its anusvara ("क्र.सं." misread as "क्र.स.")
- **Found:**
  > क्र.स.
- **Should be:**
  > क्र.सं.

### q_4.36 — solution (hi)
- **Confidence:** high
- **Reason:** Row (i) ion symbol "Ti²⁺" was OCR-misread as the Greek letter π
- **Found:**
  > $\pi^{2+}$
- **Should be:**
  > $\mathrm{Ti}^{2+}$

### q_4.36 — solution (hi)
- **Confidence:** high
- **Reason:** Row (ix), Cu²⁺'s orbital-occupancy cell was left blank; the PDF shows $t_{2g}^{6} e_{g}^{3}$ for this row
- **Found:**
  > | (ix) | $\mathrm{Cu}^{2+}$ | $3 d^{9}$ | $9$ |  | ![](images/fig_4_21.jpg)![](images/fig_4_22.jpg) |
- **Should be:**
  > | (ix) | $\mathrm{Cu}^{2+}$ | $3 d^{9}$ | $9$ | $t_{2g}^{6} e_{g}^{3}$ | ![](images/fig_4_21.jpg)![](images/fig_4_22.jpg) |

### q_4.18 — solution (hi)
- **Confidence:** medium
- **Reason:** Same-page self-contradiction, approved by user: the concluding sentence calls Ti3+, V3+, Mn2+, Fe3+, Co2+ colorless, directly contradicting the table two lines above in the same solution which assigns each of them a specific color (the derivation logic itself, stated in the opening line, also implies only Sc3+/Cu+ with d0/d10 configurations are colorless).
- **Found:**
  > शेष सभी $\mathrm{Ti}^{3+}, \mathrm{V}^{3+}, \mathrm{Mn}^{2+}, \mathrm{Fe}^{3+}$ तथा $\mathrm{Co}^{2+}$ जलीय विलयन में रंगहीन है।
- **Should be:**
  > शेष सभी $\mathrm{Ti}^{3+}, \mathrm{V}^{3+}, \mathrm{Mn}^{2+}, \mathrm{Fe}^{3+}$ तथा $\mathrm{Co}^{2+}$ जलीय विलयन में रंगीन है।

### q_4.38 — solution (hi)
- **Confidence:** high
- **Reason:** Late correction found during stage 9's mandatory manual read-back (missed by stage 5's own batch F despite being told to watch for this exact pattern). OCR misread the italic "3d" subshell notation as the digit sequence "30". Confirmed against the source solutions PDF page (sol_21.png): "...H2O के अणु धातु आयन की तरफ पहुँचते हैं तो ये 3d-इलेक्ट्रॉनों में युग्मन नहीं करते..."
- **Found:**
  > $30$-इलेक्ट्रॉनों
- **Should be:**
  > $3d$-इलेक्ट्रॉनों

### it_4.2 — solution (hi)
- **Confidence:** high
- **Reason:** chapter.hi.pdf's Table 4.1/4.2 lists Zn as [Ar]3d^10 4s^2, the standard non-exceptional configuration - 4s^1 belongs to the Cu/Cr exception pattern, not Zn. Traced to a genuine error in solutions.hi.pdf page 168 (confirmed by direct 200dpi render). Corrected to 4s^2.
- **Found:**
  > जिंक $\left(3 d^{10} 4 s^{1}\right)$ में $d$-कक्षक पूर्ण भरित है अतः $d$-कक्षक के इलेक्ट्रॉन धात्विक बंधन में भागीदारी नहीं करते हैं। अतः श्रेणी के दूसरे तत्वों, जिनमें धात्विक बन्ध बनाने में $d$-कक्षक के इलेक्ट्रॉन भागीदारी करतें हैं की अपेक्षाकृत जिंक में अधात्विक बंध दुर्बल है। यही कारण है कि जिंक की कणन एन्थैल्पी अपनी संक्रमण श्रेणी में सबसे कम है।
- **Should be:**
  > जिंक $\left(3 d^{10} 4 s^{2}\right)$ में $d$-कक्षक पूर्ण भरित है अतः $d$-कक्षक के इलेक्ट्रॉन धात्विक बंधन में भागीदारी नहीं करते हैं। अतः श्रेणी के दूसरे तत्वों, जिनमें धात्विक बन्ध बनाने में $d$-कक्षक के इलेक्ट्रॉन भागीदारी करतें हैं की अपेक्षाकृत जिंक में अधात्विक बंध दुर्बल है। यही कारण है कि जिंक की कणन एन्थैल्पी अपनी संक्रमण श्रेणी में सबसे कम है।

### q_4.32 — solution (hi)
- **Confidence:** high
- **Reason:** chapter.hi.pdf's own body text (section 4.5.3) explicitly states 'Pr, Nd, Tb तथा Dy भी +4 ऑक्सीकरण अवस्था दर्शाते हैं' - Nd and Dy both belong in the +4 list, not +2. solutions.hi.pdf's own answer instead wrongly places Nd in +2 and omits Dy from +4 entirely - an error in the official answer key contradicting the textbook's own explicit statement. Corrected to match the textbook.
- **Found:**
  > $+4$ ऑक्सीकरण अवस्था ${ }_{58} \mathrm{Ce},{ }_{59} \mathrm{Pr}$ तथा ${ }_{65} \mathrm{~Tb}$ में पायी जाती है। $+2$ ऑक्सीकरण अवस्था ${ }_{60} \mathrm{Nd},{ }_{62} \mathrm{Sm}{ }_{63} \mathrm{Fu}_{69} \mathrm{Tm}$ तथा ${ }_{70} \mathrm{Yb}$ में पायी जाती है।
  > 
  > सामान्यतः $5 d^{0} 6 s^{2}$ विन्यास वाले तत्व आसानी से दो इलेक्ट्रॉन खोकर $+2$ ऑक्सीकरण अवस्था दर्शाते हैं। इसी प्रकार वे तत्व जो चार इलेक्ट्रॉन खोकर अपेक्षाकृत स्थाईविन्यास $4 f^{0}$ या $4 f^{7}$ ग्रहण कर सकते हैं, $+4$ ऑक्सीकरण अवस्था दर्शाते हैं।
- **Should be:**
  > $+4$ ऑक्सीकरण अवस्था ${ }_{58} \mathrm{Ce}, { }_{59} \mathrm{Pr}, { }_{60} \mathrm{Nd}, { }_{65} \mathrm{Tb}$ तथा ${ }_{66} \mathrm{Dy}$ में पायी जाती है। $+2$ ऑक्सीकरण अवस्था ${ }_{62} \mathrm{Sm}, { }_{63} \mathrm{Eu}, { }_{69} \mathrm{Tm}$ तथा ${ }_{70} \mathrm{Yb}$ में पायी जाती है।
  > 
  > सामान्यतः $5 d^{0} 6 s^{2}$ विन्यास वाले तत्व आसानी से दो इलेक्ट्रॉन खोकर $+2$ ऑक्सीकरण अवस्था दर्शाते हैं। इसी प्रकार वे तत्व जो चार इलेक्ट्रॉन खोकर अपेक्षाकृत स्थाईविन्यास $4 f^{0}$ या $4 f^{7}$ ग्रहण कर सकते हैं, $+4$ ऑक्सीकरण अवस्था दर्शाते हैं।

### q_4.20 — solution (hi)
- **Confidence:** high
- **Reason:** chapter.hi.pdf's own body text explicitly states 'Pa, U तथा Np में क्रमशः +5, +6 तथा +7 तक पहुँच जाती है' - Np reaches +7. solutions.hi.pdf's own answer to this question only lists +4,+5,+6 for actinoid oxidation states, omitting +7 - contradicts the textbook's own explicit statement. Corrected to add +7.
- **Found:**
  > | क्र.सं. | लैन्येंनॉयड | ऐक्टिनॉयड |
  > | :--- | :--- | :--- |
  > | (i) | इलेक्ट्रॉनिक विन्यास $\begin{aligned} & {[\mathrm{Xe}]_{54} 4 f^{1-14} 5 d^{0-1} 6 s^{2} } \\ & \text { उदाहरण, }{ }_{57 \mathrm{La}}=[\mathrm{Xe}] 5 d^{1} 6 s^{2} \\ & 58 \mathrm{Ce}=[\mathrm{Xe}] 4 f^{1} 5 d^{1} 6 s^{2} \end{aligned}$ | इलेक्ट्रॉनिक विन्यास $\begin{aligned} & {[\mathrm{Rn}]_{86} 5 f^{1-14} 6 d^{0-1} 7 s^{2} } \\ & \text { उदाहरण, }{ }_{89} \mathrm{Ac}=[\mathrm{Rn}] 6 d^{1} 7 s^{2} \\ & 90 \mathrm{Th}=[\mathrm{Rn}] 6 d^{2} 7 s^{2} \end{aligned}$ |
  > | (ii) | ऑक्सीकरण अवस्थाएँ <br> सामान्य ऑक्सीरण अवस्थाएँ $=+3$ <br> अन्य ऑक्सीकरण अवस्थाएँ $=+2,+4$. | ऑक्सीकरण अवस्थाएँ <br> सामान्य ऑक्सीरण अवस्थाएँ $=+3$ <br> अन्य ऑक्सीकरण अवस्थाएँ $=+4,+5$, +6. |
  > | (iii) | परमाण्वीय एवं आयनिक आकार <br> परमाणु/आयन का आकार आवर्त में (बाएँ से दाएँ) घटता है। <br> अपने वर्ग में लैन्थेंनॉयड तत्व का आकार ऐक्टिनॉयड से छोटा होता है। | परमाण्वीय एवं आयनिक आकार <br> परमाणु/आयन का आकार आवर्त में (बाएँ से दाएँ) घटता है। <br> अपने वर्ग में एक्टिनॉयड का आकार सबसे बड़ा है। |
  > | (iv) | रांसायनिक अभिक्रियाशीलता<br>(a) संकुल बनाने की प्रवृत्ति कम।<br>(b) केवल प्रोमिथियम रेडियोऐक्टिव है।<br>(c) ये ऑक्सोधनायन नहीं बनाते।<br> <br> (d) इनके ऑक्साइड तथा हाइड्रॉक्साइड कम क्षारीय हैं। | रासायनिक अभिक्रियाशीलता<br>(a) संकुल बनाने की प्रवृति प्रबल<br>(b) सभी ऐक्टिनॉयड रेडियोधर्मी हैं।<br>(c) ये ऑक्सोधनायन बनाते हैं जैसे $\mathrm{UO}_{2}^{2+}, \mathrm{PuO}_{2}^{2+}, \mathrm{UO}^{+}$, आदि।<br>(d) ऑक्साइड तथा हाइड्रॉक्साइड अधिक क्षारीय हैं।<br> |
- **Should be:**
  > | क्र.सं. | लैन्येंनॉयड | ऐक्टिनॉयड |
  > | :--- | :--- | :--- |
  > | (i) | इलेक्ट्रॉनिक विन्यास $\begin{aligned} & {[\mathrm{Xe}]_{54} 4 f^{1-14} 5 d^{0-1} 6 s^{2} } \\ & \text { उदाहरण, }{ }_{57 \mathrm{La}}=[\mathrm{Xe}] 5 d^{1} 6 s^{2} \\ & 58 \mathrm{Ce}=[\mathrm{Xe}] 4 f^{1} 5 d^{1} 6 s^{2} \end{aligned}$ | इलेक्ट्रॉनिक विन्यास $\begin{aligned} & {[\mathrm{Rn}]_{86} 5 f^{1-14} 6 d^{0-1} 7 s^{2} } \\ & \text { उदाहरण, }{ }_{89} \mathrm{Ac}=[\mathrm{Rn}] 6 d^{1} 7 s^{2} \\ & 90 \mathrm{Th}=[\mathrm{Rn}] 6 d^{2} 7 s^{2} \end{aligned}$ |
  > | (ii) | ऑक्सीकरण अवस्थाएँ <br> सामान्य ऑक्सीरण अवस्थाएँ $=+3$ <br> अन्य ऑक्सीकरण अवस्थाएँ $=+2,+4$. | ऑक्सीकरण अवस्थाएँ <br> सामान्य ऑक्सीरण अवस्थाएँ $=+3$ <br> अन्य ऑक्सीकरण अवस्थाएँ $=+4,+5,+6$, +7. |
  > | (iii) | परमाण्वीय एवं आयनिक आकार <br> परमाणु/आयन का आकार आवर्त में (बाएँ से दाएँ) घटता है। <br> अपने वर्ग में लैन्थेंनॉयड तत्व का आकार ऐक्टिनॉयड से छोटा होता है। | परमाण्वीय एवं आयनिक आकार <br> परमाणु/आयन का आकार आवर्त में (बाएँ से दाएँ) घटता है। <br> अपने वर्ग में एक्टिनॉयड का आकार सबसे बड़ा है। |
  > | (iv) | रांसायनिक अभिक्रियाशीलता<br>(a) संकुल बनाने की प्रवृत्ति कम।<br>(b) केवल प्रोमिथियम रेडियोऐक्टिव है।<br>(c) ये ऑक्सोधनायन नहीं बनाते।<br> <br> (d) इनके ऑक्साइड तथा हाइड्रॉक्साइड कम क्षारीय हैं। | रासायनिक अभिक्रियाशीलता<br>(a) संकुल बनाने की प्रवृति प्रबल<br>(b) सभी ऐक्टिनॉयड रेडियोधर्मी हैं।<br>(c) ये ऑक्सोधनायन बनाते हैं जैसे $\mathrm{UO}_{2}^{2+}, \mathrm{PuO}_{2}^{2+}, \mathrm{UO}^{+}$, आदि।<br>(d) ऑक्साइड तथा हाइड्रॉक्साइड अधिक क्षारीय हैं।<br> |

### q_4.22 — solution (hi)
- **Confidence:** high
- **Reason:** A direct 250dpi render of solutions.hi.pdf page 14 shows the source prints '2CrO4^{2-}' with a small '(+6)' oxidation-state label positioned above it, exactly matching the adjacent example (i)'s own stackrel(+7)/(+4) style. mathpix merged the two annotations into one garbled superscript '+62-' during extraction. Corrected to the same stackrel style already used correctly one line above in this same item.
- **Found:**
  > असमानुपातन अभिक्रिया में, एक ही पदार्थ (तत्व) का ऑक्सीकरण (ऑक्सीकरण संख्या बढ़ना) तथा अपचयन (ऑक्सीकण संख्या घटना) दोनों होते है जिसके परिणामस्वरूप दो विभिन्न उत्पाद बनते हैं। दूसरे शब्दों में, एक ही पदार्थ किसी एक अणु के लिए ऑक्सीकारक का कार्य करता है तथा उसी समय वह दूसरे अणु के लिए अपचायक का कार्य करता हैं।
  > 
  > उदाहरण
  > 
  > (i) $3 \mathrm{MnO}_{4}^{2-}+4 \mathrm{H}^{+} \longrightarrow \stackrel{(+7)}{2 \mathrm{MnO}_{4}^{-}}+\stackrel{(+4)}{\mathrm{MnO}_{2}}+2 \mathrm{H}_{2} \mathrm{O}$
  > (ii) $3 \mathrm{CrO}_{4}^{3-}+8 \mathrm{H}^{+} \longrightarrow 2 \mathrm{CrO}_{4}^{+62-}+\mathrm{Cr}^{3+}+4 \mathrm{H}_{2} \mathrm{O}$
  > विशेष छात्र पिछले एकक से सबंधित उदाहरण भी दे सकते है।
  >     (i) $4 \mathrm{H}_{3} \mathrm{PO}_{3} \longrightarrow 3 \mathrm{H}_{3} \mathrm{PO}_{4}+\mathrm{PH}_{3}$
  >     (ii) $3 \mathrm{HNO}_{2} \longrightarrow \mathrm{HNO}_{3}+\mathrm{H}_{2} \mathrm{O}+2 \mathrm{NO}$
- **Should be:**
  > असमानुपातन अभिक्रिया में, एक ही पदार्थ (तत्व) का ऑक्सीकरण (ऑक्सीकरण संख्या बढ़ना) तथा अपचयन (ऑक्सीकण संख्या घटना) दोनों होते है जिसके परिणामस्वरूप दो विभिन्न उत्पाद बनते हैं। दूसरे शब्दों में, एक ही पदार्थ किसी एक अणु के लिए ऑक्सीकारक का कार्य करता है तथा उसी समय वह दूसरे अणु के लिए अपचायक का कार्य करता हैं।
  > 
  > उदाहरण
  > 
  > (i) $3 \mathrm{MnO}_{4}^{2-}+4 \mathrm{H}^{+} \longrightarrow \stackrel{(+7)}{2 \mathrm{MnO}_{4}^{-}}+\stackrel{(+4)}{\mathrm{MnO}_{2}}+2 \mathrm{H}_{2} \mathrm{O}$
  > (ii) $3 \mathrm{CrO}_{4}^{3-}+8 \mathrm{H}^{+} \longrightarrow \stackrel{(+6)}{2 \mathrm{CrO}_{4}^{2-}}+\mathrm{Cr}^{3+}+4 \mathrm{H}_{2} \mathrm{O}$
  > विशेष छात्र पिछले एकक से सबंधित उदाहरण भी दे सकते है।
  >     (i) $4 \mathrm{H}_{3} \mathrm{PO}_{3} \longrightarrow 3 \mathrm{H}_{3} \mathrm{PO}_{4}+\mathrm{PH}_{3}$
  >     (ii) $3 \mathrm{HNO}_{2} \longrightarrow \mathrm{HNO}_{3}+\mathrm{H}_{2} \mathrm{O}+2 \mathrm{NO}$
