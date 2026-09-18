---
subject: maths
class: 12
chapter: 3
lang: hi
title: "आव्यूह"
---

# आव्यूह

## उदाहरण

:::example{number="3.1" kind="example" id="ex_3.1" topic="Matrix representation of data"}
#### उदाहरण 3.1

:::prompt
तीन फैक्ट्रियों I, II तथा III में पुरुष तथा महिला कर्मियों से संबंधित निम्नलिखित सूचना पर विचार कीजिए:

|  | पुरुष कर्मी | महिला कर्मी |
| :--- | :--- | :--- |
| I | $30$ | $25$ |
| II | $25$ | $31$ |
| III | $27$ | $26$ |

उपर्युक्त सूचना को एक $3 \times 2$ आव्यूह में निरूपित कीजिए। तीसरी पंक्ति और दूसरे स्तंभ वाली प्रविष्टि क्या प्रकट करती है?
:::

:::solution{label="हल"}
प्रदत्त सूचना को $3 \times 2$ आव्यूह के रूप में निम्नलिखित प्रकार से निरूपित किया जा सकता है:

$$
A=\left[\begin{array}{ll}
30 & 25 \\
25 & 31 \\
27 & 26
\end{array}\right]
$$

तीसरी पंक्ति और दूसरे स्तंभ की प्रविष्टि फैक्ट्री-III कारखाने में महिला कार्यकर्ताओं की संख्या प्रकट करती है।
:::

:::answer
**उत्तर:** तीसरी पंक्ति और दूसरे स्तंभ की प्रविष्टि फैक्ट्री-III में महिला कार्यकर्ताओं की संख्या प्रकट करती है।
:::

:::

:::example{number="3.2" kind="example" id="ex_3.2" topic="Possible orders of a matrix"}
#### उदाहरण 3.2

:::prompt
यदि किसी आव्यूह में $8$ अवयव हैं, तो इसकी संभव कोटियाँ क्या हो सकती हैं?
:::

:::solution{label="हल"}
हमें ज्ञात है कि, यदि किसी आव्यूह की कोटि $m \times n$ है तो इसमें $m n$ अवयव होते हैं। अतएव $8$ अवयवों वाले किसी आव्यूह के सभी संभव कोटियाँ ज्ञात करने के लिए हम प्राकृत संख्याओं के उन सभी क्रमित युग्मों को ज्ञात करेंगे जिनका गुणनफल $8$ है।

अतः सभी संभव क्रमित युग्म $(1,8),(8,1),(4,2),(2,4)$ हैं।

अतएव संभव कोटियाँ $1 \times 8,8 \times 1,4 \times 2,2 \times 4$ हैं।
:::

:::answer
**उत्तर:** संभव कोटियाँ $1 \times 8, 8 \times 1, 4 \times 2, 2 \times 4$ हैं।
:::

:::

:::example{number="3.3" kind="example" id="ex_3.3" topic="Constructing a matrix from a formula"}
#### उदाहरण 3.3

:::prompt
एक ऐसे $3 \times 2$ आव्यूह की रचना कीजिए, जिसके अवयव $a_{i j}=\frac{1}{2}|i-3 j|$ द्वारा प्रदत्त हैं।
:::

:::solution{label="हल"}
एक $3 \times 2$ आव्यूह, सामान्यतः इस प्रकार होता है: $\mathrm{A}=\left[\begin{array}{ll}a_{11} & a_{12} \\ a_{21} & a_{22} \\ a_{31} & a_{32}\end{array}\right]$

अब,

$$
a_{i j}=\frac{1}{2}|i-3 j|, i=1,2,3 \text { तथा } j=1,2
$$

इसलिए

$$
a_{11}=\frac{1}{2}|1-3.1|=1
$$

$$
a_{12}=\frac{1}{2}|1-3.2|=\frac{5}{2}
$$

$$
\begin{aligned}
& a_{21}=\frac{1}{2}|2-3.1|=\frac{1}{2} \\
& a_{31}=\frac{1}{2}|3-3.1|=0
\end{aligned}
$$

$$
\begin{aligned}
& a_{22}=\frac{1}{2}|2-3.2|=2 \\
& a_{32}=\frac{1}{2}|3-3.2|=\frac{3}{2}
\end{aligned}
$$

अतः अभीष्ट आव्यूह $\mathrm{A}=\left[\begin{array}{cc}1 & \frac{5}{2} \\ \frac{1}{2} & 2 \\ 0 & \frac{3}{2}\end{array}\right]$ है।
:::

:::answer
**उत्तर:** $\mathrm{A}=\left[\begin{array}{cc}1 & \frac{5}{2} \\ \frac{1}{2} & 2 \\ 0 & \frac{3}{2}\end{array}\right]$
:::

:::

:::example{number="3.4" kind="example" id="ex_3.4" topic="Equality of matrices - solving unknowns"}
#### उदाहरण 3.4

:::prompt
यदि $\left[\begin{array}{ccc}x+3 & z+4 & 2 y-7 \\ -6 & a-1 & 0 \\ b-3 & -21 & 0\end{array}\right]=\left[\begin{array}{ccc}0 & 6 & 3 y-2 \\ -6 & -3 & 2 c+2 \\ 2 b+4 & -21 & 0\end{array}\right]$
हो तो $a, b, c, x, y$ तथा $z$ के मान ज्ञात कीजिए।
:::

:::solution{label="हल"}
चूँकि प्रदत्त आव्यूह समान हैं, इसलिए इनके संगत अवयव भी समान होंगे। संगत अवयवों की तुलना करने पर हमें निम्नलिखित परिणाम प्राप्त होता है:

$$
\begin{array}{llr}
x+3=0, & z+4=6, & 2 y-7=3 y-2 \\
a-1=-3, & 0=2 c+2 & b-3=2 b+4,
\end{array}
$$

इन्हें सरल करने पर हमें प्राप्त होता है कि

$$
a=-2, b=-7, c=-1, x=-3, y=-5, z=2
$$
:::

:::answer
**उत्तर:** $a=-2, b=-7, c=-1, x=-3, y=-5, z=2$
:::

:::

:::example{number="3.5" kind="example" id="ex_3.5" topic="Equality of matrices - solving unknowns"}
#### उदाहरण 3.5

:::prompt
यदि $\left[\begin{array}{cc}2 a+b & a-2 b \\ 5 c-d & 4 c+3 d\end{array}\right]=\left[\begin{array}{cc}4 & -3 \\ 11 & 24\end{array}\right]$ हो तो $a, b, c$, तथा $d$ के मान ज्ञात कीजिए।
:::

:::solution{label="हल"}
दो आव्यूहों की समानता की परिभाषा द्वारा, संगत अवयवों को समान रखने पर हमें प्राप्त होता है कि

$$
\begin{array}{rlrl}
2 a+b & =4 & 5 c-d & =11 \\
a-2 b & =-3 & 4 c+3 d & =24
\end{array}
$$

इन समीकरणों को सरल करने पर $a=1, b=2, c=3$ तथा $d=4$ प्राप्त होता है।
:::

