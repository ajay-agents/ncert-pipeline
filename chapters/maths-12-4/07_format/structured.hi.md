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
:::concept{label="जानकारी"}
ध्यान दीजिए कि तीसरे स्तंभ में दो प्रविष्टियाँ शून्य हैं। इसलिए तीसरे स्तंभ $\left(\mathrm{C}_{3}\right)$ के अनुदिश प्रसरण करने पर हमें प्राप्त होता है कि
:::

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
:::concept{label="जानकारी"}
$\mathrm{R}_{1}$ के अनुदिश प्रसरण करने पर हमें प्राप्त होता है कि
:::

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
:::formula{label="मुख्य सूत्र"}
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
:::step{n="1"}
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
:::

:::step{n="2"}
किंतु $\Delta \mathrm{ABD}$ का क्षेत्रफल $3$ वर्ग इकाई दिया है अतः
$$
\frac{1}{2}\left|\begin{array}{ccc}
1 & 3 & 1 \\
0 & 0 & 1 \\
k & 0 & 1
\end{array}\right|= \pm 3 \text { हमें प्राप्त है } \frac{-3 k}{2}= \pm 3 \text {, i.e., } k=2
$$
:::
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
:::step{n="1"}
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
:::

:::step{n="2"}
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

:::

:::example{number="4.10" kind="example" id="ex_4.10" topic="General minors and cofactors of a 3x3 determinant" simplified="True"}
#### उदाहरण 4.10

:::prompt
$\Delta=\left|\begin{array}{lll}a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \\ a_{31} & a_{32} & a_{33}\end{array}\right|$ के अवयवों $a_{11}$ तथा $a_{21}$ के उपसारणिक और सहखंड ज्ञात कीजिए।
:::

:::solution{label="हल"}
:::step{n="1"}
उपसारणिक और सहखंड की परिभाषा द्वारा हम पाते हैं:
$a_{11}$ का उपसारणिक $=\mathrm{M}_{11}=\left|\begin{array}{ll}a_{22} & a_{23} \\ a_{32} & a_{33}\end{array}\right|=a_{22} a_{33}-a_{23} a_{32}$
$a_{11}$ का सहखंड $=\mathrm{A}_{11}=(-1)^{1+1} \mathrm{M}_{11}=a_{22} a_{33}-a_{23} a_{32}$
$a_{21}$ का उपसारणिक $=\mathrm{M}_{21}=\left|\begin{array}{ll}a_{12} & a_{13} \\ a_{32} & a_{33}\end{array}\right|=a_{12} a_{33}-a_{13} a_{32}$
$a_{21}$ का सहखंड $=\mathrm{A}_{21}=(-1)^{2+1} \mathrm{M}_{21}=(-1)\left(a_{12} a_{33}-a_{13} a_{32}\right)=-a_{12} a_{33}+a_{13} a_{32}$ है।
:::

:::note{type="recall" label="टिप्पणी"}
टिप्पणी: उदाहरण $21$ में सारणिक $\boldsymbol{\Delta}$ का $\mathrm{R}_{1}$ के सापेक्ष प्रसरण करने पर हम पाते हैं कि

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

:::

:::example{number="4.11" kind="example" id="ex_4.11" topic="Minors and cofactors verification"}
#### उदाहरण 4.11

:::prompt
सारणिक $\left|\begin{array}{ccc}2 & -3 & 5 \\ 6 & 0 & 4 \\ 1 & 5 & -7\end{array}\right|$ के अवयवों के उपसारणिक और सहखंड ज्ञात कीजिए और सत्यापित कीजिए कि $a_{11} \mathrm{~A}_{31}+a_{12} \mathrm{~A}_{32}+a_{13} \mathrm{~A}_{33}=0$ है।
:::

:::solution{label="हल"}
:::step{n="1"}
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
:::

:::step{n="2"}
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
:::step{n="1"}
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
:::

:::step{n="2"}
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
:::

:::answer
**उत्तर:** $\mathrm{A}^{-1}=\left[\begin{array}{ccc}7 & -3 & -3 \\ -1 & 1 & 0 \\ -1 & 0 & 1\end{array}\right]$
:::

:::

:::example{number="4.14" kind="example" id="ex_4.14" topic="Verifying (AB)^-1 = B^-1 A^-1" simplified="True"}
#### उदाहरण 4.14

:::prompt
यदि $\mathrm{A}=\left[\begin{array}{cc}2 & 3 \\ 1 & -4\end{array}\right], \mathrm{B}=\left[\begin{array}{cc}1 & -2 \\ -1 & 3\end{array}\right]$, तो सत्यापित कीजिए कि $(\mathrm{AB})^{-1}=\mathrm{B}^{-1} \mathrm{~A}^{-1}$ है।
:::

:::solution{label="हल"}
:::step{n="1"}
हम जानते हैं कि $\mathrm{AB}=\left[\begin{array}{cc}2 & 3 \\ 1 & -4\end{array}\right]\left[\begin{array}{cc}1 & -2 \\ -1 & 3\end{array}\right]=\left[\begin{array}{cc}-1 & 5 \\ 5 & -14\end{array}\right]$ है। $|\mathrm{AB}|=-11 \neq 0,(\mathrm{AB})^{-1}$ का अस्तित्व है। इसे इस प्रकार व्यक्त किया जाता है।

$$
(\mathrm{AB})^{-1}=\frac{1}{|\mathrm{AB}|} \cdot \operatorname{adj}(\mathrm{AB})=-\frac{1}{11}\left[\begin{array}{cc}
-14 & -5 \\
-5 & -1
\end{array}\right]=\frac{1}{11}\left[\begin{array}{cc}
14 & 5 \\
5 & 1
\end{array}\right]
$$
:::

:::step{n="2"}
$|\mathrm{A}|=-11 \neq 0$ और $|\mathrm{B}|=1 \neq 0$ भी हैं। इसलिए $\mathrm{A}^{-1}$ और $\mathrm{B}^{-1}$ दोनों का अस्तित्व है। इन्हें इस प्रकार लिखा जा सकता है।

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

:::

:::example{number="4.15" kind="example" id="ex_4.15" topic="Matrix polynomial equation and inverse"}
#### उदाहरण 4.15

:::prompt
प्रदर्शित कीजिए कि आव्यूह $\mathrm{A}=\left[\begin{array}{ll}2 & 3 \\ 1 & 2\end{array}\right]$ समीकरण $\mathrm{A}^{2}-4 \mathrm{~A}+\mathrm{I}=\mathrm{O}$, जहाँ I $2 \times 2$ कोटि का एक तत्समक आव्यूह है और $\mathrm{O}, 2 \times 2$ कोटि का एक शून्य आव्यूह है। इसकी सहायता से $\mathrm{A}^{-1}$ ज्ञात कीजिए।
:::

:::solution{label="हल"}
:::step{n="1"}
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
:::

:::step{n="2"}
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
:::

:::answer
**उत्तर:** $A^{-1}=\left[\begin{array}{cc}2 & -3 \\ -1 & 2\end{array}\right]$
:::

:::

:::example{number="4.16" kind="example" id="ex_4.16" topic="Solving equation system via matrix method" simplified="True"}
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
:::formula{label="मुख्य सूत्र"}
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
:::

अब, $|\mathrm{A}|=-11 \neq 0$ है। अत: A व्युत्क्रमणीय आव्यूह है। इसलिए इसके व्युत्क्रम का अस्तित्व है, और समीकरण निकाय का एक अद्वितीय हल है।

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
:::step{n="1"}
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
:::

:::step{n="2"}
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
:::

:::answer
**उत्तर:** $x=1, y=2, z=3$
:::

:::

:::example{number="4.18" kind="example" id="ex_4.18" topic="Word problem - three numbers via matrix method" simplified="True"}
#### उदाहरण 4.18

:::prompt
तीन संख्याओं का योग $6$ है। यदि हम तीसरी संख्या को $3$ से गुणा करके दूसरी संख्या में जोड़ दें तो हमें $11$ प्राप्त होता है। पहली ओर तीसरी को जोड़ने से हमें दूसरी संख्या का दुगुना प्राप्त होता है। इसका बीजगणितीय निरूपण कीजिए और आव्यूह विधि से संख्याएँ ज्ञात कीजिए।
:::

:::solution{label="हल"}
:::step{n="1"}
मान लीजिए पहली, दूसरी और तीसरी संख्या क्रमशः $x, y$ और $z$ हैं। दी गई शर्तों के अनुसार हमें मिलता है:

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
:::

:::step{n="2"}
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
:::

:::step{n="3"}
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
:::step{n="1"}
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
:::

:::step{n="2"}
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
:::

:::answer
**उत्तर:** $x=0, y=5, z=3$
:::

:::


## प्रश्न और हल

:::question{number="4.1.1" kind="exercise" id="q_4.1.1" topic="Value of a 2x2 determinant"}
#### प्रश्न 4.1.1

:::prompt
सारणिकों का मान ज्ञात कीजिए: $\left|\begin{array}{cc}2 & 4 \\ -5 & -1\end{array}\right|$
:::

:::solution{label="हल"}
$\left|\begin{array}{cc}2 & 4 \\ -5 & -1\end{array}\right|$ $R_{1}$ के अनुदिश प्रसरण करने पर
$=2 \times(-1)-4 \times(-5)=-2+20=18$
:::

:::answer
**उत्तर:** $18$
:::

:::

:::question{number="4.1.2" kind="exercise" id="q_4.1.2" topic="Value of trig and symbolic 2x2 determinants"}
#### प्रश्न 4.1.2

:::part{label="(i)"}
:::prompt
$\left|\begin{array}{cc}\cos \theta & -\sin \theta \\ \sin \theta & \cos \theta\end{array}\right|$
:::

:::solution
$\left|\begin{array}{cc}\cos \theta & -\sin \theta \\ \sin \theta & \cos \theta\end{array}\right|=\cos \theta \times \cos \theta-\sin \theta \times(-\sin \theta)=\cos ^{2} \theta+\sin ^{2} \theta=1$
:::

:::answer
**उत्तर:** $1$
:::

:::

:::part{label="(ii)"}
:::prompt
$\left|\begin{array}{ll}x^{2}-x+1 & x-1 \\ x+1 & x+1\end{array}\right|$
:::

:::solution
$=\left(x^{2}-x+1\right) \times(x+1)-(x-1) \times(x+1)$
$=x^{3}+x^{2}-x^{2}-x+x+1-\left(x^{2}+x-x-1\right)$
$=x^{3}-x^{2}+2$
:::

:::answer
**उत्तर:** $x^{3}-x^{2}+2$
:::

:::

:::

:::question{number="4.1.3" kind="exercise" id="q_4.1.3" topic="Verifying |2A|=4|A|"}
#### प्रश्न 4.1.3

:::prompt
यदि $\mathrm{A}=\left[\begin{array}{ll}1 & 2 \\ 4 & 2\end{array}\right]$, तो दिखाइए $|2 \mathrm{~A}|=4|\mathrm{~A}|$
:::

:::solution{label="हल"}
:::step{n="1" label="मान रखो"}
$|2 A|=\left|\begin{array}{ll}2 & 4 \\ 8 & 4\end{array}\right|$ $R_{1}$ के अनुदिश प्रसरण करने पर

$$
=2 \times 4-4 \times 8=8-32=-24
$$
:::

:::step{n="2" label="मान रखो"}
$4|A|=4\left|\begin{array}{ll}1 & 2 \\ 4 & 2\end{array}\right|$ $R_{1}$ के अनुदिश प्रसरण करने पर

$$
=4(1 \times 2-2 \times 4)=4(-6)=-24
$$
:::

:::step{n="3" label="निष्कर्ष"}
समीकरण (1) और (2) से, $|2 A|=4|A|$
:::
:::

:::

:::question{number="4.1.4" kind="exercise" id="q_4.1.4" topic="Verifying |3A|=27|A|"}
#### प्रश्न 4.1.4

:::prompt
यदि $\mathrm{A}=\left[\begin{array}{lll}1 & 0 & 1 \\ 0 & 1 & 2 \\ 0 & 0 & 4\end{array}\right]$ हो, तो दिखाइए $|3 \mathrm{~A}|=27|\mathrm{~A}|$
:::

:::solution{label="हल"}
:::step{n="1" label="मान रखो"}
$|3 A|=\left|\begin{array}{ccc}3 & 0 & 3 \\ 0 & 3 & 6 \\ 0 & 0 & 12\end{array}\right|$ $R_{1}$ के अनुदिश प्रसरण करने पर

$$
=3(36-0)-0(0-0)+1(0-0)=108
$$
:::

:::step{n="2" label="मान रखो"}
$27|A|=27\left|\begin{array}{lll}1 & 0 & 1 \\ 0 & 1 & 2 \\ 0 & 0 & 4\end{array}\right|$ $R_{1}$ के अनुदिश प्रसरण करने पर

$$
=27\{1(4-0)-0(0-0)+1(0-0)\}=27(4)=108
$$
:::

:::step{n="3" label="निष्कर्ष"}
समीकरण (1) और (2) से, $|3 A|=27|A|$
:::
:::

:::

:::question{number="4.1.5" kind="exercise" id="q_4.1.5" topic="Value of several 3x3 determinants"}
#### प्रश्न 4.1.5

:::part{label="(i)"}
:::prompt
$\left|\begin{array}{ccc}3 & -1 & -2 \\ 0 & 0 & -1 \\ 3 & -5 & 0\end{array}\right|$
:::

:::solution
$R_{1}$ के अनुदिश प्रसरण करने पर $=3(0-5)+1(0+3)-2(0-0)=-15+3-0=-12$
:::

:::answer
**उत्तर:** $-12$
:::

:::

:::part{label="(ii)"}
:::prompt
$\left|\begin{array}{ccc}3 & -4 & 5 \\ 1 & 1 & -2 \\ 2 & 3 & 1\end{array}\right|$
:::

:::solution
$R_{1}$ के अनुदिश प्रसरण करने पर $=3(1+6)+4(1+4)+5(3-2)=21+20+5=46$
:::

:::answer
**उत्तर:** $46$
:::

:::

:::part{label="(iii)"}
:::prompt
$\left|\begin{array}{ccc}0 & 1 & 2 \\ -1 & 0 & -3 \\ -2 & 3 & 0\end{array}\right|$
:::

:::solution
$R_{1}$ के अनुदिश प्रसरण करने पर $=0(0+9)-1(0-6)+2(-3-0)=0+6-6=0$
:::

:::answer
**उत्तर:** $0$
:::

:::

:::part{label="(iv)"}
:::prompt
$\left|\begin{array}{ccc}2 & -1 & -2 \\ 0 & 2 & -1 \\ 3 & -5 & 0\end{array}\right|$
:::

:::solution
$R_{1}$ के अनुदिश प्रसरण करने पर $=2(0-5)+1(0+3)-2(0-6)=-10+3+12=5$
:::

:::answer
**उत्तर:** $5$
:::

:::

:::

:::question{number="4.1.6" kind="exercise" id="q_4.1.6" topic="Value of a 3x3 determinant"}
#### प्रश्न 4.1.6

:::prompt
यदि $\mathrm{A}=\left[\begin{array}{lll}1 & 1 & 2 \\ 2 & 1 & 3 \\ 5 & 4 & 9\end{array}\right]$, हो तो $|A|$ ज्ञात कीजिए।
:::

:::solution{label="हल"}
$|A|=\left|\begin{array}{lll}1 & 1 & -2 \\ 2 & 1 & -3 \\ 5 & 4 & -9\end{array}\right|$ $R_{1}$ के अनुदिश प्रसरण करने पर $=1(-9+12)-1(-18+15)-2(8-5)=3+3-6=0$
:::

:::answer
**उत्तर:** $|A|=0$
:::

:::

:::question{number="4.1.7" kind="exercise" id="q_4.1.7" topic="Solving for x from equal determinants"}
#### प्रश्न 4.1.7

:::part{label="(i)"}
:::prompt
$\left|\begin{array}{ll}2 & 4 \\ 5 & 1\end{array}\right|=\left|\begin{array}{cc}2 x & 4 \\ 6 & x\end{array}\right|$
:::

:::solution
$\Rightarrow 2-20=2 x^{2}-24 \quad \Rightarrow x^{2}=3 \quad \Rightarrow x= \pm \sqrt{3}$
:::

:::answer
**उत्तर:** $x= \pm \sqrt{3}$
:::

:::

:::part{label="(ii)"}
:::prompt
$\left|\begin{array}{ll}2 & 3 \\ 4 & 5\end{array}\right|=\left|\begin{array}{cc}x & 3 \\ 2 x & 5\end{array}\right|$
:::

:::solution
$\Rightarrow 10-12=5 x-6 x \quad \Rightarrow-2=-x \quad \Rightarrow x=2$
:::

:::answer
**उत्तर:** $x=2$
:::

:::

:::

:::question{number="4.1.8" kind="exercise" id="q_4.1.8" topic="MCQ: solving for x from equal determinants"}
#### प्रश्न 4.1.8

:::prompt
यदि $\left|\begin{array}{cc}x & 2 \\ 18 & x\end{array}\right|=\left|\begin{array}{cc}6 & 2 \\ 18 & 6\end{array}\right|$ हो तो $x$ बराबर है:
(A) $6$
(B) ±6
(C) -6
(D) $0$
:::

:::solution{label="हल"}
:::step{n="1" label="मान रखो"}
$$
\begin{aligned}
& \left|\begin{array}{cc}
x & 2 \\
18 & x
\end{array}\right|=\left|\begin{array}{cc}
6 & 2 \\
18 & 6
\end{array}\right| \\
& \Rightarrow x^{2}-36=36-36 \\
& \Rightarrow x^{2}=36 \\
& \Rightarrow x= \pm 6
\end{aligned}
$$
:::

:::step{n="2" label="निष्कर्ष"}
अतः, विकल्प (B) सही है।
:::
:::

:::answer
**उत्तर:** (B) ±6
:::

:::

:::question{number="4.2.1" kind="exercise" id="q_4.2.1" topic="Area of triangles from given vertices"}
#### प्रश्न 4.2.1

:::prompt
निम्नलिखित प्रत्येक में दिए गए शीर्ष बिंदुओं वाले त्रिभुजों का क्षेत्रफल ज्ञात कीजिए।
:::

:::part{label="(i)"}
:::prompt
(1, 0), (6, 0), $(4,3)$
:::

:::solution
त्रिभुज का क्षेत्रफल $=\frac{1}{2}\left|\begin{array}{lll}x_{1} & y_{1} & 1 \\ x_{2} & y_{2} & 1 \\ x_{3} & y_{3} & 1\end{array}\right|$

$A(1,0), B(6,0), C(4,3)$
त्रिभुज $A B C$ का क्षेत्रफल $=\frac{1}{2}\left|\begin{array}{lll}1 & 0 & 1 \\ 6 & 0 & 1 \\ 4 & 3 & 1\end{array}\right|$
$=\frac{1}{2}[1(0-3)-0(6-4)+1(18-0)]=\frac{1}{2}(15)=7.5$ वर्ग इकाई
:::

