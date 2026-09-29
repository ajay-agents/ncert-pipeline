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


---

## Second verification pass (post-completion cleanup, 2026-09-28)

The corrections below were applied in a second stage-5 pass after the chapter had already gone through stages 1-10 once. They correct genuine chemistry/formula/naming errors and formatting artifacts found on independent re-verification against the real textbook PDF (chapter.en.pdf) and real coordination chemistry, in addition to the usual OCR-vs-source checks. See the session's final report for the full claim-by-claim breakdown, including items investigated and NOT changed.

### q_5.24 — parts[2].solution (en)
- **Confidence:** high
- **Reason:** Independent symmetry check: an MA3B3 octahedron's fac isomer (C3v) and mer isomer (Cs) both retain a mirror plane, so neither is chiral; only 2 stereoisomers exist, not 4.
- **Found:**
  > Both isomers are optically active. Therefore, a total of 4 isomers exist.
- **Should be:**
  > Both the facial and meridional isomers possess a mirror plane (fac has C3v symmetry, mer has Cs symmetry), so both are optically inactive. Therefore, a total of 2 isomers exist (fac and mer).

### q_5.24 — parts[1].question (en)
- **Confidence:** high
- **Reason:** OCR artifact glued a stray subscript minus onto Cl; confirmed against chapter.en.pdf p.139 exercise 5.24(ii), which reads plain 'Cl]'.
- **Found:**
  > $\left[\mathrm{Co}\left(\mathrm{NH}_{3}\right)_{5} \mathrm{Cl}_{-}\right] \mathrm{Cl}_{2}$
- **Should be:**
  > $\left[\mathrm{Co}\left(\mathrm{NH}_{3}\right)_{5} \mathrm{Cl}\right] \mathrm{Cl}_{2}$

### q_5.24 — parts[1].solution (en)
- **Confidence:** high
- **Reason:** Independent coordination-geometry check: an octahedral MA5B complex has a single symmetric structure (C4v), so it cannot have stereoisomers; '2 isomers' is chemically wrong.
- **Found:**
  > Stereochemistry:
  > 
  > 2 isomers
- **Should be:**
  > Stereochemistry:
  > 
  > An MA5B octahedron (five identical NH3 + one Cl) has only one possible spatial arrangement — all five NH3 positions are equivalent by symmetry, so no geometrical or optical isomers exist.

### q_5.24 — parts[3].solution (en)
- **Confidence:** high
- **Reason:** Modern IUPAC ligand nomenclature uses 'chlorido', not 'chloro', for a coordinated chloride ligand.
- **Found:**
  > IUPAC name: Caesium tetrachloroferrate (III)
- **Should be:**
  > IUPAC name: Caesium tetrachloridoferrate(III)

### q_5.24 — parts[3].solution (en)
- **Confidence:** high
- **Reason:** Fe3+ has 3 electrons removed from neutral Fe ([Ar]3d6 4s2): 4s2 first, then one 3d electron, giving 3d5, not 3d6 — confirmed by the oxidation-state derivation (+3) already given two lines above in this same solution, which is a same-item self-contradiction. Also the complex is tetrahedral (CN=4), so the orbital labels are the tetrahedral e/t2 set, not the octahedral eg/t2g set.
- **Found:**
  > Electronic configuration of $d^{6}=e_{g}{ }^{2} t_{2 \mathrm{~g}}{ }^{3}$
- **Should be:**
  > Electronic configuration of $d^{5}=e^{2} t_{2}{ }^{3}$

### q_5.24 — parts[3].solution (en)
- **Confidence:** high
- **Reason:** sqrt(35) = 5.9161..., precise value 5.92 BM rather than rounding to 6 BM.
- **Found:**
  > $$
  > \begin{aligned}
  > & =\sqrt{n(n+2)} \\
  > & =\sqrt{5(5+2)} \\
  > & =\sqrt{35} \sim 6 \mathrm{BM}
  > \end{aligned}
  > $$
- **Should be:**
  > $$
  > \begin{aligned}
  > & =\sqrt{n(n+2)} \\
  > & =\sqrt{5(5+2)} \\
  > & =\sqrt{35} \approx 5.92 \mathrm{BM}
  > \end{aligned}
  > $$

### it_5.3 — solution (en)
- **Confidence:** high
- **Reason:** Independent check: MA5B octahedral complexes have a single symmetric structure and cannot be chiral. The claimed 'pair of optical isomers' is wrong; the complex genuinely shows only linkage isomerism (NO2 vs ONO) and ionisation isomerism (below).
- **Found:**
  > (iii) $\left[\mathrm{CO}\left(\mathrm{NH}_{3}\right)_{5}\left(\mathrm{NO}_{2}\right)\right]\left(\mathrm{NO}_{3}\right)_{2}$
  > A pair of optical isomers:
  > 
  > It can also show linkage isomerism.
- **Should be:**
  > (iii) $\left[\mathrm{Co}\left(\mathrm{NH}_{3}\right)_{5}\left(\mathrm{NO}_{2}\right)\right]\left(\mathrm{NO}_{3}\right)_{2}$
  > This is an MA5B octahedron (five NH3 + one NO2), so no geometrical or optical isomers are possible. It shows linkage isomerism.

### it_5.9 — solution (en)
- **Confidence:** high
- **Reason:** The question is about [Pt(CN)4]2-, not a palladium complex; Pt neutral is [Xe]4f14 5d9 6s1, so Pt2+ (losing 6s1 then one 5d) is 5d8 — the metal-symbol swap Pd->Pt is confirmed correct, Pd(+2) would be 4d8 not 5d8 in any case.
- **Found:**
  > the electronic configuration of $\operatorname{Pd}(+2)$ is $5 d^{8}$
- **Should be:**
  > the electronic configuration of $\operatorname{Pt}(+2)$ is $5 d^{8}$

### it_5.1 — solution (en)
- **Confidence:** high
- **Reason:** This answers part (iv) 'amminebromidochloridonitrito-N-platinate(II)' (chapter.en.pdf p.125 confirms part (iv) has this exact name) but was mislabelled '(vi)', duplicating the true part (vi) label below. Also fixed 'NH)3' -> '(NH3)': the name says 'ammine' (one NH3), and the OCR had detached the subscript from the ligand.
- **Found:**
  > (vi) $\left[\mathrm{Pt}(\mathrm{NH})_{3} \mathrm{BrCl}\left(\mathrm{NO}_{2}\right)\right]^{-}$
- **Should be:**
  > (iv) $\left[\mathrm{Pt}\left(\mathrm{NH}_{3}\right) \mathrm{BrCl}\left(\mathrm{NO}_{2}\right)\right]^{-}$

### it_5.1 — solution (en)
- **Confidence:** high
- **Reason:** OCR confusion of the element symbol Co (cobalt) with CO (carbon monoxide) - this is the central metal of a cobalt(III) ammine/aqua complex, not a carbonyl.
- **Found:**
  > (i) $\quad\left[\mathrm{CO}\left(\mathrm{H}_{2} \mathrm{O}\right)_{2}\left(\mathrm{NH}_{3}\right)_{4}\right] \mathrm{Cl}_{3}$
