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

## Questions and Solutions

:::question{number="1" kind="exercise" id="q_5.1.1" topic="Continuity: f(x)=5 x-3"}
#### Question 1

:::prompt
Prove that the function $f(x)=5 x-3$ is continuous at $x=0$, at $x=-3$ and at $x=5$.
:::

:::solution{label="Solution"}
The given function is $f(x)=5 x-3$

$$
\begin{aligned}
& \text { At } x=0, f(0)=5(0)-3=-3 \\
& \lim _{x \rightarrow 0} f(x)=\lim _{x \rightarrow 0}(5 x-3)=5(0)-3=-3 \\
& \therefore \lim _{x \rightarrow 0} f(x)=f(0)
\end{aligned}
$$

Therefore, $f$ is continous at $x=0$.

$$
\begin{aligned}
& \text { At } x=-3, f(-3)=5(-3)-3=-18 \\
& \lim _{x \rightarrow-3} f(x)=\lim _{x \rightarrow-3}(5 x-3)=5(-3)-3=-18 \\
& \therefore \lim _{x \rightarrow-3} f(x)=f(-3)
\end{aligned}
$$

Therefore, $f$ is continous at $x=-3$.

$$
\begin{aligned}
& \text { At } x=5, f(5)=5(5)-3=22 \\
& \lim _{x \rightarrow 5} f(x)=\lim _{x \rightarrow 5}(5 x-3)=5(5)-3=22 \\
& \therefore \lim _{x \rightarrow 5} f(x)=f(5)
\end{aligned}
$$

Therefore, $f$ is continous at $x=5$.
:::

:::

:::question{number="2" kind="exercise" id="q_5.1.2" topic="Continuity: f(x)=2 x^2-1"}
#### Question 2

:::prompt
Examine the continuity of the function $f(x)=2 x^{2}-1$ at $x=3$.
:::

:::solution{label="Solution"}
The given function is $f(x)=2 x^{2}-1$

$$
\begin{aligned}
& \text { At } x=3, f(3)=2(3)^{2}-1=17 \\
& \lim _{x \rightarrow 3} f(x)=\lim _{x \rightarrow 3}\left(2 x^{2}-1\right)=2\left(3^{2}\right)-1=17 \\
& \therefore \lim _{x \rightarrow 3} f(x)=f(3)
\end{aligned}
$$

Therefore, $f$ is continous at $x=3$.
:::

:::

:::question{number="3" kind="exercise" id="q_5.1.3" topic="Continuity: f(x)=x-5"}
#### Question 3

:::prompt
Examine the following functions for continuity.
:::

:::part{label="a"}
:::prompt
$f(x)=x-5$
:::

:::solution
The given function is $f(x)=x-5$
It is evident that $f$ is defined at every real number $k$ and its value at $k$ is $k-5$.
It is also observed that
$$
\begin{aligned}
& \lim _{x \rightarrow k} f(x)=\lim _{x \rightarrow k}(x-5)=k-5=f(k) \\
& \therefore \lim _{x \rightarrow k} f(x)=f(k)
\end{aligned}
$$
Hence, $f$ is continuous at every real number and therefore, it is a continuous function.
:::

:::

:::part{label="b"}
:::prompt
$f(x)=\frac{1}{x-5}, x \neq 5$
:::

:::solution
The given function is $f(x)=\frac{1}{x-5}, x \neq 5$
For any real number $k \neq 5$, we obtain
$$
\lim _{x \rightarrow k} f(x)=\lim _{x \rightarrow k} \frac{1}{x-5}=\frac{1}{k-5}
$$
Also,
$$
\begin{aligned}
& f(k)=\frac{1}{k-5} \quad(\text { As } k \neq 5) \\
& \therefore \lim _{x \rightarrow k} f(x)=f(k)
\end{aligned}
$$
Hence, $f$ is continuous at every point in the domain of $f$ and therefore, it is a continuous function.
:::

:::

:::part{label="c"}
:::prompt
$f(x)=\frac{x^{2}-25}{x+5}, x \neq-5$
:::

:::solution
The given function is $f(x)=\frac{x^{2}-25}{x+5}, x \neq-5$
For any real number $c \neq-5$, we obtain
$$
\lim _{x \rightarrow c} f(x)=\lim _{x \rightarrow c} \frac{x^{2}-25}{x+5}=\lim _{x \rightarrow c} \frac{(x+5)(x-5)}{x+5}=\lim _{x \rightarrow c}(x-5)=(c-5)
$$
Also,
$$
\begin{aligned}
& f(c)=\frac{(c+5)(c-5)}{c+5}=(c-5) \\
& \therefore \lim _{x \rightarrow c} f(x)=f(c)
\end{aligned}
$$

Hence, $f$ is continuous at every point in the domain of $f$ and therefore, it is a continuous function.
:::

:::

:::part{label="d"}
:::prompt
$f(x)=|x-5|$
:::

:::solution
The given function is $f(x)=|x-5|=\left\{\begin{array}{l}5-x, \text { if } x<5 \\ x-5, \text { if } x \geq 5\end{array}\right\}$
This function $f$ is defined at all points of the real line. Let c be a point on a real line. Then, $c<5, c=5$ or $c>5$

Case I: $c<5$
Then, $f(c)=5-c$

$$
\begin{aligned}
& \lim _{x \rightarrow c} f(x)=\lim _{x \rightarrow c}(5-x)=5-c \\
& \therefore \lim _{x \rightarrow c} f(x)=f(c)
\end{aligned}
$$

Therefore, $f$ is continuous at all real numbers less than 5 .

Case II: $c=5$
Then, $f(c)=f(5)=(5-5)=0$

$$
\begin{aligned}
& \lim _{x \rightarrow 5^{-}} f(x)=\lim _{x \rightarrow 5}(5-x)=(5-5)=0 \\
& \lim _{x \rightarrow 5^{+}} f(x)=\lim _{x \rightarrow 5}(x-5)=0 \\
& \therefore \lim _{x \rightarrow c^{-}} f(x)=\lim _{x \rightarrow c^{+}} f(x)=f(c)
\end{aligned}
$$

Therefore, $f$ is continuous at $x=5$
Case III: $c>5$
Then, $f(c)=f(5)=c-5$

$$
\begin{aligned}
& \lim _{x \rightarrow c} f(x)=\lim _{x \rightarrow c}(x-5)=c-5 \\
& \therefore \lim _{x \rightarrow c} f(x)=f(c)
\end{aligned}
$$

Therefore, $f$ is continuous at all real numbers greater than 5 .
Hence, $f$ is continuous at every real number and therefore, it is a continuous function.
:::

:::

:::

:::question{number="4" kind="exercise" id="q_5.1.4" topic="Continuity: f(x)=x^n"}
#### Question 4

:::prompt
Prove that the function $f(x)=x^{n}$ is continuous at $x=n$, where $n$ is a positive integer.
:::

:::solution{label="Solution"}
The given function is $f(x)=x^{n}$
It is observed that $f$ is defined at all positive integers, $n$, and its value at $n$ is $n^{n}$.
Then,

$$
\begin{aligned}
& \lim _{x \rightarrow n} f(n)=\lim _{x \rightarrow n}\left(x^{n}\right)=x^{n} \\
& \therefore \lim _{x \rightarrow n} f(x)=f(n)
\end{aligned}
$$

Therefore, $f$ is continuous at $n$, where $n$ is a positive integer.
:::

:::

:::question{number="5" kind="exercise" id="q_5.1.5" topic="Continuity: piecewise function"}
#### Question 5

:::prompt
Is the function $f$ defined by
$$
f(x)= \begin{cases}x, & \text { if } x \leq 1 \\ 5, & \text { if } x>1\end{cases}
$$
continuous at $x=0$ ? At $x=1$ ? At $x=2$ ?

Find all points of discontinuity of $f$, where $f$ is defined by
:::

