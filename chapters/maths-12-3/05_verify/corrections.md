### q_3.2.19 — question (hi)
- **Confidence:** high
- **Reason:** OCR dropped the े matra (transcribed 'बाँटं' instead of 'बाँटें'); confirmed against both chapter.hi.pdf p.29 and solutions.hi.pdf p.15, both clearly show 'बाँटें'
- **Found:**
  > प्रकार बाँटं जिससे
- **Should be:**
  > प्रकार बाँटें जिससे

### ex_3.16 — solution (hi)
- **Confidence:** high
- **Reason:** the (AB)(C) intermediate array was OCR'd as 3 columns instead of 4 - the 4th-column terms got dropped from their rows and one was stranded as a bogus extra row before the closing bracket. Confirmed against chapter.hi.pdf page 23.
- **Found:**
  > =\left[\begin{array}{rrr}
  > 2+2 & 4+0 & 6-2 \\
  > -1+36 & -2+0 & -3-36 \\
  > 1+30 & 2+0 & 3-30 \\
  > -4+18
  > \end{array}\right] \\
- **Should be:**
  > =\left[\begin{array}{rrrr}
  > 2+2 & 4+0 & 6-2 & -8+1 \\
  > -1+36 & -2+0 & -3-36 & 4+18 \\
  > 1+30 & 2+0 & 3-30 & -4+15
  > \end{array}\right] \\

### q_3.2.7 — parts[1].solution (hi)
- **Confidence:** high
- **Reason:** the subtrahend matrix's (2,2) entry is -6, so the source explicitly writes this subtraction as 0-(-6) (still yielding the correct final +6 shown in the boxed result); the extracted text drops the negative sign on the subtrahend, reading 0-6 instead - a sign that would give -6, contradicting the final answer entry of 6 immediately after it.
- **Found:**
  > 4-\frac{42}{5} & 0-6
- **Should be:**
  > 4-\frac{42}{5} & 0-(-6)

### q_3.3.2 — parts[1].solution (hi)
- **Confidence:** high
- **Reason:** source solutions.hi.pdf page 18 prints this exact concluding line for part (ii) (a copy-paste artifact repeating part (i)'s equality instead of part (ii)'s own); current extraction states the corrected version instead of the verbatim source reading. Stage 5's rule is transcription fidelity to the source, not textbook correctness - the same artifact was independently confirmed present in q_3.3.8's analogous part (ii).
- **Found:**
  > समीकरण (1) और (2) से,
  > $$
  > (A-B)^{\prime}=A^{\prime}-B^{\prime}
  > $$
- **Should be:**
  > समीकरण (1) और (2) से,
  > $$
  > (A+B)^{\prime}=A^{\prime}+B^{\prime}
  > $$

### q_3.9.2 — solution (hi)
- **Confidence:** high
- **Reason:** transcription duplicated a sentence that appears only once in the source
- **Found:**
  > इसलिए, आव्यूह $B^{\prime} A B$ एक सममित आव्यूह है।
  > यदि $A$ विषम सममित आव्यूह है। तब $A^{\prime}=-A$
  > यदि $A$ विषम सममित आव्यूह है। तब $A^{\prime}=-A$
- **Should be:**
  > इसलिए, आव्यूह $B^{\prime} A B$ एक सममित आव्यूह है।
  > यदि $A$ विषम सममित आव्यूह है। तब $A^{\prime}=-A$

### q_3.9.5 — solution (hi)
- **Confidence:** high
- **Reason:** matrix was garbled into 3 rows (2 columns) by an OCR line-split; the source shows a plain 2x2 result matrix, and the very next line's simplified matrix [[8,5],[-5,3]] confirms the intended entries
- **Found:**
  > \left[\begin{array}{cc}
  > 9 & 1 \\
  > -3 & 3+2 \\
  > -2 & -1+4
  > \end{array}\right]
- **Should be:**
  > \left[\begin{array}{cc}
  > 9-1 & 3+2 \\
  > -3-2 & -1+4
  > \end{array}\right]

### q_3.9.6 — solution (hi)
- **Confidence:** high
- **Reason:** solution was truncated mid-equation at stage 2 extraction; source (solutions.hi.pdf p.35-36, प्रश्न 9) contains the full resolution through the final answer
- **Found:**
  > \Rightarrow\left[x^{2}-2 x-40+2 x-8\right.
  > \end{array}\right]=[0] .0
  > $$
- **Should be:**
  > \Rightarrow\left[x^{2}-2 x-40+2 x-8\right]=[0]
  > \end{array}\right]
  > $$
  > 
  > $$
  > \Rightarrow x^{2}=48
  > $$
  > 
  > $$
  > \Rightarrow x=\pm 4 \sqrt{3}
  > $$
