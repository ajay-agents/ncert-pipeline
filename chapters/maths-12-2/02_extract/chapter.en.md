---
subject: maths
class: 12
chapter: 2
lang: en
title: "Inverse Trigonometric Functions"
---

# Inverse Trigonometric Functions

## Examples

:::example{number="1" kind="example" id="ex_2.1" topic="Principal value of sin^-1"}
#### Example 1

:::prompt
Find the principal value of $\sin ^{-1}\left(\frac{1}{\sqrt{2}}\right)$.
:::

:::solution{label="Solution"}
Let $\sin ^{-1}\left(\frac{1}{\sqrt{2}}\right)=y$. Then, $\sin y=\frac{1}{\sqrt{2}}$.
We know that the range of the principal value branch of $\sin ^{-1}$ is $\frac{-\pi}{2}, \frac{\pi}{2}$ and $\sin \left(\frac{\pi}{4}\right)=\frac{1}{\sqrt{2}}$. Therefore, principal value of $\sin ^{-1}\left(\frac{1}{\sqrt{2}}\right)$ is $\frac{\pi}{4}$
:::

:::

:::example{number="2" kind="example" id="ex_2.2" topic="Principal value of cot^-1"}
#### Example 2

:::prompt
Find the principal value of $\cot ^{-1}\left(\frac{-1}{\sqrt{3}}\right)$
:::

:::solution{label="Solution"}
Let $\cot ^{-1}\left(\frac{-1}{\sqrt{3}}\right)=y$. Then,

$$
\cot y=\frac{-1}{\sqrt{3}}=-\cot \left(\frac{\pi}{3}\right)=\cot \left(\pi-\frac{\pi}{3}\right)=\cot \left(\frac{2 \pi}{3}\right)
$$

We know that the range of principal value branch of $\cot ^{-1}$ is $(0, \pi)$ and $\cot \left(\frac{2 \pi}{3}\right)=\frac{-1}{\sqrt{3}}$. Hence, principal value of $\cot ^{-1}\left(\frac{-1}{\sqrt{3}}\right)$ is $\frac{2 \pi}{3}$
:::

:::

:::example{number="3" kind="example" id="ex_2.3" topic="Sine inverse double-angle identity"}
#### Example 3

:::prompt
Show that
(i) $\sin ^{-1}\left(2 x \sqrt{1-x^{2}}\right)=2 \sin ^{-1} x,-\frac{1}{\sqrt{2}} \leq x \leq \frac{1}{\sqrt{2}}$
(ii) $\sin ^{-1}\left(2 x \sqrt{1-x^{2}}\right)=2 \cos ^{-1} x, \frac{1}{\sqrt{2}} \leq x \leq 1$
:::

:::solution{label="Solution"}
(i) Let $x=\sin \theta$. Then $\sin ^{-1} x=\theta$. We have
$$
\begin{aligned}
\sin ^{-1}\left(2 x \sqrt{1-x^{2}}\right) & =\sin ^{-1}\left(2 \sin \theta \sqrt{1-\sin ^{2} \theta}\right) \\
& =\sin ^{-1}(2 \sin \theta \cos \theta)=\sin ^{-1}(\sin 2 \theta)=2 \theta \\
& =2 \sin ^{-1} x
\end{aligned}
$$
(ii) Take $x=\cos \theta$, then proceeding as above, we get, $\sin ^{-1}\left(2 x \sqrt{1-x^{2}}\right)=2 \cos ^{-1} x$
:::

:::

:::example{number="4" kind="example" id="ex_2.4" topic="Simplify inverse tangent expression"}
#### Example 4

:::prompt
Express $\tan ^{-1} \frac{\cos x}{1-\sin x},-\frac{3 \pi}{2}<x<\frac{\pi}{2}$ in the simplest form.
:::

:::solution{label="Solution"}
We write
$$
\begin{aligned}
\tan ^{-1}\left(\frac{\cos x}{1-\sin x}\right) & =\tan ^{-1}\left[\frac{\cos ^{2} \frac{x}{2}-\sin ^{2} \frac{x}{2}}{\cos ^{2} \frac{x}{2}+\sin ^{2} \frac{x}{2}-2 \sin \frac{x}{2} \cos \frac{x}{2}}\right] \\
& =\tan ^{-1}\left[\frac{\left(\cos \frac{x}{2}+\sin \frac{x}{2}\right)\left(\cos \frac{x}{2}-\sin \frac{x}{2}\right)}{\left(\cos \frac{x}{2}-\sin \frac{x}{2}\right)^{2}}\right] \\
& =\tan ^{-1}\left[\frac{\cos \frac{x}{2}+\sin \frac{x}{2}}{\cos \frac{x}{2}-\sin \frac{x}{2}}\right]=\tan ^{-1}\left[\frac{1+\tan \frac{x}{2}}{1-\tan \frac{x}{2}}\right] \\
& =\tan ^{-1}\left[\tan \left(\frac{\pi}{4}+\frac{x}{2}\right)\right]=\frac{\pi}{4}+\frac{x}{2}
\end{aligned}
$$
:::

:::

:::example{number="5" kind="example" id="ex_2.5" topic="Simplify inverse cotangent expression"}
#### Example 5

:::prompt
Write $\cot ^{-1}\left(\frac{1}{\sqrt{x^{2}-1}}\right), x>1$ in the simplest form.
:::

:::solution{label="Solution"}
Let $x=\sec \theta$, then $\sqrt{x^{2}-1}=\sqrt{\sec ^{2} \theta-1}=\tan \theta$
Therefore, $\cot ^{-1} \frac{1}{\sqrt{x^{2}-1}}=\cot ^{-1}(\cot \theta)=\theta=\sec ^{-1} x$, which is the simplest form.
:::

:::

:::example{number="6" kind="example" id="ex_2.6" topic="Value of sin^-1(sin x) outside principal range"}
#### Example 6

:::prompt
Find the value of $\sin ^{-1}\left(\sin \frac{3 \pi}{5}\right)$
:::

:::solution{label="Solution"}
We know that $\sin ^{-1}(\sin x)=x$. Therefore, $\sin ^{-1}\left(\sin \frac{3 \pi}{5}\right)=\frac{3 \pi}{5}$
But $\quad \frac{3 \pi}{5} \notin\left[-\frac{\pi}{2}, \frac{\pi}{2}\right]$, which is the principal branch of $\sin ^{-1} x$
However $\quad \sin \left(\frac{3 \pi}{5}\right)=\sin \left(\pi-\frac{3 \pi}{5}\right)=\sin \frac{2 \pi}{5}$ and $\frac{2 \pi}{5} \in\left[-\frac{\pi}{2}, \frac{\pi}{2}\right]$
Therefore $\quad \sin ^{-1}\left(\sin \frac{3 \pi}{5}\right)=\sin ^{-1}\left(\sin \frac{2 \pi}{5}\right)=\frac{2 \pi}{5}$
:::

:::

## Questions and Solutions

:::question{number="1" kind="exercise" id="q_2.1.1" topic="Principal value of sin^-1"}
#### Question 1

:::prompt
Find the principal value of $\sin ^{-1}\left(-\frac{1}{2}\right)$.
:::

:::solution{label="Solution"}
Let, $\sin ^{-1}\left(-\frac{1}{2}\right)=y$
Hence,

$$
\begin{aligned}
\sin y & =\left(-\frac{1}{2}\right) \\
& =-\sin \left(\frac{\pi}{6}\right) \\
& =\sin \left(-\frac{\pi}{6}\right)
\end{aligned}
$$

Range of the principal value of $\sin ^{-1}(x)$ is $\left(-\frac{\pi}{2}, \frac{\pi}{2}\right)$
Thus, principal value of $\sin ^{-1}\left(-\frac{1}{2}\right)=\left(-\frac{\pi}{6}\right)$.
:::

:::answer
**Answer:** $-\frac{\pi}{6}$
:::

:::

:::question{number="2" kind="exercise" id="q_2.1.2" topic="Principal value of cos^-1"}
#### Question 2

:::prompt
Find the principal value of $\cos ^{-1}\left(\frac{\sqrt{3}}{2}\right)$.
:::

:::solution{label="Solution"}
Let,

$$
\cos ^{-1}\left(\frac{\sqrt{3}}{2}\right)=y
$$

Hence,

