### it_4.8 — solution (en)
- **Confidence:** high
- **Reason:** Mathpix could not parse the orbital-filling box diagram (5 boxes: two with paired up/down arrows, three with single up arrows) and emitted meaningless digits instead. The source PDF page shows the diagram clearly and unambiguously.
- **Found:**
  > 3 d^{7}=44141414
- **Should be:**
  > 3 d^{7}=\uparrow\downarrow\quad\uparrow\downarrow\quad\uparrow\quad\uparrow\quad\uparrow

### q_4.1 — parts[5].solution (en)
- **Confidence:** high
- **Reason:** Mathpix OCR rendered this part's electron-configuration exponents (and the ion's own charge) as LaTeX subscripts instead of superscripts; every other part of this same question correctly uses superscripts, and the source PDF shows normal raised-superscript formatting throughout.
- **Found:**
  > $\mathrm{Lu}_{2+}$ : 1s2 $2 s_{2} 2 p_{6} 3 s_{2} 3 p_{6} 3 d_{10} 4 s_{2} 4 p_{6} 4 d_{10} 5 s_{2} 5 p_{6} 4 f_{14} 5 d_{1}$
- **Should be:**
  > $\mathrm{Lu}^{2+}$ : $1 s^{2} 2 s^{2} 2 p^{6} 3 s^{2} 3 p^{6} 3 d^{10} 4 s^{2} 4 p^{6} 4 d^{10} 5 s^{2} 5 p^{6} 4 f^{14} 5 d^{1}$

### q_4.1 — parts[7].solution (en)
- **Confidence:** high
- **Reason:** Same subscript/superscript OCR slip as parts[5], in the Th4+ configuration. The source PDF's own solution literally ends this configuration in "6s2 6s6" (not "6s2 6p6") - that is the source's own apparent error, preserved verbatim; only the sub/superscript formatting is fixed.
- **Found:**
  > $T h_{4+}$ : $1 s_{2} 2 s_{2} 2 p_{6} 3 s_{2} 3 p_{6} 3 d_{10} 4 s_{2} 4 p_{6} 4 d_{10} 4 f_{14} 5 s_{2} 5 p_{6} 5 d_{10} 6 s_{2} 6 s_{6}$ Or, $[\mathrm{Rn}]^{86}$
- **Should be:**
  > $\mathrm{Th}^{4+}$ : $1 s^{2} 2 s^{2} 2 p^{6} 3 s^{2} 3 p^{6} 3 d^{10} 4 s^{2} 4 p^{6} 4 d^{10} 4 f^{14} 5 s^{2} 5 p^{6} 5 d^{10} 6 s^{2} 6 s^{6}$ Or, $[\mathrm{Rn}]^{86}$

### q_4.3 — solution (en)
- **Confidence:** high
- **Reason:** Mathpix garbled the oxidation-state table into 3 disconnected `$$...$$` blocks with a stray "Oxidation state" caption wedged between two of them, and lost the column alignment entirely (making it impossible to tell which value belongs to which element). Verified directly against solutions.en.pdf page 6 (1-indexed) at high resolution, fully legible: Sc has only +3; Ti/V/Cr/Mn each have +2/+3/+4; V and Cr also have +5 (Mn has no +5, skipping straight to +6); Cr also has +6, Mn also has +7. This matches the standard NCERT table for this question.
- **Found:**
  > $$
  > \begin{array}{rrrr}
  > \mathbf{S C} \mathbf{T i} & \mathbf{V} & \mathbf{C r} & \mathbf{M n} \\
  > +2+2 & +2 & +2 \\
  > +3+3 & +3 & +3 & +3
  > \end{array}
  > $$
  > 
  > Oxidation state
  > 
  > $$
  > +4+4+4+4
  > $$
  > 
  > $$
  > \begin{array}{r}
  > +5+5+6 \\
  > +6+7
  > \end{array}
  > $$
- **Should be:**
  > | Oxidation state | Sc | Ti | V | Cr | Mn |
  > | :--- | :--- | :--- | :--- | :--- | :--- |
  > |  |  | +2 | +2 | +2 | +2 |
  > |  | +3 | +3 | +3 | +3 | +3 |
  > |  |  | +4 | +4 | +4 | +4 |
  > |  |  |  | +5 | +5 | +6 |
  > |  |  |  |  | +6 | +7 |

### q_4.15 — parts[0].solution (en)
- **Confidence:** high
- **Reason:** OCR truncated "medium" to "med" and dropped the sentence's closing period.
- **Found:**
  > acidic med }
- **Should be:**
  > acidic medium. }

### q_4.20 — parts[3].solution (en)
- **Confidence:** high
- **Reason:** OCR misread the element symbol "Al" (aluminium) as "AI" (capital i).
- **Found:**
  > similar to AI.
- **Should be:**
  > similar to Al.

### q_4.38 — question (en)
- **Confidence:** high
- **Reason:** Mathpix produced mismatched delimiters - a `\left[` opened for K4[Mn(CN)6] is closed with `\right)` instead of `\right]`. The chapter PDF shows a plain square-bracketed formula with no parenthesis anywhere near that position.
- **Found:**
  > \left[\mathrm{Mn}(\mathrm{CN})_{6}\right)
- **Should be:**
  > \left[\mathrm{Mn}(\mathrm{CN})_{6}\right]


---

## Structural fixes (not expressible as found/should_be corrections)

### q_4.15 — parts[1] ("(ii)") solution (en) — MISSING SUB-PART, ADDED
- **Confidence:** high
- **Reason:** This part's solution was entirely absent from extraction (empty `:::solution` in stage 2/4), previously believed to be a genuine gap in the solutions manual, but confirmed present and fully legible on solutions.en.pdf page 13 (1-indexed) during stage-5 verification. Per step_5/verify.md's own rule, a missing sub-part has no field to correct into via found/should_be - spliced in directly instead.
- **Added:**
  > $\mathrm{K}_{2} \mathrm{Cr}_{2} \mathrm{O}_{7}$ oxidizes iron (II) solution to iron (III) solution i.e., ferrous ions to ferric ions.
  >
  > $$
  > \begin{aligned}
  > & \mathrm{Cr}_{2} \mathrm{O}_{7}^{2-}+14 \mathrm{H}^{+}+6 \mathrm{e}^{-} \longrightarrow 2 \mathrm{Cr}^{3+}+7 \mathrm{H}_{2} \mathrm{O} \\
  > & \mathrm{Fe}^{2+}\left.\longrightarrow \mathrm{Fe}^{3+}+\mathrm{e}^{-}\right] \times 6 \\
  > & \hline \mathrm{Cr}_{2} \mathrm{O}_{7}^{2-}+14 \mathrm{H}^{+}+6 \mathrm{Fe}^{2+} \longrightarrow 2 \mathrm{Cr}^{3+}+6 \mathrm{Fe}^{3+}+7 \mathrm{H}_{2} \mathrm{O} \\
  > & \hline
  > \end{aligned}
  > $$

