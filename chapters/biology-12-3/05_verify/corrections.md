### q_3.2 — solution (hi)
- **Confidence:** high
- **Reason:** OCR dropped the आ-matra, turning "आर्थिक" (economic) into a different/misspelled word
- **Found:**
  > अनियन्त्रित जनसंख्या वृद्धि से होने वाली अर्थिक समस्याओं
- **Should be:**
  > अनियन्त्रित जनसंख्या वृद्धि से होने वाली आर्थिक समस्याओं

### q_3.2 — solution (hi)
- **Confidence:** high
- **Reason:** OCR misread ऋ as ॠ and स्र as स्त, producing a garbled non-word instead of "ऋतुस्राव" (menstrual flow)
- **Found:**
  > ॠतुस्ताव-सम्बन्धी समस्याओं
- **Should be:**
  > ऋतुस्राव-सम्बन्धी समस्याओं

### q_3.3 — solution (hi)
- **Confidence:** high
- **Reason:** OCR dropped the ध, turning "अध्ययन" (study) into a meaningless word
- **Found:**
  > अष्ययन बताते हैं
- **Should be:**
  > अध्ययन बताते हैं

### q_3.3 — solution (hi)
- **Confidence:** high
- **Reason:** OCR misread भ्र as प्र, turning "भ्रान्तियों" (misconceptions) into a meaningless word
- **Found:**
  > विभिन्न प्रान्तियों को दूर
- **Should be:**
  > विभिन्न भ्रान्तियों को दूर

### q_3.5 — solution (hi)
- **Confidence:** high
- **Reason:** OCR inserted a spurious anusvara onto "वृद्धि" (increase)
- **Found:**
  > खाद्यान्नों के उत्पादन में वृद्धिं।
- **Should be:**
  > खाद्यान्नों के उत्पादन में वृद्धि।

### q_3.6 — solution (hi)
- **Confidence:** high
- **Reason:** OCR inserted a spurious anusvara into "प्रक्रिया" (process)
- **Found:**
  > प्राकृतिक प्रंक्रिया पर रोक
- **Should be:**
  > प्राकृतिक प्रक्रिया पर रोक

### q_3.7 — solution (hi)
- **Confidence:** high
- **Reason:** OCR inserted a spurious anusvara, misspelling "हटाना" as "हंटाना"
- **Found:**
  > हंटाना
- **Should be:**
  > हटाना

### q_3.9 — solution (hi)
- **Confidence:** high
- **Reason:** OCR dropped the conjunct "्र", turning "भ्रूण" into "भूण"
- **Found:**
  > भूण स्थानान्तरण (Embryo Transfer : ET)
- **Should be:**
  > भ्रूण स्थानान्तरण (Embryo Transfer : ET)

### q_3.9 — solution (hi)
- **Confidence:** high
- **Reason:** OCR dropped the anusvara on "में", leaving the non-word "मे"
- **Found:**
  > फैलोपियन नलिका मे स्थानान्तरित
- **Should be:**
  > फैलोपियन नलिका में स्थानान्तरित

### q_3.12 — parts[0].solution (hi)
- **Confidence:** high
- **Reason:** OCR dropped the "/" separator, gluing "शुक्राणु" and "अण्डाणु" into one nonsense compound
- **Found:**
  > (शुक्राणुअण्डाणु)
- **Should be:**
  > (शुक्राणु/अण्डाणु)

### q_3.12 — parts[3].solution (hi)
- **Confidence:** high
- **Reason:** OCR corrupted "इन्ट्रा" (Intra) into "इन्टूा"
- **Found:**
  > इन्टूा यूटेराइन ट्रान्सफर
- **Should be:**
  > इन्ट्रा यूटेराइन ट्रान्सफर

