### ex_14.2 — solution (hi)
- **Confidence:** high
- **Reason:** mathpix dropped 'से उत्पन्न इलेक्ट्रॉनों की तुलना में नगण्य हैं।' right after the first 'अपमिश्रण' and instead duplicated it onto the later 'इसलिए होलों की संख्या' line, scrambling sentence order - confirmed against source PDF chapters/physics-12-14/00_raw/chapter.hi.pdf p.10 (Example 14.2), which reads in this corrected order.
- **Found:**
  > ध्यान दीजिए, यहाँ तापीय जनित की ऊष्मा से उत्पन्न इलेक्ट्रॉन ( $n_{\mathrm{i}} \sim 10^{16} \mathrm{~m}^{-3}$ ) अपमिश्रण
  > इसलिए, $n_{e} \approx N_{D}$
  > चूँकि $n_{e} n_{h}=n_{i}^{2}$, इसलिए होलों की संख्या से उत्पन्न इलेक्ट्रॉनों की तुलना में नगण्य हैं।
- **Should be:**
  > ध्यान दीजिए, यहाँ तापीय जनित की ऊष्मा से उत्पन्न इलेक्ट्रॉन ( $n_{\mathrm{i}} \sim 10^{16} \mathrm{~m}^{-3}$ ) अपमिश्रण से उत्पन्न इलेक्ट्रॉनों की तुलना में नगण्य हैं।
  > इसलिए, $n_{e} \approx N_{D}$
  > चूँकि $n_{e} n_{h}=n_{i}^{2}$, इसलिए होलों की संख्या

### ex_14.2 — final_answer (hi)
- **Confidence:** high
- **Reason:** Left empty at stage 2 pending PDF confirmation. Confirmed against source PDF p.10: the solution's own division n_h=(2.25e32)/(5e22) uses N_D=5e22 m^-3 (=n_e, since n_e≈N_D) as the denominator - stated here explicitly rather than left implicit.
- **Found:**
  > 
- **Should be:**
  > $n_e \approx N_D \approx 5\times10^{22}\ \mathrm{m}^{-3}$; $n_h \approx 4.5\times10^{9}\ \mathrm{m}^{-3}$

### q_14.3 — solution (hi)
- **Confidence:** high
- **Reason:** Same-page self-contradiction (confirmed against source PDF chapters/physics-12-14/00_raw/solutions.hi.pdf p.1, प्रश्न 3 - present in the original guide, not a mathpix artifact). The boxed answer (c) states (Eg)_C > (Eg)_Si > (Eg)_Ge, i.e. Ge has the SMALLEST gap; the chapter's own summary data (00_raw/chapter.hi.pdf p.10: C=5.4eV, Si=1.1eV, Ge=0.7eV) confirms Ge is smallest - but the explanatory sentence said Si is smallest, contradicting both its own boxed letter and the chapter body. Fixed per standing user authorization for confidently-diagnosed same-page self-contradictions, confirmed against source first.
- **Found:**
  > (c) कार्बन के लिए ऊर्जा बैंड गेप अधिकतम तथा Si के लिए न्यूनतम होता है।
- **Should be:**
  > (c) कार्बन के लिए ऊर्जा बैंड गेप अधिकतम तथा Ge के लिए न्यूनतम होता है।

### ex_14.3 — entire item missing (hi) [post-completion round]
- **Confidence:** high
- **Reason:** POST-COMPLETION user cross-check found उदाहरण 14.3 (chapter.hi.pdf p.334-335, a purely conceptual/non-numerical worked example) was never extracted at all - final_hi's भाग 1 jumped from ex_14.2 straight to ex_14.4 with no record of the gap. Confirmed against chapter.hi.pdf p.334-335 (rendered to PNG and read directly - this raw PDF's legacy font makes plain PyMuPDF text extraction garbled/unusable). Rule 5 (nothing invented) is satisfied by transcribing the source verbatim, not by inventing content; Rule 4 (question text immutable) does not apply to adding a missing item, only to rewording an existing one.
- **Found:**
  > (item absent - भाग 1 went ex_14.2 -> ex_14.4 directly)
- **Should be:**
  > उदाहरण 14.3: "क्या p-n संधि बनाने के लिए हम p-प्रकार के अर्धचालक की एक पट्टी को n-प्रकार के अर्धचालक से भौतिक रूप से संयोजित कर p-n संधि प्राप्त कर सकते हैं?" / हल: "नहीं! कोई भी पट्टी, चाहे कितनी ही समतल हो, अंतर-परमाणवीय क्रिस्टल अंतराल (~2 से 3 Å) से कहीं ज़्यादा खुरदरी होगी और इसलिए परमाणविक स्तर पर अविच्छिन्न संपर्क (अथवा संतत संपर्क) संभव नहीं होगा। प्रवाहित होने वाले आवेश वाहकों के लिए संधि एक विच्छिन्नता की तरह व्यवहार करेगी।" (see 07_format/structured.hi.md for the exact inserted text)

### q_14.2 — solution + answer (hi) [post-completion round]
- **Confidence:** high
- **Reason:** Confirmed against solutions.hi.pdf p.99: प्रश्न 2's हल gives the correct descriptive reasoning (holes majority, trivalent dopant) but never cites an option letter, unlike प्रश्न 1 and प्रश्न 3 in the same document, whose हल both open with their letter ((c) in each case) - and unlike this chapter's own q_14.1/14.3/14.4/14.5, which all cite theirs. q_14.2 also had no :::answer block at all before this round. The correct letter is unambiguous: q_14.1's own option (d) ("होल (विवर) बहुसंख्यक वाहक हैं और त्रिसंयोजी परमाणु अपमिश्रक हैं") is an exact match to q_14.2's reasoning.
- **Found:**
  > $p$-टाइप अर्द्धचालक Ge या Si में त्रिसंयोजी अशुद्धि से युक्त परमाणु मिलाया जाता है। $p$-टाइप अर्द्धचालक में इलेक्ट्रॉन अल्पसंख्यक तथा विवर बहुसंख्यक होते हैं। (no answer block)
- **Should be:**
  > (d) $p$-टाइप अर्द्धचालक Ge या Si में त्रिसंयोजी अशुद्धि से युक्त परमाणु मिलाया जाता है। $p$-टाइप अर्द्धचालक में इलेक्ट्रॉन अल्पसंख्यक तथा विवर बहुसंख्यक होते हैं। / **उत्तर:** (d)