- **Should be:**
  > (i) $\quad\left[\mathrm{Co}\left(\mathrm{H}_{2} \mathrm{O}\right)_{2}\left(\mathrm{NH}_{3}\right)_{4}\right] \mathrm{Cl}_{3}$

### it_5.3 — solution (en)
- **Confidence:** high
- **Reason:** CO/Co OCR confusion in the linkage-isomerism pair.
- **Found:**
  > \left[\mathrm{CO}\left(\mathrm{NH}_{3}\right)_{5}\left(\mathrm{NO}_{2}\right)\right]\left(\mathrm{NO}_{3}\right)_{2} \text { and }\left[\mathrm{CO}\left(\mathrm{NH}_{3}\right)_{5}(\mathrm{ONO})\right]\left(\mathrm{NO}_{3}\right)_{2}
- **Should be:**
  > \left[\mathrm{Co}\left(\mathrm{NH}_{3}\right)_{5}\left(\mathrm{NO}_{2}\right)\right]\left(\mathrm{NO}_{3}\right)_{2} \text { and }\left[\mathrm{Co}\left(\mathrm{NH}_{3}\right)_{5}(\mathrm{ONO})\right]\left(\mathrm{NO}_{3}\right)_{2}

### it_5.3 — solution (en)
- **Confidence:** high
- **Reason:** CO/Co OCR confusion in the ionisation-isomerism pair.
- **Found:**
  > \left[\mathrm{Co}\left(\mathrm{NH}_{3}\right)_{5}\left(\mathrm{NO}_{2}\right)\right]\left(\mathrm{NO}_{3}\right)_{2} \quad\left[\mathrm{CO}\left(\mathrm{NH}_{3}\right)_{5}\left(\mathrm{NO}_{3}\right)\right]\left(\mathrm{NO}_{3}\right)\left(\mathrm{NO}_{2}\right)
- **Should be:**
  > \left[\mathrm{Co}\left(\mathrm{NH}_{3}\right)_{5}\left(\mathrm{NO}_{2}\right)\right]\left(\mathrm{NO}_{3}\right)_{2} \quad\left[\mathrm{Co}\left(\mathrm{NH}_{3}\right)_{5}\left(\mathrm{NO}_{3}\right)\right]\left(\mathrm{NO}_{3}\right)\left(\mathrm{NO}_{2}\right)

