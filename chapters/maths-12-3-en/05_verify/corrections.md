### ex_3.5 — solution (en)
- **Confidence:** high
- **Reason:** OCR corruption: dropped the equation a-2b=-3 and glued the remaining two equations together with a stray CJK ideographic-description character
- **Found:**
  > \begin{array}{rlrl} 
  > & 2 a+b & =4 & 5 c-d
  > \end{array}=11 . ⿱ r d c+3 d=24
- **Should be:**
  > \begin{array}{rlrl}
  > 2 a+b & =4, & 5 c-d & =11 \\
  > a-2 b & =-3, & 4 c+3 d & =24
  > \end{array}

### ex_3.19 — question (en)
- **Confidence:** high
- **Reason:** Textbook labels each row of matrix B with its own city arrow (row1 -> X, row2 -> Y); extraction dropped the Y row label entirely
- **Found:**
  > B=\left[\begin{array}{ccc}1000 & 500 & 5000 \\ 3000 & 1000 & 10,000\end{array}\right] \rightarrow X
- **Should be:**
  > B=\left[\begin{array}{ccc}1000 & 500 & 5000 \\ 3000 & 1000 & 10,000\end{array}\right] \begin{array}{l}\rightarrow \mathrm{X} \\ \rightarrow \mathrm{Y}\end{array}

### ex_3.19 — solution (en)
- **Confidence:** high
- **Reason:** Same row-label loss as the question: BA intermediate array is missing its Y-row label
- **Found:**
  > 120,000+100,000+500,000
  > \end{array}\right] \rightarrow \mathrm{X} \\
- **Should be:**
  > 120,000+100,000+500,000
  > \end{array}\right] \begin{array}{l}\rightarrow \mathrm{X} \\ \rightarrow \mathrm{Y}\end{array} \\

### ex_3.19 — solution (en)
- **Confidence:** high
- **Reason:** Same row-label loss as the question: final result array is missing its Y-row label
- **Found:**
  > 720,000
  > \end{array}\right] \rightarrow \mathrm{X}
  > \end{aligned}
- **Should be:**
  > 720,000
  > \end{array}\right] \begin{array}{l}\rightarrow \mathrm{X} \\ \rightarrow \mathrm{Y}\end{array}
  > \end{aligned}

### q_3.30 — question (en)
- **Confidence:** high
- **Reason:** This shared preamble paragraph introduces Exercises 21-22 (the next two questions); it does not belong to q_3.30 itself and was wrongly merged into its question field
- **Found:**
  > 
  > 
  > Assume X, Y, Z, W and P are matrices of order $2 \times n, 3 \times k, 2 \times p, n \times 3$ and $p \times k$, respectively. Choose the correct answer in Exercises 21 and 22.
- **Should be:**
  > 

### ex_3.21 — solution (en)
- **Confidence:** high
- **Reason:** Second matrix-product line mislabeled: textbook labels it B′A′ (the whole point of the example, verifying (AB)′=B′A′); extraction repeated A′ from the line above
- **Found:**
  > \\
  > & \mathrm{A}^{\prime}=\left[\begin{array}{r}
  > 1 \\
  > 3 \\
  > -6
  > \end{array}\right]\left[\begin{array}{lll}
  > -2 & 4 & 5
  > \end{array}\right]
- **Should be:**
  > \\
  > & \mathrm{B}^{\prime} \mathrm{A}^{\prime}=\left[\begin{array}{r}
  > 1 \\
  > 3 \\
  > -6
  > \end{array}\right]\left[\begin{array}{lll}
  > -2 & 4 & 5
  > \end{array}\right]

### q_3.38 — solution (en)
- **Confidence:** high
- **Reason:** Truncation: part (ii)'s given-matrix statement was dropped, leaving a mangled fragment
- **Found:**
  > & \text { It is given that } \quad(-\cos \alpha \\
  > & \text { Therefore, } \\
- **Should be:**
  > & \text { It is given that } A=\left(\begin{array}{cc}\sin \alpha & \cos \alpha \\ -\cos \alpha & \sin \alpha\end{array}\right) \\
  > & \text { Therefore, } \\

### sol_3.d.16 — solution (en)
- **Confidence:** high
- **Reason:** Row-operation annotation mislabeled: R1 was OCR'd as R3; the matrix entries themselves are correct
- **Found:**
  > R_{3} \rightarrow R_{3}+3 R_{3}
- **Should be:**
  > R_{1} \rightarrow R_{1}+3 R_{3}

### sol_3.misc.12 — solution (en)
- **Confidence:** high
- **Reason:** A full equation line (AB^1=B^1A) was dropped during extraction and "[Given]" was merged onto a stray second row
- **Found:**
  > P(1) & : & A B=B A & \\
  > & \Rightarrow & \text { [Given] }
  > \end{array}
- **Should be:**
  > P(1) & : & A B=B A & & [\text{Given}] \\
  > & \Rightarrow & A B^{1}=B^{1} A &
  > \end{array}

### q_3.54 — question (en)
- **Confidence:** high
- **Reason:** Matrix brackets around A were dropped during extraction
- **Found:**
  > \mathrm{A}=\begin{array}{cc}\alpha & \beta \\ \gamma & -\alpha\end{array}$ is such that
- **Should be:**
  > \mathrm{A}=\left[\begin{array}{cc}\alpha & \beta \\ \gamma & -\alpha\end{array}\right]$ is such that

### q_3.53 — solution (en)
- **Confidence:** medium
- **Reason:** Second matrix in this equality is rendered with determinant/absolute-value bars instead of matrix brackets, inconsistent with the identical matrix one line above and with a plain matrix-equality context
- **Found:**
  > \end{array}\right]=\left|\begin{array}{ccc}
  > -7 & -8 & -9 \\
  > 2 & 4 & 6
  > \end{array}\right|
- **Should be:**
  > \end{array}\right]=\left[\begin{array}{ccc}
  > -7 & -8 & -9 \\
  > 2 & 4 & 6
  > \end{array}\right]

### q_3.53 -- solution (en) [applied on explicit user sign-off, second pass]
- **Confidence:** medium
- **Reason:** Second matrix in this equality is rendered with determinant/absolute-value bars instead of matrix brackets, inconsistent with the identical matrix one line above and with a plain matrix-equality context
- **Found:**
  > \end{array}\right]=\left|\begin{array}{ccc}
  > -7 & -8 & -9 \\
  > 2 & 4 & 6
  > \end{array}\right|
- **Should be:**
  > \end{array}\right]=\left[\begin{array}{ccc}
  > -7 & -8 & -9 \\
  > 2 & 4 & 6
  > \end{array}\right]