### q_4.20 — parts[1]/[2] ("(ii)"/"(iii)") solutions (en) — SWAPPED, CORRECTED
- **Confidence:** high
- **Reason:** The solutions manual's own answer labels its two sub-answers in the reverse order from the textbook question's own part ordering (question: (ii) atomic and ionic sizes, (iii) oxidation state; solutions manual: answers oxidation states before atomic/ionic sizes) - whatever process joined solution content to question parts by position inherited this reversal, attaching each answer to the wrong part. Swapped part (ii)'s and part (iii)'s solution content between each other so each now matches its own label.

---

## Retroactive fix pass (external review, session 2026-09-28)

### q_4.31 — solution (en)
- **Confidence:** high
- **Reason:** The question asks for Ce3+'s own configuration, but the solution derives n from the NEUTRAL Ce atom's 4f^1 5d^1 (n=2). Removing 3 electrons from neutral Ce ([Xe]4f^1 5d^1 6s^2) takes the 6s^2 and 5d^1 first, leaving Ce3+ = [Xe]4f^1 (independently re-derived), i.e. only 1 unpaired electron.
- **Found:**
  > $$
  > \mathrm{Ce}: 1 s^{2} 2 s^{2} 2 p^{6} 3 s^{2} 3 p^{6} 3 d^{10} 4 s^{2} 4 p^{6} 4 d^{10} 5 s^{2} 5 p^{6} 4 f^{1} 5 d^{1} 6 s^{2}
  > $$
  > 
  > Magnetic moment can be calculated as:
  > 
  > $$
  > \mu=\sqrt{n(n+2)}
  > $$
  > 
  > Where,
  > $n=$ number of unpaired electrons
  > 
  > In Ce, $n=2$
  > Therefore, $\mu=\sqrt{2(2+2)}$
  > 
  > $$
  > \begin{aligned}
  > & =\sqrt{2 \times 4} \\
  > & =\sqrt{8} \\
  > & =2 \sqrt{2} \\
  > & =2.828 \mathrm{BM}
  > \end{aligned}
  > $$
- **Should be:**
  > $$
  > \begin{aligned}
  > & \mathrm{Ce}: 1 s^{2} 2 s^{2} 2 p^{6} 3 s^{2} 3 p^{6} 3 d^{10} 4 s^{2} 4 p^{6} 4 d^{10} 5 s^{2} 5 p^{6} 4 f^{1} 5 d^{1} 6 s^{2} \\
  > & \mathrm{Ce}^{3+}: 1 s^{2} 2 s^{2} 2 p^{6} 3 s^{2} 3 p^{6} 3 d^{10} 4 s^{2} 4 p^{6} 4 d^{10} 5 s^{2} 5 p^{6} 4 f^{1}
  > \end{aligned}
  > $$
  > 
  > Removing 3 electrons from neutral Ce (the two 6s electrons and the one 5d electron) leaves Ce3+ with one unpaired 4f electron (Hund's rule).
  > 
  > Magnetic moment can be calculated as:
  > 
  > $$
  > \mu=\sqrt{n(n+2)}
  > $$
  > 
  > Where,
  > $n=$ number of unpaired electrons
  > 
  > In Ce3+, $n=1$
  > Therefore, $\mu=\sqrt{1(1+2)}$
  > 
  > $$
  > \begin{aligned}
  > & =\sqrt{1 \times 3} \\
  > & =\sqrt{3} \\
  > & =1.73 \mathrm{BM}
  > \end{aligned}
  > $$

### q_4.16 — parts[1].solution (en)
- **Confidence:** high
- **Reason:** The given MnO4-/Mn2+ half-reaction here (6H+/3H2O) does not balance O or charge; the correct half-reaction (used correctly elsewhere in this same item) is 8H+/4H2O. The SO2 half-reaction wrongly includes an extra O2 term and does not balance; the correct half-reaction is SO2 + 2H2O -> SO4^2- + 4H+ + 2e- (independently balanced: O 4=4, H 4=4, charge 0=0). Re-combining with the correct 2:5 electron ratio gives 2MnO4- + 5SO2 + 2H2O -> 2Mn2+ + 5SO4^2- + 4H+ (independently verified: Mn 2=2, S 5=5, O 20=20, H 4=4, charge -2=-2), matching the standard textbook equation for this titration.
- **Found:**
  > Acidified potassium permanganate oxidizes $\mathrm{SO}_{2}$ to sulphuric acid.
  > $$
  > \begin{aligned}
  > & \mathrm{MnO}_{4}^{-}+6 \mathrm{H}^{+}+5 \mathrm{e}^{-}\left.\longrightarrow \mathrm{Mn}^{2+}+3 \mathrm{H}_{2} \mathrm{O}\right] \times 2 \\
  > & 2 \mathrm{H}_{2} \mathrm{O}+2 \mathrm{SO}_{2}+\mathrm{O}_{2}\left.\longrightarrow 4 \mathrm{H}^{+}+2 \mathrm{SO}_{4}^{2-}+2 \mathrm{e}^{-}\right] \times 5 \\
  > & \hline 2 \mathrm{MnO}_{4}^{-}+10 \mathrm{SO}_{2}+5 \mathrm{O}_{2}+4 \mathrm{H}_{2} \mathrm{O} \longrightarrow 2 \mathrm{Mn}^{2+}+10 \mathrm{SO}_{4}^{2-}+8 \mathrm{H}^{+} \\
  > & \hline
  > \end{aligned}
  > $$