:::answer
**उत्तर:** $7.5$ वर्ग इकाई
:::

:::

:::part{label="(ii)"}
:::prompt
(2, 7), (1, 1), $(10,8)$
:::

:::solution
$A(2,7), B(1,1), C(10,8)$
त्रिभुज $A B C$ का क्षेत्रफल $=\frac{1}{2}\left|\begin{array}{ccc}2 & 7 & 1 \\ 1 & 1 & 1 \\ 10 & 8 & 1\end{array}\right|$
$=\frac{1}{2}[2(1-8)-7(1-10)+1(8-10)]=\frac{1}{2}(47)=25.5$ वर्ग इकाई
:::

:::answer
**उत्तर:** $25.5$ वर्ग इकाई
:::

:::

:::part{label="(iii)"}
:::prompt
(-2, -3), (3, 2), (-1, -8)
:::

:::solution
$A(-2,-3), B(3,2), C(-1,-8)$
त्रिभुज $A B C$ का क्षेत्रफल $=\frac{1}{2}\left|\begin{array}{ccc}-2 & -3 & 1 \\ 3 & 2 & 1 \\ -1 & -8 & 1\end{array}\right|$
$=\frac{1}{2}[-2(2+8)+3(3+1)+1(-24+2)]=\frac{1}{2}(-30)=-15$
त्रिभुज $A B C$ का क्षेत्रफल $=15$ वर्ग इकाई
:::

:::answer
**उत्तर:** $15$ वर्ग इकाई
:::

:::

:::

:::question{number="4.2.2" kind="exercise" id="q_4.2.2" topic="Collinearity of points via determinants" simplified="True"}
#### प्रश्न 4.2.2

:::prompt
दर्शाइए कि बिंदु $\mathrm{A}(a, b+c), \mathrm{B}(b, c+a)$ और $\mathrm{C}(c, a+b)$ संरेख हैं।
:::

:::solution{label="हल"}
यदि बिंदु $A(a, b+c), B(b, c+a)$ और $C(c, a+b)$ संरेख हैं, तो $A B C$ से बने त्रिभुज का क्षेत्रफल शून्य होगा।
त्रिभुज $A B C$ का क्षेत्रफल $=\frac{1}{2}\left|\begin{array}{lll}a & b+c & 1 \\ b & c+a & 1 \\ c & a+b & 1\end{array}\right|$

$$
\begin{array}{ll}
=\frac{1}{2}\left|\begin{array}{lll}
a & a+b+c & 1 \\
b & a+b+c & 1 \\
c & a+b+c & 1
\end{array}\right| & {\left[C_{2} \rightarrow C_{1}+C_{2} \text { द्वारा }\right]} \\
=\frac{1}{2}(a+b+c)\left|\begin{array}{lll}
a & 1 & 1 \\
b & 1 & 1 \\
c & 1 & 1
\end{array}\right| & {\left[C_{2} \text { से } a+b+c \text { उभयनिष्ठ लेने पर }\right]} \\
=0 & {\left[\because C_{1}=C_{3}\right]}
\end{array}
$$

अतः, बिंदु $A(a, b+c), B(b, c+a)$ और $C(c, a+b)$ संरेख हैं।
:::

:::

:::question{number="4.2.3" kind="exercise" id="q_4.2.3" topic="Solving for k given a triangle's area"}
#### प्रश्न 4.2.3

:::part{label="(i)"}
:::prompt
$(k, 0),(4,0),(0,2)$; त्रिभुज का क्षेत्रफल $4$ वर्ग इकाई है, $k$ का मान ज्ञात कीजिए।
:::

:::solution
$A(k, 0), B(4,0), C(0,2)$
त्रिभुज $A B C$ का क्षेत्रफल $=\frac{1}{2}\left|\begin{array}{lll}k & 0 & 1 \\ 4 & 0 & 1 \\ 0 & 2 & 1\end{array}\right|$
$=\frac{1}{2}[k(0-2)-0(4-0)+1(8-0)]=\frac{1}{2}(-2 k+8)=-k+4$
प्रश्नानुसार, त्रिभुज $A B C$ का क्षेत्रफल $=4$ वर्ग इकाई
इसलिए, $|-k+4|=4 \quad \Rightarrow-k+4= \pm 4$
$\Rightarrow-k+4=4$ या $-k+4=-4$
$\Rightarrow k=0 \quad$ या $k=8$
अतः $k$ का मान $0$ या $8$ हैं।
:::

:::answer
**उत्तर:** $k=0$ या $k=8$
:::

:::

:::part{label="(ii)"}
:::prompt
(-2, 0), (0, 4), (0, k); त्रिभुज का क्षेत्रफल $4$ वर्ग इकाई है, $k$ का मान ज्ञात कीजिए।
:::

:::solution
$A(-2,0), B(0,4), C(0, k)$
त्रिभुज $A B C$ का क्षेत्रफल $=\frac{1}{2}\left|\begin{array}{ccc}-2 & 0 & 1 \\ 0 & 4 & 1 \\ 0 & k & 1\end{array}\right|$
$=\frac{1}{2}[-2(4-k)-0(0-0)+1(0-0)]=\frac{1}{2}(-8+2 k)=-4+k$
प्रश्नानुसार, त्रिभुज $A B C$ का क्षेत्रफल $=4$ वर्ग इकाई
इसलिए, $|-4+k|=4 \quad \Rightarrow-4+k= \pm 4$
$\Rightarrow-4+k=4$ या $-4+k=-4$
$\Rightarrow k=8$ या $k=0$
अतः, $k$ का मान $0$ या $8$ हैं।
:::

:::answer
**उत्तर:** $k=0$ या $k=8$
:::

:::

:::

:::question{number="4.2.4" kind="exercise" id="q_4.2.4" topic="Equation of a line via determinants"}
#### प्रश्न 4.2.4

:::part{label="(i)"}
:::prompt
सारणिकों का प्रयोग करके $(1,2)$ और $(3,6)$ को मिलाने वाली रेखा का समीकरण ज्ञात कीजिए।
:::

:::solution
माना, $A(1,2)$ और $B(3,6)$ को मिलाने वाली रेखा पर कोई बिंदु $P(x, y)$ है। अतः बिंदु $A, \mathrm{~B}$ और $P$ संरेख होंगे और इनसे बनने वाले त्रिभुज $A \mathrm{BP}$ का क्षेत्रफल शून्य होगा।
इसलिए, त्रिभुज $A B P$ का क्षेत्रफल $=\frac{1}{2}\left|\begin{array}{lll}1 & 2 & 1 \\ 3 & 6 & 1 \\ x & y & 1\end{array}\right|=0$
$\Rightarrow \frac{1}{2}[1(6-y)-2(3-x)+1(3 y-6 x)]=0$
$\Rightarrow 6-y-6+2 x+3 y-6 x=0$
$\Rightarrow-4 x+2 y=0$
$\Rightarrow 2 x=y$
:::

:::answer
**उत्तर:** $2x=y$
:::

:::

:::part{label="(ii)"}
:::prompt
सारणिकों का प्रयोग करके $(3,1)$ और $(9,3)$ को मिलाने वाली रेखा का समीकरण ज्ञात कीजिए।
:::

:::solution
माना, $A(3,1)$ और $B(9,3)$ को मिलाने वाली रेखा पर कोई बिंदु $P(x, y)$ है। अतः, बिंदु $A, \mathrm{~B}$ और $P$ संरेख होंगे और इनसे बनने वाले त्रिभुज $A \mathrm{BP}$ का क्षेत्रफल शून्य होगा।

इसलिए, त्रिभुज $A B P$ का क्षेत्रफल $=\frac{1}{2}\left|\begin{array}{lll}3 & 1 & 1 \\ 9 & 3 & 1 \\ x & y & 1\end{array}\right|=0$

$$
\begin{aligned}
& \Rightarrow \frac{1}{2}[3(3-y)-1(9-x)+1(9 y-3 x)]=0 \\
& \Rightarrow 9-3 y-9+x+9 y-3 x=0 \\
& \Rightarrow-2 x+6 y=0 \\
& \Rightarrow x=3 y
\end{aligned}
$$
:::

:::answer
**उत्तर:** $x=3y$
:::

:::

:::

:::question{number="4.2.5" kind="exercise" id="q_4.2.5" topic="MCQ: solving for k given a triangle's area"}
#### प्रश्न 4.2.5

:::prompt
यदि शीर्ष $(2,-6),(5,4)$ और $(k, 4)$ वाले त्रिभुज का क्षेत्रफल $35$ वर्ग इकाई हो तो $k$ का मान है:
(A) $12$
(B) -2
(C) -12, -2
(D) 12, -2
:::

:::solution{label="हल"}
$$
\begin{aligned}
& A(2,-6), B(5,4), C(k, 4) \\
& \text { त्रिभुज } A B C \text { का क्षेत्रफल }=\frac{1}{2}\left|\begin{array}{ccc}
2 & -6 & 1 \\
5 & 4 & 1 \\
k & 4 & 1
\end{array}\right| \\
& =\frac{1}{2}[2(4-4)+6(5-k)+1(20-4 k)]=\frac{1}{2}(30-6 k+20-4 k)=25-5 k
\end{aligned}
$$

प्रश्नानुसार, त्रिभुज $A B C$ का क्षेत्रफल $=35$ वर्ग इकाई
इसलिए, $|25-5 k|=35 \quad \Rightarrow 25-5 k= \pm 35$

$$
\begin{aligned}
& \Rightarrow 25-5 k=35 \quad \text { या } \quad 25-5 k=-35 \\
& \Rightarrow k=\frac{-10}{5}=-2 \quad \text { या } \quad k=\frac{60}{5}=12
\end{aligned}
$$

अतः, विकल्प (D) सही है।
:::

:::answer
**उत्तर:** (D) 12, -2
:::

:::

:::question{number="4.3.1" kind="exercise" id="q_4.3.1" topic="Minors and cofactors of given determinants"}
#### प्रश्न 4.3.1

:::prompt
निम्नलिखित सारणिकों के अवयवों के उपसारणिक एवं सहखंड लिखिए।
:::

:::part{label="(i)"}
:::prompt
$\left|\begin{array}{rr}2 & -4 \\ 0 & 3\end{array}\right|$
:::

:::solution
अवयव $a_{i j}$ का उपसारणिक $M_{i j}$ है एवं $a_{i j}$ का सहखंड $A_{i j}=(-1)^{i+j} M_{i j}$ है। इसलिए, अवयव $a_{11}$ का उपसारणिक $M_{11}=3$ तथा $a_{11}$ का सहखंड $A_{11}=(-1)^{1+1} M_{11}=3$ है। अवयव $a_{12}$ का उपसारणिक $M_{12}=0$ तथा $a_{12}$ का सहखंड $A_{12}=(-1)^{1+2} M_{12}=0$ है। अवयव $a_{21}$ का उपसारणिक $M_{21}=-4$ तथा $a_{21}$ का सहखंड $A_{21}=(-1)^{2+1} M_{21}=4$ है। अवयव $a_{22}$ का उपसारणिक $M_{22}=2$ तथा $a_{22}$ का सहखंड $A_{22}=(-1)^{2+2} M_{22}=2$ है।
:::

:::

:::part{label="(ii)"}
:::prompt
$\left|\begin{array}{cc}a & c \\ b & d\end{array}\right|$
:::

:::solution
अवयव $a_{11}$ का उपसारणिक $M_{11}=d$ तथा $a_{11}$ का सहखंड $A_{11}=(-1)^{1+1} M_{11}=d$ है। अवयव $a_{12}$ का उपसारणिक $M_{12}=b$ तथा $a_{12}$ का सहखंड $A_{12}=(-1)^{1+2} M_{12}=-b$ है। अवयव $a_{21}$ का उपसारणिक $M_{21}=c$ तथा $a_{21}$ का सहखंड $A_{21}=(-1)^{2+1} M_{21}=-c$ है। अवयव $a_{22}$ का उपसारणिक $M_{22}=a$ तथा $a_{22}$ का सहखंड $A_{22}=(-1)^{2+2} M_{22}=a$ है।
:::

:::

:::

:::question{number="4.3.2" kind="exercise" id="q_4.3.2" topic="Minors and cofactors of 3x3 determinants"}
#### प्रश्न 4.3.2

:::part{label="(i)"}
:::prompt
$\left|\begin{array}{lll}1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1\end{array}\right|$
:::

:::solution
यहाँ,

$$
\begin{aligned}
& M_{11}=\left|\begin{array}{ll}
1 & 0 \\
0 & 1
\end{array}\right|=1-0=1, \quad M_{12}=\left|\begin{array}{ll}
0 & 0 \\
0 & 1
\end{array}\right|=0-0=0, \quad M_{13}=\left|\begin{array}{ll}
0 & 0 \\
0 & 1
\end{array}\right|=0-0=0 \\
& M_{21}=\left|\begin{array}{ll}
0 & 0 \\
0 & 1
\end{array}\right|=0-0=0, \quad M_{22}=\left|\begin{array}{ll}
1 & 0 \\
0 & 1
\end{array}\right|=1-0=1, \quad M_{23}=\left|\begin{array}{ll}
1 & 0 \\
0 & 0
\end{array}\right|=0-0=0 \\
& M_{31}=\left|\begin{array}{ll}
0 & 0 \\
1 & 0
\end{array}\right|=0-0=0, \quad M_{32}=\left|\begin{array}{ll}
1 & 0 \\
0 & 0
\end{array}\right|=0-0=0, \quad M_{33}=\left|\begin{array}{ll}
1 & 0 \\
0 & 1
\end{array}\right|=1-0=1
\end{aligned}
$$

एवं $A_{i j}=(-1)^{i+j} M_{i j}$, इसलिए

$$
\begin{array}{lll}
A_{11}=(-1)^{1+1} M_{11}=1 & A_{12}=(-1)^{1+2} M_{12}=0 & A_{13}=(-1)^{1+3} M_{13}=0 \\
A_{21}=(-1)^{2+1} M_{21}=0 & A_{22}=(-1)^{2+2} M_{22}=1 & A_{23}=(-1)^{2+3} M_{23}=0 \\
A_{31}=(-1)^{3+1} M_{31}=0 & A_{32}=(-1)^{3+2} M_{32}=0 & A_{33}=(-1)^{3+3} M_{33}=1
\end{array}
$$
:::

:::

:::part{label="(ii)"}
:::prompt
$\left|\begin{array}{ccc}1 & 0 & 4 \\ 3 & 5 & -1 \\ 0 & 1 & 2\end{array}\right|$
:::

:::solution
यहाँ,

$$
\begin{aligned}
& M_{11}=\left|\begin{array}{cc}
5 & -1 \\
1 & 2
\end{array}\right|=10+1=11, \quad M_{12}=\left|\begin{array}{cc}
3 & -1 \\
0 & 2
\end{array}\right|=6-0=6, \quad M_{13}=\left|\begin{array}{ll}
3 & 5 \\
0 & 1
\end{array}\right|=3-0=3 \\
& M_{21}=\left|\begin{array}{cc}
0 & 4 \\
1 & 2
\end{array}\right|=0-4=-4, \quad M_{22}=\left|\begin{array}{cc}
1 & 4 \\
0 & 2
\end{array}\right|=2-0=2, \quad M_{23}=\left|\begin{array}{ll}
1 & 0 \\
0 & 1
\end{array}\right|=1-0=1 \\
& M_{31}=\left|\begin{array}{cc}
0 & 4 \\
5 & -1
\end{array}\right|=0-20=-20, M_{32}=\left|\begin{array}{cc}
1 & 4 \\
3 & -1
\end{array}\right|=-1-12=-13, M_{33}=\left|\begin{array}{ll}
1 & 0 \\
3 & 5
\end{array}\right|=5-0=5
\end{aligned}
$$

एवं $A_{i j}=(-1)^{i+j} M_{i j}$, इसलिए

$$
\begin{array}{lll}
A_{11}=(-1)^{1+1} M_{11}=11 & A_{12}=(-1)^{1+2} M_{12}=-6 & A_{13}=(-1)^{1+3} M_{13}=3 \\
A_{21}=(-1)^{2+1} M_{21}=4 & A_{22}=(-1)^{2+2} M_{22}=2 & A_{23}=(-1)^{2+3} M_{23}=-1 \\
A_{31}=(-1)^{3+1} M_{31}=-20 & A_{32}=(-1)^{3+2} M_{32}=13 & A_{33}=(-1)^{3+3} M_{33}=5
\end{array}
$$
:::

:::

:::

:::question{number="4.3.3" kind="exercise" id="q_4.3.3" topic="Value of a determinant via second-row cofactors"}
#### प्रश्न 4.3.3

:::prompt
दूसरी पंक्ति के अवयवों के सहखंडों का प्रयोग करके $\Delta=\left|\begin{array}{lll}5 & 3 & 8 \\ 2 & 0 & 1 \\ 1 & 2 & 3\end{array}\right|$ का मान ज्ञात कीजिए।
:::

:::solution{label="हल"}
$$
\Delta=\left|\begin{array}{lll}
5 & 3 & 8 \\
2 & 0 & 1 \\
1 & 2 & 3
\end{array}\right|=a_{21} A_{21}+a_{22} A_{22}+a_{23} A_{23}
$$

यहाँ, $a_{21}=2, a_{22}=0, a_{23}=1$ तथा

$$
\begin{aligned}
& A_{21}=(-1)^{2+1}\left|\begin{array}{ll}
3 & 8 \\
2 & 3
\end{array}\right|=-(9-16)=7 \\
& A_{22}=(-1)^{2+2}\left|\begin{array}{ll}
5 & 8 \\
1 & 3
\end{array}\right|=15-8=7 \\
& A_{23}=(-1)^{2+3}\left|\begin{array}{ll}
5 & 3 \\
1 & 2
\end{array}\right|=-(10-3)=-7
\end{aligned}
$$

इसलिए, $\Delta=\left|\begin{array}{lll}5 & 3 & 8 \\ 2 & 0 & 1 \\ 1 & 2 & 3\end{array}\right|=2(7)+0(7)+1(-7)=7$
:::

:::answer
**उत्तर:** $\Delta=7$
:::

:::

:::question{number="4.3.4" kind="exercise" id="q_4.3.4" topic="Value of a symbolic determinant via third-column cofactors"}
#### प्रश्न 4.3.4

:::prompt
तीसरे स्तंभ के अवयवों के सहखंडों का प्रयोग करके $\Delta=\left|\begin{array}{lll}1 & x & y z \\ 1 & y & z x \\ 1 & z & x y\end{array}\right|$ का मान ज्ञात कीजिए।
:::

:::solution{label="हल"}
$$
\Delta=\left|\begin{array}{lll}
1 & x & y z \\
1 & y & z x \\
1 & z & x y
\end{array}\right|=a_{13} A_{13}+a_{23} A_{23}+a_{33} A_{33}
$$

यहाँ, $a_{13}=y z, a_{23}=z x, a_{33}=x y$ तथा

