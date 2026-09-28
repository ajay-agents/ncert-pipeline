---
subject: maths
class: 12
chapter: 5
lang: en
title: "Continuity and Differentiability"
---

# Continuity and Differentiability

## Examples

:::example{number="1" kind="example" id="ex_5.1" topic="Example: f(x)=2 x+3"}
#### Example 1

:::prompt
Check the continuity of the function $f$ given by $f(x)=2 x+3$ at $x=1$.
:::

:::solution{label="Solution"}
Solution First note that the function is defined at the given point $x=1$ and its value is 5 . Then find the limit of the function at $x=1$. Clearly

Thus

$$
\begin{aligned}
& \lim _{x \rightarrow 1} f(x)=\lim _{x \rightarrow 1}(2 x+3)=2(1)+3=5 \\
& \lim _{x \rightarrow 1} f(x)=5=f(1)
\end{aligned}
$$

Hence, $f$ is continuous at $x=1$.
:::

:::

:::example{number="2" kind="example" id="ex_5.2" topic="Example: f(x)=x^2"}
#### Example 2

:::prompt
Examine whether the function $f$ given by $f(x)=x^{2}$ is continuous at $x=0$.
:::

:::solution{label="Solution"}
Solution First note that the function is defined at the given point $x=0$ and its value is 0 . Then find the limit of the function at $x=0$. Clearly

Thus

$$
\begin{aligned}
& \lim _{x \rightarrow 0} f(x)=\lim _{x \rightarrow 0} x^{2}=0^{2}=0 \\
& \lim _{x \rightarrow 0} f(x)=0=f(0)
\end{aligned}
$$

Hence, $f$ is continuous at $x=0$.
:::

:::

:::example{number="3" kind="example" id="ex_5.3" topic="Example: f(x)=|x|"}
#### Example 3

:::prompt
Discuss the continuity of the function $f$ given by $f(x)=|x|$ at $x=0$.
:::

:::solution{label="Solution"}
Solution By definition

$$
f(x)= \begin{cases}-x, & \text { if } x<0 \\ x, & \text { if } x \geq 0\end{cases}
$$

Clearly the function is defined at 0 and $f(0)=0$. Left hand limit of $f$ at 0 is

$$
\lim _{x \rightarrow 0^{-}} f(x)=\lim _{x \rightarrow 0^{-}}(-x)=0
$$

Similarly, the right hand limit of $f$ at 0 is

$$
\lim _{x \rightarrow 0^{+}} f(x)=\lim _{x \rightarrow 0^{+}} x=0
$$

Thus, the left hand limit, right hand limit and the value of the function coincide at $x=0$. Hence, $f$ is continuous at $x=0$.
:::

:::

:::example{number="4" kind="example" id="ex_5.4" topic="Example: piecewise function"}
#### Example 4

:::prompt
Show that the function $f$ given by

$$
f(x)= \begin{cases}x^{3}+3, & \text { if } x \neq 0 \\ 1, & \text { if } x=0\end{cases}
$$

is not continuous at $x=0$.
:::

:::solution{label="Solution"}
Solution The function is defined at $x=0$ and its value at $x=0$ is 1 . When $x \neq 0$, the function is given by a polynomial. Hence,

$$
\lim _{x \rightarrow 0} f(x)=\lim _{x \rightarrow 0}\left(x^{3}+3\right)=0^{3}+3=3
$$

Since the limit of $f$ at $x=0$ does not coincide with $f(0)$, the function is not continuous at $x=0$. It may be noted that $x=0$ is the only point of discontinuity for this function.
:::

:::

:::example{number="5" kind="example" id="ex_5.5" topic="Example: f(x)=k"}
#### Example 5

:::prompt
Check the points where the constant function $f(x)=k$ is continuous.
:::

:::solution{label="Solution"}
Solution The function is defined at all real numbers and by definition, its value at any real number equals $k$. Let $c$ be any real number. Then

$$
\lim _{x \rightarrow c} f(x)=\lim _{x \rightarrow c} k=k
$$

Since $f(c)=k=\lim _{x \rightarrow c} f(x)$ for any real number $c$, the function $f$ is continuous at every real number.
:::

:::

:::example{number="6" kind="example" id="ex_5.6" topic="Example: f(x)=x"}
#### Example 6

:::prompt
Prove that the identity function on real numbers given by $f(x)=x$ is continuous at every real number.
:::

:::solution{label="Solution"}
Solution The function is clearly defined at every point and $f(c)=c$ for every real number $c$. Also,

$$
\lim _{x \rightarrow c} f(x)=\lim _{x \rightarrow c} x=c
$$

Thus, $\lim _{x \rightarrow c} f(x)=c=f(c)$ and hence the function is continuous at every real number.
Having defined continuity of a function at a given point, now we make a natural extension of this definition to discuss continuity of a function.
Definition 2 A real function $f$ is said to be continuous if it is continuous at every point in the domain of $f$.

This definition requires a bit of elaboration. Suppose $f$ is a function defined on a closed interval $[a, b]$, then for $f$ to be continuous, it needs to be continuous at every point in $[a, b]$ including the end points $a$ and $b$. Continuity of $f$ at $a$ means

$$
\lim _{x \rightarrow a^{+}} f(x)=f(a)
$$

and continuity of $f$ at $b$ means

$$
\lim _{x \rightarrow b^{-}} f(x)=f(b)
$$

Observe that $\lim _{x \rightarrow a^{-}} f(x)$ and $\lim _{x \rightarrow b^{+}} f(x)$ do not make sense. As a consequence of this definition, if $f$ is defined only at one point, it is continuous there, i.e., if the domain of $f$ is a singleton, $f$ is a continuous function.
:::

:::

:::example{number="7" kind="example" id="ex_5.7" topic="Example: f(x)=|x|"}
#### Example 7

:::prompt
Is the function defined by $f(x)=|x|$, a continuous function?
:::

:::solution{label="Solution"}
Solution We may rewrite $f$ as

$$
f(x)= \begin{cases}-x, & \text { if } x<0 \\ x, & \text { if } x \geq 0\end{cases}
$$

By Example 3, we know that $f$ is continuous at $x=0$.
Let $c$ be a real number such that $c<0$. Then $f(c)=-c$. Also

$$
\lim _{x \rightarrow c} f(x)=\lim _{x \rightarrow c}(-x)=-c
$$

Since $\lim _{x \rightarrow c} f(x)=f(c), f$ is continuous at all negative real numbers.
Now, let $c$ be a real number such that $c>0$. Then $f(c)=c$. Also

$$
\lim _{x \rightarrow c} f(x)=\lim _{x \rightarrow c} x=c
$$

Since $\lim _{x \rightarrow c} f(x)=f(c), f$ is continuous at all positive real numbers. Hence, $f$ is continuous at all points.
:::

:::

:::example{number="8" kind="example" id="ex_5.8" topic="Example: f(x)=x^3+x^2-1"}
#### Example 8

:::prompt
Discuss the continuity of the function $f$ given by $f(x)=x^{3}+x^{2}-1$.
:::

