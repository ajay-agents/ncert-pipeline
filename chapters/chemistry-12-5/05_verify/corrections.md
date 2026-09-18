### ex_5.2 — question (hi)
- **Confidence:** high
- **Reason:** OCR substituted the letter "O" (with added spaces) for the digit "0" denoting zero oxidation state; PDF page 126 (उदाहरण 5.2, part v) clearly shows "(0)" set tight with no internal spaces.
- **Found:**
  > टेट्राकार्बोनिलनिकल( O )
- **Should be:**
  > टेट्राकार्बोनिलनिकल(0)

### it_5.1 — question (hi)
- **Confidence:** high
- **Reason:** OCR corrupted the word "प्लैटिनम" into a per-character superscript math fragment instead of plain text; chapter PDF page (ch_08) shows it as an ordinary word.
- **Found:**
  > ${ }^{प ् ल ै ट ि न म}$
- **Should be:**
  > प्लैटिनम

### it_5.1 — solution (hi)
- **Confidence:** high
- **Reason:** OCR misread "कोबाल्ट" (cobalt) as the non-word "कोबात्ट"; solutions-manual page (sol_01) clearly shows "कोबाल्ट".
- **Found:**
  > टेट्राऐमीनडाइएक्वा कोबात्ट (III) क्लोराइड
- **Should be:**
  > टेट्राऐमीनडाइएक्वा कोबाल्ट (III) क्लोराइड

### it_5.2 — solution (hi)
- **Confidence:** high
- **Reason:** OCR misread the vowel sign in "पैलेडेट" (palladate) as "पेलेडेट"; solutions-manual page (sol_03) clearly shows "पैलेडेट" (ऐ matra) when zoomed in.
- **Found:**
  > पोटैशियमटेट्राक्लोरोडोपेलेडेट (II)
- **Should be:**
  > पोटैशियमटेट्राक्लोरोडोपैलेडेट (II)

### it_5.5 — solution (hi)
- **Confidence:** high
- **Reason:** Recurring OCR pattern in this chapter: the "3d" subshell notation misread as digit sequence "30". The solutions-manual page (sol_06) shows this exact sentence twice, both times as "3d^8 4s^2" — the second occurrence was corrupted to "30^8 4s^2" during extraction.
- **Found:**
  > ${ }_{28} \mathrm{Ni}$ परमाणु का बाहरी विन्यास $=30^{8} 4 s^{2}$
- **Should be:**
  > ${ }_{28} \mathrm{Ni}$ परमाणु का बाहरी विन्यास $=3 d^{8} 4 s^{2}$

### it_5.7 — solution (hi)
- **Confidence:** high
- **Reason:** OCR misread "अयुग्मित" (unpaired) as the non-word "अयुम्मित"; solutions-manual page (sol_08) clearly shows "अयुग्मित".
- **Found:**
  > एक इलेक्ट्रॉन अयुम्मित रहता है।
- **Should be:**
  > एक इलेक्ट्रॉन अयुग्मित रहता है।

### it_5.8 — solution (hi)
- **Confidence:** high
- **Reason:** OCR dropped a syllable, misreading "युग्मित" (paired) as "युमित"; solutions-manual page (sol_08) clearly shows "युग्मित".
- **Found:**
  > इलेक्ट्रॉन युमित हो जाते हैं।
- **Should be:**
  > इलेक्ट्रॉन युग्मित हो जाते हैं।

### it_5.8 — solution (hi)
- **Confidence:** high
- **Reason:** OCR/formula rendering corrupted the complex ion formula "[Ni(NH3)6]2+" — the opening parenthesis before NH3 was dropped and the LaTeX delimiters (\left[ ... \right)) no longer match, producing a malformed expression. Solutions-manual page (sol_09) shows the plain formula "[Ni(NH3)6]2+".
- **Found:**
  > $\left.\left[\mathrm{NiNH}_{3}\right)_{6}\right]^{2+}$
- **Should be:**
  > $\left[\mathrm{Ni}\left(\mathrm{NH}_{3}\right)_{6}\right]^{2+}$

### it_5.9 — solution (hi)
- **Confidence:** high
- **Reason:** OCR dropped a conjunct, misreading "कक्षकों" (orbitals) as "कसकों"; solutions-manual page (sol_09) clearly shows "कक्षकों".
- **Found:**
  > $5 d$ कसकों में इलेक्ट्रॉनों के युग्मन
- **Should be:**
  > $5 d$ कक्षकों में इलेक्ट्रॉनों के युग्मन

### q_5.1 — solution (hi)
- **Confidence:** high
- **Reason:** OCR substituted the long vocalic-RR vowel (ॠ) for the correct short vocalic-R (ऋ) in "ऋणात्मक" (the same word is spelled correctly two lines later in the same solution).
- **Found:**
  > ॠणात्मक
