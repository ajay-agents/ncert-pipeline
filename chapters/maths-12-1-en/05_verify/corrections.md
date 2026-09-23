### q_1.25 — question (en)
- **Confidence:** high
- **Reason:** Genuine mathpix extraction defect, not a source gap - confirmed by rendering the actual textbook page (chapter.en.pdf page 11, EXERCISE 1.2 item 9): the real printed question reads "Let f: N -> N be defined by f(n) = {(n+1)/2, if n is odd; n/2, if n is even} for all n in N." The extracted text was missing the entire lead-in clause and had the piecewise-case rows garbled/duplicated ("for all n in N." appearing twice, mid-definition). Reconstructed to match the actual PDF page using standard LaTeX piecewise-array notation, preserving the exact same content (odd case = (n+1)/2, even case = n/2) - nothing invented, only reassembled from what the source page actually shows.
- **Found:**
  > $\frac{n+1}{2}$, if $n$ is odd for all $n \in \mathbf{N}$. for all $n \in \mathbf{N}$. $\frac{n}{2}$, if $n$ is even
- **Should be:**
  > Let $f: \mathbf{N} \rightarrow \mathbf{N}$ be defined by $f(n)=\left\{\begin{array}{ll}\frac{n+1}{2}, & \text { if } n \text { is odd } \\\frac{n}{2}, & \text { if } n \text { is even }\end{array}\right.$ for all $n \in \mathbf{N}$.

### ex_1.1 — solution (en)
- **Confidence:** high
- **Reason:** Stage 2 extraction let general chapter narrative that follows this Example in the textbook (confirmed against chapter.en.pdf page 2) bleed into the Example's own solution field. The real solution ends where this correction's should_be ends; everything after that in found is expository text belonging to the surrounding chapter narrative (a Remark / Definition / discussion), not part of this worked example's own answer. Trim only - nothing invented, nothing of the Example's own solution removed.
- **Found:**
  > Since the school is boys school, no student of the school can be sister of any student of the school. Hence, $\mathrm{R}=\phi$, showing that R is the empty relation. It is also obvious that the difference between heights of any two students of the school has to be less than 3 meters. This shows that $\mathrm{R}^{\prime}=\mathrm{A} \times \mathrm{A}$ is the universal relation.
  > 
  > Remark In Class XI, we have seen two ways of representing a relation, namely raster method and set builder method. However, a relation $R$ in the set $\{1,2,3,4\}$ defined by $R$ $=\{(a, b): b=a+1\}$ is also expressed as $a \mathrm{R} b$ if and only if $b=a+1$ by many authors. We may also use this notation, as and when convenient.
  > 
  > If $(a, b) \in \mathrm{R}$, we say that $a$ is related to $b$ and we denote it as $a \mathrm{R} b$.
  > One of the most important relation, which plays a significant role in Mathematics, is an equivalence relation. To study equivalence relation, we first consider three types of relations, namely reflexive, symmetric and transitive.
  > Definition 3 A relation R in a set A is called
  > 
  > (i) reflexive, if $(a, a) \in \mathrm{R}$, for every $a \in \mathrm{~A}$,
  > (ii) symmetric, if $\left(a_{1}, a_{2}\right) \in \mathrm{R}$ implies that $\left(a_{2}, a_{1}\right) \in \mathrm{R}$, for all $a_{1}, a_{2} \in \mathrm{~A}$.
  > (iii) transitive, if $\left(a_{1}, a_{2}\right) \in \mathrm{R}$ and $\left(a_{2}, a_{3}\right) \in \mathrm{R}$ implies that $\left(a_{1}, a_{3}\right) \in \mathrm{R}$, for all $a_{1}, a_{2}$, $a_{3} \in \mathrm{~A}$.
  > 
  > Definition 4 A relation R in a set A is said to be an equivalence relation if R is reflexive, symmetric and transitive.
- **Should be:**
  > Since the school is boys school, no student of the school can be sister of any student of the school. Hence, $\mathrm{R}=\phi$, showing that R is the empty relation. It is also obvious that the difference between heights of any two students of the school has to be less than 3 meters. This shows that $\mathrm{R}^{\prime}=\mathrm{A} \times \mathrm{A}$ is the universal relation.

### ex_1.5 — solution (en)
- **Confidence:** high
- **Reason:** Stage 2 extraction let general chapter narrative that follows this Example in the textbook (confirmed against chapter.en.pdf pages 3-4) bleed into the Example's own solution field. The real solution ends where this correction's should_be ends; everything after that in found is expository text belonging to the surrounding chapter narrative (a Remark / Definition / discussion), not part of this worked example's own answer. Trim only - nothing invented, nothing of the Example's own solution removed.
- **Found:**
  > R is reflexive, as 2 divides $(a-a)$ for all $a \in \mathbf{Z}$. Further, if $(a, b) \in \mathrm{R}$, then 2 divides $a-b$. Therefore, 2 divides $b-a$. Hence, $(b, a) \in \mathrm{R}$, which shows that R is symmetric. Similarly, if $(a, b) \in \mathrm{R}$ and $(b, c) \in \mathrm{R}$, then $a-b$ and $b-c$ are divisible by 2. Now, $a-c=(a-b)+(b-c)$ is even (Why?). So, $(a-c)$ is divisible by 2 . This shows that R is transitive. Thus, R is an equivalence relation in $\mathbf{Z}$.
  > 
  > In Example 5, note that all even integers are related to zero, as $(0, \pm 2),(0, \pm 4)$ etc., lie in R and no odd integer is related to 0, as (0, ± 1), (0, ± 3) etc., do not lie in R. Similarly, all odd integers are related to one and no even integer is related to one. Therefore, the set E of all even integers and the set O of all odd integers are subsets of Z satisfying following conditions:
  > 
  > (i) All elements of E are related to each other and all elements of O are related to each other.
  > (ii) No element of E is related to any element of O and vice-versa.
  > (iii) E and O are disjoint and $\mathbf{Z}=\mathrm{E} \cup \mathrm{O}$.
  > 
  > The subset E is called the equivalence class containing zero and is denoted by [0]. Similarly, O is the equivalence class containing 1 and is denoted by [1]. Note that $[0] \neq[1],[0]=[2 r]$ and $[1]=[2 r+1], r \in \mathbf{Z}$. Infact, what we have seen above is true for an arbitrary equivalence relation R in a set X. Given an arbitrary equivalence relation R in an arbitrary set X, R divides X into mutually disjoint subsets $\mathrm{A}_{i}$ called partitions or subdivisions of X satisfying:
  > 
  > (i) all elements of $\mathrm{A}_{i}$ are related to each other, for all $i$.
  > (ii) no element of $\mathrm{A}_{i}$ is related to any element of $\mathrm{A}_{j}, i \neq j$.
  > (iii) $\cup \mathrm{A}_{j}=\mathrm{X}$ and $\mathrm{A}_{i} \cap \mathrm{~A}_{j}=\phi, i \neq j$.
  > 
  > The subsets $\mathrm{A}_{i}$ are called equivalence classes. The interesting part of the situation is that we can go reverse also. For example, consider a subdivision of the set $\mathbf{Z}$ given by three mutually disjoint subsets $\mathrm{A}_{1}, \mathrm{~A}_{2}$ and $\mathrm{A}_{3}$ whose union is $\mathbf{Z}$ with
  > 
  > $$
  > \begin{aligned}
  > & \mathrm{A}_{1}=\{x \in \mathbf{Z}: x \text { is a multiple of } 3\}=\{\ldots,-6,-3,0,3,6, \ldots\} \\
  > & \mathrm{A}_{2}=\{x \in \mathbf{Z}: x-1 \text { is a multiple of } 3\}=\{\ldots,-5,-2,1,4,7, \ldots\} \\
  > & \mathrm{A}_{3}=\{x \in \mathbf{Z}: x-2 \text { is a multiple of } 3\}=\{\ldots,-4,-1,2,5,8, \ldots\}
  > \end{aligned}
  > $$
  > 
  > Define a relation R in $\mathbf{Z}$ given by $\mathrm{R}=\{(a, b): 3$ divides $a-b\}$. Following the arguments similar to those used in Example 5, we can show that R is an equivalence relation. Also, $\mathrm{A}_{1}$ coincides with the set of all integers in $\mathbf{Z}$ which are related to zero, $\mathrm{A}_{2}$ coincides with the set of all integers which are related to 1 and $\mathrm{A}_{3}$ coincides with the set of all integers in $\mathbf{Z}$ which are related to 2 . Thus, $\mathrm{A}_{1}=[0], \mathrm{A}_{2}=[1]$ and $\mathrm{A}_{3}=[2]$. In fact, $\mathrm{A}_{1}=[3 r], \mathrm{A}_{2}=[3 r+1]$ and $\mathrm{A}_{3}=[3 r+2]$, for all $r \in \mathbf{Z}$.
- **Should be:**
  > R is reflexive, as 2 divides $(a-a)$ for all $a \in \mathbf{Z}$. Further, if $(a, b) \in \mathrm{R}$, then 2 divides $a-b$. Therefore, 2 divides $b-a$. Hence, $(b, a) \in \mathrm{R}$, which shows that R is symmetric. Similarly, if $(a, b) \in \mathrm{R}$ and $(b, c) \in \mathrm{R}$, then $a-b$ and $b-c$ are divisible by 2. Now, $a-c=(a-b)+(b-c)$ is even (Why?). So, $(a-c)$ is divisible by 2 . This shows that R is transitive. Thus, R is an equivalence relation in $\mathbf{Z}$.

### ex_1.14 — solution (en)
- **Confidence:** high
- **Reason:** Stage 2 extraction let general chapter narrative that follows this Example in the textbook (confirmed against chapter.en.pdf page 10) bleed into the Example's own solution field. The real solution ends where this correction's should_be ends; everything after that in found is expository text belonging to the surrounding chapter narrative (a Remark / Definition / discussion), not part of this worked example's own answer. Trim only - nothing invented, nothing of the Example's own solution removed.
- **Found:**
  > Since $f$ is one-one, three elements of $\{1,2,3\}$ must be taken to 3 different elements of the co-domain $\{1,2,3\}$ under $f$. Hence, $f$ has to be onto.
  > 
  > Remark The results mentioned in Examples 13 and 14 are also true for an arbitrary finite set X, i.e., a one-one function $f: \mathrm{X} \rightarrow \mathrm{X}$ is necessarily onto and an onto map $f: \mathrm{X} \rightarrow \mathrm{X}$ is necessarily one-one, for every finite set X . In contrast to this, Examples 8 and 10 show that for an infinite set, this may not be true. In fact, this is a characteristic difference between a finite and an infinite set.
- **Should be:**
  > Since $f$ is one-one, three elements of $\{1,2,3\}$ must be taken to 3 different elements of the co-domain $\{1,2,3\}$ under $f$. Hence, $f$ has to be onto.

### ex_1.16 — solution (en)
- **Confidence:** high
- **Reason:** Stage 2 extraction let general chapter narrative that follows this Example in the textbook (confirmed against chapter.en.pdf page 12) bleed into the Example's own solution field. The real solution ends where this correction's should_be ends; everything after that in found is expository text belonging to the surrounding chapter narrative (a Remark / Definition / discussion), not part of this worked example's own answer. Trim only - nothing invented, nothing of the Example's own solution removed.
- **Found:**
  > We have $g o f(x)=g(f(x))=g(\cos x)=3(\cos x)^{2}=3 \cos ^{2} x$. Similarly, $f o g(x)=f(g(x))=f\left(3 x^{2}\right)=\cos \left(3 x^{2}\right)$. Note that $3 \cos ^{2} x \neq \cos 3 x^{2}$, for $x=0$. Hence, gof $\neq$ fog .
  > Definition 9 A function $f: \mathrm{X} \rightarrow \mathrm{Y}$ is defined to be invertible, if there exists a function $g: \mathrm{Y} \rightarrow \mathrm{X}$ such that $g \circ f=\mathrm{I}_{\mathrm{X}}$ and fog $=\mathrm{I}_{\mathrm{Y}}$. The function $g$ is called the inverse of $f$ and is denoted by $f^{-1}$.
  > 
  > Thus, if $f$ is invertible, then $f$ must be one-one and onto and conversely, if $f$ is one-one and onto, then $f$ must be invertible. This fact significantly helps for proving a function $f$ to be invertible by showing that $f$ is one-one and onto, specially when the actual inverse of $f$ is not to be determined.
- **Should be:**
  > We have $g o f(x)=g(f(x))=g(\cos x)=3(\cos x)^{2}=3 \cos ^{2} x$. Similarly, $f o g(x)=f(g(x))=f\left(3 x^{2}\right)=\cos \left(3 x^{2}\right)$. Note that $3 \cos ^{2} x \neq \cos 3 x^{2}$, for $x=0$. Hence, gof $\neq$ fog .

### q_1.1 — solution (en)
- **Confidence:** high
- **Reason:** Genuine same-page logical self-contradiction in the official solutions manual itself, confirmed against the actual PDF page (solutions.en.pdf page 2, 0-indexed page 1) via direct page-image render - not a mathpix OCR artifact, mathpix faithfully transcribed exactly what the book prints. Part (iv) states the relation R = {(x,y): x-y is an integer} on Z, then reasons "(x,x) not-in R because x-x=0 is an integer" and concludes "So, R is reflexive" - a direct contradiction, since reflexivity requires (x,x) to belong to R, and the stated reasoning (x-x=0 is an integer) is exactly why (x,x) SHOULD belong to R per the relation's own definition. Every other step of this part's proof (symmetric, transitive) and every other part of this item is correct and internally consistent; only the "not-in" (should be "in") in this one sentence is wrong. User explicitly reviewed this exact finding (with the PDF-page confirmation) via AskUserQuestion and approved correcting it to match the surrounding proof's own correct logic, rather than leaving the printed contradiction in place.
- **Found:**
  > For $x \in \mathrm{Z},(x, x) \notin R$ because $x-x=0$ is an integer.
  > So, R is reflexive.
- **Should be:**
  > For $x \in \mathrm{Z},(x, x) \in R$ because $x-x=0$ is an integer.
  > So, R is reflexive.
