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
