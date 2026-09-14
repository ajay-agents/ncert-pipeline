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
