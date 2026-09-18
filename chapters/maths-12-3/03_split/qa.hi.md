---
subject: maths
class: 12
chapter: 3
lang: hi
title: "आव्यूह"
---

# आव्यूह

## प्रश्न और हल

:::question{number="3.1.1" kind="exercise" id="q_3.1.1" topic="Matrix order and elements"}
#### प्रश्न 3.1.1

:::prompt
आव्यूह $\mathrm{A}=\left[\begin{array}{cccc}2 & 5 & 19 & -7 \\ 35 & -2 & \frac{5}{2} & 12 \\ \sqrt{3} & 1 & -5 & 17\end{array}\right]$, के लिए ज्ञात कीजिए:
:::

:::part
:::prompt
आव्यूह की कोटि
:::

:::solution
आव्यूह की कोटि = पंक्तियों की संख्या $\times$ स्तंभों की संख्या $=3 \times 4$
:::

:::answer
**उत्तर:** $3 \times 4$
:::

:::

:::part
:::prompt
अवयवों की संख्या
:::

:::solution
अवयवों की संख्या $=3 \times 4=12$
:::

:::answer
**उत्तर:** $12$
:::

:::

:::part
:::prompt
अवयव $a_{13}, a_{21}, a_{33}, a_{24}, a_{23}$
:::

:::solution
अवयव $a_{13}=19, a_{21}=35, a_{33}=-5, a_{24}=12, a_{23}=\frac{5}{2}$
:::

:::answer
**उत्तर:** $a_{13}=19, a_{21}=35, a_{33}=-5, a_{24}=12, a_{23}=\frac{5}{2}$
:::

:::

:::

:::question{number="3.1.2" kind="exercise" id="q_3.1.2" topic="Possible orders from element count"}
#### प्रश्न 3.1.2

:::prompt
यदि किसी आव्यूह में $24$ अवयव हैं तो इसकी संभव कोटियाँ क्या हैं? यदि इसमें $13$ अवयव हों तो कोटियाँ क्या होंगी?
:::

:::solution{label="हल"}
आव्यूह में कुल अवयव $=24$
इसलिए, आव्यूह की संभव कोटियाँ निम्नलिखित हैं:
$1 \times 24,2 \times 12,3 \times 8,4 \times 6,6 \times 4,8 \times 3,12 \times 2$ और $24 \times 1$
यदि इसमें $13$ अवयव हों तो कोटियाँ निम्नलिखित होंगी: $13 \times 1$ और $1 \times 13$
:::

:::

:::question{number="3.1.3" kind="exercise" id="q_3.1.3" topic="Possible orders from element count"}
#### प्रश्न 3.1.3

:::prompt
यदि किसी आव्यूह में $18$ अवयव हैं तो इसकी संभव कोटियाँ क्या हैं? यदि इसमें $5$ अवयव हों तो क्या होगा?
:::

:::solution{label="हल"}
आव्यूह में कुल अवयव $=18$
इसलिए, आव्यूह की संभव कोटियाँ निम्नलिखित हैं:
$1 \times 18,2 \times 9,3 \times 6,6 \times 3,9 \times 2$ और $18 \times 1$
यदि इसमें $5$ अवयव हों तो कोटियाँ निम्नलिखित होंगी: $5 \times 1$ और $1 \times 5$
:::

:::

:::question{number="3.1.4" kind="exercise" id="q_3.1.4" topic="Constructing 2×2 matrix from formula"}
#### प्रश्न 3.1.4

:::prompt
एक $2 \times 2$ आव्यूह $\mathrm{A}=\left[a_{i j}\right]$ की रचना कीजिए जिसके अवयव निम्नलिखित प्रकार से प्रदत्त हैं
:::

:::part
:::prompt
$a_{i j}=\frac{(i+j)^{2}}{2}$
:::

:::solution
यहाँ $a_{i j}=\frac{(i+j)^{2}}{2}$, इसलिए, आव्यूह के अवयव:
$a_{11}=\frac{(1+1)^{2}}{2}=2, \quad a_{12}=\frac{(1+2)^{2}}{2}=\frac{9}{2}$,
$a_{21}=\frac{(2+1)^{2}}{2}=\frac{9}{2}, \quad a_{22}=\frac{(2+2)^{2}}{2}=8$,
इसलिए, आव्यूह $=\left[\begin{array}{cc}2 & \frac{9}{2} \\ \frac{9}{2} & 8\end{array}\right]$
:::

:::answer
**उत्तर:** $\left[\begin{array}{cc}2 & \frac{9}{2} \\ \frac{9}{2} & 8\end{array}\right]$
:::

:::

:::part
:::prompt
$a_{i j}=\frac{i}{j}$
:::

:::solution
यहाँ, $a_{i j}=\frac{i}{j}$, इसलिए, आव्यूह के अवयव:
$a_{11}=\frac{1}{1}=1, \quad a_{12}=\frac{1}{2}$,
$a_{21}=\frac{2}{1}=2, \quad a_{22}=\frac{2}{2}=1$
इसलिए, आव्यूह $=\left[\begin{array}{ll}1 & \frac{1}{2} \\ 2 & 1\end{array}\right]$
:::

:::answer
**उत्तर:** $\left[\begin{array}{ll}1 & \frac{1}{2} \\ 2 & 1\end{array}\right]$
:::

:::

:::part
:::prompt
$a_{i j}=\frac{(i+2 j)^{2}}{2}$
:::

:::solution
यहाँ $a_{i j}=\frac{(i+2 j)^{2}}{2}$, इसलिए, आव्यूह के अवयव:
$a_{11}=\frac{(1+2)^{2}}{2}=\frac{9}{2}, \quad a_{12}=\frac{(1+4)^{2}}{2}=\frac{25}{2}$,
$a_{21}=\frac{(2+2)^{2}}{2}=8, \quad a_{22}=\frac{(2+4)^{2}}{2}=18$
इसलिए, आव्यूह $=\left[\begin{array}{cc}\frac{9}{2} & \frac{25}{2} \\ 8 & 18\end{array}\right]$
:::

:::answer
**उत्तर:** $\left[\begin{array}{cc}\frac{9}{2} & \frac{25}{2} \\ 8 & 18\end{array}\right]$
:::

:::

:::

:::question{number="3.1.5" kind="exercise" id="q_3.1.5" topic="Constructing 3×4 matrix from formula"}
#### प्रश्न 3.1.5

:::prompt
एक $3 \times 4$ आव्यूह की रचना कीजिए जिसके अवयव निम्नलिखित प्रकार से प्राप्त होते हैं:
:::

:::part
:::prompt
$a_{i j}=\frac{1}{2}|-3 i+j|$
:::

:::solution
यहाँ $a_{i j}=\frac{1}{2}|-3 i+j|$, इसलिए, आव्यूह के अवयव:
$a_{11}=\frac{1}{2}|-3+1|=1, \quad a_{12}=\frac{1}{2}|-3+2|=\frac{1}{2}, \quad a_{13}=\frac{1}{2}|-3+3|=0, \quad a_{14}=\frac{1}{2}|-3+4|=\frac{1}{2}$,
$a_{21}=\frac{1}{2}|-6+1|=\frac{5}{2}, \quad a_{22}=\frac{1}{2}|-6+2|=2, \quad a_{23}=\frac{1}{2}|-6+3|=\frac{3}{2}, \quad a_{24}=\frac{1}{2}|-6+4|=1$,
$a_{31}=\frac{1}{2}|-9+1|=4, \quad a_{32}=\frac{1}{2}|-9+2|=\frac{7}{2}, \quad a_{33}=\frac{1}{2}|-9+3|=3, \quad a_{34}=\frac{1}{2}|-9+4|=\frac{5}{2}$
:::

:::answer
**उत्तर:** $\left[\begin{array}{cccc}1 & \frac{1}{2} & 0 & \frac{1}{2} \\ \frac{5}{2} & 2 & \frac{3}{2} & 1 \\ 4 & \frac{7}{2} & 3 & \frac{5}{2}\end{array}\right]$
:::

:::

:::part
:::prompt
$a_{i j}=2 i-j$
:::

:::solution
यहाँ $a_{i j}=2 i-j$, इसलिए, आव्यूह के अवयव:
$a_{11}=2-1=1, \quad a_{12}=2-2=0, \quad a_{13}=2-3=-1, \quad a_{14}=2-4=-2$,
$a_{21}=4-1=3, \quad a_{22}=4-2=2, \quad a_{23}=4-3=1, \quad a_{24}=4-4=0$,
$a_{31}=6-1=5, \quad a_{32}=6-2=4, \quad a_{33}=6-3=3, \quad a_{34}=6-4=2$,
इसलिए, आव्यूह $=\left[\begin{array}{cccc}1 & 0 & -1 & -2 \\ 3 & 2 & 1 & 0 \\ 5 & 4 & 3 & 2\end{array}\right]$
:::

:::answer
**उत्तर:** $\left[\begin{array}{cccc}1 & 0 & -1 & -2 \\ 3 & 2 & 1 & 0 \\ 5 & 4 & 3 & 2\end{array}\right]$
:::

:::

:::

:::question{number="3.1.6" kind="exercise" id="q_3.1.6" topic="Solving matrix equality equations"}
#### प्रश्न 3.1.6

:::prompt
निम्नलिखित समीकरणों से $x, y$ तथा $z$ के मान ज्ञात कीजिए:
:::

:::part
:::prompt
$\left[\begin{array}{ll}4 & 3 \\ x & 5\end{array}\right]=\left[\begin{array}{ll}y & z \\ 1 & 5\end{array}\right]$
:::

:::solution
यदि दो आव्यूह समान हैं तो उनके संगत अवयव भी समान होते हैं, इसलिए $4=y, \quad 3=z$ तथा $x=1$
:::

:::answer
**उत्तर:** $x=1, y=4, z=3$
:::

:::

:::part
:::prompt
$\left[\begin{array}{cc}x+y & 2 \\ 5+z & x y\end{array}\right]=\left[\begin{array}{ll}6 & 2 \\ 5 & 8\end{array}\right]$
:::

:::solution
यदि दो आव्यूह समान हैं तो उनके संगत अवयव भी समान होते हैं, इसलिए $x+y=6, \quad 5+z=5$ तथा $x y=8$
हल करने पर, $x=2, y=4$ तथा $z=0$ या $x=4, y=2$ तथा $z=0$
:::

:::answer
**उत्तर:** $x=2, y=4, z=0$ या $x=4, y=2, z=0$
:::

:::

:::part
:::prompt
$\left[\begin{array}{c}x+y+z \\ x+z \\ y+z\end{array}\right]=\left[\begin{array}{c}9 \\ 5 \\ 7\end{array}\right]$
:::

:::solution
यदि दो आव्यूह समान हैं तो उनके संगत अवयव भी समान होते हैं, इसलिए $x+y+z=9, \quad x+z=5$ तथा $y+z=7$
हल करने पर, $x=2, y=4$ तथा $z=3$
:::

:::answer
**उत्तर:** $x=2, y=4, z=3$
:::

:::

:::

:::question{number="3.1.7" kind="exercise" id="q_3.1.7" topic="Solving matrix equality for constants"}
#### प्रश्न 3.1.7

:::prompt
समीकरण $\left[\begin{array}{cc}a-b & 2 a+c \\ 2 a-b & 3 c+d\end{array}\right]=\left[\begin{array}{cc}-1 & 5 \\ 0 & 13\end{array}\right]$ से $a, b, c$ तथा $d$ के मान ज्ञात कीजिए।
:::

:::solution{label="हल"}
यदि दो आव्यूह समान हैं तो उनके संगत अवयव भी समान होते हैं, इसलिए
$a-b=-1$
$2 a-b=0$
$2 a+c=5$
$3 c+d=13$
समीकरण (1) और (2) को हल करने पर
$a=1, \quad b=2$
$a$ का मान समीकरण (3) में रखने पर
$c=3$
$c$ का मान समीकरण (4) में रखने पर
$d=4$
:::

:::answer
**उत्तर:** $a=1, b=2, c=3, d=4$
:::

:::

:::question{number="3.1.8" kind="exercise" id="q_3.1.8" topic="Condition for square matrix (MCQ)"}
#### प्रश्न 3.1.8

:::prompt
$\mathrm{A}=\left[a_{i j}\right]_{m \times n}$ एक वर्ग आव्यूह है यदि
(A) $m<n$
(B) $m>n$
(C) $m=n$
(D) इनमें से कोई नहीं
:::

:::solution{label="हल"}
एक वर्ग आव्यूह में स्तंभों की संख्या पंक्तियों की संख्या के बराबर होती है, इसलिए विकल्प (C) सही है।
:::

:::answer
**उत्तर:** (C) $m=n$
:::

:::

:::question{number="3.1.9" kind="exercise" id="q_3.1.9" topic="Equal matrices and unique values (MCQ)"}
#### प्रश्न 3.1.9

:::prompt
$x$ तथा $y$ के प्रदत्त किन मानों के लिए आव्यूहों के निम्नलिखित युग्म समान हैं?
$\left[\begin{array}{cc}3 x+7 & 5 \\ y+1 & 2-3 x\end{array}\right],\left[\begin{array}{cc}0 & y-2 \\ 8 & 4\end{array}\right]$
(A) $x=\frac{-1}{3}, y=7$
(B) ज्ञात करना संभव नहीं है
(C) $y=7, x=\frac{-2}{3}$
(D) $x=\frac{-1}{3}, y=\frac{-2}{3}$
:::

:::solution{label="हल"}
यहाँ, $\left[\begin{array}{cc}3 x+7 & 5 \\ y+1 & 2-3 x\end{array}\right]=\left[\begin{array}{cc}0 & y-2 \\ 8 & 4\end{array}\right]$
यदि दो आव्यूह समान हैं तो उनके संगत अवयव भी समान होते हैं,
इसलिए
$3 x+7=0, \quad 5=y-2, \quad y-1=8$ तथा $2-3 x=4$
हल करने पर, $y=7, x=-\frac{7}{2}$ तथा $x=-\frac{2}{3}$, इस प्रकार $x$ का कोई अद्वितीय मान नहीं है। इसलिए विकल्प (B) सही है।
:::

:::answer
**उत्तर:** (B) ज्ञात करना संभव नहीं है
:::

:::

:::question{number="3.1.10" kind="exercise" id="q_3.1.10" topic="Counting 0-1 matrices (MCQ)"}
#### प्रश्न 3.1.10

:::prompt
$3 \times 3$ कोटि के ऐसे आव्यूहों की कुल कितनी संख्या होगी जिनकी प्रत्येक प्रविष्टि $0$ या $1$ है?
(A) $27$
(B) $18$
(C) $81$
(D) $512$
:::

:::solution{label="हल"}
$3 \times 3$ कोटि के आव्यूह में अवयवों की कुल संख्या $=9$
यदि प्रत्येक प्रविष्टि $0$ या $1$ है, तो प्रत्येक अवयव के लिए क्रमचय $=2$
इसलिए अवयवों के लिए कुल क्रमचय $=2^{9}=512$
इसलिए विकल्प (D) सही है।
:::

:::answer
**उत्तर:** (D) $512$
:::

:::

:::question{number="3.2.1" kind="exercise" id="q_3.2.1" topic="Matrix addition, subtraction, multiplication"}
#### प्रश्न 3.2.1

:::prompt
मान लीजिए कि $\mathrm{A}=\left[\begin{array}{ll}2 & 4 \\ 3 & 2\end{array}\right], \mathrm{B}=\left[\begin{array}{rr}1 & 3 \\ -2 & 5\end{array}\right], \mathrm{C}=\left[\begin{array}{rr}-2 & 5 \\ 3 & 4\end{array}\right]$, तो निम्नलिखित ज्ञात कीजिए:
:::

:::part
:::prompt
$\mathrm{A}+\mathrm{B}$
:::

:::solution
$A+B=\left[\begin{array}{ll}2 & 4 \\ 3 & 2\end{array}\right]+\left[\begin{array}{cc}1 & 3 \\ -2 & 5\end{array}\right]=\left[\begin{array}{ll}2+1 & 4+3 \\ 3-2 & 2+5\end{array}\right]=\left[\begin{array}{ll}3 & 7 \\ 1 & 7\end{array}\right]$
:::

:::answer
**उत्तर:** $\left[\begin{array}{ll}3 & 7 \\ 1 & 7\end{array}\right]$
:::

:::

:::part
:::prompt
$\mathrm{A}-\mathrm{B}$
:::

:::solution
$A-B=\left[\begin{array}{ll}2 & 4 \\ 3 & 2\end{array}\right]-\left[\begin{array}{cc}1 & 3 \\ -2 & 5\end{array}\right]=\left[\begin{array}{ll}2-1 & 4-3 \\ 3+2 & 2-5\end{array}\right]=\left[\begin{array}{cc}1 & 1 \\ 5 & -3\end{array}\right]$
:::

:::answer
**उत्तर:** $\left[\begin{array}{cc}1 & 1 \\ 5 & -3\end{array}\right]$
:::

:::

:::part
:::prompt
3A - C
:::

:::solution
$3 A-C=3\left[\begin{array}{ll}2 & 4 \\ 3 & 2\end{array}\right]-\left[\begin{array}{cc}-2 & 5 \\ 3 & 4\end{array}\right]=\left[\begin{array}{cc}6 & 12 \\ 9 & 6\end{array}\right]-\left[\begin{array}{cc}-2 & 5 \\ 3 & 4\end{array}\right]=\left[\begin{array}{cc}6+2 & 12-5 \\ 9-3 & 6-4\end{array}\right]=\left[\begin{array}{ll}8 & 7 \\ 6 & 2\end{array}\right]$
:::

:::answer
**उत्तर:** $\left[\begin{array}{ll}8 & 7 \\ 6 & 2\end{array}\right]$
:::

:::

:::part
:::prompt
AB
:::

:::solution
$A B=\left[\begin{array}{ll}2 & 4 \\ 3 & 2\end{array}\right]\left[\begin{array}{cc}1 & 3 \\ -2 & 5\end{array}\right]=\left[\begin{array}{ll}2 \times 1+4 \times(-2) & 2 \times 3+4 \times 5 \\ 3 \times 1+2 \times(-2) & 3 \times 3+2 \times 5\end{array}\right]=\left[\begin{array}{ll}-6 & 26 \\ -1 & 19\end{array}\right]$
:::

:::answer
**उत्तर:** $\left[\begin{array}{ll}-6 & 26 \\ -1 & 19\end{array}\right]$
:::

:::

:::part
:::prompt
BA
:::

