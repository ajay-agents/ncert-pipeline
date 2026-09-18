---
subject: maths
class: 12
chapter: 2
lang: hi
title: "प्रतिलोम त्रिकोणमितीय फलन"
---

# प्रतिलोम त्रिकोणमितीय फलन

## उदाहरण

:::example{number="2.1" kind="example" id="ex_2.1" topic="sin⁻¹(1/√2) का मुख्य मान" simplified="True"}
#### उदाहरण 2.1

:::prompt
$\sin ^{-1}\left(\frac{1}{\sqrt{2}}\right)$ का मुख्य मान ज्ञात कीजिए।
:::

:::solution{label="हल"}
मान लीजिए कि $\sin ^{-1}\left(\frac{1}{\sqrt{2}}\right)=y$. अतः $\sin y=\frac{1}{\sqrt{2}}$.
हमें ज्ञात है कि $\sin ^{-1}$ की मुख्य शाखा का परिसर $\left(\frac{-\pi}{2}, \frac{\pi}{2}\right)$ होता है और $\sin \left(\frac{\pi}{4}\right)=\frac{1}{\sqrt{2}}$ है। इसलिए $\sin ^{-1}\left(\frac{1}{\sqrt{2}}\right)$ का मुख्य मान $\frac{\pi}{4}$ है।
:::

:::answer
**उत्तर:** $\frac{\pi}{4}$
:::

:::

:::example{number="2.2" kind="example" id="ex_2.2" topic="cot⁻¹(-1/√3) का मुख्य मान" simplified="True"}
#### उदाहरण 2.2

:::prompt
$\cot ^{-1}\left(\frac{-1}{\sqrt{3}}\right)$ का मुख्य मान ज्ञात कीजिए।
:::

:::solution{label="हल"}
मान लीजिए कि $\cot ^{-1}\left(\frac{-1}{\sqrt{3}}\right)=y$. अतएव

$$
\cot y=\frac{-1}{\sqrt{3}}=-\cot \left(\frac{\pi}{3}\right)=\cot \left(\pi-\frac{\pi}{3}\right)=\cot \left(\frac{2 \pi}{3}\right) \text { है। }
$$

हमें ज्ञात है कि $\cot ^{-1}$ की मुख्य शाखा का परिसर $(0, \pi)$ होता है और $\cot \left(\frac{2 \pi}{3}\right)=\frac{-1}{\sqrt{3}}$ है। अत: $\cot ^{-1}\left(\frac{-1}{\sqrt{3}}\right)$ का मुख्य मान $\frac{2 \pi}{3}$ है।
:::

:::answer
**उत्तर:** $\frac{2 \pi}{3}$
:::

:::

:::example{number="2.3" kind="example" id="ex_2.3" topic="sin⁻¹(2x√(1-x²)) के दो रूपांतरण सिद्ध करना" simplified="True"}
#### उदाहरण 2.3

:::prompt
दर्शाइए कि
:::

:::part{label="i"}
:::prompt
$\sin ^{-1}\left(2 x \sqrt{1-x^{2}}\right)=2 \sin ^{-1} x,-\frac{1}{\sqrt{2}} \leq x \leq \frac{1}{\sqrt{2}}$
:::

:::solution
मान लीजिए कि $x=\sin \theta$ तो $\sin ^{-1} x=\theta$ इस प्रकार

$$
\begin{aligned}
\sin ^{-1}\left(2 x \sqrt{1-x^{2}}\right) & =\sin ^{-1}\left(2 \sin \theta \sqrt{1-\sin ^{2} \theta}\right) \\
& =\sin ^{-1}(2 \sin \theta \cos \theta)=\sin ^{-1}(\sin 2 \theta)=2 \theta \\
& =2 \sin ^{-1} x
\end{aligned}
$$
:::

:::

:::part{label="ii"}
:::prompt
$\sin ^{-1}\left(2 x \sqrt{1-x^{2}}\right)=2 \cos ^{-1} x, \frac{1}{\sqrt{2}} \leq x \leq 1$
:::

:::solution
मान लीजिए कि $x=\cos \theta$ है। उसी विधि से $\sin ^{-1}\left(2 x \sqrt{1-x^{2}}\right)=2 \cos ^{-1} x$ मिलता है।
:::

:::

:::

:::example{number="2.4" kind="example" id="ex_2.4" topic="tan⁻¹(cosx/(1-sinx)) को सरलतम रूप में व्यक्त करना" simplified="True"}
#### उदाहरण 2.4

:::prompt
$\tan ^{-1} \frac{\cos x}{1-\sin x},-\frac{-3 \pi}{2}<x<\frac{\pi}{2}$ को सरलतम रूप में व्यक्त कीजिए।
:::

:::solution{label="हल"}
हल हम लिख सकते हैं कि

$$
\begin{aligned}
\tan ^{-1}\left(\frac{\cos x}{1-\sin x}\right) & =\tan ^{-1}\left[\frac{\cos ^{2} \frac{x}{2}-\sin ^{2} \frac{x}{2}}{\cos ^{2} \frac{x}{2}+\sin ^{2} \frac{x}{2}-2 \sin \frac{x}{2} \cos \frac{x}{2}}\right] \\
& =\tan ^{-1}\left[\frac{\left(\cos \frac{x}{2}+\sin \frac{x}{2}\right)\left(\cos \frac{x}{2}-\sin \frac{x}{2}\right)}{\left(\cos \frac{x}{2}-\sin \frac{x}{2}\right)^{2}}\right] \\
& =\tan ^{-1}\left[\frac{\cos \frac{x}{2}+\sin \frac{x}{2}}{\cos \frac{x}{2}-\sin \frac{x}{2}}\right]=\tan ^{-1}\left[\frac{1+\tan \frac{x}{2}}{1-\tan \frac{x}{2}}\right] \\
& =\tan ^{-1}\left[\tan \left(\frac{\pi}{4}+\frac{x}{2}\right)\right]=\frac{\pi}{4}+\frac{x}{2}
\end{aligned}
$$
:::

:::answer
**उत्तर:** $\frac{\pi}{4}+\frac{x}{2}$
:::

:::

:::example{number="2.5" kind="example" id="ex_2.5" topic="cot⁻¹(1/√(x²-1)) को सरलतम रूप में लिखना" simplified="True"}
#### उदाहरण 2.5

:::prompt
$\cot ^{-1}\left(\frac{1}{\sqrt{x^{2}-1}}\right), x>1$ को सरलतम रूप में लिखिए।
:::

:::solution{label="हल"}
मान लीजिए कि $x=\sec \theta$, then $\sqrt{x^{2}-1}=\sqrt{\sec ^{2} \theta-1}=\tan \theta$

इसलिए $\cot ^{-1} \frac{1}{\sqrt{x^{2}-1}}=\cot ^{-1}(\cot \theta)=\theta=\sec ^{-1} x$ जो अभीष्ट सरलतम रूप है।
:::

:::answer
**उत्तर:** $\sec ^{-1} x$
:::

:::

:::example{number="2.6" kind="example" id="ex_2.6" topic="sin⁻¹(sin(3π/5)) का मान (विविध उदाहरण)" simplified="True"}
#### उदाहरण 2.6

:::prompt
$\sin ^{-1}\left(\sin \frac{3 \pi}{5}\right)$ का मान ज्ञात कीजिए।
:::

:::solution{label="हल"}
हमें ज्ञात है कि $\sin ^{-1}(\sin x)=x$ होता है। इसलिए $\sin ^{-1}\left(\sin \frac{3 \pi}{5}\right)=\frac{3 \pi}{5}$
किंतु $\frac{3 \pi}{5} \notin\left[-\frac{\pi}{2}, \frac{\pi}{2}\right]$, जो $\sin ^{-1} x$ की मुख्य शाखा है।
फिर भी $\sin \left(\frac{3 \pi}{5}\right)=\sin \left(\pi-\frac{3 \pi}{5}\right)=\sin \frac{2 \pi}{5}$ तथा $\frac{2 \pi}{5} \in\left[-\frac{\pi}{2}, \frac{\pi}{2}\right]$
अत:

$$
\sin ^{-1}\left(\sin \frac{3 \pi}{5}\right)=\sin ^{-1}\left(\sin \frac{2 \pi}{5}\right)=\frac{2 \pi}{5}
$$
:::

:::answer
**उत्तर:** $\frac{2 \pi}{5}$
:::

:::

## प्रश्न और हल

:::question{number="2.1.1" kind="exercise" id="q_2.1.1" topic="sin⁻¹(-1/2) का मुख्य मान" simplified="True"}
#### प्रश्न 2.1.1

:::prompt
$\sin ^{-1}\left(-\frac{1}{2}\right)$
:::

:::solution{label="हल"}
माना, $\sin ^{-1}\left(-\frac{1}{2}\right)=y$, इसलिए, $\sin y=-\frac{1}{2}=-\sin \left(\frac{\pi}{6}\right)=\sin \left(-\frac{\pi}{6}\right)$
हम जानते हैं कि $\sin ^{-1}$ की मुख्य शाखा का परिसर $\left[-\frac{\pi}{2}, \frac{\pi}{2}\right]$ होता है और $\sin \left(-\frac{\pi}{6}\right)=-\frac{1}{2}$ है। अतः, $\sin ^{-1}\left(-\frac{1}{2}\right)$ का मुख्य मान $-\frac{\pi}{6}$ है।
:::