:::solution{label="Solution"}
The given function is $f(x)=\left\{\begin{array}{l}x, \text { if } x \leq 1 \\ 5, \text { if } x>1\end{array}\right.$
At $x=0$,
It is evident that $f$ is defined at 0 and its value at 0 is 0 .
Then,

$$
\begin{aligned}
& \lim _{x \rightarrow 0} f(x)=\lim _{x \rightarrow 0}(x)=0 \\
& \therefore \lim _{x \rightarrow 0} f(x)=f(0)
\end{aligned}
$$

Therefore, $f$ is continuous at $x=0$.

$$
\text { At } x=1 \text {, }
$$

It is evident that $f$ is defined at 1 and its value at 1 is 1 .
The left hand limit of $f$ at $x=1$ is,

$$
\lim _{x \rightarrow 1^{-}} f(x)=\lim _{x \rightarrow 1^{-}}(x)=1
$$

The right hand limit of $f$ at $x=1$ is,

$$
\begin{aligned}
& \lim _{x \rightarrow 1^{+}} f(x)=\lim _{x \rightarrow 1^{+}}(5)=5 \\
& \therefore \lim _{v \rightarrow 1^{-}} f(x) \neq \lim _{v \rightarrow 1^{+}} f(x)
\end{aligned}
$$

Therefore, $f$ is not continuous at $x=1$.
At $x=2$,
It is evident that $f$ is defined at 2 and its value at 2 is 5 .

$$
\begin{aligned}
& \lim _{x \rightarrow 2} f(x)=\lim _{x \rightarrow 2}(5)=5 \\
& \therefore \lim _{x \rightarrow 1} f(x)=f(2)
\end{aligned}
$$

Therefore, $f$ is continuous at $x=2$.
:::

:::

:::question{number="6" kind="exercise" id="q_5.1.6" topic="Continuity: piecewise function"}
#### Question 6

:::prompt
$f(x)=\left\{\begin{array}{l}2 x+3, \text { if } x \leq 2 \\ 2 x-3, \text { if } x>2\end{array}\right.$
:::

:::solution{label="Solution"}
The given function is $f(x)=\left\{\begin{array}{l}2 x+3, \text { if } x \leq 2 \\ 2 x-3, \text { if } x>2\end{array}\right.$
It is evident that the given function $f$ is defined at all the points of the real line.
Let $c$ be a point on the real line. Then, three cases arise.

$$
\begin{aligned}
& c<2 \\
& c>2 \\
& c=2
\end{aligned}
$$

Case I: $c<2$

$$
f(c)=2 c+3
$$

Then,

$$
\begin{aligned}
& \lim _{x \rightarrow c} f(x)=\lim _{x \rightarrow c}(2 x+3)=2 c+3 \\
& \therefore \lim _{x \rightarrow c} f(x)=f(c)
\end{aligned}
$$

Therefore, $f$ is continuous at all points $x$, such that $x<2$.
Case II: $c>2$
Then,

$$
\begin{aligned}
& f(c)=2 c-3 \\
& \lim _{x \rightarrow c} f(x)=\lim _{x \rightarrow c}(2 x-3)=2 c-3 \\
& \therefore \lim _{x \rightarrow c} f(x)=f(c)
\end{aligned}
$$

Therefore, $f$ is continuous at all points $x$, such that $x>2$
Case III: $c=2$
Then, the left hand limit of $f$ at $x=2$ is,

$$
\lim _{x \rightarrow 2^{-}} f(x)=\lim _{x \rightarrow 2^{-}}(2 x+3)=2(2)+3=7
$$

The right hand limit of $f$ at $x=2$ is,

$$
\lim _{x \rightarrow 0^{+}} f(x)=\lim _{x \rightarrow 0^{+}}(2 x-3)=2(2)-3=1
$$

It is observed that the left and right hand limit of $f$ at $x=2$ do not coincide.
Therefore, $f$ is not continuous at $x=2$.
Hence, $x=2$ is the only point of discontinuity of $f$.
:::

:::

:::question{number="7" kind="exercise" id="q_5.1.7" topic="Continuity: piecewise function"}
#### Question 7

:::prompt
$f(x)=\left\{\begin{array}{cl}|x|+3, & \text { if } x \leq-3 \\ -2 x, & \text { if }-3<x<3 \\ 6 x+2, & \text { if } x \geq 3\end{array}\right.$
:::

:::solution{label="Solution"}
The given function is

$$
f(x)=\left\{\begin{array}{l}
|x|+3, \text { if } x \leq-3 \\
-2 x, \text { if }-3<x<3 \\
6 x+2, \text { if } x \geq 3
\end{array}\right.
$$

The given function $f$ is defined at all the points of the real line.
Let $c$ be a point on the real line.
Case I:
If $c<-3$, then $f(c)=-c+3$

$$
\begin{aligned}
& \lim _{x \rightarrow c} f(x)=\lim _{x \rightarrow c}(-x+3)=-c+3 \\
& \therefore \lim _{x \rightarrow c} f(x)=f(c)
\end{aligned}
$$

Therefore, $f$ is continuous at all points $x$, such that $x<-3$.

Case II:
If $c=-3$, then $f(-3)=-(-3)+3=6$

$$
\begin{aligned}
& \lim _{x \rightarrow-3^{-}} f(x)=\lim _{x \rightarrow-3^{-}}(-x+3)=-(-3)+3=6 \\
& \lim _{x \rightarrow-3^{+}} f(x)=\lim _{x \rightarrow-3^{+}}(-2 x)=-2(-3)=6 \\
& \therefore \lim _{x \rightarrow-3} f(x)=f(-3)
\end{aligned}
$$

Therefore, $f$ is continuous at $x=-3$.
Case III:
If $-3<c<3$, then $f(c)=-2 c$

$$
\begin{aligned}
& \lim _{x \rightarrow c} f(x)=\lim _{x \rightarrow c}(-2 x)=-2 c \\
& \therefore \lim _{x \rightarrow c} f(x)=f(c)
\end{aligned}
$$

Therefore, $f$ is continuous in $(-3,3)$.
Case IV:
If $c=3$, then the left hand limit of $f$ at $x=3$ is,

$$
\lim _{x \rightarrow 3^{-}} f(x)=\lim _{x \rightarrow 3^{-}}(-2 x)=-2(3)=-6
$$

The right hand limit of $f$ at $x=3$ is,

$$
\lim _{x \rightarrow 3^{+}} f(x)=\lim _{x \rightarrow 3^{+}}(6 x+2)=6(3)+2=20
$$

It is observed that the left and right hand limit of $f$ at $x=3$ do not coincide.
Therefore, $f$ is not continuous at $x=3$.
Case V:
If $c>3$, then $f(c)=6 c+2$

$$
\begin{aligned}
& \lim _{x \rightarrow c} f(x)=\lim _{x \rightarrow c}(6 x+2)=6 c+2 \\
& \therefore \lim _{x \rightarrow c} f(x)=f(c)
\end{aligned}
$$

Therefore, $f$ is continuous at all points $x$, such that $x>3$.
Hence, $x=3$ is the only point of discontinuity of $f$.
:::

:::

:::question{number="8" kind="exercise" id="q_5.1.8" topic="Continuity: piecewise function"}
#### Question 8

:::prompt
$f(x)=\left\{\begin{array}{cc}\frac{|x|}{x}, & \text { if } x \neq 0 \\ 0, & \text { if } x=0\end{array}\right.$
:::

:::solution{label="Solution"}
The given function is

$$
f(x)= \begin{cases}\frac{|x|}{x}, & \text { if } x \neq 0 \\ 0, & \text { if } x=0\end{cases}
$$

It is known that, $x<0 \Rightarrow|x|=-x$ and $x>0 \Rightarrow|x|=x$

Therefore, the given function can be rewritten as

$$
f(x)=\left\{\begin{array}{l}
\frac{|x|}{x}=\frac{-x}{x}=-1, \text { if } x<0 \\
0, \text { if } x=0 \\
\frac{|x|}{x}=\frac{x}{x}=1, \text { if } x>0
\end{array}\right.
$$

The given function $f$ is defined at all the points of the real line.
Let $c$ be a point on the real line.
Case I:
If $c<0$, then $f(c)=-1$

$$
\begin{aligned}
& \lim _{x \rightarrow c} f(x)=\lim _{x \rightarrow c}(-1)=-1 \\
& \therefore \lim _{x \rightarrow c} f(x)=f(c)
\end{aligned}
$$

Therefore, $f$ is continuous at all points $x<0$.
Case II:
If $c=0$, then the left hand limit of $f$ at $x=0$ is,

$$
\lim _{x \rightarrow 0^{-}} f(x)=\lim _{x \rightarrow 0^{-}}(-1)=-1
$$

The right hand limit of $f$ at $x=0$ is,

$$
\lim _{x \rightarrow 0^{+}} f(x)=\lim _{x \rightarrow 0^{+}}(1)=1
$$

It is observed that the left and right hand limit of $f$ at $x=0$ do not coincide.
Therefore, $f$ is not continuous at $x=0$.

Case III:
If $c>0$, then $f(c)=1$

$$
\begin{aligned}
& \lim _{x \rightarrow c} f(x)=\lim _{x \rightarrow c}(1)=1 \\
& \therefore \lim _{x \rightarrow c} f(x)=f(c)
\end{aligned}
$$

Therefore, $f$ is continuous at all points $x$, such that $x>0$.
Hence, $x=0$ is the only point of discontinuity of $f$.
:::

:::

:::question{number="9" kind="exercise" id="q_5.1.9" topic="Continuity: piecewise function"}
#### Question 9

:::prompt
$f(x)= \begin{cases}\frac{x}{|x|}, & \text { if } x<0 \\ -1, & \text { if } x \geq 0\end{cases}$
:::

:::solution{label="Solution"}
The given function is

$$
f(x)= \begin{cases}\frac{x}{|x|}, & \text { if } x<0 \\ -1, & \text { if } x \geq 0\end{cases}
$$

It is known that $x<0 \Rightarrow|x|=-x$
Therefore, the given function can be rewritten as

$$
\begin{aligned}
& f(x)=\left\{\begin{array}{l}
\frac{x}{|x|}=\frac{x}{-x}=-1, \text { if } x<0 \\
-1, \text { if } x \geq 0
\end{array}\right. \\
& \Rightarrow f(x)=-1 \forall x \in R
\end{aligned}
$$

Let $c$ be any real number.
Then, $\lim _{x \rightarrow c} f(x)=\lim _{x \rightarrow c}(-1)=-1$
Also, $f(c)=-1=\lim _{x \rightarrow c} f(x)$
Therefore, the given function is a continuous function.
Hence, the given function has no point of discontinuity.
:::

:::

:::question{number="10" kind="exercise" id="q_5.1.10" topic="Continuity: piecewise function"}
#### Question 10

:::prompt
$f(x)= \begin{cases}x+1, & \text { if } x \geq 1 \\ x^{2}+1, \text { if } x<1\end{cases}$
:::

:::solution{label="Solution"}
The given function is $f(x)=\left\{\begin{array}{l}x+1, \text { if } x \geq 1 \\ x^{2}+1, \text { if } x<1\end{array}\right.$
The given function $f$ is defined at all the points of the real line.
Let $c$ be a point on the real line.
Case I:
If $c<1$, then $f(c)=c^{2}+1$

$$
\begin{aligned}
& \lim _{x \rightarrow c} f(x)=\lim _{x \rightarrow c}\left(x^{2}+1\right)=c^{2}+1 \\
& \therefore \lim _{x \rightarrow c} f(x)=f(c)
\end{aligned}
$$

Therefore, $f$ is continuous at all points $x$, such that $x<1$.
Case II:
If $c=1$, then $f(c)=f(1)=1+1=2$
The left hand limit of $f$ at $x=1$ is,

$$
\lim _{x \rightarrow 1^{-}} f(x)=\lim _{x \rightarrow 1^{-}}\left(x^{2}+1\right)=1^{2}+1=2
$$

The right hand limit of $f$ at $x=1$ is,

$$
\begin{aligned}
& \lim _{x \rightarrow 1^{+}} f(x)=\lim _{x \rightarrow 1^{+}}(x+1)=1+1=2 \\
& \therefore \lim _{x \rightarrow 1} f(x)=f(1)
\end{aligned}
$$

Therefore, $f$ is continuous at $x=1$.
Case III:
If $c>1$, then $f(c)=c+1$

$$
\begin{aligned}
& \lim _{x \rightarrow c} f(x)=\lim _{x \rightarrow c}(x+1)=c+1 \\
& \therefore \lim _{x \rightarrow c} f(x)=f(c)
\end{aligned}
$$

Therefore, $f$ is continuous at all points $x$, such that $x>1$.
Hence, the given function $f$ has no point of discontinuity.
:::

:::

:::question{number="11" kind="exercise" id="q_5.1.11" topic="Continuity: piecewise function"}
#### Question 11

:::prompt
$f(x)= \begin{cases}x^{3}-3, & \text { if } x \leq 2 \\ x^{2}+1, & \text { if } x>2\end{cases}$
:::

:::solution{label="Solution"}
The given function is $f(x)=\left\{\begin{array}{l}x^{3}-3, \text { if } x \leq 2 \\ x^{2}+1, \text { if } x>2\end{array}\right.$
The given function $f$ is defined at all the points of the real line.

Let $c$ be a point on the real line.
Case I:
If $c<2$, then $f(c)=c^{3}-3$

$$
\begin{aligned}
& \lim _{x \rightarrow c} f(x)=\lim _{x \rightarrow c}\left(x^{3}-3\right)=c^{3}-3 \\
& \therefore \lim _{x \rightarrow c} f(x)=f(c)
\end{aligned}
$$

Therefore, $f$ is continuous at all points $x$, such that $x<2$.
Case II:
If $c=2$, then $f(c)=f(2)=2^{3}-3=5$

$$
\begin{aligned}
& \lim _{x \rightarrow 2^{-}} f(x)=\lim _{x \rightarrow 2^{-}}\left(x^{3}-3\right)=2^{3}-3=5 \\
& \lim _{x \rightarrow 2^{+}} f(x)=\lim _{x \rightarrow 2^{+}}\left(x^{2}+1\right)=2^{2}+1=5 \\
& \therefore \lim _{x \rightarrow 2} f(x)=f(2)
\end{aligned}
$$

Therefore, $f$ is continuous at $x=2$.
Case III:
If $c>2$, then $f(c)=c^{2}+1$

$$
\begin{aligned}
& \lim _{x \rightarrow c} f(x)=\lim _{x \rightarrow c}\left(x^{2}+1\right)=c^{2}+1 \\
& \therefore \lim _{x \rightarrow c} f(x)=f(c)
\end{aligned}
$$

Therefore, $f$ is continuous at all points $x$, such that $x>2$.
Thus, the given function $f$ is continuous at every point on the real line.
Hence, $f$ has no point of discontinuity.
:::

:::

:::question{number="12" kind="exercise" id="q_5.1.12" topic="Continuity: piecewise function"}
#### Question 12

:::prompt
$f(x)= \begin{cases}x^{10}-1, & \text { if } x \leq 1 \\ x^{2}, & \text { if } x>1\end{cases}$
:::

:::solution{label="Solution"}
The given function is $f(x)=\left\{\begin{array}{l}x^{10}-1, \text { if } x \leq 1 \\ x^{2}, \text { if } x>1\end{array}\right.$
The given function $f$ is defined at all the points of the real line.
Let $c$ be a point on the real line.
Case I:
If $c<1$, then $f(c)=c^{10}-1$

$$
\begin{aligned}
& \lim _{x \rightarrow c} f(x)=\lim _{x \rightarrow c}\left(x^{10}-1\right)=c^{10}-1 \\
& \therefore \lim _{x \rightarrow \infty} f(x)=f(c)
\end{aligned}
$$

Therefore, $f$ is continuous at all points $x$, such that $x<1$.
Case II:
If $c=1$, then the left hand limit of $f$ at $x=1$ is,

$$
\lim _{x \rightarrow 1^{-}} f(x)=\lim _{x \rightarrow 1^{-}}\left(x^{10}-1\right)=1^{10}-1=1-1=0
$$

The right hand limit of $f$ at $x=1$ is,

$$
\lim _{x \rightarrow 1^{+}} f(x)=\lim _{x \rightarrow 1^{+}}\left(x^{2}\right)=1^{2}=1
$$

It is observed that the left and right hand limit of $f$ at $x=1$ do not coincide.
Therefore, $f$ is not continuous at $x=1$.
Case III:
If $c>1$, then $f(c)=c^{2}$

$$
\begin{aligned}
& \lim _{x \rightarrow c} f(x)=\lim _{x \rightarrow c}\left(x^{2}\right)=c^{2} \\
& \therefore \lim _{x \rightarrow c} f(x)=f(c)
\end{aligned}
$$

Therefore, $f$ is continuous at all points $x$, such that $x>1$.
Thus from the above observation, it can be concluded that $x=1$ is the only point of discontinuity of $f$.
:::

:::

:::question{number="13" kind="exercise" id="q_5.1.13" topic="Continuity: piecewise function"}
#### Question 13

:::prompt
Is the function defined by
$$
f(x)= \begin{cases}x+5, & \text { if } x \leq 1 \\ x-5, & \text { if } x>1\end{cases}
$$
a continuous function?

Discuss the continuity of the function $f$, where $f$ is defined by
:::

:::solution{label="Solution"}
The given function is $f(x)=\left\{\begin{array}{l}x+5, \text { if } x \leq 1 \\ x-5, \text { if } x>1\end{array}\right.$
The given function $f$ is defined at all the points of the real line.
Let $c$ be a point on the real line.
Case I:
If $c<1$, then $f(c)=c+5$

$$
\begin{aligned}
& \lim _{x \rightarrow c} f(x)=\lim _{x \rightarrow c}(x+5)=c+5 \\
& \therefore \lim _{x \rightarrow c} f(x)=f(c)
\end{aligned}
$$

Therefore, $f$ is continuous at all points $x$, such that $x<1$.
Case II:
If $c=1$, then $f(1)=1+5=6$

The left hand limit of $f$ at $x=1$ is,

$$
\lim _{x \rightarrow 1^{-}} f(x)=\lim _{x \rightarrow 1^{-}}(x+5)=1+5=6
$$

The right hand limit of $f$ at $x=1$ is,

$$
\lim _{x \rightarrow 1^{+}} f(x)=\lim _{x \rightarrow 1^{+}}(x-5)=1-5=-4
$$

It is observed that the left and right hand limit of $f$ at $x=1$ do not coincide.
Therefore, $f$ is not continuous at $x=1$.
Case III:
If $c>1$, then $f(c)=c-5$

$$
\begin{aligned}
& \lim _{x \rightarrow c} f(x)=\lim _{x \rightarrow c}(x-5)=c-5 \\
& \therefore \lim _{x \rightarrow c} f(x)=f(c)
\end{aligned}
$$

Therefore, $f$ is continuous at all points $x$, such that $x>1$.
From the above observation it can be concluded that, $x=1$ is the only point of discontinuity of $f$.
:::

:::

:::question{number="14" kind="exercise" id="q_5.1.14" topic="Continuity: piecewise function"}
#### Question 14

:::prompt
$f(x)=\left\{\begin{array}{l}3, \text { if } 0 \leq x \leq 1 \\ 4, \text { if } 1<x<3 \\ 5, \text { if } 3 \leq x \leq 10\end{array}\right.$
:::

:::solution{label="Solution"}
The given function is

$$
f(x)=\left\{\begin{array}{l}
3, \text { if } 0 \leq x \leq 1 \\
4, \text { if } 1<x<3 \\
5, \text { if } 3 \leq x \leq 10
\end{array}\right.
$$

The given function $f$ is defined at all the points of the interval $[0,10]$.
Let $c$ be a point in the interval $[0,10]$.

Case I:
If $0 \leq c<1$, then $f(c)=3$

$$
\begin{aligned}
& \lim _{x \rightarrow c} f(x)=\lim _{x \rightarrow c}(3)=3 \\
& \therefore \lim _{x \rightarrow c} f(x)=f(c)
\end{aligned}
$$

Therefore, $f$ is continuous in the interval $[0,1)$.
Case II:
If $c=1$, then $f(3)=3$
The left hand limit of $f$ at $x=1$ is,

$$
\lim _{x \rightarrow 1^{-}} f(x)=\lim _{x \rightarrow 1^{-}}(3)=3
$$

The right hand limit of $f$ at $x=1$ is,

$$
\lim _{x \rightarrow 1^{+}} f(x)=\lim _{x \rightarrow 1^{+}}(4)=4
$$

It is observed that the left and right hand limit of $f$ at $x=1$ do not coincide.
Therefore, $f$ is not continuous at $x=1$.
Case III:
If $1<c<3$, then $f(c)=4$

$$
\begin{aligned}
& \lim _{x \rightarrow c} f(x)=\lim _{x \rightarrow c}(4)=4 \\
& \therefore \lim _{x \rightarrow c} f(x)=f(c)
\end{aligned}
$$

Therefore, $f$ is continuous at in the interval $(1,3)$.
Case IV:
If $c=3$, then $f(c)=5$
The left hand limit of $f$ at $x=3$ is,

$$
\lim _{x \rightarrow 3^{-}} f(x)=\lim _{x \rightarrow 3^{-}}(4)=4
$$

The right hand limit of $f$ at $x=3$ is,

$$
\lim _{x \rightarrow 3^{+}} f(x)=\lim _{x \rightarrow 3^{+}}(5)=5
$$

It is observed that the left and right hand limit of $f$ at $x=3$ do not coincide.
Therefore, $f$ is discontinuous at $x=3$.
Case V:
If $3<c \leq 10$, then $f(c)=5$

$$
\begin{aligned}
& \lim _{x \rightarrow c} f(x)=\lim _{x \rightarrow c}(5)=5 \\
& \therefore \lim _{x \rightarrow c} f(x)=f(c)
\end{aligned}
$$

Therefore, $f$ is continuous at all points of the interval $(3,10]$.
Hence, $f$ is discontinuous at $x=1$ and $x=3$.
:::

:::

:::question{number="15" kind="exercise" id="q_5.1.15" topic="Continuity: piecewise function"}
#### Question 15

:::prompt
$f(x)= \begin{cases}2 x, & \text { if } x<0 \\ 0, & \text { if } 0 \leq x \leq 1 \\ 4 x, & \text { if } x>1\end{cases}$
:::

:::solution{label="Solution"}
The given function is

$$
f(x)=\left\{\begin{array}{l}
2 x, \text { if } x<0 \\
0, \text { if } 0 \leq x \leq 1 \\
4 x, \text { if } x>1
\end{array}\right.
$$

The given function $f$ is defined at all the points of the real line.
Let $c$ be a point on the real line.
Case I:
If $c<0$, then $f(c)=2 c$

$$
\begin{aligned}
& \lim _{x \rightarrow c} f(x)=\lim _{x \rightarrow c}(2 x)=2 c \\
& \therefore \lim _{x \rightarrow c} f(x)=f(c)
\end{aligned}
$$

Therefore, $f$ is continuous at all points $x$, such that $x<0$.
Case II:
If $c=0$, then $f(c)=f(0)=0$
The left hand limit of $f$ at $x=0$ is,

$$
\lim _{x \rightarrow 0^{-}} f(x)=\lim _{x \rightarrow 0^{-}}(2 x)=2(0)=0
$$

The right hand limit of $f$ at $x=0$ is,

$$
\begin{aligned}
& \lim _{x \rightarrow 0^{+}} f(x)=\lim _{x \rightarrow 0^{+}}(0)=0 \\
& \therefore \lim _{x \rightarrow 0} f(x)=f(0)
\end{aligned}
$$

Therefore, $f$ is continuous at $x=0$
Case III:
If $0<c<1$, then $f(x)=0$

$$
\begin{aligned}
& \lim _{x \rightarrow c} f(x)=\lim _{x \rightarrow c}(0)=0 \\
& \therefore \lim _{x \rightarrow c} f(x)=f(c)
\end{aligned}
$$

Therefore, $f$ is continuous in the interval $(0,1)$.
Case IV:
If $c=1$, then $f(c)=f(1)=0$
The left hand limit of $f$ at $x=1$ is,

$$
\lim _{x \rightarrow 1^{-}} f(x)=\lim _{x \rightarrow 1^{-}}(0)=0
$$

The right hand limit of $f$ at $x=1$ is,

$$
\lim _{x \rightarrow 1^{+}} f(x)=\lim _{x \rightarrow 1^{+}}(4 x)=4(1)=4
$$

It is observed that the left and right hand limit of $f$ at $x=1$ do not coincide.
Therefore, $f$ is not continuous at $x=1$.
Case V:
If $c<1$, then $f(c)=4 c$

$$
\begin{aligned}
& \lim _{x \rightarrow c} f(x)=\lim _{x \rightarrow c}(4 x)=4 c \\
& \therefore \lim _{x \rightarrow c} f(x)=f(c)
\end{aligned}
$$

Therefore, $f$ is continuous at all points $x$, such that $x>1$.
Hence, $f$ is not continuous only at $x=1$.
:::

:::

:::question{number="16" kind="exercise" id="q_5.1.16" topic="Continuity: piecewise function"}
#### Question 16

:::prompt
$f(x)= \begin{cases}-2, & \text { if } x \leq-1 \\ 2 x, & \text { if }-1<x \leq 1 \\ 2, & \text { if } x>1\end{cases}$
:::

:::solution{label="Solution"}
The given function is

$$
f(x)=\left\{\begin{array}{l}
-2, \text { if } x \leq-1 \\
2 x, \text { if }-1<x \leq 1 \\
2, \text { if } x>1
\end{array}\right.
$$

The given function $f$ is defined at all the points.
Let $c$ be a point on the real line.
Case I:
If $c<-1$, then $f(c)=-2$

$$
\begin{aligned}
& \lim _{x \rightarrow c} f(x)=\lim _{x \rightarrow c}(-2)=-2 \\
& \therefore \lim _{x \rightarrow c} f(x)=f(c)
\end{aligned}
$$

Therefore, $f$ is continuous at all points $x$, such that $x<-1$.
Case II:
If $c=-1$, then $f(c)=f(-1)=-2$
The left hand limit of $f$ at $x=-1$ is,

$$
\lim _{x \rightarrow-1^{-}} f(x)=\lim _{x \rightarrow-1^{-}}(-2)=-2
$$

The right hand limit of $f$ at $x=-1$ is,

$$
\begin{aligned}
& \lim _{x \rightarrow-1^{+}} f(x)=\lim _{x \rightarrow-1^{+}}(2 x)=2(-1)=-2 \\
& \therefore \lim _{x \rightarrow-1} f(x)=f(-1)
\end{aligned}
$$

Therefore, $f$ is continuous at $x=-1$

Case III:
If $-1<c<1$, then $f(c)=2 c$

$$
\begin{aligned}
& \lim _{x \rightarrow c} f(x)=\lim _{x \rightarrow c}(2 x)=2 c \\
& \therefore \lim _{x \rightarrow c} f(x)=f(c)
\end{aligned}
$$

Therefore, $f$ is continuous in the interval $(-1,1)$.
Case IV:
If $c=1$, then $f(c)=f(1)=2(1)=2$
The left hand limit of $f$ at $x=1$ is,

$$
\lim _{x \rightarrow 1^{-}} f(x)=\lim _{x \rightarrow 1^{-}}(2 x)=2(1)=2
$$

The right hand limit of $f$ at $x=1$ is,

$$
\begin{aligned}
& \lim _{x \rightarrow 1^{+}} f(x)=\lim _{x \rightarrow 1^{+}}(2)=2 \\
& \therefore \lim _{x \rightarrow 1} f(x)=f(c)
\end{aligned}
$$

Therefore, $f$ is continuous at $x=2$.
Case V:
If $c>1$, then $f(c)=2$

$$
\begin{aligned}
& \lim _{x \rightarrow c} f(x)=\lim _{x \rightarrow c}(2)=2 \\
& \therefore \lim _{x \rightarrow c} f(x)=f(c)
\end{aligned}
$$

Therefore, $f$ is continuous at all points $x$, such that $x>1$.
Thus, from the above observations, it can be concluded that $f$ is continuous at all points of the real line.
:::

:::

:::question{number="17" kind="exercise" id="q_5.1.17" topic="Continuity: piecewise function"}
#### Question 17

:::prompt
Find the relationship between $a$ and $b$ so that the function $f$ defined by
$$
f(x)= \begin{cases}a x+1, & \text { if } x \leq 3 \\ b x+3, & \text { if } x>3\end{cases}
$$
is continuous at $x=3$.
:::

:::solution{label="Solution"}
The given function is $f(x)= \begin{cases}a x+1, & \text { if } x \leq 3 \\ b x+3, & \text { if } x>3\end{cases}$
For $f$ to be continuous at $x=3$, then

$$
\lim _{x \rightarrow 3^{-}} f(x)=\lim _{x \rightarrow 3^{+}} f(x)=f(3)
$$

Also,

$$
\begin{aligned}
& \lim _{x \rightarrow 3^{-}} f(x)=\lim _{x \rightarrow 3^{-}}(a x+1)=3 a+1 \\
& \lim _{x \rightarrow 3^{+}} f(x)=\lim _{x \rightarrow 3^{+}}(b x+3)=3 b+3 \\
& f(3)=3 a+1
\end{aligned}
$$

Therefore, from (1), we obtain

$$
\begin{aligned}
& 3 a+1=3 b+3=3 a+1 \\
& \Rightarrow 3 a+1=3 b+3 \\
& \Rightarrow 3 a=3 b+2 \\
& \Rightarrow a=b+\frac{2}{3}
\end{aligned}
$$

Therefore, the required relationship is given by, $a=b+\frac{2}{3}$.
:::

:::

:::question{number="18" kind="exercise" id="q_5.1.18" topic="Continuity: "}
#### Question 18

:::prompt
For what value of $\lambda$ is the function defined by
$$
f(x)= \begin{cases}\lambda\left(x^{2}-2 x\right), & \text { if } x \leq 0 \\ 4 x+1, & \text { if } x>0\end{cases}
$$
continuous at $x=0$ ? What about continuity at $x=1$ ?
:::

:::solution{label="Solution"}
The given function is

$$
f(x)=\left\{\begin{array}{l}
\lambda\left(x^{2}-2 x\right), \text { if } x \leq 0 \\
4 x+1, \text { if } x>0
\end{array}\right.
$$

If $f$ is continuous at $x=0$, then

$$
\begin{aligned}
& \lim _{x \rightarrow 0^{-}} f(x)=\lim _{x \rightarrow 0^{+}} f(x)=f(0) \\
& \Rightarrow \lim _{x \rightarrow 0^{-}} \lambda\left(x^{2}-2 x\right)=\lim _{x \rightarrow 0^{+}}(4 x+1)=\lambda\left(0^{2}-2 \times 0\right) \\
& \Rightarrow \lambda\left(0^{2}-2 \times 0\right)=4(0)+1=0 \\
& \Rightarrow 0=1=0
\end{aligned} \quad[\text { which is not possible }]
$$

Therefore, there is no value of $\lambda$ for which $f$ is continuous at $x=0$.
At $x=1$

$$
\begin{aligned}
& f(1)=4 x+1=4(1)+1=5 \\
& \lim _{x \rightarrow 1}(4 x+1)=4(1)+1=5 \\
& \therefore \lim _{x \rightarrow 1} f(x)=f(1)
\end{aligned}
$$

Therefore, for any values of $\lambda, f$ is continuous at $x=1$.
:::

:::

:::question{number="19" kind="exercise" id="q_5.1.19" topic="Continuity: g(x)=x-[x]"}
#### Question 19

:::prompt
Show that the function defined by $g(x)=x-[x]$ is discontinuous at all integral points. Here $[x]$ denotes the greatest integer less than or equal to $x$.
:::

:::solution{label="Solution"}
The given function is $g(x)=x-[x]$
It is evident that $g$ is defined at all integral points.
Let $n$ be an integer.

Then,

$$
g(n)=n-[n]=n-n=0
$$

The left hand limit of $g$ at $x=n$ is,

$$
\lim _{x \rightarrow n^{-}} g(x)=\lim _{x \rightarrow n^{-}}(x-[x])=\lim _{x \rightarrow n^{-}}(x)-\lim _{x \rightarrow n^{-}}[x]=n-(n-1)=1
$$

The right hand limit of $g$ at $x=n$ is,

$$
\lim _{x \rightarrow n^{+}} g(x)=\lim _{x \rightarrow n^{+}}(x-[x])=\lim _{x \rightarrow n^{+}}(x)-\lim _{x \rightarrow n^{+}}[x]=n-n=0
$$

It is observed that the left and right hand limit of $g$ at $x=n$ do not coincide.
Therefore, $g$ is not continuous at $x=n$.
Hence, $g$ is discontinuous at all integral points.
:::

:::

:::question{number="20" kind="exercise" id="q_5.1.20" topic="Continuity: f(x)=x^2-sin x+5"}
#### Question 20

:::prompt
Is the function defined by $f(x)=x^{2}-\sin x+5$ continuous at $x=\pi$ ?
:::

:::solution{label="Solution"}
The given function is $f(x)=x^{2}-\sin x+5$
It is evident that $f$ is defined at $x=\pi$.
At $x=\pi, f(x)=f(\pi)=\pi^{2}-\sin \pi+5=\pi^{2}-0+5=\pi^{2}+5$
Consider $\lim _{x \rightarrow \pi} f(x)=\lim _{x \rightarrow \pi}\left(x^{2}-\sin x+5\right)$

Put $x=\pi+h$, it is evident that if $x \rightarrow \pi$, then $h \rightarrow 0$

$$
\begin{aligned}
\therefore \lim _{x \rightarrow \pi} f(x) & =\lim _{x \rightarrow \pi}\left(x^{2}-\sin x\right)+5 \\
& =\lim _{h \rightarrow 0}\left[(\pi+h)^{2}-\sin (\pi+h)+5\right] \\
& =\lim _{h \rightarrow 0}(\pi+h)^{2}-\lim _{h \rightarrow 0} \sin (\pi+h)+\lim _{h \rightarrow 0} 5 \\
& =(\pi+0)^{2}-\lim _{h \rightarrow 0}[\sin \pi \cos h+\cos \pi \sin h]+5 \\
& =\pi^{2}-\lim _{h \rightarrow 0} \sin \pi \cos h-\lim _{h \rightarrow 0} \cos \pi \sin h+5 \\
& =\pi^{2}-\sin \pi \cos 0-\cos \pi \sin 0+5 \\
& =\pi^{2}-0(1)-(-1) 0+5 \\
& =\pi^{2}+5 \\
& =f(\pi)
\end{aligned}
$$

Therefore, the given function $f$ is continuous at $x=\pi$.
:::

:::

:::question{number="21" kind="exercise" id="q_5.1.21" topic="Continuity: f(x)=sin x+cos x"}
#### Question 21

:::prompt
Discuss the continuity of the following functions:
:::

:::part{label="a"}
:::prompt
$f(x)=\sin x+\cos x$
:::

:::solution
It is known that if $g$ and $h$ are two continuous functions, then $g+h, g-h$ and $g \cdot h$ are also continuous.
Let $g(x)=\sin x$ and $h(x)=\cos x$ are continuous functions.
It is evident that $g(x)=\sin x$ is defined for every real number.
Let $c$ be a real number. Put $x=c+h$
If $x \rightarrow c$, then $h \rightarrow 0$
$$
\begin{aligned}
g(c)= & \sin c \\
\lim _{x \rightarrow c} g(x) & =\lim _{x \rightarrow c} \sin x \\
& =\lim _{h \rightarrow 0} \sin (c+h) \\
& =\lim _{h \rightarrow 0}[\sin c \cos h+\cos c \sin h] \\
& =\lim _{h \rightarrow 0}(\sin c \cos h)+\lim _{h \rightarrow 0}(\cos c \sin h) \\
& =\sin c \cos 0+\cos c \sin 0 \\
& =\sin c(1)+\cos c(0) \\
& =\sin c \\
\therefore \lim _{x \rightarrow c} g(x) & =g(c)
\end{aligned}
$$
Therefore, $g(x)=\sin x$ is a continuous function.
Let $h(x)=\cos x$
It is evident that $h(x)=\cos x$ is defined for every real number.
Let $c$ be a real number. Put $x=c+h$
If $x \rightarrow c$, then $h \rightarrow 0$
$$
h(c)=\cos c
$$
$$
\begin{aligned}
\lim _{x \rightarrow c} h(x) & =\lim _{x \rightarrow c} \cos x \\
& =\lim _{h \rightarrow 0} \cos (c+h) \\
& =\lim _{h \rightarrow 0}[\cos c \cos h-\sin c \sin h] \\
& =\lim _{h \rightarrow 0}(\cos c \cos h)-\lim _{h \rightarrow 0}(\sin c \sin h) \\
& =\cos c \cos 0-\sin c \sin 0 \\
& =\cos c(1)-\sin c(0) \\
& =\cos c \\
\therefore \lim _{x \rightarrow c} h(x) & =h(c)
\end{aligned}
$$
Therefore, $h(x)=\cos x$ is a continuous function.
:::

:::answer
**Answer:** $f(x)=g(x)+h(x)=\sin x+\cos x$ is a continuous function.
:::

:::

:::part{label="b"}
:::prompt
$f(x)=\sin x-\cos x$
:::

:::solution
It is known that if $g$ and $h$ are two continuous functions, then $g+h, g-h$ and $g \cdot h$ are also continuous.
Let $g(x)=\sin x$ and $h(x)=\cos x$ are continuous functions.
It is evident that $g(x)=\sin x$ is defined for every real number.
Let $c$ be a real number. Put $x=c+h$
If $x \rightarrow c$, then $h \rightarrow 0$
$$
\begin{aligned}
g(c)= & \sin c \\
\lim _{x \rightarrow c} g(x) & =\lim _{x \rightarrow c} \sin x \\
& =\lim _{h \rightarrow 0} \sin (c+h) \\
& =\lim _{h \rightarrow 0}[\sin c \cos h+\cos c \sin h] \\
& =\lim _{h \rightarrow 0}(\sin c \cos h)+\lim _{h \rightarrow 0}(\cos c \sin h) \\
& =\sin c \cos 0+\cos c \sin 0 \\
& =\sin c(1)+\cos c(0) \\
& =\sin c \\
\therefore \lim _{x \rightarrow c} g(x) & =g(c)
\end{aligned}
$$
Therefore, $g(x)=\sin x$ is a continuous function.
Let $h(x)=\cos x$
It is evident that $h(x)=\cos x$ is defined for every real number.
Let $c$ be a real number. Put $x=c+h$
If $x \rightarrow c$, then $h \rightarrow 0$
$$
h(c)=\cos c
$$
$$
\begin{aligned}
\lim _{x \rightarrow c} h(x) & =\lim _{x \rightarrow c} \cos x \\
& =\lim _{h \rightarrow 0} \cos (c+h) \\
& =\lim _{h \rightarrow 0}[\cos c \cos h-\sin c \sin h] \\
& =\lim _{h \rightarrow 0}(\cos c \cos h)-\lim _{h \rightarrow 0}(\sin c \sin h) \\
& =\cos c \cos 0-\sin c \sin 0 \\
& =\cos c(1)-\sin c(0) \\
& =\cos c \\
\therefore \lim _{x \rightarrow c} h(x) & =h(c)
\end{aligned}
$$
Therefore, $h(x)=\cos x$ is a continuous function.
:::

:::answer
**Answer:** $f(x)=g(x)-h(x)=\sin x-\cos x$ is a continuous function.
:::

:::

:::part{label="c"}
:::prompt
$f(x)=\sin x \cdot \cos x$
:::

:::solution
It is known that if $g$ and $h$ are two continuous functions, then $g+h, g-h$ and $g \cdot h$ are also continuous.
Let $g(x)=\sin x$ and $h(x)=\cos x$ are continuous functions.
It is evident that $g(x)=\sin x$ is defined for every real number.
Let $c$ be a real number. Put $x=c+h$
If $x \rightarrow c$, then $h \rightarrow 0$
$$
\begin{aligned}
g(c)= & \sin c \\
\lim _{x \rightarrow c} g(x) & =\lim _{x \rightarrow c} \sin x \\
& =\lim _{h \rightarrow 0} \sin (c+h) \\
& =\lim _{h \rightarrow 0}[\sin c \cos h+\cos c \sin h] \\
& =\lim _{h \rightarrow 0}(\sin c \cos h)+\lim _{h \rightarrow 0}(\cos c \sin h) \\
& =\sin c \cos 0+\cos c \sin 0 \\
& =\sin c(1)+\cos c(0) \\
& =\sin c \\
\therefore \lim _{x \rightarrow c} g(x) & =g(c)
\end{aligned}
$$
Therefore, $g(x)=\sin x$ is a continuous function.
Let $h(x)=\cos x$
It is evident that $h(x)=\cos x$ is defined for every real number.
Let $c$ be a real number. Put $x=c+h$
If $x \rightarrow c$, then $h \rightarrow 0$
$$
h(c)=\cos c
$$
$$
\begin{aligned}
\lim _{x \rightarrow c} h(x) & =\lim _{x \rightarrow c} \cos x \\
& =\lim _{h \rightarrow 0} \cos (c+h) \\
& =\lim _{h \rightarrow 0}[\cos c \cos h-\sin c \sin h] \\
& =\lim _{h \rightarrow 0}(\cos c \cos h)-\lim _{h \rightarrow 0}(\sin c \sin h) \\
& =\cos c \cos 0-\sin c \sin 0 \\
& =\cos c(1)-\sin c(0) \\
& =\cos c \\
\therefore \lim _{x \rightarrow c} h(x) & =h(c)
\end{aligned}
$$
Therefore, $h(x)=\cos x$ is a continuous function.
:::

:::answer
**Answer:** $f(x)=g(x) \times h(x)=\sin x \times \cos x$ is a continuous function.
:::

:::

:::

:::question{number="22" kind="exercise" id="q_5.1.22" topic="Continuity: Discuss the continuity of..."}
#### Question 22

:::prompt
Discuss the continuity of the cosine, cosecant, secant and cotangent functions.
:::

:::solution{label="Solution"}
It is known that if $g$ and $h$ are two continuous functions, then

(i) $\frac{h(x)}{g(x)}, g(x) \neq 0$ is continuous.
(ii) $\frac{1}{g(x)}, g(x) \neq 0$ is continuous.
(iii) $\frac{1}{h(x)}, h(x) \neq 0$ is continuous.

Let $g(x)=\sin x$ and $h(x)=\cos x$ are continuous functions.
It is evident that $g(x)=\sin x$ is defined for every real number.
Let $c$ be a real number. Put $x=c+h$
If $x \rightarrow c$, then $h \rightarrow 0$

$$
\begin{aligned}
g(c) & =\sin c \\
\lim _{x \rightarrow c} g(x) & =\lim _{x \rightarrow c} \sin x \\
& =\lim _{h \rightarrow 0} \sin (c+h) \\
& =\lim _{h \rightarrow 0}[\sin c \cos h+\cos c \sin h] \\
& =\lim _{h \rightarrow 0}(\sin c \cos h)+\lim _{h \rightarrow 0}(\cos c \sin h) \\
& =\sin c \cos 0+\cos c \sin 0 \\
& =\sin c(1)+\cos c(0) \\
& =\sin c \\
\therefore \lim _{x \rightarrow c} g(x) & =g(c)
\end{aligned}
$$

Therefore, $g(x)=\sin x$ is a continuous function.
Let $h(x)=\cos x$
It is evident that $h(x)=\cos x$ is defined for every real number.
Let $c$ be a real number. Put $x=c+h$
If $x \rightarrow c$, then $h \rightarrow 0$

$$
\begin{aligned}
h(c) & =\cos c \\
\lim _{x \rightarrow c} h(x) & =\lim _{x \rightarrow c} \cos x \\
& =\lim _{h \rightarrow 0} \cos (c+h) \\
& =\lim _{h \rightarrow 0}[\cos c \cos h-\sin c \sin h] \\
& =\lim _{h \rightarrow 0}(\cos c \cos h)-\lim _{h \rightarrow 0}(\sin c \sin h) \\
& =\cos c \cos 0-\sin c \sin 0 \\
& =\cos c(1)-\sin c(0) \\
& =\cos c \\
\therefore \lim _{x \rightarrow c} h(x) & =h(c)
\end{aligned}
$$

Therefore, $h(x)=\cos x$ is a continuous function.
Therefore, it can be concluded that,

$$
\begin{aligned}
& \operatorname{cosec} x=\frac{1}{\sin x}, \sin x \neq 0 \text { is continuous. } \\
& \Rightarrow \operatorname{cosec} x, x \neq n \pi(n \in Z) \text { is continuous. }
\end{aligned}
$$

Therefore, cosecant is continuous except at $x=n \pi(n \in Z)$

$$
\begin{aligned}
& \sec x=\frac{1}{\cos x}, \cos x \neq 0 \\
& \Rightarrow \sec x, x \neq(2 n+1) \frac{\pi}{2}(n \in Z) \text { is continuous. }
\end{aligned}
$$

Therefore, secant is continuous except at $x=(2 n+1) \frac{\pi}{2}(n \in Z)$
$\cot x=\frac{\cos x}{\sin x}, \sin x \neq 0$ is continuous.
$\Rightarrow \cot x, x \neq n \pi(n \in Z)$ is continuous.
Therefore, cotangent is continuous except at $x=n \pi(n \in Z)$.
:::

:::

:::question{number="23" kind="exercise" id="q_5.1.23" topic="Continuity: piecewise function"}
#### Question 23

:::prompt
Find all points of discontinuity of $f$, where
$$
f(x)= \begin{cases}\frac{\sin x}{x}, & \text { if } x<0 \\ x+1, & \text { if } x \geq 0\end{cases}
$$
:::

:::solution{label="Solution"}
The given function is

$$
f(x)=\left\{\begin{array}{l}
\frac{\sin x}{x}, \text { if } x<0 \\
x+1, \text { if } x \geq 0
\end{array}\right.
$$

The given function $f$ is defined at all the points of the real line.
Let $c$ be a point on the real line.
Case I:
If $c<0$, then $f(c)=\frac{\sin c}{c}$

$$
\begin{aligned}
& \lim _{x \rightarrow c} f(x)=\lim _{x \rightarrow c}\left(\frac{\sin x}{x}\right)=\frac{\sin c}{c} \\
& \therefore \lim _{x \rightarrow c} f(x)=f(c)
\end{aligned}
$$

Therefore, $f$ is continuous at all points $x$, such that $x<0$.
Case II:
If $c>0$, then $f(c)=c+1$

$$
\begin{aligned}
& \lim _{x \rightarrow c} f(x)=\lim _{x \rightarrow c}(x+1)=c+1 \\
& \therefore \lim _{x \rightarrow c} f(x)=f(c)
\end{aligned}
$$

Therefore, $f$ is continuous at all points $x$, such that $x>0$.

Case III:
If $c=0$, then $f(c)=f(0)=0+1=1$
The left hand limit of $f$ at $x=0$ is,

$$
\lim _{x \rightarrow 0^{-}} f(x)=\lim _{x \rightarrow 0^{-}}\left(\frac{\sin x}{x}\right)=1
$$

The right hand limit of $f$ at $x=0$ is,

$$
\begin{aligned}
& \lim _{x \rightarrow 0^{+}} f(x)=\lim _{x \rightarrow 0^{+}}(x+1)=1 \\
& \therefore \lim _{x \rightarrow 0^{-}} f(x)=\lim _{x \rightarrow 0^{+}} f(x)=f(0)
\end{aligned}
$$

Therefore, $f$ is continuous at $x=0$
From the above observations, it can be concluded that $f$ is continuous at all points of the real line.
Thus, $f$ has no point of discontinuity.
:::

:::

:::question{number="24" kind="exercise" id="q_5.1.24" topic="Continuity: piecewise function"}
#### Question 24

:::prompt
Determine if $f$ defined by
$$
f(x)= \begin{cases}x^{2} \sin \frac{1}{x}, & \text { if } x \neq 0 \\ 0, & \text { if } x=0\end{cases}
$$
is a continuous function?
:::

:::solution{label="Solution"}
The given function is

$$
f(x)=\left\{\begin{array}{l}
x^{2} \sin \frac{1}{x}, \text { if } x \neq 0 \\
0, \text { if } x=0
\end{array}\right.
$$

The given function $f$ is defined at all the points of the real line.
Let $c$ be a point on the real line.
Case I:
If $c \neq 0$, then $f(c)=c^{2} \sin \frac{1}{c}$

$$
\begin{aligned}
& \lim _{x \rightarrow c} f(x)=\lim _{x \rightarrow c}\left(x^{2} \sin \frac{1}{x}\right)=\left(\lim _{x \rightarrow c} x^{2}\right)\left(\lim _{x \rightarrow c} \sin \frac{1}{x}\right)=c^{2} \sin \frac{1}{c} \\
& \therefore \lim _{x \rightarrow c} f(x)=f(c)
\end{aligned}
$$

Therefore, $f$ is continuous at all points $x$, such that $x \neq 0$.
Case II:

If $c=0$, then $f(0)=0$

$$
\lim _{x \rightarrow 0^{-}} f(x)=\lim _{x \rightarrow 0^{-}}\left(x^{2} \sin \frac{1}{x}\right)=\lim _{x \rightarrow 0}\left(x^{2} \sin \frac{1}{x}\right)
$$

It is known that, $-1 \leq \sin \frac{1}{x} \leq 1, x \neq 0$

$$
\begin{aligned}
& \Rightarrow-x^{2} \leq x^{2} \sin \frac{1}{x} \leq x^{2} \\
& \Rightarrow \lim _{x \rightarrow 0}\left(-x^{2}\right) \leq \lim _{x \rightarrow 0}\left(x^{2} \sin \frac{1}{x}\right) \leq \lim _{x \rightarrow 0} x^{2} \\
& \Rightarrow 0 \leq \lim _{x \rightarrow 0}\left(x^{2} \sin \frac{1}{x}\right) \leq 0 \\
& \Rightarrow \lim _{x \rightarrow 0}\left(x^{2} \sin \frac{1}{x}\right)=0 \\
& \therefore \lim _{x \rightarrow 0^{-}} f(x)=0
\end{aligned}
$$

Similarly,

$$
\begin{aligned}
& \lim _{x \rightarrow 0^{+}} f(x)=\lim _{x \rightarrow 0^{+}}\left(x^{2} \sin \frac{1}{x}\right)=\lim _{x \rightarrow 0}\left(x^{2} \sin \frac{1}{x}\right)=0 \\
& \therefore \lim _{x \rightarrow 0^{-}} f(x)=f(0)=\lim _{x \rightarrow 0^{+}} f(x)
\end{aligned}
$$

Therefore, $f$ is continuous at $x=0$.
From the above observations, it can be concluded that $f$ is continuous at every point of the real line.
Thus, $f$ is a continuous function.
:::

:::

:::question{number="25" kind="exercise" id="q_5.1.25" topic="Continuity: piecewise function"}
#### Question 25

:::prompt
Examine the continuity of $f$, where $f$ is defined by
$$
f(x)= \begin{cases}\sin x-\cos x, & \text { if } x \neq 0 \\ -1, & \text { if } x=0\end{cases}
$$
Find the values of $k$ so that the function $f$ is continuous at the indicated point in Exercises 26 to 29.
:::

:::solution{label="Solution"}
The given function is $f(x)=\left\{\begin{array}{l}\sin x-\cos x, \text { if } x \neq 0 \\ -1, \text { if } x=0\end{array}\right.$
The given function $f$ is defined at all the points of the real line.
Let $c$ be a point on the real line.
Case I:
If $c \neq 0$, then $f(c)=\sin c-\cos c$

$$
\begin{aligned}
& \lim _{x \rightarrow c} f(x)=\lim _{x \rightarrow c}(\sin x-\cos x)=\sin c-\cos c \\
& \therefore \lim _{x \rightarrow c} f(x)=f(c)
\end{aligned}
$$

Therefore, $f$ is continuous at all points $x$, such that $x \neq 0$.

Case II:
If $c=0$, then $f(0)=-1$

$$
\begin{aligned}
\lim _{x \rightarrow 0^{-}} f(x) & =\lim _{x \rightarrow 0}(\sin x-\cos x)=\sin 0-\cos 0=0-1=-1 \\
\lim _{x \rightarrow 0^{+}} f(x) & =\lim _{x \rightarrow 0}(\sin x-\cos x)=\sin 0-\cos 0=0-1=-1 \\
\lim _{x \rightarrow 0^{-}} f(x) & =\lim _{x \rightarrow 0^{+}} f(x)=f(0)
\end{aligned}
$$

Therefore, $f$ is continuous at $x=0$.
From the above observations, it can be concluded that $f$ is continuous at every point of the real line.
Thus, $f$ is a continuous function.
:::

:::

:::question{number="26" kind="exercise" id="q_5.1.26" topic="Continuity: piecewise function"}
#### Question 26

:::prompt
$f(x)=\left\{\begin{array}{ll}\frac{k \cos x}{\pi-2 x}, & \text { if } x \neq \frac{\pi}{2} \\ 3, & \text { if } x=\frac{\pi}{2}\end{array} \quad\right.$ at $x=\frac{\pi}{2}$
:::

:::solution{label="Solution"}
The given function is

$$
f(x)=\left\{\begin{array}{l}
\frac{k \cos x}{\pi-2 x}, \text { if } x \neq \frac{\pi}{2} \\
3, \text { if } x=\frac{\pi}{2}
\end{array}\right.
$$

The given function $f$ is continuous at $x=\frac{\pi}{2}$, if $f$ is defined at $x=\frac{\pi}{2}$ and if the value of the $f$ at $x=\frac{\pi}{2}$ equals the limit of $f$ at $x=\frac{\pi}{2}$.
It is evident that $f$ is defined at $x=\frac{\pi}{2}$ and $f\left(\frac{\pi}{2}\right)=3$

$$
\begin{aligned}
& \lim _{x \rightarrow \frac{\pi}{2}} f(x)=\lim _{x \rightarrow \frac{\pi}{2}} \frac{k \cos x}{\pi-2 x} \\
& \text { Put } x=\frac{\pi}{2}+h
\end{aligned}
$$

Then $x \rightarrow \frac{\pi}{2} \Rightarrow h \rightarrow 0$

$$
\begin{aligned}
& \therefore \lim _{x \rightarrow \frac{\pi}{2}} f(x)=\lim _{x \rightarrow \frac{\pi}{2}} \frac{k \cos x}{\pi-2 x}=\lim _{h \rightarrow 0} \frac{k \cos \left(\frac{\pi}{2}+h\right)}{\pi-2\left(\frac{\pi}{2}+h\right)} \\
& \quad=k \lim _{h \rightarrow 0} \frac{-\sin h}{-2 h}=\frac{k}{2} \lim _{h \rightarrow 0} \frac{\sin h}{h}=\frac{k}{2} \cdot 1=\frac{k}{2} \\
& \therefore \lim _{x \rightarrow \frac{\pi}{2}} f(x)=f\left(\frac{\pi}{2}\right) \\
& \Rightarrow \frac{k}{2}=3 \\
& \Rightarrow k=6
\end{aligned}
$$

Therefore, the value of $k=6$.
:::

:::

:::question{number="27" kind="exercise" id="q_5.1.27" topic="Continuity: piecewise function"}
#### Question 27

:::prompt
$f(x)=\left\{\begin{array}{ll}k x^{2}, & \text { if } x \leq 2 \\ 3, & \text { if } x>2\end{array} \quad\right.$ at $x=2$
:::

:::solution{label="Solution"}
The given function is $f(x)=\left\{\begin{array}{l}k x^{2}, \text { if } x \leq 2 \\ 3, \text { if } x>2\end{array}\right.$
The given function $f$ is continuous at $x=2$, if $f$ is defined at $x=2$ and if the value of the $f$ at $x=2$ equals the limit of $f$ at $x=2$.

It is evident that $f$ is defined at $x=2$ and $f(2)=k(2)^{2}=4 k$

$$
\begin{aligned}
& \lim _{x \rightarrow 2^{-}} f(x)=\lim _{x \rightarrow 2^{+}} f(x)=f(2) \\
& \Rightarrow \lim _{x \rightarrow 2^{-}}\left(k x^{2}\right)=\lim _{x \rightarrow 2^{+}}(3)=4 k \\
& \Rightarrow k \times 2^{2}=3=4 k \\
& \Rightarrow 4 k=3 \\
& \Rightarrow k=\frac{3}{4}
\end{aligned}
$$

Therefore, the value of $k=\frac{3}{4}$.
:::

:::

:::question{number="28" kind="exercise" id="q_5.1.28" topic="Continuity: piecewise function"}
#### Question 28

:::prompt
$f(x)=\left\{\begin{array}{ll}k x+1, & \text { if } x \leq \pi \\ \cos x, & \text { if } x>\pi\end{array} \quad\right.$ at $x=\pi$
:::

:::solution{label="Solution"}
The given function is $f(x)=\left\{\begin{array}{l}k x+1, \text { if } x \leq \pi \\ \cos x, \text { if } x>\pi\end{array}\right.$
The given function $f$ is continuous at $x=\pi$, if $f$ is defined at $x=\pi$ and if the value of the $f$ at $x=\pi$ equals the limit of $f$ at $x=\pi$.

It is evident that $f$ is defined at $x=\pi$ and $f(\pi)=k \pi+1$

$$
\begin{aligned}
& \lim _{x \rightarrow \pi^{-}} f(x)=\lim _{x \rightarrow \pi^{+}} f(x)=f(\pi) \\
& \Rightarrow \lim _{x \rightarrow \pi^{-}}(k x+1)=\lim _{x \rightarrow \pi^{+}}(\cos x)=k \pi+1 \\
& \Rightarrow k \pi+1=\cos \pi=k \pi+1 \\
& \Rightarrow k \pi+1=-1=k \pi+1 \\
& \Rightarrow k=-\frac{2}{\pi}
\end{aligned}
$$

Therefore, the value of $k=-\frac{2}{\pi}$.
:::

:::

:::question{number="29" kind="exercise" id="q_5.1.29" topic="Continuity: piecewise function"}
#### Question 29

:::prompt
$f(x)=\left\{\begin{array}{ll}k x+1, & \text { if } x \leq 5 \\ 3 x-5, & \text { if } x>5\end{array} \quad\right.$ at $x=5$
:::

:::solution{label="Solution"}
The given function is $f(x)=\left\{\begin{array}{l}k x+1, \text { if } x \leq 5 \\ 3 x-5, \text { if } x>5\end{array}\right.$
The given function $f$ is continuous at $x=5$, if $f$ is defined at $x=5$ and if the value of the $f$ at $x=5$ equals the limit of $f$ at $x=5$.

It is evident that $f$ is defined at $x=5$ and $f(5)=k x+1=5 k+1$

$$
\begin{aligned}
& \lim _{x \rightarrow 5^{-}} f(x)=\lim _{x \rightarrow 5^{+}} f(x)=f(5) \\
& \Rightarrow \lim _{x \rightarrow 5^{-}}(k x+1)=\lim _{x \rightarrow 5^{+}}(3 x-5)=5 k+1 \\
& \Rightarrow 5 k+1=3(5)-5=5 k+1 \\
& \Rightarrow 5 k+1=15-5=5 k+1 \\
& \Rightarrow 5 k+1=10=5 k+1 \\
& \Rightarrow 5 k+1=10 \\
& \Rightarrow 5 k=9 \\
& \Rightarrow k=\frac{9}{5}
\end{aligned}
$$

Therefore, the value of $k=\frac{9}{5}$.
:::

:::

:::question{number="30" kind="exercise" id="q_5.1.30" topic="Continuity: piecewise function"}
#### Question 30

:::prompt
Find the values of $a$ and $b$ such that the function defined by
$$
f(x)= \begin{cases}5, & \text { if } x \leq 2 \\ a x+b, & \text { if } 2<x<10 \\ 21, & \text { if } x \geq 10\end{cases}
$$
is a continuous function.
:::

:::solution{label="Solution"}
The given function is

$$
f(x)=\left\{\begin{array}{l}
5, \text { if } x \leq 2 \\
a x+b, \text { if } 2<x<10 \\
21, \text { if } x \geq 10
\end{array}\right.
$$

It is evident that $f$ is defined at all points of the real line.
If $f$ is a continuous function, then $f$ is continuous at all real numbers.
In particular, $f$ is continuous at $x=2$ and $x=10$
Since $f$ is continuous at $x=2$, we obtain

$$
\begin{aligned}
& \lim _{x \rightarrow 2^{-}} f(x)=\lim _{x \rightarrow 2^{+}} f(x)=f(2) \\
& \Rightarrow \lim _{x \rightarrow 2^{-}}(5)=\lim _{x \rightarrow 2^{+}}(a x+b)=5 \\
& \Rightarrow 5=2 a+b=5 \\
& \Rightarrow 2 a+b=5
\end{aligned}
$$

Since $f$ is continuous at $x=10$, we obtain

$$
\begin{aligned}
& \lim _{x \rightarrow 10^{-}} f(x)=\lim _{x \rightarrow 10^{+}} f(x)=f(10) \\
& \Rightarrow \lim _{x \rightarrow 10^{-}}(a x+b)=\lim _{x \rightarrow 10^{+}}(21)=21 \\
& \Rightarrow 10 a+b=21=21 \\
& \Rightarrow 10 a+b=21
\end{aligned}
$$

On subtracting equation (1) from equation (2), we obtain

$$
\begin{aligned}
& 8 a=16 \\
& \Rightarrow a=2
\end{aligned}
$$

By putting $a=2$ in equation (1), we obtain

$$
\begin{aligned}
& 2(2)+b=5 \\
& \Rightarrow 4+b=5 \\
& \Rightarrow b=1
\end{aligned}
$$

Therefore, the values of $a$ and $b$ for which $f$ is a continuous function are 2 and 1 respectively.
:::

:::

:::question{number="31" kind="exercise" id="q_5.1.31" topic="Continuity: f(x)=cos (x^2)"}
#### Question 31

:::prompt
Show that the function defined by $f(x)=\cos \left(x^{2}\right)$ is a continuous function.
:::

:::solution{label="Solution"}
The given function is $f(x)=\cos \left(x^{2}\right)$.
This function $f$ is defined for every real number and $f$ can be written as the composition of two functions as,

$$
\begin{aligned}
& f=g o h, \text { where } g(x)=\cos x \text { and } h(x)=x^{2} \\
& {\left[\because(g o h)(x)=g(h(x))=g\left(x^{2}\right)=\cos \left(x^{2}\right)=f(x)\right]}
\end{aligned}
$$

It has to be proved first that $g(x)=\cos x$ and $h(x)=x^{2}$ are continuous functions.
It is evident that $g$ is defined for every real number.
Let $c$ be a real number.
Let $g(c)=\cos c$. Put $x=c+h$
If $x \rightarrow c$, then $h \rightarrow 0$

$$
\begin{aligned}
\lim _{x \rightarrow c} g(x) & =\lim _{x \rightarrow c} \cos x \\
& =\lim _{h \rightarrow 0} \cos (c+h) \\
& =\lim _{h \rightarrow 0}[\cos c \cos h-\sin c \sin h] \\
& =\lim _{h \rightarrow 0}(\cos c \cos h)-\lim _{h \rightarrow 0}(\sin c \sin h) \\
& =\cos c \cos 0-\sin c \sin 0 \\
& =\cos c(1)-\sin c(0) \\
& =\cos c \\
\therefore \lim _{x \rightarrow c} g(x) & =g(c)
\end{aligned}
$$

Therefore, $g(x)=\cos x$ is a continuous function.

Let $h(x)=x^{2}$

It is evident that $h$ is defined for every real number.
Let $k$ be a real number, then $h(k)=k^{2}$

$$
\begin{aligned}
& \lim _{x \rightarrow k} h(x)=\lim _{x \rightarrow k} x^{2}=k^{2} \\
& \therefore \lim _{x \rightarrow k} h(x)=h(k)
\end{aligned}
$$

Therefore, $h$ is a continuous function.
It is known that for real valued functions $g$ and $h$, such that $(g o h)$ is defined at $c$, if $g$ is continuous at $c$ and if $f$ is continuous at $g(c)$, then $(f o g)$ is continuous at $c$.
Therefore, $f(x)=(g o h)(x)=\cos \left(x^{2}\right)$ is a continuous function.
:::

:::

:::question{number="32" kind="exercise" id="q_5.1.32" topic="Continuity: f(x)=|cos x|"}
#### Question 32

:::prompt
Show that the function defined by $f(x)=|\cos x|$ is a continuous function.
:::

:::solution{label="Solution"}
The given function is $f(x)=|\cos x|$.
This function $f$ is defined for every real number and $f$ can be written as the composition of two functions as,

$$
\begin{aligned}
& f=g o h, \text { where } g(x)=|x| \text { and } h(x)=\cos x \\
& \lceil\because(g o h)(x)=g(h(x))=g(\cos x)=|\cos x|=f(x)\rceil
\end{aligned}
$$

It has to be proved first that $g(x)=|x|$ and $h(x)=\cos x$ are continuous functions.

$$
g(x)=|x| \text { can be written as } g(x)=\left\{\begin{array}{l}
-x, \text { if } x<0 \\
x, \text { if } x \geq 0
\end{array}\right.
$$

It is evident that $g$ is defined for every real number.
Let $c$ be a real number.
Case I:
If $c<0$, then $g(c)=-c$

$$
\begin{aligned}
& \lim _{x \rightarrow c} g(x)=\lim _{x \rightarrow c}(-x)=-c \\
& \therefore \lim _{x \rightarrow c} g(x)=g(c)
\end{aligned}
$$

Therefore, $g$ is continuous at all points $x$, such that $x<0$.
Case II:
If $c>0$, then $g(c)=c$

$$
\begin{aligned}
& \lim _{x \rightarrow c} g(x)=\lim _{x \rightarrow c}(x)=c \\
& \therefore \lim _{x \rightarrow c} g(x)=g(c)
\end{aligned}
$$

Therefore, $g$ is continuous at all points $x$, such that $x>0$.
Case III:
If $c=0$, then $g(c)=g(0)=0$

$$
\begin{aligned}
& \lim _{x \rightarrow 0^{-}} g(x)=\lim _{x \rightarrow 0^{-}}(-x)=0 \\
& \lim _{x \rightarrow 0^{+}} g(x)=\lim _{x \rightarrow 0^{+}}(x)=0 \\
& \therefore \lim _{x \rightarrow 0^{-}} g(x)=\lim _{x \rightarrow 0^{+}}(x)=g(0)
\end{aligned}
$$

Therefore, $g$ is continuous at all $x=0$.
From the above three observations, it can be concluded that $g$ is continuous at all points.
Let $h(x)=\cos x$
It is evident that $h(x)=\cos x$ is defined for every real number.
Let $c$ be a real number. Put $x=c+h$
If $x \rightarrow c$, then $h \rightarrow 0$

$$
\begin{aligned}
h(c) & =\cos c \\
\lim _{x \rightarrow c} h(x) & =\lim _{x \rightarrow c} \cos x \\
& =\lim _{h \rightarrow 0} \cos (c+h) \\
& =\lim _{h \rightarrow 0}[\cos c \cos h-\sin c \sin h] \\
& =\lim _{h \rightarrow 0}(\cos c \cos h)-\lim _{h \rightarrow 0}(\sin c \sin h) \\
& =\cos c \cos 0-\sin c \sin 0 \\
& =\cos c(1)-\sin c(0) \\
& =\cos c \\
\therefore \lim _{x \rightarrow c} h(x) & =h(c)
\end{aligned}
$$

Therefore, $h(x)=\cos x$ is a continuous function.
It is known that for real valued functions $g$ and $h$, such that $(g o h)$ is defined at $c$, if $g$ is continuous at $c$ and if $f$ is continuous at $g(c)$, then $(f o g)$ is continuous at $c$.
Therefore, $f(x)=(g o h)(x)=g(h(x))=g(\cos x)=|\cos x|$ is a continuous function.
:::

:::

:::question{number="33" kind="exercise" id="q_5.1.33" topic="Continuity: sin |x|"}
#### Question 33

:::prompt
Examine that $\sin |x|$ is a continuous function.
:::

:::solution{label="Solution"}
The given function is $f(x)=|\sin x|$.
This function $f$ is defined for every real number and $f$ can be written as the composition of two functions as,

$$
\begin{aligned}
& f=g o h, \text { where } g(x)=|x| \text { and } h(x)=\sin x \\
& \lceil\because(g o h)(x)=g(h(x))=g(\sin x)=|\sin x|=f(x)\rceil
\end{aligned}
$$

It has to be proved first that $g(x)=|x|$ and $h(x)=\sin x$ are continuous functions.

$$
g(x)=|x| \text { can be written as } g(x)=\left\{\begin{array}{l}
-x, \text { if } x<0 \\
x, \text { if } x \geq 0
\end{array}\right.
$$

It is evident that $g$ is defined for every real number.
Let $c$ be a real number.
Case I:
If $c<0$, then $g(c)=-c$

$$
\begin{aligned}
& \lim _{x \rightarrow c} g(x)=\lim _{x \rightarrow c}(-x)=-c \\
& \therefore \lim _{x \rightarrow c} g(x)=g(c)
\end{aligned}
$$

Therefore, $g$ is continuous at all points $x$, such that $x<0$.
Case II:
If $c>0$, then $g(c)=c$

$$
\begin{aligned}
& \lim _{x \rightarrow c} g(x)=\lim _{x \rightarrow c}(x)=c \\
& \therefore \lim _{x \rightarrow c} g(x)=g(c)
\end{aligned}
$$

Therefore, $g$ is continuous at all points $x$, such that $x>0$.
Case III:
If $c=0$, then $g(c)=g(0)=0$

$$
\begin{aligned}
& \lim _{x \rightarrow 0^{-}} g(x)=\lim _{x \rightarrow 0^{-}}(-x)=0 \\
& \lim _{x \rightarrow 0^{+}} g(x)=\lim _{x \rightarrow 0^{+}}(x)=0 \\
& \therefore \lim _{x \rightarrow 0^{-}} g(x)=\lim _{x \rightarrow 0^{+}}(x)=g(0)
\end{aligned}
$$

Therefore, $g$ is continuous at all $x=0$.
From the above three observations, it can be concluded that $g$ is continuous at all points.
Let $h(x)=\sin x$
It is evident that $h(x)=\sin x$ is defined for every real number.
Let $c$ be a real number. Put $x=c+k$
If $x \rightarrow c$, then $k \rightarrow 0$

$$
\begin{aligned}
h(c) & =\sin c \\
\lim _{x \rightarrow c} h(x) & =\lim _{x \rightarrow c} \sin x \\
& =\lim _{k \rightarrow 0} \sin (c+k) \\
& =\lim _{k \rightarrow 0}[\sin c \cos k+\cos c \sin k] \\
& =\lim _{k \rightarrow 0}(\sin c \cos k)+\lim _{k \rightarrow 0}(\cos c \sin k) \\
& =\sin c \cos 0+\cos c \sin 0 \\
& =\sin c(1)+\cos c(0) \\
& =\sin c \\
\therefore \lim _{x \rightarrow c} h(x) & =h(c)
\end{aligned}
$$

Therefore, $h(x)=\sin x$ is a continuous function.
It is known that for real valued functions $g$ and $h$, such that $(g o h)$ is defined at $c$, if $g$ is continuous at $c$ and if $f$ is continuous at $g(c)$, then $(f o g)$ is continuous at $c$.

Therefore, $f(x)=(\operatorname{goh})(x)=g(h(x))=g(\sin x)=|\sin x|$ is a continuous function.
:::

:::

:::question{number="34" kind="exercise" id="q_5.1.34" topic="Continuity: f(x)=|x|-|x+1|"}
#### Question 34

:::prompt
Find all the points of discontinuity of $f$ defined by $f(x)=|x|-|x+1|$.
:::

:::solution{label="Solution"}
The given function is $f(x)=|x|-|x+1|$.
The two functions, $g$ and $h$ are defined as $g(x)=|x|$ and $h(x)=|x+1|$.
Then, $f=g-h$
The continuity of $g$ and $h$ are examined first.

$$
g(x)=|x| \text { can be written as } g(x)=\left\{\begin{array}{l}
-x, \text { if } x<0 \\
x, \text { if } x \geq 0
\end{array}\right.
$$

It is evident that $g$ is defined for every real number.
Let $c$ be a real number.
Case I:
If $c<0$, then $g(c)=-c$

$$
\begin{aligned}
& \lim _{x \rightarrow c} g(x)=\lim _{x \rightarrow c}(-x)=-c \\
& \therefore \lim _{x \rightarrow c} g(x)=g(c)
\end{aligned}
$$

Therefore, $g$ is continuous at all points $x$, such that $x<0$.
Case II:

If $c>0$, then $g(c)=c$

$$
\begin{aligned}
& \lim _{x \rightarrow c} g(x)=\lim _{x \rightarrow c}(x)=c \\
& \therefore \lim _{x \rightarrow c} g(x)=g(c)
\end{aligned}
$$

Therefore, $g$ is continuous at all points $x$, such that $x>0$.
Case III:
If $c=0$, then $g(c)=g(0)=0$

$$
\begin{aligned}
& \lim _{x \rightarrow 0^{-}} g(x)=\lim _{x \rightarrow 0^{-}}(-x)=0 \\
& \lim _{x \rightarrow 0^{+}} g(x)=\lim _{x \rightarrow 0^{+}}(x)=0 \\
& \therefore \lim _{x \rightarrow 0^{-}} g(x)=\lim _{x \rightarrow 0^{+}}(x)=g(0)
\end{aligned}
$$

Therefore, $g$ is continuous at all $x=0$.
From the above three observations, it can be concluded that $g$ is continuous at all points.

$$
h(x)=|x+1| \text { can be written as } h(x)=\left\{\begin{array}{l}
-(x+1), \text { if } x<-1 \\
x+1, \text { if } x \geq-1
\end{array}\right.
$$

It is evident that $h$ is defined for every real number.
Let $c$ be a real number.
Case I:
If $c<-1$, then $h(c)=-(c+1)$

$$
\begin{aligned}
& \lim _{x \rightarrow c} h(x)=\lim _{x \rightarrow c}[-(x+1)]=-(c+1) \\
& \therefore \lim _{x \rightarrow c} h(x)=h(c)
\end{aligned}
$$

Therefore, $h$ is continuous at all points $x$, such that $x<-1$.
Case II:
If $c>-1$, then $h(c)=c+1$

$$
\begin{aligned}
& \lim _{x \rightarrow c} h(x)=\lim _{x \rightarrow c}(x+1)=c+1 \\
& \therefore \lim _{x \rightarrow c} h(x)=h(c)
\end{aligned}
$$

Therefore, $h$ is continuous at all points $x$, such that $x>-1$.
Case III:
If $c=-1$, then $h(c)=h(-1)=-1+1=0$

$$
\begin{aligned}
& \lim _{x \rightarrow-1^{-}} h(x)=\lim _{x \rightarrow-1^{-}}[-(x+1)]=-(-1+1)=0 \\
& \lim _{x \rightarrow-1^{+}} h(x)=\lim _{x \rightarrow-1^{+}}(x+1)=(-1+1)=0 \\
& \therefore \lim _{x \rightarrow-1^{-}} h(x)=\lim _{x \rightarrow-1^{+}} h(x)=h(-1)
\end{aligned}
$$

Therefore, $h$ is continuous at $x=-1$.
From the above three observations, it can be concluded that $h$ is continuous at all points. It concludes that $g$ and $h$ are continuous functions. Therefore, $f=g-h$ is also a continuous function.

Therefore, $f$ has no point of discontinuity.
:::

:::

:::question{number="1" kind="exercise" id="q_5.2.1" topic="Derivative of composite function: sin (x^2+5)"}
#### Question 1

:::prompt
$\sin \left(x^{2}+5\right)$
:::

:::solution{label="Solution"}
Let $f(x)=\sin \left(x^{2}+5\right), u(x)=x^{2}+5$ and $v(t)=\sin t$
Then, $(\mathrm{vou})(x)=v(u(x))=v\left(x^{2}+5\right)=\tan \left(x^{2}+5\right)=f(x)$
Thus, $f$ is a composite of two functions.
Put $t=u(x)=x^{2}+5$
Then, we get

$$
\begin{aligned}
& \frac{d v}{d t}=\frac{d}{d t}(\sin t)=\cos t=\cos \left(x^{2}+5\right) \\
& \frac{d t}{d x}=\frac{d}{d x}\left(x^{2}+5\right)=\frac{d}{d x}\left(x^{2}\right)+\frac{d}{d x}(5)=2 x+0=2 x
\end{aligned}
$$

By chain rule of derivative,

$$
\frac{d f}{d x}=\frac{d v}{d t} \cdot \frac{d t}{d x}=\cos \left(x^{2}+5\right) \times 2 x=2 x \cos \left(x^{2}+5\right)
$$

Alternate method:

$$
\begin{aligned}
\frac{d}{d x}\left[\sin \left(x^{2}+5\right)\right] & =\cos \left(x^{2}+5\right) \cdot \frac{d}{d x}\left(x^{2}+5\right) \\
& =\cos \left(x^{2}+5\right) \cdot\left[\frac{d}{d x}\left(x^{2}\right)+\frac{d}{d x}(5)\right] \\
& =\cos \left(x^{2}+5\right) \cdot[2 x+0] \\
& =2 x \cos \left(x^{2}+5\right)
\end{aligned}
$$
:::

:::

:::question{number="2" kind="exercise" id="q_5.2.2" topic="Derivative of composite function: cos (sin x)"}
#### Question 2

:::prompt
$\cos (\sin x)$
:::

:::solution{label="Solution"}
Let $f(x)=\cos (\sin x), u(x)=\sin x$ and $v(t)=\cos t$
Then, $(v o u)(x)=v(u(x))=v(\sin x)=\cos (\sin x)=f(x)$
Here, $f$ is a composite function of two functions.
Put $t=u(x)=\sin x$

$$
\begin{aligned}
& \therefore \frac{d v}{d t}=\frac{d}{d t}[\cos t]=-\sin t=-\sin (\sin x) \\
& \frac{d t}{d x}=\frac{d}{d x}(\sin x)=\cos x
\end{aligned}
$$

By chain rule,

$$
\frac{d f}{d x}=\frac{d v}{d t} \cdot \frac{d t}{d x}=-\sin (\sin x) \cdot \cos x=-\cos x \sin (\sin x)
$$

## Alternate method:

$$
\begin{aligned}
\frac{d}{d x}[\cos (\sin x)] & =-\sin (\sin x) \cdot \frac{d}{d x}(\sin x) \\
& =-\sin (\sin x) \times \cos x \\
& =-\cos x \sin (\sin x)
\end{aligned}
$$
:::

:::

:::question{number="3" kind="exercise" id="q_5.2.3" topic="Derivative of composite function: sin (a x+b)"}
#### Question 3

:::prompt
$\sin (a x+b)$
:::

:::solution{label="Solution"}
Let $f(x)=\sin (a x+b), u(x)=a x+b$ and $v(t)=\sin t$
Then, $(v o u)(x)=v(u(x))=v(a x+b)=\sin (a x+b)=f(x)$
Here, $f$ is a composite function of two functions $u$ and $v$.
Put, $t=u(x)=a x+b$
Thus,

$$
\begin{aligned}
& \frac{d v}{d t}=\frac{d}{d t}(\sin t)=\cos t=\cos (a x+b) \\
& \frac{d t}{d x}=\frac{d}{d x}(a x+b)=\frac{d}{d x}(a x)+\frac{d}{d x}(b)=a+0=a
\end{aligned}
$$

Hence, by chain rule, we get

$$
\frac{d f}{d x}=\frac{d v}{d t} \cdot \frac{d t}{d x}=\cos (a x+b) \cdot a=a \cos (a x+b)
$$

## Alternate method:

$$
\begin{aligned}
\frac{d}{d x}[\sin (a x+b)] & =\cos (a x+b) \cdot \frac{d}{d x}(a x+b) \\
& =\cos (a x+b) \cdot\left[\frac{d}{d x}(a x)+\frac{d}{d x}(b)\right] \\
& =\cos (a x+b) \cdot(a+0) \\
& =a \cos (a x+b)
\end{aligned}
$$
:::

:::

:::question{number="4" kind="exercise" id="q_5.2.4" topic="Derivative of composite function: sec (tan (sqrt x))"}
#### Question 4

:::prompt
$\sec (\tan (\sqrt{x}))$
:::

:::solution{label="Solution"}
Let $f(x)=\sec (\tan (\sqrt{x})), u(x)=\sqrt{x}, v(t)=\tan t$ and $w(s)=\sec s$
Then, $($ wovou $)(x)=w[v(u(x))]=w[v(\sqrt{x})]=w(\tan \sqrt{x})=\sec (\tan \sqrt{x})=f(x)$
Here, $f$ is a composite function of three functions $u, v$ and $w$.
Put, $s=v(t)=\tan t$ and $t=u(x)=\sqrt{x}$
Then,

$$
\begin{aligned}
\frac{d w}{d s} & =\frac{d}{d s}(\sec s) \\
& =\sec s \tan s \\
& =\sec (\tan t) \cdot \tan (\tan t) \quad[s=\tan t] \\
& =\sec (\tan \sqrt{x}) \cdot \tan (\tan \sqrt{x}) \quad[t=\sqrt{x}]
\end{aligned}
$$

Now,

$$
\begin{aligned}
& \frac{d s}{d t}=\frac{d}{d t}(\tan t)=\sec ^{2} t=\sec ^{2} \sqrt{x} \\
& \frac{d t}{d x}=\frac{d}{d x}(\sqrt{x})=\frac{d}{d x}\left(x^{\frac{1}{2}}\right)=\frac{1}{2} \cdot x^{\frac{1}{2}-1}=\frac{1}{2 \sqrt{x}}
\end{aligned}
$$

Hence, by chain rule, we get

$$
\begin{aligned}
\frac{d}{d x}[\sec (\tan \sqrt{x})] & =\frac{d w}{d s} \cdot \frac{d s}{d t} \cdot \frac{d t}{d x} \\
& =\sec (\tan \sqrt{x}) \cdot \tan (\tan \sqrt{x}) \cdot \sec ^{2} \sqrt{x} \cdot \frac{1}{2 \sqrt{x}} \\
& =\frac{1}{2 \sqrt{x}} \sec ^{2} \sqrt{x} \sec (\tan \sqrt{x}) \tan (\tan \sqrt{x}) \\
& =\frac{\sec ^{2} \sqrt{x} \sec (\tan \sqrt{x}) \tan (\tan \sqrt{x})}{2 \sqrt{x}}
\end{aligned}
$$

Alternate method:

$$
\begin{aligned}
\frac{d}{d x}[\sec (\tan \sqrt{x})] & =\sec (\tan \sqrt{x}) \cdot \tan (\tan \sqrt{x}) \cdot \frac{d}{d x}(\tan \sqrt{x}) \\
& =\sec (\tan \sqrt{x}) \cdot \tan (\tan \sqrt{x}) \cdot \sec ^{2}(\sqrt{x}) \cdot \frac{d}{d x}(\sqrt{x}) \\
& =\sec (\tan \sqrt{x}) \cdot \tan (\tan \sqrt{x}) \cdot \sec ^{2}(\sqrt{x}) \cdot \frac{1}{2 \sqrt{x}} \\
& =\frac{\sec (\tan \sqrt{x}) \cdot \tan (\tan \sqrt{x}) \cdot \sec ^{2}(\sqrt{x})}{2 \sqrt{x}}
\end{aligned}
$$
:::

:::

:::question{number="5" kind="exercise" id="q_5.2.5" topic="Derivative of composite function: sin (a x+b)/cos (c x+d)"}
#### Question 5

:::prompt
$\frac{\sin (a x+b)}{\cos (c x+d)}$
:::

:::solution{label="Solution"}
Given, $f(x)=\frac{\sin (a x+b)}{\cos (c x+d)}$, where $g(x)=\sin (a x+b)$ and $h(x)=\cos (c x+d)$

$$
\therefore f=\frac{g^{\prime} h-g h^{\prime}}{h^{2}}
$$

Consider $g(x)=\sin (a x+b)$
Let $u(x)=a x+b, v(t)=\sin t$
Then $(v o u)(x)=v(u(x))=v(a x+b)=\sin (a x+b)=g(x)$
$\therefore g$ is a composite function of two functions, $u$ and $v$.
Put, $t=u(x)=a x+b$

$$
\begin{aligned}
& \frac{d v}{d t}=\frac{d}{d t}(\sin t)=\cos t=\cos (a x+b) \\
& \frac{d t}{d x}=\frac{d}{d x}(a x+b)=\frac{d}{d x}(a x)+\frac{d}{d x}(b)=a+0=a
\end{aligned}
$$

Thus, by chain rule, we get

$$
g^{\prime}=\frac{d g}{d x}=\frac{d v}{d t} \cdot \frac{d t}{d x}=\cos (a x+b) \cdot a=a \cos (a x+b)
$$

Consider $h(x)=\cos (c x+d)$
Let $p(x)=c x+d, q(y)=\cos y$
Then, $(q o p)(x)=q(p(x))=q(c x+d)=\cos (c x+d)=h(x)$
$\therefore h$ is a composite function of two functions, $p$ and $q$.
Put, $y=p(x)=c x+d$

$$
\begin{aligned}
& \frac{d q}{d y}=\frac{d}{d y}(\cos y)=-\sin y=-\sin (c x+d) \\
& \frac{d y}{d x}=\frac{d}{d x}(c x+d)=\frac{d}{d x}(c x)+\frac{d}{d x}(d)=c
\end{aligned}
$$

Using chain rule, we get

$$
\begin{aligned}
h^{\prime} & =\frac{d h}{d x}=\frac{d q}{d y} \cdot \frac{d y}{d x} \\
& =-\sin (c x+d) \times c \\
& =-c \sin (c x+d)
\end{aligned}
$$

Therefore,

$$
\begin{aligned}
f^{\prime} & =\frac{a \cos (a x+b) \cdot \cos (c x+d)-\sin (a x+b)\{-c \sin (c x+d)\}}{[\cos (c x+d)]^{2}} \\
& =\frac{a \cos (a x+b)}{\cos (c x+d)}+c \sin (a x+b) \cdot \frac{\sin (c x+d)}{\cos (c x+d)} \times \frac{1}{\cos (c x+d)} \\
& =a \cos (a x+b) \sec (c x+d)+c \sin (a x+b) \tan (c x+d) \sec (c x+d)
\end{aligned}
$$
:::

:::

:::question{number="6" kind="exercise" id="q_5.2.6" topic="Derivative of composite function: cos x^3 * sin ^2(x^5)"}
#### Question 6

:::prompt
$\cos x^{3} \cdot \sin ^{2}\left(x^{5}\right)$
:::

:::solution{label="Solution"}
Given, $\cos x^{3} . \sin ^{2}\left(x^{5}\right)$

$$
\begin{aligned}
\frac{d}{d x}\left[\cos x^{3} \cdot \sin ^{2}\left(x^{5}\right)\right] & =\sin ^{2}\left(x^{5}\right) \times \frac{d}{d x}\left(\cos x^{3}\right)+\cos x^{3} \times \frac{d}{d x}\left[\sin ^{2}\left(x^{5}\right)\right] \\
& =\sin ^{2}\left(x^{5}\right) \times\left(-\sin x^{3}\right) \times \frac{d}{d x}\left(x^{3}\right)+\cos x^{3} \times 2 \sin \left(x^{5}\right) \cdot \frac{d}{d x}\left[\sin x^{5}\right] \\
& =-\sin x^{3} \sin ^{2}\left(x^{5}\right) \times 3 x^{2}+2 \sin x^{5} \cos x^{3} \cdot \cos x^{5} \times \frac{d}{d x}\left(x^{5}\right) \\
& =-3 x^{2} \sin x^{3} \cdot \sin ^{2}\left(x^{5}\right)+2 \sin x^{5} \cos x^{5} \cos x^{3} \times 5 x^{4} \\
& =10 x^{4} \sin x^{5} \cos x^{5} \cos x^{3}-3 x^{2} \sin x^{3} \sin ^{2}\left(x^{5}\right)
\end{aligned}
$$
:::

:::

:::question{number="7" kind="exercise" id="q_5.2.7" topic="Derivative of composite function: 2 sqrt cot (x^2)"}
#### Question 7

:::prompt
$2 \sqrt{\cot \left(x^{2}\right)}$
:::

:::solution{label="Solution"}
$$
\begin{aligned}
\frac{d}{d x}\left[2 \sqrt{\cot \left(x^{2}\right)}\right] & =2 \cdot \frac{1}{2 \sqrt{\cot \left(x^{2}\right)}} \times \frac{d}{d x}\left[\cot \left(x^{2}\right)\right] \\
& =\sqrt{\frac{\sin \left(x^{2}\right)}{\cos \left(x^{2}\right)}} \times-\operatorname{cosec} e^{2}\left(x^{2}\right) \times \frac{d}{d x}\left(x^{2}\right) \\
& =\sqrt{\frac{\sin \left(x^{2}\right)}{\cos \left(x^{2}\right)}} \times \frac{-1}{\sin ^{2}\left(x^{2}\right)} \times(2 x) \\
& =\frac{-2 x}{\sin x^{2} \sqrt{\cos x^{2} \sin x^{2}}} \\
& =\frac{-2 \sqrt{2} x}{\sin x^{2} \sqrt{2 \sin x^{2} \cos x^{2}}} \\
& =\frac{-2 \sqrt{2} x}{\sin x^{2} \sqrt{\sin 2 x^{2}}}
\end{aligned}
$$
:::

:::

:::question{number="8" kind="exercise" id="q_5.2.8" topic="Derivative of composite function: cos (sqrt x)"}
#### Question 8

:::prompt
$\cos (\sqrt{x})$
:::

:::solution{label="Solution"}
Let $f(x)=\cos (\sqrt{x})$
Also, let $u(x)=\sqrt{x}$ and, $v(t)=\cos t$

Then,

$$
\begin{aligned}
(v o u)(x) & =v(u(x)) \\
& =v(\sqrt{x}) \\
& =\cos \sqrt{x} \\
& =f(x)
\end{aligned}
$$

Since, $f$ is a composite function of $u$ and $v$.

$$
t=u(x)=\sqrt{x}
$$

Then,

$$
\begin{aligned}
& \begin{array}{l}
\frac{d t}{d x}=\frac{d}{d x}(\sqrt{x})=\frac{d}{d x}\left(x^{\frac{1}{2}}\right)=\frac{1}{2} x^{\frac{-1}{2}} \\
\quad=\frac{1}{2 \sqrt{x}} \\
\quad \frac{d v}{d t}=\frac{d}{d t}(\cos t)=-\sin t
\end{array} \\
& \text { And, } \quad=-\sin (\sqrt{x})
\end{aligned}
$$

Using chain rule, we get

$$
\begin{aligned}
\frac{d t}{d x} & =\frac{d v}{d t} \cdot \frac{d t}{d x} \\
& =-\sin (\sqrt{x}) \cdot \frac{1}{2 \sqrt{x}} \\
& =-\frac{1}{2 \sqrt{x}} \sin (\sqrt{x}) \\
& =-\frac{\sin (\sqrt{x})}{2 \sqrt{x}}
\end{aligned}
$$

Alternate method:

$$
\begin{aligned}
\frac{d}{d x}[\cos (\sqrt{x})] & =-\sin (\sqrt{x}) \cdot \frac{d}{d x}(\sqrt{x}) \\
& =-\sin (\sqrt{x}) \times \frac{d}{d x}\left(x^{\frac{1}{2}}\right) \\
& =-\sin \sqrt{x} \times \frac{1}{2} x^{\frac{-1}{2}} \\
& =\frac{-\sin \sqrt{x}}{2 \sqrt{x}}
\end{aligned}
$$
:::

:::

:::question{number="9" kind="exercise" id="q_5.2.9" topic="Derivative of composite function: f(x)=|x-1|, x R"}
#### Question 9

:::prompt
Prove that the function $f$ given by
$$
f(x)=|x-1|, x \in \mathbf{R}
$$
is not differentiable at $x=1$.
:::

:::solution{label="Solution"}
Given, $f(x)=|x-1|, x \in \mathbf{R}$
It is known that a function $f$ is differentiable at a point $x=c$ in its domain if both $\lim _{h \rightarrow 0^{-}} \frac{f(c)-f(c-h)}{h}$ and $\lim _{h \rightarrow 0^{+}} \frac{f(c+h)-f(c)}{h}$ are finite and equal.

To check the differentiability of the given function at $x=1$,

Consider LHD at $x=1$

$$
\begin{aligned}
\lim _{h \rightarrow 0^{-}} \frac{f(1)-f(1-h)}{h} & =\lim _{h \rightarrow 0^{-}} \frac{f|1-1|-|1-h-1|}{h} \\
& =\lim _{h \rightarrow 0^{-}} \frac{0-|h|}{h} \\
& =\lim _{h \rightarrow 0^{-}} \frac{-h}{h} \quad(h<0 \Rightarrow|h|=-h) \\
& =-1
\end{aligned}
$$

Consider RHD at $x=1$

$$
\begin{aligned}
\lim _{h \rightarrow 0^{+}} \frac{f(1+h)-f(1)}{h} & =\lim _{h \rightarrow 0^{+}} \frac{f|1+h-1|-|1-1|}{h} \\
& =\lim _{h \rightarrow 0^{+}} \frac{|h|-0}{h} \\
& =\lim _{h \rightarrow 0^{+}} \frac{h}{h} \quad(h>0 \Rightarrow|h|=h) \\
& =1
\end{aligned}
$$

Since LHD and RHD at $x=1$ are not equal,

Therefore, $f$ is not differentiable at $x=1$.
:::

:::

:::question{number="10" kind="exercise" id="q_5.2.10" topic="Derivative of composite function: f(x)=[x], 0<x<3"}
#### Question 10

:::prompt
Prove that the greatest integer function defined by
$$
f(x)=[x], 0<x<3
$$
is not differentiable at $x=1$ and $x=2$.
:::

:::solution{label="Solution"}
Given, $f(x)=[x], 0<x<3$
It is known that a function $f$ is differentiable at a point $x=c$ in its domain if both $\lim _{h \rightarrow 0^{-}} \frac{f(c)-f(c-h)}{h}$ and $\lim _{h \rightarrow 0^{+}} \frac{f(c+h)-f(c)}{h}$ are finite and equal.
At $x=1$,

Consider the LHD at $x=1$

$$
\begin{aligned}
\lim _{h \rightarrow 0^{-}} \frac{f(1)-f(1-h)}{h} & =\lim _{h \rightarrow 0^{-}} \frac{[1]-[1-h]}{h} \\
& =\lim _{h \rightarrow 0^{-}} \frac{1-0}{h} \\
& =\lim _{h \rightarrow 0^{-}} \frac{1}{h} \\
& =\infty
\end{aligned}
$$

Consider RHD at $x=1$

$$
\begin{aligned}
\lim _{h \rightarrow 0^{+}} \frac{f(1+h)-f(1)}{h} & =\lim _{h \rightarrow 0^{+}} \frac{[1+h]-[1]}{h} \\
& =\lim _{h \rightarrow 0^{+}} \frac{1-1}{h} \\
& =\lim _{h \rightarrow 0^{+}} 0 \\
& =0
\end{aligned}
$$

Since LHD and RHD at $x=1$ are not equal,
Hence, $f$ is not differentiable at $x=1$.

To check the differentiability of the given function at $x=2$,
Consider LHD at $x=2$

$$
\begin{aligned}
\lim _{h \rightarrow 0^{-}} \frac{f(2)-f(2-h)}{h} & =\lim _{h \rightarrow 0^{-}} \frac{[2]-[2-h]}{h} \\
& =\lim _{h \rightarrow 0^{-}} \frac{2-1}{h} \\
& =\lim _{h \rightarrow 0^{-}} \frac{1}{h} \\
& =\infty
\end{aligned}
$$

Now, consider RHD at $x=2$

$$
\begin{aligned}
\lim _{h \rightarrow 0^{+}} \frac{f(2+h)-f(2)}{h} & =\lim _{h \rightarrow 0^{+}} \frac{[2+h]-[2]}{h} \\
& =\lim _{h \rightarrow 0^{+}} \frac{2-2}{h} \\
& =\lim _{h \rightarrow 0^{+}} 0 \\
& =0
\end{aligned}
$$

Since, LHD and RHD at $x=2$ are not equal.

Hence, $f$ is not differentiable at $x=2$.
:::

:::

:::question{number="1" kind="exercise" id="q_5.3.1" topic="Implicit derivative: 2 x+3 y=sin x"}
#### Question 1

:::prompt
$2 x+3 y=\sin x$
:::

:::solution{label="Solution"}
Given, $2 x+3 y=\sin x$
Differentiating with respect to $x$, we get

$$
\begin{aligned}
& \frac{d}{d y}(2 x+3 y)=\frac{d}{d x}(\sin x) \\
& \Rightarrow \frac{d}{d x}(2 x)+\frac{d}{d x}(3 y)=\cos x \\
& \Rightarrow 2+3 \frac{d y}{d x}=\cos x \\
& \Rightarrow 3 \frac{d y}{d x}=\cos x-2 \\
& \therefore \frac{d x}{d y}=\frac{\cos x-2}{3}
\end{aligned}
$$
:::

:::

:::question{number="2" kind="exercise" id="q_5.3.2" topic="Implicit derivative: 2 x+3 y=sin y"}
#### Question 2

:::prompt
$2 x+3 y=\sin y$
:::

:::solution{label="Solution"}
Given, $2 x+3 y=\sin y$
Differentiating with respect to $x$, we get

$$
\begin{aligned}
& \frac{d}{d x}(2 x)+\frac{d}{d x}(3 y)=\frac{d}{d x}(\sin y) \\
& \Rightarrow 2+3 \frac{d y}{d x}=\cos y \frac{d y}{d x} \quad \text { [By using chain rule] } \\
& \Rightarrow 2=(\cos y-3) \frac{d y}{d x} \\
& \therefore \frac{d y}{d x}=\frac{2}{\cos y-3}
\end{aligned}
$$
:::

:::

:::question{number="3" kind="exercise" id="q_5.3.3" topic="Implicit derivative: a x+b y^2=cos y"}
#### Question 3

:::prompt
$a x+b y^{2}=\cos y$
:::

:::solution{label="Solution"}
Given, $a x+b y^{2}=\cos y$
Differentiating with respect to $x$, we get

$$
\begin{aligned}
& \frac{d}{d x}(a x)+\frac{d}{d x}\left(b y^{2}\right)=\frac{d}{d x}(\cos y) \\
& \Rightarrow a+b \frac{d}{d x}\left(y^{2}\right)=\frac{d}{d x}(\cos y) \\
& \frac{d}{d x}\left(y^{2}\right)=2 y \frac{d y}{d x} \text { and } \frac{d}{d x}(\cos y)=-\sin y \frac{d y}{d x}
\end{aligned}
$$

From (1) and (2), we obtain

$$
\begin{aligned}
& a+b \times 2 y \frac{d y}{d x}=-\sin y \frac{d y}{d x} \\
& \Rightarrow(2 b y+\sin y) \frac{d y}{d x}=-a \\
& \therefore \frac{d y}{d x}=\frac{-a}{2 b y+\sin y}
\end{aligned}
$$
:::

:::

:::question{number="4" kind="exercise" id="q_5.3.4" topic="Implicit derivative: x y+y^2=tan x+y"}
#### Question 4

:::prompt
$x y+y^{2}=\tan x+y$
:::

:::solution{label="Solution"}
Given, $x y+y^{2}=\tan x+y$
Differentiating with respect to $x$, we get

$$
\begin{aligned}
& \frac{d}{d x}\left(x y+y^{2}\right)=\frac{d}{d x}(\tan x+y) \\
& \Rightarrow \frac{d}{d x}(x y)+\frac{d}{d x}\left(y^{2}\right)=\frac{d}{d x}(\tan x)+\frac{d y}{d x} \\
& \Rightarrow\left[y \cdot \frac{d}{d x}(x)+x \cdot \frac{d y}{d x}\right]+2 y \frac{d y}{d x}=\sec ^{2} x+\frac{d y}{d x} \quad \text { [using product rule and chain rule] } \\
& \Rightarrow y \cdot 1+x \frac{d y}{d x}+2 y \frac{d y}{d x}=\sec ^{2} x+\frac{d y}{d x} \Rightarrow(x+2 y-1) \frac{d y}{d x}=\sec ^{2} x-y \\
& \therefore \frac{d y}{d x}=\frac{\sec ^{2} x-y}{(x+2 y-1)}
\end{aligned}
$$
:::

:::

:::question{number="5" kind="exercise" id="q_5.3.5" topic="Implicit derivative: x^2+x y+y^2=100"}
#### Question 5

:::prompt
$x^{2}+x y+y^{2}=100$
:::

:::solution{label="Solution"}
Given, $x^{2}+x y+y^{2}=100$
Differentiating with respect to $x$, we get

$$
\begin{aligned}
& \frac{d}{d x}\left(x^{2}+x y+y^{2}\right)=\frac{d}{d x}(100) \\
& \Rightarrow \frac{d}{d x}\left(x^{2}\right)+\frac{d}{d x}(x y)+\frac{d}{d x}\left(y^{2}\right)=0 \\
& \Rightarrow 2 x+\left[y \cdot \frac{d}{d x}(x)+x \cdot \frac{d y}{d x}\right]+2 y \frac{d y}{d x}=0 \\
& \Rightarrow 2 x+y \cdot 1+x \cdot \frac{d y}{d x}+2 y \frac{d y}{d x}=0 \\
& \Rightarrow 2 x+y+(x+2 y) \frac{d y}{d x}=0 \\
& \therefore \frac{d y}{d x}=-\frac{2 x+y}{x+2 y}
\end{aligned}
$$
:::

:::

:::question{number="6" kind="exercise" id="q_5.3.6" topic="Implicit derivative: x^3+x^2 y+x y^2+y^3=81"}
#### Question 6

:::prompt
$x^{3}+x^{2} y+x y^{2}+y^{3}=81$
:::

:::solution{label="Solution"}
Given, $x^{3}+x^{2} y+x y^{2}+y^{3}=81$
Differentiating with respect to $x$, we get

$$
\begin{aligned}
& \frac{d}{d x}\left(x^{3}+x^{2} y+x y^{2}+y^{3}\right)=\frac{d}{d x}(81) \\
& \Rightarrow \frac{d}{d x}\left(x^{3}\right)+\frac{d}{d x}\left(x^{2} y\right)+\frac{d}{d x}\left(x y^{2}\right)+\frac{d}{d x}\left(y^{3}\right)=0 \\
& \Rightarrow 3 x^{2}+\left[y \frac{d}{d x}\left(x^{2}\right)+x^{2} \frac{d y}{d x}\right]+\left[y^{2} \frac{d}{d x}(x)+x \frac{d}{d x}\left(y^{2}\right)\right]+3 y^{2} \frac{d y}{d x}=0 \\
& \Rightarrow 3 x^{2}+\left[y \cdot 2 x+x^{2} \frac{d y}{d x}\right]+\left[y^{2} \cdot 1+x \cdot 2 y \cdot \frac{d y}{d x}\right]+3 y^{2} \frac{d x}{d y}=0 \\
& \Rightarrow\left(x^{2}+2 x y+3 y^{2}\right) \frac{d y}{d x}+\left(3 x^{2}+2 x y+y^{2}\right)=0 \\
& \therefore \frac{d y}{d x}=\frac{-\left(3 x^{2}+2 x y+y^{2}\right)}{\left(x^{2}+2 x y+3 y^{2}\right)}
\end{aligned}
$$
:::

:::

:::question{number="7" kind="exercise" id="q_5.3.7" topic="Implicit derivative: sin ^2 y+cos x y="}
#### Question 7

:::prompt
$\sin ^{2} y+\cos x y=\kappa$
:::

:::solution{label="Solution"}
Given, $\sin ^{2} y+\cos x y=\pi$
Differentiating with respect to $x$, we get

$$
\begin{aligned}
& \frac{d}{d x}\left(\sin ^{2} y+\cos x y\right)=\frac{d}{d x}(\pi) \\
& \Rightarrow \frac{d}{d x}\left(\sin ^{2} y\right)+\frac{d}{d x}(\cos x y)=0
\end{aligned}
$$

Using chain rule, we obtain

$$
\begin{aligned}
& \frac{d}{d x}\left(\sin ^{2} y\right)=2 \sin y \frac{d}{d x}(\sin y)=2 \sin y \cos y \frac{d y}{d x} \\
& \frac{d}{d x}(\cos x y)=-\sin x y \frac{d}{d x}(x y)=-\sin x y\left[y \frac{d}{d x}(x)+x \frac{d y}{d x}\right] \\
& =-\sin x y\left[y \cdot 1+x \frac{d y}{d x}\right]=-y \sin x y-x \sin x y \frac{d y}{d x}
\end{aligned}
$$

From (1), (2) and (3), we obtain

$$
\begin{aligned}
& 2 \sin y \cos y \frac{d y}{d x}+\left(-y \sin x y-x \sin x y \frac{d y}{d x}\right)=0 \\
& \Rightarrow(2 \sin y \cos y-x \sin x y) \frac{d y}{d x}=y \sin x y \\
& \Rightarrow(\sin 2 y-x \sin x y) \frac{d x}{d y}=y \sin x y \\
& \therefore \frac{d x}{d y}=\frac{y \sin x y}{\sin 2 y-x \sin x y}
\end{aligned}
$$
:::

:::

:::question{number="8" kind="exercise" id="q_5.3.8" topic="Implicit derivative: sin ^2 x+cos ^2 y=1"}
#### Question 8

:::prompt
$\sin ^{2} x+\cos ^{2} y=1$
:::

:::solution{label="Solution"}
Given, $\sin ^{2} x+\cos ^{2} y=1$
Differentiating with respect to $x$, we get

$$
\begin{aligned}
& \frac{d}{d x}\left(\sin ^{2} x+\cos ^{2} y\right)=\frac{d}{d x}(1) \\
& \Rightarrow \frac{d}{d x}\left(\sin ^{2} x\right)+\frac{d}{d x}\left(\cos ^{2} y\right)=0 \\
& \Rightarrow 2 \sin x \cdot \frac{d}{d x}(\sin x)+2 \cos y \cdot \frac{d}{d x}(\cos y)=0 \\
& \Rightarrow 2 \sin x \cos x+2 \cos y(-\sin y) \cdot \frac{d y}{d x}=0 \\
& \Rightarrow \sin 2 x-\sin 2 y \frac{d y}{d x}=0 \\
& \therefore \frac{d y}{d x}=\frac{\sin 2 x}{\sin 2 y}
\end{aligned}
$$
:::

:::

:::question{number="9" kind="exercise" id="q_5.3.9" topic="Implicit derivative: y=sin ^-1(2 x1+x^2)"}
#### Question 9

:::prompt
$y=\sin ^{-1}\left(\frac{2 x}{1+x^{2}}\right)$
:::

:::solution{label="Solution"}
Given,

$$
\begin{aligned}
& y=\sin ^{-1}\left(\frac{2 x}{1+x^{2}}\right) \\
& \Rightarrow \sin y=\frac{2 x}{1+x^{2}}
\end{aligned}
$$

Differentiating with respect to $x$, we get

$$
\begin{aligned}
& \frac{d}{d x}(\sin y)=\frac{d}{d x}\left(\frac{2 x}{1+x^{2}}\right) \\
& \Rightarrow \cos y \frac{d y}{d x}=\frac{d}{d x}\left(\frac{2 x}{1+x^{2}}\right)
\end{aligned}
$$

The function $\frac{2 x}{1+x^{2}}$, is of the form of $\frac{u}{v}$
By quotient rule, we get

$$
\begin{aligned}
\frac{d}{d x}\left(\frac{2 x}{1+x^{2}}\right) & =\frac{\left(1+x^{2}\right) \frac{d}{d x}(2 x)-2 x \cdot \frac{d}{d x}\left(1+x^{2}\right)}{\left(1+x^{2}\right)^{2}} \\
& =\frac{\left(1+x^{2}\right) \cdot 2-2 x \cdot[0+2 x]}{\left(1+x^{2}\right)^{2}} \\
& =\frac{2+2 x^{2}-4 x^{2}}{\left(1+x^{2}\right)^{2}} \\
& =\frac{2\left(1-x^{2}\right)}{\left(1+x^{2}\right)^{2}}
\end{aligned}
$$

Also, $\sin y=\frac{2 x}{1+x^{2}}$

$$
\begin{aligned}
\cos y & =\sqrt{1-\sin ^{2} y}=\sqrt{1-\left(\frac{2 x}{1+x^{2}}\right)^{2}} \\
& =\sqrt{\frac{\left(1+x^{2}\right)^{2}-4 x^{2}}{\left(1+x^{2}\right)^{2}}} \\
& =\sqrt{\frac{\left(1-x^{2}\right)^{2}}{\left(1+x^{2}\right)^{2}}} \\
& =\frac{1-x^{2}}{1+x^{2}}
\end{aligned}
$$

From (1), (2) and (3), we get

$$
\begin{aligned}
& \frac{1-x^{2}}{1+x^{2}} \times \frac{d y}{d x}=\frac{2\left(1-x^{2}\right)}{\left(1+x^{2}\right)^{2}} \\
& \Rightarrow \frac{d y}{d x}=\frac{2}{1+x^{2}}
\end{aligned}
$$
:::

:::

:::question{number="10" kind="exercise" id="q_5.3.10" topic="Implicit derivative: y=tan ^-1(3 x-x^31-3 x^2),..."}
#### Question 10

:::prompt
$y=\tan ^{-1}\left(\frac{3 x-x^{3}}{1-3 x^{2}}\right),-\frac{1}{\sqrt{3}}<x<\frac{1}{\sqrt{3}}$
:::

:::solution{label="Solution"}
Given,

$$
y=\tan ^{-1}\left(\frac{3 x-x^{3}}{1-3 x^{2}}\right)
$$

$$
\Rightarrow \tan y=\left(\frac{3 x-x^{3}}{1-3 x^{2}}\right)
$$

Since, we know that

$$
\Rightarrow \tan y=\left(\frac{3 \tan \frac{y}{3}-\tan ^{3} \frac{y}{3}}{1-3 \tan ^{2} \frac{y}{3}}\right)
$$

Comparing (1) and (2) we get,

$$
x=\tan \frac{y}{3}
$$

Differentiating with respect to $x$, we get

$$
\begin{aligned}
& \frac{d}{d x}(x)=\frac{d}{d x}\left(\tan \frac{y}{3}\right) \\
& \Rightarrow 1=\sec ^{2} \frac{y}{3} \cdot \frac{d}{d x}\left(\frac{y}{3}\right) \\
& \Rightarrow 1=\sec ^{2} \frac{y}{3} \cdot \frac{1}{3} \cdot \frac{d y}{d x} \\
& \Rightarrow \frac{d y}{d x}=\frac{3}{\sec ^{2} \frac{y}{3}}=\frac{3}{1+\tan ^{2} \frac{y}{3}} \\
& \therefore \frac{d y}{d x}=\frac{3}{1+x^{2}}
\end{aligned}
$$
:::

:::

:::question{number="11" kind="exercise" id="q_5.3.11" topic="Implicit derivative: y=cos ^-1(1-x^21+x^2), 0<x..."}
#### Question 11

:::prompt
$y=\cos ^{-1}\left(\frac{1-x^{2}}{1+x^{2}}\right), 0<x<1$
:::

:::solution{label="Solution"}
Given,

$$
y=\cos ^{-1}\left(\frac{1-x^{2}}{1+x^{2}}\right)
$$

$$
\begin{aligned}
& \Rightarrow \cos y=\left(\frac{1-x^{2}}{1+x^{2}}\right) \\
& \Rightarrow \frac{1-\tan ^{2} \frac{y}{2}}{1+\tan ^{2} \frac{y}{2}}=\frac{1-x^{2}}{1+x^{2}}
\end{aligned}
$$

Comparing LHS and RHS, we get

$$
\tan \frac{y}{2}=x
$$

Differentiating with respect to $x$, we get

$$
\begin{aligned}
& \sec ^{2} \frac{y}{2} \cdot \frac{d}{d x}\left(\frac{y}{2}\right)=\frac{d}{d x}(x) \\
& \Rightarrow \sec ^{2} \frac{y}{2} \times \frac{1}{2} \frac{d y}{d x}=1 \\
& \Rightarrow \frac{d y}{d x}=\frac{2}{\sec ^{2} \frac{y}{2}} \\
& \Rightarrow \frac{d y}{d x}=\frac{2}{1+\tan ^{2} \frac{y}{2}} \\
& \therefore \frac{d y}{d x}=\frac{2}{1+x^{2}}
\end{aligned}
$$
:::

:::

:::question{number="12" kind="exercise" id="q_5.3.12" topic="Implicit derivative: y=sin ^-1(1-x^21+x^2), 0<x..."}
#### Question 12

:::prompt
$y=\sin ^{-1}\left(\frac{1-x^{2}}{1+x^{2}}\right), 0<x<1$
:::

:::solution{label="Solution"}
Given, $y=\sin ^{-1}\left(\frac{1-x^{2}}{1+x^{2}}\right)$

$$
\begin{aligned}
& y=\sin ^{-1}\left(\frac{1-x^{2}}{1+x^{2}}\right) \\
& \Rightarrow \sin y=\frac{1-x^{2}}{1+x^{2}}
\end{aligned}
$$

Differentiating with respect to $x$, we get

$$
\frac{d}{d x}(\sin y)=\frac{d}{d x}\left(\frac{1-x^{2}}{1+x^{2}}\right)
$$

Using chain rule, we get

$$
\begin{aligned}
& \frac{d}{d x}(\sin y)=\cos y \cdot \frac{d y}{d x} \\
& \cos y=\sqrt{1-\sin ^{2} y}=\sqrt{1-\left(\frac{1-x^{2}}{1+x^{2}}\right)^{2}} \\
& \quad=\sqrt{\frac{\left(1+x^{2}\right)^{2}-\left(1-x^{2}\right)^{2}}{\left(1+x^{2}\right)^{2}}}=\sqrt{\frac{4 x^{2}}{\left(1+x^{2}\right)^{2}}}=\frac{2 x}{1+x^{2}}
\end{aligned}
$$

Therefore,

$$
\begin{aligned}
\frac{d}{d x}(\sin y)= & \frac{2 x}{1+x^{2}} \frac{d y}{d x} \\
\frac{d}{d x}\left(\frac{1-x^{2}}{1+x^{2}}\right) & =\frac{\left(1+x^{2}\right) \cdot \frac{d}{d x}\left(1-x^{2}\right)-\left(1-x^{2}\right) \cdot \frac{d}{d x}\left(1+x^{2}\right)}{\left(1+x^{2}\right)^{2}} \\
& =\frac{\left(1+x^{2}\right)(-2 x)-\left(1-x^{2}\right)(2 x)}{\left(1+x^{2}\right)^{2}} \\
& =\frac{-2 x-2 x^{3}-2 x+2 x^{3}}{\left(1+x^{2}\right)^{2}} \\
& =\frac{-4 x}{\left(1+x^{2}\right)^{2}}
\end{aligned}
$$

From equation (1), (2) and (3), we get

$$
\begin{aligned}
& \frac{2 x}{1+x^{2}} \frac{d y}{d x}=\frac{-4 x}{\left(1+x^{2}\right)^{2}} \\
& \Rightarrow \frac{d y}{d x}=\frac{-2}{1+x^{2}}
\end{aligned}
$$
:::

:::

:::question{number="13" kind="exercise" id="q_5.3.13" topic="Implicit derivative: y=cos ^-1(2 x1+x^2),-1<x<1"}
#### Question 13

:::prompt
$y=\cos ^{-1}\left(\frac{2 x}{1+x^{2}}\right),-1<x<1$
:::

:::solution{label="Solution"}
Given, $y=\cos ^{-1}\left(\frac{2 x}{1+x^{2}}\right)$

$$
\begin{aligned}
& y=\cos ^{-1}\left(\frac{2 x}{1+x^{2}}\right) \\
& \cos y=\left(\frac{2 x}{1+x^{2}}\right)
\end{aligned}
$$

Differentiating with respect to $x$, we get

$$
\begin{aligned}
& \frac{d}{d x}(\cos y)=\frac{d}{d x}\left(\frac{2 x}{1+x^{2}}\right) \\
& \Rightarrow-\sin y \cdot \frac{d y}{d x}=\frac{\left(1+x^{2}\right) \cdot \frac{d}{d x}(2 x)-2 x \cdot \frac{d}{d x}\left(1+x^{2}\right)}{\left(1+x^{2}\right)^{2}} \\
& \Rightarrow-\sqrt{1-\cos ^{2} y} \frac{d y}{d x}=\frac{\left(1+x^{2}\right) \times 2-2 x \times 2 x}{\left(1+x^{2}\right)^{2}} \\
& \Rightarrow\left[\sqrt{1-\left(\frac{2 x}{1+x^{2}}\right)^{2}}\right] \frac{d y}{d x}=-\left[\frac{2\left(1-x^{2}\right)}{\left(1+x^{2}\right)^{2}}\right] \\
& \Rightarrow \sqrt{\frac{\left(1+x^{2}\right)^{2}-4 x^{2}}{\left(1+x^{2}\right)^{2}} \cdot \frac{d y}{d x}=\frac{-2\left(1-x^{2}\right)}{\left(1+x^{2}\right)}} \\
& \Rightarrow \sqrt{\frac{\left(1-x^{2}\right)^{2}}{\left(1+x^{2}\right)^{2}}} \frac{d y}{d x}=\frac{-2\left(1-x^{2}\right)}{\left(1-x^{2}\right)^{2}} \\
& \Rightarrow \frac{1-x^{2}}{1+x^{2}} \cdot \frac{d y}{d x}=\frac{-2\left(1-x^{2}\right)}{\left(1+x^{2}\right)^{2}} \\
& \Rightarrow \frac{d y}{d x}=\frac{-2}{1+x^{2}}
\end{aligned}
$$
:::

:::

:::question{number="14" kind="exercise" id="q_5.3.14" topic="Implicit derivative: y=sin ^-1(2 x sqrt 1-x^2),..."}
#### Question 14

:::prompt
$y=\sin ^{-1}\left(2 x \sqrt{1-x^{2}}\right),-\frac{1}{\sqrt{2}}<x<\frac{1}{\sqrt{2}}$
:::

:::solution{label="Solution"}
Given, $y=\sin ^{-1}\left(2 x \sqrt{1-x^{2}}\right)$

$$
\begin{aligned}
& y=\sin ^{-1}\left(2 x \sqrt{1-x^{2}}\right) \\
& \Rightarrow \sin y=\left(2 x \sqrt{1-x^{2}}\right)
\end{aligned}
$$

Differentiating with respect to $x$, we get
$\cos y . \frac{d y}{d x}=2\left[x \frac{d}{d x}\left(\sqrt{1-x^{2}}\right)+\sqrt{1-x^{2}} \frac{d x}{d x}\right]$

$$
\begin{aligned}
& \Rightarrow \sqrt{1-\sin ^{2} y} \frac{d y}{d x}=2\left[\frac{x}{2} \cdot \frac{-2 x}{\sqrt{1-x^{2}}}+\sqrt{1-x^{2}}\right] \\
& \Rightarrow \sqrt{1-\left(2 x \sqrt{1-x^{2}}\right)^{2}} \cdot \frac{d y}{d x}=2\left[\frac{-x^{2}+1-x^{2}}{\sqrt{1-x^{2}}}\right] \\
& \Rightarrow \sqrt{1-4 x^{2}\left(1-x^{2}\right)} \frac{d y}{d x}=2\left[\frac{1-2 x^{2}}{\sqrt{1-x^{2}}}\right] \\
& \Rightarrow \sqrt{\left(1-2 x^{2}\right)^{2}} \frac{d y}{d x}=2\left[\frac{1-2 x^{2}}{\sqrt{1-x^{2}}}\right] \\
& \Rightarrow\left(1-2 x^{2}\right) \frac{d y}{d x}=2\left[\frac{1-2 x^{2}}{\sqrt{1-x^{2}}}\right] \\
& \Rightarrow \frac{d y}{d x}=\frac{2}{\sqrt{1-x^{2}}}
\end{aligned}
$$
:::

:::

:::question{number="15" kind="exercise" id="q_5.3.15" topic="Implicit derivative: y=sec ^-1(12 x^2-1), 0<x<1..."}
#### Question 15

:::prompt
$y=\sec ^{-1}\left(\frac{1}{2 x^{2}-1}\right), 0<x<\frac{1}{\sqrt{2}}$
:::

:::solution{label="Solution"}
Given, $y=\sec ^{-1}\left(\frac{1}{2 x^{2}-1}\right)$

$$
\begin{aligned}
& \Rightarrow y=\sec ^{-1}\left(\frac{1}{2 x^{2}-1}\right) \\
& \Rightarrow \sec y=\left(\frac{1}{2 x^{2}-1}\right) \\
& \Rightarrow \cos y=2 x^{2}-1 \\
& \Rightarrow 2 x^{2}=1+\cos y \\
& \Rightarrow 2 x^{2}=2 \cos ^{2} \frac{y}{2} \\
& \Rightarrow x=\cos \frac{y}{2}
\end{aligned}
$$

Differentiating with respect to $x$, we get

$$
\begin{aligned}
& \frac{d}{d x}(x)=\frac{d}{d x}\left(\cos \frac{y}{2}\right) \\
& \Rightarrow 1=\sin \frac{y}{2} \cdot \frac{d}{d x}\left(\frac{y}{2}\right) \\
& \Rightarrow \frac{-1}{\sin \frac{y}{2}}=\frac{1}{2} \frac{d y}{d x} \\
& \Rightarrow \frac{d y}{d x}=\frac{-2}{\sin \frac{y}{2}} \\
& \Rightarrow \frac{d y}{d x}=\frac{-2}{\sqrt{1-\cos ^{2} \frac{y}{2}}} \\
& \Rightarrow \frac{d y}{d x}=\frac{-2}{\sqrt{1-x^{2}}}
\end{aligned}
$$
:::

:::

:::question{number="1" kind="exercise" id="q_5.4.1" topic="Derivative of exponential/log function: e^xsin x"}
#### Question 1

:::prompt
$\frac{e^{x}}{\sin x}$
:::

:::solution{label="Solution"}
Let $y=\frac{e^{x}}{\sin x}$
By using the quotient rule, we get

$$
\begin{aligned}
\frac{d y}{d x} & =\frac{\sin x \frac{d}{d x}\left(e^{x}\right)-e^{x} \frac{d}{d x}(\sin x)}{\sin ^{2} x} \\
& =\frac{\sin x \cdot\left(e^{x}\right)-e^{x} \cdot(\cos x)}{\sin ^{2} x} \\
& =\frac{e^{x}(\sin x-\cos x)}{\sin ^{2} x}
\end{aligned}
$$
:::

:::

:::question{number="2" kind="exercise" id="q_5.4.2" topic="Derivative of exponential/log function: e^sin ^-1 x"}
#### Question 2

:::prompt
$e^{\sin ^{-1} x}$
:::

:::solution{label="Solution"}
Let $y=e^{\sin ^{-1} x}$
By using the quotient rule, we get

$$
\begin{aligned}
\frac{d y}{d x} & =\frac{d}{d x}\left(e^{\sin ^{-1} x}\right) \\
& =e^{\sin ^{-1} x} \cdot \frac{d}{d x}\left(\sin ^{-1} x\right) \\
& =e^{\sin ^{-1} x} \cdot \frac{1}{\sqrt{1-x^{2}}} \\
& =\frac{e^{\sin ^{-1} x}}{\sqrt{1-x^{2}}} \\
& =\frac{e^{\sin ^{-1} x}}{\sqrt{1-x^{2}}}, x \in(-1,1)
\end{aligned}
$$
:::

:::

:::question{number="3" kind="exercise" id="q_5.4.3" topic="Derivative of exponential/log function: e^x^3"}
#### Question 3

:::prompt
$e^{x^{3}}$
:::

:::solution{label="Solution"}
Let $y=e^{x^{3}}$
By using the quotient rule, we get

$$
\begin{aligned}
\frac{d y}{d x} & =\frac{d}{d x}\left(e^{x^{3}}\right) \\
& =e^{x^{3}} \cdot \frac{d}{d x}\left(x^{3}\right) \\
& =e^{x^{3}} \cdot 3 x^{2} \\
& =3 x^{2} e^{x^{3}}
\end{aligned}
$$
:::

:::

:::question{number="4" kind="exercise" id="q_5.4.4" topic="Derivative of exponential/log function: sin (tan ^-1 e^-x)"}
#### Question 4

:::prompt
$\sin \left(\tan ^{-1} e^{-x}\right)$
:::

:::solution{label="Solution"}
Let $y=\sin \left(\tan ^{-1} e^{-x}\right)$
By using the chain rule, we get

$$
\begin{aligned}
\frac{d y}{d x} & =\frac{d}{d x}\left[\sin \left(\tan ^{-1} e^{-x}\right)\right] \\
& =\cos \left(\tan ^{-1} e^{-x}\right) \cdot \frac{d}{d x}\left(\tan ^{-1} e^{-x}\right) \\
& =\cos \left(\tan ^{-1} e^{-x}\right) \cdot \frac{1}{1+\left(e^{-x}\right)^{2}} \cdot \frac{d}{d x}\left(e^{-x}\right) \\
& =\frac{\cos \left(\tan ^{-1} e^{-x}\right)}{1+e^{-2 x}} \cdot e^{-x} \cdot \frac{d}{d x}(-x) \\
& =\frac{e^{-x} \cos \left(\tan ^{-1} e^{-x}\right)}{1+e^{-2 x}} \times(-1) \\
& =\frac{-e^{-x} \cos \left(\tan ^{-1} e^{-x}\right)}{1+e^{-2 x}}
\end{aligned}
$$
:::

:::

:::question{number="5" kind="exercise" id="q_5.4.5" topic="Derivative of exponential/log function: log (cos e^x)"}
#### Question 5

:::prompt
$\log \left(\cos e^{x}\right)$
:::

:::solution{label="Solution"}
Let $y=\log \left(\cos e^{x}\right)$
By using the chain rule, we get

$$
\begin{aligned}
\frac{d y}{d x} & =\frac{d}{d x}\left[\log \left(\cos e^{x}\right)\right] \\
& =\frac{1}{\cos e^{x}} \cdot \frac{d}{d x}\left(\cos e^{x}\right) \\
& =\frac{1}{\cos e^{x}} \cdot\left(-\sin e^{x}\right) \cdot \frac{d}{d x}\left(e^{x}\right) \\
& =\frac{-\sin e^{x}}{\cos e^{x}} \cdot e^{x} \\
& =-e^{x} \tan e^{x}, e^{x} \neq(2 n+1) \frac{\pi}{2}, n \in \mathbf{N}
\end{aligned}
$$
:::

:::

:::question{number="6" kind="exercise" id="q_5.4.6" topic="Derivative of exponential/log function: e^x+e^x^2++e^x^5"}
#### Question 6

:::prompt
$e^{x}+e^{x^{2}}+\ldots+e^{x^{5}}$
:::

:::solution{label="Solution"}
$$
\frac{d}{d x}\left(e^{x}+e^{x^{2}}+\ldots+e^{x^{5}}\right)
$$

Differentiating wrt $x$, we get

$$
\begin{aligned}
\frac{d}{d x}\left(e^{x}+e^{x^{2}}+\ldots+e^{x^{5}}\right) & =\frac{d}{d x}\left(e^{x}\right)+\frac{d}{d x}\left(e^{x^{2}}\right)+\frac{d}{d x}\left(e^{x^{3}}\right)+\frac{d}{d x}\left(e^{x^{4}}\right)+\frac{d}{d x}\left(e^{x^{5}}\right) \\
& =e^{x}+\left[e^{x^{2}} \times \frac{d}{d x}\left(x^{2}\right)\right]+\left[e^{x^{3}} \times \frac{d}{d x}\left(x^{3}\right)\right]+\left[e^{x^{4}} \times \frac{d}{d x}\left(x^{4}\right)\right]+\left[e^{x^{5}} \times \frac{d}{d x}\left(x^{5}\right)\right] \\
& =e^{x}+\left(e^{x^{2}} \times 2 x\right)+\left(e^{x^{3}} \times 3 x^{2}\right)+\left(e^{x^{4}} \times 4 x^{3}\right)+\left(e^{x^{5}} \times 5 x^{4}\right) \\
& =e^{x}+2 x e^{x^{2}}+3 x^{2} e^{x^{3}}+4 x^{3} e^{x^{4}}+5 x^{4} e^{x^{5}}
\end{aligned}
$$
:::

:::

:::question{number="7" kind="exercise" id="q_5.4.7" topic="Derivative of exponential/log function: sqrt e^sqrt x, x>0"}
#### Question 7

:::prompt
$\sqrt{e^{\sqrt{x}}}, x>0$
:::

:::solution{label="Solution"}
Let $y=\sqrt{e^{\sqrt{x}}}$
Then, $y^{2}=e^{\sqrt{x}}$
Differentiating wrt $x$, we get

$$
y^{2}=e^{\sqrt{x}}
$$

$$
\begin{aligned}
& \frac{d}{d x}\left(y^{2}\right)=\frac{d}{d x}\left(e^{\sqrt{x}}\right) \\
& \Rightarrow 2 y \frac{d y}{d x}=e^{\sqrt{x}} \frac{d}{d x}(\sqrt{x}) \\
& \Rightarrow 2 y \frac{d y}{d x}=e^{\sqrt{x}} \frac{1}{2} \cdot \frac{1}{\sqrt{x}} \\
& \Rightarrow \frac{d y}{d x}=\frac{e^{\sqrt{x}}}{4 y \sqrt{x}} \\
& \Rightarrow \frac{d y}{d x}=\frac{e^{\sqrt{x}}}{4 \sqrt{e^{\sqrt{x}}} \sqrt{x}} \\
& \Rightarrow \frac{d y}{d x}=\frac{e^{\sqrt{x}}}{4 \sqrt{x e^{\sqrt{x}}}}, x>0
\end{aligned}
$$
:::

:::

:::question{number="8" kind="exercise" id="q_5.4.8" topic="Derivative of exponential/log function: log (log x), x>1"}
#### Question 8

:::prompt
$\log (\log x), x>1$
:::

:::solution{label="Solution"}
Let $y=\log (\log x)$
By using the chain rule, we get

$$
\begin{aligned}
\frac{d y}{d x} & =\frac{d}{d x}[\log (\log x)] \\
& =\frac{1}{\log x} \cdot \frac{d}{d x}(\log x) \\
& =\frac{1}{\log x} \cdot \frac{1}{x} \\
& =\frac{1}{x \log x}, x>1
\end{aligned}
$$
:::

:::

:::question{number="9" kind="exercise" id="q_5.4.9" topic="Derivative of exponential/log function: cos x/log x, x>0"}
#### Question 9

:::prompt
$\frac{\cos x}{\log x}, x>0$
:::

:::solution{label="Solution"}
Let $y=\frac{\cos x}{\log x}$
By using the quotient rule, we get

$$
\begin{aligned}
\frac{d y}{d x} & =\frac{\frac{d}{d x}(\cos x) \cdot \log x-\cos x \cdot \frac{d}{d x}(\log x)}{(\log x)^{2}} \\
& =\frac{-\sin x \log x-\cos x \cdot \frac{1}{x}}{(\log x)^{2}} \\
& =-\left[\frac{x \log x \cdot \sin x+\cos x}{x(\log x)^{2}}\right], x>0
\end{aligned}
$$
:::

:::

:::question{number="10" kind="exercise" id="q_5.4.10" topic="Derivative of exponential/log function: cos (log x+e^x), x>0"}
#### Question 10

:::prompt
$\cos \left(\log x+e^{x}\right), x>0$
:::

:::solution{label="Solution"}
Let $y=\cos \left(\log x+e^{x}\right)$
By using the chain rule, we get

$$
\begin{aligned}
\frac{d y}{d x} & =-\sin \left[\log x+e^{x}\right] \cdot \frac{d}{d x}\left(\log x+e^{x}\right) \\
& =-\sin \left(\log x+e^{x}\right) \cdot\left[\frac{d}{d x}(\log x)+\frac{d}{d x}\left(e^{x}\right)\right] \\
& =-\sin \left(\log x+e^{x}\right) \cdot\left(\frac{1}{x}+e^{x}\right) \\
& =-\left(\frac{1}{x}+e^{x}\right) \sin \left(\log x+e^{x}\right), x>0
\end{aligned}
$$
:::

:::

:::question{number="1" kind="exercise" id="q_5.5.1" topic="Logarithmic differentiation: cos x * cos 2 x * cos 3 x"}
#### Question 1

:::prompt
$\cos x \cdot \cos 2 x \cdot \cos 3 x$
:::

:::solution{label="Solution"}
Let $y=\cos x . \cos 2 x . \cos 3 x$
Taking logarithm on both the sides, we obtain

$$
\begin{aligned}
& \log y=\log (\cos x \cdot \cos 2 x \cdot \cos 3 x) \\
& \Rightarrow \log y=\log (\cos x)+\log (\cos 2 x)+\log (\cos 3 x)
\end{aligned}
$$

Differentiating both sides with respect to $x$, we obtain

$$
\begin{aligned}
& \frac{1}{y} \frac{d y}{d x}=\frac{1}{\cos x} \cdot \frac{d}{d x}(\cos x)+\frac{1}{\cos 2 x} \cdot \frac{d}{d x}(\cos 2 x)+\frac{1}{\cos 3 x} \cdot \frac{d}{d x}(\cos 3 x) \\
& \Rightarrow \frac{d y}{d x}=y\left[-\frac{\sin x}{\cos x}-\frac{\sin 2 x}{\cos 2 x} \cdot \frac{d}{d x}(2 x)-\frac{\sin 3 x}{\cos 3 x} \cdot \frac{d}{d x}(3 x)\right] \\
& \therefore \frac{d y}{d x}=-\cos x \cdot \cos 2 x \cdot \cos 3 x[\tan x+2 \tan 2 x+3 \tan 3 x]
\end{aligned}
$$
:::

:::

:::question{number="2" kind="exercise" id="q_5.5.2" topic="Logarithmic differentiation: sqrt (x-1)(x-2)/(x-3)(x-4)..."}
#### Question 2

:::prompt
$\sqrt{\frac{(x-1)(x-2)}{(x-3)(x-4)(x-5)}}$
:::

:::solution{label="Solution"}
Let $y=\sqrt{\frac{(x-1)(x-2)}{(x-3)(x-4)(x-5)}}$
Taking logarithm on both the sides, we obtain

$$
\begin{aligned}
& \log y=\log \sqrt{\frac{(x-1)(x-2)}{(x-3)(x-4)(x-5)}} \\
& \Rightarrow \log y=\frac{1}{2} \log \left[\frac{(x-1)(x-2)}{(x-3)(x-4)(x-5)}\right] \\
& \Rightarrow \log y=\frac{1}{2}[\log \{(x-1)(x-2)\}-\log \{(x-3)(x-4)(x-5)\}] \\
& \Rightarrow \log y=\frac{1}{2}[\log (x-1)+\log (x-2)-\log (x-3)-\log (x-4)-\log (x-5)]
\end{aligned}
$$

Differentiating both sides with respect to $x$, we obtain

$$
\begin{aligned}
& \frac{1}{y} \frac{d y}{d x}=\frac{1}{2}\left[\begin{array}{l}
\frac{1}{x-1} \cdot \frac{d}{d x}(x-1)+\frac{1}{x-2} \cdot \frac{d}{d x}(x-2)-\frac{1}{x-3} \cdot \frac{d}{d x}(x-3) \\
-\frac{1}{x-4} \cdot \frac{d}{d x}(x-4)-\frac{1}{x-5} \cdot \frac{d}{d x}(x-5)
\end{array}\right] \\
& \Rightarrow \frac{d y}{d x}=\frac{y}{2}\left[\frac{1}{x-1}+\frac{1}{x-2}-\frac{1}{x-3}-\frac{1}{x-4}-\frac{1}{x-5}\right] \\
& \therefore \frac{d y}{d x}=\frac{1}{2} \sqrt{\frac{(x-1)(x-2)}{(x-3)(x-4)(x-5)}\left[\frac{1}{x-1}+\frac{1}{x-2}-\frac{1}{x-3}-\frac{1}{x-4}-\frac{1}{x-5}\right]}
\end{aligned}
$$
:::

:::

:::question{number="3" kind="exercise" id="q_5.5.3" topic="Logarithmic differentiation: (log x)^cos x"}
#### Question 3

:::prompt
$(\log x)^{\cos x}$
:::

:::solution{label="Solution"}
Let $y=(\log x)^{\cos x}$
Taking logarithm on both the sides, we obtain

$$
\log y=\cos x \cdot \log (\log x)
$$

Differentiating both sides with respect to $x$, we obtain

$$
\begin{aligned}
& \frac{1}{y} \cdot \frac{d y}{d x}=\frac{d}{d x}(\cos x) \cdot \log (\log x)+\cos x \cdot \frac{d}{d x}[\log (\log x)] \\
& \Rightarrow \frac{1}{y} \cdot \frac{d y}{d x}=-\sin x \log (\log x)+\cos x \cdot \frac{1}{\log x} \cdot \frac{d}{d x}(\log x) \\
& \Rightarrow \frac{d}{d x}=y\left[-\sin x \log (\log x)+\frac{\cos x}{\log x} \cdot \frac{1}{x}\right] \\
& \therefore \frac{d y}{d x}=(\log x)^{\cos x}\left[\frac{\cos x}{x \log x}-\sin x \log (\log x)\right]
\end{aligned}
$$
:::

:::

:::question{number="4" kind="exercise" id="q_5.5.4" topic="Logarithmic differentiation: x^x-2^sin x"}
#### Question 4

:::prompt
$x^{x}-2^{\sin x}$
:::

:::solution{label="Solution"}
Let $y=x^{x}-2^{\sin x}$
Also, let $x^{x}=u$ and $2^{\sin x}=v$

$$
\begin{aligned}
& \therefore y=u-v \\
& \Rightarrow \frac{d y}{d x}=\frac{d u}{d x}-\frac{d v}{d x} \\
& u=x^{x}
\end{aligned}
$$

Taking logarithm on both the sides, we obtain

$$
\log u=x \log x
$$

Differentiating both sides with respect to $x$, we obtain

$$
\begin{aligned}
& \frac{1}{u} \cdot \frac{d u}{d x}=\left[\frac{d}{d x}(x) \times \log x+x \times \frac{d}{d x}(\log x)\right] \\
& \Rightarrow \frac{d u}{d x}=u\left[1 \times \log x+x \times \frac{1}{x}\right] \\
& \Rightarrow \frac{d u}{d x}=x^{x}(\log x+1) \\
& \Rightarrow \frac{d u}{d x}=x^{x}(1+\log x) \\
& v=2^{\sin x}
\end{aligned}
$$

Taking logarithm on both the sides, we obtain

$$
\log v=\sin x \cdot \log 2
$$

Differentiating both sides with respect to $x$, we obtain

$$
\begin{aligned}
& \frac{1}{v} \cdot \frac{d v}{d x}=\log 2 \cdot \frac{d}{d x}(\sin x) \\
& \Rightarrow \frac{d v}{d x}=v \log 2 \cos x \\
& \Rightarrow \frac{d v}{d x}=2^{\sin x} \cos x \log 2 \\
& \therefore \frac{d y}{d x}=x^{x}(1+\log x)-2^{\sin x} \cos x \log 2
\end{aligned}
$$
:::

:::

:::question{number="5" kind="exercise" id="q_5.5.5" topic="Logarithmic differentiation: (x+3)^2 * (x+4)^3 * (x+5)^..."}
#### Question 5

:::prompt
$(x+3)^{2} \cdot(x+4)^{3} \cdot(x+5)^{4}$
:::

:::solution{label="Solution"}
Let $y=(x+3)^{2} .(x+4)^{3} .(x+5)^{4}$
Taking logarithm on both the sides, we obtain

$$
\begin{aligned}
& \log y=\log (x+3)^{2}+\log (x+4)^{3}+\log (x+5)^{4} \\
& \Rightarrow \log y=2 \log (x+3)+3 \log (x+4)+4 \log (x+5)
\end{aligned}
$$

Differentiating both sides with respect to $x$, we obtain

$$
\begin{aligned}
& \frac{1}{y} \cdot \frac{d y}{d x}=2 \cdot \frac{1}{x+3} \cdot \frac{d}{d x}(x+3)+3 \cdot \frac{1}{x+4} \cdot \frac{d}{d x}(x+4)+4 \cdot \frac{1}{x+5} \cdot \frac{d}{d x}(x+5) \\
& \Rightarrow \frac{d y}{d x}=y\left[\frac{2}{x+3}+\frac{3}{x+4}+\frac{4}{x+5}\right] \\
& \Rightarrow \frac{d y}{d x}=(x+3)^{2}(x+4)^{3}(x+5)^{4} \cdot\left[\frac{2}{x+3}+\frac{3}{x+4}+\frac{4}{x+5}\right] \\
& \Rightarrow \frac{d y}{d x}=(x+3)^{2}(x+4)^{3}(x+5)^{4} \cdot\left[\begin{array}{l}
\frac{2(x+4)(x+5)+3(x+3)(x+5)}{+4(x+3)(x+4)} \\
(x+3)(x+4)(x+5)
\end{array}\right] \\
& \Rightarrow \frac{d y}{d x}=(x+3)(x+4)^{2}(x+5)^{3} \cdot\left[\begin{array}{l}
2\left(x^{2}+9 x+20\right)+3\left(x^{2}+8 x+15\right) \\
+4\left(x^{2}+7 x+12\right)
\end{array}\right] \\
& \therefore \frac{d y}{d x}=(x+3)(x+4)^{2}(x+5)^{3}\left(9 x^{2}+70 x+133\right)
\end{aligned}
$$
:::

:::

:::question{number="6" kind="exercise" id="q_5.5.6" topic="Logarithmic differentiation: (x+1/x)^x+x^(1+1/x)"}
#### Question 6

:::prompt
$\left(x+\frac{1}{x}\right)^{x}+x^{\left(1+\frac{1}{x}\right)}$
:::

:::solution{label="Solution"}
Let $y=\left(x+\frac{1}{x}\right)^{x}+x^{\left(1+\frac{1}{x}\right)}$
Also, let $u=\left(x+\frac{1}{x}\right)^{x}$ and $v=x^{\left(1+\frac{1}{x}\right)}$

$$
\begin{aligned}
& \therefore y=u+v \\
& \Rightarrow \frac{d y}{d x}=\frac{d u}{d x}+\frac{d v}{d x}
\end{aligned}
$$

Then, $u=\left(x+\frac{1}{x}\right)^{x}$
Taking logarithm on both the sides, we obtain

$$
\begin{aligned}
& \Rightarrow \log u=\log \left(x+\frac{1}{x}\right)^{x} \\
& \Rightarrow \log u=x \log \left(x+\frac{1}{x}\right)
\end{aligned}
$$

Differentiating both sides with respect to $x$, we obtain

$$
\begin{aligned}
& \frac{1}{u} \cdot \frac{d u}{d x}=\frac{d}{d x}(x) \times \log \left(x+\frac{1}{x}\right)+x \times \frac{d}{d x}\left[\log \left(x+\frac{1}{x}\right)\right] \\
& \Rightarrow \frac{1}{u} \cdot \frac{d u}{d x}=1 \times \log \left(x+\frac{1}{x}\right)+x \times \frac{1}{\left(x+\frac{1}{x}\right)} \cdot \frac{d}{d x}\left(x+\frac{1}{x}\right) \\
& \Rightarrow \frac{d u}{d x}=u\left[\log \left(x+\frac{1}{x}\right)+\frac{x}{\left(x+\frac{1}{x}\right)} \times\left(1-\frac{1}{x^{2}}\right)\right] \\
& \Rightarrow \frac{d u}{d x}=\left(x+\frac{1}{x}\right)^{x}\left[\log \left(x+\frac{1}{x}\right)+\frac{\left(x-\frac{1}{x}\right)}{\left(x+\frac{1}{x}\right)}\right] \\
& \Rightarrow \frac{d u}{d x}=\left(x+\frac{1}{x}\right)^{x}\left[\log \left(x+\frac{1}{x}\right)+\frac{x^{2}-1}{x^{2}+1}\right] \\
& \Rightarrow \frac{d u}{d x}=\left(x+\frac{1}{x}\right)^{x}\left[\frac{x^{2}-1}{x^{2}+1}+\log \left(x+\frac{1}{x}\right)\right]
\end{aligned} .
$$

Now, $v=x^{\left(1+\frac{1}{x}\right)}$
Taking logarithm on both the sides, we obtain

$$
\begin{aligned}
& \Rightarrow \log v=\log \left[x^{\left(1+\frac{1}{x}\right)}\right] \\
& \Rightarrow \log v=\left(1+\frac{1}{x}\right) \log x
\end{aligned}
$$

Differentiating both sides with respect to $x$, we obtain

$$
\begin{aligned}
& \frac{1}{v} \cdot \frac{d v}{d x}=\left[\frac{d}{d x}\left(1+\frac{1}{x}\right)\right] \times \log x+\left(1+\frac{1}{x}\right) \cdot \frac{d}{d x} \log x \\
& \Rightarrow \frac{1}{v} \cdot \frac{d v}{d x}=\left(-\frac{1}{x^{2}}\right) \log x+\left(1+\frac{1}{x}\right) \cdot \frac{1}{x} \\
& \Rightarrow \frac{1}{v} \cdot \frac{d v}{d x}=-\frac{\log x}{x^{2}}+\frac{1}{x}+\frac{1}{x^{2}} \\
& \Rightarrow \frac{d v}{d x}=v\left[\frac{-\log x+x+1}{x^{2}}\right] \\
& \Rightarrow \frac{d v}{d x}=x^{\left(1+\frac{1}{x}\right)}\left[\frac{-\log x+x+1}{x^{2}}\right]
\end{aligned}
$$

Therefore, from (1), (2) and (3);

$$
\frac{d y}{d x}=\left(x+\frac{1}{x}\right)^{x}\left[\frac{x^{2}-1}{x^{2}+1}+\log \left(x+\frac{1}{x}\right)\right]+x^{\left(1+\frac{1}{x}\right)}\left[\frac{x+1-\log x}{x^{2}}\right]
$$
:::

:::

:::question{number="7" kind="exercise" id="q_5.5.7" topic="Logarithmic differentiation: (log x)^x+x^log x"}
#### Question 7

:::prompt
$(\log x)^{x}+x^{\log x}$
:::

:::solution{label="Solution"}
Let $y=(\log x)^{x}+x^{\log x}$
Also, let $u=(\log x)^{x}$ and $v=x^{\log x}$

$$
\begin{aligned}
& \therefore y=u+v \\
& \Rightarrow \frac{d y}{d x}=\frac{d u}{d x}+\frac{d v}{d x}
\end{aligned}
$$

Then, $u=(\log x)^{x}$
Taking logarithm on both the sides, we obtain

$$
\begin{aligned}
& \Rightarrow \log u=\log \left[(\log x)^{x}\right] \\
& \Rightarrow \log u=x \log (\log x)
\end{aligned}
$$

Differentiating both sides with respect to $x$, we obtain

$$
\begin{aligned}
& \frac{1}{u} \cdot \frac{d u}{d x}=\frac{d}{d x}(x) \times \log (\log x)+x \cdot \frac{d}{d x}[\log (\log x)] \\
& \Rightarrow \frac{d u}{d x}=u\left[1 \times \log (\log x)+x \cdot \frac{1}{(\log x)} \cdot \frac{d}{d x}(\log x)\right] \\
& \Rightarrow \frac{d u}{d x}=(\log x)^{x}\left[\log (\log x)+\frac{x}{(\log x)} \cdot \frac{1}{x}\right] \\
& \Rightarrow \frac{d u}{d x}=(\log x)^{x}\left[\log (\log x)+\frac{1}{(\log x)}\right] \\
& \Rightarrow \frac{d u}{d x}=(\log x)^{x}\left[\frac{\log (\log x) \cdot \log x+1}{\log x}\right] \\
& \Rightarrow \frac{d u}{d x}=(\log x)^{x-1}[1+\log x \cdot \log (\log x)] \\
& v=x^{\log x}
\end{aligned}
$$

Taking logarithm on both the sides, we obtain

$$
\begin{aligned}
& \Rightarrow \log v=\log \left(x^{\log x}\right) \\
& \Rightarrow \log v=\log x \log x=(\log x)^{2}
\end{aligned}
$$

Differentiating both sides with respect to $x$, we obtain

$$
\begin{aligned}
& \frac{1}{v} \cdot \frac{d v}{d x}=\frac{d}{d x}\left[(\log x)^{2}\right] \\
& \Rightarrow \frac{1}{v} \cdot \frac{d v}{d x}=2(\log x) \cdot \frac{d}{d x}(\log x) \\
& \Rightarrow \frac{d v}{d x}=2 v(\log x) \cdot \frac{1}{x} \\
& \Rightarrow \frac{d v}{d x}=2 x^{\log x} \frac{\log x}{x} \\
& \Rightarrow \frac{d v}{d x}=2 x^{\log x-1} \cdot \log x
\end{aligned}
$$

Therefore, from (1), (2) and (3);

$$
\frac{d y}{d x}=(\log x)^{x-1}[1+\log x \cdot \log (\log x)]+2 x^{\log x-1} \cdot \log x
$$
:::

:::

:::question{number="8" kind="exercise" id="q_5.5.8" topic="Logarithmic differentiation: (sin x)^x+sin ^-1 sqrt x"}
#### Question 8

:::prompt
$(\sin x)^{x}+\sin ^{-1} \sqrt{x}$
:::

:::solution{label="Solution"}
Let $y=(\sin x)^{x}+\sin ^{-1} \sqrt{x}$
Also, let $u=(\sin x)^{x}$ and $v=\sin ^{-1} \sqrt{x}$

$$
\begin{aligned}
& \therefore y=u+v \\
& \Rightarrow \frac{d y}{d x}=\frac{d u}{d x}+\frac{d v}{d x}
\end{aligned}
$$

Then, $u=(\sin x)^{x}$
Taking logarithm on both the sides, we obtain

$$
\begin{aligned}
& \Rightarrow \log u=\log (\sin x)^{x} \\
& \Rightarrow \log u=x \log (\sin x)
\end{aligned}
$$

Differentiating both sides with respect to $x$, we obtain

$$
\begin{aligned}
& \frac{1}{u} \cdot \frac{d u}{d x}=\frac{d}{d x}(x) \times \log (\sin x)+x \cdot \frac{d}{d x}[\log (\sin x)] \\
& \Rightarrow \frac{d u}{d x}=u\left[1 \times \log (\sin x)+x \cdot \frac{1}{(\sin x)} \cdot \frac{d}{d x}(\sin x)\right] \\
& \Rightarrow \frac{d u}{d x}=(\sin x)^{x}\left[\log (\sin x)+\frac{x}{(\sin x)} \cdot \cos x\right] \\
& \Rightarrow \frac{d u}{d x}=(\sin x)^{x}[x \cot x+\log \sin x]
\end{aligned}
$$

$$
v=\sin ^{-1} \sqrt{x}
$$

Differentiating both sides with respect to $x$, we obtain

$$
\begin{aligned}
& \frac{d v}{d x}=\frac{1}{\sqrt{1-(\sqrt{x})^{2}}} \cdot \frac{d}{d x}(\sqrt{x}) \\
& \Rightarrow \frac{d v}{d x}=\frac{1}{\sqrt{1-x}} \cdot \frac{1}{2 \sqrt{x}} \\
& \Rightarrow \frac{d v}{d x}=\frac{1}{2 \sqrt{x-x^{2}}}
\end{aligned}
$$

Therefore, from (1), (2) and (3);

$$
\frac{d y}{d x}=(\sin x)^{x}[x \cot x+\log \sin x]+\frac{1}{2 \sqrt{x-x^{2}}}
$$
:::

:::

:::question{number="9" kind="exercise" id="q_5.5.9" topic="Logarithmic differentiation: x^sin x+(sin x)^cos x"}
#### Question 9

:::prompt
$x^{\sin x}+(\sin x)^{\cos x}$
:::

:::solution{label="Solution"}
Let $y=x^{\sin x}+(\sin x)^{\cos x}$
Also, let $u=x^{\sin x}$ and $v=(\sin x)^{\cos x}$

$$
\begin{aligned}
& \therefore y=u+v \\
& \Rightarrow \frac{d y}{d x}=\frac{d u}{d x}+\frac{d v}{d x}
\end{aligned}
$$

Then, $u=x^{\sin x}$
Taking logarithm on both the sides, we obtain

$$
\begin{aligned}
& \Rightarrow \log u=\log \left(x^{\sin x}\right) \\
& \Rightarrow \log u=\sin x \log x
\end{aligned}
$$

Differentiating both sides with respect to $x$, we obtain

$$
\begin{aligned}
& \frac{1}{u} \cdot \frac{d u}{d x}=\frac{d}{d x}(\sin x) \cdot \log x+\sin x \cdot \frac{d}{d x}(\log x) \\
& \Rightarrow \frac{d u}{d x}=u\left[\cos x \log x+\sin x \cdot \frac{1}{x}\right] \\
& \Rightarrow \frac{d u}{d x}=x^{\sin x}\left[\cos x \log x+\frac{\sin x}{x}\right]
\end{aligned}
$$

$$
v=(\sin x)^{\cos x}
$$

Taking logarithm on both the sides, we obtain

$$
\begin{aligned}
& \Rightarrow \log v=\log (\sin x)^{\cos x} \\
& \Rightarrow \log v=\cos x \log (\sin x)
\end{aligned}
$$

Differentiating both sides with respect to $x$, we obtain

$$
\begin{aligned}
& \frac{1}{v} \frac{d v}{d x}=\frac{d}{d x}(\cos x) \times \log (\sin x)+\cos x \times \frac{d}{d x}[\log (\sin x)] \\
& \Rightarrow \frac{d v}{d x}=v\left[-\sin x \cdot \log (\sin x)+\cos x \cdot \frac{1}{\sin x} \cdot \frac{d}{d x}(\sin x)\right] \\
& \Rightarrow \frac{d v}{d x}=(\sin x)^{\cos x}\left[-\sin x \log (\sin x)+\frac{\cos x}{\sin x} \cos x\right] \\
& \Rightarrow \frac{d v}{d x}=(\sin x)^{\cos x}[-\sin x \log (\sin x)+\cot x \cos x] \\
& \Rightarrow \frac{d v}{d x}=(\sin x)^{\cos x}[\cot x \cos x-\sin x \log (\sin x)]
\end{aligned}
$$

Therefore, from (1), (2) and (3);

$$
\frac{d y}{d x}=x^{\sin x}\left\lceil\cos x \log x+\frac{\sin x}{x}\right\rceil+(\sin x)^{\cos x}[\cot x \cos x-\sin x \log (\sin x)]
$$
:::

:::

:::question{number="10" kind="exercise" id="q_5.5.10" topic="Logarithmic differentiation: x^x cos x+x^2+1x^2-1"}
#### Question 10

:::prompt
$x^{x \cos x}+\frac{x^{2}+1}{x^{2}-1}$
:::

:::solution{label="Solution"}
Let $y=x^{x \cos x}+\frac{x^{2}+1}{x^{2}-1}$
Also, let $u=x^{x \cos x}$ and $v=\frac{x^{2}+1}{x^{2}-1}$

$$
\begin{aligned}
& \therefore y=u+v \\
& \Rightarrow \frac{d y}{d x}=\frac{d u}{d x}+\frac{d v}{d x}
\end{aligned}
$$

Then, $u=x^{x \cos x}$
Taking logarithm on both the sides, we obtain

$$
\begin{aligned}
& \Rightarrow \log u=\log \left(x^{x \cos x}\right) \\
& \Rightarrow \log u=x \cos x \log x
\end{aligned}
$$

Differentiating both sides with respect to $x$, we obtain

$$
\begin{aligned}
& \frac{1}{u} \cdot \frac{d u}{d x}=\frac{d}{d x}(x) \cdot \cos x \cdot \log x+x \cdot \frac{d}{d x}(\cos x) \cdot \log x+x \cos x \cdot \frac{d}{d x}(\log x) \\
& \Rightarrow \frac{d u}{d x}=u\left[1 \cdot \cos x \cdot \log x+x \cdot(-\sin x) \log x+x \cos x \cdot \frac{1}{x}\right] \\
& \Rightarrow \frac{d u}{d x}=x^{x \cos x}[\cos x \log x-x \cdot \sin x \log x+\cos x] \\
& \Rightarrow \frac{d u}{d x}=x^{x \cos x}[\cos x(1+\log x)-x \cdot \sin x \log x]
\end{aligned}
$$

$$
v=\frac{x^{2}+1}{x^{2}-1}
$$

Taking logarithm on both the sides, we obtain

$$
\Rightarrow \log v=\log \left(x^{2}+1\right)-\log \left(x^{2}-1\right)
$$

Differentiating both sides with respect to $x$, we obtain

$$
\begin{aligned}
& \frac{1}{v} \frac{d v}{d x}=\frac{2 x}{x^{2}+1}-\frac{2 x}{x^{2}-1} \\
& \Rightarrow \frac{d v}{d x}=v\left[\frac{2 x\left(x^{2}-1\right)-2 x\left(x^{2}+1\right)}{\left(x^{2}+1\right)\left(x^{2}-1\right)}\right] \\
& \Rightarrow \frac{d v}{d x}=\frac{x^{2}+1}{x^{2}-1} \times\left[\frac{-4 x}{\left(x^{2}+1\right)\left(x^{2}-1\right)}\right] \\
& \Rightarrow \frac{d v}{d x}=\frac{-4 x}{\left(x^{2}-1\right)^{2}}
\end{aligned}
$$

Therefore, from (1), (2) and (3);

$$
\frac{d y}{d x}=x^{x \cos x}[\cos x(1+\log x)-x \cdot \sin x \log x]-\frac{4 x}{\left(x^{2}-1\right)^{2}}
$$
:::

:::

:::question{number="11" kind="exercise" id="q_5.5.11" topic="Logarithmic differentiation: (x cos x)^x+(x sin x)^1/x"}
#### Question 11

:::prompt
$(x \cos x)^{x}+(x \sin x)^{\frac{1}{x}}$
:::

:::solution{label="Solution"}
Let $y=(x \cos x)^{x}+(x \sin x)^{\frac{1}{x}}$
Also, let $u=(x \cos x)^{x}$ and $v=(x \sin x)^{\frac{1}{x}}$

$$
\begin{aligned}
& \therefore y=u+v \\
& \Rightarrow \frac{d y}{d x}=\frac{d u}{d x}+\frac{d v}{d x}
\end{aligned}
$$

Then, $u=(x \cos x)^{x}$
Taking logarithm on both the sides, we obtain

$$
\begin{aligned}
& \Rightarrow \log u=(x \cos x)^{x} \\
& \Rightarrow \log u=x \log (x \cos x) \\
& \Rightarrow \log u=x[\log x+\log \cos x] \\
& \Rightarrow \log u=x \log x+x \log \cos x
\end{aligned}
$$

Differentiating both sides with respect to $x$, we obtain

$$
\begin{aligned}
& \frac{1}{u} \cdot \frac{d u}{d x}=\frac{d}{d x}(x \log x)+\frac{d}{d x}(x \log \cos x) \\
& \Rightarrow \frac{d u}{d x}=u\left[\left\{\log x \cdot \frac{d}{d x}(x)+x \cdot \frac{d}{d x}(\log x)\right\}+\left\{\log \cos x \cdot \frac{d}{d x}(x)+x \cdot \frac{d}{d x}(\log \cos x)\right\}\right] \\
& \Rightarrow \frac{d u}{d x}=(x \cos x)^{x}\left[\left(\log x \cdot 1+x \cdot \frac{1}{x}\right)+\left\{\log \cos x \cdot 1+x \cdot \frac{1}{\cos x} \cdot \frac{d}{d x}(\cos x)\right\}\right] \\
& \Rightarrow \frac{d u}{d x}=(x \cos x)^{x}\left[(\log x+1)+\left\{\log \cos x+\frac{x}{\cos x} \cdot(-\sin x)\right\}\right] \\
& \Rightarrow \frac{d u}{d x}=(x \cos x)^{x}[(1+\log x)+(\log \cos x-x \tan x)] \\
& \Rightarrow \frac{d u}{d x}=(x \cos x)^{x}[(1-x \tan x)+(\log x+\log \cos x)] \\
& \Rightarrow \frac{d u}{d x}=(x \cos x)^{x}[1-x \tan x+\log (x \cos x)] \\
& v=(x \sin x)^{\frac{1}{x}}
\end{aligned}
$$

Taking logarithm on both the sides, we obtain

$$
\begin{aligned}
& \Rightarrow \log v=\log (x \sin x)^{\frac{1}{x}} \\
& \Rightarrow \log v=\frac{1}{x} \log (x \sin x) \\
& \Rightarrow \log v=\frac{1}{x}(\log x+\log \sin x) \\
& \Rightarrow \log v=\frac{1}{r} \log x+\frac{1}{r} \log \sin x
\end{aligned}
$$

Differentiating both sides with respect to $x$, we obtain

$$
\begin{aligned}
& \frac{1}{v} \frac{d v}{d x}=\frac{d}{d x}\left(\frac{1}{x} \log x\right)+\frac{d}{d x}\left[\frac{1}{x} \log (\sin x)\right] \\
& \Rightarrow \frac{1}{v} \frac{d v}{d x}=\left[\log x \cdot \frac{d}{d x}\left(\frac{1}{x}\right)+\frac{1}{x} \cdot \frac{d}{d x}(\log x)\right]+\left[\log (\sin x) \cdot \frac{d}{d x}\left(\frac{1}{x}\right)+\frac{1}{x} \cdot \frac{d}{d x}\{\log (\sin x)\}\right] \\
& \Rightarrow \frac{1}{v} \frac{d v}{d x}=\left[\log x \cdot\left(-\frac{1}{x^{2}}\right)+\frac{1}{x} \cdot \frac{1}{x}\right]+\left[\log (\sin x) \cdot\left(-\frac{1}{x^{2}}\right)+\frac{1}{x} \cdot \frac{1}{\sin x} \cdot \frac{d}{d x}(\sin x)\right] \\
& \Rightarrow \frac{1}{v} \frac{d v}{d x}=\frac{1}{x^{2}}(1-\log x)+\left[-\frac{\log (\sin x)}{x^{2}}+\frac{1}{x \sin x} \cdot \cos x\right] \\
& \Rightarrow \frac{d v}{d x}=(x \sin x)^{\frac{1}{x}}\left[\frac{1-\log x}{x^{2}}+\frac{-\log (\sin x)+x \cot x}{x^{2}}\right] \\
& \Rightarrow \frac{d v}{d x}=(x \sin x)^{\frac{1}{x}}\left[\frac{1-\log x-\log (\sin x)+x \cot x}{x^{2}}\right] \\
& \Rightarrow \frac{d v}{d x}=(x \sin x)^{\frac{1}{x}}\left[\frac{1-\log (x \sin x)+x \cot x}{x^{2}}\right]
\end{aligned}
$$

Therefore, from (1), (2) and (3);

$$
\frac{d y}{d x}=(x \cos x)^{x}[1-x \tan x+\log (x \cos x)]+(x \sin x)^{\frac{1}{x}}\left\lceil\frac{x \cot x+1-\log (x \sin x)}{x^{2}}\right\rceil
$$
:::

:::

:::question{number="12" kind="exercise" id="q_5.5.12" topic="Logarithmic differentiation: x^y+y^x=1"}
#### Question 12

:::prompt
$x^{y}+y^{x}=1$
:::

:::solution{label="Solution"}
The given function is $x^{y}+y^{x}=1$

Let, $x^{y}=u$ and $y^{x}=v$

$$
\begin{aligned}
& \therefore u+v=1 \\
& \Rightarrow \frac{d u}{d x}+\frac{d v}{d x}=0
\end{aligned}
$$

Then, $u=x^{y}$
Taking logarithm on both the sides, we obtain

$$
\begin{aligned}
& \Rightarrow \log u=\log \left(x^{y}\right) \\
& \Rightarrow \log u=y \log x
\end{aligned}
$$

Differentiating both sides with respect to $x$, we obtain

$$
\begin{aligned}
& \frac{1}{u} \cdot \frac{d u}{d x}=\log x \frac{d y}{d x}+y \cdot \frac{d}{d x}(\log x) \\
& \Rightarrow \frac{d u}{d x}=u\left[\log x \frac{d y}{d x}+y \cdot \frac{1}{x}\right] \\
& \Rightarrow \frac{d u}{d x}=x^{y}\left[\log x \frac{d y}{d x}+\frac{y}{x}\right]
\end{aligned}
$$

Now, $v=y^{x}$
Taking logarithm on both the sides, we obtain

$$
\begin{aligned}
& \Rightarrow \log v=\log \left(y^{x}\right) \\
& \Rightarrow \log v=x \log y
\end{aligned}
$$

Differentiating both sides with respect to $x$, we obtain

$$
\begin{aligned}
& \frac{1}{v} \frac{d v}{d x}=\log y \cdot \frac{d}{d x}(x)+x \cdot \frac{d}{d x}(\log y) \\
& \Rightarrow \frac{d v}{d x}=v\left[\log y \cdot 1+x \cdot \frac{1}{y} \cdot \frac{d y}{d x}\right] \\
& \Rightarrow \frac{d v}{d x}=y^{x}\left[\log y+\frac{x}{y} \cdot \frac{d y}{d x}\right]
\end{aligned}
$$

Therefore, from (1), (2) and (3);

$$
\begin{aligned}
& x^{y}\left[\log x \frac{d y}{d x}+\frac{y}{x}\right]+y^{x}\left[\log y+\frac{x}{y} \cdot \frac{d y}{d x}\right]=0 \\
& \Rightarrow\left(x^{y} \log x+x y^{x-1}\right) \frac{d y}{d x}=-\left(y x^{y-1}+y^{x} \log y\right) \\
& \therefore \frac{d y}{d x}=\frac{-\left(y x^{y-1}+y^{x} \log y\right)}{\left(x^{y} \log x+x y^{x-1}\right)}
\end{aligned}
$$
:::

:::

:::question{number="13" kind="exercise" id="q_5.5.13" topic="Logarithmic differentiation: y^x=x^y"}
#### Question 13

:::prompt
$y^{x}=x^{y}$
:::

:::solution{label="Solution"}
The given function is $y^{x}=x^{y}$

Taking logarithm on both the sides, we obtain

$$
x \log y=y \log x
$$

Differentiating both sides with respect to $x$, we obtain

$$
\begin{aligned}
& \log y \cdot \frac{d}{d x}(x)+x \cdot \frac{d}{d x}(\log y)=\log x \cdot \frac{d}{d x}(y)+y \cdot \frac{d}{d x}(\log x) \\
& \Rightarrow \log y \cdot 1+x \cdot \frac{1}{y} \cdot \frac{d y}{d x}=\log x \cdot \frac{d y}{d x}+y \cdot \frac{1}{x} \\
& \Rightarrow \log y+\frac{x}{y} \cdot \frac{d y}{d x}=\log x \cdot \frac{d y}{d x}+\frac{y}{x} \\
& \Rightarrow\left(\frac{x}{y}-\log x\right) \frac{d y}{d x}=\frac{y}{x}-\log y \\
& \Rightarrow\left(\frac{x-y \log x}{y}\right) \frac{d y}{d x}=\frac{y-x \log y}{x} \\
& \therefore \frac{d y}{d x}=\frac{y}{x}\left(\frac{y-x \log y}{x-y \log x}\right)
\end{aligned}
$$
:::

:::

:::question{number="14" kind="exercise" id="q_5.5.14" topic="Logarithmic differentiation: (cos x)^y=(cos y)^x"}
#### Question 14

:::prompt
$(\cos x)^{y}=(\cos y)^{x}$
:::

:::solution{label="Solution"}
The given function is $(\cos x)^{y}=(\cos y)^{x}$
Taking logarithm on both the sides, we obtain

$$
y \log \cos x=x \log \cos y
$$

Differentiating both sides with respect to $x$, we obtain

$$
\begin{aligned}
& \log \cos x \cdot \frac{d y}{d x}+y \cdot \frac{d}{d x}(\log \cos x)=\log \cos y \cdot \frac{d}{d x}(x)+x \cdot \frac{d}{d x}(\log \cos y) \\
& \Rightarrow \log \cos x \cdot \frac{d y}{d x}+y \cdot \frac{1}{\cos x} \cdot \frac{d}{d x}(\cos x)=\log \cos y \cdot 1+x \cdot \frac{1}{\cos y} \cdot \frac{d}{d x}(\cos y) \\
& \Rightarrow \log \cos x \cdot \frac{d y}{d x}+\frac{y}{\cos x} \cdot(-\sin x)=\log \cos y+\frac{x}{\cos y} \cdot(-\sin y) \cdot \frac{d y}{d x} \\
& \Rightarrow \log \cos x \cdot \frac{d y}{d x}-y \tan x=\log \cos y-x \tan y \frac{d y}{d x} \\
& \Rightarrow(\log \cos x+x \tan y) \frac{d y}{d x}=y \tan x+\log \cos y \\
& \therefore \frac{d y}{d x}=\frac{y \tan x+\log \cos y}{x \tan y+\log \cos x}
\end{aligned}
$$
:::

:::

:::question{number="15" kind="exercise" id="q_5.5.15" topic="Logarithmic differentiation: x y=e^(x-y)"}
#### Question 15

:::prompt
$x y=e^{(x-y)}$
:::

:::solution{label="Solution"}
The given function is $x y=e^{(x-y)}$

Taking logarithm on both the sides, we obtain

$$
\begin{aligned}
& \log (x y)=\log \left(e^{x-y}\right) \\
& \Rightarrow \log x+\log y=(x-y) \log e \\
& \Rightarrow \log x+\log y=(x-y) \times 1 \\
& \Rightarrow \log x+\log y=(x-y)
\end{aligned}
$$

Differentiating both sides with respect to $x$, we obtain

$$
\begin{aligned}
& \frac{d}{d x}(\log x)+\frac{d}{d x}(\log y)=\frac{d}{d x}(x)-\frac{d y}{d x} \\
& \Rightarrow \frac{1}{x}+\frac{1}{y} \frac{d y}{d x}=1-\frac{d y}{d x} \\
& \Rightarrow\left(1+\frac{1}{y}\right) \frac{d y}{d x}=1-\frac{1}{x} \\
& \Rightarrow\left(\frac{y+1}{y}\right) \frac{d y}{d x}=\frac{x-1}{x} \\
& \therefore \frac{d y}{d x}=\frac{y(x-1)}{x(y+1)}
\end{aligned}
$$
:::

:::

:::question{number="16" kind="exercise" id="q_5.5.16" topic="Logarithmic differentiation: f(x)=(1+x)(1+x^2)(1+x^4)(1..."}
#### Question 16

:::prompt
Find the derivative of the function given by $f(x)=(1+x)\left(1+x^{2}\right)\left(1+x^{4}\right)\left(1+x^{8}\right)$ and hence find $f^{\prime}(1)$.
:::

:::solution{label="Solution"}
The given function is $f(x)=(1+x)\left(1+x^{2}\right)\left(1+x^{4}\right)\left(1+x^{8}\right)$

Taking logarithm on both the sides, we obtain

$$
\log f(x)=\log (1+x)+\log \left(1+x^{2}\right)+\log \left(1+x^{4}\right)+\log \left(1+x^{8}\right)
$$

Differentiating both sides with respect to $x$, we obtain

$$
\begin{aligned}
& \begin{aligned}
\frac{1}{f(x)} \cdot \frac{d}{d x}[f(x)]= & \frac{d}{d x} \log (1+x)+\frac{d}{d x} \log \left(1+x^{2}\right) \\
+ & \frac{d}{d x} \log \left(1+x^{4}\right)+\frac{d}{d x} \log \left(1+x^{8}\right)
\end{aligned} \\
& \Rightarrow \frac{1}{f(x)} \cdot f^{\prime}(x)=\frac{1}{1+x} \cdot \frac{d}{d x}(1+x)+\frac{1}{1+x^{2}} \cdot \frac{d}{d x}\left(1+x^{2}\right) \\
& +\frac{1}{1+x^{4}} \cdot \frac{d}{d x}\left(1+x^{4}\right)+\frac{1}{1+x^{8}} \cdot \frac{d}{d x}\left(1+x^{8}\right) \\
& \Rightarrow f^{\prime}(x)=f(x)\left[\frac{1}{1+x}+\frac{1}{1+x^{2}} \cdot 2 x+\frac{1}{1+x^{4}} \cdot 4 x^{3}+\frac{1}{1+x^{8}} \cdot 8 x^{7}\right] \\
& \therefore f^{\prime}(x)=(1+x)\left(1+x^{2}\right)\left(1+x^{4}\right)\left(1+x^{8}\right)\left[\frac{1}{1+x}+\frac{2 x}{1+x^{2}}+\frac{4 x^{3}}{1+x^{4}}+\frac{8 x^{7}}{1+x^{8}}\right]
\end{aligned}
$$

Hence,

$$
\begin{aligned}
f^{\prime}(1) & =(1+1)\left(1+1^{2}\right)\left(1+1^{4}\right)\left(1+1^{8}\right)\left[\frac{1}{1+1}+\frac{2(1)}{1+1^{2}}+\frac{4(1)^{3}}{1+1^{4}}+\frac{8(1)^{7}}{1+1^{8}}\right] \\
& =2 \times 2 \times 2 \times 2\left[\frac{1}{2}+\frac{2}{2}+\frac{4}{2}+\frac{8}{2}\right] \\
& =16\left(\frac{15}{2}\right) \\
& =120
\end{aligned}
$$
:::

:::

:::question{number="17" kind="exercise" id="q_5.5.17" topic="Logarithmic differentiation: (x^2-5 x+8)(x^3+7 x+9)"}
#### Question 17

:::prompt
Differentiate $\left(x^{2}-5 x+8\right)\left(x^{3}+7 x+9\right)$ in three ways mentioned below:


(i) by using product rule
(ii) by expanding the product to obtain a single polynomial.
(iii) by logarithmic differentiation.

Do they all give the same answer?
:::

:::part{label="i"}
:::prompt
by using product rule
:::

:::solution
Let $y=\left(x^{2}-5 x+8\right)\left(x^{3}+7 x+9\right)$
Let $u=\left(x^{2}-5 x+8\right)$ and $v=x^{3}+7 x+9$
$$
\begin{aligned}
& \therefore y=u v \\
& \Rightarrow \frac{d y}{d x}=\frac{d u}{d x} \cdot v+u \cdot \frac{d v}{d x} \\
& \Rightarrow \frac{d y}{d x}=\frac{d}{d x}\left(x^{2}-5 x+8\right) \cdot\left(x^{3}+7 x+9\right)+\left(x^{2}-5 x+8\right) \cdot \frac{d}{d x}\left(x^{3}+7 x+9\right) \\
& \Rightarrow \frac{d y}{d x}=(2 x-5)\left(x^{3}+7 x+9\right)+\left(x^{2}-5 x+8\right)\left(3 x^{2}+7\right) \\
& \Rightarrow \frac{d y}{d x}=2 x\left(x^{3}+7 x+9\right)-5\left(x^{3}+7 x+9\right)+x^{2}\left(3 x^{2}+7\right) \\
& -5 x\left(3 x^{2}+7\right)+8\left(3 x^{2}+7\right) \\
& \Rightarrow \frac{d y}{d x}=\left(2 x^{4}+14 x^{2}+18 x\right)-5 x^{3}-35 x-45+\left(3 x^{4}+7 x^{2}\right) \\
& \Rightarrow \frac{d y}{d x}=-15 x^{3}-35 x+24 x^{2}+56 \\
& \therefore \frac{d y}{d x}=5 x^{4}-20 x^{3}+45 x^{2}-52 x+11
\end{aligned}
$$
:::

:::

:::part{label="ii"}
:::prompt
by expanding the product to obtain a single polynomial.
:::

:::solution
$$
\begin{aligned}
y & =\left(x^{2}-5 x+8\right)\left(x^{3}+7 x+9\right) \\
& =x^{2}\left(x^{3}+7 x+9\right)-5 x\left(x^{3}+7 x+9\right)+8\left(x^{3}+7 x+9\right) \\
& =x^{5}+7 x^{3}+9 x^{2}-5 x^{4}-35 x^{2}-45 x+8 x^{3}+56 x+72 \\
& =x^{5}-5 x^{4}+15 x^{3}-26 x^{2}+11 x+72
\end{aligned}
$$
Therefore,
$$
\begin{aligned}
\frac{d y}{d x} & =\frac{d}{d x}\left(x^{5}-5 x^{4}+15 x^{3}-26 x^{2}+11 x+72\right) \\
& =\frac{d}{d x}\left(x^{5}\right)-5 \frac{d}{d x}\left(x^{4}\right)+15 \frac{d}{d x}\left(x^{3}\right)-26 \frac{d}{d x}\left(x^{2}\right)+11 \frac{d}{d x}(x)+\frac{d}{d x} \\
& =5 x^{4}-5\left(4 x^{3}\right)+15\left(3 x^{2}\right)-26(2 x)+11(1)+0 \\
& =5 x^{4}-20 x^{3}+45 x^{2}-52 x+11
\end{aligned}
$$
:::

:::

:::part{label="iii"}
:::prompt
by logarithmic differentiation.
:::

:::solution
$$
y=\left(x^{2}-5 x+8\right)\left(x^{3}+7 x+9\right)
$$
Taking logarithm on both the sides, we obtain
$$
\log y=\log \left(x^{2}-5 x+8\right)+\log \left(x^{3}+7 x+9\right)
$$
Differentiating both sides with respect to $x$, we obtain
$$
\begin{aligned}
& \frac{1}{y} \cdot \frac{d y}{d x}=\frac{d}{d x} \log \left(x^{2}-5 x+8\right)+\frac{d}{d x} \log \left(x^{3}+7 x+9\right) \\
& \Rightarrow \frac{1}{y} \cdot \frac{d y}{d x}=\frac{1}{x^{2}-5 x+8} \cdot \frac{d}{d x}\left(x^{2}-5 x+8\right)+\frac{1}{x^{3}+7 x+9} \cdot \frac{d}{d x}\left(x^{3}+7 x+9\right) \\
& \Rightarrow \frac{d y}{d x}=y\left[\frac{1}{x^{2}-5 x+8} \cdot(2 x-5)+\frac{1}{x^{3}+7 x+9} \cdot\left(3 x^{2}+7\right)\right] \\
& \Rightarrow \frac{d y}{d x}=\left(x^{2}-5 x+8\right)\left(x^{3}+7 x+9\right)\left[\frac{2 x-5}{x^{2}-5 x+8}+\frac{3 x^{2}+7}{x^{3}+7 x+9}\right] \\
& \Rightarrow \frac{d y}{d x}=\left(x^{2}-5 x+8\right)\left(x^{3}+7 x+9\right)\left[\frac{(2 x-5)\left(x^{3}+7 x+9\right)+\left(3 x^{2}+7\right)\left(x^{2}-5 x+8\right)}{\left(x^{2}-5 x+8\right)\left(x^{3}+7 x+9\right)}\right] \\
& \Rightarrow \frac{d y}{d x}=2 x\left(x^{3}+7 x+9\right)-5\left(x^{3}+7 x+9\right)+3 x^{2}\left(x^{2}-5 x+8\right)+7\left(x^{2}-5 x+8\right) \\
& \Rightarrow \frac{d y}{d x}=2 x^{4}+14 x^{2}+18 x-5 x^{3}-35 x-45+3 x^{5}-15 x^{3}+24 x^{2}+7 x^{2}-35 x+56 \\
& \Rightarrow \frac{d y}{d x}=5 x^{4}-20 x^{3}+45 x^{2}-52 x+11
\end{aligned}
$$
:::

:::

:::answer
**Answer:** From the above three observations, it can be concluded that all the results of $\frac{d y}{d x}$ are same.
:::

:::

:::question{number="18" kind="exercise" id="q_5.5.18" topic="Logarithmic differentiation: u, v"}
#### Question 18

:::prompt
If $u, v$ and $w$ are functions of $x$, then show that

$$
\frac{d}{d x}(u \cdot v \cdot w)=\frac{d u}{d x} v \cdot w+u \cdot \frac{d v}{d x} \cdot w+u \cdot v \frac{d w}{d x}
$$

in two ways - first by repeated application of product rule, second by logarithmic differentiation.
:::

:::solution{label="Solution"}
Let $y=u . v . w=u .(v . w)$
By applying product rule, we get

$$
\begin{aligned}
& \frac{d y}{d x}=\frac{d u}{d x} \cdot(v \cdot w)+u \cdot \frac{d}{d x}(v \cdot w) \\
& \Rightarrow \frac{d y}{d x}=\frac{d u}{d x} \cdot(v \cdot w)+u\left[\frac{d v}{d x} \cdot w+v \cdot \frac{d w}{d x}\right] \quad \text { (Again applying product rule) } \\
& \Rightarrow \frac{d y}{d x}=\frac{d u}{d x} \cdot v \cdot w+u \cdot \frac{d v}{d x} \cdot w+u \cdot v \cdot \frac{d w}{d x}
\end{aligned}
$$

Taking logarithm on both the sides of the equation $y=u . v . w$, we obtain $\log y=\log u+\log v+\log w$

Differentiating both sides with respect to $x$, we obtain

$$
\begin{aligned}
& \frac{1}{y} \cdot \frac{d y}{d x}=\frac{d}{d x}(\log u)+\frac{d}{d x}(\log v)+\frac{d}{d x}(\log w) \\
& \Rightarrow \frac{1}{y} \cdot \frac{d y}{d x}=\frac{1}{u} \frac{d u}{d x}+\frac{1}{v} \frac{d v}{d x}+\frac{1}{w} \frac{d w}{d x} \\
& \Rightarrow \frac{d y}{d x}=y\left(\frac{1}{u} \frac{d u}{d x}+\frac{1}{v} \frac{d v}{d x}+\frac{1}{w} \frac{d w}{d x}\right) \\
& \Rightarrow \frac{d y}{d x}=u . v . w\left(\frac{1}{u} \frac{d u}{d x}+\frac{1}{v} \frac{d v}{d x}+\frac{1}{w} \frac{d w}{d x}\right) \\
& \therefore \frac{d}{d x}(u . v . w)=\frac{d u}{d x} v . w+u \cdot \frac{d v}{d x} . w+u . v . \frac{d w}{d x}
\end{aligned}
$$
:::

:::

:::question{number="1" kind="exercise" id="q_5.6.1" topic="Parametric derivative: x=2 a t^2, y=a t^4"}
#### Question 1

:::prompt
$x=2 a t^{2}, y=a t^{4}$
:::

:::solution{label="Solution"}
Given, $x=2 a t^{2}, y=a t^{4}$
Then,

$$
\begin{aligned}
& \frac{d x}{d t}=\frac{d}{d t}\left(2 a t^{2}\right)=2 a \cdot \frac{d}{d t}\left(t^{2}\right)=2 a \cdot 2 t=4 a t \\
& \frac{d y}{d t}=\frac{d}{d t}\left(a t^{4}\right)=a \cdot \frac{d}{d t}\left(t^{4}\right)=a \cdot 4 \cdot t^{3}=4 a t^{3} \\
& \therefore \frac{d y}{d t}=\frac{\left(\frac{d y}{d t}\right)}{\left(\frac{d x}{d t}\right)}=\frac{4 a t^{3}}{4 a t}=t^{2}
\end{aligned}
$$
:::

:::

:::question{number="2" kind="exercise" id="q_5.6.2" topic="Parametric derivative: x=a cos , y=b cos"}
#### Question 2

:::prompt
$x=a \cos \theta, y=b \cos \theta$
:::

:::solution{label="Solution"}
Given, $x=a \cos \theta, y=b \cos \theta$
Then,

$$
\begin{aligned}
& \frac{d x}{d \theta}=\frac{d}{d \theta}(a \cos \theta)=a(-\sin \theta)=-a \sin \theta \\
& \frac{d y}{d \theta}=\frac{d}{d \theta}(b \cos \theta)=b(-\sin \theta)=-b \sin \theta \\
& \therefore \frac{d y}{d x}=\frac{\left(\frac{d y}{d \theta}\right)}{\left(\frac{d x}{d \theta}\right)}=\frac{-b \sin \theta}{-a \sin \theta}=\frac{b}{a}
\end{aligned}
$$
:::

:::

:::question{number="3" kind="exercise" id="q_5.6.3" topic="Parametric derivative: x=sin t, y=cos 2 t"}
#### Question 3

:::prompt
$x=\sin t, y=\cos 2 t$
:::

:::solution{label="Solution"}
Given, $x=\sin t, y=\cos 2 t$
Then, $\frac{d x}{d t}=\frac{d}{d t}(\sin t)=\cos t$

$$
\begin{aligned}
& \frac{d y}{d t}=\frac{d}{d t}(\cos 2 t)=-\sin 2 t \cdot \frac{d}{d t}(2 t)=-2 \sin 2 t \\
& \therefore \frac{d y}{d x}=\frac{\left(\frac{d y}{d t}\right)}{\left(\frac{d x}{d t}\right)}=\frac{-2 \sin 2 t}{\cos t}=\frac{-2 \cdot 2 \sin t \cos t}{\cos t}=-4 \sin t
\end{aligned}
$$
:::

:::

:::question{number="4" kind="exercise" id="q_5.6.4" topic="Parametric derivative: x=4 t, y=4/t"}
#### Question 4

:::prompt
$x=4 t, y=\frac{4}{t}$
:::

:::solution{label="Solution"}
Given, $x=4 t, y=\frac{4}{t}$

$$
\begin{aligned}
& \frac{d x}{d t}=\frac{d}{d t}(4 t)=4 \\
& \frac{d y}{d t}=\frac{d}{d t}\left(\frac{4}{t}\right)=4 \cdot \frac{d}{d t}\left(\frac{1}{t}\right)=4 \cdot\left(\frac{-1}{t^{2}}\right)=\frac{-4}{t^{2}} \\
& \therefore \frac{d y}{d x}=\frac{\left(\frac{d y}{d t}\right)}{\left(\frac{d x}{d t}\right)}=\frac{\left(\frac{-4}{t^{2}}\right)}{4}=\frac{-1}{t^{2}}
\end{aligned}
$$
:::

:::

:::question{number="5" kind="exercise" id="q_5.6.5" topic="Parametric derivative: x=cos -cos 2 , y=sin -sin..."}
#### Question 5

:::prompt
$x=\cos \theta-\cos 2 \theta, y=\sin \theta-\sin 2 \theta$
:::

:::solution{label="Solution"}
Given, $x=\cos \theta-\cos 2 \theta, y=\sin \theta-\sin 2 \theta$
Then,

$$
\begin{aligned}
& \frac{d x}{d \theta}=\frac{d}{d \theta}(\cos \theta-\cos 2 \theta)=\frac{d}{d \theta}(\cos \theta)-\frac{d}{d \theta}(\cos 2 \theta) \\
& =-\sin \theta-(-2 \sin 2 \theta)=2 \sin 2 \theta-\sin \theta \\
& \frac{d y}{d \theta}=\frac{d}{d \theta}(\sin \theta-\sin 2 \theta)=\frac{d}{d \theta}(\sin \theta)-\frac{d}{d \theta}(\sin 2 \theta) \\
& =\cos \theta-2 \cos 2 \theta \\
& \therefore \frac{d y}{d x}=\frac{\left(\frac{d y}{d \theta}\right)}{\left(\frac{d x}{d \theta}\right)}=\frac{\cos \theta-2 \cos 2 \theta}{2 \sin 2 \theta-\sin \theta}
\end{aligned}
$$
:::

:::

:::question{number="6" kind="exercise" id="q_5.6.6" topic="Parametric derivative: x=a(-sin ), y=a(1+cos )"}
#### Question 6

:::prompt
$x=a(\theta-\sin \theta), y=a(1+\cos \theta)$
:::

:::solution{label="Solution"}
Given, $x=a(\theta-\sin \theta), y=a(1+\cos \theta)$

$$
\begin{aligned}
& \text { Then, } \frac{d x}{d \theta}=a\left[\frac{d}{d \theta}(\theta)-\frac{d}{d \theta}(\sin \theta)\right]=a(1-\cos \theta) \\
& \frac{d y}{d \theta}=a\left[\frac{d}{d \theta}(1)+\frac{d}{d \theta}(\cos \theta)\right]=a[0+(-\sin \theta)]=-a \sin \theta \\
& \therefore \frac{d y}{d x}=\frac{\left(\frac{d y}{d \theta}\right)}{\left(\frac{d x}{d \theta}\right)}=\frac{-a \sin \theta}{a(1-\cos \theta)}=\frac{-2 \sin \frac{\theta}{2} \cos \frac{\theta}{2}}{2 \sin ^{2} \frac{\theta}{2}}=\frac{-\cos \frac{\theta}{2}}{\sin \frac{\theta}{2}}=-\cot \frac{\theta}{2}
\end{aligned}
$$
:::

:::

:::question{number="7" kind="exercise" id="q_5.6.7" topic="Parametric derivative: x=sin ^3 tsqrt cos 2 t, y=..."}
#### Question 7

:::prompt
$x=\frac{\sin ^{3} t}{\sqrt{\cos 2 t}}, y=\frac{\cos ^{3} t}{\sqrt{\cos 2 t}}$
:::

:::solution{label="Solution"}
Given, $x=\frac{\sin ^{3} t}{\sqrt{\cos 2 t}}, y=\frac{\cos ^{3} t}{\sqrt{\cos 2 t}}$
Then,

$$
\begin{aligned}
& \frac{d x}{d t}=\frac{d}{d t}\left[\frac{\sin ^{3} t}{\sqrt{\cos 2 t}}\right] \\
& =\frac{\sqrt{\cos 2 t} \cdot \frac{d}{d t}\left(\sin ^{3} t\right)-\sin ^{3} t \cdot \frac{d}{d t} \sqrt{\cos 2 t}}{\cos 2 t} \\
& =\frac{\sqrt{\cos 2 t} \cdot 3 \sin ^{2} t \cdot \frac{d}{d t}(\sin t)-\sin ^{3} t \times \frac{1}{2 \sqrt{\cos 2 t}} \cdot \frac{d}{d t}(\cos 2 t)}{\cos 2 t} \\
& =\frac{3 \sqrt{\cos 2 t} \cdot \sin ^{2} t \cdot \cos t-\frac{\sin ^{3} t}{2 \sqrt{\cos 2 t}} \cdot(-2 \sin 2 t)}{\cos 2 t} \\
& =\frac{3 \cos 2 t \cdot \sin ^{2} t \cos t+\sin ^{3} t \cdot \sin 2 t}{\cos 2 t \sqrt{\cos 2 t}} \\
& \frac{d y}{d t}=\frac{d}{d t}\left[\frac{\cos ^{3} t}{\sqrt{\cos 2 t}}\right] \\
& =\frac{\sqrt{\cos 2 t} \cdot \frac{d}{d t}\left(\cos ^{3} t\right)-\cos ^{3} t \cdot \frac{d}{d t}(\sqrt{\cos 2 t})}{\cos 2 t} \\
& =\frac{\sqrt{\cos 2 t} \cdot 3 \cos ^{2} t \cdot \frac{d}{d t}(\cos t)-\cos ^{3} t \cdot \frac{1}{2 \sqrt{\cos 2 t}} \cdot \frac{d}{d t}(\cos 2 t)}{\cos 2 t} \\
& =\frac{3 \sqrt{\cos 2 t} \cdot \cos ^{2} t(-\sin t)-\cos ^{3} t \cdot \frac{1}{\sqrt{\cos 2 t}} \cdot(-2 \sin 2 t)}{\cos 2 t} \\
& =\frac{-3 \cos 2 t \cdot \cos ^{2} t \cdot \sin t+\cos ^{3} t \cdot \sin 2 t}{\cos 2 t^{\cos 2 t}}
\end{aligned}
$$

$$
\begin{aligned}
& \therefore \frac{d y}{d x}=\frac{\left(\frac{d y}{d t}\right)}{\left(\frac{d x}{d t}\right)}=\frac{\frac{-3 \cos 2 t \cdot \cos ^{2} t \cdot \sin t+\cos ^{3} t \sin 2 t}{\cos 2 t \cdot \sqrt{\cos 2 t}}}{\frac{3 \cos 2 t \cdot \sin ^{2} t \cdot \cos t+\sin ^{3} t \sin 2 t}{\cos 2 t \cdot \sqrt{\cos 2 t}}} \\
& =\frac{-3 \cos 2 t \cdot \cos ^{2} t \cdot \sin t+\cos ^{3} t \sin 2 t}{3 \cos 2 t \cdot \sin ^{2} t \cdot \cos t+\sin ^{3} t \sin 2 t} \\
& =\frac{-3 \cos 2 t \cdot \cos ^{2} t \cdot \sin t+\cos ^{3} t(2 \sin t \cos t)}{3 \cos 2 t \cdot \sin ^{2} t \cdot \cos t+\sin ^{3} t(2 \sin t \cos t)} \\
& =\frac{\sin t \cos t\left[-3 \cos 2 t \cdot \cos t+2 \cos ^{3} t\right]}{\sin t \cos t\left[3 \cos 2 t \sin t+2 \sin ^{3} t\right]} \\
& =\frac{\left[-3\left(2 \cos ^{2} t-1\right) \cos t+2 \cos ^{3} t\right]}{\left[3\left(1-2 \sin ^{2} t\right) \sin t+2 \sin ^{3} t\right]} \quad\left[\begin{array}{l}
\cos 2 t=\left(2 \cos ^{2} t-1\right) \\
\cos 2 t=\left(1-2 \sin ^{2} t\right)
\end{array}\right] \\
& =\frac{-4 \cos ^{3} t+3 \cos t}{3 \sin t-4 \sin ^{3} t} \quad\left[\begin{array}{l}
\cos 3 t=4 \cos ^{3} t-3 \cos t \\
\sin 3 t=3 \sin t-4 \sin ^{2} t
\end{array}\right] \\
& =\frac{-\cos 3 t}{\sin 3 t}=-\cot 3 t
\end{aligned}
$$
:::

:::

:::question{number="8" kind="exercise" id="q_5.6.8" topic="Parametric derivative: x=a(cos t+log tan t/2) y=a..."}
#### Question 8

:::prompt
$x=a\left(\cos t+\log \tan \frac{t}{2}\right) y=a \sin t$
:::

:::solution{label="Solution"}
Given, $x=a\left(\cos t+\log \tan \frac{t}{2}\right), y=a \sin t$

Then,

$$
\begin{aligned}
\frac{d x}{d t} & =a \cdot\left[\frac{d}{d t}(\cos t)+\frac{d}{d t}\left(\log \tan \frac{t}{2}\right)\right] \\
& =a\left[-\sin t+\frac{1}{\tan \frac{t}{2}} \cdot \frac{d}{d t}\left(\tan \frac{t}{2}\right)\right] \\
& =a\left[-\sin t+\cot \frac{t}{2} \cdot \sec ^{2} \frac{t}{2} \cdot \frac{d}{d t}\left(\frac{t}{2}\right)\right] \\
& =a\left[-\sin t+\frac{\cos \frac{t}{2}}{\sin \frac{t}{2}} \times \frac{1}{\cos ^{2} \frac{t}{2}} \times \frac{1}{2}\right] \\
& =a\left[-\sin t+\frac{1}{2 \sin \frac{t}{2} \cos \frac{t}{2}}\right] \\
& =a\left(-\sin t+\frac{1}{\sin t}\right) \\
& =a\left(\frac{-\sin s^{2} t+1}{\sin t}\right) \\
& =a\left(\frac{\cos ^{2} t}{\sin t}\right) \\
\frac{d y}{d t} & =a \frac{d}{d t}(\sin t)=a \cos t
\end{aligned}
$$

Therefore,

$$
\frac{d y}{d x}=\frac{\left(\frac{d y}{d t}\right)}{\left(\frac{d x}{d t}\right)}=\frac{a \cos t}{\left(a \frac{\cos ^{2} t}{\sin t}\right)}=\frac{\sin t}{\cos t}=\tan t
$$
:::

:::

:::question{number="9" kind="exercise" id="q_5.6.9" topic="Parametric derivative: x=a sec , y=b tan"}
#### Question 9

:::prompt
$x=a \sec \theta, y=b \tan \theta$
:::

:::solution{label="Solution"}
Given, $x=a \sec \theta, y=b \tan \theta$
Then,

$$
\begin{aligned}
& \frac{d x}{d \theta}=a \cdot \frac{d}{d \theta}(\sec \theta)=a \sec \theta \tan \theta \\
& \frac{d y}{d \theta}=b \cdot \frac{d}{d \theta}(\tan \theta)=b \sec ^{2} \theta
\end{aligned}
$$

Therefore,

$$
\begin{aligned}
\frac{d y}{d x} & =\frac{\left(\frac{d y}{d \theta}\right)}{\left(\frac{d x}{d \theta}\right)} \\
& =\frac{b \sec ^{2} \theta}{a \sec \theta \tan \theta} \\
& =\frac{b}{a} \sec \theta \cot \theta \\
& =\frac{b \cos \theta}{a \cos \theta \sin \theta} \\
& =\frac{b}{a} \times \frac{1}{\sin \theta} \\
& =\frac{b}{a} \operatorname{cosec} \theta
\end{aligned}
$$
:::

:::

:::question{number="10" kind="exercise" id="q_5.6.10" topic="Parametric derivative: x=a(cos + sin ), y=a(sin -..."}
#### Question 10

:::prompt
$x=a(\cos \theta+\theta \sin \theta), y=a(\sin \theta-\theta \cos \theta)$
:::

:::solution{label="Solution"}
Given, $x=a(\cos \theta+\theta \sin \theta), y=a(\sin \theta-\theta \cos \theta)$
Then,

$$
\begin{aligned}
\frac{d x}{d \theta} & =a\left[\frac{d}{d \theta} \cos \theta+\frac{d}{d \theta}(\theta \sin \theta)\right] \\
& =a\left[-\sin \theta+\theta \frac{d}{d \theta}(\sin \theta)+\sin \theta \frac{d}{d \theta}(\theta)\right] \\
& =a[-\sin \theta+\theta \cos \theta+\sin \theta] \\
& =a \theta \cos \theta
\end{aligned}
$$

$$
\begin{aligned}
\frac{d y}{d \theta} & =a\left[\frac{d}{d \theta}(\sin \theta)-\frac{d}{d \theta}(\theta \cos \theta)\right]=a\left[\cos \theta-\left\{\theta \frac{d}{d \theta}(\cos \theta)+\cos \theta \cdot \frac{d}{d \theta}(\theta)\right\}\right] \\
& =a[\cos \theta+\theta \sin \theta-\cos \theta] \\
& =a \theta \sin \theta
\end{aligned}
$$

Therefore,

$$
\begin{aligned}
\frac{d y}{d x} & =\frac{\left(\frac{d y}{d \theta}\right)}{\left(\frac{d x}{d \theta}\right)} \\
& =\frac{a \theta \sin \theta}{a \theta \cos \theta} \\
& =\tan \theta
\end{aligned}
$$
:::

:::

:::question{number="11" kind="exercise" id="q_5.6.11" topic="Parametric derivative: x=sqrt a^sin ^-1 t, y=sqrt..."}
#### Question 11

:::prompt
If $x=\sqrt{a^{\sin ^{-1} t}}, y=\sqrt{a^{\cos ^{-1} t}}$, show that $\frac{d y}{d x}=-\frac{y}{x}$
:::

:::solution{label="Solution"}
Given, $x=\sqrt{a^{\sin ^{-1} t}}$ and $y=\sqrt{a^{\cos ^{-1} t}}$
Hence,

$$
x=\sqrt{a^{\sin ^{-1} t}}=\left(a^{\sin ^{-1} t}\right)^{\frac{1}{2}}=a^{\frac{1}{2} \sin ^{-1} t} \text { and } y=\sqrt{a^{\cos ^{-1} t}}=\left(a^{\cos ^{-1} t}\right)^{\frac{1}{2}}=a^{\frac{1}{2} \cos ^{-1} t}
$$

Consider $x=a^{\frac{1}{2} \sin ^{-1} t}$
Taking $\log$ on both sides, we get

$$
\log x=\frac{1}{2} \sin ^{-1} t \log a
$$

Therefore,

$$
\begin{aligned}
& \Rightarrow \frac{1}{x} \cdot \frac{d x}{d t}=\frac{1}{2} \log a \cdot \frac{d}{d t}\left(\sin ^{-1} t\right) \\
& \Rightarrow \frac{d x}{d t}=\frac{x}{2} \log a \cdot \frac{1}{\sqrt{1-t^{2}}} \\
& \Rightarrow \frac{d x}{d t}=\frac{x \log a}{2 \sqrt{1-t^{2}}}
\end{aligned}
$$

Now, $y=a^{\frac{1}{2} \cos ^{-1} t}$
Taking log on both sides, we get

$$
\log x=\frac{1}{2} \cos ^{-1} t \log a
$$

Therefore,

$$
\begin{aligned}
& \Rightarrow \frac{1}{y} \cdot \frac{d y}{d t}=\frac{1}{2} \log a \cdot \frac{d}{d t}\left(\cos ^{-1} t\right) \\
& \Rightarrow \frac{d y}{d t}=\frac{y}{2} \log a \cdot \frac{-1}{\sqrt{1-t^{2}}} \\
& \Rightarrow \frac{d y}{d t}=\frac{-y \log a}{2 \sqrt{1-t^{2}}}
\end{aligned}
$$

Hence,

$$
\frac{d y}{d x}=\frac{\left(\frac{d y}{d t}\right)}{\left(\frac{d x}{d t}\right)}=\frac{\left(\frac{-y \log a}{2 \sqrt{1-t^{2}}}\right)}{\left(\frac{x \log a}{2 \sqrt{1-t^{2}}}\right)}=-\frac{y}{x}
$$
:::

:::

:::question{number="1" kind="exercise" id="q_5.7.1" topic="Second order derivative: x^2+3 x+2"}
#### Question 1

:::prompt
$x^{2}+3 x+2$
:::

:::solution{label="Solution"}
Consider, $y=x^{2}+3 x+2$
Then,

$$
\begin{aligned}
\frac{d y}{d x} & =\frac{d}{d x}\left(x^{2}\right)+\frac{d}{d x}(3 x)+\frac{d}{d x}(2) \\
& =2 x+3+0 \\
& =2 x+3
\end{aligned}
$$

Therefore,

$$
\begin{aligned}
\frac{d^{2} y}{d x^{2}} & =\frac{d}{d x}(2 x+3) \\
& =\frac{d}{d x}(2 x)+\frac{d}{d x}(3) \\
& =2+0 \\
& =?
\end{aligned}
$$
:::

:::

:::question{number="2" kind="exercise" id="q_5.7.2" topic="Second order derivative: x^20"}
#### Question 2

:::prompt
$x^{20}$
:::

:::solution{label="Solution"}
Consider, $y=x^{20}$
Then,

$$
\begin{aligned}
\frac{d y}{d x} & =\frac{d}{d x}\left(x^{20}\right) \\
& =20 x^{19}
\end{aligned}
$$

Therefore,

$$
\begin{aligned}
\frac{d^{2} y}{d x^{2}} & =\frac{d}{d x}\left(20 x^{19}\right) \\
& =20 \frac{d}{d x}\left(x^{19}\right) \\
& =20.19 . x^{18} \\
& =380 x^{18}
\end{aligned}
$$
:::

:::

:::question{number="3" kind="exercise" id="q_5.7.3" topic="Second order derivative: x * cos x"}
#### Question 3

:::prompt
$x \cdot \cos x$
:::

:::solution{label="Solution"}
Consider, $y=x \cos x$

Then,

$$
\begin{aligned}
\frac{d y}{d x} & =\frac{d}{d x}(x \cdot \cos x) \\
& =\cos x \cdot \frac{d}{d x}(x)+x \frac{d}{d x}(\cos x) \\
& =\cos x \cdot 1+x(-\sin x) \\
& =\cos x-x \sin x
\end{aligned}
$$

Therefore,

$$
\begin{aligned}
\frac{d^{2} y}{d x^{2}} & =\frac{d}{d x}[\cos x-x \sin x] \\
& =\frac{d}{d x}(\cos x)-\frac{d}{d x}(x \sin x) \\
& =-\sin x-\left[\sin x \cdot \frac{d}{d x}(x)+x \cdot \frac{d}{d x}(\sin x)\right] \\
& =-\sin x-(\sin x+x \cos x) \\
& =-(x \cos x+2 \sin x)
\end{aligned}
$$
:::

:::

:::question{number="4" kind="exercise" id="q_5.7.4" topic="Second order derivative: log x"}
#### Question 4

:::prompt
$\log x$
:::

:::solution{label="Solution"}
Let $y=\log x$
Then,

$$
\begin{aligned}
\frac{d y}{d x} & =\frac{d}{d x}(\log x) \\
& =\frac{1}{x}
\end{aligned}
$$

Therefore,

$$
\begin{aligned}
\frac{d^{2} y}{d x^{2}} & =\frac{d}{d x}\left(\frac{1}{x}\right) \\
& =\frac{-1}{x^{2}}
\end{aligned}
$$
:::

:::

:::question{number="5" kind="exercise" id="q_5.7.5" topic="Second order derivative: x^3 log x"}
#### Question 5

:::prompt
$x^{3} \log x$
:::

:::solution{label="Solution"}
Let $y=x^{3} \log x$

Then,

$$
\begin{aligned}
\frac{d y}{d x} & =\frac{d}{d x}\left[x^{3} \log x\right] \\
& =\log x \cdot \frac{d}{d x}\left(x^{3}\right)+x^{3} \cdot \frac{d}{d x}(\log x) \\
& =\log x \cdot 3 x^{2}+x^{3} \cdot \frac{1}{x}=\log x \cdot 3 x^{2}+x^{2} \\
& =x^{2}(1+3 \log x)
\end{aligned}
$$

Therefore,

$$
\begin{aligned}
\frac{d^{2} y}{d x^{2}} & =\frac{d}{d x}\left[x^{2}(1+3 \log x)\right] \\
& =(1+3 \log x) \cdot \frac{d}{d x}\left(x^{2}\right)+x^{2} \frac{d}{d x}(1+3 \log x) \\
& =(1+3 \log x) \cdot 2 x+x^{2} \cdot \frac{3}{x} \\
& =2 x+6 \log x+3 x \\
& =5 x+6 x \log x \\
& =x(5+6 \log x)
\end{aligned}
$$
:::

:::

:::question{number="6" kind="exercise" id="q_5.7.6" topic="Second order derivative: e^x sin 5 x"}
#### Question 6

:::prompt
$e^{x} \sin 5 x$
:::

:::solution{label="Solution"}
Let $y=e^{x} \sin 5 x$
Then,

$$
\begin{aligned}
\frac{d y}{d x} & =\frac{d}{d x}\left(e^{x} \sin 5 x\right) \\
& =\sin 5 x \times \frac{d}{d x}\left(e^{x}\right)+e^{x} \frac{d}{d x}(\sin 5 x) \\
& =\sin 5 x \cdot e^{x}+e^{x} \cdot \cos 5 x \cdot \frac{d}{d x}(5 x) \\
& =e^{x} \sin 5 x+e^{x} \cos 5 x \cdot 5 \\
& =e^{x}(\sin 5 x+5 \cos 5 x)
\end{aligned}
$$

Therefore,

$$
\begin{aligned}
\frac{d^{2} y}{d x^{2}} & =\frac{d}{d x}\left[e^{x}(\sin 5 x+5 \cos 5 x)\right] \\
& =(\sin 5 x+5 \cos 5 x) \cdot \frac{d}{d x}\left(e^{x}\right)+e^{x} \cdot \frac{d}{d x}(\sin 5 x+5 \cos 5 x) \\
& =(\sin 5 x+5 \cos 5 x) e^{x}+e^{x}\left[\cos 5 x \cdot \frac{d}{d x}(5 x)+5(-\sin 5 x) \cdot \frac{d}{d x}(5 x)\right] \\
& =e^{x}(\sin 5 x+5 \cos 5 x)+e^{x}(5 \cos 5 x-25 \sin 5 x) \\
& =e^{x}(10 \cos 5 x-24 \sin 5 x) \\
& =2 e^{x}(5 \cos 5 x-12 \sin 5 x)
\end{aligned}
$$
:::

:::

:::question{number="7" kind="exercise" id="q_5.7.7" topic="Second order derivative: e^6 x cos 3 x"}
#### Question 7

:::prompt
$e^{6 x} \cos 3 x$
:::

:::solution{label="Solution"}
Let $y=e^{6 x} \cos 3 x$
Then,

$$
\begin{aligned}
\frac{d y}{d x} & =\frac{d}{d x}\left(e^{6 x} \cos 3 x\right)=\cos 3 x \cdot \frac{d}{d x}\left(e^{6 x}\right)+e^{6 x} \cdot \frac{d}{d x}(\cos 3 x) \\
& =\cos 3 x \cdot e^{6 x} \cdot \frac{d}{d x}(6 x)+e^{6 x} \cdot(-\sin 3 x) \cdot \frac{d}{d x}(3 x) \\
& =6 e^{6 x} \cos 3 x-3 e^{6 x} \sin 3 x
\end{aligned}
$$

Therefore,

$$
\begin{aligned}
\frac{d^{2} y}{d x^{2}} & =\frac{d}{d x}\left(6 e^{6 x} \cos 3 x-3 e^{6 x} \sin 3 x\right)=6 \cdot \frac{d}{d x}\left(e^{6 x} \cos 3 x\right)-3 \cdot \frac{d}{d x}\left(e^{6 x} \sin 3 x\right) \\
& =6 \cdot\left[6 e^{6 x} \cos 3 x-3 e^{6 x} \sin 3 x\right]-3 \cdot\left[\sin 3 x \cdot \frac{d}{d x}\left(e^{6 x}\right)+e^{6 x} \cdot \frac{d}{d x}(\sin 3 x)\right] \quad \quad[\text { using (1) }] \\
& =36 e^{6 x} \cos 3 x-18 e^{6 x} \sin 3 x-3\left[\sin 3 x \cdot e^{6 x} \cdot 6+e^{6 x} \cdot \cos 3 x \cdot 3\right] \\
& =36 e^{6 x} \cos 3 x-18 e^{6 x} \sin 3 x-18 e^{6 x} \sin 3 x-9 e^{6 x} \cos 3 x \\
& =27 e^{6 x} \cos 3 x-36 e^{6 x} \sin 3 x \\
& =9 e^{6 x}(3 \cos 3 x-4 \sin 3 x)
\end{aligned}
$$
:::

:::

:::question{number="8" kind="exercise" id="q_5.7.8" topic="Second order derivative: tan ^-1 x"}
#### Question 8

:::prompt
$\tan ^{-1} x$
:::

:::solution{label="Solution"}
Let $y=\tan ^{-1} x$
Then,

$$
\begin{aligned}
\frac{d y}{d x} & =\frac{d}{d x}\left(\tan ^{-1} x\right) \\
& =\frac{1}{1+x^{2}}
\end{aligned}
$$

Therefore,

$$
\begin{aligned}
\frac{d^{2} y}{d x^{2}} & =\frac{d}{d x}\left(\frac{1}{1+x^{2}}\right)=\frac{d}{d x}\left(1+x^{2}\right)^{-1} \\
& =(-1) \cdot\left(1+x^{2}\right)^{-2} \cdot \frac{d}{d x}\left(1+x^{2}\right)=\frac{-1}{\left(1+x^{2}\right)^{2}} \times 2 x \\
& =\frac{-2 x}{\left(1+x^{2}\right)^{2}}
\end{aligned}
$$
:::

:::

:::question{number="9" kind="exercise" id="q_5.7.9" topic="Second order derivative: log (log x)"}
#### Question 9

:::prompt
$\log (\log x)$
:::

:::solution{label="Solution"}
Consider, $y=\log (\log x)$
Then,

$$
\begin{aligned}
\frac{d y}{d x} & =\frac{d}{d x}[\log (\log x)] \\
& =\frac{1}{\log x} \cdot \frac{d}{d x}(\log x) \\
& =\frac{1}{\log x} \cdot \frac{1}{x}=(x \log x)^{-1}
\end{aligned}
$$

Therefore,

$$
\begin{aligned}
\frac{d^{2} y}{d x^{2}} & =\frac{d}{d x}\left[(x \log x)^{-1}\right] \\
& =(-1) \cdot(x \log x)^{-2} \frac{d}{d x}(x \log x) \\
& =\frac{-1}{(x \log x)^{2}} \cdot\left[\log x \cdot \frac{d}{d x}(x)+x \cdot \frac{d}{d x}(\log x)\right] \\
& =\frac{-1}{(x \log x)^{2}} \cdot\left[\log x \cdot 1+x \cdot \frac{1}{x}\right] \\
& =\frac{-(1+\log x)}{(x \log x)^{2}}
\end{aligned}
$$
:::

:::

:::question{number="10" kind="exercise" id="q_5.7.10" topic="Second order derivative: sin (log x)"}
#### Question 10

:::prompt
$\sin (\log x)$
:::

:::solution{label="Solution"}
Let $y=\sin (\log x)$
Then,

$$
\begin{aligned}
\frac{d y}{d x} & =\frac{d}{d x}[\sin x(\log x)] \\
& =\cos (\log x) \cdot \frac{d}{d x}(\log x) \\
& =\frac{\cos (\log x)}{x}
\end{aligned}
$$

Therefore,

$$
\begin{aligned}
\frac{d^{2} y}{d x^{2}} & =\frac{d}{d x}\left[\frac{\cos (\log x)}{x}\right] \\
& =\frac{x \cdot \frac{d}{d x}[\cos (\log x)]-\cos (\log x) \cdot \frac{d}{d x}(x)}{x^{2}}
\end{aligned}
$$

$$
\begin{aligned}
\frac{d^{2} y}{d x^{2}} & =\frac{x\left[-\sin (\log x) \cdot \frac{d}{d x}(\log x)\right]-\cos (\log x) \cdot 1}{x^{2}} \\
& =\frac{-x \sin (\log x) \cdot \frac{1}{x}-\cos (\log x)}{x^{2}} \\
& =\frac{-[\sin (\log x)+\cos (\log x)]}{x^{2}}
\end{aligned}
$$
:::

:::

:::question{number="11" kind="exercise" id="q_5.7.11" topic="Second order derivative: y=5 cos x-3 sin x"}
#### Question 11

:::prompt
If $y=5 \cos x-3 \sin x$, prove that $\frac{d^{2} y}{d x^{2}}+y=0$
:::

:::solution{label="Solution"}
Given, $y=5 \cos x-3 \sin x$
Then,

$$
\begin{aligned}
\frac{d y}{d x} & =\frac{d}{d x}(5 \cos x)-\frac{d}{d x}(3 \sin x) \\
& =5 \frac{d}{d x}(\cos x)-3 \frac{d}{d x}(\sin x) \\
& =5(-\sin x)-3 \cos x \\
& =-(5 \sin x+3 \cos x)
\end{aligned}
$$

Therefore,

$$
\begin{aligned}
\frac{d^{2} y}{d x^{2}} & =\frac{d}{d x}[-(5 \sin x+3 \cos x)] \\
& =-\left[5 \cdot \frac{d}{d x}(\sin x)+3 \cdot \frac{d}{d x}(\cos x)\right] \\
& =-[5 \cos x+3(-\sin x)] \\
& =-[5 \cos x-3 \sin x] \\
& =-y
\end{aligned}
$$

Thus, $\frac{d^{2} y}{d x^{2}}+y=0$
Hence proved.
:::

:::

:::question{number="12" kind="exercise" id="q_5.7.12" topic="Second order derivative: y=cos ^-1 x"}
#### Question 12

:::prompt
If $y=\cos ^{-1} x$, Find $\frac{d^{2} y}{d x^{2}}$ in terms of $y$ alone.
:::

:::solution{label="Solution"}
Given, $y=\cos ^{-1} x$
Then,

$$
\begin{aligned}
\frac{d y}{d x} & =\frac{d}{d x}\left(\cos ^{-1} x\right) \\
& =\frac{-1}{\sqrt{1-x^{2}}} \\
& =-\left(1-x^{2}\right)^{\frac{-1}{2}}
\end{aligned}
$$

Therefore,

$$
\begin{aligned}
\frac{d^{2} y}{d x^{2}} & =\frac{d}{d x}\left[-\left(1-x^{2}\right)^{\frac{-1}{2}}\right] \\
& =-\left(-\frac{1}{2}\right) \cdot\left(1-x^{2}\right)^{\frac{-3}{2}} \cdot \frac{d}{d x}\left(1-x^{2}\right) \\
& =\frac{1}{2 \sqrt{\left(1-x^{2}\right)^{3}}} \times(-2 x) \\
\frac{d^{2} y}{d x^{2}} & =\frac{-x}{\sqrt{\left(1-x^{2}\right)^{3}}}
\end{aligned}
$$

But we need to calculate $\frac{d^{2} y}{d x^{2}}$ in terms of $y$

$$
\begin{aligned}
& \Rightarrow y=\cos ^{-1} x \\
& \Rightarrow x=\cos y
\end{aligned}
$$

Putting $x=\cos y$ in equation (1), we get

$$
\begin{aligned}
\frac{d^{2} y}{d x^{2}} & =\frac{-\cos y}{\sqrt{\left(1-\cos ^{2} y\right)^{3}}} \\
& =\frac{-\cos y}{\sqrt{\left(\sin ^{2} y\right)^{3}}} \\
& =\frac{-\cos y}{\sin ^{3} y} \\
& =\frac{-\cos y}{\sin y} \times \frac{1}{\sin ^{2} y} \\
& =-\cot y \cdot \operatorname{cosec}^{2} y
\end{aligned}
$$
:::

:::

:::question{number="13" kind="exercise" id="q_5.7.13" topic="Second order derivative: y=3 cos (log x)+4 sin (log..."}
#### Question 13

:::prompt
If $y=3 \cos (\log x)+4 \sin (\log x)$, show that $x^{2} y_{2}+x y_{1}+y=0$
:::

:::solution{label="Solution"}
Given, $y=3 \cos (\log x)+4 \sin (\log x)$

Then,

$$
\begin{aligned}
y_{1} & =3 \cdot \frac{d}{d x}[\cos (\log x)]+4 \cdot \frac{d}{d x}[\sin (\log x)] \\
& =3 \cdot\left[-\sin (\log x) \cdot \frac{d}{d x}(\log x)\right]+4 \cdot\left[\cos (\log x) \cdot \frac{d}{d x}(\log x)\right] \\
& =\frac{-3 \sin (\log x)}{x}+\frac{4 \cos (\log x)}{x} \\
& =\frac{4 \cos (\log x)-3 \sin (\log x)}{x}
\end{aligned}
$$

Therefore,

$$
\begin{aligned}
y_{2} & =\frac{d}{d x}\left(\frac{4 \cos (\log x)-3 \sin (\log x)}{x}\right) \\
& =\frac{x \cdot\{4 \cos (\log x)-3 \sin (\log x)\}^{\prime}-\{4 \cos (\log x)-3 \sin (\log x)\}\{x\}^{\prime}}{x^{2}} \\
& =\frac{x \cdot\left[4\{\cos (\log x)\}^{\prime}-\{3 \sin (\log x)\}^{\prime}\right]-\{4 \cos (\log x)-3 \sin (\log x)\} \cdot 1}{x^{2}} \\
& =\frac{x \cdot\left[-4 \sin (\log x) \cdot(\log x)^{\prime}-3 \cos (\log x) \cdot(\log x)^{\prime}\right]-4 \cos (\log x)+3 \sin (\log x)}{x^{2}} \\
& =\frac{x \cdot\left[-4 \sin (\log x) \frac{1}{x}-3 \cos (\log x) \frac{1}{x}\right]-4 \cos (\log x)+3 \sin (\log x)}{x^{2}} \\
& =\frac{-4 \sin (\log x)-3 \cos (\log x)-4 \cos (\log x)+3 \sin (\log x)}{x^{2}} \\
& =\frac{-\sin (\log x)-7 \cos (\log x)}{x^{2}}
\end{aligned}
$$

Thus,

$$
\begin{aligned}
x^{2} y_{2}+x y_{1}+y & =\left[\begin{array}{c}
x^{2}\left(\frac{-\sin (\log x)-7 \cos (\log x)}{x^{2}}\right)+x\left(\frac{4 \cos (\log x)-3 \sin (\log x)}{x}\right) \\
+3 \cos (\log x)+4 \sin (\log x)
\end{array}\right] \\
& =\left[\begin{array}{c}
-\sin (\log x)-7 \cos (\log x)+4 \cos (\log x)-3 \sin (\log x) \\
+3 \cos (\log x)+4 \sin (\log x)
\end{array}\right] \\
& =0
\end{aligned}
$$

Hence proved.
:::

:::

:::question{number="14" kind="exercise" id="q_5.7.14" topic="Second order derivative: y=A e^m x+B e^n x"}
#### Question 14

:::prompt
If $y=\mathrm{A} e^{m x}+\mathrm{B} e^{n x}$, show that $\frac{d^{2} y}{d x^{2}}-(m+n) \frac{d y}{d x}+m n y=0$
:::

:::solution{label="Solution"}
Given, $y=A e^{m x}+B e^{m x}$
Then,

$$
\begin{aligned}
\frac{d y}{d x} & =A \cdot \frac{d}{d x}\left(e^{m x}\right)+B \cdot \frac{d}{d x}\left(e^{n x}\right) \\
& =A \cdot e^{m x} \cdot \frac{d}{d x}(m x)+B \cdot e^{n x} \cdot \frac{d}{d x}(n x) \\
& =A m e^{m x}+B n e^{n x}
\end{aligned}
$$

Therefore,

$$
\begin{aligned}
\frac{d^{2} y}{d x^{2}} & =\frac{d}{d x}\left(A m e^{m x}+B n e^{n x}\right) \\
& =A m \cdot \frac{d}{d x}\left(e^{m x}\right)+B n \cdot \frac{d}{d x}\left(e^{m x}\right) \\
& =A m \cdot e^{m x} \cdot \frac{d}{d x}(m x)+B n \cdot e^{n x} \cdot \frac{d}{d x}(n x) \\
& =A m^{2} e^{m x}+B n^{2} e^{n x}
\end{aligned}
$$

Thus,

$$
\begin{aligned}
\frac{d^{2} y}{d x^{2}}-(m+n) \frac{d y}{d x}+m n y & =A m^{2} e^{m x}+B n^{2} e^{n x}-(m+n) \cdot\left(A m e^{m x}+B n e^{n x}\right)+m n\left(A e^{m x}+B e^{n x}\right) \\
& =A m^{2} e^{m x}+B n^{2} e^{n x}-A m^{2} e^{m x}-B m n e^{n x}-A m n e^{m x}-B n^{2} e^{n x}+A m n e^{m x}+B m n e^{n x} \\
& =0
\end{aligned}
$$

Hence proved.
:::

:::

:::question{number="15" kind="exercise" id="q_5.7.15" topic="Second order derivative: y=500 e^7 x+600 e^-7 x"}
#### Question 15

:::prompt
If $y=500 e^{7 x}+600 e^{-7 x}$, show that $\frac{d^{2} y}{d x^{2}}=49 y$
:::

:::solution{label="Solution"}
Given, $y=500 e^{7 x}+600 e^{-7 x}$
Then,

$$
\begin{aligned}
\frac{d y}{d x} & =500 \cdot \frac{d}{d x}\left(e^{7 x}\right)+600 \cdot \frac{d}{d x}\left(e^{-7 x}\right) \\
& =500 \cdot e^{7 x} \cdot \frac{d}{d x}(7 x)+600 \cdot e^{-7 x} \cdot \frac{d}{d x}(-7 x) \\
& =3500 e^{7 x}-4200 e^{-7 x}
\end{aligned}
$$

Therefore,

$$
\begin{aligned}
\frac{d^{2} y}{d x^{2}} & =3500 e^{7 x} \cdot \frac{d}{d x}\left(e^{7 x}\right)-4200 \cdot \frac{d}{d x}\left(e^{-7 x}\right) \\
& =3500 \cdot e^{7 x} \cdot \frac{d}{d x}(7 x)-4200 \cdot e^{-7 x} \cdot \frac{d}{d x}(-7 x) \\
& =7 \times 3500 \cdot e^{7 x}+7 \times 4200 \cdot e^{-7 x} \\
& =49 \times 500 \cdot e^{7 x}+49 \times 600 e^{-7 x} \\
& =49\left(500 e^{7 x}+600 e^{-7 x}\right) \\
& =49 y
\end{aligned}
$$

Hence proved.
:::

:::

:::question{number="16" kind="exercise" id="q_5.7.16" topic="Second order derivative: e^y(x+1)=1"}
#### Question 16

:::prompt
If $e^{y}(x+1)=1$, show that $\frac{d^{2} y}{d x^{2}}=\left(\frac{d y}{d x}\right)^{2}$
:::

:::solution{label="Solution"}
Given, $e^{y}(x+1)=1$

$$
\begin{aligned}
& \Rightarrow e^{y}(x+1)=1 \\
& \Rightarrow e^{y}=\frac{1}{x+1}
\end{aligned}
$$

Taking $\log$ on both sides, we get

$$
y=\log \frac{1}{(x+1)}
$$

Differentiating with respect to $x$, we get

$$
\begin{aligned}
\frac{d y}{d x} & =(x+1) \frac{d}{d x}\left(\frac{1}{x+1}\right) \\
& =(x+1) \cdot \frac{-1}{(x+1)^{2}} \\
& =\frac{-1}{x+1}
\end{aligned}
$$

Therefore,

$$
\begin{aligned}
\frac{d^{2} y}{d x^{2}} & =\frac{d}{d x}\left(\frac{-1}{x+1}\right)=-\left(\frac{-1}{(x+1)^{2}}\right) \\
& =\frac{1}{(x+1)^{2}}=\left(\frac{-1}{x+1}\right)^{2} \\
& =\left(\frac{d y}{d x}\right)^{2}
\end{aligned}
$$

Hence proved.
:::

:::

:::question{number="17" kind="exercise" id="q_5.7.17" topic="Second order derivative: y=(tan ^-1 x)^2"}
#### Question 17

:::prompt
If $y=\left(\tan ^{-1} x\right)^{2}$, show that $\left(x^{2}+1\right)^{2} y_{2}+2 x\left(x^{2}+1\right) y_{1}=2$
:::

:::solution{label="Solution"}
Given, $y=\left(\tan ^{-1} x\right)^{2}$

Then,

$$
\begin{aligned}
& \Rightarrow y_{1}=2 \tan ^{-1} x \frac{d}{d x}\left(\tan ^{-1} x\right) \\
& \Rightarrow y_{1}=2 \tan ^{-1} x \cdot\left(\frac{1}{1+x^{2}}\right) \\
& \Rightarrow\left(1+x^{2}\right) y_{1}=2 \tan ^{-1} x
\end{aligned}
$$

Again, differentiating with respect to $x$, we get

$$
\begin{aligned}
& \Rightarrow\left(1+x^{2}\right) y_{2}+2 x y_{1}=2\left(\frac{1}{1+x^{2}}\right) \\
& \Rightarrow\left(1+x^{2}\right)^{2} y_{2}+2 x\left(1+x^{2}\right) y_{1}=2
\end{aligned}
$$

Hence proved.
:::

:::

## Additional Questions

:::question{number="1" kind="additional_exercise" id="q_5.misc.1" topic="Misc: (3 x^2-9 x+5)^9"}
#### Additional Question 1

:::prompt
$\left(3 x^{2}-9 x+5\right)^{9}$
:::

:::solution{label="Solution"}
Let $y=\left(3 x^{2}-9 x+5\right)^{9}$

Using chain rule, we get

$$
\begin{aligned}
\frac{d y}{d x} & =\frac{d}{d x}\left(3 x^{2}-9 x+5\right)^{9} \\
& =9\left(3 x^{2}-9 x+5\right)^{8} \cdot \frac{d}{d x}\left(3 x^{2}-9 x+5\right) \\
& =9\left(3 x^{2}-9 x+5\right)^{8} \cdot(6 x-9) \\
& =9\left(3 x^{2}-9 x+5\right)^{8} \cdot 3(2 x-3) \\
& =27\left(3 x^{2}-9 x+5\right)^{8}(2 x-3)
\end{aligned}
$$
:::

:::

:::question{number="2" kind="additional_exercise" id="q_5.misc.2" topic="Misc: sin ^3 x+cos ^6 x"}
#### Additional Question 2

:::prompt
$\sin ^{3} x+\cos ^{6} x$
:::

:::solution{label="Solution"}
Let $y=\sin ^{3} x+\cos ^{6} x$

Using chain rule, we get

$$
\begin{aligned}
\frac{d y}{d x} & =\frac{d}{d x}\left(\sin ^{3} x\right)+\frac{d}{d x}\left(\cos ^{6} x\right) \\
& =3 \sin ^{2} x \cdot \frac{d}{d x}(\sin x)+6 \cos ^{5} x \cdot \frac{d}{d x}(\cos x) \\
& =3 \sin ^{2} x \cdot \cos x+6 \cos ^{5} x \cdot(-\sin x) \\
& =3 \sin x \cos x\left(\sin x-2 \cos ^{4} x\right)
\end{aligned}
$$
:::

:::

:::question{number="3" kind="additional_exercise" id="q_5.misc.3" topic="Misc: (5 x)^3 cos 2 x"}
#### Additional Question 3

:::prompt
$(5 x)^{3 \cos 2 x}$
:::

:::solution{label="Solution"}
Let $y=(5 x)^{3 \cos 2 x}$
Taking logarithm on both the sides, we obtain

$$
\log y=3 \cos 2 x \log 5 x
$$

Differentiating both sides with respect to $x$, we get

$$
\begin{aligned}
\frac{1}{y} \frac{d y}{d x} & =3\left[\log 5 x \cdot \frac{d}{d x}(\cos 2 x)+\cos 2 x \cdot \frac{d}{d x}(\log 5 x)\right] \\
\frac{d y}{d x} & =3 y\left[\log 5 x \cdot(-\sin 2 x) \cdot \frac{d}{d x}(2 x)+\cos 2 x \cdot \frac{1}{5 x} \cdot \frac{d}{d x}(5 x)\right] \\
& =3 y\left[-2 \sin 2 x \cdot \log 5 x+\frac{\cos 2 x}{x}\right] \\
& =y\left[\frac{3 \cos 2 x}{x}-6 \sin 2 x \log 5 x\right] \\
& =(5 x)^{3 \cos 2 x}\left[\frac{3 \cos 2 x}{x}-6 \sin 2 x \log 5 x\right]
\end{aligned}
$$
:::

:::

:::question{number="4" kind="additional_exercise" id="q_5.misc.4" topic="Misc: sin ^-1(x sqrt x), 0 x 1"}
#### Additional Question 4

:::prompt
$\sin ^{-1}(x \sqrt{x}), 0 \leq x \leq 1$
:::

:::solution{label="Solution"}
Let $y=\sin ^{-1}(x \sqrt{x})$

Using chain rule, we get

$$
\begin{aligned}
\frac{d y}{d x} & =\frac{d}{d x} \sin ^{-1}(x \sqrt{x}) \\
& =\frac{1}{\sqrt{1-(x \sqrt{x})^{2}}} \times \frac{d}{d x}(x \sqrt{x}) \\
& =\frac{1}{\sqrt{1-x^{3}}} \cdot \frac{d}{d x}\left(x^{\frac{3}{2}}\right) \\
& =\frac{1}{\sqrt{1-x^{3}}} \cdot \frac{3}{2} \cdot x^{\frac{1}{2}} \\
& =\frac{3 \sqrt{x}}{2 \sqrt{1-x^{3}}} \\
& =\frac{3}{2} \sqrt{\frac{x}{1-x^{3}}}
\end{aligned}
$$
:::

:::

:::question{number="5" kind="additional_exercise" id="q_5.misc.5" topic="Misc: cos ^-1 x/2sqrt 2 x+7,-2<x..."}
#### Additional Question 5

:::prompt
$\frac{\cos ^{-1} \frac{x}{2}}{\sqrt{2 x+7}},-2<x<2$
:::

:::solution{label="Solution"}
Let $y=\frac{\cos ^{-1} \frac{x}{2}}{\sqrt{2 x+7}}$

Using quotient rule, we get

$$
\begin{aligned}
\frac{d y}{d x} & =\frac{\sqrt{2 x+7} \cdot \frac{d}{d x}\left(\cos ^{-1} \frac{x}{2}\right)-\left(\cos ^{-1} \frac{x}{2}\right) \cdot \frac{d}{d x}(\sqrt{2 x+7})}{(\sqrt{2 x+7})^{2}} \\
& =\frac{\sqrt{2 x+7}\left[\frac{-1}{\sqrt{1-\left(\frac{x}{2}\right)^{2}}} \cdot \frac{d}{d x}\left(\frac{x}{2}\right)\right]-\left(\cos ^{-1} \frac{x}{2}\right) \cdot \frac{1}{2 \sqrt{2 x+7}} \cdot \frac{d}{d x}(2 x+7)}{2 x+7} \\
& =\frac{\sqrt{2 x+7} \cdot \frac{-1}{\sqrt{4-x^{2}}}-\left(\cos ^{-1} \frac{x}{2}\right) \cdot \frac{2}{2 \sqrt{2 x+7}}}{2 x+7} \\
& =\frac{-\sqrt{2 x+7}}{\left(\sqrt{4-x^{2}}\right) \cdot(2 x+7)}-\frac{\cos ^{-1} \frac{x}{2}}{(\sqrt{2 x+7})(2 x+7)} \\
& =-\left[\frac{1}{\sqrt{4-x^{2}} \sqrt{2 x+7}}+\frac{\cos ^{-1} \frac{x}{2}}{(2 x+7)^{\frac{3}{2}}}\right]
\end{aligned}
$$
:::

:::

:::question{number="6" kind="additional_exercise" id="q_5.misc.6" topic="Misc: cot ^-1[sqrt 1+sin x+sqrt..."}
#### Additional Question 6

:::prompt
$\cot ^{-1}\left[\frac{\sqrt{1+\sin x}+\sqrt{1-\sin x}}{\sqrt{1+\sin x}-\sqrt{1-\sin x}}\right], 0<x<\frac{\pi}{2}$
:::

:::solution{label="Solution"}
$$
y=\cot ^{-1}\left[\frac{\sqrt{1+\sin x}+\sqrt{1-\sin x}}{\sqrt{1+\sin x}-\sqrt{1-\sin x}}\right]
$$

Then,

$$
\begin{aligned}
\frac{\sqrt{1+\sin x}+\sqrt{1-\sin x}}{\sqrt{1+\sin x}-\sqrt{1-\sin x}} & =\frac{(\sqrt{1+\sin x}+\sqrt{1-\sin x})^{2}}{(\sqrt{1+\sin x}-\sqrt{1-\sin x})(\sqrt{1+\sin x}+\sqrt{1-\sin x})} \\
& =\frac{(1+\sin x)+(1-\sin x)+2 \sqrt{(1+\sin x)(1-\sin x)}}{(1+\sin x)-(1-\sin x)} \\
& =\frac{2+2 \sqrt{1-\sin ^{2} x}}{2 \sin x}=\frac{1+\cos x}{\sin x} \\
& =\frac{1+2 \cos ^{2} \frac{x}{2}-1}{2 \sin \frac{x}{2} \cos \frac{x}{2}}=\frac{2 \cos ^{2} \frac{x}{2}}{2 \sin \frac{x}{2} \cos \frac{x}{2}} \\
& =\cot \frac{x}{2}
\end{aligned}
$$

Therefore, equation (1) becomes,

$$
\begin{aligned}
& y=\cot ^{-1}\left(\cot \frac{x}{2}\right) \\
& \Rightarrow y=\frac{x}{2}
\end{aligned}
$$

Thus,

$$
\begin{aligned}
& \Rightarrow \frac{d y}{d x}=\frac{1}{2} \frac{d}{d x}(x) \\
& =\frac{1}{2}
\end{aligned}
$$
:::

:::

:::question{number="7" kind="additional_exercise" id="q_5.misc.7" topic="Misc: (log x)^log x, x>1"}
#### Additional Question 7

:::prompt
$(\log x)^{\log x}, x>1$
:::

:::solution{label="Solution"}
Let $y=(\log x)^{\log x}$
Taking logarithm on both the sides, we obtain

$$
\log y=\log x \cdot \log (\log x)
$$

Differentiating both sides with respect to $x$, we obtain

$$
\begin{aligned}
& \Rightarrow \frac{1}{y} \frac{d y}{d x}=\frac{d}{d x}[\log x \cdot \log (\log x)] \\
& \Rightarrow \frac{1}{y} \frac{d y}{d x}=\log (\log x) \cdot \frac{d}{d x}(\log x)+\log x \cdot \frac{d}{d x}[\log (\log x)] \\
& \Rightarrow \frac{d y}{d x}=y\left[\log (\log x) \cdot \frac{1}{x}+\log x \cdot \frac{1}{\log x} \cdot \frac{d}{d x}(\log x)\right] \\
& \Rightarrow \frac{d y}{d x}=y\left[\frac{1}{x} \cdot \log (\log x)+\frac{1}{x}\right] \\
& \Rightarrow \frac{d y}{d x}=(\log x)^{\log x}\left[\frac{1}{x}+\frac{\log (\log x)}{x}\right]
\end{aligned}
$$
:::

:::

:::question{number="8" kind="additional_exercise" id="q_5.misc.8" topic="Misc: cos (a cos x+b sin x)"}
#### Additional Question 8

:::prompt
$\cos (a \cos x+b \sin x)$, for some constant $a$ and $b$.
:::

:::solution{label="Solution"}
Let $y=\cos (a \cos x+b \sin x)$

Using chain rule, we get

$$
\begin{aligned}
\frac{d y}{d x} & =\frac{d}{d x} \cos (a \cos x+b \sin x) \\
& =-\sin (a \cos x+b \sin x) \cdot \frac{d}{d x}(a \cos x+b \sin x) \\
& =-\sin (a \cos x+b \sin x) \cdot[a(-\sin x)+b \cos x] \\
& =(a \sin x-b \cos x) \cdot \sin (a \cos x+b \sin x)
\end{aligned}
$$
:::

:::

:::question{number="9" kind="additional_exercise" id="q_5.misc.9" topic="Misc: (sin x-cos x)^(sin x-cos x..."}
#### Additional Question 9

:::prompt
$(\sin x-\cos x)^{(\sin x-\cos x)}, \frac{\pi}{4}<x<\frac{3 \pi}{4}$
:::

:::solution{label="Solution"}
Let $y=(\sin x-\cos x)^{(\sin x-\cos x)}$
Taking log on both the sides, we obtain

$$
\begin{aligned}
\log y & =\log \left[(\sin x-\cos x)^{(\sin x-\cos x)}\right] \\
& =(\sin x-\cos x) \log (\sin x-\cos x)
\end{aligned}
$$

Differentiating both sides with respect to $x$, we obtain

$$
\begin{aligned}
& \frac{1}{y} \frac{d y}{d x}=\frac{d}{d x}[(\sin x-\cos x) \log (\sin x-\cos x)] \\
& \Rightarrow \frac{1}{y} \frac{d y}{d x}=\log (\sin x-\cos x) \cdot \frac{d}{d x}(\sin x-\cos x)+(\sin x-\cos x) \cdot \frac{d}{d x} \log (\sin x-\cos x) \\
& \Rightarrow \frac{1}{y} \frac{d y}{d x}=\log (\sin x-\cos x) \cdot(\cos x+\sin x)+(\sin x-\cos x) \cdot \frac{1}{(\sin x-\cos x)} \cdot \frac{d}{d x}(\sin x-\cos x) \\
& \Rightarrow \frac{d y}{d x}=(\sin x-\cos x)^{(\sin x-\cos x)}[(\cos x+\sin x) \cdot \log (\sin x-\cos x)+(\cos x+\sin x)] \\
& \Rightarrow \frac{d y}{d x}=(\sin x-\cos x)^{(\sin x-\cos x)}(\cos x+\sin x)[1+\log (\sin x-\cos x)]
\end{aligned}
$$
:::

:::

:::question{number="10" kind="additional_exercise" id="q_5.misc.10" topic="Misc: x^x+x^a+a^x+a^a"}
#### Additional Question 10

:::prompt
$x^{x}+x^{a}+a^{x}+a^{a}$, for some fixed $a>0$ and $x>0$
:::

:::solution{label="Solution"}
Let $y=x^{x}+x^{a}+a^{x}+a^{a}$

Also, let $x^{x}=u, x^{a}=v, a^{x}=w$ and $a^{a}=s$
Therefore,

$$
\begin{aligned}
& \Rightarrow y=u+v+w+s \\
& \Rightarrow \frac{d y}{d x}=\frac{d u}{d x}+\frac{d v}{d x}+\frac{d w}{d x}+\frac{d s}{d x}
\end{aligned}
$$

Now, $u=x^{x}$

Taking logarithm on both the sides, we obtain

$$
\begin{aligned}
& \Rightarrow \log u=\log x^{x} \\
& \Rightarrow \log u=x \log x
\end{aligned}
$$

Differentiating both sides with respect to $x$, we obtain

$$
\begin{aligned}
\frac{1}{u} \frac{d u}{d x} & =\log x \cdot \frac{d}{d x}(x)+x \cdot \frac{d}{d x}(\log x) \\
\frac{d u}{d x} & =u\left[\log x \cdot 1+x \cdot \frac{1}{x}\right] \\
& =x^{x}[\log x+1]=x^{x}(1+\log x)
\end{aligned}
$$

Now, $v=x^{a}$
Hence,

$$
\begin{aligned}
\frac{d v}{d x} & =\frac{d}{d x}\left(x^{a}\right) \\
& =a x^{a-1}
\end{aligned}
$$

Now, $w=a^{x}$
Taking logarithm on both the sides, we obtain

$$
\begin{aligned}
& \Rightarrow \log w=\log a^{x} \\
& \Rightarrow \log w=x \log a
\end{aligned}
$$

Differentiating both sides with respect to $x$, we obtain

$$
\begin{aligned}
\frac{1}{w} \frac{d w}{d x} & =\log a \cdot \frac{d}{d x}(x) \\
\frac{d w}{d x} & =w \log a \\
& =a^{x} \log a
\end{aligned}
$$

Now, $s=a^{a}$
Since $a$ is constant, $a^{a}$ is also a constant.
Hence,

$$
\frac{d s}{d x}=0
$$

From (1), (2), (3), (4) and (5), we obtain

$$
\begin{aligned}
\frac{d y}{d x} & =x^{x}(1+\log x)+a x^{a-1}+a^{x} \log a+0 \\
& =x^{x}(1+\log x)+a x^{a-1}+a^{x} \log a
\end{aligned}
$$
:::

:::

:::question{number="11" kind="additional_exercise" id="q_5.misc.11" topic="Misc: x^x^2-3+(x-3)^x^2"}
#### Additional Question 11

:::prompt
$x^{x^{2}-3}+(x-3)^{x^{2}}$, for $x>3$
:::

:::solution{label="Solution"}
Let $y=x^{x^{2}-3}+(x-3)^{x^{2}}$
Also, let $u=x^{x^{2}-3}$ and $v=(x-3)^{x^{2}}$
Therefore,

$$
\begin{aligned}
& y=u+v \\
& \Rightarrow \frac{d y}{d x}=\frac{d u}{d x}+\frac{d v}{d x}
\end{aligned}
$$

Now, $u=x^{x^{2}-3}$
Taking logarithm on both the sides, we obtain

$$
\begin{aligned}
\log u & =\log \left(x^{x^{2}-3}\right) \\
& =\left(x^{2}-3\right) \log x
\end{aligned}
$$

Differentiating both sides with respect to $x$, we obtain

$$
\begin{aligned}
& \frac{1}{u} \frac{d u}{d x}=\log x \cdot \frac{d}{d x}\left(x^{2}-3\right)+\left(x^{2}-3\right) \cdot \frac{d}{d x}(\log x) \\
& \Rightarrow \frac{1}{u} \frac{d u}{d x}=\log x \cdot 2 x+\left(x^{2}-3\right) \cdot \frac{1}{x} \\
& \Rightarrow \frac{d u}{d x}=x^{x^{2}-3}\left\lceil\frac{x^{2}-3}{x}+2 x \log x\right\rceil
\end{aligned}
$$

Now, $v=(x-3)^{x^{2}}$
Taking logarithm on both the sides, we obtain

$$
\begin{aligned}
\log v & =\log (x-3)^{x^{2}} \\
& =x^{2} \log (x-3)
\end{aligned}
$$

Differentiating both sides with respect to $x$, we obtain

$$
\begin{aligned}
& \frac{1}{v} \frac{d v}{d x}=\log (x-3) \cdot \frac{d}{d x}\left(x^{2}\right)+\left(x^{2}\right) \cdot \frac{d}{d x}[\log (x-3)] \\
& \Rightarrow \frac{1}{v} \frac{d v}{d x}=\log (x-3) \cdot 2 x+x^{2} \cdot \frac{1}{x-3} \cdot \frac{d}{d x}(x-3) \\
& \Rightarrow \frac{d v}{d x}=v\left[2 x \log (x-3)+\frac{x^{2}}{x-3} \cdot 1\right] \\
& \Rightarrow \frac{d v}{d x}=(x-3)^{x^{2}}\left[\frac{x^{2}}{x-3}+2 x \log (x-3)\right]
\end{aligned}
$$

From (1), (2), and (3), we obtain

$$
\frac{d y}{d x}=x^{x^{2}-3}\left[\frac{x^{2}-3}{x}+2 x \log x\right]+(x-3)^{x^{2}}\left[\frac{x^{2}}{x-3}+2 x \log (x-3)\right]
$$
:::

:::

:::question{number="12" kind="additional_exercise" id="q_5.misc.12" topic="Misc: d y/d x"}
#### Additional Question 12

:::prompt
Find $\frac{d y}{d x}$, if $y=12(1-\cos t), x=10(t-\sin t),-\frac{\pi}{2}<t<\frac{\pi}{2}$
:::

:::solution{label="Solution"}
The given function is $y=12(1-\cos t), x=10(t-\sin t)$
Hence,

$$
\begin{aligned}
\frac{d x}{d t} & =\frac{d}{d t}[10(t-\sin t)] \\
& =10 \cdot \frac{d}{d t}(t-\sin t) \\
& =10(1-\cos t) \\
\frac{d y}{d t} & =\frac{d}{d t}[12(1-\cos t)] \\
& =12 \cdot \frac{d}{d t}(1-\cos t) \\
& =12 \cdot[0-(-\sin t)] \\
& =12 \sin t
\end{aligned}
$$

Therefore,

$$
\begin{aligned}
\frac{d y}{d x} & =\frac{\frac{d y}{d t}}{\frac{d x}{d t}}=\frac{12 \sin t}{10(1-\cos t)} \\
& =\frac{12.2 \sin \frac{t}{2} \cdot \cos \frac{t}{2}}{10.2 \sin ^{2} \frac{t}{2}} \\
& =\frac{6}{5} \cot \frac{t}{2}
\end{aligned}
$$
:::

:::

:::question{number="13" kind="additional_exercise" id="q_5.misc.13" topic="Misc: d y/d x"}
#### Additional Question 13

:::prompt
Find $\frac{d y}{d x}$, if $y=\sin ^{-1} x+\sin ^{-1} \sqrt{1-x^{2}}, 0<x<1$
:::

:::solution{label="Solution"}
The given function is $y=\sin ^{-1} x+\sin ^{-1} \sqrt{1-x^{2}}$

Hence,

$$
\begin{aligned}
\frac{d y}{d x} & =\frac{d}{d x}\left[\sin ^{-1} x+\sin ^{-1} \sqrt{1-x^{2}}\right] \\
& =\frac{d}{d x}\left(\sin ^{-1} x\right)+\frac{d}{d x}\left(\sin ^{-1} \sqrt{1-x^{2}}\right) \\
\frac{d y}{d x} & =\frac{1}{\sqrt{1-x^{2}}}+\frac{1}{\sqrt{1-\left(\sqrt{1-x^{2}}\right)^{2}}} \cdot \frac{d}{d x}\left(\sqrt{1-x^{2}}\right) \\
& =\frac{1}{\sqrt{1-x^{2}}}+\frac{1}{x} \cdot \frac{1}{2 \sqrt{1-x^{2}}} \cdot \frac{d}{d x}\left(1-x^{2}\right) \\
& =\frac{1}{\sqrt{1-x^{2}}}+\frac{1}{2 x \sqrt{1-x^{2}}}(-2 x) \\
& =\frac{1}{\sqrt{1-x^{2}}}-\frac{1}{\sqrt{1-x^{2}}} \\
& =0
\end{aligned}
$$
:::

:::

:::question{number="14" kind="additional_exercise" id="q_5.misc.14" topic="Misc: x sqrt 1+y+y sqrt 1+x=0"}
#### Additional Question 14

:::prompt
If $x \sqrt{1+y}+y \sqrt{1+x}=0$, for , $-1<x<1$, prove that
$$
\frac{d y}{d x}=-\frac{1}{(1+x)^{2}}
$$
:::

:::solution{label="Solution"}
The given function is $x \sqrt{1+y}+y \sqrt{1+x}=0$

$$
\Rightarrow x \sqrt{1+y}=-y \sqrt{1+x}
$$

Squaring both sides, we obtain

$$
\begin{aligned}
& x^{2}(1+y)=y^{2}(1+x) \\
& \Rightarrow x^{2}+x^{2} y=y^{2}+x y^{2} \\
& \Rightarrow x^{2}-y^{2}=x y^{2}-x^{2} y \\
& \Rightarrow x^{2}-y^{2}=x y(y-x) \\
& \Rightarrow(x+y)(x-y)=x y(y-x) \\
& \Rightarrow x+y=-x y \\
& \Rightarrow(1+x) y=-x \\
& \Rightarrow y=\frac{-x}{(1+x)}
\end{aligned}
$$

Differentiating both sides with respect to $x$, we obtain

$$
\begin{aligned}
\frac{d y}{d x} & =-\left[\frac{(1+x) \frac{d}{d x}(x)-(x) \cdot \frac{d}{d x}(1+x)}{(1+x)^{2}}\right] \\
& =-\frac{(1+x)-x}{(1+x)^{2}} \\
& =-\frac{1}{(1+x)^{2}}
\end{aligned}
$$

Hence proved.
:::

:::

:::question{number="15" kind="additional_exercise" id="q_5.misc.15" topic="Misc: (x-a)^2+(y-b)^2=c^2"}
#### Additional Question 15

:::prompt
If $(x-a)^{2}+(y-b)^{2}=c^{2}$, for some $c>0$, prove that
$$
\frac{\left[1+\left(\frac{d y}{d x}\right)^{2}\right]^{\frac{3}{2}}}{\frac{d^{2} y}{d x^{2}}}
$$
is a constant independent of $a$ and $b$.
:::

:::solution{label="Solution"}
The given function is $(x-a)^{2}+(y-b)^{2}=c^{2}$

Differentiating both sides with respect to $x$, we obtain

$$
\begin{aligned}
& \frac{d}{d x}\left[(x-a)^{2}\right]+\frac{d}{d x}\left[(y-b)^{2}\right]=\frac{d}{d x}\left(c^{2}\right) \\
& \Rightarrow 2(x-a) \cdot \frac{d}{d x}(x-a)+2(y-b) \cdot \frac{d}{d x}(y-b)=0 \\
& \Rightarrow 2(x-a) \cdot 1+2(y-b) \cdot \frac{d y}{d x}=0 \\
& \Rightarrow \frac{d y}{d x}=\frac{-(x-a)}{y-b}
\end{aligned}
$$

Therefore,

$$
\begin{aligned}
\frac{d^{2} y}{d x^{2}} & =\frac{d}{d x}\left[\frac{-(x-a)}{y-b}\right] \\
& =-\left[\frac{(y-b) \cdot \frac{d}{d x}(x-a)-(x-a) \cdot \frac{d}{d x}(y-b)}{(y-b)^{2}}\right] \\
& =-\left[\frac{(y-b)-(x-a) \cdot \frac{d y}{d x}}{(y-b)^{2}}\right] \\
& =-\left[\frac{(y-b)-(x-a) \cdot\left\{\frac{-(x-a)}{y-b}\right\}}{(y-b)^{2}}\right] \quad[\text { Using (1) }] \\
& =-\left[\frac{(y-b)^{2}+(x-a)^{2}}{(y-b)^{3}}\right] \quad
\end{aligned}
$$

Hence,

$$
\begin{aligned}
\frac{\left[1+\left(\frac{d y}{d x}\right)^{2}\right]^{\frac{3}{2}}}{\frac{d^{2} y}{d x^{2}}}= & \frac{\left[1+\frac{(x-a)^{2}}{(y-b)^{2}}\right]^{\frac{3}{2}}}{-\left[\frac{(y-b)^{2}+(x-a)^{2}}{(y-b)^{3}}\right]} \\
= & \frac{\left[\frac{(y-b)^{2}+(x-a)^{2}}{(y-b)^{2}}\right]^{\frac{3}{2}}}{-\left[\frac{(y-b)^{2}+(x-a)^{2}}{(y-b)^{3}}\right]} \\
= & \frac{\left[\frac{c^{2}}{(y-b)^{2}}\right]^{\frac{3}{2}}}{-\frac{c^{2}}{(y-b)^{3}}} \\
= & \frac{\frac{c^{3}}{(y-b)^{3}}}{-\frac{c^{2}}{(y-b)^{3}}} \\
= & -c
\end{aligned}
$$

- $c$ is a constant and is independent of $a$ and $b$.

Hence proved.
:::

:::

:::question{number="16" kind="additional_exercise" id="q_5.misc.16" topic="Misc: cos y=x cos (a+y)"}
#### Additional Question 16

:::prompt
If $\cos y=x \cos (a+y)$, with $\cos a \neq \pm 1$, prove that $\frac{d y}{d x}=\frac{\cos ^{2}(a+y)}{\sin a}$.
:::

:::solution{label="Solution"}
The given function is $\cos y=x \cos (a+y)$
Therefore,

$$
\begin{aligned}
& \Rightarrow \frac{d}{d x}[\cos y]=\frac{d}{d x}[x \cos (a+y)] \\
& \Rightarrow-\sin y \frac{d y}{d x}=\cos (a+y) \cdot \frac{d}{d x}(x)+x \cdot \frac{d}{d x}[\cos (a+y)] \\
& \Rightarrow-\sin y \frac{d y}{d x}=\cos (a+y)+x \cdot[-\sin (a+y)] \frac{d y}{d x} \\
& \Rightarrow[x \sin (a+y)-\sin y] \frac{d y}{d x}=\cos (a+y)
\end{aligned}
$$

Since, $\cos y=x \cos (a+y) \Rightarrow x=\frac{\cos y}{\cos (a+y)}$
Then, equation (1) becomes,

$$
\begin{aligned}
& {\left[\frac{\cos y}{\cos (a+y)} \cdot \sin (a+y)-\sin y\right] \frac{d y}{d x}=\cos (a+y)} \\
& \Rightarrow[\cos y \cdot \sin (a+y)-\sin y \cdot \cos (a+y)] \cdot \frac{d y}{d x}=\cos ^{2}(a+y) \\
& \Rightarrow \sin (a+y-y) \frac{d y}{d x}=\cos ^{2}(a+y) \\
& \Rightarrow \frac{d y}{d x}=\frac{\cos ^{2}(a+y)}{\sin a}
\end{aligned}
$$

Hence proved.
:::

:::

:::question{number="17" kind="additional_exercise" id="q_5.misc.17" topic="Misc: x=a(cos t+t sin t)"}
#### Additional Question 17

:::prompt
If $x=a(\cos t+t \sin t)$ and $y=a(\sin t-t \cos t)$, find $\frac{d^{2} y}{d x^{2}}$.
:::

:::solution{label="Solution"}
The given function is $x=a(\cos t+t \sin t)$ and $y=a(\sin t-t \cos t)$
Therefore,

$$
\begin{aligned}
\frac{d x}{d t} & =a \cdot \frac{d}{d t}(\cos t+t \sin t) \\
& =a\left[-\sin t+\sin t \cdot \frac{d}{d x}(t)+t \cdot \frac{d}{d t}(\sin t)\right] \\
& =a[-\sin t+\sin t+t \cos t] \\
& =a t \cos t
\end{aligned}
$$

$$
\begin{aligned}
\frac{d y}{d t} & =a \cdot \frac{d}{d t}(\sin t-t \cos t) \\
& =a\left[\cos t-\left\{\cos t \cdot \frac{d}{d t}(t)+t \cdot \frac{d}{d t}(\cos t)\right\}\right] \\
& =a[\cos t-\{\cos t-t \sin t\}] \\
& =a t \sin t
\end{aligned}
$$

$$
\begin{aligned}
\frac{d y}{d x} & =\frac{\left(\frac{d y}{d t}\right)}{\left(\frac{d x}{d t}\right)}=\frac{a t \sin t}{a t \cos t}=\tan t \\
\frac{d^{2} y}{d x^{2}} & =\frac{d}{d x}\left(\frac{d y}{d x}\right)=\frac{d}{d x}(\tan t)=\sec ^{2} t \cdot \frac{d t}{d x} \\
& =\sec ^{2} t \cdot \frac{1}{a t \cos t} \quad\left[\frac{d x}{d t}=a t \cos t \Rightarrow \frac{d t}{d x}=\frac{1}{a t \cos t}\right] \\
& =\frac{\sec ^{3} t}{a t}, 0<t<\frac{\pi}{2}
\end{aligned}
$$
:::

:::

:::question{number="18" kind="additional_exercise" id="q_5.misc.18" topic="Misc: f(x)=|x|^3"}
#### Additional Question 18

:::prompt
If $f(x)=|x|^{3}$, show that $f^{\prime \prime}(x)$ exists for all real $x$ and find it.
:::

:::solution{label="Solution"}
It is known that $|x|=\left\{\begin{array}{l}x, \text { if } x \geq 0 \\ -x, \text { if } x<0\end{array}\right.$
Therefore, when $x \geq 0, f(x)=|x|^{3}=x^{3}$

In this case, $f^{\prime}(x)=3 x^{2}$ and hence, $f^{\prime \prime}(x)=6 x$

When $x<0, f(x)=|x|^{3}=(-x)^{3}=-x^{3}$

In this case, $f^{\prime}(x)=-3 x^{2}$ and hence, $f^{\prime \prime}(x)=-6 x$
Thus, for $f(x)=|x|^{3}, f^{\prime \prime}(x)$ exists for all real $x$ and is given by,

$$
f^{\prime \prime}(x)=\left\{\begin{array}{l}
6 x, \text { if } x \geq 0 \\
-6 x, \text { if } x<0
\end{array}\right.
$$
:::

:::

:::question{number="19" kind="additional_exercise" id="q_5.misc.19" topic="Misc: sin (A+B)=sin A cos B+cos..."}
#### Additional Question 19

:::prompt
Using the fact that $\sin (\mathrm{A}+\mathrm{B})=\sin \mathrm{A} \cos \mathrm{B}+\cos \mathrm{A} \sin \mathrm{B}$ and the differentiation, obtain the sum formula for cosines.
:::

:::solution{label="Solution"}
Given, $\sin (A+B)=\sin A \cos B+\cos A \sin B$
Differentiating both sides with respect to $x$, we obtain

$$
\begin{aligned}
& \frac{d}{d x}[\sin (A+B)]=\frac{d}{d x}(\sin A \cos B)+\frac{d}{d x}(\cos A \sin B) \\
& \Rightarrow \cos (A+B) \cdot \frac{d}{d x}(A+B)=\cos B \cdot \frac{d}{d x}(\sin A)+\sin A \cdot \frac{d}{d x}(\cos B)+\sin B \cdot \frac{d}{d x}(\cos A)+\cos A \cdot \frac{d}{d x}(\sin B) \\
& \Rightarrow \cos (A+B) \cdot \frac{d}{d x}(A+B)=\cos B \cdot \cos A \frac{d A}{d x}+\sin A(-\sin B) \frac{d B}{d x}+\sin B(-\sin A) \cdot \frac{d A}{d x}+\cos A \cos B \frac{d B}{d x} \\
& \Rightarrow \cos (A+B) \cdot\left[\frac{d A}{d x}+\frac{d B}{d x}\right]=(\cos A \cos B-\sin A \sin B) \cdot\left[\frac{d A}{d x}+\frac{d B}{d x}\right] \\
& \Rightarrow \cos (A+B)=\cos A \cos B-\sin A \sin B
\end{aligned}
$$
:::

:::

:::question{number="20" kind="additional_exercise" id="q_5.misc.20" topic="Misc: Does there exist a functio..."}
#### Additional Question 20

:::prompt
Does there exist a function which is continuous everywhere but not differentiable at exactly two points? Justify your answer.
:::

:::figure{src="images/fig_5_12.jpg" id="fig_5_12"}
:::

:::solution{label="Solution"}
Consider, $y=\left\{\begin{array}{lr}|x| & -\infty<x \leq 1 \\ 2-x & 1 \leq x \leq \infty\end{array}\right.$
It can be seen from the above graph that the given function is continuous everywhere but not differentiable at exactly two points which are 0 and 1 .
:::

:::

:::question{number="21" kind="additional_exercise" id="q_5.misc.21" topic="Misc: piecewise function"}
#### Additional Question 21

:::prompt
If $y=\left|\begin{array}{ccc}f(x) & g(x) & h(x) \\ l & m & n \\ a & b & c\end{array}\right|$, prove that $\frac{d y}{d x}=\left|\begin{array}{ccc}f^{\prime}(x) & g^{\prime}(x) & h^{\prime}(x) \\ l & m & n \\ a & b & c\end{array}\right|$
:::

:::solution{label="Solution"}
$$
y=\left|\begin{array}{ccc}
f(x) & g(x) & h(x) \\
l & m & n \\
a & b & c
\end{array}\right|
$$

$$
\Rightarrow y=(m c-n b) f(x)-(l c-n a) g(x)+(l b-m a) h(x)
$$

Then,

$$
\begin{aligned}
\frac{d y}{d x} & =\frac{d}{d x}[(m c-n b) f(x)]-\frac{d}{d x}[(l c-n a) g(x)]+\frac{d}{d x}[(l b-m a) h(x)] \\
& =(m c-n b) f^{\prime}(x)-(l c-n a) g^{\prime}(x)+(l b-m a) h^{\prime}(x) \\
& =\left|\begin{array}{ccc}
f^{\prime}(x) & g^{\prime}(x) & h^{\prime}(x) \\
l & m & n \\
a & b & c
\end{array}\right|
\end{aligned}
$$

$$
\frac{d y}{d x}=\left|\begin{array}{ccc}
f^{\prime}(x) & g^{\prime}(x) & h^{\prime}(x) \\
l & m & n \\
a & b & c
\end{array}\right| \text { proved. }
$$
:::

:::

:::question{number="22" kind="additional_exercise" id="q_5.misc.22" topic="Misc: y=e^a cos ^-1 x,-1 x 1"}
#### Additional Question 22

:::prompt
If $y=e^{a \cos ^{-1} x},-1 \leq x \leq 1$, show that $\left(1-x^{2}\right) \frac{d^{2} y}{d x^{2}}-x \frac{d y}{d x}-a^{2} y=0$.
:::

:::solution{label="Solution"}
The given function is $y=e^{a \cos ^{-1} x}$
Taking logarithm on both the sides, we obtain

$$
\begin{aligned}
& \Rightarrow \log y=a \cos ^{-1} x \log e \\
& \Rightarrow \log y=a \cos ^{-1} x
\end{aligned}
$$

Differentiating both sides with respect to $x$, we obtain

$$
\begin{aligned}
& \Rightarrow \frac{1}{y} \frac{d y}{d x}=a \cdot \frac{-1}{\sqrt{1-x^{2}}} \\
& \Rightarrow \frac{d y}{d x}=\frac{-a y}{\sqrt{1-x^{2}}}
\end{aligned}
$$

By squaring both the sides, we obtain

$$
\begin{aligned}
& \Rightarrow\left(\frac{d y}{d x}\right)^{2}=\frac{a^{2} y^{2}}{1-x^{2}} \\
& \Rightarrow\left(1-x^{2}\right)\left(\frac{d y}{d x}\right)^{2}=a^{2} y^{2}
\end{aligned}
$$

Again, differentiating both sides with respect to $x$, we obtain

$$
\begin{aligned}
& \Rightarrow\left(\frac{d y}{d x}\right)^{2} \frac{d}{d x}\left(1-x^{2}\right)+\left(1-x^{2}\right) \times \frac{d}{d x}\left[\left(\frac{d y}{d x}\right)^{2}\right]=a^{2} \frac{d}{d x}\left(y^{2}\right) \\
& \Rightarrow\left(\frac{d y}{d x}\right)^{2}(-2 x)+\left(1-x^{2}\right) \times 2 \frac{d y}{d x} \cdot \frac{d^{2} y}{d x^{2}}=a^{2} \cdot 2 y \cdot \frac{d y}{d x} \\
& \Rightarrow-x \frac{d y}{d x}+\left(1-x^{2}\right) \frac{d^{2} y}{d x^{2}}=a^{2} \cdot y \quad\left[\frac{d y}{d x} \neq 0\right] \\
& \Rightarrow\left(1-x^{2}\right) \frac{d^{2} y}{d x^{2}}-x \frac{d y}{d x}-a^{2} y=0
\end{aligned}
$$

Hence proved.
:::

:::
