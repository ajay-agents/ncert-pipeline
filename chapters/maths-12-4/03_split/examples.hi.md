---
subject: maths
class: 12
chapter: 4
lang: hi
title: "सारणिक"
---

# सारणिक

## उदाहरण

:::example{number="4.1" kind="example" id="ex_4.1" topic="Value of a 2x2 determinant"}
#### उदाहरण 4.1

:::prompt
$\left|\begin{array}{cc}2 & 4 \\ -1 & 2\end{array}\right|$ का मान ज्ञात कीजिए।
:::

:::solution{label="हल"}
$\left|\begin{array}{cc}2 & 4 \\ -1 & 2\end{array}\right|=2(2)-4(-1)=4+4=8$
:::

:::answer
**उत्तर:** $8$
:::

:::

:::example{number="4.2" kind="example" id="ex_4.2" topic="Value of a symbolic 2x2 determinant"}
#### उदाहरण 4.2

:::prompt
$\left|\begin{array}{cc}x & x+1 \\ x-1 & x\end{array}\right|$ का मान ज्ञात कीजिए।
:::

:::solution{label="हल"}
$\left|\begin{array}{cc}x & x+1 \\ x-1 & x\end{array}\right|=x(x)-(x+1)(x-1)=x^{2}-\left(x^{2}-1\right)=x^{2}-x^{2}+1=1$
:::

:::answer
**उत्तर:** $1$
:::

:::

:::example{number="4.3" kind="example" id="ex_4.3" topic="3x3 determinant via column expansion"}
#### उदाहरण 4.3

:::prompt
सारणिक $\Delta=\left|\begin{array}{rrr}1 & 2 & 4 \\ -1 & 3 & 0 \\ 4 & 1 & 0\end{array}\right|$ का मान ज्ञात कीजिए।
:::

:::solution{label="हल"}
ध्यान दीजिए कि तीसरे स्तंभ में दो प्रविष्टियाँ शून्य हैं। इसलिए तीसरे स्तंभ $\left(\mathrm{C}_{3}\right)$ के अनुदिश प्रसरण करने पर हमें प्राप्त होता है कि

$$
\begin{aligned}
\Delta & =4\left|\begin{array}{cc}
-1 & 3 \\
4 & 1
\end{array}\right|-0\left|\begin{array}{ll}
1 & 2 \\
4 & 1
\end{array}\right|+0\left|\begin{array}{cc}
1 & 2 \\
-1 & 3
\end{array}\right| \\
& =4(-1-12)-0+0=-52
\end{aligned}
$$
:::

:::answer
**उत्तर:** $-52$
:::

:::

:::example{number="4.4" kind="example" id="ex_4.4" topic="Determinant of a skew-symmetric-like trig matrix"}
#### उदाहरण 4.4

:::prompt
$\Delta=\left|\begin{array}{ccc}0 & \sin \alpha & -\cos \alpha \\ -\sin \alpha & 0 & \sin \beta \\ \cos \alpha & -\sin \beta & 0\end{array}\right|$ का मान ज्ञात कीजिए।
:::

:::solution{label="हल"}
$\mathrm{R}_{1}$ के अनुदिश प्रसरण करने पर हमें प्राप्त होता है कि

$$
\begin{aligned}
\Delta & =0\left|\begin{array}{cc}
0 & \sin \beta \\
-\sin \beta & 0
\end{array}\right|-\sin \alpha\left|\begin{array}{cc}
-\sin \alpha & \sin \beta \\
\cos \alpha & 0
\end{array}\right|-\cos \alpha\left|\begin{array}{cc}
-\sin \alpha & 0 \\
\cos \alpha & -\sin \beta
\end{array}\right| \\
& =0-\sin \alpha(0-\sin \beta \cos \alpha)-\cos \alpha(\sin \alpha \sin \beta-0) \\
& =\sin \alpha \sin \beta \cos \alpha-\cos \alpha \sin \alpha \sin \beta=0
\end{aligned}
$$
:::

:::answer
**उत्तर:** $0$
:::

:::

:::example{number="4.5" kind="example" id="ex_4.5" topic="Solving for x from equal determinants"}
#### उदाहरण 4.5

:::prompt
यदि $\left|\begin{array}{ll}3 & x \\ x & 1\end{array}\right|=\left|\begin{array}{ll}3 & 2 \\ 4 & 1\end{array}\right|$ तो $x$ के मान ज्ञात कीजिए।
:::

:::solution{label="हल"}
दिया है कि $\left|\begin{array}{ll}3 & x \\ x & 1\end{array}\right|=\left|\begin{array}{ll}3 & 2 \\ 4 & 1\end{array}\right|$
अर्थात्
अर्थात्
अत:

$$
\begin{aligned}
3-x^{2} & =3-8 \\
x^{2} & =8 \\
x & = \pm 2 \sqrt{2}
\end{aligned}
$$
:::