:::answer
**उत्तर:** $-\frac{\pi}{6}$
:::

:::

:::question{number="2.1.2" kind="exercise" id="q_2.1.2" topic="cos⁻¹(√3/2) का मुख्य मान" simplified="True"}
#### प्रश्न 2.1.2

:::prompt
$\cos ^{-1}\left(\frac{\sqrt{3}}{2}\right)$
:::

:::solution{label="हल"}
माना, $\cos ^{-1}\left(\frac{\sqrt{3}}{2}\right)=y$, इसलिए, $\cos y=\frac{\sqrt{3}}{2}=\cos \left(\frac{\pi}{6}\right)$
हम जानते हैं कि $\cos ^{-1}$ की मुख्य शाखा का परिसर $[0, \pi]$ होता है और $\cos \left(\frac{\pi}{6}\right)=\frac{\sqrt{3}}{2}$ है। अतः, $\cos ^{-1}\left(\frac{\sqrt{3}}{2}\right)$ का मुख्य मान $\frac{\pi}{6}$ है।
:::

:::answer
**उत्तर:** $\frac{\pi}{6}$
:::

:::

:::question{number="2.1.3" kind="exercise" id="q_2.1.3" topic="cosec⁻¹(2) का मुख्य मान" simplified="True"}
#### प्रश्न 2.1.3

:::prompt
$\operatorname{cosec}^{-1}(2)$
:::

:::solution{label="हल"}
माना, $\operatorname{cosec}^{-1}(2)=y$. इसलिए,, $\operatorname{cosec} \mathrm{y}=2=\operatorname{cosec}\left(\frac{\pi}{6}\right)$
हम जानते हैं कि $\operatorname{cosec}^{-1}$ की मुख्य शाखा का परिसर $\left[-\frac{\pi}{2}, \frac{\pi}{2}\right]-\{0\}$ होता है और $\operatorname{cosec}\left(\frac{\pi}{6}\right)=$ $2$ है। अतः, $\operatorname{cosec}^{-1}(2)$ का मुख्य मान $\frac{\pi}{6}$ है।
:::

:::answer
**उत्तर:** $\frac{\pi}{6}$
:::

:::

:::question{number="2.1.4" kind="exercise" id="q_2.1.4" topic="tan⁻¹(-√3) का मुख्य मान" simplified="True"}
#### प्रश्न 2.1.4

:::prompt
$\tan ^{-1}(-\sqrt{3})$
:::

:::solution{label="हल"}
माना, $\tan ^{-1}(-\sqrt{3})=\mathrm{y}$, इसलिए, $\tan \mathrm{y}=-\sqrt{3}=-\tan \frac{\pi}{3}=\tan \left(-\frac{\pi}{3}\right)$
हम जानते हैं कि $\tan ^{-1}$ की मुख्य शाखा का परिसर $\left(-\frac{\pi}{2}, \frac{\pi}{2}\right)$ होता है और $\tan \left(-\frac{\pi}{3}\right)=-\sqrt{3}$ है। अतः, $\tan ^{-1}(-\sqrt{3})$ का मुख्य मान $-\frac{\pi}{3}$ है।
:::

:::answer
**उत्तर:** $-\frac{\pi}{3}$
:::

:::

:::question{number="2.1.5" kind="exercise" id="q_2.1.5" topic="cos⁻¹(-1/2) का मुख्य मान" simplified="True"}
#### प्रश्न 2.1.5

:::prompt
$\cos ^{-1}\left(-\frac{1}{2}\right)$
:::

:::solution{label="हल"}
माना, $\cos ^{-1}\left(-\frac{1}{2}\right)=\mathrm{y}$, इसलिए, $\cos \mathrm{y}=-\frac{1}{2}=-\cos \frac{\pi}{3}=\cos \left(\pi-\frac{\pi}{3}\right)=\cos \left(\frac{2 \pi}{3}\right)$
हम जानते हैं कि $\cos ^{-1}$ की मुख्य शाखा का परिसर $[0, \pi]$ होता है और $\cos \left(\frac{2 \pi}{3}\right)=-\frac{1}{2}$ है। अतः, $\cos ^{-1}\left(-\frac{1}{2}\right)$ का मुख्य मान $\frac{2 \pi}{3}$ है।
:::

:::answer
**उत्तर:** $\frac{2 \pi}{3}$
:::

:::

:::question{number="2.1.6" kind="exercise" id="q_2.1.6" topic="tan⁻¹(-1) का मुख्य मान" simplified="True"}
#### प्रश्न 2.1.6

:::prompt
$\tan ^{-1}(-1)$
:::

:::solution{label="हल"}
माना, $\tan ^{-1}(-1)=\mathrm{y}$. इसलिए, $\tan \mathrm{y}=-1=-\tan \left(\frac{\pi}{4}\right)=\tan \left(-\frac{\pi}{4}\right)$
हम जानते हैं कि $\tan ^{-1}$ की मुख्य शाखा का परिसर $\left(-\frac{\pi}{2}, \frac{\pi}{2}\right)$ होता है और $\tan \left(-\frac{\pi}{4}\right)=-1$ है। अतः, $\tan ^{-1}(-1)$ का मुख्य मान $-\frac{\pi}{4}$ है।
:::

:::answer
**उत्तर:** $-\frac{\pi}{4}$
:::

:::

:::question{number="2.1.7" kind="exercise" id="q_2.1.7" topic="sec⁻¹(2/√3) का मुख्य मान" simplified="True"}
#### प्रश्न 2.1.7

:::prompt
$\sec ^{-1}\left(\frac{2}{\sqrt{3}}\right)$
:::

:::solution{label="हल"}
माना, $\sec ^{-1}\left(\frac{2}{\sqrt{3}}\right)=y$, इसलिए, $\sec y=\frac{2}{\sqrt{3}}=\sec \left(\frac{\pi}{6}\right)$
हम जानते हैं कि $\sec ^{-1}$ की मुख्य शाखा का परिसर $[0, \pi]-\left\{\frac{\pi}{2}\right\}$ होता है और $\sec \left(\frac{\pi}{6}\right)=\frac{2}{\sqrt{3}}$ है। अतः, $\sec ^{-1}\left(\frac{2}{\sqrt{3}}\right)$ का मुख्य मान $\frac{\pi}{6}$ है।
:::

:::answer
**उत्तर:** $\frac{\pi}{6}$
:::

:::

:::question{number="2.1.8" kind="exercise" id="q_2.1.8" topic="cot⁻¹(√3) का मुख्य मान" simplified="True"}
#### प्रश्न 2.1.8

:::prompt
$\cot ^{-1}(\sqrt{3})$
:::

:::solution{label="हल"}
माना, $\cot ^{-1} \sqrt{3}=\mathrm{y}$, इसलिए, $\cot \mathrm{y}=\sqrt{3}=\cot \left(\frac{\pi}{6}\right)$.
हम जानते हैं कि $\cot ^{-1}$ की मुख्य शाखा का परिसर $(0, \pi)$ होता है और $\cot \left(\frac{\pi}{6}\right)=\sqrt{3}$ है। अतः, $\cot ^{-1} \sqrt{3}$ का मुख्य मान $\frac{\pi}{6}$ है।
:::

:::answer
**उत्तर:** $\frac{\pi}{6}$
:::

:::

:::question{number="2.1.9" kind="exercise" id="q_2.1.9" topic="cos⁻¹(-1/√2) का मुख्य मान" simplified="True"}
#### प्रश्न 2.1.9

:::prompt
$\cos ^{-1}\left(-\frac{1}{\sqrt{2}}\right)$
:::

:::solution{label="हल"}
माना, $\cos ^{-1}\left(-\frac{1}{\sqrt{2}}\right)=\mathrm{y}$, इसलिए, $\cos \mathrm{y}=-\frac{1}{\sqrt{2}}=-\cos \left(\frac{\pi}{4}\right)=\cos \left(\pi-\frac{\pi}{4}\right)=\cos \left(\frac{3 \pi}{4}\right)$.
हम जानते हैं कि $\cos ^{-1}$ की मुख्य शाखा का परिसर $[0, \pi]$ होता है और $\cos \left(\frac{3 \pi}{4}\right)=-\frac{1}{\sqrt{2}}$ है। अतः, $\cos ^{-1}\left(-\frac{1}{\sqrt{2}}\right)$ का मुख्य मान $\frac{3 \pi}{4}$ है।
:::

:::answer
**उत्तर:** $\frac{3 \pi}{4}$
:::

:::

:::question{number="2.1.10" kind="exercise" id="q_2.1.10" topic="cosec⁻¹(-√2) का मुख्य मान" simplified="True"}
#### प्रश्न 2.1.10

:::prompt
$\operatorname{cosec}^{-1}(-\sqrt{2})$
:::