### q_5.6 — parts[0].solution (en)
- **Confidence:** high
- **Reason:** Missing subscript 4 on OH; zinc is 4-coordinate here (matches Example 5.2(b)'s K2[Zn(OH)4] for the same ligand/ion).
- **Found:**
  > $\quad\left[\mathrm{Zn}(\mathrm{OH})\right]^{2-}$
- **Should be:**
  > $\quad\left[\mathrm{Zn}(\mathrm{OH})_{4}\right]^{2-}$

### q_5.6 — parts[9].solution (en)
- **Confidence:** high
- **Reason:** Mismatched bracket types (square open, round close) around NO2 - an OCR artifact, should be a matching round-bracket pair like the rest of the ligand list.
- **Found:**
  > $\left[\mathrm{Co}\left[\mathrm{NO}_{2}\right)\left(\mathrm{NH}_{3}\right)_{5}\right]^{2+}$
- **Should be:**
  > $\left[\mathrm{Co}\left(\mathrm{NO}_{2}\right)\left(\mathrm{NH}_{3}\right)_{5}\right]^{2+}$

### q_5.3 — parts[0].solution (en)
- **Confidence:** high
- **Reason:** [Fe(CN)6]^4+ is chemically impossible as written and was mislabelled cationic - the real [Fe(CN)6] complex is anionic ([Fe(CN)6]^4-, already correctly listed as the second anionic example on the next line). Replaced with a genuine cationic example, [Co(NH3)6]3+, keeping the two-example format.
- **Found:**
  > {\left[\mathrm{Ni}\left(\mathrm{NH}_{3}\right)_{6}\right]^{2+},\left[\mathrm{Fe}(\mathrm{CN})_{6}\right]^{4+}} & =\text { cationic complex }
- **Should be:**
  > {\left[\mathrm{Ni}\left(\mathrm{NH}_{3}\right)_{6}\right]^{2+},\left[\mathrm{Co}\left(\mathrm{NH}_{3}\right)_{6}\right]^{3+}} & =\text { cationic complex }

### q_5.28 — solution (en)
- **Confidence:** high
- **Reason:** Charge-balance check: two Cl- counterions require the complex cation to carry a 2+ charge, not 1+. The ion count itself (1 complex cation + 2 Cl- = 3 ions -> option (iii)) was already correct; only the superscript was wrong.
- **Found:**
  > Thus, $\left[\mathrm{Co}\left(\mathrm{NH}_{3}\right)_{6}\right]^{+}$along with two $\mathrm{Cl}^{-}$ions are produced.
- **Should be:**
  > Thus, $\left[\mathrm{Co}\left(\mathrm{NH}_{3}\right)_{6}\right]^{2+}$along with two $\mathrm{Cl}^{-}$ions are produced.

### q_5.17 — solution (en)
- **Confidence:** high
- **Reason:** Verified directly against chapter.en.pdf p.132 (NCERT's own printed spectrochemical series); the version in this file had several ligands out of order, a spurious N3/H- and duplicated SO3^2-/phen not in the textbook's series, and was missing edta^4-.
- **Found:**
  > $$
  > \begin{aligned}
  > & \mathrm{I}-<\mathrm{Br}^{-}<\mathrm{S}^{2-}<\mathrm{SCN}^{-}<\mathrm{Cl}^{-}<\mathrm{N}_{3}<\mathrm{F}^{-}<\mathrm{OH}^{-}<\mathrm{C}_{2} \mathrm{O}_{4}^{2-} \sim \mathrm{H}_{2} \mathrm{O}<\mathrm{NCS}^{-} \sim \mathrm{H}^{-}<\mathrm{CN}^{-}<\mathrm{NH}_{3} \\
  > & <\text { en } \sim \mathrm{SO}_{3}^{2-}<\mathrm{NO}_{2}^{-}<\text {phen }<\mathrm{CO}
  > \end{aligned}
  > $$
- **Should be:**
  > $$
  > I^{-}<Br^{-}<SCN^{-}<Cl^{-}<S^{2-}<F^{-}<OH^{-}<C_{2}O_{4}^{2-}<H_{2}O<NCS^{-}<edta^{4-}<NH_{3}<en<CN^{-}<CO
  > $$

### q_5.7 — parts[1].solution (en)
- **Confidence:** high
- **Reason:** IUPAC 2005 names the CH3NH2 ligand systematically as 'methanamine', not the common name 'methylamine'; also removed the stray space before 'platinum'.
- **Found:**
  > Diamminechlorido(methylamine) platinum(II) chloride
- **Should be:**
  > Diamminechlorido(methanamine)platinum(II) chloride

### q_5.7 — parts[2].solution (en)
- **Confidence:** high
- **Reason:** Missing an 'a': the multiplying prefix hexa- + ligand aqua- gives 'hexaaqua-' (both a's kept, standard IUPAC style, e.g. hexaaquachromium(III)).
- **Found:**
  > Hexaquatitanium(III) ion
- **Should be:**
  > Hexaaquatitanium(III) ion

### q_5.7 — parts[3].solution (en)
- **Confidence:** high
- **Reason:** 'Ammini' should be 'ammine' (the NH3 ligand prefix), and 'Cobalt' should not be capitalised mid-name.
- **Found:**
  > Tetraamminichloridonitrito-N-Cobalt(III) chloride
- **Should be:**
  > Tetraamminechloridonitrito-N-cobalt(III) chloride

### q_5.7 — parts[4].solution (en)
- **Confidence:** high
- **Reason:** Same missing-'a' elision error as part (iii): hexa- + aqua- = 'hexaaqua-'.
- **Found:**
  > Hexaquamanganese(II) ion
- **Should be:**
  > Hexaaquamanganese(II) ion

### q_5.7 — parts[7].solution (en)
- **Confidence:** high
- **Reason:** 'Diammine' (with two m's) would mean two ammine/NH3 ligands; the en ligand is ethane-1,2-diamine (one m). Also removed the stray space after the comma in the locant and before 'cobalt'.
- **Found:**
  > Tris(ethane-1, 2-diammine) cobalt(III) ion
- **Should be:**
  > Tris(ethane-1,2-diamine)cobalt(III) ion

### it_5.2 — solution (en)
- **Confidence:** high
- **Reason:** Modern IUPAC ligand name for coordinated CN- is 'cyanido', not 'cyano'.
- **Found:**
  > (iii) Potassium hexacyanoferrate(III)
- **Should be:**
  > (iii) Potassium hexacyanidoferrate(III)

### it_5.2 — solution (en)
- **Confidence:** high
- **Reason:** Same methylamine -> methanamine fix as q_5.7(ii), for the identical ligand/complex.
- **Found:**
  > (vi) Diamminechlorido(methylamine)platinum(II) chloride
- **Should be:**
  > (vi) Diamminechlorido(methanamine)platinum(II) chloride

### q_5.24 — parts[4].solution (en)
- **Confidence:** high
- **Reason:** Modern IUPAC ligand name for coordinated CN- is 'cyanido', not 'cyano' (same fix as it_5.2(iii)).
- **Found:**
  > Potassium hexacyanomanganate(II)
- **Should be:**
  > Potassium hexacyanidomanganate(II)

### q_5.24 — parts[4].solution (en)
- **Confidence:** high
- **Reason:** 'd5+' is a stray typo (the oxidation state +2 is already given on the line above); the configuration itself, d5: t2g5, is correct for low-spin Mn2+ with the strong-field CN- ligand.
- **Found:**
  > Electronic configuration: $d^{5+}: t_{2 g}{ }^{5}$
- **Should be:**
  > Electronic configuration: $d^{5}: t_{2 g}{ }^{5}$

### q_5.24 — parts[4].solution (en)
- **Confidence:** high
- **Reason:** Spelling fix.
- **Found:**
  > Streochemistry: optically inactive
- **Should be:**
  > Stereochemistry: optically inactive

### q_5.23 — parts[0].solution (en)
- **Confidence:** high
- **Reason:** Cross-item consistency + independent spectrochemical-series check (verified against chapter.en.pdf p.132): oxalate is weak-field, so [Co(C2O4)3]3- is high-spin/outer-orbital, matching Ex 5.15(iii)'s sp3d2 answer for the identical ion. Ex 5.23(i)'s low-spin t2g6eg0 was the one in error, not Ex 5.15(iii).
- **Found:**
  > The $d$ orbital occupation for $\mathrm{Co}^{3+}$ is $t_{2 \mathrm{~g}}{ }^{6} e_{g}{ }^{0 .}$
- **Should be:**
  > Oxalate (C2O4^2-) is a weak-field ligand (it sits below H2O in the spectrochemical series), so it does not pair the 3d electrons of Co3+. The $d$ orbital occupation for $\mathrm{Co}^{3+}$ is therefore $t_{2 \mathrm{~g}}{ }^{4} e_{g}{ }^{2}$ (high-spin, outer-orbital sp3d2 complex, 4 unpaired electrons) - consistent with Ex 5.15(iii)'s valence-bond-theory answer for the same ion.

### q_5.3 — parts[0].solution (en)
- **Confidence:** high
- **Reason:** The original definition claimed a coordination entity is always a charged species, directly contradicted by its own third example two lines later, [Ni(CO)4] (neutral complex). Fixed the definition, not the example, per the textbook's own definition on chapter.en.pdf p.121 ('A coordination entity constitutes a central metal atom or ion bonded to a fixed number of ions or molecules').
- **Found:**
  > A coordination entity is an electrically charged radical or species carrying a positive or negative charge. In a coordination entity, the central atom or ion is surrounded by a suitable number of neutral molecules or negative ions ( called ligands). For example:
- **Should be:**
  > A coordination entity constitutes a central metal atom or ion bonded to a fixed number of ions or molecules; it may be cationic, anionic, or neutral overall. In a coordination entity, the central atom or ion is surrounded by a suitable number of neutral molecules or negative ions (called ligands). For example:

### it_5.8 — solution (en)
- **Confidence:** high
- **Reason:** The two-column table's explanation text had been merged into a single garbled run-on paragraph mixing Co and Ni reasoning mid-sentence. Reconstructed as two clearly-attributed paragraphs; the underlying chemistry (Co3+ d6 inner-orbital d2sp3, Ni2+ d8 outer-orbital sp3d2) was independently re-derived and is correct - d8 can never free up a 3d orbital regardless of ligand field strength, since 6+2=8 fills all five 3d orbitals.
- **Found:**
  > $\mathrm{NH}_{3}$ being a strong field ligand causes the
  > 
  > 
  > 
  > 
  > 
  > pairing. Therefore, Ni can undergo $d^{2} s p^{3}$
  > 
  > If $\mathrm{NH}_{3}$ causes the pairing, then only one $3 d$ hybridization. orbital is empty. Thus, it cannot undergo
  > 
  > 
  > $d^{2} s p^{3}$ hybridization. Therefore, it undergoes $s p^{3} d^{2}$ hybridization.
  > Hence, it is an inner orbital complex.
  > 
  > 
  > 
  > Hence, it forms an outer orbital complex.
- **Should be:**
  > For $\left[\mathrm{Co}\left(\mathrm{NH}_{3}\right)_{6}\right]^{3+}$: $\mathrm{NH}_{3}$ is a strong field ligand, so it pairs up the six $3d$ electrons of $\mathrm{Co}^{3+}$ ($d^6$), giving $t_{2g}{}^{6}e_g{}^{0}$. This leaves two $3d$ orbitals vacant, so $\mathrm{Co}^{3+}$ undergoes $d^{2}sp^{3}$ hybridisation using the two now-empty inner $3d$ orbitals. Hence $\left[\mathrm{Co}\left(\mathrm{NH}_{3}\right)_{6}\right]^{3+}$ is an inner orbital complex (diamagnetic).
  > 
  > For $\left[\mathrm{Ni}\left(\mathrm{NH}_{3}\right)_{6}\right]^{2+}$: $\mathrm{Ni}^{2+}$ has a $d^8$ configuration, so even with a strong field ligand the eight electrons must occupy all five $3d$ orbitals ($t_{2g}{}^{6}e_g{}^{2}$, 2 unpaired) - no $3d$ orbital is left vacant. $\mathrm{Ni}^{2+}$ therefore cannot undergo $d^{2}sp^{3}$ hybridisation and instead uses the outer $4d$ orbitals, undergoing $sp^{3}d^{2}$ hybridisation. Hence $\left[\mathrm{Ni}\left(\mathrm{NH}_{3}\right)_{6}\right]^{2+}$ forms an outer orbital complex (paramagnetic, 2 unpaired electrons).

### q_5.19 — solution (en)
- **Confidence:** high
- **Reason:** Independent check: a d3 ion (Cr3+) always has 3 unpaired electrons in an octahedral field regardless of ligand field strength, since pairing is only a possibility once a 4th electron must be placed. Calling NH3 'weak field' here is also inaccurate (NH3 sits well up the strong-field end of the spectrochemical series, p.132) and, more importantly, irrelevant to this ion's magnetism.
- **Found:**
  > Cr is in the +3 oxidation state i.e., $d^{3}$ configuration. Also, $\mathrm{NH}_{3}$ is a weak field ligand that does not cause the pairing of the electrons in the $3 d$ orbital. $\mathrm{Cr}^{3+}$
  > 
  > Therefore, it undergoes $d^{2} s p^{3}$ hybridization and the electrons in the $3 d$ orbitals remain unpaired. Hence, it is paramagnetic in nature.
- **Should be:**
  > Cr is in the +3 oxidation state i.e., $d^{3}$ configuration. For a $d^3$ ion, ligand field strength does not matter: with only three electrons and three $t_{2g}$ orbitals available, all three electrons occupy the $t_{2g}$ level singly (Hund's rule) whether the ligand is weak or strong field - pairing only becomes a possibility from the fourth electron onward ($d^4$ and beyond). $\mathrm{Cr}^{3+}$ ($t_{2g}{}^{3}e_g{}^{0}$) therefore undergoes $d^{2} s p^{3}$ hybridization with all three $3d$ electrons unpaired. Hence, it is paramagnetic in nature.

### q_5.14 — solution (en)
- **Confidence:** high
- **Reason:** Independently balanced (charge: 2(+2)+10(-1) = -6 both sides; atoms: 2 Cu, 10 C, 10 N on both sides - confirmed balanced) and re-derived: this is the standard textbook explanation that excess CN- reduces Cu2+ to Cu+ forming the very stable [Cu(CN)4]3- (cuprate(I), not cuprate(II)) - the previous text's 'K2[Cu(CN)4] is stable so doesn't ionise' explanation kept Cu at +2 throughout, which is chemically wrong and also left a garbled run-on sentence ('K2[Cu(CN)4]_is a very stable complex').
- **Found:**
  > Thus, the coordination entity formed in the process is $\mathrm{K}_{2}\left[\mathrm{Cu}(\mathrm{CN})_{4}\right] . \mathrm{K}_{2}\left[\mathrm{Cu}(\mathrm{CN})_{4}\right]_{\text {is a }}$ very stable complex, which does not ionize to give $\mathrm{Cu}^{2+}$ ions when added to water. Hence, $\mathrm{Cu}^{2+}$ ions are not precipitated when $\mathrm{H}_{2} \mathrm{~S}_{(g)}$ is passed through the solution.
- **Should be:**
  > In excess $\mathrm{KCN}$, $\mathrm{Cu}^{2+}$ is actually reduced to $\mathrm{Cu}^{+}$, with the excess $\mathrm{CN}^{-}$ itself being oxidised to cyanogen, $(\mathrm{CN})_{2}$:
  > $$
  > 2\mathrm{Cu}^{2+}+10\mathrm{CN}^{-} \longrightarrow 2\left[\mathrm{Cu}(\mathrm{CN})_{4}\right]^{3-}+(\mathrm{CN})_{2}
  > $$
  > Thus, the coordination entity formed in the process is the very stable $\left[\mathrm{Cu}(\mathrm{CN})_{4}\right]^{3-}$ (i.e. $\mathrm{K}_{3}\left[\mathrm{Cu}(\mathrm{CN})_{4}\right]$), which does not dissociate to give free $\mathrm{Cu}^{2+}$ (or even $\mathrm{Cu}^{+}$) ions in solution. Since no free $\mathrm{Cu}^{2+}$ ions remain available, $\mathrm{CuS}$ is not precipitated when $\mathrm{H}_{2}\mathrm{~S}_{(g)}$ is passed through the solution.

### q_5.14 — solution (en)
- **Confidence:** high
- **Reason:** Corrected the formation equation to reflect the real Cu(II)->Cu(I) reduction (complex is [Cu(CN)4]^3-/K3[Cu(CN)4], not [Cu(CN)4]^2-/K2[Cu(CN)4]) - independently balanced both for atoms and charge.
- **Found:**
  > \mathrm{CuSO}_{4(a q)}+4 \mathrm{KCN}_{(a q)} \longrightarrow \mathrm{K}_{2}\left[\mathrm{Cu}(\mathrm{CN})_{4}\right]_{(a q)}+\mathrm{K}_{2} \mathrm{SO}_{4(a q)} \\
  > & \text {.e., }\left[\mathrm{Cu}\left(\mathrm{H}_{2} \mathrm{O}\right)_{4}\right]^{2+}+4 \mathrm{CN}^{-} \longrightarrow\left[\mathrm{Cu}(\mathrm{CN})_{4}\right]^{2-}+4 \mathrm{H}_{2} \mathrm{O}
- **Should be:**
  > 2\mathrm{CuSO}_{4(a q)}+10 \mathrm{KCN}_{(a q)} \longrightarrow 2\mathrm{K}_{3}\left[\mathrm{Cu}(\mathrm{CN})_{4}\right]_{(a q)}+2\mathrm{K}_{2} \mathrm{SO}_{4(a q)}+(\mathrm{CN})_2 \\
  > & \text {i.e., } 2\left[\mathrm{Cu}\left(\mathrm{H}_{2} \mathrm{O}\right)_{4}\right]^{2+}+10\mathrm{CN}^{-} \longrightarrow 2\left[\mathrm{Cu}(\mathrm{CN})_{4}\right]^{3-}+8 \mathrm{H}_{2} \mathrm{O}+(\mathrm{CN})_2

### ex_5.3 — parts[4].solution (en)
- **Confidence:** high
- **Reason:** Confirmed verbatim against chapter.en.pdf p.124 (Example 5.3(e)): the textbook itself gives this exact name. Per step_5/verify.md, a textbook error is not stage 5's call to silently override - added a clarifying note instead of changing the textbook-sourced answer.
- **Found:**
  > mercury (I) tetrathiocyanato-S-cobaltate(III)
- **Should be:**
  > mercury (I) tetrathiocyanato-S-cobaltate(III) (as printed in the textbook; note that mononuclear Hg(I) is unusual - Hg(I) is otherwise only known as the dimeric Hg2^2+ ion - but this is the formal oxidation-state bookkeeping NCERT itself uses for this name)

### q_5.2 — solution (en)
- **Confidence:** high
- **Reason:** Naming typo: 'ammino' -> 'ammine' (the NH3 ligand prefix), and the oxidation-state roman numeral should not be lower-case.
- **Found:**
  > tetraamminocopper(ii) sulphate
- **Should be:**
  > tetraamminecopper(II) sulphate

### q_5.2 — solution (en)
- **Confidence:** high
- **Reason:** The original sentence had the causal relationship backwards: retaining the complex's identity in solution is the *cause* of the failed Cu2+ test, not the other way around.
- **Found:**
  > This happens because $\left[\mathrm{Cu}\left(\mathrm{NH}_{3}\right)_{4}\right] \mathrm{SO}_{4} \cdot 5 \mathrm{H}_{2} \mathrm{O}$ does not show the test for $\mathrm{Cu}^{2+}$.
- **Should be:**
  > Since $\left[\mathrm{Cu}\left(\mathrm{NH}_{3}\right)_{4}\right] \mathrm{SO}_{4} \cdot 5 \mathrm{H}_{2} \mathrm{O}$ retains its identity (as the complex ion) in solution, it does not show the test for $\mathrm{Cu}^{2+}$.

### q_5.2 — solution (en)
- **Confidence:** high
- **Reason:** The solution ended mid-sentence with dangling, meaningless trailing text ('solution of' followed by a stray bare hyphen) - removed, completing the sentence that was already there.
- **Found:**
  > The ions present in the $\left[\mathrm{Cu}\left(\mathrm{NH}_{3}\right)_{4}\right] \mathrm{SO}_{4} \cdot 5 \mathrm{H}_{2} \mathrm{O}$ are $\left[\mathrm{Cu}\left(\mathrm{NH}_{3}\right)_{4}\right]^{2+}$ and $\mathrm{SO}_{4}{ }^{2-}$ solution of
  > -
- **Should be:**
  > The ions present in the $\left[\mathrm{Cu}\left(\mathrm{NH}_{3}\right)_{4}\right] \mathrm{SO}_{4} \cdot 5 \mathrm{H}_{2} \mathrm{O}$ are $\left[\mathrm{Cu}\left(\mathrm{NH}_{3}\right)_{4}\right]^{2+}$ and $\mathrm{SO}_{4}{ }^{2-}$.

### q_5.24 — parts[0].solution (en)
- **Confidence:** high
- **Reason:** sqrt(15) = 3.873..., precise value 3.87 BM rather than rounding to 4 BM.
- **Found:**
  > $$
  > \begin{aligned}
  > & =\sqrt{3(3+2)} \\
  > & =\sqrt{15} \\
  > & \sim 4 \mathrm{BM}
  > \end{aligned}
  > $$
- **Should be:**
  > $$
  > \begin{aligned}
  > & =\sqrt{3(3+2)} \\
  > & =\sqrt{15} \\
  > & \approx 3.87 \mathrm{BM}
  > \end{aligned}
  > $$

### q_5.24 — parts[2].solution (en)
- **Confidence:** high
- **Reason:** sqrt(15) = 3.873..., precise value 3.87 BM rather than rounding to 4 BM (same fix as part (i), also a Cr3+/d3 ion).
- **Found:**
  > $$
  > \begin{aligned}
  > & =\sqrt{3(3+2)} \\
  > & =\sqrt{15} \\
  > & \sim 4 \mathrm{BM}
  > \end{aligned}
  > $$
- **Should be:**
  > $$
  > \begin{aligned}
  > & =\sqrt{3(3+2)} \\
  > & =\sqrt{15} \\
  > & \approx 3.87 \mathrm{BM}
  > \end{aligned}
  > $$

### q_5.29 — parts[0].solution (en)
- **Confidence:** high
- **Reason:** sqrt(15) = 3.873..., precise value 3.87 BM rather than rounding to 4 BM.
- **Found:**
  > $$
  > \begin{aligned}
  > & =\sqrt{3(3+2)} \\
  > & =\sqrt{15} \\
  > & \sim 4 \mathrm{BM}
  > \end{aligned}
  > $$
- **Should be:**
  > $$
  > \begin{aligned}
  > & =\sqrt{3(3+2)} \\
  > & =\sqrt{15} \\
  > & \approx 3.87 \mathrm{BM}
  > \end{aligned}
  > $$

### q_5.29 — parts[1].solution (en)
- **Confidence:** high
- **Reason:** sqrt(24) = 4.899..., precise value 4.90 BM rather than rounding to 5 BM.
- **Found:**
  > $$
  > \begin{aligned}
  > & =\sqrt{24} \\
  > & \sim 5 \mathrm{BM}
  > \end{aligned}
  > $$
- **Should be:**
  > $$
  > \begin{aligned}
  > & =\sqrt{24} \\
  > & \approx 4.90 \mathrm{BM}
  > \end{aligned}
  > $$

### q_5.27 — parts[3].solution (en)
- **Confidence:** high
- **Reason:** Au(I) + 2 CN- (each -1) gives an overall -1 charge on the complex; the charge was dropped from the formula.
- **Found:**
  > gold combines with cyanide ions to form $\left[\mathrm{Au}(\mathrm{CN})_{2}\right]$.
- **Should be:**
  > gold combines with cyanide ions to form $\left[\mathrm{Au}(\mathrm{CN})_{2}\right]^{-}$.

### it_5.6 — question (en)
- **Confidence:** high
- **Reason:** The question number '5.6' was glued onto the start of the question text itself (an OCR/extraction artifact); confirmed against chapter.en.pdf p.132 intext question 5.6, which reads plainly '[NiCl4]2- is paramagnetic...'.
- **Found:**
  > $5.6\left[\mathrm{NiCl}_{4}\right]^{2-}$ is paramagnetic
- **Should be:**
  > $\left[\mathrm{NiCl}_{4}\right]^{2-}$ is paramagnetic

### it_5.7 — question (en)
- **Confidence:** high
- **Reason:** Same glued-question-number artifact as it_5.6, confirmed against chapter.en.pdf p.132 intext question 5.7.
- **Found:**
  > $5.7\left[\mathrm{Fe}\left(\mathrm{H}_{2} \mathrm{O}\right)_{6}\right]^{3+}$ is strongly paramagnetic
- **Should be:**
  > $\left[\mathrm{Fe}\left(\mathrm{H}_{2} \mathrm{O}\right)_{6}\right]^{3+}$ is strongly paramagnetic

### q_5.3 — parts[1].solution (en)
- **Confidence:** high
- **Reason:** Typo: 'coordinal complex' -> 'coordination complex'.
- **Found:**
  > the metal atom in a coordination entity or a coordinal complex are known as ligands.
- **Should be:**
  > the metal atom in a coordination entity or a coordination complex are known as ligands.

### q_5.3 — parts[3].solution (en)
- **Confidence:** high
- **Reason:** The answer ended with the single bare word 'Tetrahedral' - not the 'two examples' format the question explicitly asks for ('Explain with two examples each of the following...'). Added a second example (octahedral) alongside a concrete formula for the first.
- **Found:**
  > Coordination polyhedrons about the central atom can be defined as the spatial arrangement of the ligands that are directly attached to the central metal ion in the coordination sphere. For example:
  > 
  > 
  > 
  > Tetrahedral
- **Should be:**
  > Coordination polyhedrons about the central atom can be defined as the spatial arrangement of the ligands that are directly attached to the central metal ion in the coordination sphere. For example:
  > 
  > (a) $\left[\mathrm{Ni}(\mathrm{CO})_{4}\right]$ is tetrahedral.
  > (b) $\left[\mathrm{Co}\left(\mathrm{NH}_{3}\right)_{6}\right]^{3+}$ is octahedral.

### q_5.5 — parts[1].solution (en)
- **Confidence:** high
- **Reason:** Mismatched/stray LaTeX bracket commands (\left. and \right. left dangling instead of a single matched \left[ ... \right] pair) - an OCR/typesetting artifact carried over from stage 1-4; the underlying chemistry (oxidation-state derivation) is unaffected.
- **Found:**
  > & {\left[\begin{array}{lll}
  > \mathrm{Co} & (\mathrm{Br})_{2} & \left.(\mathrm{en})_{2}\right]^{2+} \\
  > \downarrow & \downarrow & \downarrow
  > \end{array}\right.} \\
- **Should be:**
  > & {\left[\begin{array}{lll}
  > \mathrm{Co} & (\mathrm{Br})_{2} & (\mathrm{en})_{2}
  > \end{array}\right]^{2+}} \\
  > & \downarrow \quad \downarrow \quad \downarrow \\

### q_5.8 — solution (en)
- **Confidence:** high
- **Reason:** Cleaned up a cluster of OCR/extraction artifacts in one pass: several formulas had missing or mismatched brackets ([Co(NH3)5(ONO)Cl2 missing its closing bracket around the complex ion; the two ionisation-isomer formulas both missing their opening bracket; [Cr[H2O)6] mixing bracket types), and the '(d)'/'(e)' sub-part labels had been glued onto the end of the previous line/formula instead of starting their own line. No chemistry content was changed, only formula punctuation and line breaks.
- **Found:**
  > $\left[\mathrm{Co}\left(\mathrm{NH}_{3}\right)_{5}\left(\mathrm{NO}_{2}\right)\right] \mathrm{Cl}_{2}$ and $\left[\mathrm{Co}\left(\mathrm{NH}_{3}\right)_{5}(\mathrm{ONO}) \mathrm{Cl}_{2}\right.$
  > Yellow form Red form (d)
  > Coordination isomerism:
  > This type of isomerism arises when the ligands are interchanged between cationic and anionic entities of differnet metal ions present in the complex.
  > $\left[\mathrm{Co}\left(\mathrm{NH}_{3}\right)_{6}\right]\left[\mathrm{Cr}(\mathrm{CN})_{6}\right]$ and $\left[\mathrm{Cr}\left(\mathrm{NH}_{3}\right)_{6}\right]\left[\mathrm{Co}(\mathrm{CN})_{6}\right](\mathbf{e})$
  > Ionization isomerism:
  > This type of isomerism arises when a counter ion replaces a ligand within the coordination sphere. Thus, complexes that have the same composition, but furnish different ions when dissolved in water are called ionization isomers. For e.g.,
  > $\left.\mathrm{Co}\left(\mathrm{NH}_{3}\right)_{5} \mathrm{SO}_{4}\right) \mathrm{Br}$ and $\left.\mathrm{Co}\left(\mathrm{NH}_{3}\right)_{5} \mathrm{Br}\right] \mathrm{SO}_{4}$.
  > (f) Solvate isomerism:
  > Solvate isomers differ by whether or not the solvent molecule is directly bonded to the metal ion or merely present as a free solvent molecule in the crystal lattice.
  > $\left[\mathrm{Cr}\left[\mathrm{H}_{2} \mathrm{O}\right)_{6}\right] \mathrm{Cl}_{3}\left[\mathrm{Cr}\left(\mathrm{H}_{2} \mathrm{O}\right)_{5} \mathrm{Cl}\right] \mathrm{Cl}_{2} . \mathrm{H}_{2} \mathrm{O}\left[\mathrm{Cr}\left(\mathrm{H}_{2} \mathrm{O}\right)_{5} \mathrm{Cl}_{2}\right] \mathrm{Cl} .2 \mathrm{H}_{2} \mathrm{O}$
- **Should be:**
  > $\left[\mathrm{Co}\left(\mathrm{NH}_{3}\right)_{5}\left(\mathrm{NO}_{2}\right)\right] \mathrm{Cl}_{2}$ and $\left[\mathrm{Co}\left(\mathrm{NH}_{3}\right)_{5}(\mathrm{ONO})\right] \mathrm{Cl}_{2}$
  > Yellow form, Red form
  > 
  > (d) Coordination isomerism:
  > This type of isomerism arises when the ligands are interchanged between cationic and anionic entities of different metal ions present in the complex.
  > $\left[\mathrm{Co}\left(\mathrm{NH}_{3}\right)_{6}\right]\left[\mathrm{Cr}(\mathrm{CN})_{6}\right]$ and $\left[\mathrm{Cr}\left(\mathrm{NH}_{3}\right)_{6}\right]\left[\mathrm{Co}(\mathrm{CN})_{6}\right]$
  > 
  > (e) Ionization isomerism:
  > This type of isomerism arises when a counter ion replaces a ligand within the coordination sphere. Thus, complexes that have the same composition, but furnish different ions when dissolved in water are called ionization isomers. For e.g.,
  > $\left[\mathrm{Co}\left(\mathrm{NH}_{3}\right)_{5} \mathrm{SO}_{4}\right] \mathrm{Br}$ and $\left[\mathrm{Co}\left(\mathrm{NH}_{3}\right)_{5} \mathrm{Br}\right] \mathrm{SO}_{4}$.
  > 
  > (f) Solvate isomerism:
  > Solvate isomers differ by whether or not the solvent molecule is directly bonded to the metal ion or merely present as a free solvent molecule in the crystal lattice.
  > $\left[\mathrm{Cr}\left(\mathrm{H}_{2} \mathrm{O}\right)_{6}\right] \mathrm{Cl}_{3}$, $\left[\mathrm{Cr}\left(\mathrm{H}_{2} \mathrm{O}\right)_{5} \mathrm{Cl}\right] \mathrm{Cl}_{2} . \mathrm{H}_{2} \mathrm{O}$, $\left[\mathrm{Cr}\left(\mathrm{H}_{2} \mathrm{O}\right)_{5} \mathrm{Cl}_{2}\right] \mathrm{Cl} .2 \mathrm{H}_{2} \mathrm{O}$

### q_5.12 — solution (en)
- **Confidence:** high
- **Reason:** Independent geometry check: Pt(II) with coordination number 4 is a d8 metal ion, which is characteristically square planar (like the [PtCl2(en)2]2+, [Pt(CN)4]2- examples used elsewhere in this same chapter), not tetrahedral. The original 'tetrahedral complexes rarely show optical isomerism' reasoning was for the wrong geometry; the correct reason square-planar MABCD complexes are achiral is that the molecular plane itself is always a mirror plane. Also made explicit the isomer count (3) that the question asks for.
- **Found:**
  > $\left[\mathrm{Pt}\left(\mathrm{NH}_{3}\right)(\mathrm{Br})(\mathrm{Cl})(\mathrm{py})\right.$
  > 
  > 
  > 
  > From the above isomers, none will exhibit optical isomers. Tetrahedral complexes rarely show optical isomerization. They do so only in the presence of unsymmetrical chelating agents.
- **Should be:**
  > $\left[\mathrm{Pt}\left(\mathrm{NH}_{3}\right)(\mathrm{Br})(\mathrm{Cl})(\mathrm{py})\right]$ is a Pt(II), 4-coordinate complex, which (being a d8 metal ion) is square planar, not tetrahedral. A square planar MABCD complex (four different unidentate ligands) has 3 geometrical isomers, one for each possible pair of mutually trans ligands.
  > 
  > None of these three isomers exhibits optical isomerism: a square planar MABCD complex always retains the plane of the four ligands and the metal as a mirror plane, so it is superimposable on its own mirror image regardless of which ligands are trans to which.

### q_5.13 — solution (en)
- **Confidence:** high
- **Reason:** Mismatched bracket types (square open, round close) around H2O - an OCR artifact.
- **Found:**
  > the presence of $\left[\mathrm{Cu}\left[\mathrm{H}_{2} \mathrm{O}\right)_{4}\right]^{2+}$ ions.
- **Should be:**
  > the presence of $\left[\mathrm{Cu}\left(\mathrm{H}_{2} \mathrm{O}\right)_{4}\right]^{2+}$ ions.

### q_5.23 — parts[0].solution (en)
- **Confidence:** high
- **Reason:** Run-on line: 'x-6=-3 x' glued two separate equation lines ('x-6=-3' and 'x=+3') together.
- **Found:**
  > $$
  > \begin{aligned}
  > & x-6=-3 x \\
  > & =+3
  > \end{aligned}
  > $$
- **Should be:**
  > $$
  > \begin{aligned}
  > & x-6=-3 \\
  > & x=+3
  > \end{aligned}
  > $$

### q_5.23 — parts[2].solution (en)
- **Confidence:** high
- **Reason:** $(NH_4)_2[CoF_4]$ is 4-coordinate/tetrahedral (matches the coordination number of 4 already given two lines above in this same solution), so the orbital labels should be the tetrahedral e/t2 set, consistent with the fix already made to Ex 5.24(iv)'s Cs[FeCl4] (also tetrahedral) elsewhere in this chapter.
- **Found:**
  > The $d$ orbital occupation for $\mathrm{Co}^{2+}$ is $e_{g}{ }^{4} t_{2 \mathrm{~g}}{ }^{3 .}$
- **Should be:**
  > The $d$ orbital occupation for $\mathrm{Co}^{2+}$ is $e^{4} t_{2}{ }^{3}$ (tetrahedral splitting, so the plain $e/t_2$ labels apply, not the octahedral $e_g/t_{2g}$ labels).

### q_5.24 — parts[2].solution (en)
- **Confidence:** high
- **Reason:** Spelling fix: 'Meriodional' -> 'Meridional'.
- **Found:**
  > Meriodional isomer
- **Should be:**
  > Meridional isomer

### q_5.4 — parts[2].solution (en)
- **Confidence:** high
- **Reason:** The two examples were blank placeholders. Filled in with the textbook's own standard ambidentate-ligand examples (chapter.en.pdf p.121 gives NO2- and SCN- as its two examples of ambidentate ligands, with exactly these two donor-atom modes).
- **Found:**
  > Ligands that can attach themselves to the central metal atom through two different atoms are called ambidentate ligands. For example:
  > 
  > (a)
  > 
  > 
  > (b)
- **Should be:**
  > Ligands that can attach themselves to the central metal atom through two different atoms are called ambidentate ligands. For example:
  > 
  > (a) Nitrite ion, $\mathrm{NO}_{2}^{-}$: can coordinate either through the nitrogen atom (nitro, $-\mathrm{NO}_{2}$) or through an oxygen atom (nitrito, $-\mathrm{ONO}$).
  > 
  > (b) Thiocyanate ion, $\mathrm{SCN}^{-}$: can coordinate through the sulphur atom (thiocyanato, $-\mathrm{SCN}$) or through the nitrogen atom (isothiocyanato, $-\mathrm{NCS}$).

### q_5.11 — parts[2].solution (en)
- **Confidence:** high
- **Reason:** This part's solution had only the bare formula repeated, with no isomer analysis at all (unlike parts (i) and (ii) of the same question, which both give the isomer count and chirality). Completed following the identical pattern already used in this item's own parts (i)/(ii) for the analogous MA2B2(en) octahedral complexes: one achiral trans form + a chiral cis enantiomer pair = 3 stereoisomers total.
- **Found:**
  > $\left[\mathrm{Co}\left(\mathrm{NH}_{3}\right)_{2} \mathrm{Cl}_{2}(\mathrm{en})\right]^{+}$
- **Should be:**
  > $\left[\mathrm{Co}\left(\mathrm{NH}_{3}\right)_{2} \mathrm{Cl}_{2}(\mathrm{en})\right]^{+}$
  > 
  > The en ligand always spans two cis positions. Of the remaining four sites, the two Cl (and correspondingly the two NH3) can be arranged either cis or trans to each other, giving in total three stereoisomers:
  > 
  > Trans-$\left[\mathrm{Co}\left(\mathrm{NH}_{3}\right)_{2} \mathrm{Cl}_{2}(\mathrm{en})\right]^{+}$ (the two Cl trans to each other) - has a mirror plane, optically inactive.
  > 
  > Cis-$\left[\mathrm{Co}\left(\mathrm{NH}_{3}\right)_{2} \mathrm{Cl}_{2}(\mathrm{en})\right]^{+}$ (the two Cl cis to each other) - chiral, exists as a non-superimposable pair of optical isomers (d and l), optically active.

### q_5.8 — solution (en)
- **Confidence:** high
- **Reason:** The definition was given with no worked example, unlike every other isomerism type in this same solution. Added the textbook's own standard example of an octahedral optically-active complex.
- **Found:**
  > (b) Optical isomerism:
  > 
  > This type of isomerism arises in chiral molecules. Isomers are mirror images of each other and are non-superimposable.
- **Should be:**
  > (b) Optical isomerism:
  > 
  > This type of isomerism arises in chiral molecules. Isomers are mirror images of each other and are non-superimposable. For example, $\left[\mathrm{Co}(\mathrm{en})_{3}\right]^{3+}$ exists as a pair of non-superimposable mirror-image (d and l) forms.


---

## Third verification pass (it_5.4 CO/Co sweep, found during 09_design cross-check)

### it_5.4 — solution (en)
- **Confidence:** high
- **Reason:** CO/Co OCR confusion recurring in it_5.4, same pattern as it_5.1/it_5.3
- **Found:**
  > \left[\mathrm{CO}\left(\mathrm{NH}_{3}
ight)_{5} \mathrm{Cl}
ight] \mathrm{SO}_{4}+\mathrm{Ba}^{2+} \longrightarrow \mathrm{BaSO}_{4} \downarrow
- **Should be:**
  > \left[\mathrm{Co}\left(\mathrm{NH}_{3}
ight)_{5} \mathrm{Cl}
ight] \mathrm{SO}_{4}+\mathrm{Ba}^{2+} \longrightarrow \mathrm{BaSO}_{4} \downarrow

### it_5.4 — solution (en)
- **Confidence:** high
- **Reason:** CO/Co OCR confusion recurring in it_5.4
- **Found:**
  > \left[\mathrm{CO}\left(\mathrm{NH}_{3}
ight)_{5} \mathrm{Cl}
ight] \mathrm{SO}_{4}+\mathrm{Ag}^{+} \longrightarrow 	ext { No reaction }
- **Should be:**
  > \left[\mathrm{Co}\left(\mathrm{NH}_{3}
ight)_{5} \mathrm{Cl}
ight] \mathrm{SO}_{4}+\mathrm{Ag}^{+} \longrightarrow 	ext { No reaction }

### it_5.4 — solution (en)
- **Confidence:** high
- **Reason:** CO/Co OCR confusion recurring in it_5.4
- **Found:**
  > {\left[\mathrm{CO}\left(\mathrm{NH}_{3}
ight)_{5} \mathrm{SO}_{4}
ight] \mathrm{Cl}+\mathrm{Ba}^{2+} \longrightarrow 	ext { No reaction }}
- **Should be:**
  > {\left[\mathrm{Co}\left(\mathrm{NH}_{3}
ight)_{5} \mathrm{SO}_{4}
ight] \mathrm{Cl}+\mathrm{Ba}^{2+} \longrightarrow 	ext { No reaction }}

### it_5.4 — solution (en)
- **Confidence:** high
- **Reason:** CO/Co OCR confusion recurring in it_5.4
- **Found:**
  > {\left[\mathrm{CO}\left(\mathrm{NH}_{3}
ight)_{5} \mathrm{SO}_{4}
ight] \mathrm{Cl}+\mathrm{Ag}^{+} \longrightarrow \quad \mathrm{AgCl} \downarrow}
- **Should be:**
  > {\left[\mathrm{Co}\left(\mathrm{NH}_{3}
ight)_{5} \mathrm{SO}_{4}
ight] \mathrm{Cl}+\mathrm{Ag}^{+} \longrightarrow \quad \mathrm{AgCl} \downarrow}


---

## Third verification pass (it_5.4 CO/Co sweep, found during 09_design cross-check)

### it_5.4 — solution (en)
- **Confidence:** high
- **Reason:** CO/Co OCR confusion recurring in it_5.4, same pattern as it_5.1/it_5.3
- **Found:**
  > \left[\mathrm{CO}\left(\mathrm{NH}_{3}\right)_{5} \mathrm{Cl}\right] \mathrm{SO}_{4}+\mathrm{Ba}^{2+} \longrightarrow \mathrm{BaSO}_{4} \downarrow
- **Should be:**
  > \left[\mathrm{Co}\left(\mathrm{NH}_{3}\right)_{5} \mathrm{Cl}\right] \mathrm{SO}_{4}+\mathrm{Ba}^{2+} \longrightarrow \mathrm{BaSO}_{4} \downarrow

### it_5.4 — solution (en)
- **Confidence:** high
- **Reason:** CO/Co OCR confusion recurring in it_5.4
- **Found:**
  > \left[\mathrm{CO}\left(\mathrm{NH}_{3}\right)_{5} \mathrm{Cl}\right] \mathrm{SO}_{4}+\mathrm{Ag}^{+} \longrightarrow \text { No reaction }
- **Should be:**
  > \left[\mathrm{Co}\left(\mathrm{NH}_{3}\right)_{5} \mathrm{Cl}\right] \mathrm{SO}_{4}+\mathrm{Ag}^{+} \longrightarrow \text { No reaction }

### it_5.4 — solution (en)
- **Confidence:** high
- **Reason:** CO/Co OCR confusion recurring in it_5.4
- **Found:**
  > {\left[\mathrm{CO}\left(\mathrm{NH}_{3}\right)_{5} \mathrm{SO}_{4}\right] \mathrm{Cl}+\mathrm{Ba}^{2+} \longrightarrow \text { No reaction }}
- **Should be:**
  > {\left[\mathrm{Co}\left(\mathrm{NH}_{3}\right)_{5} \mathrm{SO}_{4}\right] \mathrm{Cl}+\mathrm{Ba}^{2+} \longrightarrow \text { No reaction }}

### it_5.4 — solution (en)
- **Confidence:** high
- **Reason:** CO/Co OCR confusion recurring in it_5.4
- **Found:**
  > {\left[\mathrm{CO}\left(\mathrm{NH}_{3}\right)_{5} \mathrm{SO}_{4}\right] \mathrm{Cl}+\mathrm{Ag}^{+} \longrightarrow \quad \mathrm{AgCl} \downarrow}
- **Should be:**
  > {\left[\mathrm{Co}\left(\mathrm{NH}_{3}\right)_{5} \mathrm{SO}_{4}\right] \mathrm{Cl}+\mathrm{Ag}^{+} \longrightarrow \quad \mathrm{AgCl} \downarrow}