:::answer
**उत्तर:** $x= \pm 2 \sqrt{2}$
:::

:::

:::example{number="4.6" kind="example" id="ex_4.6" topic="Area of a triangle using determinants"}
#### उदाहरण 4.6

:::prompt
एक त्रिभुज का क्षेत्रफल ज्ञात कीजिए जिसके शीर्ष $(3,8),(-4,2)$ और $(5,1)$ हैं।
:::

:::solution{label="हल"}
त्रिभुज का क्षेत्रफल:

$$
\begin{aligned}
\Delta & =\frac{1}{2}\left|\begin{array}{rrr}
3 & 8 & 1 \\
-4 & 2 & 1 \\
5 & 1 & 1
\end{array}\right|=\frac{1}{2}[3(2-1)-8(-4-5)+1(-4-10)] \\
& =\frac{1}{2}(3+72-14)=\frac{61}{2}
\end{aligned}
$$
:::

:::answer
**उत्तर:** $\frac{61}{2}$
:::

:::

:::example{number="4.7" kind="example" id="ex_4.7" topic="Equation of a line and area condition via determinants"}
#### उदाहरण 4.7

:::prompt
सारणिकों का प्रयोग करके $\mathrm{A}(1,3)$ और $\mathrm{B}(0,0)$ को जोड़ने वाली रेखा का समीकरण ज्ञात कीजिए और $k$ का मान ज्ञात कीजिए यदि एक बिंदु $\mathrm{D}(k, 0)$ इस प्रकार है कि $\Delta \mathrm{ABD}$ का क्षेत्रफल $3$ वर्ग इकाई है।
:::

:::solution{label="हल"}
मान लीजिए AB पर कोई बिंदु $\mathrm{P}(x, y)$ है तब $\Delta \mathrm{ABP}$ का क्षेत्रफल $=0$ (क्यों?)
इसलिए
$$
\frac{1}{2}\left|\begin{array}{lll}
0 & 0 & 1 \\
1 & 3 & 1 \\
x & y & 1
\end{array}\right|=0
$$
इससे प्राप्त है
$$
\frac{1}{2}(y-3 x)=0 \text { या } y=3 x
$$
जो अभीष्ट रेखा AB का समीकरण है।
किंतु $\Delta \mathrm{ABD}$ का क्षेत्रफल $3$ वर्ग इकाई दिया है अतः
$$
\frac{1}{2}\left|\begin{array}{ccc}
1 & 3 & 1 \\
0 & 0 & 1 \\
k & 0 & 1
\end{array}\right|= \pm 3 \text { हमें प्राप्त है } \frac{-3 k}{2}= \pm 3 \text {, i.e., } k=2
$$
:::

:::answer
**उत्तर:** रेखा AB का समीकरण $y=3x$; $k=2$
:::

:::

:::example{number="4.8" kind="example" id="ex_4.8" topic="Finding a minor of a determinant element"}
#### उदाहरण 4.8

:::prompt
सारणिक $\Delta=\left|\begin{array}{lll}1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9\end{array}\right|$ में अवयव $6$ का उपसारणिक ज्ञात कीजिए।
:::

:::solution{label="हल"}
हल क्योंकि $6$ दूसरी पंक्ति एवं तृतीय स्तंभ में स्थित है। इसलिए इसका उपसारिणक $=\mathrm{M}_{23}$ निम्नलिखित प्रकार से प्राप्त होता है।

$$
\mathrm{M}_{23}=\left|\begin{array}{ll}
1 & 2 \\
7 & 8
\end{array}\right|=8-14=-6\left(\Delta \text { से } \mathrm{R}_{2} \text { और } \mathrm{C}_{3} \text { हटाने पर }\right)
$$
:::

:::answer
**उत्तर:** $\mathrm{M}_{23}=-6$
:::

:::

:::example{number="4.9" kind="example" id="ex_4.9" topic="Minors and cofactors of a 2x2 determinant"}
#### उदाहरण 4.9

:::prompt
सारणिक $\left|\begin{array}{cc}1 & -2 \\ 4 & 3\end{array}\right|$ के सभी अवयवों के उपसारणिक व सहखंड ज्ञात कीजिए।
:::

:::solution{label="हल"}
अवयव $a_{i j}$ का उपसारणिक $\mathrm{M}_{i j}$ है।
यहाँ

$$
\begin{aligned}
& a_{11}=1, \text { इसलिए } \mathrm{M}_{11}=a_{11} \text { का उपसारणिक }=3 \\
& \mathrm{M}_{12}=\text { अवयव } a_{12} \text { का उपसारणिक }=4 \\
& \mathrm{M}_{21}=\text { अवयव } a_{21} \text { का उपसारणिक }=-2 \\
& \mathrm{M}_{22}=\text { अवयव } a_{22} \text { का उपसारणिक }=1
\end{aligned}
$$