:::solution{label="हल"}
माना, $\operatorname{cosec}^{-1}(-\sqrt{2})=y$, इसलिए, $\operatorname{cosec} y=-\sqrt{2}=-\operatorname{cosec}\left(\frac{\pi}{4}\right)=\operatorname{cosec}\left(-\frac{\pi}{4}\right)$
हम जानते हैं कि $\operatorname{cosec}^{-1}$ की मुख्य शाखा का परिसर $\left[-\frac{\pi}{2}, \frac{\pi}{2}\right]-\{0\}$ होता है और $\operatorname{cosec}\left(-\frac{\pi}{4}\right)=-\sqrt{2}$ है। अतः, $\operatorname{cosec}^{-1}(-\sqrt{2})$ का मुख्य मान $-\frac{\pi}{4}$ है।
:::

:::answer
**उत्तर:** $-\frac{\pi}{4}$
:::

:::

:::question{number="2.1.11" kind="exercise" id="q_2.1.11" topic="tan⁻¹1+cos⁻¹(-1/2)+sin⁻¹(-1/2) का मान" simplified="True"}
#### प्रश्न 2.1.11

:::prompt
$\tan ^{-1}(1)+\cos ^{-1}\left(-\frac{1}{2}\right)+\sin ^{-1}\left(-\frac{1}{2}\right)$
:::

:::solution{label="हल"}
माना, $\tan ^{-1}(1)=x$, इसलिए, $\tan x=1=\tan \frac{\pi}{4}$
हम जानते हैं कि $\tan ^{-1}$ की मुख्य शाखा का परिसर $\left(-\frac{\pi}{2}, \frac{\pi}{2}\right)$ होता है। $\therefore \tan ^{-1}(1)=\frac{\pi}{4}$
माना, $\cos ^{-1}\left(-\frac{1}{2}\right)=y$, इसलिए,

$$
\cos y=-\frac{1}{2}=-\cos \frac{\pi}{3}=\cos \left(\pi-\frac{\pi}{3}\right)=\cos \left(\frac{2 \pi}{3}\right)
$$

हम जानते हैं कि $\cos ^{-1}$ की मुख्य शाखा का परिसर $[0, \pi]$ होता है। $\therefore \cos ^{-1}\left(-\frac{1}{2}\right)=\frac{2 \pi}{3}$
माना, $\sin ^{-1}\left(-\frac{1}{2}\right)=z$, इसलिए,

$$
\sin z=-\frac{1}{2}=-\sin \frac{\pi}{6}=\sin \left(-\frac{\pi}{6}\right)
$$

हम जानते हैं कि $\sin ^{-1}$ की मुख्य शाखा का परिसर $\left[-\frac{\pi}{2}, \frac{\pi}{2}\right]$ होता है। $\therefore \sin ^{-1}\left(-\frac{1}{2}\right)=-\frac{\pi}{6}$
अब, $\tan ^{-1}(1)+\cos ^{-1}\left(-\frac{1}{2}\right)+\sin ^{-1}\left(-\frac{1}{2}\right)$

$$
=\frac{\pi}{4}+\frac{2 \pi}{3}-\frac{\pi}{6}=\frac{3 \pi+8 \pi-2 \pi}{12}=\frac{9 \pi}{12}=\frac{3 \pi}{4}
$$
:::

:::answer
**उत्तर:** $\frac{3 \pi}{4}$
:::

:::

:::question{number="2.1.12" kind="exercise" id="q_2.1.12" topic="cos⁻¹(1/2)+2sin⁻¹(1/2) का मान" simplified="True" corrections_applied="1"}
#### प्रश्न 2.1.12

:::prompt
$\cos ^{-1}\left(\frac{1}{2}\right)+2 \sin ^{-1}\left(\frac{1}{2}\right)$
:::

:::solution{label="हल"}
माना, $\cos ^{-1}\left(\frac{1}{2}\right)=x$, इसलिए,

$$
\cos x=\frac{1}{2}=\cos \frac{\pi}{3}
$$

हम जानते हैं कि $\cos ^{-1}$ की मुख्य शाखा का परिसर $[0, \pi]$ होता है। $\therefore \cos ^{-1}\left(\frac{1}{2}\right)=\frac{\pi}{3}$
माना, $\sin ^{-1}\left(\frac{1}{2}\right)=\mathrm{y}$, इसलिए,

$$
\sin y=\frac{1}{2}=\sin \frac{\pi}{6}
$$

हम जानते हैं कि $\sin ^{-1}$ की मुख्य शाखा का परिसर $\left[-\frac{\pi}{2}, \frac{\pi}{2}\right]$ होता है। $\therefore \sin ^{-1}\left(\frac{1}{2}\right)=\frac{\pi}{6}$ अब, $\cos ^{-1}\left(\frac{1}{2}\right)+2 \sin ^{-1}\left(\frac{1}{2}\right)=\frac{\pi}{3}+2 \times \frac{\pi}{6}=\frac{\pi}{3}+\frac{\pi}{3}=\frac{2 \pi}{3}$.
:::

:::answer
**उत्तर:** $\frac{2 \pi}{3}$
:::

:::

:::question{number="2.1.13" kind="exercise" id="q_2.1.13" topic="MCQ — sin⁻¹x=y का परिसर" simplified="True"}
#### प्रश्न 2.1.13

:::prompt
यदि $\sin ^{-1} x=y$, तो
(A) $0 \leq y \leq \pi$
(B) $-\frac{\pi}{2} \leq y \leq \frac{\pi}{2}$
(C) $0<y<\pi$
(D) $-\frac{\pi}{2}<y<\frac{\pi}{2}$
:::

:::solution{label="हल"}
दिया है: $\sin ^{-1} x=y$
हम जानते हैं कि $\sin ^{-1}$ की मुख्य शाखा का परिसर $\left[-\frac{\pi}{2}, \frac{\pi}{2}\right]$ होता है। इसलिए, $-\frac{\pi}{2} \leq \mathrm{y} \leq \frac{\pi}{2}$. अतः, विकल्प (B) सही है।
:::

:::answer
**उत्तर:** (B)
:::

:::

:::question{number="2.1.14" kind="exercise" id="q_2.1.14" topic="MCQ — tan⁻¹√3-sec⁻¹(-2) का मान" simplified="True"}
#### प्रश्न 2.1.14

:::prompt
$\tan ^{-1} \sqrt{3}-\sec ^{-1}(-2)$ का मान बराबर है
(A) $\pi$
(B) $-\frac{\pi}{3}$
(C) $\frac{\pi}{3}$
(D) $\frac{2 \pi}{3}$
:::

:::solution{label="हल"}
माना, $\tan ^{-1} \sqrt{3}=x$, इसलिए,

$$
\tan x=\sqrt{3}=\tan \frac{\pi}{3}
$$

हम जानते हैं कि $\tan ^{-1}$ की मुख्य शाखा का परिसर $\left(-\frac{\pi}{2}, \frac{\pi}{2}\right)$ होता है। $\therefore \tan ^{-1} \sqrt{3}=\frac{\pi}{3}$ माना, $\sec ^{-1}(-2)=\mathrm{y}$, इसलिए,

$$
\sec y=-2=-\sec \frac{\pi}{3}=\sec \left(\pi-\frac{\pi}{3}\right)=\sec \left(\frac{2 \pi}{3}\right)
$$

हम जानते हैं कि $\sec ^{-1}$ की मुख्य शाखा का परिसर $[0, \pi]-\left\{\frac{\pi}{2}\right\}$ होता है। $\therefore \sec ^{-1}(-2)=\frac{2 \pi}{3}$ अब,

$$
\tan ^{-1} \sqrt{3}-\sec ^{-1}(-2)=\frac{\pi}{3}-\frac{2 \pi}{3}=-\frac{\pi}{3}
$$

अतः, विकल्प (B) सही है।
:::

:::answer
**उत्तर:** (B)
:::

:::

:::question{number="2.2.1" kind="exercise" id="q_2.2.1" topic="सिद्ध — 3sin⁻¹x=sin⁻¹(3x-4x³)" simplified="True"}
#### प्रश्न 2.2.1

:::prompt
$3 \sin ^{-1} x=\sin ^{-1}\left(3 x-4 x^{3}\right), x \in\left[-\frac{1}{2}, \frac{1}{2}\right]$
:::

:::solution{label="हल"}
माना, $\sin ^{-1} x=\theta$, तब $x=\sin \theta$ है। अतः,

$$
\begin{aligned}
\mathrm{RHS} & =\sin ^{-1}\left(3 x-4 x^{3}\right)=\sin ^{-1}\left(3 \sin \theta-4 \sin ^{3} \theta\right) \\
& =\sin ^{-1}(\sin 3 \theta)=3 \theta=3 \sin ^{-1} x=\mathrm{LHS}
\end{aligned}
$$
:::

:::

:::question{number="2.2.2" kind="exercise" id="q_2.2.2" topic="सिद्ध — 3cos⁻¹x=cos⁻¹(4x³-3x)" simplified="True"}
#### प्रश्न 2.2.2

:::prompt
$3 \cos ^{-1} x=\cos ^{-1}\left(4 x^{3}-3 x\right), x \in\left[\frac{1}{2}, 1\right]$
:::

:::solution{label="हल"}
माना, $\cos ^{-1} x=\theta$, तब $x=\cos \theta$ है। अतः,