- **Should be:**
  > Acidified potassium permanganate oxidizes $\mathrm{SO}_{2}$ to sulphuric acid.
  > $$
  > \begin{aligned}
  > & \left.\mathrm{MnO}_{4}^{-}+8 \mathrm{H}^{+}+5 \mathrm{e}^{-} \longrightarrow \mathrm{Mn}^{2+}+4 \mathrm{H}_{2} \mathrm{O}\right] \times 2 \\
  > & \left.\mathrm{SO}_{2}+2 \mathrm{H}_{2} \mathrm{O} \longrightarrow \mathrm{SO}_{4}^{2-}+4 \mathrm{H}^{+}+2 \mathrm{e}^{-}\right] \times 5 \\
  > & \hline 2 \mathrm{MnO}_{4}^{-}+5 \mathrm{SO}_{2}+2 \mathrm{H}_{2} \mathrm{O} \longrightarrow 2 \mathrm{Mn}^{2+}+5 \mathrm{SO}_{4}^{2-}+4 \mathrm{H}^{+} \\
  > & \hline
  > \end{aligned}
  > $$

### q_4.16 — solution (en)
- **Confidence:** high
- **Reason:** The ozone-oxidation equation shows the same species (MnO4^2-) as both reactant and product; manganate is oxidised to PERMANGANATE (MnO4^-), a different ion/oxidation state, matching the immediately preceding molecular equation in this same solution (2K2MnO4+O3+H2O -> 2KMnO4+2KOH+O2) and independently charge/atom-balanced (O: 8+3+1=12 both sides; charge -4=-4).
- **Found:**
  > 2 \mathrm{MnO}_{4}^{2-}+\mathrm{O}_{3}+\mathrm{H}_{2} \mathrm{O} \longrightarrow 2 \mathrm{MnO}_{4}^{2-}+2 \mathrm{OH}^{-}+\mathrm{O}_{2}
- **Should be:**
  > 2 \mathrm{MnO}_{4}^{2-}+\mathrm{O}_{3}+\mathrm{H}_{2} \mathrm{O} \longrightarrow 2 \mathrm{MnO}_{4}^{-}+2 \mathrm{OH}^{-}+\mathrm{O}_{2}

### q_4.26 — parts[1].solution (en)
- **Confidence:** high
- **Reason:** Same duplicate-species error as q_4.16's identical passage; manganate is oxidised to permanganate (MnO4^-), independently balanced (see q_4.16 correction).
- **Found:**
  > 2 \mathrm{MnO}_{4}^{2-}+\mathrm{O}_{3}+\mathrm{H}_{2} \mathrm{O} \longrightarrow 2 \mathrm{MnO}_{4}^{2-}+2 \mathrm{OH}^{-}+\mathrm{O}_{2}
- **Should be:**
  > 2 \mathrm{MnO}_{4}^{2-}+\mathrm{O}_{3}+\mathrm{H}_{2} \mathrm{O} \longrightarrow 2 \mathrm{MnO}_{4}^{-}+2 \mathrm{OH}^{-}+\mathrm{O}_{2}

### it_4.8 — solution (en)
- **Confidence:** high
- **Reason:** sqrt(15) = 3.872..., i.e. 3.87 BM (matches this chapter's own q_4.38, which computes the same sqrt(15)=3.87 correctly) - rounding it to a bare '4 BM' loses precision without reason.
- **Found:**
  > \mu \approx 4 \mathrm{BM}
- **Should be:**
  > \mu \approx 3.87 \mathrm{BM}

### q_4.1 — parts[1].solution (en)
- **Confidence:** high
- **Reason:** Pm (Z=61) neutral is [Xe]4f^5 6s^2; Pm3+ removes the 6s^2 and one 4f electron, giving [Xe]4f^4 (matches the long form already correctly given in this same line) - the short-form line wrongly copies '3d^3' from the Cr3+ answer above it.
- **Found:**
  > Or, $[\mathrm{Xe}]^{54} 3 d^{3}$
- **Should be:**
  > Or, $[\mathrm{Xe}]^{54} 4 f^{4}$

### q_4.1 — parts[5].solution (en)
- **Confidence:** high
- **Reason:** Lu (Z=71) neutral is [Xe]4f^14 5d^1 6s^2; Lu2+ removes the 6s^2, leaving [Xe]4f^14 5d^1 (matches the long form already correctly given in this same line) - the short-form wrongly reads '2f^14 3d^3'.
- **Found:**
  > Or, $[\mathrm{Xe}]^{54} 2 f^{14} 3 d^{3}$
- **Should be:**
  > Or, $[\mathrm{Xe}]^{54} 4 f^{14} 5 d^{1}$

### q_4.1 — parts[7].solution (en)
- **Confidence:** high
- **Reason:** Th4+ is [Rn] (86 electrons, matching the 'Or, [Rn]^86' given right after) - the long form's own electron count only reaches 86 if the last shell reads 6p^6, not a duplicated '6s^6' (Rn's own configuration ends ...5d^10 6s^2 6p^6).
- **Found:**
  > 6 s^{2} 6 s^{6}$ Or, $[\mathrm{Rn}]^{86}$
- **Should be:**
  > 6 s^{2} 6 p^{6}$ Or, $[\mathrm{Rn}]^{86}$

### q_4.17 — question (en)
- **Confidence:** high
- **Reason:** OCR dropped the '+' superscript on Cr3+ in this data row; every other row/column in this same table correctly shows the ion charge (Cr2+/Cr, Mn3+/Mn2+, etc.), and the standard published E-values for this exact exercise are Cr3+/Cr2+ = -0.4 V.
- **Found:**
  > \mathrm{Cr}^{3} / \mathrm{Cr}^{2+}
- **Should be:**
  > \mathrm{Cr}^{3+} / \mathrm{Cr}^{2+}