अब $a_{i j}$ का सहखंड $\mathrm{A}_{i j}$ है। इसलिए

$$
\begin{aligned}
& A_{11}=(-1)^{1+1} \quad M_{11}=(-1)^{2}(3)=3 \\
& A_{12}=(-1)^{1+2} \quad M_{12}=(-1)^{3}(4)=-4 \\
& A_{21}=(-1)^{2+1} \quad M_{21}=(-1)^{3}(-2)=2 \\
& A_{22}=(-1)^{2+2} \quad M_{22}=(-1)^{4}(1)=1
\end{aligned}
$$
:::

:::

:::example{number="4.10" kind="example" id="ex_4.10" topic="General minors and cofactors of a 3x3 determinant"}
#### उदाहरण 4.10

:::prompt
$\Delta=\left|\begin{array}{lll}a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \\ a_{31} & a_{32} & a_{33}\end{array}\right|$ के अवयवों $a_{11}$ तथा $a_{21}$ के उपसारणिक और सहखंड ज्ञात कीजिए।
:::

:::solution{label="हल"}
उपसारणिक और सहखंड की परिभाषा द्वारा हम पाते हैं:
$a_{11}$ का उपसारणिक $=\mathrm{M}_{11}=\left|\begin{array}{ll}a_{22} & a_{23} \\ a_{32} & a_{33}\end{array}\right|=a_{22} a_{33}-a_{23} a_{32}$
$a_{11}$ का सहखंड $=\mathrm{A}_{11}=(-1)^{1+1} \mathrm{M}_{11}=a_{22} a_{33}-a_{23} a_{32}$
$a_{21}$ का उपसारणिक $=\mathrm{M}_{21}=\left|\begin{array}{ll}a_{12} & a_{13} \\ a_{32} & a_{33}\end{array}\right|=a_{12} a_{33}-a_{13} a_{32}$
$a_{21}$ का सहखंड $=\mathrm{A}_{21}=(-1)^{2+1} \mathrm{M}_{21}=(-1)\left(a_{12} a_{33}-a_{13} a_{32}\right)=-a_{12} a_{33}+a_{13} a_{32}$ टिप्पणी उदाहरण $21$ में सारणिक $\boldsymbol{\Delta}$ का $\mathrm{R}_{1}$ के सापेक्ष प्रसरण करने पर हम पाते हैं कि

$$
\begin{aligned}
\Delta & =(-1)^{1+1} a_{11}\left|\begin{array}{ll}
a_{22} & a_{23} \\
a_{32} & a_{33}
\end{array}\right|+(-1)^{1+2} a_{12}\left|\begin{array}{ll}
a_{21} & a_{23} \\
a_{31} & a_{33}
\end{array}\right|+(-1)^{1+3} a_{13}\left|\begin{array}{ll}
a_{21} & a_{22} \\
a_{31} & a_{32}
\end{array}\right| \\
& =a_{11} \mathrm{~A}_{11}+a_{12} \mathrm{~A}_{12}+a_{13} \mathrm{~A}_{13} \text {, जहाँ } a_{i j} \text { का सहखंड } \mathrm{A}_{i j} \text { हैं। } \\
& =\mathrm{R}_{1} \text { के अवयवों और उनके संगत सहखंडों के गुणनफल का योग। }
\end{aligned}
$$

इसी प्रकार $\Delta$ का $\mathrm{R}_{2}, \mathrm{R}_{3}, \mathrm{C}_{1}, \mathrm{C}_{2}$ और $\mathrm{C}_{3}$ के अनुदिश $5$ प्रसरण अन्य प्रकार से हैं।
अतः सारणिक $\Delta$, किसी पंक्ति (या स्तंभ) के अवयवों और उनके संगत सहखंडों के गुणनफल का योग है।
:::

:::

:::example{number="4.11" kind="example" id="ex_4.11" topic="Minors and cofactors verification"}
#### उदाहरण 4.11

:::prompt
सारणिक $\left|\begin{array}{ccc}2 & -3 & 5 \\ 6 & 0 & 4 \\ 1 & 5 & -7\end{array}\right|$ के अवयवों के उपसारणिक और सहखंड ज्ञात कीजिए और सत्यापित कीजिए कि $a_{11} \mathrm{~A}_{31}+a_{12} \mathrm{~A}_{32}+a_{13} \mathrm{~A}_{33}=0$ है।
:::

:::solution{label="हल"}
यहाँ $\mathrm{M}_{11}=\left|\begin{array}{cc}0 & 4 \\ 5 & -7\end{array}\right|=0-20=-20 ;$ इसलिए $\mathrm{A}_{11}=(-1)^{1+1}(-20)=-20$