$$
\begin{aligned}
\cos y & =\left(\frac{\sqrt{3}}{2}\right) \\
& =\cos \frac{\pi}{6}
\end{aligned}
$$

Range of the principal value of $\cos ^{-1}(x)$ is $(0, \pi)$.
Thus, principal value of $\cos ^{-1}\left(\frac{\sqrt{3}}{2}\right)=\left(\frac{\pi}{6}\right)$
:::

:::answer
**Answer:** $\frac{\pi}{6}$
:::

:::

:::question{number="3" kind="exercise" id="q_2.1.3" topic="Principal value of cosec^-1"}
#### Question 3

:::prompt
Find the principal value of $\operatorname{cosec}^{-1}(2)$.
:::

:::solution{label="Solution"}
Let, $\operatorname{cosec}^{-1}(2)=y$
Hence,

$$
\begin{aligned}
\operatorname{cosec} y & =2 \\
& =\operatorname{cosec}\left(\frac{\pi}{6}\right)
\end{aligned}
$$

Range of the principal value of $\operatorname{cosec}^{-1}(x)=\left[-\frac{\pi}{2}, \frac{\pi}{2}\right]-\{0\}$
Thus, principal value of $\operatorname{cosec}^{-1}(2)=\left(\frac{\pi}{6}\right)$.
:::

:::answer
**Answer:** $\frac{\pi}{6}$
:::

:::

:::question{number="4" kind="exercise" id="q_2.1.4" topic="Principal value of tan^-1"}
#### Question 4

:::prompt
Find the principal value of $\tan ^{-1}(-\sqrt{3})$
:::

:::solution{label="Solution"}
Let, $\tan ^{-1}(-\sqrt{3})=y$
Hence,

$$
\begin{aligned}
\tan y & =-\sqrt{3} \\
& =-\tan \left(\frac{\pi}{3}\right) \\
& =\tan \left(-\frac{\pi}{3}\right)
\end{aligned}
$$

Range of the principal value of $\tan ^{-1}(x)=\left(-\frac{\pi}{2}, \frac{\pi}{2}\right)$
Thus, principal value of $\tan ^{-1}(-\sqrt{3})=\left(-\frac{\pi}{3}\right)$.
:::

:::answer
**Answer:** $-\frac{\pi}{3}$
:::

:::

:::question{number="5" kind="exercise" id="q_2.1.5" topic="Principal value of cos^-1"}
#### Question 5

:::prompt
Find the principal value of $\cos ^{-1}\left(-\frac{1}{2}\right)$
:::

:::solution{label="Solution"}
Let, $\cos ^{-1}\left(-\frac{1}{2}\right)=y$

Hence,

$$
\begin{aligned}
\cos y & =-\frac{1}{2} \\
& =-\cos \left(\frac{\pi}{3}\right) \\
& =\cos \left(\pi-\frac{\pi}{3}\right) \\
& =\cos \left(\frac{2 \pi}{3}\right)
\end{aligned}
$$

Range of the principal value of $\cos ^{-1}(x)=[0, \pi]$
Thus, principal value of $\cos ^{-1}\left(-\frac{1}{2}\right)=\left(\frac{2 \pi}{3}\right)$.
:::

:::answer
**Answer:** $\frac{2 \pi}{3}$
:::

:::

:::question{number="6" kind="exercise" id="q_2.1.6" topic="Principal value of tan^-1"}
#### Question 6

:::prompt
Find the principal value of $\tan ^{-1}(-1)$
:::

:::solution{label="Solution"}
Let, $\tan ^{-1}(-1)=y$
Hence,

$$
\begin{aligned}
\tan y & =-1 \\
& =-\tan \left(\frac{\pi}{4}\right) \\
& =\tan \left(-\frac{\pi}{4}\right)
\end{aligned}
$$

Range of the principal value of $\tan ^{-1}(x)=\left(-\frac{\pi}{2}, \frac{\pi}{2}\right)$
Thus, principal value of $\tan ^{-1}(-1)=\left(-\frac{\pi}{4}\right)$.
:::

:::answer
**Answer:** $-\frac{\pi}{4}$
:::

:::

:::question{number="7" kind="exercise" id="q_2.1.7" topic="Principal value of sec^-1"}
#### Question 7

:::prompt
Find the principal value of $\sec ^{-1}\left(\frac{2}{\sqrt{3}}\right)$
:::

:::solution{label="Solution"}
Let, $\sec ^{-1}\left(\frac{2}{\sqrt{3}}\right)=y$
Hence,

$$
\begin{aligned}
\sec y & =\frac{2}{\sqrt{3}} \\
& =\sec \left(\frac{\pi}{6}\right)
\end{aligned}
$$

Range of the principal value of $\sec ^{-1}(x)=[0, \pi]-\left\{\frac{\pi}{2}\right\}$
Thus, principal value of $\sec ^{-1}\left(\frac{2}{\sqrt{3}}\right)=\left(\frac{\pi}{6}\right)$.
:::

:::answer
**Answer:** $\frac{\pi}{6}$
:::

:::

:::question{number="8" kind="exercise" id="q_2.1.8" topic="Principal value of cot^-1"}
#### Question 8

:::prompt
Find the principal value of $\cot ^{-1}(\sqrt{3})$
:::

:::solution{label="Solution"}
Let, $\cot ^{-1}(\sqrt{3})=y$
Hence,

$$
\begin{aligned}
\cot y & =\sqrt{3} \\
& =\cot \left(\frac{\pi}{6}\right)
\end{aligned}
$$

Range of the principal value of $\cot ^{-1}(x)=(0, \pi)$
Thus, principal value of $\cot ^{-1}(\sqrt{3})=\left(\frac{\pi}{6}\right)$.
:::

:::answer
**Answer:** $\frac{\pi}{6}$
:::

:::

:::question{number="9" kind="exercise" id="q_2.1.9" topic="Principal value of cos^-1"}
#### Question 9

:::prompt
Find the principal value of $\cos ^{-1}\left(-\frac{1}{\sqrt{2}}\right)$
:::

:::solution{label="Solution"}
Let, $\cos ^{-1}\left(-\frac{1}{\sqrt{2}}\right)=y$
Hence,

$$
\begin{aligned}
\cos y & =-\frac{1}{\sqrt{2}} \\
& =-\cos \left(\frac{\pi}{4}\right) \\
& =\cos \left(-\frac{\pi}{4}\right) \\
& =\cos \left(\pi-\frac{\pi}{4}\right) \\
& =\cos \left(\frac{3 \pi}{4}\right)
\end{aligned}
$$

Range of the principal value of $\cos ^{-1}(x)=[0, \pi]$
Thus, principal value of $\cos ^{-1}\left(-\frac{1}{\sqrt{2}}\right)=\left(\frac{3 \pi}{4}\right)$.
:::

:::answer
**Answer:** $\frac{3 \pi}{4}$
:::

:::

:::question{number="10" kind="exercise" id="q_2.1.10" topic="Principal value of cosec^-1"}
#### Question 10

:::prompt
Find the principal value of $\operatorname{cosec}^{-1}(-\sqrt{2})$
:::

:::solution{label="Solution"}
Let, $\operatorname{cosec}^{-1}(-\sqrt{2})=y$
Hence,

$$
\begin{aligned}
\operatorname{cosec} y & =-\sqrt{2} \\
& =-\operatorname{cosec}\left(\frac{\pi}{4}\right) \\
& =\operatorname{cosec}\left(-\frac{\pi}{4}\right)
\end{aligned}
$$

Range of the principal value of $\operatorname{cosec}^{-1}(x)=\left[-\frac{\pi}{2}, \frac{\pi}{2}\right]-\{0\}$
Thus, principal value of $\operatorname{cosec}^{-1}(-\sqrt{2})=\left(-\frac{\pi}{4}\right)$.
:::

:::answer
**Answer:** $-\frac{\pi}{4}$
:::

:::

:::question{number="11" kind="exercise" id="q_2.1.11" topic="Sum of inverse trig values"}
#### Question 11

:::prompt
Find the value of $\tan ^{-1}(1)+\cos ^{-1}-\frac{1}{2}+\sin ^{-1}-\frac{1}{2}$
:::

:::solution{label="Solution"}
Let, $\tan ^{-1}(1)=x$
Hence,

$$
\begin{aligned}
\tan x & =1 \\
& =\tan \left(\frac{\pi}{4}\right)
\end{aligned}
$$