:::answer
**उत्तर:** $a=1, b=2, c=3, d=4$
:::

:::

:::example{number="3.6" kind="example" id="ex_3.6" topic="Addition of matrices"}
#### उदाहरण 3.6

:::prompt
$\mathrm{A}=\left[\begin{array}{ccc}\sqrt{3} & 1 & -1 \\ 2 & 3 & 0\end{array}\right]$ तथा $\mathrm{B}=\left[\begin{array}{ccc}2 & \sqrt{5} & 1 \\ -2 & 3 & \frac{1}{2}\end{array}\right]$ है तो $\mathrm{A}+\mathrm{B}$ ज्ञात कीजिए।
:::

:::solution{label="हल"}
क्योंकि A तथा B समान कोटि $2 \times 3$ वाले आव्यूह हैं, इसलिए A तथा B का योग परिभाषित है, और
$\mathrm{A}+\mathrm{B}=\left[\begin{array}{lll}2+\sqrt{3} & 1+\sqrt{5} & 1-1 \\ 2-2 & 3+3 & 0+\frac{1}{2}\end{array}\right]=\left[\begin{array}{ccc}2+\sqrt{3} & 1+\sqrt{5} & 0 \\ 0 & 6 & \frac{1}{2}\end{array}\right]$ द्वारा प्राप्त होता है।
:::

:::answer
**उत्तर:** $\mathrm{A}+\mathrm{B}=\left[\begin{array}{ccc}2+\sqrt{3} & 1+\sqrt{5} & 0 \\ 0 & 6 & \frac{1}{2}\end{array}\right]$
:::

:::

:::example{number="3.7" kind="example" id="ex_3.7" topic="Scalar multiplication and subtraction"}
#### उदाहरण 3.7

:::prompt
यदि $\mathrm{A}=\left[\begin{array}{lll}1 & 2 & 3 \\ 2 & 3 & 1\end{array}\right]$ तथा $\mathrm{B}=\left[\begin{array}{rrr}3 & -1 & 3 \\ -1 & 0 & 2\end{array}\right]$ हैं तो $2 \mathrm{~A}-\mathrm{B}$ ज्ञात कीजिए।
:::

:::solution{label="हल"}
हम पाते हैं

$$
\begin{aligned}
2 A-B & =2\left[\begin{array}{lll}
1 & 2 & 3 \\
2 & 3 & 1
\end{array}\right]-\left[\begin{array}{lrl}
3 & -1 & 3 \\
-1 & 0 & 2
\end{array}\right] \\
& =\left[\begin{array}{lll}
2 & 4 & 6 \\
4 & 6 & 2
\end{array}\right]+\left[\begin{array}{rrr}
-3 & 1 & -3 \\
1 & 0 & -2
\end{array}\right] \\
& =\left[\begin{array}{lll}
2-3 & 4+1 & 6-3 \\
4+1 & 6+0 & 2-2
\end{array}\right]=\left[\begin{array}{ccc}
-1 & 5 & 3 \\
5 & 6 & 0
\end{array}\right]
\end{aligned}
$$
:::

:::answer
**उत्तर:** $2 A-B=\left[\begin{array}{ccc}-1 & 5 & 3 \\ 5 & 6 & 0\end{array}\right]$
:::

:::

:::example{number="3.8" kind="example" id="ex_3.8" topic="Solving a matrix equation"}
#### उदाहरण 3.8

:::prompt
यदि $\mathrm{A}=\left[\begin{array}{rr}8 & 0 \\ 4 & -2 \\ 3 & 6\end{array}\right], \mathrm{B}=\left[\begin{array}{cc}2 & -2 \\ 4 & 2 \\ -5 & 1\end{array}\right]$ तथा $2 \mathrm{~A}+3 \mathrm{X}=5 \mathrm{~B}$ दिया हो तो आव्यूह X ज्ञात कीजिए।
:::

:::solution{label="हल"}
दिया है $2 \mathrm{~A}+3 \mathrm{X}=5 \mathrm{~B}$

या

$$
2 A+3 X-2 A=5 B-2 A
$$

या

$$
2 A-2 A+3 X=5 B-2 A
$$

(आव्यूह योग क्रम-विनिमेय है)

या

$$
O+3 X=5 B-2 A
$$

(-2A, आव्यूह 2A का योग प्रतिलोम है)

या

$$
3 X=5 B-2 A
$$

(O, योग का तत्समक है)

या

$$
X=\frac{1}{3}(5 B-2 A)
$$

या

$$
\mathrm{X}=\frac{1}{3}\left(5\left[\begin{array}{cc}
2 & -2 \\
4 & 2 \\
-5 & 1
\end{array}\right]-2\left[\begin{array}{cc}
8 & 0 \\
4 & -2 \\
3 & 6
\end{array}\right]\right)=\frac{1}{3}\left(\left[\begin{array}{cc}
10 & -10 \\
20 & 10 \\
-25 & 5
\end{array}\right]+\left[\begin{array}{cc}
-16 & 0 \\
-8 & 4 \\
-6 & -12
\end{array}\right]\right)
$$

$$
=\frac{1}{3}\left[\begin{array}{cc}
10-16 & -10+0 \\
20-8 & 10+4 \\
-25-6 & 5-12
\end{array}\right]=\frac{1}{3}\left[\begin{array}{cc}
-6 & -10 \\
12 & 14 \\
-31 & -7
\end{array}\right]=\left[\begin{array}{cc}
-2 & \frac{-10}{3} \\
4 & \frac{14}{3} \\
\frac{-31}{3} & \frac{-7}{3}
\end{array}\right]
$$
:::

:::answer
**उत्तर:** $\mathrm{X}=\left[\begin{array}{cc}-2 & \frac{-10}{3} \\ 4 & \frac{14}{3} \\ \frac{-31}{3} & \frac{-7}{3}\end{array}\right]$
:::

:::

:::example{number="3.9" kind="example" id="ex_3.9" topic="Solving simultaneous matrix equations"}
#### उदाहरण 3.9

:::prompt
X तथा Y , ज्ञात कीजिए, यदि $\mathrm{X}+\mathrm{Y}=\left[\begin{array}{ll}5 & 2 \\ 0 & 9\end{array}\right]$ तथा $\mathrm{X}-\mathrm{Y}=\left[\begin{array}{cc}3 & 6 \\ 0 & -1\end{array}\right]$ है।
:::

:::solution{label="हल"}
यहाँ पर $(\mathrm{X}+\mathrm{Y})+(\mathrm{X}-\mathrm{Y})=\left[\begin{array}{cc}5 & 2 \\ 0 & 9\end{array}\right]+\left[\begin{array}{cc}3 & 6 \\ 0 & -1\end{array}\right]$

या

$$
(\mathrm{X}+\mathrm{X})+(\mathrm{Y}-\mathrm{Y})=\left[\begin{array}{ll}
8 & 8 \\
0 & 8
\end{array}\right] \Rightarrow 2 \mathrm{X}=\left[\begin{array}{ll}
8 & 8 \\
0 & 8
\end{array}\right]
$$

