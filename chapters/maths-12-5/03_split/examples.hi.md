---
subject: maths
class: 12
chapter: 5
lang: hi
title: "सांतत्य तथा अवकलनीयता"
---

# सांतत्य तथा अवकलनीयता

## उदाहरण

:::example{number="1" kind="example" id="ex_5.1" topic="Continuity of a linear function at a point"}
#### उदाहरण 1

:::prompt
$x=1$ पर फलन $f(x)=2 x+3$ के सांतत्य की जाँच कीजिए।
:::

:::solution{label="हल"}
हल पहले यह ध्यान दीजिए कि फलन, $x=1$ पर परिभाषित है और इसका मान $5$ है। अब फलन की $x=1$ पर सीमा ज्ञात करते हैं। स्पष्ट है कि

$$
\lim _{x \rightarrow 1} f(x)=\lim _{x \rightarrow 1}(2 x+3)=2(1)+3=5 \text { है। }
$$

अत:

$$
\lim _{x \rightarrow 1} f(x)=5=f(1)
$$

अतएव $x=1$ पर $f$ संतत है।
:::

:::

:::example{number="2" kind="example" id="ex_5.2" topic="Continuity of x-squared at x=0"}
#### उदाहरण 2

:::prompt
जाँचिए कि क्या फलन $f(x)=x^{2}, x=0$ पर संतत है?
:::

:::solution{label="हल"}
हल ध्यान दीजिए कि प्रदत्त बिंदु $x=0$ पर फलन परिभाषित है और इसका मान $0$ है। अब $x=0$ पर फलन की सीमा निकालते हैं। स्पष्टतया

$$
\lim _{x \rightarrow 0} f(x)=\lim _{x \rightarrow 0} x^{2}=0^{2}=0
$$

इस प्रकार

$$
\lim _{x \rightarrow 0} f(x)=0=f(0)
$$

अत:

$$
x=0 \text { पर } f \text { संतत है। }
$$
:::

:::

:::example{number="3" kind="example" id="ex_5.3" topic="Continuity of the modulus function at 0"}
#### उदाहरण 3

:::prompt
$x=0$ पर फलन $f(x)=|x|$ के सांतत्य पर विचार कीजिए।
:::

:::solution{label="हल"}
हल परिभाषा द्वारा