:::solution{label="Solution"}
Solution Clearly $f$ is defined at every real number $c$ and its value at $c$ is $c^{3}+c^{2}-1$. We also know that

$$
\lim _{x \rightarrow c} f(x)=\lim _{x \rightarrow c}\left(x^{3}+x^{2}-1\right)=c^{3}+c^{2}-1
$$

Thus $\lim _{x \rightarrow c} f(x)=f(c)$, and hence $f$ is continuous at every real number. This means $f$ is a continuous function.
:::

:::

:::example{number="9" kind="example" id="ex_5.9" topic="Example: f(x)=1/x, x 0"}
#### Example 9

:::prompt
Discuss the continuity of the function $f$ defined by $f(x)=\frac{1}{x}, x \neq 0$.
:::

:::figure{src="images/fig_5_3.jpg" id="fig_5_3"}
Fig 5.3
:::

:::solution{label="Solution"}
Solution Fix any non zero real number $c$, we have

$$
\lim _{x \rightarrow c} f(x)=\lim _{x \rightarrow c} \frac{1}{x}=\frac{1}{c}
$$

Also, since for $c \neq 0, f(c)=\frac{1}{c}$, we have $\lim _{x \rightarrow c} f(x)=f(c)$ and hence, $f$ is continuous at every point in the domain of $f$. Thus $f$ is a continuous function.

We take this opportunity to explain the concept of infinity. This we do by analysing the function $f(x)=\frac{1}{x}$ near $x=0$. To carry out this analysis we follow the usual trick of finding the value of the function at real numbers close to 0. Essentially we are trying to find the right hand limit of $f$ at 0 . We tabulate this in the following (Table 5.1).

Table 5.1
| $x$ | 1 | 0.3 | 0.2 | $0.1=10^{-1}$ | $0.01=10^{-2}$ | $0.001=10^{-3}$ | $10^{-n}$ |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| $f(x)$ | 1 | 3.333... | 5 | 10 | $100=10^{2}$ | $1000=10^{3}$ | $10^{n}$ |

We observe that as $x$ gets closer to 0 from the right, the value of $f(x)$ shoots up higher. This may be rephrased as: the value of $f(x)$ may be made larger than any given number by choosing a positive real number very close to 0 . In symbols, we write

$$
\lim _{x \rightarrow 0^{+}} f(x)=+\infty
$$

(to be read as: the right hand limit of $f(x)$ at 0 is plus infinity). We wish to emphasise that $+\infty$ is NOT a real number and hence the right hand limit of $f$ at 0 does not exist (as a real number).

Similarly, the left hand limit of $f$ at 0 may be found. The following table is self explanatory.

Table 5.2
| $x$ | -1 | -0.3 | -0.2 | $-10^{-1}$ | $-10^{-2}$ | $-10^{-3}$ | $-10^{-n}$ |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| $f(x)$ | -1 | - 3.333... | -5 | - 10 | $-10^{2}$ | $-10^{3}$ | $-10^{n}$ |

From the Table 5.2, we deduce that the value of $f(x)$ may be made smaller than any given number by choosing a negative real number very close to 0 . In symbols, we write

$$
\lim _{x \rightarrow 0^{-}} f(x)=-\infty
$$

(to be read as: the left hand limit of $f(x)$ at 0 is minus infinity). Again, we wish to emphasise that $-\infty$ is NOT a real number and hence the left hand limit of $f$ at 0 does not exist (as a real number). The graph of the reciprocal function given in Fig 5.3 is a geometric representation of the above mentioned facts.
:::

:::

:::example{number="10" kind="example" id="ex_5.10" topic="Example: piecewise function"}
#### Example 10

:::prompt
Discuss the continuity of the function $f$ defined by