या

$$
\mathrm{X}=\frac{1}{2}\left[\begin{array}{ll}
8 & 8 \\
0 & 8
\end{array}\right]=\left[\begin{array}{ll}
4 & 4 \\
0 & 4
\end{array}\right]
$$

साथ ही

$$
(X+Y)-(X-Y)=\left[\begin{array}{ll}
5 & 2 \\
0 & 9
\end{array}\right]-\left[\begin{array}{rr}
3 & 6 \\
0 & -1
\end{array}\right]
$$

या

$$
(\mathrm{X}-\mathrm{X})+(\mathrm{Y}+\mathrm{Y})=\left[\begin{array}{cc}
5-3 & 2-6 \\
0 & 9+1
\end{array}\right] \Rightarrow 2 \mathrm{Y}=\left[\begin{array}{cc}
2 & -4 \\
0 & 10
\end{array}\right]
$$

या

$$
\mathrm{Y}=\frac{1}{2}\left[\begin{array}{rr}
2 & -4 \\
0 & 10
\end{array}\right]=\left[\begin{array}{rr}
1 & -2 \\
0 & 5
\end{array}\right]
$$
:::

:::answer
**उत्तर:** $\mathrm{X}=\left[\begin{array}{ll}4 & 4 \\ 0 & 4\end{array}\right], \mathrm{Y}=\left[\begin{array}{rr}1 & -2 \\ 0 & 5\end{array}\right]$
:::

:::

:::example{number="3.10" kind="example" id="ex_3.10" topic="Solving for unknowns in a matrix equation"}
#### उदाहरण 3.10

:::prompt
निम्नलिखित समीकरण से $x$ तथा $y$ के मानों को ज्ञात कीजिए:

$$
2\left[\begin{array}{lc}
x & 5 \\
7 & y-3
\end{array}\right]+\left[\begin{array}{rr}
3 & -4 \\
1 & 2
\end{array}\right]=\left[\begin{array}{cc}
7 & 6 \\
15 & 14
\end{array}\right]
$$
:::

:::solution{label="हल"}
दिया है

$$
2\left[\begin{array}{cc}
x & 5 \\
7 & y-3
\end{array}\right]+\left[\begin{array}{cc}
3 & -4 \\
1 & 2
\end{array}\right]=\left[\begin{array}{cc}
7 & 6 \\
15 & 14
\end{array}\right] \Rightarrow\left[\begin{array}{cc}
2 x & 10 \\
14 & 2 y-6
\end{array}\right]+\left[\begin{array}{cc}
3 & -4 \\
1 & 2
\end{array}\right]=\left[\begin{array}{cc}
7 & 6 \\
15 & 14
\end{array}\right]
$$

या

$$
\left[\begin{array}{cc}
2 x+3 & 10-4 \\
14+1 & 2 y-6+2
\end{array}\right]=\begin{array}{cc}
7 & 6 \\
15 & 14
\end{array} \Rightarrow\left[\begin{array}{cc}
2 x+3 & 6 \\
15 & 2 y-4
\end{array}\right]=\left[\begin{array}{cc}
7 & 6 \\
15 & 14
\end{array}\right]
$$

या

$$
2 x+3=7 \quad \text { तथा } \quad 2 y-4=14 \text { (क्यों?) }
$$

या

$$
2 x=7-3 \quad \text { तथा } \quad 2 y=18
$$

या

$$
x=\frac{4}{2} \quad \text { तथा } \quad y=\frac{18}{2}
$$

अर्थात्

$$
x=2 \quad \text { तथा } \quad y=9
$$
:::

:::answer
**उत्तर:** $x=2, y=9$
:::

:::

:::example{number="3.11" kind="example" id="ex_3.11" topic="Matrix application - farmers' rice sales"}
#### उदाहरण 3.11

:::prompt
दो किसान रामकिशन और गुरचरन सिंह केवल तीन प्रकार के चावल जैसे बासमती, परमल तथा नउरा की खेती करते हैं। दोनों किसानों द्वारा, सितंबर तथा अक्तूबर माह में, इस प्रकार के चावल की बिक्री (रुपयों में) को, निम्नलिखित A त था B आव्यूहों में व्यक्त किया गया है:

सितंबर माह की बिक्री (Rs में)
बासमती परमल नउरा
$\mathrm{A}=\left[\begin{array}{lll}10,000 & 20,000 & 30,000 \\ 50,000 & 30,000 & 10,000\end{array}\right] \begin{aligned} & \text { रामकिशन } \\ & \text { गुरुचरण सिंह }\end{aligned}$

अक्तूबर माह की बिक्री (Rs में)
बासमती परमल नउरा
$\mathrm{A}-\mathrm{B}=\left[\begin{array}{ccc}5000 & 10,000 & 24,000 \\ 30,000 & 20,000 & 0\end{array}\right] \begin{aligned} & \text { रामकिशन } \\ & \text { गुरुचरण सिंह }\end{aligned}$
:::

:::part{label="(i)"}
:::prompt
प्रत्येक किसान की प्रत्येक प्रकार के चावल की सितंबर तथा अक्तूबर की सम्मिलित बिक्री ज्ञात कीजिए।
:::

:::solution
प्रत्येक किसान की प्रत्येक प्रकार के चावल की सितंबर तथा अक्तूबर में प्रत्येक प्रकार के चावल की बिक्री अगले पृष्ठ पर दी गई है:

$$
\mathrm{A}+\mathrm{B}=\left[\begin{array}{ccc}
\text { बासमती } & \text { परमल } & \text { नउरा } \\
15,000 & 30,000 & 36,000 \\
70,000 & 40,000 & 20,000
\end{array}\right] \begin{aligned}
& \text { रामकिशन } \\
& \text { गुरुचरण सिंह }
\end{aligned}
$$
:::

:::

:::part{label="(ii)"}
:::prompt
सितंबर की अपेक्षा अक्तूबर में हुई बिक्री में कमी ज्ञात कीजिए।
:::

:::solution
सितंबर की अपेक्षा अक्तूबर में हुई बिक्री में कमी नीचे दी गई है,
$$
\mathrm{A}-\mathrm{B}=\left[\begin{array}{ccc}
\text { बासमती } & \text { परमल } & \text { नउरा } \\
5000 & 10,000 & 24,000 \\
30,000 & 20,000 & 0
\end{array}\right] \begin{aligned}
& \text { रामकिशन } \\
& \text { गुरुचरण सिंह }
\end{aligned}
$$
:::

:::

:::part{label="(iii)"}
:::prompt
यदि दोनों किसानों को कुल बिक्री पर $2 \%$ लाभ मिलता है, तो अक्तूबर में प्रत्येक प्रकार के चावल की बिक्री पर प्रत्येक किसान को मिलने वाला लाभ ज्ञात कीजिए।
:::

