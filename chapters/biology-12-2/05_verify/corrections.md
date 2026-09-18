### q_2.1 — parts[0].question (hi)
- **Confidence:** high
- **Reason:** Extraction substituted the short "e" vowel sign for the "ai" vowel sign in "लैंगिक", producing a misspelling not present in the source
- **Found:**
  > लेंगिक
- **Should be:**
  > लैंगिक

### q_2.11 — solution (hi)
- **Confidence:** high
- **Reason:** OCR truncated "यूरेथ्रा" (urethra) to a non-word
- **Found:**
  > वासा डिफरेन्शिया → यूरेश ← स्खलन नलिका
- **Should be:**
  > वासा डिफरेन्शिया → यूरेथ्रा ← स्खलन नलिका

### q_2.11 — solution (hi)
- **Confidence:** high
- **Reason:** OCR corrupted "स्रावित" (secreted) into the non-word "स्तावित"
- **Found:**
  > इससे स्तावित तरल शुक्राणुओं
- **Should be:**
  > इससे स्रावित तरल शुक्राणुओं

### q_2.11 — solution (hi)
- **Confidence:** high
- **Reason:** OCR dropped the conjunct in "पार्श्वों" (sides), corrupting it to "पाश्वों"
- **Found:**
  > मूत्रमार्ग के पाश्वों में स्थित होती हैं
- **Should be:**
  > मूत्रमार्ग के पार्श्वों में स्थित होती हैं

### q_2.12 — solution (hi)
- **Confidence:** medium
- **Reason:** extra अनुस्वार+न turns "हॉर्मोन" (hormone) into the misspelled "हॉर्मोंन"; meaning unaffected but the word form is wrong per source
- **Found:**
  > स्त्री में हॉर्मोंन के प्रभाव से
- **Should be:**
  > स्त्री में हॉर्मोन के प्रभाव से

### q_2.12 — solution (hi)
- **Confidence:** high
- **Reason:** OCR dropped the ्र conjunct in "ध्रुवीय पिण्ड" (polar body), producing the non-word "धुवीय"
- **Found:**
  > एक अगुणित लोपिका या धुवीय पिण्ड (polar body) बनती है
- **Should be:**
  > एक अगुणित लोपिका या ध्रुवीय पिण्ड (polar body) बनती है

### q_2.12 — solution (hi)
- **Confidence:** high
- **Reason:** OCR corrupted "ग्राफियन पुटिका" (Graafian follicle) into the non-word "प्राफियन पुटिका" (ग्→प् substitution)
- **Found:**
  > इसी अवस्था में प्राफियन पुटिका फटकर
- **Should be:**
  > इसी अवस्था में ग्राफियन पुटिका फटकर

### q_2.15 — parts[4].solution (hi)
- **Confidence:** high
- **Reason:** OCR dropped the "र" (Fimbriae's Hindi term) in its first mention; the source solutions PDF spells it "फिम्ब्री" both times (heading and body), extraction rendered it as "फिम्बी" once
- **Found:**
  > झालर (फिम्बी-Fimbriae)
- **Should be:**
  > झालर (फिम्ब्री-Fimbriae)

### q_2.16 — parts[5].question (hi)
- **Confidence:** high
- **Reason:** the chapter PDF spells this transliteration "मेन्सटुअल" (no र); extraction inserted an extra "र" making it "मेन्सट्रुअल"
- **Found:**
  > मेन्सट्रुअल
- **Should be:**
  > मेन्सटुअल

### q_2.17 — question (hi)
- **Confidence:** high
- **Reason:** same transliteration error as above — chapter PDF's own Q17 text reads "मेन्सटुअल", not "मेन्सट्रुअल"
- **Found:**
  > मेन्सट्रुअल
- **Should be:**
  > मेन्सटुअल

### q_2.17 — solution (hi)
- **Confidence:** high
- **Reason:** solutions PDF spells this word "मेन्सटुअल" (yet another distinct OCR corruption than the question-field one, but still wrong)
- **Found:**
  > मेन्सट्रअल
- **Should be:**
  > मेन्सटुअल

### q_2.17 — solution (hi)
- **Confidence:** high
- **Reason:** OCR substituted स् with त् — source reads "ऋतुस्राव" ("प्रथम ऋतुस्राव/रजोधर्म")
- **Found:**
  > ऋतुत्राव
- **Should be:**
  > ऋतुस्राव

### q_2.17 — solution (hi)
- **Confidence:** high
- **Reason:** OCR inserted an extra र् — source reads "इसमें ऋतुस्राव (menstruation)"
- **Found:**
  > इसमें ऋतुर्राव (menstruation)
- **Should be:**
  > इसमें ऋतुस्राव (menstruation)

### q_2.17 — solution (hi)
- **Confidence:** high
- **Reason:** OCR substituted र with त — source reads "रक्तस्राव शुरू हो जाता है"
- **Found:**
  > रक्तस्ताव शुरू
- **Should be:**
  > रक्तस्राव शुरू

### q_2.17 — solution (hi)
- **Confidence:** high
- **Reason:** OCR inserted an extra त् — source reads "रक्तस्राव के साथ"
- **Found:**
  > रक्तस्त्राव के साथ
- **Should be:**
  > रक्तस्राव के साथ

### q_2.17 — solution (hi)
- **Confidence:** high
- **Reason:** OCR inserted an extra त् — source reads "इसी को ऋतुस्राव कहते हैं"
- **Found:**
  > ऋतुस्त्राव कहते
- **Should be:**
  > ऋतुस्राव कहते

### q_2.19 — solution (hi)
- **Confidence:** medium
- **Reason:** extracted text has "समयुंग्मकी" (with an extra anusvara) in its first mention, but the same solution's third paragraph mentions the identical term as "समयुग्मकी" (no anusvara) and this is the standard, unambiguous spelling of the biology term (homogametic). Source page mark at this position is not fully unambiguous (could be scan noise); the second instance on the same page is clean and matches the standard term.
- **Found:**
  > समयुंग्मकी
- **Should be:**
  > समयुग्मकी