- **Should be:**
  > ऋणात्मक

### q_5.1 — solution (hi)
- **Confidence:** high
- **Reason:** OCR garbled "अन-आयननीय" (non-ionizable) into the meaningless "अन्कआयननीय".
- **Found:**
  > अन्कआयननीय
- **Should be:**
  > अन-आयननीय

### q_5.1 — solution (hi)
- **Confidence:** high
- **Reason:** OCR dropped a character, turning "विभिन्न" (various) into the meaningless "विमिन्न".
- **Found:**
  > विमिन्न
- **Should be:**
  > विभिन्न

### q_5.3 — solution (hi)
- **Confidence:** high
- **Reason:** OCR dropped a conjunct, turning "समन्वय सत्ता" (coordination entity) into the meaningless "समन्वय सता" — the same term is spelled correctly twice later in the same sentence.
- **Found:**
  > समन्वय सता
- **Should be:**
  > समन्वय सत्ता

### q_5.3 — solution (hi)
- **Confidence:** high
- **Reason:** OCR garbled "द्विदंतुर" (bidentate) into the meaningless "द्विंदुर" when introducing definition (b); the same word is spelled correctly ("द्विदंतुर लिगेण्ड") later in this same solution.
- **Found:**
  > (b) द्विंदुर दो दाता
- **Should be:**
  > (b) द्विदंतुर दो दाता

### q_5.5 — solution (hi)
- **Confidence:** high
- **Reason:** In the oxidation-number equation for [Cr(NH3)3Cl3], the solutions-manual page shows "x + (3 × 0) + (3 × −1) = 0", parallel to the "(3 × 0)" term just before it. OCR read the "×" as a literal "x" and merged it with "−1", producing the nonsensical "(3 x-1)".
- **Found:**
  > x+(3 \times 0)+(3 x-1) & =0 \\
- **Should be:**
  > x+(3 \times 0)+(3 \times(-1)) & =0 \\

### q_5.7 — solution (hi)
- **Confidence:** high
- **Reason:** The solutions-manual page (page 17) lists items (ii)–(viii) as one compound name followed by its "(II)/(III) क्लोराइड/आयन" qualifier on the same line. Extraction split each qualifier onto its own line and shuffled/duplicated them (one qualifier line is even garbled into Bengali script, "(II) ক্লাराइड"), so every compound from (ii) through (viii) has lost or been given the wrong qualifier. Item (i) and (ix), which were not affected, are left unchanged.
- **Found:**
  > (ii) डाइऐमीनक्लोरोडो (मिथाइल ऐमीन) प्लेटिनम
  > (II) क्लोराइड
  > (II) आयन
  > (II) आयन
  > (II) ক্লাराइड
  > (iii) हेक्साएक्वाटाइटेनियम
  > (III) आयन
  > (III) क्लोराइड
  > (III) आयन
  > (iv) टेट्राऐमीनक्लोरोडोनाइट्राइटो-N-कोबाल्ट
  > (v) हेक्साएक्वामैंगनीज
  > (vi) टेट्राक्लोरोडोनिकैलेट
  > (vii) हेक्साऐमीननिकैल
  > (viii) ट्रिस(एथेन-1, 2-डाइऐमीन) कोबाल्ट
- **Should be:**
  > (ii) डाइऐमीनक्लोरोडो (मिथाइल ऐमीन) प्लेटिनम (II) क्लोराइड
  > (iii) हेक्साएक्वाटाइटेनियम (III) आयन
  > (iv) टेट्राऐमीनक्लोरोडोनाइट्राइटो-N-कोबाल्ट (III) क्लोराइड
  > (v) हेक्साएक्वामैंगनीज (II) आयन
  > (vi) टेट्राक्लोरोडोनिकैलेट (II) आयन
  > (vii) हेक्साऐमीननिकैल (II) क्लोराइड
  > (viii) ट्रिस(एथेन-1, 2-डाइऐमीन) कोबाल्ट (III) आयन

### q_5.8 — solution (hi)
- **Confidence:** high
- **Reason:** OCR substituted "घ" for "ध" in "बंधनी समावयवता" (linkage isomerism), in the overview list of isomerism types.
- **Found:**
  > 1. संरचनात्मक समावयवता
  > (a) बंघनी समावयवता
- **Should be:**
  > 1. संरचनात्मक समावयवता
  > (a) बंधनी समावयवता

### q_5.8 — solution (hi)
- **Confidence:** high
- **Reason:** Same "घ"/"ध" OCR substitution recurs where this term is used again to head the worked examples.
- **Found:**
  > 1. (a) बंघनी समावयवता
- **Should be:**
  > 1. (a) बंधनी समावयवता