### q_3.9 — solution (hi)
- **Confidence:** high
- **Reason:** The sentence had the transfer direction reversed: it said the embryo forms in the fallopian tube of the woman who HAS the gestation problem, and is then sent OUT to another woman's uterus - which defeats the stated purpose of helping her. chapter.hi.pdf page 54 (confirmed by direct 200dpi render) states the opposite: an embryo formed by in-vivo fertilization is transferred INTO the woman with the gestation problem, to help her. The reversed version traces to solutions.hi.pdf's own text (confirmed via mathpix) - an inherited error, but corrected here since it directly contradicts the textbook's own explicit statement. The following sentences (donor ovum -> same recipient's own tube = GIFT) were already correct and left unchanged.
- **Found:**
  > भारतवर्ष सहित विश्व में अनेक दम्पती बन्ध्य (sterile) हैं अर्थात् वे सन्तान उत्पन्न करने में असमर्थ होते हैं। यह शारीरिक, जन्मजात, रोगजन्य, औषधिक, प्रतिरक्षात्मक (immunological) या मनोवैज्ञानिक कारणों से हो सकता है। यह पुरुष या स्त्री में पाए जाने वाले दोष के कारण हो सकता है।
  > 
  > अनेक प्रकार की बन्ध्यताओं का उपचार केवल औषधियों से हो जाता है। कभी-कभी परामर्श व मनोवैज्ञानिक उपचार भी सहायक होता है।
  > 
  > विशिष्ट स्वास्थ्य सेवा इकाइयाँ (बन्ध्यता क्लीनिक infertility clinics) निदानिक जाँच में सहायता एवं उपचार करके बन्ध्य दम्पतियों को सन्तान पैदा करने में मदद दे सकते हैं। इन तकनीकों को सहायक जनन प्रौद्योगिकी (Assisted Reproductive Technologies : ART) कहते हैं।
  > 
  > शरीर से बाहर निषेचन अर्थात् पात्रे निषेचन (In Vitro Fertilization : IVF) के पश्चात् भ्रूण स्थानान्तरण (Embryo Transfer : ET) एक उपयुक्त उपाय हो सकता है। इस तकनीक को सामान्य रूप से टेस्ट ट्यूब बेबी (test tube baby) तकनीक के नाम से जानते हैं। प्रयोगशाला में पत्नी या दाता के अण्ड को पति अथवा दाता के शुक्राणु से निषेचित कराया जाता है। इसके पश्चात् युग्मनज या $8$ कोशिकीय भ्रूण को फैलोपियन नलिका में स्थानान्तरित किया जाता है। $8$ कोशिकाओं से अधिक विकसित होने वाले भ्रूण को गर्भाशय में स्थानान्तरित कर दिया जाता है। इसे इन्ट्रा यूटेराइन ट्रान्सफर (Intra Uterine Transfer : IUT) कहते हैं।
  > 
  > जिन स्त्रियों में गर्भधारण की समस्या होती है, उनकी फैलोपियन नलिका में बने भ्रूण को अन्य स्त्री के गर्भाशय में स्थानान्तरित किया जा सकता है। जिन स्त्रियों में अण्डाणु उत्पन्न नहीं हो सकते, लेकिन निषेचन और भ्रूणीय विकास के लिए उपयुक्त वातावरण प्रदान कर सकती हैं, इनके लिए दाता स्त्री से अण्डाणु प्राप्त करके उसकी फैलोपियन नलिका में स्थानान्तरित कर दिया जाता है। इसे गैमीट इन्ट्रा फैलोपियन ट्रान्सफर (Gamete Intra Fallopian Transfer : GIFT) कहते हैं।
  > 
  > कृत्रिम वीर्यसेचन तकनीक का प्रयोग वहाँ किया जाता है, जहाँ पुरुष के वीर्य में शुक्राणुओं की संख्या बहुत कम होती है अथवा पुरुष वीर्य सेचित कर सकने में असमर्थ होता है। इस तकनीक में दाता से शुक्राणुओं को प्राप्त करके कृत्रिम रूप से स्त्री की योनि या गर्भाशय में प्रविष्ट कर दिया जाता है। इसे अन्तःगर्भाशयी वीर्यसेचन (Intra Uterine Insemination : IUI) कहते हैं। ऐसी अन्य कुछ तकनीक हैं-ZIFT तथा ICSI आदि। वर्तमान में उपर्युक्त तकनीकी सुविधाएँ अनेक शहरों में उपलब्ध हैं। ये बहुत महँगी तकनीक हैं। इन तकनीकों को अपनाने में सामाजिक, धार्मिक और भावनात्मक कारक महत्त्वपूर्ण भूमिका निभाते हैं।