$$
\begin{aligned}
& A_{13}=(-1)^{1+3}\left|\begin{array}{ll}
1 & y \\
1 & z
\end{array}\right|=z-y \\
& A_{23}=(-1)^{2+3}\left|\begin{array}{ll}
1 & x \\
1 & z
\end{array}\right|=-(z-x)=x-z \\
& A_{33}=(-1)^{3+3}\left|\begin{array}{ll}
1 & x \\
1 & y
\end{array}\right|=y-x
\end{aligned}
$$

इसलिए, $\Delta=\left|\begin{array}{lll}1 & x & y z \\ 1 & y & z x \\ 1 & z & x y\end{array}\right|=y z(z-y)+z x(x-z)+x y(y-x)$
$=y z^{2}-y^{2} z+z x^{2}-x z^{2}+x y^{2}-x^{2} y$
$=z x^{2}-x^{2} y-x z^{2}+x y^{2}+y z^{2}-y^{2} z$
$=x^{2}(z-y)-x\left(z^{2}-y^{2}\right)+y z(z-y)$
$=(z-y)\left[x^{2}-x(z+y)+y z\right]$
$=(z-y)\left[x^{2}-x z-x y+y z\right]$
$=(z-y)[x(x-z)-y(x-z)]$
$=(x-z)(z-y)(x-y)$
$=(x-y)(y-z)(z-x)$
:::

:::answer
**उत्तर:** $\Delta=(x-y)(y-z)(z-x)$
:::

:::

:::question{number="4.3.5" kind="exercise" id="q_4.3.5" topic="MCQ: expansion of a determinant via cofactors" simplified="True"}
#### प्रश्न 4.3.5

:::prompt
यदि $\Delta=\left|\begin{array}{lll}a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \\ a_{31} & a_{32} & a_{33}\end{array}\right|$ और $a_{i j}$ का सहखंड $\mathrm{A}_{i j}$ हो तो $\Delta$ का मान निम्नलिखित रूप में व्यक्त किया जाता है:
(A) $a_{11} \mathrm{~A}_{31}+a_{12} \mathrm{~A}_{32}+a_{13} \mathrm{~A}_{33}$
(B) $a_{11} \mathrm{~A}_{11}+a_{12} \mathrm{~A}_{21}+a_{13} \mathrm{~A}_{31}$
(C) $a_{21} \mathrm{~A}_{11}+a_{22} \mathrm{~A}_{12}+a_{23} \mathrm{~A}_{13}$
(D) $a_{11} \mathrm{~A}_{11}+a_{21} \mathrm{~A}_{21}+a_{31} \mathrm{~A}_{31}$
:::

:::solution{label="हल"}
$\left|\begin{array}{lll}a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \\ a_{31} & a_{32} & a_{33}\end{array}\right|$ को इस प्रकार लिखा जा सकता है: $a_{11} A_{11}+a_{21} A_{21}+a_{31} A_{31}$ अतः, विकल्प (D) सही है।
:::

:::answer
**उत्तर:** (D) $a_{11} \mathrm{~A}_{11}+a_{21} \mathrm{~A}_{21}+a_{31} \mathrm{~A}_{31}$
:::

:::

:::question{number="4.4.1" kind="exercise" id="q_4.4.1" topic="Adjoint of a 2x2 matrix"}
#### प्रश्न 4.4.1

:::prompt
प्रत्येक आव्यूह का सहखंडज (adjoint) ज्ञात कीजिए: $\left[\begin{array}{ll}1 & 2 \\ 3 & 4\end{array}\right]$
:::

:::solution{label="हल"}
यहाँ, $A=\left[\begin{array}{ll}1 & 2 \\ 3 & 4\end{array}\right]$, इसलिए, $A_{11}=4 \quad A_{12}=-3 \quad A_{21}=-2 \quad A_{22}=1$
आव्यूह $A$ का सहखंडज $=\left[\begin{array}{ll}A_{11} & A_{21} \\ A_{12} & A_{22}\end{array}\right]=\left[\begin{array}{cc}4 & -2 \\ -3 & 1\end{array}\right]$
:::

:::answer
**उत्तर:** $\left[\begin{array}{cc}4 & -2 \\ -3 & 1\end{array}\right]$
:::

:::

:::question{number="4.4.2" kind="exercise" id="q_4.4.2" topic="Adjoint of a 3x3 matrix"}
#### प्रश्न 4.4.2

:::prompt
प्रत्येक आव्यूह का सहखंडज (adjoint) ज्ञात कीजिए: $\left[\begin{array}{ccc}1 & -1 & 2 \\ 2 & 3 & 5 \\ -2 & 0 & 1\end{array}\right]$
:::

:::solution{label="हल"}
यहाँ, $A=\left[\begin{array}{ccc}1 & -1 & 2 \\ 2 & 3 & 5 \\ -2 & 0 & 1\end{array}\right]$, इसलिए

$$
\begin{aligned}
& A_{11}=3 \\
& A_{21}=1 \\
& A_{31}=-11
\end{aligned}
$$

$$
\begin{aligned}
& A_{12}=-12 \\
& A_{22}=5 \\
& A_{32}=-1
\end{aligned}
$$

$$
\begin{aligned}
A_{13} & =6 \\
A_{23} & =2 \\
A_{33} & =5
\end{aligned}
$$

आव्यूह $A$ का सहखंडज $=\left[\begin{array}{lll}A_{11} & A_{21} & A_{31} \\ A_{12} & A_{22} & A_{32} \\ A_{13} & A_{23} & A_{33}\end{array}\right]=\left[\begin{array}{ccc}3 & 1 & -11 \\ -12 & 5 & -1 \\ 6 & 2 & 5\end{array}\right]$
:::

:::answer
**उत्तर:** $\left[\begin{array}{ccc}3 & 1 & -11 \\ -12 & 5 & -1 \\ 6 & 2 & 5\end{array}\right]$
:::

:::

:::question{number="4.4.3" kind="exercise" id="q_4.4.3" topic="Verifying A(adjA)=(adjA)A=|A|I for a singular matrix"}
#### प्रश्न 4.4.3

:::prompt
सत्यापित कीजिए कि $\mathrm{A}(\operatorname{adj} \mathrm{A})=(\operatorname{adj} \mathrm{A}) . \mathrm{A}=|\mathrm{A}| . \mathrm{I}$ है: $\left[\begin{array}{cc}2 & 3 \\ -4 & -6\end{array}\right]$
:::

:::solution{label="हल"}
यहाँ, $A=\left[\begin{array}{cc}2 & 3 \\ -4 & -6\end{array}\right]$,
इसलिए, $A_{11}=-6 \quad A_{12}=4$

$$
A_{21}=-3
$$

$$
A_{22}=2
$$

$|A|=-12+12=0$

$$
\operatorname{adj} A=\left[\begin{array}{ll}
A_{11} & A_{21} \\
A_{12} & A_{22}
\end{array}\right]=\left[\begin{array}{cc}
-6 & -3 \\
4 & 2
\end{array}\right]
$$

$A(\operatorname{adj} A)=\left[\begin{array}{cc}2 & 3 \\ -4 & -6\end{array}\right]\left[\begin{array}{cc}-6 & -3 \\ 4 & 2\end{array}\right]=\left[\begin{array}{cc}-12+12 & -6+6 \\ 24-24 & 12-12\end{array}\right]=\left[\begin{array}{ll}0 & 0 \\ 0 & 0\end{array}\right]$
$(\operatorname{adj} A) . A=\left[\begin{array}{cc}-6 & -3 \\ 4 & 2\end{array}\right]\left[\begin{array}{cc}2 & 3 \\ -4 & -6\end{array}\right]=\left[\begin{array}{cc}-12+12 & -18+18 \\ 8-8 & 12-12\end{array}\right]=\left[\begin{array}{ll}0 & 0 \\ 0 & 0\end{array}\right]$
$|A| . I=0 .\left[\begin{array}{ll}1 & 0 \\ 0 & 1\end{array}\right]=\left[\begin{array}{ll}0 & 0 \\ 0 & 0\end{array}\right]$
अतः, $A(\operatorname{adj} A)=(\operatorname{adj} A) . A=|A| . I=\left[\begin{array}{ll}0 & 0 \\ 0 & 0\end{array}\right]$
:::

:::

:::question{number="4.4.4" kind="exercise" id="q_4.4.4" topic="Verifying A(adjA)=(adjA)A=|A|I for a 3x3 matrix"}
#### प्रश्न 4.4.4

:::prompt
सत्यापित कीजिए कि $\mathrm{A}(\operatorname{adj} \mathrm{A})=(\operatorname{adj} \mathrm{A}) . \mathrm{A}=|\mathrm{A}| . \mathrm{I}$ है: $\left[\begin{array}{ccc}1 & -1 & 2 \\ 3 & 0 & -2 \\ 1 & 0 & 3\end{array}\right]$
:::

:::solution{label="हल"}
यहाँ, $A=\left[\begin{array}{ccc}1 & -1 & 2 \\ 3 & 0 & -2 \\ 1 & 0 & 3\end{array}\right]$, इसलिए $|A|=1(0-0)+1(9+2)+2(0-0)=11$

$$
\begin{aligned}
& A_{11}=0 \\
& A_{21}=3 \\
& A_{31}=2
\end{aligned}
$$

$$
\begin{aligned}
& A_{12}=-11 \\
& A_{22}=1 \\
& A_{32}=8
\end{aligned}
$$

$$
\begin{aligned}
A_{13} & =0 \\
A_{23} & =-1 \\
A_{33} & =3
\end{aligned}
$$

आव्यूह $A$ का सहखंडज $=\left[\begin{array}{lll}A_{11} & A_{21} & A_{31} \\ A_{12} & A_{22} & A_{32} \\ A_{13} & A_{23} & A_{33}\end{array}\right]=\left[\begin{array}{ccc}0 & 3 & 2 \\ -11 & 1 & 8 \\ 0 & -1 & 3\end{array}\right]$

$$
\begin{aligned}
& A(\operatorname{adj} A)=\left[\begin{array}{ccc}
1 & -1 & 2 \\
3 & 0 & -2 \\
1 & 0 & 3
\end{array}\right]\left[\begin{array}{ccc}
0 & 3 & 2 \\
-11 & 1 & 8 \\
0 & -1 & 3
\end{array}\right] \\
& =\left[\begin{array}{ccc}
0+11+0 & 3-1-2 & 2-8+6 \\
0+0+0 & 9+0+2 & 6+0-6 \\
0+0+0 & 3+0-3 & 2+0+9
\end{array}\right]=\left[\begin{array}{ccc}
11 & 0 & 0 \\
0 & 11 & 0 \\
0 & 0 & 11
\end{array}\right]
\end{aligned}
$$

$$
\begin{aligned}
& (\operatorname{adj} A) \cdot A=\left[\begin{array}{ccc}
0 & 3 & 2 \\
-11 & 1 & 8 \\
0 & -1 & 3
\end{array}\right]\left[\begin{array}{ccc}
1 & -1 & 2 \\
3 & 0 & -2 \\
1 & 0 & 3
\end{array}\right] \\
& =\left[\begin{array}{ccc}
0+9+2 & 0+0+0 & 0-6+6 \\
-11+3+8 & 11+0+0 & -22-2+24 \\
0-3+3 & 0+0+0 & 0+2+9
\end{array}\right]=\left[\begin{array}{ccc}
11 & 0 & 0 \\
0 & 11 & 0 \\
0 & 0 & 11
\end{array}\right]
\end{aligned}
$$

$|A| . I=11 .\left[\begin{array}{lll}1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1\end{array}\right]=\left[\begin{array}{ccc}11 & 0 & 0 \\ 0 & 11 & 0 \\ 0 & 0 & 11\end{array}\right]$
अतः, $A(\operatorname{adj} A)=(\operatorname{adj} A) . A=|A| . I=\left[\begin{array}{ccc}11 & 0 & 0 \\ 0 & 11 & 0 \\ 0 & 0 & 11\end{array}\right]$
:::

:::

:::question{number="4.4.5" kind="exercise" id="q_4.4.5" topic="Inverse of a 2x2 matrix"}
#### प्रश्न 4.4.5

:::prompt
दिए गए आव्यूह का व्युत्क्रम (जिनका अस्तित्व हो) ज्ञात कीजिए: $\left[\begin{array}{cc}2 & -2 \\ 4 & 3\end{array}\right]$
:::

:::solution{label="हल"}
यहाँ, $A=\left[\begin{array}{cc}2 & -2 \\ 4 & 3\end{array}\right]$,
इसलिए, $A_{11}=3 \quad A_{12}=-4 \quad A_{21}=2 \quad A_{22}=2$
$|A|=6+8=14 \neq 0 \Rightarrow A^{-1}$ का अस्तित्व है।

:::formula{label="मुख्य सूत्र"}
$$
A^{-1}=\frac{1}{|A|} \operatorname{adj} A=\frac{1}{|A|}\left[\begin{array}{ll}
A_{11} & A_{21} \\
A_{12} & A_{22}
\end{array}\right]=\frac{1}{14}\left[\begin{array}{cc}
3 & 2 \\
-4 & 2
\end{array}\right]
$$
:::
:::

:::answer
**उत्तर:** $A^{-1}=\frac{1}{14}\left[\begin{array}{cc}3 & 2 \\ -4 & 2\end{array}\right]$
:::

:::

:::question{number="4.4.6" kind="exercise" id="q_4.4.6" topic="Inverse of a 2x2 matrix"}
#### प्रश्न 4.4.6

:::prompt
दिए गए आव्यूह का व्युत्क्रम (जिनका अस्तित्व हो) ज्ञात कीजिए: $\left[\begin{array}{ll}-1 & 5 \\ -3 & 2\end{array}\right]$
:::

:::solution{label="हल"}
यहाँ, $A=\left[\begin{array}{ll}-1 & 5 \\ -3 & 2\end{array}\right]$,
इसलिए, $A_{11}=2 \quad A_{12}=3 \quad A_{21}=-5 \quad A_{22}=-1$
$|A|=-2+15=13 \neq 0 \quad \Rightarrow A^{-1}$ का अस्तित्व है।

:::formula{label="मुख्य सूत्र"}
$$
A^{-1}=\frac{1}{|A|} \operatorname{adj} A=\frac{1}{|A|}\left[\begin{array}{ll}
A_{11} & A_{21} \\
A_{12} & A_{22}
\end{array}\right]=\frac{1}{13}\left[\begin{array}{ll}
2 & -5 \\
3 & -1
\end{array}\right]
$$
:::
:::

:::answer
**उत्तर:** $A^{-1}=\frac{1}{13}\left[\begin{array}{ll}2 & -5 \\ 3 & -1\end{array}\right]$
:::

:::

:::question{number="4.4.7" kind="exercise" id="q_4.4.7" topic="Inverse of an upper triangular 3x3 matrix"}
#### प्रश्न 4.4.7

:::prompt
दिए गए आव्यूह का व्युत्क्रम (जिनका अस्तित्व हो) ज्ञात कीजिए: $\left[\begin{array}{lll}1 & 2 & 3 \\ 0 & 2 & 4 \\ 0 & 0 & 5\end{array}\right]$
:::

:::solution{label="हल"}
यहाँ, $A=\left[\begin{array}{lll}1 & 2 & 3 \\ 0 & 2 & 4 \\ 0 & 0 & 5\end{array}\right]$,
इसलिए $|A|=1(10-0)-2(0-0)+3(0-0)=10 \neq 0 \Rightarrow A^{-1}$ का अस्तित्व है।

$$
\begin{aligned}
& A_{11}=10 \\
& A_{21}=-10 \\
& A_{31}=2
\end{aligned}
$$

:::formula{label="मुख्य सूत्र"}
$$
\begin{array}{cc}
A_{12}=0 & A_{13}=0 \\
A_{22}=5 & A_{23}=0 \\
A_{32}=-4 & A_{33}=2 \\
A^{-1}=\frac{1}{|A|} \text { adj } A=\frac{1}{|A|}\left[\begin{array}{lll}
A_{11} & A_{21} & A_{31} \\
A_{12} & A_{22} & A_{32} \\
A_{13} & A_{23} & A_{33}
\end{array}\right]=\frac{1}{10}\left[\begin{array}{ccc}
10 & -10 & 2 \\
0 & 5 & -4 \\
0 & 0 & 2
\end{array}\right]
\end{array}
$$
:::
:::

:::answer
**उत्तर:** $A^{-1}=\frac{1}{10}\left[\begin{array}{ccc}10 & -10 & 2 \\ 0 & 5 & -4 \\ 0 & 0 & 2\end{array}\right]$
:::

:::

:::question{number="4.4.8" kind="exercise" id="q_4.4.8" topic="Inverse of a lower triangular 3x3 matrix"}
#### प्रश्न 4.4.8

:::prompt
दिए गए आव्यूह का व्युत्क्रम (जिनका अस्तित्व हो) ज्ञात कीजिए: $\left[\begin{array}{ccc}1 & 0 & 0 \\ 3 & 3 & 0 \\ 5 & 2 & -1\end{array}\right]$
:::

:::solution{label="हल"}
यहाँ, $A=\left[\begin{array}{ccc}1 & 0 & 0 \\ 3 & 3 & 0 \\ 5 & 2 & -1\end{array}\right]$,
इसलिए $|A|=1(-3-0)-0(-3-0)+0(6-15)=-3 \neq 0 \Rightarrow A^{-1}$ का अस्तित्व है।

$$
\begin{aligned}
& A_{11}=-3 \\
& A_{21}=0 \\
& A_{31}=0
\end{aligned}
$$

$$
\begin{aligned}
& A_{12}=3 \\
& A_{22}=-1 \\
& A_{32}=0
\end{aligned}
$$

$$
\begin{aligned}
A_{13} & =-9 \\
A_{23} & =-2 \\
A_{33} & =3
\end{aligned}
$$

:::formula{label="मुख्य सूत्र"}
$$
A^{-1}=\frac{1}{|A|} \text { adj } A=\frac{1}{|A|}\left[\begin{array}{lll}
A_{11} & A_{21} & A_{31} \\
A_{12} & A_{22} & A_{32} \\
A_{13} & A_{23} & A_{33}
\end{array}\right]=\frac{1}{-3}\left[\begin{array}{ccc}
-3 & 0 & 0 \\
3 & -1 & 0 \\
-9 & -2 & 3
\end{array}\right]
$$
:::
:::

:::answer
**उत्तर:** $A^{-1}=\frac{1}{-3}\left[\begin{array}{ccc}-3 & 0 & 0 \\ 3 & -1 & 0 \\ -9 & -2 & 3\end{array}\right]$
:::

:::

:::question{number="4.4.9" kind="exercise" id="q_4.4.9" topic="Inverse of a 3x3 matrix"}
#### प्रश्न 4.4.9

:::prompt
दिए गए आव्यूह का व्युत्क्रम (जिनका अस्तित्व हो) ज्ञात कीजिए: $\left[\begin{array}{ccc}2 & 1 & 3 \\ 4 & -1 & 0 \\ -7 & 2 & 1\end{array}\right]$
:::