$$
\begin{aligned}
\mathrm{RHS} & =\cos ^{-1}\left(4 x^{3}-3 x\right)=\cos ^{-1}\left(4 \cos ^{3} \theta-3 \cos \theta\right) \\
& =\cos ^{-1}(\cos 3 \theta)=3 \theta=3 \cos ^{-1} x=\mathrm{LHS}
\end{aligned}
$$
:::

:::

:::question{number="2.2.3" kind="exercise" id="q_2.2.3" topic="सरलतम रूप — tan⁻¹((√(1+x²)-1)/x)" simplified="True"}
#### प्रश्न 2.2.3

:::prompt
$\tan ^{-1} \frac{\sqrt{1+x^{2}}-1}{x}, x \neq 0$
:::

:::solution{label="हल"}
दिया है: $\tan ^{-1} \frac{\sqrt{1+x^{2}}-1}{x}$
माना, $x=\tan \theta$

$$
\begin{aligned}
& \therefore \tan ^{-1} \frac{\sqrt{1+x^{2}}-1}{x}=\tan ^{-1} \frac{\sqrt{1+\tan ^{2} \theta}-1}{\tan \theta} \\
& =\tan ^{-1}\left(\frac{\sec \theta-1}{\tan \theta}\right)=\tan ^{-1}\left(\frac{1-\cos \theta}{\sin \theta}\right) \\
& =\tan ^{-1}\left(\frac{2 \sin ^{2} \frac{\theta}{2}}{2 \sin \frac{\theta}{2} \cos \frac{\theta}{2}}\right)=\tan ^{-1}\left(\tan \frac{\theta}{2}\right) \\
& =\frac{\theta}{2}=\frac{1}{2} \tan ^{-1} x
\end{aligned}
$$
:::

:::answer
**उत्तर:** $\frac{1}{2} \tan ^{-1} x$
:::

:::

:::question{number="2.2.4" kind="exercise" id="q_2.2.4" topic="सरलतम रूप — tan⁻¹(√((1-cosx)/(1+cosx)))" simplified="True"}
#### प्रश्न 2.2.4

:::prompt
$\tan ^{-1}\left(\sqrt{\frac{1-\cos x}{1+\cos x}}\right), 0<x<\pi$
:::

:::solution{label="हल"}
दिया है: $\tan ^{-1}\left(\sqrt{\frac{1-\cos x}{1+\cos x}}\right)=\tan ^{-1}\left(\sqrt{\frac{2 \sin ^{2} \frac{x}{2}}{2 \cos ^{2} \frac{x}{2}}}\right)$

$$
=\tan ^{-1}\left(\sqrt{\tan ^{2} \frac{x}{2}}\right)=\tan ^{-1}\left(\tan \frac{x}{2}\right)=\frac{x}{2}
$$
:::

:::answer
**उत्तर:** $\frac{x}{2}$
:::

:::

:::question{number="2.2.5" kind="exercise" id="q_2.2.5" topic="सरलतम रूप — tan⁻¹((cosx-sinx)/(cosx+sinx))" simplified="True"}
#### प्रश्न 2.2.5

:::prompt
$\tan ^{-1}\left(\frac{\cos x-\sin x}{\cos x+\sin x}\right), \frac{-\pi}{4}<x<\frac{3 \pi}{4}$
:::

:::solution{label="हल"}
दिया है: $\tan ^{-1}\left(\frac{\cos x-\sin x}{\cos x+\sin x}\right)$

$$
\begin{aligned}
& \tan ^{-1}\left(\frac{\cos x-\sin x}{\cos x+\sin x}\right)=\tan ^{-1}\left(\frac{1-\frac{\sin x}{\cos x}}{1+\frac{\sin x}{\cos x}}\right)=\tan ^{-1}\left(\frac{1-\tan x}{1+\tan x}\right) \\
& =\tan ^{-1}\left(\frac{1-\tan x}{1+1 \cdot \tan x}\right)=\tan ^{-1}\left(\frac{\tan \frac{\pi}{4}-\tan x}{1+\tan \frac{\pi}{4} \cdot \tan x}\right) \\
& =\tan ^{-1}\left[\tan \left(\frac{\pi}{4}-x\right)\right]=\frac{\pi}{4}-x
\end{aligned}
$$
:::

:::answer
**उत्तर:** $\frac{\pi}{4}-x$
:::

:::

:::question{number="2.2.6" kind="exercise" id="q_2.2.6" topic="सरलतम रूप — tan⁻¹(x/√(a²-x²))" simplified="True"}
#### प्रश्न 2.2.6

:::prompt
$\tan ^{-1} \frac{x}{\sqrt{a^{2}-x^{2}}},|x|<a$
:::

:::solution{label="हल"}
दिया है: $\tan ^{-1} \frac{x}{\sqrt{a^{2}-x^{2}}}$.
माना, $x=\mathrm{a} \sin \theta$

$$
\begin{aligned}
& \therefore \tan ^{-1} \frac{x}{\sqrt{a^{2}-x^{2}}}=\tan ^{-1}\left(\frac{a \sin \theta}{\sqrt{a^{2}-a^{2} \sin ^{2} \theta}}\right)=\tan ^{-1}\left(\frac{a \sin \theta}{a \sqrt{1-\sin ^{2} \theta}}\right) \\
& =\tan ^{-1}\left(\frac{a \sin \theta}{a \sin \theta}\right)=\tan ^{-1}(\tan \theta)=\bar{\theta}=\sin ^{-1} \frac{x}{a}
\end{aligned}
$$
:::

:::answer
**उत्तर:** $\sin ^{-1} \frac{x}{a}$
:::

:::

:::question{number="2.2.7" kind="exercise" id="q_2.2.7" topic="सरलतम रूप — tan⁻¹((3a²x-x³)/(a³-3ax²))" simplified="True"}
#### प्रश्न 2.2.7

:::prompt
$\tan ^{-1}\left(\frac{3 a^{2} x-x^{3}}{a^{3}-3 a x^{2}}\right), a>0 ; \frac{-a}{\sqrt{3}}<x<\frac{a}{\sqrt{3}}$
:::

:::solution{label="हल"}
दिया है: $\tan ^{-1}\left(\frac{3 a^{2} x-x^{3}}{a^{3}-3 a x^{2}}\right)$
माना, $x=a \tan \theta$

$$
\begin{aligned}
& \therefore \tan ^{-1}\left(\frac{3 a^{2} x-x^{3}}{a^{3}-3 a x^{2}}\right)=\tan ^{-1}\left(\frac{3 a^{2} \cdot a \tan \theta-a^{3} \tan ^{3} \theta}{a^{3}-3 a \cdot a^{2} \tan ^{2} \theta}\right) \\
& =\tan ^{-1}\left(\frac{3 a^{3} \tan \theta-a^{3} \tan ^{3} \theta}{a^{3}-3 a^{3} \tan ^{2} \theta}\right) \\
& =\tan ^{-1}\left(\frac{3 \tan \theta-\tan ^{3} \theta}{1-3 \tan ^{2} \theta}\right) \\
& =\tan ^{-1}(\tan 3 \theta)=3 \theta \\
& =3 \tan ^{-1} \frac{x}{a}
\end{aligned}
$$
:::

:::answer
**उत्तर:** $3 \tan ^{-1} \frac{x}{a}$
:::

:::

:::question{number="2.2.8" kind="exercise" id="q_2.2.8" topic="मान — tan⁻¹[2cos(2sin⁻¹(1/2))]" simplified="True"}
#### प्रश्न 2.2.8

:::prompt
$\tan ^{1}\left[2 \cos \left(2 \sin ^{1} \frac{1}{2}\right)\right]$
:::

:::solution{label="हल"}
दिया है: $\tan ^{-1}\left[2 \cos \left(2 \sin ^{-1} \frac{1}{2}\right)\right]$

$$
\begin{aligned}
& \therefore \tan ^{-1}\left[2 \cos \left(2 \sin ^{-1} \frac{1}{2}\right)\right]=\tan ^{-1}\left[2 \cos \left(2 \sin ^{-1}\left(\sin \frac{\pi}{6}\right)\right)\right] \\
& =\tan ^{-1}\left[2 \cos \left(2 \times \frac{\pi}{6}\right)\right]=\tan ^{-1}\left[2 \cos \left(\frac{\pi}{3}\right)\right]=\tan ^{-1}\left[2 \times \frac{1}{2}\right] \\
& =\tan ^{-1}[1]=\frac{\pi}{4}
\end{aligned}
$$
:::

:::answer
**उत्तर:** $\frac{\pi}{4}$
:::

:::

:::question{number="2.2.9" kind="exercise" id="q_2.2.9" topic="मान — tan(1/2)[sin⁻¹(2x/(1+x²))+cos⁻¹((1-y²)/(1+y²))]" simplified="True"}
#### प्रश्न 2.2.9

:::prompt
$\tan \frac{1}{2}\left[\sin ^{-1} \frac{2 x}{1+x^{2}}+\cos ^{-1} \frac{1-y^{2}}{1+y^{2}}\right],|x|<1, y>0$ तथा $x y<1$
:::

