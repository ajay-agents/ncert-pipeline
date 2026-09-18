---
subject: maths
class: 12
chapter: 2
lang: hi
title: "प्रतिलोम त्रिकोणमितीय फलन"
---

# प्रतिलोम त्रिकोणमितीय फलन

## उदाहरण

:::example{number="2.1" kind="example" id="ex_2.1" topic="sin⁻¹(1/√2) का मुख्य मान"}
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

:::example{number="2.2" kind="example" id="ex_2.2" topic="cot⁻¹(-1/√3) का मुख्य मान"}
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

:::example{number="2.3" kind="example" id="ex_2.3" topic="sin⁻¹(2x√(1-x²)) के दो रूपांतरण सिद्ध करना"}
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
मान लीजिए कि $x=\cos \theta$ तो उपर्युक्त विधि के प्रयोग द्वारा हमें $\sin ^{-1}\left(2 x \sqrt{1-x^{2}}\right)=2 \cos ^{-1} x$ प्राप्त होता है।
:::

:::

:::

:::example{number="2.4" kind="example" id="ex_2.4" topic="tan⁻¹(cosx/(1-sinx)) को सरलतम रूप में व्यक्त करना"}
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

:::example{number="2.5" kind="example" id="ex_2.5" topic="cot⁻¹(1/√(x²-1)) को सरलतम रूप में लिखना"}
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

:::example{number="2.6" kind="example" id="ex_2.6" topic="sin⁻¹(sin(3π/5)) का मान (विविध उदाहरण)"}
#### उदाहरण 2.6

:::prompt
$\sin ^{-1}\left(\sin \frac{3 \pi}{5}\right)$ का मान ज्ञात कीजिए।
:::

:::solution{label="हल"}
हमें ज्ञात है कि $\sin ^{-1}(\sin x)=x$ होता है। इसलिए $\sin ^{-1}\left(\sin \frac{3 \pi}{5}\right)=\frac{3 \pi}{5}$
किंतु $\frac{3 \pi}{5} \notin\left[-\frac{\pi}{2}, \frac{\pi}{2}\right]$, जो $\sin ^{-1} x$ की मुख्य शाखा है।
तथापि $\sin \left(\frac{3 \pi}{5}\right)=\sin \left(\pi-\frac{3 \pi}{5}\right)=\sin \frac{2 \pi}{5}$ तथा $\frac{2 \pi}{5} \in\left[-\frac{\pi}{2}, \frac{\pi}{2}\right]$
अत:

$$
\sin ^{-1}\left(\sin \frac{3 \pi}{5}\right)=\sin ^{-1}\left(\sin \frac{2 \pi}{5}\right)=\frac{2 \pi}{5}
$$
:::

:::answer
**उत्तर:** $\frac{2 \pi}{5}$
:::

:::