:::solution{label="हल"}
यहाँ, $A=\left[\begin{array}{ccc}2 & 1 & 3 \\ 4 & -1 & 0 \\ -7 & 2 & 1\end{array}\right]$,
इसलिए $|A|=2(-1-0)-1(4-0)+3(8-7)=-3 \neq 0 \Rightarrow A^{-1}$ का अस्तित्व है।

$$
\begin{aligned}
& A_{11}=-1 \\
& A_{21}=5 \\
& A_{31}=3
\end{aligned}
$$

$$
\begin{aligned}
& A_{12}=-4 \\
& A_{22}=23 \\
& A_{32}=12
\end{aligned}
$$

$$
\begin{aligned}
A_{13} & =1 \\
A_{23} & =-11 \\
A_{33} & =-6
\end{aligned}
$$

:::formula{label="मुख्य सूत्र"}
$$
A^{-1}=\frac{1}{|A|} \text { adj } A=\frac{1}{|A|}\left[\begin{array}{lll}
A_{11} & A_{21} & A_{31} \\
A_{12} & A_{22} & A_{32} \\
A_{13} & A_{23} & A_{33}
\end{array}\right]=\frac{1}{-3}\left[\begin{array}{ccc}
-1 & 5 & 3 \\
-4 & 23 & 12 \\
1 & -11 & -6
\end{array}\right]
$$
:::
:::

:::answer
**उत्तर:** $A^{-1}=\frac{1}{-3}\left[\begin{array}{ccc}-1 & 5 & 3 \\ -4 & 23 & 12 \\ 1 & -11 & -6\end{array}\right]$
:::

:::

:::question{number="4.4.10" kind="exercise" id="q_4.4.10" topic="Inverse of a 3x3 matrix" simplified="True"}
#### प्रश्न 4.4.10

:::prompt
दिए गए आव्यूह का व्युत्क्रम (जिनका अस्तित्व हो) ज्ञात कीजिए: $\left[\begin{array}{ccc}1 & -1 & 2 \\ 0 & 2 & -3 \\ 3 & -2 & 4\end{array}\right]$
:::

:::solution{label="हल"}
यहाँ $A=\left[\begin{array}{ccc}1 & -1 & 2 \\ 0 & 2 & -3 \\ 3 & -2 & 4\end{array}\right]$ है।
इसलिए $|A|=1(8-6)+1(0+9)+2(0-6)=-1 \neq 0 \Rightarrow A^{-1}$ का अस्तित्व है।

$$
\begin{aligned}
& A_{11}=2 \\
& A_{21}=0 \\
& A_{31}=-1
\end{aligned}
$$

$$
\begin{aligned}
& A_{12}=-9 \\
& A_{22}=-2 \\
& A_{32}=3
\end{aligned}
$$

$$
\begin{aligned}
A_{13} & =-6 \\
A_{23} & =-1 \\
A_{33} & =2
\end{aligned}
$$

$$
A^{-1}=\frac{1}{|A|} \text { adj } A=\frac{1}{|A|}\left[\begin{array}{lll}
A_{11} & A_{21} & A_{31} \\
A_{12} & A_{22} & A_{32} \\
A_{13} & A_{23} & A_{33}
\end{array}\right]=\frac{1}{-1}\left[\begin{array}{ccc}
2 & 0 & -1 \\
-9 & -2 & 3 \\
-6 & -1 & 2
\end{array}\right]=\left[\begin{array}{ccc}
-2 & 0 & 1 \\
9 & 2 & -3 \\
6 & 1 & -2
\end{array}\right]
$$
:::

:::answer
**उत्तर:** $A^{-1}=\left[\begin{array}{ccc}-2 & 0 & 1 \\ 9 & 2 & -3 \\ 6 & 1 & -2\end{array}\right]$
:::

:::

:::question{number="4.4.11" kind="exercise" id="q_4.4.11" topic="Inverse of a matrix with trig entries" simplified="True"}
#### प्रश्न 4.4.11

:::prompt
दिए गए आव्यूह का व्युत्क्रम (जिनका अस्तित्व हो) ज्ञात कीजिए: $\left[\begin{array}{ccc}1 & 0 & 0 \\ 0 & \cos \alpha & \sin \alpha \\ 0 & \sin \alpha & -\cos \alpha\end{array}\right]$
:::

:::solution{label="हल"}
यहाँ $A=\left[\begin{array}{ccc}1 & 0 & 0 \\ 0 & \cos \alpha & \sin \alpha \\ 0 & \sin \alpha & -\cos \alpha\end{array}\right]$ है। इसलिए:

$$
\begin{aligned}
& |A|=1\left(-\cos ^{2} \alpha-\sin ^{2} \alpha\right)+0(0-0)+0(0-0)=-1 \neq 0 \Rightarrow A^{-1} \text { का अस्तित्व है। } \\
& A_{11}=1 \quad A_{12}=0 \quad A_{13}=0 \\
& A_{21}=0 \quad A_{22}=-\cos \alpha \quad A_{23}=-\sin \alpha \\
& A_{31}=0 \quad A_{32}=-\sin \alpha \quad A_{33}=\cos \alpha \\
& A^{-1}=\frac{1}{|A|} a d j A=\frac{1}{|A|}\left[\begin{array}{ccc}
A_{11} & A_{21} & A_{31} \\
A_{12} & A_{22} & A_{32} \\
A_{13} & A_{23} & A_{33}
\end{array}\right]=\frac{1}{-1}\left[\begin{array}{ccc}
1 & 0 & 0 \\
0 & -\cos \alpha & -\sin \alpha \\
0 & -\sin \alpha & \cos \alpha
\end{array}\right] \\
& \Rightarrow A^{-1}=\left[\begin{array}{ccc}
-1 & 0 & 0 \\
0 & \cos \alpha & \sin \alpha \\
0 & \sin \alpha & -\cos \alpha
\end{array}\right]
\end{aligned}
$$
:::

:::answer
**उत्तर:** $A^{-1}=\left[\begin{array}{ccc}-1 & 0 & 0 \\ 0 & \cos \alpha & \sin \alpha \\ 0 & \sin \alpha & -\cos \alpha\end{array}\right]$
:::

:::

:::question{number="4.4.12" kind="exercise" id="q_4.4.12" topic="Verifying (AB)^-1 = B^-1 A^-1" simplified="True" corrections_applied="1"}
#### प्रश्न 4.4.12

:::prompt
यदि $\mathrm{A}=\left[\begin{array}{ll}3 & 7 \\ 2 & 5\end{array}\right]$ और $\mathrm{B}=\left[\begin{array}{ll}6 & 8 \\ 7 & 9\end{array}\right]$ है तो सत्यापित कीजिए कि $(\mathrm{AB})^{-1}=\mathrm{B}^{-1} \mathrm{~A}^{-1}$ है।
:::

:::solution{label="हल"}
यहाँ $A=\left[\begin{array}{ll}3 & 7 \\ 2 & 5\end{array}\right]$ है। इसलिए $A_{11}=5 \quad A_{12}=-2 \quad A_{21}=-7 \quad A_{22}=3$
$|A|=15-14=1 \neq 0 \quad \Rightarrow A^{-1}$ का अस्तित्व है।

$$
A^{-1}=\frac{1}{|A|} \operatorname{adj} A=\frac{1}{|A|}\left[\begin{array}{ll}
A_{11} & A_{21} \\
A_{12} & A_{22}
\end{array}\right]=\frac{1}{1}\left[\begin{array}{cc}
5 & -7 \\
-2 & 3
\end{array}\right]=\left[\begin{array}{cc}
5 & -7 \\
-2 & 3
\end{array}\right]
$$

और $B=\left[\begin{array}{ll}6 & 8 \\ 7 & 9\end{array}\right]$ है। इसलिए $B_{11}=9 \quad B_{12}=-7 \quad B_{21}=-8 \quad B_{22}=6$
$|A|=54-56=-2 \neq 0 \quad \Rightarrow B^{-1}$ का अस्तित्व है।

$$
\begin{gathered}
B^{-1}=\frac{1}{|B|} \text { adj } B=\frac{1}{|B|}\left[\begin{array}{ll}
B_{11} & B_{21} \\
B_{12} & B_{22}
\end{array}\right]=\frac{1}{-2}\left[\begin{array}{cc}
9 & -8 \\
-7 & 6
\end{array}\right]=\left[\begin{array}{cc}
-9 / 2 & 4 \\
7 / 2 & -3
\end{array}\right] \\
B^{-1} A^{-1}=\left[\begin{array}{cc}
-9 / 2 & 4 \\
7 / 2 & -3
\end{array}\right]\left[\begin{array}{cc}
5 & -7 \\
-2 & 3
\end{array}\right]=\left[\begin{array}{cc}
-\frac{45}{2}-8 & \frac{63}{2}+12 \\
\frac{35}{2}+6 & -\frac{49}{2}-9
\end{array}\right]=\left[\begin{array}{cc}
-\frac{61}{2} & \frac{87}{2} \\
\frac{47}{2} & -\frac{67}{2}
\end{array}\right] \\
A B=\left[\begin{array}{ll}
3 & 7 \\
2 & 5
\end{array}\right]\left[\begin{array}{cc}
6 & 8 \\
7 & 9
\end{array}\right]=\left[\begin{array}{cc}
18+49 & 24+63 \\
12+35 & 16+45
\end{array}\right]=\left[\begin{array}{cc}
67 & 87 \\
47 & 61
\end{array}\right] \\
|A B|=67 \times 61-87 \times 47=4087-4089=-2 \neq 0 \Rightarrow(A B)^{-1} \text { का अस्तित्व है। } \\
C_{11}=61 \quad C_{12}=-47 \quad C_{21}=-87 \quad C_{22}=67 \\
(A B)^{-1}=\frac{1}{|A B|} a d j A B=\frac{1}{|A B|}\left[\begin{array}{ll}
C_{11} & C_{21} \\
C_{12} & C_{22}
\end{array}\right]=\frac{1}{-2}\left[\begin{array}{cc}
61 & -87 \\
-47 & 67
\end{array}\right]=\left[\begin{array}{cc}
-\frac{61}{2} & \frac{87}{2} \\
\frac{47}{2} & -\frac{67}{2}
\end{array}\right]
\end{gathered}
$$

अतः $(A B)^{-1}=B^{-1} A^{-1}$ है।
:::

:::

:::question{number="4.4.13" kind="exercise" id="q_4.4.13" topic="Matrix polynomial equation and inverse"}
#### प्रश्न 4.4.13

:::prompt
यदि $\mathrm{A}=\left[\begin{array}{cc}3 & 1 \\ -1 & 2\end{array}\right]$ है तो दर्शाइए कि $\mathrm{A}^{2}-5 \mathrm{~A}+7 \mathrm{I}=\mathrm{O}$ है इसकी सहायता से $\mathrm{A}^{-1}$ ज्ञात कीजिए।
:::

:::solution{label="हल"}
:::step{n="1"}
LHS $=A^{2}-5 A+7 I=A A-5 A+7 I$

$$
\begin{aligned}
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
9-1 & 3+2 \\
-3-2 & -1+4
\end{array}\right]-\left[\begin{array}{cc}
15 & 5 \\
-5 & 10
\end{array}\right]+\left[\begin{array}{ll}
7 & 0 \\
0 & 7
\end{array}\right] \\
& =\left[\begin{array}{cc}
8-15+7 & 5-5+0 \\
-5+5+0 & 3-10+7
\end{array}\right]=\left[\begin{array}{ll}
0 & 0 \\
0 & 0
\end{array}\right]=0=\text { RHS } \\
& \Rightarrow A^{2}-5 A+7 I=0 \quad \Rightarrow A^{2}-5 A=-7 I
\end{aligned}
$$
:::

:::step{n="2"}
दोनों ओर $A^{-1}$ से उत्तर गुणन करने पर (क्योंकि $|A| \neq 0$ )

$$
\begin{aligned}
& A A A^{-1}-5 A A^{-1}=-7 I A^{-1} \\
& \Rightarrow A I-5 I=-7 A^{-1} \\
& \Rightarrow 7 A^{-1}=5 I-A=5\left[\begin{array}{ll}
1 & 0 \\
0 & 1
\end{array}\right]-\left[\begin{array}{cc}
3 & 1 \\
-1 & 2
\end{array}\right]=\left[\begin{array}{ll}
5 & 0 \\
0 & 5
\end{array}\right]-\left[\begin{array}{cc}
3 & 1 \\
-1 & 2
\end{array}\right]=\left[\begin{array}{cc}
2 & -1 \\
1 & 3
\end{array}\right] \\
& \Rightarrow A^{-1}=\frac{1}{7}\left[\begin{array}{cc}
2 & -1 \\
1 & 3
\end{array}\right]
\end{aligned}
$$
:::
:::

:::answer
**उत्तर:** $A^{-1}=\frac{1}{7}\left[\begin{array}{cc}2 & -1 \\ 1 & 3\end{array}\right]$
:::

:::

:::question{number="4.4.14" kind="exercise" id="q_4.4.14" topic="Finding constants a, b for a matrix polynomial" simplified="True"}
#### प्रश्न 4.4.14

:::prompt
आव्यूह $\mathrm{A}=\left[\begin{array}{ll}3 & 2 \\ 1 & 1\end{array}\right]$ के लिए $a$ और $b$ ऐसी संख्याएँ ज्ञात कीजिए ताकि

$$
\mathrm{A}^{2}+a \mathrm{~A}+b \mathrm{I}=\mathrm{O} \text { हो। }
$$
:::

:::solution{label="हल"}
दिया है: $A^{2}+a A+b I=O$

$$
\begin{aligned}
& \Rightarrow\left[\begin{array}{ll}
3 & 2 \\
1 & 1
\end{array}\right]\left[\begin{array}{ll}
3 & 2 \\
1 & 1
\end{array}\right]+a\left[\begin{array}{ll}
3 & 2 \\
1 & 1
\end{array}\right]+b\left[\begin{array}{ll}
1 & 0 \\
0 & 1
\end{array}\right]=\left[\begin{array}{ll}
0 & 0 \\
0 & 0
\end{array}\right] \\
& \Rightarrow\left[\begin{array}{cc}
9+2 & 6+2 \\
3+1 & 2+1
\end{array}\right]+\left[\begin{array}{cc}
3 a & 2 a \\
a & a
\end{array}\right]+\left[\begin{array}{ll}
b & 0 \\
0 & b
\end{array}\right]=\left[\begin{array}{ll}
0 & 0 \\
0 & 0
\end{array}\right] \\
& \Rightarrow\left[\begin{array}{cc}
11+3 a+b & 8+2 a+0 \\
4+a+0 & 3+a+b
\end{array}\right]=\left[\begin{array}{ll}
0 & 0 \\
0 & 0
\end{array}\right] \\
& \Rightarrow 4+a=0 \Rightarrow a=-4 \quad \text { और } \quad 3+a+b=0 \Rightarrow b=-3-a=-3+4=1
\end{aligned}
$$

अतः $a=-4, b=1$
:::

:::answer
**उत्तर:** $a=-4, b=1$
:::

:::

:::question{number="4.4.15" kind="exercise" id="q_4.4.15" topic="Matrix polynomial equation for a 3x3 matrix"}
#### प्रश्न 4.4.15

:::prompt
आव्यूह $\mathrm{A}=\left[\begin{array}{ccc}1 & 1 & 1 \\ 1 & 2 & -3 \\ 2 & -1 & 3\end{array}\right]$ के लिए दर्शाइए कि $\mathrm{A}^{3}-6 \mathrm{~A}^{2}+5 \mathrm{~A}+11 \mathrm{I}=\mathrm{O}$ है। इसकी सहायता से $\mathrm{A}^{-1}$ ज्ञात कीजिए।
:::

:::solution{label="हल"}
:::step{n="1"}
$$
\begin{aligned}
& A^{2}=A \cdot A=\left[\begin{array}{ccc}
1 & 1 & 1 \\
1 & 2 & -3 \\
2 & -1 & 3
\end{array}\right]\left[\begin{array}{ccc}
1 & 1 & 1 \\
1 & 2 & -3 \\
2 & -1 & 3
\end{array}\right] \\
& =\left[\begin{array}{ccc}
1+1+2 & 1+2-1 & 1-3+3 \\
1+2-6 & 1+4+3 & 1-6-9 \\
2-1+6 & 2-2-3 & 2+3+9
\end{array}\right]=\left[\begin{array}{ccc}
4 & 2 & 1 \\
-3 & 8 & -14 \\
7 & -3 & 14
\end{array}\right] \\
& A^{3}=A^{2} \cdot A=\left[\begin{array}{ccc}
4 & 2 & 1 \\
-3 & 8 & -14 \\
7 & -3 & 14
\end{array}\right]\left[\begin{array}{ccc}
1 & 1 & 1 \\
1 & 2 & -3 \\
2 & -1 & 3
\end{array}\right] \\
& =\left[\begin{array}{ccc}
4+2+2 & 4+4-1 & 4-6+3 \\
-3+8-28 & -3+16+14 & -3-24-42 \\
7-3+28 & 7-6-14 & 7+9+42
\end{array}\right]=\left[\begin{array}{ccc}
8 & 7 & 1 \\
-23 & 27 & -69 \\
32 & -13 & 58
\end{array}\right] \\
& \text { LHS }=A^{3}-6 A^{2}+5 A+11 I \\
& =\left[\begin{array}{ccc}
8 & 7 & 1 \\
-23 & 27 & -69 \\
32 & -13 & 58
\end{array}\right]-6\left[\begin{array}{ccc}
4 & 2 & 1 \\
-3 & 8 & -14 \\
7 & -3 & 14
\end{array}\right]+5\left[\begin{array}{ccc}
1 & 1 & 1 \\
1 & 2 & -3 \\
2 & -1 & 3
\end{array}\right]+11\left[\begin{array}{ccc}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{array}\right] \\
& =\left[\begin{array}{ccc}
8 & 7 & 1 \\
-23 & 27 & -69 \\
32 & -13 & 58
\end{array}\right]-\left[\begin{array}{ccc}
24 & 12 & 6 \\
-18 & 48 & -84 \\
42 & -18 & 84
\end{array}\right]+\left[\begin{array}{ccc}
5 & 5 & 5 \\
5 & 10 & -15 \\
10 & -5 & 15
\end{array}\right]+\left[\begin{array}{ccc}
11 & 0 & 0 \\
0 & 11 & 0 \\
0 & 0 & 11
\end{array}\right] \\
& =\left[\begin{array}{ccc}
8-24+5+11 & 7-12+5+0 & 1-6+5+0 \\
-23+18+5+0 & 27-48+10+11 & -69+84-15+0 \\
32-42+10+0 & -13+18-5+0 & 58-84+15+11
\end{array}\right] \\
& =\left[\begin{array}{ccc}
0 & 0 & 0 \\
0 & 0 & 0 \\
0 & 0 & 0
\end{array}\right]=0=\text { RHS } \\
& \Rightarrow A^{3}-6 A^{2}+5 A+11 I=O
\end{aligned}
$$
:::

:::step{n="2"}
दोनों ओर $A^{-1}$ से उत्तर गुणन करने पर (क्योंकि $|A| \neq 0$ )

