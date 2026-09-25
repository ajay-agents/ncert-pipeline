### ex_4.12 — solution (en)
- **Confidence:** high
- **Reason:** Item boundary bleed from stage 2 extraction: everything from this point on is the textbook's own expository text between Example 12 and Example 13 (a Remark, Theorem 1 with verification, Definitions 4-5, Theorems 2-4 with proof) plus a stray OCR fragment ("133") - none of it is part of Example 12's own worked answer, which is complete and correct as everything before this point (confirmed directly against textbook page index 12, 0-indexed, printed page 88).
- **Found:**
  > 
  > 
  > Remark For a square matrix of order 2, given by
  > 
  > $$
  > \mathrm{A}=\left[\begin{array}{ll}
  > a_{11} & a_{12} \\
  > a_{21} & a_{22}
  > \end{array}\right]
  > $$
  > 
  > The $\operatorname{adj}$ A can also be obtained by interchanging $a_{11}$ and $a_{22}$ and by changing signs of $a_{12}$ and $a_{21}$, i.e.,
  > 
  > $$
  > \operatorname{adj} \mathrm{A}=\left[\begin{array}{cc}
  > a_{11} & a_{12} \\
  > a_{21} & a_{22}
  > \end{array}\right]=\left[\begin{array}{cc}
  > a_{22} & -a_{12} \\
  > -a_{21} & a_{11}
  > \end{array}\right]
  > $$
  > Change sign Interchange
  > 
  > We state the following theorem without proof.
  > Theorem 1 If A be any given square matrix of order $n$, then
  > 
  > $$
  > \mathrm{A}(\operatorname{adj} \mathrm{~A})=(\operatorname{adj} \mathrm{A}) \mathrm{A}=|\mathrm{A}| \mathrm{I},
  > $$
  > 
  > where I is the identity matrix of order $n$
  > Verification
  > 
  > Let
  > 
  > $$
  > \mathrm{A}=\left[\begin{array}{lll}
  > a_{11} & a_{12} & a_{13} \\
  > a_{21} & a_{22} & a_{23} \\
  > a_{31} & a_{32} & a_{33}
  > \end{array}\right] \text {, then } \text { adj } \mathrm{A}=\left[\begin{array}{lll}
  > \mathrm{A}_{11} & \mathrm{~A}_{21} & \mathrm{~A}_{31} \\
  > \mathrm{~A}_{12} & \mathrm{~A}_{22} & \mathrm{~A}_{32} \\
  > \mathrm{~A}_{13} & \mathrm{~A}_{23} & \mathrm{~A}_{33}
  > \end{array}\right]
  > $$
  > 
  > Since sum of product of elements of a row (or a column) with corresponding cofactors is equal to $|\mathrm{A}|$ and otherwise zero, we have
  > 
  > $$
  > \mathrm{A}(\operatorname{adj} \mathrm{~A})=\left[\begin{array}{ccc}
  > |\mathrm{A}| & 0 & 0 \\
  > 0 & |\mathrm{~A}| & 0 \\
  > 0 & 0 & |\mathrm{~A}|
  > \end{array}\right]=|\mathrm{A}|\left[\begin{array}{lll}
  > 1 & 0 & 0 \\
  > 0 & 1 & 0 \\
  > 0 & 0 & 1
  > \end{array}\right]=|\mathrm{A}| \mathrm{I}
  > $$
  > 
  > Similarly, we can show $(\operatorname{adj} \mathrm{A}) \mathrm{A}=|\mathrm{A}| \mathrm{I}$
  > Hence $\mathrm{A}(\operatorname{adj} \mathrm{A})=(\operatorname{adj} \mathrm{A}) \mathrm{A}=|\mathrm{A}| \mathrm{I}$
  > Definition 4 A square matrix A is said to be singular if $|\mathrm{A}|=0$.
  > For example, the determinant of matrix $\mathrm{A}=\begin{array}{ll}1 & 2 \\ 4 & 8\end{array}$ is zero
  > Hence A is a singular matrix.
  > Definition 5 A square matrix A is said to be non-singular if $|\mathrm{A}| \neq 0$
  > 
  > Let
  > 
  > $$
  > \mathrm{A}=\left[\begin{array}{ll}
  > 1 & 2 \\
  > 3 & 4
  > \end{array}\right] . \text { Then }|\mathrm{A}|=\left|\begin{array}{ll}
  > 1 & 2 \\
  > 3 & 4
  > \end{array}\right|=4-6=-2 \neq 0 .
  > $$
  > 
  > Hence A is a nonsingular matrix
  > We state the following theorems without proof.
  > Theorem 2 If A and B are nonsingular matrices of the same order, then AB and BA are also nonsingular matrices of the same order.
  > Theorem 3 The determinant of the product of matrices is equal to product of their respective determinants, that is, $|\mathrm{AB}|=|\mathrm{A}||\mathrm{B}|$, where A and B are square matrices of the same order
  > 
  > $$
  > |\mathrm{A}| \quad 0 \quad 0
  > $$
  > 
  > Remark We know that $(\operatorname{adj} \mathrm{A}) \mathrm{A}=|\mathrm{A}| \mathrm{I}=0 \quad|\mathrm{~A}| \quad 0,|\mathrm{~A}| \neq 0$
  > 
  > $$
  > 0 \quad 0 \quad|\mathrm{~A}|
  > $$
  > 
  > Writing determinants of matrices on both sides, we have
  > 
  > $$
  > |(\operatorname{adj} \mathrm{A}) \mathrm{A}|=\left|\begin{array}{ccc}
  > |\mathrm{A}| & 0 & 0 \\
  > 0 & |\mathrm{~A}| & 0 \\
  > 0 & 0 & |\mathrm{~A}|
  > \end{array}\right|
  > $$
  > 
  > i.e.
  > 
  > $$
  > |(\operatorname{adj} \mathrm{A})||\mathrm{A}|=|\mathrm{A}|^{3}\left|\begin{array}{lll}
  > 1 & 0 & 0 \\
  > 0 & 1 & 0 \\
  > 0 & 0 & 1
  > \end{array}\right|
  > $$
  > 
  > i.e.
  > 
  > $$
  > |(\operatorname{adj} \mathrm{A})||\mathrm{A}|=|\mathrm{A}|^{3}
  > $$
  > 
  > i.e.
  > 
  > $$
  > |(\operatorname{adj} \mathrm{A})|=|\mathrm{A}|^{2}
  > $$
  > 
  > In general, if A is $a$ square matrix of order $n$, then $|\operatorname{adj}(\mathrm{A})|=|\mathrm{A}|^{n-1}$.
  > Theorem 4 A square matrix A is invertible if and only if A is nonsingular matrix.
  > Proof Let A be invertible matrix of order $n$ and I be the identity matrix of order $n$.
  > Then, there exists a square matrix B of order $n$ such that $\mathrm{AB}=\mathrm{BA}=\mathrm{I}$
  > Now
  > 
  > $$
  > \mathrm{AB}=\mathrm{I} . \text { So }|\mathrm{AB}|=|\mathrm{I}| \quad \text { or } \quad|\mathrm{A}| \quad|\mathrm{B}|=1 \quad(\text { since }|\mathrm{I}|=1,|\mathrm{AB}|=|\mathrm{A}||\mathrm{B}|)
  > $$
  > 
  > This gives
  > 
  > $$
  > |\mathrm{A}| \neq 0 . \text { Hence } \mathrm{A} \text { is nonsingular. }
  > $$
  > 
  > Conversely, let A be nonsingular. Then $|\mathrm{A}| \neq 0$
  > Now
  > 
  > $$
  > \mathrm{A}(\operatorname{adj} \mathrm{~A})=(\operatorname{adj} \mathrm{A}) \mathrm{A}=|\mathrm{A}| \mathrm{I}
  > $$
  > 
  > or
  > 
  > $$
  > \mathrm{A}\left(\frac{1}{|\mathrm{~A}|} \operatorname{adj} \mathrm{A}\right)=\left(\frac{1}{|\mathrm{~A}|} \operatorname{adj} \mathrm{A}\right) \mathrm{A}=\mathrm{I}
  > $$
  > 
  > or
  > 
  > $$
  > \mathrm{AB}=\mathrm{BA}=\mathrm{I} \text {, where } \mathrm{B}=\frac{1}{|\mathrm{~A}|} \text { adj } \mathrm{A}
  > $$
  > 
  > Thus
  > 
  > $$
  > \mathrm{A} \text { is invertible and } \mathrm{A}^{-1}=\frac{1}{|\mathrm{~A}|} \text { adj } \mathrm{A}
  > $$
  > 
  > $$
  > 133
  > $$
