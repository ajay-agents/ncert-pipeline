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

## प्रश्न और हल

:::question{number="1" kind="exercise" id="q_5.1.1" topic="Continuity of a linear function at given points"}
#### प्रश्न 1

:::prompt
सिद्ध कीजिए कि फलन $f(x)=5 x-3, x=0, x=-3$ तथा $x=5$ पर संतत है।
:::

:::solution{label="हल"}
दिया गया फलन $f(x)=5 x-3$
$x=0$ पर, $f(0)=5(0)-3=-3$
बाएँ पक्ष की सीमा $=\lim _{x \rightarrow 0^{-}} f(x)=\lim _{x \rightarrow 0^{-}}(5 x-3)=-3$
दाएँ पक्ष की सीमा $=\lim _{x \rightarrow 0^{+}} f(x)=\lim _{x \rightarrow 0^{+}}(5 x-3)=-3$
यहाँ, $x=0$ पर, फलन $f$ के बाएँ पक्ष की सीमा = दाएँ पक्ष की सीमा $=f(0)=-3$
अतः, $x=0$ पर, फलन $f$ संतत है।
$x=-3$ पर, $f(-3)=5(-3)-3=-18$
बाएँ पक्ष की सीमा $=\lim _{x \rightarrow-3^{-}} f(x)=\lim _{x \rightarrow-3^{-}}(5 x-3)=-18$
दाएँ पक्ष की सीमा $=\lim _{x \rightarrow-3^{+}} f(x)=\lim _{x \rightarrow-3^{+}}(5 x-3)=-18$
यहाँ, $x=-3$ पर, फलन $f$ के बाएँ पक्ष की सीमा = दाएँ पक्ष की सीमा = $f(-3)=-18$
अतः, $x=-3$ पर, फलन $f$ संतत है।
$x=5$ पर, $f(5)=5(5)-3=22$
बाएँ पक्ष की सीमा $=\lim _{x \rightarrow 5^{-}} f(x)=\lim _{x \rightarrow 5^{-}}(5 x-3)=22$
दाएँ पक्ष की सीमा $=\lim _{x \rightarrow 5^{+}} f(x)=\lim _{x \rightarrow 5^{+}}(5 x-3)=22$
यहाँ, $x=5$ पर, फलन $f$ के बाएँ पक्ष की सीमा = दाएँ पक्ष की सीमा $=f(5)=22$
अतः, $x=5$ पर, फलन $f$ संतत है।
:::

:::

:::question{number="2" kind="exercise" id="q_5.1.2" topic="Continuity check at x=3"}
#### प्रश्न 2

:::prompt
$x=3$ पर फलन $f(x)=2 x^{2}-1$ के सांतत्य की जाँच कीजिए।
:::

:::solution{label="हल"}
दिया गया फलन $f(x)=2 x^{2}-1$
$x=3$ पर, $f(3)=2(3)^{2}-1=17$
बाएँ पक्ष की सीमा $=\lim _{x \rightarrow 3^{-}} f(x)=\lim _{x \rightarrow 3^{-}}\left(2 x^{2}-1\right)=17$
दाएँ पक्ष की सीमा $=\lim _{x \rightarrow 3^{+}} f(x)=\lim _{x \rightarrow 3^{+}}\left(2 x^{2}-1\right)=17$
यहाँ, $x=3$ पर, फलन $f$ के बाएँ पक्ष की सीमा = दाएँ पक्ष की सीमा $=f(3)=17$
अतः, $x=3$ पर, फलन $f$ संतत है।
:::

:::

:::question{number="3" kind="exercise" id="q_5.1.3" topic="Continuity of four rational and modulus functions"}
#### प्रश्न 3

:::prompt
निम्नलिखित फलनों के सांतत्य की जाँच कीजिए:
:::

:::part{label="(a)"}
:::prompt
$f(x)=x-5$
:::

:::solution
दिया गया फलन $f(x)=x-5$
माना, $k$ कोई वास्तविक संख्या है।
$x=k$ पर, $f(k)=k-5$
बाएँ पक्ष की सीमा $=\lim _{x \rightarrow k^{-}} f(x)=\lim _{x \rightarrow k^{-}}(x-5)=k-5$
दाएँ पक्ष की सीमा $=\lim _{x \rightarrow k^{+}} f(x)=\lim _{x \rightarrow k^{+}}(x-5)=k-5$
यहाँ, $x=k$ पर, फलन $f$ के बाएँ पक्ष की सीमा = दाएँ पक्ष की सीमा $=f(k)=k-5$
अतः, फलन $f$ सभी वास्तविक संख्याओं के लिए संतत है।
:::

:::

:::part{label="(b)"}
:::prompt
$f(x)=\frac{1}{x-5}, x \neq 5$
:::

:::solution
दिया गया फलन $f(x)=\frac{1}{x-5}, x \neq 5$
माना, $k(k \neq 5)$ कोई वास्तविक संख्या है।
$x=k$ पर, $f(k)=\frac{1}{k-5}$
बाएँ पक्ष की सीमा $=\lim _{x \rightarrow k^{-}} f(x)=\lim _{x \rightarrow k^{-}}\left(\frac{1}{x-5}\right)=\frac{1}{k-5}$
दाएँ पक्ष की सीमा $=\lim _{x \rightarrow k^{+}} f(x)=\lim _{x \rightarrow k^{+}}\left(\frac{1}{x-5}\right)=\frac{1}{k-5}$
यहाँ, $x=k$ पर, फलन $f$ के बाएँ पक्ष की सीमा = दाएँ पक्ष की सीमा $=f(k)=\frac{1}{k-5}$
अतः, फलन $f$ सभी वास्तविक संख्याओं ( $5$ के अतिरिक्त) के लिए संतत है।
:::

:::

:::part{label="(c)"}
:::prompt
$f(x)=\frac{x^{2}-25}{x+5}, x \neq-5$
:::

:::solution
दिया गया फलन $f(x)=\frac{x^{2}-25}{x+5}, x \neq-5$
माना, $k(k \neq-5)$ कोई वास्तविक संख्या है।
$x=k$ पर, $f(k)=\frac{k^{2}-25}{k+5}=\frac{(k+5)(k-5)}{(k+5)}=(k+5)$
बाएँ पक्ष की सीमा $=\lim _{x \rightarrow k^{-}} f(x)=\lim _{x \rightarrow k^{-}}\left(\frac{x^{2}-25}{x+5}\right)=\lim _{x \rightarrow k^{-}}\left(\frac{(k+5)(k-5)}{(k+5)}\right)=k+5$
दाएँ पक्ष की सीमा $=\lim _{x \rightarrow k^{+}} f(x)=\lim _{x \rightarrow k^{+}}\left(\frac{x^{2}-25}{x+5}\right)=\lim _{x \rightarrow k^{+}}\left(\frac{(k+5)(k-5)}{(k+5)}\right)=k+5$
यहाँ, $x=k$ पर, फलन $f$ के बाएँ पक्ष की सीमा = दाएँ पक्ष की सीमा $=f(k)=k+5$
अतः, फलन $f$ सभी वास्तविक संख्याओं ( $-5$ के अतिरिक्त) के लिए संतत है।
:::

:::

:::part{label="(d)"}
:::prompt
$f(x)=|x-5|$
:::

:::solution
दिया गया फलन $f(x)=|x-5|= \begin{cases}5-x, & x<5 \\ x-5, & x \geq 5\end{cases}$
माना, $k$ कोई वास्तविक संख्या है। प्रश्नानुसार $k<5$ या $k=5$ या $k>5$
पहली स्थिति: यदि, $k<5$,
$f(k)=5-k$ तथा $\lim _{x \rightarrow k} f(x)=\lim _{x \rightarrow k}(5-x)=5-k$, यहाँ, $\lim _{x \rightarrow k} f(x)=f(k)$
अतः, फलन $f, 5$ से छोटी सभी वास्तविक संख्याओं के लिए संतत है।
दूसरी स्थिति: यदि, $k=5$,
$f(k)=k-5$ तथा $\lim _{x \rightarrow k} f(x)=\lim _{x \rightarrow k}(x-5)=k-5$, यहाँ, $\lim _{x \rightarrow k} f(x)=f(k)$
अतः, फलन $f, 5$ पर संतत है।
तीसरी स्थिति: यदि, $k>5$,
$f(k)=k-5$ तथा $\lim _{x \rightarrow k} f(x)=\lim _{x \rightarrow k}(x-5)=k-5$, यहाँ, $\lim _{x \rightarrow k} f(x)=f(k)$
अतः, फलन $f, 5$ से बड़ी सभी वास्तविक संख्याओं के लिए संतत है।
अतः, फलन $f$ सभी वास्तविक संख्याओं के लिए संतत है।
:::

:::

:::

:::question{number="4" kind="exercise" id="q_5.1.4" topic="Continuity of x^n at x=n"}
#### प्रश्न 4

:::prompt
सिद्ध कीजिए कि फलन $f(x)=x^{n}, x=n$, पर संतत है, जहाँ $n$ एक धन पूर्णांक है।
:::

:::solution{label="हल"}
दिया गया फलन $f(x)=x^{n}$
$x=n$ पर, $f(n)=n^{n}$

$$
\lim _{x \rightarrow n} f(x)=\lim _{x \rightarrow n}\left(x^{n}\right)=n^{n}
$$

यहाँ, $x=n$ पर, $\lim _{x \rightarrow n} f(x)=f(n)=n^{n}$
अतः, $x=n$ पर, जहाँ $n$ एक धन पूर्णांक है, फलन $f$ संतत है।
:::

:::

:::question{number="5" kind="exercise" id="q_5.1.5" topic="Continuity of a piecewise function at three points"}
#### प्रश्न 5