$$
\begin{aligned}
& \mathrm{M}_{12}=\left|\begin{array}{cc}
6 & 4 \\
1 & -7
\end{array}\right|=-42-4=-46 ; \text { इसलिए } \mathrm{A}_{12}=(-1)^{1+2}(-46)=46 \\
& \mathrm{M}_{13}=\left|\begin{array}{cc}
6 & 0 \\
1 & 5
\end{array}\right|=30-0=30 ; \text { इसलिए } \mathrm{A}_{13}=(-1)^{1+3}(30)=30 \\
& \mathrm{M}_{21}=\left|\begin{array}{cc}
-3 & 5 \\
5 & -7
\end{array}\right|=21-25=-4 ; \text { इसलिए } \mathrm{A}_{21}=(-1)^{2+1}(-4)=4 \\
& \mathrm{M}_{22}=\left|\begin{array}{cc}
2 & 5 \\
1 & -7
\end{array}\right|=-14-5=-19 ; \text { इसलिए } \mathrm{A}_{22}=(-1)^{2+2}(-19)=-19 \\
& \mathrm{M}_{23}=\left|\begin{array}{cc}
2 & -3 \\
1 & 5
\end{array}\right|=10+3=13 ; \text { इसलिए } \mathrm{A}_{23}=(-1)^{2+3}(13)=-13 \\
& \mathrm{M}_{31}=\left|\begin{array}{cc}
-3 & 5 \\
0 & 4
\end{array}\right|=-12-0=-12 ; \text { इसलिए } \mathrm{A}_{31}=(-1)^{3+1}(-12)=-12 \\
& \mathrm{M}_{32}=\left|\begin{array}{cc}
2 & 5 \\
6 & 4
\end{array}\right|=8-30=-22 ; \text { इसलिए } \mathrm{A}_{32}=(-1)^{3+2}(-22)=22
\end{aligned}
$$

और

$$
\mathrm{M}_{33}=\left|\begin{array}{cc}
2 & -3 \\
6 & 0
\end{array}\right|=0+18=18 ; \text { इसलिए } \mathrm{A}_{33}=(-1)^{3+3}(18)=18
$$

अब

$$
a_{11}=2, a_{12}=-3, a_{13}=5 ; \text { तथा } \mathrm{A}_{31}=-12, \mathrm{~A}_{32}=22, \mathrm{~A}_{33}=18 \text { है। }
$$

इसलिए

$$
\begin{aligned}
& a_{11} \mathrm{~A}_{31}+a_{12} \mathrm{~A}_{32}+a_{13} \mathrm{~A}_{33} \\
& =2(-12)+(-3)(22)+5(18)=-24-66+90=0
\end{aligned}
$$
:::

:::

:::example{number="4.12" kind="example" id="ex_4.12" topic="Adjoint of a 2x2 matrix"}
#### उदाहरण 4.12

:::prompt
आव्यूह $\mathrm{A}=\left[\begin{array}{ll}2 & 3 \\ 1 & 4\end{array}\right]$ का सहखंडज ज्ञात कीजिए।
:::

:::solution{label="हल"}
हम जानते हैं कि $\mathrm{A}_{11}=4, \mathrm{~A}_{12}=-1, \mathrm{~A}_{21}=-3, \mathrm{~A}_{22}=2$
अत:

$$
\operatorname{adj} \mathrm{A}=\left[\begin{array}{ll}
\mathrm{A}_{11} & \mathrm{~A}_{21} \\
\mathrm{~A}_{12} & \mathrm{~A}_{22}
\end{array}\right]=\left[\begin{array}{cc}
4 & -3 \\
-1 & 2
\end{array}\right]
$$
:::

:::answer
**उत्तर:** $\operatorname{adj} \mathrm{A}=\left[\begin{array}{cc}4 & -3 \\ -1 & 2\end{array}\right]$
:::

:::

:::example{number="4.13" kind="example" id="ex_4.13" topic="Verifying A.adjA=|A|.I and finding inverse"}
#### उदाहरण 4.13

:::prompt
यदि $\mathrm{A}=\left[\begin{array}{lll}1 & 3 & 3 \\ 1 & 4 & 3 \\ 1 & 3 & 4\end{array}\right]$ हो तो सत्यापित कीजिए कि $\mathrm{A} \cdot \operatorname{adj} \mathrm{A}=|\mathrm{A}| \cdot \mathrm{I}$ और $\mathrm{A}^{-1}$
ज्ञात कीजिए।
:::

:::solution{label="हल"}
हम पाते हैं कि $|\mathrm{A}|=1(16-9)-3(4-3)+3(3-4)=1 \neq 0$
अब $\mathrm{A}_{11}=7, \mathrm{~A}_{12}=-1, \mathrm{~A}_{13}=-1, \mathrm{~A}_{21}=-3, \mathrm{~A}_{22}=1, \mathrm{~A}_{23}=0, \mathrm{~A}_{31}=-3, \mathrm{~A}_{32}=0, \mathrm{~A}_{33}=1$
इसलिए

