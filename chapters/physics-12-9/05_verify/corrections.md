### q_9.30 — solution (hi)
- **Confidence:** high
- **Reason:** Own stage-2 extraction had bracketed an editorial flag-note into the solution text itself instead of leaving verbatim source text and flagging separately; replacing with clean, corrected verbatim-equivalent text now that the fix is confirmed against the actual solutions.hi.pdf page 27 (प्रश्न 37): the source itself prints 'd=1.5 x (7deg x pi/180deg) = 0.184 m = 18.4 m' -- a same-page self-contradiction (18.4 m is 100x its own preceding 0.184 m). 0.184 m = 18.4 cm is the arithmetically consistent reading. User reviewed and approved this exact fix (matching the ex_2.3/q_5.7(ii)/ex_5.5(d)/q_3.6/q_3.7/q_8.4 precedent for same-page self-contradictions) via the coordinating session.
- **Found:**
  > $\Rightarrow d=1.5 \times \frac{7^{\circ} \times \pi}{180^{\circ}}=0.184 \mathrm{~m}$ [हल-प्रति में इसे असंगत रूप से '$=18.4$ m' भी लिखा गया है, जो स्वयं इसी पंक्ति के $0.184$ m मान से मेल नहीं खाता — सही रूपांतरण $0.184 \mathrm{~m}=18.4$ सेमी है, PDF से पुष्टि आवश्यक।]
- **Should be:**
  > $\Rightarrow d=1.5 \times \frac{7^{\circ} \times \pi}{180^{\circ}}=0.184 \mathrm{~m}=18.4 \mathrm{~cm}$

### q_9.30 — final_answer (hi)
- **Confidence:** high
- **Reason:** Same fix as the solution-field correction above, applied to the final_answer field: strip the inline editorial flag note now that the source disagreement is confirmed and fixed, leaving a clean stated answer.
- **Found:**
  > $d \approx 0.184\ \mathrm{m} = 18.4\ \mathrm{cm}$ (स्रोत में स्वयं-विरोधाभासी रूप से '$18.4$ m' भी छपा है — इकाई-असंगति के रूप में ऊपर ध्वजांकित)
- **Should be:**
  > $d \approx 0.184\ \mathrm{m} = 18.4\ \mathrm{cm}$

### q_9.22 — parts[0].solution (hi)
- **Confidence:** high
- **Reason:** Remove stage 2's own inline editorial bracket-note from the solution text (Rule 1: this field should carry verbatim/near-verbatim source content, not commentary); the chapter-vs-solutions value disagreement stays fully documented in match_report.md's needs_review_flags_for_stage_5 and this stage's manifest entry instead. Confirmed against both PDF pages directly (chapter.hi.pdf p.252: '9 cm फ़ोकस दूरी'; solutions.hi.pdf p.21/प्रश्न 29: '10 cm फोकस दूरी') -- left exactly as printed in each source, per standing instruction, not resolved.
- **Found:**
  > [नोट: चित्र की प्रकाशित सौर्स-सामग्री में लेंस की फोकस दूरी $9$ cm छपी है; उपलब्ध हल-प्रति (solutions.hi.pdf) में यह गणना $f=+10$ cm मानकर की गई है — दोनों स्रोतों में अंतर है, नीचे दोनों मान अंकित हैं।] दिया है, $u=-9$ सेमी। हल-प्रति के अनुसार $f=+10$ सेमी: लेंस के सूत्र
- **Should be:**
  > दिया है, $u=-9$ सेमी, $f=+10$ सेमी लेंस के सूत्र

### q_9.22 — parts[0].final_answer (hi)
- **Confidence:** high
- **Reason:** Same cleanup as the solution field above -- disagreement stays documented in match_report.md/manifest, not inline in the data.
- **Found:**
  > $m=10$ (हल-प्रति के $f=10$cm मानकर); प्रत्येक वर्ग का क्षेत्रफल $=100\ \mathrm{mm}^2$ — प्रश्न में मुद्रित $f=9$cm के साथ यह असंगति है, PDF से पुष्टि आवश्यक।
- **Should be:**
  > $m=10$; प्रत्येक वर्ग का क्षेत्रफल $=100\ \mathrm{mm}^2$