- **Should be:**
  > 

### ex_4.19 — question (en)
- **Confidence:** high
- **Reason:** OCR garbled two 3x3 matrices in the product statement into digit soup ("023923"); confirmed against textbook page index 22 (0-indexed, printed page 98).
- **Found:**
  > Use product 023923 to solve the system of equations
- **Should be:**
  > Use product $\left[\begin{array}{ccc}1 & 1 & 2 \\ 0 & 2 & 3 \\ 3 & 2 & 4\end{array}\right]\left[\begin{array}{ccc}2 & 0 & 1 \\ 9 & 2 & 3 \\ 6 & 1 & 2\end{array}\right]$ to solve the system of equations

### ex_4.19 — question (en)
- **Confidence:** high
- **Reason:** The stray orphaned row "3 2 & 4" (a fragment of the same garbled matrix) was glued onto the system-of-equations array; the real system has only 3 equations, confirmed against the page.
- **Found:**
  > $$
  > \begin{array}{rl}
  > 3 \quad 2 & 4 \\
  > x-y+2 z & =1 \\
  > 2 y-3 z & =1 \\
  > 3 x-2 y+4 z & =2
  > \end{array}
  > $$
- **Should be:**
  > $$
  > \begin{array}{rl}
  > x-y+2 z & =1 \\
  > 2 y-3 z & =1 \\
  > 3 x-2 y+4 z & =2
  > \end{array}
  > $$