:::solution
$$
\begin{aligned}
& \mathrm{B} \text { का } 2 \%=\frac{2}{100} \times \mathrm{B}=0.02 \times \mathrm{B} \\
&=0.02\left[\begin{array}{ccc}
\text { बासमती } & \text { परमल } & \text { नउरा } \\
5000 & 10,000 & 6000 \\
20,000 & 10,000 & 10,000
\end{array}\right] \begin{array}{cc}
\text { रामकिशन } \\
\text { गुरुचरण सिंह }
\end{array} \\
&=\left[\begin{array}{ccc}
\text { बासमती } & \text { परमल } & \text { नउरा } \\
100 & 200 & 120 \\
400 & 200 & 200
\end{array}\right] \text { रामकिशन } \\
& \text { गुरुचरण सिंह }
\end{aligned}
$$

अतः अक्तूबर माह में, रामकिशन, प्रत्येक प्रकार के चावल की बिक्री पर क्रमशः ₹ $100$, ₹200, तथा ₹120 लाभ प्राप्त करता है और गुरचरन सिंह, प्रत्येक प्रकार के चावल की बिक्री पर क्रमशः ₹ $400$, ₹ $200$ तथा ₹ $200$ लाभ अर्जित करता है।
:::

:::

:::

:::example{number="3.12" kind="example" id="ex_3.12" topic="Multiplication of matrices"}
#### उदाहरण 3.12

:::prompt
यदि $\mathrm{A}=\left[\begin{array}{ll}6 & 9 \\ 2 & 3\end{array}\right]$ तथा $\mathrm{B}=\left[\begin{array}{lll}2 & 6 & 0 \\ 7 & 9 & 8\end{array}\right]$ है तो AB ज्ञात कीजिए।
:::

:::solution{label="हल"}
आव्यूह A में $2$ स्तंभ हैं जो आव्यूह B की पंक्तियों के समान हैं। अतएव AB परिभाषित है। अब

$$
\begin{aligned}
A B & =\left[\begin{array}{lll}
6(2)+9(7) & 6(6)+9(9) & 6(0)+9(8) \\
2(2)+3(7) & 2(6)+3(9) & 2(0)+3(8)
\end{array}\right] \\
& =\left[\begin{array}{rrr}
12+63 & 36+81 & 0+72 \\
4+21 & 12+27 & 0+24
\end{array}\right]=\left[\begin{array}{ccc}
75 & 117 & 72 \\
25 & 39 & 24
\end{array}\right]
\end{aligned}
$$
:::

:::answer
**उत्तर:** $\mathrm{AB}=\left[\begin{array}{ccc}75 & 117 & 72 \\ 25 & 39 & 24\end{array}\right]$
:::

:::

:::example{number="3.13" kind="example" id="ex_3.13" topic="आव्यूह गुणन में क्रम-विनिमेयता का अभाव"}
#### उदाहरण 3.13

:::prompt
यदि $\mathrm{A}=\left[\begin{array}{rrr}1 & -2 & 3 \\ -4 & 2 & 5\end{array}\right]$ और $\mathrm{B}=\left[\begin{array}{ll}2 & 3 \\ 4 & 5 \\ 2 & 1\end{array}\right]$, तो AB तथा BA ज्ञात कीजिए। दर्शाइए कि $\mathrm{AB} \neq \mathrm{BA}$
:::

:::solution{label="हल"}
हल क्योंकि कि A एक $2 \times 3$ आव्यूह है और B एक $3 \times 2$ आव्यूह है, इसलिए AB तथा BA दोनों ही परिभाषित हैं तथा क्रमशः $2 \times 2$ तथा $3 \times 3$, कोटियों के आव्यूह हैं। नोट कीजिए कि

$$
\mathrm{AB}=\left[\begin{array}{rrr}
1 & -2 & 3 \\
-4 & 2 & 5
\end{array}\right]\left[\begin{array}{ll}
2 & 3 \\
4 & 5 \\
2 & 1
\end{array}\right]=\left[\begin{array}{cc}
2-8+6 & 3-10+3 \\
-8+8+10 & -12+10+5
\end{array}\right]=\left[\begin{array}{cr}
0 & -4 \\
10 & 3
\end{array}\right]
$$

और

$$
\mathrm{BA}=\left[\begin{array}{ll}
2 & 3 \\
4 & 5 \\
2 & 1
\end{array}\right]\left[\begin{array}{rrr}
1 & -2 & 3 \\
-4 & 2 & 5
\end{array}\right]=\left[\begin{array}{ccc}
2-12 & -4+6 & 6+15 \\
4-20 & -8+10 & 12+25 \\
2-4 & -4+2 & 6+5
\end{array}\right]=\left[\begin{array}{ccc}
-10 & 2 & 21 \\
-16 & 2 & 37 \\
-2 & -2 & 11
\end{array}\right]
$$

स्पष्टतया $\mathrm{AB} \neq \mathrm{BA}$.
:::

:::

:::example{number="3.14" kind="example" id="ex_3.14" topic="AB ≠ BA का एक और उदाहरण"}
#### उदाहरण 3.14

:::prompt
यदि $\mathrm{A}=\left[\begin{array}{rr}1 & 0 \\ 0 & -1\end{array}\right]$ तथा $\mathrm{B}=\left[\begin{array}{ll}0 & 1 \\ 1 & 0\end{array}\right]$ है तो $\mathrm{AB}=\left[\begin{array}{rr}0 & 1 \\ -1 & 0\end{array}\right]$
:::

:::solution{label="हल"}
और

$$
\mathrm{BA}=\left[\begin{array}{rr}
0 & -1 \\
1 & 0
\end{array}\right] \text { है। स्पष्टतया } \mathrm{AB} \neq \mathrm{BA} \text { है। }
$$

अतः आव्यूह गुणन क्रम-विनिमेय नहीं होता है।
:::

:::

:::example{number="3.15" kind="example" id="ex_3.15" topic="दो शून्येतर आव्यूहों का गुणनफल शून्य आव्यूह"}
#### उदाहरण 3.15

:::prompt
यदि $\mathrm{A}=\left[\begin{array}{rr}0 & -1 \\ 0 & 2\end{array}\right]$ तथा $\mathrm{B}=\left[\begin{array}{ll}3 & 5 \\ 0 & 0\end{array}\right]$ है तो AB का मान ज्ञात कीजिए
:::

:::solution{label="हल"}
हल यहाँ पर $\mathrm{AB}=\left[\begin{array}{rr}0 & -1 \\ 0 & 2\end{array}\right]\left[\begin{array}{ll}3 & 5 \\ 0 & 0\end{array}\right]=\left[\begin{array}{ll}0 & 0 \\ 0 & 0\end{array}\right]$

अतः यदि दो आव्यूहों का गुणनफल एक शून्य आव्यूह है तो आवश्यक नहीं है कि उनमें से एक आव्यूह अनिवार्यतः शून्य आव्यूह हो।
:::

:::

:::example{number="3.16" kind="example" id="ex_3.16" topic="आव्यूह गुणन की साहचर्यता का सत्यापन"}
#### उदाहरण 3.16