$$
\begin{aligned}
& A^{2} A A^{-1}-6 A A A^{-1}+5 A A^{-1}=-11 I A^{-1} \\
& \Rightarrow A^{2} I-6 A I+5 I=-11 A^{-1} \\
& \Rightarrow 11 A^{-1}=-A^{2}+6 A-5 I \\
& \Rightarrow 11 A^{-1}=-\left[\begin{array}{ccc}
4 & 2 & 1 \\
-3 & 8 & -14 \\
7 & -3 & 14
\end{array}\right]+6\left[\begin{array}{ccc}
1 & 1 & 1 \\
1 & 2 & -3 \\
2 & -1 & 3
\end{array}\right]-5\left[\begin{array}{lll}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{array}\right] \\
& \Rightarrow 11 A^{-1}=\left[\begin{array}{ccc}
-4 & -2 & -1 \\
3 & -8 & 14 \\
-7 & 3 & -14
\end{array}\right]+\left[\begin{array}{ccc}
6 & 6 & 6 \\
6 & 12 & -18 \\
12 & -6 & 18
\end{array}\right]-\left[\begin{array}{ccc}
5 & 0 & 0 \\
0 & 5 & 0 \\
0 & 0 & 5
\end{array}\right] \\
& \Rightarrow 11 A^{-1}=\left[\begin{array}{ccc}
-4+6-5 & -2+6+0 & -1+6+0 \\
3+6-0 & -8+12-5 & 14-18+0 \\
-7+12+0 & 3-6+0 & -14+18-5
\end{array}\right]=\left[\begin{array}{ccc}
-3 & 4 & 5 \\
9 & -1 & -4 \\
5 & -3 & -1
\end{array}\right] \\
& \Rightarrow A^{-1}=\frac{1}{11}\left[\begin{array}{ccc}
-3 & 4 & 5 \\
9 & -1 & -4 \\
5 & -3 & -1
\end{array}\right]
\end{aligned}
$$
:::
:::

:::answer
**उत्तर:** $A^{-1}=\frac{1}{11}\left[\begin{array}{ccc}-3 & 4 & 5 \\ 9 & -1 & -4 \\ 5 & -3 & -1\end{array}\right]$
:::

:::

:::question{number="4.4.16" kind="exercise" id="q_4.4.16" topic="Verifying a matrix polynomial identity for a 3x3 matrix"}
#### प्रश्न 4.4.16

:::prompt
यदि $\mathrm{A}=\left[\begin{array}{ccc}2 & -1 & 1 \\ -1 & 2 & -1 \\ 1 & -1 & 2\end{array}\right]$, तो सत्यापित कीजिए कि $\mathrm{A}^{3}-6 \mathrm{~A}^{2}+9 \mathrm{~A}-4 \mathrm{I}=\mathrm{O}$ है तथा इसकी सहायता से $\mathrm{A}^{-1}$ ज्ञात कीजिए।
:::

:::solution{label="हल"}
:::step{n="1"}
$$
\begin{aligned}
& A^{2}=A \cdot A=\left[\begin{array}{ccc}
2 & -1 & 1 \\
-1 & 2 & -1 \\
1 & -1 & 2
\end{array}\right]\left[\begin{array}{ccc}
2 & -1 & 1 \\
-1 & 2 & -1 \\
1 & -1 & 2
\end{array}\right] \\
& =\left[\begin{array}{ccc}
4+1+1 & -2-2-1 & 2+1+2 \\
-2-2-1 & 1+4+1 & -1-2-2 \\
2+1+2 & -1-2-2 & 1+1+4
\end{array}\right]=\left[\begin{array}{ccc}
6 & -5 & 5 \\
-5 & 6 & -5 \\
5 & -5 & 6
\end{array}\right] \\
& A^{3}=A^{2} \cdot A=\left[\begin{array}{ccc}
6 & -5 & 5 \\
-5 & 6 & -5 \\
5 & -5 & 6
\end{array}\right]\left[\begin{array}{ccc}
2 & -1 & 1 \\
-1 & 2 & -1 \\
1 & -1 & 2
\end{array}\right] \\
& =\left[\begin{array}{ccc}
12+5+5 & -6-10-5 & 6+5+10 \\
-10-6-5 & 5+12+5 & -5-6-10 \\
10+5+6 & -5-10-6 & 5+5+12
\end{array}\right]=\left[\begin{array}{ccc}
22 & -21 & 21 \\
-21 & 22 & -21 \\
21 & -21 & 22
\end{array}\right] \\
& \text { LHS }=A^{3}-6 A^{2}+9 A-4 I \\
& =\left[\begin{array}{ccc}
22 & -21 & 21 \\
-21 & 22 & -21 \\
21 & -21 & 22
\end{array}\right]-6\left[\begin{array}{ccc}
6 & -5 & 5 \\
-5 & 6 & -5 \\
5 & -5 & 6
\end{array}\right]+9\left[\begin{array}{ccc}
2 & -1 & 1 \\
-1 & 2 & -1 \\
1 & -1 & 2
\end{array}\right]-4\left[\begin{array}{ccc}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{array}\right] \\
& =\left[\begin{array}{ccc}
22 & -21 & 21 \\
-21 & 22 & -21 \\
21 & -21 & 22
\end{array}\right]-\left[\begin{array}{ccc}
36 & -30 & 30 \\
-30 & 36 & -30 \\
30 & -30 & 36
\end{array}\right]+\left[\begin{array}{ccc}
18 & -9 & 9 \\
-9 & 18 & -9 \\
9 & -9 & 18
\end{array}\right]-\left[\begin{array}{ccc}
4 & 0 & 0 \\
0 & 4 & 0 \\
0 & 0 & 4
\end{array}\right] \\
& =\left[\begin{array}{ccc}
22-36+18-4 & -21+30-9+0 & 21-30+9+0 \\
-21+30-9-0 & 22-36+18-4 & -21+30-9+0 \\
21-30+9-0 & -21+30-9-0 & 22-36+18-4
\end{array}\right] \\
& =\left[\begin{array}{ccc}
0 & 0 & 0 \\
0 & 0 & 0 \\
0 & 0 & 0
\end{array}\right]=0=\mathrm{RHS} \\
& \Rightarrow A^{3}-6 A^{2}+9 A-4 I=O \quad \Rightarrow A^{3}-6 A^{2}+9 A=4 I
\end{aligned}
$$
:::

:::step{n="2"}
दोनों ओर $A^{-1}$ से उत्तर गुणन करने पर (क्योंकि $|A| \neq 0$ )

$$
\begin{aligned}
& A^{2} A A^{-1}-6 A A A^{-1}+9 A A^{-1}=4 I A^{-1} \\
& \left.\Rightarrow A^{2} I-6 A I+9 I=4 A^{-1} \quad \text { [क्योंकि } A A^{-1}=I\right] \\
& \Rightarrow 4 A^{-1}=A^{2}-6 A+9 I \\
& \Rightarrow 4 A^{-1}=\left[\begin{array}{ccc}
6 & -5 & 5 \\
-5 & 6 & -5 \\
5 & -5 & 6
\end{array}\right]-6\left[\begin{array}{ccc}
2 & -1 & 1 \\
-1 & 2 & -1 \\
1 & -1 & 2
\end{array}\right]+9\left[\begin{array}{ccc}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{array}\right] \\
& \Rightarrow 4 A^{-1}=\left[\begin{array}{ccc}
6 & -5 & 5 \\
-5 & 6 & -5 \\
5 & -5 & 6
\end{array}\right]-\left[\begin{array}{ccc}
12 & -6 & 6 \\
-6 & 12 & -6 \\
6 & -6 & 12
\end{array}\right]+\left[\begin{array}{ccc}
9 & 0 & 0 \\
0 & 9 & 0 \\
0 & 0 & 9
\end{array}\right] \\
& \Rightarrow 4 A^{-1}=\left[\begin{array}{ccc}
6-12+9 & -5+6+0 & 5-6+0 \\
-5+6+0 & 6-12+9 & -5+6+0 \\
5-6+0 & -5+6+0 & 6-12+9
\end{array}\right]=\left[\begin{array}{ccc}
3 & 1 & -1 \\
1 & 3 & 1 \\
-1 & 1 & 3
\end{array}\right] \\
& \Rightarrow A^{-1}=\frac{1}{4}\left[\begin{array}{ccc}
3 & 1 & -1 \\
1 & 3 & 1 \\
-1 & 1 & 3
\end{array}\right]
\end{aligned}
$$
:::
:::

:::answer
**उत्तर:** $A^{-1}=\frac{1}{4}\left[\begin{array}{ccc}3 & 1 & -1 \\ 1 & 3 & 1 \\ -1 & 1 & 3\end{array}\right]$
:::

:::

:::question{number="4.4.17" kind="exercise" id="q_4.4.17" topic="MCQ: value of |adj A| for a 3x3 matrix" simplified="True"}
#### प्रश्न 4.4.17

:::prompt
यदि $\mathrm{A}, 3 \times 3$ कोटि का वर्ग आव्यूह है तो $|\operatorname{adj} \mathrm{Al}|$ का मान है:
(A) $|\mathrm{A}|$
(B) $|\mathrm{A}|^{2}$
(C) $|\mathrm{A}|^{3}$
(D) $3|\mathrm{~A}|$
:::

:::solution{label="हल"}
हम जानते हैं कि $\operatorname{adj} A=|A| I$

$$
\Rightarrow(\operatorname{adj} A) A=|A|\left[\begin{array}{lll}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{array}\right] \Rightarrow|(\operatorname{adj} A) A|=|A|\left|\begin{array}{lll}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{array}\right|=\left|\begin{array}{ccc}
|A| & 0 & 0 \\
0 & |A| & 0 \\
0 & 0 & |A|
\end{array}\right|=|A|^{3}
$$

$\Rightarrow|\operatorname{adj} A|=|A|^{2}$। अतः विकल्प (B) सही है।
:::

:::answer
**उत्तर:** (B) $|\mathrm{A}|^{2}$
:::

:::

:::question{number="4.4.18" kind="exercise" id="q_4.4.18" topic="MCQ: det(A^-1) for an invertible 2x2 matrix" simplified="True"}
#### प्रश्न 4.4.18

:::prompt
यदि A कोटि दो का व्युत्क्रमीय आव्यूह है तो $\operatorname{det}\left(\mathrm{A}^{-1}\right)$ बराबर:
(A) $\operatorname{det}(\mathrm{A})$
(B) $\frac{1}{\operatorname{det}(\mathrm{~A})}$
(C) $1$
(D) $0$
:::

:::solution{label="हल"}
दिया है: A व्युत्क्रमीय आव्यूह है। अतः $A^{-1}=\frac{1}{|A|} \operatorname{adj} A$
A कोटि दो का आव्यूह है, माना $A=\left[\begin{array}{ll}a & b \\ c & d\end{array}\right]$
इसलिए $|A|=a d-b c$ तथा $a d j A=\left[\begin{array}{cc}d & -b \\ -c & a\end{array}\right]$

$$
\begin{aligned}
& A^{-1}=\frac{1}{|A|} \text { adj } A=A^{-1}=\frac{1}{|A|}\left[\begin{array}{cc}
d & -b \\
-c & a
\end{array}\right]=\left[\begin{array}{cc}
\frac{d}{|A|} & -\frac{b}{|A|} \\
-\frac{c}{|A|} & \frac{a}{|A|}
\end{array}\right] \\
& \operatorname{det}\left(A^{-1}\right)=\left|A^{-1}\right|=\left|\begin{array}{cc}
\frac{d}{|A|} & -\frac{b}{|A|} \\
-\frac{c}{|A|} & \frac{a}{|A|}
\end{array}\right| \\
& =\frac{1}{|A|^{2}}\left|\begin{array}{cc}
d & -b \\
-c & a
\end{array}\right|=\frac{1}{|A|^{2}}(a d-b c)=\frac{1}{|A|^{2}}|A|=\frac{1}{|A|}
\end{aligned}
$$

अतः विकल्प (B) सही है।
:::

:::answer
**उत्तर:** (B) $\frac{1}{\operatorname{det}(\mathrm{~A})}$
:::

:::

:::question{number="4.5.1" kind="exercise" id="q_4.5.1" topic="Classifying a system as consistent/inconsistent" simplified="True"}
#### प्रश्न 4.5.1

:::prompt
निम्नलिखित समीकरण निकाय का संगत अथवा असंगत के रूप में वर्गीकरण कीजिए:

$$
\begin{aligned}
& x+2 y=2 \\
& 2 x+3 y=3
\end{aligned}
$$
:::

:::solution{label="हल"}
समीकरण निकाय को $A X=B$ के रूप में लिखा जा सकता है, जहाँ

$$
A=\left[\begin{array}{ll}
1 & 2 \\
2 & 3
\end{array}\right], X=\left[\begin{array}{l}
x \\
y
\end{array}\right] \text { और } B=\left[\begin{array}{l}
2 \\
3
\end{array}\right]
$$

$|A|=3-4=-1 \neq 0 \quad \Rightarrow$ आव्यूह $A$ व्युत्क्रमणीय है। इसलिए, $A^{-1}$ का अस्तित्व है। अतः, दी गई समीकरण निकाय संगत हैं।
:::

:::answer
**उत्तर:** संगत
:::

:::

:::question{number="4.5.2" kind="exercise" id="q_4.5.2" topic="Classifying a system as consistent/inconsistent" simplified="True"}
#### प्रश्न 4.5.2

:::prompt
निम्नलिखित समीकरण निकाय का संगत अथवा असंगत के रूप में वर्गीकरण कीजिए:

$$
\begin{aligned}
& 2 x-y=5 \\
& x+y=4
\end{aligned}
$$
:::

:::solution{label="हल"}
समीकरण निकाय को $A X=B$ के रूप में लिखा जा सकता है, जहाँ

$$
A=\left[\begin{array}{cc}
2 & -1 \\
1 & 1
\end{array}\right], X=\left[\begin{array}{l}
x \\
y
\end{array}\right] \text { और } B=\left[\begin{array}{l}
5 \\
4
\end{array}\right]
$$

$|A|=2+1=3 \neq 0 \quad \Rightarrow$ आव्यूह $A$ व्युत्क्रमणीय है। इसलिए, $A^{-1}$ का अस्तित्व है। अतः, दी गई समीकरण निकाय संगत हैं।
:::

:::answer
**उत्तर:** संगत
:::

:::

:::question{number="4.5.3" kind="exercise" id="q_4.5.3" topic="Classifying a system as consistent/inconsistent"}
#### प्रश्न 4.5.3

:::prompt
निम्नलिखित समीकरण निकाय का संगत अथवा असंगत के रूप में वर्गीकरण कीजिए:

$$
\begin{aligned}
& x+3 y=5 \\
& 2 x+6 y=8
\end{aligned}
$$
:::

:::solution{label="हल"}
समीकरण निकाय को $A X=B$ के रूप में लिखा जा सकता है, जहाँ

$$
A=\left[\begin{array}{ll}
1 & 3 \\
2 & 6
\end{array}\right], X=\left[\begin{array}{l}
x \\
y
\end{array}\right] \text { और } B=\left[\begin{array}{l}
5 \\
8
\end{array}\right]
$$

$|A|=6-6=0 \quad \Rightarrow$ आव्यूह $A$ अव्युत्क्रमणीय है। इसलिए, $A^{-1}$ का अस्तित्व नहीं है।
अब, $\operatorname{adj} A=\left[\begin{array}{cc}6 & -3 \\ -2 & 1\end{array}\right]$

$$
(\operatorname{adj} A) B=\left[\begin{array}{cc}
6 & -3 \\
-2 & 1
\end{array}\right]\left[\begin{array}{l}
5 \\
8
\end{array}\right]=\left[\begin{array}{c}
30-24 \\
-10+8
\end{array}\right]=\left[\begin{array}{c}
6 \\
-2
\end{array}\right] \neq 0
$$

इसलिए, दी गई समीकरण निकाय का कोई हल नहीं है।
अतः, दी गई समीकरण निकाय असंगत हैं।
:::

:::answer
**उत्तर:** असंगत
:::

:::

:::question{number="4.5.4" kind="exercise" id="q_4.5.4" topic="Classifying a system as consistent/inconsistent"}
#### प्रश्न 4.5.4

:::prompt
निम्नलिखित समीकरण निकाय का संगत अथवा असंगत के रूप में वर्गीकरण कीजिए:

$$
\begin{aligned}
& x+y+z=1 \\
& 2 x+3 y+2 z=2 \\
& a x+a y+2 a z=4
\end{aligned}
$$
:::

:::solution{label="हल"}
समीकरण निकाय को $A X=B$ के रूप में लिखा जा सकता है, जहाँ

$$
A=\left[\begin{array}{ccc}
1 & 1 & 1 \\
2 & 3 & 2 \\
a & a & 2 a
\end{array}\right], X=\left[\begin{array}{l}
x \\
y \\
z
\end{array}\right] \text { और } B=\left[\begin{array}{l}
1 \\
2 \\
3
\end{array}\right]
$$

$|A|=1(6 a-2 a)-1(4 a-2 a)+1(2 a-3 a)=a \neq 0$
$\Rightarrow$ आव्यूह $A$ व्युत्क्रमणीय है। इसलिए, $A^{-1}$ का अस्तित्व है।
अतः, दी गई समीकरण निकाय संगत हैं।
:::

:::answer
**उत्तर:** संगत
:::

:::

:::question{number="4.5.5" kind="exercise" id="q_4.5.5" topic="Classifying a system as consistent/inconsistent"}
#### प्रश्न 4.5.5

:::prompt
निम्नलिखित समीकरण निकाय का संगत अथवा असंगत के रूप में वर्गीकरण कीजिए:

$$
\begin{aligned}
& 3 x-y-2 z=2 \\
& 2 y-z=-1 \\
& 3 x-5 y=3
\end{aligned}
$$
:::

:::solution{label="हल"}
समीकरण निकाय को $A X=B$ के रूप में लिखा जा सकता है, जहाँ

$$
A=\left[\begin{array}{ccc}
3 & -1 & -2 \\
0 & 2 & -1 \\
3 & -5 & 0
\end{array}\right], X=\left[\begin{array}{l}
x \\
y \\
z
\end{array}\right] \text { और } B=\left[\begin{array}{c}
2 \\
-1 \\
3
\end{array}\right]
$$

$|A|=3(0-5)+1(0+3)-2(0-6)=-15+3+12=0$
$\Rightarrow$ आव्यूह $A$ अव्युक्रमणीय है। इसलिए, $A^{-1}$ का अस्तित्व नहीं है। अब,

$$
\begin{aligned}
& A_{11}=-5 \\
& A_{21}=10 \\
& A_{31}=5
\end{aligned}
$$

$$
\begin{aligned}
& A_{12}=-3 \\
& A_{22}=6 \\
& A_{32}=3
\end{aligned}
$$

$$
\begin{aligned}
A_{13} & =-6 \\
A_{23} & =12 \\
A_{33} & =6
\end{aligned}
$$