### q_4.17 — parts[0].solution (en)
- **Confidence:** high
- **Reason:** A higher (more positive) E-degree means the ion is MORE easily reduced (less stable), not more stable. Given Cr3+/Cr2+=-0.4V < Fe3+/Fe2+=+0.8V < Mn3+/Mn2+=+1.5V, Mn3+ is reduced most easily (least stable) and Cr3+ least easily (most stable) - the opposite of what the original explanation's 'easier than'/'not as easy as' comparisons said, even though its final stated order (Mn3+<Fe3+<Cr3+ stability) was already correct.
- **Found:**
  > The ${ }^{\ominus}$ value for $\mathrm{Fe}^{3+} / \mathrm{Fe}^{2+}$ is higher than that for $\mathrm{Cr}^{3+} / \mathrm{Cr}^{2+}$ and lower than that for $\mathrm{Mn}^{3+} / \mathrm{Mn}^{2+}$. So, the reduction of $\mathrm{Fe}^{3+}$ to $\mathrm{Fe}^{2+}$ is easier than the reduction of $\mathrm{Mn}^{3+}$ to $\mathrm{Mn}^{2+}$, but not as easy as the reduction of $\mathrm{Cr}^{3+}$ to $\mathrm{Cr}^{2+}$. Hence, $\mathrm{Fe}^{3+}$ is more stable than $\mathrm{Mn}^{3+}$, but less stable than $\mathrm{Cr}^{3+}$. These metal ions can be arranged in the increasing order of their stability as: $\mathrm{Mn}^{3+}<\mathrm{Fe}^{3+}<\mathrm{Cr}^{3+}$
- **Should be:**
  > The $E^{\ominus}$ value for $\mathrm{Fe}^{3+} / \mathrm{Fe}^{2+}$ is higher than that for $\mathrm{Cr}^{3+} / \mathrm{Cr}^{2+}$ and lower than that for $\mathrm{Mn}^{3+} / \mathrm{Mn}^{2+}$. A higher (more positive) value means the ion is reduced more easily, so $\mathrm{Mn}^{3+}$ is reduced to $\mathrm{Mn}^{2+}$ most easily, $\mathrm{Fe}^{3+}$ to $\mathrm{Fe}^{2+}$ less easily, and $\mathrm{Cr}^{3+}$ to $\mathrm{Cr}^{2+}$ least easily of the three. Hence, $\mathrm{Cr}^{3+}$ is the most stable of the three ions in acid solution, $\mathrm{Fe}^{3+}$ is next, and $\mathrm{Mn}^{3+}$ is the least stable. These metal ions can be arranged in the increasing order of their stability as: $\mathrm{Mn}^{3+}<\mathrm{Fe}^{3+}<\mathrm{Cr}^{3+}$

### q_4.18 — solution (en)
- **Confidence:** high
- **Reason:** Colour requires a PARTIALLY filled d-subshell (d-d transitions); an empty (d0) or completely filled (d10) d-subshell gives no d-d transition and is colourless - the original rule ('electrons in d-orbital') is imprecise and its own table shows Cu+ as 3d10 (full), which the conclusion then wrongly calls coloured. Also fixes table typos ('T 1^{3+}'->'Ti^{3+}', subscript->superscript on V) and the stray duplicate ':--- ' header-separator row merged into the table body.
- **Found:**
  > Only the ions that have electrons in $d$-orbital will be coloured. The ions in which $d$-orbital is empty will be colourless.
  > 
  > | Element | Atomic Number | Ionic State | Electronic configuration in ionic state |
  > | :--- | :--- | :--- | :--- |
  > 
  > 
  > | Ti | 22 | $\mathrm{T} 1^{3+}$ | $[\mathrm{Ar}] 3 d^{1}$ |
  > | :--- | :--- | :--- | :--- |
  > | V | 23 | $\mathrm{V}_{3+}$ | $[\mathrm{Ar}] 3 d^{2}$ |
  > | Cu | 29 | $\mathrm{Cu}^{+}$ | $[\mathrm{Ar}] 3 d^{10}$ |
  > | Sc | 21 | $\mathrm{Sc}^{3+}$ | [Ar] |
  > | Mn | 25 | $\mathrm{Mn}^{2+}$ | $[\mathrm{Ar}] 3 d^{5}$ |
  > | Fe | 26 | $\mathrm{Fe}^{3+}$ | $[\mathrm{Ar}] 3 d^{5}$ |
  > | Co | 27 | $\mathrm{Co}^{2+}$ | $[\mathrm{Ar}] 3 d^{7}$ |
  > 
  > From the above table, it can be easily observed that only $\mathrm{Sc}^{3+}$ has an empty $d$-orbital. All other ions, except $\mathrm{Sc}^{3+}$, will be coloured in aqueous solution because of $d-d$ transitions.
- **Should be:**
  > Colour comes from d-d transitions, which need a partially filled $d$-orbital: an ion with an empty or completely filled $d$-subshell is colourless.
  > 
  > | Element | Atomic Number | Ionic State | Electronic configuration in ionic state |
  > | :--- | :--- | :--- | :--- |
  > 
  > 
  > | Ti | 22 | $\mathrm{Ti}^{3+}$ | $[\mathrm{Ar}] 3 d^{1}$ |
  > | V | 23 | $\mathrm{V}^{3+}$ | $[\mathrm{Ar}] 3 d^{2}$ |
  > | Cu | 29 | $\mathrm{Cu}^{+}$ | $[\mathrm{Ar}] 3 d^{10}$ |
  > | Sc | 21 | $\mathrm{Sc}^{3+}$ | [Ar] |
  > | Mn | 25 | $\mathrm{Mn}^{2+}$ | $[\mathrm{Ar}] 3 d^{5}$ |
  > | Fe | 26 | $\mathrm{Fe}^{3+}$ | $[\mathrm{Ar}] 3 d^{5}$ |
  > | Co | 27 | $\mathrm{Co}^{2+}$ | $[\mathrm{Ar}] 3 d^{7}$ |
  > 
  > From the table, $\mathrm{Sc}^{3+}$ and $\mathrm{Cu}^{+}$ have no partially filled $d$-orbital (empty or full), so both are colourless; the rest are coloured because of d-d transitions in a partially filled $d$-subshell.

### q_4.7 — solution (en)
- **Confidence:** high
- **Reason:** Lanthanoid contraction makes the lanthanoids' sizes (and therefore properties) nearly identical to one another, which makes separating them from each other HARDER, not possible/easier - the original text has this backwards. This also fixes the literal '## ' markdown heading printed as visible text and a stray leftover 'ii.' numbering artifact.
- **Found:**
  > ## Consequences of lanthanoid contraction
  > 
  > (i) There is similarity in the properties of second and third transition series. ii.
  > 
  > Separation of lanthanoids is possible due to lanthanide contraction.
  > (iii) It is due to lanthanide contraction that there is variation in the basic strength of lanthanide hydroxides. (Basic strength decreases from $\mathrm{La}(\mathrm{OH})_{3}$ to $\mathrm{Lu}(\mathrm{OH})_{3}$.)