### ex_4.19 — solution (en)
- **Confidence:** high
- **Reason:** OCR garbled the "[matrix]^-1 = [matrix]" line into one malformed row; confirmed against textbook page index 22.
- **Found:**
  > $$
  > \begin{array}{lllll}
  > 1 & -1 & 2^{-1} & -2 & 0
  > \end{array}
  > $$
  > 
  > Hence
- **Should be:**
  > $$
  > \left[\begin{array}{ccc}
  > 1 & -1 & 2
  > \end{array}\right]^{-1}=\left[\begin{array}{ccc}
  > -2 & 0 & 1 \\
  > 9 & 2 & -3 \\
  > 6 & 1 & -2
  > \end{array}\right]
  > $$
  > 
  > Hence

### ex_4.13 — question (en)
- **Confidence:** high
- **Reason:** OCR collapsed the 3x3 matrix A into a bare number, apparently reading only its middle row; confirmed against textbook page index 12 (printed page 88) and the item's own solution field, which uses this same matrix correctly.
- **Found:**
  > \mathrm{A}=143
- **Should be:**
  > \mathrm{A}=\left[\begin{array}{lll}1 & 3 & 3 \\ 1 & 4 & 3 \\ 1 & 3 & 4\end{array}\right]

### ex_4.13 — question (en)
- **Confidence:** high
- **Reason:** Stray numeric fragment with no counterpart in the source (a scattered OCR remnant of the same matrix's third row); page goes directly from the question sentence into "Solution".
- **Found:**
  > 
  > 
  > $$
  > 134
  > $$
- **Should be:**
  > 

### ex_4.14 — solution (en)
- **Confidence:** high
- **Reason:** Bracket delimiters were dropped around both A^-1 and B^-1 (entries themselves correct); confirmed against textbook page index 15 (printed page 91).
- **Found:**
  > A^{-1}=-\frac{1}{11} \quad \begin{array}{cc}
  > -4 & -3 \\
  > -1 & 2
  > \end{array}, B^{-1}=\begin{array}{cc}
  > 3 & 2 \\
  > 1 & 1
  > \end{array}
- **Should be:**
  > A^{-1}=-\frac{1}{11}\left[\begin{array}{cc}
  > -4 & -3 \\
  > -1 & 2
  > \end{array}\right], B^{-1}=\left[\begin{array}{cc}
  > 3 & 2 \\
  > 1 & 1
  > \end{array}\right]

### ex_4.14 — solution (en)
- **Confidence:** high
- **Reason:** The B^-1 A^-1 matrix multiplication line is badly garbled (B^-1 misread as a fraction plus stray digits, A^-1 lost its second row, intermediate product lost its brackets); confirmed against textbook page index 15 - the final numeric answer was already correct.
- **Found:**
  > Therefore
  > 
  > $$
  > \mathrm{B}^{-1} \mathrm{~A}^{-1}=-\frac{1}{11} \quad \frac{3}{1} \quad 2 \quad 1 \quad-4 \quad-3 \quad=-\frac{1}{11} \quad \begin{array}{cc}
  > -14 & -5 \\
  > -5 & -1
  > \end{array} \quad=\frac{1}{11}\left[\begin{array}{cc}
  > 14 & 5 \\
  > 5 & 1
  > \end{array}\right]
  > $$
- **Should be:**
  > Therefore
  > 
  > $$
  > \mathrm{B}^{-1} \mathrm{~A}^{-1}=-\frac{1}{11}\left[\begin{array}{cc}
  > 3 & 2 \\
  > 1 & 1
  > \end{array}\right]\left[\begin{array}{cc}
  > -4 & -3 \\
  > -1 & 2
  > \end{array}\right]=-\frac{1}{11}\left[\begin{array}{cc}
  > -14 & -5 \\
  > -5 & -1
  > \end{array}\right]=\frac{1}{11}\left[\begin{array}{cc}
  > 14 & 5 \\
  > 5 & 1
  > \end{array}\right]
  > $$

### ex_4.15 — solution (en)
- **Confidence:** high
- **Reason:** Each occurrence of matrix A in A^2=A.A was wrapped in doubled bracket delimiters instead of one pair; entries and computed product are correct. Confirmed against textbook page index 16 (printed page 92).
- **Found:**
  > \left[\left[\begin{array}{ll}2 & 3 \\ 1 & 2\end{array}\right]\right]\left[\left[\begin{array}{ll}2 & 3 \\ 1 & 2\end{array}\right]\right]
- **Should be:**
  > \left[\begin{array}{ll}2 & 3 \\ 1 & 2\end{array}\right]\left[\begin{array}{ll}2 & 3 \\ 1 & 2\end{array}\right]

### sol_4.d.5 — solution (en)
- **Confidence:** high
- **Reason:** OCR collapsed a 3x3 determinant into a garbled 4-row/2-column array, dropping the middle row and the x entry; confirmed against the solutions-manual page.
- **Found:**
  > \Delta_{2} & =(-1)^{2}\left|\begin{array}{cc}
  > a & p \\
  > c & y \\
  > c & r \\
  > z
  > \end{array}\right| & \quad\left[R_{1} \leftrightarrow R_{2} \text { and } R_{2} \leftrightarrow R_{3}\right]
- **Should be:**
  > \Delta_{2} & =(-1)^{2}\left|\begin{array}{ccc}
  > a & p & x \\
  > b & q & y \\
  > c & r & z
  > \end{array}\right| & \quad\left[R_{1} \leftrightarrow R_{2} \text { and } R_{2} \leftrightarrow R_{3}\right]

### sol_4.d.7 — solution (en)
- **Confidence:** high
- **Reason:** Missing row-factoring label beside this line; confirmed present in the solutions-manual page.
- **Found:**
  > & =a b c\left|\begin{array}{ccc}
  > -a & b & c \\
  > a & -b & c \\
  > a & b & -c
  > \end{array}\right| & \\
- **Should be:**
  > & =a b c\left|\begin{array}{ccc}
  > -a & b & c \\
  > a & -b & c \\
  > a & b & -c
  > \end{array}\right| & \text { [Taking out factors } \left.a, b, c \text { from } R_{1}, R_{2}, R_{3}\right] \\

### sol_4.d.7 — solution (en)
- **Confidence:** high
- **Reason:** This line's label wrongly duplicates the row-factoring label from the previous line; the PDF shows the column-factoring label here instead.
- **Found:**
  > & =a^{2} b^{2} c^{2}\left|\begin{array}{ccc}
  > -1 & 1 & 1 \\
  > 1 & -1 & 1 \\
  > 1 & 1 & -1
  > \end{array}\right| & \text { [Taking out factors } \left.a, b, c \text { from } R_{1}, R_{2}, R_{3}\right] \\
- **Should be:**
  > & =a^{2} b^{2} c^{2}\left|\begin{array}{ccc}
  > -1 & 1 & 1 \\
  > 1 & -1 & 1 \\
  > 1 & 1 & -1
  > \end{array}\right| & \text { [Taking out factors } \left.a, b, c \text { from } C_{1}, C_{2}, C_{3}\right] \\

### sol_4.d.11 — solution (en)
- **Confidence:** high
- **Reason:** OCR collapsed the 3x3 matrix into a garbled 4-row/2-column array, dropping the y-column entries; confirmed against the solutions-manual page.
- **Found:**
  > \Delta & =\left|\begin{array}{cc}
  > 2(x+y+z) & x \\
  > 2(x+y+z) & y+z+2 x \\
  > 2(x+y+z) & x \\
  > z+x+2 y
  > \end{array}\right| \quad\left[C_{1} \rightarrow C_{1}+C_{2}+C_{3}\right] \\
- **Should be:**
  > \Delta & =\left|\begin{array}{ccc}
  > 2(x+y+z) & x & y \\
  > 2(x+y+z) & y+z+2 x & y \\
  > 2(x+y+z) & x & z+x+2 y
  > \end{array}\right| \quad\left[C_{1} \rightarrow C_{1}+C_{2}+C_{3}\right] \\

### sol_4.d.13 — solution (en)
- **Confidence:** high
- **Reason:** OCR collapsed the 3x3 matrix into a 3-row/2-column array, dropping the third column and merging rows; confirmed against the solutions-manual page.
- **Found:**
  > & =\left|\begin{array}{cc}
  > 1+a^{2}+b^{2} & 0 \\
  > 0 & -b\left(1+a^{2}+b^{2}\right) \\
  > 2 b & -2 a
  > \end{array}\right| \quad\left[R_{1} \rightarrow R_{1}+b R_{3} \text { and } R_{2} \rightarrow R_{2}-a R_{3}\right] \\
- **Should be:**
  > & =\left|\begin{array}{ccc}
  > 1+a^{2}+b^{2} & 0 & -b\left(1+a^{2}+b^{2}\right) \\
  > 0 & 1+a^{2}+b^{2} & a\left(1+a^{2}+b^{2}\right) \\
  > 2 b & -2 a & 1-a^{2}-b^{2}
  > \end{array}\right| \quad\left[R_{1} \rightarrow R_{1}+b R_{3} \text { and } R_{2} \rightarrow R_{2}-a R_{3}\right] \\

### sol_4.d.14 — solution (en)
- **Confidence:** high
- **Reason:** OCR collapsed the 3x3 matrix into a garbled 4-row/2-column array, dropping the c^2 column and merging rows; confirmed against the solutions-manual page.
- **Found:**
  > & =\left|\begin{array}{cc}
  > a^{2}+1 & b^{2} \\
  > -1 & 1 \\
  > -1 & 0 \\
  > 1 & 1
  > \end{array}\right| \\
- **Should be:**
  > & =\left|\begin{array}{ccc}
  > a^{2}+1 & b^{2} & c^{2} \\
  > -1 & 1 & 0 \\
  > -1 & 0 & 1
  > \end{array}\right| \\

### q_4.58 — question (en)
- **Confidence:** high
- **Reason:** This line is the textbook's own section header introducing Exercises 11-15 (it precedes Question 11/q_4.59 on the page), not part of this item's (Question 10) own question - misattached during extraction; confirmed against the textbook page.
- **Found:**
  > 
  > 
  > Using properties of determinants in Exercises 11 to 15, prove that:
- **Should be:**
  > 

### q_4.59 — solution (en)
- **Confidence:** high
- **Reason:** OCR dropped the leading digit "1" from a matrix entry (110 -> 10) in the X=A^-1 B step; the same entry is correctly "110" two lines earlier in this same solution and confirmed against the solutions-manual page.
- **Found:**
  > 75 & 150 & 75 \\
  > 10 & -100 & 30 \\
  > 72 & 0 & -24
  > \end{array}\right)\left[\begin{array}{l}
  > 4
- **Should be:**
  > 75 & 150 & 75 \\
  > 110 & -100 & 30 \\
  > 72 & 0 & -24
  > \end{array}\right)\left[\begin{array}{l}
  > 4

### q_4.42 — question (en)
- **Confidence:** high
- **Reason:** This line is the textbook's own section header introducing Exercises 7-14 (it sits between Exercise 6 and Exercise 7 on the page), not part of this item's (Question 6) own question - misattached during extraction; confirmed against the textbook page.
- **Found:**
  > 
  > 
  > Solve system of linear equations, using matrix method, in Exercises 7 to 14.
- **Should be:**
  >

### q_4.57 — solution (en)
- **Confidence:** high
- **Reason:** Trailing bare "##" markdown-heading marker bled in from the following page/section boundary during stage 2 extraction (the heading text itself was lost, only the marker survived) - the same known artifact class documented in maths-12-3-en's stage 6 noise-strip passes. Not part of the item's own answer.
- **Found:**
  > 
  > 
  > ##
- **Should be:**
  > 

### q_4.58 — solution (en)
- **Confidence:** high
- **Reason:** Same trailing bare "##" heading-bleed artifact as q_4.57 (this field also separately carries a leading "## Solution:" opener before the real derivation, which is a distinct, much more widespread pattern across nearly every exercise item in this chapter - left untouched here since CLAUDE.md assigns stripping redundant textbook openers to stage 8, not stage 5/6).
- **Found:**
  > \end{array}
  > $$
  > 
  > ##
- **Should be:**
  > \end{array}
  > $$

### sol_4.misc.11 — question (en)
- **Confidence:** high
- **Reason:** Same trailing bare "##" heading-bleed artifact.
- **Found:**
  > 
  > 
  > ##
- **Should be:**
  > 

### sol_4.misc.11 — solution (en)
- **Confidence:** high
- **Reason:** Same trailing bare "##" heading-bleed artifact.
- **Found:**
  > 
  > 
  > ##
- **Should be:**
  >

### q_4.32 — solution (en)
- **Confidence:** high
- **Reason:** OCR/typo: solving -1/b=-1 for b gives b=1, and the item's own final line already states "Thus, a=-4 and b=1" - "h=1" is a stray misread of "b=1" one step earlier, not a second variable. This was identified with high confidence during the original stage-5 verification batch but was missed when the corrections script was written; caught retroactively during stage 9's manual read-back and applied now as a stage-5 amendment, cascaded through 06/07/08/09.
- **Found:**
  > & \Rightarrow h=1
- **Should be:**
  > & \Rightarrow b=1