:::prompt
यदि $\mathrm{A}=\left[\begin{array}{ccc}1 & 1 & -1 \\ 2 & 0 & 3 \\ 3 & -1 & 2\end{array}\right], \mathrm{B}=\left[\begin{array}{cc}1 & 3 \\ 0 & 2 \\ -1 & 4\end{array}\right]$ तथा $\mathrm{C}=\left[\begin{array}{cccc}1 & 2 & 3 & -4 \\ 2 & 0 & -2 & 1\end{array}\right]$ तो $\mathrm{A}(\mathrm{BC})$ तथा $(\mathrm{AB}) \mathrm{C}$ ज्ञात कीजिए और दिखलाइए कि $(\mathrm{AB}) \mathrm{C}=\mathrm{A}(\mathrm{BC})$ है।
:::

:::solution{label="हल"}
हल यहाँ $\mathrm{AB}=\left[\begin{array}{rcr}1 & 1 & -1 \\ 2 & 0 & 3 \\ 3 & -1 & 2\end{array}\right]\left[\begin{array}{rr}1 & 3 \\ 0 & 2 \\ -1 & 4\end{array}\right]=\left[\begin{array}{ll}1+0+1 & 3+2-4 \\ 2+0-3 & 6+0+12 \\ 3+0-2 & 9-2+8\end{array}\right]=\left[\begin{array}{rc}2 & 1 \\ -1 & 18 \\ 1 & 15\end{array}\right]$

$$
\text { (AB) (C) } \begin{aligned}
& =\left[\begin{array}{rc}
2 & 1 \\
-1 & 18 \\
1 & 15
\end{array}\right]\left[\begin{array}{rrrr}
1 & 2 & 3 & -4 \\
2 & 0 & -2 & 1
\end{array}\right]=\left[\begin{array}{rrr}
2+2 & 4+0 & 6-2 \\
-1+36 & -2+0 & -3-36 \\
1+30 & 2+0 & 3-30 \\
-4+18
\end{array}\right] \\
& =\left[\begin{array}{cccc}
4 & 4 & 4 & -7 \\
35 & -2 & -39 & 22 \\
31 & 2 & -27 & 11
\end{array}\right]
\end{aligned}
$$

अब
$$
\begin{aligned}
\mathrm{BC} & =\left[\begin{array}{rr}
1 & 3 \\
0 & 2 \\
-1 & 4
\end{array}\right]\left[\begin{array}{rrrr}
1 & 2 & 3 & -4 \\
2 & 0 & -2 & 1
\end{array}\right]=\left[\begin{array}{rrrr}
1+6 & 2+0 & 3-6 & -4+3 \\
0+4 & 0+0 & 0-4 & 0+2 \\
-1+8 & -2+0 & -3-8 & 4+4
\end{array}\right] \\
& =\left[\begin{array}{rrrr}
7 & 2 & -3 & -1 \\
4 & 0 & -4 & 2 \\
7 & -2 & -11 & 8
\end{array}\right]
\end{aligned}
$$

अतएव

$$
\begin{aligned}
A(B C) & =\left[\begin{array}{rrr}
1 & 1 & -1 \\
2 & 0 & 3 \\
3 & -1 & 2
\end{array}\right]\left[\begin{array}{cccc}
7 & 2 & -3 & -1 \\
4 & 0 & -4 & 2 \\
7 & -2 & -11 & 8
\end{array}\right] \\
& =\left[\begin{array}{cccc}
7+4-7 & 2+0+2 & -3-4+11 & -1+2-8 \\
14+0+21 & 4+0-6 & -6+0-33 & -2+0+24 \\
21-4+14 & 6+0-4 & -9+4-22 & -3-2+16
\end{array}\right] \\
& =\left[\begin{array}{crcc}
4 & 4 & 4 & -7 \\
35 & -2 & -39 & 22 \\
31 & 2 & -27 & 11
\end{array}\right]
\end{aligned}
$$

स्पष्टतया, (AB) $\mathrm{C}=\mathrm{A}(\mathrm{BC})$
:::

:::

:::example{number="3.17" kind="example" id="ex_3.17" topic="आव्यूह गुणन के वितरण नियम का सत्यापन"}
#### उदाहरण 3.17

:::prompt
यदि $\mathrm{A}=\left[\begin{array}{rrr}0 & 6 & 7 \\ -6 & 0 & 8 \\ 7 & -8 & 0\end{array}\right], \mathrm{B}=\left[\begin{array}{lll}0 & 1 & 1 \\ 1 & 0 & 2 \\ 1 & 2 & 0\end{array}\right], \mathrm{C}=\left[\begin{array}{r}2 \\ -2 \\ 3\end{array}\right]$
तो $\mathrm{AC}, \mathrm{BC}$ तथा $(\mathrm{A}+\mathrm{B}) \mathrm{C}$ का परिकलन कीजिए। यह भी सत्यापित कीजिए कि $(\mathrm{A}+\mathrm{B}) \mathrm{C}=\mathrm{AC}+\mathrm{BC}$
:::

:::solution{label="हल"}
हल $\mathrm{A}+\mathrm{B}=\left[\begin{array}{ccc}0 & 7 & 8 \\ -5 & 0 & 10 \\ 8 & -6 & 0\end{array}\right]$

अतएव,

$$
(A+B) C=\left[\begin{array}{rrc}
0 & 7 & 8 \\
-5 & 0 & 10 \\
8 & -6 & 0
\end{array}\right]\left[\begin{array}{r}
2 \\
-2 \\
3
\end{array}\right]=\left[\begin{array}{r}
0-14+24 \\
-10+0+30 \\
16+12+0
\end{array}\right]=\left[\begin{array}{l}
10 \\
20 \\
28
\end{array}\right]
$$

इसके अतिरिक्त

$$
\mathrm{AC}=\left[\begin{array}{ccc}
0 & 6 & 7 \\
-6 & 0 & 8 \\
7 & -8 & 0
\end{array}\right]\left[\begin{array}{r}
2 \\
-2 \\
3
\end{array}\right]=\left[\begin{array}{r}
0-12+21 \\
-12+0+24 \\
14+16+0
\end{array}\right]=\left[\begin{array}{c}
9 \\
12 \\
30
\end{array}\right]
$$

और

$$
\mathrm{BC}=\left[\begin{array}{lll}
0 & 1 & 1 \\
1 & 0 & 2 \\
1 & 2 & 0
\end{array}\right]\left[\begin{array}{r}
2 \\
-2 \\
3
\end{array}\right]=\left[\begin{array}{l}
0-2+3 \\
2+0+6 \\
2-4+0
\end{array}\right]=\left[\begin{array}{c}
1 \\
8 \\
-2
\end{array}\right]
$$

इसलिए

$$
A C+B C=\left[\begin{array}{l}
9 \\
12 \\
30
\end{array}\right]+\left[\begin{array}{r}
1 \\
8 \\
-2
\end{array}\right]=\left[\begin{array}{l}
10 \\
20 \\
28
\end{array}\right]
$$

स्पष्टतया