:::solution{label="हल"}
दिया है: $\tan \frac{1}{2}\left[\sin ^{-1} \frac{2 x}{1+x^{2}}+\cos ^{-1} \frac{1-y^{2}}{1+y^{2}}\right]$

$$
\begin{aligned}
& =\tan \frac{1}{2}\left[2 \tan ^{-1} x+2 \tan ^{-1} y\right] \quad\left[\because 2 \tan ^{-1} x=\sin ^{-1} \frac{2 x}{1+x^{2}}=\cos ^{-1} \frac{1-x^{2}}{1+x^{2}}\right] \\
& =\tan \frac{1}{2}\left[2\left(\tan ^{-1} x+\tan ^{-1} y\right)\right]=\tan \left[\tan ^{-1} x+\tan ^{-1} y\right] \\
& =\tan \left[\tan ^{-1} \frac{x+y}{1-x y}\right]=\frac{x+y}{1-x y}
\end{aligned}
$$
:::

:::answer
**उत्तर:** $\frac{x+y}{1-x y}$
:::

:::

:::question{number="2.2.10" kind="exercise" id="q_2.2.10" topic="मान — sin⁻¹(sin(2π/3))" simplified="True"}
#### प्रश्न 2.2.10

:::prompt
$\sin ^{-1}\left(\sin \frac{2 \pi}{3}\right)$
:::

:::solution{label="हल"}
दिया है: $\sin ^{-1}\left(\sin \frac{2 \pi}{3}\right)$.
हम जानते हैं कि $\sin ^{-1}$ की मुख्य शाखा का परिसर $\left[-\frac{\pi}{2}, \frac{\pi}{2}\right]$ होता है।

$$
\therefore \sin ^{-1}\left(\sin \frac{2 \pi}{3}\right)=\sin ^{-1}\left(\sin \left\{\pi-\frac{\pi}{3}\right\}\right)=\sin ^{-1}\left(\sin \frac{\pi}{3}\right)=\frac{\pi}{3} \in\left[-\frac{\pi}{2}, \frac{\pi}{2}\right]
$$

अतः, $\sin ^{-1}\left(\sin \frac{2 \pi}{3}\right)=\frac{\pi}{3}$
:::

:::answer
**उत्तर:** $\frac{\pi}{3}$
:::

:::

:::question{number="2.2.11" kind="exercise" id="q_2.2.11" topic="मान — tan⁻¹(tan(3π/4))" simplified="True"}
#### प्रश्न 2.2.11

:::prompt
$\tan ^{-1}\left(\tan \frac{3 \pi}{4}\right)$
:::

:::solution{label="हल"}
दिया है: $\tan ^{-1}\left(\tan \frac{3 \pi}{4}\right)$
हम जानते हैं कि $\tan ^{-1}$ की मुख्य शाखा का परिसर $\left(-\frac{\pi}{2}, \frac{\pi}{2}\right)$ होता है।

$$
\begin{aligned}
& \therefore \tan ^{-1}\left(\tan \frac{3 \pi}{4}\right)=\tan ^{-1}\left(\tan \left\{\pi-\frac{\pi}{4}\right\}\right)=\tan ^{-1}\left(-\tan \frac{\pi}{4}\right) \\
& =\tan ^{-1}\left(\tan \left\{-\frac{\pi}{4}\right\}\right)=-\frac{\pi}{4} \in\left(-\frac{\pi}{2}, \frac{\pi}{2}\right)
\end{aligned}
$$

अतः, $\tan ^{-1}\left(\tan \frac{3 \pi}{4}\right)=-\frac{\pi}{4}$
:::

:::answer
**उत्तर:** $-\frac{\pi}{4}$
:::

:::

:::question{number="2.2.12" kind="exercise" id="q_2.2.12" topic="मान — tan(sin⁻¹(3/5)+cot⁻¹(3/2))" simplified="True"}
#### प्रश्न 2.2.12

:::prompt
$\tan \left(\sin ^{-1} \frac{3}{5}+\cot ^{-1} \frac{3}{2}\right)$
:::

:::solution{label="हल"}
दिया है: $\tan \left(\sin ^{-1} \frac{3}{5}+\cot ^{-1} \frac{3}{2}\right)$

$$
\begin{aligned}
& \therefore \tan \left(\sin ^{-1} \frac{3}{5}+\cot ^{-1} \frac{3}{2}\right)=\tan \left(\tan ^{-1} \frac{3}{\sqrt{5^{2}-3^{2}}}+\tan ^{-1} \frac{2}{3}\right) \\
& \quad\left[\because \sin ^{-1} \frac{a}{b}=\tan ^{-1} \frac{a}{\sqrt{b^{2}-a^{2}}} \text { तथा } \cot ^{-1} \frac{a}{b}=\tan ^{-1} \frac{b}{a}\right] \\
& =\tan \left(\tan ^{-1} \frac{3}{4}+\tan ^{-1} \frac{2}{3}\right) \\
& =\tan \left[\tan ^{-1}\left(\frac{\frac{3}{4}+\frac{2}{3}}{1-\frac{3}{4} \times \frac{2}{3}}\right)\right] \\
& =\tan \left[\tan ^{-1}\left(\frac{\frac{9+8}{4 \times 3}}{\frac{4 \times 3-3 \times 2}{4 \times 3}}\right)\right] \\
& =\tan \left(\tan ^{-1} \frac{17}{6}\right)=\frac{17}{6}
\end{aligned}
$$
:::

:::answer
**उत्तर:** $\frac{17}{6}$
:::

:::

:::question{number="2.2.13" kind="exercise" id="q_2.2.13" topic="MCQ — cos⁻¹(cos(7π/6)) का मान" simplified="True"}
#### प्रश्न 2.2.13

:::prompt
$\cos ^{-1}\left(\cos \frac{7 \pi}{6}\right)$ का मान बराबर है
(A) $\frac{7 \pi}{6}$
(B) $\frac{5 \pi}{6}$
(C) $\frac{\pi}{3}$
(D) $\frac{\pi}{6}$
:::

:::solution{label="हल"}
दिया है: $\cos ^{-1}\left(\cos \frac{7 \pi}{6}\right)$
हम जानते हैं कि $\cos ^{-1}$ की मुख्य शाखा का परिसर $[0, \pi]$ होता है।

$$
\begin{aligned}
& \therefore \cos ^{-1}\left(\cos \frac{7 \pi}{6}\right) \\
& =\cos ^{-1}\left[\cos \left(2 \pi-\frac{5 \pi}{6}\right)\right] \\
& =\cos ^{-1}\left(\cos \frac{5 \pi}{6}\right) \\
& =\frac{5 \pi}{6} \in[0, \pi]
\end{aligned}
$$

इसलिए, $\cos ^{-1}\left(\cos \frac{7 \pi}{6}\right)=\frac{5 \pi}{6}$
अतः, विकल्प (B) सही है।
:::

:::answer
**उत्तर:** (B)
:::

:::

:::question{number="2.2.14" kind="exercise" id="q_2.2.14" topic="MCQ — sin(π/3-sin⁻¹(-1/2)) का मान" simplified="True"}
#### प्रश्न 2.2.14

:::prompt
$\sin \left(\frac{\pi}{3}-\sin ^{-1}\left(-\frac{1}{2}\right)\right)$ का मान है
(A) $\frac{1}{2}$ है
(B) $\frac{1}{3}$ है
(C) $\frac{1}{4}$ है
(D) $1$
:::

:::solution{label="हल"}
दिया है: $\sin \left(\frac{\pi}{3}-\sin ^{-1}\left(-\frac{1}{2}\right)\right)$
हम जानते हैं कि $\sin ^{-1}$ की मुख्य शाखा का परिसर $\left[-\frac{\pi}{2}, \frac{\pi}{2}\right]$ होता है।

$$
\begin{aligned}
& \therefore \sin \left(\frac{\pi}{3}-\sin ^{-1}\left(-\frac{1}{2}\right)\right) \\
& =\sin \left[\frac{\pi}{3}-\sin ^{-1}\left(-\sin \frac{\pi}{6}\right)\right] \\
& =\sin \left[\frac{\pi}{3}-\sin ^{-1}\left\{\sin \left(-\frac{\pi}{6}\right)\right\}\right] \\
& =\sin \left(\frac{\pi}{3}+\frac{\pi}{6}\right)=\sin \left(\frac{3 \pi}{6}\right) \\
& =\sin \frac{\pi}{2}=1
\end{aligned}
$$

इसलिए, $\sin \left(\frac{\pi}{3}-\sin ^{-1}\left(-\frac{1}{2}\right)\right)=1$
अतः, विकल्प (D) सही है।
:::

:::answer
**उत्तर:** (D)
:::

:::

:::question{number="2.2.15" kind="exercise" id="q_2.2.15" topic="MCQ — tan⁻¹√3-cot⁻¹(-√3) का मान" simplified="True"}
#### प्रश्न 2.2.15

:::prompt
$\tan ^{-1} \sqrt{3}-\cot ^{-1}(-\sqrt{3})$ का मान
(A) $\pi$ है
(B) $-\frac{\pi}{2}$ है
(C) $0$ है
(D) $2 \sqrt{3}$
:::

