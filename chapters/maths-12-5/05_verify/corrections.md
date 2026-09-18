### q_5.2.7 — solution (hi)
- **Confidence:** high
- **Reason:** solutions.hi.pdf page 2 of its own प्रश्नावली 5.2 section prints 'cossec' (a typo for 'cosec') consistently in BOTH derivative lines of this solution. Prior extraction preserved the typo in the first occurrence but silently corrected the second occurrence to the proper spelling - inconsistent with the source's own repeated typo. Confirmed against the actual page image by the stage-5 verification batch.
- **Found:**
  > \left[-\operatorname{cosec} x^{2}\right] \cdot 2 x
- **Should be:**
  > \left[-\operatorname{cossec} x^{2}\right] \cdot 2 x

### ex_5.13 — solution (hi)
- **Confidence:** high
- **Reason:** extraction truncated immediately after defining D1/D2/D3, dropping the entire remainder of the printed solution (दशा 1, दशा 2, दशा 3, and the concluding sentence) - confirmed on chapter.hi.pdf page 119 (file page 10) by the stage-5 verification batch. Genuine truncation, not a wording difference.
- **Found:**
  > \mathrm{D}_{3}=\{x \in \mathbf{R}: x>0\} \text { है। }
  > \end{aligned}
  > $$
- **Should be:**
  > \mathrm{D}_{3}=\{x \in \mathbf{R}: x>0\} \text { है। }
  > \end{aligned}
  > $$
  > 
  > दशा $1$ $\mathrm{D}_{1}$ के किसी भी बिंदु पर $f(x)=x^{2}$ है और यह सरलता से देखा जा सकता है कि $\mathrm{D}_{1}$ में $f$ संतत है। (उदाहरण $2$ देखिए)
  > दशा $2$ $\mathrm{D}_{3}$ के किसी भी बिंदु पर $f(x)=x$ है और यह सरलता से देखा जा सकता है कि $\mathrm{D}_{3}$ में $f$ संतत है। (उदाहरण $6$ देखिए)
  > दशा $3$ अब हम $x=0$ पर फलन का विश्लेषण करते हैं। $0$ के लिए फलन का मान $f(0)=0$ है।
  > $0$ पर $f$ के बाएँ पक्ष की सीमा
  > 
  > $$
  > \lim _{x \rightarrow 0^{-}} f(x)=\lim _{x \rightarrow 0^{-}} x^{2}=0^{2}=0 \text { है }
  > $$
  > 
  > तथा
  > 
  > $0$ पर $f$ के दाएँ पक्ष की सीमा
  > 
  > $$
  > \lim _{x \rightarrow 0^{+}} f(x)=\lim _{x \rightarrow 0^{+}} x=0 \text { है। }
  > $$
  > 
  > अत: $\lim _{x \rightarrow 0} f(x)=0=f(0)$ अतएव $0$ पर $f$ संतत है। इसका अर्थ यह हुआ कि $f$ अपने प्रांत के प्रत्येक बिंदु पर संतत है। अत: $f$ एक संतत फलन है।

### ex_5.7 — solution (hi)
- **Confidence:** high
- **Reason:** chapter.hi.pdf page 114 prints a parenthetical '(क्यों?)' ("why?") immediately after this limit equation, prompting the reader - omitted from extraction. Confirmed by the stage-5 verification batch.
- **Found:**
  > \lim _{x \rightarrow c} f(x)=\lim _{x \rightarrow c}(-x)=-c
  > $$
  > 
  > चूँकि
- **Should be:**
  > \lim _{x \rightarrow c} f(x)=\lim _{x \rightarrow c}(-x)=-c
  > $$
  > (क्यों?)
  > 
  > चूँकि

### ex_5.7 — solution (hi)
- **Confidence:** high
- **Reason:** chapter.hi.pdf page 114 prints a second parenthetical '(क्यों?)' after this second limit equation too - omitted from extraction. Confirmed by the stage-5 verification batch.
- **Found:**
  > \lim _{x \rightarrow c} f(x)=\lim _{x \rightarrow c} x=c
  > $$
  > 
  > क्योंकि