$$
f(x)=\left\{\begin{array}{l}
x+2, \text { if } x \leq 1 \\
x-2, \text { if } x>1
\end{array}\right.
$$
:::

:::figure{src="images/fig_5_4.jpg" id="fig_5_4"}
Fig 5.4
:::

:::solution{label="Solution"}
Solution The function $f$ is defined at all points of the real line.
Case 1 If $c<1$, then $f(c)=c+2$. Therefore, $\lim _{x \rightarrow c} f(x)=\lim _{x \rightarrow c}(x+2)=c+2$ Thus, $f$ is continuous at all real numbers less than 1 .
Case 2 If $c>1$, then $f(c)=c-2$. Therefore,

$$
\lim _{x \rightarrow c} f(x)=\lim _{x \rightarrow c}(x-2)=c-2=f(c)
$$

Thus, $f$ is continuous at all points $x>1$.
Case 3 If $c=1$, then the left hand limit of $f$ at $x=1$ is

$$
\lim _{x \rightarrow 1^{-}} f(x)=\lim _{x \rightarrow 1^{-}}(x+2)=1+2=3
$$

The right hand limit of $f$ at $x=1$ is

$$
\lim _{x \rightarrow 1^{+}} f(x)=\lim _{x \rightarrow 1^{+}}(x-2)=1-2=-1
$$

Since the left and right hand limits of $f$ at $x=1$

do not coincide, $f$ is not continuous at $x=1$. Hence $x=1$ is the only point of discontinuity of $f$. The graph of the function is given in Fig 5.4.
:::

:::

:::example{number="11" kind="example" id="ex_5.11" topic="Example: piecewise function"}
#### Example 11

:::prompt
Find all the points of discontinuity of the function $f$ defined by

$$
f(x)=\left\{\begin{array}{cc}
x+2, & \text { if } x<1 \\
0, & \text { if } x=1 \\
x-2, & \text { if } x>1
\end{array}\right.
$$
:::

:::figure{src="images/fig_5_5.jpg" id="fig_5_5"}
Fig 5.5
:::

:::solution{label="Solution"}
Solution As in the previous example we find that $f$ is continuous at all real numbers $x \neq 1$. The left hand limit of $f$ at $x=1$ is

$$
\lim _{x \rightarrow 1^{-}} f(x)=\lim _{x \rightarrow 1^{-}}(x+2)=1+2=3
$$

The right hand limit of $f$ at $x=1$ is

$$
\lim _{x \rightarrow 1^{+}} f(x)=\lim _{x \rightarrow 1^{+}}(x-2)=1-2=-1
$$

Since, the left and right hand limits of $f$ at $x=1$ do not coincide, $f$ is not continuous at $x=1$. Hence $x=1$ is the only point of discontinuity of $f$. The graph of the function is given in the Fig 5.5.
:::

:::

:::example{number="12" kind="example" id="ex_5.12" topic="Example: piecewise function"}
#### Example 12

:::prompt
Discuss the continuity of the function defined by

$$
f(x)=\left\{\begin{array}{r}
x+2, \text { if } x<0 \\
-x+2, \text { if } x>0
\end{array}\right.
$$
:::

:::figure{src="images/fig_5_6.jpg" id="fig_5_6"}
Fig 5.6
:::

:::solution{label="Solution"}
Solution Observe that the function is defined at all real numbers except at 0. Domain of definition of this function is

$$
\begin{aligned}
& \mathrm{D}_{1} \cup \mathrm{D}_{2} \text { where } \mathrm{D}_{1}=\{x \in \mathbf{R}: x<0\} \text { and } \\
& \mathrm{D}_{2}=\{x \in \mathbf{R}: x>0\}
\end{aligned}
$$

Case 1 If $c \in \mathrm{D}_{1}$, then $\lim _{x \rightarrow c} f(x)=\lim _{x \rightarrow c}(x+2)$ $=c+2=f(c)$ and hence $f$ is continuous in $\mathrm{D}_{1}$.

Case 2 If $c \in \mathrm{D}_{2}$, then $\lim _{x \rightarrow c} f(x)=\lim _{x \rightarrow c}(-x+2)$ $=-c+2=f(c)$ and hence $f$ is continuous in $\mathrm{D}_{2}$. Since $f$ is continuous at all points in the domain of $f$, we deduce that $f$ is continuous. Graph of this function is given in the Fig 5.6. Note that to graph
:::

:::

:::example{number="13" kind="example" id="ex_5.13" topic="Example: piecewise function"}
#### Example 13

:::prompt
Discuss the continuity of the function $f$ given by

$$
f(x)= \begin{cases}x, & \text { if } x \geq 0 \\ x^{2}, & \text { if } x<0\end{cases}
$$
:::

:::figure{src="images/fig_5_7.jpg" id="fig_5_7"}
Fig 5.7
:::

:::solution{label="Solution"}
Solution Clearly the function is defined at every real number. Graph of the function is given in Fig 5.7. By inspection, it seems prudent to partition the domain of definition of $f$ into three disjoint subsets of the real line.
Let $\mathrm{D}_{1}=\{x \in \mathbf{R}: x<0\}, \mathrm{D}_{2}=\{0\}$ and $\mathrm{D}_{3}=\{x \in \mathbf{R}: x>0\}$

Case 1 At any point in $\mathrm{D}_{1}$, we have $f(x)=x^{2}$ and it is easy to see that it is continuous there (see Example 2).
Case 2 At any point in $\mathrm{D}_{3}$, we have $f(x)=x$ and it is easy to see that it is continuous there (see Example 6).

Case 3 Now we analyse the function at $x=0$. The value of the function at 0 is $f(0)=0$. The left hand limit of $f$ at 0 is

$$
\lim _{x \rightarrow 0^{-}} f(x)=\lim _{x \rightarrow 0^{-}} x^{2}=0^{2}=0
$$

The right hand limit of $f$ at 0 is

$$
\lim _{x \rightarrow 0^{+}} f(x)=\lim _{x \rightarrow 0^{+}} x=0
$$

Thus $\lim _{x \rightarrow 0} f(x)=0=f(0)$ and hence $f$ is continuous at 0 . This means that $f$ is continuous at every point in its domain and hence, $f$ is a continuous function.
:::

:::

:::example{number="14" kind="example" id="ex_5.14" topic="Example: Show that every polynomial..."}
#### Example 14

:::prompt
Show that every polynomial function is continuous.
:::

:::solution{label="Solution"}
Solution Recall that a function $p$ is a polynomial function if it is defined by $p(x)=a_{0}+a_{1} x+\ldots+a_{n} x^{n}$ for some natural number $n, a_{n} \neq 0$ and $a_{i} \in \mathbf{R}$. Clearly this function is defined for every real number. For a fixed real number $c$, we have

$$
\lim _{x \rightarrow c} p(x)=p(c)
$$

By definition, $p$ is continuous at $c$. Since $c$ is any real number, $p$ is continuous at every real number and hence $p$ is a continuous function.
:::

:::

:::example{number="15" kind="example" id="ex_5.15" topic="Example: f(x)=[x]"}
#### Example 15

:::prompt
Find all the points of discontinuity of the greatest integer function defined by $f(x)=[x]$, where $[x]$ denotes the greatest integer less than or equal to $x$.
:::

:::figure{src="images/fig_5_8.jpg" id="fig_5_8"}
Fig 5.8
:::

:::solution{label="Solution"}
Solution First observe that $f$ is defined for all real numbers. Graph of the function is given in Fig 5.8. From the graph it looks like that $f$ is discontinuous at every integral point. Below we explore, if this is true.

Case 1 Let $c$ be a real number which is not equal to any integer. It is evident from the graph that for all real numbers close to $c$ the value of the function is equal to $[c]$; i.e., $\lim _{x \rightarrow c} f(x)=\lim _{x \rightarrow c}[x]=[c]$. Also $f(c)=[c]$ and hence the function is continuous at all real numbers not equal to integers.
Case 2 Let $c$ be an integer. Then we can find a sufficiently small real number $r>0$ such that $[c-r]=c-1$ whereas $[c+r]=c$.
This, in terms of limits mean that

$$
\lim _{x \rightarrow c^{-}} f(x)=c-1, \lim _{x \rightarrow c^{+}} f(x)=c
$$

Since these limits cannot be equal to each other for any $c$, the function is discontinuous at every integral point.
:::

:::

:::example{number="16" kind="example" id="ex_5.16" topic="Example: Prove that every rational..."}
#### Example 16

:::prompt
Prove that every rational function is continuous.
:::

:::solution{label="Solution"}
Solution Recall that every rational function $f$ is given by

$$
f(x)=\frac{p(x)}{q(x)}, q(x) \neq 0
$$

where $p$ and $q$ are polynomial functions. The domain of $f$ is all real numbers except points at which $q$ is zero. Since polynomial functions are continuous (Example 14), $f$ is continuous by (4) of Theorem 1.
:::

:::

:::example{number="17" kind="example" id="ex_5.17" topic="Example: Discuss the continuity of..."}
#### Example 17

:::prompt
Discuss the continuity of sine function.
:::

:::solution{label="Solution"}
Solution To see this we use the following facts

$$
\lim _{x \rightarrow 0} \sin x=0
$$

We have not proved it, but is intuitively clear from the graph of $\sin x$ near 0 .
Now, observe that $f(x)=\sin x$ is defined for every real number. Let $c$ be a real number. Put $x=c+h$. If $x \rightarrow c$ we know that $h \rightarrow 0$. Therefore

$$
\begin{aligned}
\lim _{x \rightarrow c} f(x) & =\lim _{x \rightarrow c} \sin x \\
& =\lim _{h \rightarrow 0} \sin (c+h) \\
& =\lim _{h \rightarrow 0}[\sin c \cos h+\cos c \sin h] \\
& =\lim _{h \rightarrow 0}[\sin c \cos h]+\lim _{h \rightarrow 0}[\cos c \sin h] \\
& =\sin c+0=\sin c=f(c)
\end{aligned}
$$

Thus $\lim _{x \rightarrow c} f(x)=f(c)$ and hence $f$ is a continuous function.

Remark A similar proof may be given for the continuity of cosine function.
:::

:::

:::example{number="18" kind="example" id="ex_5.18" topic="Example: f(x)=tan x"}
#### Example 18

:::prompt
Prove that the function defined by $f(x)=\tan x$ is a continuous function.
:::

:::solution{label="Solution"}
Solution The function $f(x)=\tan x=\frac{\sin x}{\cos x}$. This is defined for all real numbers such that $\cos x \neq 0$, i.e., $x \neq(2 n+1) \frac{\pi}{2}$. We have just proved that both sine and cosine functions are continuous. Thus $\tan x$ being a quotient of two continuous functions is continuous wherever it is defined.

An interesting fact is the behaviour of continuous functions with respect to composition of functions. Recall that if $f$ and $g$ are two real functions, then

$$
(f \circ g)(x)=f(g(x))
$$

is defined whenever the range of $g$ is a subset of domain of $f$. The following theorem (stated without proof) captures the continuity of composite functions.
Theorem 2 Suppose $f$ and $g$ are real valued functions such that ( $f \mathrm{o} g$ ) is defined at $c$. If $g$ is continuous at $c$ and if $f$ is continuous at $g(c)$, then $(f \circ g)$ is continuous at $c$.

The following examples illustrate this theorem.
:::

:::

:::example{number="19" kind="example" id="ex_5.19" topic="Example: f(x)=sin (x^2)"}
#### Example 19

:::prompt
Show that the function defined by $f(x)=\sin \left(x^{2}\right)$ is a continuous function.
:::

:::solution{label="Solution"}
Solution Observe that the function is defined for every real number. The function $f$ may be thought of as a composition $g$ o $h$ of the two functions $g$ and $h$, where $g(x)=\sin x$ and $h(x)=x^{2}$. Since both $g$ and $h$ are continuous functions, by Theorem 2, it can be deduced that $f$ is a continuous function.
:::

:::

:::example{number="20" kind="example" id="ex_5.20" topic="Example: f(x)=|1-x+|x||,"}
#### Example 20

:::prompt
Show that the function $f$ defined by

$$
f(x)=|1-x+|x||,
$$

where $x$ is any real number, is a continuous function.
:::

:::solution{label="Solution"}
Solution Define $g$ by $g(x)=1-x+|x|$ and $h$ by $h(x)=|x|$ for all real $x$. Then

$$
\begin{aligned}
(h \circ g)(x) & =h(g(x)) \\
& =h(1-x+|x|) \\
& =|1-x+|x||=f(x)
\end{aligned}
$$

In Example 7, we have seen that $h$ is a continuous function. Hence $g$ being a sum of a polynomial function and the modulus function is continuous. But then $f$ being a composite of two continuous functions is continuous.
:::

:::

:::example{number="21" kind="example" id="ex_5.21" topic="Example: f(x)=sin (x^2)"}
#### Example 21

:::prompt
Find the derivative of the function given by $f(x)=\sin \left(x^{2}\right)$.
:::

:::solution{label="Solution"}
Solution Observe that the given function is a composite of two functions. Indeed, if $t=u(x)=x^{2}$ and $v(t)=\sin t$, then

$$
f(x)=(v \circ u)(x)=v(u(x))=v\left(x^{2}\right)=\sin x^{2}
$$

Put $t=u(x)=x^{2}$. Observe that $\frac{d v}{d t}=\cos t$ and $\frac{d t}{d x}=2 x$ exist. Hence, by chain rule

$$
\frac{d f}{d x}=\frac{d v}{d t} \cdot \frac{d t}{d x}=\cos t \cdot 2 x
$$

It is normal practice to express the final result only in terms of $x$. Thus

$$
\frac{d f}{d x}=\cos t \cdot 2 x=2 x \cos x^{2}
$$
:::

:::

:::example{number="22" kind="example" id="ex_5.22" topic="Example: d y/d x"}
#### Example 22

:::prompt
Find $\frac{d y}{d x}$ if $x-y=\pi$.
:::

:::solution{label="Solution"}
Solution One way is to solve for $y$ and rewrite the above as

$$
y=x-\pi
$$

But then

$$
\frac{d y}{d x}=1
$$

Alternatively, directly differentiating the relationship w.r.t., $x$, we have

$$
\frac{d}{d x}(x-y)=\frac{d \pi}{d x}
$$

Recall that $\frac{d \pi}{d x}$ means to differentiate the constant function taking value $\pi$ everywhere w.r.t., $x$. Thus

$$
\frac{d}{d x}(x)-\frac{d}{d x}(y)=0
$$

which implies that

$$
\frac{d y}{d x}=\frac{d x}{d x}=1
$$
:::

:::

:::example{number="23" kind="example" id="ex_5.23" topic="Example: d y/d x"}
#### Example 23

:::prompt
Find $\frac{d y}{d x}$, if $y+\sin y=\cos x$.
:::

:::solution{label="Solution"}
Solution We differentiate the relationship directly with respect to $x$, i.e.,

$$
\frac{d y}{d x}+\frac{d}{d x}(\sin y)=\frac{d}{d x}(\cos x)
$$

which implies using chain rule

$$
\frac{d y}{d x}+\cos y \cdot \frac{d y}{d x}=-\sin x
$$

This gives

$$
\frac{d y}{d x}=-\frac{\sin x}{1+\cos y}
$$

where

$$
y \neq(2 n+1) \pi
$$
:::

:::

:::example{number="24" kind="example" id="ex_5.24" topic="Example: f(x)=sin ^-1 x"}
#### Example 24

:::prompt
Find the derivative of $f$ given by $f(x)=\sin ^{-1} x$ assuming it exists.
:::

:::solution{label="Solution"}
Solution Let $y=\sin ^{-1} x$. Then, $x=\sin y$.
Differentiating both sides w.r.t. $x$, we get

$$
1=\cos y \frac{d y}{d x}
$$

which implies that

$$
\frac{d y}{d x}=\frac{1}{\cos y}=\frac{1}{\cos \left(\sin ^{-1} x\right)}
$$

Observe that this is defined only for $\cos y \neq 0$, i.e., $\sin ^{-1} x \neq-\frac{\pi}{2}, \frac{\pi}{2}$, i.e., $x \neq-1,1$, i.e., $x \in(-1,1)$.

To make this result a bit more attractive, we carry out the following manipulation. Recall that for $x \in(-1,1), \sin \left(\sin ^{-1} x\right)=x$ and hence

$$
\cos ^{2} y=1-(\sin y)^{2}=1-\left(\sin \left(\sin ^{-1} x\right)\right)^{2}=1-x^{2}
$$

Also, since $y \in\left(-\frac{\pi}{2}, \frac{\pi}{2}\right), \cos y$ is positive and hence $\cos y=\sqrt{1-x^{2}}$ Thus, for $x \in(-1,1)$,

$$
\frac{d y}{d x}=\frac{1}{\cos y}=\frac{1}{\sqrt{1-x^{2}}}
$$

| $f(x)$ | $\sin ^{-1} x$ | $\cos ^{-1} x$ | $\tan ^{-1} x$ |
| :--- | :--- | :--- | :--- |
| $f^{1}(x)$ | $1 / \sqrt{1-x^{2}}$ | $-1 / \sqrt{1-x^{2}}$ | $1 / 1+x^{2}$ |
| Domain off | (-1, 1) | (-1, 1) | R |
:::

:::

:::example{number="25" kind="example" id="ex_5.25" topic="Example: x=e^log x"}
#### Example 25

:::prompt
Is it true that $x=e^{\log x}$ for all real $x$ ?
:::

:::solution{label="Solution"}
Solution First, observe that the domain of log function is set of all positive real numbers. So the above equation is not true for non-positive real numbers. Now, let $y=e^{\log x}$. If $y>0$, we may take $\operatorname{logarithm}$ which gives us $\log y=\log \left(e^{\log x}\right)=\log x \cdot \log e=\log x$. Thus $y=x$. Hence $x=e^{\log x}$ is true only for positive values of $x$.

One of the striking properties of the natural exponential function in differential calculus is that it doesn't change during the process of differentiation. This is captured in the following theorem whose proof we skip.
Theorem 5*

(1) The derivative of $e^{x}$ w.r.t., $x$ is $e^{x}$; i.e., $\frac{d}{d x}\left(e^{x}\right)=e^{x}$.
(2) The derivative of $\log x$ w.r.t., $x$ is $\frac{1}{x}$; i.e., $\frac{d}{d x}(\log x)=\frac{1}{x}$.
:::

:::

:::example{number="26" kind="example" id="ex_5.26" topic="Example: e^-x"}
#### Example 26

:::prompt
Differentiate the following w.r.t. $x$ :
(i) $e^{-x}$
(ii) $\sin (\log x), x>0$
(iii) $\cos ^{-1}\left(e^{x}\right)$
(iv) $e^{\cos x}$
:::

:::solution{label="Solution"}
Solution

(i) Let $y=e^{-x}$. Using chain rule, we have
$$
\frac{d y}{d x}=e^{-x} \cdot \frac{d}{d x}(-x)=-e^{-x}
$$
(ii) Let $y=\sin (\log x)$. Using chain rule, we have
$$
\frac{d y}{d x}=\cos (\log x) \cdot \frac{d}{d x}(\log x)=\frac{\cos (\log x)}{x}
$$

[^0]

(iii)Let $y=\cos ^{-1}\left(e^{x}\right)$. Using chain rule, we have
$$
\frac{d y}{d x}=\frac{-1}{\sqrt{1-\left(e^{x}\right)^{2}}} \cdot \frac{d}{d x}\left(e^{x}\right)=\frac{-e^{x}}{\sqrt{1-e^{2 x}}}
$$
(iv)Let $y=e^{\cos x}$. Using chain rule, we have
$$
\frac{d y}{d x}=e^{\cos x} \cdot(-\sin x)=-(\sin x) e^{\cos x}
$$
:::

:::

:::example{number="27" kind="example" id="ex_5.27" topic="Example: sqrt (x-3)(x^2+4)3 x^2+4 x..."}
#### Example 27

:::prompt
Differentiate $\sqrt{\frac{(x-3)\left(x^{2}+4\right)}{3 x^{2}+4 x+5}}$ w.r.t. $x$.
:::

:::solution{label="Solution"}
Solution Let $y=\sqrt{\frac{(x-3)\left(x^{2}+4\right)}{\left(3 x^{2}+4 x+5\right)}}$
Taking logarithm on both sides, we have

$$
\log y=\frac{1}{2}\left[\log (x-3)+\log \left(x^{2}+4\right)-\log \left(3 x^{2}+4 x+5\right)\right]
$$

Now, differentiating both sides w.r.t. $x$, we get

$$
\frac{1}{y} \cdot \frac{d y}{d x}=\frac{1}{2}\left[\frac{1}{(x-3)}+\frac{2 x}{x^{2}+4}-\frac{6 x+4}{3 x^{2}+4 x+5}\right]
$$

or

$$
\begin{aligned}
\frac{d y}{d x} & =\frac{y}{2}\left[\frac{1}{(x-3)}+\frac{2 x}{x^{2}+4}-\frac{6 x+4}{3 x^{2}+4 x+5}\right] \\
& =\frac{1}{2} \sqrt{\frac{(x-3)\left(x^{2}+4\right)}{3 x^{2}+4 x+5}}\left[\frac{1}{(x-3)}+\frac{2 x}{x^{2}+4}-\frac{6 x+4}{3 x^{2}+4 x+5}\right]
\end{aligned}
$$
:::

:::

:::example{number="28" kind="example" id="ex_5.28" topic="Example: a^x"}
#### Example 28

:::prompt
Differentiate $a^{x}$ w.r.t. $x$, where $a$ is a positive constant.
:::

:::solution{label="Solution"}
Solution Let $y=a^{x}$. Then

$$
\log y=x \log a
$$

Differentiating both sides w.r.t. $x$, we have

$$
\frac{1}{y} \frac{d y}{d x}=\log a
$$

or

$$
\frac{d y}{d x}=y \log a
$$

Thus

$$
\frac{d}{d x}\left(a^{x}\right)=a^{x} \log a
$$

Alternatively

$$
\begin{aligned}
\frac{d}{d x}\left(a^{x}\right) & =\frac{d}{d x}\left(e^{x \log a}\right)=e^{x \log a} \frac{d}{d x}(x \log a) \\
& =e^{x \log a} \cdot \log a=a^{x} \log a
\end{aligned}
$$
:::

:::

:::example{number="29" kind="example" id="ex_5.29" topic="Example: x^sin x, x>0"}
#### Example 29

:::prompt
Differentiate $x^{\sin x}, x>0$ w.r.t. $x$.
:::

:::solution{label="Solution"}
Solution Let $y=x^{\sin x}$. Taking logarithm on both sides, we have

$$
\log y=\sin x \log x
$$

Therefore

$$
\frac{1}{y} \cdot \frac{d y}{d x}=\sin x \frac{d}{d x}(\log x)+\log x \frac{d}{d x}(\sin x)
$$

or

$$
\frac{1}{y} \frac{d y}{d x}=(\sin x) \frac{1}{x}+\log x \cos x
$$

or

$$
\begin{aligned}
\frac{d y}{d x} & =y\left[\frac{\sin x}{x}+\cos x \log x\right] \\
& =x^{\sin x}\left[\frac{\sin x}{x}+\cos x \log x\right] \\
& =x^{\sin x-1} \cdot \sin x+x^{\sin x} \cdot \cos x \log x
\end{aligned}
$$
:::

:::

:::example{number="30" kind="example" id="ex_5.30" topic="Example: d y/d x"}
#### Example 30

:::prompt
Find $\frac{d y}{d x}$, if $y^{x}+x^{y}+x^{x}=a^{b}$.
:::

:::solution{label="Solution"}
Solution Given that $y^{x}+x^{y}+x^{x}=a^{b}$.
Putting $u=y^{x}, v=x^{y}$ and $w=x^{x}$, we get $u+v+w=a^{b}$
Therefore

$$
\frac{d u}{d x}+\frac{d v}{d x}+\frac{d w}{d x}=0
$$

Now, $u=y^{x}$. Taking logarithm on both sides, we have

$$
\log u=x \log y
$$

Differentiating both sides w.r.t. $x$, we have

$$
\begin{aligned}
\frac{1}{u} \cdot \frac{d u}{d x} & =x \frac{d}{d x}(\log y)+\log y \frac{d}{d x}(x) \\
& =x \frac{1}{y} \cdot \frac{d y}{d x}+\log y \cdot 1
\end{aligned}
$$

So

$$
\frac{d u}{d x}=u\left(\frac{x}{y} \frac{d y}{d x}+\log y\right)=y^{x}\left[\frac{x}{y} \frac{d y}{d x}+\log y\right]
$$

Also $v=x^{y}$

Taking logarithm on both sides, we have

$$
\log v=y \log x
$$

Differentiating both sides w.r.t. $x$, we have

$$
\begin{aligned}
\frac{1}{v} \cdot \frac{d v}{d x} & =y \frac{d}{d x}(\log x)+\log x \frac{d y}{d x} \\
& =y \cdot \frac{1}{x}+\log x \cdot \frac{d y}{d x}
\end{aligned}
$$

So

$$
\begin{aligned}
\frac{d v}{d x} & =v\left[\frac{y}{x}+\log x \frac{d y}{d x}\right] \\
& =x^{y}\left[\frac{y}{x}+\log x \frac{d y}{d x}\right]
\end{aligned}
$$

Again

$$
w=x^{x}
$$

Taking logarithm on both sides, we have

$$
\log w=x \log x .
$$

Differentiating both sides w.r.t $x$, we have

$$
\begin{aligned}
\frac{1}{w} \cdot \frac{d w}{d x} & =x \frac{d}{d x}(\log x)+\log x \cdot \frac{d}{d x}(x) \\
& =x \cdot \frac{1}{x}+\log x \cdot 1
\end{aligned}
$$

i.e.

$$
\begin{aligned}
\frac{d w}{d x} & =w(1+\log x) \\
& =x^{x}(1+\log x)
\end{aligned}
$$

From (1), (2), (3), (4), we have

$$
y^{x}\left(\frac{x}{y} \frac{d y}{d x}+\log y\right)+x^{y}\left(\frac{y}{x}+\log x \frac{d y}{d x}\right)+x^{x}(1+\log x)=0
$$

or

$$
\left(x \cdot y^{x-1}+x^{y} \cdot \log x\right) \frac{d y}{d x}=-x^{x}(1+\log x)-y \cdot x^{y-1}-y^{x} \log y
$$

Therefore

$$
\frac{d y}{d x}=\frac{-\left[y^{x} \log y+y \cdot x^{y-1}+x^{x}(1+\log x)\right]}{x \cdot y^{x-1}+x^{y} \log x}
$$
:::

:::

:::example{number="31" kind="example" id="ex_5.31" topic="Example: d y/d x"}
#### Example 31

:::prompt
Find $\frac{d y}{d x}$, if $x=a \cos \theta, y=a \sin \theta$.
:::

:::solution{label="Solution"}
Solution Given that

$$
x=a \cos \theta, y=a \sin \theta
$$

Therefore

$$
\frac{d x}{d \theta}=-a \sin \theta, \frac{d y}{d \theta}=a \cos \theta
$$

Hence

$$
\frac{d y}{d x}=\frac{\frac{d y}{d \theta}}{\frac{d x}{d \theta}}=\frac{a \cos \theta}{-a \sin \theta}=-\cot \theta
$$
:::

:::

:::example{number="32" kind="example" id="ex_5.32" topic="Example: d y/d x"}
#### Example 32

:::prompt
Find $\frac{d y}{d x}$, if $x=a t^{2}, y=2 a t$.
:::

:::solution{label="Solution"}
Solution Given that $x=a t^{2}, y=2 a t$
So

$$
\frac{d x}{d t}=2 a t \quad \text { and } \quad \frac{d y}{d t}=2 a
$$

Therefore

$$
\frac{d y}{d x}=\frac{\frac{d y}{d t}}{\frac{d x}{d t}}=\frac{2 a}{2 a t}=\frac{1}{t}
$$
:::

:::

:::example{number="33" kind="example" id="ex_5.33" topic="Example: d y/d x"}
#### Example 33

:::prompt
Find $\frac{d y}{d x}$, if $x=a(\theta+\sin \theta), y=a(1-\cos \theta)$.
:::

:::solution{label="Solution"}
Solution We have $\frac{d x}{d \theta}=a(1+\cos \theta), \frac{d y}{d \theta}=a(\sin \theta)$

Therefore

$$
\frac{d y}{d x}=\frac{\frac{d y}{d \theta}}{\frac{d x}{d \theta}}=\frac{a \sin \theta}{a(1+\cos \theta)}=\tan \frac{\theta}{2}
$$

- Note It may be noted here that $\frac{d y}{d x}$ is expressed in terms of parameter only without directly involving the main variables $x$ and $y$.
:::

:::

:::example{number="34" kind="example" id="ex_5.34" topic="Example: d y/d x"}
#### Example 34

:::prompt
Find $\frac{d y}{d x}$, if $x^{\frac{2}{3}}+y^{\frac{2}{3}}=a^{\frac{2}{3}}$.
:::

:::solution{label="Solution"}
Solution Let $x=a \cos ^{3} \theta, y=a \sin ^{3} \theta$. Then

$$
\begin{aligned}
x^{\frac{2}{3}}+y^{\frac{2}{3}} & =\left(a \cos ^{3} \theta\right)^{\frac{2}{3}}+\left(a \sin ^{3} \theta\right)^{\frac{2}{3}} \\
& =a^{\frac{2}{3}}\left(\cos ^{2} \theta+\left(\sin ^{2} \theta\right)=a^{\frac{2}{3}}\right.
\end{aligned}
$$

Hence, $x=a \cos ^{3} \theta, y=a \sin ^{3} \theta$ is parametric equation of $x^{\frac{2}{3}}+y^{\frac{2}{3}}=a^{\frac{2}{3}}$

Now

$$
\frac{d x}{d \theta}=-3 a \cos ^{2} \theta \sin \theta \text { and } \frac{d y}{d \theta}=3 a \sin ^{2} \theta \cos \theta
$$

Therefore

$$
\frac{d y}{d x}=\frac{\frac{d y}{d \theta}}{\frac{d x}{d \theta}}=\frac{3 a \sin ^{2} \theta \cos \theta}{-3 a \cos ^{2} \theta \sin \theta}=-\tan \theta=-\sqrt[3]{\frac{y}{x}}
$$
:::

:::

:::example{number="35" kind="example" id="ex_5.35" topic="Example: d^2 yd x^2"}
#### Example 35

:::prompt
Find $\frac{d^{2} y}{d x^{2}}$, if $y=x^{3}+\tan x$.
:::

:::solution{label="Solution"}
Solution Given that $y=x^{3}+\tan x$. Then

$$
\frac{d y}{d x}=3 x^{2}+\sec ^{2} x
$$

Therefore

$$
\begin{aligned}
\frac{d^{2} y}{d x^{2}} & =\frac{d}{d x}\left(3 x^{2}+\sec ^{2} x\right) \\
& =6 x+2 \sec x \cdot \sec x \tan x=6 x+2 \sec ^{2} x \tan x
\end{aligned}
$$
:::

:::

:::example{number="36" kind="example" id="ex_5.36" topic="Example: y=A sin x+B cos x"}
#### Example 36

:::prompt
If $y=\mathrm{A} \sin x+\mathrm{B} \cos x$, then prove that $\frac{d^{2} y}{d x^{2}}+y=0$.
:::

:::solution{label="Solution"}
Solution We have

$$
\frac{d y}{d x}=\mathrm{A} \cos x-\mathrm{B} \sin x
$$

and

$$
\begin{aligned}
\frac{d^{2} y}{d x^{2}} & =\frac{d}{d x}(\mathrm{~A} \cos x-\mathrm{B} \sin x) \\
& =-\mathrm{A} \sin x-\mathrm{B} \cos x=-y
\end{aligned}
$$

Hence

$$
\frac{d^{2} y}{d x^{2}}+y=0
$$
:::

:::

:::example{number="37" kind="example" id="ex_5.37" topic="Example: y=3 e^2 x+2 e^3 x"}
#### Example 37

:::prompt
If $y=3 e^{2 x}+2 e^{3 x}$, prove that $\frac{d^{2} y}{d x^{2}}-5 \frac{d y}{d x}+6 y=0$.
:::

:::solution{label="Solution"}
Solution Given that $y=3 e^{2 x}+2 e^{3 x}$. Then

$$
\frac{d y}{d x}=6 e^{2 x}+6 e^{3 x}=6\left(e^{2 x}+e^{3 x}\right)
$$

Therefore

$$
\frac{d^{2} y}{d x^{2}}=12 e^{2 x}+18 e^{3 x}=6\left(2 e^{2 x}+3 e^{3 x}\right)
$$

Hence

$$
\begin{aligned}
\frac{d^{2} y}{d x^{2}}-5 \frac{d y}{d x}+6 y= & 6\left(2 e^{2 x}+3 e^{3 x}\right) \\
& -30\left(e^{2 x}+e^{3 x}\right)+6\left(3 e^{2 x}+2 e^{3 x}\right)=0
\end{aligned}
$$
:::

:::

:::example{number="38" kind="example" id="ex_5.38" topic="Example: y=sin ^-1 x"}
#### Example 38

:::prompt
If $y=\sin ^{-1} x$, show that $\left(1-x^{2}\right) \frac{d^{2} y}{d x^{2}}-x \frac{d y}{d x}=0$.
:::

:::solution{label="Solution"}
Solution We have $y=\sin ^{-1} x$. Then

$$
\frac{d y}{d x}=\frac{1}{\sqrt{\left(1-x^{2}\right)}}
$$

or

$$
\sqrt{\left(1-x^{2}\right)} \frac{d y}{d x}=1
$$

So

$$
\frac{d}{d x}\left(\sqrt{\left(1-x^{2}\right)} \cdot \frac{d y}{d x}\right)=0
$$

or

$$
\sqrt{\left(1-x^{2}\right)} \cdot \frac{d^{2} y}{d x^{2}}+\frac{d y}{d x} \cdot \frac{d}{d x}\left(\sqrt{\left(1-x^{2}\right)}\right)=0
$$

or

$$
\sqrt{\left(1-x^{2}\right)} \cdot \frac{d^{2} y}{d x^{2}}-\frac{d y}{d x} \cdot \frac{2 x}{2 \sqrt{1-x^{2}}}=0
$$

Hence

$$
\left(1-x^{2}\right) \frac{d^{2} y}{d x^{2}}-x \frac{d y}{d x}=0
$$

Alternatively, Given that $y=\sin ^{-1} x$, we have

$$
y_{1}=\frac{1}{\sqrt{1-x^{2}}} \text {, i.e., }\left(1-x^{2}\right) y_{1}^{2}=1
$$

So

$$
\left(1-x^{2}\right) \cdot 2 y_{1} y_{2}+y_{1}^{2}(0-2 x)=0
$$

Hence

$$
\left(1-x^{2}\right) y_{2}-x y_{1}=0
$$
:::

:::

:::example{number="39" kind="example" id="ex_5.39" topic="Example: sqrt 3 x+2+1sqrt 2 x^2+4"}
#### Example 39

:::prompt
Differentiate w.r.t. $x$, the following function:
(i) $\sqrt{3 x+2}+\frac{1}{\sqrt{2 x^{2}+4}}$
(ii) $\log _{7}(\log x)$
:::

:::solution{label="Solution"}
Solution

(i) Let $y=\sqrt{3 x+2}+\frac{1}{\sqrt{2 x^{2}+4}}=(3 x+2)^{\frac{1}{2}}+\left(2 x^{2}+4\right)^{-\frac{1}{2}}$
Note that this function is defined at all real numbers $x>-\frac{2}{3}$. Therefore
$$
\frac{d y}{d x}=\frac{1}{2}(3 x+2)^{\frac{1}{2}-1} \cdot \frac{d}{d x}(3 x+2)+\left(-\frac{1}{2}\right)\left(2 x^{2}+4\right)^{-\frac{1}{2}-1} \cdot \frac{d}{d x}\left(2 x^{2}+4\right)
$$
$$
=\frac{1}{2}(3 x+2)^{-\frac{1}{2}} \cdot(3)-\frac{1}{2}\left(2 x^{2}+4\right)^{-\frac{3}{2}} \cdot 4 x
$$
$$
=\frac{3}{2 \sqrt{3 x+2}}-\frac{2 x}{\left(2 x^{2}+4\right)^{\frac{3}{2}}}
$$
This is defined for all real numbers $x>-\frac{2}{3}$.

(ii) Let $y=\log _{7}(\log x)=\frac{\log (\log x)}{\log 7}$ (by change of base formula).
The function is defined for all real numbers $x>1$. Therefore
$$
\begin{aligned}
\frac{d y}{d x} & =\frac{1}{\log 7} \frac{d}{d x}(\log (\log x)) \\
& =\frac{1}{\log 7} \frac{1}{\log x} \cdot \frac{d}{d x}(\log x) \\
& =\frac{1}{x \log 7 \log x}
\end{aligned}
$$
:::

:::

:::example{number="40" kind="example" id="ex_5.40" topic="Example: cos ^-1(sin x)"}
#### Example 40

:::prompt
Differentiate the following w.r.t. $x$.
(i) $\cos ^{-1}(\sin x)$
(ii) $\tan ^{-1}\left(\frac{\sin x}{1+\cos x}\right)$
(iii) $\sin ^{-1}\left(\frac{2^{x+1}}{1+4^{x}}\right)$
:::

:::solution{label="Solution"}
Solution

(i) Let $f(x)=\cos ^{-1}(\sin x)$. Observe that this function is defined for all real numbers. We may rewrite this function as
$$
\begin{aligned}
f(x) & =\cos ^{-1}(\sin x) \\
& =\cos ^{-1} \cos \frac{\pi}{2}-x \\
& =\frac{\pi}{2}-x
\end{aligned}
$$
Thus $\quad f^{\prime}(x)=-1$.
(ii) Let $f(x)=\tan ^{-1}\left(\frac{\sin x}{1+\cos x}\right)$. Observe that this function is defined for all real numbers, where $\cos x \neq-1$; i.e., at all odd multiplies of $\pi$. We may rewrite this function as
$$
\begin{aligned}
f(x) & =\tan ^{-1}\left(\frac{\sin x}{1+\cos x}\right) \\
& =\tan ^{-1}\left[\frac{2 \sin \left(\frac{x}{2}\right) \cos \left(\frac{x}{2}\right)}{2 \cos ^{2} \frac{x}{2}}\right]
\end{aligned}
$$

$$
=\tan ^{-1}\left[\tan \left(\frac{x}{2}\right)\right]=\frac{x}{2}
$$

Observe that we could cancel $\cos \left(\frac{x}{2}\right)$ in both numerator and denominator as it is not equal to zero. Thus $f^{\prime}(x)=\frac{1}{2}$.

(iii) Let $f(x)=\sin ^{-1}\left(\frac{2^{x+1}}{1+4^{x}}\right)$. To find the domain of this function we need to find all $x$ such that $-1 \leq \frac{2^{x+1}}{1+4^{x}} \leq 1$. Since the quantity in the middle is always positive, we need to find all $x$ such that $\frac{2^{x+1}}{1+4^{x}} \leq 1$, i.e., all $x$ such that $2^{x+1} \leq 1+4^{x}$. We may rewrite this as $2 \leq \frac{1}{2^{x}}+2^{x}$ which is true for all $x$. Hence the function is defined at every real number. By putting $2^{x}=\tan \theta$, this function may be rewritten as
$$
\begin{aligned}
f(x) & =\sin ^{-1}\left[\frac{2^{x+1}}{1+4^{x}}\right] \\
& =\sin ^{-1} \frac{2^{x} \cdot 2}{1+\left(2^{x}\right)^{2}} \\
& =\sin ^{-1}\left[\frac{2 \tan \theta}{1+\tan ^{2} \theta}\right] \\
& =\sin ^{-1}[\sin 2 \theta] \\
& =2 \theta=2 \tan ^{-1}\left(2^{x}\right)
\end{aligned}
$$
Thus
$$
\begin{aligned}
f^{\prime}(x) & =2 \cdot \frac{1}{1+\left(2^{x}\right)^{2}} \cdot \frac{d}{d x}\left(2^{x}\right) \\
& =\frac{2}{1+4^{x}} \cdot\left(2^{x}\right) \log 2 \\
& =\frac{2^{x+1} \log 2}{1+4^{x}}
\end{aligned}
$$
:::

:::

:::example{number="41" kind="example" id="ex_5.41" topic="Example: f^(x)"}
#### Example 41

:::prompt
Find $f^{\prime}(x)$ if $f(x)=(\sin x)^{\sin x}$ for all $0<x<\pi$.
:::

:::solution{label="Solution"}
Solution The function $y=(\sin x)^{\sin x}$ is defined for all positive real numbers. Taking logarithms, we have

$$
\log y=\log (\sin x)^{\sin x}=\sin x \log (\sin x)
$$

Then

$$
\begin{aligned}
\frac{1}{y} \frac{d y}{d x} & =\frac{d}{d x}(\sin x \log (\sin x)) \\
& =\cos x \log (\sin x)+\sin x \cdot \frac{1}{\sin x} \cdot \frac{d}{d x}(\sin x) \\
& =\cos x \log (\sin x)+\cos x \\
& =(1+\log (\sin x)) \cos x
\end{aligned}
$$

Thus

$$
\frac{d y}{d x}=y((1+\log (\sin x)) \cos x)=(1+\log (\sin x))(\sin x)^{\sin x} \cos x
$$
:::

:::

:::example{number="42" kind="example" id="ex_5.42" topic="Example: d y/d x"}
#### Example 42

:::prompt
For a positive constant $a$ find $\frac{d y}{d x}$, where

$$
y=a^{t+\frac{1}{t}}, \text { and } x=\left(t+\frac{1}{t}\right)^{a}
$$
:::

:::solution{label="Solution"}
Solution Observe that both $y$ and $x$ are defined for all real $t \neq 0$. Clearly

$$
\begin{aligned}
\frac{d y}{d t}=\frac{d}{d t}\left(a^{t+\frac{1}{t}}\right) & =a^{t+\frac{1}{t}} \frac{d}{d t}\left(t+\frac{1}{t}\right) \cdot \log a \\
& =a^{t+\frac{1}{t}}\left(1-\frac{1}{t^{2}}\right) \log a
\end{aligned}
$$

Similarly

$$
\begin{aligned}
\frac{d x}{d t} & =a\left[t+\frac{1}{t}\right]^{a-1} \cdot \frac{d}{d t}\left(t+\frac{1}{t}\right) \\
& =a\left[t+\frac{1}{t}\right]^{a-1} \cdot\left(1-\frac{1}{t^{2}}\right)
\end{aligned}
$$

$\frac{d x}{d t} \neq 0$ only if $t \neq \pm 1$. Thus for $t \neq \pm 1$,

$$
\begin{aligned}
\frac{d y}{d x}=\frac{\frac{d y}{d t}}{\frac{d x}{d t}} & =\frac{a^{t+\frac{1}{t}} 1-\frac{1}{t^{2}} \log a}{a t+\frac{1}{t}} \cdot 1-\frac{1}{t^{2}} \\
& =\frac{a^{t+\frac{1}{t}} \log a}{a\left(t+\frac{1}{t}\right)^{a-1}}
\end{aligned}
$$
:::

:::

:::example{number="43" kind="example" id="ex_5.43" topic="Example: sin ^2 x"}
#### Example 43

:::prompt
Differentiate $\sin ^{2} x$ w.r.t. $e^{\cos x}$.
:::

:::solution{label="Solution"}
Solution Let $u(x)=\sin ^{2} x$ and $v(x)=e^{\cos x}$. We want to find $\frac{d u}{d v}=\frac{d u / d x}{d v / d x}$. Clearly

$$
\frac{d u}{d x}=2 \sin x \cos x \text { and } \frac{d v}{d x}=e^{\cos x}(-\sin x)=-(\sin x) e^{\cos x}
$$

Thus

$$
\frac{d u}{d v}=\frac{2 \sin x \cos x}{-\sin x e^{\cos x}}=-\frac{2 \cos x}{e^{\cos x}}
$$
:::

:::