$\operatorname{adj} A=\left[\begin{array}{ccc}-5 & 10 & 5 \\ -3 & 6 & 3 \\ -6 & 12 & 6\end{array}\right]$
$(\operatorname{adj} A) B=\left[\begin{array}{ccc}-5 & 10 & 5 \\ -3 & 6 & 3 \\ -6 & 12 & 6\end{array}\right]\left[\begin{array}{c}2 \\ -1 \\ 3\end{array}\right]=\left[\begin{array}{c}-10-10+15 \\ -6-6+9 \\ -12-12+16\end{array}\right]=\left[\begin{array}{l}-5 \\ -3 \\ -6\end{array}\right] \neq 0$
इसलिए, दी गई समीकरण निकाय का कोई हल नहीं है।
अतः, दी गई समीकरण निकाय असंगत हैं।
:::

:::answer
**उत्तर:** असंगत
:::

:::

:::question{number="4.5.6" kind="exercise" id="q_4.5.6" topic="Classifying a system as consistent/inconsistent"}
#### प्रश्न 4.5.6

:::prompt
निम्नलिखित समीकरण निकाय का संगत अथवा असंगत के रूप में वर्गीकरण कीजिए:

$$
\begin{aligned}
& 5 x-y+4 z=5 \\
& 2 x+3 y+5 z=2 \\
& 5 x-2 y+6 z=-1
\end{aligned}
$$
:::

:::solution{label="हल"}
समीकरण निकाय को $A X=B$ के रूप में लिखा जा सकता है, जहाँ

$$
A=\left[\begin{array}{ccc}
5 & -1 & 4 \\
2 & 3 & 5 \\
5 & -2 & 6
\end{array}\right], X=\left[\begin{array}{l}
x \\
y \\
z
\end{array}\right] \text { और } B=\left[\begin{array}{c}
5 \\
2 \\
-1
\end{array}\right]
$$

$|A|=5(18+10)+1(12-25)+4(-4-15)=140-13-76=51 \neq 0$
$\Rightarrow$ आव्यूह $A$ व्युत्क्रमणीय है। इसलिए, $A^{-1}$ का अस्तित्व है।
अतः, दी गई समीकरण निकाय संगत हैं।
:::

:::answer
**उत्तर:** संगत
:::

:::

:::question{number="4.5.7" kind="exercise" id="q_4.5.7" topic="Solving a 2x2 system via matrix method" simplified="True"}
#### प्रश्न 4.5.7

:::prompt
निम्नलिखित समीकरण निकाय को आव्यूह विधि से हल कीजिए:

$$
\begin{aligned}
& 5 x+2 y=4 \\
& 7 x+3 y=5
\end{aligned}
$$
:::

:::solution{label="हल"}
समीकरण निकाय को $A X=B$ के रूप में लिखा जा सकता है, जहाँ

$$
A=\left[\begin{array}{ll}
5 & 2 \\
7 & 3
\end{array}\right], X=\left[\begin{array}{l}
x \\
y
\end{array}\right] \text { और } B=\left[\begin{array}{l}
4 \\
5
\end{array}\right]
$$

$|A|=15-14=1 \neq 0 \quad \Rightarrow$ आव्यूह $A$ व्युत्क्रमणीय है। इसलिए, $A^{-1}$ का अस्तित्व है।
अतः, दी गई समीकरण निकाय संगत हैं।
इसलिए, $A_{11}=3 \quad A_{12}=-7 \quad A_{21}=-2 \quad A_{22}=5$

$$
A^{-1}=\frac{1}{|A|} \operatorname{adj} A=\frac{1}{|A|}\left[\begin{array}{ll}
A_{11} & A_{21} \\
A_{12} & A_{22}
\end{array}\right]=\frac{1}{1}\left[\begin{array}{cc}
3 & -2 \\
-7 & 5
\end{array}\right]
$$

$X=A^{-1} B \quad \Rightarrow\left[\begin{array}{l}x \\ y\end{array}\right]=\left[\begin{array}{cc}3 & -2 \\ -7 & 5\end{array}\right]\left[\begin{array}{l}4 \\ 5\end{array}\right]$

$$
\Rightarrow\left[\begin{array}{l}
x \\
y
\end{array}\right]=\left[\begin{array}{c}
12-10 \\
-28+25
\end{array}\right] \quad \Rightarrow\left[\begin{array}{l}
x \\
y
\end{array}\right]=\left[\begin{array}{c}
2 \\
-3
\end{array}\right] \quad \Rightarrow x=2, \quad y=-3
$$
:::

:::answer
**उत्तर:** $x=2, y=-3$
:::

:::

:::question{number="4.5.8" kind="exercise" id="q_4.5.8" topic="Solving a 2x2 system via matrix method" simplified="True"}
#### प्रश्न 4.5.8

:::prompt
निम्नलिखित समीकरण निकाय को आव्यूह विधि से हल कीजिए:

$$
\begin{aligned}
& 2 x-y=-2 \\
& 3 x+4 y=3
\end{aligned}
$$
:::

:::solution{label="हल"}
समीकरण निकाय को $A X=B$ के रूप में लिखा जा सकता है, जहाँ

$$
A=\left[\begin{array}{cc}
2 & -1 \\
3 & 4
\end{array}\right], X=\left[\begin{array}{l}
x \\
y
\end{array}\right] \text { और } B=\left[\begin{array}{c}
-2 \\
3
\end{array}\right]
$$

$|A|=8+3=11 \neq 0 \quad \Rightarrow$ आव्यूह $A$ व्युत्क्रमणीय है। इसलिए, $A^{-1}$ का अस्तित्व है। अतः, दी गई समीकरण निकाय संगत हैं।
इसलिए, $A_{11}=4 \quad A_{12}=-3 \quad A_{21}=1 \quad A_{22}=2$

$$
\begin{gathered}
A^{-1}=\frac{1}{|A|} \text { adj } A=\frac{1}{|A|}\left[\begin{array}{ll}
A_{11} & A_{21} \\
A_{12} & A_{22}
\end{array}\right]=\frac{1}{11}\left[\begin{array}{cc}
4 & 1 \\
-3 & 2
\end{array}\right] \\
X=A^{-1} B \quad \Rightarrow\left[\begin{array}{l}
x \\
y
\end{array}\right]=\frac{1}{11}\left[\begin{array}{cc}
4 & 1 \\
-3 & 2
\end{array}\right]\left[\begin{array}{c}
-2 \\
3
\end{array}\right] \\
\Rightarrow\left[\begin{array}{l}
x \\
y
\end{array}\right]=\frac{1}{11}\left[\begin{array}{c}
-8+3 \\
6+6
\end{array}\right] \quad \Rightarrow\left[\begin{array}{c}
x \\
y
\end{array}\right]=\left[\begin{array}{c}
-\frac{5}{11} \\
\frac{12}{11}
\end{array}\right] \quad \Rightarrow x=-\frac{5}{11}, \quad y=\frac{12}{11}
\end{gathered}
$$
:::

:::answer
**उत्तर:** $x=-\frac{5}{11}, y=\frac{12}{11}$
:::

:::

:::question{number="4.5.9" kind="exercise" id="q_4.5.9" topic="Solving a 2x2 system via matrix method" simplified="True"}
#### प्रश्न 4.5.9

:::prompt
निम्नलिखित समीकरण निकाय को आव्यूह विधि से हल कीजिए:

$$
\begin{aligned}
& 4 x-3 y=3 \\
& 3 x-5 y=7
\end{aligned}
$$
:::

:::solution{label="हल"}
समीकरण निकाय को $A X=B$ के रूप में लिखा जा सकता है, जहाँ

$$
A=\left[\begin{array}{ll}
4 & -3 \\
3 & -5
\end{array}\right], X=\left[\begin{array}{l}
x \\
y
\end{array}\right] \text { और } B=\left[\begin{array}{l}
3 \\
7
\end{array}\right]
$$

$|A|=-20+9=-11 \neq 0 \quad \Rightarrow$ आव्यूह $A$ व्युत्क्रमणीय है। इसलिए, $A^{-1}$ का अस्तित्व है। अतः, दी गई समीकरण निकाय संगत हैं।
इसलिए, $A_{11}=-5 \quad A_{12}=-3 \quad A_{21}=3 \quad A_{22}=4$

$$
\begin{gathered}
A^{-1}=\frac{1}{|A|} \text { adj } A=\frac{1}{|A|}\left[\begin{array}{ll}
A_{11} & A_{21} \\
A_{12} & A_{22}
\end{array}\right]=\frac{1}{-11}\left[\begin{array}{ll}
-5 & 3 \\
-3 & 4
\end{array}\right] \\
X=A^{-1} B \quad \Rightarrow\left[\begin{array}{l}
x \\
y
\end{array}\right]=-\frac{1}{11}\left[\begin{array}{ll}
-5 & 3 \\
-3 & 4
\end{array}\right]\left[\begin{array}{l}
3 \\
7
\end{array}\right] \\
\Rightarrow\left[\begin{array}{l}
x \\
y
\end{array}\right]=-\frac{1}{11}\left[\begin{array}{c}
-15+21 \\
-9+28
\end{array}\right] \quad \Rightarrow\left[\begin{array}{l}
x \\
y
\end{array}\right]=\left[\begin{array}{r}
-\frac{6}{11} \\
-\frac{19}{11}
\end{array}\right] \quad \Rightarrow x=-\frac{6}{11}, \quad y=-\frac{19}{11}
\end{gathered}
$$
:::

:::answer
**उत्तर:** $x=-\frac{6}{11}, y=-\frac{19}{11}$
:::

:::

:::question{number="4.5.10" kind="exercise" id="q_4.5.10" topic="Solving a 2x2 system via matrix method" simplified="True"}
#### प्रश्न 4.5.10

:::prompt
निम्नलिखित समीकरण निकाय को आव्यूह विधि से हल कीजिए:

$$
\begin{aligned}
& 5 x+2 y=3 \\
& 3 x+2 y=5
\end{aligned}
$$
:::

:::solution{label="हल"}
समीकरण निकाय को $A X=B$ के रूप में लिखा जा सकता है, जहाँ

$$
A=\left[\begin{array}{ll}
5 & 2 \\
3 & 2
\end{array}\right], X=\left[\begin{array}{l}
x \\
y
\end{array}\right] \text { और } B=\left[\begin{array}{l}
3 \\
5
\end{array}\right]
$$

$|A|=10-6=4 \neq 0 \quad \Rightarrow$ आव्यूह $A$ व्युत्क्रमणीय है। इसलिए, $A^{-1}$ का अस्तित्व है। अतः, दी गई समीकरण निकाय संगत हैं।
इसलिए, $A_{11}=2 \quad A_{12}=-3 \quad A_{21}=-2 \quad A_{22}=5$

$$
\begin{aligned}
& A^{-1}=\frac{1}{|A|} \text { adj } A=\frac{1}{|A|}\left[\begin{array}{ll}
A_{11} & A_{21} \\
A_{12} & A_{22}
\end{array}\right]=\frac{1}{4}\left[\begin{array}{cc}
2 & -2 \\
-3 & 5
\end{array}\right] \\
& X=A^{-1} B \quad \Rightarrow\left[\begin{array}{l}
x \\
y
\end{array}\right]=\frac{1}{4}\left[\begin{array}{cc}
2 & -2 \\
-3 & 5
\end{array}\right]\left[\begin{array}{l}
3 \\
5
\end{array}\right] \\
& \Rightarrow\left[\begin{array}{l}
x \\
y
\end{array}\right]=\frac{1}{4}\left[\begin{array}{c}
6-10 \\
-9+25
\end{array}\right] \quad \Rightarrow\left[\begin{array}{l}
x \\
y
\end{array}\right]=\left[\begin{array}{c}
-\frac{4}{4} \\
\frac{16}{4}
\end{array}\right] \quad \Rightarrow x=-1, \quad y=4
\end{aligned}
$$
:::

:::answer
**उत्तर:** $x=-1, y=4$
:::

:::

:::question{number="4.5.11" kind="exercise" id="q_4.5.11" topic="Solving a 3x3 system via matrix method"}
#### प्रश्न 4.5.11

:::prompt
निम्नलिखित समीकरण निकाय को आव्यूह विधि से हल कीजिए:

$$
\begin{aligned}
& 2 x+y+z=1 \\
& x-2 y-z=\frac{3}{2} \\
& 3 y-5 z=9
\end{aligned}
$$
:::

:::solution{label="हल"}
समीकरण निकाय को $A X=B$ के रूप में लिखा जा सकता है, जहाँ

$$
A=\left[\begin{array}{ccc}
2 & 1 & 1 \\
1 & -2 & -1 \\
0 & 3 & -5
\end{array}\right], X=\left[\begin{array}{l}
x \\
y \\
z
\end{array}\right] \text { और } B=\left[\begin{array}{c}
1 \\
3 / 2 \\
9
\end{array}\right]
$$

$|A|=2(10+3)-1(-5-0)+1(3-0)=26+5+3=34 \neq 0$
⇒ आव्यूह $A$ व्युत्क्रमणीय है। इसलिए, $A^{-1}$ का अस्तित्व है।
अतः, दी गई समीकरण निकाय संगत हैं। इसलिए,

$$
\begin{array}{lll}
A_{11}=13 & A_{12}=5 & A_{13}=3 \\
A_{21}=8 & A_{22}=-10 & A_{23}=-6 \\
A_{31}=1 & A_{32}=3 & A_{33}=-5
\end{array}
$$

$$
A^{-1}=\frac{1}{|A|} \text { adj } A=\frac{1}{34}\left[\begin{array}{ccc}
13 & 8 & 1 \\
5 & -10 & 3 \\
3 & -6 & -5
\end{array}\right]
$$

$$
X=A^{-1} B \Rightarrow\left[\begin{array}{l}
x \\
y \\
z
\end{array}\right]=\frac{1}{34}\left[\begin{array}{ccc}
13 & 8 & 1 \\
5 & -10 & 3 \\
3 & -6 & -5
\end{array}\right]\left[\begin{array}{c}
1 \\
3 / 2 \\
9
\end{array}\right] \Rightarrow\left[\begin{array}{l}
x \\
y \\
z
\end{array}\right]=\frac{1}{34}\left[\begin{array}{c}
13+12+9 \\
5-15+27 \\
3-9-45
\end{array}\right] \Rightarrow\left[\begin{array}{c}
x \\
y \\
z
\end{array}\right]=\frac{1}{34}\left[\begin{array}{c}
34 \\
17 \\
-51
\end{array}\right]=\left[\begin{array}{c}
1 \\
1 / 2 \\
-3 / 2
\end{array}\right] \Rightarrow x=1, y=\frac{1}{2}, z=-\frac{3}{2}
$$
:::

:::answer
**उत्तर:** $x=1, y=\frac{1}{2}, z=-\frac{3}{2}$
:::

:::

:::question{number="4.5.12" kind="exercise" id="q_4.5.12" topic="Solving a 3x3 system via matrix method"}
#### प्रश्न 4.5.12

:::prompt
निम्नलिखित समीकरण निकाय को आव्यूह विधि से हल कीजिए:

$$
\begin{aligned}
& x-y+z=4 \\
& 2 x+y-3 z=0 \\
& x+y+z=2
\end{aligned}
$$
:::

:::solution{label="हल"}
समीकरण निकाय को $A X=B$ के रूप में लिखा जा सकता है, जहाँ

$$
A=\left[\begin{array}{ccc}
1 & -1 & 1 \\
2 & 1 & -3 \\
1 & 1 & 1
\end{array}\right], X=\left[\begin{array}{l}
x \\
y \\
z
\end{array}\right] \text { और } B=\left[\begin{array}{l}
4 \\
0 \\
2
\end{array}\right]
$$

$$
|A|=1(1+3)+1(2+3)+1(2-1)=4+5+1=10 \neq 0
$$

$\Rightarrow$ आव्यूह $A$ व्युत्क्रमणीय है। इसलिए, $A^{-1}$ का अस्तित्व है।
अतः, दी गई समीकरण निकाय संगत हैं। इसलिए,

$$
\begin{array}{lll}
A_{11}=4 & A_{12}=-5 & A_{13}=1 \\
A_{21}=2 & A_{22}=0 & A_{23}=-2 \\
A_{31}=2 & A_{32}=5 & A_{33}=3
\end{array}
$$

$$
A^{-1}=\frac{1}{|A|} a d j A=\frac{1}{10}\left[\begin{array}{ccc}
4 & 2 & 2 \\
-5 & 0 & 5 \\
1 & -2 & 3
\end{array}\right]
$$

$$
X=A^{-1} B \quad \Rightarrow\left[\begin{array}{c}
x \\
y \\
z
\end{array}\right]=\frac{1}{10}\left[\begin{array}{ccc}
4 & 2 & 2 \\
-5 & 0 & 5 \\
1 & -2 & 3
\end{array}\right]\left[\begin{array}{c}
4 \\
0 \\
2
\end{array}\right] \Rightarrow\left[\begin{array}{l}
x \\
y \\
z
\end{array}\right]=\frac{1}{10}\left[\begin{array}{c}
16+0+4 \\
-20+0+10 \\
4+0+6
\end{array}\right] \Rightarrow\left[\begin{array}{c}
x \\
y \\
z
\end{array}\right]=\frac{1}{10}\left[\begin{array}{c}
20 \\
-10 \\
10
\end{array}\right]=\left[\begin{array}{c}
2 \\
-1 \\
1
\end{array}\right] \Rightarrow x=2, y=-1, z=1
$$
:::

:::answer
**उत्तर:** $x=2, y=-1, z=1$
:::

:::

:::question{number="4.5.13" kind="exercise" id="q_4.5.13" topic="Solving a 3x3 system via matrix method"}
#### प्रश्न 4.5.13

:::prompt
निम्नलिखित समीकरण निकाय को आव्यूह विधि से हल कीजिए:

$$
\begin{aligned}
& 2 x+3 y+3 z=5 \\
& x-2 y+z=-4 \\
& 3 x-y-2 z=3
\end{aligned}
$$
:::

:::solution{label="हल"}
समीकरण निकाय को $A X=B$ के रूप में लिखा जा सकता है, जहाँ

$$
A=\left[\begin{array}{ccc}
2 & 3 & 3 \\
1 & -2 & 1 \\
3 & -1 & -2
\end{array}\right], X=\left[\begin{array}{l}
x \\
y \\
z
\end{array}\right] \text { और } B=\left[\begin{array}{c}
5 \\
-4 \\
3
\end{array}\right]
$$

$$
|A|=2(4+1)-3(-2-3)+3(-1+6)=10+15+15=40 \neq 0
$$

$\Rightarrow$ आव्यूह $A$ व्युत्क्रमणीय है। इसलिए, $A^{-1}$ का अस्तित्व है।
अतः, दी गई समीकरण निकाय संगत हैं। इसलिए,

$$
\begin{array}{lcl}
A_{11}=5 & A_{12}=5 & A_{13}=5 \\
A_{21}=3 & A_{22}=-13 & A_{23}=11 \\
A_{31}=9 & A_{32}=1 & A_{33}=-7
\end{array}
$$

