### ex_5.6 — question (en)
- **Confidence:** high
- **Reason:** OCR capitalized the oxalato ligand abbreviation "ox" as "OX" in part (a), inconsistent with part (b)'s lowercase "ox" in the same field and with the source page, which prints "ox" (lowercase) in both places.
- **Found:**
  > \mathrm{OX}
- **Should be:**
  > \mathrm{ox}

### it_5.3 — parts[0].question (en)
- **Confidence:** high
- **Reason:** The formula's LaTeX never closes — mathpix rendered the final closing bracket as "\right." instead of "\right]", so the ion is left with a dangling bracket. Chapter PDF page 11 (Intext Question 5.3(i)) shows the complete formula "K[Cr(H₂O)₂(C₂O₄)₂]" with a normal closing square bracket, matching how this same formula is written correctly elsewhere in this same item's own solution field.
- **Found:**
  > \left(\mathrm{C}_{2} \mathrm{O}_{4}\right)_{2}\right.$
- **Should be:**
  > \left(\mathrm{C}_{2} \mathrm{O}_{4}\right)_{2}\right]$

### it_5.5 — solution (en)
- **Confidence:** high
- **Reason:** Missing subscript — solutions PDF page 4 (Question 9.5 answer) reads "[NiCl4]2-" here, matching the "4" subscript already present earlier in this same item's own question field ("[NiCl4]2- ion with tetrahedral geometry"). The extracted solution drops the subscript on this second mention, turning the formula into a different, non-existent ion "[NiCl]2-".
- **Found:**
  > $[\mathrm{NiCl}]^{2-}, \mathrm{Cl}^{-}$
- **Should be:**
  > $[\mathrm{NiCl}_{4}]^{2-}, \mathrm{Cl}^{-}$

### it_5.10 — solution (en)
- **Confidence:** high
- **Reason:** Extraction dropped the negative-charge superscript on [Mn(CN)6]; the PDF clearly shows "4-" (consistent with Mn2+ + 6 CN- giving an overall -4 charge)
- **Found:**
  > \left[\mathrm{Mn}(\mathrm{CN})_{6}\right]^{4}
  > $$
- **Should be:**
  > \left[\mathrm{Mn}(\mathrm{CN})_{6}\right]^{4-}
  > $$

### it_5.10 — solution (en)
- **Confidence:** high
- **Reason:** Same missing negative-charge superscript on [Mn(CN)6], second occurrence later in the solution
- **Found:**
  > \left[\mathrm{Mn}(\mathrm{CN})_{6}\right]^{4} \text { is }
- **Should be:**
  > \left[\mathrm{Mn}(\mathrm{CN})_{6}\right]^{4-} \text { is }

### q_5.4 — parts[0].solution (en)
- **Confidence:** high
- **Reason:** The PDF (solutions.en.pdf, p.12) clearly shows NH3 with the 3 as a subscript ("N̈H₃"), not a superscript. The extracted text renders it as a superscript, which misrepresents the formula.
- **Found:**
  > \ddot{\mathrm{N}} \mathrm{H}^{3}
- **Should be:**
  > \ddot{\mathrm{N}} \mathrm{H}_{3}

### q_5.6 — parts[0].solution (en)
- **Confidence:** high
- **Reason:** The PDF (solutions.en.pdf, p.15) prints this formula with properly matched brackets: "[Zn(OH)]2-" (outer square brackets, inner parentheses closed normally). The extracted LaTeX has a mismatched bracket ("(\mathrm{OH}]" — opens with a round paren and closes with a square one, then dangles "\right."), which is a transcription defect independent of the source. Note: the PDF itself omits the "4" subscript on OH here (a source print error, not corrected per rule — see stage report).
- **Found:**
  > $\quad\left[\mathrm{Zn}(\mathrm{OH}]^{2-}\right.$
- **Should be:**
  > $\quad\left[\mathrm{Zn}(\mathrm{OH})\right]^{2-}$

### q_5.22 — solution (en)
- **Confidence:** high
- **Reason:** Mathpix OCR misread the Greek letter π (pi) as the Latin letter "n" in "anti-bonding π* orbital" — solutions.en.pdf p.29 clearly reads "π*" (the antibonding orbital of CO accepting metal d-electron back-donation), not "n*" (which would denote a non-bonding orbital, a different concept).
- **Found:**
  > into the vacant anti-bonding $n^{*}$ orbital
- **Should be:**
  > into the vacant anti-bonding $\pi^{*}$ orbital

### q_5.22 — solution (en)
- **Confidence:** high
- **Reason:** Mathpix OCR misread the Greek letter π (pi) as a superscripted capital Pi (Π) in "The σ bond strengthens the π bond" — solutions.en.pdf p.29 clearly reads "π bond" (lowercase pi, matching the π bond described one sentence earlier), not "Π" (an unrelated symbol here).
- **Found:**
  > The $\sigma$ bond strengthens the ${ }^{\Pi}$ bond and vice-versa.
- **Should be:**
  > The $\sigma$ bond strengthens the $\pi$ bond and vice-versa.

### q_5.24 — parts[0].solution (en)
- **Confidence:** high
- **Reason:** OCR error: "mactive" is not a word. solutions.en.pdf p.30 clearly reads "Trans is optically inactive" (paired with "Cis is optically active" on the next line, which the extraction already has correct).
- **Found:**
  > Trans is optically mactive
- **Should be:**
  > Trans is optically inactive