:::solution{label="हल"}
दिया है: $\tan ^{-1} \sqrt{3}-\cot ^{-1}(-\sqrt{3})$
हम जानते हैं कि $\tan ^{-1}$ की मुख्य शाखा का परिसर $\left(-\frac{\pi}{2}, \frac{\pi}{2}\right)$ तथा $\cot ^{-1}$ की मुख्य शाखा का परिसर $(0, \pi)$ होता है।

$$
\begin{aligned}
& \therefore \tan ^{-1} \sqrt{3}-\cot ^{-1}(-\sqrt{3}) \\
& =\tan ^{-1}\left(\tan \frac{\pi}{3}\right)-\cot ^{-1}\left(-\cot \frac{\pi}{6}\right) \\
& =\frac{\pi}{3}-\cot ^{-1}\left[\cot \left(\pi-\frac{\pi}{6}\right)\right] \\
& =\frac{\pi}{3}-\cot ^{-1}\left(\cot \frac{5 \pi}{6}\right) \\
& =\frac{\pi}{3}-\frac{5 \pi}{6}=\frac{2 \pi-5 \pi}{6}=-\frac{3 \pi}{6}=-\frac{\pi}{2}
\end{aligned}
$$

इसलिए, $\tan ^{-1} \sqrt{3}-\cot ^{-1}(-\sqrt{3})=-\frac{\pi}{2}$
अतः, विकल्प (B) सही है।
:::

:::answer
**उत्तर:** (B)
:::

:::

## अतिरिक्त प्रश्न

:::question{number="2.5.1" kind="additional_exercise" id="q_2.5.1" topic="मान — cos⁻¹(cos(13π/6))" simplified="True"}
#### अतिरिक्त प्रश्न 2.5.1

:::prompt
$\cos ^{-1}\left(\cos \frac{13 \pi}{6}\right)$
:::

:::solution{label="हल"}
दिया है: $\cos ^{-1}\left(\cos \frac{13 \pi}{6}\right)$
हम जानते हैं कि $\cos ^{-1}$ की मुख्य शाखा का परिसर $[0, \pi]$ होता है।

$$
\begin{aligned}
& \therefore \cos ^{-1}\left(\cos \frac{13 \pi}{6}\right)=\cos ^{-1}\left[\cos \left(2 \pi+\frac{\pi}{6}\right)\right] \\
& =\cos ^{-1}\left(\cos \frac{\pi}{6}\right)=\frac{\pi}{6} \in[0, \pi]
\end{aligned}
$$

इसलिए, $\cos ^{-1}\left(\cos \frac{13 \pi}{6}\right)=\frac{\pi}{6}$
:::

:::answer
**उत्तर:** $\frac{\pi}{6}$
:::

:::

:::question{number="2.5.2" kind="additional_exercise" id="q_2.5.2" topic="मान — tan⁻¹(tan(7π/6))" simplified="True"}
#### अतिरिक्त प्रश्न 2.5.2

:::prompt
$\tan ^{-1}\left(\tan \frac{7 \pi}{6}\right)$
:::

:::solution{label="हल"}
दिया है: $\tan ^{-1}\left(\tan \frac{7 \pi}{6}\right)$
हम जानते हैं कि $\tan ^{-1}$ की मुख्य शाखा का परिसर $\left(-\frac{\pi}{2}, \frac{\pi}{2}\right)$ होता है।

$$
\begin{aligned}
& \therefore \tan ^{-1}\left(\tan \frac{7 \pi}{6}\right)=\tan ^{-1}\left[\tan \left(\pi+\frac{\pi}{6}\right)\right] \\
& =\tan ^{-1}\left(\tan \frac{\pi}{6}\right)=\frac{\pi}{6}
\end{aligned}
$$

इसलिए, $\tan ^{-1}\left(\tan \frac{7 \pi}{6}\right)=\frac{\pi}{6}$
:::

:::answer
**उत्तर:** $\frac{\pi}{6}$
:::

:::

:::question{number="2.5.3" kind="additional_exercise" id="q_2.5.3" topic="सिद्ध — 2sin⁻¹(3/5)=tan⁻¹(24/7)" simplified="True"}
#### अतिरिक्त प्रश्न 2.5.3

:::prompt
सिद्ध कीजिए: $2 \sin ^{-1} \frac{3}{5}=\tan ^{-1} \frac{24}{7}$
:::

:::solution{label="हल"}
$$
\begin{array}{ll}
\text { LHS }=2 \sin ^{-1} \frac{3}{5}=2 \tan ^{-1} \frac{3}{\sqrt{5^{2-3^{2}}}} & {\left[\because \sin ^{-1} \frac{a}{b}=\tan ^{-1} \frac{a}{\sqrt{b^{2}-a^{2}}}\right]} \\
=2 \tan ^{-1} \frac{3}{4}=\tan ^{-1}\left[\frac{2 \times \frac{3}{4}}{1-\left(\frac{3}{4}\right)^{2}}\right] & {\left[\because 2 \tan ^{-1} x=\tan ^{-1} \frac{2 x}{1-x^{2}}\right]} \\
=\tan ^{-1}\left[\frac{\frac{3}{2}}{\frac{16-9}{16}}\right] & \\
=\tan ^{-1}\left(\frac{3}{2} \times \frac{16}{7}\right) & \\
=\tan ^{-1} \frac{24}{7} & \\
=\text { RHS } &
\end{array}
$$
:::

:::

:::question{number="2.5.4" kind="additional_exercise" id="q_2.5.4" topic="सिद्ध — sin⁻¹(8/17)+sin⁻¹(3/5)=tan⁻¹(77/36)" simplified="True"}
#### अतिरिक्त प्रश्न 2.5.4

:::prompt
सिद्ध कीजिए: $\sin ^{-1} \frac{8}{17}+\sin ^{-1} \frac{3}{5}=\tan ^{-1} \frac{77}{36}$
:::

:::solution{label="हल"}
$$
\begin{aligned}
& \mathrm{LHS}=\sin ^{-1} \frac{8}{17}+\sin ^{-1} \frac{3}{5} \\
& =\tan ^{-1} \frac{8}{\sqrt{17^{2}-8^{2}}}+\tan ^{-1} \frac{3}{\sqrt{5^{2}-3^{2}}} \quad\left[\because \sin ^{-1} \frac{a}{b}=\tan ^{-1} \frac{a}{\sqrt{b^{2}-a^{2}}}\right] \\
& =\tan ^{-1} \frac{8}{15}+\tan ^{-1} \frac{3}{4} \\
& =\tan ^{-1}\left[\frac{\frac{8}{15}+\frac{3}{4}}{1-\frac{8}{15} \times \frac{3}{4}}\right] \quad\left[\because \tan ^{-1} x+\tan ^{-1} y=\tan ^{-1}\left(\frac{x+y}{1-x y}\right)\right] \\
& =\tan ^{-1}\left[\frac{\frac{32+45}{15 \times 4}}{\frac{15 \times 4-8 \times 3}{15 \times 4}}\right]=\tan ^{-1}\left[\frac{\frac{77}{60}}{\frac{36}{60}}\right] \\
& =\tan ^{-1} \frac{77}{36}=\text { RHS }
\end{aligned}
$$
:::

:::

:::question{number="2.5.5" kind="additional_exercise" id="q_2.5.5" topic="सिद्ध — cos⁻¹(4/5)+cos⁻¹(12/13)=cos⁻¹(33/65)" simplified="True"}
#### अतिरिक्त प्रश्न 2.5.5

:::prompt
सिद्ध कीजिए: $\cos ^{-1} \frac{4}{5}+\cos ^{-1} \frac{12}{13}=\cos ^{-1} \frac{33}{65}$
:::

:::solution{label="हल"}
$$
\begin{aligned}
& \text { LHS }=\cos ^{-1} \frac{4}{5}+\cos ^{-1} \frac{12}{13} \\
& =\tan ^{-1} \frac{\sqrt{5^{2}-4^{2}}}{4}+\tan ^{-1} \frac{\sqrt{13^{2}-12^{2}}}{12} \quad\left[\because \cos ^{-1} \frac{a}{b}=\tan ^{-1} \frac{\sqrt{b^{2}-a^{2}}}{a}\right] \\
& =\tan ^{-1} \frac{3}{4}+\tan ^{-1} \frac{5}{12} \\
& =\tan ^{-1}\left[\frac{\frac{3}{4}+\frac{5}{12}}{1-\frac{3}{4} \times \frac{5}{12}}\right] \quad\left[\because \tan ^{-1} x+\tan ^{-1} y=\tan ^{-1}\left(\frac{x+y}{1-x y}\right)\right] \\
& =\tan ^{-1}\left[\frac{\frac{36+20}{4 \times 12}}{\frac{4 \times 12-3 \times 5}{4 \times 12}}\right]=\tan ^{-1} \frac{56}{33} \\
& =\cos ^{-1} \frac{33}{\sqrt{56^{2}+33^{2}}} \quad\left[\because \tan ^{-1} \frac{a}{b}=\cos ^{-1} \frac{b}{\sqrt{a^{2}+b^{2}}}\right] \\
& =\cos ^{-1} \frac{33}{\sqrt{4225}}=\cos ^{-1} \frac{33}{65}=\text { RHS }
\end{aligned}
$$
:::