Therefore,

$$
\tan ^{-1}(1)=\left(\frac{\pi}{4}\right)
$$

Now, let $\cos ^{-1}\left(-\frac{1}{2}\right)=y$
Hence,

$$
\begin{aligned}
\cos y & =-\frac{1}{2} \\
& =-\cos \left(\frac{\pi}{3}\right) \\
& =\cos \left(\pi-\frac{\pi}{3}\right) \\
& =\cos \left(\frac{2 \pi}{3}\right)
\end{aligned}
$$

Therefore,

$$
\cos ^{-1}\left(-\frac{1}{2}\right)=\frac{2 \pi}{3}
$$

Again, let $\sin ^{-1}\left(-\frac{1}{2}\right)=z$

Hence,

$$
\begin{aligned}
\sin z & =-\frac{1}{2} \\
& =-\sin \left(\frac{\pi}{6}\right) \\
& =\sin \left(-\frac{\pi}{6}\right)
\end{aligned}
$$

Therefore,

$$
\sin ^{-1}\left(-\frac{1}{2}\right)=-\frac{\pi}{6}
$$

Thus,

$$
\begin{aligned}
\tan ^{-1}(1)+\cos ^{-1}\left(-\frac{1}{2}\right)+\sin ^{-1}\left(-\frac{1}{2}\right) & =\frac{\pi}{4}+\frac{2 \pi}{3}-\frac{\pi}{6} \\
& =\frac{3 \pi+8 \pi-2 \pi}{12} \\
& =\frac{9 \pi}{12} \\
& =\frac{3 \pi}{4}
\end{aligned}
$$
:::

:::answer
**Answer:** $\frac{3 \pi}{4}$
:::

:::

:::question{number="12" kind="exercise" id="q_2.1.12" topic="Sum of inverse trig values"}
#### Question 12

:::prompt
Find the value of $\cos ^{-1} \frac{1}{2}+2 \sin ^{-1} \frac{1}{2}$
:::

:::solution{label="Solution"}
Let, $\tan ^{-1}(1)=x$
Hence,

$$
\begin{aligned}
\cos x & =\frac{1}{2} \\
& =\cos \left(\frac{\pi}{3}\right)
\end{aligned}
$$

Therefore,

$$
\cos ^{-1}\left(\frac{1}{2}\right)=\frac{\pi}{3}
$$

Let, $\sin ^{-1}\left(\frac{1}{2}\right)=y$
Hence,

$$
\begin{aligned}
\sin y & =\frac{1}{2} \\
& =\sin \left(\frac{\pi}{6}\right)
\end{aligned}
$$

Therefore,

$$
\sin ^{-1}\left(\frac{1}{2}\right)=\frac{\pi}{6}
$$

Thus

$$
\begin{aligned}
\cos ^{-1}\left(\frac{1}{2}\right)+2 \sin ^{-1}\left(\frac{1}{2}\right) & =\frac{\pi}{3}+2\left(\frac{\pi}{6}\right) \\
& =\frac{2 \pi}{3}
\end{aligned}
$$
:::

:::answer
**Answer:** $\frac{2 \pi}{3}$
:::

:::

:::question{number="13" kind="exercise" id="q_2.1.13" topic="Range of sin^-1 (multiple choice)"}
#### Question 13

:::prompt
If $\sin ^{-1} x=y$, then
(A) $0 \leq y \leq \pi$
(B) $-\frac{\pi}{2} \leq y \leq \frac{\pi}{2}$
(C) $0<y<\pi$
(D) $-\frac{\pi}{2}<y<\frac{\pi}{2}$
:::

:::solution{label="Solution"}
It is given that $\sin ^{-1} x=y$
Range of the principal value of $\sin ^{-1} x=\left[-\frac{\pi}{2}, \frac{\pi}{2}\right]$
Thus, $-\frac{\pi}{2} \leq y \leq \frac{\pi}{2}$
The answer is B.
:::

:::answer
**Answer:** Option (B)
:::

:::

:::question{number="14" kind="exercise" id="q_2.1.14" topic="Difference of inverse trig values (multiple choice)"}
#### Question 14

:::prompt
$\tan ^{-1} \sqrt{3}-\sec ^{-1}(-2)$ is equal to
(A) $\pi$
(B) $-\frac{\pi}{3}$
(C) $\frac{\pi}{3}$
(D) $\frac{2 \pi}{3}$
:::

:::solution{label="Solution"}
Let $\tan ^{-1}(\sqrt{3})=x$
Hence,

$$
\begin{aligned}
\tan x & =\sqrt{3} \\
& =\tan \left(\frac{\pi}{3}\right)
\end{aligned}
$$

Range of the principal value of $\tan ^{-1} x=\left(-\frac{\pi}{2}, \frac{\pi}{2}\right)$
Therefore, $\tan ^{-1}(\sqrt{3})=\left(\frac{\pi}{3}\right)$

Let $\sec ^{-1}(-2)=y$
Hence,

$$
\begin{aligned}
\sec y & =(-2) \\
& =-\sec \left(\frac{\pi}{3}\right) \\
& =\sec \left(-\frac{\pi}{3}\right) \\
& =\sec \left(\pi-\frac{\pi}{3}\right) \\
& =\sec \left(\frac{2 \pi}{3}\right)
\end{aligned}
$$

Range of the principal value of $\sec ^{-1} \mathrm{x}=[0, \pi]-\left\{\frac{\pi}{2}\right\}$
Therefore, $\sec ^{-1}(-2)=\frac{2 \pi}{3}$
Thus,

$$
\begin{aligned}
\tan ^{-1} \sqrt{3}-\sec ^{-1}(-2) & =\frac{\pi}{3}-\frac{2 \pi}{3} \\
& =-\frac{\pi}{3}
\end{aligned}
$$
:::

:::answer
**Answer:** Option (B)
:::

:::

:::question{number="1" kind="exercise" id="q_2.2.1" topic="Prove triple-angle sine identity"}
#### Question 1

:::prompt
Prove $3 \sin ^{-1} x=\sin ^{-1}\left(3 x-4 x^{3}\right), x \in\left[-\frac{1}{2}, \frac{1}{2}\right]$.
:::

:::solution{label="Solution"}
Let $x=8 \mathrm{in}$
Hence, $\sin ^{-1}(x)=$
Now,