$$
\operatorname{adj} \mathrm{A}=\left[\begin{array}{rcc}
7 & -3 & -3 \\
-1 & 1 & 0 \\
-1 & 0 & 1
\end{array}\right]
$$

अब

$$
\mathrm{A} \cdot(\operatorname{adj} \mathrm{~A})=\left[\begin{array}{lll}
1 & 3 & 3 \\
1 & 4 & 3 \\
1 & 3 & 4
\end{array}\right]\left[\begin{array}{rcc}
7 & -3 & -3 \\
-1 & 1 & 0 \\
-1 & 0 & 1
\end{array}\right]
$$

$$
=\left[\begin{array}{lll}
7-3-3 & -3+3+0 & -3+0+3 \\
7-4-3 & -3+4+0 & -3+0+3 \\
7-3-4 & -3+3+0 & -3+0+4
\end{array}\right]
$$

$$
=\left[\begin{array}{lll}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{array}\right]=(1)\left[\begin{array}{lll}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{array}\right]=|\mathrm{A}| \cdot \mathrm{I}
$$

और

$$
\mathrm{A}^{-1}=\frac{1}{|\mathrm{~A}|} \cdot \operatorname{adj} \mathrm{A}=\frac{1}{1}\left[\begin{array}{ccc}
7 & -3 & -3 \\
-1 & 1 & 0 \\
-1 & 0 & 1
\end{array}\right]=\left[\begin{array}{ccc}
7 & -3 & -3 \\
-1 & 1 & 0 \\
-1 & 0 & 1
\end{array}\right]
$$
:::

:::answer
**उत्तर:** $\mathrm{A}^{-1}=\left[\begin{array}{ccc}7 & -3 & -3 \\ -1 & 1 & 0 \\ -1 & 0 & 1\end{array}\right]$
:::

:::

:::example{number="4.14" kind="example" id="ex_4.14" topic="Verifying (AB)^-1 = B^-1 A^-1"}
#### उदाहरण 4.14

:::prompt
यदि $\mathrm{A}=\left[\begin{array}{cc}2 & 3 \\ 1 & -4\end{array}\right], \mathrm{B}=\left[\begin{array}{cc}1 & -2 \\ -1 & 3\end{array}\right]$, तो सत्यापित कीजिए कि $(\mathrm{AB})^{-1}=\mathrm{B}^{-1} \mathrm{~A}^{-1}$ है।
:::

:::solution{label="हल"}
हम जानते हैं कि $\mathrm{AB}=\left[\begin{array}{cc}2 & 3 \\ 1 & -4\end{array}\right]\left[\begin{array}{cc}1 & -2 \\ -1 & 3\end{array}\right]=\left[\begin{array}{cc}-1 & 5 \\ 5 & -14\end{array}\right]$
क्योंकि $|\mathrm{AB}|=-11 \neq 0,(\mathrm{AB})^{-1}$ का अस्तित्व है और इसे निम्नलिखित प्रकार से व्यक्त किया जाता है।

$$
(\mathrm{AB})^{-1}=\frac{1}{|\mathrm{AB}|} \cdot \operatorname{adj}(\mathrm{AB})=-\frac{1}{11}\left[\begin{array}{cc}
-14 & -5 \\
-5 & -1
\end{array}\right]=\frac{1}{11}\left[\begin{array}{cc}
14 & 5 \\
5 & 1
\end{array}\right]
$$

और $|\mathrm{A}|=-11 \neq 0$ व $|\mathrm{B}|=1 \neq 0$. इसलिए $\mathrm{A}^{-1}$ और $\mathrm{B}^{-1}$ दोनों का अस्तित्व है और जिसे निम्नलिखित रूप में व्यक्त किया जा सकता है।

$$
\mathrm{A}^{-1}=-\frac{1}{11}\left[\begin{array}{cc}
-4 & -3 \\
-1 & 2
\end{array}\right], \mathrm{B}^{-1}=\left[\begin{array}{ll}
3 & 2 \\
1 & 1
\end{array}\right]
$$

इसलिए

$$
\mathrm{B}^{-1} \mathrm{~A}^{-1}=-\frac{1}{11}\left[\begin{array}{ll}
3 & 2 \\
1 & 1
\end{array}\right]\left[\begin{array}{cc}
-4 & -3 \\
-1 & 2
\end{array}\right]=-\frac{1}{11}\left[\begin{array}{cc}
-14 & -5 \\
-5 & -1
\end{array}\right]=\frac{1}{11}\left[\begin{array}{cc}
14 & 5 \\
5 & 1
\end{array}\right]
$$

अत:

$$
(\mathrm{AB})^{-1}=\mathrm{B}^{-1} \mathrm{~A}^{-1} \text { है। }
$$
:::

:::

:::example{number="4.15" kind="example" id="ex_4.15" topic="Matrix polynomial equation and inverse"}
#### उदाहरण 4.15