$$
A^{-1}=\frac{1}{|A|} \text { adj } A=\frac{1}{40}\left[\begin{array}{ccc}
5 & 3 & 9 \\
5 & -13 & 1 \\
5 & 11 & -7
\end{array}\right]
$$

$$
X=A^{-1} B \quad \Rightarrow\left[\begin{array}{l}
x \\
y \\
z
\end{array}\right]=\frac{1}{40}\left[\begin{array}{ccc}
5 & 3 & 9 \\
5 & -13 & 1 \\
5 & 11 & -7
\end{array}\right]\left[\begin{array}{c}
5 \\
-4 \\
3
\end{array}\right] \Rightarrow\left[\begin{array}{l}
x \\
y \\
z
\end{array}\right]=\frac{1}{40}\left[\begin{array}{c}
25-12+27 \\
25+52+3 \\
25-44-21
\end{array}\right] \Rightarrow\left[\begin{array}{c}
x \\
y \\
z
\end{array}\right]=\frac{1}{40}\left[\begin{array}{c}
40 \\
80 \\
-40
\end{array}\right]=\left[\begin{array}{c}
1 \\
2 \\
-1
\end{array}\right] \Rightarrow x=1, y=2, z=-1
$$
:::

:::answer
**उत्तर:** $x=1, y=2, z=-1$
:::

:::

:::question{number="4.5.14" kind="exercise" id="q_4.5.14" topic="Solving a 3x3 system via matrix method"}
#### प्रश्न 4.5.14

:::prompt
निम्नलिखित समीकरण निकाय को आव्यूह विधि से हल कीजिए:

$$
\begin{aligned}
& x-y+2 z=7 \\
& 3 x+4 y-5 z=-5 \\
& 2 x-y+3 z=12
\end{aligned}
$$
:::

:::solution{label="हल"}
समीकरण निकाय को $A X=B$ के रूप में लिखा जा सकता है, जहाँ

$$
A=\left[\begin{array}{ccc}
1 & -1 & 2 \\
3 & 4 & -5 \\
2 & -1 & 3
\end{array}\right], X=\left[\begin{array}{l}
x \\
y \\
z
\end{array}\right] \text { और } B=\left[\begin{array}{c}
7 \\
-5 \\
12
\end{array}\right]
$$

$|A|=1(12-5)+1(9+10)+2(-3-8)=7+19-22=4 \neq 0$
$\Rightarrow$ आव्यूह $A$ व्युत्क्रमणीय है। इसलिए, $A^{-1}$ का अस्तित्व है।
अतः, दी गई समीकरण निकाय संगत हैं। इसलिए,

$$
\begin{array}{lcl}
A_{11}=7 & A_{12}=-19 & A_{13}=-11 \\
A_{21}=1 & A_{22}=-1 & A_{23}=-1 \\
A_{31}=-3 & A_{32}=11 & A_{33}=7
\end{array}
$$

$$
A^{-1}=\frac{1}{|A|} \operatorname{adj} A=\frac{1}{4}\left[\begin{array}{ccc}
7 & 1 & -3 \\
-19 & -1 & 11 \\
-11 & -1 & 7
\end{array}\right]
$$

$$
X=A^{-1} B \quad \Rightarrow\left[\begin{array}{c}
x \\
y \\
z
\end{array}\right]=\frac{1}{4}\left[\begin{array}{ccc}
7 & 1 & -3 \\
-19 & -1 & 11 \\
-11 & -1 & 7
\end{array}\right]\left[\begin{array}{c}
7 \\
-5 \\
12
\end{array}\right] \Rightarrow\left[\begin{array}{l}
x \\
y \\
z
\end{array}\right]=\frac{1}{4}\left[\begin{array}{c}
49-5-36 \\
-133+5+132 \\
-77+5+84
\end{array}\right] \Rightarrow\left[\begin{array}{c}
x \\
y \\
z
\end{array}\right]=\frac{1}{4}\left[\begin{array}{c}
4 \\
4 \\
12
\end{array}\right]=\left[\begin{array}{l}
1 \\
1 \\
3
\end{array}\right] \Rightarrow x=1, y=1, z=3
$$
:::

:::answer
**उत्तर:** $x=1, y=1, z=3$
:::

:::

:::question{number="4.5.15" kind="exercise" id="q_4.5.15" topic="Finding A^-1 and using it to solve a 3x3 system"}
#### प्रश्न 4.5.15

:::prompt
यदि $\mathrm{A}=\left[\begin{array}{ccc}2 & -3 & 5 \\ 3 & 2 & -4 \\ 1 & 1 & -2\end{array}\right]$ है तो $\mathrm{A}^{-1}$ ज्ञात कीजिए। $\mathrm{A}^{-1}$ का प्रयोग करके निम्नलिखित समीकरण निकाय को हल कीजिए।

$$
\begin{aligned}
& 2 x-3 y+5 z=11 \\
& 3 x+2 y-4 z=-5 \\
& x+y-2 z=-3
\end{aligned}
$$
:::

:::solution{label="हल"}
$$
A=\left[\begin{array}{ccc}
2 & -3 & 5 \\
3 & 2 & -4 \\
1 & 1 & -2
\end{array}\right]
$$

$|A|=2(-4+4)+3(-6+4)+5(3-2)=0-6+5=-1 \neq 0$
$\Rightarrow$ आव्यूह $A$ व्युत्क्रमणीय है। इसलिए, $A^{-1}$ का अस्तित्व है। इसलिए,

$$
\begin{aligned}
& A_{11}=0 \\
& A_{21}=-1 \\
& A_{31}=2
\end{aligned}
$$

$$
\begin{aligned}
& A_{12}=2 \\
& A_{22}=-9 \\
& A_{32}=23
\end{aligned}
$$

$$
\begin{aligned}
& A_{13}=1 \\
& A_{23}=-5 \\
& A_{33}=13
\end{aligned}
$$

$$
A^{-1}=\frac{1}{|A|} \operatorname{adj} A=\frac{1}{-1}\left[\begin{array}{ccc}
0 & -1 & 2 \\
2 & -9 & 23 \\
1 & -5 & 13
\end{array}\right]=\left[\begin{array}{ccc}
0 & 1 & -2 \\
-2 & 9 & -23 \\
-1 & 5 & -13
\end{array}\right]
$$

समीकरण निकाय को $A X=B$ के रूप में लिखा जा सकता है, जहाँ

$$
A=\left[\begin{array}{ccc}
2 & -3 & 5 \\
3 & 2 & -4 \\
1 & 1 & -2
\end{array}\right], X=\left[\begin{array}{l}
x \\
y \\
z
\end{array}\right] \text { और } B=\left[\begin{array}{l}
11 \\
-5 \\
-3
\end{array}\right]
$$

$$
X=A^{-1} B \quad \Rightarrow\left[\begin{array}{l}
x \\
y \\
z
\end{array}\right]=\left[\begin{array}{ccc}
0 & 1 & -2 \\
-2 & 9 & -23 \\
-1 & 5 & -13
\end{array}\right]\left[\begin{array}{l}
11 \\
-5 \\
-3
\end{array}\right] \Rightarrow\left[\begin{array}{l}
x \\
y \\
z
\end{array}\right]=\left[\begin{array}{c}
0-5+6 \\
-22-45+69 \\
-11-25+39
\end{array}\right] \Rightarrow\left[\begin{array}{l}
x \\
y \\
z
\end{array}\right]=\left[\begin{array}{l}
1 \\
2 \\
3
\end{array}\right] \Rightarrow x=1, y=2, z=3
$$
:::

:::answer
**उत्तर:** $A^{-1}=\left[\begin{array}{ccc}0 & 1 & -2 \\ -2 & 9 & -23 \\ -1 & 5 & -13\end{array}\right]$; $x=1, y=2, z=3$
:::

:::

:::question{number="4.5.16" kind="exercise" id="q_4.5.16" topic="Word problem - price per kg via matrix method"}
#### प्रश्न 4.5.16

:::prompt
$4$ kg प्याज, $3$ kg गेहूँ और $2$ kg चावल का मूल्य Rs $60$ है। $2$ kg प्याज, $4$ kg गेहूँ और $6 \mathrm{~kg}$ चावल का मूल्य Rs $90$ है। $6 \mathrm{~kg}$ प्याज, $2 \mathrm{~kg}$ और $3 \mathrm{~kg}$ चावल का मूल्य Rs $70$ है। आव्यूह विधि द्वारा प्रत्येक का मूल्य प्रति kg ज्ञात कीजिए।
:::

:::solution{label="हल"}
माना, $1 \mathrm{~kg}$ प्याज का मूल्य $=₹ x$,
माना, $1 \mathrm{~kg}$ गेहूँ का मूल्य = ₹ $y$ और
माना, $1 k g$ चावल का मूल्य $=₹ z$ है।
यहाँ, $4 k g$ प्याज, $3 k g$ गेहूँ और $2 k g$ चावल का मूल्य ₹ $60$ है। इसलिए, $4 x+3 y+2 z=60$ $2 k g$ प्याज, $4 k g$ गेहूँ और $6 k g$ चावल का मूल्य ₹ $90$ है। इसलिए, $2 x+4 y+6 z=90$ और $6 k g$ प्याज, $2 k g$ और $3 k g$ चावल का मूल्य ₹ $70$ है। इसलिए, $6 x+2 y+3 z=70$

समीकरण निकाय को $A X=B$ के रूप में लिखा जा सकता है, जहाँ

$$
A=\left[\begin{array}{lll}
4 & 3 & 2 \\
2 & 4 & 6 \\
6 & 2 & 3
\end{array}\right], X=\left[\begin{array}{l}
x \\
y \\
z
\end{array}\right] \text { और } B=\left[\begin{array}{l}
60 \\
90 \\
70
\end{array}\right]
$$

$|A|=4(12-12)-3(6-36)+2(4-24)=0+90-40=50 \neq 0$
$\Rightarrow$ आव्यूह $A$ व्युत्क्रमणीय है। इसलिए, $A^{-1}$ का अस्तित्व है।
अतः, दी गई समीकरण निकाय संगत हैं। इसलिए,

$$
\begin{array}{lcl}
A_{11}=0 & A_{12}=30 & A_{13}=-20 \\
A_{21}=-5 & A_{22}=0 & A_{23}=10 \\
A_{31}=10 & A_{32}=-20 & A_{33}=10
\end{array}
$$

$$
A^{-1}=\frac{1}{|A|} \text { adj } A=\frac{1}{50}\left[\begin{array}{ccc}
0 & -5 & 10 \\
30 & 0 & -20 \\
-20 & 10 & 10
\end{array}\right]
$$

$$
X=A^{-1} B \Rightarrow\left[\begin{array}{l}
x \\
y \\
z
\end{array}\right]=\frac{1}{50}\left[\begin{array}{ccc}
0 & -5 & 10 \\
30 & 0 & -20 \\
-20 & 10 & 10
\end{array}\right]\left[\begin{array}{l}
60 \\
90 \\
70
\end{array}\right] \Rightarrow\left[\begin{array}{l}
x \\
y \\
z
\end{array}\right]=\frac{1}{50}\left[\begin{array}{c}
0-450+700 \\
1800+0-1400 \\
-1200+900+700
\end{array}\right] \Rightarrow\left[\begin{array}{l}
x \\
y \\
z
\end{array}\right]=\frac{1}{50}\left[\begin{array}{l}
250 \\
400 \\
400
\end{array}\right]=\left[\begin{array}{l}
5 \\
8 \\
8
\end{array}\right] \Rightarrow x=5, y=8, z=8
$$

अतः, $1 \mathrm{~kg}$ प्याज का मूल्य ₹ $5,1 \mathrm{~kg}$ गेहूँ का मूल्य ₹ $8$ और $1 \mathrm{~kg}$ चावल का मूल्य ₹ $8$ है।
:::

:::answer
**उत्तर:** प्याज ₹5/kg, गेहूँ ₹8/kg, चावल ₹8/kg
:::

:::


## अतिरिक्त प्रश्न

:::question{number="4.9.1" kind="additional_exercise" id="q_4.9.1" topic="Proving a determinant is independent of θ"}
#### अतिरिक्त प्रश्न 4.9.1

:::prompt
सिद्ध कीजिए कि सारणिक $\left|\begin{array}{ccc}x & \sin \theta & \cos \theta \\ -\sin \theta & -x & 1 \\ \cos \theta & 1 & x\end{array}\right|, \theta$ से स्वतंत्र है।
:::

:::solution{label="हल"}
$$
\Delta=\left|\begin{array}{ccc}
x & \sin \theta & \cos \theta \\
-\sin \theta & -x & 1 \\
\cos \theta & 1 & x
\end{array}\right|
$$

$=x\left(-x^{2}-1\right)-\sin \theta(-x \sin \theta-\cos \theta)+\cos \theta(-\sin \theta+x \cos \theta)$
$=-x^{3}-x+x \sin ^{2} \theta+\sin \theta \cos \theta-\cos \theta \sin \theta+x \cos ^{2} \theta$
$=-x^{3}-x+x\left(\sin ^{2} \theta+\cos ^{2} \theta\right)=-x^{3}-x+x=-x^{3}$, जो $\theta$ से स्वतंत्र है।
:::

:::

:::question{number="4.9.2" kind="additional_exercise" id="q_4.9.2" topic="Value of a determinant with trigonometric entries" corrections_applied="1"}
#### अतिरिक्त प्रश्न 4.9.2

:::prompt
$\left|\begin{array}{ccc}\cos \alpha \cos \beta & \cos \alpha \sin \beta & -\sin \alpha \\ -\sin \beta & \cos \beta & 0 \\ \sin \alpha \cos \beta & \sin \alpha \sin \beta & \cos \alpha\end{array}\right|$ का मान ज्ञात कीजिए।
:::

:::solution{label="हल"}
$\left|\begin{array}{ccc}\cos \alpha \cos \beta & \cos \alpha \sin \beta & -\sin \alpha \\ -\sin \beta & \cos \beta & 0 \\ \sin \alpha \cos \beta & \sin \alpha \sin \beta & \cos \alpha\end{array}\right|$
$=-\sin \alpha\left(-\sin \alpha \sin ^{2} \beta-\sin \alpha \cos ^{2} \beta\right)-0(\cos \alpha \cos \beta \sin \alpha \sin \beta-\cos \alpha \sin \beta \sin \alpha \cos \beta)+\cos \alpha\left(\cos \alpha \cos ^{2} \beta+\cos \alpha \sin ^{2} \beta\right)$
$\left[C_{3}\right.$ के अनुदिश प्रसरण करने पर]

$$
\begin{aligned}
& =\sin ^{2} \alpha\left(\sin ^{2} \beta+\cos ^{2} \beta\right)+\cos ^{2} \alpha\left(\cos ^{2} \beta+\sin ^{2} \beta\right) \\
& =\sin ^{2} \alpha+\sin^{2} \alpha=1
\end{aligned}
$$
:::

:::answer
**उत्तर:** $1$
:::

:::

:::question{number="4.9.3" kind="additional_exercise" id="q_4.9.3" topic="Finding (AB)^-1 from A^-1 and B"}
#### अतिरिक्त प्रश्न 4.9.3

:::prompt
यदि $\mathrm{A}^{-1}=\left[\begin{array}{lll}3 & 1 & 1 \\ 15 & 6 & 5 \\ 5 & 2 & 2\end{array}\right]$ और $\mathrm{B}=\left[\begin{array}{ccc}1 & 2 & 2 \\ 1 & 3 & 0 \\ 0 & 2 & 1\end{array}\right]$, हो तो $(\mathrm{AB})^{-1}$ का मान ज्ञात कीजिए।
:::

:::solution{label="हल"}
यहाँ, $B=\left[\begin{array}{ccc}1 & 2 & -2 \\ -1 & 3 & 0 \\ 0 & -2 & 1\end{array}\right]$,
इसलिए $|B|=1(3-0)-2(-1-0)-2(2-0)=1 \neq 0 \Rightarrow B^{-1}$ का अस्तित्व है।

$$
\begin{array}{lll}
B_{11}=3 & B_{12}=1 & B_{13}=2 \\
B_{21}=2 & B_{22}=1 & B_{23}=2 \\
B_{31}=6 & B_{32}=2 & B_{33}=5
\end{array}
$$

$$
B^{-1}=\frac{1}{|B|} \operatorname{adj} B=\frac{1}{1}\left[\begin{array}{lll}
B_{11} & B_{21} & B_{31} \\
B_{12} & B_{22} & B_{32} \\
B_{13} & B_{23} & B_{33}
\end{array}\right]=\left[\begin{array}{lll}
3 & 2 & 6 \\
1 & 1 & 2 \\
2 & 2 & 5
\end{array}\right]
$$

हम जानते हैं कि $(\mathrm{AB})^{-1}=\mathrm{B}^{-1} \mathrm{~A}^{-1}$, इसलिए

$$
(A B)^{-1}=B^{-1} A^{-1}=\left[\begin{array}{lll}
3 & 2 & 6 \\
1 & 1 & 2 \\
2 & 2 & 5
\end{array}\right]\left[\begin{array}{ccc}
3 & -1 & 1 \\
-15 & 6 & -5 \\
5 & -2 & 2
\end{array}\right]
$$

$$
=\left[\begin{array}{ccc}
9-30+30 & -3+12-12 & 3-10+12 \\
3-15+10 & -1+6-4 & 1-5+4 \\
6-30+25 & -2+12-10 & 2-10+10
\end{array}\right]=\left[\begin{array}{ccc}
9 & -3 & 5 \\
-2 & 1 & 0 \\
1 & 0 & 2
\end{array}\right]
$$
:::

:::answer
**उत्तर:** $(AB)^{-1}=\left[\begin{array}{ccc}9 & -3 & 5 \\ -2 & 1 & 0 \\ 1 & 0 & 2\end{array}\right]$
:::

:::

:::question{number="4.9.4" kind="additional_exercise" id="q_4.9.4" topic="Verifying (adj A)^-1 = adj(A^-1) and (A^-1)^-1 = A"}
#### अतिरिक्त प्रश्न 4.9.4

:::prompt
मान लीजिए $\mathrm{A}=\left[\begin{array}{lll}1 & 2 & 1 \\ 2 & 3 & 1 \\ 1 & 1 & 5\end{array}\right]$ हो तो सत्यापित कीजिए कि
:::

:::part{label="(i)"}
:::prompt
$[\operatorname{adj} \mathrm{A}]^{-1}=\operatorname{adj}\left(\mathrm{A}^{-1}\right)$
:::

:::solution
यहाँ, $A=\left[\begin{array}{ccc}1 & -2 & 1 \\ -2 & 3 & 1 \\ 1 & 1 & 5\end{array}\right]$, इसलिए
$|A|=1(15-1)+2(-10-1)+1(-2-3)=-13 \neq 0 \Rightarrow A^{-1}$ का अस्तित्व है।

$$
\begin{aligned}
& A_{11}=14 \\
& A_{21}=11 \\
& A_{31}=-5
\end{aligned}
$$