:::prompt
क्या $f(x)=\left\{\begin{array}{l}x, \text { यदि } x \leq 1 \\ 5, \text { यदि } x>1\end{array}\right.$ द्वारा परिभाषित फलन $f$ $x=0, x=1$, तथा $x=2$ पर संतत है?
:::

:::solution{label="हल"}
दिया गया फलन $f(x)= \begin{cases}x, & x \leq 1 \\ 5, & x>1\end{cases}$
$x=0$ पर, $f(0)=0$

$$
\lim _{x \rightarrow 0} f(x)=\lim _{x \rightarrow 0}(x)=0
$$

यहाँ, $x=0$ पर, $\lim _{x \rightarrow 0} f(x)=f(0)=0$
अतः, $x=0$ पर, फलन $f$ संतत है।
$x=1$ पर, $f(1)=1$
बाएँ पक्ष की सीमा $=\lim _{x \rightarrow 1^{-}} f(x)=\lim _{x \rightarrow 1^{-}}(x)=1$
दाएँ पक्ष की सीमा $=\lim _{x \rightarrow 1^{+}} f(x)=\lim _{x \rightarrow 1^{+}}(5)=5$
यहाँ, $x=1$ पर, फलन $f$ के बाएँ पक्ष की सीमा $\neq$ दाएँ पक्ष की सीमा
अतः, $x=1$ पर, फलन $f$ संतत नहीं है।
$x=2$ पर, $f(2)=5$

$$
\lim _{x \rightarrow 2} f(x)=\lim _{x \rightarrow 2}(5)=5
$$

यहाँ, $x=2$ पर, $\lim _{x \rightarrow 2} f(x)=f(2)=5$
अतः, $x=2$ पर, फलन $f$ संतत है।
:::

:::

:::question{number="6" kind="exercise" id="q_5.1.6" topic="Points of discontinuity of a two-piece function"}
#### प्रश्न 6

:::prompt
$f$ के सभी असांतत्य के बिंदुओं को ज्ञात कीजिए, जब कि $f$ निम्नलिखित प्रकार से परिभाषित है:
$f(x)=\left\{\begin{array}{l}2 x+3, \text { यदि } x \leq 2 \\ 2 x-3, \text { यदि } x>2\end{array}\right.$
:::

:::solution{label="हल"}
माना, $k$ कोई वास्तविक संख्या है। प्रश्नानुसार $k<2$ या $k=2$ या $k>2$
पहली स्थिति: यदि, $k<2$,
$f(k)=2 k+3$ तथा $\lim _{x \rightarrow k} f(x)=\lim _{x \rightarrow k}(2 x+3)=2 k+3$, यहाँ, $\lim _{x \rightarrow k} f(x)=f(k)$
अतः, फलन $f, 2$ से छोटी सभी वास्तविक संख्याओं के लिए संतत है।

दूसरी स्थिति: यदि, $k=2$ पर, $f(2)=2 k+3$
बाएँ पक्ष की सीमा $=\lim _{x \rightarrow 2^{-}} f(x)=\lim _{x \rightarrow 2^{-}}(2 x+3)=7$
दाएँ पक्ष की सीमा $=\lim _{x \rightarrow 2^{+}} f(x)=\lim _{x \rightarrow 2^{+}}(2 x-3)=1$
यहाँ, $x=2$ पर, फलन $f$ के बाएँ पक्ष की सीमा $\neq$ दाएँ पक्ष की सीमा
अतः, $x=2$ पर, फलन $f$ संतत नहीं है।
तीसरी स्थिति: यदि, $k>2$,
$f(k)=2 k-3$ तथा $\lim _{x \rightarrow k} f(x)=\lim _{x \rightarrow k}(2 x-3)=2 k-3$, यहाँ, $\lim _{x \rightarrow k} f(x)=f(k)$
अतः, फलन $f, 2$ से बड़ी सभी वास्तविक संख्याओं के लिए संतत है।
अतः, फलन $f, x=2$ पर असांतत्य है।
:::

:::

:::question{number="7" kind="exercise" id="q_5.1.7" topic="Points of discontinuity of a three-piece function"}
#### प्रश्न 7

:::prompt
$f$ के सभी असांतत्य के बिंदुओं को ज्ञात कीजिए, जब कि $f$ निम्नलिखित प्रकार से परिभाषित है:
$f(x)=\left\{\begin{array}{l}|x|+3, \text { यदि } x \leq-3 \\ -2 x, \text { यदि }-3<x<3 \\ 6 x+2, \text { यदि } x \geq 3\end{array}\right.$
:::

:::solution{label="हल"}
माना, $k$ कोई वास्तविक संख्या है। प्रश्नानुसार
$k<-3$ या $k=-3$ या $-3<k<3$ या $k=3$ या $k>3$
पहली स्थिति: यदि, $k<-3$,
$f(k)=-k+3$ तथा $\lim _{x \rightarrow k} f(x)=\lim _{x \rightarrow k}(-x+3)=-k+3$, यहाँ, $\lim _{x \rightarrow k} f(x)=f(k)$
अतः, फलन $f,-3$ से छोटी सभी वास्तविक संख्याओं के लिए संतत है।
दूसरी स्थिति: यदि, $k=-3$ पर, $f(-3)=-(-3)+3=6$
बाएँ पक्ष की सीमा $=\lim _{x \rightarrow-3^{-}} f(x)=\lim _{x \rightarrow-3^{-}}(-x+3)=-(-3)+3=6$
दाएँ पक्ष की सीमा $=\lim _{x \rightarrow-3^{+}} f(x)=\lim _{x \rightarrow-3^{+}}(-2 x)=-2(-3)=6$, यहाँ, $\lim _{x \rightarrow k} f(x)=f(k)$
अतः, फलन $f, x=-3$ पर संतत है।
तीसरी स्थिति: यदि, $-3<k<3$,
$f(k)=-2 k$ तथा $\lim _{x \rightarrow k} f(x)=\lim _{x \rightarrow k}(-2 x)=-2 k$, यहाँ, $\lim _{x \rightarrow k} f(x)=f(k)$
अतः, फलन $f,-3<x<3$, के लिए संतत है।
चौथी स्थिति: $k=3$ पर,
बाएँ पक्ष की सीमा $=\lim _{x \rightarrow k^{-}} f(x)=\lim _{x \rightarrow k^{-}}(-2 x)=-2 k$
दाएँ पक्ष की सीमा $=\lim _{x \rightarrow k^{+}} f(x)=\lim _{x \rightarrow k^{+}}(6 x+2)=6 k+2$,
यहाँ, $x=3$ पर, फलन $f$ के बाएँ पक्ष की सीमा $\neq$ दाएँ पक्ष की सीमा,
अतः, $x=3$ पर, फलन $f$ संतत नहीं है।
पाँचवीं स्थिति: यदि, $k>3$,
$f(k)=6 k+2$ तथा $\lim _{x \rightarrow k} f(x)=\lim _{x \rightarrow k}(6 x+2)=6 k+2$, यहाँ, $\lim _{x \rightarrow k} f(x)=f(k)$
अतः, फलन $f, 3$ से बड़ी सभी वास्तविक संख्याओं के लिए संतत है।

इसप्रकार, फलन $f$, केवल $x=3$ पर असांतत्य है।
:::

:::

:::question{number="8" kind="exercise" id="q_5.1.8" topic="Points of discontinuity of |x|/x"}
#### प्रश्न 8

:::prompt
$f$ के सभी असांतत्य के बिंदुओं को ज्ञात कीजिए, जब कि $f$ निम्नलिखित प्रकार से परिभाषित है:
$f(x)=\left\{\begin{array}{cc}\frac{|x|}{x}, & \text { यदि } x \neq 0 \\ 0, & \text { यदि } x=0\end{array}\right.$
:::

:::solution{label="हल"}
इस फलन $f$ को पुनः व्यवस्थित करने पर,

$$
f(x)= \begin{cases}-\frac{x}{x}=-1, & \text { यदि } x<0 \\ 0, & \text { यदि } x=0 \\ \frac{x}{x}=1, & \text { यदि } x>0\end{cases}
$$

माना, $k$ कोई वास्तविक संख्या है। प्रश्नानुसार $k<0$ या $k=0$ या $k>0$
पहली स्थिति: यदि, $k<0$,
$f(k)=-\frac{k}{k}=-1$ तथा $\lim _{x \rightarrow k} f(x)=\lim _{x \rightarrow k}\left(-\frac{x}{x}\right)=-1$, यहाँ, $\lim _{x \rightarrow k} f(x)=f(k)$
अतः, फलन $f, 0$ से छोटी सभी वास्तविक संख्याओं के लिए संतत है।
दूसरी स्थिति: यदि, $k=0$ पर, $f(0)=0$
बाएँ पक्ष की सीमा $=\lim _{x \rightarrow k^{-}} f(x)=\lim _{x \rightarrow k^{-}}\left(-\frac{x}{x}\right)=-1$
दाएँ पक्ष की सीमा $=\lim _{x \rightarrow k^{+}} f(x)=\lim _{x \rightarrow k^{+}}\left(\frac{x}{x}\right)=1$,
यहाँ, $x=0$ पर, फलन $f$ के बाएँ पक्ष की सीमा $\neq$ दाएँ पक्ष की सीमा,
अतः, $x=0$ पर, फलन $f$ संतत नहीं है।
तीसरी स्थिति: यदि, $k>0$,
$f(k)=\frac{k}{k}=1$ तथा $\lim _{x \rightarrow k} f(x)=\lim _{x \rightarrow k}\left(\frac{x}{x}\right)=1$, यहाँ, $\lim _{x \rightarrow k} f(x)=f(k)$
अतः, फलन $f, x>0$, के लिए संतत है।
इसप्रकार, फलन $f$, केवल $x=0$ पर असांतत्य है।
:::

:::

:::question{number="9" kind="exercise" id="q_5.1.9" topic="Points of discontinuity of a signum-like function"}
#### प्रश्न 9

:::prompt
$f$ के सभी असांतत्य के बिंदुओं को ज्ञात कीजिए, जब कि $f$ निम्नलिखित प्रकार से परिभाषित है:
$f(x)= \begin{cases}\frac{x}{|x|}, & \text { यदि } x<0 \\ -1, & \text { यदि } x \geq 0\end{cases}$
:::

:::solution{label="हल"}
इस फलन $f$ को पुनः व्यवस्थित करने पर,

$$
f(x)= \begin{cases}\frac{x}{|x|}=\frac{x}{-x}=-1, & \text { यदि } x<0 \\ -1, & \text { यदि } x \geq 0\end{cases}
$$

यहाँ, $\lim _{x \rightarrow k}(x)=f(k)=-1$, जहाँ $k$ कोई वास्तविक संख्या है।
इसप्रकार, फलन $f$, सभी वास्तविक संख्याओं के लिए संतत है।
:::

:::

:::question{number="10" kind="exercise" id="q_5.1.10" topic="Points of discontinuity of a two-piece function at x=1"}
#### प्रश्न 10

:::prompt
$f$ के सभी असांतत्य के बिंदुओं को ज्ञात कीजिए, जब कि $f$ निम्नलिखित प्रकार से परिभाषित है:
$f(x)=\left\{\begin{array}{l}x+1, \text { यदि } x \geq 1 \\ x^{2}+1, \text { यदि } x<1\end{array}\right.$
:::

:::solution{label="हल"}
माना, $k$ कोई वास्तविक संख्या है। प्रश्नानुसार $k<1$ या $k=1$ या $k>1$
पहली स्थिति: यदि, $k<1$,
$f(k)=k^{2}+1$ तथा $\lim _{x \rightarrow k} f(x)=\lim _{x \rightarrow k}\left(x^{2}+1\right)=k^{2}+1$, यहाँ, $\lim _{x \rightarrow k} f(x)=f(k)$
अतः, फलन $f, 1$ से छोटी सभी वास्तविक संख्याओं के लिए संतत है।
दूसरी स्थिति: यदि, $k=1$ पर, $f(1)=1+1=2$
बाएँ पक्ष की सीमा $=\lim _{x \rightarrow 1^{-}} f(x)=\lim _{x \rightarrow 1^{-}}\left(x^{2}+1\right)=1+1=2$
दाएँ पक्ष की सीमा $=\lim _{x \rightarrow 1^{+}} f(x)=\lim _{x \rightarrow 1^{+}}(x+1)=1+1=2$,
यहाँ, $x=1$ पर, फलन $f$ के बाएँ पक्ष की सीमा = दाएँ पक्ष की सीमा = $f(1)$
अतः, $x=1$ पर, फलन $f$ संतत है।
तीसरी स्थिति: यदि, $k>1$,
$f(k)=k+1$ तथा $\lim _{x \rightarrow k} f(x)=\lim _{x \rightarrow k}(x+1)=k+1$, यहाँ, $\lim _{x \rightarrow k} f(x)=f(k)$
अतः, फलन $f, x>1$, के लिए संतत है।
इसप्रकार, फलन $f$, सभी वास्तविक संख्याओं के लिए संतत है।
:::

:::

:::question{number="11" kind="exercise" id="q_5.1.11" topic="Points of discontinuity of a two-piece function at x=2"}
#### प्रश्न 11

:::prompt
$f$ के सभी असांतत्य के बिंदुओं को ज्ञात कीजिए, जब कि $f$ निम्नलिखित प्रकार से परिभाषित है:
$f(x)= \begin{cases}x^{3}-3, & \text { यदि } x \leq 2 \\ x^{2}+1, & \text { यदि } x>2\end{cases}$
:::

:::solution{label="हल"}
माना, $k$ कोई वास्तविक संख्या है। प्रश्नानुसार $k<2$ या $k=2$ या $k>2$
पहली स्थिति: यदि, $k<2$,
$f(k)=k^{3}-3$ तथा $\lim _{x \rightarrow k} f(x)=\lim _{x \rightarrow k}\left(x^{3}-3\right)=k^{3}-3$, यहाँ, $\lim _{x \rightarrow k} f(x)=f(k)$
अतः, फलन $f, 2$ से छोटी सभी वास्तविक संख्याओं के लिए संतत है।
दूसरी स्थिति: यदि, $k=2$ पर, $f(2)=2^{3}-3=5$
बाएँ पक्ष की सीमा $=\lim _{x \rightarrow 2^{-}} f(x)=\lim _{x \rightarrow 2^{-}}\left(x^{3}-3\right)=2^{3}-3=5$
दाएँ पक्ष की सीमा $=\lim _{x \rightarrow 2^{+}} f(x)=\lim _{x \rightarrow 2^{+}}\left(x^{2}+1\right)=2^{2}+1=5$,
यहाँ, $x=2$ पर, फलन $f$ के बाएँ पक्ष की सीमा = दाएँ पक्ष की सीमा = $f(2)$
अतः, $x=2$ पर, फलन $f$ संतत है।
तीसरी स्थिति: यदि, $k>2$,
$f(k)=k^{2}+1$ तथा $\lim _{x \rightarrow k} f(x)=\lim _{x \rightarrow k}\left(x^{2}+1\right)=k^{2}+1$, यहाँ, $\lim _{x \rightarrow k} f(x)=f(k)$
अतः, फलन $f, x>2$, के लिए संतत है।
इसप्रकार, फलन $f$, सभी वास्तविक संख्याओं के लिए संतत है।
:::

:::

:::question{number="12" kind="exercise" id="q_5.1.12" topic="Points of discontinuity of a two-piece function at x=1"}
#### प्रश्न 12

:::prompt
$f$ के सभी असांतत्य के बिंदुओं को ज्ञात कीजिए, जब कि $f$ निम्नलिखित प्रकार से परिभाषित है:
$f(x)= \begin{cases}x^{10}-1, & \text { यदि } x \leq 1 \\ x^{2}, & \text { यदि } x>1\end{cases}$
:::

:::solution{label="हल"}
माना, $k$ कोई वास्तविक संख्या है। प्रश्नानुसार $k<1$ या $k=1$ या $k>1$
पहली स्थिति: यदि, $k<1$,
$f(k)=k^{10}-1$ तथा $\lim _{x \rightarrow k} f(x)=\lim _{x \rightarrow k}\left(x^{10}-1\right)=k^{10}-1$, यहाँ, $\lim _{x \rightarrow k} f(x)=f(k)$
अतः, फलन $f, 1$ से छोटी सभी वास्तविक संख्याओं के लिए संतत है।
दूसरी स्थिति: यदि, $k=1$ पर, $f(1)=1^{10}-1=0$
बाएँ पक्ष की सीमा $=\lim _{x \rightarrow 1^{-}} f(x)=\lim _{x \rightarrow 1^{-}}\left(x^{10}-1\right)=0$
दाएँ पक्ष की सीमा $=\lim _{x \rightarrow 1^{+}} f(x)=\lim _{x \rightarrow 1^{+}}\left(x^{2}\right)=1$,
यहाँ, $x=1$ पर, फलन $f$ के बाएँ पक्ष की सीमा $\neq$ दाएँ पक्ष की सीमा,
अतः, $x=1$ पर, फलन $f$ संतत नहीं है।
तीसरी स्थिति: यदि, $k>1$,
$f(k)=k^{2}$ तथा $\lim _{x \rightarrow k} f(x)=\lim _{x \rightarrow k}\left(x^{2}\right)=k^{2}$, यहाँ, $\lim _{x \rightarrow k} f(x)=f(k)$
अतः, फलन $f, x>1$, के लिए संतत है।
इसप्रकार, फलन $f$, केवल $x=1$ पर असांतत्य है।
:::

:::

:::question{number="13" kind="exercise" id="q_5.1.13" topic="Continuity check of a two-piece function at x=1"}
#### प्रश्न 13

:::prompt
क्या $f(x)=\left\{\begin{array}{ll}x+5, & \text { यदि } x \leq 1 \\ x-5, & \text { यदि } x>1\end{array}\right.$ द्वारा परिभाषित फलन, एक संतत फलन है?
:::

:::solution{label="हल"}
माना, $k$ कोई वास्तविक संख्या है। प्रश्नानुसार $k<1$ या $k=1$ या $k>1$
पहली स्थिति: यदि, $k<1$,
$f(k)=k+5$ तथा $\lim _{x \rightarrow k} f(x)=\lim _{x \rightarrow k}(x+5)=k+5$, यहाँ, $\lim _{x \rightarrow k} f(x)=f(k)$
अतः, फलन $f, 1$ से छोटी सभी वास्तविक संख्याओं के लिए संतत है।
दूसरी स्थिति: यदि, $k=1$ पर, $f(1)=1+5=6$
बाएँ पक्ष की सीमा $=\lim _{x \rightarrow 1^{-}} f(x)=\lim _{x \rightarrow 1^{-}}(x+5)=6$
दाएँ पक्ष की सीमा $=\lim _{x \rightarrow 1^{+}} f(x)=\lim _{x \rightarrow 1^{+}}(x-5)=-4$,
यहाँ, $x=1$ पर, फलन $f$ के बाएँ पक्ष की सीमा $\neq$ दाएँ पक्ष की सीमा,
अतः, $x=1$ पर, फलन $f$ संतत नहीं है।
तीसरी स्थिति: यदि, $k>1$,
$f(k)=k-5$ तथा $\lim _{x \rightarrow k} f(x)=\lim _{x \rightarrow k}(x-5)=k-5$, यहाँ, $\lim _{x \rightarrow k} f(x)=f(k)$
अतः, फलन $f, x>1$, के लिए संतत है।
इसप्रकार, फलन $f$, केवल $x=1$ पर असांतत्य है।
:::

:::

:::question{number="14" kind="exercise" id="q_5.1.14" topic="Continuity of a three-piece step function"}
#### प्रश्न 14

:::prompt
फलन $f$, के सांतत्य पर विचार कीजिए, जहाँ $f$ निम्नलिखित द्वारा परिभाषित है:
$f(x)=\left\{\begin{array}{l}3, \text { यदि } 0 \leq x \leq 1 \\ 4, \text { यदि } 1<x<3 \\ 5, \text { यदि } 3 \leq x \leq 10\end{array}\right.$
:::

:::solution{label="हल"}
माना, $k$ कोई वास्तविक संख्या है। प्रश्नानुसार
$0 \leq k \leq 1$ या $k=1$ या $1<k<3$ या $k=3$ या $3 \leq k \leq 10$
पहली स्थिति: यदि, $0 \leq k \leq 1$,
$f(k)=3$ तथा $\lim _{x \rightarrow k} f(x)=\lim _{x \rightarrow k}(3)=3$, यहाँ, $\lim _{x \rightarrow k} f(x)=f(k)$
अतः, फलन $f, 0 \leq x \leq 1$ के लिए संतत है।
दूसरी स्थिति: यदि, $k=1$ पर, $f(1)=3$
बाएँ पक्ष की सीमा $=\lim _{x \rightarrow 1^{-}} f(x)=\lim _{x \rightarrow 1^{-}}(3)=3$
दाएँ पक्ष की सीमा $=\lim _{x \rightarrow 1^{+}} f(x)=\lim _{x \rightarrow 1^{+}}(4)=4$,
यहाँ, $x=1$ पर, फलन $f$ के बाएँ पक्ष की सीमा $\neq$ दाएँ पक्ष की सीमा,
अतः, $x=1$ पर, फलन $f$ संतत नहीं है।
तीसरी स्थिति: यदि, $1<k<3$,
$f(k)=4$ तथा $\lim _{x \rightarrow k} f(x)=\lim _{x \rightarrow k}(4)=4$, यहाँ, $\lim _{x \rightarrow k} f(x)=f(k)$
अतः, फलन $f, 1<x<3$, के लिए संतत है।
चौथी स्थिति: $k=3$ पर,
बाएँ पक्ष की सीमा $=\lim _{x \rightarrow 3^{-}} f(x)=\lim _{x \rightarrow 3^{-}}(4)=4$
दाएँ पक्ष की सीमा $=\lim _{x \rightarrow 3^{+}} f(x)=\lim _{x \rightarrow 3^{+}}(5)=5$,
यहाँ, $x=3$ पर, फलन $f$ के बाएँ पक्ष की सीमा $\neq$ दाएँ पक्ष की सीमा,
अतः, $x=3$ पर, फलन $f$ संतत नहीं है।
पाँचवीं स्थिति: यदि, $3 \leq k \leq 10$,
$f(k)=5$ तथा $\lim _{x \rightarrow k} f(x)=\lim _{x \rightarrow k}(5)=5$, यहाँ, $\lim _{x \rightarrow k} f(x)=f(k)$
अतः, फलन $f, 3 \leq x \leq 10$ के लिए संतत है।
इसप्रकार, फलन $f$, केवल $x=1$ तथा $x=3$ पर असांतत्य है।
:::

:::

:::question{number="15" kind="exercise" id="q_5.1.15" topic="Continuity of a three-piece function"}
#### प्रश्न 15

:::prompt
फलन $f$, के सांतत्य पर विचार कीजिए, जहाँ $f$ निम्नलिखित द्वारा परिभाषित है:
$f(x)= \begin{cases}2 x, & \text { यदि } x<0 \\ 0, & \text { यदि } 0 \leq x \leq 1 \\ 4 x, & \text { यदि } x>1\end{cases}$
:::

:::solution{label="हल"}
माना, $k$ कोई वास्तविक संख्या है। प्रश्नानुसार $k<0$ या $k=0$ या $0 \leq k \leq 1$ या $k=1$ या $k>1$ पहली स्थिति: यदि, $k<0$,
$f(k)=2 k$ तथा $\lim _{x \rightarrow k} f(x)=\lim _{x \rightarrow k}(2 x)=2 k$, यहाँ, $\lim _{x \rightarrow k} f(x)=f(k)$
अतः, फलन $f, x<0$ के लिए संतत है।
दूसरी स्थिति: यदि, $k=0$ पर, $f(0)=0$
बाएँ पक्ष की सीमा $=\lim _{x \rightarrow 0^{-}} f(x)=\lim _{x \rightarrow 0^{-}}(2 \mathrm{x})=0$
दाएँ पक्ष की सीमा $=\lim _{x \rightarrow 0^{+}} f(x)=\lim _{x \rightarrow 0^{+}}(0)=0$, यहाँ, $\lim _{x \rightarrow k} f(x)=f(k)$
अतः, फलन $f, x=0$ के लिए संतत है।
तीसरी स्थिति: यदि, $0 \leq k \leq 1$,
$f(k)=0$ तथा $\lim _{x \rightarrow k} f(x)=\lim _{x \rightarrow k}(0)=0$, यहाँ, $\lim _{x \rightarrow k} f(x)=f(k)$
अतः, फलन $f, 0 \leq x \leq 1$, के लिए संतत है।
चौथी स्थिति: $k=1$ पर,
बाएँ पक्ष की सीमा $=\lim _{x \rightarrow 1^{-}} f(x)=\lim _{x \rightarrow 1^{-}}(0)=0$
दाएँ पक्ष की सीमा $=\lim _{x \rightarrow 1^{+}} f(x)=\lim _{x \rightarrow 1^{+}}(4 \mathrm{x})=4$,
यहाँ, $x=1$ पर, फलन $f$ के बाएँ पक्ष की सीमा $\neq$ दाएँ पक्ष की सीमा,
अतः, $x=1$ पर, फलन $f$ संतत नहीं है।
पाँचवीं स्थिति: यदि, $k>1$,
$f(k)=4 k$ तथा $\lim _{x \rightarrow k} f(x)=\lim _{x \rightarrow k}(4 x)=4 k$, यहाँ, $\lim _{x \rightarrow k} f(x)=f(k)$
अतः, फलन $f, x>1$ के लिए संतत है।
इसप्रकार, फलन $f$, केवल $x=1$ पर असांतत्य है।
:::

:::

:::question{number="16" kind="exercise" id="q_5.1.16" topic="Continuity of a three-piece function"}
#### प्रश्न 16

:::prompt
फलन $f$, के सांतत्य पर विचार कीजिए, जहाँ $f$ निम्नलिखित द्वारा परिभाषित है:
$f(x)= \begin{cases}-2, & \text { यदि } x \leq-1 \\ 2 x, & \text { यदि }-1<x \leq 1 \\ 2, & \text { यदि } x>1\end{cases}$
:::

:::solution{label="हल"}
माना, $k$ कोई वास्तविक संख्या है।
प्रश्नानुसार $k<-1$ या $k=-1$ या $-1<x \leq 1$ या $k=1$ या $k>1$
पहली स्थिति: यदि, $k<-1$,
$f(k)=-2$ तथा $\lim _{x \rightarrow k} f(x)=\lim _{x \rightarrow k}(-2)=-2$, यहाँ, $\lim _{x \rightarrow k} f(x)=f(k)$
अतः, फलन $f, x<-1$ के लिए संतत है।
दूसरी स्थिति: यदि, $k=-1$ पर, $f(-1)=-2$
बाएँ पक्ष की सीमा $=\lim _{x \rightarrow-1^{-}} f(x)=\lim _{x \rightarrow-1^{-}}(-2)=-2$
दाएँ पक्ष की सीमा $=\lim _{x \rightarrow-1^{+}} f(x)=\lim _{x \rightarrow-1^{+}}(2 x)=-2$, यहाँ, $\lim _{x \rightarrow k} f(x)=f(k)$
अतः, फलन $f, x=-1$ के लिए संतत है।
तीसरी स्थिति: यदि, $-1<x \leq 1$,
$f(k)=2 k$ तथा $\lim _{x \rightarrow k} f(x)=\lim _{x \rightarrow k}(2 x)=2 k$, यहाँ, $\lim _{x \rightarrow k} f(x)=f(k)$
अतः, फलन $f,-1<x \leq 1$, के लिए संतत है।
चौथी स्थिति: $k=1$ पर,
बाएँ पक्ष की सीमा $=\lim _{x \rightarrow 1^{-}} f(x)=\lim _{x \rightarrow 1^{-}}(2 x)=2$
दाएँ पक्ष की सीमा $=\lim _{x \rightarrow 1^{+}} f(x)=\lim _{x \rightarrow 1^{+}}(2)=2$, यहाँ, $\lim _{x \rightarrow k} f(x)=f(k)$
अतः, फलन $f, x=1$, के लिए संतत है।
पाँचवीं स्थिति: यदि, $k>1$,
$f(k)=2$ तथा $\lim _{x \rightarrow k} f(x)=\lim _{x \rightarrow k}(2)=2$, यहाँ, $\lim _{x \rightarrow k} f(x)=f(k)$
अतः, फलन $f, x>1$ के लिए संतत है।
इसप्रकार, फलन $f$, सभी वास्तविक संख्याओं के लिए संतत है।
:::

:::

:::question{number="17" kind="exercise" id="q_5.1.17" topic="Finding a, b for continuity at x=3"}
#### प्रश्न 17

:::prompt
$a$ और $b$ के उन मानों को ज्ञात कीजिए जिनके लिए

$$
f(x)= \begin{cases}a x+1, & \text { यदि } x \leq 3 \\ b x+3, & \text { यदि } x>3\end{cases}
$$

द्वारा परिभाषित फलन $x=3$ पर संतत है।
:::

:::solution{label="हल"}
दिया है: फलन $x=3$ पर संतत है। इसलिए, बाएँ पक्ष की सीमा = दाएँ पक्ष की सीमा = $f(3)$

$$
\begin{aligned}
& \Rightarrow \lim _{x \rightarrow 3^{-}} f(x)=\lim _{x \rightarrow 3^{+}} f(x)=f(3) \\
& \Rightarrow \lim _{x \rightarrow 3^{-}} a x+1=\lim _{x \rightarrow 3^{+}} b x+3=3 a+1 \\
& \Rightarrow 3 a+1=3 b+3=3 a+1 \\
& \Rightarrow 3 a=3 b+2 \quad \Rightarrow a=b+\frac{2}{3}
\end{aligned}
$$
:::

:::answer
**उत्तर:** $a=b+\frac{2}{3}$
:::

:::

:::question{number="18" kind="exercise" id="q_5.1.18" topic="Continuity of a piecewise function depending on lambda"}
#### प्रश्न 18

:::prompt
$\lambda$ के किस मान के लिए
$$
f(x)= \begin{cases}\lambda\left(x^{2}-2 x\right), & \text { यदि } x \leq 0 \\ 4 x+1, & \text { यदि } x>0\end{cases}
$$
द्वारा परिभाषित फलन $x=0$ पर संतत है। $x=1$ पर इसके सांतत्य पर विचार कीजिए।
:::

:::solution{label="हल"}
दिया है: फलन $x=0$ पर संतत है। इसलिए, बाएँ पक्ष की सीमा = दाएँ पक्ष की सीमा = $f(0)$

$$
\begin{aligned}
& \Rightarrow \lim _{x \rightarrow 0^{-}} f(x)=\lim _{x \rightarrow 0^{+}} f(x)=f(0) \\
& \Rightarrow \lim _{x \rightarrow 0^{-}} \lambda\left(x^{2}-2 x\right)=\lim _{x \rightarrow 0^{+}} 4 x+1=\lambda\left[(0)^{2}-2(0)\right] \\
& \Rightarrow \lambda\left[(0)^{2}-2(0)\right]=4(0)+1=\lambda(0) \\
& \Rightarrow 0 \cdot \lambda=1 \quad \Rightarrow \lambda=\frac{1}{0}
\end{aligned}
$$

अतः, $\lambda$ का कोई वास्तविक मान ऐसा नहीं है जिस पर फलन संतत हो।
यदि, $x=1$,
$f(1)=4(1)+1=5$ तथा $\lim _{x \rightarrow 1} f(x)=\lim _{x \rightarrow 1} 4(1)+1=5$, यहाँ, $\lim _{x \rightarrow 1} f(x)=f(1)$
अतः, फलन $f, \lambda$ के सभी मानों के लिए संतत है।
:::

:::

:::question{number="19" kind="exercise" id="q_5.1.19" topic="Discontinuity of the fractional part function at integers"}
#### प्रश्न 19

:::prompt
दर्शाइए कि $g(x)=x-[x]$ द्वारा परिभाषित फलन समस्त पूर्णांक बिंदुओं पर असंतत है। यहाँ $[x]$ उस महत्तम पूर्णांक निरूपित करता है, जो $x$ के बराबर या $x$ से कम है।
:::

:::solution{label="हल"}
माना, $k$ कोई पूर्णांक संख्या है।
बाएँ पक्ष की सीमा $=\lim _{x \rightarrow k^{-}} f(x)=\lim _{x \rightarrow k^{-}} x-[x]=k-(\mathrm{k}-1)=1$
दाएँ पक्ष की सीमा $=\lim _{x \rightarrow k^{+}} f(x)=\lim _{x \rightarrow k^{+}} x-[x]=k-(\mathrm{k})=0$,
यहाँ, $x=k$ पर, फलन $f$ के बाएँ पक्ष की सीमा $\neq$ दाएँ पक्ष की सीमा,
अतः, समस्त पूर्णांक बिंदुओं पर, फलन $f$ संतत नहीं है।
:::

:::

:::question{number="20" kind="exercise" id="q_5.1.20" topic="Continuity of a trigonometric-polynomial function at x=pi"}
#### प्रश्न 20

:::prompt
क्या $f(x)=x^{2}-\sin x+5$ द्वारा परिभाषित फलन $x=\pi$ पर संतत है?
:::

:::solution{label="हल"}
दिया गया फलन $f(x)=x^{2}-\sin x+5$ तथा
$x=\pi$ पर, $f(\pi)=\pi^{2}-\sin \pi+5=\pi^{2}-0+5=\pi^{2}+5$
$\lim _{x \rightarrow n} f(x)=\lim _{x \rightarrow n} x^{2}-\sin x+5=\pi^{2}-\sin \pi+5=\pi^{2}-0+5=\pi^{2}+5$
यहाँ, $x=\pi$ पर, $\lim _{x \rightarrow n} f(x)=f(\pi)=\pi^{2}+5$
अतः, $x=\pi$ पर, फलन $f$ संतत है।
:::

:::

:::question{number="21" kind="exercise" id="q_5.1.21" topic="Continuity of sums, differences and products of sin and cos"}
#### प्रश्न 21

:::prompt
निम्नलिखित फलनों के सांतत्य पर विचार कीजिए:
:::

:::part{label="(a)"}
:::prompt
$f(x)=\sin x+\cos x$
:::

:::solution
माना, फलन $g(x)=\sin x$
माना, $k$ कोई वास्तविक संख्या है। $x=k$ पर, $g(k)=\sin k$
बाएँ पक्ष की सीमा
$\lim _{x \rightarrow k^{-}} g(x)=\lim _{x \rightarrow k^{-}} \sin x=\lim _{h \rightarrow 0} \sin (k-h)=\lim _{h \rightarrow 0} \sin k \cos h-\cos k \sin h=\sin k$
दाएँ पक्ष की सीमा
$\lim _{x \rightarrow k^{+}} g(x)=\lim _{x \rightarrow k^{+}} \sin x=\lim _{h \rightarrow 0} \sin (k+h)=\lim _{h \rightarrow 0} \sin k \cos h+\cos k \sin h=\sin k$
यहाँ, $x=k$ पर, फलन $g$ के बाएँ पक्ष की सीमा = दाएँ पक्ष की सीमा $=g(k)$
अतः, फलन $g$, समस्त वास्तविक बिंदुओं के लिए संतत है।
माना, फलन $h(x)=\cos x$
माना, $k$ कोई वास्तविक संख्या है। $x=k$ पर, $h(k)=\cos k$
बाएँ पक्ष की सीमा
$\lim _{x \rightarrow k^{-}} h(x)=\lim _{x \rightarrow k^{-}} \cos x=\lim _{h \rightarrow 0} \cos (k-h)=\lim _{h \rightarrow 0} \cos k \cos h+\sin k \sin h=\cos k$
दाएँ पक्ष की सीमा
$\lim _{x \rightarrow k^{+}} h(x)=\lim _{x \rightarrow k^{+}} \cos x=\lim _{h \rightarrow 0} \cos (k+h)=\lim _{h \rightarrow 0} \cos k \cos h-\sin k \sin h=\cos k$
यहाँ, $x=k$ पर, फलन $h$ के बाएँ पक्ष की सीमा = दाएँ पक्ष की सीमा $=h(k)$
अतः, फलन $h$, समस्त वास्तविक बिंदुओं के लिए संतत है।

हम जानते हैं कि यदि $g$ और $h$ दो संतत फलन हैं, तो $g+h, g-h$ और $g h$ भी संतत फलन होंगे। अतः, (a) $f(x)=\sin x+\cos x$ (b) $f(x)=\sin x-\cos x$ और (c) $f(x)=\sin x \cdot \cos x$ संतत फलन है।
:::

:::

:::part{label="(b)"}
:::prompt
$f(x)=\sin x-\cos x$
:::

:::solution
माना, फलन $g(x)=\sin x$
माना, $k$ कोई वास्तविक संख्या है। $x=k$ पर, $g(k)=\sin k$
बाएँ पक्ष की सीमा
$\lim _{x \rightarrow k^{-}} g(x)=\lim _{x \rightarrow k^{-}} \sin x=\lim _{h \rightarrow 0} \sin (k-h)=\lim _{h \rightarrow 0} \sin k \cos h-\cos k \sin h=\sin k$
दाएँ पक्ष की सीमा
$\lim _{x \rightarrow k^{+}} g(x)=\lim _{x \rightarrow k^{+}} \sin x=\lim _{h \rightarrow 0} \sin (k+h)=\lim _{h \rightarrow 0} \sin k \cos h+\cos k \sin h=\sin k$
यहाँ, $x=k$ पर, फलन $g$ के बाएँ पक्ष की सीमा = दाएँ पक्ष की सीमा $=g(k)$
अतः, फलन $g$, समस्त वास्तविक बिंदुओं के लिए संतत है।
माना, फलन $h(x)=\cos x$
माना, $k$ कोई वास्तविक संख्या है। $x=k$ पर, $h(k)=\cos k$
बाएँ पक्ष की सीमा
$\lim _{x \rightarrow k^{-}} h(x)=\lim _{x \rightarrow k^{-}} \cos x=\lim _{h \rightarrow 0} \cos (k-h)=\lim _{h \rightarrow 0} \cos k \cos h+\sin k \sin h=\cos k$
दाएँ पक्ष की सीमा
$\lim _{x \rightarrow k^{+}} h(x)=\lim _{x \rightarrow k^{+}} \cos x=\lim _{h \rightarrow 0} \cos (k+h)=\lim _{h \rightarrow 0} \cos k \cos h-\sin k \sin h=\cos k$
यहाँ, $x=k$ पर, फलन $h$ के बाएँ पक्ष की सीमा = दाएँ पक्ष की सीमा $=h(k)$
अतः, फलन $h$, समस्त वास्तविक बिंदुओं के लिए संतत है।

हम जानते हैं कि यदि $g$ और $h$ दो संतत फलन हैं, तो $g+h, g-h$ और $g h$ भी संतत फलन होंगे। अतः, (a) $f(x)=\sin x+\cos x$ (b) $f(x)=\sin x-\cos x$ और (c) $f(x)=\sin x \cdot \cos x$ संतत फलन है।
:::

:::

:::part{label="(c)"}
:::prompt
$f(x)=\sin x \cdot \cos x$
:::

:::solution
माना, फलन $g(x)=\sin x$
माना, $k$ कोई वास्तविक संख्या है। $x=k$ पर, $g(k)=\sin k$
बाएँ पक्ष की सीमा
$\lim _{x \rightarrow k^{-}} g(x)=\lim _{x \rightarrow k^{-}} \sin x=\lim _{h \rightarrow 0} \sin (k-h)=\lim _{h \rightarrow 0} \sin k \cos h-\cos k \sin h=\sin k$
दाएँ पक्ष की सीमा
$\lim _{x \rightarrow k^{+}} g(x)=\lim _{x \rightarrow k^{+}} \sin x=\lim _{h \rightarrow 0} \sin (k+h)=\lim _{h \rightarrow 0} \sin k \cos h+\cos k \sin h=\sin k$
यहाँ, $x=k$ पर, फलन $g$ के बाएँ पक्ष की सीमा = दाएँ पक्ष की सीमा $=g(k)$
अतः, फलन $g$, समस्त वास्तविक बिंदुओं के लिए संतत है।
माना, फलन $h(x)=\cos x$
माना, $k$ कोई वास्तविक संख्या है। $x=k$ पर, $h(k)=\cos k$
बाएँ पक्ष की सीमा
$\lim _{x \rightarrow k^{-}} h(x)=\lim _{x \rightarrow k^{-}} \cos x=\lim _{h \rightarrow 0} \cos (k-h)=\lim _{h \rightarrow 0} \cos k \cos h+\sin k \sin h=\cos k$
दाएँ पक्ष की सीमा
$\lim _{x \rightarrow k^{+}} h(x)=\lim _{x \rightarrow k^{+}} \cos x=\lim _{h \rightarrow 0} \cos (k+h)=\lim _{h \rightarrow 0} \cos k \cos h-\sin k \sin h=\cos k$
यहाँ, $x=k$ पर, फलन $h$ के बाएँ पक्ष की सीमा = दाएँ पक्ष की सीमा $=h(k)$
अतः, फलन $h$, समस्त वास्तविक बिंदुओं के लिए संतत है।

हम जानते हैं कि यदि $g$ और $h$ दो संतत फलन हैं, तो $g+h, g-h$ और $g h$ भी संतत फलन होंगे। अतः, (a) $f(x)=\sin x+\cos x$ (b) $f(x)=\sin x-\cos x$ और (c) $f(x)=\sin x \cdot \cos x$ संतत फलन है।
:::

:::

:::solution{label="हल"}
माना, फलन $g(x)=\sin x$
माना, $k$ कोई वास्तविक संख्या है। $x=k$ पर, $g(k)=\sin k$
बाएँ पक्ष की सीमा
$\lim _{x \rightarrow k^{-}} g(x)=\lim _{x \rightarrow k^{-}} \sin x=\lim _{h \rightarrow 0} \sin (k-h)=\lim _{h \rightarrow 0} \sin k \cos h-\cos k \sin h=\sin k$
दाएँ पक्ष की सीमा
$\lim _{x \rightarrow k^{+}} g(x)=\lim _{x \rightarrow k^{+}} \sin x=\lim _{h \rightarrow 0} \sin (k+h)=\lim _{h \rightarrow 0} \sin k \cos h+\cos k \sin h=\sin k$
यहाँ, $x=k$ पर, फलन $g$ के बाएँ पक्ष की सीमा = दाएँ पक्ष की सीमा $=g(k)$
अतः, फलन $g$, समस्त वास्तविक बिंदुओं के लिए संतत है।
माना, फलन $h(x)=\cos x$
माना, $k$ कोई वास्तविक संख्या है। $x=k$ पर, $h(k)=\cos k$
बाएँ पक्ष की सीमा
$\lim _{x \rightarrow k^{-}} h(x)=\lim _{x \rightarrow k^{-}} \cos x=\lim _{h \rightarrow 0} \cos (k-h)=\lim _{h \rightarrow 0} \cos k \cos h+\sin k \sin h=\cos k$
दाएँ पक्ष की सीमा
$\lim _{x \rightarrow k^{+}} h(x)=\lim _{x \rightarrow k^{+}} \cos x=\lim _{h \rightarrow 0} \cos (k+h)=\lim _{h \rightarrow 0} \cos k \cos h-\sin k \sin h=\cos k$
यहाँ, $x=k$ पर, फलन $h$ के बाएँ पक्ष की सीमा = दाएँ पक्ष की सीमा $=h(k)$
अतः, फलन $h$, समस्त वास्तविक बिंदुओं के लिए संतत है।

हम जानते हैं कि यदि $g$ और $h$ दो संतत फलन हैं, तो $g+h, g-h$ और $g h$ भी संतत फलन होंगे। अतः, (a) $f(x)=\sin x+\cos x$ (b) $f(x)=\sin x-\cos x$ और (c) $f(x)=\sin x \cdot \cos x$ संतत फलन है।
:::

:::

:::question{number="22" kind="exercise" id="q_5.1.22" topic="Continuity of cosine, cosecant, secant and cotangent"}
#### प्रश्न 22

:::prompt
cosine, cosecant, secant और cotangent फलनों के सांतत्य पर विचार कीजिए।
:::

:::solution{label="हल"}
माना, फलन $g(x)=\sin x$
माना, $k$ कोई वास्तविक संख्या है। $x=k$ पर, $g(k)=\sin k$
बाएँ पक्ष की सीमा
$\lim _{x \rightarrow k^{-}} g(x)=\lim _{x \rightarrow k^{-}} \sin x=\lim _{h \rightarrow 0} \sin (k-h)=\lim _{h \rightarrow 0} \sin k \cos h-\cos k \sin h=\sin k$ दाएँ पक्ष की सीमा
$\lim _{x \rightarrow k^{+}} g(x)=\lim _{x \rightarrow k^{+}} \sin x=\lim _{h \rightarrow 0} \sin (k+h)=\lim _{h \rightarrow 0} \sin k \cos h+\cos k \sin h=\sin k$ यहाँ, $x=k$ पर, फलन $g$ के बाएँ पक्ष की सीमा = दाएँ पक्ष की सीमा $=g(k)$
अतः, फलन $g$, समस्त वास्तविक बिंदुओं के लिए संतत है।
माना, फलन $h(x)=\cos x$
माना, $k$ कोई वास्तविक संख्या है। $x=k$ पर, $h(k)=\cos k$
बाएँ पक्ष की सीमा
$\lim _{x \rightarrow k^{-}} h(x)=\lim _{x \rightarrow k^{-}} \cos x=\lim _{h \rightarrow 0} \cos (k-h)=\lim _{h \rightarrow 0} \cos k \cos h+\sin k \sin h=\cos k$ दाएँ पक्ष की सीमा
$\lim _{x \rightarrow k^{+}} h(x)=\lim _{x \rightarrow k^{+}} \cos x=\lim _{h \rightarrow 0} \cos (k+h)=\lim _{h \rightarrow 0} \cos k \cos h-\sin k \sin h=\cos k$ यहाँ, $x=k$ पर, फलन $h$ के बाएँ पक्ष की सीमा = दाएँ पक्ष की सीमा $=h(k)$
अतः, फलन $h$, समस्त वास्तविक बिंदुओं के लिए संतत है।
हम जानते हैं कि यदि $g$ और $h$ दो संतत फलन हैं, तो
$\frac{g}{h}, h \neq 0$ संतत है, $\frac{1}{h}, h \neq 0$ संतत है और $\frac{1}{g}, g \neq 0$ भी संतत है।
इसलिए, $\operatorname{cosec} x=\frac{1}{\sin x}, \sin x \neq 0$, संतत है। $\Rightarrow x \neq n \pi(n \in Z)$, संतत है।
अतः, $\operatorname{cosec} x, x=n \pi(n \in Z)$, के अतिरिक्त सभी बिंदुओं पर संतत है।
$\sec x=\frac{1}{\cos x}, \cos x \neq 0$, संतत है। $\Rightarrow x \neq \frac{(2 n+1) \pi}{2}(n \in Z)$, संतत है।
अतः, $\sec x, x=\frac{(2 n+1) \pi}{2}(n \in Z)$, के अतिरिक्त सभी बिंदुओं पर संतत है।
$\cot x=\frac{\cos x}{\sin x}, \sin x \neq 0$, संतत है। $\Rightarrow x \neq n \pi(n \in Z)$, संतत है।
अतः, $\cot x, x=n \pi(n \in Z)$, के अतिरिक्त सभी बिंदुओं पर संतत है।
:::

:::

:::question{number="23" kind="exercise" id="q_5.1.23" topic="Points of discontinuity of a sinx/x piecewise function"}
#### प्रश्न 23

:::prompt
$f$ के सभी असांतत्यता के बिंदुओं को ज्ञात कीजिए, जहाँ
$$
f(x)= \begin{cases}\frac{\sin x}{x}, & \text { यदि } x<0 \\ x+1, & \text { यदि } x \geq 0\end{cases}
$$
:::

:::solution{label="हल"}
माना, $k$ कोई वास्तविक संख्या है। प्रश्नानुसार $k<0$ या $k=0$ या $k>0$
पहली स्थिति: यदि, $k<0$,
$f(k)=\frac{\sin k}{k}$ तथा $\lim _{x \rightarrow k} f(x)=\lim _{x \rightarrow k}\left(\frac{\sin x}{x}\right)=\frac{\sin k}{k}$, यहाँ, $\lim _{x \rightarrow k} f(x)=f(k)$
अतः, फलन $f, 0$ से छोटी सभी वास्तविक संख्याओं के लिए संतत है।
दूसरी स्थिति: यदि, $k=0$ पर, $f(0)=0+1=1$
बाएँ पक्ष की सीमा $=\lim _{x \rightarrow 0^{-}} f(x)=\lim _{x \rightarrow 0^{-}}(x+1)=0+1=1$
दाएँ पक्ष की सीमा $=\lim _{x \rightarrow 0^{+}} f(x)=\lim _{x \rightarrow 0^{+}}(x+1)=0+1=1$,
यहाँ, $x=0$ पर, फलन $f$ के बाएँ पक्ष की सीमा = दाएँ पक्ष की सीमा = $f(0)$
अतः, $x=0$ पर, फलन $f$ संतत है।
तीसरी स्थिति: यदि, $k>0$,
$f(k)=k+1$ तथा $\lim _{x \rightarrow k} f(x)=\lim _{x \rightarrow k}(\mathrm{x}+1)=\mathrm{k}+1$, यहाँ, $\lim _{x \rightarrow k} f(x)=f(k)$
अतः, फलन $f, x>0$, के लिए संतत है।
इसप्रकार, फलन $f$, सभी वास्तविक संख्याओं के लिए संतत है।
:::

:::

:::question{number="24" kind="exercise" id="q_5.1.24" topic="Continuity of x^2 sin(1/x) piecewise function at 0"}
#### प्रश्न 24

:::prompt
निर्धारित कीजिए कि फलन $f$
$$
f(x)= \begin{cases}x^{2} \sin \frac{1}{x}, & \text { यदि } x \neq 0 \\ 0, & \text { यदि } x=0\end{cases}
$$
द्वारा परिभाषित एक संतत फलन है।
:::

:::solution{label="हल"}
माना, $k$ कोई वास्तविक संख्या है। प्रश्नानुसार $k \neq 0$ या $k=0$
पहली स्थिति: यदि, $k \neq 0$,
$f(k)=k^{2} \sin \frac{1}{k}$ तथा $\lim _{x \rightarrow k} f(x)=\lim _{x \rightarrow k}\left(x^{2} \sin \frac{1}{x}\right)=k^{2} \sin \frac{1}{k^{\prime}}$ यहाँ, $\lim _{x \rightarrow k} f(x)=f(k)$
अतः, फलन $f, k \neq 0$ के लिए संतत है।
दूसरी स्थिति: यदि, $k=0$ पर, $f(0)=0$
बाएँ पक्ष की सीमा $=\lim _{x \rightarrow 0^{-}} f(x)=\lim _{x \rightarrow 0^{-}}\left(x^{2} \sin \frac{1}{x}\right)=\lim _{x \rightarrow 0}\left(x^{2} \sin \frac{1}{x}\right)$
हम जानते हैं कि, $-1 \leq \sin \frac{1}{x} \leq 1, x \neq 0 \quad \Rightarrow-x^{2} \leq \sin \frac{1}{x} \leq x^{2}$

$$
\begin{aligned}
& \Rightarrow \lim _{x \rightarrow 0}\left(-x^{2}\right) \leq \lim _{x \rightarrow 0} \sin \frac{1}{x} \leq \lim _{x \rightarrow 0} x^{2} \\
& \Rightarrow 0 \leq \lim _{x \rightarrow 0} \sin \frac{1}{x} \leq 0 \quad \Rightarrow \lim _{x \rightarrow 0} \sin \frac{1}{x}=0 \quad \Rightarrow \lim _{x \rightarrow 0^{-}} x^{2} \sin \frac{1}{x}=0 \quad \Rightarrow \lim _{x \rightarrow 0^{-}} f(x)=0
\end{aligned}
$$

इसीप्रकार, दाएँ पक्ष की सीमा $=\lim _{x \rightarrow 0^{+}} f(x)=\lim _{x \rightarrow 0^{+}}\left(x^{2} \sin \frac{1}{x}\right)=\lim _{x \rightarrow 0}\left(x^{2} \sin \frac{1}{x}\right)=0$,
यहाँ, $x=0$ पर, फलन $f$ के बाएँ पक्ष की सीमा = दाएँ पक्ष की सीमा = $f(0)$
अतः, $x=0$ पर, $f$ संतत है। इसप्रकार, फलन $f$, सभी वास्तविक संख्याओं के लिए संतत है।
:::

:::

:::question{number="25" kind="exercise" id="q_5.1.25" topic="Continuity of sinx-cosx piecewise function at 0"}
#### प्रश्न 25

:::prompt
$f$ के सांतत्य की जाँच कीजिए, जहाँ $f$ निम्नलिखित प्रकार से परिभाषित है
$$
f(x)= \begin{cases}\sin x-\cos x, & \text { यदि } x \neq 0 \\ -1, & \text { यदि } x=0\end{cases}
$$
:::

:::solution{label="हल"}
माना, $k$ कोई वास्तविक संख्या है। प्रश्नानुसार $k \neq 0$ या $k=0$
पहली स्थिति: यदि, $k \neq 0$ पर, $f(0)=0-1=-1$
बाएँ पक्ष की सीमा $=\lim _{k \rightarrow 0^{-}} f(x)=\lim _{k \rightarrow 0^{-}}(\sin x-\cos x)=0-1=-1$
दाएँ पक्ष की सीमा $=\lim _{k \rightarrow 0^{+}} f(x)=\lim _{k \rightarrow 0^{+}}(\sin x-\cos x)=0-1=-1$,
यहाँ, $x \neq 0$ पर, फलन $f$ के बाएँ पक्ष की सीमा = दाएँ पक्ष की सीमा = $f(x)$
अतः, फलन $f, x \neq 0$ पर संतत है।
दूसरी स्थिति: यदि, $k=0$ पर, $f(k)=-1$
तथा $\lim _{x \rightarrow k} f(x)=\lim _{x \rightarrow k}(-1)=-1$, यहाँ, $\lim _{x \rightarrow k} f(x)=f(k)$
अतः $x=0$ पर, $f$ संतत है। इसप्रकार, फलन $f$, सभी वास्तविक संख्याओं के लिए संतत है।
:::

:::

:::question{number="26" kind="exercise" id="q_5.1.26" topic="Value of k for continuity of k cosx/(pi-2x) piecewise function"}
#### प्रश्न 26

:::prompt
प्रश्न $26$ से $29$ में $k$ के मानों को ज्ञात कीजिए ताकि प्रदत्त फलन निर्दिष्ट बिंदु पर संतत हो:
$f(x)=\left\{\begin{array}{ll}\frac{k \cos x}{\pi-2 x}, & \text { यदि } x \neq \frac{\pi}{2} \\ 3, & \text { यदि } x=\frac{\pi}{2}\end{array}\right.$ द्वारा परिभाषित फलन $x=\frac{\pi}{2}$ पर
:::

:::solution{label="हल"}
दिया है: फलन $x=\frac{\pi}{2}$ पर संतत है। इसलिए, बाएँ पक्ष की सीमा = दाएँ पक्ष की सीमा $=f\left(\frac{\pi}{2}\right)$

$$
\begin{aligned}
& \Rightarrow \lim _{x \rightarrow \frac{\pi^{-}}{2}} f(x)=\lim _{x \rightarrow \frac{\pi^{+}}{2}} f(x)=f\left(\frac{\pi}{2}\right) \\
& \Rightarrow \lim _{x \rightarrow \frac{\pi}{2}} \frac{k \cos x}{\pi-2 x}=\lim _{x \rightarrow \frac{\pi^{+}}{2}} \frac{k \cos x}{\pi-2 x}=3 \\
& \Rightarrow \lim _{h \rightarrow 0} \frac{k \cos \left(\frac{\pi}{2}-h\right)}{\pi-2\left(\frac{\pi}{2}-h\right)}=\lim _{h \rightarrow 0} \frac{k \cos \left(\frac{\pi}{2}+h\right)}{\pi-2\left(\frac{\pi}{2}+h\right)}=3 \\
& \Rightarrow \lim _{h \rightarrow 0} \frac{k \sin h}{2 h}=\lim _{h \rightarrow 0} \frac{-k \sin h}{-2 h}=3 \\
& \Rightarrow \frac{k}{2}=\frac{k}{2}=3 \quad \quad\left[\because \lim _{h \rightarrow 0} \frac{\sin h}{h}=1\right] \\
& \Rightarrow k=6
\end{aligned}
$$
:::

:::answer
**उत्तर:** $k=6$
:::

:::

:::question{number="27" kind="exercise" id="q_5.1.27" topic="Value of k for continuity of kx^2 piecewise function at x=2"}
#### प्रश्न 27

:::prompt
प्रश्न $26$ से $29$ में $k$ के मानों को ज्ञात कीजिए ताकि प्रदत्त फलन निर्दिष्ट बिंदु पर संतत हो:
$f(x)=\left\{\begin{array}{ll}k x^{2}, & \text { यदि } x \leq 2 \\ 3, & \text { यदि } x>2\end{array}\right.$ द्वारा परिभाषित फलन $x=2$ पर
:::

:::solution{label="हल"}
दिया है: फलन $x=2$ पर संतत है। इसलिए, बाएँ पक्ष की सीमा = दाएँ पक्ष की सीमा = $f(2)$

$$
\begin{aligned}
& \Rightarrow \lim _{x \rightarrow 2^{-}} f(x)=\lim _{x \rightarrow 2^{+}} f(x)=f(2) \\
& \Rightarrow \lim _{x \rightarrow 2^{-}} k x^{2}=\lim _{x \rightarrow 2^{+}} 3=k(2)^{2} \\
& \Rightarrow 4 k=3=4 k \\
& \Rightarrow k=\frac{3}{4}
\end{aligned}
$$
:::

:::answer
**उत्तर:** $k=\frac{3}{4}$
:::

:::

:::question{number="28" kind="exercise" id="q_5.1.28" topic="Value of k for continuity of kx+1 piecewise function at x=pi"}
#### प्रश्न 28

:::prompt
प्रश्न $26$ से $29$ में $k$ के मानों को ज्ञात कीजिए ताकि प्रदत्त फलन निर्दिष्ट बिंदु पर संतत हो:
$f(x)=\left\{\begin{array}{ll}k x+1, & \text { यदि } x \leq \pi \\ \cos x, & \text { यदि } x>\pi\end{array}\right.$ द्वारा परिभाषित फलन $x=\pi$ पर
:::

:::solution{label="हल"}
दिया है: फलन $x=\pi$ पर संतत है। इसलिए, बाएँ पक्ष की सीमा = दाएँ पक्ष की सीमा $=f(\pi)$

$$
\begin{aligned}
& \Rightarrow \lim _{x \rightarrow \pi^{-}} f(x)=\lim _{x \rightarrow \pi^{+}} f(x)=f(\pi) \\
& \Rightarrow \lim _{x \rightarrow \pi^{-}} k x+1=\lim _{x \rightarrow \pi^{+}} \cos x=k(\pi)+1 \\
& \Rightarrow k(\pi)+1=\cos \pi=k \pi+1 \\
& \Rightarrow k \pi+1=-1=k \pi+1 \\
& \Rightarrow \pi k=-2 \quad \Rightarrow k=-\frac{2}{\pi}
\end{aligned}
$$
:::

:::answer
**उत्तर:** $k=-\frac{2}{\pi}$
:::

:::

:::question{number="29" kind="exercise" id="q_5.1.29" topic="Value of k for continuity of kx+1 piecewise function at x=5"}
#### प्रश्न 29

:::prompt
प्रश्न $26$ से $29$ में $k$ के मानों को ज्ञात कीजिए ताकि प्रदत्त फलन निर्दिष्ट बिंदु पर संतत हो:
$f(x)=\left\{\begin{array}{ll}k x+1, & \text { यदि } x \leq 5 \\ 3 x-5, & \text { यदि } x>5\end{array}\right.$ द्वारा परिभाषित फलन $x=5$ पर
:::

:::solution{label="हल"}
दिया है: फलन $x=5$ पर संतत है। इसलिए, बाएँ पक्ष की सीमा = दाएँ पक्ष की सीमा = $f(5)$

$$
\begin{aligned}
& \Rightarrow \lim _{x \rightarrow 5^{-}} f(x)=\lim _{x \rightarrow 5^{+}} f(x)=f(5) \\
& \Rightarrow \lim _{x \rightarrow 5^{-}} k x+1=\lim _{x \rightarrow 5^{+}} 3 x-5=5 k+1 \\
& \Rightarrow 5 k+1=15-5=5 k+1 \\
& \Rightarrow 5 k=9 \quad \Rightarrow k=\frac{9}{5}
\end{aligned}
$$
:::

:::answer
**उत्तर:** $k=\frac{9}{5}$
:::

:::

:::question{number="30" kind="exercise" id="q_5.1.30" topic="Values of a and b for continuity of a three-piece function"}
#### प्रश्न 30

:::prompt
$a$ तथा $b$ के मानों को ज्ञात कीजिए ताकि
$$
f(x)= \begin{cases}5, & \text { यदि } x \leq 2 \\ a x+b, & \text { यदि } 2<x<10 \\ 21, & \text { यदि } x \geq 10\end{cases}
$$
द्वारा परिभाषित फलन एक संतत फलन हो।
:::

:::solution{label="हल"}
दिया है: फलन $x=2$ पर संतत है। इसलिए, बाएँ पक्ष की सीमा = दाएँ पक्ष की सीमा = $f(2)$

$$
\begin{aligned}
& \Rightarrow \lim _{x \rightarrow 2^{-}} f(x)=\lim _{x \rightarrow 2^{+}} f(x)=f(2) \\
& \Rightarrow \lim _{x \rightarrow 2^{-}} 5=\lim _{x \rightarrow 2^{+}} a x+b=5
\end{aligned}
$$

$$
\Rightarrow 2 a+b=5
$$

फलन $x=10$ पर संतत है। इसलिए, बाएँ पक्ष की सीमा = दाएँ पक्ष की सीमा = $f(10)$

$$
\begin{aligned}
& \Rightarrow \lim _{x \rightarrow 10^{-}} f(x)=\lim _{x \rightarrow 10^{+}} f(x)=f(10) \\
& \Rightarrow \lim _{x \rightarrow 10^{-}} a x+b=\lim _{x \rightarrow 10^{+}} 21=21 \\
& \Rightarrow 10 a+b=21
\end{aligned}
$$

समीकरण (1) और (2) को हल करने पर

$$
a=2 \quad b=1
$$
:::

:::answer
**उत्तर:** $a=2, b=1$
:::

:::

:::question{number="31" kind="exercise" id="q_5.1.31" topic="Continuity of cos(x^2)"}
#### प्रश्न 31

:::prompt
दर्शाइए कि $f(x)=\cos \left(x^{2}\right)$ द्वारा परिभाषित फलन एक संतत फलन है।
:::

:::solution{label="हल"}
दिए गए फलन को प्रत्येक वास्तविक संख्या के लिए परिभाषित मानते हुए, फलन $f$ को दो फलनों $g$ और $h$ के संयोजन में लिख सकते हैं $(f=g o h)$ । जहाँ, $g(x)=\cos x$ और $h(x)=x^{2}$ है। यदि $g$ और $h$ दोनों ही संतत फलन हैं, तो $f$ भी एक संतत फलन होगा।

$$
\left[\because g o h(x)=g(h(x))=g\left(x^{2}\right)=\cos \left(x^{2}\right)\right]
$$

फलन $g(x)=\cos x$
माना, $k$ कोई वास्तविक संख्या है। $x=k$ पर, $g(k)=\cos k$

$$
\lim _{x \rightarrow k} g(x)=\lim _{x \rightarrow k} \cos x=\lim _{h \rightarrow 0} \cos (k+h)=\lim _{h \rightarrow 0} \cos k \cos h-\sin k \sin h=\cos k
$$

यहाँ, $\lim _{x \rightarrow k} g(x)=g(k)$, अतः, फलन $g$, सभी वास्तविक संख्याओं के लिए संतत है।
फलन $h(x)=x^{2}$
माना, $k$ कोई वास्तविक संख्या है। $x=k$ पर, $h(k)=k^{2}$

$$
\lim _{x \rightarrow k} h(x)=\lim _{x \rightarrow k} x^{2}=k^{2}
$$

यहाँ, $\lim _{x \rightarrow k} h(x)=h(k)$, अतः, फलन $h$, सभी वास्तविक संख्याओं के लिए संतत है।
इसप्रकार, $g$ और $h$ दोनों ही संतत फलन हैं, अतः $f$ भी एक संतत फलन होगा।
:::

:::

:::question{number="32" kind="exercise" id="q_5.1.32" topic="Continuity of the absolute value of cosine"}
#### प्रश्न 32

:::prompt
दर्शाइए कि $f(x)=|\cos x|$ द्वारा परिभाषित फलन एक संतत फलन है।
:::

:::solution{label="हल"}
दिए गए फलन को प्रत्येक वास्तविक संख्या के लिए परिभाषित मानते हुए, फलन $f$ को दो फलनों $g$ और $h$ के संयोजन में लिख सकते हैं $(f=g o h)$ । जहाँ, $g(x)=|x|$ और $h(x)=\cos x$ है। यदि $g$ और $h$ दोनों ही संतत फलन हैं, तो $f$ भी एक संतत फलन होगा।

$$
[\because g o h(x)=g(h(x))=g(\cos x)=|\cos x|]
$$

फलन $g(x)=|x|$
इस फलन $g$ को पुनः व्यवस्थित करने पर,

$$
g(x)= \begin{cases}-x, & \text { यदि } x<0 \\ \mathrm{x}, & \text { यदि } x \geq 0\end{cases}
$$

माना, $k$ कोई वास्तविक संख्या है। प्रश्नानुसार $k<0$ या $k=0$ या $k>0$
पहली स्थिति: यदि, $k<0$,
$g(k)=0$ तथा $\lim _{x \rightarrow k} g(x)=\lim _{x \rightarrow k}(-\mathrm{x})=0$, यहाँ, $\lim _{x \rightarrow k} g(x)=g(k)$

अतः, फलन $g, 0$ से छोटी सभी वास्तविक संख्याओं के लिए संतत है।
दूसरी स्थिति: यदि, $k=0$ पर, $g(0)=0+1=1$
बाएँ पक्ष की सीमा $=\lim _{x \rightarrow 0^{-}} g(x)=\lim _{x \rightarrow 0^{-}}(-x)=0$
दाएँ पक्ष की सीमा $=\lim _{x \rightarrow 0^{+}} g(x)=\lim _{x \rightarrow 0^{+}}(x)=0$,
यहाँ, $x=0$ पर, फलन $g$ के बाएँ पक्ष की सीमा = दाएँ पक्ष की सीमा $=g(0)$
अतः, $x=0$ पर, फलन $g$ संतत है।
तीसरी स्थिति: यदि, $k>0$,
$g(k)=0$ तथा $\lim _{x \rightarrow k} g(x)=\lim _{x \rightarrow k}(x)=0$, यहाँ, $\lim _{x \rightarrow k}(x)=g(k)$
अतः, फलन $g, x>0$, के लिए संतत है।
इसप्रकार, फलन $g$, सभी वास्तविक संख्याओं के लिए संतत है।
फलन $h(x)=\cos x$
माना, $k$ कोई वास्तविक संख्या है। $x=k$ पर, $h(k)=\cos k$
$\lim _{x \rightarrow k} h(x)=\lim _{x \rightarrow k} \cos x=\cos k$
यहाँ, $\lim _{x \rightarrow k} h(x)=h(k)$, अतः, फलन $h$, सभी वास्तविक संख्याओं के लिए संतत है।
इसप्रकार, $g$ और $h$ दोनों ही संतत फलन हैं, अतः $f$ भी एक संतत फलन होगा।
:::

:::

:::question{number="33" kind="exercise" id="q_5.1.33" topic="Continuity check of sin|x|"}
#### प्रश्न 33

:::prompt
जाँचिए कि क्या $\sin |x|$ एक संतत फलन है।
:::

:::solution{label="हल"}
दिए गए फलन को प्रत्येक वास्तविक संख्या के लिए परिभाषित मानते हुए, फलन $f$ को दो फलनों $h$ और $g$ के संयोजन में लिख सकते हैं $(f=h o g)$ । जहाँ, $h(x)=\sin x$ और $g(x)=|x|$ है। यदि $h$ और $g$ दोनों ही संतत फलन हैं, तो $f$ भी एक संतत फलन होगा।
$[\because h o g(x)=h(g(x))=h(|x|)=\sin |x|]$
फलन $h(x)=\sin x$
माना, $k$ कोई वास्तविक संख्या है। $x=k$ पर, $h(k)=\sin k$
$\lim _{x \rightarrow k} h(x)=\lim _{x \rightarrow k} \sin x=\sin k$
यहाँ, $\lim _{x \rightarrow k} h(x)=h(k)$, अतः, फलन $h$, सभी वास्तविक संख्याओं के लिए संतत है।
फलन $g(x)=|x|$
इस फलन $g$ को पुनः व्यवस्थित करने पर,

$$
g(x)= \begin{cases}-x, & \text { यदि } x<0 \\ \mathrm{x}, & \text { यदि } x \geq 0\end{cases}
$$

माना, $k$ कोई वास्तविक संख्या है। प्रश्नानुसार $k<0$ या $k=0$ या $k>0$
पहली स्थिति: यदि, $k<0$,
$g(k)=0$ तथा $\lim _{x \rightarrow k} g(x)=\lim _{x \rightarrow k}(-\mathrm{x})=0$, यहाँ, $\lim _{x \rightarrow k} g(x)=g(k)$
अतः, फलन $g, 0$ से छोटी सभी वास्तविक संख्याओं के लिए संतत है।
दूसरी स्थिति: यदि, $k=0$ पर, $g(0)=0+1=1$

बाएँ पक्ष की सीमा $=\lim _{x \rightarrow 0^{-}} g(x)=\lim _{x \rightarrow 0^{-}}(-x)=0$
दाएँ पक्ष की सीमा $=\lim _{x \rightarrow 0^{+}} g(x)=\lim _{x \rightarrow 0^{+}}(x)=0$,
यहाँ, $x=0$ पर, फलन $g$ के बाएँ पक्ष की सीमा = दाएँ पक्ष की सीमा $=g(0)$
अतः, $x=0$ पर, फलन $g$ संतत है।
तीसरी स्थिति: यदि, $k>0$,
$g(k)=0$ तथा $\lim _{x \rightarrow k} g(x)=\lim _{x \rightarrow k}(x)=0$, यहाँ, $\lim _{x \rightarrow k} g(x)=g(k)$
अतः, फलन $g, x>0$, के लिए संतत है।
इसप्रकार, फलन $g$, सभी वास्तविक संख्याओं के लिए संतत है।
इसप्रकार, $g$ और $h$ दोनों ही संतत फलन हैं, अतः $f$ भी एक संतत फलन होगा।
:::

:::

:::question{number="34" kind="exercise" id="q_5.1.34" topic="Points of discontinuity of |x|-|x+1|"}
#### प्रश्न 34

:::prompt
$f(x)=|x|-|x+1|$ द्वारा परिभाषित फलन $f$ के सभी असांत्यता के बिंदुओं को ज्ञात कीजिए।
:::

:::solution{label="हल"}
दिए गए फलन को प्रत्येक वास्तविक संख्या के लिए परिभाषित मानते हुए, फलन $f$ को दो फलनों $h$ और $g$ के संयोजन में लिख सकते हैं $(f=g-h)$ । जहाँ, $g(x)=|x|$ और $h(x)=|x+1|$ है। यदि $h$ और $g$ दोनों ही संतत फलन हैं, तो $f$ भी एक संतत फलन होगा।
फलन $g(x)=|x|$
इस फलन $g$ को पुनः व्यवस्थित करने पर,

$$
g(x)= \begin{cases}-x, & \text { यदि } x<0 \\ \mathrm{x}, & \text { यदि } x \geq 0\end{cases}
$$

माना, $k$ कोई वास्तविक संख्या है। प्रश्नानुसार $k<0$ या $k=0$ या $k>0$
पहली स्थिति: यदि, $k<0$,
$g(k)=0$ तथा $\lim _{x \rightarrow k} g(x)=\lim _{x \rightarrow k}(-\mathrm{x})=0$, यहाँ, $\lim _{x \rightarrow k}(x)=g(k)$
अतः, फलन $g, 0$ से छोटी सभी वास्तविक संख्याओं के लिए संतत है।
दूसरी स्थिति: यदि, $k=0$ पर, $g(0)=0+1=1$
बाएँ पक्ष की सीमा $=\lim _{x \rightarrow 0^{-}} g(x)=\lim _{x \rightarrow 0^{-}}(-x)=0$
दाएँ पक्ष की सीमा $=\lim _{x \rightarrow 0^{+}} g(x)=\lim _{x \rightarrow 0^{+}}(x)=0$,
यहाँ, $x=0$ पर, फलन $g$ के बाएँ पक्ष की सीमा = दाएँ पक्ष की सीमा $=g(0)$
अतः, $x=0$ पर, फलन $g$ संतत है।
तीसरी स्थिति: यदि, $k>0$,
$g(k)=0$ तथा $\lim _{x \rightarrow k} g(x)=\lim _{x \rightarrow k}(x)=0$, यहाँ, $\lim _{x \rightarrow k} g(x)=g(k)$
अतः, फलन $g, x>0$, के लिए संतत है।
इसप्रकार, फलन $g$, सभी वास्तविक संख्याओं के लिए संतत है।
फलन $h(x)=|x+1|$
इस फलन $h$ को पुनः व्यवस्थित करने पर,

$$
h(x)=\left\{\begin{array}{cc}
-(x+1), & \text { यदि } x<-1 \\
x+1, & \text { यदि } x \geq-1
\end{array}\right.
$$

माना, $k$ कोई वास्तविक संख्या है। प्रश्नानुसार $k<-1$ या $k=-1$ या $k>-1$
पहली स्थिति: यदि, $k<-1$,
$h(k)=-(k+1)$ तथा $\lim _{x \rightarrow k} h(x)=\lim _{x \rightarrow k}-(k+1)=-(k+1)$, यहाँ, $\lim _{x \rightarrow k} h(x)=h(k)$
अतः, फलन $h,-1$ से छोटी सभी वास्तविक संख्याओं के लिए संतत है।
दूसरी स्थिति: यदि, $k=-1$ पर, $h(-1)=-1+1=0$
बाएँ पक्ष की सीमा $=\lim _{x \rightarrow-1^{-}} h(x)=\lim _{x \rightarrow-1^{-}}-(-1+1)=0$
दाएँ पक्ष की सीमा $=\lim _{x \rightarrow-1^{+}} h(x)=\lim _{x \rightarrow-1^{+}}(x+1)=-1+1=0$,
यहाँ, $x=-1$ पर, फलन $h$ के बाएँ पक्ष की सीमा = दाएँ पक्ष की सीमा = $h(-1)$
अतः, $x=-1$ पर, फलन $h$ संतत है।
तीसरी स्थिति: यदि, $k>-1$,
$h(k)=k+1$ तथा $\lim _{x \rightarrow k} h(x)=\lim _{x \rightarrow k}(k+1)=\mathrm{k}+1$, यहाँ, $\lim _{x \rightarrow k} h(x)=h(k)$
अतः, फलन $h, x>-1$, के लिए संतत है।
इसप्रकार, फलन $h$, सभी वास्तविक संख्याओं के लिए संतत है।
इसप्रकार, $g$ और $h$ दोनों ही संतत फलन हैं, अतः $f$ भी एक संतत फलन होगा।
:::

:::

:::question{number="1" kind="exercise" id="q_5.2.1" topic="Chain rule differentiation"}
#### प्रश्न 1

:::prompt
$x$ के सापेक्ष निम्नलिखित फलन का अवकलन कीजिए: $\sin \left(x^{2}+5\right)$
:::

:::solution{label="हल"}
माना $y=\sin \left(x^{2}+5\right)$
इसलिए,

$$
\begin{aligned}
\frac{d y}{d x} & =\cos \left(x^{2}+5\right) \cdot \frac{d}{d x}\left(x^{2}+5\right) \\
& =\cos \left(x^{2}+5\right) \cdot 2 x
\end{aligned}
$$
:::

:::answer
**उत्तर:** $\cos \left(x^{2}+5\right) \cdot 2 x$
:::

:::

:::question{number="2" kind="exercise" id="q_5.2.2" topic="Chain rule differentiation"}
#### प्रश्न 2

:::prompt
$x$ के सापेक्ष निम्नलिखित फलन का अवकलन कीजिए: $\cos (\sin x)$
:::

:::solution{label="हल"}
माना $y=\cos (\sin x)$
इसलिए,

$$
\begin{aligned}
\frac{d y}{d x} & =-\sin (\sin x) \cdot \frac{d}{d x}(\sin x) \\
& =-\sin (\sin x) \cdot \cos x
\end{aligned}
$$
:::

:::answer
**उत्तर:** $-\sin (\sin x) \cdot \cos x$
:::

:::

:::question{number="3" kind="exercise" id="q_5.2.3" topic="Chain rule differentiation"}
#### प्रश्न 3

:::prompt
$x$ के सापेक्ष निम्नलिखित फलन का अवकलन कीजिए: $\sin (a x+b)$
:::

:::solution{label="हल"}
माना $y=\sin (a x+b)$
इसलिए,

$$
\begin{aligned}
\frac{d y}{d x} & =\cos (a x+b) \cdot \frac{d}{d x}(a x+b) \\
& =\cos (a x+b) \cdot a
\end{aligned}
$$
:::

:::answer
**उत्तर:** $\cos (a x+b) \cdot a$
:::

:::

:::question{number="4" kind="exercise" id="q_5.2.4" topic="Chain rule differentiation of nested functions"}
#### प्रश्न 4

:::prompt
$x$ के सापेक्ष निम्नलिखित फलन का अवकलन कीजिए: $\sec (\tan (\sqrt{x}))$
:::

:::solution{label="हल"}
माना $y=\sec (\tan (\sqrt{x}))$
इसलिए,

$$
\begin{aligned}
\frac{d y}{d x} & =\sec (\tan \sqrt{x}) \tan (\tan \sqrt{x}) \cdot \frac{d}{d x}(\tan \sqrt{x}) \\
& =\sec (\tan \sqrt{x}) \tan (\tan \sqrt{x}) \cdot \sec ^{2} \sqrt{x} \frac{d}{d x}(\sqrt{x}) \\
& =\sec (\tan \sqrt{x}) \tan (\tan \sqrt{x}) \cdot \sec ^{2} \sqrt{x}\left(\frac{1}{2 \sqrt{x}}\right)
\end{aligned}
$$
:::

:::answer
**उत्तर:** $\sec (\tan \sqrt{x}) \tan (\tan \sqrt{x}) \cdot \sec ^{2} \sqrt{x}\left(\frac{1}{2 \sqrt{x}}\right)$
:::

:::

:::question{number="5" kind="exercise" id="q_5.2.5" topic="Chain rule differentiation of a quotient"}
#### प्रश्न 5

:::prompt
$x$ के सापेक्ष निम्नलिखित फलन का अवकलन कीजिए: $\frac{\sin (a x+b)}{\cos (c x+d)}$
:::

:::solution{label="हल"}
माना

$$
y=\frac{\sin (a x+b)}{\cos (c x+d)}
$$

इसलिए,

$$
\begin{aligned}
& \frac{d y}{d x}=\frac{\cos (c x+d) \cdot \frac{d}{d x} \sin (a x+b)-\sin (a x+b) \cdot \frac{d}{d x} \cos (c x+d)}{[\cos (c x+d)]^{2}} \\
& =\frac{\cos (c x+d) \cdot \sin (a x+b) \cdot \frac{d}{d x}(a x+b)-\sin (a x+b) \cdot\left[-\sin (c x+d) \cdot \frac{d}{d x}(c x+d)\right]}{\cos ^{2}(c x+d)} \\
& =\frac{\cos (c x+d) \cdot \sin (a x+b) \cdot a+\sin (a x+b) \cdot \sin (c x+d) c}{\cos ^{2}(c x+d)}
\end{aligned}
$$
:::

:::answer
**उत्तर:** $\frac{\cos (c x+d) \cdot \sin (a x+b) \cdot a+\sin (a x+b) \cdot \sin (c x+d) c}{\cos ^{2}(c x+d)}$
:::

:::

:::question{number="6" kind="exercise" id="q_5.2.6" topic="Chain rule differentiation of a product"}
#### प्रश्न 6

:::prompt
$x$ के सापेक्ष निम्नलिखित फलन का अवकलन कीजिए: $\cos x^{3} \cdot \sin ^{2}\left(x^{5}\right)$
:::

:::solution{label="हल"}
माना $y=\cos x^{3} . \sin ^{2}\left(x^{5}\right)$
इसलिए,

$$
\begin{aligned}
\frac{d y}{d x} & =\cos x^{3} \cdot \frac{d}{d x} \sin ^{2}\left(x^{5}\right)+\sin ^{2}\left(x^{5}\right) \cdot \frac{d}{d x} \cos x^{3} \\
& =\cos x^{3} \cdot 2 \sin x^{5} \cos x^{5} \cdot \frac{d}{d x} x^{5}+\sin ^{2}\left(x^{5}\right)\left[-\sin x^{3}\right] \cdot \frac{d}{d x} x^{3} \\
& =\cos x^{3} \cdot 2 \sin x^{5} \cos x^{5} \cdot 5 x^{4}-\sin ^{2}\left(x^{5}\right) \sin x^{3} \cdot 3 x^{2}
\end{aligned}
$$
:::

:::answer
**उत्तर:** $\cos x^{3} \cdot 2 \sin x^{5} \cos x^{5} \cdot 5 x^{4}-\sin ^{2}\left(x^{5}\right) \sin x^{3} \cdot 3 x^{2}$
:::

:::

:::question{number="7" kind="exercise" id="q_5.2.7" topic="Chain rule differentiation with a square root"}
#### प्रश्न 7

:::prompt
$x$ के सापेक्ष निम्नलिखित फलन का अवकलन कीजिए: $2 \sqrt{\cot \left(x^{2}\right)}$
:::

:::solution{label="हल"}
माना $y=2 \sqrt{\cot \left(x^{2}\right)}$
इसलिए,

$$
\begin{aligned}
\frac{d y}{d x} & =2 \cdot \frac{1}{2 \sqrt{\cot \left(x^{2}\right)}} \cdot \frac{d}{d x}\left[\cot \left(x^{2}\right)\right] \\
& =\frac{1}{\sqrt{\cot \left(x^{2}\right)}} \cdot\left[-\operatorname{cossec} x^{2}\right] \cdot \frac{d}{d x} x^{2} \\
& =\frac{1}{\sqrt{\cot \left(x^{2}\right)}} \cdot\left[-\operatorname{cosec} x^{2}\right] \cdot 2 x
\end{aligned}
$$
:::

:::answer
**उत्तर:** $\frac{1}{\sqrt{\cot \left(x^{2}\right)}} \cdot\left[-\operatorname{cosec} x^{2}\right] \cdot 2 x$
:::

:::

:::question{number="8" kind="exercise" id="q_5.2.8" topic="Chain rule differentiation with a square root"}
#### प्रश्न 8

:::prompt
$x$ के सापेक्ष निम्नलिखित फलन का अवकलन कीजिए: $\cos (\sqrt{x})$
:::

:::solution{label="हल"}
माना $y=\cos (\sqrt{x})$
इसलिए,

$$
\begin{aligned}
\frac{d y}{d x} & =-\sin (\sqrt{x}) \cdot \frac{d}{d x} \sqrt{x} \\
& =-\sin (\sqrt{x}) \cdot \frac{1}{2 \sqrt{x}}
\end{aligned}
$$
:::

:::answer
**उत्तर:** $-\sin (\sqrt{x}) \cdot \frac{1}{2 \sqrt{x}}$
:::

:::

:::question{number="9" kind="exercise" id="q_5.2.9" topic="Non-differentiability of |x-1| at x=1"}
#### प्रश्न 9

:::prompt
सिद्ध कीजिए कि फलन $f(x)=|x-1|, x \in \mathbf{R}, x=1$ पर अवकलित नहीं है।
:::

:::solution{label="हल"}
$x=1$ पर,

$$
\begin{aligned}
& L H D=\lim _{h \rightarrow 0} \frac{f(1-h)-f(1)}{-h}=\lim _{h \rightarrow 0} \frac{|1-h-1|-|1-1|}{-h}=\lim _{h \rightarrow 0} \frac{h}{-h}=-1 \\
& R H D=\lim _{h \rightarrow 0} \frac{f(1+h)-f(1)}{h}=\lim _{h \rightarrow 0} \frac{|1+h-1|-|1-1|}{h}=\lim _{h \rightarrow 0} \frac{h}{h}=1
\end{aligned}
$$

यहाँ, $L H D \neq R H D$, इसलिए, फलन $f(x)=|x-1|, x \in \boldsymbol{R}, x=1$ पर अवकलित नहीं है।
:::

:::

:::question{number="10" kind="exercise" id="q_5.2.10" topic="Non-differentiability of the greatest integer function"}
#### प्रश्न 10

:::prompt
सिद्ध कीजिए कि महत्तम पूर्णांक फलन $f(x)=[x], 0<x<3, x=1$ तथा $x=2$ पर अवकलित नहीं है।
:::

:::solution{label="हल"}
$x=1$ पर,

$$
\begin{aligned}
& L H D=\lim _{h \rightarrow 0} \frac{f(1-h)-f(1)}{-h}=\lim _{h \rightarrow 0} \frac{[1-h]-|1|}{-h}=\lim _{h \rightarrow 0} \frac{0-1}{-h}=\infty \\
& R H D=\lim _{h \rightarrow 0} \frac{f(1+h)-f(1)}{h}=\lim _{h \rightarrow 0} \frac{[1+h]-[1]}{h}=\lim _{h \rightarrow 0} \frac{1-1}{h}=0
\end{aligned}
$$

यहाँ, $L H D \neq R H D$, इसलिए, फलन $f(x)=[x], 0<x<3, x=1$ पर अवकलित नहीं है।
$x=2$ पर,

$$
\begin{aligned}
& L H D=\lim _{h \rightarrow 0} \frac{f(1-h)-f(1)}{-h}=\lim _{h \rightarrow 0} \frac{[2-h]-[2]}{-h}=\lim _{h \rightarrow 0} \frac{1-2}{-h}=\infty \\
& R H D=\lim _{h \rightarrow 0} \frac{f(1+h)-f(1)}{h}=\lim _{h \rightarrow 0} \frac{[2+h]-[2]}{h}=\lim _{h \rightarrow 0} \frac{2-2}{h}=0
\end{aligned}
$$

यहाँ, $L H D \neq R H D$, इसलिए, फलन $f(x)=[x], 0<x<3, x=2$ पर अवकलित नहीं है।
:::

:::

:::question{number="1" kind="exercise" id="q_5.3.1" topic="Implicit differentiation"}
#### प्रश्न 1

:::prompt
निम्नलिखित प्रश्न में $\frac{d y}{d x}$ ज्ञात कीजिए: $2 x+3 y=\sin x$
:::

:::solution{label="हल"}
$$
2 x+3 y=\sin x
$$

दोनों पक्षों का $x$ के सापेक्ष अवकलन करने पर

$$
\begin{aligned}
& \frac{d}{d x}(2 x)+\frac{d}{d x}(3 y)=\frac{d}{d x} \sin x \\
& \Rightarrow 2+3 \frac{d y}{d x}=\cos x \quad \Rightarrow \frac{d y}{d x}=\frac{\cos x-2}{3}
\end{aligned}
$$
:::

:::answer
**उत्तर:** $\frac{d y}{d x}=\frac{\cos x-2}{3}$
:::

:::

:::question{number="2" kind="exercise" id="q_5.3.2" topic="Implicit differentiation"}
#### प्रश्न 2

:::prompt
निम्नलिखित प्रश्न में $\frac{d y}{d x}$ ज्ञात कीजिए: $2 x+3 y=\sin y$
:::

:::solution{label="हल"}
$$
2 x+3 y=\sin y
$$

दोनों पक्षों का $x$ के सापेक्ष अवकलन करने पर

$$
\begin{aligned}
& \frac{d}{d x}(2 x)+\frac{d}{d x}(3 y)=\frac{d}{d x} \sin y \\
& \Rightarrow 2+3 \frac{d y}{d x}=\cos y \frac{d y}{d x} \\
& \Rightarrow \frac{d y}{d x}(\cos y-3)=2 \quad \Rightarrow \frac{d y}{d x}=\frac{2}{\cos y-3}
\end{aligned}
$$
:::

:::answer
**उत्तर:** $\frac{d y}{d x}=\frac{2}{\cos y-3}$
:::

:::

:::question{number="3" kind="exercise" id="q_5.3.3" topic="Implicit differentiation"}
#### प्रश्न 3

:::prompt
निम्नलिखित प्रश्न में $\frac{d y}{d x}$ ज्ञात कीजिए: $a x+b y^{2}=\cos y$
:::

:::solution{label="हल"}
$$
a x+b y^{2}=\cos y
$$

दोनों पक्षों का $x$ के सापेक्ष अवकलन करने पर

$$
\begin{aligned}
& \frac{d}{d x}(a x)+\frac{d}{d x}\left(b y^{2}\right)=\frac{d}{d x} \cos y \\
& \Rightarrow a+2 b y \frac{d y}{d x}=-\sin y \frac{d y}{d x} \\
& \Rightarrow \frac{d y}{d x}(2 b y+\sin y)=-a \quad \Rightarrow \frac{d y}{d x}=-\frac{a}{2 b y+\sin y}
\end{aligned}
$$
:::

:::answer
**उत्तर:** $\frac{d y}{d x}=-\frac{a}{2 b y+\sin y}$
:::

:::

:::question{number="4" kind="exercise" id="q_5.3.4" topic="Implicit differentiation"}
#### प्रश्न 4

:::prompt
निम्नलिखित प्रश्न में $\frac{d y}{d x}$ ज्ञात कीजिए: $x y+y^{2}=\tan x+y$
:::

:::solution{label="हल"}
$$
x y+y^{2}=\tan x+y
$$

दोनों पक्षों का $x$ के सापेक्ष अवकलन करने पर

$$
\frac{d}{d x}(x y)+\frac{d}{d x}\left(y^{2}\right)=\frac{d}{d x} \tan x+\frac{d y}{d x}
$$

$$
\begin{aligned}
& \Rightarrow x \frac{d y}{d x}+y+2 y \frac{d y}{d x}=\sec ^{2} x+\frac{d y}{d x} \\
& \Rightarrow \frac{d y}{d x}(x+2 y-1)=\sec ^{2} x-y \quad \Rightarrow \frac{d y}{d x}=\frac{\sec ^{2} x-y}{x+2 y-1}
\end{aligned}
$$
:::

:::answer
**उत्तर:** $\frac{d y}{d x}=\frac{\sec ^{2} x-y}{x+2 y-1}$
:::

:::

:::question{number="5" kind="exercise" id="q_5.3.5" topic="Implicit differentiation"}
#### प्रश्न 5

:::prompt
निम्नलिखित प्रश्न में $\frac{d y}{d x}$ ज्ञात कीजिए: $x^{2}+x y+y^{2}=100$
:::

:::solution{label="हल"}
$$
x^{2}+x y+y^{2}=100
$$

दोनों पक्षों का $x$ के सापेक्ष अवकलन करने पर

$$
\begin{aligned}
& \frac{d}{d x} x^{2}+\frac{d}{d x}(x y)+\frac{d}{d x} y^{2}=\frac{d}{d x}(100) \\
& \Rightarrow 2 x+x \frac{d y}{d x}+y+2 y \frac{d y}{d x}=0 \\
& \Rightarrow \frac{d y}{d x}(x+2 y)=2 x+y \quad \Rightarrow \frac{d y}{d x}=\frac{2 x+y}{x+2 y}
\end{aligned}
$$
:::

:::answer
**उत्तर:** $\frac{d y}{d x}=\frac{2 x+y}{x+2 y}$
:::

:::

:::question{number="6" kind="exercise" id="q_5.3.6" topic="Implicit differentiation"}
#### प्रश्न 6

:::prompt
निम्नलिखित प्रश्न में $\frac{d y}{d x}$ ज्ञात कीजिए: $x^{3}+x^{2} y+x y^{2}+y^{3}=81$
:::

:::solution{label="हल"}
$$
x^{3}+x^{2} y+x y^{2}+y^{3}=81
$$

दोनों पक्षों का $x$ के सापेक्ष अवकलन करने पर

$$
\begin{aligned}
& \frac{d}{d x} x^{3}+\frac{d}{d x}\left(x^{2} y\right)+\frac{d}{d x}\left(x y^{2}\right)+\frac{d}{d x} y^{3}=\frac{d}{d x} 81 \\
& \Rightarrow 3 x^{2}+x^{2} \frac{d y}{d x}+y \cdot 2 x+x \cdot 2 y \frac{d y}{d x}+y^{2} \cdot 1+3 y^{2} \frac{d y}{d x}=0 \\
& \Rightarrow \frac{d y}{d x}\left(x^{2}+2 x y+3 y^{2}\right)=-\left(3 x^{2}+2 x y+y^{2}\right) \quad \Rightarrow \frac{d y}{d x}=-\frac{3 x^{2}+2 x y+y^{2}}{x^{2}+2 x y+3 y^{2}}
\end{aligned}
$$
:::

:::answer
**उत्तर:** $\frac{d y}{d x}=-\frac{3 x^{2}+2 x y+y^{2}}{x^{2}+2 x y+3 y^{2}}$
:::

:::

:::question{number="7" kind="exercise" id="q_5.3.7" topic="Implicit differentiation"}
#### प्रश्न 7

:::prompt
निम्नलिखित प्रश्न में $\frac{d y}{d x}$ ज्ञात कीजिए: $\sin ^{2} y+\cos x y=k$
:::

:::solution{label="हल"}
$$
\sin ^{2} y+\cos x y=k
$$

दोनों पक्षों का $x$ के सापेक्ष अवकलन करने पर

$$
\begin{aligned}
& \frac{d}{d x} \sin ^{2} y+\frac{d}{d x} \cos x y=\frac{d}{d x} k \\
& \Rightarrow 2 \sin y \cos y \frac{d y}{d x}-\sin x y\left(x \frac{d y}{d x}+y\right)=0 \\
& \Rightarrow \sin 2 y \frac{d y}{d x}-x \sin x y \frac{d y}{d x}-y \sin x y=0 \\
& \Rightarrow(\sin 2 y-x \sin x y) \frac{d y}{d x}=y \sin x y \\
& \Rightarrow \frac{d y}{d x}=\frac{y \sin x y}{\sin 2 y-x \sin x y}
\end{aligned}
$$
:::

:::answer
**उत्तर:** $\frac{d y}{d x}=\frac{y \sin x y}{\sin 2 y-x \sin x y}$
:::

:::

:::question{number="8" kind="exercise" id="q_5.3.8" topic="Implicit differentiation"}
#### प्रश्न 8

:::prompt
निम्नलिखित प्रश्न में $\frac{d y}{d x}$ ज्ञात कीजिए: $\sin ^{2} x+\cos ^{2} y=1$
:::

:::solution{label="हल"}
$$
\sin ^{2} x+\cos ^{2} y=1
$$

दोनों पक्षों का $x$ के सापेक्ष अवकलन करने पर

$$
\begin{aligned}
& \frac{d}{d x} \sin ^{2} x+\frac{d}{d x} \cos ^{2} y=\frac{d}{d x} 1 \\
& \Rightarrow 2 \sin x \cos x+2 \cos y(-\sin y) \frac{d y}{d x}=0 \\
& \Rightarrow \sin 2 x-\sin 2 y \frac{d y}{d x}=0 \quad \Rightarrow \frac{d y}{d x}=\frac{\sin 2 x}{\sin 2 y}
\end{aligned}
$$
:::

:::answer
**उत्तर:** $\frac{d y}{d x}=\frac{\sin 2 x}{\sin 2 y}$
:::

:::

:::question{number="9" kind="exercise" id="q_5.3.9" topic="Derivative of an inverse-sine double-angle form"}
#### प्रश्न 9

:::prompt
निम्नलिखित प्रश्न में $\frac{d y}{d x}$ ज्ञात कीजिए: $y=\sin ^{-1}\left(\frac{2 x}{1+x^{2}}\right)$
:::

:::solution{label="हल"}
$$
y=\sin ^{-1}\left(\frac{2 x}{1+x^{2}}\right)
$$

माना, $x=\tan \theta$
इसलिए, $y=\sin ^{-1}\left(\frac{2 \tan \theta}{1+\tan ^{2} \theta}\right)=\sin ^{-1}(\sin 2 \theta)=2 \theta=2 \tan ^{-1} x$
$\Rightarrow y=2 \tan ^{-1} x$
दोनों पक्षों का $x$ के सापेक्ष अवकलन करने पर

$$
\frac{d y}{d x}=\frac{2}{1+x^{2}}
$$
:::

:::answer
**उत्तर:** $\frac{d y}{d x}=\frac{2}{1+x^{2}}$
:::

:::

:::question{number="10" kind="exercise" id="q_5.3.10" topic="Derivative of an inverse-tangent triple-angle form"}
#### प्रश्न 10

:::prompt
निम्नलिखित प्रश्न में $\frac{d y}{d x}$ ज्ञात कीजिए: $y=\tan ^{-1}\left(\frac{3 x-x^{3}}{1-3 x^{2}}\right),-\frac{1}{\sqrt{3}}<x<\frac{1}{\sqrt{3}}$
:::

:::solution{label="हल"}
$$
y=\tan ^{-1}\left(\frac{3 x-x^{3}}{1-3 x^{2}}\right)
$$

माना, $x=\tan \theta$
इसलिए, $y=\tan ^{-1}\left(\frac{3 \tan \theta-\tan ^{3} \theta}{1-3 \tan ^{2} \theta}\right)=\tan ^{-1}(\tan 3 \theta)=3 \theta=3 \tan ^{-1} x$
$\Rightarrow y=3 \tan ^{-1} x$
दोनों पक्षों का $x$ के सापेक्ष अवकलन करने पर

$$
\frac{d y}{d x}=\frac{3}{1+x^{2}}
$$
:::

:::answer
**उत्तर:** $\frac{d y}{d x}=\frac{3}{1+x^{2}}$
:::

:::

:::question{number="11" kind="exercise" id="q_5.3.11" topic="Derivative of an inverse-cosine double-angle form"}
#### प्रश्न 11

:::prompt
निम्नलिखित प्रश्न में $\frac{d y}{d x}$ ज्ञात कीजिए: $y=\cos ^{-1}\left(\frac{1-x^{2}}{1+x^{2}}\right), 0<x<1$
:::

:::solution{label="हल"}
$$
y=\cos ^{-1}\left(\frac{1-x^{2}}{1+x^{2}}\right)
$$

माना, $x=\tan \theta$

इसलिए, $y=\cos ^{-1}\left(\frac{1-\tan ^{2} \theta}{1+\tan ^{2} \theta}\right)=\cos ^{-1}(\cos 2 \theta)=2 \theta=2 \tan ^{-1} x$
$\Rightarrow y=2 \tan ^{-1} x$
दोनों पक्षों का $x$ के सापेक्ष अवकलन करने पर

$$
\frac{d y}{d x}=\frac{2}{1+x^{2}}
$$
:::

:::answer
**उत्तर:** $\frac{d y}{d x}=\frac{2}{1+x^{2}}$
:::

:::

:::question{number="12" kind="exercise" id="q_5.3.12" topic="Derivative of an inverse-sine double-angle form"}
#### प्रश्न 12

:::prompt
निम्नलिखित प्रश्न में $\frac{d y}{d x}$ ज्ञात कीजिए: $y=\sin ^{-1}\left(\frac{1-x^{2}}{1+x^{2}}\right), 0<x<1$
:::

:::solution{label="हल"}
$$
y=\sin ^{-1}\left(\frac{1-x^{2}}{1+x^{2}}\right)
$$

माना, $x=\tan \theta$
इसलिए,

$$
\begin{aligned}
& y=\sin ^{-1}\left(\frac{1-\tan ^{2} \theta}{1+\tan ^{2} \theta}\right) \\
& =\sin ^{-1}(\cos 2 \theta)=\sin ^{-1}\left\{\sin \left(\frac{\pi}{2}-2 \theta\right)\right\}=\frac{\pi}{2}-2 \theta=\frac{\pi}{2}-2 \tan ^{-1} x \\
& \Rightarrow y=\frac{\pi}{2}-2 \tan ^{-1} x
\end{aligned}
$$

दोनों पक्षों का $x$ के सापेक्ष अवकलन करने पर

$$
\frac{d y}{d x}=0-\frac{2}{1+x^{2}}=-\frac{2}{1+x^{2}}
$$
:::

:::answer
**उत्तर:** $\frac{d y}{d x}=-\frac{2}{1+x^{2}}$
:::

:::

:::question{number="13" kind="exercise" id="q_5.3.13" topic="Derivative of an inverse-cosine double-angle form"}
#### प्रश्न 13

:::prompt
निम्नलिखित प्रश्न में $\frac{d y}{d x}$ ज्ञात कीजिए: $y=\cos ^{-1}\left(\frac{2 x}{1+x^{2}}\right),-1<x<1$
:::

:::solution{label="हल"}
$$
y=\cos ^{-1}\left(\frac{2 x}{1+x^{2}}\right)
$$

माना, $x=\tan \theta$
इसलिए, $y=\cos ^{-1}\left(\frac{2 \tan \theta}{1+\tan ^{2} \theta}\right)$

$$
\begin{aligned}
& =\cos ^{-1}(\sin 2 \theta)=\cos ^{-1}\left\{\cos \left(\frac{\pi}{2}-2 \theta\right)\right\}=\frac{\pi}{2}-2 \theta=\frac{\pi}{2}-2 \tan ^{-1} x \\
& \Rightarrow y=\frac{\pi}{2}-2 \tan ^{-1} x
\end{aligned}
$$

दोनों पक्षों का $x$ के सापेक्ष अवकलन करने पर

$$
\frac{d y}{d x}=0-\frac{2}{1+x^{2}}=-\frac{2}{1+x^{2}}
$$
:::

:::answer
**उत्तर:** $\frac{d y}{d x}=-\frac{2}{1+x^{2}}$
:::

:::

:::question{number="14" kind="exercise" id="q_5.3.14" topic="Derivative of an inverse-sine double-angle form"}
#### प्रश्न 14

:::prompt
निम्नलिखित प्रश्न में $\frac{d y}{d x}$ ज्ञात कीजिए: $y=\sin ^{-1}\left(2 x \sqrt{1-x^{2}}\right),-\frac{1}{\sqrt{2}}<x<\frac{1}{\sqrt{2}}$
:::

:::solution{label="हल"}
$$
y=\sin ^{-1}\left(2 x \sqrt{1-x^{2}}\right)
$$

माना, $x=\sin \theta$

इसलिए, $y=\sin ^{-1}\left(2 \sin \theta \sqrt{1-\sin ^{2} \theta}\right)$

$$
\begin{aligned}
& =\sin ^{-1}(2 \sin \theta \cos \theta)=\sin ^{-1}(\sin 2 \theta)=2 \theta=2 \sin ^{-1} x \\
& \Rightarrow y=2 \sin ^{-1} x
\end{aligned}
$$

दोनों पक्षों का $x$ के सापेक्ष अवकलन करने पर

$$
\frac{d y}{d x}=\frac{2}{\sqrt{1-x^{2}}}
$$
:::

:::answer
**उत्तर:** $\frac{d y}{d x}=\frac{2}{\sqrt{1-x^{2}}}$
:::

:::

:::question{number="15" kind="exercise" id="q_5.3.15" topic="Derivative of an inverse-secant double-angle form"}
#### प्रश्न 15

:::prompt
निम्नलिखित प्रश्न में $\frac{d y}{d x}$ ज्ञात कीजिए: $y=\sec ^{-1}\left(\frac{1}{2 x^{2}-1}\right), 0<x<\frac{1}{\sqrt{2}}$
:::

:::solution{label="हल"}
$$
y=\sec ^{-1}\left(\frac{1}{2 x^{2}-1}\right)
$$

माना, $x=\cos \theta$
इसलिए, $y=\sec ^{-1}\left(\frac{1}{2 \cos ^{2} \theta-1}\right)=\sec ^{-1}\left(\frac{1}{\cos 2 \theta}\right)=\sec ^{-1}(\sec 2 \theta)=2 \theta=2 \cos ^{-1} x$

$$
\Rightarrow y=2 \cos ^{-1} x
$$

दोनों पक्षों का $x$ के सापेक्ष अवकलन करने पर

$$
\frac{d y}{d x}=-\frac{2}{\sqrt{1-x^{2}}}
$$
:::

:::answer
**उत्तर:** $\frac{d y}{d x}=-\frac{2}{\sqrt{1-x^{2}}}$
:::

:::

:::question{number="1" kind="exercise" id="q_5.4.1" topic="Derivative of an exponential-over-trig quotient"}
#### प्रश्न 1

:::prompt
$x$ के सापेक्ष निम्नलिखित का अवकलन कीजिए: $\frac{e^{x}}{\sin x}$
:::

:::solution{label="हल"}
माना $y=\frac{e^{x}}{\sin x^{x}}$ इसलिए,

$$
\frac{d y}{d x}=\frac{e^{x} \cdot \frac{d}{d x} \sin x-\sin x \frac{d}{d x} e^{x}}{\sin ^{2} x}=\frac{e^{x} \cdot \cos x-\sin x \cdot e^{x}}{\sin ^{2} x}=\frac{e^{x}(\cos x-\sin x)}{\sin ^{2} x}
$$
:::

:::answer
**उत्तर:** $\frac{e^{x}(\cos x-\sin x)}{\sin ^{2} x}$
:::

:::

:::question{number="2" kind="exercise" id="q_5.4.2" topic="Derivative of an exponential of arcsine"}
#### प्रश्न 2

:::prompt
$x$ के सापेक्ष निम्नलिखित का अवकलन कीजिए: $e^{\sin ^{-1} x}$
:::

:::solution{label="हल"}
माना $y=e^{\sin ^{-1} x}$, इसलिए,

$$
\frac{d y}{d x}=e^{\sin ^{-1} x} \cdot \frac{d}{d x} \sin ^{-1} x=e^{\sin ^{-1} x} \cdot \frac{1}{\sqrt{1-x^{2}}}=\frac{e^{\sin ^{-1} x}}{\sqrt{1-x^{2}}}
$$
:::

:::answer
**उत्तर:** $\frac{e^{\sin ^{-1} x}}{\sqrt{1-x^{2}}}$
:::

:::

:::question{number="3" kind="exercise" id="q_5.4.3" topic="Derivative of an exponential with a cubic exponent"}
#### प्रश्न 3

:::prompt
$x$ के सापेक्ष निम्नलिखित का अवकलन कीजिए: $e^{x^{3}}$
:::

:::solution{label="हल"}
माना $y=e^{x^{3}}$, इसलिए,

$$
\frac{d y}{d x}=e^{x^{3}} \cdot \frac{d}{d x} x^{3}=e^{x^{3}} \cdot 3 x^{2}=3 x^{2} e^{x^{3}}
$$
:::

:::answer
**उत्तर:** $3 x^{2} e^{x^{3}}$
:::

:::

:::question{number="4" kind="exercise" id="q_5.4.4" topic="Derivative of a sine of an inverse-tangent exponential"}
#### प्रश्न 4

:::prompt
$x$ के सापेक्ष निम्नलिखित का अवकलन कीजिए: $\sin \left(\tan ^{-1} e^{-x}\right)$
:::

:::solution{label="हल"}
माना $y=\sin \left(\tan ^{-1} e^{-x}\right)$, इसलिए,

$$
\begin{aligned}
& \frac{d y}{d x}=\cos \left(\tan ^{-1} e^{-x}\right) \cdot \frac{d}{d x} \tan ^{-1} e^{-x}=\cos \left(\tan ^{-1} e^{-x}\right) \cdot \frac{1}{1+\left(e^{-x}\right)^{2}} \cdot \frac{d}{d x} e^{-x} \\
& =\cos \left(\tan ^{-1} e^{-x}\right) \cdot \frac{1}{1+e^{-2 x}} \cdot\left(-e^{-x}\right)=-\frac{e^{-x} \cos \left(\tan ^{-1} e^{-x}\right)}{1+e^{-2 x}}
\end{aligned}
$$
:::

:::answer
**उत्तर:** $-\frac{e^{-x} \cos \left(\tan ^{-1} e^{-x}\right)}{1+e^{-2 x}}$
:::

:::

:::question{number="5" kind="exercise" id="q_5.4.5" topic="Derivative of a log-of-cosine-of-exponential"}
#### प्रश्न 5

:::prompt
$x$ के सापेक्ष निम्नलिखित का अवकलन कीजिए: $\log \left(\cos e^{x}\right)$
:::

:::solution{label="हल"}
माना $y=\log \left(\cos e^{x}\right)$, इसलिए,

$$
\frac{d y}{d x}=\frac{1}{\cos e^{x}} \cdot \frac{d}{d x} \cos e^{x}=\frac{1}{\cos e^{x}}\left(-\sin e^{x}\right) \frac{d}{d x} e^{x}=-\tan e^{x} \cdot e^{x}
$$
:::

:::answer
**उत्तर:** $-\tan e^{x} \cdot e^{x}$
:::

:::

:::question{number="6" kind="exercise" id="q_5.4.6" topic="Derivative of a sum of exponentials"}
#### प्रश्न 6

:::prompt
$x$ के सापेक्ष निम्नलिखित का अवकलन कीजिए: $e^{x}+e^{x^{2}}+\ldots+e^{x^{5}}$
:::

:::solution{label="हल"}
माना $y=e^{x}+e^{x^{2}}+e^{x^{3}}+e^{x^{4}}+e^{x^{5}}$, इसलिए,

$$
\begin{aligned}
\frac{d y}{d x} & =e^{x}+e^{x^{2}} \frac{d}{d x} x^{2}+e^{x^{3}} \frac{d}{d x} x^{3}+e^{x^{4}} \frac{d}{d x} x^{4}+e^{x^{5}} \frac{d}{d x} x^{5} \\
& =e^{x}+e^{x^{2}} \cdot 2 x+e^{x^{3}} \cdot 3 x^{2}+e^{x^{4}} \cdot 4 x^{3}+e^{x^{5}} \cdot 5 x^{4} \\
& =e^{x}+2 x e^{x^{2}}+3 x^{2} e^{x^{3}}+4 x^{3} e^{x^{4}}+5 x^{4} e^{x^{5}}
\end{aligned}
$$
:::

:::answer
**उत्तर:** $e^{x}+2 x e^{x^{2}}+3 x^{2} e^{x^{3}}+4 x^{3} e^{x^{4}}+5 x^{4} e^{x^{5}}$
:::

:::

:::question{number="7" kind="exercise" id="q_5.4.7" topic="Derivative of a square root of an exponential"}
#### प्रश्न 7

:::prompt
$x$ के सापेक्ष निम्नलिखित का अवकलन कीजिए: $\sqrt{e^{\sqrt{x}}}, x>0$
:::

:::solution{label="हल"}
माना $y=\sqrt{e^{\sqrt{x}}}$
इसलिए,

$$
\frac{d y}{d x}=\frac{1}{2 \sqrt{e^{\sqrt{x}}}} \frac{d}{d x} e^{\sqrt{x}}=\frac{1}{2 \sqrt{e^{\sqrt{x}}}} \cdot e^{\sqrt{x}} \cdot \frac{d}{d x} \sqrt{x}=\frac{1}{2 \sqrt{e^{\sqrt{x}}}} \cdot e^{\sqrt{x}} \cdot \frac{1}{2 \sqrt{x}}=\frac{\sqrt{e^{\sqrt{x}}}}{4 \sqrt{x}}
$$
:::

:::answer
**उत्तर:** $\frac{\sqrt{e^{\sqrt{x}}}}{4 \sqrt{x}}$
:::

:::

:::question{number="8" kind="exercise" id="q_5.4.8" topic="Derivative of log of log"}
#### प्रश्न 8

:::prompt
$x$ के सापेक्ष निम्नलिखित का अवकलन कीजिए: $\log (\log x), x>1$
:::

:::solution{label="हल"}
माना $y=\frac{e^{x}}{\sin x}$
इसलिए,

$$
\frac{d y}{d x}=\frac{1}{\log x} \cdot \frac{d}{d x} \log x=\frac{1}{\log x} \cdot \frac{1}{x}=\frac{1}{x \log x}
$$
:::

:::answer
**उत्तर:** $\frac{1}{x \log x}$
:::

:::

:::question{number="9" kind="exercise" id="q_5.4.9" topic="Derivative of a cosine-over-log quotient"}
#### प्रश्न 9

:::prompt
$x$ के सापेक्ष निम्नलिखित का अवकलन कीजिए: $\frac{\cos x}{\log x}, x>0$
:::

:::solution{label="हल"}
माना $y=\frac{\cos x}{\log x}$
इसलिए, $\frac{d y}{d x}=\frac{\log x \frac{d}{d x} \cos x-\cos x \frac{d}{d x} \log x}{(\log x)^{2}}=\frac{\log x .(-\sin x)-\cos x . \frac{1}{x}}{(\log x)^{2}}=\frac{-(x \sin x \log x+\cos x)}{x(\log x)^{2}}$
:::

:::answer
**उत्तर:** $\frac{-(x \sin x \log x+\cos x)}{x(\log x)^{2}}$
:::

:::

:::question{number="10" kind="exercise" id="q_5.4.10" topic="Derivative of cosine of a log-plus-exponential"}
#### प्रश्न 10

:::prompt
$x$ के सापेक्ष निम्नलिखित का अवकलन कीजिए: $\cos \left(\log x+e^{x}\right)$
:::

:::solution{label="हल"}
माना $y=\cos \left(\log x+e^{x}\right)$
इसलिए,

$$
\frac{d y}{d x}=-\sin \left(\log x+e^{x}\right) \cdot \frac{d}{d x}\left(\log x+e^{x}\right)=-\sin \left(\log x+e^{x}\right) \cdot\left(\frac{1}{x}+e^{x}\right)
$$
:::

:::answer
**उत्तर:** $-\sin \left(\log x+e^{x}\right) \cdot\left(\frac{1}{x}+e^{x}\right)$
:::

:::

:::question{number="1" kind="exercise" id="q_5.5.1" topic="Logarithmic differentiation of a triple product"}
#### प्रश्न 1

:::prompt
$1$ से $11$ तक के प्रश्नों में प्रदत्त फलनों का $x$ के सापेक्ष अवकलन कीजिए: $\cos x . \cos 2 x . \cos 3 x$
:::

:::solution{label="हल"}
माना $y=\cos x . \cos 2 x . \cos 3 x$, दोनों ओर $\log$ लेने पर

$$
\log y=\log \cos x+\log \cos 2 x+\log \cos 3 x
$$

इसलिए,

$$
\begin{aligned}
& \frac{1}{y} \frac{d y}{d x}=\frac{1}{\cos x} \cdot \frac{d}{d x} \cos x+\frac{1}{\cos 2 x} \cdot \frac{d}{d x} \cos 2 x+\frac{1}{\cos 3 x} \cdot \frac{d}{d x} \cos 3 x \\
& \Rightarrow \frac{d y}{d x}=y\left[\frac{1}{\cos x} \cdot(-\sin x)+\frac{1}{\cos 2 x} \cdot(-\sin 2 x) \cdot 2+\frac{1}{\cos 3 x} \cdot(-\sin 3 x) \cdot 3\right] \\
& \Rightarrow \frac{d y}{d x}=\cos x \cdot \cos 2 x \cdot \cos 3 x[-\tan x-2 \tan 2 x-3 \tan 3 x]
\end{aligned}
$$
:::

:::answer
**उत्तर:** $\cos x \cdot \cos 2 x \cdot \cos 3 x[-\tan x-2 \tan 2 x-3 \tan 3 x]$
:::

:::

:::question{number="2" kind="exercise" id="q_5.5.2" topic="Logarithmic differentiation of a nested radical quotient"}
#### प्रश्न 2

:::prompt
$1$ से $11$ तक के प्रश्नों में प्रदत्त फलनों का $x$ के सापेक्ष अवकलन कीजिए: $\sqrt{\frac{(x-1)(x-2)}{(x-3)(x-4)(x-5)}}$
:::

:::solution{label="हल"}
माना $y=\sqrt{\frac{(x-1)(x-2)}{(x-3)(x-4)(x-5)}}$, दोनों ओर $\log$ लेने पर

$$
\log y=\frac{1}{2}[\log (x-1)+\log (x-2)-\log (x-3)-\log (x-4)-\log (x-5)]
$$

इसलिए,

$$
\begin{aligned}
& \frac{1}{y} \frac{d y}{d x}=\frac{1}{2}\left[\frac{1}{(x-1)}+\frac{1}{(x-2)}-\frac{1}{(x-3)}-\frac{1}{(x-4)}-\frac{1}{(x-5)}\right] \\
& \Rightarrow \frac{d y}{d x}=\frac{1}{2} \sqrt{\frac{(x-1)(x-2)}{(x-3)(x-4)(x-5)}}\left[\frac{1}{(x-1)}+\frac{1}{(x-2)}-\frac{1}{(x-3)}-\frac{1}{(x-4)}-\frac{1}{(x-5)}\right]
\end{aligned}
$$
:::

:::answer
**उत्तर:** $\frac{1}{2} \sqrt{\frac{(x-1)(x-2)}{(x-3)(x-4)(x-5)}}\left[\frac{1}{(x-1)}+\frac{1}{(x-2)}-\frac{1}{(x-3)}-\frac{1}{(x-4)}-\frac{1}{(x-5)}\right]$
:::

:::

:::question{number="3" kind="exercise" id="q_5.5.3" topic="Logarithmic differentiation of (log x)^cos x"}
#### प्रश्न 3

:::prompt
$1$ से $11$ तक के प्रश्नों में प्रदत्त फलनों का $x$ के सापेक्ष अवकलन कीजिए: $(\log x)^{\cos x}$
:::

:::solution{label="हल"}
माना $y=(\log x)^{\cos x}$, दोनों ओर $\log$ लेने पर
$\log y=\log (\log x)^{\cos x}=\cos x . \log \log x$
इसलिए,

$$
\begin{aligned}
& \frac{1}{y} \frac{d y}{d x}=\cos x \cdot \frac{d}{d x} \log \log x+\log \log x \cdot \frac{d}{d x} \cos x \\
& \Rightarrow \frac{d y}{d x}=y\left[\cos x \cdot \frac{1}{\log x} \cdot \frac{1}{x}+\log \log x \cdot(-\sin x)\right] \\
& \Rightarrow \frac{d y}{d x}=(\log x)^{\cos x}\left[\frac{\cos x-\sin x \log \log x}{x \log x}\right]
\end{aligned}
$$
:::

:::answer
**उत्तर:** $(\log x)^{\cos x}\left[\frac{\cos x-\sin x \log \log x}{x \log x}\right]$
:::

:::

:::question{number="4" kind="exercise" id="q_5.5.4" topic="Logarithmic differentiation of x^x - 2^sin x"}
#### प्रश्न 4

:::prompt
$1$ से $11$ तक के प्रश्नों में प्रदत्त फलनों का $x$ के सापेक्ष अवकलन कीजिए: $x^{x}-2^{\sin x}$
:::

:::solution{label="हल"}
माना $u=x^{x}$ तथा $v=2^{\sin x}$ इसलिए, $y=u-v$
दोनों ओर $x$ के सापेक्ष अवकलन करने पर

$$
\frac{d y}{d x}=\frac{d u}{d x}-\frac{d v}{d x}
$$

यहाँ, $u=x^{x}$, दोनों ओर $\log$ लेने पर
$\log u=x \log x$, इसलिए,

$$
\begin{aligned}
& \frac{1}{u} \frac{d u}{d x}=x \cdot \frac{d}{d x} \log x+\log x \cdot \frac{d}{d x} x=x \cdot \frac{1}{x}+\log x \cdot 1=1+\log x \\
& \frac{d u}{d x}=u[1+\log x]=x^{x}[1+\log x]
\end{aligned}
$$

तथा, $v=2^{\sin x}$, दोनों ओर $\log$ लेने पर
$\log v=\sin x \log 2$, इसलिए,

$$
\begin{aligned}
& \frac{1}{v} \frac{d v}{d x}=\log 2 \cdot \frac{d}{d x} \sin x=\log 2 \cdot \cos x \\
& \frac{d v}{d x}=v[\cos x \log 2]=2^{\sin x}[\cos x \log 2]
\end{aligned}
$$

समीकरण (2) से $\frac{d u}{d x}$ का तथा समीकरण (3) से $\frac{d v}{d x}$ का मान समीकरण (1) में रखने पर

$$
\frac{d y}{d x}=x^{x}[1+\log x]-2^{\sin x}[\cos x \log 2]
$$
:::

:::answer
**उत्तर:** $\frac{d y}{d x}=x^{x}[1+\log x]-2^{\sin x}[\cos x \log 2]$
:::

:::

:::question{number="5" kind="exercise" id="q_5.5.5" topic="Logarithmic differentiation of a triple product of binomials"}
#### प्रश्न 5

:::prompt
$1$ से $11$ तक के प्रश्नों में प्रदत्त फलनों का $x$ के सापेक्ष अवकलन कीजिए: $(x+3)^{2} \cdot(x+4)^{3} \cdot(x+5)^{4}$
:::

:::solution{label="हल"}
माना $y=(x+3)^{2} \cdot(x+4)^{3} \cdot(x+5)^{4}$, दोनों ओर $\log$ लेने पर

$$
\log y=2 \log (x+3)+3 \log (x+4)+4 \log (x+5)
$$

इसलिए,

$$
\begin{aligned}
& \frac{1}{y} \frac{d y}{d x}=2 \cdot \frac{1}{(x+3)}+3 \cdot \frac{1}{(x+4)}+4 \cdot \frac{1}{(x+5)} \\
& \Rightarrow \frac{d y}{d x}=y\left[\frac{2(x+4)(x+5)+3(x+3)(x+5)+4(x+3)(x+4)}{(x+3)(x+4)(x+5)}\right] \\
& \Rightarrow \frac{d y}{d x}=y\left[\frac{2\left(x^{2}+9 x+20\right)+3\left(x^{2}+8 x+15\right)+4\left(x^{2}+7 x+12\right)}{(x+3)(x+4)(x+5)}\right] \\
& \Rightarrow \frac{d y}{d x}=(x+3)^{2} \cdot(x+4)^{3} \cdot(x+5)^{4}\left[\frac{9 x^{2}+70 x+133}{(x+3)(x+4)(x+5)}\right] \\
& \Rightarrow \frac{d y}{d x}=(x+3) \cdot(x+4)^{2} \cdot(x+5)^{3}\left(9 x^{2}+70 x+133\right)
\end{aligned}
$$
:::

:::answer
**उत्तर:** $\frac{d y}{d x}=(x+3) \cdot(x+4)^{2} \cdot(x+5)^{3}\left(9 x^{2}+70 x+133\right)$
:::

:::

:::question{number="6" kind="exercise" id="q_5.5.6" topic="Logarithmic differentiation of a sum of variable exponents"}
#### प्रश्न 6

:::prompt
$1$ से $11$ तक के प्रश्नों में प्रदत्त फलनों का $x$ के सापेक्ष अवकलन कीजिए: $\left(x+\frac{1}{x}\right)^{x}+x^{\left(1+\frac{1}{x}\right)}$
:::

:::solution{label="हल"}
माना $u=\left(x+\frac{1}{x}\right)^{x}$ तथा $v=x^{\left(1+\frac{1}{x}\right)}$ इसलिए, $y=u+v$
दोनों ओर $x$ के सापेक्ष अवकलन करने पर

$$
\frac{d y}{d x}=\frac{d u}{d x}+\frac{d v}{d x}
$$

यहाँ, $u=\left(x+\frac{1}{x}\right)^{x}$, दोनों ओर $\log$ लेने पर
$\log u=x \log \left(x+\frac{1}{x}\right)$, इसलिए,

$$
\begin{aligned}
& \frac{1}{u} \frac{d u}{d x}=x \cdot \frac{d}{d x} \log \left(x+\frac{1}{x}\right)+\log \left(x+\frac{1}{x}\right) \cdot \frac{d}{d x} x \\
& =x \cdot \frac{1}{\left(x+\frac{1}{x}\right)} \cdot\left(1-\frac{1}{x^{2}}\right)+\log \left(x+\frac{1}{x}\right) \cdot 1=\frac{x^{2}}{x^{2}+1} \cdot \frac{x^{2}-1}{x^{2}}+\log \left(x+\frac{1}{x}\right) \\
& \frac{d u}{d x}=\left(x+\frac{1}{x}\right)^{x}\left[\frac{x^{2}-1}{x^{2}+1}+\log \left(x+\frac{1}{x}\right)\right]
\end{aligned}
$$

तथा, $v=x^{\left(1+\frac{1}{x}\right)}$, दोनों ओर $\log$ लेने पर
$\log v=\left(1+\frac{1}{x}\right) \log x$, इसलिए,

$$
\begin{aligned}
& \frac{1}{v} \frac{d v}{d x}=\left(1+\frac{1}{x}\right) \cdot \frac{d}{d x} \log x+\log x \cdot \frac{d}{d x}\left(1+\frac{1}{x}\right)=\left(1+\frac{1}{x}\right) \cdot \frac{1}{x}+\log x \cdot\left(-\frac{1}{x^{2}}\right) \\
& \frac{d v}{d x}=v\left[\left(\frac{x^{2}+1}{x}\right) \cdot \frac{1}{x}-\frac{\log x}{x^{2}}\right]=x^{\left(1+\frac{1}{x}\right)}\left[\frac{x^{2}+1-\log x}{x^{2}}\right] \ldots \text { (3) }
\end{aligned}
$$

समीकरण (2) से $\frac{d u}{d x}$ का तथा समीकरण (3) से $\frac{d v}{d x}$ का मान समीकरण (1) में रखने पर

$$
\frac{d y}{d x}=\left(x+\frac{1}{x}\right)^{x}\left[\frac{x^{2}-1}{x^{2}+1}+\log \left(x+\frac{1}{x}\right)\right]+x^{\left(1+\frac{1}{x}\right)}\left[\frac{x^{2}+1-\log x}{x^{2}}\right]
$$
:::

:::answer
**उत्तर:** $\frac{d y}{d x}=\left(x+\frac{1}{x}\right)^{x}\left[\frac{x^{2}-1}{x^{2}+1}+\log \left(x+\frac{1}{x}\right)\right]+x^{\left(1+\frac{1}{x}\right)}\left[\frac{x^{2}+1-\log x}{x^{2}}\right]$
:::

:::

:::question{number="7" kind="exercise" id="q_5.5.7" topic="Logarithmic differentiation of a sum of variable exponents"}
#### प्रश्न 7

:::prompt
$1$ से $11$ तक के प्रश्नों में प्रदत्त फलनों का $x$ के सापेक्ष अवकलन कीजिए: $(\log x)^{x}+x^{\log x}$
:::

:::solution{label="हल"}
माना $u=(\log x)^{x}$ तथा $v=x^{\log x}$ इसलिए, $y=u+v$
दोनों ओर $x$ के सापेक्ष अवकलन करने पर

$$
\frac{d y}{d x}=\frac{d u}{d x}+\frac{d v}{d x}
$$

यहाँ, $u=(\log x)^{x}$, दोनों ओर $\log$ लेने पर
$\log u=x \log \log x$, इसलिए,

$$
\frac{1}{u} \frac{d u}{d x}=x \cdot \frac{d}{d x} \log \log x+\log \log x \cdot \frac{d}{d x} x
$$

$$
\begin{aligned}
& =x \cdot \frac{1}{\log x} \cdot \frac{1}{x}+\log \log x \cdot 1=\frac{1}{\log x}+\log \log x \\
& \frac{d u}{d x}=(\log x)^{x}\left[\frac{1+\log x \cdot \log \log x}{\log x}\right] \\
& =(\log x)^{x-1}(1+\log x \cdot \log \log x)
\end{aligned}
$$

तथा, $v=x^{\log x}$, दोनों ओर $\log$ लेने पर
$\log v=\log x \log x$, इसलिए,

$$
\begin{aligned}
& \frac{1}{v} \frac{d v}{d x}=\log x \cdot \frac{d}{d x} \log x+\log x \cdot \frac{d}{d x} \log x \\
& =\log x \cdot \frac{1}{x}+\log x \cdot \frac{1}{x} \\
& \frac{d v}{d x}=v\left[\frac{2 \log x}{x}\right]=x^{\log x}\left[\frac{2 \log x}{x}\right]=x^{\log x-1}(2 \log x)
\end{aligned}
$$

समीकरण (2) से $\frac{d u}{d x}$ का तथा समीकरण (3) से $\frac{d v}{d x}$ का मान समीकरण (1) में रखने पर

$$
\frac{d y}{d x}=(\log x)^{x-1}(1+\log x \cdot \log \log x)+x^{\log x-1}(2 \log x)
$$
:::

:::answer
**उत्तर:** $\frac{d y}{d x}=(\log x)^{x-1}(1+\log x \cdot \log \log x)+x^{\log x-1}(2 \log x)$
:::

:::

:::question{number="8" kind="exercise" id="q_5.5.8" topic="Logarithmic differentiation of a sum of variable exponents"}
#### प्रश्न 8

:::prompt
$1$ से $11$ तक के प्रश्नों में प्रदत्त फलनों का $x$ के सापेक्ष अवकलन कीजिए: $(\sin x)^{x}+\sin ^{-1} \sqrt{x}$
:::

:::solution{label="हल"}
माना $u=(\sin x)^{x}$ तथा $v=\sin ^{-1} \sqrt{x}$ इसलिए, $y=u+v$
दोनों ओर $x$ के सापेक्ष अवकलन करने पर

$$
\frac{d y}{d x}=\frac{d u}{d x}+\frac{d v}{d x}
$$

यहाँ, $u=(\sin x)^{x}$, दोनों ओर $\log$ लेने पर
$\log u=x \log \sin x$, इसलिए,

$$
\begin{aligned}
& \frac{1}{u} \frac{d u}{d x}=x \cdot \frac{d}{d x} \log \sin x+\log \sin x \cdot \frac{d}{d x} x \\
& =x \cdot \frac{1}{\sin x} \cdot \cos x+\log \sin x \cdot 1=x \cot x+\log \sin x \\
& \frac{d u}{d x}=(\sin x)^{x}(x \cot x+\log \sin x)
\end{aligned}
$$

तथा , $v=\sin ^{-1} \sqrt{x}$, इसलिए,

$$
\begin{aligned}
& \frac{1}{v} \frac{d v}{d x}=\log x \cdot \frac{d}{d x} \log x+\log x \cdot \frac{d}{d x} \log x=\log x \cdot \frac{1}{x}+\log x \cdot \frac{1}{x} \\
& \frac{d v}{d x}=\frac{1}{\sqrt{1-x}} \cdot \frac{d}{d x} \sqrt{x}=\frac{1}{\sqrt{1-x}} \cdot \frac{1}{2 \sqrt{x}}=\frac{1}{2 \sqrt{x-x^{2}}}
\end{aligned}
$$

समीकरण (2) से $\frac{d u}{d x}$ का तथा समीकरण (3) से $\frac{d v}{d x}$ का मान समीकरण (1) में रखने पर

$$
\frac{d y}{d x}=(\sin x)^{x}(x \cot x+\log \sin x)+\frac{1}{2 \sqrt{x-x^{2}}}
$$
:::

:::answer
**उत्तर:** $\frac{d y}{d x}=(\sin x)^{x}(x \cot x+\log \sin x)+\frac{1}{2 \sqrt{x-x^{2}}}$
:::

:::

:::question{number="9" kind="exercise" id="q_5.5.9" topic="Logarithmic differentiation of a sum of variable exponents"}
#### प्रश्न 9

:::prompt
$1$ से $11$ तक के प्रश्नों में प्रदत्त फलनों का $x$ के सापेक्ष अवकलन कीजिए: $x^{\sin x}+(\sin x)^{\cos x}$
:::

:::solution{label="हल"}
माना $u=x^{\sin x}$ तथा $v=(\sin x)^{\cos x}$ इसलिए, $y=u+v$
दोनों ओर $x$ के सापेक्ष अवकलन करने पर

$$
\frac{d y}{d x}=\frac{d u}{d x}+\frac{d v}{d x}
$$

यहाँ, $u=x^{\sin x}$, दोनों ओर $\log$ लेने पर
$\log u=\sin x \log x$, इसलिए,

$$
\begin{aligned}
& \frac{1}{u} \frac{d u}{d x}=\sin x \cdot \frac{d}{d x} \log x+\log x \cdot \frac{d}{d x} \sin x=\sin x \cdot \frac{1}{x}+\log x \cdot \cos x=\frac{\sin x}{x}+\log x \cos x \\
& \frac{d u}{d x}=x^{\sin x}\left[\frac{\sin x}{x}+\log x \cos x\right]=x^{\sin x-1}(\sin x+x \log x \cos x)
\end{aligned}
$$

तथा, $v=(\sin x)^{\cos x}$, दोनों ओर $\log$ लेने पर
$\log v=\cos x \log \sin x$, इसलिए,

$$
\begin{aligned}
& \frac{1}{v} \frac{d v}{d x}=\cos x \cdot \frac{d}{d x} \log \sin x+\log \sin x \cdot \frac{d}{d x} \cos x=\cos x \cdot \frac{1}{\sin x} \cos x+\log \sin x(-\sin x) \\
& \frac{d v}{d x}=v[\cos x \cot x-\sin x \log \sin x]=(\sin x)^{\cos x}(\cos x \cot x-\sin x \log \sin x)
\end{aligned}
$$

समीकरण (2) से $\frac{d u}{d x}$ का तथा समीकरण (3) से $\frac{d v}{d x}$ का मान समीकरण (1) में रखने पर

$$
\frac{d y}{d x}=x^{\sin x-1}(\sin x+x \log x \cos x)+(\sin x)^{\cos x}(\cos x \cot x-\sin x \log \sin x)
$$
:::

:::answer
**उत्तर:** $\frac{d y}{d x}=x^{\sin x-1}(\sin x+x \log x \cos x)+(\sin x)^{\cos x}(\cos x \cot x-\sin x \log \sin x)$
:::

:::

:::question{number="10" kind="exercise" id="q_5.5.10" topic="Logarithmic differentiation of a sum with a rational function"}
#### प्रश्न 10

:::prompt
$1$ से $11$ तक के प्रश्नों में प्रदत्त फलनों का $x$ के सापेक्ष अवकलन कीजिए: $x^{x \cos x}+\frac{x^{2}+1}{x^{2}-1}$
:::

:::solution{label="हल"}
माना $u=x^{x \cos x}$ तथा $v=\frac{x^{2}+1}{x^{2}-1}$ इसलिए, $y=u+v$
दोनों ओर $x$ के सापेक्ष अवकलन करने पर

$$
\frac{d y}{d x}=\frac{d u}{d x}+\frac{d v}{d x}
$$

यहाँ, $u=x^{x \cos x}$, दोनों ओर $\log$ लेने पर
$\log u=x \log x$, इसलिए,

$$
\begin{aligned}
& \frac{1}{u} \frac{d u}{d x}=x \cos x \cdot \frac{d}{d x} \log x+\log x \cdot \frac{d}{d x} x \cos x=x \cos x \cdot \frac{1}{x}+\log x \cdot(-x \cdot \sin x+\cos x) \\
& =\cos x-x \sin x \log x+\cos x \log x \\
& \frac{d u}{d x}=u[\cos x-x \sin x \log x+\cos x \log x] \\
& =x^{x \cos x}[\cos x-x \sin x \log x+\cos x \log x]
\end{aligned}
$$

तथा, $v=\frac{x^{2}+1}{x^{2}-1}$, दोनों ओर $\log$ लेने पर
$\log v=\log \left(x^{2}+1\right)-\log \left(x^{2}-1\right)$, इसलिए,

$$
\begin{aligned}
& \frac{1}{v} \frac{d v}{d x}=\frac{1}{x^{2}+1} \cdot 2 x-\frac{1}{x^{2}-1} \cdot 2 x=\frac{2 x\left(x^{2}-1\right)-2 x\left(x^{2}+1\right)}{\left(x^{2}+1\right)\left(x^{2}-1\right)}=\frac{-4 x}{\left(x^{2}+1\right)\left(x^{2}-1\right)} \\
& \frac{d v}{d x}=v\left[\frac{-4 x}{\left(x^{2}+1\right)\left(x^{2}-1\right)}\right]=\frac{x^{2}+1}{x^{2}-1}\left[\frac{-4 x}{\left(x^{2}+1\right)\left(x^{2}-1\right)}\right]=-\frac{4 x}{\left(x^{2}-1\right)^{2}} \ldots(3)
\end{aligned}
$$

समीकरण (2) से $\frac{d u}{d x}$ का तथा समीकरण (3) से $\frac{d v}{d x}$ का मान समीकरण (1)में रखने पर

$$
\frac{d y}{d x}=x^{x \cos x}[\cos x-x \sin x \log x+\cos x \log x]-\frac{4 x}{\left(x^{2}-1\right)^{2}}
$$
:::

:::answer
**उत्तर:** $\frac{d y}{d x}=x^{x \cos x}[\cos x-x \sin x \log x+\cos x \log x]-\frac{4 x}{\left(x^{2}-1\right)^{2}}$
:::

:::

:::question{number="11" kind="exercise" id="q_5.5.11" topic="Logarithmic differentiation of a sum of variable exponents"}
#### प्रश्न 11

:::prompt
$1$ से $11$ तक के प्रश्नों में प्रदत्त फलनों का $x$ के सापेक्ष अवकलन कीजिए: $(x \cos x)^{x}+(x \sin x)^{\frac{1}{x}}$
:::

:::solution{label="हल"}
माना $u=(x \cos x)^{x}$ तथा $v=(x \sin x)^{\frac{1}{x}}$ इसलिए, $y=u+v$
दोनों ओर $x$ के सापेक्ष अवकलन करने पर

$$
\frac{d y}{d x}=\frac{d u}{d x}+\frac{d v}{d x}
$$

यहाँ, $u=(x \cos x)^{x}$, दोनों ओर $\log$ लेने पर
$\log u=x \log (x \cos x)$, इसलिए,

$$
\begin{aligned}
& \frac{1}{u} \frac{d u}{d x}=x \cdot \frac{d}{d x} \log (x \cos x)+\log (x \cos x) \cdot \frac{d}{d x} x \\
& =x \cdot \frac{1}{(x \cos x)}(-x \sin x+\cos x)+\log (x \cos x) \cdot 1=-x \tan x+1+\log (x \cos x) \\
& \frac{d u}{d x}=(x \cos x)^{x}[1-x \tan x+\log (x \cos x)] \\
& =(x \cos x)^{x}[1-x \tan x+\log (x \cos x)] \ldots \text { (2) }
\end{aligned}
$$

तथा, $v=(x \sin x)^{\frac{1}{x}}$, दोनों ओर $\log$ लेने पर
$\log v=\frac{1}{x} \log (x \sin x)$, इसलिए,

$$
\begin{aligned}
& \frac{1}{v} \frac{d v}{d x}=\frac{1}{x} \cdot \frac{d}{d x} \log (x \sin x)+\log (x \sin x) \cdot \frac{d}{d x} \frac{1}{x} \\
& =\frac{1}{x} \cdot \frac{1}{x \sin x}(x \cos x+\sin x)+\log (x \sin x)\left(-\frac{1}{x^{2}}\right) \\
& \frac{d v}{d x}=v\left[\frac{x \cot x+1-\log (x \sin x)}{x^{2}}\right]=(x \sin x)^{\frac{1}{x}}\left[\frac{x \cot x+1-\log (x \sin x)}{x^{2}}\right]
\end{aligned}
$$

समीकरण (2) से $\frac{d u}{d x}$ का तथा समीकरण (3) से $\frac{d v}{d x}$ का मान समीकरण (1) में रखने पर

$$
\frac{d y}{d x}=(x \cos x)^{x}[1-x \tan x+\log (x \cos x)]+(x \sin x)^{\frac{1}{x}}\left[\frac{x \cot x+1-\log (x \sin x)}{x^{2}}\right]
$$
:::

:::answer
**उत्तर:** $\frac{d y}{d x}=(x \cos x)^{x}[1-x \tan x+\log (x \cos x)]+(x \sin x)^{\frac{1}{x}}\left[\frac{x \cot x+1-\log (x \sin x)}{x^{2}}\right]$
:::

:::

:::question{number="12" kind="exercise" id="q_5.5.12" topic="Derivative of y for an implicit x^y + y^x = 1"}
#### प्रश्न 12

:::prompt
$12$ से $15$ तक के प्रश्नों में प्रदत्त फलनों के लिए $\frac{d y}{d x}$ ज्ञात कीजिए: $x^{y}+y^{x}=1$
:::

:::solution{label="हल"}
माना $u=x^{y}$ तथा $v=y^{x}$ इसलिए, $u+v=1$
दोनों ओर $x$ के सापेक्ष अवकलन करने पर

$$
\frac{d u}{d x}+\frac{d v}{d x}=0
$$

यहाँ, $u=x^{y}$, दोनों ओर $\log$ लेने पर, $\log u=y \log x$, इसलिए,

$$
\begin{aligned}
& \frac{1}{u} \frac{d u}{d x}=y \cdot \frac{d}{d x} \log x+\log x \cdot \frac{d}{d x} y=y \cdot \frac{1}{x}+\log x \cdot \frac{d y}{d x} \\
& \frac{d u}{d x}=x^{y}\left[\frac{y}{x}+\log x \cdot \frac{d y}{d x}\right]
\end{aligned}
$$

तथा, $v=y^{x}$, दोनों ओर $\log$ लेने पर
$\log v=x \log y$, इसलिए,

$$
\begin{aligned}
& \frac{1}{v} \frac{d v}{d x}=x \cdot \frac{d}{d x} \log y+\log y \cdot \frac{d}{d x} x=x \cdot \frac{1}{y} \frac{d y}{d x}+\log y \cdot 1 \\
& \frac{d v}{d x}=v\left[\frac{x}{y} \frac{d y}{d x}+\log y\right]=y^{x}\left[\frac{x}{y} \frac{d y}{d x}+\log y\right]
\end{aligned}
$$

समीकरण (2) से $\frac{d u}{d x}$ का तथा समीकरण (3) से $\frac{d v}{d x}$ का मान समीकरण (1) में रखने पर

$$
\begin{aligned}
& x^{y}\left[\frac{y}{x}+\log x \cdot \frac{d y}{d x}\right]+y^{x}\left[\frac{x}{y} \frac{d y}{d x}+\log y\right]=0 \\
& \Rightarrow y x^{y-1}+x^{y} \log x \frac{d y}{d x}+x y^{x-1} \frac{d y}{d x}+y^{x} \log y=0 \\
& \Rightarrow \frac{d y}{d x}\left(x^{y} \log x+x y^{x-1}\right)=-\left(y^{x} \log y+y x^{y-1}\right) \\
& \Rightarrow \frac{d y}{d x}=-\frac{y^{x} \log y+y x^{y-1}}{x^{y} \log x+x y^{x-1}}
\end{aligned}
$$
:::

:::answer
**उत्तर:** $\frac{d y}{d x}=-\frac{y^{x} \log y+y x^{y-1}}{x^{y} \log x+x y^{x-1}}$
:::

:::

:::question{number="13" kind="exercise" id="q_5.5.13" topic="Derivative of y for an implicit y^x = x^y"}
#### प्रश्न 13

:::prompt
$12$ से $15$ तक के प्रश्नों में प्रदत्त फलनों के लिए $\frac{d y}{d x}$ ज्ञात कीजिए: $y^{x}=x^{y}$
:::

:::solution{label="हल"}
$$
y^{x}=x^{y}
$$

दोनों ओर $\log$ लेने पर, $x \log y=y \log x$, इसलिए,

$$
\begin{aligned}
& x \cdot \frac{d}{d x} \log y+\log y \cdot \frac{d}{d x} x=y \cdot \frac{d}{d x} \log x+\log x \cdot \frac{d}{d x} y \\
& \Rightarrow x \cdot \frac{1}{y} \frac{d y}{d x}+\log y \cdot 1=y \cdot \frac{1}{x}+\log x \cdot \frac{d y}{d x} \\
& \Rightarrow \frac{d y}{d x}\left(\frac{x}{y}-\log x\right)=\frac{y}{x}-\log y \quad \Rightarrow \frac{d y}{d x}\left(\frac{x-y \log x}{y}\right)=\frac{y-x \log y}{x} \\
& \Rightarrow \frac{d y}{d x}=\frac{y(y-x \log y)}{x(x-y \log x)}
\end{aligned}
$$
:::

:::answer
**उत्तर:** $\frac{d y}{d x}=\frac{y(y-x \log y)}{x(x-y \log x)}$
:::

:::

:::question{number="14" kind="exercise" id="q_5.5.14" topic="Derivative of y for an implicit (cos x)^y = (cos y)^x"}
#### प्रश्न 14

:::prompt
$12$ से $15$ तक के प्रश्नों में प्रदत्त फलनों के लिए $\frac{d y}{d x}$ ज्ञात कीजिए: $(\cos x)^{y}=(\cos y)^{x}$
:::

:::solution{label="हल"}
$$
(\cos x)^{y}=(\cos y)^{x}
$$

दोनों ओर $\log$ लेने पर, $y \cos x=x \cos y$, इसलिए,

$$
\begin{aligned}
& y \cdot \frac{d}{d x} \cos x+\cos x \cdot \frac{d}{d x} y=x \cdot \frac{d}{d x} \cos y+\cos y \cdot \frac{d}{d x} x \\
& \Rightarrow y(-\sin x)+\cos x \cdot \frac{d y}{d x}=x \cdot(-\sin y) \frac{d y}{d x}+\cos y \cdot 1 \\
& \Rightarrow \frac{d y}{d x}(\cos x+x \sin y)=\cos y+y \sin x \\
& \Rightarrow \frac{d y}{d x}=\frac{\cos y+y \sin x}{\cos x+x \sin y}
\end{aligned}
$$
:::

:::answer
**उत्तर:** $\frac{d y}{d x}=\frac{\cos y+y \sin x}{\cos x+x \sin y}$
:::

:::

:::question{number="15" kind="exercise" id="q_5.5.15" topic="Derivative of y for an implicit xy = e^(x-y)"}
#### प्रश्न 15

:::prompt
$12$ से $15$ तक के प्रश्नों में प्रदत्त फलनों के लिए $\frac{d y}{d x}$ ज्ञात कीजिए: $x y=e^{(x-y)}$
:::

:::solution{label="हल"}
$$
x y=e^{(x-y)}
$$

दोनों ओर $\log$ लेने पर, $\log x+\log y=(x-y) \log e \quad \Rightarrow \log x+\log y=(x-y)$, इसलिए, $\frac{1}{x}+\frac{1}{y} \cdot \frac{d y}{d x}=1-\frac{d y}{d x}$

$$
\begin{aligned}
& \Rightarrow \frac{d y}{d x}\left(\frac{1}{y}+1\right)=1-\frac{1}{x} \quad \Rightarrow \frac{d y}{d x}\left(\frac{1+y}{y}\right)=\frac{x-1}{x} \\
& \Rightarrow \frac{d y}{d x}=\frac{y(x-1)}{x(y+1)}
\end{aligned}
$$
:::

:::answer
**उत्तर:** $\frac{d y}{d x}=\frac{y(x-1)}{x(y+1)}$
:::

:::

:::question{number="16" kind="exercise" id="q_5.5.16" topic="Derivative of a product of four binomials, evaluated at a point"}
#### प्रश्न 16

:::prompt
$f(x)=(1+x)\left(1+x^{2}\right)\left(1+x^{4}\right)\left(1+x^{8}\right)$ द्वारा प्रदत्त फलन का अवकलज ज्ञात कीजिए और इस प्रकार $f^{\prime}(1)$ ज्ञात कीजिए।
:::

:::solution{label="हल"}
$f(x)=(1+x)\left(1+x^{2}\right)\left(1+x^{4}\right)\left(1+x^{8}\right)$
दोनों ओर $\log$ लेने पर,
$\log f(x)=\log (1+x)+\log \left(1+x^{2}\right)+\log \left(1+x^{4}\right)+\log \left(1+x^{8}\right)$, इसलिए,

$$
\begin{aligned}
& \frac{1}{f(x)} \cdot \frac{d}{d x} f(x)=\frac{1}{1+x}+\frac{1}{1+x^{2}} \cdot \frac{d}{d x} x^{2}+\frac{1}{1+x^{4}} \cdot \frac{d}{d x} x^{4}+\frac{1}{1+x^{8}} \cdot \frac{d}{d x} x^{8} \\
& \Rightarrow \frac{1}{f(x)} \cdot f^{\prime}(x)=\frac{1}{1+x}+\frac{1}{1+x^{2}} \cdot 2 x+\frac{1}{1+x^{4}} \cdot 4 x^{3}+\frac{1}{1+x^{8}} \cdot 8 x^{7} \\
& \Rightarrow f^{\prime}(x)=f(x)\left[\frac{1}{1+x}+\frac{2 x}{1+x^{2}}+\frac{4 x^{3}}{1+x^{4}}+\frac{8 x^{7}}{1+x^{8}}\right] \\
& \Rightarrow f^{\prime}(x)=(1+x)\left(1+x^{2}\right)\left(1+x^{4}\right)\left(1+x^{8}\right)\left[\frac{1}{1+x}+\frac{2 x}{1+x^{2}}+\frac{4 x^{3}}{1+x^{4}}+\frac{8 x^{7}}{1+x^{8}}\right]
\end{aligned}
$$
:::

:::answer
**उत्तर:** $f^{\prime}(x)=(1+x)\left(1+x^{2}\right)\left(1+x^{4}\right)\left(1+x^{8}\right)\left[\frac{1}{1+x}+\frac{2 x}{1+x^{2}}+\frac{4 x^{3}}{1+x^{4}}+\frac{8 x^{7}}{1+x^{8}}\right]$
:::

:::

:::question{number="17" kind="exercise" id="q_5.5.17" topic="Differentiating a product three ways and verifying equal results"}
#### प्रश्न 17

:::prompt
$\left(x^{2}-5 x+8\right)\left(x^{3}+7 x+9\right)$ का अवकलन निम्नलिखित तीन प्रकार से कीजिए:
:::

:::part{label="(i)"}
:::prompt
गुणनफल नियम का प्रयोग करके
:::

:::solution
गुणनफल नियम का प्रयोग करके अवकलन
$$
\begin{aligned}
\frac{d y}{d x} & =\left(x^{2}-5 x+8\right) \frac{\mathrm{d}}{\mathrm{dx}}\left(x^{3}+7 x+9\right)+\left(x^{3}+7 x+9\right) \frac{\mathrm{d}}{\mathrm{dx}}\left(x^{2}-5 x+8\right) \\
& =\left(x^{2}-5 x+8\right)\left(3 x^{2}+7\right)+\left(x^{3}+7 x+9\right)(2 x-5) \\
& =\left(3 x^{4}+7 x^{2}-15 x^{3}-35 x+24 x^{2}+56\right)+2 x^{4}-5 x^{3}+14 x^{2}-35 x+18 x-45 \\
& =5 x^{4}-20 x^{3}+45 x^{2}-52 x+11
\end{aligned}
$$
:::

:::answer
**उत्तर:** $5 x^{4}-20 x^{3}+45 x^{2}-52 x+11$
:::

:::

:::part{label="(ii)"}
:::prompt
गुणनफल के विस्तारण द्वारा एक एकल बहुपद प्राप्त करके
:::

:::solution
गुणनफल के विस्तारण द्वारा एक एकल बहुपद प्राप्त करके अवकलन
$$
\begin{aligned}
y & =\left(x^{2}-5 x+8\right)\left(x^{3}+7 x+9\right) \\
& =x^{5}+7 x^{3}+9 x^{2}-5 x^{4}-35 x^{2}-45 x+8 x^{3}+56 x+72 \\
& =x^{5}-5 x^{4}+15 x^{3}-26 x^{2}+11 x+72 \\
\frac{d y}{d x} & =\frac{d}{d x} x^{5}-5 \frac{d}{d x} x^{4}+15 \frac{d}{d x} x^{3}-26 \frac{d}{d x} x^{2}+11 \frac{d}{d x} x+\frac{d}{d x} 72 \\
& =5 x^{4}-20 x^{3}+45 x^{2}-52 x+11
\end{aligned}
$$
:::

:::answer
**उत्तर:** $5 x^{4}-20 x^{3}+45 x^{2}-52 x+11$
:::

:::

:::part{label="(iii)"}
:::prompt
लघुगणकीय अवकलन द्वारा
यह भी सत्यापित कीजिए कि इस प्रकार प्राप्त तीनों उत्तर समान हैं।
:::

:::solution
लघुगणकीय अवकलन
$y=\left(x^{2}-5 x+8\right)\left(x^{3}+7 x+9\right)$
दोनों ओर $\log$ लेने पर, $\log y=\log \left(x^{2}-5 x+8\right)+\log \left(x^{3}+7 x+9\right)$
$$
\begin{aligned}
& \frac{1}{y} \cdot \frac{d y}{d x}=\frac{1}{\left(x^{2}-5 x+8\right)} \cdot \frac{d}{d x}\left(x^{2}-5 x+8\right)+\frac{1}{\left(x^{3}+7 x+9\right)} \cdot \frac{d}{d x}\left(x^{3}+7 x+9\right) \\
& \frac{1}{y} \cdot \frac{d y}{d x}=\frac{1}{x^{2}-5 x+8} \cdot(2 x-5)+\frac{1}{x^{3}+7 x+9} \cdot\left(3 x^{2}+7\right) \\
& \frac{d y}{d x}=y\left[\frac{(2 x-5)\left(x^{3}+7 x+9\right)+\left(3 x^{2}+7\right)\left(x^{2}-5 x+8\right)}{\left(x^{2}-5 x+8\right)\left(x^{3}+7 x+9\right)}\right] \\
& =y\left[\frac{2 x^{4}+14 x^{2}+18 x-5 x^{3}-35 x-45+3 x^{4}-15 x^{3}+24 x^{2}+7 x^{2}-35 x+56}{\left(x^{2}-5 x+8\right)\left(x^{3}+7 x+9\right)}\right] \\
& \Rightarrow \frac{d y}{d x}=\left(x^{2}-5 x+8\right)\left(x^{3}+7 x+9\right)\left[\frac{5 x^{5}-20 x^{3}+45 x^{2}-52 x+11}{\left(x^{2}-5 x+8\right)\left(x^{3}+7 x+9\right)}\right] \\
& \Rightarrow \frac{d y}{d x}=5 x^{4}-20 x^{3}+45 x^{2}-52 x+11
\end{aligned}
$$

अतः, इस प्रकार प्राप्त तीनों उत्तर समान हैं।
:::

:::answer
**उत्तर:** $5 x^{4}-20 x^{3}+45 x^{2}-52 x+11$ (तीनों विधियों से समान)
:::

:::

:::solution{label="हल"}
माना $y=\left(x^{2}-5 x+8\right)\left(x^{3}+7 x+9\right.$
:::

:::

:::question{number="18" kind="exercise" id="q_5.5.18" topic="Proving the triple product rule two ways"}
#### प्रश्न 18

:::prompt
यदि $u, v$ तथा $w, x$ के फलन हैं, तो दो विधियों अर्थात् प्रथम-गुणनफल नियम की पुनरावृत्ति द्वारा, द्वितीय - लघुगणकीय अवकलन द्वारा दर्शाइए कि

$$
\frac{d}{d x}(u \cdot v \cdot w)=\frac{d u}{d x} v \cdot w+u \cdot \frac{d v}{d x} \cdot w+u \cdot v \frac{d w}{d x}
$$
:::

:::solution{label="हल"}
माना $y=u . v . w=u .(v . w)$
गुणनफल नियम की पुनरावृत्ति द्वारा अवकलन

$$
\begin{aligned}
& \frac{d y}{d x}=u \cdot \frac{d}{d x}(v \cdot w)+(v \cdot w) \cdot \frac{d}{d x} u \\
& =u\left[v \frac{d}{d x} w+w \frac{d}{d x} v\right]+v \cdot w \cdot \frac{d u}{d x} \\
& \Rightarrow \frac{d y}{d x}=u \cdot v \cdot \frac{d w}{d x}+u \cdot w \cdot \frac{d v}{d x}+v \cdot w \cdot \frac{d u}{d x}
\end{aligned}
$$

लघुगणकीय अवकलन
माना $y=$ u.v.w
दोनों ओर $\log$ लेने पर, $\log y=\log u+\log v+\log w$

$$
\begin{aligned}
& \frac{1}{y} \cdot \frac{d y}{d x}=\frac{1}{u} \cdot \frac{d u}{d x}+\frac{1}{v} \cdot \frac{d v}{d x}+\frac{1}{w} \cdot \frac{d w}{d x} \\
& \Rightarrow \frac{d y}{d x}=y\left[\frac{1}{u} \cdot \frac{d u}{d x}+\frac{1}{v} \cdot \frac{d v}{d x}+\frac{1}{w} \cdot \frac{d w}{d x}\right] \\
& \Rightarrow \frac{d y}{d x}=u \cdot v \cdot w\left[\frac{1}{u} \cdot \frac{d u}{d x}+\frac{1}{v} \cdot \frac{d v}{d x}+\frac{1}{w} \cdot \frac{d w}{d x}\right] \\
& \Rightarrow \frac{d y}{d x}=\frac{u \cdot v \cdot w}{u} \cdot \frac{d u}{d x}+\frac{u \cdot v \cdot w}{v} \cdot \frac{d v}{d x}+\frac{u \cdot v \cdot w}{w} \cdot \frac{d w}{d x} \\
& \Rightarrow \frac{d y}{d x}=v \cdot w \cdot \frac{d u}{d x}+u \cdot w \cdot \frac{d v}{d x}+u \cdot v \cdot \frac{d w}{d x}
\end{aligned}
$$
:::

:::

:::question{number="1" kind="exercise" id="q_5.6.1" topic="Parametric derivative"}
#### प्रश्न 1

:::prompt
यदि प्रश्न संख्या $1$ से $10$ तक में $x$ तथा $y$ दिए समीकरणों द्वारा, एक दूसरे से प्राचलिक रूप में संबंधित हों, तो प्राचलों का विलोपन किए बिना, $\frac{d y}{d x}$ ज्ञात कीजिए: $x=2 a t^{2}, y=a t^{4}$
:::

:::solution{label="हल"}
यहाँ, $x=2 a t^{2}, y=a t^{4}$
इसलिए, $\frac{d x}{d t}=2 a(2 t)$ तथा $\frac{d y}{d t}=a\left(4 t^{3}\right)$

$$
\frac{d y}{d x}=\frac{\frac{d y}{d t}}{\frac{d x}{d t}}=\frac{4 a t^{3}}{4 a t}=t^{2}
$$
:::

:::answer
**उत्तर:** $t^{2}$
:::

:::

:::question{number="2" kind="exercise" id="q_5.6.2" topic="Parametric derivative"}
#### प्रश्न 2

:::prompt
यदि प्रश्न संख्या $1$ से $10$ तक में $x$ तथा $y$ दिए समीकरणों द्वारा, एक दूसरे से प्राचलिक रूप में संबंधित हों, तो प्राचलों का विलोपन किए बिना, $\frac{d y}{d x}$ ज्ञात कीजिए: $x=a \cos \theta, y=b \cos \theta$
:::

:::solution{label="हल"}
यहाँ, $x=a \cos \theta, y=b \cos \theta$
इसलिए, $\frac{d x}{d \theta}=a(-\sin \theta)$ तथा $\frac{d y}{d \theta}=b(-\sin \theta)$

$$
\frac{d y}{d x}=\frac{\frac{d y}{d \theta}}{\frac{d x}{d \theta}}=\frac{-b \sin \theta}{-a \sin \theta}=\frac{b}{a}
$$
:::

:::answer
**उत्तर:** $\frac{b}{a}$
:::

:::

:::question{number="3" kind="exercise" id="q_5.6.3" topic="Parametric derivative"}
#### प्रश्न 3

:::prompt
यदि प्रश्न संख्या $1$ से $10$ तक में $x$ तथा $y$ दिए समीकरणों द्वारा, एक दूसरे से प्राचलिक रूप में संबंधित हों, तो प्राचलों का विलोपन किए बिना, $\frac{d y}{d x}$ ज्ञात कीजिए: $x=\sin t, y=\cos 2 t$
:::

:::solution{label="हल"}
यहाँ, $x=\sin t, y=\cos 2 t$
इसलिए, $\frac{d x}{d t}=\cos t$ तथा $\frac{d y}{d t}=-\sin 2 t .2$

$$
\frac{d y}{d x}=\frac{\frac{d y}{d t}}{\frac{d x}{d t}}=\frac{-2 \sin 2 t}{\cot t}=-\frac{2(2 \sin t \cos t)}{\cos t}=-4 \sin t
$$
:::

:::answer
**उत्तर:** $-4 \sin t$
:::

:::

:::question{number="4" kind="exercise" id="q_5.6.4" topic="Parametric derivative"}
#### प्रश्न 4

:::prompt
यदि प्रश्न संख्या $1$ से $10$ तक में $x$ तथा $y$ दिए समीकरणों द्वारा, एक दूसरे से प्राचलिक रूप में संबंधित हों, तो प्राचलों का विलोपन किए बिना, $\frac{d y}{d x}$ ज्ञात कीजिए: $x=4 t, y=\frac{4}{t}$
:::

:::solution{label="हल"}
यहाँ, $x=4 t, y=\frac{4}{t}$
इसलिए, $\frac{d x}{d t}=4$ तथा $\frac{d y}{d t}=-\frac{4}{t^{2}}$

$$
\frac{d y}{d x}=\frac{\frac{d y}{d t}}{\frac{d x}{d t}}=\frac{-\frac{4}{t^{2}}}{4}=-\frac{1}{t^{2}}
$$
:::

:::answer
**उत्तर:** $-\frac{1}{t^{2}}$
:::

:::

:::question{number="5" kind="exercise" id="q_5.6.5" topic="Parametric derivative"}
#### प्रश्न 5

:::prompt
यदि प्रश्न संख्या $1$ से $10$ तक में $x$ तथा $y$ दिए समीकरणों द्वारा, एक दूसरे से प्राचलिक रूप में संबंधित हों, तो प्राचलों का विलोपन किए बिना, $\frac{d y}{d x}$ ज्ञात कीजिए: $x=\cos \theta-\cos 2 \theta, y=\sin \theta-\sin 2 \theta$
:::

:::solution{label="हल"}
यहाँ, $x=\cos \theta-\cos 2 \theta, y=\sin \theta-\sin 2 \theta$
इसलिए, $\frac{d x}{d \theta}=-\sin \theta+2 \sin 2 \theta$ तथा $\frac{d y}{d \theta}=\cos \theta-2 \cos 2 \theta$

$$
\frac{d y}{d x}=\frac{\frac{d y}{d \theta}}{\frac{d x}{d \theta}}=\frac{\cos \theta-2 \cos 2 \theta}{-\sin \theta+2 \sin 2 \theta}
$$
:::

:::answer
**उत्तर:** $\frac{\cos \theta-2 \cos 2 \theta}{-\sin \theta+2 \sin 2 \theta}$
:::

:::

:::question{number="6" kind="exercise" id="q_5.6.6" topic="Parametric derivative"}
#### प्रश्न 6

:::prompt
यदि प्रश्न संख्या $1$ से $10$ तक में $x$ तथा $y$ दिए समीकरणों द्वारा, एक दूसरे से प्राचलिक रूप में संबंधित हों, तो प्राचलों का विलोपन किए बिना, $\frac{d y}{d x}$ ज्ञात कीजिए: $x=a(\theta-\sin \theta), y=a(1+\cos \theta)$
:::

:::solution{label="हल"}
यहाँ, $x=a(\theta-\sin \theta), y=a(1+\cos \theta)$
इसलिए, $\frac{d x}{d \theta}=a(1-\cos \theta)$ तथा $\frac{d y}{d \theta}=a(0-\sin \theta)$

$$
\frac{d y}{d x}=\frac{\frac{d y}{d \theta}}{\frac{d x}{d \theta}}=\frac{-a \sin \theta)}{a(1-\cos \theta)}=-\frac{2 \sin \frac{\theta}{2} \cos \frac{\theta}{2}}{2 \sin ^{2} \frac{\theta}{2}}=-\cot \frac{\theta}{2}
$$
:::

:::answer
**उत्तर:** $-\cot \frac{\theta}{2}$
:::

:::

:::question{number="7" kind="exercise" id="q_5.6.7" topic="Parametric derivative"}
#### प्रश्न 7

:::prompt
यदि प्रश्न संख्या $1$ से $10$ तक में $x$ तथा $y$ दिए समीकरणों द्वारा, एक दूसरे से प्राचलिक रूप में संबंधित हों, तो प्राचलों का विलोपन किए बिना, $\frac{d y}{d x}$ ज्ञात कीजिए: $x=\frac{\sin ^{3} t}{\sqrt{\cos 2 t}}, y=\frac{\cos ^{3} t}{\sqrt{\cos 2 t}}$
:::

:::solution{label="हल"}
यहाँ, $x=\frac{\sin ^{3} t}{\sqrt{\cos 2 t}}, y=\frac{\cos ^{3} t}{\sqrt{\cos 2 t}}$
इसलिए, $\frac{d x}{d t}=\frac{\sin ^{3} t \frac{d}{d t} \sqrt{\cos 2 t}-\sqrt{\cos 2 t} \frac{d}{d t} \sin ^{3} t}{(\sqrt{\cos 2 t})^{2}}$

$$
=\frac{\sin ^{3} t \cdot \frac{1}{2 \sqrt{\cos 2 t}} \cdot(-\sin 2 t) \cdot 2-\sqrt{\cos 2 t} \cdot 3 \sin ^{2} t \cos t}{\cos 2 t}=\frac{-\sin ^{3} t \cdot \sin 2 t-3 \cos 2 t \cdot \sin ^{2} t \cos t}{\cos 2 t \sqrt{\cos 2 t}}
$$

तथा $\frac{d y}{d t}=\frac{\cos ^{3} t \frac{d}{d t} \sqrt{\cos 2 t}-\sqrt{\cos 2 t} \frac{d}{d t} \cos ^{3} t}{(\sqrt{\cos 2 t})^{2}}$

$$
=\frac{\cos ^{3} t \cdot \frac{1}{2 \sqrt{\cos 2 t}} \cdot(-\sin 2 t) \cdot 2-\sqrt{\cos 2 t} \cdot 3 \cos ^{2} t(-\sin t)}{\cos 2 t}=\frac{-\cos ^{3} t \cdot \sin 2 t+3 \cos 2 t \cdot \cos ^{2} t \sin t}{\cos 2 t \sqrt{\cos 2 t}}
$$

$$
\frac{d y}{d x}=\frac{\frac{d y}{d t}}{\frac{d x}{d t}}=\frac{-\cos ^{3} t \cdot \sin 2 t+3 \cos 2 t \cdot \cos ^{2} t \sin t}{-\sin ^{3} t \cdot \sin 2 t-3 \cos 2 t \cdot \sin ^{2} t \cos t}
$$

$$
=\frac{-\cos ^{3} t \cdot(2 \sin t \cos t)+3 \cos 2 t \cdot \cos ^{2} t \sin t}{-\sin ^{3} t \cdot(2 \sin t \cos t)-3 \cos 2 t \cdot \sin ^{2} t \cos t}=\frac{\cos ^{2} t \sin t\left(-2 \cos ^{2} t+3 \cos 2 t\right)}{\sin ^{2} t \cos t\left(-2 \sin ^{2} t-3 \cos 2 t\right)}
$$

$$
=\frac{\cos t\left[-2 \cos ^{2} t+3\left(2 \cos ^{2} t-1\right)\right]}{\sin t\left[-2 \sin ^{2} t-3\left(1-2 \sin ^{2} t\right)\right]}=\frac{\cos t\left[-2 \cos ^{2} t+6 \cos ^{2} t-3\right]}{\sin t\left[-2 \sin ^{2} t-3+6 \sin ^{2} t\right]}
$$

$$
=\frac{\cos t\left[4 \cos ^{2} t-3\right]}{\sin t\left[-3+4 \sin ^{2} t\right]}=-\frac{4 \cos ^{3} t-3 \cos t}{3 \sin t-4 \sin ^{3} t}=-\frac{\cos 3 t}{\sin 3 t}=-\cot 3 t
$$
:::

:::answer
**उत्तर:** $-\cot 3 t$
:::

:::

:::question{number="8" kind="exercise" id="q_5.6.8" topic="Parametric derivative"}
#### प्रश्न 8

:::prompt
यदि प्रश्न संख्या $1$ से $10$ तक में $x$ तथा $y$ दिए समीकरणों द्वारा, एक दूसरे से प्राचलिक रूप में संबंधित हों, तो प्राचलों का विलोपन किए बिना, $\frac{d y}{d x}$ ज्ञात कीजिए: $x=a\left(\cos t+\log \tan \frac{t}{2}\right) y=a \sin t$
:::

:::solution{label="हल"}
यहाँ, $x=a\left(\cos t+\log \tan \frac{t}{2}\right) y=a \sin t$
इसलिए, $\frac{d x}{d t}=a\left(-\sin t+\frac{1}{\tan ^{\frac{t}{2}}} \cdot \sec ^{2} \frac{t}{2} \cdot \frac{1}{2}\right)=a\left(-\sin t+\frac{\cos ^{\frac{t}{2}}}{\sin \frac{t}{2}} \cdot \frac{1}{\cos ^{2} \frac{t}{2}} \cdot \frac{1}{2}\right)$

$$
=a\left(-\sin t+\frac{1}{2 \sin \frac{t}{2} \cos \frac{t}{2}}\right)=a\left(-\sin t+\frac{1}{\sin t}\right)=a\left(\frac{-\sin ^{2} t+1}{\sin t}\right)=a\left(\frac{\cos ^{2} t}{\sin t}\right)
$$

तथा $\frac{d y}{d t}=a \cos t$

$$
\frac{d y}{d x}=\frac{\frac{d y}{d t}}{\frac{d x}{d t}}=\frac{a \cos t}{a\left(\frac{\cos ^{2} t}{\sin t}\right)}=\frac{\sin t}{\cos t}=\tan t
$$
:::

:::answer
**उत्तर:** $\tan t$
:::

:::

:::question{number="9" kind="exercise" id="q_5.6.9" topic="Parametric derivative"}
#### प्रश्न 9

:::prompt
यदि प्रश्न संख्या $1$ से $10$ तक में $x$ तथा $y$ दिए समीकरणों द्वारा, एक दूसरे से प्राचलिक रूप में संबंधित हों, तो प्राचलों का विलोपन किए बिना, $\frac{d y}{d x}$ ज्ञात कीजिए: $x=a \sec \theta, y=b \tan \theta$
:::

:::solution{label="हल"}
यहाँ, $x=a \sec \theta, y=b \tan \theta$
इसलिए, $\frac{d x}{d \theta}=a \sec \theta \tan \theta$
तथा $\frac{d y}{d \theta}=b \sec ^{2} \theta$

$$
\frac{d y}{d x}=\frac{\frac{d y}{d \theta}}{\frac{d x}{d \theta}}=\frac{b \sec ^{2} \theta}{a \sec \theta \tan \theta}=\frac{b \sec \theta}{a \tan \theta}=\frac{b\left(\frac{1}{\cos \theta}\right)}{a\left(\frac{\sin \theta}{\cos \theta}\right)}=\frac{b}{a} \operatorname{cosec} \theta
$$
:::

:::answer
**उत्तर:** $\frac{b}{a} \operatorname{cosec} \theta$
:::

:::

:::question{number="10" kind="exercise" id="q_5.6.10" topic="Parametric derivative"}
#### प्रश्न 10

:::prompt
यदि प्रश्न संख्या $1$ से $10$ तक में $x$ तथा $y$ दिए समीकरणों द्वारा, एक दूसरे से प्राचलिक रूप में संबंधित हों, तो प्राचलों का विलोपन किए बिना, $\frac{d y}{d x}$ ज्ञात कीजिए: $x=a(\cos \theta+\theta \sin \theta), y=a(\sin \theta-\theta \cos \theta)$
:::

:::solution{label="हल"}
यहाँ, $x=a(\cos \theta+\theta \sin \theta), y=a(\sin \theta-\theta \cos \theta)$
इसलिए, $\frac{d x}{d \theta}=a[-\sin \theta+(\theta \cos \theta+\sin \theta)]=a \theta \cos \theta$
तथा $\frac{d y}{d \theta}=a[\cos \theta-(-\theta \sin \theta+\cos \theta)]=a \theta \sin \theta$

$$
\frac{d y}{d x}=\frac{\frac{d y}{d \theta}}{\frac{d x}{d \theta}}=\frac{a \theta \sin \theta}{a \theta \cos \theta}=\tan \theta
$$
:::

:::answer
**उत्तर:** $\tan \theta$
:::

:::

:::question{number="11" kind="exercise" id="q_5.6.11" topic="Proving dy/dx = -y/x for a parametric power form"}
#### प्रश्न 11

:::prompt
यदि $x=\sqrt{a^{\sin ^{-1} t}}, y=\sqrt{a^{\cos ^{-1} t}}$, तो दर्शाइए कि $\frac{d y}{d x}=-\frac{y}{x}$
:::

:::solution{label="हल"}
यहाँ, $x=\sqrt{a^{\sin ^{-1} t}}, y=\sqrt{a^{\cos ^{-1} t}}$
इसलिए,

$$
\begin{aligned}
& \frac{d x}{d t}=\frac{1}{2 \sqrt{a^{\sin ^{-1} t}}} \cdot \frac{d}{d x} a^{\sin ^{-1} t}=\frac{1}{2 \sqrt{a^{\sin ^{-1} t}}} \cdot a^{\sin ^{-1} t} \cdot \log a \frac{1}{\sqrt{1-t^{2}}} \\
& =\frac{1}{2 x} \cdot x^{2} \cdot \log a \frac{1}{\sqrt{1-t^{2}}}=\frac{x \log a}{\sqrt{1-t^{2}}}
\end{aligned}
$$

तथा

$$
\begin{aligned}
& \frac{d y}{d t}=\frac{1}{2 \sqrt{a^{\cos ^{-1} t}}} \cdot \frac{d}{d x} a^{\cos ^{-1} t}=\frac{1}{2 \sqrt{a^{\cos ^{-1} t}}} \cdot a^{\cos ^{-1} t} \cdot \log a \frac{-1}{\sqrt{1-t^{2}}} \\
& =\frac{1}{2 y} \cdot y^{2} \cdot \log a \frac{1}{\sqrt{1-t^{2}}}=-\frac{y \log a}{\sqrt{1-t^{2}}} \\
& \frac{d y}{d x}=\frac{\frac{d y}{d t}}{\frac{d x}{d t}}=\frac{-\frac{y \log a}{\sqrt{1-t^{2}}}}{\frac{x \log a}{\sqrt{1-t^{2}}}}=-\frac{y}{x}
\end{aligned}
$$
:::

:::

:::question{number="1" kind="exercise" id="q_5.7.1" topic="Second-order derivative"}
#### प्रश्न 1

:::prompt
प्रश्न संख्या $1$ से $10$ तक में दिए फलनों के द्वितीय कोटि के अवकलज ज्ञात कीजिए: $x^{2}+3 x+2$
:::

:::solution{label="हल"}
माना $y=x^{2}+3 x+2$, इसलिए,

$$
\frac{d y}{d x}=\frac{d}{d x}\left(x^{2}+3 x+2\right)=2 x+3 \quad \Rightarrow \frac{d^{2} y}{d x^{2}}=\frac{d}{d x}(2 x+3)=2
$$
:::

:::answer
**उत्तर:** $2$
:::

:::

:::question{number="2" kind="exercise" id="q_5.7.2" topic="Second-order derivative"}
#### प्रश्न 2

:::prompt
प्रश्न संख्या $1$ से $10$ तक में दिए फलनों के द्वितीय कोटि के अवकलज ज्ञात कीजिए: $x^{20}$
:::

:::solution{label="हल"}
माना $y=x^{20}$, इसलिए,

$$
\frac{d y}{d x}=\frac{d}{d x}\left(x^{20}\right)=20 x^{19}
$$

$$
\Rightarrow \frac{d^{2} y}{d x^{2}}=\frac{d}{d x}\left(20 x^{19}\right)=380 x^{18}
$$
:::

:::answer
**उत्तर:** $380 x^{18}$
:::

:::

:::question{number="3" kind="exercise" id="q_5.7.3" topic="Second-order derivative"}
#### प्रश्न 3

:::prompt
प्रश्न संख्या $1$ से $10$ तक में दिए फलनों के द्वितीय कोटि के अवकलज ज्ञात कीजिए: $x \cdot \cos x$
:::

:::solution{label="हल"}
माना $y=x . \cos x$, इसलिए,

$$
\begin{aligned}
& \frac{d y}{d x}=\frac{d}{d x}(x \cdot \cos x)=x \cdot \frac{d}{d x} \cos x+\cos x \cdot \frac{d}{d x} x=-x \sin x+\cos x \\
& \Rightarrow \frac{d^{2} y}{d x^{2}}=\frac{d}{d x}(-x \sin x+\cos x)=-\left(x \frac{d}{d x} \sin x+\sin x \frac{d}{d x} x\right)-\sin x \\
& =-x \cos x-\sin x-\sin x=-(x \cos x+2 \sin x)
\end{aligned}
$$
:::

:::answer
**उत्तर:** $-(x \cos x+2 \sin x)$
:::

:::

:::question{number="4" kind="exercise" id="q_5.7.4" topic="Second-order derivative"}
#### प्रश्न 4

:::prompt
प्रश्न संख्या $1$ से $10$ तक में दिए फलनों के द्वितीय कोटि के अवकलज ज्ञात कीजिए: $\log x$
:::

:::solution{label="हल"}
माना $y=\log x$, इसलिए,

$$
\frac{d y}{d x}=\frac{d}{d x}(\log x)=\frac{1}{x} \quad \Rightarrow \frac{d^{2} y}{d x^{2}}=\frac{d}{d x}\left(\frac{1}{x}\right)=-\frac{1}{x^{2}}
$$
:::

:::answer
**उत्तर:** $-\frac{1}{x^{2}}$
:::

:::

:::question{number="5" kind="exercise" id="q_5.7.5" topic="Second-order derivative"}
#### प्रश्न 5

:::prompt
प्रश्न संख्या $1$ से $10$ तक में दिए फलनों के द्वितीय कोटि के अवकलज ज्ञात कीजिए: $x^{3} \log x$
:::

:::solution{label="हल"}
माना $y=x^{3} \log x$, इसलिए,

$$
\begin{aligned}
& \frac{d y}{d x}=\frac{d}{d x}\left(x^{3} \log x\right)=x^{3} \cdot \frac{d}{d x} \log x+\log x \cdot \frac{d}{d x} x^{3}=x^{3} \cdot \frac{1}{x}+\log x \cdot 3 x^{2}=x^{2}+3 x^{2} \log x \\
& \Rightarrow \frac{d^{2} y}{d x^{2}}=\frac{d}{d x}\left(x^{2}+3 x^{2} \log x\right)=2 x+3\left(x^{2} \frac{d}{d x} \log x+\log x \frac{d}{d x} x^{2}\right) \\
& =2 x+3\left(x^{2} \cdot \frac{1}{x}+\log x \cdot 2 x\right)=2 x+3 x+6 x \log x=5 x+6 x \log x=x(5+6 \log x)
\end{aligned}
$$
:::

:::answer
**उत्तर:** $x(5+6 \log x)$
:::

:::

:::question{number="6" kind="exercise" id="q_5.7.6" topic="Second-order derivative"}
#### प्रश्न 6

:::prompt
प्रश्न संख्या $1$ से $10$ तक में दिए फलनों के द्वितीय कोटि के अवकलज ज्ञात कीजिए: $e^{x} \sin 5 x$
:::

:::solution{label="हल"}
माना $y=e^{x} \sin 5 x$, इसलिए,

$$
\begin{aligned}
& \frac{d y}{d x}=\frac{d}{d x}\left(e^{x} \sin 5 x\right)=e^{x} \cdot \frac{d}{d x} \sin 5 x+\sin 5 x \cdot \frac{d}{d x} e^{x}=e^{x} \cdot \cos 5 x \cdot 5+\sin 5 x \cdot e^{x} \\
& \Rightarrow \frac{d^{2} y}{d x^{2}}=\frac{d}{d x}\left(5 e^{x} \cos 5 x+e^{x} \sin 5 x\right) \\
& =5\left(e^{x} \cdot \frac{d}{d x} \cos 5 x+\cos 5 x \cdot \frac{d}{d x} e^{x}\right)+\left(e^{x} \cdot \frac{d}{d x} \sin 5 x+\sin 5 x \cdot \frac{d}{d x} e^{x}\right) \\
& =5\left[e^{x} \cdot(-\sin 5 x) \cdot 5+\cos 5 x \cdot e^{x}\right]+\left[e^{x} \cdot \cos 5 x \cdot 5+\sin 5 x \cdot e^{x}\right] \\
& =e^{x}(-25 \sin 5 x+5 \cos 5 x+5 \cos 5 x+\sin 5 x)=e^{x}(10 \cos 5 x-24 \sin 5 x)
\end{aligned}
$$
:::

:::answer
**उत्तर:** $e^{x}(10 \cos 5 x-24 \sin 5 x)$
:::

:::

:::question{number="7" kind="exercise" id="q_5.7.7" topic="Second-order derivative"}
#### प्रश्न 7

:::prompt
प्रश्न संख्या $1$ से $10$ तक में दिए फलनों के द्वितीय कोटि के अवकलज ज्ञात कीजिए: $e^{6 x} \cos 3 x$
:::

:::solution{label="हल"}
माना $y=e^{6 x} \cos 3 x$, इसलिए,

$$
\begin{aligned}
& \frac{d y}{d x}=\frac{d}{d x}\left(e^{6 x} \cos 3 x\right)=e^{6 x} \cdot \frac{d}{d x} \cos 3 x+\cos 3 x \cdot \frac{d}{d x} e^{6 x} \\
& =e^{6 x} \cdot(-\sin 3 x) \cdot 3+\cos 3 x \cdot e^{6 x} \cdot 6=3 e^{6 x}(-\sin 3 x+2 \cos 3 x) \\
& \Rightarrow \frac{d^{2} y}{d x^{2}}=\frac{d}{d x}\left[3 e^{6 x}(-\sin 3 x+2 \cos 3 x)\right] \\
& =3 e^{6 x} \cdot \frac{d}{d x}(-\sin 3 x+2 \cos 3 x)+(-\sin 3 x+2 \cos 3 x) \cdot \frac{d}{d x} 3 e^{6 x} \\
& =3 e^{6 x} \cdot(-3 \cos 3 x-6 \sin 3 x)+(-\sin 3 x+2 \cos 3 x) \cdot 18 e^{6 x} \\
& =e^{6 x}(-9 \operatorname{cso} 3 x-18 \sin 3 x-18 \sin 3 x+36 \cos 3 x) \\
& =e^{6 x}(27 \cos 3 x-36 \sin 3 x)=9 e^{6 x}(3 \cos 3 x-4 \sin 3 x)
\end{aligned}
$$
:::

:::answer
**उत्तर:** $9 e^{6 x}(3 \cos 3 x-4 \sin 3 x)$
:::

:::

:::question{number="8" kind="exercise" id="q_5.7.8" topic="Second-order derivative"}
#### प्रश्न 8

:::prompt
प्रश्न संख्या $1$ से $10$ तक में दिए फलनों के द्वितीय कोटि के अवकलज ज्ञात कीजिए: $\tan ^{-1} x$
:::

:::solution{label="हल"}
माना $y=\tan ^{-1} x$, इसलिए,

$$
\begin{aligned}
& \frac{d y}{d x}=\frac{d}{d x}\left(\tan ^{-1} x\right)=\frac{1}{1+x^{2}} \\
& \Rightarrow \frac{d^{2} y}{d x^{2}}=\frac{d}{d x}\left(\frac{1}{1+x^{2}}\right)=\frac{\left(1+x^{2}\right) \frac{d}{d x} 1-1 \cdot \frac{d}{d x}\left(1+x^{2}\right)}{\left(1+x^{2}\right)^{2}} \\
& =\frac{0-2 x}{\left(1+x^{2}\right)^{2}}=-\frac{2 x}{\left(1+x^{2}\right)^{2}}
\end{aligned}
$$
:::

:::answer
**उत्तर:** $-\frac{2 x}{\left(1+x^{2}\right)^{2}}$
:::

:::

:::question{number="9" kind="exercise" id="q_5.7.9" topic="Second-order derivative"}
#### प्रश्न 9

:::prompt
प्रश्न संख्या $1$ से $10$ तक में दिए फलनों के द्वितीय कोटि के अवकलज ज्ञात कीजिए: $\log (\log x)$
:::

:::solution{label="हल"}
माना $y=\log (\log x)$, इसलिए,

$$
\begin{aligned}
& \frac{d y}{d x}=\frac{d}{d x}(\log (\log x))=\frac{1}{\log x} \cdot \frac{1}{x}=\frac{1}{x \log x} \\
& \Rightarrow \frac{d^{2} y}{d x^{2}}=\frac{d}{d x}\left(\frac{1}{x \log x}\right)=\frac{(x \log x) \frac{d}{d x} 1-1 \cdot \frac{d}{d x}(x \log x)}{(x \log x)^{2}} \\
& =\frac{0-\left(x \cdot \frac{1}{x}+\log x\right)}{(x \log x)^{2}}=-\frac{1+\log x}{(x \log x)^{2}}
\end{aligned}
$$
:::

:::answer
**उत्तर:** $-\frac{1+\log x}{(x \log x)^{2}}$
:::

:::

:::question{number="10" kind="exercise" id="q_5.7.10" topic="Second-order derivative"}
#### प्रश्न 10

:::prompt
प्रश्न संख्या $1$ से $10$ तक में दिए फलनों के द्वितीय कोटि के अवकलज ज्ञात कीजिए: $\sin (\log x)$
:::

:::solution{label="हल"}
माना $y=\sin (\log x)$, इसलिए,

$$
\begin{aligned}
& \frac{d y}{d x}=\frac{d}{d x}(\sin (\log x))=\cos (\log x) \cdot \frac{1}{x}=\frac{\cos (\log x)}{x} \\
& \Rightarrow \frac{d^{2} y}{d x^{2}}=\frac{d}{d x}\left[\frac{\cos (\log x)}{x}\right]=\frac{x \frac{d}{d x} \cos (\log x)-\cos (\log x) \cdot \frac{d}{d x} x}{(x)^{2}} \\
& =\frac{x\left\{-\sin (\log x) \cdot \frac{1}{x}\right\}-\cos (\log x) \cdot 1}{(x)^{2}}=\frac{-\sin (\log x)-\cos (\log x)}{(x)^{2}}
\end{aligned}
$$
:::

:::answer
**उत्तर:** $\frac{-\sin (\log x)-\cos (\log x)}{(x)^{2}}$
:::

:::

:::question{number="11" kind="exercise" id="q_5.7.11" topic="Proving a second-order ODE for 5cos x - 3sin x"}
#### प्रश्न 11

:::prompt
यदि $y=5 \cos x-3 \sin x$ है तो सिद्ध कीजिए कि $\frac{d^{2} y}{d x^{2}}+y=0$
:::

:::solution{label="हल"}
दिया है: $y=5 \cos x-3 \sin x$, इसलिए,

$$
\begin{aligned}
& \frac{d y}{d x}=\frac{d}{d x}(5 \cos x-3 \sin x)=-5 \sin x-3 \cos x \\
& \Rightarrow \frac{d^{2} y}{d x^{2}}=\frac{d}{d x}(-5 \sin x-3 \cos x)=-5 \cos x+3 \sin x=-(5 \cos x-3 \sin x)=-y \\
& \Rightarrow \frac{d^{2} y}{d x^{2}}+y=0
\end{aligned}
$$
:::

:::

:::question{number="12" kind="exercise" id="q_5.7.12" topic="Second-order derivative of arccos in terms of y"}
#### प्रश्न 12

:::prompt
यदि $y=\cos ^{-1} x$ है तो $\frac{d^{2} y}{d x^{2}}$ को केवल $y$ के पदों में ज्ञात कीजिए।
:::

:::solution{label="हल"}
दिया है: $y=\cos ^{-1} x \quad \Rightarrow \cos y=x$, इसलिए,

$$
\begin{aligned}
& -\sin y \frac{d y}{d x}=1 \quad \Rightarrow \frac{d y}{d x}=-\frac{1}{\sin y}=-\operatorname{cosec} y \\
& \Rightarrow \frac{d^{2} y}{d x^{2}}=-(-\operatorname{cosec} y \cot y) \cdot \frac{d y}{d x}=(\operatorname{cosec} y \cot y) \cdot(-\operatorname{cosec} y)=-\operatorname{cosec}^{2} y \cot y
\end{aligned}
$$
:::

:::answer
**उत्तर:** $-\operatorname{cosec}^{2} y \cot y$
:::

:::

:::question{number="13" kind="exercise" id="q_5.7.13" topic="Proving a second-order ODE involving log x"}
#### प्रश्न 13

:::prompt
यदि $y=3 \cos (\log x)+4 \sin (\log x)$ है तो दर्शाइए कि $x^{2} y_{2}+x y_{1}+y=0$
:::

:::solution{label="हल"}
दिया है: $y=3 \cos (\log x)+4 \sin (\log x)$, इसलिए,

$$
\begin{aligned}
& \frac{d y}{d x}=\frac{d}{d x}(3 \cos (\log x)+4 \sin (\log x))=-3 \sin (\log x) \cdot \frac{1}{x}+4 \cos (\log x) \cdot \frac{1}{x} \\
& \Rightarrow x \frac{d y}{d x}=-3 \sin (\log x)+4 \cos (\log x) \\
& \Rightarrow x \frac{d^{2} y}{d x^{2}}+\frac{d y}{d x} \cdot \frac{d}{d x} x=\frac{d}{d x}[-3 \sin (\log x)+4 \cos (\log x)] \\
& =-3 \cos (\log x) \cdot \frac{1}{x}-4 \sin (\log x) \cdot \frac{1}{x}=-\frac{1}{x}[3 \cos (\log x)+4 \sin (\log x)]=-\frac{1}{x} \cdot y \\
& \Rightarrow x \frac{d^{2} y}{d x^{2}}+\frac{d y}{d x}=-\frac{1}{x} y \quad \Rightarrow x^{2} \frac{d^{2} y}{d x^{2}}+x \frac{d y}{d x}=-y \quad \Rightarrow x^{2} \frac{d^{2} y}{d x^{2}}+x \frac{d y}{d x}+y=0 \\
& \Rightarrow x^{2} y_{2}+x y_{1}+y=0
\end{aligned}
$$
:::

:::

:::question{number="14" kind="exercise" id="q_5.7.14" topic="Proving a second-order ODE for a sum of exponentials"}
#### प्रश्न 14

:::prompt
यदि $y=\mathrm{A} e^{m x}+\mathrm{B} e^{n x}$ है तो दर्शाइए कि $\frac{d^{2} y}{d x^{2}}-(m+n) \frac{d y}{d x}+m n y=0$
:::

:::solution{label="हल"}
दिया है: $y=A e^{m x}+B e^{n x}$, इसलिए,

$$
\begin{aligned}
& \frac{d y}{d x}=\frac{d}{d x}\left(A e^{m x}+B e^{n x}\right)=m A e^{m x}+n B e^{n x} \\
& \Rightarrow \frac{d^{2} y}{d x^{2}}=\frac{d}{d x}\left(m A e^{m x}+n B e^{n x}\right)=m^{2} A e^{m x}+n^{2} B e^{n x} \\
& \frac{d^{2} y}{d x^{2}}-(m+n) \frac{d y}{d x}+m n y \text { में } \frac{d^{2} y}{d x^{2}} \text { और } \frac{d y}{d x} \text { का मान रखने पर } \\
& L H S=\left(m^{2} A e^{m x}+n^{2} B e^{n x}\right)-(m+n)\left(m A e^{m x}+n B e^{n x}\right)+m n y \\
& =m^{2} A e^{m x}+n^{2} B e^{n x}-\left(m^{2} A e^{m x}+m n B e^{n x}+m n A e^{m x}+n^{2} B e^{n x}\right)+m n y \\
& =-\left(m n A e^{m x}+m n B e^{n x}\right)+m n y \\
& =-m n\left(A e^{m x}+B e^{n x}\right)+m n y \\
& =-m n y+m n y=0=R H S
\end{aligned}
$$
:::

:::

:::question{number="15" kind="exercise" id="q_5.7.15" topic="Proving a second-order ODE proportional to y"}
#### प्रश्न 15

:::prompt
यदि $y=500 e^{7 x}+600 e^{-7 x}$ है तो दर्शाइए कि $\frac{d^{2} y}{d x^{2}}=49 y$ है।
:::

:::solution{label="हल"}
दिया है: $y=500 e^{7 x}+600 e^{-7 x}$, इसलिए,

$$
\begin{aligned}
& \frac{d y}{d x}=\frac{d}{d x}\left(500 e^{7 x}+600 e^{-7 x}\right)=500 e^{7 x} \cdot 7+600 e^{-7 x} \cdot(-7)=7\left(500 e^{7 x}-600 e^{-7 x}\right) \\
& \Rightarrow \frac{d^{2} y}{d x^{2}}=\frac{d}{d x} 7\left(500 e^{7 x}-600 e^{-7 x}\right)=7\left[500 e^{7 x} \cdot 7+600 e^{-7 x} \cdot(-7)\right] \\
& =49\left(500 e^{7 x}-600 e^{-7 x}\right)=49 y \quad \Rightarrow \frac{d^{2} y}{d x^{2}}=49 y
\end{aligned}
$$
:::

:::

:::question{number="16" kind="exercise" id="q_5.7.16" topic="Proving a second-order ODE equals squared first derivative"}
#### प्रश्न 16

:::prompt
यदि $e^{y}(x+1)=1$ है तो दर्शाइए कि $\frac{d^{2} y}{d x^{2}}=\left(\frac{d y}{d x}\right)^{2}$ है।
:::

:::solution{label="हल"}
दिया है: $e^{y}(x+1)=1$, इसलिए,

$$
\begin{aligned}
& e^{y} \frac{d y}{d x}(x+1)+(x+1) \frac{d}{d x} e^{y}=\frac{d}{d x} 1 \\
& \Rightarrow e^{y}+(x+1) e^{y} \frac{d y}{d x}=0 \\
& \Rightarrow \frac{d y}{d x}=-\frac{1}{x+1} \\
& \Rightarrow \frac{d^{2} y}{d x^{2}}=\frac{d}{d x}\left(-\frac{1}{x+1}\right)=-\left[\frac{(x+1) \cdot \frac{d}{d x} 1-1 \cdot \frac{d}{d x}(x+1)}{(x+1)^{2}}\right]=-\left[\frac{0-1}{(x+1)^{2}}\right]=\frac{1}{(x+1)^{2}} \\
& \Rightarrow \frac{d^{2} y}{d x^{2}}=\left(-\frac{1}{x+1}\right)^{2} \\
& \Rightarrow \frac{d^{2} y}{d x^{2}}=\left(\frac{d y}{d x}\right)^{2}
\end{aligned}
$$
:::

:::

:::question{number="17" kind="exercise" id="q_5.7.17" topic="Proving a second-order ODE for arctan squared"}
#### प्रश्न 17

:::prompt
यदि $y=\left(\tan ^{-1} x\right)^{2}$ है तो दर्शाइए कि $\left(x^{2}+1\right)^{2} y_{2}+2 x\left(x^{2}+1\right) y_{1}=2$ है।
:::

:::solution{label="हल"}
दिया है: $y=\left(\tan ^{-1} x\right)^{2}$, इसलिए,

$$
\begin{aligned}
& \frac{d y}{d x}=\frac{d}{d x}\left[\left(\tan ^{-1} x\right)^{2}\right]=2 \tan ^{-1} x \cdot \frac{1}{1+x^{2}}=\frac{2 \tan ^{-1} x}{1+x^{2}} \\
& \Rightarrow\left(1+x^{2}\right) \frac{d y}{d x}=2 \tan ^{-1} x \\
& \Rightarrow\left(1+x^{2}\right) \frac{d^{2} y}{d x^{2}}+\frac{d y}{d x} \cdot \frac{d}{d x}\left(1+x^{2}\right)=\frac{d}{d x}\left(2 \tan ^{-1} x\right) \\
& \Rightarrow\left(1+x^{2}\right) \frac{d^{2} y}{d x^{2}}+\frac{d y}{d x} \cdot 2 x=\frac{2}{1+x^{2}} \\
& \Rightarrow\left(1+x^{2}\right)^{2} \frac{d^{2} y}{d x^{2}}+2 x\left(1+x^{2}\right) \frac{d y}{d x}=2 \\
& \Rightarrow\left(x^{2}+1\right)^{2} y_{2}+2 x\left(x^{2}+1\right) y_{1}=2
\end{aligned}
$$
:::

:::

## अतिरिक्त प्रश्न

:::question{number="1" kind="additional_exercise" id="q_5.9.1" topic="Differentiating a power of a trinomial"}
#### अतिरिक्त प्रश्न 1

:::prompt
प्रश्न संख्या $1$ से $11$ तक प्रदत्त फलनों का, $x$ के सापेक्ष अवकलन कीजिए: $\left(3 x^{2}-9 x+5\right)^{9}$
:::

:::solution{label="हल"}
माना $y=\left(3 x^{2}-9 x+5\right)^{9}$, इसलिए,

$$
\begin{aligned}
& \frac{d y}{d x}=9\left(3 x^{2}-9 x+5\right)^{8} \cdot \frac{d}{d x}\left(3 x^{2}-9 x+5\right)=9\left(3 x^{2}-9 x+5\right)^{8} \cdot(6 x-9) \\
& =27\left(3 x^{2}-9 x+5\right)^{8} \cdot(2 x-3)
\end{aligned}
$$
:::

:::answer
**उत्तर:** $27\left(3 x^{2}-9 x+5\right)^{8} \cdot(2 x-3)$
:::

:::

:::question{number="2" kind="additional_exercise" id="q_5.9.2" topic="Differentiating a sum of trig powers"}
#### अतिरिक्त प्रश्न 2

:::prompt
प्रश्न संख्या $1$ से $11$ तक प्रदत्त फलनों का, $x$ के सापेक्ष अवकलन कीजिए: $\sin ^{3} x+\cos ^{6} x$
:::

:::solution{label="हल"}
माना $y=\sin ^{3} x+\cos ^{6} x$, इसलिए,

$$
\begin{aligned}
& \frac{d y}{d x}=3 \sin ^{2} x \cdot \frac{d}{d x} \sin x+6 \cos ^{5} x \cdot \frac{d}{d x} \cos x=3 \sin ^{2} x \cdot \cos x+6 \cos ^{5} x \cdot(-\sin x) \\
& =3 \sin x \cos x\left(\sin x-2 \cos ^{4} x\right)
\end{aligned}
$$
:::

:::answer
**उत्तर:** $3 \sin x \cos x\left(\sin x-2 \cos ^{4} x\right)$
:::

:::

:::question{number="3" kind="additional_exercise" id="q_5.9.3" topic="Differentiating a variable-base power with trig exponent"}
#### अतिरिक्त प्रश्न 3

:::prompt
प्रश्न संख्या $1$ से $11$ तक प्रदत्त फलनों का, $x$ के सापेक्ष अवकलन कीजिए: $(5 x)^{3 \cos x 2 x}$
:::

:::solution{label="हल"}
माना $y=(5 x)^{3 \cos 2 x}$, दोनों ओर $\log$ लेने पर $\log y=\log (5 x)^{3 \cos 2 x}=3 \cos 2 x . \log 5 x$ इसलिए,

$$
\begin{aligned}
& \frac{1}{y} \frac{d y}{d x}=3 \cos 2 x \cdot \frac{d}{d x} \log 5 x+\log 5 x \cdot \frac{d}{d x} 3 \cos 2 x \\
& \Rightarrow \frac{d y}{d x}=y\left[3 \cos 2 x \cdot \frac{1}{5 x} \cdot 5+\log 5 x \cdot 3(-\sin 2 x) \cdot 2\right] \\
& \Rightarrow \frac{d y}{d x}=3(5 x)^{3 \cos 2 x}\left[\frac{\cos 2 x-2 \sin 2 x \log 5 x}{x}\right]
\end{aligned}
$$
:::

:::answer
**उत्तर:** $3(5 x)^{3 \cos 2 x}\left[\frac{\cos 2 x-2 \sin 2 x \log 5 x}{x}\right]$
:::

:::

:::question{number="4" kind="additional_exercise" id="q_5.9.4" topic="Differentiating an inverse sine of a radical"}
#### अतिरिक्त प्रश्न 4

:::prompt
प्रश्न संख्या $1$ से $11$ तक प्रदत्त फलनों का, $x$ के सापेक्ष अवकलन कीजिए: $\sin ^{-1}(x \sqrt{x}), 0 \leq x \leq 1$.
:::

:::solution{label="हल"}
माना $y=\sin ^{-1}(x \sqrt{x})$, इसलिए,

$$
\begin{aligned}
& \frac{d y}{d x}=\frac{1}{\sqrt{1-(x \sqrt{x})^{2}}} \cdot \frac{d}{d x}(x \sqrt{x})=\frac{1}{\sqrt{1-x^{3}}} \cdot\left[x \frac{d}{d x} \sqrt{x}+\sqrt{x} \cdot \frac{d}{d x} x\right] \\
& =\frac{1}{\sqrt{1-x^{3}}} \cdot\left[x \frac{1}{2 \sqrt{x}}+\sqrt{x} \cdot 1\right]=\frac{1}{\sqrt{1-x^{3}}} \cdot\left[\frac{x+2 x}{2 \sqrt{x}}\right]=\frac{3 x}{2 \sqrt{x} \sqrt{1-x^{3}}}=\frac{3}{2} \sqrt{\frac{x}{1-x^{3}}}
\end{aligned}
$$
:::

:::answer
**उत्तर:** $\frac{3}{2} \sqrt{\frac{x}{1-x^{3}}}$
:::

:::

:::question{number="5" kind="additional_exercise" id="q_5.9.5" topic="Differentiating an inverse-cosine-over-radical quotient"}
#### अतिरिक्त प्रश्न 5

:::prompt
प्रश्न संख्या $1$ से $11$ तक प्रदत्त फलनों का, $x$ के सापेक्ष अवकलन कीजिए: $\frac{\cos ^{-1} \frac{x}{2}}{\sqrt{2 x+7}},-2<x<2$.
:::

:::solution{label="हल"}
माना $y=\frac{\cos ^{-1} \frac{x}{2}}{\sqrt{2 x+7}}$, इसलिए,

$$
\begin{aligned}
& \frac{d y}{d x}=\frac{\cos ^{-1} \frac{x}{2} \cdot \frac{d}{d x} \sqrt{2 x+7}-\sqrt{2 x+7} \frac{d}{d x} \cos ^{-1} \frac{x}{2}}{(\sqrt{2 x+7})^{2}} \\
& =\frac{\left[\cos ^{-1} \frac{x}{2} \cdot \frac{1}{2 \sqrt{2 x+7}} \cdot 2\right]-\sqrt{2 x+7} \frac{-1}{\sqrt{1-\left(\frac{x}{2}\right)^{2}}} \cdot \frac{1}{2}}{2 x+7} \\
& =\frac{\cos ^{-1} \frac{x}{2} \cdot \frac{1}{\sqrt{2 x+7}}+\sqrt{2 x+7} \frac{1}{\sqrt{4-(x)^{2}}}}{2 x+7}=\frac{\cos ^{-1} \frac{x}{2} \cdot \sqrt{4-x^{2}}+2 x+7}{(2 x+7) \sqrt{2 x+7} \sqrt{4-x^{2}}}
\end{aligned}
$$
:::

:::answer
**उत्तर:** $\frac{\cos ^{-1} \frac{x}{2} \cdot \sqrt{4-x^{2}}+2 x+7}{(2 x+7) \sqrt{2 x+7} \sqrt{4-x^{2}}}$
:::

:::

:::question{number="6" kind="additional_exercise" id="q_5.9.6" topic="Differentiating an inverse-cotangent radical expression"}
#### अतिरिक्त प्रश्न 6

:::prompt
प्रश्न संख्या $1$ से $11$ तक प्रदत्त फलनों का, $x$ के सापेक्ष अवकलन कीजिए: $\cot ^{-1}\left[\frac{\sqrt{1+\sin x}+\sqrt{1-\sin x}}{\sqrt{1+\sin x}-\sqrt{1-\sin x}}\right], 0<x<\frac{\pi}{2}$
:::

:::solution{label="हल"}
माना $y=\cot ^{-1}\left[\frac{\sqrt{1+\sin x}+\sqrt{1-\sin x}}{\sqrt{1+\sin x}+\sqrt{1-\sin x}}\right]$, इसलिए,

$$
\begin{aligned}
& y=\cot ^{-1}\left[\frac{\sqrt{\cos ^{2} \frac{x}{2}+\sin ^{2} \frac{x}{2}+2 \sin \frac{x}{2} \cos \frac{x}{2}}+\sqrt{\cos ^{2} \frac{x}{2}+\sin ^{2} \frac{x}{2}-2 \sin \frac{x}{2} \cos \frac{x}{2}}}{\sqrt{\cos ^{2} \frac{x}{2}+\sin ^{2} \frac{x}{2}+2 \sin \frac{x}{2} \cos \frac{x}{2}}-\sqrt{\cos ^{2} \frac{x}{2}+\sin ^{2} \frac{x}{2}-2 \sin \frac{x}{2} \cos \frac{x}{2}}}\right] \\
& =\cot ^{-1}\left[\frac{\sqrt{\left(\cos \frac{x}{2}+\sin \frac{x}{2}\right)^{2}}+\sqrt{\left(\cos \frac{x}{2}-\sin \frac{x}{2}\right)^{2}}}{\sqrt{\left(\cos \frac{x}{2}+\sin \frac{x}{2}\right)^{2}}-\sqrt{\left(\cos \frac{x}{2}-\sin \frac{x}{2}\right)^{2}}}\right] \\
& =\cot ^{-1}\left[\frac{\cos \frac{x}{2}+\sin \frac{x}{2}+\cos \frac{x}{2}-\sin \frac{x}{2}}{\cos \frac{x}{2}+\sin \frac{x}{2}-\cos \frac{x}{2}+\sin \frac{x}{2}}\right]=\cot ^{-1}\left[\frac{2 \cos \frac{x}{2}}{2 \sin \frac{x}{2}}\right]=\cot ^{-1}\left[\cot \frac{x}{2}\right]=\frac{x}{2}
\end{aligned}
$$

इसलिए, $\frac{d y}{d x}=\frac{1}{2}$
:::

:::answer
**उत्तर:** $\frac{d y}{d x}=\frac{1}{2}$
:::

:::

:::question{number="7" kind="additional_exercise" id="q_5.9.7" topic="Differentiating (log x)^log x"}
#### अतिरिक्त प्रश्न 7

:::prompt
प्रश्न संख्या $1$ से $11$ तक प्रदत्त फलनों का, $x$ के सापेक्ष अवकलन कीजिए: $(\log x)^{\log x}, x>1$
:::

:::solution{label="हल"}
माना $y=(\log x)^{\log x}$, दोनों ओर $\log$ लेने पर
$\log y=\log (\log x)^{\log x}=\log x . \log (\log x)$
इसलिए,

$$
\frac{1}{y} \frac{d y}{d x}=\log x \cdot \frac{d}{d x} \log (\log x)+\log (\log x) \cdot \frac{d}{d x} \log x
$$

$$
\begin{aligned}
& \Rightarrow \frac{d y}{d x}=y\left[\log x \cdot \frac{1}{\log x} \cdot \frac{1}{x}+\log (\log x) \cdot \frac{1}{x}\right] \\
& \Rightarrow \frac{d y}{d x}=(\log x)^{\log x}\left[\frac{1+\log (\log x)}{x}\right]
\end{aligned}
$$
:::

:::answer
**उत्तर:** $(\log x)^{\log x}\left[\frac{1+\log (\log x)}{x}\right]$
:::

:::

:::question{number="8" kind="additional_exercise" id="q_5.9.8" topic="Differentiating cosine of a linear trig combination"}
#### अतिरिक्त प्रश्न 8

:::prompt
प्रश्न संख्या $1$ से $11$ तक प्रदत्त फलनों का, $x$ के सापेक्ष अवकलन कीजिए: $\cos (a \cos x+b \sin x)$, किन्हीं अचर $a$ तथा $b$ के लिए
:::

:::solution{label="हल"}
माना $y=\cos (a \cos x+b \sin x)$, इसलिए,

$$
\begin{aligned}
& \frac{d y}{d x}=-\sin (a \cos x+b \sin x) \cdot \frac{d}{d x}(a \cos x+b \sin x) \\
& =-\sin (a \cos x+b \sin x)(-a \sin x+b \cos x) \\
& =\sin (a \cos x+b \sin x)(a \sin x-b \cos x)
\end{aligned}
$$
:::

:::answer
**उत्तर:** $\sin (a \cos x+b \sin x)(a \sin x-b \cos x)$
:::

:::

:::question{number="9" kind="additional_exercise" id="q_5.9.9" topic="Differentiating a trig-difference power of itself"}
#### अतिरिक्त प्रश्न 9

:::prompt
प्रश्न संख्या $1$ से $11$ तक प्रदत्त फलनों का, $x$ के सापेक्ष अवकलन कीजिए: $(\sin x-\cos x)^{(\sin x-\cos x)}, \frac{\pi}{4}<x<\frac{3 \pi}{4}$
:::

:::solution{label="हल"}
माना $y=(\sin x-\cos x)^{(\sin x-\cos x)}$, दोनों ओर $\log$ लेने पर

$$
\log y=\log (\sin x-\cos x)^{(\sin x-\cos x)}=(\sin x-\cos x) \cdot \log (\sin x-\cos x)
$$

इसलिए,

$$
\begin{aligned}
& \frac{1}{y} \frac{d y}{d x}=(\sin x-\cos x) \cdot \frac{d}{d x} \log (\sin x-\cos x)+\log (\sin x-\cos x) \cdot \frac{d}{d x}(\sin x-\cos x) \\
& \Rightarrow \frac{d y}{d x}=y\left[(\sin x-\cos x) \cdot \frac{(\cos x+\sin x)}{(\sin x-\cos x)}+\log (\sin x-\cos x)(\cos x+\sin x)\right] \\
& \Rightarrow \frac{d y}{d x}=(\sin x-\cos x)^{(\sin x-\cos x)}(\cos x+\sin x)[1+\log (\cos x-\sin x)]
\end{aligned}
$$
:::

:::answer
**उत्तर:** $(\sin x-\cos x)^{(\sin x-\cos x)}(\cos x+\sin x)[1+\log (\cos x-\sin x)]$
:::

:::

:::question{number="10" kind="additional_exercise" id="q_5.9.10" topic="Differentiating a sum of variable-exponent powers"}
#### अतिरिक्त प्रश्न 10

:::prompt
प्रश्न संख्या $1$ से $11$ तक प्रदत्त फलनों का, $x$ के सापेक्ष अवकलन कीजिए: $x^{x}+x^{a}+a^{x}+a^{a}$, किसी नियत $a>0$ तथा $x>0$ के लिए
:::

:::solution{label="हल"}
माना $u=x^{x}$ तथा $y=u+x^{a}+a^{x}+a^{a}$ इसलिए

$$
\begin{aligned}
& \frac{d y}{d x}=\frac{d u}{d x}+\frac{\mathrm{d}}{\mathrm{dx}} x^{a}+\frac{\mathrm{d}}{\mathrm{dx}} a^{x}+\frac{\mathrm{d}}{\mathrm{dx}} a^{a} \\
& \Rightarrow \frac{d y}{d x}=\frac{d u}{d x}+a x^{a-1}+a^{x} \log a+0
\end{aligned}
$$

यहाँ, $u=x^{x}$, दोनों ओर $\log$ लेने पर
$\log u=\log x^{x}=x . \log x$
इसलिए,

$$
\begin{aligned}
& \frac{1}{u} \frac{d u}{d x}=x \cdot \frac{d}{d x} \log x+\log x \cdot \frac{d}{d x} x=x \cdot \frac{1}{x}+\log x \cdot 1 \\
& \Rightarrow \frac{d u}{d x}=u(1+\log x)=x^{x}(1+\log x)
\end{aligned}
$$

समीकरण (1) में $\frac{d u}{d x}$ का मान रखने पर

$$
\frac{d y}{d x}=x^{x}(1+\log x)+a x^{a-1}+a^{x} \log a
$$
:::

:::answer
**उत्तर:** $x^{x}(1+\log x)+a x^{a-1}+a^{x} \log a$
:::

:::

:::question{number="11" kind="additional_exercise" id="q_5.9.11" topic="Differentiating a sum of variable-exponent powers"}
#### अतिरिक्त प्रश्न 11

:::prompt
प्रश्न संख्या $1$ से $11$ तक प्रदत्त फलनों का, $x$ के सापेक्ष अवकलन कीजिए: $x^{x^{2}-3}+(x-3)^{x^{2}}, x>3$ के लिए
:::

:::solution{label="हल"}
माना $u=x^{x^{2}-3}$ तथा $v=(x-3)^{x^{2}}$ इसलिए, $y=u+v$
दोनों ओर $x$ के सापेक्ष अवकलन करने पर

$$
\frac{d y}{d x}=\frac{d u}{d x}+\frac{d v}{d x}
$$

यहाँ, $u=x^{x^{2}-3}$, दोनों ओर $\log$ लेने पर
$\log u=\left(x^{2}-3\right) \log x$, इसलिए,

$$
\begin{aligned}
& \frac{1}{u} \frac{d u}{d x}=\left(x^{2}-3\right) \cdot \frac{d}{d x} \log x+\log x \cdot \frac{d}{d x}\left(x^{2}-3\right) \\
& =\left(x^{2}-3\right) \cdot \frac{1}{x}+\log x \cdot 2 x \\
& \frac{d u}{d x}=u\left[\frac{x^{2}-3+2 x^{2} \log x}{x}\right] \\
& \frac{d u}{d x}=x^{x^{2}-3}\left[\frac{x^{2}-3+2 x^{2} \log x}{x}\right]=x^{x^{2}-4}\left(x^{2}-3+2 x^{2} \log x\right)
\end{aligned}
$$

तथा , $v=(x-3)^{x^{2}}$, दोनों ओर $\log$ लेने पर
$\log v=x^{2} \log (x-3)$, इसलिए,

$$
\begin{aligned}
& \frac{1}{v} \frac{d v}{d x}=x^{2} \cdot \frac{d}{d x} \log (x-3)+\log (x-3) \cdot \frac{d}{d x} x^{2} \\
& =x^{2} \cdot \frac{1}{x-3}+\log (x-3) \cdot 2 x \\
& =\frac{x^{2}}{x-3}+2 x \cdot \log (x-3) \\
& \frac{d v}{d x}=v\left[\frac{x^{2}}{x-3}+2 x \cdot \log (x-3)\right] \\
& =(x-3)^{x^{2}}\left[\frac{x^{2}}{x-3}+2 x \cdot \log (x-3)\right]
\end{aligned}
$$

समीकरण (2) से $\frac{d u}{d x}$ का तथा समीकरण (3) से $\frac{d v}{d x}$ का मान समीकरण (1) में रखने पर

$$
\frac{d y}{d x}=x^{x^{2}-4}\left(x^{2}-3+2 x^{2} \log x\right)+(x-3)^{x^{2}}\left[\frac{x^{2}}{x-3}+2 x \cdot \log (x-3)\right]
$$
:::

:::answer
**उत्तर:** $x^{x^{2}-4}\left(x^{2}-3+2 x^{2} \log x\right)+(x-3)^{x^{2}}\left[\frac{x^{2}}{x-3}+2 x \cdot \log (x-3)\right]$
:::

:::

:::question{number="12" kind="additional_exercise" id="q_5.9.12" topic="Parametric second-order derivative"}
#### अतिरिक्त प्रश्न 12

:::prompt
यदि $y=12(1-\cos t), x=10(t-\sin t),-\frac{\pi}{2}<t<\frac{\pi}{2}$ तो $\frac{d y}{d x}$ ज्ञात कीजिए।
:::

:::solution{label="हल"}
यहाँ, $x=10(t-\sin t), y=12(1-\cos t)$
इसलिए, $\frac{d x}{d t}=10(1-\cos t)$ तथा $\frac{d y}{d t}=12(0+\sin t)$

$$
\frac{d y}{d x}=\frac{\frac{d y}{d t}}{\frac{d x}{d t}}=\frac{12 \sin t}{10(1-\cos t)}=\frac{6\left(2 \sin \frac{t}{2} \cos \frac{t}{2}\right)}{5\left(2 \sin ^{2} \frac{t}{2}\right)}=\frac{6}{5} \cot \frac{t}{2}
$$
:::

:::answer
**उत्तर:** $\frac{6}{5} \cot \frac{t}{2}$
:::

:::

:::question{number="13" kind="additional_exercise" id="q_5.9.13" topic="Derivative of a sum of inverse-trig functions"}
#### अतिरिक्त प्रश्न 13

:::prompt
यदि $y=\sin ^{-1} x+\sin ^{-1} \sqrt{1-x^{2}}, 0<x<1$ है तो $\frac{d y}{d x}$ ज्ञात कीजिए।
:::

:::solution{label="हल"}
यहाँ, $y=\sin ^{-1} x+\sin ^{-1} \sqrt{1-x^{2}}$
इसलिए,

$$
\begin{aligned}
& \frac{d y}{d x}=\frac{d}{d x} \sin ^{-1} x+\frac{d}{d x} \sin ^{-1} \sqrt{1-x^{2}} \\
& \Rightarrow \frac{d y}{d x}=\frac{1}{\sqrt{1-x^{2}}}+\frac{1}{\sqrt{1-\left(\sqrt{1-x^{2}}\right)^{2}}} \frac{d}{d x} \sqrt{1-x^{2}} \\
& \Rightarrow \frac{d y}{d x}=\frac{1}{\sqrt{1-x^{2}}}+\frac{1}{x} \cdot \frac{1}{2 \sqrt{1-x^{2}}} \frac{d}{d x}\left(1-x^{2}\right) \\
& \Rightarrow \frac{d y}{d x}=\frac{1}{\sqrt{1-x^{2}}}+\frac{1}{x} \cdot \frac{1}{2 \sqrt{1-x^{2}}}(-2 x)=\frac{1}{\sqrt{1-x^{2}}}-\frac{1}{\sqrt{1-x^{2}}}=0
$$
:::

:::answer
**उत्तर:** $\frac{d y}{d x}=0$
:::

:::

:::question{number="14" kind="additional_exercise" id="q_5.9.14" topic="Proving an implicit-derivative identity"}
#### अतिरिक्त प्रश्न 14

:::prompt
यदि $-1<x<1$ के लिए $x \sqrt{1+y}+y \sqrt{1+x}=0$ है तो सिद्ध कीजिए कि

$$
\frac{d y}{d x}=-\frac{1}{(1+x)^{2}}
$$
:::

:::solution{label="हल"}
दिया है: $x \sqrt{1+y}+y \sqrt{1+x}=0 \quad \Rightarrow x \sqrt{1+y}=-y \sqrt{1+x}$
दोनों ओर वर्ग करने पर

$$
\begin{array}{lc}
x^{2}(1+y)=y^{2}(1+x) & \Rightarrow x^{2}+x^{2} y=y^{2}+y^{2} x \\
\Rightarrow x^{2}-y^{2}+x^{2} y-y^{2} x=0 & \\
\Rightarrow(x+y)(x-y)+x y(x-y)=0 & \Rightarrow(x-y)(x+y+x y)=0 \\
\Rightarrow(x+y+x y)=0 & {[\because x \neq y \quad \Rightarrow x-y \neq 0]} \\
\Rightarrow y(1+x)=-x & \\
\Rightarrow y=-\frac{x}{1+x} &
\end{array}
$$

इसलिए,

$$
\frac{d y}{d x}=-\left[\frac{(1+x) \frac{d}{d x} x-x \frac{d}{d x}(1+x)}{(1+x)^{2}}\right]=-\frac{1+x-x}{(1+x)^{2}}=-\frac{1}{(1+x)^{2}}
$$
:::

:::

:::question{number="15" kind="additional_exercise" id="q_5.9.15" topic="Proving a circle-parametrization curvature identity"}
#### अतिरिक्त प्रश्न 15

:::prompt
यदि किसी $c>0$ के लिए $(x-a)^{2}+(y-b)^{2}=c^{2}$ है तो सिद्ध कीजिए कि

$$
\frac{\left[1+\left(\frac{d y}{d x}\right)^{2}\right]^{\frac{3}{2}}}{\frac{d^{2} y}{d x^{2}}}, a \text { और } b \text { से स्वतंत्र एक स्थिर राशि है। }
$$
:::

:::solution{label="हल"}
दिया है: $(x-a)^{2}+(y-b)^{2}=c^{2}$, इसलिए,
दोनों पक्षों का $x$ के सापेक्ष अवकलन करने पर

$$
\begin{aligned}
& \frac{d}{d x}(x-a)^{2}+\frac{d}{d x}(y-b)^{2}=\frac{d}{d x} c^{2} \\
& \Rightarrow 2(x-a)+2(y-b) \frac{d y}{d x}=0 \\
& \Rightarrow \frac{d y}{d x}=-\frac{x-a}{y-b}
\end{aligned}
$$

पुनः अवकलन करने पर

$$
\begin{aligned}
& \frac{d^{2} y}{d x^{2}}=-\frac{(y-b) \frac{d}{d x}(x-a)-(x-a) \frac{d}{d x}(y-b)}{(y-b)^{2}}=-\frac{(y-b) 1-(x-a) \frac{d y}{d x}}{(y-b)^{2}} \\
& \Rightarrow \frac{d^{2} y}{d x^{2}}=-\frac{(y-b) 1-(x-a)\left(-\frac{x-a}{y-b}\right)}{(y-b)^{2}}=-\frac{(y-b)^{2}+(x-a)^{2}}{(y-b)^{3}}=-\frac{c^{2}}{(y-b)^{3}}
\end{aligned}
$$

$\frac{\left[1+\left(\frac{d y}{d x}\right)^{2}\right]^{\frac{3}{2}}}{\frac{d^{2} y}{d x^{2}}}$ में मान रखने पर

$$
\frac{\left[1+\left(-\frac{x-a}{y-b}\right)^{2}\right]^{\frac{3}{2}}}{-\frac{c^{2}}{(y-b)^{3}}}=\frac{\left[1+\frac{(x-a)^{2}}{(y-b)^{2}}\right]^{\frac{3}{2}}}{-\frac{c^{2}}{(y-b)^{3}}}=\frac{\left[\frac{(y-b)^{2}+(x-a)^{2}}{(y-b)^{2}}\right]^{\frac{3}{2}}}{-\frac{c^{2}}{(y-b)^{3}}}=\frac{\left[\frac{c^{2}}{(y-b)^{2}}\right]^{\frac{3}{2}}}{-\frac{c^{2}}{(y-b)^{3}}}
$$

$=\frac{\frac{c^{3}}{(y-b)^{3}}}{-\frac{c^{2}}{(y-b)^{3}}}=-\frac{c^{3}}{c^{2}}=-c, \quad$ जो $a$ और $b$ से स्वतंत्र एक स्थिर राशि है।
:::

:::

:::question{number="16" kind="additional_exercise" id="q_5.9.16" topic="Proving an implicit-derivative identity"}
#### अतिरिक्त प्रश्न 16

:::prompt
यदि $\cos y=x \cos (a+y)$, तथा $\cos a \neq \pm 1$, तो सिद्ध कीजिए कि $\frac{d y}{d x}=\frac{\cos ^{2}(a+y)}{\sin a}$
:::

:::solution{label="हल"}
दिया है: $\cos y=x \cos (a+y) \quad \Rightarrow x=\frac{\cos y}{\cos (a+y)}$, इसलिए,
दोनों पक्षों का $y$ के सापेक्ष अवकलन करने पर

$$
\frac{d x}{d y}=\frac{\cos (a+y) \frac{d}{d y} \cos y-\cos y \frac{d}{d y} \cos (a+y)}{\cos ^{2}(a+y)}
$$

$$
\begin{aligned}
& \Rightarrow \frac{d x}{d y}=\frac{\cos (a+y)(-\sin y)-\cos y(-\sin (a+y))}{\cos ^{2}(a+y)} \\
& \Rightarrow \frac{d x}{d y}=\frac{-\sin y \cos (a+y)+\cos y \sin (a+y)}{\cos ^{2}(a+y)}=\frac{\sin (a+y-y)}{\cos ^{2}(a+y)}=\frac{\sin a}{\cos ^{2}(a+y)} \\
& \Rightarrow \frac{d y}{d x}=\frac{\cos ^{2}(a+y)}{\sin a}
\end{aligned}
$$
:::

:::

:::question{number="17" kind="additional_exercise" id="q_5.9.17" topic="Parametric second-order derivative"}
#### अतिरिक्त प्रश्न 17

:::prompt
यदि $x=a(\cos t+t \sin t)$ और $y=a(\sin t-t \cos t)$, तो $\frac{d^{2} y}{d x^{2}}$ ज्ञात कीजिए।
:::

:::solution{label="हल"}
यहाँ, $x=a(\cos t+t \sin t), y=a(\sin t-t \cos t)$
इसलिए, $\frac{d x}{d t}=a[-\sin t+(t \cos t+\sin t)]=a t \cos t$ तथा

$$
\begin{aligned}
& \frac{d y}{d t}=a[(\cos t-(-t \sin t+\cos t))]=a t \sin t \\
& \frac{d y}{d x}=\frac{\frac{d y}{d t}}{\frac{d x}{d t}}=\frac{a t \sin t}{a t \cos t}=\tan t \Rightarrow \frac{d^{2} y}{d x^{2}}=\sec ^{2} t \cdot \frac{d t}{d x}=\sec ^{2} t \cdot \frac{1}{a t \cos t}=\frac{\sec ^{3} t}{a t}
\end{aligned}
$$
:::

:::answer
**उत्तर:** $\frac{\sec ^{3} t}{a t}$
:::

:::

:::question{number="18" kind="additional_exercise" id="q_5.9.18" topic="Proving the second derivative of |x|^3 exists"}
#### अतिरिक्त प्रश्न 18

:::prompt
यदि $f(x)=|x|^{3}$, तो प्रमाणित कीजिए कि $f^{\prime \prime}(x)$ का अस्तित्व है और इसे ज्ञात भी कीजिए।
:::

:::solution{label="हल"}
$f(x)=|x|^{3}$ को पुनः व्यवस्थित करके लिखने पर

$$
f(x)=\left\{\begin{array}{cc}
x^{3} & \text { यदि } \mathrm{x} \geq 0 \\
-x^{3} & \text { यदि } \mathrm{x}<0
\end{array}\right.
$$

यदि $x \geq 0, f(x)=x^{3} \quad \Rightarrow f^{\prime}(x)=3 x^{2} \quad \Rightarrow f^{\prime \prime}(x)=6 x$
यदि $x<0, f(x)=-x^{3} \quad \Rightarrow f^{\prime}(x)=-3 x^{2} \quad \Rightarrow f^{\prime \prime}(x)=-6 x$
अतः, $f^{\prime \prime}(x)$ का अस्तित्व सभी वास्तविक संख्याओं के लिए है। इसप्रकार

$$
f^{\prime \prime}(x)=\left\{\begin{array}{cc}
6 x & \text { यदि } \mathrm{x} \geq 0 \\
-6 x & \text { यदि } \mathrm{x}<0
\end{array}\right.
$$
:::

:::answer
**उत्तर:** $f^{\prime \prime}(x)=6 x$ ($x \geq 0$ के लिए), $f^{\prime \prime}(x)=-6 x$ ($x<0$ के लिए)
:::

:::

:::question{number="19" kind="additional_exercise" id="q_5.9.19" topic="Deriving the cosine sum formula by differentiation"}
#### अतिरिक्त प्रश्न 19

:::prompt
$\sin (\mathrm{A}+\mathrm{B})=\sin \mathrm{A} \cos \mathrm{B}+\cos \mathrm{A} \sin \mathrm{B}$ का प्रयोग करते हुए अवकलन द्वारा cosines के लिए योग सूत्र ज्ञात कीजिए।
:::

:::solution{label="हल"}
दिया है: $\sin (A+B)=\sin A \cos B+\cos A \sin B$, दोनों पक्षों का $x$ के सापेक्ष अवकलन करने पर

$$
\begin{aligned}
& \frac{d}{d x} \sin (A+B)=\left(\sin A \frac{d}{d x} \cos B+\cos B \frac{d}{d x} \sin A\right)+\left(\cos A \frac{d}{d x} \sin B+\sin B \frac{d}{d x} \cos A\right) \\
& \Rightarrow \cos (A+B) \cdot\left(\frac{d A}{d x}+\frac{d B}{d x}\right) \\
& =\left(\sin A(-\sin B) \frac{d B}{d x}+\cos B \cos A \frac{d A}{d x}\right)+\left(\cos A \cos B \frac{d B}{d x}+\sin B(-\sin A) \frac{d A}{d x}\right) \\
& \Rightarrow \cos (A+B) \cdot\left(\frac{d A}{d x}+\frac{d B}{d x}\right) \\
& =(\cos A \cos B-\sin A \sin B) \frac{d B}{d x}+(\cos A \cos B-\sin A \sin B) \frac{d A}{d x} \\
& \Rightarrow \cos (A+B) \cdot\left(\frac{d A}{d x}+\frac{d B}{d x}\right)=(\cos A \cos B-\sin A \sin B)\left(\frac{d A}{d x}+\frac{d B}{d x}\right) \\
& \Rightarrow \cos (A+B)=\cos A \cos B-\sin A \sin B
\end{aligned}
$$
:::

:::answer
**उत्तर:** $\cos (A+B)=\cos A \cos B-\sin A \sin B$
:::

:::

:::question{number="20" kind="additional_exercise" id="q_5.9.20" topic="Existence of a continuous, twice-non-differentiable function"}
#### अतिरिक्त प्रश्न 20

:::prompt
क्या एक ऐसे फलन का अस्तित्व है, जो प्रत्येक बिंदु पर संतत हो किंतु केवल दो बिंदुओं पर अवकलनीय न हो? अपने उत्तर का औचित्य भी बतलाइए।
:::

:::solution{label="हल"}
फलन $f(x)=|x-1|+|x-3|$ प्रत्येक बिंदु पर संतत है किंतु केवल दो बिंदुओं $(x=1$ तथा $x=3)$ पर अवकलनीय नहीं है।
:::

:::answer
**उत्तर:** $f(x)=|x-1|+|x-3|$
:::

:::

:::question{number="21" kind="additional_exercise" id="q_5.9.21" topic="Proving a determinant-derivative identity"}
#### अतिरिक्त प्रश्न 21

:::prompt
यदि $y=\left|\begin{array}{ccc}f(x) & g(x) & h(x) \\ l & m & n \\ a & b & c\end{array}\right|$ है तो सिद्ध कीजिए कि $\frac{d y}{d x}=\left|\begin{array}{ccc}f^{\prime}(x) & g^{\prime}(x) & h^{\prime}(x) \\ l & m & n \\ a & b & c\end{array}\right|$
:::

:::solution{label="हल"}
दिया है: $y=\left|\begin{array}{ccc}f(x) & g(x) & h(x) \\ l & m & n \\ a & b & c\end{array}\right|$, इसलिए,

$$
\begin{aligned}
& \frac{d y}{d x}=\left|\begin{array}{ccc}
f^{\prime}(x) & g^{\prime}(x) & h^{\prime}(x) \\
l & m & n \\
a & b & c
\end{array}\right|+\left|\begin{array}{ccc}
f(x) & g(x) & h(x) \\
\frac{d l}{d x} & \frac{d m}{d x} & \frac{d n}{d x} \\
a & b & c
\end{array}\right|+\left|\begin{array}{ccc}
f(x) & g(x) & h(x) \\
l & m & n \\
\frac{d a}{d x} & \frac{d b}{d x} & \frac{d c}{d x}
\end{array}\right| \\
& \Rightarrow \frac{d y}{d x}=\left|\begin{array}{ccc}
f^{\prime}(x) & g^{\prime}(x) & h^{\prime}(x) \\
l & m & n \\
a & b & c
\end{array}\right|+\left|\begin{array}{ccc}
f(x) & g(x) & h(x) \\
0 & 0 & 0 \\
a & b & c
\end{array}\right|+\left|\begin{array}{ccc}
f(x) & g(x) & h(x) \\
l & m & n \\
0 & 0 & 0
\end{array}\right| \\
& \Rightarrow \frac{d y}{d x}=\left|\begin{array}{ccc}
f^{\prime}(x) & g^{\prime}(x) & h^{\prime}(x) \\
l & m & n \\
a & b & c
\end{array}\right|+0+0 \Rightarrow \frac{d y}{d x}=\left|\begin{array}{ccc}
f^{\prime}(x) & g^{\prime}(x) & h^{\prime}(x) \\
l & m & n \\
a & b & c
\end{array}\right|
\end{aligned}
$$
:::

:::

:::question{number="22" kind="additional_exercise" id="q_5.9.22" topic="Proving a second-order ODE for an inverse-cosine exponential"}
#### अतिरिक्त प्रश्न 22

:::prompt
यदि $y=e^{a \cos ^{-1} x},-1 \leq x \leq 1$, तो दर्शाइए कि

$$
\left(1-x^{2}\right) \frac{d^{2} y}{d x^{2}}-x \frac{d y}{d x}-a^{2} y=0
$$
:::

:::solution{label="हल"}
दिया है: $y=e^{\mathrm{a} \cos ^{-1} x}$, इसलिए,
दोनों पक्षों का $x$ के सापेक्ष अवकलन करने पर

$$
\begin{aligned}
& \frac{d y}{d x}=\frac{d}{d x} e^{\mathrm{a} \cos ^{-1} x}=e^{\mathrm{a} \cos ^{-1} x} \frac{d}{d x} \mathrm{a}^{-\cos ^{-1} x} \\
& \Rightarrow \frac{d y}{d x}=e^{\mathrm{a} \cos ^{-1} x} a \cdot \frac{-1}{\sqrt{1-x^{2}}}=-\frac{a y}{\sqrt{1-x^{2}}}
\end{aligned}
$$

दोनों ओर वर्ग करने पर

$$
\left(\frac{d y}{d x}\right)^{2}=\frac{a^{2} y^{2}}{1-x^{2}} \quad \Rightarrow\left(1-x^{2}\right)\left(\frac{d y}{d x}\right)^{2}=a^{2} y^{2}
$$

दोनों पक्षों का $x$ के सापेक्ष पुनः अवकलन करने पर

$$
\begin{aligned}
& \left(1-x^{2}\right) \cdot 2 \frac{d y}{d x} \cdot \frac{d^{2} y}{d x^{2}}+\left(\frac{d y}{d x}\right)^{2} \frac{d}{d x}\left(1-x^{2}\right)=a^{2} 2 y \frac{d y}{d x} \\
& \Rightarrow \frac{d y}{d x}\left[2\left(1-x^{2}\right) \frac{d^{2} y}{d x^{2}}+\frac{d y}{d x}(-2 x)\right]=2 a^{2} y \frac{d y}{d x} \\
& \Rightarrow 2 \frac{d y}{d x}\left[\left(1-x^{2}\right) \frac{d^{2} y}{d x^{2}}-x \frac{d y}{d x}\right]=2 a^{2} y \frac{d y}{d x} \\
& \Rightarrow\left(1-x^{2}\right) \frac{d^{2} y}{d x^{2}}-x \frac{d y}{d x}=a^{2} y \\
& \Rightarrow\left(1-x^{2}\right) \frac{d^{2} y}{d x^{2}}-x \frac{d y}{d x}-a^{2} y=0
\end{aligned}
$$
:::

:::