- **Should be:**
  > **Consequences of lanthanoid contraction:**
  > 
  > (i) There is similarity in the properties of the second and third transition series.
  > (ii) Lanthanoid contraction makes the lanthanoids so close to one another in size and properties that separating them from each other is difficult.
  > (iii) It is due to lanthanoid contraction that there is variation in the basic strength of lanthanoid hydroxides. (Basic strength decreases from $\mathrm{La}(\mathrm{OH})_{3}$ to $\mathrm{Lu}(\mathrm{OH})_{3}$.)

### q_4.33 — solution (en)
- **Confidence:** high
- **Reason:** Literal markdown heading syntax leaked into solution prose (heading-bleed artefact, same class as chemistry-12-2's q_2.7 fix) - render as bold inline labels, not raw '##'.
- **Found:**
  > ## Electronic configuration
- **Should be:**
  > **Electronic configuration:**

### q_4.33 — solution (en)
- **Confidence:** high
- **Reason:** Same heading-bleed artefact.
- **Found:**
  > ## Oxidation states
- **Should be:**
  > **Oxidation states:**

### q_4.33 — solution (en)
- **Confidence:** high
- **Reason:** Same heading-bleed artefact.
- **Found:**
  > ## Chemical reactivity
- **Should be:**
  > **Chemical reactivity:**

### q_4.14 — solution (en)
- **Confidence:** high
- **Reason:** Per the textbook's own preparation passage: 'Sodium dichromate is more soluble than potassium dichromate. The latter is therefore prepared by treating the solution of sodium dichromate with potassium chloride... Orange crystals of potassium dichromate crystallise out.' The crystallising orange solid is potassium DICHROMATE, not potassium chloride, and the relevant solubility comparison is between the two dichromates, not the two chlorides.
- **Found:**
  > Potassium chloride being less soluble than sodium chloride is obtained in the form of orange coloured crystals and can be removed by filtration.
- **Should be:**
  > Sodium dichromate is more soluble than potassium dichromate, so orange crystals of potassium dichromate crystallise out of the solution and can be removed by filtration.

### q_4.14 — solution (en)
- **Confidence:** high
- **Reason:** This question has two parts; the second ('effect of increasing pH') was never answered, and the equilibrium itself was garbled OCR. Per the textbook's own equations (2CrO4^2- + 2H+ -> Cr2O7^2- + H2O; Cr2O7^2- + 2OH- -> 2CrO4^2- + H2O), increasing pH (making the solution more alkaline) shifts the equilibrium towards chromate (yellow); independently balanced (O: 8+2=10 vs 7+2+1=10; charge -4-2=-6 vs -2 for the first; similarly for the second).
- **Found:**
  > The dichromate ion $\left(\mathrm{Cr}_{2} \mathrm{O}_{7}^{2-}\right)$ exists in equilibrium with chromate $\left(\mathrm{CrO}_{4}^{2-}\right)_{\text {ion at } \mathrm{pH} 4}$. However, by changing the pH , they can be interconverted.
  > 
  > $$
  > 2 \mathrm{CrO}_{4}^{2-} \hat{ \pm}_{\text {Alkali }}^{2 \text { alaid }} 2 \mathrm{HCrO}_{4}^{-} \quad \hat{ \pm}_{\text {Alkalt }}^{\text {2ladat }} \mathrm{Cr}_{2} \mathrm{O}_{7}^{2-}
  > $$
  > 
  > | Chromate | Hydrogen | Dichromate |
  > | :--- | :--- | :--- |
  > | (Yellow) | chromate | (Orange) |
- **Should be:**
  > The chromate ($\mathrm{CrO}_{4}^{2-}$, yellow) and dichromate ($\mathrm{Cr}_{2} \mathrm{O}_{7}^{2-}$, orange) ions are interconvertible in aqueous solution, depending on the pH.
  > 
  > $$
  > \begin{aligned}
  > & 2 \mathrm{CrO}_{4}^{2-}+2 \mathrm{H}^{+} \longrightarrow \mathrm{Cr}_{2} \mathrm{O}_{7}^{2-}+\mathrm{H}_{2} \mathrm{O} \\
  > & \mathrm{Cr}_{2} \mathrm{O}_{7}^{2-}+2 \mathrm{OH}^{-} \longrightarrow 2 \mathrm{CrO}_{4}^{2-}+\mathrm{H}_{2} \mathrm{O}
  > \end{aligned}
  > $$
  > 
  > Increasing the pH (making the solution more alkaline) shifts the equilibrium towards chromate, turning the solution yellow; decreasing it (acidifying) shifts it back towards dichromate, turning it orange.
  > 
  > | Chromate | Dichromate |
  > | :--- | :--- |
  > | (Yellow) | (Orange) |

### q_4.26 — parts[0].solution (en)
- **Confidence:** high
- **Reason:** Same wrong potassium-chloride-solubility claim as q_4.14's identical passage - see that correction's reasoning.
- **Found:**
  > Potassium chloride being less soluble than sodium chloride is obtained in the form of orange coloured crystals and can be removed by filtration.
- **Should be:**
  > Sodium dichromate is more soluble than potassium dichromate, so orange crystals of potassium dichromate crystallise out of the solution and can be removed by filtration.

### q_4.26 — parts[0].solution (en)
- **Confidence:** high
- **Reason:** Same garbled chromate/dichromate equilibrium block as q_4.14 (plus a stray unmatched '(Yellow' line) - replaced with the textbook's own balanced interconversion equations.
- **Found:**
  > $$
  > \begin{array}{llcl}
  > 2 \mathrm{CrO}_{4}^{2-} & \stackrel{\text { Acid }}{\text { Alkali }} & 2 \mathrm{HCrO}_{4}^{-} & \stackrel{\text { Acid }}{\leftrightarrow} \\
  > \text { Chromate } & & \text { Hydrogen } & \\
  > \text { (Yellow) } & & \text { chromate } & \\
  > \text { (Yellow } & & \text { Dichromate } \\
  > \text { (Orange) } &
  > \end{array}
  > $$
- **Should be:**
  > $$
  > \begin{aligned}
  > & 2 \mathrm{CrO}_{4}^{2-}+2 \mathrm{H}^{+} \longrightarrow \mathrm{Cr}_{2} \mathrm{O}_{7}^{2-}+\mathrm{H}_{2} \mathrm{O} \\
  > & \mathrm{Cr}_{2} \mathrm{O}_{7}^{2-}+2 \mathrm{OH}^{-} \longrightarrow 2 \mathrm{CrO}_{4}^{2-}+\mathrm{H}_{2} \mathrm{O}
  > \end{aligned}
  > $$

### q_4.20 — parts[3].solution (en)
- **Confidence:** high
- **Reason:** Per the textbook's own text: 'Hydrochloric acid attacks all metals but most are slightly affected by nitric acid owing to the formation of protective oxide layers' - the original wrongly implies only nitric acid affects actinoids at all.
- **Found:**
  > In case of acids, they are slightly affected by nitric acid (because of the formation of a protective oxide layer).
- **Should be:**
  > Hydrochloric acid attacks all of them, but most are only slightly affected by nitric acid because of the formation of a protective oxide layer.

### q_4.33 — solution (en)
- **Confidence:** high
- **Reason:** Same fix as q_4.20(iv), same textbook passage.
- **Found:**
  > In case of acids, they are slightly affected by nitric acid (because of the formation of a protective oxide layer).
- **Should be:**
  > Hydrochloric acid attacks all of them, but most are only slightly affected by nitric acid because of the formation of a protective oxide layer.

### q_4.5 — solution (en)
- **Confidence:** high
- **Reason:** V (Z=23, 3d3 4s2) most stable oxidation state is +5, not a list. 3d5 belongs to both Cr (Z=24) and Mn (Z=25): Cr's most stable state is +3 (not +6, despite the noble-gas-like d0 argument - Cr3+ is far more kinetically/thermodynamically stable in practice than Cr6+), Mn's is +2 (half-filled d5). 3d8 is Ni (Z=28, [Ar]3d8 4s2), NOT Co (Co is Z=27, [Ar]3d7 4s2, i.e. 3d7) - Co's own d-count doesn't match this row at all. Independently re-derived from atomic numbers/configurations.
- **Found:**
  > | (i) | $3 d^{3}$ (Vanadium) | +2, +3, +4 and +5 |
- **Should be:**
  > | (i) | $3 d^{3}$ (Vanadium) | +5 |

### q_4.5 — solution (en)
- **Confidence:** high
- **Reason:** See above: Cr's stable state is +3, Mn's is +2, 3d8 is Nickel (not Cobalt, which is 3d7) - this also removes the stray duplicate ':--- ' header-separator row and the missing space in 'no3d'.
- **Found:**
  > | (ii) | $3 d^{5}$ (Chromium) | +3, +4, +6 |
  > | :--- | :--- | :--- |
  > | (iii) | $3 d^{5}$ (Manganese) | +2, +4, +6, +7 |
  > | (iv) | $3 d^{8}$ (Cobalt) | +2, +3 |
  > | (v) | $3 d^{4}$ | There is no3d ${ }^{4}$ configuration in ground state. |
- **Should be:**
  > | (ii) | $3 d^{5}$ (Chromium) | +3 |
  > | (iii) | $3 d^{5}$ (Manganese) | +2 |
  > | (iv) | $3 d^{8}$ (Nickel) | +2 |
  > | (v) | $3 d^{4}$ | There is no $3 d^{4}$ configuration in the ground state of any transition element. |

### q_4.34 — solution (en)
- **Confidence:** high
- **Reason:** Element 101 is Md (Mendelevium), an actinoid - actinoids fill the 6d subshell (like Z=91's own row in this same table, 6d^1), not 5d (which belongs to the lanthanoid/6th-period-d-block shell already used correctly in the Z=61 row above). This also removes the stray duplicate ':--- ' separator row.
- **Found:**
  > | 91 | $[\mathrm{Rn}]^{86} 5 f^{2} 6 d^{1} 7 s^{2}$ |
  > | :--- | :--- |
  > | 101 | $[\mathrm{Rn}]^{86} 5 f^{13} 5 d^{0} 7 s^{2}$ |
- **Should be:**
  > | 91 | $[\mathrm{Rn}]^{86} 5 f^{2} 6 d^{1} 7 s^{2}$ |
  > | 101 | $[\mathrm{Rn}]^{86} 5 f^{13} 6 d^{0} 7 s^{2}$ |

### q_4.35 — parts[0].solution (en)
- **Confidence:** high
- **Reason:** The textbook's own Table 4.1 shows Cr and Cu with 4s^1 (a stray OCR prime mark, not superscript 1, crept in here).
- **Found:**
  > \operatorname{Cr}(24)=3 d^{5} 4 s^{\prime} \\
  > & \operatorname{Cu}(29)=3 d^{10} 4 s^{\prime}
- **Should be:**
  > \operatorname{Cr}(24)=3 d^{5} 4 s^{1} \\
  > & \operatorname{Cu}(29)=3 d^{10} 4 s^{1}

### q_4.35 — parts[0].solution (en)
- **Confidence:** high
- **Reason:** Per the textbook's own Table 4.1, Nb (Z=41) is 5s^1 4d^4 - an exception to the normal filling order just like Mo-Ag - but is missing from this list.
- **Found:**
  > & \operatorname{Mo}(42)=4 d^{5} 5 s^{1}
- **Should be:**
  > & \operatorname{Nb}(41)=4 d^{4} 5 s^{1} \\
  > & \operatorname{Mo}(42)=4 d^{5} 5 s^{1}

### q_4.35 — parts[0].solution (en)
- **Confidence:** high
- **Reason:** Per the textbook's own Table 4.1, W (Z=74) is 5d^4 6s^2 - exactly the NORMAL expected filling for that position (not an exception at all); only Pt and Au deviate from the normal pattern in the third series.
- **Found:**
  > \mathrm{W}(74)=5 d^{4} 6 s^{2} \\
  > & \mathrm{Pt}(78)=5 d^{9} 6 s^{1}
- **Should be:**
  > \mathrm{Pt}(78)=5 d^{9} 6 s^{1}

### q_4.35 — parts[1].solution (en)
- **Confidence:** high
- **Reason:** 'In' (Indium) is a p-block element, not a transition metal, and doesn't belong in this list of second/third-series transition metals; 'Ir' (Iridium) fits the context. Also fixes a bracket-notation typo, Cn -> CN.
- **Found:**
  > \left[\mathrm{Fe}(\mathrm{Cn})_{6}\right]^{4-}
- **Should be:**
  > \left[\mathrm{Fe}(\mathrm{CN})_{6}\right]^{4-}

### q_4.35 — parts[1].solution (en)
- **Confidence:** high
- **Reason:** 'In' (Indium, p-block) does not belong in this list of second/third-series transition metals; 'Ir' (Iridium) does.
- **Found:**
  > such as Mo, W, Rh, In.
- **Should be:**
  > such as Mo, W, Rh, Ir.

### q_4.19 — solution (en)
- **Confidence:** high
- **Reason:** Removes the stray duplicate ':--- ' header-separator row that had been merged into the middle of this oxidation-states table (it printed as literal ':--- ' text between Fe and Co).
- **Found:**
  > | Fe | +1 | +2 | +3 | +4 | +5 | +6 |  |
  > 
  > 
  > | Co | +1 | +2 | +3 | +4 | +5 |  |  |
  > | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
  > | Ni | +1 | +2 | +3 | +4 |  |  |  |
- **Should be:**
  > | Fe | +1 | +2 | +3 | +4 | +5 | +6 |  |
  > 
  > 
  > | Co | +1 | +2 | +3 | +4 | +5 |  |  |
  > | Ni | +1 | +2 | +3 | +4 |  |  |  |

### q_4.24 — solution (en)
- **Confidence:** high
- **Reason:** This is the 4th row of the table (after (i)(ii)(iii)) - labelled '(vi)' by mistake, should be '(iv)'.
- **Found:**
  > | (vi) | $\mathrm{Ti}^{3+},[\mathrm{Ar}] 3 d^{1}$ | 1 |
- **Should be:**
  > | (iv) | $\mathrm{Ti}^{3+},[\mathrm{Ar}] 3 d^{1}$ | 1 |

### q_4.36 — solution (en)
- **Confidence:** high
- **Reason:** OCR confused 'Co' (cobalt) with 'CO' (carbon monoxide) - an important OCR-confusion class in inorganic chemistry; this row is about the Co2+ ion, not a carbon monoxide species. Also removes the stray duplicate ':--- ' header-separator row.
- **Found:**
  > | $\mathrm{Fe}^{2+}$ | 6 | $t_{2 g}^{4} e_{g}^{2}$ |
  > | :--- | :--- | :--- |
  > | $\mathrm{Fe}^{3+}$ | 5 | $t_{2 g}^{3} e_{g}^{2}$ |
  > | $\mathrm{CO}^{2+}$ | 7 | $t_{2 g}^{5} e_{g}^{2}$ |
- **Should be:**
  > | $\mathrm{Fe}^{2+}$ | 6 | $t_{2 g}^{4} e_{g}^{2}$ |
  > | $\mathrm{Fe}^{3+}$ | 5 | $t_{2 g}^{3} e_{g}^{2}$ |
  > | $\mathrm{Co}^{2+}$ | 7 | $t_{2 g}^{5} e_{g}^{2}$ |

### q_4.36 — solution (en)
- **Confidence:** high
- **Reason:** Ion charge should be a superscript, not a subscript (every other row in this table uses the superscript form correctly).
- **Found:**
  > | $\mathrm{V}_{2+}$ | 3 | $t_{2 g}^{3}$ |
- **Should be:**
  > | $\mathrm{V}^{2+}$ | 3 | $t_{2 g}^{3}$ |

### q_4.37 — solution (en)
- **Confidence:** high
- **Reason:** Stronger M-M metallic bonding (from the heavier elements' more diffuse, more extensively overlapping 4d/5d orbitals) explains why the SECOND and THIRD series have HIGHER melting/boiling points, not why the first series is lower.
- **Found:**
  > (iv) The melting and boiling points of the first transition series are lower than those of the heavier transition elements. This is because of the occurrence of stronger metallic bonding (M-M bonding).
- **Should be:**
  > (iv) The melting and boiling points of the first transition series are lower than those of the heavier transition elements. This is because the heavier elements' more diffuse 4d and 5d orbitals overlap more extensively, giving stronger metallic (M-M) bonding than in the first series.

### q_4.27 — solution (en)
- **Confidence:** high
- **Reason:** Per the textbook's own text: 'A good deal of mischmetall is used in Mg-based alloy to produce bullets, shell and lighter flint.' There is no textbook mention of 'flame throwing tanks'; the real use is Mg-based alloys for bullets, shells and lighter flints.
- **Found:**
  > (1) Mischmetal is used in cigarettes and gas lighters.
  > (2) It is used in flame throwing tanks.
  > (3) It is used in tracer bullets and shells.
- **Should be:**
  > (1) A good deal of mischmetal is used in Mg-based alloys to make lighter flints (as in cigarette/gas lighters).
  > (2) It is used to make bullets and shells.

### q_4.12 — solution (en)
- **Confidence:** high
- **Reason:** Per the textbook's own text, interstitial compounds are usually non-stoichiometric, and their defining properties (high melting points, hardness, retained metallic conductivity, chemical inertness) were missing from this answer.
- **Found:**
  > Transition metals are large in size and contain lots of interstitial sites. Transition elements can trap atoms of other elements (that have small atomic size), such as H, C, N, in the interstitial sites of their crystal lattices. The resulting compounds are called interstitial compounds.
- **Should be:**
  > Transition metals are large in size and contain lots of interstitial sites (voids) in their crystal lattices. Small atoms of other elements, such as H, C or N, get trapped in these interstitial sites; the resulting compounds - usually non-stoichiometric (e.g. VH0.56) and neither typically ionic nor covalent - are called interstitial compounds. They are well known for transition metals because of these large lattices, and are characterised by: (i) high melting points, higher than the pure metal; (ii) considerable hardness, some approaching diamond; (iii) retained metallic conductivity; and (iv) chemical inertness.

### q_4.29 — solution (en)
- **Confidence:** high
- **Reason:** Per the textbook's own Table 4.11 (independently reconstructed from the source PDF's word coordinates): U's oxidation states are +3,+4,+5,+6 (max +6), while BOTH Np and Pu reach +3,+4,+5,+6,+7 (max +7) - the original wrongly caps plutonium at +6 and omits +6 for neptunium.
- **Found:**
  > For example, uranium and plutonium
  > display +3, +4, +5, and +6 oxidation states while neptunium displays +3, +4, +5, and +7.
- **Should be:**
  > For example, uranium displays +3, +4, +5, and +6 oxidation states, while neptunium and plutonium display +3, +4, +5, +6, and +7.

### q_4.11 — parts[2].solution (en)
- **Confidence:** high
- **Reason:** Missing space between 'to' and 'another'.
- **Found:**
  > one set toanother.
- **Should be:**
  > one set to another.

### q_4.3 — solution (en)
- **Confidence:** high
- **Reason:** This solution's own preceding sentence states Sc does NOT show +2 ('except Sc, all others metals display +2') - listing 'Sc(+2)=d1' right after directly contradicts that. The list should start at Ti.
- **Found:**
  > \begin{aligned}
  > & \mathrm{Sc}(+2)=d^{1} \\
  > & \mathrm{Ti}(+2)=d^{2}
- **Should be:**
  > \begin{aligned}
  > & \mathrm{Ti}(+2)=d^{2}

### it_4.6 — solution (en)
- **Confidence:** high
- **Reason:** Ions don't carry 'electronegativity' in the usual sense - it is the small, highly electronegative O and F ATOMS that pull electron density from the metal. Oxygen additionally forms multiple (pi) bonds with the metal, letting it stabilise even higher oxidation states than fluorine (e.g. Mn reaches +7 in Mn2O7 but not in any fluoride).
- **Found:**
  > Both oxide and fluoride ions are highly electronegative and have a very small size. Due to these properties, they are able to oxidize the metal to its highest oxidation state.
- **Should be:**
  > Oxygen and fluorine are small, highly electronegative atoms, which lets them pull electron density strongly from a metal and stabilise it in a high oxidation state. Oxygen can, in addition, form multiple (p pi - d pi) bonds with the metal, letting it stabilise even higher oxidation states than fluorine can (e.g. Mn reaches +7 in Mn2O7 but not in any fluoride) - which is why a transition metal's highest oxidation state is usually seen in its oxide or fluoride.

### it_4.7 — solution (en)
- **Confidence:** high
- **Reason:** The reaction line and E-value block were garbled OCR (species written as 'Cr_2+3+Fe_2+', label glued onto the E-value sentence); independently re-derived the two half-reactions and their real E-values (Cr3+/Cr2+=-0.41V, Fe3+/Fe2+=+0.77V) from this item's own question. Also fixes 'better reducing agent that Fe3+' -> 'than Fe2+' (Fe2+ is the ion actually being compared, not Fe3+).
- **Found:**
  > The following reactions are involved when $\mathrm{Cr}^{2+}$ and $\mathrm{Fe}^{2+}$ act as reducing agents.
  > 
  > $$
  > \begin{array}{ll}
  > \longrightarrow & \mathrm{Cr}_{2}+3+\mathrm{Fe}_{2}+ \\
  > E^{\circ} \mathrm{Cr}^{3+} / \mathrm{Cr}^{2+} & \text { The value is }-0.41 \mathrm{~V} \text { and } E_{\mathrm{Fe}^{3+} / \mathrm{Fe}^{2+}}^{\circ} \text { is }+0.77 \mathrm{~V} . \text { This means that } \mathrm{Cr}^{2+} \text { can }
  > \end{array}
  > $$
  > 
  > be easily oxidized to $\mathrm{Cr}^{3+}$, but $\mathrm{Fe}^{2+}$ does not get oxidized to $\mathrm{Fe}^{3+}$ easily. Therefore, $\mathrm{Cr}^{2+}$ is a better reducing agent that $\mathrm{Fe}^{3+}$.
- **Should be:**
  > The following reactions are involved when $\mathrm{Cr}^{2+}$ and $\mathrm{Fe}^{2+}$ act as reducing agents.
  > 
  > $$
  > \begin{aligned}
  > & \mathrm{Cr}^{2+} \longrightarrow \mathrm{Cr}^{3+}+\mathrm{e}^{-} ; \quad E^{\ominus}=-0.41 \mathrm{~V} \\
  > & \mathrm{Fe}^{2+} \longrightarrow \mathrm{Fe}^{3+}+\mathrm{e}^{-} ; \quad E^{\ominus}=+0.77 \mathrm{~V}
  > \end{aligned}
  > $$
  > 
  > $\mathrm{Cr}^{2+}$ is readily oxidised to $\mathrm{Cr}^{3+}$ (negative E-value), but $\mathrm{Fe}^{2+}$ is not easily oxidised to $\mathrm{Fe}^{3+}$ (positive E-value). Therefore, it is a better reducing agent than $\mathrm{Fe}^{2+}$.

### q_4.38 — solution (en)
- **Confidence:** high
- **Reason:** Scrambled OCR reading order - the label 'Magnetic moment' and its symbol/formula were split apart across the line.
- **Found:**
  > Magnetic
  > 
  > $$
  > \mu \text { ) is given as } \mu=\sqrt{n(n+2)} \text { moment }(.
  > $$
- **Should be:**
  > Magnetic moment is given as
  > 
  > $$
  > \mu=\sqrt{n(n+2)}
  > $$

### q_4.38 — solution (en)
- **Confidence:** high
- **Reason:** Stray spaces inside the formula/bracket notation ('M n', 'C N').
- **Found:**
  > (i) $\mathbf{K}_{\mathbf{4}}\left[\mathbf{M n}(\mathbf{C N})_{\mathbf{6}}\right]$
- **Should be:**
  > (i) $\mathbf{K}_{\mathbf{4}}\left[\mathbf{Mn}(\mathbf{CN})_{\mathbf{6}}\right]$

### q_4.38 — solution (en)
- **Confidence:** high
- **Reason:** Stray spaces inside the formula/bracket notation ('M n C l').
- **Found:**
  > (iii) $\mathbf{K}_{\mathbf{2}}\left[\mathbf{M n C l}_{\mathbf{4}}\right]$
- **Should be:**
  > (iii) $\mathbf{K}_{\mathbf{2}}\left[\mathbf{MnCl}_{\mathbf{4}}\right]$