$$
(\mathrm{A}+\mathrm{B}) \mathrm{C}=\mathrm{AC}+\mathrm{BC}
$$
:::

:::

:::example{number="3.18" kind="example" id="ex_3.18" topic="आव्यूह बहुपद A³-23A-40I=O का सत्यापन"}
#### उदाहरण 3.18

:::prompt
यदि $\mathrm{A}=\left[\begin{array}{rrr}1 & 2 & 3 \\ 3 & -2 & 1 \\ 4 & 2 & 1\end{array}\right]$ है तो दर्शाइए कि $\mathrm{A}^{3}-23 \mathrm{~A}-40 \mathrm{I}=\mathrm{O}$
:::

:::solution{label="हल"}
हल हम जानते हैं कि $\mathrm{A}^{2}=\mathrm{A} . \mathrm{A}=\left[\begin{array}{rrr}1 & 2 & 3 \\ 3 & -2 & 1 \\ 4 & 2 & 1\end{array}\right]\left[\begin{array}{rrr}1 & 2 & 3 \\ 3 & -2 & 1 \\ 4 & 2 & 1\end{array}\right]=\left[\begin{array}{lll}19 & 4 & 8 \\ 1 & 12 & 8 \\ 14 & 6 & 15\end{array}\right]$
इसलिए

$$
A^{3}=A A^{2}=\left[\begin{array}{ccc}
1 & 2 & 3 \\
3 & -2 & 1 \\
4 & 2 & 1
\end{array}\right]\left[\begin{array}{llr}
19 & 4 & 8 \\
1 & 12 & 8 \\
14 & 6 & 15
\end{array}\right]=\left[\begin{array}{ccc}
63 & 46 & 69 \\
69 & -6 & 23 \\
92 & 46 & 63
\end{array}\right]
$$

अब $\mathrm{A}^{3}-23 \mathrm{~A}-40 \mathrm{I}=\left[\begin{array}{rrr}63 & 46 & 69 \\ 69 & -6 & 23 \\ 92 & 46 & 63\end{array}\right]-23\left[\begin{array}{rrr}1 & 2 & 3 \\ 3 & -2 & 1 \\ 4 & 2 & 1\end{array}\right]-40\left[\begin{array}{lll}1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1\end{array}\right]$

$$
\begin{aligned}
& =\left[\begin{array}{ccc}
63 & 46 & 69 \\
69 & -6 & 23 \\
92 & 46 & 63
\end{array}\right]+\left[\begin{array}{ccc}
-23 & -46 & -69 \\
-69 & 46 & -23 \\
-92 & -46 & -23
\end{array}\right]+\left[\begin{array}{ccc}
-40 & 0 & 0 \\
0 & -40 & 0 \\
0 & 0 & -40
\end{array}\right] \\
& =\left[\begin{array}{ccc}
63-23-40 & 46-46+0 & 69-69+0 \\
69-69+0 & -6+46-40 & 23-23+0 \\
92-92+0 & 46-46+0 & 63-23-40
\end{array}\right]=\left[\begin{array}{ccc}
0 & 0 & 0 \\
0 & 0 & 0 \\
0 & 0 & 0
\end{array}\right]=\mathrm{O}
\end{aligned}
$$
:::

:::

:::example{number="3.19" kind="example" id="ex_3.19" topic="चुनाव प्रचार व्यय — आव्यूह गुणन का अनुप्रयोग"}
#### उदाहरण 3.19

:::prompt
किसी विधान सभा चुनाव के दौरान एक राजनैतिक दल ने अपने उम्मीदवार के प्रचार हेतु एक जन संपर्क फर्म को ठेके पर अनुबंद्धित किया। प्रचार हेतु तीन विधियों द्वारा संपर्क स्थापित करना निश्चित हुआ। ये हैं: टेलीफोन द्वारा, घर-घर जाकर तथा पर्चा वितरण द्वारा। प्रत्येक संपर्क का शुल्क (पैसों में) नीचे आव्यूह A में व्यक्त है,

$$
\begin{aligned}
& \text { प्रति संपर्क मूल्य } \\
& \mathrm{A}=\left[\begin{array}{c}
40 \\
100 \\
50
\end{array}\right] \begin{array}{c}
\text { टेलीफोन द्वारा } \\
\text { घर जाकर } \\
\text { पर्चा द्वारा }
\end{array}
\end{aligned}
$$

$X$ तथा $Y$ दो शहरों में, प्रत्येक प्रकार के सम्पर्कों की संख्या आव्यूह
टेलीफोन घर जाकर पर्चा द्वारा
$B=\left[\begin{array}{ccc}1000 & 500 & 5000 \\ 3000 & 1000 & 10,000\end{array}\right] \rightarrow X$ में व्यक्त है। $X$ तथा $Y$ शहरों में राजनैतिक दल द्वारा व्यय की गई कुल धनराशि ज्ञात कीजिए।
:::

:::solution{label="हल"}
हल यहाँ पर

$$
\begin{aligned}
\mathrm{BA} & =\left[\begin{array}{c}
40,000+50,000+250,000 \\
120,000+100,000+500,000
\end{array}\right] \rightarrow \mathrm{X} \\
& =\left[\begin{array}{c}
340,000 \\
720,000
\end{array}\right] \rightarrow \mathrm{X}
\end{aligned}
$$
:::

:::answer
**उत्तर:** अतः दल द्वारा दोनों शहरों में व्यय की गई कुल धनराशि क्रमशः $3,40,000$ पैसे व $7,20,000$ पैसे अर्थात् Rs $3400$ तथा Rs $7200$ हैं।
:::

:::

:::example{number="3.20" kind="example" id="ex_3.20" topic="आव्यूह परिवर्त के गुणधर्मों का सत्यापन"}
#### उदाहरण 3.20

:::prompt
यदि $\mathrm{A}=\left[\begin{array}{lll}3 & \sqrt{3} & 2 \\ 4 & 2 & 0\end{array}\right]$ तथा $\mathrm{B}=\left[\begin{array}{rrr}2 & -1 & 2 \\ 1 & 2 & 4\end{array}\right]$ तो निम्नलिखित को सत्यापित कीजिए:
:::

:::part{label="(i)"}
:::prompt
$\left(\mathrm{A}^{\prime}\right)^{\prime}=\mathrm{A}$
:::

:::solution
यहाँ
$$
A=\left[\begin{array}{lll}
3 & \sqrt{3} & 2 \\
4 & 2 & 0
\end{array}\right] \Rightarrow A^{\prime}=\left[\begin{array}{cc}
3 & 4 \\
\sqrt{3} & 2 \\
2 & 0
\end{array}\right] \Rightarrow\left(A^{\prime}\right)^{\prime}=\left[\begin{array}{ccc}
3 & \sqrt{3} & 2 \\
4 & 2 & 0
\end{array}\right]=A
$$
अत: $\left(\mathrm{A}^{\prime}\right)^{\prime}=\mathrm{A}$
:::

:::