- **Should be:**
  > \lim _{x \rightarrow c} f(x)=\lim _{x \rightarrow c} x=c
  > $$
  > (क्यों?)
  > 
  > क्योंकि

### ex_5.25 — parts[0].solution (hi)
- **Confidence:** high
- **Reason:** OCR/extraction corrupted 'शृंखला' (chain) to 'श्रंखला' in part (i)'s solution; the source page clearly prints 'शृंखला नियम के प्रयोग द्वारा', and this item's own parts (iii)/(iv) correctly spell it 'शृंखला'. Confirmed by the stage-5 verification batch.
- **Found:**
  > अब श्रंखला नियम के प्रयोग द्वारा
- **Should be:**
  > अब शृंखला नियम के प्रयोग द्वारा

### ex_5.25 — parts[1].solution (hi)
- **Confidence:** high
- **Reason:** Same OCR/extraction corruption as part (i), but a different mis-spelling this time ('शंखला'); source page clearly prints 'अब शृंखला नियम द्वारा'. Confirmed by the stage-5 verification batch.
- **Found:**
  > अब शंखला नियम द्वारा
- **Should be:**
  > अब शृंखला नियम द्वारा

### q_5.5.17 — question (hi)
- **Confidence:** high
- **Reason:** chapter.hi.pdf page 143 shows the full question includes three labelled method-instructions and a verification instruction that extraction dropped entirely, ending right after '...तीन प्रकार से कीजिए:' with nothing following. Confirmed by the stage-5 verification batch, which rendered and read the actual page image.
- **Found:**
  > $\left(x^{2}-5 x+8\right)\left(x^{3}+7 x+9\right)$ का अवकलन निम्नलिखित तीन प्रकार से कीजिए:
- **Should be:**
  > $\left(x^{2}-5 x+8\right)\left(x^{3}+7 x+9\right)$ का अवकलन निम्नलिखित तीन प्रकार से कीजिए:
  > (i) गुणनफल नियम का प्रयोग करके
  > (ii) गुणनफल के विस्तारण द्वारा एक एकल बहुपद प्राप्त करके
  > (iii) लघुगणकीय अवकलन द्वारा
  > यह भी सत्यापित कीजिए कि इस प्रकार प्राप्त तीनों उत्तर समान हैं।