:::solution
$B A=\left[\begin{array}{cc}1 & 3 \\ -2 & 5\end{array}\right]\left[\begin{array}{ll}2 & 4 \\ 3 & 2\end{array}\right]=\left[\begin{array}{cc}1 \times 2+3 \times 3 & 1 \times 4+3 \times 2 \\ -2 \times 2+5 \times 3 & -2 \times 4+5 \times 2\end{array}\right]=\left[\begin{array}{cc}11 & 10 \\ 11 & 2\end{array}\right]$
:::

:::answer
**उत्तर:** $\left[\begin{array}{cc}11 & 10 \\ 11 & 2\end{array}\right]$
:::

:::

:::

:::question{number="3.2.2" kind="exercise" id="q_3.2.2" topic="Matrix addition simplification"}
#### प्रश्न 3.2.2

:::prompt
निम्नलिखित को परिकलित कीजिए:
:::

:::part
:::prompt
$\left[\begin{array}{cc}a & b \\ -b & a\end{array}\right]+\left[\begin{array}{ll}a & b \\ b & a\end{array}\right]$
:::

:::solution
$\left[\begin{array}{cc}a & b \\ -b & a\end{array}\right]+\left[\begin{array}{ll}a & b \\ b & a\end{array}\right]=\left[\begin{array}{cc}a+a & b+b \\ -b+b & a+a\end{array}\right]=\left[\begin{array}{cc}2 \mathrm{a} & 2 \mathrm{~b} \\ 0 & 2 \mathrm{a}\end{array}\right]$
:::

:::answer
**उत्तर:** $\left[\begin{array}{cc}2a & 2b \\ 0 & 2a\end{array}\right]$
:::

:::

:::part
:::prompt
$\left[\begin{array}{ll}a^{2}+b^{2} & b^{2}+c^{2} \\ a^{2}+c^{2} & a^{2}+b^{2}\end{array}\right]+\left[\begin{array}{cc}2 a b & 2 b c \\ -2 a c & -2 a b\end{array}\right]$
:::

:::solution
$\left[\begin{array}{ll}a^{2}+b^{2} & b^{2}+c^{2} \\ a^{2}+c^{2} & a^{2}+b^{2}\end{array}\right]+\left[\begin{array}{cc}2 a b & 2 b c \\ -2 a c & -2 a b\end{array}\right]=\left[\begin{array}{ll}a^{2}+b^{2}+2 a b & b^{2}+c^{2}+2 b c \\ a^{2}+c^{2}-2 a c & a^{2}+b^{2}-2 a b\end{array}\right]=\left[\begin{array}{ll}(a+b)^{2} & (b+c)^{2} \\ (a-c)^{2} & (a-b)^{2}\end{array}\right]$
:::

:::answer
**उत्तर:** $\left[\begin{array}{ll}(a+b)^{2} & (b+c)^{2} \\ (a-c)^{2} & (a-b)^{2}\end{array}\right]$
:::

:::

:::part
:::prompt
$\left[\begin{array}{rrr}-1 & 4 & -6 \\ 8 & 5 & 16 \\ 2 & 8 & 5\end{array}\right]+\left[\begin{array}{ccc}12 & 7 & 6 \\ 8 & 0 & 5 \\ 3 & 2 & 4\end{array}\right]$
:::

:::solution
$\left[\begin{array}{ccc}-1 & 4 & -6 \\ 8 & 5 & 16 \\ 2 & 8 & 5\end{array}\right]+\left[\begin{array}{ccc}12 & 7 & 6 \\ 8 & 0 & 5 \\ 3 & 2 & 4\end{array}\right]=\left[\begin{array}{ccc}-1+12 & 4+7 & -6+6 \\ 8+8 & 5+0 & 16+5 \\ 2+3 & 8+2 & 5+4\end{array}\right]=\left[\begin{array}{ccc}11 & 11 & 0 \\ 16 & 5 & 21 \\ 5 & 10 & 9\end{array}\right]$
:::

:::answer
**उत्तर:** $\left[\begin{array}{ccc}11 & 11 & 0 \\ 16 & 5 & 21 \\ 5 & 10 & 9\end{array}\right]$
:::

:::

:::part
:::prompt
$\left[\begin{array}{cc}\cos ^{2} x & \sin ^{2} x \\ \sin ^{2} x & \cos ^{2} x\end{array}\right]+\left[\begin{array}{cc}\sin ^{2} x & \cos ^{2} x \\ \cos ^{2} x & \sin ^{2} x\end{array}\right]$
:::

:::solution
$\left[\begin{array}{cc}\cos ^{2} x & \sin ^{2} x \\ \sin ^{2} x & \cos ^{2} x\end{array}\right]+\left[\begin{array}{cc}\sin ^{2} x & \cos ^{2} x \\ \cos ^{2} x & \sin ^{2} x\end{array}\right]=\left[\begin{array}{cc}\cos ^{2} x+\sin ^{2} x & \sin ^{2} x+\cos ^{2} x \\ \sin ^{2} x+\cos ^{2} x & \cos ^{2} x+\sin ^{2} x\end{array}\right]=\left[\begin{array}{ll}1 & 1 \\ 1 & 1\end{array}\right]$
:::

:::answer
**उत्तर:** $\left[\begin{array}{ll}1 & 1 \\ 1 & 1\end{array}\right]$
:::

:::

:::

:::question{number="3.2.3" kind="exercise" id="q_3.2.3" topic="Matrix multiplication"}
#### प्रश्न 3.2.3

:::prompt
निदर्शित गुणनफल परिकलित कीजिए:
:::

:::part
:::prompt
$\left[\begin{array}{rr}a & b \\ -b & a\end{array}\right]\left[\begin{array}{rr}a & -b \\ b & a\end{array}\right]$
:::

:::solution
$\left[\begin{array}{cc}a & b \\ -b & a\end{array}\right]\left[\begin{array}{cc}a & -b \\ b & a\end{array}\right]=\left[\begin{array}{cc}a \times a+b \times b & a \times(-b)+b \times a \\ -b \times a+a \times b & -b \times(-b)+a \times a\end{array}\right]=\left[\begin{array}{cc}a^{2}+b^{2} & 0 \\ 0 & b^{2}+a^{2}\end{array}\right]$
:::

:::answer
**उत्तर:** $\left[\begin{array}{cc}a^{2}+b^{2} & 0 \\ 0 & a^{2}+b^{2}\end{array}\right]$
:::

:::

:::part
:::prompt
$\left[\begin{array}{l}1 \\ 2 \\ 3\end{array}\right]\left[\begin{array}{lll}2 & 3 & 4\end{array}\right]$
:::

:::solution
$\left[\begin{array}{l}1 \\ 2 \\ 3\end{array}\right]\left[\begin{array}{lll}2 & 3 & 4\end{array}\right]=\left[\begin{array}{lll}1 \times 2 & 1 \times 3 & 1 \times 4 \\ 2 \times 2 & 2 \times 3 & 2 \times 4 \\ 3 \times 2 & 3 \times 3 & 3 \times 4\end{array}\right]=\left[\begin{array}{ccc}2 & 3 & 4 \\ 4 & 6 & 8 \\ 6 & 9 & 12\end{array}\right]$
:::

:::answer
**उत्तर:** $\left[\begin{array}{ccc}2 & 3 & 4 \\ 4 & 6 & 8 \\ 6 & 9 & 12\end{array}\right]$
:::

:::

:::part
:::prompt
$\left[\begin{array}{rr}1 & -2 \\ 2 & 3\end{array}\right]\left[\begin{array}{lll}1 & 2 & 3 \\ 2 & 3 & 1\end{array}\right]$
:::

:::solution
$$
\left[\begin{array}{cc}
1 & -2 \\
2 & 3
\end{array}\right]\left[\begin{array}{lll}
1 & 2 & 3 \\
2 & 3 & 1
\end{array}\right]=\left[\begin{array}{ccc}
1 \times 1+(-2) \times 2 & 1 \times 2+(-2) \times 3 & 1 \times 3+(-2) \times 1 \\
2 \times 1+3 \times 2 & 2 \times 2+3 \times 3 & 2 \times 3+3 \times 1
\end{array}\right]=\left[\begin{array}{ccc}
-3 & -4 & 1 \\
8 & 13 & 9
\end{array}\right]
$$
:::

:::answer
**उत्तर:** $\left[\begin{array}{ccc}-3 & -4 & 1 \\ 8 & 13 & 9\end{array}\right]$
:::

:::

:::part
:::prompt
$\left[\begin{array}{lll}2 & 3 & 4 \\ 3 & 4 & 5 \\ 4 & 5 & 6\end{array}\right]\left[\begin{array}{rrr}1 & -3 & 5 \\ 0 & 2 & 4 \\ 3 & 0 & 5\end{array}\right]$
:::

:::solution
$$
\left[\begin{array}{lll}
2 & 3 & 4 \\
3 & 4 & 5 \\
4 & 5 & 6
\end{array}\right]\left[\begin{array}{ccc}
1 & -3 & 5 \\
0 & 2 & 4 \\
3 & 0 & 5
\end{array}\right]
$$
$$
\begin{aligned}
& =\left[\begin{array}{lll}
2 \times 1+3 \times 0+4 \times 3 & 2 \times(-3)+3 \times 2+4 \times 0 & 2 \times 5+3 \times 4+4 \times 5 \\
3 \times 1+4 \times 0+5 \times 3 & 3 \times(-3)+4 \times 2+5 \times 0 & 3 \times 5+4 \times 4+5 \times 5 \\
4 \times 1+5 \times 0+6 \times 3 & 4 \times(-3)+5 \times 2+6 \times 0 & 4 \times 5+5 \times 4+6 \times 5
\end{array}\right] \\
& =\left[\begin{array}{ccc}
14 & 0 & 42 \\
18 & -1 & 56 \\
22 & -2 & 70
\end{array}\right]
\end{aligned}
$$
:::

:::answer
**उत्तर:** $\left[\begin{array}{ccc}14 & 0 & 42 \\ 18 & -1 & 56 \\ 22 & -2 & 70\end{array}\right]$
:::

:::

:::part
:::prompt
$\left[\begin{array}{rr}2 & 1 \\ 3 & 2 \\ -1 & 1\end{array}\right]\left[\begin{array}{rrr}1 & 0 & 1 \\ -1 & 2 & 1\end{array}\right]$
:::

:::solution
$$
\left[\begin{array}{cc}
2 & 1 \\
3 & 2 \\
-1 & 1
\end{array}\right]\left[\begin{array}{ccc}
1 & 0 & 1 \\
-1 & 2 & 1
\end{array}\right]
$$
$$
\begin{aligned}
& =\left[\begin{array}{ccc}
2 \times 1+1 \times(-1) & 2 \times 0+1 \times 2 & 2 \times 1+1 \times 1 \\
3 \times 1+2 \times(-1) & 3 \times 0+2 \times 2 & 3 \times 1+2 \times 1 \\
-1 \times 1+1 \times(-1) & -1 \times 0+1 \times 2 & -1 \times 1+1 \times 1
\end{array}\right] \\
& =\left[\begin{array}{ccc}
1 & 2 & 3 \\
1 & 4 & 5 \\
-2 & 2 & 0
\end{array}\right]
\end{aligned}
$$
:::

:::answer
**उत्तर:** $\left[\begin{array}{ccc}1 & 2 & 3 \\ 1 & 4 & 5 \\ -2 & 2 & 0\end{array}\right]$
:::

:::

:::part
:::prompt
$\left[\begin{array}{rrr}3 & -1 & 3 \\ -1 & 0 & 2\end{array}\right]\left[\begin{array}{rr}2 & -3 \\ 1 & 0 \\ 3 & 1\end{array}\right]$
:::

:::solution
$$
\left[\begin{array}{ccc}
3 & -1 & 3 \\
-1 & 0 & 2
\end{array}\right]\left[\begin{array}{cc}
2 & -3 \\
1 & 0 \\
3 & 1
\end{array}\right]=\left[\begin{array}{cc}
3 \times 2+(-1) \times 1+3 \times 3 & 3 \times(-3)+(-1) \times 0+3 \times 1 \\
-1 \times 2+0 \times 1+2 \times 3 & -1 \times(-3)+0 \times 0+2 \times 1
\end{array}\right]=\left[\begin{array}{cc}
14 & -6 \\
4 & 5
\end{array}\right]
$$
:::

:::answer
**उत्तर:** $\left[\begin{array}{cc}14 & -6 \\ 4 & 5\end{array}\right]$
:::

:::

:::

:::question{number="3.2.4" kind="exercise" id="q_3.2.4" topic="Matrix operations verification"}
#### प्रश्न 3.2.4

:::prompt
यदि $\mathrm{A}=\left[\begin{array}{rrr}1 & 2 & -3 \\ 5 & 0 & 2 \\ 1 & -1 & 1\end{array}\right], \mathrm{B}=\left[\begin{array}{rrr}3 & -1 & 2 \\ 4 & 2 & 5 \\ 2 & 0 & 3\end{array}\right]$ तथा $\mathrm{C}=\left[\begin{array}{rrr}4 & 1 & 2 \\ 0 & 3 & 2 \\ 1 & -2 & 3\end{array}\right]$, तो $(\mathrm{A}+\mathrm{B})$ तथा $(\mathrm{B}-\mathrm{C})$ परिकलित कीजिए। साथ ही सत्यापित कीजिए कि $\mathrm{A}+(\mathrm{B}-\mathrm{C})=(\mathrm{A}+\mathrm{B})-\mathrm{C}$.
:::

:::solution{label="हल"}
$$
\begin{aligned}
& A+B=\left[\begin{array}{ccc}
1 & 2 & -3 \\
5 & 0 & 2 \\
1 & -1 & 1
\end{array}\right]+\left[\begin{array}{ccc}
3 & -1 & 2 \\
4 & 2 & 5 \\
2 & 0 & 3
\end{array}\right] \\
& =\left[\begin{array}{ccc}
1+3 & 2-1 & -3+2 \\
5+4 & 0+2 & 2+5 \\
1+2 & -1+0 & 1+3
\end{array}\right]=\left[\begin{array}{ccc}
4 & 1 & -1 \\
9 & 2 & 7 \\
3 & -1 & 4
\end{array}\right] \\
& B-C=\left[\begin{array}{ccc}
3 & -1 & 2 \\
4 & 2 & 5 \\
2 & 0 & 3
\end{array}\right]-\left[\begin{array}{ccc}
4 & 1 & 2 \\
0 & 3 & 2 \\
1 & -2 & 3
\end{array}\right] \\
& =\left[\begin{array}{ccc}
3-4 & -1-1 & 2-2 \\
4-0 & 2-3 & 5-2 \\
2-1 & 0-(-2) & 3-3
\end{array}\right]=\left[\begin{array}{ccc}
-1 & -2 & 0 \\
4 & -1 & 3 \\
1 & 2 & 0
\end{array}\right] \\
& \text { LHS }=A+(B-C)=\left[\begin{array}{ccc}
1 & 2 & -3 \\
5 & 0 & 2 \\
1 & -1 & 1
\end{array}\right]+\left[\begin{array}{ccc}
-1 & -2 & 0 \\
4 & -1 & 3 \\
1 & 2 & 0
\end{array}\right]=\left[\begin{array}{ccc}
0 & 0 & -3 \\
9 & -1 & 5 \\
2 & 1 & 1
\end{array}\right] \\
& \text { RHS }=(A+B)-C=\left[\begin{array}{ccc}
4 & 1 & -1 \\
9 & 2 & 7 \\
3 & -1 & 4
\end{array}\right]-\left[\begin{array}{ccc}
4 & 1 & 2 \\
0 & 3 & 2 \\
1 & -2 & 3
\end{array}\right]=\left[\begin{array}{ccc}
0 & 0 & -3 \\
9 & -1 & 5 \\
2 & 1 & 1
\end{array}\right]
\end{aligned}
$$
इस प्रकार, $A+(B-C)=(A+B)-C=\left[\begin{array}{ccc}0 & 0 & -3 \\ 9 & -1 & 5 \\ 2 & 1 & 1\end{array}\right]$
:::

:::answer
**उत्तर:** $A+B=\left[\begin{array}{ccc}4 & 1 & -1 \\ 9 & 2 & 7 \\ 3 & -1 & 4\end{array}\right]$, $B-C=\left[\begin{array}{ccc}-1 & -2 & 0 \\ 4 & -1 & 3 \\ 1 & 2 & 0\end{array}\right]$, दोनों पक्ष $\left[\begin{array}{ccc}0 & 0 & -3 \\ 9 & -1 & 5 \\ 2 & 1 & 1\end{array}\right]$ के बराबर सत्यापित
:::

:::

:::question{number="3.2.5" kind="exercise" id="q_3.2.5" topic="Scalar multiplication of matrices"}
#### प्रश्न 3.2.5

:::prompt
यदि $\mathrm{A}=\left[\begin{array}{ccc}\frac{2}{3} & 1 & \frac{5}{3} \\ \frac{1}{3} & \frac{2}{3} & \frac{4}{3} \\ \frac{7}{3} & 2 & \frac{2}{3}\end{array}\right]$ तथा $\mathrm{B}=\left[\begin{array}{ccc}\frac{2}{5} & \frac{3}{5} & 1 \\ \frac{1}{5} & \frac{2}{5} & \frac{4}{5} \\ \frac{7}{5} & \frac{6}{5} & \frac{2}{5}\end{array}\right]$, तो $3 \mathrm{~A}-5 \mathrm{~B}$ परिकलित कीजिए।
:::

:::solution{label="हल"}
$$
\begin{aligned}
& 3 A-5 B=3\left[\begin{array}{ccc}
\frac{2}{3} & 1 & \frac{5}{3} \\
\frac{1}{3} & \frac{2}{3} & \frac{4}{3} \\
\frac{7}{3} & 2 & \frac{2}{3}
\end{array}\right]-5\left[\begin{array}{ccc}
\frac{2}{5} & \frac{3}{5} & 1 \\
\frac{1}{5} & \frac{2}{5} & \frac{4}{5} \\
\frac{7}{5} & \frac{6}{5} & \frac{2}{5}
\end{array}\right] \\
& =\left[\begin{array}{lll}
2 & 3 & 5 \\
1 & 2 & 4 \\
7 & 6 & 2
\end{array}\right]-\left[\begin{array}{ccc}
2 & 3 & 5 \\
1 & 2 & 4 \\
7 & 6 & 2
\end{array}\right] \\
& =\left[\begin{array}{lll}
2-2 & 3-3 & 5-5 \\
1-1 & 2-2 & 4-4 \\
7-7 & 6-6 & 2-2
\end{array}\right]=\left[\begin{array}{lll}
0 & 0 & 0 \\
0 & 0 & 0 \\
0 & 0 & 0
\end{array}\right]=0
\end{aligned}
$$
:::