:::part{label="(ii)"}
:::prompt
$(\mathrm{A}+\mathrm{B})^{\prime}=\mathrm{A}^{\prime}+\mathrm{B}^{\prime}$
:::

:::solution
यहाँ
$$
\mathrm{A}=\left[\begin{array}{lll}
3 & \sqrt{3} & 2 \\
4 & 2 & 0
\end{array}\right], \mathrm{B}=\left[\begin{array}{rrr}
2 & -1 & 2 \\
1 & 2 & 4
\end{array}\right] \Rightarrow \mathrm{A}+\mathrm{B}=\left[\begin{array}{ccc}
5 & \sqrt{3}-1 & 4 \\
5 & 4 & 4
\end{array}\right]
$$
अतएव
$$
(\mathrm{A}+\mathrm{B})^{\prime}=\left[\begin{array}{cc}
5 & 5 \\
\sqrt{3}-1 & 4 \\
4 & 4
\end{array}\right]
$$
अब
$$
\mathrm{A}^{\prime}=\left[\begin{array}{ll}
3 & 4 \\
\sqrt{3} & 2 \\
2 & 0
\end{array}\right], \mathrm{B}^{\prime}=\left[\begin{array}{rr}
2 & 1 \\
-1 & 2 \\
2 & 4
\end{array}\right]
$$
अतएव
$$
\mathrm{A}^{\prime}+\mathrm{B}^{\prime}=\left[\begin{array}{cr}
5 & 5 \\
\sqrt{3}-1 & 4 \\
4 & 4
\end{array}\right]
$$
अत:
$$
(\mathrm{A}+\mathrm{B})^{\prime}=\mathrm{A}^{\prime}+\mathrm{B}^{\prime}
$$
:::

:::

:::part{label="(iii)"}
:::prompt
$(k \mathrm{~B})^{\prime}=k \mathrm{~B}^{\prime}$, जहाँ $k$ कोई अचर है।
:::

:::solution
यहाँ
$$
k \mathrm{~B}=k\left[\begin{array}{rrr}
2 & -1 & 2 \\
1 & 2 & 4
\end{array}\right]=\left[\begin{array}{lll}
2 k & -k & 2 k \\
k & 2 k & 4 k
\end{array}\right]
$$
तब
$$
(k \mathrm{~B})^{\prime}=\left[\begin{array}{cc}
2 k & k \\
-k & 2 k \\
2 k & 4 k
\end{array}\right]=k\left[\begin{array}{rc}
2 & 1 \\
-1 & 2 \\
2 & 4
\end{array}\right]=k \mathrm{~B}^{\prime}
$$
अत:
$$
(k \mathrm{~B})^{\prime}=k \mathrm{~B}^{\prime}
$$
:::

:::

:::

:::example{number="3.21" kind="example" id="ex_3.21" topic="(AB)' = B'A' का सत्यापन"}
#### उदाहरण 3.21

:::prompt
यदि $\mathrm{A}=\left[\begin{array}{r}-2 \\ 4 \\ 5\end{array}\right], \mathrm{B}=\left[\begin{array}{lll}1 & 3 & -6\end{array}\right]$ है तो सत्यापित कीजिए $(\mathrm{AB})^{\prime}=\mathrm{B}^{\prime} \mathrm{A}^{\prime}$ है।
:::

:::solution{label="हल"}
हल यहाँ

$$
\mathrm{A}=\left[\begin{array}{r}
-2 \\
4 \\
5
\end{array}\right], \mathrm{B}=\left[\begin{array}{lll}
1 & 3 & -6
\end{array}\right]
$$

इसलिए

$$
A B=\left[\begin{array}{r}
-2 \\
4 \\
5
\end{array}\right]\left[\begin{array}{lll}
1 & 3 & -6
\end{array}\right]=\left[\begin{array}{ccc}
-2 & -6 & 12 \\
4 & 12 & -24 \\
5 & 15 & -30
\end{array}\right]
$$

अत:

$$
(\mathrm{AB})^{\prime}=\left[\begin{array}{ccc}
-2 & 4 & 5 \\
-6 & 12 & 15 \\
12 & -24 & -30
\end{array}\right]
$$

अब

$$
A^{\prime}=\left[\begin{array}{lll}
-2 & 4 & 5
\end{array}\right], B^{\prime}=\left[\begin{array}{r}
1 \\
3 \\
-6
\end{array}\right]
$$

इसलिए

$$
\mathrm{B}^{\prime} \mathrm{A}^{\prime}=\left[\begin{array}{r}
1 \\
3 \\
-6
\end{array}\right]\left[\begin{array}{lll}
-2 & 4 & 5
\end{array}\right]=\left[\begin{array}{ccc}
-2 & 4 & 5 \\
-6 & 12 & 15 \\
12 & -24 & -30
\end{array}\right]=(\mathrm{AB})^{\prime}
$$

स्पष्टतया

$$
(\mathrm{AB})^{\prime}=\mathrm{B}^{\prime} \mathrm{A}^{\prime}
$$
:::

:::

:::example{number="3.22" kind="example" id="ex_3.22" topic="आव्यूह को सममित व विषम सममित के योग में व्यक्त करना"}
#### उदाहरण 3.22

:::prompt
आव्यूह $\mathrm{B}=\left[\begin{array}{rrr}2 & -2 & -4 \\ -1 & 3 & 4 \\ 1 & -2 & -3\end{array}\right]$ को एक सममित आव्यूह तथा एक विषम सममित आव्यूह के योगफल के रूप में व्यक्त कीजिए।
:::

:::solution{label="हल"}
हल यहाँ $\mathrm{B}^{\prime}=\left[\begin{array}{rrr}2 & -1 & 1 \\ -2 & 3 & -2 \\ -4 & 4 & -3\end{array}\right]$

मान लीजिए कि

$$
\mathrm{P}=\frac{1}{2}\left(\mathrm{~B}+\mathrm{B}^{\prime}\right)=\frac{1}{2}\left[\begin{array}{ccc}
4 & -3 & -3 \\
-3 & 6 & 2 \\
-3 & 2 & -6
\end{array}\right]=\left[\begin{array}{ccc}
2 & \frac{-3}{2} & \frac{-3}{2} \\
\frac{-3}{2} & 3 & 1 \\
\frac{-3}{2} & 1 & -3
\end{array}\right] \text { है। }
$$

अब

$$
P^{\prime}=\left[\begin{array}{ccc}
2 & \frac{-3}{2} & \frac{-3}{2} \\
\frac{-3}{2} & 3 & 1 \\
\frac{-3}{2} & 1 & -3
\end{array}\right]=P
$$

अत:

$$
\mathrm{P}=\frac{1}{2}\left(\mathrm{~B}+\mathrm{B}^{\prime}\right) \text { एक सममित आव्यूह है। }
$$