### q_5.5.17 — solution (hi)
- **Confidence:** high
- **Reason:** solutions.hi.pdf page 9 of its own internal pagination shows the complete three-method solution (product rule, expanded-polynomial, logarithmic differentiation, each independently deriving the same final derivative). Prior extraction truncated immediately after the very first line, dropping the entire remainder. Confirmed by the stage-5 verification batch via direct page-image comparison. Note: the source itself prints '5x^5' in the penultimate line of method (iii) (inconsistent with the same computation's own result one line later and with methods (i)/(ii)) and a doubled '==' in the final line - both genuine printed artifacts, transcribed exactly as printed per Rule 5, not corrected here.
- **Found:**
  > माना $y=\left(x^{2}-5 x+8\right)\left(x^{3}+7 x+9\right.$
- **Should be:**
  > माना $y=\left(x^{2}-5 x+8\right)\left(x^{3}+7 x+9\right)$
  > (i) गुणनफल नियम का प्रयोग करके अवकलन
  > 
  > $$
  > \begin{aligned}
  > \frac{d y}{d x} & =\left(x^{2}-5 x+8\right) \frac{d}{d x}\left(x^{3}+7 x+9\right)+\left(x^{3}+7 x+9\right) \frac{d}{d x}\left(x^{2}-5 x+8\right) \\
  > & =\left(x^{2}-5 x+8\right)\left(3 x^{2}+7\right)+\left(x^{3}+7 x+9\right)(2 x-5) \\
  > & =\left(3 x^{4}+7 x^{2}-15 x^{3}-35 x+24 x^{2}+56\right)+2 x^{4}-5 x^{3}+14 x^{2}-35 x+18 x-45 \\
  > & =5 x^{4}-20 x^{3}+45 x^{2}-52 x+11
  > \end{aligned}
  > $$
  > 
  > (ii) गुणनफल के विस्तारण द्वारा एक एकल बहुपद प्राप्त करके अवकलन
  > $y=\left(x^{2}-5 x+8\right)\left(x^{3}+7 x+9\right)$
  > $=x^{5}+7 x^{3}+9 x^{2}-5 x^{4}-35 x^{2}-45 x+8 x^{3}+56 x+72$
  > $=x^{5}-5 x^{4}+15 x^{3}-26 x^{2}+11 x+72$
  > 
  > $$
  > \begin{aligned}
  > \frac{d y}{d x} & =\frac{d}{d x} x^{5}-5 \frac{d}{d x} x^{4}+15 \frac{d}{d x} x^{3}-26 \frac{d}{d x} x^{2}+11 \frac{d}{d x} x+\frac{d}{d x} 72 \\
  > & =5 x^{4}-20 x^{3}+45 x^{2}-52 x+11
  > \end{aligned}
  > $$
  > 
  > (iii) लघुगणकीय अवकलन
  > $y=\left(x^{2}-5 x+8\right)\left(x^{3}+7 x+9\right)$
  > दोनों ओर log लेने पर, $\log y=\log \left(x^{2}-5 x+8\right)+\log \left(x^{3}+7 x+9\right)$
  > $\frac{1}{y} \cdot \frac{d y}{d x}=\frac{1}{x^{2}-5 x+8} \cdot(2 x-5)+\frac{1}{x^{3}+7 x+9} \cdot\left(3 x^{2}+7\right)$
  > $\frac{d y}{d x}=y\left[\frac{(2 x-5)\left(x^{3}+7 x+9\right)+\left(3 x^{2}+7\right)\left(x^{2}-5 x+8\right)}{\left(x^{2}-5 x+8\right)\left(x^{3}+7 x+9\right)}\right]$
  > $=y\left[\frac{2 x^{4}+14 x^{2}+18 x-5 x^{3}-35 x-45+3 x^{4}-15 x^{3}+24 x^{2}+7 x^{2}-35 x+56}{\left(x^{2}-5 x+8\right)\left(x^{3}+7 x+9\right)}\right]$
  > $\Rightarrow \frac{d y}{d x}=\left(x^{2}-5 x+8\right)\left(x^{3}+7 x+9\right)\left[\frac{5 x^{5}-20 x^{3}+45 x^{2}-52 x+11}{\left(x^{2}-5 x+8\right)\left(x^{3}+7 x+9\right)}\right]$
  > $\Rightarrow \frac{d y}{d x}==5 x^{4}-20 x^{3}+45 x^{2}-52 x+11$
  > 
  > अतः, इस प्रकार प्राप्त तीनों उत्तर समान हैं।

### ex_5.10 — solution (hi)
- **Confidence:** high
- **Reason:** extraction truncated mid-sentence immediately after '...दाएँ पक्ष की सीमा, अर्थात्', dropping the actual right-hand-limit computation and the concluding paragraph - confirmed on chapter.hi.pdf page 117 (file page 8) via 400dpi zoom. Same truncation class as ex_5.13, missed by the original stage-5 ex1-14 batch, caught during stage 7 formatting when a fork flagged the solution ending mid-sentence. Note: the source itself prints the second lim's subscript as x->1- (not x->1+, which would match the right-hand-limit context) - a genuine printed inconsistency, transcribed exactly as shown, not corrected.
- **Found:**
  > $x=1$ पर $f$ के दाएँ पक्ष की सीमा, अर्थात्
- **Should be:**
  > $x=1$ पर $f$ के दाएँ पक्ष की सीमा, अर्थात्
  > 
  > $$
  > \lim _{x \rightarrow 1^{+}} f(x)=\lim _{x \rightarrow 1^{-}}(x-2)=1-2=-1
  > $$
  > 
  > अब चूँकि $x=1$ पर $f$ के बाएँ तथा दाएँ पक्ष की सीमाएँ संपाती (coincident) नहीं हैं, अत: $x=1$ पर $f$ संतत नहीं है। इस प्रकार $f$ के असांतत्य का बिंदु केवल मात्र $x=1$ है। इस फलन का आलेख आकृति $5.4$ में दर्शाया गया है।