:::answer
**उत्तर:** शून्य आव्यूह $\left[\begin{array}{lll}0 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0\end{array}\right]$
:::

:::

:::question{number="3.2.6" kind="exercise" id="q_3.2.6" topic="Simplify trigonometric matrix expression"}
#### प्रश्न 3.2.6

:::prompt
सरल कीजिए, $\cos \theta\left[\begin{array}{rr}\cos \theta & \sin \theta \\ -\sin \theta & \cos \theta\end{array}\right]+\sin \theta\left[\begin{array}{rr}\sin \theta & -\cos \theta \\ \cos \theta & \sin \theta\end{array}\right]$
:::

:::solution{label="हल"}
$$
\begin{aligned}
& \cos \theta\left[\begin{array}{cc}
\cos \theta & \sin \theta \\
-\sin \theta & \cos \theta
\end{array}\right]+\sin \theta\left[\begin{array}{cc}
\sin \theta & -\cos \theta \\
\cos \theta & \sin \theta
\end{array}\right] \\
& =\left[\begin{array}{cc}
\cos ^{2} \theta & \sin \theta \cos \theta \\
-\sin \theta \cos \theta & \cos ^{2} \theta
\end{array}\right]+\left[\begin{array}{cc}
\sin ^{2} \theta & -\sin \theta \cos \theta \\
\sin \theta \cos \theta & \sin ^{2} \theta
\end{array}\right] \\
& =\left[\begin{array}{cc}
\cos ^{2} \theta+\sin ^{2} \theta & \sin \theta \cos \theta-\sin \theta \cos \theta \\
-\sin \theta \cos \theta+\sin \theta \cos \theta & \cos ^{2} \theta+\sin ^{2} \theta
\end{array}\right]=\left[\begin{array}{ll}
1 & 0 \\
0 & 1
\end{array}\right]=I
\end{aligned}
$$
:::

:::answer
**उत्तर:** $I=\left[\begin{array}{ll}1 & 0 \\ 0 & 1\end{array}\right]$
:::

:::

:::question{number="3.2.7" kind="exercise" id="q_3.2.7" topic="Solve simultaneous matrix equations"}
#### प्रश्न 3.2.7

:::prompt
$X$ तथा $Y$ ज्ञात कीजिए यदि
:::

:::part
:::prompt
$\mathrm{X}+\mathrm{Y}=\left[\begin{array}{ll}7 & 0 \\ 2 & 5\end{array}\right]$ तथा $\mathrm{X}-\mathrm{Y}=\left[\begin{array}{ll}3 & 0 \\ 0 & 3\end{array}\right]$
:::

:::solution
समीकरण (1) और (2) को जोड़ने पर
$$
\begin{aligned}
& 2 X=\left[\begin{array}{ll}
7 & 0 \\
2 & 5
\end{array}\right]+\left[\begin{array}{ll}
3 & 0 \\
0 & 3
\end{array}\right]=\left[\begin{array}{cc}
10 & 0 \\
2 & 8
\end{array}\right] \\
& \Rightarrow X=\left[\begin{array}{ll}
5 & 0 \\
1 & 4
\end{array}\right]
\end{aligned}
$$
समीकरण (1) में X का मान रखने पर
$$
\begin{aligned}
& {\left[\begin{array}{ll}
5 & 0 \\
1 & 4
\end{array}\right]+Y=\left[\begin{array}{ll}
7 & 0 \\
2 & 5
\end{array}\right]} \\
& \Rightarrow Y=\left[\begin{array}{ll}
7 & 0 \\
2 & 5
\end{array}\right]-\left[\begin{array}{ll}
5 & 0 \\
1 & 4
\end{array}\right]=\left[\begin{array}{ll}
2 & 0 \\
1 & 1
\end{array}\right]
\end{aligned}
$$
:::

:::answer
**उत्तर:** $X=\left[\begin{array}{ll}5 & 0 \\ 1 & 4\end{array}\right]$, $Y=\left[\begin{array}{ll}2 & 0 \\ 1 & 1\end{array}\right]$
:::

:::

:::part
:::prompt
$2 \mathrm{X}+3 \mathrm{Y}=\left[\begin{array}{ll}2 & 3 \\ 4 & 0\end{array}\right]$ तथा $3 \mathrm{X}+2 \mathrm{Y}=\left[\begin{array}{rr}2 & -2 \\ -1 & 5\end{array}\right]$
:::

:::solution
समीकरण (1) को 3 से और (2) को 2 से गुणा करके घटाने पर
$$
\begin{aligned}
& 3(2 X+3 Y)-2(3 X+2 Y)=3\left[\begin{array}{ll}
2 & 3 \\
4 & 0
\end{array}\right]-2\left[\begin{array}{cc}
2 & -2 \\
-1 & 5
\end{array}\right] \\
& \Rightarrow 6 X+9 Y-6 X-4 Y=\left[\begin{array}{cc}
6 & 9 \\
12 & 0
\end{array}\right]-\left[\begin{array}{cc}
4 & -4 \\
-2 & 10
\end{array}\right] \\
& \Rightarrow 5 Y=\left[\begin{array}{cc}
2 & 13 \\
14 & -10
\end{array}\right] \Rightarrow Y=\left[\begin{array}{cc}
\frac{2}{5} & \frac{13}{5} \\
\frac{14}{5} & -2
\end{array}\right]
\end{aligned}
$$
समीकरण (1) में Y का मान रखने पर
$$
\begin{aligned}
& 2 X+\left[\begin{array}{cc}
\frac{2}{5} & \frac{13}{5} \\
\frac{14}{5} & -2
\end{array}\right]=\left[\begin{array}{ll}
2 & 3 \\
4 & 0
\end{array}\right] \\
& \Rightarrow 2 X=\left[\begin{array}{ll}
2 & 3 \\
4 & 0
\end{array}\right]-\left[\begin{array}{cc}
\frac{6}{5} & \frac{39}{5} \\
\frac{42}{5} & -6
\end{array}\right]=\left[\begin{array}{cc}
2-\frac{6}{5} & 3-\frac{39}{5} \\
4-\frac{42}{5} & 0-6
\end{array}\right]=\left[\begin{array}{cc}
\frac{4}{5} & -\frac{24}{5} \\
-\frac{22}{5} & 6
\end{array}\right] \\
& \Rightarrow X=\left[\begin{array}{cc}
\frac{2}{5} & -\frac{12}{5} \\
-\frac{11}{5} & 3
\end{array}\right]
\end{aligned}
$$
:::

:::answer
**उत्तर:** $X=\left[\begin{array}{cc}\frac{2}{5} & -\frac{12}{5} \\ -\frac{11}{5} & 3\end{array}\right]$, $Y=\left[\begin{array}{cc}\frac{2}{5} & \frac{13}{5} \\ \frac{14}{5} & -2\end{array}\right]$
:::

:::

:::

:::question{number="3.2.8" kind="exercise" id="q_3.2.8" topic="Solve for unknown matrix X"}
#### प्रश्न 3.2.8

:::prompt
$X$ तथा $Y$ ज्ञात कीजिए यदि $\mathrm{Y}=\left[\begin{array}{ll}3 & 2 \\ 1 & 4\end{array}\right]$ तथा $2 \mathrm{X}+\mathrm{Y}=\left[\begin{array}{rr}1 & 0 \\ -3 & 2\end{array}\right]$
:::

:::solution{label="हल"}
$$
\begin{aligned}
& 2 X+Y=\left[\begin{array}{cc}
1 & 0 \\
-3 & 2
\end{array}\right] \\
& \Rightarrow 2 X+\left[\begin{array}{ll}
3 & 2 \\
1 & 4
\end{array}\right]=\left[\begin{array}{cc}
1 & 0 \\
-3 & 2
\end{array}\right] \\
& \Rightarrow 2 X=\left[\begin{array}{cc}
1 & 0 \\
-3 & 2
\end{array}\right]-\left[\begin{array}{ll}
3 & 2 \\
1 & 4
\end{array}\right]=\left[\begin{array}{cc}
-2 & -2 \\
-4 & -2
\end{array}\right] \\
& \Rightarrow X=\left[\begin{array}{cc}
-1 & -1 \\
-2 & -1
\end{array}\right]
\end{aligned}
$$
:::

:::answer
**उत्तर:** $X=\left[\begin{array}{cc}-1 & -1 \\ -2 & -1\end{array}\right]$
:::

:::

:::question{number="3.2.9" kind="exercise" id="q_3.2.9" topic="Solve for unknowns using matrix equality"}
#### प्रश्न 3.2.9

:::prompt
$x$ तथा $y$ ज्ञात कीजिए यदि $2\left[\begin{array}{ll}1 & 3 \\ 0 & x\end{array}\right]+\left[\begin{array}{ll}y & 0 \\ 1 & 2\end{array}\right]=\left[\begin{array}{ll}5 & 6 \\ 1 & 8\end{array}\right]$
:::

:::solution{label="हल"}
$$
\begin{aligned}
& 2\left[\begin{array}{ll}
1 & 3 \\
0 & x
\end{array}\right]+\left[\begin{array}{ll}
y & 0 \\
1 & 2
\end{array}\right]=\left[\begin{array}{ll}
5 & 6 \\
1 & 8
\end{array}\right] \\
& \Rightarrow\left[\begin{array}{ll}
2 & 6 \\
0 & 2 x
\end{array}\right]+\left[\begin{array}{ll}
y & 0 \\
1 & 2
\end{array}\right]=\left[\begin{array}{ll}
5 & 6 \\
1 & 8
\end{array}\right] \\
& \Rightarrow\left[\begin{array}{ll}
2+y & 6+0 \\
0+1 & 2 x+2
\end{array}\right]=\left[\begin{array}{ll}
5 & 6 \\
1 & 8
\end{array}\right]
\end{aligned}
$$
यदि दो आव्यूह समान हैं तो उनके संगत अवयव भी समान होते हैं, इसलिए
$$
\begin{aligned}
& 2+y=5 \text { तथा } 2 x+2=8 \\
& \Rightarrow y=3 \text { तथा } x=3
\end{aligned}
$$
:::

:::answer
**उत्तर:** $x=3$, $y=3$
:::

:::

:::question{number="3.2.10" kind="exercise" id="q_3.2.10" topic="Solve matrix equation for x, y, z, t"}
#### प्रश्न 3.2.10

:::prompt
प्रदत्त समीकरण को $x, y, z$ तथा $t$ के लिए हल कीजिए यदि
$$
2\left[\begin{array}{ll}
x & z \\
y & t
\end{array}\right]+3\left[\begin{array}{rr}
1 & -1 \\
0 & 2
\end{array}\right]=3\left[\begin{array}{ll}
3 & 5 \\
4 & 6
\end{array}\right]
$$
:::

:::solution{label="हल"}
$$
\begin{aligned}
& 2\left[\begin{array}{ll}
x & z \\
y & t
\end{array}\right]+3\left[\begin{array}{cc}
1 & -1 \\
0 & 2
\end{array}\right]=3\left[\begin{array}{ll}
3 & 5 \\
4 & 6
\end{array}\right] \\
& \Rightarrow\left[\begin{array}{ll}
2 x & 2 z \\
2 y & 2 t
\end{array}\right]+\left[\begin{array}{cc}
3 & -3 \\
0 & 6
\end{array}\right]=\left[\begin{array}{cc}
9 & 15 \\
12 & 18
\end{array}\right] \\
& \Rightarrow\left[\begin{array}{ll}
2 x+3 & 2 z-3 \\
2 y+0 & 2 t+6
\end{array}\right]=\left[\begin{array}{cc}
9 & 15 \\
12 & 18
\end{array}\right]
\end{aligned}
$$
यदि दो आव्यूह समान हैं तो उनके संगत अवयव भी समान होते हैं, इसलिए $2 x+3=9,2 z-3=15,2 y=12$ तथा $2 t+6=18$
$\Rightarrow x=3, z=9, y=6$ तथा $t=6$
:::

:::answer
**उत्तर:** $x=3$, $y=6$, $z=9$, $t=6$
:::

:::

:::question{number="3.2.11" kind="exercise" id="q_3.2.11" topic="Solve for x and y using column matrices"}
#### प्रश्न 3.2.11

:::prompt
यदि $x\left[\begin{array}{l}2 \\ 3\end{array}\right]+y\left[\begin{array}{r}-1 \\ 1\end{array}\right]=\left[\begin{array}{l}10 \\ 5\end{array}\right]$ है, तो $x$ तथा $y$ के मान ज्ञात कीजिए।
:::

:::solution{label="हल"}
$$
\begin{aligned}
& x\left[\begin{array}{l}
2 \\
3
\end{array}\right]+y\left[\begin{array}{c}
-1 \\
1
\end{array}\right]=\left[\begin{array}{c}
10 \\
5
\end{array}\right] \\
& \Rightarrow\left[\begin{array}{l}
2 x \\
3 x
\end{array}\right]+\left[\begin{array}{c}
-\mathrm{y} \\
y
\end{array}\right]=\left[\begin{array}{c}
10 \\
5
\end{array}\right] \\
& \Rightarrow\left[\begin{array}{l}
2 x-y \\
3 x+y
\end{array}\right]=\left[\begin{array}{c}
10 \\
5
\end{array}\right]
\end{aligned}
$$
यदि दो आव्यूह समान हैं तो उनके संगत अवयव भी समान होते हैं, इसलिए
$2 x-y=10$ तथा $3 x+y=5$
दोनों समीकरणों को जोड़ने पर
$$
\begin{aligned}
& 5 x=15 \\
& \Rightarrow x=3
\end{aligned}
$$
$x$ का मान $3 x+y=5$ में रखने पर
$$
3(3)+y=5 \quad \Rightarrow y=-4
$$
:::

:::answer
**उत्तर:** $x=3$, $y=-4$
:::

:::

:::question{number="3.2.12" kind="exercise" id="q_3.2.12" topic="Matrix equality — solve for x, y, z, w"}
#### प्रश्न 3.2.12

:::prompt
यदि $3\left[\begin{array}{cc}x & y \\ z & w\end{array}\right]=\left[\begin{array}{cc}x & 6 \\ -1 & 2 w\end{array}\right]+\left[\begin{array}{cc}4 & x+y \\ z+w & 3\end{array}\right]$ है तो $x, y, z$ तथा $w$ के मानों को ज्ञात कीजिए।
:::

:::solution{label="हल"}
$$
\begin{aligned}
& 3\left[\begin{array}{cc}
x & y \\
z & w
\end{array}\right]=\left[\begin{array}{cc}
x & 6 \\
-1 & 2 w
\end{array}\right]+\left[\begin{array}{cc}
4 & x+y \\
z+w & 3
\end{array}\right] \\
& \Rightarrow\left[\begin{array}{cc}
3 x & 3 \mathrm{y} \\
3 \mathrm{z} & 3 w
\end{array}\right]=\left[\begin{array}{cc}
x+4 & 6+x+y \\
-1+z+w & 2 w+3
\end{array}\right]
\end{aligned}
$$
यदि दो आव्यूह समान हैं तो उनके संगत अवयव भी समान होते हैं, इसलिए
$3 x=x+4,3 y=6+x+y, 3 z=-1+z+w$ तथा $3 w=2 w+3$
$\Rightarrow x=2, \quad y=4, \quad z=1 \quad$ तथा $\quad w=3$
:::

:::answer
**उत्तर:** $x=2,\ y=4,\ z=1,\ w=3$
:::

:::

:::question{number="3.2.13" kind="exercise" id="q_3.2.13" topic="Proving F(x)F(y) = F(x+y)"}
#### प्रश्न 3.2.13

:::prompt
यदि $\mathrm{F}(x)=\left[\begin{array}{ccc}\cos x & -\sin x & 0 \\ \sin x & \cos x & 0 \\ 0 & 0 & 1\end{array}\right]$ है तो सिद्ध कीजिए कि $\mathrm{F}(x) \mathrm{F}(y)=\mathrm{F}(x+y)$
:::

:::solution{label="हल"}
LHS $=F(x) F(y)$

$$
\begin{aligned}
& =\left[\begin{array}{ccc}
\cos x & -\sin x & 0 \\
\sin x & \cos x & 0 \\
0 & 0 & 1
\end{array}\right]\left[\begin{array}{ccc}
\cos y & -\sin y & 0 \\
\sin y & \cos y & 0 \\
0 & 0 & 1
\end{array}\right] \\
& =\left[\begin{array}{ccc}
\cos x \cos y-\sin x \sin y+0 & -\cos x \sin y-\sin x \cos y+0 & 0+0+0 \\
\sin x \cos y+\cos x \sin y+0 & -\sin x \sin y+\cos x \cos y+0 & 0+0+0 \\
0+0+0 & 0+0+0+ & 0+0+1
\end{array}\right] \\
& =\left[\begin{array}{ccc}
\cos (x+y) & -\sin (x+y) & 0 \\
\sin (x+y) & \cos (x+y) & 0 \\
0 & 0 & 1
\end{array}\right]=F(x+y)=\text { RHS }
\end{aligned}
$$
:::

:::

:::question{number="3.2.14" kind="exercise" id="q_3.2.14" topic="Showing AB ≠ BA (non-commutativity)"}
#### प्रश्न 3.2.14

:::prompt
दर्शाइए कि
:::

:::part
:::prompt
$\left[\begin{array}{cc}5 & -1 \\ 6 & 7\end{array}\right]\left[\begin{array}{ll}2 & 1 \\ 3 & 4\end{array}\right] \neq\left[\begin{array}{ll}2 & 1 \\ 3 & 4\end{array}\right]\left[\begin{array}{cc}5 & -1 \\ 6 & 7\end{array}\right]$
:::

:::solution
LHS $=\left[\begin{array}{cc}5 & -1 \\ 6 & 7\end{array}\right]\left[\begin{array}{ll}2 & 1 \\ 3 & 4\end{array}\right]$
$$
=\left[\begin{array}{cc}
5 \times 2+(-1) \times 3 & 5 \times 1+(-1) \times 4 \\
6 \times 2+7 \times 3 & 6 \times 1+7 \times 4
\end{array}\right]=\left[\begin{array}{cc}
7 & 1 \\
33 & 34
\end{array}\right]
$$
$$
\begin{aligned}
& \text { RHS }=\left[\begin{array}{ll}
2 & 1 \\
3 & 4
\end{array}\right]\left[\begin{array}{cc}
5 & -1 \\
6 & 7
\end{array}\right] \\
& =\left[\begin{array}{ll}
2 \times 5+1 \times 6 & 2 \times(-1)+1 \times 7 \\
3 \times 5+4 \times 6 & 3 \times(-1)+4 \times 7
\end{array}\right]=\left[\begin{array}{cc}
16 & 5 \\
39 & 25
\end{array}\right]
\end{aligned}
$$
इसलिए, $\quad\left[\begin{array}{cc}5 & -1 \\ 6 & 7\end{array}\right]\left[\begin{array}{ll}2 & 1 \\ 3 & 4\end{array}\right] \neq\left[\begin{array}{ll}2 & 1 \\ 3 & 4\end{array}\right]\left[\begin{array}{cc}5 & -1 \\ 6 & 7\end{array}\right]$
:::

