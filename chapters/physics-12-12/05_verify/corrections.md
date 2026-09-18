### ex_12.4 — solution (hi)
- **Confidence:** high
- **Reason:** Same-page self-contradiction, confirmed against chapter.hi.pdf page 298 (उदाहरण 12.4): the prose states the electron's speed as 2.2x10^-6 m/s, but the very next line's own formula uses v=2.2x10^6 m/s (positive exponent) to compute the frequency, and this value correctly matches example 12.3's own derived speed on the previous page. Printer typo (missing/extra minus sign) in the source textbook itself, not an OCR artifact -- fixing the prose to match the value actually used in the calculation, per CLAUDE.md's recurring same-page self-contradiction guidance (flagged, standing user approval each time).
- **Found:**
  > त्रिज्या की कक्षा में परिक्रामी इलेक्ट्रॉन का वेग $2.2 \times 10^{-6} \mathrm{~m} / \mathrm{s}$ है
- **Should be:**
  > त्रिज्या की कक्षा में परिक्रामी इलेक्ट्रॉन का वेग $2.2 \times 10^{6} \mathrm{~m} / \mathrm{s}$ है

### q_12.8 — solution (hi)
- **Confidence:** high
- **Reason:** Same-page self-contradiction, confirmed against solutions.hi.pdf page 71 (प्रश्न 9): the derivation directly above computes lambda=993 Angstrom, but the concluding sentence restates it as 933 Angstrom -- a digit-transposition typo in the source solutions manual itself (confirmed present in the actual PDF page image, not an OCR/mathpix artifact). Fixing the concluding restatement to match the value the derivation actually computed, per CLAUDE.md's recurring same-page self-contradiction guidance.
- **Found:**
  > अतः लाइमन श्रेणी में तरंग परास $912 \AA$ से $1216 \AA$ है। अतः लाइमन श्रेणी $933 \AA$ की तरंगदैर्ध्य का प्रकाश उत्सर्जित करेगा।
- **Should be:**
  > अतः लाइमन श्रेणी में तरंग परास $912 \AA$ से $1216 \AA$ है। अतः लाइमन श्रेणी $993 \AA$ की तरंगदैर्ध्य का प्रकाश उत्सर्जित करेगा।

### q_12.9 — solution (hi) [SUPERSEDED — see post-completion round below]
- **Confidence:** high
- **Reason:** Extraction-completeness fix, not a content correction: confirmed against solutions.hi.pdf page 72 that this trailing remark (about an unrelated electron transition n=1->n=3 landing in the Lyman series) IS genuinely printed as part of प्रश्न 10's own solution in the source (not a page-bleed/OCR artifact) -- stage 2 had prematurely omitted it as an apparent non-sequitur. Restoring it verbatim per Rule 5 (nothing invented -- but also nothing of the source silently dropped): it still does not logically follow from the earth-orbital-quantum-number question actually asked, and reads as a genuine authoring error in this (non-official, guide-book-style) solutions manual, which is not stage 5's call to fix -- flagged prominently rather than silently corrected or silently kept dropped.
- **Found:**
  > अतः क्वांटम संख्या $2.6 \times 10^{74}$ बहुत अधिक है।
- **Should be:**
  > अतः क्वांटम संख्या $2.6 \times 10^{74}$ बहुत अधिक है।
  > 
  > अतः इलेक्ट्रॉन $n=1$ से $n=3$ में उदेलित होगा।
  > 
  > $$
  > E_{3}=\frac{-13.6}{3^{2}}=-1.5 \mathrm{eV}
  > $$
  > 
  > अतः यह लाइमन श्रेणी से सम्बन्धित है।
- **Superseded by:** the post-completion round below re-examined this and found it is not a non-sequitur authoring error at all -- it is genuinely प्रश्न 9's (q_12.8's) own continuation, misattached to q_12.9 by a page-break reading-order artifact. Moved back to q_12.8 and used to correct q_12.8's method (see below); removed from q_12.9 entirely.