$$
\begin{aligned}
\text { RHS } & =\sin ^{-1}\left(3 x-4 x^{3}\right) \\
& =\sin 4(\sin \sin - \\
& =\sin ^{-1}(\sin 3) \\
& =\theta \\
& =3 \sin ^{-1} x \\
& =L H S
\end{aligned}
$$
:::

:::

:::question{number="2" kind="exercise" id="q_2.2.2" topic="Prove triple-angle cosine identity"}
#### Question 2

:::prompt
Prove $3 \cos ^{-1} x=\cos ^{-1}\left(4 x^{3}-3 x\right), x \in\left[\frac{1}{2}, 1\right]$.
:::

:::solution{label="Solution"}
Let $x=\theta_{\mathrm{os}}$
Hence, $\operatorname{tos}^{-1}(x)=$
Now,

$$
\begin{aligned}
R H S & =\cos ^{-1}\left(4 x^{3}-3 x\right) \\
& =\theta \operatorname{os} 3^{1}\left(\operatorname{coscos} \sin ^{-}\right) \\
& =\cos ^{-1}(\cos 3) \\
& =\theta \\
& =3 \cos ^{-1} x \\
& =L H S
\end{aligned}
$$
:::

:::

:::question{number="3" kind="exercise" id="q_2.2.3" topic="Simplify inverse tangent expression"}
#### Question 3

:::prompt
$\tan ^{-1} \frac{\sqrt{1+x^{2}}-1}{x}, x \neq 0$
:::

:::solution{label="Solution"}
Let $x=\tan \theta \Rightarrow \theta=\tan ^{-1} x$
Hence,

$$
\begin{aligned}
\tan ^{-1} \frac{\sqrt{1+x^{2}}-1}{x} & =\tan ^{-1}\left(\frac{\sqrt{1+\tan ^{2} \theta}-1}{\tan \theta}\right) \\
& =\tan ^{-1}\left(\frac{\sec \theta-1}{\tan \theta}\right) \\
& =\tan ^{-1}\left(\frac{1-\cos \theta}{\sin \theta}\right) \\
& =\tan ^{-1}\left(\frac{2 \sin ^{2} \frac{\theta}{2}}{2 \sin \frac{\theta}{2} \cos \frac{\theta}{2}}\right) \\
& =\tan ^{-1}\left(\tan \frac{\theta}{2}\right) \\
& =\frac{\theta}{2} \\
& =\frac{1}{2} \tan ^{-1} x
\end{aligned}
$$
:::

:::answer
**Answer:** $\frac{1}{2} \tan ^{-1} x$
:::

:::

:::question{number="4" kind="exercise" id="q_2.2.4" topic="Simplify inverse tangent expression"}
#### Question 4

:::prompt
$\tan ^{-1}\left(\sqrt{\frac{1-\cos x}{1+\cos x}}\right), 0<x<\pi$
:::

:::solution{label="Solution"}
Since, $1-\cos x=2 \sin ^{2} \frac{x}{2}$ and $1+\cos x=2 \cos ^{2} \frac{x}{2}$
Hence,

$$
\begin{aligned}
\tan ^{-1}\left(\sqrt{\frac{1-\cos x}{1+\cos x}}\right) & =\tan ^{-1}\left(\sqrt{\frac{2 \sin ^{2} \frac{x}{2}}{2 \cos ^{2} \frac{x}{2}}}\right) \\
& =\tan ^{-1}\left(\frac{\sin \frac{x}{2}}{\cos \frac{x}{2}}\right) \\
& =\tan ^{-1}\left(\tan \frac{x}{2}\right) \\
& =\frac{x}{2}
\end{aligned}
$$
:::

:::answer
**Answer:** $\frac{x}{2}$
:::

:::

:::question{number="5" kind="exercise" id="q_2.2.5" topic="Simplify inverse tangent expression"}
#### Question 5

:::prompt
$\tan ^{-1}\left(\frac{\cos x-\sin x}{\cos x+\sin x}\right), \frac{-\pi}{4}<x<\frac{3 \pi}{4}$
:::

:::solution{label="Solution"}
$$
\begin{aligned}
\tan ^{-1}\left(\frac{\cos x-\sin x}{\cos x+\sin x}\right) & =\tan ^{-1}\left(\frac{\frac{\cos x-\sin x}{\cos x}}{\frac{\cos x+\sin x}{\cos x}}\right) \\
& =\tan ^{-1}\left(\frac{1-\frac{\sin x}{\cos x}}{1+\frac{\sin x}{\cos x}}\right) \\
& =\tan ^{-1}\left(\frac{1-\tan x}{1+\tan x}\right) \\
& =\tan ^{-1}(1)-\tan ^{-1}(\tan x) \\
& =\frac{\pi}{4}-x
\end{aligned}
$$
:::

:::answer
**Answer:** $\frac{\pi}{4}-x$
:::

:::

:::question{number="6" kind="exercise" id="q_2.2.6" topic="Simplify inverse tangent expression"}
#### Question 6

:::prompt
$\tan ^{-1} \frac{x}{\sqrt{a^{2}-x^{2}}},|x|<a$
:::

:::solution{label="Solution"}
Let

$$
x=a \sin \theta \Rightarrow \theta=\sin ^{-1}\left(\frac{x}{a}\right)
$$

Hence,

$$
\begin{aligned}
\tan ^{-1} \frac{x}{\sqrt{a^{2}-x^{2}}} & =\tan ^{-1}\left(\frac{a \sin \theta}{\sqrt{a^{2}-a^{2} \sin ^{2} \theta}}\right) \\
& =\tan ^{-1}\left(\frac{a \sin \theta}{a \sqrt{1-\sin ^{2} \theta}}\right) \\
& =\tan ^{-1}\left(\frac{a \sin \theta}{a \cos \theta}\right) \\
& =\tan ^{-1}(\tan \theta) \\
& =\theta \\
& =\sin ^{-1} \frac{x}{a}
\end{aligned}
$$
:::

:::answer
**Answer:** $\sin ^{-1} \frac{x}{a}$
:::

:::

:::question{number="7" kind="exercise" id="q_2.2.7" topic="Simplify inverse tangent expression"}
#### Question 7

:::prompt
$\tan ^{-1}\left(\frac{3 a^{2} x-x^{3}}{a^{3}-3 a x^{2}}\right), a>0 ; \frac{-a}{\sqrt{3}}<x<\frac{a}{\sqrt{3}}$
:::

:::solution{label="Solution"}
Let $x=a \tan \theta \Rightarrow \theta=\tan ^{-1}\left(\frac{x}{a}\right)$
Hence,

$$
\begin{aligned}
\tan ^{-1}\left(\frac{3 a^{2} x-x^{3}}{a^{3}-3 a x^{2}}\right) & =\tan ^{-1}\left(\frac{3 a^{2} \cdot a \tan \theta-a^{3} \tan ^{3} \theta}{a^{3}-3 a \cdot a^{2} \tan ^{2} \theta}\right) \\
& =\tan ^{-1}\left(\frac{3 a^{3} \tan \theta-a^{3} \tan ^{3} \theta}{a^{3}-3 a^{3} \tan ^{2} \theta}\right) \\
& =\tan ^{-1}(\tan 3 \theta) \\
& =3 \theta \\
& =3 \tan ^{-1} \frac{x}{a}
\end{aligned}
$$
:::

:::answer
**Answer:** $3 \tan ^{-1} \frac{x}{a}$
:::

:::

:::question{number="8" kind="exercise" id="q_2.2.8" topic="Value of nested inverse trig expression"}
#### Question 8

:::prompt
$\tan ^{-1}\left[2 \cos \left(2 \sin ^{-1} \frac{1}{2}\right)\right]$
:::

:::solution{label="Solution"}
Let $\sin ^{-1} \frac{1}{2}=x$
Hence,

$$
\begin{aligned}
\sin x & =\frac{1}{2} \\
& =\sin \left(\frac{\pi}{6}\right) \\
x & =\frac{\pi}{6} \\
\sin ^{-1}\left(\frac{1}{2}\right) & =\frac{\pi}{6}
\end{aligned}
$$

Therefore,

$$
\begin{aligned}
\tan ^{-1}\left[2 \cos \left(2 \sin ^{-1} \frac{1}{2}\right)\right] & =\tan ^{-1}\left[2 \cos \left(2 \times \frac{\pi}{6}\right)\right] \\
& =\tan ^{-1}\left[2 \cos \frac{\pi}{3}\right] \\
& =\tan ^{-1}\left[2 \times \frac{1}{2}\right] \\
& =\tan ^{-1}[1] \\
& =\frac{\pi}{4}
\end{aligned}
$$
:::

:::answer
**Answer:** $\frac{\pi}{4}$
:::

:::

:::question{number="9" kind="exercise" id="q_2.2.9" topic="Value of combined inverse trig expression"}
#### Question 9

:::prompt
$\tan \frac{1}{2}\left[\sin ^{-1} \frac{2 x}{1+x^{2}}+\cos ^{-1} \frac{1-y^{2}}{1+y^{2}}\right],|x|<1, y>0$ and $x y<1$
:::

:::solution{label="Solution"}
Let $x=\tan \theta \Rightarrow \theta=\tan ^{-1} x$
Hence,

$$
\begin{aligned}
\sin ^{-1} \frac{2 x}{1+x^{2}} & =\sin ^{-1}\left(\frac{2 \tan \theta}{1+\tan ^{2} \theta}\right) \\
& =\sin ^{-1}(\sin 2 \theta) \\
& =2 \theta \\
& =2 \tan ^{-1} x
\end{aligned}
$$

Now, let $y=\tan \phi \Rightarrow \phi=\tan ^{-1} y$
Hence,

$$
\begin{aligned}
\cos ^{-1} \frac{1-y^{2}}{1+y^{2}} & =\cos ^{-1}\left(\frac{1-\tan ^{2} \phi}{1+\tan ^{2} \phi}\right) \\
& =\cos ^{-1}(\cos 2 \phi) \\
& =2 \phi \\
& =2 \tan ^{-1} y
\end{aligned}
$$

Therefore,

$$
\begin{aligned}
\tan \frac{1}{2}\left(\sin ^{-1} \frac{2 x}{1+x^{2}}+\cos ^{-1} \frac{1-y^{2}}{1+y^{2}}\right) & =\tan \frac{1}{2}\left(2 \tan ^{-1} x+2 \tan ^{-1} y\right) \\
& =\tan \left(\tan ^{-1} x+\tan ^{-1} y\right) \\
& =\tan \left[\tan ^{-1}\left(\frac{x+y}{1-x y}\right)\right] \\
& =\left(\frac{x+y}{1-x y}\right)
\end{aligned}
$$
:::

:::answer
**Answer:** $\frac{x+y}{1-x y}$
:::

:::

:::question{number="10" kind="exercise" id="q_2.2.10" topic="Value of sin^-1(sin x) outside principal range"}
#### Question 10

:::prompt
$\sin ^{-1}\left(\sin \frac{2 \pi}{3}\right)$
:::

:::solution{label="Solution"}
Since, ${ }^{\text {θin }}$ sin ( $\theta-$ )
Therefore,

$$
\begin{aligned}
\sin ^{-1}\left(\sin \frac{2 \pi}{3}\right) & =\sin ^{-1}\left[\sin \left(\pi-\frac{2 \pi}{3}\right)\right] \\
& =\sin ^{-1}\left(\sin \frac{\pi}{3}\right) \\
& =\frac{\pi}{3}
\end{aligned}
$$
:::

:::answer
**Answer:** $\frac{\pi}{3}$
:::

:::

:::question{number="11" kind="exercise" id="q_2.2.11" topic="Value of tan^-1(tan x) outside principal range"}
#### Question 11

:::prompt
$\tan ^{-1}\left(\tan \frac{3 \pi}{4}\right)$
:::

:::solution{label="Solution"}
Since, ${ }^{\text {tan } \tan }(\theta-)$
Therefore,

$$
\begin{aligned}
\tan ^{-1}\left(\tan \frac{3 \pi}{4}\right) & =\tan ^{-1}\left[-\tan \left(-\frac{3 \pi}{4}\right)\right] \\
& =\tan ^{-1}\left[-\tan \left(\pi-\frac{\pi}{4}\right)\right] \\
& =\tan ^{-1}\left[-\tan \left(\frac{\pi}{4}\right)\right] \\
& =\tan ^{-1}\left[\tan \left(-\frac{\pi}{4}\right)\right] \\
& =\left(-\frac{\pi}{4}\right)
\end{aligned}
$$
:::

:::answer
**Answer:** $-\frac{\pi}{4}$
:::

:::

:::question{number="12" kind="exercise" id="q_2.2.12" topic="Value of combined inverse trig expression"}
#### Question 12

:::prompt
$\tan \left(\sin ^{-1} \frac{3}{5}+\cot ^{-1} \frac{3}{2}\right)$
:::

:::solution{label="Solution"}
Let $\sin ^{-1} \frac{3}{5}=x \Rightarrow \sin x=\frac{3}{5}$
Then,

$$
\begin{aligned}
& \Rightarrow \cos x=\sqrt{1-\sin ^{2} x}=\frac{4}{5} \\
& \Rightarrow \sec x=\frac{5}{4}
\end{aligned}
$$

Therefore,

$$
\begin{aligned}
\tan x & =\sqrt{\sec ^{2} x-1} \\
& =\sqrt{\frac{25}{16}-1} \\
& =\frac{3}{4} \\
x & =\tan ^{-1} \frac{3}{4} \\
\sin ^{-1} \frac{3}{5} & =\tan ^{-1} \frac{3}{4}
\end{aligned}
$$

Now,

$$
\cot ^{-1} \frac{3}{2}=\tan ^{-1} \frac{2}{3}
$$

Thus, by using (1) and (2)

$$
\begin{aligned}
\tan \left(\sin ^{-1} \frac{3}{5}+\cot ^{-1} \frac{2}{3}\right) & =\tan \left(\tan ^{-1} \frac{3}{4}+\tan ^{-1} \frac{2}{3}\right) \\
& =\tan \left[\tan ^{-1} \frac{\frac{3}{4}+\frac{2}{3}}{1-\frac{3}{4} \cdot \frac{2}{3}}\right] \\
& =\tan \left(\tan ^{-1} \frac{17}{6}\right) \\
& =\frac{17}{6}
\end{aligned}
$$
:::

:::answer
**Answer:** $\frac{17}{6}$
:::

:::

:::question{number="13" kind="exercise" id="q_2.2.13" topic="Value of cos^-1(cos x) outside principal range (multiple choice)"}
#### Question 13

:::prompt
$\cos ^{-1}\left(\cos \frac{7 \pi}{6}\right)$ is equal to
(A) $\frac{7 \pi}{6}$
(B) $\frac{5 \pi}{6}$
(C) $\frac{\pi}{3}$
(D) $\frac{\pi}{6}$
:::

:::solution{label="Solution"}
$$
\begin{aligned}
\cos ^{-1}\left(\cos \frac{7 \pi}{6}\right) & =\cos ^{-1}\left(\cos \frac{-7 \pi}{6}\right) \\
& =\cos ^{-1}\left[\cos \left(2 \pi-\frac{7 \pi}{6}\right)\right] \\
& =\cos ^{-1}\left[\cos \left(\frac{5 \pi}{6}\right)\right] \\
& =\frac{5 \pi}{6}
\end{aligned}
$$

Thus, the correct option is B.
:::

:::answer
**Answer:** Option (B)
:::

:::

:::question{number="14" kind="exercise" id="q_2.2.14" topic="Value of trig expression with inverse sine (multiple choice)"}
#### Question 14

:::prompt
$\sin \left(\frac{\pi}{3}-\sin ^{-1}\left(-\frac{1}{2}\right)\right)$ is equal to
(A) $\frac{1}{2}$
(B) $\frac{1}{3}$
(C) $\frac{1}{4}$
(D) 1
:::

:::solution{label="Solution"}
Let $\sin ^{-1}\left(-\frac{1}{2}\right)=x$
Hence,

$$
\begin{aligned}
\sin x & =-\frac{1}{2} \\
& =-\sin \frac{\pi}{6} \\
& =\sin \left(-\frac{\pi}{6}\right) \\
x & =-\frac{\pi}{6}
\end{aligned}
$$

Since, Range of principal value of $\sin ^{-1}(x)=\left[\frac{-\pi}{2}, \frac{\pi}{2}\right]$.
Therefore,

$$
\sin ^{-1}\left(-\frac{1}{2}\right)=-\frac{\pi}{6}
$$

Then,

$$
\begin{aligned}
\sin \left(\frac{\pi}{3}-\sin ^{-1}\left(-\frac{1}{2}\right)\right) & =\sin \left(\frac{\pi}{3}+\frac{\pi}{6}\right) \\
& =\sin \left(\frac{\pi}{2}\right) \\
& =1
\end{aligned}
$$

Thus, the correct option is D.
:::

:::answer
**Answer:** Option (D)
:::

:::

:::question{number="15" kind="exercise" id="q_2.2.15" topic="Difference of inverse trig values (multiple choice)"}
#### Question 15

:::prompt
$\tan ^{-1} \sqrt{3}-\cot ^{-1}(-\sqrt{3})$ is equal to
(A) $\pi$
(B) $-\frac{\pi}{2}$
(C) 0
(D) $2 \sqrt{3}$
:::

:::solution{label="Solution"}
Let $\tan ^{-1} \sqrt{3}=x$
Hence,

$$
\tan x=\sqrt{3}=\tan \frac{\pi}{3} \text {, where } \frac{\pi}{3} \in\left(-\frac{\pi}{2}, \frac{\pi}{2}\right)
$$

Therefore, $\tan ^{-1} \sqrt{3}=\frac{\pi}{3}$
Now, let $\cot ^{-1}(-\sqrt{3})=y$

Hence,

$$
\begin{aligned}
\cot y & =(-\sqrt{3}) \\
& =-\cot \left(\frac{\pi}{6}\right) \\
& =\cot \left(\pi-\frac{\pi}{6}\right) \\
& =\cot \left(\frac{5 \pi}{6}\right)
\end{aligned}
$$

Since, Range of principal value of $\cot ^{-1} x=(0, \pi)$ Therefore,

$$
\cot ^{-1}(-\sqrt{3})=\frac{5 \pi}{6}
$$

Then,

$$
\begin{aligned}
\tan ^{-1} \sqrt{3}-\cot ^{-1}(-\sqrt{3}) & =\frac{\pi}{3}-\frac{5 \pi}{6} \\
& =-\frac{\pi}{2}
\end{aligned}
$$

Thus, the correct option is B.
:::

:::answer
**Answer:** Option (B)
:::

:::

## Additional Questions

:::question{number="1" kind="additional_exercise" id="q_2.3.1" topic="Value of cos^-1(cos x) outside principal range"}
#### Additional Question 1

:::prompt
$\cos ^{-1}\left(\cos \frac{13 \pi}{6}\right)$
:::

:::solution{label="Solution"}
$$
\begin{aligned}
\cos ^{-1}\left(\cos \frac{13 \pi}{6}\right) & =\cos ^{-1}\left[\cos \left(2 \pi+\frac{\pi}{6}\right)\right] \\
& =\cos ^{-1}\left[\cos \frac{\pi}{6}\right] \\
& =\frac{\pi}{6}
\end{aligned}
$$
:::

:::answer
**Answer:** $\frac{\pi}{6}$
:::

:::

:::question{number="2" kind="additional_exercise" id="q_2.3.2" topic="Value of tan^-1(tan x) outside principal range"}
#### Additional Question 2

:::prompt
$\tan ^{-1}\left(\tan \frac{7 \pi}{6}\right)$
:::

:::solution{label="Solution"}
$$
\begin{aligned}
\tan ^{-1}\left(\tan \frac{7 \pi}{6}\right) & =\tan ^{-1}\left[\tan \left(2 \pi-\frac{5 \pi}{6}\right)\right] \\
& =\tan ^{-1}\left[-\tan \left(\frac{5 \pi}{6}\right)\right] \\
& =\tan ^{-1}\left[\tan \left(\pi-\frac{5 \pi}{6}\right)\right] \\
& =\tan ^{-1}\left[\tan \frac{\pi}{6}\right] \\
& =\frac{\pi}{6}
\end{aligned}
$$
:::

:::answer
**Answer:** $\frac{\pi}{6}$
:::

:::

:::question{number="3" kind="additional_exercise" id="q_2.3.3" topic="Prove sine-to-tangent double-angle identity"}
#### Additional Question 3

:::prompt
Prove that $2 \sin ^{-1} \frac{3}{5}=\tan ^{-1} \frac{24}{7}$
:::

:::solution{label="Solution"}
Let $\sin ^{-1} \frac{3}{5}=x \Rightarrow \sin x=\frac{3}{5}$
Then,

$$
\cos x=\sqrt{1-\left(\frac{3}{5}\right)^{2}}=\frac{4}{5}
$$

Therefore,

$$
\begin{aligned}
\tan x & =\frac{3}{4} \\
x & =\tan ^{-1} \frac{3}{4} \\
\sin ^{-1} \frac{3}{5} & =\tan ^{-1} \frac{3}{4}
\end{aligned}
$$

Thus,

$$
\begin{aligned}
\text { LHS } & =2 \sin ^{-1} \frac{3}{5} \\
& =2 \tan ^{-1} \frac{3}{4} \quad \text { [from (1)] } \\
& =\tan ^{-1}\left(\frac{2 \times \frac{3}{4}}{1-\left(\frac{3}{4}\right)^{2}}\right) \\
& =\tan ^{-1}\left(\frac{24}{7}\right) \\
& =\text { RHS }
\end{aligned}
$$
:::

:::

:::question{number="4" kind="additional_exercise" id="q_2.3.4" topic="Sum of two inverse sines as inverse tangent"}
#### Additional Question 4

:::prompt
Prove that $\sin ^{-1} \frac{8}{17}+\sin ^{-1} \frac{3}{5}=\tan ^{-1} \frac{77}{36}$
:::

:::solution{label="Solution"}
Let $\sin ^{-1} \frac{8}{17}=x \Rightarrow \sin x=\frac{8}{17}$
Then,

$$
\cos x=\sqrt{1-\left(\frac{8}{17}\right)^{2}}=\sqrt{\frac{225}{289}}=\frac{15}{17}
$$

Therefore,

$$
\begin{aligned}
\tan x & =\frac{8}{15} \\
x & =\tan ^{-1} \frac{8}{15} \\
\sin ^{-1} \frac{8}{17} & =\tan ^{-1} \frac{8}{15}
\end{aligned}
$$

Now, let $\sin ^{-1} \frac{3}{5}=y \Rightarrow \sin y=\frac{3}{5}$
Then,

$$
\cos y=\sqrt{1-\left(\frac{3}{5}\right)^{2}}=\sqrt{\frac{16}{25}}=\frac{4}{5}
$$

Therefore,

$$
\begin{aligned}
\tan y & =\frac{3}{4} \\
y & =\tan ^{-1} \frac{3}{4} \\
\sin ^{-1} \frac{3}{5} & =\tan ^{-1} \frac{3}{4}
\end{aligned}
$$

Thus, by using (1) and (2)

$$
\begin{aligned}
\text { LHS } & =\sin ^{-1} \frac{8}{17}+\sin ^{-1} \frac{3}{5} \\
& =\tan ^{-1} \frac{8}{15}+\tan ^{-1} \frac{3}{4} \\
& =\tan ^{-1}\left[\frac{\frac{8}{15}+\frac{3}{4}}{1-\frac{8}{15} \cdot \frac{3}{4}}\right] \\
& =\tan ^{-1}\left[\frac{\frac{32+45}{60}}{\frac{60-24}{60}}\right] \\
& =\tan ^{-1} \frac{77}{36} \\
& =\text { RHS }
\end{aligned}
$$
:::

:::

:::question{number="5" kind="additional_exercise" id="q_2.3.5" topic="Sum of two inverse cosines as another inverse cosine"}
#### Additional Question 5

:::prompt
Prove that $\cos ^{-1} \frac{4}{5}+\cos ^{-1} \frac{12}{13}=\cos ^{-1} \frac{33}{65}$
:::

:::solution{label="Solution"}
Let $\cos ^{-1} \frac{4}{5}=x \Rightarrow \cos x=\frac{4}{5}$
Then,

$$
\sin x=\sqrt{1-\left(\frac{4}{5}\right)^{2}}=\frac{3}{5}
$$

Therefore,

$$
\begin{aligned}
\tan x & =\frac{3}{4} \\
x & =\tan ^{-1} \frac{3}{4} \\
\cos ^{-1} \frac{4}{5} & =\tan ^{-1} \frac{3}{4}
\end{aligned}
$$

Now, let $\cos ^{-1} \frac{12}{13}=y \Rightarrow \cos y=\frac{12}{13}$

Then,

$$
\sin y=\frac{5}{13}
$$

Therefore,

$$
\begin{aligned}
\tan y & =\frac{5}{12} \\
y & =\tan ^{-1} \frac{5}{12} \\
\cos ^{-1} \frac{12}{13} & =\tan ^{-1} \frac{5}{12}
\end{aligned}
$$

Thus, by using (1) and (2)

$$
\begin{aligned}
\cos ^{-1} \frac{4}{5}+\cos ^{-1} \frac{12}{13} & =\tan ^{-1} \frac{3}{4}+\tan ^{-1} \frac{5}{12} \\
& =\tan ^{-1}\left[\frac{\frac{3}{4}+\frac{5}{12}}{1-\frac{3}{4} \cdot \frac{5}{12}}\right] \\
& =\tan ^{-1}\left[\frac{56}{33}\right]
\end{aligned}
$$

Now, let $\cos ^{-1} \frac{33}{65}=z \Rightarrow \cos z=\frac{33}{65}$
Then,

$$
\sin z=\sqrt{1-\left(\frac{33}{65}\right)^{2}}=\frac{56}{65}
$$

Therefore,

$$
\begin{aligned}
\tan z & =\frac{33}{56} \\
z & =\tan ^{-1} \frac{56}{33} \\
\cos ^{-1} \frac{33}{65} & =\tan ^{-1} \frac{56}{33}
\end{aligned}
$$

Thus, by using (3) and (4)

$$
\cos ^{-1} \frac{4}{5}+\cos ^{-1} \frac{12}{13}=\cos ^{-1} \frac{33}{65}
$$

Hence proved.
:::

:::

:::question{number="6" kind="additional_exercise" id="q_2.3.6" topic="Sum of inverse cosine and inverse sine as another inverse sine"}
#### Additional Question 6

:::prompt
Prove that $\cos ^{-1} \frac{12}{13}+\sin ^{-1} \frac{3}{5}=\sin ^{-1} \frac{56}{65}$
:::

:::solution{label="Solution"}
Let $\cos ^{-1} \frac{12}{13}=y \Rightarrow \cos y=\frac{12}{13}$
Then,

$$
\sin y=\sqrt{1-\left(\frac{12}{13}\right)^{2}}=\frac{5}{13}
$$

Therefore,

$$
\begin{aligned}
\tan y & =\frac{5}{12} \\
y & =\tan ^{-1} \frac{5}{12} \\
\cos ^{-1} \frac{12}{13} & =\tan ^{-1} \frac{5}{12}
\end{aligned}
$$

Now, let $\sin ^{-1} \frac{3}{5}=x \Rightarrow \sin x=\frac{3}{5}$
Then,

$$
\cos x=\sqrt{1-\left(\frac{3}{5}\right)^{2}}=\frac{4}{5}
$$

Therefore,

$$
\begin{aligned}
\tan x & =\frac{3}{4} \\
x & =\tan ^{-1} \frac{3}{4} \\
\sin ^{-1} \frac{3}{5} & =\tan ^{-1} \frac{3}{4}
\end{aligned}
$$

Now, let $\sin ^{-1} \frac{56}{65}=z \Rightarrow \sin z=\frac{56}{65}$
Then,

$$
\cos z=\sqrt{1-\left(\frac{56}{65}\right)^{2}}=\frac{33}{65}
$$

Therefore,

$$
\begin{aligned}
& \tan z=\frac{56}{33} \\
& z=\tan ^{-1} \frac{56}{33} \\
& \sin ^{-1} \frac{56}{65}=\tan ^{-1} \frac{56}{33}
\end{aligned}
$$

Thus, by using (1) and (2)

$$
\begin{aligned}
\text { LHS } & =\cos ^{-1} \frac{12}{13}+\sin ^{-1} \frac{3}{5} \\
& =\tan ^{-1} \frac{5}{12}+\tan ^{-1} \frac{3}{4} \\
& =\tan ^{-1}\left[\frac{\frac{5}{12}+\frac{3}{4}}{1-\frac{5}{12} \cdot \frac{3}{4}}\right] \\
& =\tan ^{-1}\left[\frac{\frac{20+36}{48}}{\frac{48-15}{48}}\right] \\
& =\tan ^{-1}\left(\frac{56}{33}\right) \\
& =\sin ^{-1} \frac{56}{65} \quad \text { [Using (3)] } \\
& =\text { RHS }
\end{aligned}
$$
:::

:::

:::question{number="7" kind="additional_exercise" id="q_2.3.7" topic="Inverse tangent as sum of inverse sine and inverse cosine"}
#### Additional Question 7

:::prompt
Prove that $\tan ^{-1} \frac{63}{16}=\sin ^{-1} \frac{5}{13}+\cos ^{-1} \frac{3}{5}$
:::

:::solution{label="Solution"}
Let $\sin ^{-1} \frac{5}{13}=x \Rightarrow \sin x=\frac{5}{13}$
Then,

$$
\cos x=\sqrt{1-\left(\frac{5}{13}\right)^{2}}=\frac{12}{13}
$$

Therefore,

$$
\begin{aligned}
\tan x & =\frac{5}{12} \\
x & =\tan ^{-1} \frac{5}{12} \\
\sin ^{-1} \frac{5}{13} & =\tan ^{-1} \frac{5}{12}
\end{aligned}
$$

Now, let $\cos ^{-1} \frac{3}{5}=y \Rightarrow \cos y=\frac{3}{5}$
Then,

$$
\sin y=\sqrt{1-\left(\frac{3}{5}\right)^{2}}=\frac{4}{5}
$$

Therefore,

$$
\begin{aligned}
\tan y & =\frac{4}{3} \\
y & =\tan ^{-1} \frac{4}{3} \\
\cos ^{-1} \frac{3}{5} & =\tan ^{-1} \frac{4}{3}
\end{aligned}
$$

Thus, by using (1) and (2)

$$
\begin{aligned}
\text { RHS } & =\sin ^{-1} \frac{5}{13}+\cos ^{-1} \frac{3}{5} \\
& =\tan ^{-1} \frac{5}{12}+\tan ^{-1} \frac{4}{3} \\
& =\tan ^{-1}\left(\frac{\frac{5}{12}+\frac{4}{3}}{1-\frac{5}{12} \cdot \frac{4}{3}}\right) \\
& =\tan ^{-1}\left(\frac{63}{16}\right) \\
& =L H S
\end{aligned}
$$
:::

:::

:::question{number="8" kind="additional_exercise" id="q_2.3.8" topic="Inverse tangent of √x"}
#### Additional Question 8

:::prompt
Prove that $\tan ^{-1} \sqrt{x}=\frac{1}{2} \cos ^{-1} \frac{1-x}{1+x}, x \in[0,1]$
:::

:::solution{label="Solution"}
Let $x=\tan ^{2} \theta$
Then,

$$
\begin{aligned}
\sqrt{x} & =\tan \theta \\
\theta & =\tan ^{-1} \sqrt{x}
\end{aligned}
$$

Therefore,

$$
\begin{aligned}
\left(\frac{1-x}{1+x}\right) & =\frac{1-\tan ^{2} \theta}{1+\tan ^{2} \theta} \\
& =\cos 2 \theta
\end{aligned}
$$

Thus,

$$
\begin{aligned}
\text { RHS } & =\frac{1}{2} \cos ^{-1}\left(\frac{1-x}{1+x}\right) \\
& =\frac{1}{2} \cos ^{-1}(\cos 2 \theta) \\
& =\frac{1}{2} \times 2 \theta \\
& =\theta \\
& =\tan ^{-1} \sqrt{x} \\
& =\text { I.HS }
\end{aligned}
$$
:::

:::

:::question{number="9" kind="additional_exercise" id="q_2.3.9" topic="Inverse cotangent of a trigonometric ratio"}
#### Additional Question 9

:::prompt
Prove that $\cot ^{-1}\left(\frac{\sqrt{1+\sin x}+\sqrt{1-\sin x}}{\sqrt{1+\sin x}-\sqrt{1-\sin x}}\right)=\frac{x}{2}, x \in\left(0, \frac{\pi}{4}\right)$
:::

:::solution{label="Solution"}
$$
\begin{aligned}
\left(\frac{\sqrt{1+\sin x}+\sqrt{1-\sin x}}{\sqrt{1+\sin x}-\sqrt{1-\sin x}}\right) & =\frac{(\sqrt{1+\sin x}+\sqrt{1-\sin x})^{2}}{(\sqrt{1+\sin x})^{2}-(\sqrt{1-\sin x})^{2}} \quad \text { (by rationalizing) } \\
& =\frac{(1+\sin x)+(1-\sin x)+2 \sqrt{(1+\sin x)(1-\sin x)}}{1+\sin x-1+\sin x} \\
& =\frac{2\left(1+\sqrt{1-\sin ^{2} x}\right)}{2 \sin x}=\frac{1+\cos x}{\sin x} \\
& =\frac{2 \cos ^{2} \frac{x}{2}}{2 \sin \frac{x}{2} \cos \frac{x}{2}} \\
& =\cot \frac{x}{2}
\end{aligned}
$$

Thus,

$$
\begin{aligned}
L H S & =\cot ^{-1}\left(\frac{\sqrt{1+\sin x}+\sqrt{1-\sin x}}{\sqrt{1+\sin x}-\sqrt{1-\sin x}}\right) \\
& =\cot ^{-1}\left(\cot \frac{x}{2}\right) \\
& =\frac{x}{2} \\
& =R H S
\end{aligned}
$$
:::

:::

:::question{number="10" kind="additional_exercise" id="q_2.3.10" topic="Inverse tangent of a ratio as a shifted half-inverse-cosine"}
#### Additional Question 10

:::prompt
Prove that $\tan ^{-1}\left(\frac{\sqrt{1+x}-\sqrt{1-x}}{\sqrt{1+x}+\sqrt{1-x}}\right)=\frac{\pi}{4}-\frac{1}{2} \cos ^{-1} x,-\frac{1}{\sqrt{2}} \leq x \leq 1$ [Hint: Put $x=\cos 2 \theta$ ]
:::

:::solution{label="Solution"}
Let $x=\cos 2 \theta \Rightarrow \theta=\frac{1}{2} \cos ^{-1} x$
Thus,

$$
\begin{aligned}
\text { LHS } & =\tan ^{-1}\left(\frac{\sqrt{1+x}-\sqrt{1-x}}{\sqrt{1+x}+\sqrt{1-x}}\right) \\
& =\tan ^{-1}\left(\frac{\sqrt{1+\cos 2 \theta}-\sqrt{1-\cos 2 \theta}}{\sqrt{1+\cos 2 \theta}+\sqrt{1-\cos 2 \theta}}\right) \\
& =\tan ^{-1}\left(\frac{\sqrt{2 \cos ^{2} \theta}-\sqrt{2 \sin ^{2} \theta}}{\sqrt{2 \cos ^{2} \theta}+\sqrt{2 \sin ^{2} \theta}}\right) \\
& =\tan ^{-1}\left(\frac{\sqrt{2} \cos \theta-\sqrt{2} \sin \theta}{\sqrt{2} \cos \theta+\sqrt{2} \sin \theta}\right) \\
& =\tan ^{-1}\left(\frac{\cos \theta-\sin \theta}{\cos \theta+\sin \theta}\right) \\
& =\tan ^{-1}\left(\frac{1-\tan \theta}{1+\tan \theta}\right) \\
& =\tan ^{-1} 1-\tan ^{-1}(\tan \theta) \\
& =\frac{\pi}{4}-\theta \\
& =\frac{\pi}{4}-\frac{1}{2} \cos ^{-1} x \\
& =\text { RHS }
\end{aligned}
$$
:::

:::

:::question{number="11" kind="additional_exercise" id="q_2.3.11" topic="Solve an inverse trig equation"}
#### Additional Question 11

:::prompt
Solve $2 \tan ^{-1}(\cos x)=\tan ^{-1}(2 \operatorname{cosec} x)$
:::

:::solution{label="Solution"}
It is given that $2 \tan ^{-1}(\cos x)=\tan ^{-1}(2 \operatorname{cosec} x)$
Since, $2 \tan ^{-1}(x)=\tan ^{-1} \frac{2 x}{1-x^{2}}$
Hence,

$$
\begin{aligned}
& \Rightarrow \tan ^{-1}\left(\frac{2 \cos x}{1-\cos ^{2} x}\right)=\tan ^{-1}(2 \operatorname{cosec} x) \\
& \Rightarrow\left(\frac{2 \cos x}{1-\cos ^{2} x}\right)=(2 \operatorname{cosec} x) \\
& \Rightarrow \frac{2 \cos x}{\sin ^{2} x}=\frac{2}{\sin x} \\
& \Rightarrow \cos x=\sin x \\
& \Rightarrow \tan x=1 \\
& \Rightarrow \tan x=\tan \frac{\pi}{4}
\end{aligned}
$$

Therefore,

$$
x=n \pi+\frac{\pi}{4}, \text { where } n \in Z .
$$
:::

:::answer
**Answer:** $x=n \pi+\frac{\pi}{4}, n \in Z$
:::

:::

:::question{number="12" kind="additional_exercise" id="q_2.3.12" topic="Solve an inverse trig equation"}
#### Additional Question 12

:::prompt
Solve $\tan ^{-1} \frac{1-x}{1+x}=\frac{1}{2} \tan ^{-1} x,(x>0)$
:::

:::solution{label="Solution"}
Since $\tan ^{-1} x-\tan ^{-1} y=\tan ^{-1} \frac{x-y}{1+x y}$
Hence,

$$
\begin{aligned}
& \Rightarrow \tan ^{-1} \frac{1-x}{1+x}=\frac{1}{2} \tan ^{-1} x \\
& \Rightarrow \tan ^{-1} 1-\tan ^{-1} x=\frac{1}{2} \tan ^{-1} x \\
& \Rightarrow \frac{\pi}{4}=\frac{3}{2} \tan ^{-1} x \\
& \Rightarrow \tan ^{-1} x=\frac{\pi}{6} \\
& \Rightarrow x=\tan \frac{\pi}{6} \\
& \Rightarrow x=\frac{1}{\sqrt{3}}
\end{aligned}
$$
:::

:::answer
**Answer:** $x=\frac{1}{\sqrt{3}}$
:::

:::

:::question{number="13" kind="additional_exercise" id="q_2.3.13" topic="Value of sin(tan^-1 x) (multiple choice)"}
#### Additional Question 13

:::prompt
$\sin \left(\tan ^{-1} x\right),|x|<1$ is equal to
(A) $\frac{x}{\sqrt{1-x^{2}}}$
(B) $\frac{1}{\sqrt{1-x^{2}}}$
(C) $\frac{1}{\sqrt{1+x^{2}}}$
(D) $\frac{x}{\sqrt{1+x^{2}}}$
:::

:::solution{label="Solution"}
Let $\tan y=x$
Therefore,

$$
\sin y=\frac{x}{\sqrt{1+x^{2}}}
$$

Now, let $\tan ^{-1} x=y$
Therefore,

$$
y=\sin ^{-1}\left(\frac{x}{\sqrt{1+x^{2}}}\right)
$$

Hence,

$$
\tan ^{-1} x=\sin ^{-1}\left(\frac{x}{\sqrt{1+x^{2}}}\right)
$$

Thus,

$$
\begin{aligned}
\sin \left(\tan ^{-1} x\right) & =\sin \left(\sin ^{-1}\left(\frac{x}{\sqrt{1+x^{2}}}\right)\right) \\
& =\frac{x}{\sqrt{1+x^{2}}}
\end{aligned}
$$

Thus, the correct option is D.
:::

:::answer
**Answer:** Option (D)
:::

:::

:::question{number="14" kind="additional_exercise" id="q_2.3.14" topic="Solve an inverse-sine equation (multiple choice)"}
#### Additional Question 14

:::prompt
Solve: $\sin ^{-1}(1-x)-2 \sin ^{-1} x=\frac{\pi}{2}$, then $x$ is equal to
(A) $0, \frac{1}{2}$
(B) $1, \frac{1}{2}$
(C) 0
(D) $\frac{1}{2}$
:::

:::solution{label="Solution"}
It is given that $\sin ^{-1}(1-x)-2 \sin ^{-1} x=\frac{\pi}{2}$

$$
\begin{aligned}
& \Rightarrow \sin ^{-1}(1-x)-2 \sin ^{-1} x=\frac{\pi}{2} \\
& \Rightarrow-2 \sin ^{-1} x=\frac{\pi}{2}-\sin ^{-1}(1-x) \\
& \Rightarrow-2 \sin ^{-1} x=\cos ^{-1}(1-x)
\end{aligned}
$$

Let $\sin ^{-1} x=y \Rightarrow \sin y=x$
Hence,

$$
\begin{aligned}
\cos y & =\sqrt{1-x^{2}} \\
y & =\cos ^{-1}\left(\sqrt{1-x^{2}}\right) \\
\sin ^{-1} x & =\cos ^{-1} \sqrt{1-x^{2}}
\end{aligned}
$$

From equation (1), we have

$$
-2 \cos ^{-1} \sqrt{1-x^{2}}=\cos ^{-1}(1-x)
$$

Put $x=\sin y$

$$
\begin{aligned}
& \Rightarrow-2 \cos ^{-1} \sqrt{1-\sin ^{2} y}=\cos ^{-1}(1-\sin y) \\
& \Rightarrow-2 \cos ^{-1}(\cos y)=\cos ^{-1}(1-\sin y) \\
& \Rightarrow-2 y=\cos ^{-1}(1-\sin y) \\
& \Rightarrow 1-\sin y=\cos (-2 y) \\
& \Rightarrow 1-\sin y=\cos 2 y \\
& \Rightarrow 1-\sin y=1-2 \sin ^{2} y \\
& \Rightarrow 2 \sin ^{2} y-\sin y=0 \\
& \Rightarrow \sin y(2 \sin y-1)=0 \\
& \Rightarrow \sin y=0, \frac{1}{2}
\end{aligned}
$$

Therefore,

$$
x=0, \frac{1}{2}
$$

When $x=\frac{1}{2}$, it does not satisfy the equation.
Hence, $x=0$ is the only solution
Thus, the correct option is C.
:::

:::answer
**Answer:** Option (C)
:::

:::