:::

:::part
:::prompt
$\left[\begin{array}{lll}1 & 2 & 3 \\ 0 & 1 & 0 \\ 1 & 1 & 0\end{array}\right]\left[\begin{array}{ccc}-1 & 1 & 0 \\ 0 & -1 & 1 \\ 2 & 3 & 4\end{array}\right] \neq\left[\begin{array}{ccc}-1 & 1 & 0 \\ 0 & -1 & 1 \\ 2 & 3 & 4\end{array}\right]\left[\begin{array}{lll}1 & 2 & 3 \\ 0 & 1 & 0 \\ 1 & 1 & 0\end{array}\right]$
:::

:::solution
$L H S=\left[\begin{array}{lll}1 & 2 & 3 \\ 0 & 1 & 0 \\ 1 & 1 & 0\end{array}\right]\left[\begin{array}{ccc}-1 & 1 & 0 \\ 0 & -1 & 1 \\ 2 & 3 & 4\end{array}\right]$
$$
\begin{aligned}
& =\left[\begin{array}{ccc}
1 \times(-1)+2 \times 0+3 \times 2 & 1 \times 1+2 \times(-1)+3 \times 3 & 1 \times 0+2 \times 1+3 \times 4 \\
0 \times(-1)+1 \times 0+0 \times 2 & 0 \times 1+1 \times(-1)+0 \times 3 & 0 \times 0+1 \times 1+0 \times 4 \\
1 \times(-1)+1 \times 0+0 \times 2 & 1 \times 1+1 \times(-1)+0 \times 3 & 1 \times 0+1 \times 1+0 \times 4
\end{array}\right] \\
& =\left[\begin{array}{ccc}
5 & 8 & 14 \\
0 & -1 & 1 \\
-1 & 0 & 1
\end{array}\right]
\end{aligned}
$$
$$
\begin{aligned}
& \text { RHS }=\left[\begin{array}{ccc}
-1 & 1 & 0 \\
0 & -1 & 1 \\
2 & 3 & 4
\end{array}\right]\left[\begin{array}{lll}
1 & 2 & 3 \\
0 & 1 & 0 \\
1 & 1 & 0
\end{array}\right] \\
& =\left[\begin{array}{ccc}
-1 \times 1+1 \times 0+0 \times 1 & -1 \times 2+1 \times 1+0 \times 1 & -1 \times 3+1 \times 0+0 \times 0 \\
0 \times 1+(-1) \times 0+1 \times 1 & 0 \times 2+(-1) \times 1+1 \times 1 & 0 \times 3+(-1) \times 0+1 \times 0 \\
2 \times 1+3 \times 0+4 \times 1 & 2 \times 2+3 \times 1+4 \times 1 & 2 \times 3+3 \times 0+4 \times 0
\end{array}\right]
\end{aligned}
$$
$$
=\left[\begin{array}{ccc}
-1 & -1 & -3 \\
1 & 0 & 0 \\
6 & 11 & 6
\end{array}\right]
$$
इसलिए, $\left[\begin{array}{lll}1 & 2 & 3 \\ 0 & 1 & 0 \\ 1 & 1 & 0\end{array}\right]\left[\begin{array}{ccc}-1 & 1 & 0 \\ 0 & -1 & 1 \\ 2 & 3 & 4\end{array}\right] \neq\left[\begin{array}{ccc}-1 & 1 & 0 \\ 0 & -1 & 1 \\ 2 & 3 & 4\end{array}\right]\left[\begin{array}{lll}1 & 2 & 3 \\ 0 & 1 & 0 \\ 1 & 1 & 0\end{array}\right]$
:::

:::

:::

:::question{number="3.2.15" kind="exercise" id="q_3.2.15" topic="Evaluating A² − 5A + 6I"}
#### प्रश्न 3.2.15

:::prompt
यदि $\mathrm{A}=\left[\begin{array}{rrr}2 & 0 & 1 \\ 2 & 1 & 3 \\ 1 & -1 & 0\end{array}\right]$ है तो $\mathrm{A}^{2}-5 \mathrm{~A}+6 \mathrm{I}$, का मान ज्ञात कीजिए।
:::

:::solution{label="हल"}
$$
\begin{aligned}
& A=\left[\begin{array}{ccc}
2 & 0 & 1 \\
2 & 1 & 3 \\
1 & -1 & 0
\end{array}\right] \\
& \Rightarrow A^{2}=\left[\begin{array}{ccc}
2 & 0 & 1 \\
2 & 1 & 3 \\
1 & -1 & 0
\end{array}\right]\left[\begin{array}{ccc}
2 & 0 & 1 \\
2 & 1 & 3 \\
1 & -1 & 0
\end{array}\right] \\
& =\left[\begin{array}{ccc}
2 \times 2+0 \times 2+1 \times 1 & 2 \times 0+0 \times 1+1 \times(-1) & 2 \times 1+0 \times 3+1 \times 0 \\
2 \times 2+1 \times 2+3 \times 1 & 2 \times 0+1 \times 1+3 \times(-1) & 2 \times 1+1 \times 3+3 \times 0 \\
1 \times 2+(-1) \times 2+0 \times 1 & 1 \times 0+(-1) \times 1+0 \times(-1) & 1 \times 1+(-1) \times 3+0 \times 0
\end{array}\right] \\
& =\left[\begin{array}{ccc}
5 & -1 & 2 \\
9 & -2 & 5 \\
0 & -1 & -2
\end{array}\right]
\end{aligned}
$$

इसलिए, $A^{2}-5 A+6 I$

$$
\begin{aligned}
& =\left[\begin{array}{ccc}
5 & -1 & 2 \\
9 & -2 & 5 \\
0 & -1 & -2
\end{array}\right]-5\left[\begin{array}{ccc}
2 & 0 & 1 \\
2 & 1 & 3 \\
1 & -1 & 0
\end{array}\right]+6\left[\begin{array}{lll}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{array}\right] \\
& =\left[\begin{array}{ccc}
5 & -1 & 2 \\
9 & -2 & 5 \\
0 & -1 & -2
\end{array}\right]-\left[\begin{array}{ccc}
10 & 0 & 5 \\
10 & 5 & 15 \\
5 & -5 & 0
\end{array}\right]+\left[\begin{array}{ccc}
6 & 0 & 0 \\
0 & 6 & 0 \\
0 & 0 & 6
\end{array}\right] \\
& =\left[\begin{array}{ccc}
5-10+6 & -1-0+0 & 2-5+0 \\
9-10+0 & -2-5+6 & 5-15+0 \\
0-5+0 & -1+5+0 & -2-0+6
\end{array}\right] \\
& =\left[\begin{array}{ccc}
1 & -1 & -3 \\
-1 & -1 & -10 \\
-5 & 4 & 4
\end{array}\right]
\end{aligned}
$$
:::

:::answer
**उत्तर:** $A^{2}-5A+6I=\left[\begin{array}{ccc}1 & -1 & -3 \\ -1 & -1 & -10 \\ -5 & 4 & 4\end{array}\right]$
:::

:::

:::question{number="3.2.16" kind="exercise" id="q_3.2.16" topic="Proving A³ − 6A² + 7A + 2I = 0"}
#### प्रश्न 3.2.16

:::prompt
यदि $\mathrm{A}=\left[\begin{array}{lll}1 & 0 & 2 \\ 0 & 2 & 1 \\ 2 & 0 & 3\end{array}\right]$ है तो सिद्ध कीजिए कि $\mathrm{A}^{3}-6 \mathrm{~A}^{2}+7 \mathrm{~A}+2 \mathrm{I}=0$
:::

:::solution{label="हल"}
$$
A=\left[\begin{array}{lll}
1 & 0 & 2 \\
0 & 2 & 1 \\
2 & 0 & 3
\end{array}\right]
$$

$$
\begin{aligned}
& \Rightarrow A^{2}=\left[\begin{array}{lll}
1 & 0 & 2 \\
0 & 2 & 1 \\
2 & 0 & 3
\end{array}\right]\left[\begin{array}{lll}
1 & 0 & 2 \\
0 & 2 & 1 \\
2 & 0 & 3
\end{array}\right] \\
& =\left[\begin{array}{lll}
1 \times 1+0 \times 0+2 \times 2 & 1 \times 0+0 \times 2+2 \times 0 & 1 \times 2+0 \times 1+2 \times 3 \\
0 \times 1+2 \times 0+1 \times 2 & 0 \times 0+2 \times 2+1 \times 0 & 0 \times 2+2 \times 1+1 \times 3 \\
2 \times 1+0 \times 0+3 \times 2 & 2 \times 0+0 \times 2+3 \times 0 & 2 \times 2+0 \times 1+3 \times 3
\end{array}\right] \\
& =\left[\begin{array}{ccc}
5 & 0 & 8 \\
2 & 4 & 5 \\
8 & 0 & 13
\end{array}\right] \\
& A^{3}=A^{2} A=\left[\begin{array}{lll}
5 & 0 & 8 \\
2 & 4 & 5 \\
8 & 0 & 13
\end{array}\right]\left[\begin{array}{ccc}
1 & 0 & 2 \\
0 & 2 & 1 \\
2 & 0 & 3
\end{array}\right] \\
& =\left[\begin{array}{ccc}
5 \times 1+0 \times 0+8 \times 2 & 5 \times 0+0 \times 2+8 \times 0 & 5 \times 2+0 \times 1+8 \times 3 \\
2 \times 1+4 \times 0+5 \times 2 & 2 \times 0+4 \times 2+5 \times 0 & 2 \times 2+4 \times 1+5 \times 3 \\
8 \times 1+0 \times 0+13 \times 2 & 8 \times 0+0 \times 2+13 \times 0 & 8 \times 2+0 \times 1+13 \times 3
\end{array}\right] \\
& =\left[\begin{array}{ccc}
21 & 0 & 34 \\
12 & 8 & 23 \\
34 & 0 & 55
\end{array}\right]
\end{aligned}
$$

इसलिए, LHS $=A^{3}-6 A^{2}+7 A+2 I$

$$
\begin{aligned}
& =\left[\begin{array}{lll}
21 & 0 & 34 \\
12 & 8 & 23 \\
34 & 0 & 55
\end{array}\right]-6\left[\begin{array}{lll}
5 & 0 & 8 \\
2 & 4 & 5 \\
8 & 0 & 13
\end{array}\right]+7\left[\begin{array}{lll}
1 & 0 & 2 \\
0 & 2 & 1 \\
2 & 0 & 3
\end{array}\right]+2\left[\begin{array}{lll}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{array}\right] \\
& =\left[\begin{array}{lll}
21 & 0 & 34 \\
12 & 8 & 23 \\
34 & 0 & 55
\end{array}\right]-\left[\begin{array}{ccc}
30 & 0 & 48 \\
12 & 24 & 30 \\
48 & 0 & 78
\end{array}\right]+\left[\begin{array}{ccc}
7 & 0 & 14 \\
0 & 14 & 7 \\
14 & 0 & 21
\end{array}\right]+\left[\begin{array}{lll}
2 & 0 & 0 \\
0 & 2 & 0 \\
0 & 0 & 2
\end{array}\right] \\
& =\left[\begin{array}{ccc}
21-30+7+2 & 0-0+0+0 & 34-48+14+0 \\
12-12+0+0 & 8-24+14+2 & 23-30+7+0 \\
34-48+14+0 & 0-0+0+0 & 55-78+21+2
\end{array}\right] \\
& =\left[\begin{array}{lll}
0 & 0 & 0 \\
0 & 0 & 0 \\
0 & 0 & 0
\end{array}\right]=0=R H S
\end{aligned}
$$
:::

:::

:::question{number="3.2.17" kind="exercise" id="q_3.2.17" topic="Finding k in A² = kA − 2I"}
#### प्रश्न 3.2.17

:::prompt
यदि $\mathrm{A}=\left[\begin{array}{ll}3 & -2 \\ 4 & -2\end{array}\right]$ तथा $\mathrm{I}=\left[\begin{array}{ll}1 & 0 \\ 0 & 1\end{array}\right]$ एवं $\mathrm{A}^{2}=k \mathrm{~A}-2 \mathrm{I}$ हो तो $k$ ज्ञात कीजिए।
:::

:::solution{label="हल"}
दिया है: $A^{2}=k A-2 I$

$$
\begin{aligned}
& \Rightarrow\left[\begin{array}{ll}
3 & -2 \\
4 & -2
\end{array}\right]\left[\begin{array}{ll}
3 & -2 \\
4 & -2
\end{array}\right]=k\left[\begin{array}{ll}
3 & -2 \\
4 & -2
\end{array}\right]-2\left[\begin{array}{ll}
1 & 0 \\
0 & 1
\end{array}\right] \\
& \Rightarrow\left[\begin{array}{ll}
3 \times 3+(-2) \times 4 & 3 \times(-2)+(-2) \times(-2) \\
4 \times 3+(-2) \times 4 & 4 \times(-2)+(-2) \times(-2)
\end{array}\right]=\left[\begin{array}{ll}
3 k & -2 k \\
4 k & -2 k
\end{array}\right]-\left[\begin{array}{ll}
2 & 0 \\
0 & 2
\end{array}\right] \\
& \Rightarrow\left[\begin{array}{ll}
1 & -2 \\
4 & -4
\end{array}\right]=\left[\begin{array}{ll}
3 k-2 & -2 k \\
4 k & -2 k-2
\end{array}\right] \\
& \Rightarrow 4 k=4 \quad \Rightarrow k=1
\end{aligned}
$$
:::

:::answer
**उत्तर:** $k=1$
:::

:::

:::question{number="3.2.18" kind="exercise" id="q_3.2.18" topic="Proving I+A = (I−A) rotation-matrix identity"}
#### प्रश्न 3.2.18

:::prompt
यदि $\mathrm{A}=\left[\begin{array}{cc}0 & -\tan \frac{\alpha}{2} \\ \tan \frac{\alpha}{2} & 0\end{array}\right]$ तथा I कोटि $2$ का एक तत्समक आव्यूह है। तो सिद्ध कीजिए कि $\mathrm{I}+\mathrm{A}=(\mathrm{I}-\mathrm{A})\left[\begin{array}{rr}\cos \alpha & -\sin \alpha \\ \sin \alpha & \cos \alpha\end{array}\right]$
:::

:::solution{label="हल"}
$$
\begin{aligned}
& \text { LHS }=I+A \\
& =\left[\begin{array}{ll}
1 & 0 \\
0 & 1
\end{array}\right]+\left[\begin{array}{cc}
0 & -\tan \frac{\alpha}{2} \\
\tan \frac{\alpha}{2} & 0
\end{array}\right]=\left[\begin{array}{cc}
1 & -\tan \frac{\alpha}{2} \\
\tan \frac{\alpha}{2} & 1
\end{array}\right]
\end{aligned}
$$

अब RHS $=(I-A)\left[\begin{array}{cc}\cos \alpha & -\sin \alpha \\ \sin \alpha & \cos \alpha\end{array}\right]$

$$
=\left(\left[\begin{array}{ll}
1 & 0 \\
0 & 1
\end{array}\right]-\left[\begin{array}{cc}
0 & -\tan \frac{\alpha}{2} \\
\tan \frac{\alpha}{2} & 0
\end{array}\right]\right)\left[\begin{array}{cc}
\cos \alpha & -\sin \alpha \\
\sin \alpha & \cos \alpha
\end{array}\right]=\left[\begin{array}{cc}
1 & \tan \frac{\alpha}{2} \\
-\tan \frac{\alpha}{2} & 1
\end{array}\right]\left[\begin{array}{cc}
\cos \alpha & -\sin \alpha \\
\sin \alpha & \cos \alpha
\end{array}\right]
$$

$$
\begin{aligned}
& =\left[\begin{array}{ll}
\cos \alpha+\tan \frac{\alpha}{2} \sin \alpha & -\sin \alpha+\tan \frac{\alpha}{2} \cos \alpha \\
-\tan \frac{\alpha}{2} \cos \alpha+\sin \alpha & \tan \frac{\alpha}{2} \sin \alpha+\cos \alpha
\end{array}\right] \\
& =\left[\begin{array}{ll}
\cos \alpha+\frac{\sin \frac{\alpha}{2}}{\cos \frac{\alpha}{2}} \sin \alpha & -\sin \alpha+\frac{\sin \frac{\alpha}{2}}{\cos \frac{\alpha}{2}} \cos \alpha \\
-\frac{\sin \frac{\alpha}{2}}{\cos \frac{\alpha}{2}} \cos \alpha+\sin \alpha & \frac{\sin \frac{\alpha}{2}}{\cos \frac{\alpha}{2}} \sin \alpha+\cos \alpha
\end{array}\right] \\
& =\left[\begin{array}{ll}
\frac{\cos \alpha \cos \frac{\alpha}{2}+\sin \frac{\alpha}{2} \sin \alpha}{\cos \frac{\alpha}{2}} & \frac{-\sin \alpha \cos \frac{\alpha}{2}+\sin \frac{\alpha}{2} \cos \alpha}{\cos \frac{\alpha}{2}} \\
\frac{-\cos \alpha \sin \frac{\alpha}{2}+\cos \frac{\alpha}{2} \sin \alpha}{\cos \frac{\alpha}{2}} & \frac{\sin \alpha \sin \frac{\alpha}{2}+\cos \frac{\alpha}{2} \cos \alpha}{\cos \frac{\alpha}{2}}
\end{array}\right] \\
& =\left[\begin{array}{cc}
\frac{\cos \left(\alpha-\frac{\alpha}{2}\right)}{\cos \frac{\alpha}{2}} & \frac{-\sin \left(\alpha-\frac{\alpha}{2}\right)}{\cos \frac{\alpha}{2}} \\
\frac{\sin \left(\alpha-\frac{\alpha}{2}\right)}{\cos \frac{\alpha}{2}} & \frac{\cos \left(\alpha-\frac{\alpha}{2}\right)}{\cos \frac{\alpha}{2}}
\end{array}\right]=\left[\begin{array}{cc}
1 & -\tan \frac{\alpha}{2} \\
\tan \frac{\alpha}{2} & 1
\end{array}\right]=L H S
\end{aligned}
$$
:::

:::

:::question{number="3.2.19" kind="exercise" id="q_3.2.19" topic="Bond investment via matrix multiplication"}
#### प्रश्न 3.2.19