### q_5.8 — solution (hi)
- **Confidence:** high
- **Reason:** The solutions-manual page labels the two optical-isomer forms of [Co(en)3]3+ as "(d)" and "(l)" (matching the "दक्षिणावर्त (d–)" / "वामावर्त (l–)" captions on the accompanying diagram). OCR misread the italic "d" as "O" and lost the "l" entirely, leaving a dangling, empty math delimiter.
- **Found:**
  > के दो रूप दक्षिणावर्त ( O ) और वामावर्त ( $)$ हैं।
- **Should be:**
  > के दो रूप दक्षिणावर्त ($d$) और वामावर्त ($l$) हैं।

### q_5.10 — solution (hi)
- **Confidence:** high
- **Reason:** OCR dropped the subscript 3 on (C2O4); the PDF (and the item's own mirror-image diagram, which shows three C2O4 groups) confirms [Cr(C2O4)3]3-
- **Found:**
  > $\left[\mathrm{Cr}\left(\mathrm{C}_{2} \mathrm{O}_{4}\right)\right]^{3-}$
- **Should be:**
  > $\left[\mathrm{Cr}\left(\mathrm{C}_{2} \mathrm{O}_{4}\right)_{3}\right]^{3-}$

### q_5.10 — solution (hi)
- **Confidence:** high
- **Reason:** OCR garbled the bracket/subscript structure of part (ii)'s formula; the PDF clearly prints "Cis-[PtCl2(en)2]2+" with the 2 as a subscript on the closed (en) group, not inside it
- **Found:**
  > $\mathbf{C i s}-\left[\mathbf{P t C l}_{\mathbf{2}}\left(\mathbf{e n}_{\mathbf{2}}\right]^{\mathbf{2}+}\right.$
- **Should be:**
  > $\mathbf{C i s}-\left[\mathbf{P t C l}_{\mathbf{2}}\left(\mathbf{e n}\right)_{\mathbf{2}}\right]^{\mathbf{2}+}$

### q_5.13 — solution (hi)
- **Confidence:** high
- **Reason:** OCR dropped the क्ष conjunct — "अवशेप" is not a word; the PDF reads "हरा अवक्षेप" (green precipitate) under reaction (i)
- **Found:**
  > हरा अवशेप
- **Should be:**
  > हरा अवक्षेप

### q_5.14 — solution (hi)
- **Confidence:** high
- **Reason:** OCR confused त्व with त्य; the PDF reads "स्थायित्व स्थिरांक" (stability constant), the standard term, not "स्थायित्य"
- **Found:**
  > स्थायित्य स्थिरांक
- **Should be:**
  > स्थायित्व स्थिरांक

### q_5.15 — solution (hi)
- **Confidence:** high
- **Reason:** OCR garbled part (i)'s formula and mis-nested the brackets; the PDF clearly prints [Fe(CN)6]4- (six CN ligands, matching the same solution's own later hexacyanoferrate diagram)
- **Found:**
  > $\left[\mathrm{Fe}\left(\mathrm{CN}_{2}\right]^{4-}\right.$
- **Should be:**
  > $\left[\mathrm{Fe}(\mathrm{CN})_{6}\right]^{4-}$

### q_5.15 — solution (hi)
- **Confidence:** high
- **Reason:** the recurring "3d" subshell notation misread as digits "30" — the PDF clearly prints Co3+ = 3d6 4s0 (matching the electron configuration given one line above and part (iv)'s parallel line)
- **Found:**
  > \mathrm{Co}^{3+}=30^{6} 4 s^{0}
- **Should be:**
  > \mathrm{Co}^{3+}=3 d^{6} 4 s^{0}

### q_5.15 — solution (hi)
- **Confidence:** high
- **Reason:** OCR misread ग् as म् — "युम्मित" is not a word; the PDF reads "युग्मित" (paired), consistent with every other use of this word in the same solution
- **Found:**
  > युम्मित कर देता है
- **Should be:**
  > युग्मित कर देता है

### q_5.15 — solution (hi)
- **Confidence:** high
- **Reason:** OCR confused ध with घ — "आबंघन" is not a word; the PDF reads "आबंधन" (bonding), consistent with the same solution's own correctly-spelled instance later ("nd-कक्षक आबंधन में भाग ले रही हैं")
- **Found:**
  > होगा तथा आबंघन में
- **Should be:**
  > होगा तथा आबंधन में

### q_5.15 — solution (hi)
- **Confidence:** high
- **Reason:** two OCR errors in one clause — "आबंघन" should be "आबंधन" (bonding), and "कसक" should be "कक्षक" (orbital); the PDF reads "इसके आबंधन में nd-कक्षक के भाग लेने के कारण"
- **Found:**
  > इसके आबंघन में $n d$-कसक के भाग लेने के कारण
- **Should be:**
  > इसके आबंधन में $n d$-कक्षक के भाग लेने के कारण

### q_5.15 — solution (hi)
- **Confidence:** high
- **Reason:** OCR confused ध with घ — "आबंघन" is not a word; the PDF reads "आबंधन" (bonding)
- **Found:**
  > इसके आबंघन में $(n-1) d$-कक्षक भाग लेते है।
- **Should be:**
  > इसके आबंधन में $(n-1) d$-कक्षक भाग लेते है।

### q_5.17 — solution (hi)
- **Confidence:** high
- **Reason:** missing superscript minus charge on F in the spectrochemical series (all other anions in the list carry the ⁻ superscript in the source)
- **Found:**
  > <\mathrm{Cl}^{-}<\mathrm{F}<\mathrm{OH}^{-}
- **Should be:**
  > <\mathrm{Cl}^{-}<\mathrm{F}^{-}<\mathrm{OH}^{-}

### q_5.17 — solution (hi)
- **Confidence:** high
- **Reason:** OCR garbled the caption under the spectrochemical series formula
- **Found:**
  > स्पेक्टूमी रासायनिक श्रेणी
- **Should be:**
  > स्पेक्ट्रमी रासायनिक श्रेणी

### q_5.17 — solution (hi)
- **Confidence:** high
- **Reason:** OCR typo, "लिग्रेण्डों" is not a word; source reads "लिगेण्डों" (ligands)
- **Found:**
  > इस प्रकार के लिग्रेण्डों के लिए
- **Should be:**
  > इस प्रकार के लिगेण्डों के लिए

### q_5.17 — solution (hi)
- **Confidence:** high
- **Reason:** stray nukta; source reads "जहाँ" (where), not "ज़हाँ"
- **Found:**
  > ज़हाँ $P$ युग्मन ऊर्जा है
- **Should be:**
  > जहाँ $P$ युग्मन ऊर्जा है

### q_5.18 — solution (hi)
- **Confidence:** high
- **Reason:** OCR typo, "कस्सकों" is not a word; source reads "कक्षकों" (orbitals)
- **Found:**
  > $d$-कस्सकों का विपाटन
- **Should be:**
  > $d$-कक्षकों का विपाटन

### q_5.19 — solution (hi)
- **Confidence:** medium
- **Reason:** the glyph at this exact spot in the source scan is illegible/garbled, but the identical quantity (Ni²⁺ configuration) is printed clearly and unambiguously as 3d⁸ elsewhere in the same solutions manual (the very next solution, Q20, restates "Ni²⁺ = [Ar] 3d⁸")
- **Found:**
  > \mathrm{Ni}^{2+} & =[\mathrm{Ar}] 3 c^{,^{3}}
- **Should be:**
  > \mathrm{Ni}^{2+} & =[\mathrm{Ar}] 3 d^{8}

### q_5.19 — solution (hi)
- **Confidence:** high
- **Reason:** recurring OCR pattern — "3d" (the 3d-subshell notation) misread as the digit sequence "30"
- **Found:**
  > 30-कक्षकों में इलेक्ट्रॉनों को युग्मित
- **Should be:**
  > $3 d$-कक्षकों में इलेक्ट्रॉनों को युग्मित

### q_5.20 — solution (hi)
- **Confidence:** high
- **Reason:** another instance of "3d" mis-OCR'd (here as "अग"), plus "युम्मित" is not a word — source reads "युग्मित" (paired)
- **Found:**
  > अग-कक्षकों में उपस्थित दो अयुग्मित इलेक्ट्रॉन, युम्मित हो जाते हैं
- **Should be:**
  > 3d-कक्षकों में उपस्थित दो अयुग्मित इलेक्ट्रॉन, युग्मित हो जाते हैं

### q_5.22 — solution (hi)
- **Confidence:** high
- **Reason:** the sigma symbol (σ) was OCR'd as "o", making "M–Cσ" (the M–C sigma bond) read as "M-Co" (which looks like the element symbol for cobalt); also "कार्बोनिल" (carbonyl) was misread as "कार्बोनित"
- **Found:**
  > $M-\mathrm{Co}$ आंबंध कार्बोनित समूह के कार्बन पर उपस्थित इलेक्ट्रॉन युग्म को धातु के रिक्त कक्षक में दान करने से बनता है।
- **Should be:**
  > $M-C\sigma$ आबंध कार्बोनिल समूह के कार्बन पर उपस्थित इलेक्ट्रॉन युग्म को धातु के रिक्त कक्षक में दान करने से बनता है।

### q_5.22 — solution (hi)
- **Confidence:** high
- **Reason:** OCR typo, "आबंघ" is not a word; source reads "आबंध" (bond)
- **Found:**
  > धातु से लिगेण्ड का आबंघ एक सहक्रियाशीलता
- **Should be:**
  > धातु से लिगेण्ड का आबंध एक सहक्रियाशीलता

### q_5.23 — solution (hi)
- **Confidence:** high
- **Reason:** OCR typo, "अवस्या" is not a word; source reads "अवस्था" (oxidation state)
- **Found:**
  > माना Co की ऑक्सीकरण अवस्या $x$ है।
- **Should be:**
  > माना Co की ऑक्सीकरण अवस्था $x$ है।

### q_5.23 — solution (hi)
- **Confidence:** high
- **Reason:** same OCR typo repeated ("अवस्या" for "अवस्था")
- **Found:**
  > अत: Co की ऑक्सीकरण अवस्या $+2$ है।
- **Should be:**
  > अत: Co की ऑक्सीकरण अवस्था $+2$ है।

### q_5.23 — solution (hi)
- **Confidence:** high
- **Reason:** same OCR typo repeated ("अवस्या" for "अवस्था")
- **Found:**
  > माना Cr की ऑक्सीकरण अवस्या $x$ है।
- **Should be:**
  > माना Cr की ऑक्सीकरण अवस्था $x$ है।

### q_5.23 — solution (hi)
- **Confidence:** high
- **Reason:** same OCR typo repeated ("अवस्या" for "अवस्था")
- **Found:**
  > माना Mn की ऑक्सीकरण अवस्या $x$ है।
- **Should be:**
  > माना Mn की ऑक्सीकरण अवस्था $x$ है।

### q_5.23 — solution (hi)
- **Confidence:** high
- **Reason:** same OCR typo repeated ("अवस्या" for "अवस्था")
- **Found:**
  > अत: Mn की ऑक्सीकरण अवस्या $+2$ है।
- **Should be:**
  > अत: Mn की ऑक्सीकरण अवस्था $+2$ है।

### q_5.24 — solution (hi)
- **Confidence:** medium
- **Reason:** the source scan is smudged at this exact word; the compound is a di-oxalato complex, and the surrounding letters point to "ऑक्सेलेटो" rather than "थॉक्सेलेटो"
- **Found:**
  > IUPAC नाम पोटैशियमडाइएक्वाडाइथॉक्सेलेटोक्रोमेट (III) हाइड्रेट
- **Should be:**
  > IUPAC नाम पोटैशियमडाइएक्वाडाइऑक्सेलेटोक्रोमेट (III) हाइड्रेट

### q_5.24 — solution (hi)
- **Confidence:** high
- **Reason:** three OCR typos in one line: "समपस" for "समपक्ष" (cis), the italic "l" of "l-रूप" misread as a slash, and "धुवण" for "ध्रुवण" (polarization)
- **Found:**
  > समपस रूप $d$-तथा /-रूप भी दर्शाता है (अर्थात् धुवण समावयवता)
- **Should be:**
  > समपक्ष रूप $d$-तथा $l$-रूप भी दर्शाता है (अर्थात् ध्रुवण समावयवता)

### q_5.24 — solution (hi)
- **Confidence:** high
- **Reason:** recurring OCR pattern — "3d" misread as "30"
- **Found:**
  > $\mathrm{Cr}^{3+}$ का बाह्य इलेक्ट्रॉनिक विन्यास $=30^{3}\left(t_{2 g}^{3} e_{g}^{0}\right)$
- **Should be:**
  > $\mathrm{Cr}^{3+}$ का बाह्य इलेक्ट्रॉनिक विन्यास $=3 d^{3}\left(t_{2 g}^{3} e_{g}^{0}\right)$

### q_5.24 — solution (hi)
- **Confidence:** high
- **Reason:** recurring OCR pattern — "3d" misread as "30" — plus the "$e_g^2$" term was garbled into a stray "g" during OCR
- **Found:**
  > Fe का बाह्य इलेक्ट्रॉनिक विन्यास $=30^{5}\left(t_{2 g}^{3} \mathrm{~g}{ }_{g}^{2}\right)$
- **Should be:**
  > Fe का बाह्य इलेक्ट्रॉनिक विन्यास $=3 d^{5}\left(t_{2 g}^{3} e_{g}^{2}\right)$

### q_5.24 — solution (hi)
- **Confidence:** high
- **Reason:** OCR typo, "दुम्बकीय" is not a word; source reads "चुम्बकीय" (magnetic)
- **Found:**
  > ∴ दुम्बकीय आघूर्ण $\mu=\sqrt{n(n+2)}$ BM
- **Should be:**
  > ∴ चुम्बकीय आघूर्ण $\mu=\sqrt{n(n+2)}$ BM

### q_5.24 — solution (hi)
- **Confidence:** high
- **Reason:** the "g" subscript of $t_{2g}$ was split off from its base by OCR, garbling the term notation
- **Found:**
  > Mn का बाह्य इलेक्ट्रॉनिक विन्यास $=3 d^{5}\left[t_{2}^{5} \mathrm{~g} e_{g}^{0}\right]$
- **Should be:**
  > Mn का बाह्य इलेक्ट्रॉनिक विन्यास $=3 d^{5}\left[t_{2 g}^{5} e_{g}^{0}\right]$

### q_5.26 — solution (hi)
- **Confidence:** high
- **Reason:** OCR corrupted the technical term "bidentate" (द्विदंतुर) into a non-word
- **Found:**
  > द्विंदुर
- **Should be:**
  > द्विदंतुर

### q_5.26 — solution (hi)
- **Confidence:** high
- **Reason:** OCR letter confusion (घ for ध) turns "bonding" (आबंधन) into a non-word
- **Found:**
  > आबंघन
- **Should be:**
  > आबंधन

### q_5.26 — solution (hi)
- **Confidence:** high
- **Reason:** OCR inserted an extra matra, turning "manner" (प्रकार) into a non-word
- **Found:**
  > प्रेकार
- **Should be:**
  > प्रकार

### q_5.27 — solution (hi)
- **Confidence:** high
- **Reason:** OCR misread "भूमिका" (role) as "मूमिका" (not a word)
- **Found:**
  > जैव प्रणालियों में उपसहसंयोजन यौगिकों की मूमिका
- **Should be:**
  > जैव प्रणालियों में उपसहसंयोजन यौगिकों की भूमिका

### q_5.27 — solution (hi)
- **Confidence:** high
- **Reason:** OCR misread "कोबाल्ट" (cobalt) as "कोबात्ट" (not a word)
- **Found:**
  > कोबात्ट का एक उपसहसंयोजक यौगिक है।
- **Should be:**
  > कोबाल्ट का एक उपसहसंयोजक यौगिक है।

### q_5.27 — solution (hi)
- **Confidence:** high
- **Reason:** OCR misread "औषध" (medicinal) as "औषघ", and "भूमिका" (role) as "मूमिका"
- **Found:**
  > औषघ रसायन में उपसहसंयोजक यौगिकों की मूमिका
- **Should be:**
  > औषध रसायन में उपसहसंयोजक यौगिकों की भूमिका

### q_5.27 — solution (hi)
- **Confidence:** high
- **Reason:** OCR misread "प्रभावी" (effective) as "प्रमावी" (not a word)
- **Found:**
  > ट्यूमर वृद्धि को प्रमावी रूप से रोकने
- **Should be:**
  > ट्यूमर वृद्धि को प्रभावी रूप से रोकने

### q_5.27 — solution (hi)
- **Confidence:** medium
- **Reason:** OCR added a spurious anusvara to "बाहर" (out)
- **Found:**
  > मूत्र के साथ बाहरं आ जाता है।
- **Should be:**
  > मूत्र के साथ बाहर आ जाता है।

### q_5.27 — solution (hi)
- **Confidence:** high
- **Reason:** OCR misread "जीव-जन्तु" (living organisms) as "जीक्जन्तु" (not a word)
- **Found:**
  > जीक्जन्तु निकायों में कॉपर
- **Should be:**
  > जीव-जन्तु निकायों में कॉपर

### q_5.27 — solution (hi)
- **Confidence:** high
- **Reason:** OCR corrupted "ग्लाइऑक्सिम" (glyoxime) into a stray superscript "7" plus a truncated fragment
- **Found:**
  > डाइमेथिल ${ }^{7}$ लाइऑक्सिम के बनने से
- **Should be:**
  > डाइमेथिल ग्लाइऑक्सिम के बनने से

### q_5.27 — solution (hi)
- **Confidence:** high
- **Reason:** OCR misread the "bis dimethylglyoxime" label: "बिस" became "विस" and "डाइमेथिल" became "डाइयेथित"
- **Found:**
  > निकल विस डाइयेथित
- **Should be:**
  > निकल बिस डाइमेथिल

### q_5.27 — solution (hi)
- **Confidence:** high
- **Reason:** OCR misread the Roman numeral "I" (qualitative-analysis Group I) as the Devanagari danda "।"
- **Found:**
  > समूह । में
- **Should be:**
  > समूह I में

### q_5.27 — solution (hi)
- **Confidence:** high
- **Reason:** OCR misread "डाइमेथिल" (dimethyl) as "डाइयेथिल" in the compound name "nickel dimethylglyoxime"
- **Found:**
  > निकैल डाइयेथिल ग्लाइऑक्सिम संकुल
- **Should be:**
  > निकैल डाइमेथिल ग्लाइऑक्सिम संकुल

### q_5.27 — solution (hi)
- **Confidence:** high
- **Reason:** OCR misread "भूमिका" (role) as "मूमिका" (not a word)
- **Found:**
  > विश्लेषणात्मक रसायन में उपसहसंयोजक यौगिकों की मूमिका
- **Should be:**
  > विश्लेषणात्मक रसायन में उपसहसंयोजक यौगिकों की भूमिका

### q_5.27 — solution (hi)
- **Confidence:** high
- **Reason:** OCR letter confusion (घ for ध) turns "metallurgy" (धातुकर्म) into a non-word, in the section heading
- **Found:**
  > धातुओं के निष्कर्षण/घातुकर्म में उपसहसंयोजन यौगिकों की भूमिका
- **Should be:**
  > धातुओं के निष्कर्षण/धातुकर्म में उपसहसंयोजन यौगिकों की भूमिका

### q_5.27 — solution (hi)
- **Confidence:** medium
- **Reason:** OCR added a spurious anusvara to "धातुओं" (metals)
- **Found:**
  > विभिन्न धांतुओं की कुछ प्रमुख निष्कर्षण
- **Should be:**
  > विभिन्न धातुओं की कुछ प्रमुख निष्कर्षण

### q_5.27 — solution (hi)
- **Confidence:** high
- **Reason:** OCR misread "सिल्वर" (silver) as "सित्वर" (not a word)
- **Found:**
  > जैसे सित्वर तथा गोल्ड
- **Should be:**
  > जैसे सिल्वर तथा गोल्ड

### q_5.27 — solution (hi)
- **Confidence:** high
- **Reason:** OCR letter confusion (घ for ध) turns "metals" (धातुओं) into a non-word
- **Found:**
  > कुछ घातुओं के शुद्धिकरण में भी
- **Should be:**
  > कुछ धातुओं के शुद्धिकरण में भी

### q_5.27 — solution (hi)
- **Confidence:** medium
- **Reason:** OCR flattened the vowel sign in "मॉन्ड" (Mond, as in the Mond process) to "मोन्ड"
- **Found:**
  > उदाहरण मोन्ड प्रक्रम में
- **Should be:**
  > उदाहरण मॉन्ड प्रक्रम में

### q_5.31 — solution (hi)
- **Confidence:** high
- **Reason:** OCR misread "हालाँकि" (however) as "हालॉकि" (not a word)
- **Found:**
  > हालॉकि संकुल (c) एक कीलेट है
- **Should be:**
  > हालाँकि संकुल (c) एक कीलेट है

### q_5.32 — solution (hi)
- **Confidence:** high
- **Reason:** A spurious "2+" charge was inserted directly on Ni inside the third term of the absorption-order inequality; the source page shows only the overall 4- charge on the whole complex, matching the other two terms in the same line
- **Found:**
  > \left[\mathrm{Ni}^{2+}\left(\mathrm{NO}_{2}\right)_{6}\right]^{4-}
- **Should be:**
  > \left[\mathrm{Ni}\left(\mathrm{NO}_{2}\right)_{6}\right]^{4-}

### q_5.8 — solution (hi)
- **Confidence:** high
- **Reason:** The classification list self-contradicts (group 2's lettering jumps (b)->(d), skipping (c)) because solutions.hi.pdf page 17 prints this as a two-column table and (d) sits at a 4th-row/column-2 position purely for layout reasons, not as a genuine third item of group 2 - confirmed by direct 200dpi render and by this same item's own worked-examples list two lines below, which already correctly places (d) under group 1. Moved (d) to group 1, right after (c), matching the worked-example list, the textbook's own conceptual grouping, and solutions.hi.pdf's own worked-example page (page 18).
- **Found:**
  > उपसहसंयोजक यौगिकों में समावयवता मुख्यतः दो प्रकार की होती है।
  > 
  > 1. संरचनात्मक समावयवता
  > (a) बंधनी समावयवता
  > (b) उपसहसंयोजन समावयवता
  > (c) आयनन समावयवता
  > 2. त्रिविम समावयवता
  > (a) ज्यामितीय समावयवता
  > (b) ध्रुवण समावयवता
  > (d) विलायकयोजन समावयवता
  > 
  > उदाहरण
  > 
  > 1. (a) बंधनी समावयवता
  >     (i) $\left[\mathrm{Co}\left(\mathrm{NH}_{3}\right)_{5} \mathrm{NO}_{2}\right] \mathrm{Cl}_{2}$ तथा $\left[\mathrm{Co}\left(\mathrm{NH}_{3}\right)_{5} \mathrm{ONO}\right] \mathrm{Cl}_{2}$
  >     (ii) $\left[\mathrm{Mn}(\mathrm{CO})_{5} \mathrm{SCN}\right]$ तथा $\left[\mathrm{Mn}(\mathrm{CO})_{5} \mathrm{NCS}\right]$
  >     (b) उपसहसंयोजन समावयवता
  >     (i) $\left[\mathrm{Co}\left(\mathrm{NH}_{3}\right)_{6}\right]\left[\mathrm{Cr}(\mathrm{CN})_{6}\right]$ तथा $\left[\mathrm{Cr}\left(\mathrm{NH}_{3}\right)_{6}\right]\left[\mathrm{Co}(\mathrm{CN})_{6}\right]$
  >     (c) आयनन समावयवता
  >         (i) $\left[\mathrm{Co}\left(\mathrm{NH}_{3}\right)_{5} \mathrm{SO}_{4}\right] \mathrm{Br}$ तथा $\left[\mathrm{Co}\left(\mathrm{NH}_{3}\right)_{5} \mathrm{Br}\right] \mathrm{SO}_{4}$
  >     (d) विलायकयोजन समावयवता
  >     (i) $\left[\mathrm{Cr}\left(\mathrm{H}_{2} \mathrm{O}\right)_{6}\right] \mathrm{Cl}_{3}$ (बैंगनी) तथा $\left[\mathrm{Cr}\left(\mathrm{H}_{2} \mathrm{O}\right)_{5} \mathrm{Cl}\right] \mathrm{Cl}_{2} \cdot \mathrm{H}_{2} \mathrm{O}$ (स्लेटी हरा)
  > 2. (a) ज्यामितीय समावयवता
  >     (i) $\left[\mathrm{CoCl}_{2}(\mathrm{en})_{2}\right]$ के समपक्ष तथा विपक्ष समावयव
  > 
  >     (b)ध्रुवण समावयवता
  > (i) $\left[\mathrm{Co}(\mathrm{en})_{3}\right]^{3+}$ के दो रूप दक्षिणावर्त ($d$) और वामावर्त ($l$) हैं।
  > 
  > विपक्ष रूप
  > 
  > 
  > दर्पण
- **Should be:**
  > उपसहसंयोजक यौगिकों में समावयवता मुख्यतः दो प्रकार की होती है।
  > 
  > 1. संरचनात्मक समावयवता
  > (a) बंधनी समावयवता
  > (b) उपसहसंयोजन समावयवता
  > (c) आयनन समावयवता
  > (d) विलायकयोजन समावयवता
  > 2. त्रिविम समावयवता
  > (a) ज्यामितीय समावयवता
  > (b) ध्रुवण समावयवता
  > 
  > उदाहरण
  > 
  > 1. (a) बंधनी समावयवता
  >     (i) $\left[\mathrm{Co}\left(\mathrm{NH}_{3}\right)_{5} \mathrm{NO}_{2}\right] \mathrm{Cl}_{2}$ तथा $\left[\mathrm{Co}\left(\mathrm{NH}_{3}\right)_{5} \mathrm{ONO}\right] \mathrm{Cl}_{2}$
  >     (ii) $\left[\mathrm{Mn}(\mathrm{CO})_{5} \mathrm{SCN}\right]$ तथा $\left[\mathrm{Mn}(\mathrm{CO})_{5} \mathrm{NCS}\right]$
  >     (b) उपसहसंयोजन समावयवता
  >     (i) $\left[\mathrm{Co}\left(\mathrm{NH}_{3}\right)_{6}\right]\left[\mathrm{Cr}(\mathrm{CN})_{6}\right]$ तथा $\left[\mathrm{Cr}\left(\mathrm{NH}_{3}\right)_{6}\right]\left[\mathrm{Co}(\mathrm{CN})_{6}\right]$
  >     (c) आयनन समावयवता
  >         (i) $\left[\mathrm{Co}\left(\mathrm{NH}_{3}\right)_{5} \mathrm{SO}_{4}\right] \mathrm{Br}$ तथा $\left[\mathrm{Co}\left(\mathrm{NH}_{3}\right)_{5} \mathrm{Br}\right] \mathrm{SO}_{4}$
  >     (d) विलायकयोजन समावयवता
  >     (i) $\left[\mathrm{Cr}\left(\mathrm{H}_{2} \mathrm{O}\right)_{6}\right] \mathrm{Cl}_{3}$ (बैंगनी) तथा $\left[\mathrm{Cr}\left(\mathrm{H}_{2} \mathrm{O}\right)_{5} \mathrm{Cl}\right] \mathrm{Cl}_{2} \cdot \mathrm{H}_{2} \mathrm{O}$ (स्लेटी हरा)
  > 2. (a) ज्यामितीय समावयवता
  >     (i) $\left[\mathrm{CoCl}_{2}(\mathrm{en})_{2}\right]$ के समपक्ष तथा विपक्ष समावयव
  > 
  >     (b)ध्रुवण समावयवता
  > (i) $\left[\mathrm{Co}(\mathrm{en})_{3}\right]^{3+}$ के दो रूप दक्षिणावर्त ($d$) और वामावर्त ($l$) हैं।
  > 
  > विपक्ष रूप
  > 
  > 
  > दर्पण