$$
\begin{aligned}
& A_{12}=11 \\
& A_{22}=4 \\
& A_{32}=-3
\end{aligned}
$$

$$
\begin{gathered}
A_{13}=-5 \\
A_{23}=-3 \\
A_{33}=-1
\end{gathered}
$$

$$
\operatorname{adj} A=\left[\begin{array}{lll}
A_{11} & A_{21} & A_{31} \\
A_{12} & A_{22} & A_{32} \\
A_{13} & A_{23} & A_{33}
\end{array}\right]=\left[\begin{array}{ccc}
14 & 11 & -5 \\
11 & 4 & -3 \\
-5 & -3 & -1
\end{array}\right]
$$

$$
A^{-1}=\frac{1}{|A|} \text { adj } A=\frac{1}{-13}\left[\begin{array}{ccc}
14 & 11 & -5 \\
11 & 4 & -3 \\
-5 & -3 & -1
\end{array}\right]
$$

माना, $B=\operatorname{adj} A$, इसलिए, $B=\left[\begin{array}{ccc}14 & 11 & -5 \\ 11 & 4 & -3 \\ -5 & -3 & -1\end{array}\right]$, इसलिए
$|B|=14(-4-9)-11(-11-15)-5(-33+20)=-182+286+65=169 \neq 0$
$\Rightarrow B^{-1}$ का अस्तित्व है।

$$
\begin{aligned}
& B_{11}=-13 \\
& B_{21}=26 \\
& B_{31}=-13
\end{aligned}
$$

$$
\begin{aligned}
& B_{12}=26 \\
& B_{22}=-39 \\
& B_{32}=-13
\end{aligned}
$$

$$
\begin{aligned}
& B_{13}=-13 \\
& B_{23}=-13 \\
& B_{33}=-65
\end{aligned}
$$

$$
\begin{aligned}
& B^{-1}=\frac{1}{|B|}\left[\begin{array}{lll}
B_{11} & B_{21} & B_{31} \\
B_{12} & B_{22} & B_{32} \\
B_{13} & B_{23} & B_{33}
\end{array}\right]=\frac{1}{169}\left[\begin{array}{ccc}
-13 & 26 & -13 \\
26 & -39 & -13 \\
-13 & -13 & -65
\end{array}\right] \\
& \Rightarrow(\operatorname{adj} A)^{-1}=\frac{1}{13}\left[\begin{array}{ccc}
-1 & 2 & -1 \\
2 & -3 & -1 \\
-1 & -1 & -5
\end{array}\right]
\end{aligned}
$$

माना, $C=A^{-1}$, इसलिए, $C=\frac{1}{-13}\left[\begin{array}{ccc}14 & 11 & -5 \\ 11 & 4 & -3 \\ -5 & -3 & -1\end{array}\right]=\left[\begin{array}{ccc}-\frac{14}{13} & -\frac{11}{13} & \frac{5}{13} \\ -\frac{11}{13} & -\frac{4}{13} & \frac{3}{13} \\ \frac{5}{13} & \frac{3}{13} & \frac{1}{13}\end{array}\right]$, इसलिए

$$
\begin{aligned}
& C_{11}=-\frac{1}{13} \\
& C_{21}=\frac{2}{13} \\
& C_{31}=-\frac{1}{13}
\end{aligned}
$$

$$
\begin{aligned}
& C_{12}=\frac{2}{13} \\
& C_{22}=-\frac{3}{13} \\
& C_{32}=-\frac{1}{13}
\end{aligned}
$$

$$
\begin{aligned}
& C_{13}=-\frac{1}{13} \\
& C_{23}=-\frac{1}{13} \\
& C_{33}=-\frac{5}{13}
\end{aligned}
$$

$$
\begin{aligned}
& \operatorname{Adj} C=\left[\begin{array}{lll}
C_{11} & C_{21} & C_{31} \\
C_{12} & C_{22} & C_{32} \\
C_{13} & C_{23} & C_{33}
\end{array}\right]=\left[\begin{array}{ccc}
-\frac{1}{13} & \frac{2}{13} & -\frac{1}{13} \\
\frac{2}{13} & -\frac{3}{13} & -\frac{1}{13} \\
-\frac{1}{13} & -\frac{1}{13} & -\frac{5}{13}
\end{array}\right]=\frac{1}{13}\left[\begin{array}{ccc}
-1 & 2 & -1 \\
2 & -3 & -1 \\
-1 & -1 & -5
\end{array}\right] \\
& \Rightarrow \operatorname{Adj} C=\operatorname{adj}\left(A^{-1}\right)=\frac{1}{13}\left[\begin{array}{ccc}
-1 & 2 & -1 \\
2 & -3 & -1 \\
-1 & -1 & -5
\end{array}\right]
\end{aligned}
$$

अतः, $(\operatorname{adj} A)^{-1}=\operatorname{adj}\left(A^{-1}\right)$
:::

:::

:::part{label="(ii)"}
:::prompt
$\left(\mathrm{A}^{-1}\right)^{-1}=\mathrm{A}$
:::

:::solution
$$
A^{-1}=\frac{1}{-13}\left[\begin{array}{ccc}
14 & 11 & -5 \\
11 & 4 & -3 \\
-5 & -3 & -1
\end{array}\right]
$$

माना, $D=A^{-1}$, इसलिए, $D=\frac{1}{-13}\left[\begin{array}{ccc}14 & 11 & -5 \\ 11 & 4 & -3 \\ -5 & -3 & -1\end{array}\right]=\left[\begin{array}{ccc}-\frac{14}{13} & -\frac{11}{13} & \frac{5}{13} \\ -\frac{11}{13} & -\frac{4}{13} & \frac{3}{13} \\ \frac{5}{13} & \frac{3}{13} & \frac{1}{13}\end{array}\right]$, इसलिए

$$
\begin{aligned}
& |D|=-\left(\frac{1}{13}\right)^{3}[14(-4-9)-11(-11-15)-5(-33+20)] \\
& =-\left(\frac{1}{13}\right)^{3}(169)=-\frac{1}{13} \neq 0 \quad \Rightarrow D^{-1} \text { का अस्तित्व है। } \\
& \begin{array}{lll}
D_{11}=-\frac{1}{13} & D_{12}=\frac{2}{13} & D_{13}=-\frac{1}{13} \\
D_{21}=\frac{2}{13} & D_{22}=-\frac{3}{13} & D_{23}=-\frac{1}{13} \\
D_{31}=-\frac{1}{13} & D_{32}=-\frac{1}{13} & D_{33}=-\frac{5}{13}
\end{array} \\
& D^{-1}=\frac{1}{|D|}\left[\begin{array}{ccc}
D_{11} & D_{21} & D_{31} \\
D_{12} & D_{22} & D_{32} \\
D_{13} & D_{23} & D_{33}
\end{array}\right]=\frac{1}{-1 / 13}\left[\begin{array}{ccc}
-\frac{1}{13} & \frac{2}{13} & -\frac{1}{13} \\
\frac{2}{13} & -\frac{3}{13} & -\frac{1}{13} \\
-\frac{1}{13} & -\frac{1}{13} & -\frac{5}{13}
\end{array}\right]=\left[\begin{array}{ccc}
1 & -2 & 1 \\
-2 & 3 & 1 \\
1 & 1 & 5
\end{array}\right] \\
& \Rightarrow D^{-1}=\left(A^{-1}\right)^{-1}=\left[\begin{array}{ccc}
1 & -2 & 1 \\
-2 & 3 & 1 \\
1 & 1 & 5
\end{array}\right]=A
$$
:::

:::

:::

:::question{number="4.9.5" kind="additional_exercise" id="q_4.9.5" topic="Value of a determinant with symmetric entries"}
#### अतिरिक्त प्रश्न 4.9.5

:::prompt
$\left|\begin{array}{ccc}x & y & x+y \\ y & x+y & x \\ x+y & x & y\end{array}\right|$ का मान ज्ञात कीजिए।
:::

:::solution{label="हल"}
दिया है: $\left|\begin{array}{ccc}x & y & x+y \\ y & x+y & x \\ x+y & x & y\end{array}\right|$

$$
\begin{array}{lll}
=\left|\begin{array}{ccc}
2(x+y) & y & x+y \\
2(x+y) & x+y & x \\
2(x+y) & x & y
\end{array}\right| & & {\left[C_{1} \rightarrow C_{1}+C_{2}+C_{3} \text { द्वारा }\right]} \\
=2(x+y)\left|\begin{array}{ccc}
1 & y & x+y \\
1 & x+y & x \\
1 & x & y
\end{array}\right| & & {\left[C_{1} \text { से } 2(x+y) \text { उभयनिष्ठ लेने पर }\right]} \\
=2(x+y)\left|\begin{array}{ccc}
0 & -x & y \\
0 & y & x-y \\
1 & x & y
\end{array}\right| & & {\left[R_{1} \rightarrow R_{1}-R_{2}, R_{2} \rightarrow R_{2}-R_{3} \text { द्वारा }\right]} \\
=2(x+y)\{(-x)(x-y)-y . y\} & & {\left[C_{1} \text { के अनुदिश प्रसरण करने पर }\right]} \\
=2(x+y)\left(-x^{2}+x y-y^{2}\right) & & \\
=-2(x+y)\left(x^{2}-x y+y^{2}\right) & & \\
=-2\left(x^{3}+y^{3}\right) & &
\end{array}
$$
:::

:::answer
**उत्तर:** $-2(x^3+y^3)$
:::

:::

:::question{number="4.9.6" kind="additional_exercise" id="q_4.9.6" topic="Value of a determinant with symmetric entries"}
#### अतिरिक्त प्रश्न 4.9.6

:::prompt
$\left|\begin{array}{ccc}1 & x & y \\ 1 & x+y & y \\ 1 & x & x+y\end{array}\right|$ का मान ज्ञात कीजिए।
:::

:::solution{label="हल"}
दिया है: $\left|\begin{array}{ccc}1 & x & y \\ 1 & x+y & y \\ 1 & x & x+y\end{array}\right|$

$$
\begin{array}{ll}
=\left|\begin{array}{ccc}
0 & -y & 0 \\
0 & y & -x \\
1 & x & x+y
\end{array}\right| & {\left[R_{1} \rightarrow R_{1}-R_{2}, R_{2} \rightarrow R_{2}-R_{3} \text { द्वारा }\right]} \\
=\{(-y)(-x)-y .0\} & {\left[C_{1} \text { के अनुदिश प्रसरण करने पर }\right]} \\
=x y &
\end{array}
$$
:::

:::answer
**उत्तर:** $xy$
:::

:::

:::question{number="4.9.7" kind="additional_exercise" id="q_4.9.7" topic="Solving a system of equations in 1/x, 1/y, 1/z via matrix method"}
#### अतिरिक्त प्रश्न 4.9.7

:::prompt
निम्नलिखित समीकरण निकाय को हल कीजिए

$$
\begin{aligned}
& \frac{2}{x}+\frac{3}{y}+\frac{10}{z}=4 \\
& \frac{4}{x}-\frac{6}{y}+\frac{5}{z}=1 \\
& \frac{6}{x}+\frac{9}{y}-\frac{20}{z}=2
\end{aligned}
$$
:::

:::solution{label="हल"}
दी गई समीकरण निकाय:

$$
\begin{aligned}
& \frac{2}{x}+\frac{3}{y}+\frac{10}{z}=4 \\
& \frac{4}{x}-\frac{6}{y}+\frac{5}{z}=1 \\
& \frac{6}{x}+\frac{9}{y}-\frac{20}{z}=2
\end{aligned}
$$

समीकरण निकाय को $A X=B$ के रूप में लिखा जा सकता है, जहाँ

$$
A=\left[\begin{array}{ccc}
2 & 3 & 10 \\
4 & -6 & 5 \\
6 & 9 & -20
\end{array}\right], X=\left[\begin{array}{l}
1 / x \\
1 / y \\
1 / z
\end{array}\right] \text { और } B=\left[\begin{array}{l}
4 \\
1 \\
2
\end{array}\right]
$$

$|A|=2(120-45)-3(-80-30)+10(36+36)=150+330+720=1200 \neq 0$
⇒ आव्यूह $A$ व्युत्क्रमणीय है।
अतः, $A^{-1}$ का अस्तित्व है। इसलिए,

$$
\begin{aligned}
& A_{11}=75 \quad A_{12}=110 \quad A_{13}=72 \\
& A_{21}=150 \quad A_{22}=-100 \quad A_{23}=0 \\
& A_{31}=75 \quad A_{32}=30 \quad A_{33}=-24 \\
& A^{-1}=\frac{1}{|A|} \text { adj } A=\frac{1}{1200}\left[\begin{array}{ccc}
75 & 150 & 75 \\
110 & -100 & 30 \\
72 & 0 & -24
\end{array}\right] \\
& X=A^{-1} B \quad \Rightarrow\left[\begin{array}{c}
1 / x \\
1 / y \\
1 / z
\end{array}\right]=\frac{1}{1200}\left[\begin{array}{ccc}
75 & 150 & 75 \\
110 & -100 & 30 \\
72 & 0 & -24
\end{array}\right]\left[\begin{array}{c}
4 \\
1 \\
2
\end{array}\right] \\
& \Rightarrow\left[\begin{array}{c}
\frac{1}{x} \\
\frac{1}{y} \\
\frac{1}{z}
\end{array}\right]=\frac{1}{1200}\left[\begin{array}{c}
300+150+150 \\
440-100+60 \\
288+0-48
\end{array}\right] \Rightarrow\left[\begin{array}{c}
\frac{1}{x} \\
\frac{1}{y} \\
\frac{1}{z}
\end{array}\right]=\frac{1}{1200}\left[\begin{array}{l}
600 \\
400 \\
240
\end{array}\right]=\left[\begin{array}{l}
\frac{1}{2} \\
\frac{1}{3} \\
\frac{1}{5}
\end{array}\right] \\
& \Rightarrow \frac{1}{x}=\frac{1}{2}, \quad \frac{1}{y}=\frac{1}{3}, \quad \frac{1}{z}=\frac{1}{5} \quad \Rightarrow x=2, y=3, z=5
\end{aligned}
$$
:::

:::answer
**उत्तर:** $x=2, y=3, z=5$
:::

:::

:::question{number="4.9.8" kind="additional_exercise" id="q_4.9.8" topic="MCQ: inverse of a diagonal matrix"}
#### अतिरिक्त प्रश्न 4.9.8

:::prompt
निम्नलिखित प्रश्नों में सही उत्तर का चुनाव कीजिए।
यदि $x, y, z$ शून्येतर वास्तविक संख्याएँ हों तो आव्यूह $\mathrm{A}=\left[\begin{array}{ccc}x & 0 & 0 \\ 0 & y & 0 \\ 0 & 0 & z\end{array}\right]$ का व्युत्क्रम है:
(A) $\left[\begin{array}{ccc}x^{-1} & 0 & 0 \\ 0 & y^{-1} & 0 \\ 0 & 0 & z^{-1}\end{array}\right]$
(B) $x y z\left[\begin{array}{ccc}x^{-1} & 0 & 0 \\ 0 & y^{-1} & 0 \\ 0 & 0 & z^{-1}\end{array}\right]$
(C) $\frac{1}{x y z}\left[\begin{array}{ccc}x & 0 & 0 \\ 0 & y & 0 \\ 0 & 0 & z\end{array}\right]$
(D) $\frac{1}{x y z}\left[\begin{array}{lll}1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1\end{array}\right]$
:::

:::solution{label="हल"}
$$
A=\left[\begin{array}{lll}
x & 0 & 0 \\
0 & y & 0 \\
0 & 0 & z
\end{array}\right]
$$

$|A|=x(y z-0)-0(0-0)+0(0-0)=x y z \neq 0 \Rightarrow A^{-1}$ का अस्तित्व है। इसलिए,

$$
\begin{array}{lll}
A_{11}=y z & A_{12}=0 & A_{13}=0 \\
A_{21}=0 & A_{22}=x z & A_{23}=0 \\
A_{31}=0 & A_{32}=0 & A_{33}=x y
\end{array}
$$

$A^{-1}=\frac{1}{|A|} \operatorname{adj} A=\frac{1}{\mathrm{xyz}}\left[\begin{array}{ccc}y z & 0 & 0 \\ 0 & x z & 0 \\ 0 & 0 & x y\end{array}\right]=\left[\begin{array}{ccc}\frac{1}{x} & 0 & 0 \\ 0 & \frac{1}{y} & 0 \\ 0 & 0 & \frac{1}{z}\end{array}\right]=\left[\begin{array}{ccc}x^{-1} & 0 & 0 \\ 0 & y^{-1} & 0 \\ 0 & 0 & z^{-1}\end{array}\right]$
अतः, विकल्प (A) सही है।
:::

:::answer
**उत्तर:** (A) $\left[\begin{array}{ccc}x^{-1} & 0 & 0 \\ 0 & y^{-1} & 0 \\ 0 & 0 & z^{-1}\end{array}\right]$
:::

:::

:::question{number="4.9.9" kind="additional_exercise" id="q_4.9.9" topic="MCQ: range of a determinant involving sinθ"}
#### अतिरिक्त प्रश्न 4.9.9

:::prompt
यदि $\mathrm{A}=\left[\begin{array}{ccc}1 & \sin \theta & 1 \\ -\sin \theta & 1 & \sin \theta \\ -1 & -\sin \theta & 1\end{array}\right]$, जहाँ $0 \leq \theta \leq 2 \pi$ हो तो:
(A) $\operatorname{det}(\mathrm{A})=0$
(B) $\operatorname{det}(\mathrm{A}) \in(2, \infty)$
(C) $\operatorname{det}(\mathrm{A}) \in(2,4)$
(D) $\operatorname{det}(\mathrm{A}) \in[2,4]$.
:::

:::solution{label="हल"}
$$
\begin{aligned}
& A=\left[\begin{array}{ccc}
1 & \sin \theta & 1 \\
-\sin \theta & 1 & \sin \theta \\
-1 & -\sin \theta & 1
\end{array}\right] \\
& =1\left(1+\sin ^{2} \theta\right)+\sin \theta(-\sin \theta+\sin \theta)+1\left(\sin ^{2} \theta+1\right) \\
& =2\left(1+\sin ^{2} \theta\right)
\end{aligned}
$$

$\left[C_{1}\right.$ के अनुदिश प्रसरण करने पर $]$

दिया है: $0 \leq \theta \leq 2 \pi$

$$
\begin{aligned}
& \Rightarrow 0 \leq \sin \theta \leq 1 \\
& \Rightarrow 0 \leq \sin ^{2} \theta \leq 1 \\
& \Rightarrow 1 \leq 1+\sin ^{2} \theta \leq 2 \\
& \Rightarrow 2 \leq 2\left(1+\sin ^{2} \theta\right) \leq 4 \\
& \Rightarrow \operatorname{det}(A) \in[2,4]
\end{aligned}
$$

अतः, विकल्प (D) सही है।
:::

:::answer
**उत्तर:** (D) $\operatorname{det}(\mathrm{A}) \in[2,4]$
:::

:::