:::prompt
किसी व्यापार संघ के पास $30,000$ रुपयों का कोष है जिसे दो भिन्न-भिन्न प्रकार के बांडों में निवेशित करना है। प्रथम बांड पर $5 \%$ वार्षिक तथा द्वितीय बांड पर $7 \%$ वार्षिक ब्याज प्राप्त होता है। आव्यूह गुणन के प्रयोग द्वारा यह निर्धारित कीजिए कि $30,000$ रुपयों के कोष को दो प्रकार के बांडों में निवेश करने के लिए किस प्रकार बाँटं जिससे व्यापार संघ को प्राप्त कुल वार्षिक ब्याज
:::

:::part
:::prompt
Rs $1800$ हो।
:::

:::solution
माना प्रथम बांड पर निवेश की गई राशि $=₹ x$
इसलिए, द्वितीय बांड पर निवेश की गई राशि $=₹(30000-x)$
यदि कुल वार्षिक ब्याज ₹ $1800$ हो।
बांडों में निवेश (रुपयों में) वार्षिक ब्याज दर वार्षिक ब्याज (रुपयों में)

$$
\left[\begin{array}{ll}
x & 30000-x
\end{array}\right] \quad\left[\begin{array}{l}
5 \% \\
7 \%
\end{array}\right] \quad[1800]
$$

हल करने पर $x \times 5 \%+(30000-x) \times 7 \%=1800$

$$
\begin{aligned}
& \Rightarrow \frac{5 x}{100}+\frac{7}{100}(30000-x)=1800 \\
& \Rightarrow 5 x+210000-7 x=180000 \\
& \Rightarrow-2 x=-30000 \\
& \Rightarrow x=15000
\end{aligned}
$$

इसलिए, प्रथम बांड पर निवेश की गई राशि = ₹15000
तथा द्वितीय बांड पर निवेश की गई राशि = ₹15000
:::

:::answer
**उत्तर:** प्रथम बांड में ₹15000 तथा द्वितीय बांड में ₹15000
:::

:::

:::part
:::prompt
Rs $2000$ हो।
:::

:::solution
यदि कुल वार्षिक ब्याज ₹ $2000$ हो।
बांडों में निवेश (रुपयों में) वार्षिक ब्याज दर वार्षिक ब्याज (रुपयों में)

$$
\left[\begin{array}{ll}
x & 30000-x
\end{array}\right] \quad\left[\begin{array}{l}
5 \% \\
7 \%
\end{array}\right] \quad[2000]
$$

हल करने पर $x \times 5 \%+(30000-x) \times 7 \%=2000$

$$
\begin{aligned}
& \Rightarrow \frac{5 x}{100}+\frac{7}{100}(30000-x)=2000 \\
& \Rightarrow 5 x+210000-7 x=200000 \\
& \Rightarrow-2 x=-10000 \\
& \Rightarrow x=5000
\end{aligned}
$$

इसलिए, प्रथम बांड पर निवेश की गई राशि = ₹5000
तथा द्वितीय बांड पर निवेश की गई राशि = ₹25000
:::

:::answer
**उत्तर:** प्रथम बांड में ₹5000 तथा द्वितीय बांड में ₹25000
:::

:::

:::

:::question{number="3.2.20" kind="exercise" id="q_3.2.20" topic="Bookshop revenue via matrix algebra"}
#### प्रश्न 3.2.20

:::prompt
किसी स्कूल की पुस्तकों की दुकान में $10$ दर्जन रसायन विज्ञान, $8$ दर्जन भौतिक विज्ञान तथा $10$ दर्जन अर्थशास्त्र की पुस्तकें हैं। इन पुस्तकों का विक्रय मूल्य क्रमशः Rs $80$, Rs $60$ तथा Rs $40$ प्रति पुस्तक है। आव्यूह बीजगणित के प्रयोग द्वारा ज्ञात कीजिए कि सभी पुस्तकों को बेचने से दुकान को कुल कितनी धनराशि प्राप्त होगी।
:::

:::solution{label="हल"}
पुस्तकों की संख्या विक्रय मूल्य प्रति पुस्तक कुल धनराशि (रुपयों में)
रसायन भौतिक अर्थशास्त्र
$\left[\begin{array}{lll}120 & 96 & 120\end{array}\right]$ $\left[\begin{array}{l}80 \\ 60 \\ 40\end{array}\right]$ $[x]$
हल करने पर
$120 \times 80+96 \times 60+120 \times 40=x$
$\Rightarrow x=9600+5760+4800$
$\Rightarrow x=20160$
अतः, सभी पुस्तकों को बेचने से दुकान को कुल धनराशि ₹20160 प्राप्त होगी।
:::

:::answer
**उत्तर:** कुल धनराशि ₹20160
:::

:::

:::question{number="3.2.21" kind="exercise" id="q_3.2.21" topic="MCQ — condition for PY+WY defined"}
#### प्रश्न 3.2.21

:::prompt
मान लीजिए कि X, Y, Z, W तथा P क्रमशः $2 \times n, 3 \times k, 2 \times p, n \times 3$ तथा $p \times k$, कोटियों के आव्यूह हैं।

PY + WY के परिभाषित होने के लिए $n, k$ तथा $p$ पर क्या प्रतिबंध होगा ?
(A) $k=3, p=n$
(B) $k$ स्वेच्छ है , $p=2$
(C) $p$ स्वेच्छ है, $k=3$
(D) $k=2, p=3$
:::

:::solution{label="हल"}
P की कोटि $=p \times k$ तथा Y की कोटि $=3 \times k$ है।
इसलिए, PY के परिभाषित होने के लिए, $k=3$ होना चाहिए। इस प्रकार PY की कोटि $p \times k$ है।
W की कोटि $=n \times 3$ तथा Y की कोटि $=3 \times k$ है।
कोटि के अनुसार, WY परिभाषित है तथा इसकी कोटि $n \times k$ है।
$\mathrm{PY}+\mathrm{WY}$ के परिभाषित होने के लिए, PY तथा WY की कोटि बराबर होनी चाहिए।
$\Rightarrow p \times k=n \times k \quad \Rightarrow p=n$
अतः, विकल्प $(\mathrm{A})$ सही है।
:::

:::answer
**उत्तर:** (A) $k=3, p=n$
:::

:::

:::question{number="3.2.22" kind="exercise" id="q_3.2.22" topic="MCQ — order of the matrix 7X−5Z"}
#### प्रश्न 3.2.22

:::prompt
मान लीजिए कि X, Y, Z, W तथा P क्रमशः $2 \times n, 3 \times k, 2 \times p, n \times 3$ तथा $p \times k$, कोटियों के आव्यूह हैं।

यदि $n=p$, तो आव्यूह $7 \mathrm{X}-5 \mathrm{Z}$ की कोटि है।
(A) $p \times 2$
(B) $2 \times n$
(C) $n \times 3$
(D) $p \times n$
:::

:::solution{label="हल"}
आव्यूहों को जोड़ने या घटाने पर उनकी कोटि समान रहती है।
इसलिए, $7 X-5 Z$ की कोटि $=X$ की कोटि $=Z$ की कोटि $=2 \times n$
अतः, विकल्प (B) सही है।
:::

:::answer
**उत्तर:** (B) $2 \times n$
:::

:::

:::question{number="3.3.1" kind="exercise" id="q_3.3.1" topic="Matrix transpose"}
#### प्रश्न 3.3.1

:::prompt
निम्नलिखित आव्यूहों में से प्रत्येक का परिवर्त ज्ञात कीजिए:
:::

:::part{label="(i)"}
:::prompt
$\left[\begin{array}{c}5 \\ \frac{1}{2} \\ -1\end{array}\right]$
:::

:::solution
माना $A=\left[\begin{array}{c}5 \\ \frac{1}{2} \\ -1\end{array}\right]$ अतः $A^{\prime}=\left[\begin{array}{lll}5 & \frac{1}{2} & -1\end{array}\right]$
:::

:::

:::part{label="(ii)"}
:::prompt
$\left[\begin{array}{rr}1 & -1 \\ 2 & 3\end{array}\right]$
:::

:::solution
माना $B=\left[\begin{array}{cc}1 & -1 \\ 2 & 3\end{array}\right]$ अतः $B^{\prime}=\left[\begin{array}{cc}1 & 2 \\ -1 & 3\end{array}\right]$
:::

:::

:::part{label="(iii)"}
:::prompt
$\left[\begin{array}{rrr}-1 & 5 & 6 \\ \sqrt{3} & 5 & 6 \\ 2 & 3 & -1\end{array}\right]$
:::

:::solution
माना $C=\left[\begin{array}{ccc}-1 & 5 & 6 \\ \sqrt{3} & 5 & 6 \\ 2 & 3 & -1\end{array}\right]$ अतः $C^{\prime}=\left[\begin{array}{ccc}-1 & \sqrt{3} & 2 \\ 5 & 5 & 3 \\ 6 & 6 & -1\end{array}\right]$
:::

:::

:::

:::question{number="3.3.2" kind="exercise" id="q_3.3.2" topic="Verifying transpose of sum and difference"}
#### प्रश्न 3.3.2

:::prompt
यदि $\mathrm{A}=\left[\begin{array}{rrr}-1 & 2 & 3 \\ 5 & 7 & 9 \\ -2 & 1 & 1\end{array}\right]$ तथा $\mathrm{B}=\left[\begin{array}{rrr}-4 & 1 & -5 \\ 1 & 2 & 0 \\ 1 & 3 & 1\end{array}\right]$ हैं तो सत्यापित कीजिए कि
:::

:::part{label="(i)"}
:::prompt
$(\mathrm{A}+\mathrm{B})^{\prime}=\mathrm{A}^{\prime}+\mathrm{B}^{\prime}$
:::

:::solution
$(A+B)$
$=\left[\begin{array}{ccc}-1 & 2 & 3 \\ 5 & 7 & 9 \\ -2 & 1 & 1\end{array}\right]+\left[\begin{array}{ccc}-4 & 1 & -5 \\ 1 & 2 & 0 \\ 1 & 3 & 1\end{array}\right]=\left[\begin{array}{ccc}-1-4 & 2+1 & 3-5 \\ 5+1 & 7+2 & 9+0 \\ -2+1 & 1+3 & 1+1\end{array}\right]=\left[\begin{array}{ccc}-5 & 3 & -2 \\ 6 & 9 & 9 \\ -1 & 4 & 2\end{array}\right]$

इसलिए $(A+B)^{\prime}=\left[\begin{array}{ccc}-5 & 6 & -1 \\ 3 & 9 & 4 \\ -2 & 9 & 2\end{array}\right]$

$A^{\prime}+B^{\prime}=\left[\begin{array}{ccc}-1 & 2 & 3 \\ 5 & 7 & 9 \\ -2 & 1 & 1\end{array}\right]^{\prime}+\left[\begin{array}{ccc}-4 & 1 & -5 \\ 1 & 2 & 0 \\ 1 & 3 & 1\end{array}\right]^{\prime}$

$=\left[\begin{array}{ccc}-1 & 5 & -2 \\ 2 & 7 & 1 \\ 3 & 9 & 1\end{array}\right]+\left[\begin{array}{ccc}-4 & 1 & 1 \\ 1 & 2 & 3 \\ -5 & 0 & 1\end{array}\right]=\left[\begin{array}{ccc}-1-4 & 5+1 & -2+1 \\ 2+1 & 7+2 & 1+3 \\ 3-5 & 9+0 & 1+1\end{array}\right]=\left[\begin{array}{ccc}-5 & 6 & -1 \\ 3 & 9 & 4 \\ -2 & 9 & 2\end{array}\right]$

समीकरण (1) और (2) से,
$$
(A+B)^{\prime}=A^{\prime}+B^{\prime}
$$
:::

:::

:::part{label="(ii)"}
:::prompt
$(\mathrm{A}-\mathrm{B})^{\prime}=\mathrm{A}^{\prime}-\mathrm{B}^{\prime}$
:::

:::solution
$(A-B)$
$=\left[\begin{array}{ccc}-1 & 2 & 3 \\ 5 & 7 & 9 \\ -2 & 1 & 1\end{array}\right]-\left[\begin{array}{ccc}-4 & 1 & -5 \\ 1 & 2 & 0 \\ 1 & 3 & 1\end{array}\right]=\left[\begin{array}{ccc}-1+4 & 2-1 & 3+5 \\ 5-1 & 7-2 & 9-0 \\ -2-1 & 1-3 & 1-1\end{array}\right]=\left[\begin{array}{ccc}3 & 1 & 8 \\ 4 & 5 & 9 \\ -3 & -2 & 0\end{array}\right]$

इसलिए $(A-B)^{\prime}=\left[\begin{array}{ccc}3 & 4 & -3 \\ 1 & 5 & -2 \\ 8 & 9 & 0\end{array}\right]$

$$
\begin{aligned}
& A^{\prime}-B^{\prime}=\left[\begin{array}{ccc}
-1 & 2 & 3 \\
5 & 7 & 9 \\
-2 & 1 & 1
\end{array}\right]^{\prime}-\left[\begin{array}{ccc}
-4 & 1 & -5 \\
1 & 2 & 0 \\
1 & 3 & 1
\end{array}\right]^{\prime} \\
& =\left[\begin{array}{ccc}
-1 & 5 & -2 \\
2 & 7 & 1 \\
3 & 9 & 1
\end{array}\right]-\left[\begin{array}{ccc}
-4 & 1 & 1 \\
1 & 2 & 3 \\
-5 & 0 & 1
\end{array}\right]=\left[\begin{array}{ccc}
-1+4 & 5-1 & -2-1 \\
2-1 & 7-2 & 1-3 \\
3+5 & 9-0 & 1-1
\end{array}\right]=\left[\begin{array}{ccc}
3 & 4 & -3 \\
1 & 5 & -2 \\
8 & 9 & 0
\end{array}\right]
\end{aligned}
$$

समीकरण (1) और (2) से,
$$
(A-B)^{\prime}=A^{\prime}-B^{\prime}
$$
:::

:::

:::

:::question{number="3.3.3" kind="exercise" id="q_3.3.3" topic="Verifying transpose given A′"}
#### प्रश्न 3.3.3

:::prompt
यदि $\mathrm{A}^{\prime}=\left[\begin{array}{rr}3 & 4 \\ -1 & 2 \\ 0 & 1\end{array}\right]$ तथा $\mathrm{B}=\left[\begin{array}{rrr}-1 & 2 & 1 \\ 1 & 2 & 3\end{array}\right]$ हैं तो सत्यापित कीजिए कि
:::

:::part{label="(i)"}
:::prompt
$(\mathrm{A}+\mathrm{B})^{\prime}=\mathrm{A}^{\prime}+\mathrm{B}^{\prime}$
:::

:::solution
$$
\begin{aligned}
& \text { (i) } A^{\prime}=\left[\begin{array}{cc}
3 & 4 \\
-1 & 2 \\
0 & 1
\end{array}\right] \Rightarrow A=\left[\begin{array}{ccc}
3 & -1 & 0 \\
4 & 2 & 1
\end{array}\right] \quad\left[\text { क्योंकि }\left(A^{\prime}\right)^{\prime}=A\right] \\
& (A+B)=\left[\begin{array}{ccc}
3 & -1 & 0 \\
4 & 2 & 1
\end{array}\right]+\left[\begin{array}{ccc}
-1 & 2 & 1 \\
1 & 2 & 3
\end{array}\right]=\left[\begin{array}{ccc}
3-1 & -1+2 & 0+1 \\
4+1 & 2+2 & 1+3
\end{array}\right]=\left[\begin{array}{lll}
2 & 1 & 1 \\
5 & 4 & 4
\end{array}\right]
\end{aligned}
$$

इसलिए $(A+B)^{\prime}=\left[\begin{array}{ll}2 & 5 \\ 1 & 4 \\ 1 & 4\end{array}\right]$

$$
\begin{aligned}
& A^{\prime}+B^{\prime}=\left[\begin{array}{ccc}
3 & -1 & 0 \\
4 & 2 & 1
\end{array}\right]^{\prime}+\left[\begin{array}{ccc}
-1 & 2 & 1 \\
1 & 2 & 3
\end{array}\right]^{\prime} \\
& =\left[\begin{array}{cc}
3 & 4 \\
-1 & 2 \\
0 & 1
\end{array}\right]+\left[\begin{array}{cc}
-1 & 1 \\
2 & 2 \\
1 & 3
\end{array}\right]=\left[\begin{array}{cc}
3-1 & 4+1 \\
-1+2 & 2+2 \\
0+1 & 1+3
\end{array}\right]=\left[\begin{array}{ll}
2 & 5 \\
1 & 4 \\
1 & 4
\end{array}\right]
\end{aligned}
$$

समीकरण (1) और (2) से,
$$
(A+B)^{\prime}=A^{\prime}+B^{\prime}
$$
:::

:::

:::part{label="(ii)"}
:::prompt
$(\mathrm{A}-\mathrm{B})^{\prime}=\mathrm{A}^{\prime}-\mathrm{B}^{\prime}$
:::

:::solution
(ii) $A^{\prime}=\left[\begin{array}{cc}3 & 4 \\ -1 & 2 \\ 0 & 1\end{array}\right] \Rightarrow A=\left[\begin{array}{ccc}3 & -1 & 0 \\ 4 & 2 & 1\end{array}\right] \quad\left[\right.$ क्योंकि $\left.\left(A^{\prime}\right)^{\prime}=A\right]$

$$
(A-B)=\left[\begin{array}{ccc}
3 & -1 & 0 \\
4 & 2 & 1
\end{array}\right]-\left[\begin{array}{ccc}
-1 & 2 & 1 \\
1 & 2 & 3
\end{array}\right]=\left[\begin{array}{ccc}
3+1 & -1-2 & 0-1 \\
4-1 & 2-2 & 1-3
\end{array}\right]=\left[\begin{array}{ccc}
4 & -3 & -1 \\
3 & 0 & -2
\end{array}\right]
$$

इसलिए $(A-B)^{\prime}=\left[\begin{array}{cc}4 & 3 \\ -3 & 0 \\ -1 & -2\end{array}\right]$

$$
\begin{aligned}
& A^{\prime}-B^{\prime}=\left[\begin{array}{ccc}
3 & -1 & 0 \\
4 & 2 & 1
\end{array}\right]^{\prime}-\left[\begin{array}{ccc}
-1 & 2 & 1 \\
1 & 2 & 3
\end{array}\right]^{\prime} \\
& =\left[\begin{array}{cc}
3 & 4 \\
-1 & 2 \\
0 & 1
\end{array}\right]-\left[\begin{array}{cc}
-1 & 1 \\
2 & 2 \\
1 & 3
\end{array}\right]=\left[\begin{array}{cc}
3+1 & 4-1 \\
-1-2 & 2-2 \\
0-1 & 1-3
\end{array}\right]=\left[\begin{array}{cc}
4 & 3 \\
-3 & 0 \\
-1 & -2
\end{array}\right]
\end{aligned}
$$