:::prompt
प्रदर्शित कीजिए कि आव्यूह $\mathrm{A}=\left[\begin{array}{ll}2 & 3 \\ 1 & 2\end{array}\right]$ समीकरण $\mathrm{A}^{2}-4 \mathrm{~A}+\mathrm{I}=\mathrm{O}$, जहाँ I $2 \times 2$ कोटि का एक तत्समक आव्यूह है और $\mathrm{O}, 2 \times 2$ कोटि का एक शून्य आव्यूह है। इसकी सहायता से $\mathrm{A}^{-1}$ ज्ञात कीजिए।
:::

:::solution{label="हल"}
हम जानते हैं कि $\mathrm{A}^{2}=\mathrm{A} . \mathrm{A}=\left[\begin{array}{ll}2 & 3 \\ 1 & 2\end{array}\right]\left[\begin{array}{ll}2 & 3 \\ 1 & 2\end{array}\right]=\left[\begin{array}{cc}7 & 12 \\ 4 & 7\end{array}\right]$
अत:

$$
A^{2}-4 A+I=\left[\begin{array}{cc}
7 & 12 \\
4 & 7
\end{array}\right]-\left[\begin{array}{cc}
8 & 12 \\
4 & 8
\end{array}\right]+\left[\begin{array}{ll}
1 & 0 \\
0 & 1
\end{array}\right]=\left[\begin{array}{ll}
0 & 0 \\
0 & 0
\end{array}\right]=O
$$

अब

$$
\mathrm{A}^{2}-4 \mathrm{~A}+\mathrm{I}=\mathrm{O}
$$

इसलिए

$$
A A-4 A=-I
$$

या $\mathrm{A} \mathrm{A}\left(\mathrm{A}^{-1}\right)-4 \mathrm{AA}^{-1}=-\mathrm{IA}^{-1}$ (दोनों ओर $\mathrm{A}^{-1}$ से उत्तर गुणन द्वारा क्योंकि $|\mathrm{A}| \neq 0$ )
या

$$
\mathrm{A}\left(\mathrm{~A} \mathrm{~A}^{-1}\right)-4 \mathrm{I}=-\mathrm{A}^{-1}
$$

या

$$
A I-4 I=-A^{-1}
$$

या

$$
A^{-1}=4 I-A=\left[\begin{array}{ll}
4 & 0 \\
0 & 4
\end{array}\right]-\left[\begin{array}{ll}
2 & 3 \\
1 & 2
\end{array}\right]=\left[\begin{array}{cc}
2 & -3 \\
-1 & 2
\end{array}\right]
$$

अत:

$$
A^{-1}=\left[\begin{array}{cc}
2 & -3 \\
-1 & 2
\end{array}\right]
$$
:::

:::answer
**उत्तर:** $A^{-1}=\left[\begin{array}{cc}2 & -3 \\ -1 & 2\end{array}\right]$
:::

:::

:::example{number="4.16" kind="example" id="ex_4.16" topic="Solving equation system via matrix method"}
#### उदाहरण 4.16

:::prompt
निम्नलिखित समीकरण निकाय को हल कीजिए:

$$
\begin{aligned}
& 2 x+5 y=1 \\
& 3 x+2 y=7
\end{aligned}
$$
:::

:::solution{label="हल"}
समीकरण निकाय $\mathrm{AX}=\mathrm{B}$ के रूप में लिखा जा सकता है, जहाँ

$$
\mathrm{A}=\left[\begin{array}{ll}
2 & 5 \\
3 & 2
\end{array}\right], \mathrm{X}=\left[\begin{array}{l}
x \\
y
\end{array}\right] \text { और } \mathrm{B}=\left[\begin{array}{l}
1 \\
7
\end{array}\right]
$$

अब, $|\mathrm{A}|=-11 \neq 0$, अत: A व्युत्क्रमणीय आव्यूह है इसलिए इसके व्युत्क्रम का अस्तित्व है। और इसका एक अद्वितीय हल है।

ध्यान दीजिए कि

$$
\mathrm{A}^{-1}=-\frac{1}{11}\left[\begin{array}{cc}
2 & -5 \\
-3 & 2
\end{array}\right]
$$

इसलिए

$$
\mathrm{X}=\mathrm{A}^{-1} \mathrm{~B}=-\frac{1}{11}\left[\begin{array}{cc}
2 & -5 \\
-3 & 2
\end{array}\right]\left[\begin{array}{l}
1 \\
7
\end{array}\right]
$$

अर्थात्

$$
\left[\begin{array}{l}
x \\
y
\end{array}\right]=-\frac{1}{11}\left[\begin{array}{c}
-33 \\
11
\end{array}\right]=\left[\begin{array}{c}
3 \\
-1
\end{array}\right]
$$

अत:

$$
x=3, y=-1
$$
:::

:::answer
**उत्तर:** $x=3, y=-1$
:::

:::

