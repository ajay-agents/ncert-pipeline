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