समीकरण (1) और (2) से,
$$
(A-B)^{\prime}=A^{\prime}-B^{\prime}
$$
:::

:::

:::

:::question{number="3.3.4" kind="exercise" id="q_3.3.4" topic="Finding (A+2B)′"}
#### प्रश्न 3.3.4

:::prompt
यदि $\mathrm{A}^{\prime}=\left[\begin{array}{cc}-2 & 3 \\ 1 & 2\end{array}\right]$ तथा $\mathrm{B}=\left[\begin{array}{rr}-1 & 0 \\ 1 & 2\end{array}\right]$ हैं तो $(\mathrm{A}+2 \mathrm{~B})^{\prime}$ ज्ञात कीजिए।
:::

:::solution{label="हल"}
$$
\begin{aligned}
& (A+2 B)=\left[\begin{array}{cc}
-2 & 3 \\
1 & 2
\end{array}\right]+2\left[\begin{array}{cc}
-1 & 0 \\
1 & 2
\end{array}\right] \\
& =\left[\begin{array}{cc}
-2 & 3 \\
1 & 2
\end{array}\right]+\left[\begin{array}{cc}
-2 & 0 \\
2 & 4
\end{array}\right]=\left[\begin{array}{cc}
-2-2 & 3+0 \\
1+2 & 2+4
\end{array}\right]=\left[\begin{array}{cc}
-4 & 3 \\
3 & 6
\end{array}\right]
\end{aligned}
$$

इसलिए $(A+2 B)^{\prime}=\left[\begin{array}{cc}-4 & 3 \\ 3 & 6\end{array}\right]$
:::

:::answer
**उत्तर:** $(A+2B)^{\prime}=\left[\begin{array}{cc}-4 & 3 \\ 3 & 6\end{array}\right]$
:::

:::

:::question{number="3.3.5" kind="exercise" id="q_3.3.5" topic="Verifying (AB)′=B′A′"}
#### प्रश्न 3.3.5

:::prompt
A तथा B आव्यूहों के लिए सत्यापित कीजिए कि $(\mathrm{AB})^{\prime}=\mathrm{B}^{\prime} \mathrm{A}^{\prime}$, जहाँ
:::

:::part{label="(i)"}
:::prompt
$\mathrm{A}=\left[\begin{array}{r}1 \\ -4 \\ 3\end{array}\right], \mathrm{B}=\left[\begin{array}{lll}-1 & 2 & 1\end{array}\right]$
:::

:::solution
दिया है: $A=\left[\begin{array}{c}1 \\ -4 \\ 3\end{array}\right], B=\left[\begin{array}{lll}-1 & 2 & 1\end{array}\right]$

इसलिए, $A B=\left[\begin{array}{c}1 \\ -4 \\ 3\end{array}\right]\left[\begin{array}{lll}-1 & 2 & 1\end{array}\right]=\left[\begin{array}{ccc}1 \times(-1) & 1 \times 2 & 1 \times 1 \\ -4 \times(-1) & -4 \times 2 & -4 \times 1 \\ 3 \times(-1) & 3 \times 2 & 3 \times 1\end{array}\right]=\left[\begin{array}{ccc}-1 & 2 & 1 \\ 4 & -8 & -4 \\ -3 & 6 & 3\end{array}\right]$

इसलिए $A B^{\prime}=\left[\begin{array}{ccc}-1 & 4 & -3 \\ 2 & -8 & 6 \\ 1 & -4 & 3\end{array}\right]$

$B^{\prime}=\left[\begin{array}{lll}-1 & 2 & 1\end{array}\right]^{\prime}=\left[\begin{array}{c}-1 \\ 2 \\ 1\end{array}\right]$ तथा $A^{\prime}=\left[\begin{array}{c}1 \\ -4 \\ 3\end{array}\right]^{\prime}=\left[\begin{array}{lll}1 & -4 & 3\end{array}\right]$

इसलिए, $B^{\prime} A^{\prime}=\left[\begin{array}{c}-1 \\ 2 \\ 1\end{array}\right]\left[\begin{array}{lll}1 & -4 & 3\end{array}\right]=\left[\begin{array}{ccc}-1 \times 1 & -1 \times(-4) & -1 \times 3 \\ 2 \times 1 & 2 \times(-4) & 2 \times 3 \\ 1 \times 1 & 1 \times(-4) & 1 \times 3\end{array}\right]$

$$
=\left[\begin{array}{ccc}
-1 & 4 & -3 \\
2 & -8 & 6 \\
1 & -4 & 3
\end{array}\right]
$$

समीकरण (1) और (2) से,
$$
(A B)^{\prime}=B^{\prime} A^{\prime}
$$
:::

:::

:::part{label="(ii)"}
:::prompt
$\mathrm{A}=\left[\begin{array}{l}0 \\ 1 \\ 2\end{array}\right], \mathrm{B}=\left[\begin{array}{lll}1 & 5 & 7\end{array}\right]$
:::

:::solution
दिया है: $A=\left[\begin{array}{l}0 \\ 1 \\ 2\end{array}\right], B=\left[\begin{array}{lll}1 & 5 & 7\end{array}\right]$

इसलिए, $A B=\left[\begin{array}{l}0 \\ 1 \\ 2\end{array}\right]\left[\begin{array}{lll}1 & 5 & 7\end{array}\right]=\left[\begin{array}{lll}0 \times 1 & 0 \times 5 & 0 \times 7 \\ 1 \times 1 & 1 \times 5 & 1 \times 7 \\ 2 \times 1 & 2 \times 5 & 2 \times 7\end{array}\right]=\left[\begin{array}{ccc}0 & 0 & 0 \\ 1 & 5 & 7 \\ 2 & 10 & 14\end{array}\right]$

इसलिए $A B^{\prime}=\left[\begin{array}{ccc}0 & 1 & 2 \\ 0 & 5 & 10 \\ 0 & 7 & 14\end{array}\right]$

$B^{\prime}=\left[\begin{array}{lll}1 & 5 & 7\end{array}\right]^{\prime}=\left[\begin{array}{l}1 \\ 5 \\ 7\end{array}\right]$ तथा $A^{\prime}=\left[\begin{array}{l}0 \\ 1 \\ 2\end{array}\right]^{\prime}=\left[\begin{array}{lll}0 & 1 & 2\end{array}\right]$

इसलिए, $B^{\prime} A^{\prime}=\left[\begin{array}{l}1 \\ 5 \\ 7\end{array}\right]\left[\begin{array}{lll}0 & 1 & 2\end{array}\right]=\left[\begin{array}{lll}1 \times 0 & 1 \times 1 & 1 \times 2 \\ 5 \times 0 & 5 \times 1 & 5 \times 2 \\ 7 \times 0 & 7 \times 1 & 7 \times 2\end{array}\right]$

$$
=\left[\begin{array}{ccc}
0 & 1 & 2 \\
0 & 5 & 10 \\
0 & 7 & 14
\end{array}\right]
$$

समीकरण (1) और (2) से,
$$
(A B)^{\prime}=B^{\prime} A^{\prime}
$$
:::

:::

:::

:::question{number="3.3.6" kind="exercise" id="q_3.3.6" topic="Verifying A′A=I"}
#### प्रश्न 3.3.6

:::part{label="(i)"}
:::prompt
यदि $\mathrm{A}=\left[\begin{array}{cc}\cos \alpha & \sin \alpha \\ -\sin \alpha & \cos \alpha\end{array}\right]$ हो तो सत्यापित कीजिए कि $\mathrm{A}^{\prime} \mathrm{A}=\mathrm{I}$
:::

:::solution
$A=\left[\begin{array}{cc}\cos \alpha & \sin \alpha \\ -\sin \alpha & \cos \alpha\end{array}\right] \Rightarrow A^{\prime}=\left[\begin{array}{cc}\cos \alpha & -\sin \alpha \\ \sin \alpha & \cos \alpha\end{array}\right]$

इसलिए $A^{\prime} A=\left[\begin{array}{cc}\cos \alpha & -\sin \alpha \\ \sin \alpha & \cos \alpha\end{array}\right]\left[\begin{array}{cc}\cos \alpha & \sin \alpha \\ -\sin \alpha & \cos \alpha\end{array}\right]$
$$
=\left[\begin{array}{cc}
\cos ^{2} \alpha+\sin ^{2} \alpha & \cos \alpha \sin \alpha-\sin \alpha \cos \alpha \\
\sin \alpha \cos \alpha-\cos \alpha \sin \alpha & \sin ^{2} \alpha+\cos ^{2} \alpha
\end{array}\right]=\left[\begin{array}{ll}
1 & 0 \\
0 & 1
\end{array}\right]=I
$$
अतः, $A^{\prime} A=I$
:::

:::

:::part{label="(ii)"}
:::prompt
यदि $\mathrm{A}=\left[\begin{array}{cc}\sin \alpha & \cos \alpha \\ -\cos \alpha & \sin \alpha\end{array}\right]$ हो तो सत्यापित कीजिए कि $\mathrm{A}^{\prime} \mathrm{A}=\mathrm{I}$
:::

:::solution
$A=\left[\begin{array}{cc}\sin \alpha & \cos \alpha \\ -\cos \alpha & \sin \alpha\end{array}\right] \Rightarrow A^{\prime}=\left[\begin{array}{cc}\sin \alpha & -\cos \alpha \\ \cos \alpha & \sin \alpha\end{array}\right]$

इसलिए $A^{\prime} A=\left[\begin{array}{cc}\sin \alpha & -\cos \alpha \\ \cos \alpha & \sin \alpha\end{array}\right]\left[\begin{array}{cc}\sin \alpha & \cos \alpha \\ -\cos \alpha & \sin \alpha\end{array}\right]$
$$
=\left[\begin{array}{cc}
\sin ^{2} \alpha+\cos ^{2} \alpha & \sin \alpha \cos \alpha-\cos \alpha \sin \alpha \\
\cos \alpha \sin \alpha-\sin \alpha \cos \alpha & \cos ^{2} \alpha+\sin ^{2} \alpha
\end{array}\right]=\left[\begin{array}{ll}
1 & 0 \\
0 & 1
\end{array}\right]=I
$$
अतः, $A^{\prime} A=I$
:::

:::

:::

:::question{number="3.3.7" kind="exercise" id="q_3.3.7" topic="Symmetric and skew-symmetric proof"}
#### प्रश्न 3.3.7

:::part{label="(i)"}
:::prompt
सिद्ध कीजिए कि आव्यूह $\mathrm{A}=\left[\begin{array}{rrr}1 & -1 & 5 \\ -1 & 2 & 1 \\ 5 & 1 & 3\end{array}\right]$ एक सममित आव्यूह है।
:::

:::solution
$A=\left[\begin{array}{ccc}1 & -1 & 5 \\ -1 & 2 & 1 \\ 5 & 1 & 3\end{array}\right] \Rightarrow A^{\prime}=\left[\begin{array}{ccc}1 & -1 & 5 \\ -1 & 2 & 1 \\ 5 & 1 & 3\end{array}\right]^{\prime}=\left[\begin{array}{ccc}1 & -1 & 5 \\ -1 & 2 & 1 \\ 5 & 1 & 3\end{array}\right]=A$

$\Rightarrow A^{\prime}=A$, इसलिए आव्यूह $A=\left[\begin{array}{ccc}1 & -1 & 5 \\ -1 & 2 & 1 \\ 5 & 1 & 3\end{array}\right]$ एक सममित आव्यूह है।
:::

:::

:::part{label="(ii)"}
:::prompt
सिद्ध कीजिए कि आव्यूह $\mathrm{A}=\left[\begin{array}{rrr}0 & 1 & -1 \\ -1 & 0 & 1 \\ 1 & -1 & 0\end{array}\right]$ एक विषम सममित आव्यूह है।
:::

:::solution
$A=\left[\begin{array}{ccc}0 & 1 & -1 \\ -1 & 0 & 1 \\ 1 & -1 & 0\end{array}\right] \Rightarrow A^{\prime}=\left[\begin{array}{ccc}0 & 1 & -1 \\ -1 & 0 & 1 \\ 1 & -1 & 0\end{array}\right]^{\prime}=-\left[\begin{array}{ccc}0 & 1 & -1 \\ -1 & 0 & 1 \\ 1 & -1 & 0\end{array}\right]=-A$

$\Rightarrow A^{\prime}=-A$, इसलिए आव्यूह $A=\left[\begin{array}{ccc}0 & 1 & -1 \\ -1 & 0 & 1 \\ 1 & -1 & 0\end{array}\right]$ एक विषम सममित आव्यूह है।
:::

:::

:::

:::question{number="3.3.8" kind="exercise" id="q_3.3.8" topic="A+A′ symmetric, A−A′ skew-symmetric"}
#### प्रश्न 3.3.8

:::prompt
आव्यूह $\mathrm{A}=\left[\begin{array}{ll}1 & 5 \\ 6 & 7\end{array}\right]$ के लिए सत्यापित कीजिए कि
:::

:::part{label="(i)"}
:::prompt
$\left(\mathrm{A}+\mathrm{A}^{\prime}\right)$ एक सममित आव्यूह है।
:::

:::solution
दिया है: $A=\left[\begin{array}{ll}1 & 5 \\ 6 & 7\end{array}\right] \Rightarrow A^{\prime}=\left[\begin{array}{ll}1 & 5 \\ 6 & 7\end{array}\right]^{\prime}=\left[\begin{array}{ll}1 & 6 \\ 5 & 7\end{array}\right]$

इसलिए, $\quad\left(A+A^{\prime}\right)=\left[\begin{array}{ll}1 & 5 \\ 6 & 7\end{array}\right]+\left[\begin{array}{ll}1 & 6 \\ 5 & 7\end{array}\right]=\left[\begin{array}{cc}2 & 11 \\ 11 & 14\end{array}\right]$
$$
\left(A+A^{\prime}\right)^{\prime}=\left[\begin{array}{cc}
2 & 11 \\
11 & 14
\end{array}\right]^{\prime}=\left[\begin{array}{cc}
2 & 11 \\
11 & 14
\end{array}\right]=A
$$
$\Rightarrow\left(A+A^{\prime}\right)^{\prime}=\left(A+A^{\prime}\right)$, इसलिए आव्यूह $\left(A+A^{\prime}\right)$ एक सममित आव्यूह है।
:::

:::

:::part{label="(ii)"}
:::prompt
$\left(\mathrm{A}-\mathrm{A}^{\prime}\right)$ एक विषम सममित आव्यूह है।
:::

:::solution
$\left(A-A^{\prime}\right)=\left[\begin{array}{ll}1 & 5 \\ 6 & 7\end{array}\right]-\left[\begin{array}{ll}1 & 6 \\ 5 & 7\end{array}\right]=\left[\begin{array}{cc}0 & -1 \\ 1 & 0\end{array}\right]$
$$
\left(A-A^{\prime}\right)^{\prime}=\left[\begin{array}{cc}
0 & -1 \\
1 & 0
\end{array}\right]^{\prime}=-\left[\begin{array}{cc}
0 & -1 \\
1 & 0
\end{array}\right]=-A
$$
$\Rightarrow\left(A-A^{\prime}\right)^{\prime}=-\left(A-A^{\prime}\right)$, इसलिए आव्यूह $\left(A-A^{\prime}\right)$ एक विषम सममित आव्यूह है।
:::

:::

:::

:::question{number="3.3.9" kind="exercise" id="q_3.3.9" topic="Symmetric and skew-symmetric parts of a matrix"}
#### प्रश्न 3.3.9

:::prompt
यदि $\mathrm{A}=\left[\begin{array}{rrr}0 & a & b \\ -a & 0 & c \\ -b & -c & 0\end{array}\right]$ तो $\frac{1}{2}\left(\mathrm{~A}+\mathrm{A}^{\prime}\right)$ तथा $\frac{1}{2}\left(\mathrm{~A}-\mathrm{A}^{\prime}\right)$ ज्ञात कीजिए।
:::

:::solution{label="हल"}
दिया है: $A=\left[\begin{array}{ccc}0 & a & b \\ -a & 0 & c \\ -b & -c & 0\end{array}\right] \Rightarrow A^{\prime}=\left[\begin{array}{ccc}0 & a & b \\ -a & 0 & c \\ -b & -c & 0\end{array}\right]^{\prime}=\left[\begin{array}{ccc}0 & -a & -b \\ a & 0 & -c \\ b & c & 0\end{array}\right]$

इसलिए, $\frac{1}{2}\left(A+A^{\prime}\right)=\frac{1}{2}\left(\left[\begin{array}{ccc}0 & a & b \\ -a & 0 & c \\ -b & -c & 0\end{array}\right]+\left[\begin{array}{ccc}0 & -a & -b \\ a & 0 & -c \\ b & c & 0\end{array}\right]\right)$

$$
=\frac{1}{2}\left[\begin{array}{lll}
0 & 0 & 0 \\
0 & 0 & 0 \\
0 & 0 & 0
\end{array}\right]=\left[\begin{array}{lll}
0 & 0 & 0 \\
0 & 0 & 0 \\
0 & 0 & 0
\end{array}\right]
$$

तथा, $\frac{1}{2}\left(A-A^{\prime}\right)=\frac{1}{2}\left(\left[\begin{array}{ccc}0 & a & b \\ -a & 0 & c \\ -b & -c & 0\end{array}\right]-\left[\begin{array}{ccc}0 & -a & -b \\ a & 0 & -c \\ b & c & 0\end{array}\right]\right)$

$$
=\frac{1}{2}\left[\begin{array}{ccc}
0 & 2 a & 2 b \\
-2 a & 0 & 2 c \\
-2 b & -2 c & 0
\end{array}\right]=\left[\begin{array}{ccc}
0 & a & b \\
-a & 0 & c \\
-b & -c & 0
\end{array}\right]
$$
:::

:::answer
**उत्तर:** $\frac{1}{2}\left(A+A^{\prime}\right)=\left[\begin{array}{lll}0 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0\end{array}\right]$, $\frac{1}{2}\left(A-A^{\prime}\right)=\left[\begin{array}{ccc}0 & a & b \\ -a & 0 & c \\ -b & -c & 0\end{array}\right]$
:::

:::

:::question{number="3.3.10" kind="exercise" id="q_3.3.10" topic="Expressing as sum of symmetric and skew-symmetric"}
#### प्रश्न 3.3.10

:::prompt
निम्नलिखित आव्यूहों को एक सममित आव्यूह तथा एक विषम सममित आव्यूह के योगफल के रूप में व्यक्त कीजिए:
:::