:::

:::question{number="2.5.6" kind="additional_exercise" id="q_2.5.6" topic="सिद्ध — cos⁻¹(12/13)+sin⁻¹(3/5)=sin⁻¹(56/65)" simplified="True"}
#### अतिरिक्त प्रश्न 2.5.6

:::prompt
सिद्ध कीजिए: $\cos ^{-1} \frac{12}{13}+\sin ^{-1} \frac{3}{5}=\sin ^{-1} \frac{56}{65}$
:::

:::solution{label="हल"}
$$
\mathrm{LHS}=\cos ^{-1} \frac{12}{13}+\sin ^{-1} \frac{3}{5}
$$

$$
\begin{aligned}
& =\tan ^{-1} \frac{\sqrt{13^{2}-12^{2}}}{12}+\tan ^{-1} \frac{3}{\sqrt{5^{2}-3^{2}}} \\
& =\tan ^{-1} \frac{5}{12}+\tan ^{-1} \frac{3}{4} \\
& =\tan ^{-1}\left[\frac{\frac{5}{12}+\frac{3}{4}}{1-\frac{5}{12} \times \frac{3}{4}}\right] \quad\left[\because \tan ^{-1} \frac{a}{b}=\tan ^{-1} \frac{\sqrt{b^{2}-a^{2}}}{a} \text { तथा } \sin ^{-1} \frac{a}{b}=\tan ^{-1} \frac{a}{\sqrt{b^{2}-a^{2}}}\right] \\
& =\tan ^{-1}\left[\frac{\frac{20+36}{12 \times 4}}{\frac{12 \times 4-5 \times 3}{12 \times 4}}\right]=\tan ^{-1} \frac{56}{33} \\
& =\sin ^{-1} \frac{56}{\sqrt{56^{2}+33^{2}}} \quad\left[\because \tan ^{-1} \frac{a}{b}=\sin ^{-1} \frac{a}{\sqrt{a^{2}+b^{2}}}\right] \\
& =\sin ^{-1} \frac{56}{\sqrt{4225}}=\sin ^{-1} \frac{56}{65}=\text { RHS }
\end{aligned}
$$
:::

:::

:::question{number="2.5.7" kind="additional_exercise" id="q_2.5.7" topic="सिद्ध — tan⁻¹(63/16)=sin⁻¹(5/13)+cos⁻¹(3/5)" simplified="True"}
#### अतिरिक्त प्रश्न 2.5.7

:::prompt
सिद्ध कीजिए: $\tan ^{-1} \frac{63}{16}=\sin ^{-1} \frac{5}{13}+\cos ^{-1} \frac{3}{5}$
:::

:::solution{label="हल"}
$$
\begin{aligned}
& \mathrm{RHS}=\sin ^{-1} \frac{5}{13}+\cos ^{-1} \frac{3}{5} \\
& =\tan ^{-1} \frac{5}{\sqrt{13^{2}-5^{2}}}+\tan ^{-1} \frac{\sqrt{5^{2}-3^{2}}}{3}\left[\because \cos ^{-1} \frac{a}{b}=\tan ^{-1} \frac{\sqrt{b^{2}-a^{2}}}{a} \text { तथा } \sin ^{-1} \frac{a}{b}=\tan ^{-1} \frac{a}{\sqrt{b^{2}-a^{2}}}\right] \\
& =\tan ^{-1} \frac{5}{12}+\tan ^{-1} \frac{4}{3} \\
& =\tan ^{-1}\left[\frac{\frac{5}{12}+\frac{4}{3}}{1-\frac{5}{12} \times \frac{4}{3}}\right] \quad\left[\because \tan ^{-1} x+\tan ^{-1} y=\tan ^{-1}\left(\frac{x+y}{1-x y}\right)\right] \\
& =\tan ^{-1}\left[\frac{\frac{15+48}{12 \times 3}}{\frac{12 \times 3-5 \times 4}{12 \times 3}}\right]=\tan ^{-1} \frac{63}{16}=\mathrm{RHS}
\end{aligned}
$$
:::

:::

:::question{number="2.5.8" kind="additional_exercise" id="q_2.5.8" topic="सिद्ध — tan⁻¹√x=(1/2)cos⁻¹((1-x)/(1+x))" simplified="True"}
#### अतिरिक्त प्रश्न 2.5.8

:::prompt
सिद्ध कीजिए: $\tan ^{1} \sqrt{x}=\frac{1}{2} \cos ^{1}\left(\frac{1-x}{1+x}\right), x \in[0,1]$
:::

:::solution{label="हल"}
$$
\begin{aligned}
& \text { LHS }=\tan ^{-1} \sqrt{x}=\frac{1}{2} \times 2 \tan ^{-1} \sqrt{x}=\frac{1}{2} \times 2 \tan ^{-1} \sqrt{x} \\
& =\frac{1}{2} \cos ^{-1}\left[\frac{1-(\sqrt{x})^{2}}{1+(\sqrt{x})^{2}}\right] \quad \quad\left[\because 2 \tan ^{-1} x=\cos ^{-1}\left[\frac{1-x^{2}}{1+x^{2}}\right]\right] \\
& =\frac{1}{2} \cos ^{-1}\left(\frac{1-x}{1+x}\right)=\text { RHS }
\end{aligned}
$$
:::

:::

:::question{number="2.5.9" kind="additional_exercise" id="q_2.5.9" topic="सिद्ध — cot⁻¹((√(1+sinx)+√(1-sinx))/(√(1+sinx)-√(1-sinx)))=x/2" simplified="True"}
#### अतिरिक्त प्रश्न 2.5.9

:::prompt
सिद्ध कीजिए: $\cot ^{1}\left(\frac{\sqrt{1+\sin x}+\sqrt{1-\sin x}}{\sqrt{1+\sin x}-\sqrt{1-\sin x}}\right)=\frac{x}{2}, x \in\left(0, \frac{\pi}{4}\right)$
:::

:::solution{label="हल"}
$$
\begin{aligned}
& \mathrm{LHS}=\cot ^{-1}\left(\frac{\sqrt{1+\sin x}+\sqrt{1-\sin x}}{\sqrt{1+\sin x}-\sqrt{1-\sin x}}\right)=\cot ^{-1}\left(\frac{\sqrt{1+\cos \left(\frac{\pi}{2}-x\right)}+\sqrt{1-\cos \left(\frac{\pi}{2}-x\right)}}{\sqrt{1+\cos \left(\frac{\pi}{2}-x\right)}-\sqrt{1-\cos \left(\frac{\pi}{2}-x\right)}}\right) \\
& =\cot ^{-1}\left(\frac{\sqrt{1+\cos y}+\sqrt{1-\cos y}}{\sqrt{1+\cos y}-\sqrt{1-\cos y}}\right) \quad\left[\text { माना } \frac{\pi}{2}-x=y\right] \\
& =\cot ^{-1}\left(\frac{\sqrt{2 \cos ^{2} \frac{y}{2}}+\sqrt{2 \sin ^{2} \frac{y}{2}}}{\sqrt{2 \cos ^{2} \frac{y}{2}}-\sqrt{2 \sin ^{2} \frac{y}{2}}}\right) \quad\left[\because 1+\cos y=2 \cos ^{2} \frac{y}{2} \text { तथा } 1-\cos y=2 \sin ^{2} \frac{y}{2}\right] \\
& =\cot ^{-1}\left(\frac{\sqrt{2} \cos \frac{y}{2}+\sqrt{2} \sin \frac{y}{2}}{\sqrt{2} \cos \frac{y}{2}-\sqrt{2} \sin \frac{y}{2}}\right) \\
& =\cot ^{-1}\left(\frac{1+\tan \frac{y}{2}}{1-\tan ^{\frac{y}{2}}}\right) \quad \text { [प्रत्येक पद को } \sqrt{2} \cos \frac{y}{2} \text { से भाग देने पर] }
\end{aligned}
$$

$$
\begin{aligned}
& =\cot ^{-1}\left(\frac{\tan \frac{\pi}{4}+\tan \frac{y}{2}}{1-\tan \frac{\pi}{4} \cdot \tan \frac{y}{2}}\right)=\cot ^{-1}\left[\tan \left(\frac{\pi}{4}+\frac{y}{2}\right)\right] \\
& =\cot ^{-1}\left[\cot \left\{\frac{\pi}{2}-\left(\frac{\pi}{4}+\frac{y}{2}\right)\right\}\right]=\frac{\pi}{2}-\left(\frac{\pi}{4}+\frac{y}{2}\right)=\frac{\pi}{4}-\frac{y}{2} \\
& =\frac{\pi}{4}-\frac{1}{2}\left(\frac{\pi}{2}-x\right) \quad \quad\left[\because \frac{\pi}{2}-x=y\right] \\
& =\frac{x}{2}=\text { RHS }
\end{aligned}
$$
:::

:::

:::question{number="2.5.10" kind="additional_exercise" id="q_2.5.10" topic="सिद्ध — tan⁻¹((√(1+x)-√(1-x))/(√(1+x)+√(1-x)))=π/4-(1/2)cos⁻¹x" simplified="True"}
#### अतिरिक्त प्रश्न 2.5.10