$$
f(x)=\left\{\begin{array}{l}
-x, \text { यदि } x<0 \\
x, \text { यदि } \quad x \geq 0
\end{array}\right.
$$

स्पष्टतया $x=0$ पर फलन परिभाषित है और $f(0)=0$ है। बिंदु $x=0$ पर $f$ की बाएँ पक्ष की सीमा

$$
\lim _{x \rightarrow 0^{-}} f(x)=\lim _{x \rightarrow 0^{-}}(-x)=0 \text { है। }
$$

इसी प्रकार $0$ पर $f$ की दाएँ पक्ष की सीमा के लिए

$$
\lim _{x \rightarrow 0^{+}} f(x)=\lim _{x \rightarrow 0^{+}} x=0 \text { है। }
$$

इस प्रकार $x=0$ पर बाएँ पक्ष की सीमा, दाएँ पक्ष की सीमा तथा फलन का मान संपाती हैं। अतः $x=0$ पर $f$ संतत है।
:::

:::

:::example{number="4" kind="example" id="ex_5.4" topic="Discontinuity of a piecewise cubic function at 0"}
#### उदाहरण 4

:::prompt
दर्शाइए कि फलन

$$
f(x)= \begin{cases}x^{3}+3, & \text { यदि } x \neq 0 \\ 1, & \text { यदि } x=0\end{cases}
$$

$x=0$ पर संतत नहीं है।
:::

:::solution{label="हल"}
हल यहाँ $x=0$ पर फलन परिभाषित है और $x=0$ पर इसका मान $1$ है। जब $x \neq 0$, तब फलन बहुपदीय है। इसलिए

$$
\lim _{x \rightarrow 0} f(x)=\lim _{x \rightarrow 0}\left(x^{3}+3\right)=0^{3}+3=3
$$

क्योंकि $x=0$ पर $f$ की सीमा, $f(0)$ के बराबर नहीं है, इसलिए $x=0$ पर फलन संतत नहीं है। हम यह भी सुनिश्चित कर सकते हैं कि इस फलन के लिए असांतत्य का बिंदु केवल $x=0$ है।
:::

:::

:::example{number="5" kind="example" id="ex_5.5" topic="Continuity of a constant function"}
#### उदाहरण 5

:::prompt
उन बिंदुओं की जाँच कीजिए जिन पर अचर फलन (Constant function) $f(x)=k$ संतत है।
:::

:::solution{label="हल"}
हल यह फलन सभी वास्तविक संख्याओं के लिए परिभाषित है और किसी भी वास्तविक संख्या के लिए इसका मान $k$ है। मान लीजिए कि $c$ एक वास्तविक संख्या है, तो

$$
\lim _{x \rightarrow c} f(x)=\lim _{x \rightarrow c} k=k
$$

चूँकि किसी वास्तविक संख्या $c$ के लिए $f(c)=k=\lim _{x \rightarrow c} f(x)$ है इसलिए फलन $f$ प्रत्येक वास्तविक संख्या के लिए संतत है।
:::

:::

:::example{number="6" kind="example" id="ex_5.6" topic="Continuity of the identity function"}
#### उदाहरण 6

:::prompt
सिद्ध कीजिए कि वास्तविक संख्याओं के लिए तत्समक फलन (Identity function) $f(x)=x$, प्रत्येक वास्तविक संख्या के लिए संतत है।
:::

:::solution{label="हल"}
हल स्पष्टतया यह फलन प्रत्येक बिंदु पर परिभाषित है और प्रत्येक वास्तविक संख्या $c$ के लिए $f(c)=c$ है।

साथ ही

$$
\lim _{x \rightarrow c} f(x)=\lim _{x \rightarrow c} x=c
$$

इस प्रकार, $\lim _{x \rightarrow c} f(x)=c=f(c)$ और इसलिए यह फलन $f$ के प्रांत के सभी बिंदुओं पर संतत है ।
:::

:::

:::example{number="7" kind="example" id="ex_5.7" topic="Continuity of the modulus function on all reals"}
#### उदाहरण 7

:::prompt
क्या $f(x)=|x|$ द्वारा परिभाषित फलन एक संतत फलन है?
:::

:::solution{label="हल"}
हल $f$ को हम ऐसे लिख सकते हैं कि $f(x)= \begin{cases}-x, \text { यदि } & x<0 \\ x, \text { यदि } & x \geq 0\end{cases}$
उदाहरण $3$ से हम जानते हैं कि $x=0$ पर $f$ संतत है।
मान लीजिए कि $c$ एक वास्तविक संख्या इस प्रकार है कि $c<0$ है। अतएव $f(c)=-c$
साथ ही

$$
\lim _{x \rightarrow c} f(x)=\lim _{x \rightarrow c}(-x)=-c
$$

चूँकि $\lim _{x \rightarrow c} f(x)=f(c)$, इसलिए $f$ सभी ऋणात्मक वास्तविक संख्याओं के लिए संतत है। अब मान लीजिए कि $c$ एक वास्तविक संख्या इस प्रकार है कि $c>0$ है। अतएव $f(c)=c$ साथ ही

$$
\lim _{x \rightarrow c} f(x)=\lim _{x \rightarrow c} x=c
$$

क्योंकि $\lim _{x \rightarrow c} f(x)=f(c)$, इसलिए $f$ सभी धनात्मक वास्तविक संख्याओं के लिए संतत है। चूँकि $f$ सभी बिंदुओं पर संतत है, अतः यह एक संतत फलन है।
:::

:::

:::example{number="8" kind="example" id="ex_5.8" topic="Continuity of a cubic polynomial function"}
#### उदाहरण 8

:::prompt
फलन $f(x)=x^{3}+x^{2}-1$ के सांतत्य पर विचार कीजिए।
:::

:::solution{label="हल"}
हल स्पष्टतया $f$ प्रत्येक वास्तविक संख्या $c$ के लिए परिभाषित है और $c$ पर इसका मान $c^{3}+c^{2}-1$ है। हम यह भी जानते हैं कि

$$
\lim _{x \rightarrow c} f(x)=\lim _{x \rightarrow c}\left(x^{3}+x^{2}-1\right)=c^{3}+c^{2}-1
$$

अतः $\lim _{x \rightarrow c} f(x)=f(c)$ है इसलिए प्रत्येक वास्तविक संख्या के लिए $f$ संतत है। इसका अर्थ है कि $f$ एक संतत फलन है।
:::

:::

:::example{number="9" kind="example" id="ex_5.9" topic="Continuity of 1/x and infinite one-sided limits"}
#### उदाहरण 9

:::prompt
$f(x)=\frac{1}{x}, x \neq 0$ द्वारा परिभाषित फलन $f$ के सांतत्य पर विचार कीजिए।
:::

:::figure{src="images/fig_maths-12-5_3.jpg" id="fig_5.3"}
आकृति 5.3
:::

:::solution{label="हल"}
हल किसी एक शून्येतर ( Non-zero) वास्तविक संख्या $c$ को सुनिश्चित कीजिए

अब

$$
\lim _{x \rightarrow c} f(x)=\lim _{x \rightarrow c} \frac{1}{x}=\frac{1}{c}
$$

साथ ही, चूँकि $c \neq 0$, इसलिए $f(c)=\frac{1}{c}$ है। इस प्रकार $\lim _{x \rightarrow c} f(x)=f(c)$ और इसलिए $f$ अपने प्रांत के प्रत्येक बिंदु पर संतत है। इस प्रकार $f$ एक संतत फलन है।

हम इस अवसर का लाभ, अनंत (infinity) की संकल्पना (concept) को समझाने के लिए, उठाते हैं। हम इसके लिए फलन $f(x)=\frac{1}{x}$ का विश्लेषण $x=0$ के निकटस्थ मानों पर करते हैं। इसके लिए हम $0$ के सन्निकट की वास्तविक संख्याओं के लिए फलन के मानों का अध्ययन करने की प्रचलित युक्ति का प्रयोग करते हैं। अनिवार्यतः (essentially) हम $x=0$ पर $f$ के दाएँ पक्ष की सीमा ज्ञात करने का प्रयास करते हैं। इसको हम नीचे सारणीबद्ध करते हैं। (सारणी 5.1)

सारणी $5.1$
| $x$ | $1$ | $0.3$ | $0.2$ | $0.1=10^{-1}$ | $0.01=10^{-2}$ | $0.001=10^{-3}$ | $10^{-n}$ |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| $f(x)$ | $1$ | 3.333... | $5$ | $10$ | $100=10^{2}$ | $1000=10^{3}$ | $10^{n}$ |

हम देखते हैं कि जैसे-जैसे $x$ दायीं ओर से $0$ के निकट अग्रसर होता है $f(x)$ का मान उत्तरोत्तर अति शीघ्रता से बढ़ता जाता है। इस बात को एक अन्य प्रकार से भी व्यक्त किया जा सकता है, जैसे:

एक धन वास्तविक संख्या को $0$ के अत्यंत निकट चुनकर, $f(x)$ के मान को किसी भी प्रदत्त संख्या से अधिक किया जा सकता है। प्रतीकों में इस बात को हम निम्नलिखित प्रकार से लिखते हैं कि

$$
\lim _{x \rightarrow 0^{+}} f(x)=+\infty
$$

(इसको इस प्रकार पढ़ा जाता है: $0$ पर, $f(x)$ के दाएँ पक्ष की धनात्मक सीमा अनंत है)। यहाँ पर हम बल देना चाहते हैं कि $+\infty$ एक वास्तविक संख्या नहीं है और इसलिए $0$ पर $f$ के दाएँ पक्ष की सीमा का अस्तित्व नहीं है (वास्तविक संख्याओं के रूप में)।

इसी प्रकार से $0$ पर $f$ के बाएँ पक्ष की सीमा ज्ञात की जा सकती है। निम्नलिखित सारणी से स्वतः स्पष्ट है।

सारणी $5.2$
| $x$ | - $1$ | -0.3 | -0.2 | $-10^{-1}$ | $-10^{-2}$ | $-10^{-3}$ | $-10^{-n}$ |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| $f(x)$ | -1 | - 3.333... | -5 | - $10$ | $-10^{2}$ | $-10^{3}$ | $-10^{n}$ |

सारणी $5.2$ से हम निष्कर्ष निकालते हैं कि एक ऋणात्मक वास्तविक संख्या को $0$ के अत्यंत निकट चुनकर, $f(x)$ के मान को किसी भी प्रदत्त संख्या से कम किया जा सकता है। प्रतीकात्मक रूप से हम

$$
\lim _{x \rightarrow 0^{-}} f(x)=-\infty \text { लिखते हैं }
$$

(जिसे इस प्रकार पढ़ा जाता है: $0$ पर $f(x)$ के बाएँ पक्ष की सीमा ऋणात्मक अनंत है।) यहाँ हम इस बात पर बल देना चाहते हैं कि $-\infty$ एक वास्तविक संख्या नहीं है अतएव $0$ पर $f$ के बाएँ पक्ष की सीमा का अस्तित्व नहीं है (वास्तविक संख्याओं के रूप में)। आकृति $5.3$ का आलेख उपर्युक्त तथ्यों का ज्यामितीय निरूपण है।
:::

:::

:::example{number="10" kind="example" id="ex_5.10" topic="Discontinuity of a piecewise linear function at x=1"}
#### उदाहरण 10

:::prompt
निम्नलिखित फलन के सांतत्य पर विचार कीजिए:

$$
f(x)=\left\{\begin{array}{l}
x+2, \text { यदि } x \leq 1 \\
x-2, \text { यदि } x>1
\end{array}\right.
$$
:::

:::figure{src="images/fig_maths-12-5_4.jpg" id="fig_5.4"}
आकृति 5.4
:::

:::solution{label="हल"}
हल फलन $f$ वास्तविक रेखा के प्रत्येक बिंदु पर परिभाषित है।
दशा $1$ यदि $c<1$, तो $f(c)=c+2$ है। इस प्रकार $\lim _{x \rightarrow c} f(x)=\lim _{x \rightarrow c} x+2=c+2$ है।

अतः $1$ से कम सभी वास्तविक संख्याओं पर $f$ संतत है।
दशा $2$ यदि $c>1$, तो $f(c)=c-2$ है।
इसलिए $\lim _{x \rightarrow c} f(x)=\lim _{x \rightarrow c}(x-2)=c-2=f(c)$ है। अतएव उन सभी बिंदुओं पर जहाँ $x>1$ है, $f$ संतत है। दशा $3$ यदि $c=1$, तो $x=1$ पर $f$ के बाएँ पक्ष की सीमा, अर्थात्

$$
\lim _{x \rightarrow 1^{-}} f(x)=\lim _{x \rightarrow 1^{-}}(x+2)=1+2=3
$$

$x=1$ पर $f$ के दाएँ पक्ष की सीमा, अर्थात्
:::

:::

:::example{number="11" kind="example" id="ex_5.11" topic="Points of discontinuity of a three-piece function"}
#### उदाहरण 11

:::prompt
निम्नलिखित प्रकार से परिभाषित फलन $f$ के समस्त (सभी) असांतत्य बिंदुओं को ज्ञात कीजिए

$$
f(x)=\left\{\begin{array}{c}
x+2, \text { यदि } x<1 \\
0, \text { यदि } \quad x=1 \\
x-2, \text { यदि } x>1
\end{array}\right.
$$
:::

:::figure{src="images/fig_maths-12-5_5.jpg" id="fig_5.5"}
आकृति 5.5
:::

:::solution{label="हल"}
हल पूर्ववर्ती उदाहरण की तरह यहाँ भी हम देखते हैं प्रत्येक वास्तविक संख्या $x \neq 1$ के लिए $f$ संतत है। $x=1$ के लिए $f$ के बाएँ पक्ष की सीमा, $\lim _{x \rightarrow 1^{-}} f(x)=\lim _{x \rightarrow 1^{-}}(x+2)=1+2=3$ है। $x=1$ के लिए $f$ के दाएँ पक्ष की सीमा, $\lim _{x \rightarrow 1^{-}} f(x)=\lim _{x \rightarrow 1^{-}}(x-2)=1-2=-1$ है।

चूँकि $x=1$ पर $f$ के बाएँ तथा दाएँ पक्ष की सीमाएँ संपाती नहीं हैं, अतः $x=1$ पर $f$ संतत नहीं है। इस प्रकार $f$ के असांतत्य का बिंदु केवल मात्र $x=1$ है। इस फलन का आलेख आकृति $5.5$ में दर्शाया गया है।
:::

:::

:::example{number="12" kind="example" id="ex_5.12" topic="Continuity of a function undefined at zero"}
#### उदाहरण 12

:::prompt
निम्नलिखित फलन के सांतत्य पर विचार कीजिए:

$$
f(x)=\left\{\begin{array}{r}
x+2, \text { यदि } x<0 \\
-x+2, \text { यदि } x>0
\end{array}\right.
$$
:::

:::figure{src="images/fig_maths-12-5_6.jpg" id="fig_5.6"}
आकृति 5.6
:::

:::solution{label="हल"}
हल ध्यान दीजिए कि विचाराधीन फलन $0$ (शून्य) के अतिरिक्त अन्य समस्त वास्तविक संख्याओं के लिए परिभाषित है। परिभाषानुसार इस फलन का प्रांत
$\mathrm{D}_{1} \cup \mathrm{D}_{2}$ है जहाँ $\mathrm{D}_{1}=\{x \in \mathbf{R}: x<0\}$ और

$$
\mathrm{D}_{2}=\{x \in \mathbf{R}: x>0\} \text { है। }
$$

दशा $1$ यदि $c \in \mathrm{D}_{1}$, तो $\lim _{x \rightarrow c} f(x)=\lim _{x \rightarrow c}(x+2)=$ $c+2=f(c)$ है अतएव $\mathrm{D}_{1}$ में $f$ संतत है।

दशा $2$ यदि $c \in \mathrm{D}_{2}$, तो $\lim _{x \rightarrow c} f(x)=\lim _{x \rightarrow c}(-x+2)=$ $-c+2=f(c)$ है अतएव $\mathrm{D}_{2}$ में भी $f$ संतत है।

क्योंकि $f$ अपने प्रांत के समस्त बिंदुओं पर संतत है जिससे हम निष्कर्ष निकालते हैं कि $f$ एक संतत फलन है। इस फलन का आलेख आकृति $5.6$ में खींचा गया है। ध्यान दीजिए कि इस फलन के आलेख को खींचने के लिए हमें कलम को कागज़ की सतह से उठाना पड़ता है, किंतु हमें ऐसा केवल उन बिंदुओं पर करना पड़ता है जहाँ पर फलन परिभाषित नहीं है।
:::

:::

:::example{number="13" kind="example" id="ex_5.13" topic="Continuity of a piecewise function split at 0"}
#### उदाहरण 13

:::prompt
निम्नलिखित फलन के सांतत्य पर विचार कीजिए:

$$
f(x)= \begin{cases}x, & \text { यदि } x \geq 0 \\ x^{2}, & \text { यदि } x<0\end{cases}
$$
:::

:::figure{src="images/fig_maths-12-5_7.jpg" id="fig_5.7"}
आकृति 5.7
:::

:::solution{label="हल"}
हल स्पष्टतया, प्रदत्त फलन प्रत्येक वास्तविक संख्या के लिए परिभाषित है। इस फलन का आलेख आकृति $5.7$ में दिया है। इस आलेख के निरीक्षण से यह तर्कसंगत लगता है कि फलन के प्रांत को वास्तविक रेखा के तीन असंयुक्त (disjoint) उप समुच्चयों में विभाजित कर लिया जाए। मान लिया कि

$$
\begin{aligned}
& \mathrm{D}_{1}=\{x \in \mathbf{R}: x<0\}, \mathrm{D}_{2}=\{0\} \text { तथा } \\
& \mathrm{D}_{3}=\{x \in \mathbf{R}: x>0\} \text { है। }
\end{aligned}
$$
:::

:::

:::example{number="14" kind="example" id="ex_5.14" topic="Continuity of every polynomial function"}
#### उदाहरण 14

:::prompt
दर्शाइए कि प्रत्येक बहुपद फलन संतत होता है।
:::

:::solution{label="हल"}
हल स्मरण कीजिए कि कोई फलन $p$, एक बहुपद फलन होता है यदि वह किसी प्राकृत संख्या $n$ के लिए $p(x)=a_{0}+a_{1} x+\ldots+a_{n} x^{n}$ द्वारा परिभाषित हो, जहाँ $a_{i} \in \mathbf{R}$ तथा $a_{n} \neq 0$ है। स्पष्टतया यह फलन प्रत्येक वास्तविक संख्या के लिए परिभाषित है। किसी निश्चित वास्तविक संख्या $c$ के लिए हम देखते हैं कि

$$
\lim _{x \rightarrow c} p(x)=p(c)
$$

इसलिए परिभाषा द्वारा $c$ पर $p$ संतत है। चूँकि $c$ कोई भी वास्तविक संख्या है इसलिए $p$ किसी भी वास्तविक संख्या के लिए संतत है, अर्थात् $p$ एक संतत फलन है।
:::

:::

:::example{number="15" kind="example" id="ex_5.15" topic="Discontinuity points of the greatest integer function"}
#### उदाहरण 15

:::prompt
$f(x)=[x]$ द्वारा परिभाषित महत्तम पूर्णांक फलन के असांतत्य के समस्त बिंदुओं को ज्ञात कीजिए, जहाँ $[x]$ उस महत्तम पूर्णांक को प्रकट करता है, जो $x$ से कम या उसके बराबर है।
:::

:::figure{src="images/fig_maths-12-5_8.jpg" id="fig_5.8"}
आकृति 5.8
:::

:::solution{label="हल"}
हल पहले तो हम यह देखते हैं कि $f$ सभी वास्तविक संख्याओं के लिए परिभाषित है। इस फलन का आलेख आकृति $5.8$ में दिखाया गया है।

आलेख से ऐसा प्रतीत होता है कि प्रदत्त फलन $x$ के सभी पूर्णांक मानों के लिए असंतत है। नीचे हम छानबीन करेंगे कि क्या यह सत्य है।

दशा $1$ मान लीजिए कि $c$ एक ऐसी वास्तविक संख्या है, जो किसी भी पूर्णांक के बराबर नहीं है। आलेख से यह स्पष्ट है कि $c$ के निकट की सभी वास्तविक संख्याओं के लिए दिए हुए फलन का मान $[c]$; हैं, अर्थात् $\lim _{x \rightarrow c} f(x)=\lim _{x \rightarrow c}[x]=[c]$ साथ ही $f(c)=[c]$ अतः प्रदत्त फलन, उन सभी वास्तविक संख्याओं के लिए संतत है, जो पूर्णांक नहीं है।
दशा $2$ मान लीजिए कि $c$ एक पूर्णांक है। अतएव हम एक ऐसी पर्याप्ततः छोटी वास्तविक संख्या $r>0$ प्राप्त कर सकते हैं जो कि $[c-r]=c-1$ जबकि $[c+r]=c$ है। सीमाओं के रूप में, इसका अर्थ यह हुआ कि

$$
\lim _{x \rightarrow c^{-}} f(x)=c-1 \text { तथा } \lim _{x \rightarrow c^{+}} f(x)=c
$$

चूँकि किसी भी पूर्णांक $c$ के लिए ये सीमाएँ समान नहीं हो सकती हैं, अतः प्रदत्त फलन $x$ सभी पूर्णांक मानों के लिए असंतत है।
:::

:::

:::example{number="16" kind="example" id="ex_5.16" topic="Every rational function is continuous"}
#### उदाहरण 16

:::prompt
सिद्ध कीजिए कि प्रत्येक परिमेय फलन संतत होता है।
:::

:::solution{label="हल"}
हल स्मरण कीजिए कि प्रत्येक परिमेय फलन $f$ निम्नलिखित रूप का होता है:

$$
f(x)=\frac{p(x)}{q(x)}, q(x) \neq 0
$$

जहाँ $p$ और $q$ बहुपद फलन हैं। $f$ का प्रांत, उन बिंदुओं को छोड़कर जिन पर $q$ शून्य है, समस्त वास्तविक संख्याएँ हैं। चूँकि बहुपद फलन संतत होते हैं (उदाहरण 14), अतएव प्रमेय $1$ के भाग (4) द्वारा $f$ एक संतत फलन है।
:::

:::

:::example{number="17" kind="example" id="ex_5.17" topic="Continuity of the sine function"}
#### उदाहरण 17

:::prompt
sine फलन के सांतत्य पर विचार कीजिए।
:::

:::solution{label="हल"}
हल इस पर विचार करने के लिए हम निम्नलिखित तथ्यों का प्रयोग करते हैं:

$$
\lim _{x \rightarrow 0} \sin x=0
$$

हमने इन तथ्यों को यहाँ प्रमाणित तो नहीं किया है, किन्तु sine फलन के आलेख को शून्य के निकट देख कर ये तथ्य सहजानुभूति (intuitively) से स्पष्ट हो जाता है।

अब देखिए कि $f(x)=\sin x$ सभी वास्तविक संख्याओं के लिए परिभाषित है। मान लीजिए कि $c$ एक वास्तविक संख्या है। $x=c+h$ रखने पर, यदि $x \rightarrow c$ तो हम देखते हैं कि $h \rightarrow 0$ इसलिए

$$
\begin{aligned}
\lim _{x \rightarrow c} f(x) & =\lim _{x \rightarrow c} \sin x \\
& =\lim _{h \rightarrow 0} \sin (c+h) \\
& =\lim _{h \rightarrow 0}[\sin c \cos h+\cos c \sin h] \\
& =\lim _{h \rightarrow 0}[\sin c \cos h]+\lim _{h \rightarrow 0}[\cos c \sin h] \\
& =\sin c+0=\sin c=f(c)
\end{aligned}
$$

इस प्रकार $\lim _{x \rightarrow c} f(x)=f(c)$ अतः $f$ एक संतत फलन है।
टिप्पणी इसी प्रकार cosine फलन के सांतत्य को भी प्रमाणित किया जा सकता है।
:::

:::

:::example{number="18" kind="example" id="ex_5.18" topic="Continuity of the tangent function"}
#### उदाहरण 18

:::prompt
सिद्ध कीजिए कि $f(x)=\tan x$ एक संतत फलन है।
:::

:::solution{label="हल"}
हल दिया हुआ फलन $f(x)=\tan x=\frac{\sin x}{\cos x}$ है। यह फलन उन सभी वास्तविक संख्याओं के लिए परिभाषित है, जहाँ $\cos x \neq 0$, अर्थात् $x \neq(2 n+1) \frac{\pi}{2}$ है। हमने अभी प्रमाणित किया है कि sine और cosine फलन, संतत फलन हैं। इसलिए $\tan$ फलन, इन दोनों फलनों का भागफल होने के कारण, $x$ के उन सभी मानों के लिए संतत है जिन के लिए यह परिभाषित है।
:::

:::

:::example{number="19" kind="example" id="ex_5.19" topic="Continuity of a composite function sin(x^2)"}
#### उदाहरण 19

:::prompt
दर्शाइए कि $f(x)=\sin \left(x^{2}\right)$ द्वारा परिभाषित फलन, एक संतत फलन है।
:::

:::solution{label="हल"}
हल प्रेक्षण कीजिए कि विचाराधीन फलन प्रत्येक वास्तविक संख्या के लिए परिभाषित है। फलन $f$ को, $g$ तथा $h$ दो फलनों के संयोजन $(g \circ h)$ के रूप में सोचा जा सकता है, जहाँ $g(x)=\sin x$ तथा $h(x)=x^{2}$ है। चूँकि $g$ और $h$ दोनों ही संतत फलन हैं, इसलिए प्रमेय $2$ द्वारा यह निष्कर्ष निकाला जा सकता है, कि $f$ एक संतत फलन है।
:::

:::

:::example{number="20" kind="example" id="ex_5.20" topic="Continuity of f(x)=|1-x+|x||"}
#### उदाहरण 20

:::prompt
दर्शाइए कि $f(x)=|1-x+|x||$ द्वारा परिभाषित फलन $f$, जहाँ $x$ एक वास्तविक संख्या है, एक संतत फलन है।
:::

:::solution{label="हल"}
हल सभी वास्तविक संख्याओं $x$ के लिए $g$ को $g(x)=1-x+|x|$ तथा $h$ को $h(x)=|x|$ द्वारा परिभाषित कीजिए। तब,

$$
\begin{aligned}
(h \circ g)(x) & =h(g(x)) \\
& =h(1-x+|x|) \\
& =|1-x+|x||=f(x)
\end{aligned}
$$

उदाहरण $7$ में हम देख चुके हैं कि $h$ एक संतत फलन है। इसी प्रकार एक बहुपद फलन और एक मापांक फलन का योग होने के कारण $g$ एक संतत फलन है। अतः दो संतत फलनों का संयुक्त फलन होने के कारण $f$ भी एक संतत फलन है।
:::

:::

:::example{number="21" kind="example" id="ex_5.21" topic="Derivative of sin(x^2) via chain rule"}
#### उदाहरण 21

:::prompt
$f(x)=\sin \left(x^{2}\right)$ का अवकलज ज्ञात कीजिए।
:::

:::solution{label="हल"}
हल ध्यान दीजिए कि प्रदत्त फलन दो फलनों का संयोजन है। वास्तव में, यदि $u(x)=x^{2}$ और $v(t)=\sin t$ है तो

$$
f(x)=(v \circ u)(x)=v(u(x))=v\left(x^{2}\right)=\sin x^{2}
$$

$t=u(x)=x^{2}$ रखने पर ध्यान दीजिए कि $\frac{d v}{d t}=\cos t$ तथा $\frac{d t}{d x}=2 x$ और दोनों का अस्तित्व भी हैं। अतः शृंखला नियम द्वारा

$$
\frac{d f}{d x}=\frac{d v}{d t} \cdot \frac{d t}{d x}=\cos t \cdot 2 x
$$

सामान्यतः अंतिम परिणाम को $x$ के पदों में व्यक्त करने का प्रचलन है अतएव

$$
\frac{d f}{d x}=\cos t \cdot 2 x=2 x \cos x^{2}
$$
:::

:::answer
**उत्तर:** $\frac{d f}{d x}=2 x \cos x^{2}$
:::

:::

:::example{number="22" kind="example" id="ex_5.22" topic="Derivative of an implicit function x-y=pi"}
#### उदाहरण 22

:::prompt
यदि $x-y=\pi$ तो $\frac{d y}{d x}$ ज्ञात कीजिए।
:::

:::solution{label="हल"}
हल एक विधि यह है कि हम $y$ के लिए सरल करके उपर्युक्त संबंध को निम्न प्रकार लिखें यथा

$$
y=x-\pi
$$

तब

$$
\frac{d y}{d x}=1
$$

विकल्पतः इस संबंध का $x$, के सापेक्ष सीधे अवकलन करने पर

$$
\frac{d}{d x}(x-y)=\frac{d \pi}{d x}
$$

याद कीजिए कि $\frac{d \pi}{d x}$ का अर्थ है कि $x$ के सापेक्ष एक अचर $\pi$ का अवकलन करना। इस प्रकार

$$
\frac{d}{d x}(x)-\frac{d}{d x}(y)=0
$$

जिसका तात्पर्य है कि

$$
\frac{d y}{d x}=\frac{d x}{d x}=1
$$
:::

:::answer
**उत्तर:** $\frac{d y}{d x}=1$
:::

:::

:::example{number="23" kind="example" id="ex_5.23" topic="Derivative of an implicit function y+sin y=cos x"}
#### उदाहरण 23

:::prompt
यदि $y+\sin y=\cos x$ तो $\frac{d y}{d x}$ ज्ञात कीजिए।
:::

:::solution{label="हल"}
हल हम इस संबंध का सीधे अवकलज करते हैं।

$$
\frac{d y}{d x}+\frac{d}{d x}(\sin y)=\frac{d}{d x}(\cos x)
$$

शृंखला नियम का प्रयोग करने पर

$$
\frac{d y}{d x}+\cos y \cdot \frac{d y}{d x}=-\sin x
$$

इससे निम्नलिखित परिणाम मिलता है,

$$
\frac{d y}{d x}=-\frac{\sin x}{1+\cos y}
$$

जहाँ

$$
y \neq(2 n+1) \pi
$$
:::

:::answer
**उत्तर:** $\frac{d y}{d x}=-\frac{\sin x}{1+\cos y}$, जहाँ $y \neq(2 n+1) \pi$
:::

:::

:::example{number="24" kind="example" id="ex_5.24" topic="Whether x=e^(log x) holds for all real x"}
#### उदाहरण 24

:::prompt
क्या यह सत्य है कि $x$ के सभी वास्तविक मानों के लिए $x=e^{\log x}$ है?
:::

:::solution{label="हल"}
हल पहले तो ध्यान दीजिए कि log फलन का प्रांत सभी धन वास्तविक संख्याओं का समुच्चय होता है। इसलिए उपर्युक्त समीकरण धनेतर वास्तविक संख्याओं के लिए सत्य नहीं है। अब मान लीजिए कि $y=e^{\log x}$ है। यदि $y>0$ तब दोनो पक्षों का लघुगणक लेने से $\log y=\log \left(e^{\log x}\right)=\log x \cdot \log$ $e=\log x$ है। जिससे $y=x$ प्राप्त होता है। अतएव $x=e^{\log x}$ केवल $x$ के धन मानों के लिए सत्य है।
:::

:::answer
**उत्तर:** $x=e^{\log x}$ केवल $x$ के धन मानों के लिए सत्य है।
:::

:::

:::example{number="25" kind="example" id="ex_5.25" topic="Differentiating exponential/logarithmic composite functions"}
#### उदाहरण 25

:::prompt
$x$ के सापेक्ष निम्नलिखित का अवकलन कीजिए:
:::

:::part{label="(i)"}
:::prompt
$e^{-x}$
:::

:::solution
मान लीजिए $y=e^{-x}$ है। अब श्रंखला नियम के प्रयोग द्वारा
$$
\frac{d y}{d x}=e^{-x} \cdot \frac{d}{d x}(-x)=-e^{-x}
$$
:::

:::answer
**उत्तर:** $\frac{d y}{d x}=-e^{-x}$
:::

:::

:::part{label="(ii)"}
:::prompt
$\sin (\log x), x>0$
:::

:::solution
मान लीजिए कि $y=\sin (\log x)$ है। अब शंखला नियम द्वारा
$$
\frac{d y}{d x}=\cos (\log x) \cdot \frac{d}{d x}(\log x)=\frac{\cos (\log x)}{x}
$$
:::

:::answer
**उत्तर:** $\frac{d y}{d x}=\frac{\cos (\log x)}{x}$
:::

:::

:::part{label="(iii)"}
:::prompt
$\cos ^{-1}\left(e^{x}\right)$
:::

:::solution
मान लीजिए कि $y=\cos ^{-1}\left(e^{x}\right)$ है। अब शृंखला नियम द्वारा
$$
\frac{d y}{d x}=\frac{-1}{\sqrt{1-\left(e^{x}\right)^{2}}} \cdot \frac{d}{d x}\left(e^{x}\right)=\frac{-e^{x}}{\sqrt{1-e^{2 x}}} .
$$
:::

:::answer
**उत्तर:** $\frac{d y}{d x}=\frac{-e^{x}}{\sqrt{1-e^{2 x}}}$
:::

:::

:::part{label="(iv)"}
:::prompt
$e^{\cos x}$
:::

:::solution
मान लीजिए कि $y=e^{\cos x}$ है। अब शृंखला नियम द्वारा
$$
\frac{d y}{d x}=e^{\cos x} \cdot(-\sin x)=-(\sin x) e^{\cos x}
$$
:::

:::answer
**उत्तर:** $\frac{d y}{d x}=-(\sin x) e^{\cos x}$
:::

:::

:::

:::example{number="26" kind="example" id="ex_5.26" topic="Logarithmic differentiation of a square-root rational expression"}
#### उदाहरण 26

:::prompt
$x$ के सापेक्ष $\sqrt{\frac{(x-3)\left(x^{2}+4\right)}{3 x^{2}+4 x+5}}$ का अवकलन कीजिए।
:::

:::solution{label="हल"}
हल मान लीजिए कि $y=\sqrt{\frac{(x-3)\left(x^{2}+4\right)}{\left(3 x^{2}+4 x+5\right)}}$

दोनों पक्षों के लघुगणक लेने पर

$$
\log y=\frac{1}{2}\left[\log (x-3)+\log \left(x^{2}+4\right)-\log \left(3 x^{2}+4 x+5\right)\right]
$$

दोनों पक्षों का $x$, के सापेक्ष अवलकन करने पर

$$
\frac{1}{y} \cdot \frac{d y}{d x}=\frac{1}{2}\left[\frac{1}{(x-3)}+\frac{2 x}{x^{2}+4}-\frac{6 x+4}{3 x^{2}+4 x+5}\right]
$$

अथवा

$$
\begin{aligned}
\frac{d y}{d x} & =\frac{y}{2}\left[\frac{1}{(x-3)}+\frac{2 x}{x^{2}+4}-\frac{6 x+4}{3 x^{2}+4 x+5}\right] \\
& =\frac{1}{2} \sqrt{\frac{(x-3)\left(x^{2}+4\right)}{3 x^{2}+4 x+5}}\left[\frac{1}{(x-3)}+\frac{2 x}{x^{2}+4}-\frac{6 x+4}{3 x^{2}+4 x+5}\right]
\end{aligned}
$$
:::

:::

:::example{number="27" kind="example" id="ex_5.27" topic="Derivative of a^x via logarithmic differentiation"}
#### उदाहरण 27

:::prompt
$x$ के सापेक्ष $a^{x}$ का अवकलन कीजिए, जहाँ $a$ एक धन अचर है।
:::

:::solution{label="हल"}
हल मान लीजिए कि $y=a^{x}$, तो

$$
\log y=x \log a
$$

दोनों पक्षों का $x$, के सापेक्ष अवकलन करने पर

$$
\frac{1}{y} \frac{d y}{d x}=\log a
$$

अथवा

$$
\frac{d y}{d x}=y \log a
$$

इस प्रकार

$$
\frac{d}{d x}\left(a^{x}\right)=a^{x} \log a
$$

विकल्पत:

$$
\begin{aligned}
\frac{d}{d x}\left(a^{x}\right) & =\frac{d}{d x}\left(e^{x \log a}\right)=e^{x \log a} \frac{d}{d x}(x \log a) \\
& =e^{x \log a} \cdot \log a=a^{x} \log a
\end{aligned}
$$
:::

:::answer
**उत्तर:** $\frac{d}{d x}\left(a^{x}\right)=a^{x} \log a$
:::

:::

:::example{number="28" kind="example" id="ex_5.28" topic="Derivative of x^(sin x) via logarithmic differentiation"}
#### उदाहरण 28

:::prompt
$x$ के सापेक्ष $x^{\sin x}$, का अवकलन कीजिए, जब कि $x>0$ है।
:::

:::solution{label="हल"}
हल मान लीजिए कि $y=x^{\sin x}$ है। अब दोनों पक्षों का लघुगणक लेने पर

अतएव

$$
\begin{aligned}
\log y & =\sin x \log x \\
\frac{1}{y} \cdot \frac{d y}{d x} & =\sin x \frac{d}{d x}(\log x)+\log x \frac{d}{d x}(\sin x)
\end{aligned}
$$

या

$$
\frac{1}{y} \frac{d y}{d x}=(\sin x) \frac{1}{x}+\log x \cos x
$$

या

$$
\begin{aligned}
\frac{d y}{d x} & =y\left[\frac{\sin x}{x}+\cos x \log x\right] \\
& =x^{\sin x}\left[\frac{\sin x}{x}+\cos x \log x\right] \\
& =x^{\sin x-1} \cdot \sin x+x^{\sin x} \cdot \cos x \log x
\end{aligned}
$$
:::

:::answer
**उत्तर:** $\frac{d y}{d x}=x^{\sin x-1} \cdot \sin x+x^{\sin x} \cdot \cos x \log x$
:::

:::

:::example{number="29" kind="example" id="ex_5.29" topic="Implicit differentiation of y^x + x^y + x^x"}
#### उदाहरण 29

:::prompt
यदि $y^{x}+x^{y}+x^{x}=a^{b}$ है। तो $\frac{d y}{d x}$ ज्ञात कीजिए।
:::

:::solution{label="हल"}
हल दिया है कि $y^{x}+x^{y}+x^{x}=a^{b}$
$u=y^{x}, v=x^{y}$ तथा $w=x^{x}$ रखने पर हमें $u+v+w=a^{b}$ प्राप्त होता है।
इसलिए

$$
\frac{d u}{d x}+\frac{d v}{d x}+\frac{d w}{d x}=0
$$

अब $u=y^{x}$ है। दोनों पक्षों का लघुगणक लेने पर

$$
\log u=x \log y
$$

दोनों पक्षों का $x$ के सापेक्ष अवकलन करने पर

$$
\begin{aligned}
\frac{1}{u} \cdot \frac{d u}{d x} & =x \frac{d}{d x}(\log y)+\log y \frac{d}{d x}(x) \\
& =x \frac{1}{y} \cdot \frac{d y}{d x}+\log y \cdot 1 \text { प्राप्त होता है। }
\end{aligned}
$$

इसलिए

$$
\frac{d u}{d x}=u\left(\frac{x}{y} \frac{d y}{d x}+\log y\right)=y^{x}\left[\frac{x}{y} \frac{d y}{d x}+\log y\right]
$$

इसी प्रकार

$$
v=x^{y}
$$

दोनों पक्षों का लघुगणक लेने पर

$$
\log v=y \log x
$$

दोनों पक्षों का $x$ के सापेक्ष अवकलन करने पर

$$
\begin{aligned}
\frac{1}{v} \cdot \frac{d v}{d x} & =y \frac{d}{d x}(\log x)+\log x \frac{d y}{d x} \\
& =y \cdot \frac{1}{x}+\log x \cdot \frac{d y}{d x} \text { प्राप्त होता है। }
\end{aligned}
$$

अतएव

$$
\begin{aligned}
\frac{d v}{d x} & =v\left[\frac{y}{x}+\log x \frac{d y}{d x}\right] \\
& =x^{y}\left[\frac{y}{x}+\log x \frac{d y}{d x}\right] \\
w & =x^{x}
\end{aligned}
$$

पुनः
दोनों पक्षों का लघुगणन करने पर

$$
\log w=x \log x
$$

दोनों पक्षों का $x$ के सापेक्ष अवकलन करने पर

$$
\begin{aligned}
\frac{1}{w} \cdot \frac{d w}{d x} & =x \frac{d}{d x}(\log x)+\log x \cdot \frac{d}{d x}(x) \\
& =x \cdot \frac{1}{x}+\log x \cdot 1 \text { प्राप्त होता है। }
\end{aligned}
$$

अर्थात्

$$
\begin{aligned}
\frac{d w}{d x} & =w(1+\log x) \\
& =x^{x}(1+\log x)
\end{aligned}
$$

(1), (2), (3) तथा (4), द्वारा

$$
y^{x}\left(\frac{x}{y} \frac{d y}{d x}+\log y\right)+x^{y}\left(\frac{y}{x}+\log x \frac{d y}{d x}\right)+x^{x}(1+\log x)=0
$$

या

$$
\left(x \cdot y^{x-1}+x^{y} \cdot \log x\right) \frac{d y}{d x}=-x^{x}(1+\log x)-y \cdot x^{y-1}-y^{x} \log y
$$

अत:

$$
\frac{d y}{d x}=\frac{-\left[y^{x} \log y+y \cdot x^{y-1}+x^{x}(1+\log x)\right]}{x \cdot y^{x-1}+x^{y} \log x}
$$
:::

:::answer
**उत्तर:** $\frac{d y}{d x}=\frac{-\left[y^{x} \log y+y \cdot x^{y-1}+x^{x}(1+\log x)\right]}{x \cdot y^{x-1}+x^{y} \log x}$
:::

:::

:::example{number="30" kind="example" id="ex_5.30" topic="Derivative of a parametric circle"}
#### उदाहरण 30

:::prompt
यदि $x=a \cos \theta, y=a \sin \theta$, तो $\frac{d y}{d x}$ ज्ञात कीजिए।
:::

:::solution{label="हल"}
हल दिया है कि

$$
x=a \cos \theta, y=a \sin \theta
$$

इसलिए

$$
\frac{d x}{d \theta}=-a \sin \theta, \frac{d y}{d \theta}=a \cos \theta
$$

अत:

$$
\frac{d y}{d x}=\frac{\frac{d y}{d \theta}}{\frac{d x}{d \theta}}=\frac{a \cos \theta}{-a \sin \theta}=-\cot \theta
$$
:::

:::answer
**उत्तर:** $-\cot \theta$
:::

:::

:::example{number="31" kind="example" id="ex_5.31" topic="Derivative of a parametric parabola"}
#### उदाहरण 31

:::prompt
यदि $x=a t^{2}, y=2 a t$ है तो $\frac{d y}{d x}$ ज्ञात कीजिए।
:::

:::solution{label="हल"}
हल दिया है कि

$$
x=a t^{2}, y=2 a t
$$

इसलिए

$$
\frac{d x}{d t}=2 a t \text { तथा } \frac{d y}{d t}=2 a
$$

अत:

$$
\frac{d y}{d x}=\frac{\frac{d y}{d t}}{\frac{d x}{d t}}=\frac{2 a}{2 a t}=\frac{1}{t}
$$
:::

:::answer
**उत्तर:** $\frac{1}{t}$
:::

:::

:::example{number="32" kind="example" id="ex_5.32" topic="Derivative of a parametric cycloid"}
#### उदाहरण 32

:::prompt
यदि $x=a(\theta+\sin \theta), y=a(1-\cos \theta)$ है तो $\frac{d y}{d x}$ ज्ञात कीजिए ।
:::

:::solution{label="हल"}
हल यहाँ $\frac{d x}{d \theta}=a(1+\cos \theta), \frac{d y}{d \theta}=a(\sin \theta)$

अत:

$$
\frac{d y}{d x}=\frac{\frac{d y}{d \theta}}{\frac{d x}{d \theta}}=\frac{a \sin \theta}{a(1+\cos \theta)}=\tan \frac{\theta}{2}
$$

- टिप्पणी यहाँ, यह ध्यान दीजिए कि $\frac{d y}{d x}$ को मुख्य चर राशियों $x$ और $y$ को सम्मिलित किए बिना ही, केवल प्राचल के पदों में व्यक्त करते हैं।
:::

:::answer
**उत्तर:** $\tan \frac{\theta}{2}$
:::

:::

:::example{number="33" kind="example" id="ex_5.33" topic="Parametric substitution for an implicit curve"}
#### उदाहरण 33

:::prompt
यदि $x^{\frac{2}{3}}+y^{\frac{2}{3}}=a^{\frac{2}{3}}$ है तो $\frac{d y}{d x}$ ज्ञात कीजिए।
:::

:::solution{label="हल"}
हल मान लीजिए कि $x=a \cos ^{3} \theta, y=a \sin ^{3} \theta$ है तब

$$
\begin{aligned}
x^{\frac{2}{3}}+y^{\frac{3}{2}} & =\left(a \cos ^{3} \theta\right)^{\frac{2}{3}}+\left(a \sin ^{3} \theta\right)^{\frac{2}{3}} \\
& =a^{\frac{2}{3}}\left(\cos ^{2} \theta+\left(\sin ^{2} \theta\right)=a^{\frac{2}{3}}\right.
\end{aligned}
$$

अत:

$$
x=a \cos ^{3} \theta, y=a \sin ^{3} \theta, x^{\frac{2}{3}}+y^{\frac{2}{3}}=a^{\frac{2}{3}} \text { का प्राचलिक समीकरण है। }
$$

इस प्रकार, $\frac{d x}{d \theta}=-3 a \cos ^{2} \theta \sin \theta$ और $\frac{d y}{d \theta}=3 a \sin ^{2} \theta \cos \theta$
इसलिए, $\frac{d y}{d x}=\frac{\frac{d y}{d \theta}}{\frac{d x}{d \theta}}=\frac{3 a \sin ^{2} \theta \cos \theta}{-3 a \cos ^{2} \theta \sin \theta}=-\tan \theta=-\sqrt[3]{\frac{y}{x}}$
:::

:::answer
**उत्तर:** $-\sqrt[3]{\frac{y}{x}}$
:::

:::

:::example{number="34" kind="example" id="ex_5.34" topic="Second-order derivative of x^3 + tan x"}
#### उदाहरण 34

:::prompt
यदि $y=x^{3}+\tan x$ है तो $\frac{d^{2} y}{d x^{2}}$ ज्ञात कीजिए।
:::

:::solution{label="हल"}
हल दिया है कि $y=x^{3}+\tan x$ है। अब

$$
\frac{d y}{d x}=3 x^{2}+\sec ^{2} x
$$

इसलिए

$$
\begin{aligned}
\frac{d^{2} y}{d x^{2}} & =\frac{d}{d x}\left(3 x^{2}+\sec ^{2} x\right) \\
& =6 x+2 \sec x \cdot \sec x \tan x=6 x+2 \sec ^{2} x \tan x
\end{aligned}
$$
:::

:::answer
**उत्तर:** $6 x+2 \sec ^{2} x \tan x$
:::

:::

:::example{number="35" kind="example" id="ex_5.35" topic="Verifying a second-order ODE for A sin x + B cos x"}
#### उदाहरण 35

:::prompt
यदि $y=\mathrm{A} \sin x+\mathrm{B} \cos x$ है तो सिद्ध कीजिए कि $\frac{d^{2} y}{d x^{2}}+y=0$ है।
:::

:::solution{label="हल"}
हल यहाँ पर

$$
\frac{d y}{d x}=\mathrm{A} \cos x-\mathrm{B} \sin x
$$

और

$$
\begin{aligned}
\frac{d^{2} y}{d x^{2}} & =\frac{d}{d x}(\mathrm{~A} \cos x-\mathrm{B} \sin x) \\
& =-\mathrm{A} \sin x-\mathrm{B} \cos x=-y
\end{aligned}
$$

इस प्रकार

$$
\frac{d^{2} y}{d x^{2}}+y=0
$$
:::

:::

:::example{number="36" kind="example" id="ex_5.36" topic="Verifying a second-order ODE for an exponential sum"}
#### उदाहरण 36

:::prompt
यदि $y=3 e^{2 x}+2 e^{3 x}$ है तो सिद्ध कीजिए कि $\frac{d^{2} y}{d x^{2}}-5 \frac{d y}{d x}+6 y=0$
:::

:::solution{label="हल"}
हल यहाँ $y=3 e^{2 x}+2 e^{3 x}$ है। अब

$$
\frac{d y}{d x}=6 e^{2 x}+6 e^{3 x}=6\left(e^{2 x}+e^{3 x}\right)
$$

इसलिए

$$
\frac{d^{2} y}{d x^{2}}=12 e^{2 x}+18 e^{3 x}=6\left(2 e^{2 x}+3 e^{3 x}\right)
$$

अत:

$$
\begin{aligned}
\frac{d^{2} y}{d x^{2}}-5 \frac{d y}{d x}+6 y= & 6\left(2 e^{2 x}+3 e^{3 x}\right) \\
& -30\left(e^{2 x}+e^{3 x}\right)+6\left(3 e^{2 x}+2 e^{3 x}\right)=0
\end{aligned}
$$
:::

:::

:::example{number="37" kind="example" id="ex_5.37" topic="Verifying a second-order ODE for arcsine, two methods"}
#### उदाहरण 37

:::prompt
यदि $y=\sin ^{-1} x$ है तो दर्शाइए कि $\left(1-x^{2}\right) \frac{d^{2} y}{d x^{2}}-x \frac{d y}{d x}=0$ है।
:::

:::solution{label="हल"}
हल यहाँ $y=\sin ^{-1} x$ है तो

$$
\frac{d y}{d x}=\frac{1}{\sqrt{\left(1-x^{2}\right)}}
$$

या

$$
\sqrt{\left(1-x^{2}\right)} \frac{d y}{d x}=1
$$

या

$$
\frac{d}{d x}\left(\sqrt{\left(1-x^{2}\right)} \cdot \frac{d y}{d x}\right)=0
$$

या

$$
\sqrt{\left(1-x^{2}\right)} \cdot \frac{d^{2} y}{d x^{2}}+\frac{d y}{d x} \cdot \frac{d}{d x}\left(\sqrt{\left(1-x^{2}\right)}\right)=0
$$

या

$$
\sqrt{\left(1-x^{2}\right)} \cdot \frac{d^{2} y}{d x^{2}}-\frac{d y}{d x} \cdot \frac{2 x}{2 \sqrt{1-x^{2}}}=0
$$

अत:

$$
\left(1-x^{2}\right) \frac{d^{2} y}{d x^{2}}-x \frac{d y}{d x}=0
$$

विकल्पतः दिया है कि $y=\sin ^{-1} x$ है तो

$$
y_{1}=\frac{1}{\sqrt{1-x^{2}}}, \text { अर्थात् }\left(1-x^{2}\right) y_{1}^{2}=1
$$

अतएव

$$
\left(1-x^{2}\right) \cdot 2 y_{1} y_{2}+y_{1}^{2}(0-2 x)=0
$$

अतः

$$
\left(1-x^{2}\right) y_{2}-x y_{1}=0
$$
:::

:::

:::example{number="38" kind="example" id="ex_5.38" topic="Differentiating a sum and a base-7 log-of-log"}
#### उदाहरण 38

:::prompt
$x$ के सापेक्ष निम्नलिखित का अवकलन कीजिए:
:::

:::part{label="(i)"}
:::prompt
$\sqrt{3 x+2}+\frac{1}{\sqrt{2 x^{2}+4}}$
:::

:::solution
मान लीजिए कि $y=\sqrt{3 x+2}+\frac{1}{\sqrt{2 x^{2}+4}}=(3 x+2)^{\frac{1}{2}}+\left(2 x^{2}+4\right)^{-\frac{1}{2}}$ है।
ध्यान दीजिए कि यह फलन सभी वास्तविक संख्याओं $x>-\frac{2}{3}$ के लिए परिभाषित है। इसलिए

$$
\begin{aligned}
\frac{d y}{d x} & =\frac{1}{2}(3 x+2)^{\frac{1}{2}-1} \cdot \frac{d}{d x}(3 x+2)+\left(-\frac{1}{2}\right)\left(2 x^{2}+4\right)^{-\frac{1}{2}-1} \cdot \frac{d}{d x}\left(2 x^{2}+4\right) \\
& =\frac{1}{2}(3 x+2)^{-\frac{1}{2}} \cdot(3)-\left(\frac{1}{2}\right)\left(2 x^{2}+4\right)^{-\frac{3}{2}} \cdot 4 x \\
& =\frac{3}{2 \sqrt{3 x+2}}-\frac{2 x}{\left(2 x^{2}+4\right)^{\frac{3}{2}}}
\end{aligned}
$$

यह सभी वास्तविक संख्याओं $x>-\frac{2}{3}$ के लिए परिभाषित है।
:::

:::answer
**उत्तर:** $\frac{3}{2 \sqrt{3 x+2}}-\frac{2 x}{\left(2 x^{2}+4\right)^{\frac{3}{2}}}$
:::

:::

:::part{label="(ii)"}
:::prompt
$\log _{7}(\log x)$
:::

:::solution
मान लीजिए कि $y=\log _{7}(\log x)=\frac{\log (\log x)}{\log 7}$ (आधार परिवर्तन के सूत्र द्वारा) समस्त वास्तविक संख्याओं $x>1$ के लिए फलन परिभाषित है। इसलिए

$$
\begin{aligned}
\frac{d y}{d x} & =\frac{1}{\log 7} \frac{d}{d x}(\log (\log x)) \\
& =\frac{1}{\log 7} \frac{1}{\log x} \cdot \frac{d}{d x}(\log x) \\
& =\frac{1}{x \log 7 \log x}
\end{aligned}
$$
:::

:::answer
**उत्तर:** $\frac{1}{x \log 7 \log x}$
:::

:::

:::

:::example{number="39" kind="example" id="ex_5.39" topic="Differentiating inverse trig compositions"}
#### उदाहरण 39

:::prompt
$x$ के सापेक्ष निम्नलिखित का अवकलन कीजिए:
:::

:::part{label="(i)"}
:::prompt
$\cos ^{-1}(\sin x)$
:::

:::solution
मान लीजिए कि $f(x)=\cos ^{-1}(\sin x)$ है। ध्यान दीजिए कि यह फलन सभी वास्तविक संख्याओं के लिए परिभाषित है। हम इसे निम्नलिखित रूप में लिख सकते हैं।

$$
\begin{aligned}
f(x) & =\cos ^{-1}(\sin x) \\
& =\cos ^{-1}\left[\cos \left(\frac{\pi}{2}-x\right)\right], \text { since } \frac{\pi}{2}-x \in[0 . \pi] \\
& =\frac{\pi}{2}-x
\end{aligned}
$$

अत:

$$
f^{\prime}(x)=-1 \text { है। }
$$
:::

:::answer
**उत्तर:** $f^{\prime}(x)=-1$
:::

:::

:::part{label="(ii)"}
:::prompt
$\tan ^{-1}\left(\frac{\sin x}{1+\cos x}\right)$
:::

:::solution
मान लीजिए कि $f(x)=\tan ^{-1}\left(\frac{\sin x}{1+\cos x}\right)$ है। ध्यान दीजिए कि यह फलन उन सभी वास्तविक संख्याओं के लिए परिभाषित है जिनके लिए $\cos x \neq-1$, अर्थात् $\pi$ के समस्त विषम गुणजों के अतिरिक्त अन्य सभी वास्तविक संख्याओं के लिए हम इस फलन को निम्नलिखित प्रकार से पुनः व्यक्त कर सकते हैं:

$$
\begin{aligned}
f(x) & =\tan ^{-1}\left(\frac{\sin x}{1+\cos x}\right) \\
& =\tan ^{-1}\left[\frac{2 \sin \left(\frac{x}{2}\right) \cos \left(\frac{x}{2}\right)}{2 \cos ^{2} \frac{x}{2}}\right]=\tan ^{-1}\left[\tan \left(\frac{x}{2}\right)\right]=\frac{x}{2}
\end{aligned}
$$

ध्यान दीजिए कि हम अंश तथा हर में $\cos \left(\frac{x}{2}\right)$ को काट सके, क्योंकि यह शून्य के बराबर नहीं है। अतः $f^{\prime}(x)=\frac{1}{2}$ है।
:::

:::answer
**उत्तर:** $f^{\prime}(x)=\frac{1}{2}$
:::

:::

:::part{label="(iii)"}
:::prompt
$\sin ^{-1}\left(\frac{2^{x+1}}{1+4^{x}}\right)$
:::

:::solution
मान लीजिए कि $f(x)=\sin ^{-1}\left(\frac{2^{x+1}}{1+4^{x}}\right)$. है। इस फलन का प्रांत ज्ञात करने के लिए हमें उन सभी $x$ को ज्ञात करने की आवश्यकता है जिनके लिए $-1 \leq \frac{2^{x+1}}{1+4^{x}} \leq 1$ है। क्योंकि $\frac{2^{x+1}}{1+4^{x}}$ सदैव
धन राशि है, इसलिए हमें उन सभी $x$ को ज्ञात करना है जिनके लिए $\frac{2^{x+1}}{1+4^{x}} \leq 1$, अर्थात् वे सभी $x$ जिनके लिए $2^{x+1} \leq 1+4^{x}$ है। हम इसको $2 \leq \frac{1}{2^{x}}+2^{x}$ प्रकार भी लिख सकते हैं, जो सभी $x$ के लिए सत्य है। अतः फलन प्रत्येक वास्तविक संख्या के लिए परिभाषित है। अब $2^{x}=\tan \theta$ रखने पर यह फलन निम्नलिखित प्रकार से पुनः लिखा जा सकता है:

$$
\begin{aligned}
f(x) & =\sin ^{-1}\left[\frac{2^{x+1}}{1+4^{x}}\right] \\
& =\sin ^{-1}\left[\frac{2^{x} \cdot 2}{1+\left(2^{x}\right)^{2}}\right] \\
& =\sin ^{-1}\left[\frac{2 \tan \theta}{1+\tan ^{2} \theta}\right] \\
& =\sin ^{-1}[\sin 2 \theta]=2 \theta=2 \tan ^{-1}\left(2^{x}\right)
\end{aligned}
$$

अत:

$$
\begin{aligned}
f^{\prime}(x) & =2 \cdot \frac{1}{1+\left(2^{x}\right)^{2}} \cdot \frac{d}{d x}\left(2^{x}\right) \\
& =\frac{2}{1+4^{x}} \cdot\left(2^{x}\right) \log 2 \\
& =\frac{2^{x+1} \log 2}{1+4^{x}}
\end{aligned}
$$
:::

:::answer
**उत्तर:** $f^{\prime}(x)=\frac{2^{x+1} \log 2}{1+4^{x}}$
:::

:::

:::

:::example{number="40" kind="example" id="ex_5.40" topic="Logarithmic differentiation of (sin x)^sin x"}
#### उदाहरण 40

:::prompt
यदि सभी $0<x<\pi$ के लिए $f(x)=(\sin x)^{\sin x}$ है तो $f^{\prime}(x)$ ज्ञात कीजिए।
:::

:::solution{label="हल"}
हल यहाँ फलन $y=(\sin x)^{\sin x}$ सभी धन वास्तविक संख्याओं के लिए परिभाषित है। लघुगणक लेने पर
अब

$$
\begin{aligned}
\log y & =\log (\sin x)^{\sin x}=\sin x \log (\sin x) \\
\frac{1}{y} \frac{d y}{d x} & =\frac{d}{d x}(\sin x \log (\sin x)) \\
& =\cos x \log (\sin x)+\sin x \cdot \frac{1}{\sin x} \cdot \frac{d}{d x}(\sin x) \\
& =\cos x \log (\sin x)+\cos x \\
& =(1+\log (\sin x)) \cos x
\end{aligned}
$$

अब $\frac{d y}{d x}=y((1+\log (\sin x)) \cos x)=(1+\log (\sin x))(\sin x)^{\sin x} \cos x$
:::

:::answer
**उत्तर:** $\frac{d y}{d x}=(1+\log (\sin x))(\sin x)^{\sin x} \cos x$
:::

:::

:::example{number="41" kind="example" id="ex_5.41" topic="Derivative of parametric exponential/power forms"}
#### उदाहरण 41

:::prompt
धनात्मक अचर $a$ के लिए $\frac{d y}{d x}$, ज्ञात कीजिए, जहाँ

$$
y=a^{t+\frac{1}{t}}, \text { तथा } x=\left(t+\frac{1}{t}\right)^{a} \text { है। }
$$
:::

:::solution{label="हल"}
हल ध्यान दीजिए कि दोनों $y$ तथा $x$, समस्त वास्तविक संख्या $t \neq 0$ के लिए परिभाषित हैं। स्पष्टत:

$$
\begin{aligned}
\frac{d y}{d t}=\frac{d}{d t}\left(a^{t+\frac{1}{t}}\right) & =a^{t+\frac{1}{t}} \frac{d}{d t}\left(t+\frac{1}{t}\right) \cdot \log a \\
& =a^{t+\frac{1}{t}}\left(1-\frac{1}{t^{2}}\right) \log a
\end{aligned}
$$

इसी प्रकार

$$
\begin{aligned}
\frac{d x}{d t} & =a\left[t+\frac{1}{t}\right]^{a-1} \cdot \frac{d}{d t}\left(t+\frac{1}{t}\right) \\
& =a\left[t+\frac{1}{t}\right]^{a-1} \cdot\left(1-\frac{1}{t^{2}}\right)
\end{aligned}
$$

$\frac{d x}{d t} \neq 0$ केवल यदि $t \neq \pm 1$ है। अत: $t \neq \pm 1$ के लिए

$$
\frac{d y}{d x}=\frac{\frac{d y}{d t}}{\frac{d x}{d t}}=\frac{a^{t+\frac{1}{t}}\left(1-\frac{1}{t^{2}}\right) \log a}{a\left[t+\frac{1}{t}\right]^{a-1} \cdot\left(1-\frac{1}{t^{2}}\right)}=\frac{a^{t+\frac{1}{t}} \log a}{a\left(t+\frac{1}{t}\right)^{a-1}}
$$
:::

:::answer
**उत्तर:** $\frac{d y}{d x}=\frac{a^{t+\frac{1}{t}} \log a}{a\left(t+\frac{1}{t}\right)^{a-1}}$
:::

:::

:::example{number="42" kind="example" id="ex_5.42" topic="Derivative of one function w.r.t. another"}
#### उदाहरण 42

:::prompt
$e^{\cos x}$ के सापेक्ष $\sin ^{2} x$ का अवकलन कीजिए।
:::

:::solution{label="हल"}
हल मान लीजिए कि $u(x)=\sin ^{2} x$ तथा $v(x)=e^{\cos x}$ है। यहाँ हमें $\frac{d u}{d v}=\frac{d u / d x}{d v / d x}$ ज्ञात करना है। स्पष्टत:

$$
\frac{d u}{d x}=2 \sin x \cos x \text { और } \frac{d v}{d x}=e^{\cos x}(-\sin x)=-(\sin x) e^{\cos x} \text { है। }
$$

अत: $\frac{d u}{d v}=\frac{2 \sin x \cos x}{-\sin x e^{\cos x}}=-\frac{2 \cos x}{e^{\cos x}}$
:::

:::answer
**उत्तर:** $\frac{d u}{d v}=-\frac{2 \cos x}{e^{\cos x}}$
:::

:::