साथ ही मान लीजिए $\mathrm{Q}=\frac{1}{2}\left(\mathrm{~B}-\mathrm{B}^{\prime}\right)=\frac{1}{2}\left[\begin{array}{rrr}0 & -1 & -5 \\ 1 & 0 & 6 \\ 5 & -6 & 0\end{array}\right]=\left[\begin{array}{ccc}0 & \frac{-1}{2} & \frac{-5}{2} \\ \frac{1}{2} & 0 & 3 \\ \frac{5}{2} & -3 & 0\end{array}\right]$ है।

तब

$$
Q^{\prime}=\left[\begin{array}{ccc}
0 & \frac{1}{2} & \frac{5}{3} \\
\frac{-1}{2} & 0 & -3 \\
\frac{-5}{2} & 3 & 0
\end{array}\right]=-Q
$$

अत:

$$
\mathrm{Q}=\frac{1}{2}\left(\mathrm{~B}-\mathrm{B}^{\prime}\right) \text { एक विषम सममित आव्यूह है। }
$$

अब

$$
\mathrm{P}+\mathrm{Q}=\left[\begin{array}{ccc}
2 & \frac{-3}{2} & \frac{-3}{2} \\
\frac{-3}{2} & 3 & 1 \\
\frac{-3}{2} & 1 & -3
\end{array}\right]+\left[\begin{array}{ccc}
0 & \frac{-1}{2} & \frac{-5}{2} \\
\frac{1}{2} & 0 & 3 \\
\frac{5}{2} & -3 & 0
\end{array}\right]=\left[\begin{array}{rrr}
2 & -2 & -4 \\
-1 & 3 & 4 \\
1 & -2 & -3
\end{array}\right]=\mathrm{B}
$$
:::

:::answer
**उत्तर:** अतः आव्यूह B एक सममित आव्यूह तथा एक विषम सममित आव्यूह के योगफल के रूप में व्यक्त किया गया, जहाँ $\mathrm{P}=\left[\begin{array}{ccc}2 & \frac{-3}{2} & \frac{-3}{2} \\ \frac{-3}{2} & 3 & 1 \\ \frac{-3}{2} & 1 & -3\end{array}\right]$ सममित तथा $\mathrm{Q}=\left[\begin{array}{ccc}0 & \frac{-1}{2} & \frac{-5}{2} \\ \frac{1}{2} & 0 & 3 \\ \frac{5}{2} & -3 & 0\end{array}\right]$ विषम सममित है।
:::

:::

:::example{number="3.23" kind="example" id="ex_3.23" topic="सममित आव्यूहों के गुणनफल की सममिति की शर्त"}
#### उदाहरण 3.23

:::prompt
यदि A तथा B समान कोटि के सममित आव्यूह हैं तो दर्शाइए कि AB सममित है, यदि और केवल यदि A तथा B क्रमविनिमेय है, अर्थात् $\mathrm{AB}=\mathrm{BA}$ है।
:::

:::solution{label="हल"}
हल दिया है कि A तथा B दोनों सममित आव्यूह हैं, इसलिए $\mathrm{A}^{\prime}=\mathrm{A}$ तथा $\mathrm{B}^{\prime}=\mathrm{B}$ है। मान लीजिए कि AB सममित है तो $(\mathrm{AB})^{\prime}=\mathrm{AB}$
किंतु

$$
(\mathrm{AB})^{\prime}=\mathrm{B}^{\prime} \mathrm{A}^{\prime}=\mathrm{BA} \text { (क्यों?) }
$$

अत:

$$
\mathrm{BA}=\mathrm{AB}
$$

विलोमतः, यदि $\mathrm{AB}=\mathrm{BA}$ है तो हम सिद्ध करेंगे कि AB सममित है।
अब

$$
\begin{aligned}
(\mathrm{AB})^{\prime} & =\mathrm{B}^{\prime} \mathrm{A}^{\prime} \\
& =\mathrm{B} \mathrm{~A} \text { (क्योंकि } \mathrm{A} \text { तथा } \mathrm{B} \text { सममित हैं ) } \\
& =\mathrm{AB}
\end{aligned}
$$

अत: AB सममित है।
:::

:::

:::example{number="3.24" kind="example" id="ex_3.24" topic="आव्यूह समीकरण CD-AB=O से D ज्ञात करना"}
#### उदाहरण 3.24

:::prompt
मान लीजिए कि $\mathrm{A}=\left[\begin{array}{rr}2 & -1 \\ 3 & 4\end{array}\right], \mathrm{B}=\left[\begin{array}{ll}5 & 2 \\ 7 & 4\end{array}\right], \mathrm{C}=\left[\begin{array}{ll}2 & 5 \\ 3 & 8\end{array}\right]$ है। एक ऐसा आव्यूह D ज्ञात कीजिए कि $\mathrm{CD}-\mathrm{AB}=\mathrm{O}$ हो।
:::

:::solution{label="हल"}
हल क्योंकि A, B, C सभी कोटि 2, के वर्ग आव्यूह हैं और $\mathrm{CD}-\mathrm{AB}$ भली-भाँति परिभाषित है, इसलिए D कोटि $2$ का एक वर्ग आव्यूह होना चाहिए।
मान लीजिए कि $\mathrm{D}=\left[\begin{array}{ll}a & b \\ c & d\end{array}\right]$ है। तब $\mathrm{CD}-\mathrm{AB}=\mathrm{O}$ से प्राप्त होता है कि

$$
\left[\begin{array}{ll}
2 & 5 \\
3 & 8
\end{array}\right]\left[\begin{array}{ll}
a & b \\
c & d
\end{array}\right]-\left[\begin{array}{rr}
2 & -1 \\
3 & 4
\end{array}\right]\left[\begin{array}{ll}
5 & 2 \\
7 & 4
\end{array}\right]=\mathrm{O}
$$

या

$$
\left[\begin{array}{ll}
2 a+5 c & 2 b+5 d \\
3 a+8 c & 3 b+8 d
\end{array}\right]-\left[\begin{array}{ll}
3 & 0 \\
43 & 22
\end{array}\right]=\left[\begin{array}{ll}
0 & 0 \\
0 & 0
\end{array}\right]
$$

या

$$
\left[\begin{array}{cc}
2 a+5 c-3 & 2 b+5 d \\
3 a+8 c-43 & 3 b+8 d-22
\end{array}\right]=\left[\begin{array}{ll}
0 & 0 \\
0 & 0
\end{array}\right]
$$

आव्यूहों की समानता से हमें निम्नलिखित समीकरण प्राप्त होते हैं:

$$
\begin{aligned}
& 2 a+5 c-3=0 \\
& 3 a+8 c-43=0 \\
& 2 b+5 d=0
\end{aligned}
$$

तथा

$$
3 b+8 d-22=0
$$

(1) तथा (2), को सरल करने पर $a=-191, c=77$ प्राप्त होता है।
(3) तथा (4), को सरल करने पर $b=-110, d=44$ प्राप्त होता है।
:::

:::answer
**उत्तर:** अत:
$$
\mathrm{D}=\left[\begin{array}{ll}
a & b \\
c & d
\end{array}\right]=\left[\begin{array}{cc}
-191 & -110 \\
77 & 44
\end{array}\right]
$$
:::

:::