### q_12.1(a) — solution + answer (hi) [post-completion round]
- **Confidence:** high
- **Reason:** Confirmed against solutions.hi.pdf page 67: the question is a 3-option fill-in-the-blank (अपेक्षाकृत काफ़ी अधिक / भिन्न नहीं / अपेक्षाकृत काफ़ी कम), but the printed answer is "इनमें से कोई नहीं" (none of these) -- not one of the three options offered, a structural self-contradiction within the item itself. Physics: Thomson's model atomic size and Rutherford's model atomic-orbit size are both ~1e-10 m (only the nucleus, ~1e-15 m, is different in Rutherford's model), and the question asks about atomic (not nuclear) size, so the two models are not different at this scale.
- **Found:**
  > इनमें से कोई नहीं
- **Should be:**
  > भिन्न नहीं

### q_12.8 — solution + answer (hi) [post-completion round]
- **Confidence:** high
- **Reason:** Confirmed against solutions.hi.pdf pp.71-72: the source computes lambda=hc/E=993 Angstrom by treating the 12.5 eV impact energy as converting directly into one emitted photon, then separately (a few lines later, printed as the top of page 72, extracted into q_12.9 by the artifact noted above) correctly finds the electron is excited only to n=3 -- two incompatible methods in the same solution reaching different conclusions. Correct physics: excitation energy to n=3 is 13.6(1-1/9)=12.09 eV (within the 12.5 eV budget); to n=4 is 13.6(1-1/16)=12.75 eV (exceeds it, not reachable). So the electron reaches n=3 and can de-excite via three transitions, emitting three lines: 3->1 (1028 Å, Lyman), 3->2 (6581 Å, Balmer), 2->1 (1219 Å, Lyman) -- computed with this chapter's own h=6.63e-34 J-s, c=3e8 m/s for internal consistency with the rest of the manual.
- **Found:**
  > सम्बन्ध का प्रयोग करने पर, $E=\frac{hc}{\lambda}=\frac{6.62\times10^{-34}\times3\times10^{8}}{12.5\times1.6\times10^{-19}}=993\ \text{Å}$। अतः लाइमन श्रेणी में तरंग परास 912 Å से 1216 Å है। अतः लाइमन श्रेणी 993 Å की तरंगदैर्ध्य का प्रकाश उत्सर्जित करेगा।
- **Should be:**
  > (full re-derivation via excitation-energy budget and three-transition cascade — see 07_format/structured.hi.md's q_12.8 for the exact text)

### q_12.9 — मुख्य सूत्र (hi) [post-completion round]
- **Confidence:** high
- **Reason:** Confirmed against solutions.hi.pdf page 71 at 8x zoom: the boxed formula reads n=2(pi)vm/h, omitting r, even though the line directly above (mvr=nh/2pi) and the substitution two lines below (which uses r=1.5e11 m) both correctly include it, and the final answer (n=2.6e74) was already right.
- **Found:**
  > $n=\frac{2 \pi v m}{h}$
- **Should be:**
  > $n=\frac{2 \pi m v r}{h}$

### q_12.4 — solution (hi)
- **Confidence:** high
- **Reason:** Same-page self-contradiction, confirmed against solutions.hi.pdf page 68 (प्रश्न 5): the line states KE = -E = 3.6 eV, but E = -13.6 eV so -E must equal +13.6 eV, not 3.6 -- and the very next line's own PE calculation already uses the correct value (PE = -2KE = -2x13.6 = -27.2 eV), contradicting the 3.6 eV stated for KE one line above. A dropped leading '1' digit typo in the source solutions manual itself (confirmed present in the actual PDF page image, not an OCR/mathpix artifact) -- fixing the KE line to match both the underlying physics and the PE line's own consistent use of 13.6. This item's final_answer field already had the correct 13.6 eV value from stage 2 extraction; only the solution derivation text carried the typo.
- **Found:**
  > (\mathrm{KE})=-E=3.6 \mathrm{eV}
- **Should be:**
  > (\mathrm{KE})=-E=13.6 \mathrm{eV}

### q_12.6 — parts[1].solution (hi)
- **Confidence:** high
- **Reason:** Confirmed against solutions.hi.pdf page 70 (part b, r1 derivation): the printed formula denominator omits the square exponent on the last factor (1.6x10^-19), even though the formula above it (r_n = n^2h^2/(4pi^2 K m e^2)) needs e^2, and the arithmetic only reaches the stated answer (0.53x10^-10 m) when that factor is squared -- confirmed by direct recomputation (with e^1 the result is off by ~24 orders of magnitude; with e^2 it matches exactly). A typesetting omission in the source solutions manual itself (confirmed present in the actual PDF page image at full zoom, not an OCR/mathpix artifact) -- adding the missing exponent so the displayed formula is internally consistent with its own stated result.
- **Found:**
  > 4 \times 9.87 \times\left(9 \times 10^{9}\right) \times 9 \times 10^{-31} \times\left(1.6 \times 10^{-19}\right)}
- **Should be:**
  > 4 \times 9.87 \times\left(9 \times 10^{9}\right) \times 9 \times 10^{-31} \times\left(1.6 \times 10^{-19}\right)^{2}}

### ex_12.1 — solution (hi)
- **Confidence:** high
- **Reason:** Caught at stage 9's manual read-back (screenshot review): this ratio expression arrived from Mathpix split across TWO separate $...$ spans mid-expression (a line-wrap artifact in the source PDF's own layout), with the second paren's closing delimiter corrupted to '\right.' (invisible) plus a stray bare ')' character outside any \left/\right pairing. Confirmed against chapter.hi.pdf page 294 that the source actually shows one continuous ratio '(10^-10 m)/(10^-15 m) = 10^5' with no such split -- the two-span shape is a pure OCR/mathpix artifact, not printed content. This should have been caught and fixed during the original stage-5 pass (a math-fidelity issue exactly the kind stage 5 exists to catch), and is fixed here as a follow-up correction, reconstructing it as one well-formed $...$ span with balanced \left(/\right) delimiters. Un-fixed, the broken span rendered as literal escaped LaTeX text on the final page (stage 9's own renderer correctly declines to guess at an unbalanced/malformed math span rather than silently mangling it further).
- **Found:**
  > $\left(10^{-10} \mathrm{~m}\right) /\left(10^{-15}\right.$ $\mathrm{m})=10^{5}$
- **Should be:**
  > $\left(10^{-10} \mathrm{~m}\right) /\left(10^{-15} \mathrm{~m}\right)=10^{5}$
