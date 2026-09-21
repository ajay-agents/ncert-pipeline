### q_1.11 — parts[1].solution (en)
- **Confidence:** high
- **Reason:** Extraction fidelity fix (not a content judgment call): solutions.en.pdf page 9 (Question 1.11) literally prints '9.1 x 10^-3 kg' on this defining line - confirmed via both a 200dpi page render and the PDF's own text layer. My stage-2 extraction had mis-copied this as '10^-31'. Restoring verbatim fidelity to the source, even though the source's own value here is itself an inherited typo (the correct physics value, -31, is what the very next line's actual multiplication already uses).
- **Found:**
  > m_{e}=9.1 \times 10^{-31} \mathrm{~kg}
- **Should be:**
  > m_{e}=9.1 \times 10^{-3} \mathrm{~kg}

### q_1.11 — parts[1].solution (en)
- **Confidence:** high
- **Reason:** User-approved fix for a same-page self-contradiction in the official solutions manual: this defining line printed '9.1 x 10^-3 kg' while the very next line's own calculation already correctly used 9.1 x 10^-31. User explicitly chose to correct the exponent here rather than leave the printed typo.
- **Found:**
  > m_{e}=9.1 \times 10^{-3} \mathrm{~kg}
- **Should be:**
  > m_{e}=9.1 \times 10^{-31} \mathrm{~kg}

### q_1.20 — solution (en)
- **Confidence:** high
- **Reason:** User-approved fix for a same-page self-contradiction in the official solutions manual: this derivation step printed '6.67 x 10^9 C' immediately followed by '= 6.67 nC' in the same breath (off by 18 orders of magnitude). User explicitly chose to correct the exponent to -9 to match the stated nC conclusion.
- **Found:**
  > 6.67 \times 10^{9} \mathrm{C}
- **Should be:**
  > 6.67 \times 10^{-9} \mathrm{C}