- **Should be:**
  > भारतवर्ष सहित विश्व में अनेक दम्पती बन्ध्य (sterile) हैं अर्थात् वे सन्तान उत्पन्न करने में असमर्थ होते हैं। यह शारीरिक, जन्मजात, रोगजन्य, औषधिक, प्रतिरक्षात्मक (immunological) या मनोवैज्ञानिक कारणों से हो सकता है। यह पुरुष या स्त्री में पाए जाने वाले दोष के कारण हो सकता है।
  > 
  > अनेक प्रकार की बन्ध्यताओं का उपचार केवल औषधियों से हो जाता है। कभी-कभी परामर्श व मनोवैज्ञानिक उपचार भी सहायक होता है।
  > 
  > विशिष्ट स्वास्थ्य सेवा इकाइयाँ (बन्ध्यता क्लीनिक infertility clinics) निदानिक जाँच में सहायता एवं उपचार करके बन्ध्य दम्पतियों को सन्तान पैदा करने में मदद दे सकते हैं। इन तकनीकों को सहायक जनन प्रौद्योगिकी (Assisted Reproductive Technologies : ART) कहते हैं।
  > 
  > शरीर से बाहर निषेचन अर्थात् पात्रे निषेचन (In Vitro Fertilization : IVF) के पश्चात् भ्रूण स्थानान्तरण (Embryo Transfer : ET) एक उपयुक्त उपाय हो सकता है। इस तकनीक को सामान्य रूप से टेस्ट ट्यूब बेबी (test tube baby) तकनीक के नाम से जानते हैं। प्रयोगशाला में पत्नी या दाता के अण्ड को पति अथवा दाता के शुक्राणु से निषेचित कराया जाता है। इसके पश्चात् युग्मनज या $8$ कोशिकीय भ्रूण को फैलोपियन नलिका में स्थानान्तरित किया जाता है। $8$ कोशिकाओं से अधिक विकसित होने वाले भ्रूण को गर्भाशय में स्थानान्तरित कर दिया जाता है। इसे इन्ट्रा यूटेराइन ट्रान्सफर (Intra Uterine Transfer : IUT) कहते हैं।
  > 
  > जिन स्त्रियों में गर्भधारण की समस्या होती है, उनकी सहायता के लिए जीवे निषेचन (in-vivo fertilization) द्वारा बने भ्रूण को उनके गर्भाशय में स्थानान्तरित किया जा सकता है। जिन स्त्रियों में अण्डाणु उत्पन्न नहीं हो सकते, लेकिन निषेचन और भ्रूणीय विकास के लिए उपयुक्त वातावरण प्रदान कर सकती हैं, इनके लिए दाता स्त्री से अण्डाणु प्राप्त करके उसकी फैलोपियन नलिका में स्थानान्तरित कर दिया जाता है। इसे गैमीट इन्ट्रा फैलोपियन ट्रान्सफर (Gamete Intra Fallopian Transfer : GIFT) कहते हैं।
  > 
  > कृत्रिम वीर्यसेचन तकनीक का प्रयोग वहाँ किया जाता है, जहाँ पुरुष के वीर्य में शुक्राणुओं की संख्या बहुत कम होती है अथवा पुरुष वीर्य सेचित कर सकने में असमर्थ होता है। इस तकनीक में दाता से शुक्राणुओं को प्राप्त करके कृत्रिम रूप से स्त्री की योनि या गर्भाशय में प्रविष्ट कर दिया जाता है। इसे अन्तःगर्भाशयी वीर्यसेचन (Intra Uterine Insemination : IUI) कहते हैं। ऐसी अन्य कुछ तकनीक हैं-ZIFT तथा ICSI आदि। वर्तमान में उपर्युक्त तकनीकी सुविधाएँ अनेक शहरों में उपलब्ध हैं। ये बहुत महँगी तकनीक हैं। इन तकनीकों को अपनाने में सामाजिक, धार्मिक और भावनात्मक कारक महत्त्वपूर्ण भूमिका निभाते हैं।