:::example{number="4.17" kind="example" id="ex_4.17" topic="Solving 3x3 equation system via matrix method"}
#### उदाहरण 4.17

:::prompt
निम्नलिखित समीकरण निकाय

$$
\begin{array}{r}
3 x-2 y+3 z=8 \\
2 x+y-z=1 \\
4 x-3 y+2 z=4
\end{array}
$$

को आव्यूह विधि से हल कीजिए।
:::

:::solution{label="हल"}
समीकरण निकाय को $\mathrm{AX}=\mathrm{B}$ के रूप में व्यक्त किया जा सकता है जहाँ

$$
\mathrm{A}=\left[\begin{array}{ccc}
3 & -2 & 3 \\
2 & 1 & -1 \\
4 & -3 & 2
\end{array}\right], \mathrm{X}=\left[\begin{array}{l}
x \\
y \\
z
\end{array}\right] \text { और } \mathrm{B}=\left[\begin{array}{l}
8 \\
1 \\
4
\end{array}\right]
$$

हम देखते हैं कि

$$
|\mathrm{A}|=3(2-3)+2(4+4)+3(-6-4)=-17 \neq 0 \text { है। }
$$

अतः A व्युत्क्रमणीय है, और इसके व्युत्क्रम का अस्तित्व है।

$$
\begin{array}{lll}
\mathrm{A}_{11}=-1, & \mathrm{~A}_{12}=-8, & \mathrm{~A}_{13}=-10 \\
\mathrm{~A}_{21}=-5, & \mathrm{~A}_{22}=-6, & \mathrm{~A}_{23}=1 \\
\mathrm{~A}_{31}=-1, & \mathrm{~A}_{32}=9, & \mathrm{~A}_{33}=7
\end{array}
$$

इसलिए

$$
\mathrm{A}^{-1}=-\frac{1}{17}\left[\begin{array}{ccc}
-1 & -5 & -1 \\
-8 & -6 & 9 \\
-10 & 1 & 7
\end{array}\right]
$$

और

$$
\mathrm{X}=\mathrm{A}^{-1} \mathrm{~B}=-\frac{1}{17}\left[\begin{array}{ccc}
-1 & -5 & -1 \\
-8 & -6 & 9 \\
-10 & 1 & 7
\end{array}\right]\left[\begin{array}{l}
8 \\
1 \\
4
\end{array}\right]
$$

अत:

$$
\left[\begin{array}{l}
x \\
y \\
z
\end{array}\right]=-\frac{1}{17}\left[\begin{array}{l}
-17 \\
-34 \\
-51
\end{array}\right]=\left[\begin{array}{l}
1 \\
2 \\
3
\end{array}\right]
$$

अत:

$$
x=1, y=2 \text { व } z=3
$$
:::

:::answer
**उत्तर:** $x=1, y=2, z=3$
:::

:::

:::example{number="4.18" kind="example" id="ex_4.18" topic="Word problem - three numbers via matrix method"}
#### उदाहरण 4.18

:::prompt
तीन संख्याओं का योग $6$ है। यदि हम तीसरी संख्या को $3$ से गुणा करके दूसरी संख्या में जोड़ दें तो हमें $11$ प्राप्त होता है। पहली ओर तीसरी को जोड़ने से हमें दूसरी संख्या का दुगुना प्राप्त होता है। इसका बीजगणितीय निरूपण कीजिए और आव्यूह विधि से संख्याएँ ज्ञात कीजिए।
:::

:::solution{label="हल"}
मान लीजिए पहली, दूसरी व तीसरी संख्या क्रमशः $x, y$ और $z$, द्वारा निरूपित है। तब दी गई शर्तों के अनुसार हमें प्राप्त होता है:

$$
\begin{aligned}
x+y+z & =6 \\
y+3 z & =11 \\
x+z & =2 y
\end{aligned}
$$

या

$$
x-2 y+z=0
$$

इस निकाय को $\mathrm{AX}=\mathrm{B}$ के रूप में लिखा जा सकता है जहाँ

$$
\mathrm{A}=\left[\begin{array}{lll}
1 & 1 & 1 \\
0 & 1 & 3 \\
1 & 2 & 1
\end{array}\right], \mathrm{X}=\left[\begin{array}{l}
x \\
y \\
z
\end{array}\right] \text { और } \mathrm{B}=\left[\begin{array}{c}
6 \\
11 \\
0
\end{array}\right] \text { है। }
$$

यहाँ $|\mathrm{A}|=1(1+6)+0+1(3-1)=9 \neq 0$ है। अब हम $\operatorname{adj} \mathrm{A}$ ज्ञात करते हैं।

$$
\begin{array}{lll}
A_{11}=1(1+6)=7, & A_{12}=-(0-3)=3, & A_{13}=-1 \\
A_{21}=-(1+2)=-3, & A_{22}=0, & A_{23}=-(-2-1)=3 \\
A_{31}=(3-1)=2, & A_{32}=-(3-0)=-3, & A_{33}=(1-0)=1
\end{array}
$$