:::prompt
सिद्ध कीजिए: $\tan ^{1}\left(\frac{\sqrt{1+x}-\sqrt{1-x}}{\sqrt{1+x}+\sqrt{1-x}}\right)=\frac{\pi}{4}-\frac{1}{2} \cos ^{1} x,-\frac{1}{\sqrt{2}} \leq x \leq 1$ [संकेत: $x=\cos 2 \theta$ रखिए]
:::

:::solution{label="हल"}
$$
\left.\begin{array}{l}
\mathrm{LHS}=\tan ^{-1}\left(\frac{\sqrt{1+x}-\sqrt{1-x}}{\sqrt{1+x}+\sqrt{1-x}}\right) \\
=\tan ^{-1}\left(\frac{\sqrt{1+\cos y}-\sqrt{1-\cos y}}{\sqrt{1+\cos y}+\sqrt{1-\cos y}}\right) \quad[\text { माना } x=\cos y] \\
=\tan ^{-1}\left(\frac{\sqrt{2 \cos ^{2} \frac{y}{2}}-\sqrt{2 \sin ^{2} \frac{y}{2}}}{\sqrt{2 \cos ^{2} \frac{y}{2}}+\sqrt{2 \sin ^{2} \frac{y}{2}}}\right) \quad\left[\because 1+\cos y=2 \cos ^{2} \frac{y}{2} \text { तथा } 1-\cos y=2 \sin ^{2} \frac{y}{2}\right] \\
=\tan ^{-1}\left(\frac{\sqrt{2} \cos \frac{y}{2}-\sqrt{2} \sin \frac{y}{2}}{\sqrt{2} \cos \frac{y}{2}+\sqrt{2} \sin \frac{y}{2}}\right) \\
=\tan ^{-1}\left(\frac{1-\tan \frac{y}{2}}{1+\tan \frac{y}{2}}\right) \\
=\tan ^{-1}\left(\frac{\tan \frac{\pi}{4}-\tan \frac{y}{2}}{1+\tan \frac{\pi}{4} \cdot \tan \frac{y}{2}}\right)=\tan ^{-1}\left[\tan \left(\frac{\pi}{4}-\frac{y}{2}\right)\right] \\
=\frac{\pi}{4}-\frac{y}{2}=\frac{\pi}{4}-\frac{1}{2} \cos ^{-1} x=\mathrm{RHS}
\end{array} \quad \text { प्रत्येक पद को } \sqrt{2} \cos \frac{y}{2} \text { से भाग देने पर }\right] ~{ }^{\tan \left(\frac{\pi}{2}\right)}
$$
:::

:::

:::question{number="2.5.11" kind="additional_exercise" id="q_2.5.11" topic="हल — 2tan⁻¹(cosx)=tan⁻¹(2cosecx)" simplified="True"}
#### अतिरिक्त प्रश्न 2.5.11

:::prompt
$2 \tan ^{-1}(\cos x)=\tan ^{-1}(2 \operatorname{cosec} x)$
:::

:::solution{label="हल"}
दिया है: $2 \tan ^{-1}(\cos x)=\tan ^{-1}(2 \operatorname{cosec} x)$

$$
\begin{aligned}
& \Rightarrow \tan ^{-1}\left(\frac{2 \cos x}{1-\cos ^{2} x}\right)=\tan ^{-1}(2 \operatorname{cosec} x) \quad\left[\because 2 \tan ^{-1} x=\tan ^{-1} \frac{2 x}{1-x^{2}}\right] \\
& \Rightarrow \frac{2 \cos x}{1-\cos ^{2} x}=2 \operatorname{cosec} x \\
& \Rightarrow \frac{2 \cos x}{\sin ^{2} x}=\frac{2}{\sin x} \Rightarrow 2 \sin x \cdot \cos x=2 \sin ^{2} x \\
& \Rightarrow 2 \sin x \cdot \cos x-2 \sin ^{2} x=0 \quad \Rightarrow 2 \sin x(\cos x-\sin x)=0 \\
& \Rightarrow 2 \sin x=0 \quad \text { या } \quad \cos x-\sin x=0
\end{aligned}
$$

परन्तु $\sin x \neq 0$ क्योंकि यह समीकरण को संतुष्ट नहीं करता है। $\therefore \cos x-\sin x=0$

$$
\begin{aligned}
& \Rightarrow \cos x=\sin x \\
& \Rightarrow \tan x=1 \\
& \therefore x=\frac{\pi}{4}
\end{aligned}
$$
:::

:::answer
**उत्तर:** $x=\frac{\pi}{4}$
:::

:::

:::question{number="2.5.12" kind="additional_exercise" id="q_2.5.12" topic="हल — tan⁻¹((1-x)/(1+x))=(1/2)tan⁻¹x" simplified="True"}
#### अतिरिक्त प्रश्न 2.5.12

:::prompt
$\tan ^{-1} \frac{1-x}{1+x}=\frac{1}{2} \tan ^{-1} x,(x>0)$
:::

:::solution{label="हल"}
दिया है: $\tan ^{-1} \frac{1-x}{1+x}=\frac{1}{2} \tan ^{-1} x$

$$
\begin{aligned}
& \Rightarrow \tan ^{-1} 1-\tan ^{-1} x=\frac{1}{2} \tan ^{-1} x \quad\left[\because \tan ^{-1} x-\tan ^{-1} y=\tan ^{-1}\left(\frac{x-y}{1+x y}\right)\right] \\
& \Rightarrow \frac{\pi}{4}=\frac{3}{2} \tan ^{-1} x \\
& \Rightarrow \frac{\pi}{6}=\tan ^{-1} x \\
& \Rightarrow \tan \left(\frac{\pi}{6}\right)=x \\
& \therefore x=\frac{1}{\sqrt{3}}
\end{aligned}
$$
:::

:::answer
**उत्तर:** $x=\frac{1}{\sqrt{3}}$
:::

:::

:::question{number="2.5.13" kind="additional_exercise" id="q_2.5.13" topic="MCQ — sin(tan⁻¹x), |x|<1 का मान" simplified="True"}
#### अतिरिक्त प्रश्न 2.5.13

:::prompt
$\sin \left(\tan ^{-1} x\right),|x|<1$ बराबर होता है:
(A) $\frac{x}{\sqrt{1-x^{2}}}$
(B) $\frac{1}{\sqrt{1-x^{2}}}$
(C) $\frac{1}{\sqrt{1+x^{2}}}$
(D) $\frac{x}{\sqrt{1+x^{2}}}$
:::

:::solution{label="हल"}
दिया है: $\sin \left(\tan ^{-1} x\right)$

$$
\begin{aligned}
& =\sin \left(\sin ^{-1} \frac{x}{\sqrt{1+x^{2}}}\right) \quad\left[\because \tan ^{-1} \frac{a}{b}=\sin ^{-1} \frac{a}{\sqrt{a^{2}+b^{2}}}\right] \\
& =\frac{x}{\sqrt{1+x^{2}}}
\end{aligned}
$$

अतः, विकल्प (D) सही है।
:::

:::answer
**उत्तर:** (D)
:::

:::

:::question{number="2.5.14" kind="additional_exercise" id="q_2.5.14" topic="MCQ — sin⁻¹(1-x)-2sin⁻¹x=π/2 का हल" simplified="True"}
#### अतिरिक्त प्रश्न 2.5.14

:::prompt
यदि $\sin ^{-1}(1-x)-2 \sin ^{-1} x=\frac{\pi}{2}$, तो $x$ का मान बराबर है:
(A) $0, \frac{1}{2}$
(B) $1, \frac{1}{2}$
(C) $0$
(D) $\frac{1}{2}$
:::

:::solution{label="हल"}
दिया है: $\sin ^{-1}(1-x)-2 \sin ^{-1} x=\frac{\pi}{2}$
माना, $x=\sin y$

$$
\begin{array}{ll}
\therefore \sin ^{-1}(1-\sin y)-2 y=\frac{\pi}{2} & \\
\Rightarrow \sin ^{-1}(1-\sin y)=\frac{\pi}{2}+2 y & \\
\Rightarrow 1-\sin y=\sin \left(\frac{\pi}{2}+2 y\right) & \\
\Rightarrow 1-\sin y=\cos 2 y & \\
\Rightarrow 1-\sin y=1-2 \sin ^{2} y & {\left[\because \cos 2 y=1-2 \sin ^{2} y\right]} \\
\Rightarrow 2 \sin ^{2} y-\sin y=0 & {[\because x=\sin y]} \\
\Rightarrow 2 x^{2}-x=0 & \\
\Rightarrow x(2 x-1)=0 & \\
\Rightarrow x=0 \quad \text { या } x=\frac{1}{2} &
\end{array}
$$

परन्तु $x \neq \frac{1}{2}$ क्योंकि यह समीकरण को संतुष्ट नहीं करता है।
$\therefore x=0$ दी गई समीकरण का हल है।
अतः, विकल्प (C) सही है।
:::

:::answer
**उत्तर:** (C)
:::

:::
