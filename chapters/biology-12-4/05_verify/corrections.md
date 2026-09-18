### q_4.2 — parts[0].solution (hi)
- **Confidence:** high
- **Reason:** OCR corrupted एन्जाइम (enzyme) to एज्जाइम on its second occurrence in the Dominance/Recessiveness table's second row
- **Found:**
  > बनता है या एज्जाइम बनता ही नहीं
- **Should be:**
  > बनता है या एन्जाइम बनता ही नहीं

### q_4.2 — parts[2].solution (hi)
- **Confidence:** high
- **Reason:** OCR transposed सन्तति (progeny/offspring) to सन्तित
- **Found:**
  > सन्तित
- **Should be:**
  > सन्तति

### q_4.2 — parts[2].solution (hi)
- **Confidence:** high
- **Reason:** OCR corrupted सहलग्नता (linkage) to सहलन्नता; confirmed at high resolution the PDF shows the ग्न conjunct, not न्न
- **Found:**
  > सहलन्नता
- **Should be:**
  > सहलग्नता

### q_4.4 — solution (hi)
- **Confidence:** high
- **Reason:** OCR dropped the े matra, turning लम्बे (tall) into लम्ब
- **Found:**
  > संकर लम्ब (hybrid tall)
- **Should be:**
  > संकर लम्बे (hybrid tall)

### q_4.8 — solution (hi)
- **Confidence:** high
- **Reason:** OCR misread सकता (can/possible) as मकता
- **Found:**
  > समझा जा मकता है
- **Should be:**
  > समझा जा सकता है

### q_4.8 — solution (hi)
- **Confidence:** high
- **Reason:** OCR garbled मीठी (sweet, as in "sweet pea") into मोंटी
- **Found:**
  > मोंटी मटर
- **Should be:**
  > मीठी मटर

### q_4.8 — solution (hi)
- **Confidence:** high
- **Reason:** OCR garbled नीला (blue) into नोला
- **Found:**
  > फूल का नोला रंग
- **Should be:**
  > फूल का नीला रंग

### q_4.8 — solution (hi)
- **Confidence:** high
- **Reason:** OCR garbled गोल परागकण (round pollen) into नोल पगतकण, and misread the recessive allele symbol (l) as (b) — a genotype-notation error that also collides with the flower-color gene's own (b) symbol used earlier in the same sentence
- **Found:**
  > नोल पगतकण (b)
- **Should be:**
  > गोल परागकण (l)

### q_4.8 — solution (hi)
- **Confidence:** high
- **Reason:** OCR dropped the anusvara on हैं (plural verb agreement with जीन... है/हैं)
- **Found:**
  > क्योंकि जीन सहलग्न है।
- **Should be:**
  > क्योंकि जीन सहलग्न हैं।

### q_4.8 — solution (hi)
- **Confidence:** high
- **Reason:** OCR garbled जनकीय (parental) into जनर्काय
- **Found:**
  > जनर्काय अनुपात 100\%
- **Should be:**
  > जनकीय अनुपात 100\%

### q_4.12 — solution (hi)
- **Confidence:** high
- **Reason:** Mathpix OCR nested the trailing "i" as a subscript inside the exponent instead of "I superscript A" followed by a plain "i" — the same pattern used correctly elsewhere in this item (e.g. the table's "I^A i"). The source page shows the father's blood group as two separate elements, not a nested exponent.
- **Found:**
  > $I^{A_{i}}$
- **Should be:**
  > $\mathrm{I}^{\mathrm{A}} \mathrm{i}$

### q_4.12 — solution (hi)
- **Confidence:** high
- **Reason:** Same nested-exponent OCR artifact as the correction above, for the mother's genotype.
- **Found:**
  > $I^{B_{i}}$
- **Should be:**
  > $\mathrm{I}^{\mathrm{B}} \mathrm{i}$

### q_4.13 — parts[1].solution (hi)
- **Confidence:** high
- **Reason:** OCR dropped a character — source page reads "सन्तति" (offspring/progeny), extracted as "सन्ति" (not a word).
- **Found:**
  > पीढ़ी की सन्ति के बीच संकरण कराने पर
- **Should be:**
  > पीढ़ी की सन्तति के बीच संकरण कराने पर