अतः $\operatorname{adj} \mathrm{A}=\left[\begin{array}{ccc}7 & -3 & 2 \\ 3 & 0 & -3 \\ -1 & 3 & 1\end{array}\right]$
इस प्रकार

$$
\mathrm{A}^{-1}=\frac{1}{|\mathrm{~A}|} \operatorname{adj} .(\mathrm{A})=\frac{1}{9}\left[\begin{array}{ccc}
7 & -3 & 2 \\
3 & 0 & -3 \\
-1 & 3 & 1
\end{array}\right]
$$

क्योंकि

$$
\begin{aligned}
X & =A^{-1} B \\
X & =\frac{1}{9}\left[\begin{array}{ccc}
7 & -3 & 2 \\
3 & 0 & -3 \\
-1 & 3 & 1
\end{array}\right]\left[\begin{array}{c}
6 \\
11 \\
0
\end{array}\right]
\end{aligned}
$$

या

$$
\left[\begin{array}{l}
x \\
y \\
z
\end{array}\right]=\frac{1}{9}\left[\begin{array}{l}
42-33+0 \\
18+0+0 \\
-6+33+0
\end{array}\right]=\frac{1}{9}\left[\begin{array}{c}
9 \\
18 \\
27
\end{array}\right]=\left[\begin{array}{l}
1 \\
2 \\
3
\end{array}\right]
$$

अत:

$$
x=1, y=2, z=3
$$
:::

:::answer
**उत्तर:** $x=1, y=2, z=3$
:::

:::

:::example{number="4.19" kind="example" id="ex_4.19" topic="Matrix product application to solve equations"}
#### उदाहरण 4.19

:::prompt
आव्यूहों के गुणनफल $\left[\begin{array}{ccc}1 & 1 & 2 \\ 0 & 2 & 3 \\ 3 & 2 & 4\end{array}\right]\left[\begin{array}{ccc}2 & 0 & 1 \\ 9 & 2 & 3 \\ 6 & 1 & 2\end{array}\right]$ का प्रयोग करते हुए निम्नलिखित समीकरण निकाय को हल कीजिए:

$$
\begin{array}{r}
x-y+2 z=1 \\
2 y-3 z=1 \\
3 x-2 y+4 z=2
\end{array}
$$
:::

:::solution{label="हल"}
हल दिया गया गुणनफल $\left[\begin{array}{ccc}1 & -1 & 2 \\ 0 & 2 & -3 \\ 3 & -2 & 4\end{array}\right]\left[\begin{array}{ccc}-2 & 0 & 1 \\ 9 & 2 & -3 \\ 6 & 1 & -2\end{array}\right]$

$$
=\left[\begin{array}{ccc}
-2-9+12 & 0-2+2 & 1+3-4 \\
0+18-18 & 0+4-3 & 0-6+6 \\
-6-18+24 & 0-4+4 & 3+6-8
\end{array}\right]=\left[\begin{array}{lll}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{array}\right]
$$

अत:

$$
\left[\begin{array}{ccc}
1 & 1 & 2 \\
0 & 2 & 3 \\
3 & 2 & 4
\end{array}\right]^{1}=\left[\begin{array}{ccc}
2 & 0 & 1 \\
9 & 2 & 3 \\
6 & 1 & 2
\end{array}\right]
$$

अब दिए गए समीकरण निकाय को आव्यूह के रूप निम्नलिखित रूप में लिखा जा सकता है

$$
\left[\begin{array}{ccc}
1 & -1 & 2 \\
0 & 2 & -3 \\
3 & -2 & 4
\end{array}\right]\left[\begin{array}{l}
x \\
y \\
z
\end{array}\right]=\left[\begin{array}{l}
1 \\
1 \\
2
\end{array}\right]
$$

या

$$
\begin{aligned}
{\left[\begin{array}{l}
x \\
y \\
z
\end{array}\right] } & =\left[\begin{array}{rrr}
1 & -1 & 2 \\
0 & 2 & -3 \\
3 & -2 & 4
\end{array}\right]^{-1}\left[\begin{array}{l}
1 \\
1 \\
2
\end{array}\right]=\left[\begin{array}{lll}
2 & 0 & 1 \\
9 & 2 & 3 \\
6 & 1 & 2
\end{array}\right]\left[\begin{array}{l}
1 \\
1 \\
2
\end{array}\right] \\
& =\left[\begin{array}{c}
-2+0+2 \\
9+2-6 \\
6+1-4
\end{array}\right]=\left[\begin{array}{l}
0 \\
5 \\
3
\end{array}\right]
\end{aligned}
$$

अतः

$$
x=0, y=5 \text { और } z=3
$$
:::

:::answer
**उत्तर:** $x=0, y=5, z=3$
:::

:::