:::part{label="(i)"}
:::prompt
$\left[\begin{array}{rr}3 & 5 \\ 1 & -1\end{array}\right]$
:::

:::solution
दिया है: $A=\left[\begin{array}{cc}3 & 5 \\ 1 & -1\end{array}\right]$

इसलिए, $\mathrm{A}=\frac{1}{2}\left(A+A^{\prime}\right)+\frac{1}{2}\left(A-A^{\prime}\right)$

माना, $P=\frac{1}{2}\left(A+A^{\prime}\right)$ तथा $Q=\frac{1}{2}\left(A-A^{\prime}\right)$

$$
\begin{aligned}
& P=\frac{1}{2}\left(A+A^{\prime}\right)=\frac{1}{2}\left(\left[\begin{array}{cc}
3 & 5 \\
1 & -1
\end{array}\right]+\left[\begin{array}{cc}
3 & 1 \\
5 & -1
\end{array}\right]\right)=\frac{1}{2}\left[\begin{array}{cc}
6 & 6 \\
6 & -2
\end{array}\right]=\left[\begin{array}{cc}
3 & 3 \\
3 & -1
\end{array}\right] \\
& P^{\prime}=\left[\begin{array}{cc}
3 & 3 \\
3 & -1
\end{array}\right]^{\prime}=\left[\begin{array}{cc}
3 & 3 \\
3 & -1
\end{array}\right]=P
\end{aligned}
$$

$\Rightarrow P$ एक सममित आव्यूह है।

$$
\begin{aligned}
& Q=\frac{1}{2}\left(A-A^{\prime}\right)=\frac{1}{2}\left(\left[\begin{array}{cc}
3 & 5 \\
1 & -1
\end{array}\right]-\left[\begin{array}{cc}
3 & 1 \\
5 & -1
\end{array}\right]\right)=\frac{1}{2}\left[\begin{array}{cc}
0 & 4 \\
-4 & 0
\end{array}\right]=\left[\begin{array}{cc}
0 & 2 \\
-2 & 0
\end{array}\right] \\
& Q^{\prime}=\left[\begin{array}{cc}
0 & 2 \\
-2 & 0
\end{array}\right]^{\prime}=\left[\begin{array}{cc}
0 & -2 \\
2 & 0
\end{array}\right]=-\left[\begin{array}{cc}
0 & 2 \\
-2 & 0
\end{array}\right]=-Q
\end{aligned}
$$

$\Rightarrow Q$ एक विषम सममित आव्यूह है।

इसप्रकार, $A=P+Q=\left[\begin{array}{cc}3 & 3 \\ 3 & -1\end{array}\right]+\left[\begin{array}{cc}0 & 2 \\ -2 & 0\end{array}\right]$
:::

:::

:::part{label="(ii)"}
:::prompt
$\left[\begin{array}{rrr}6 & -2 & 2 \\ -2 & 3 & -1 \\ 2 & -1 & 3\end{array}\right]$
:::

:::solution
दिया है: $A=\left[\begin{array}{ccc}6 & -2 & 2 \\ -2 & 3 & -1 \\ 2 & -1 & 3\end{array}\right]$

इसलिए, $\mathrm{A}=\frac{1}{2}\left(A+A^{\prime}\right)+\frac{1}{2}\left(A-A^{\prime}\right)$

माना, $P=\frac{1}{2}\left(A+A^{\prime}\right)$ तथा $Q=\frac{1}{2}\left(A-A^{\prime}\right)$

$$
\begin{aligned}
& P=\frac{1}{2}\left(A+A^{\prime}\right)=\frac{1}{2}\left(\left[\begin{array}{ccc}
6 & -2 & 2 \\
-2 & 3 & -1 \\
2 & -1 & 3
\end{array}\right]+\left[\begin{array}{ccc}
6 & -2 & 2 \\
-2 & 3 & -1 \\
2 & -1 & 3
\end{array}\right]\right) \\
& =\frac{1}{2}\left[\begin{array}{ccc}
12 & -4 & 4 \\
-4 & 6 & -2 \\
4 & -2 & 6
\end{array}\right]=\left[\begin{array}{ccc}
6 & -2 & 2 \\
-2 & 3 & -1 \\
2 & -1 & 3
\end{array}\right] \\
& P^{\prime}=\left[\begin{array}{ccc}
6 & -2 & 2 \\
-2 & 3 & -1 \\
2 & -1 & 3
\end{array}\right]=\left[\begin{array}{ccc}
6 & -2 & 2 \\
-2 & 3 & -1 \\
2 & -1 & 3
\end{array}\right]=P
\end{aligned}
$$

$\Rightarrow P$ एक सममित आव्यूह है।

$$
\begin{aligned}
& Q=\frac{1}{2}\left(A-A^{\prime}\right)=\frac{1}{2}\left(\left[\begin{array}{ccc}
6 & -2 & 2 \\
-2 & 3 & -1 \\
2 & -1 & 3
\end{array}\right]-\left[\begin{array}{ccc}
6 & -2 & 2 \\
-2 & 3 & -1 \\
2 & -1 & 3
\end{array}\right]\right) \\
& =\frac{1}{2}\left[\begin{array}{lll}
0 & 0 & 0 \\
0 & 0 & 0 \\
0 & 0 & 0
\end{array}\right]=\left[\begin{array}{lll}
0 & 0 & 0 \\
0 & 0 & 0 \\
0 & 0 & 0
\end{array}\right] \\
& Q^{\prime}=\left[\begin{array}{lll}
0 & 0 & 0 \\
0 & 0 & 0 \\
0 & 0 & 0
\end{array}\right]^{\prime}=\left[\begin{array}{lll}
0 & 0 & 0 \\
0 & 0 & 0 \\
0 & 0 & 0
\end{array}\right]=-\left[\begin{array}{lll}
0 & 0 & 0 \\
0 & 0 & 0 \\
0 & 0 & 0
\end{array}\right]=-Q
\end{aligned}
$$

$\Rightarrow Q$ एक विषम सममित आव्यूह है।

इसप्रकार, $A=P+Q=\left[\begin{array}{ccc}6 & -2 & 2 \\ -2 & 3 & -1 \\ 2 & -1 & 3\end{array}\right]+\left[\begin{array}{lll}0 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0\end{array}\right]$
:::

:::

:::part{label="(iii)"}
:::prompt
$\left[\begin{array}{rrr}3 & 3 & -1 \\ -2 & -2 & 1 \\ -4 & -5 & 2\end{array}\right]$
:::

:::solution
दिया है: $A=\left[\begin{array}{ccc}3 & 3 & -1 \\ -2 & -2 & 1 \\ -4 & -5 & 2\end{array}\right]$

इसलिए, $\mathrm{A}=\frac{1}{2}\left(A+A^{\prime}\right)+\frac{1}{2}\left(A-A^{\prime}\right)$

माना, $P=\frac{1}{2}\left(A+A^{\prime}\right) \quad$ तथा $\quad Q=\frac{1}{2}\left(A-A^{\prime}\right)$

$$
\begin{aligned}
& P=\frac{1}{2}\left(A+A^{\prime}\right)=\frac{1}{2}\left(\left[\begin{array}{ccc}
3 & 3 & -1 \\
-2 & -2 & 1 \\
-4 & -5 & 2
\end{array}\right]+\left[\begin{array}{ccc}
3 & -2 & -4 \\
3 & -2 & -5 \\
-1 & 1 & 2
\end{array}\right]\right) \\
& =\frac{1}{2}\left[\begin{array}{ccc}
6 & 1 & -5 \\
1 & -4 & -4 \\
-5 & -4 & 4
\end{array}\right]=\left[\begin{array}{ccc}
3 & 1 / 2 & -5 / 2 \\
1 / 2 & -2 & -2 \\
-5 / 2 & -2 & 2
\end{array}\right] \\
& P^{\prime}=\left[\begin{array}{ccc}
3 & 1 / 2 & -5 / 2 \\
1 / 2 & -2 & -2 \\
-5 / 2 & -2 & 2
\end{array}\right]=\left[\begin{array}{ccc}
3 & 1 / 2 & -5 / 2 \\
1 / 2 & -2 & -2 \\
-5 / 2 & -2 & 2
\end{array}\right]=P
\end{aligned}
$$

$\Rightarrow P$ एक सममित आव्यूह है।

$$
\begin{aligned}
& Q=\frac{1}{2}\left(A-A^{\prime}\right)=\frac{1}{2}\left(\left[\begin{array}{ccc}
3 & 3 & -1 \\
-2 & -2 & 1 \\
-4 & -5 & 2
\end{array}\right]-\left[\begin{array}{ccc}
3 & -2 & -4 \\
3 & -2 & -5 \\
-1 & 1 & 2
\end{array}\right]\right) \\
& =\frac{1}{2}\left[\begin{array}{ccc}
0 & 5 & 3 \\
-5 & 0 & 6 \\
-3 & -6 & 0
\end{array}\right]=\left[\begin{array}{ccc}
0 & 5 / 2 & 3 / 2 \\
-5 / 2 & 0 & 3 \\
-3 / 2 & -3 & 0
\end{array}\right] \\
& Q^{\prime}=\left[\begin{array}{ccc}
0 & 5 / 2 & 3 / 2 \\
-5 / 2 & 0 & 3 \\
-3 / 2 & -3 & 0
\end{array}\right]^{\prime}=\left[\begin{array}{ccc}
0 & -5 / 2 & -3 / 2 \\
5 / 2 & 0 & -3 \\
3 / 2 & 3 & 0
\end{array}\right]=-\left[\begin{array}{ccc}
0 & 5 / 2 & 3 / 2 \\
-5 / 2 & 0 & 3 \\
-3 / 2 & -3 & 0
\end{array}\right]=-Q
\end{aligned}
$$

$\Rightarrow Q$ एक विषम सममित आव्यूह है।

इसप्रकार, $A=P+Q=\left[\begin{array}{ccc}3 & 1 / 2 & -5 / 2 \\ 1 / 2 & -2 & -2 \\ -5 / 2 & -2 & 2\end{array}\right]+\left[\begin{array}{ccc}0 & 5 / 2 & 3 / 2 \\ -5 / 2 & 0 & 3 \\ -3 / 2 & -3 & 0\end{array}\right]$
:::

:::

:::part{label="(iv)"}
:::prompt
$\left[\begin{array}{rr}1 & 5 \\ -1 & 2\end{array}\right]$
:::

:::solution
दिया है: $A=\left[\begin{array}{cc}1 & 5 \\ -1 & 2\end{array}\right]$

इसलिए, $\mathrm{A}=\frac{1}{2}\left(A+A^{\prime}\right)+\frac{1}{2}\left(A-A^{\prime}\right)$

माना, $P=\frac{1}{2}\left(A+A^{\prime}\right) \quad$ तथा $\quad Q=\frac{1}{2}\left(A-A^{\prime}\right)$

$P=\frac{1}{2}\left(A+A^{\prime}\right)=\frac{1}{2}\left(\left[\begin{array}{cc}1 & 5 \\ -1 & 2\end{array}\right]+\left[\begin{array}{cc}1 & -1 \\ 5 & 2\end{array}\right]\right)=\frac{1}{2}\left[\begin{array}{ll}2 & 4 \\ 4 & 4\end{array}\right]=\left[\begin{array}{ll}1 & 2 \\ 2 & 2\end{array}\right]$

$P^{\prime}=\left[\begin{array}{ll}1 & 2 \\ 2 & 2\end{array}\right]^{\prime}=\left[\begin{array}{ll}1 & 2 \\ 2 & 2\end{array}\right]=P$

$\Rightarrow P$ एक सममित आव्यूह है।

$Q=\frac{1}{2}\left(A-A^{\prime}\right)=\frac{1}{2}\left(\left[\begin{array}{cc}1 & 5 \\ -1 & 2\end{array}\right]-\left[\begin{array}{cc}1 & -1 \\ 5 & 2\end{array}\right]\right)=\frac{1}{2}\left[\begin{array}{cc}0 & 6 \\ -6 & 0\end{array}\right]=\left[\begin{array}{cc}0 & 3 \\ -3 & 0\end{array}\right]$

$Q^{\prime}=\left[\begin{array}{cc}0 & 3 \\ -3 & 0\end{array}\right]^{\prime}=\left[\begin{array}{cc}0 & -3 \\ 3 & 0\end{array}\right]=-\left[\begin{array}{cc}0 & 3 \\ -3 & 0\end{array}\right]=-Q$

$\Rightarrow Q$ एक विषम सममित आव्यूह है।

इसप्रकार, $A=P+Q=\left[\begin{array}{ll}1 & 2 \\ 2 & 2\end{array}\right]+\left[\begin{array}{cc}0 & 3 \\ -3 & 0\end{array}\right]$
:::

:::

:::

:::question{number="3.3.11" kind="exercise" id="q_3.3.11" topic="MCQ: AB−BA for symmetric A, B"}
#### प्रश्न 3.3.11

:::prompt
यदि A तथा B समान कोटि के सममित आव्यूह हैं तो $\mathrm{AB}-\mathrm{BA}$ एक
(A) विषम सममित आव्यूह है
(B) सममित आव्यूह है
(C) शून्य आव्यूह है
(D) तत्समक आव्यूह है
:::

:::solution{label="हल"}
$$
\begin{array}{lr}
(A B-B A)^{\prime}=(A B)^{\prime}-(B A)^{\prime} & {\left[\because(X-Y)^{\prime}=X^{\prime}-Y^{\prime}\right]} \\
=B^{\prime} A^{\prime}-A^{\prime} B^{\prime} & {\left[\because(X Y)^{\prime}=Y^{\prime} X^{\prime}\right]} \\
=B A-A B & {\left[\because \text { दिया है: } A^{\prime}=A, B^{\prime}=B\right]} \\
=-(A B-B A) & \\
\Rightarrow(\mathrm{AB}-\mathrm{BA})^{\prime}=-(\mathrm{AB}-\mathrm{BA}), &
\end{array}
$$

इसलिए आव्यूह $(\mathrm{AB}-\mathrm{BA})$ एक विषम सममित आव्यूह है। अतः, विकल्प $(\mathrm{A})$ सही है।
:::

:::answer
**उत्तर:** (A) विषम सममित आव्यूह है
:::

:::

:::question{number="3.3.12" kind="exercise" id="q_3.3.12" topic="MCQ: solving for α given A+A′=I"}
#### प्रश्न 3.3.12

:::prompt
यदि $\mathrm{A}=\left[\begin{array}{cc}\cos \alpha & -\sin \alpha \\ \sin \alpha & \cos \alpha\end{array}\right]$ तथा $\mathrm{A}+\mathrm{A}^{\prime}=\mathrm{I}$, तो $\alpha$ का मान है
(A) $\frac{\pi}{6}$
(B) $\frac{\pi}{3}$
(C) $\pi$
(D) $\frac{3 \pi}{2}$
:::

:::solution{label="हल"}
दिया है: $A+A^{\prime}=I \Rightarrow\left[\begin{array}{cc}\cos \alpha & -\sin \alpha \\ \sin \alpha & \cos \alpha\end{array}\right]+\left[\begin{array}{cc}\cos \alpha & \sin \alpha \\ -\sin \alpha & \cos \alpha\end{array}\right]=\left[\begin{array}{ll}1 & 0 \\ 0 & 1\end{array}\right]$

$\Rightarrow\left[\begin{array}{cc}2 \cos \alpha & 0 \\ 0 & 2 \cos \alpha\end{array}\right]=\left[\begin{array}{ll}1 & 0 \\ 0 & 1\end{array}\right] \quad \Rightarrow 2 \cos \alpha=1 \quad \Rightarrow \cos \alpha=\frac{1}{2} \quad \Rightarrow \alpha=\frac{\pi}{3}$

अतः, विकल्प (B) सही है।
:::

:::answer
**उत्तर:** (B) $\frac{\pi}{3}$
:::

:::

## अतिरिक्त प्रश्न

:::question{number="3.9.1" kind="additional_exercise" id="q_3.9.1" topic="Skew-symmetric matrix proof"}
#### अतिरिक्त प्रश्न 3.9.1

:::prompt
यदि A तथा B सममित आव्यूह हैं तो सिद्ध कीजिए कि $\mathrm{AB}-\mathrm{BA}$ एक विषम सममित आव्यूह है।
:::

:::solution{label="हल"}
$$
\begin{array}{ll}
(A B-B A)^{\prime}=(A B)^{\prime}-(B A)^{\prime} & {\left[\because(X-Y)^{\prime}=X^{\prime}-Y^{\prime}\right]} \\
=B^{\prime} A^{\prime}-A^{\prime} B^{\prime} & {\left[\because(A B)^{\prime}=B^{\prime} A^{\prime}\right]} \\
=B A-A B & {\left[\because \text { दिया है: } A^{\prime}=A, B^{\prime}=B\right]} \\
=-(A B-B A) & \\
\Rightarrow(A B-B A)^{\prime}=-(A B-B A), &
\end{array}
$$

इसलिए, आव्यूह $(\mathrm{AB}-\mathrm{BA})$ एक विषम सममित आव्यूह है।
:::

:::

:::question{number="3.9.2" kind="additional_exercise" id="q_3.9.2" topic="Symmetric or skew-symmetric of B'AB"}
#### अतिरिक्त प्रश्न 3.9.2

:::prompt
सिद्ध कीजिए कि आव्यूह $\mathrm{B}^{\prime} \mathrm{AB}$ सममित अथवा विषम सममित है यदि A सममित अथवा विषम सममित है।
:::

:::solution{label="हल"}
यदि $A$ सममित आव्यूह है। तब $A^{\prime}=A$

$$
\begin{aligned}
& \text { यहाँ, }\left(B^{\prime} A B\right)^{\prime}=(A B)^{\prime}\left(B^{\prime}\right)^{\prime} \\
& =(A B)^{\prime} B \\
& =B^{\prime} A^{\prime} B \\
& =B^{\prime} A B \\
& \Rightarrow\left(B^{\prime} A B\right)^{\prime}=B^{\prime} A B,
\end{aligned}
$$

इसलिए, आव्यूह $B^{\prime} A B$ एक सममित आव्यूह है।
यदि $A$ विषम सममित आव्यूह है। तब $A^{\prime}=-A$
यदि $A$ विषम सममित आव्यूह है। तब $A^{\prime}=-A$

$$
\begin{aligned}
& \text { यहाँ, }\left(B^{\prime} A B\right)^{\prime}=(A B)^{\prime}\left(B^{\prime}\right)^{\prime} \\
& =(A B)^{\prime} B \\
& =B^{\prime} A^{\prime} B \\
& =-B^{\prime} A B \\
& \Rightarrow\left(B^{\prime} A B\right)^{\prime}=-B^{\prime} A B,
\end{aligned}
$$

$$
\begin{aligned}
& {\left[\because(A B)^{\prime}=B^{\prime} A^{\prime}\right]} \\
& {\left[\because\left(B^{\prime}\right)^{\prime}=B\right]} \\
& {\left[\because(A B)^{\prime}=B^{\prime} A^{\prime}\right]} \\
& {\left[\because \text { दिया है: } A^{\prime}=-A\right]}
\end{aligned}
$$

इसलिए, आव्यूह $B^{\prime} A B$ एक विषम सममित आव्यूह है।
:::

:::

:::question{number="3.9.3" kind="additional_exercise" id="q_3.9.3" topic="Finding x, y, z from A'A=I"}
#### अतिरिक्त प्रश्न 3.9.3

:::prompt
$x, y$, तथा $z$ के मानों को ज्ञात कीजिए, यदि आव्यूह $\mathrm{A}=\left[\begin{array}{rrr}0 & 2 y & z \\ x & y & -z \\ x & -y & z\end{array}\right]$ समीकरण $\mathrm{A}^{\prime} \mathrm{A}=\mathrm{I}$ को संतुष्ट करता है।
:::

:::solution{label="हल"}
दिया है: $A^{\prime} A=I$

$$
\begin{aligned}
& \Rightarrow\left[\begin{array}{ccc}
0 & 2 y & z \\
x & y & -z \\
x & -y & z
\end{array}\right]\left[\begin{array}{ccc}
0 & 2 y & z \\
x & y & -z \\
x & -y & z
\end{array}\right]^{\prime}=\left[\begin{array}{lll}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{array}\right] \\
& \Rightarrow\left[\begin{array}{ccc}
0 & 2 y & z \\
x & y & -z \\
x & -y & z
\end{array}\right]\left[\begin{array}{ccc}
0 & \mathrm{x} & x \\
2 y & y & -y \\
z & -z & z
\end{array}\right]=\left[\begin{array}{ccc}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{array}\right]
\end{aligned}
$$

$$
\Rightarrow\left[\begin{array}{ccc}
0+4 y^{2}+z^{2} & 0+2 y^{2}-z^{2} & 0-2 y^{2}+z^{2} \\
0+2 y^{2}-z^{2} & x^{2}+y^{2}+z^{2} & x^{2}-y^{2}-z^{2} \\
0-2 y^{2}+z^{2} & x^{2}-y^{2}-z^{2} & x^{2}+y^{2}+z^{2}
\end{array}\right]=\left[\begin{array}{lll}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{array}\right]
$$

यदि दो आव्यूह समान हैं तो उनके संगत अवयव भी समान होते हैं, इसलिए $4 y^{2}+z^{2}=1, \quad 2 y^{2}-z^{2}=0$ तथा $x^{2}+y^{2}+z^{2}=1$
हल करने पर, $x= \pm \frac{1}{\sqrt{2}}, y= \pm \frac{1}{\sqrt{6}}$ तथा $z= \pm \frac{1}{\sqrt{3}}$
:::

:::answer
**उत्तर:** $x= \pm \frac{1}{\sqrt{2}}, y= \pm \frac{1}{\sqrt{6}}, z= \pm \frac{1}{\sqrt{3}}$
:::

:::

:::question{number="3.9.4" kind="additional_exercise" id="q_3.9.4" topic="Solving x from matrix product equation"}
#### अतिरिक्त प्रश्न 3.9.4

:::prompt
$x$ के किस मान के लिए $\left[\begin{array}{lll}1 & 2 & 1\end{array}\right]\left[\begin{array}{lll}1 & 2 & 0 \\ 2 & 0 & 1 \\ 1 & 0 & 2\end{array}\right]\left[\begin{array}{l}0 \\ 2 \\ x\end{array}\right]=\mathrm{O}$ है ?
:::

:::solution{label="हल"}
दिया है: $\left[\begin{array}{lll}1 & 2 & 1\end{array}\right]\left[\begin{array}{lll}1 & 2 & 0 \\ 2 & 0 & 1 \\ 1 & 0 & 2\end{array}\right]\left[\begin{array}{l}0 \\ 2 \\ x\end{array}\right]=0$

$$
\begin{aligned}
& \Rightarrow\left[\begin{array}{lll}
1+4+1 & 2+0+0 & 0+2+2
\end{array}\right]\left[\begin{array}{l}
0 \\
2 \\
x
\end{array}\right]=O \\
& \Rightarrow\left[\begin{array}{lll}
6 & 2 & 4
\end{array}\right]\left[\begin{array}{l}
0 \\
2 \\
x
\end{array}\right]=O \\
& \Rightarrow[0+4+4 x]=[0] \\
& \Rightarrow 4+4 x=0 \quad \Rightarrow x=-1
\end{aligned}
$$
:::

:::answer
**उत्तर:** $x=-1$
:::

:::

:::question{number="3.9.5" kind="additional_exercise" id="q_3.9.5" topic="Verifying A²-5A+7I=O"}
#### अतिरिक्त प्रश्न 3.9.5

:::prompt
यदि $\mathrm{A}=\left[\begin{array}{rr}3 & 1 \\ -1 & 2\end{array}\right]$ हो तो सिद्ध कीजिए कि $\mathrm{A}^{2}-5 \mathrm{~A}+7 \mathrm{I}=\mathrm{O}$ है।
:::

:::solution{label="हल"}
$$
\begin{aligned}
& \text { LHS }=A^{2}-5 A+7 I \\
& =\left[\begin{array}{cc}
3 & 1 \\
-1 & 2
\end{array}\right]\left[\begin{array}{cc}
3 & 1 \\
-1 & 2
\end{array}\right]-5\left[\begin{array}{cc}
3 & 1 \\
-1 & 2
\end{array}\right]+7\left[\begin{array}{ll}
1 & 0 \\
0 & 1
\end{array}\right] \\
& =\left[\begin{array}{cc}
9 & 1 \\
-3 & 3+2 \\
-2 & -1+4
\end{array}\right]-\left[\begin{array}{cc}
15 & 5 \\
-5 & 10
\end{array}\right]+\left[\begin{array}{ll}
7 & 0 \\
0 & 7
\end{array}\right] \\
& =\left[\begin{array}{cc}
8 & 5 \\
-5 & 3
\end{array}\right]-\left[\begin{array}{cc}
15 & 5 \\
-5 & 10
\end{array}\right]+\left[\begin{array}{cc}
7 & 0 \\
0 & 7
\end{array}\right] \\
& =\left[\begin{array}{cc}
8-15+7 & 5-5+0 \\
-5+5+0 & 3-10+7
\end{array}\right]=\left[\begin{array}{ll}
0 & 0 \\
0 & 0
\end{array}\right]=O=\text { RHS }
\end{aligned}
$$
:::

:::

:::question{number="3.9.6" kind="additional_exercise" id="q_3.9.6" topic="Solving x from vector-matrix equation"}
#### अतिरिक्त प्रश्न 3.9.6

:::prompt
यदि $\left[\begin{array}{lll}x & -5 & -1\end{array}\right]\left[\begin{array}{lll}1 & 0 & 2 \\ 0 & 2 & 1 \\ 2 & 0 & 3\end{array}\right]\left[\begin{array}{l}x \\ 4 \\ 1\end{array}\right]=\mathrm{O}$ है तो $x$ का मान ज्ञात कीजिए।
:::

:::solution{label="हल"}
दिया है: $\left[\begin{array}{lll}x & -5 & -1\end{array}\right]\left[\begin{array}{lll}1 & 0 & 2 \\ 0 & 2 & 1 \\ 2 & 0 & 3\end{array}\right]\left[\begin{array}{l}x \\ 4 \\ 1\end{array}\right]=0$

$$
\left.\begin{array}{l}
{\left[\begin{array}{lll}
x & -5 & -1
\end{array}\right]\left[\begin{array}{lll}
1 & 0 & 2 \\
0 & 2 & 1 \\
2 & 0 & 3
\end{array}\right]\left[\begin{array}{l}
x \\
4 \\
1
\end{array}\right]} \\
\Rightarrow\left[\begin{array}{lll}
x+0-2 & 0-10+0 & 2 x-5-3
\end{array}\right]\left[\begin{array}{l}
x \\
4 \\
1
\end{array}\right]=0 \\
\Rightarrow\left[\begin{array}{lll}
x-2 & -10 & 2 x-8
\end{array}\right]\left[\begin{array}{l}
x \\
4 \\
1
\end{array}\right]=0 \\
\Rightarrow\left[x^{2}-2 x-40+2 x-8\right.
\end{array}\right]=[0] .0
$$
:::

:::

:::question{number="3.9.7" kind="additional_exercise" id="q_3.9.7" topic="Revenue and profit via matrix algebra"}
#### अतिरिक्त प्रश्न 3.9.7

:::prompt
एक निर्माता तीन प्रकार की वस्तुएँ $x, y$, तथा z का उत्पादन करता है जिन का वह दो बाजारों में विक्रय करता है। वस्तुओं की वार्षिक बिक्री नीचे सूचित (निदर्शित) है:

| बाज़ार | उत्पादन |  |  |
| :--- | :--- | :--- | :--- |
| I | 10,000 | 2,000 | 18,000 |
| II | 6,000 | 20,000 | 8,000 |
:::

:::part
:::prompt
यदि $x, y$ तथा $z$ की प्रत्येक इकाई का विक्रय मूल्य क्रमशः Rs $2.50$, Rs $1.50$ तथा Rs $1.00$ है तो प्रत्येक बाज़ार में कुल आय (Revenue), आव्यूह बीजगणित की सहायता से ज्ञात कीजिए।
:::

:::solution
यदि $x, y$ तथा $z$ की प्रत्येक इकाई का विक्रय मूल्य क्रमशः ₹ $2.50$, ₹ $1.50$ तथा ₹ $1.00$ है तो वस्तुएँ विक्रय मूल्य

|  | $x$ | $y$ | $z$ |  |
| :--- | :--- | :--- | :--- | :--- |
| बाजार I | [10000 | $2000$ | $18000$ | ₹2.50] |
| बाजार II | $6000$ | $20000$ | $8000$ J | ₹1.00] |
|  |  |  |  |  |

प्रत्येक बाज़ार में कुल आय

$$
=\left[\begin{array}{ccc}
10000 & 2000 & 18000 \\
6000 & 20000 & 8000
\end{array}\right]\left[\begin{array}{c}
₹ 2.50 \\
₹ 1.50 \\
₹ 1.00
\end{array}\right]=\left[\begin{array}{c}
₹ 25000+₹ 3000+₹ 18000 \\
₹ 15000+₹ 30000+₹ 8000
\end{array}\right]=\left[\begin{array}{c}
₹ 46000 \\
₹ 53000
\end{array}\right]
$$

अतः, बाज़ार I में कुल आय ₹46000 तथा बाज़ार II में कुल आय ₹53000 है।
:::

:::

:::part
:::prompt
यदि उपर्युक्त तीन वस्तुओं की प्रत्येक इकाई की लागत (Cost) क्रमश: Rs 2.00, Rs $1.00$ तथा पैसे $50$ है तो कुल लाभ (Gross profit) ज्ञात कीजिए।
:::

:::solution
यदि $x, y$ तथा $z$ की प्रत्येक इकाई की लागत क्रमशः ₹ $2.00$, ₹ $1.00$ तथा $50$ पैसे है तो वस्तुएँ लागत

|  | $x$ | $y$ | $z$ |  |
| :--- | :--- | :--- | :--- | :--- |
| बाजार I | [10000 | $2000$ | $18000$ | ₹2.00] |
| बाजार II | $6000$ | $20000$ | $8000$ J | ₹0.50] |
|  |  |  |  |  |

प्रत्येक बाज़ार में कुल लागत

$$
=\left[\begin{array}{ccc}
10000 & 2000 & 18000 \\
6000 & 20000 & 8000
\end{array}\right]\left[\begin{array}{c}
₹ 2.00 \\
₹ 1.00 \\
₹ 0.50
\end{array}\right]=\left[\begin{array}{c}
₹ 20000+₹ 2000+₹ 9000 \\
₹ 12000+₹ 20000+₹ 4000
\end{array}\right]=\left[\begin{array}{c}
₹ 31000 \\
₹ 36000
\end{array}\right]
$$

बाज़ार I में कुल आय ₹46000 तथा कुल लागत ₹31000 है।
अतः, कुल लाभ = आय - लागत = ₹46000 - ₹31000 = ₹15000
बाज़ार $I I$ में कुल आय ₹ $53000$ तथा कुल लागत ₹ $36000$ है।
अतः, कुल लाभ = आय - लागत =₹53000-₹36000=₹17000
:::

:::

:::

:::question{number="3.9.8" kind="additional_exercise" id="q_3.9.8" topic="Finding matrix X from an equation"}
#### अतिरिक्त प्रश्न 3.9.8

:::prompt
आव्यूह X ज्ञात कीजिए, यदि $\mathrm{X}\left[\begin{array}{lll}1 & 2 & 3 \\ 4 & 5 & 6\end{array}\right]=\left[\begin{array}{rrr}-7 & -8 & -9 \\ 2 & 4 & 6\end{array}\right]$ है।
:::

:::solution{label="हल"}
माना, $\mathrm{X}=\left[\begin{array}{ll}a & b \\ c & d\end{array}\right]$
इसलिए, $\mathrm{X}\left[\begin{array}{lll}1 & 2 & 3 \\ 4 & 5 & 6\end{array}\right]=\left[\begin{array}{ccc}-7 & -8 & -9 \\ 2 & 4 & 6\end{array}\right]$

$$
\begin{aligned}
& \Rightarrow\left[\begin{array}{ll}
a & b \\
c & d
\end{array}\right]\left[\begin{array}{lll}
1 & 2 & 3 \\
4 & 5 & 6
\end{array}\right]=\left[\begin{array}{ccc}
-7 & -8 & -9 \\
2 & 4 & 6
\end{array}\right] \\
& \Rightarrow\left[\begin{array}{lll}
a+4 b & 2 a+5 b & 3 a+6 b \\
c+4 d & 2 c+5 d & 3 c+6 d
\end{array}\right]=\left[\begin{array}{ccc}
-7 & -8 & -9 \\
2 & 4 & 6
\end{array}\right]
\end{aligned}
$$

यदि दो आव्यूह समान हैं तो उनके संगत अवयव भी समान होते हैं, इसलिए

$$
a+4 b=-7, \quad 2 a+5 b=-8, c+4 d=2 \text { तथा } 2 c+5 d=4
$$

हल करने पर, $a=1, b=-2, c=2$ तथा $d=0$
इसलिए, $\mathrm{X}=\left[\begin{array}{cc}1 & -2 \\ 2 & 0\end{array}\right]$
:::

:::answer
**उत्तर:** $\mathrm{X}=\left[\begin{array}{cc}1 & -2 \\ 2 & 0\end{array}\right]$
:::

:::

:::question{number="3.9.9" kind="additional_exercise" id="q_3.9.9" topic="MCQ: property from A²=I"}
#### अतिरिक्त प्रश्न 3.9.9

:::prompt
यदि $\mathrm{A}=\left[\begin{array}{cc}\alpha & \beta \\ \gamma & -\alpha\end{array}\right]$ इस प्रकार है कि $\mathrm{A}^{2}=\mathrm{I}$, तो
(A) $1+\alpha^{2}+\beta \gamma=0$
(B) $1-\alpha^{2}+\beta \gamma=0$
(C) $1-\alpha^{2}-\beta \gamma=0$
(D) $1+\alpha^{2}-\beta \gamma=0$
:::

:::solution{label="हल"}
दिया है: $A^{2}=I$

$$
\Rightarrow\left[\begin{array}{cc}
\alpha & \beta \\
\gamma & -\alpha
\end{array}\right]\left[\begin{array}{cc}
\alpha & \beta \\
\gamma & -\alpha
\end{array}\right]=\left[\begin{array}{ll}
1 & 0 \\
0 & 1
\end{array}\right] \quad \Rightarrow\left[\begin{array}{cc}
\alpha^{2}+\beta \gamma & \alpha \beta-\beta \alpha \\
\alpha \gamma-\alpha \gamma & \beta \gamma+\alpha^{2}
\end{array}\right]=\left[\begin{array}{ll}
1 & 0 \\
0 & 1
\end{array}\right]
$$

तुलना करने पर, $\alpha^{2}+\beta \gamma=1$, अतः, विकल्प (C) सही है।
:::

:::answer
**उत्तर:** (C) $1-\alpha^{2}-\beta \gamma=0$
:::

:::

:::question{number="3.9.10" kind="additional_exercise" id="q_3.9.10" topic="MCQ: symmetric and skew-symmetric matrix"}
#### अतिरिक्त प्रश्न 3.9.10

:::prompt
यदि एक आव्यूह सममित तथा विषम सममित दोनों ही है तो:
(A) A एक विकर्ण आव्यूह है।
(B) A एक शून्य आव्यूह है।
(C) A एक वर्ग आव्यूह है।
(D) इनमें से कोई नहीं।
:::

:::solution{label="हल"}
एक शून्य आव्यूह ही सममित तथा विषम सममित दोनों प्रकार का होता है।
अतः, विकल्प (B) सही है।
:::

:::answer
**उत्तर:** (B) A एक शून्य आव्यूह है।
:::

:::

:::question{number="3.9.11" kind="additional_exercise" id="q_3.9.11" topic="MCQ: (I+A)³-7A given A²=A"}
#### अतिरिक्त प्रश्न 3.9.11

:::prompt
यदि A एक वर्ग आव्यूह इस प्रकार है कि $\mathrm{A}^{2}=\mathrm{A}$, तो $(\mathrm{I}+\mathrm{A})^{3}-7 \mathrm{~A}$ बराबर है:
(A) A
(B) $\mathrm{I}-\mathrm{A}$
(C) I
(D) 3A
:::

:::solution{label="हल"}
$$
\begin{array}{ll}
(I+A)^{3}-7 A=I^{3}+A^{3}+3 I^{2} \mathrm{~A}+3 I A^{2}-7 A & \\
=I+A^{2} A+3 I \mathrm{~A}+3 I A^{2}-7 A & {\left[\text { क्योंकि } I^{3}=I^{2}=I\right]} \\
=I+A A+3 \mathrm{~A}+3 I A-7 A & {\left[\text { क्योंकि } A^{2}=A\right]} \\
=I+A+3 \mathrm{~A}+3 A-7 A=I & {[\text { क्योंकि } I A=A]}
\end{array}
$$

अतः, विकल्प (C) सही है।
:::

:::answer
**उत्तर:** (C) I
:::

:::
