---
subject: maths
class: 12
chapter: 1
lang: en
title: "Relations and Functions"
---

# Relations and Functions

## Examples

:::example{number="1.1" kind="example" id="ex_1.1" topic="Empty and universal relations" corrections_applied="1"}
#### Example 1.1

:::prompt
Let A be the set of all students of a boys school. Show that the relation R in A given by $\mathrm{R}=\{(a, b): a$ is sister of $b\}$ is the empty relation and $\mathrm{R}^{\prime}=\{(a, b):$ the difference between heights of $a$ and $b$ is less than 3 meters\} is the universal relation.
:::

:::solution{label="Solution"}
Since the school is boys school, no student of the school can be sister of any student of the school. Hence, $\mathrm{R}=\phi$, showing that R is the empty relation. It is also obvious that the difference between heights of any two students of the school has to be less than 3 meters. This shows that $\mathrm{R}^{\prime}=\mathrm{A} \times \mathrm{A}$ is the universal relation.
:::

:::

:::example{number="1.2" kind="example" id="ex_1.2" topic="Equivalence relation - congruent triangles"}
#### Example 1.2

:::prompt
Let T be the set of all triangles in a plane with R a relation in T given by $\mathrm{R}=\left\{\left(\mathrm{T}_{1}, \mathrm{~T}_{2}\right): \mathrm{T}_{1}\right.$ is congruent to $\left.\mathrm{T}_{2}\right\}$. Show that R is an equivalence relation.
:::

:::solution{label="Solution"}
R is reflexive, since every triangle is congruent to itself. Further, $\left(\mathrm{T}_{1}, \mathrm{~T}_{2}\right) \in \mathrm{R} \Rightarrow \mathrm{T}_{1}$ is congruent to $\mathrm{T}_{2} \Rightarrow \mathrm{~T}_{2}$ is congruent to $\mathrm{T}_{1} \Rightarrow\left(\mathrm{~T}_{2}, \mathrm{~T}_{1}\right) \in \mathrm{R}$. Hence, R is symmetric. Moreover, $\left(\mathrm{T}_{1}, \mathrm{~T}_{2}\right),\left(\mathrm{T}_{2}, \mathrm{~T}_{3}\right) \in \mathrm{R} \Rightarrow \mathrm{T}_{1}$ is congruent to $\mathrm{T}_{2}$ and $\mathrm{T}_{2}$ is congruent to $\mathrm{T}_{3} \Rightarrow \mathrm{~T}_{1}$ is congruent to $\mathrm{T}_{3} \Rightarrow\left(\mathrm{~T}_{1}, \mathrm{~T}_{3}\right) \in \mathrm{R}$. Therefore, R is an equivalence relation.
:::

:::

:::example{number="1.3" kind="example" id="ex_1.3" topic="Symmetric but not equivalence - perpendicular lines"}
#### Example 1.3

:::prompt
Let L be the set of all lines in a plane and R be the relation in L defined as $\mathrm{R}=\left\{\left(\mathrm{L}_{1}, \mathrm{~L}_{2}\right): \mathrm{L}_{1}\right.$ is perpendicular to $\left.\mathrm{L}_{2}\right\}$. Show that R is symmetric but neither reflexive nor transitive.
:::

:::figure{src="images/fig_maths-12-1_0.jpg" id="fig_1.1"}
Fig 1.1
:::

:::solution{label="Solution"}
R is not reflexive, as a line $\mathrm{L}_{1}$ can not be perpendicular to itself, i.e., ( $\mathrm{L}_{1}, \mathrm{~L}_{1}$ ) $\notin \mathrm{R}$. R is symmetric as $\left(\mathrm{L}_{1}, \mathrm{~L}_{2}\right) \in \mathrm{R}$

$$
\begin{array}{ll}
\Rightarrow & \mathrm{L}_{1} \text { is perpendicular to } \mathrm{L}_{2} \\
\Rightarrow & \mathrm{~L}_{2} \text { is perpendicular to } \mathrm{L}_{1} \\
\Rightarrow & \left(\mathrm{~L}_{2}, \mathrm{~L}_{1}\right) \in \mathrm{R} .
\end{array}
$$

R is not transitive. Indeed, if $\mathrm{L}_{1}$ is perpendicular to $\mathrm{L}_{2}$ and

![](images/fig_maths-12-1_0.jpg)
Fig 1.1

$\mathrm{L}_{2}$ is perpendicular to $\mathrm{L}_{3}$, then $\mathrm{L}_{1}$ can never be perpendicular to $\mathrm{L}_{3}$. In fact, $\mathrm{L}_{1}$ is parallel to $\mathrm{L}_{3}$, i.e., $\left(\mathrm{L}_{1}, \mathrm{~L}_{2}\right) \in \mathrm{R},\left(\mathrm{L}_{2}, \mathrm{~L}_{3}\right) \in \mathrm{R}$ but $\left(\mathrm{L}_{1}, \mathrm{~L}_{3}\right) \notin \mathrm{R}$.
:::

:::

:::example{number="1.4" kind="example" id="ex_1.4" topic="Reflexive but not equivalence relation"}
#### Example 1.4

:::prompt
Show that the relation R in the set $\{1,2,3\}$ given by $\mathrm{R}=\{(1,1),(2,2)$, $(3,3),(1,2),(2,3)\}$ is reflexive but neither symmetric nor transitive.
:::

:::solution{label="Solution"}
$R$ is reflexive, since $(1,1),(2,2)$ and $(3,3)$ lie in $R$. Also, $R$ is not symmetric, as $(1,2) \in \mathrm{R}$ but $(2,1) \notin \mathrm{R}$. Similarly, R is not transitive, as $(1,2) \in \mathrm{R}$ and $(2,3) \in \mathrm{R}$ but $(1,3) \notin \mathrm{R}$.
:::

:::

:::example{number="1.5" kind="example" id="ex_1.5" topic="Equivalence relation - divisibility by 2" corrections_applied="1"}
#### Example 1.5

:::prompt
Show that the relation R in the set $\mathbf{Z}$ of integers given by

$$
\mathrm{R}=\{(a, b): 2 \text { divides } a-b\}
$$

is an equivalence relation.
:::

:::solution{label="Solution"}
R is reflexive, as 2 divides $(a-a)$ for all $a \in \mathbf{Z}$. Further, if $(a, b) \in \mathrm{R}$, then 2 divides $a-b$. Therefore, 2 divides $b-a$. Hence, $(b, a) \in \mathrm{R}$, which shows that R is symmetric. Similarly, if $(a, b) \in \mathrm{R}$ and $(b, c) \in \mathrm{R}$, then $a-b$ and $b-c$ are divisible by 2. Now, $a-c=(a-b)+(b-c)$ is even (Why?). So, $(a-c)$ is divisible by 2 . This shows that R is transitive. Thus, R is an equivalence relation in $\mathbf{Z}$.
:::

:::

:::example{number="1.6" kind="example" id="ex_1.6" topic="Equivalence relation - odd/even parity"}
#### Example 1.6

:::prompt
Let R be the relation defined in the set $\mathrm{A}=\{1,2,3,4,5,6,7\}$ by $\mathrm{R}=\{(a, b):$ both $a$ and $b$ are either odd or even $\}$. Show that R is an equivalence relation. Further, show that all the elements of the subset \{1,3,5,7\} are related to each other and all the elements of the subset \{2, 4, 6\} are related to each other, but no element of the subset \{1, 3, 5, 7\} is related to any element of the subset \{2, 4, 6\}.
:::

:::solution{label="Solution"}
Take any element $a$ in A. Both $a$ and $a$ must be either odd or even, so $(a, a) \in \mathrm{R}$.
Next, if $(a, b) \in \mathrm{R} \Rightarrow$ then both $a$ and $b$ must be either odd or even, so $\Rightarrow(b, a) \in \mathrm{R}$.
Similarly, if $(a, b) \in \mathrm{R}$ and $(b, c) \in \mathrm{R} \Rightarrow$ then all elements $a, b, c$ must be either even or odd at the same time, so $\Rightarrow(a, c) \in \mathrm{R}$. Hence, R is an equivalence relation.
All elements of $\{1,3,5,7\}$ are related to each other, since they are all odd. In the same way, all elements of the subset \{2, 4, 6\} are related to each other, since they are all even. No element of \{1, 3, 5, 7\} is related to any element of \{2, 4, 6\}, because elements of \{1, 3, 5, 7\} are odd while elements of \{2, 4, 6\} are even.
:::

:::

:::example{number="1.7" kind="example" id="ex_1.7" topic="One-one but not onto - roll numbers"}
#### Example 1.7

:::prompt
Let A be the set of all 50 students of Class X in a school. Let $f: \mathrm{A} \rightarrow \mathbf{N}$ be function defined by $f(x)=$ roll number of the student $x$. Show that $f$ is one-one but not onto.
:::

:::solution{label="Solution"}
No two different students of the class can have same roll number. Therefore, $f$ must be one-one. We can assume without any loss of generality that roll numbers of students are from 1 to 50 . This implies that 51 in N is not roll number of any student of the class, so that 51 can not be image of any element of X under $f$. Hence, $f$ is not onto.
:::

:::

:::example{number="1.8" kind="example" id="ex_1.8" topic="One-one but not onto - f(x)=2x on N"}
#### Example 1.8

:::prompt
Show that the function $f: \mathbf{N} \rightarrow \mathbf{N}$, given by $f(x)=2 x$, is one-one but not onto.
:::

:::solution{label="Solution"}
The function $f$ is one-one, for $f\left(x_{1}\right)=f\left(x_{2}\right) \Rightarrow 2 x_{1}=2 x_{2} \Rightarrow x_{1}=x_{2}$. Further, $f$ is not onto, as for $1 \in \mathbf{N}$, there does not exist any $x$ in $\mathbf{N}$ such that $f(x)=2 x=1$.
:::

:::

:::example{number="1.9" kind="example" id="ex_1.9" topic="Bijective function - f(x)=2x on R"}
#### Example 1.9

:::prompt
Prove that the function $f: \mathbf{R} \rightarrow \mathbf{R}$, given by $f(x)=2 x$, is one-one and onto.
:::

:::figure{src="images/fig_maths-12-1_2.jpg" id="fig_1.3"}
Fig 1.3
:::

:::solution{label="Solution"}
$f$ is one-one, as $f\left(x_{1}\right)=f\left(x_{2}\right) \Rightarrow 2 x_{1}=2 x_{2} \Rightarrow x_{1}=x_{2}$. Also, given any real number $y$ in R, there exists $\frac{y}{2}$ in R such that $f\left(\frac{y}{2}\right)=2 .\left(\frac{y}{2}\right)=y$. Hence, $f$ is onto.

![](images/fig_maths-12-1_2.jpg)
Fig 1.3
:::

:::

:::example{number="1.10" kind="example" id="ex_1.10" topic="Onto but not one-one function"}
#### Example 1.10

:::prompt
Show that the function $f: \mathbf{N} \rightarrow \mathbf{N}$, given by $f(1)=f(2)=1$ and $f(x)=x-1$, for every $x>2$, is onto but not one-one.
:::

:::solution{label="Solution"}
$f$ is not one-one, as $f(1)=f(2)=1$. But $f$ is onto, as given any $y \in \mathbf{N}, y \neq 1$, we can choose $x$ as $y+1$ such that $f(y+1)=y+1-1=y$. Also for $1 \in \mathbf{N}$, we have $f(1)=1$.
:::

:::

:::example{number="1.11" kind="example" id="ex_1.11" topic="Neither one-one nor onto - f(x)=x^2"}
#### Example 1.11

:::prompt
Show that the function $f: \mathbf{R} \rightarrow \mathbf{R}$, defined as $f(x)=x^{2}$, is neither one-one nor onto.
:::

:::solution{label="Solution"}
Since $f(-1)=1=f(1), f$ is not oneone. Also, the element - 2 in the co-domain $\mathbf{R}$ is not image of any element $x$ in the domain $\mathbf{R}$ (Why?). Therefore $f$ is not onto.
:::

:::

:::example{number="1.12" kind="example" id="ex_1.12" topic="Bijective piecewise function"}
#### Example 1.12

:::prompt
Show that $f: \mathbf{N} \rightarrow \mathbf{N}$, given by

$$
f(x)=\begin{aligned}
& x+1, \text { if } x \text { is odd, } \\
& x-1, \text { if } x \text { is even }
\end{aligned}
$$

is both one-one and onto.

![](images/fig_maths-12-1_3.jpg)
The image of 1 and -1 under $\boldsymbol{f}$ is 1.

Fig 1.4
:::

:::figure{src="images/fig_maths-12-1_3.jpg" id="fig_1.4"}
Fig 1.4
:::

:::solution{label="Solution"}
Suppose $f\left(x_{1}\right)=f\left(x_{2}\right)$. If $x_{1}$ is odd and $x_{2}$ is even, then $x_{1}+1=x_{2}-1$, i.e., $x_{2}-x_{1}=2$, which is impossible. In the same way, $x_{1}$ being even and $x_{2}$ being odd can also be ruled out, by a similar argument. So both $x_{1}$ and $x_{2}$ must be either odd or even.
Suppose both $x_{1}$ and $x_{2}$ are odd. Then $f\left(x_{1}\right)=f\left(x_{2}\right) \Rightarrow x_{1}+1=x_{2}+1 \Rightarrow x_{1}=x_{2}$. Suppose instead both $x_{1}$ and $x_{2}$ are even. Then also $f\left(x_{1}\right)=f\left(x_{2}\right) \Rightarrow x_{1}-1=x_{2}-1 \Rightarrow x_{1}=x_{2}$. So $f$ is one-one.
Also, any odd number $2 r+1$ in the co-domain $\mathbf{N}$ is the image of $2 r+2$ in the domain $\mathbf{N}$, and any even number $2 r$ in the co-domain $\mathbf{N}$ is the image of $2 r-1$ in the domain $\mathbf{N}$. So $f$ is onto.
:::

:::

:::example{number="1.13" kind="example" id="ex_1.13" topic="Onto implies one-one on finite set"}
#### Example 1.13

:::prompt
Show that an onto function $f:\{1,2,3\} \rightarrow\{1,2,3\}$ is always one-one.
:::

:::solution{label="Solution"}
Suppose $f$ is not one-one. Then there exists two elements, say 1 and 2 in the domain whose image in the co-domain is same. Also, the image of 3 under $f$ can be only one element. Therefore, the range set can have at the most two elements of the co-domain $\{1,2,3\}$, showing that $f$ is not onto, a contradiction. Hence, $f$ must be one-one.
:::

:::

:::example{number="1.14" kind="example" id="ex_1.14" topic="One-one implies onto on finite set" corrections_applied="1"}
#### Example 1.14

:::prompt
Show that a one-one function $f:\{1,2,3\} \rightarrow\{1,2,3\}$ must be onto.
:::

:::solution{label="Solution"}
Since $f$ is one-one, three elements of $\{1,2,3\}$ must be taken to 3 different elements of the co-domain $\{1,2,3\}$ under $f$. Hence, $f$ has to be onto.
:::

:::

:::example{number="1.15" kind="example" id="ex_1.15" topic="Composition of finite functions"}
#### Example 1.15

:::prompt
Let $f:\{2,3,4,5\} \rightarrow\{3,4,5,9\}$ and $g:\{3,4,5,9\} \rightarrow\{7,11,15\}$ be functions defined as $f(2)=3, f(3)=4, f(4)=f(5)=5$ and $g(3)=g(4)=7$ and $g(5)=g(9)=11$. Find $g o f$.
:::

:::solution{label="Solution"}
We have $\operatorname{gof}(2)=g(f(2))=g(3)=7, \operatorname{gof}(3)=g(f(3))=g(4)=7$, $\operatorname{gof}(4)=g(f(4))=g(5)=11$ and $\operatorname{gof}(5)=g(5)=11$.
:::

:::

:::example{number="1.16" kind="example" id="ex_1.16" topic="gof not equal to fog" corrections_applied="1"}
#### Example 1.16

:::prompt
Find $g o f$ and $f o g$, if $f: \mathbf{R} \rightarrow \mathbf{R}$ and $g: \mathbf{R} \rightarrow \mathbf{R}$ are given by $f(x)=\cos x$ and $g(x)=3 x^{2}$. Show that $g o f \neq f o g$.
:::

:::solution{label="Solution"}
We have $g o f(x)=g(f(x))=g(\cos x)=3(\cos x)^{2}=3 \cos ^{2} x$. Similarly, $f o g(x)=f(g(x))=f\left(3 x^{2}\right)=\cos \left(3 x^{2}\right)$. Note that $3 \cos ^{2} x \neq \cos 3 x^{2}$, for $x=0$. Hence, gof $\neq$ fog .
:::

:::

:::example{number="1.17" kind="example" id="ex_1.17" topic="Invertible function and its inverse"}
#### Example 1.17

:::prompt
Let $f: \mathbf{N} \rightarrow \mathrm{Y}$ be a function defined as $f(x)=4 x+3$, where, $\mathrm{Y}=\{y \in \mathbf{N}: y=4 x+3$ for some $x \in \mathbf{N}\}$. Show that $f$ is invertible. Find the inverse.
:::

:::solution{label="Solution"}
Consider an arbitrary element $y$ of Y. By the definition of Y, $y=4 x+3$ for some $x$ in the domain $\mathbf{N}$. So $x=\frac{(y-3)}{4}$.
Define $g: \mathrm{Y} \rightarrow \mathbf{N}$ by

$$
g(y)=\frac{(y-3)}{4} . \text { Now, } g \circ f(x)=g(f(x))=g(4 x+3)=\frac{(4 x+3-3)}{4}=x \text { and }
$$

$f o g(y)=f(g(y))=f\left(\frac{(y-3)}{4}\right)=\frac{4(y-3)}{4}+3=y-3+3=y$. This shows $g o f=\mathrm{I}_{\mathrm{N}}$ and $f o g=\mathrm{I}_{\mathrm{Y}}$. So $f$ is invertible, and $g$ is the inverse of $f$.
:::

:::

:::example{number="1.18" kind="example" id="ex_1.18" topic="Intersection of equivalence relations"}
#### Example 1.18

:::prompt
If $R_{1}$ and $R_{2}$ are equivalence relations in a set $A$, show that $R_{1} \cap R_{2}$ is also an equivalence relation.
:::

:::solution{label="Solution"}
Since $\mathrm{R}_{1}$ and $\mathrm{R}_{2}$ are equivalence relations, $(a, a) \in \mathrm{R}_{1}$, and $(a, a) \in \mathrm{R}_{2} \forall a \in \mathrm{~A}$. This implies that $(a, a) \in \mathrm{R}_{1} \cap \mathrm{R}_{2}, \forall a$, showing $\mathrm{R}_{1} \cap \mathrm{R}_{2}$ is reflexive. Further, $(a, b) \in \mathrm{R}_{1} \cap \mathrm{R}_{2} \Rightarrow(a, b) \in \mathrm{R}_{1}$ and $(a, b) \in \mathrm{R}_{2} \Rightarrow(b, a) \in \mathrm{R}_{1}$ and $(b, a) \in \mathrm{R}_{2} \Rightarrow$ $(b, a) \in \mathrm{R}_{1} \cap \mathrm{R}_{2}$, hence, $\mathrm{R}_{1} \cap \mathrm{R}_{2}$ is symmetric. Similarly, $(a, b) \in \mathrm{R}_{1} \cap \mathrm{R}_{2}$ and $(b, c) \in \mathrm{R}_{1} \cap \mathrm{R}_{2} \Rightarrow(a, c) \in \mathrm{R}_{1}$ and $(a, c) \in \mathrm{R}_{2} \Rightarrow(a, c) \in \mathrm{R}_{1} \cap \mathrm{R}_{2}$. This shows that $\mathrm{R}_{1} \cap \mathrm{R}_{2}$ is transitive. Thus, $\mathrm{R}_{1} \cap \mathrm{R}_{2}$ is an equivalence relation.
:::

:::

:::example{number="1.19" kind="example" id="ex_1.19" topic="Equivalence relation on ordered pairs"}
#### Example 1.19

:::prompt
Let R be a relation on the set A of ordered pairs of positive integers defined by $(x, y) \mathrm{R}(u, v)$ if and only if $x v=y u$. Show that R is an equivalence relation.
:::

:::solution{label="Solution"}
Clearly, $(x, y) \mathrm{R}(x, y), \forall(x, y) \in \mathrm{A}$, since $x y=y x$. This shows that R is reflexive. Further, $(x, y) \mathrm{R}(u, v) \Rightarrow x v=y u \Rightarrow u y=v x$ and hence $(u, v) \mathrm{R}(x, y)$. This shows that R is symmetric. Similarly, $(x, y) \mathrm{R}(u, v)$ and $(u, v) \mathrm{R}(a, b) \Rightarrow x v=y u$ and $u b=v a \Rightarrow x v \frac{a}{u}=y u \frac{a}{u} \Rightarrow x v \frac{b}{v}=y u \frac{a}{u} \Rightarrow x b=y a$ and hence $(x, y) \mathrm{R}(a, b)$. Thus, R is transitive. Thus, R is an equivalence relation.
:::

:::

:::example{number="1.20" kind="example" id="ex_1.20" topic="Equality of two relations"}
#### Example 1.20

:::prompt
Let $\mathrm{X}=\{1,2,3,4,5,6,7,8,9\}$. Let $\mathrm{R}_{1}$ be a relation in X given by $\mathrm{R}_{1}=\left\{(x, y): x-y\right.$ is divisible by 3\} and $\mathrm{R}_{2}$ be another relation on X given by $\mathrm{R}_{2}=\{(x, y):\{x, y\} \subset\{1,4,7\}\}$ or $\{x, y\} \subset\{2,5,8\}$ or $\left.\{x, y\} \subset\{3,6,9\}\right\}$. Show that $\mathrm{R}_{1}=\mathrm{R}_{2}$.
:::

:::solution{label="Solution"}
Note that the characteristic of sets $\{1,4,7\},\{2,5,8\}$ and $\{3,6,9\}$ is that difference between any two elements of these sets is a multiple of 3 . Therefore, $(x, y) \in \mathrm{R}_{1} \Rightarrow x-y$ is a multiple of $3 \Rightarrow\{x, y\} \subset\{1,4,7\}$ or $\{x, y\} \subset\{2,5,8\}$ or $\{x, y\} \subset\{3,6,9\} \Rightarrow(x, y) \in \mathrm{R}_{2}$. Hence, $\mathrm{R}_{1} \subset \mathrm{R}_{2}$. Similarly, $\{x, y\} \in \mathrm{R}_{2} \Rightarrow\{x, y\}$
$\subset\{1,4,7\}$ or $\{x, y\} \subset\{2,5,8\}$ or $\{x, y\} \subset\{3,6,9\} \Rightarrow x-y$ is divisible by $3 \Rightarrow\{x, y\} \in \mathrm{R}_{1}$. This shows that $\mathrm{R}_{2} \subset \mathrm{R}_{1}$. Hence, $\mathrm{R}_{1}=\mathrm{R}_{2}$.
:::

:::

:::example{number="1.21" kind="example" id="ex_1.21" topic="Equivalence relation from a function"}
#### Example 1.21

:::prompt
Let $f: \mathrm{X} \rightarrow \mathrm{Y}$ be a function. Define a relation R in X given by $\mathrm{R}=\{(a, b): f(a)=f(b)\}$. Examine whether R is an equivalence relation or not.
:::

:::solution{label="Solution"}
For every $a \in \mathrm{X},(a, a) \in \mathrm{R}$, since $f(a)=f(a)$, showing that R is reflexive. Similarly, $(a, b) \in \mathrm{R} \Rightarrow f(a)=f(b) \Rightarrow f(b)=f(a) \Rightarrow(b, a) \in \mathrm{R}$. Therefore, R is symmetric. Further, $(a, b) \in \mathrm{R}$ and $(b, c) \in \mathrm{R} \Rightarrow f(a)=f(b)$ and $f(b)=f(c) \Rightarrow f(a)$ $=f(c) \Rightarrow(a, c) \in \mathrm{R}$, which implies that R is transitive. Hence, R is an equivalence relation.
:::

:::

:::example{number="1.22" kind="example" id="ex_1.22" topic="Counting one-one functions"}
#### Example 1.22

:::prompt
Find the number of all one-one functions from set $\mathrm{A}=\{1,2,3\}$ to itself.
:::

:::solution{label="Solution"}
One-one function from \{1, 2, 3\} to itself is simply a permutation on three symbols $1,2,3$. Therefore, total number of one-one maps from $\{1,2,3\}$ to itself is same as total number of permutations on three symbols $1,2,3$ which is $3!=6$.
:::

:::

:::example{number="1.23" kind="example" id="ex_1.23" topic="Counting relations with given constraints"}
#### Example 1.23

:::prompt
Let $\mathrm{A}=\{1,2,3\}$. Then show that the number of relations containing $(1,2)$ and $(2,3)$ which are reflexive and transitive but not symmetric is three.
:::

:::solution{label="Solution"}
The smallest relation $\mathrm{R}_{1}$ containing $(1,2)$ and $(2,3)$ that is reflexive and transitive but not symmetric is \{(1, 1), (2, 2), (3, 3), (1, 2), (2, 3), (1, 3)\}.
If we add the pair $(2,1)$ to $\mathrm{R}_{1}$, we get $\mathrm{R}_{2}$. The relation $\mathrm{R}_{2}$ is reflexive and transitive but not symmetric.
In the same way, adding $(3,2)$ to $\mathrm{R}_{1}$ gives the relation $\mathrm{R}_{3}$, with the same property.
We cannot add both pairs $(2,1),(3,2)$, or just the single pair $(3,1)$, to $\mathrm{R}_{1}$ at the same time. Doing so would force us to add the remaining pair to keep transitivity, and the relation would then also become symmetric, which we do not want.
So the total number of such relations is three.
:::

:::

:::example{number="1.24" kind="example" id="ex_1.24" topic="Counting equivalence relations"}
#### Example 1.24

:::prompt
Show that the number of equivalence relation in the set $\{1,2,3\}$ containing $(1,2)$ and $(2,1)$ is two.
:::

:::solution{label="Solution"}
The smallest equivalence relation $\mathrm{R}_{1}$ containing ( 1,2 ) and ( 2,1 ) is $\{(1,1)$, $(2,2),(3,3),(1,2),(2,1)\}$. This leaves only 4 pairs: $(2,3),(3,2)$, $(1,3)$ and $(3,1)$.
Suppose we add just one of them, say $(2,3)$, to $\mathrm{R}_{1}$. Then symmetry forces us to also add $(3,2)$, and transitivity then forces us to add $(1,3)$ and $(3,1)$ too.
So the only equivalence relation bigger than $\mathrm{R}_{1}$ is the universal relation. Hence, the total number of equivalence relations containing $(1,2)$ and $(2,1)$ is two.
:::

:::

:::example{number="1.25" kind="example" id="ex_1.25" topic="Sum of onto functions not onto"}
#### Example 1.25

:::prompt
Consider the identity function $\mathrm{I}_{\mathbf{N}}: \mathbf{N} \rightarrow \mathbf{N}$ defined as $\mathrm{I}_{\mathbf{N}}(x)=x \forall x \in \mathbf{N}$. Show that although $\mathrm{I}_{\mathrm{N}}$ is onto but $\mathrm{I}_{\mathrm{N}}+\mathrm{I}_{\mathrm{N}}: \mathbf{N} \rightarrow \mathbf{N}$ defined as

$$
\left(\mathrm{I}_{\mathrm{N}}+\mathrm{I}_{\mathrm{N}}\right)(x)=\mathrm{I}_{\mathrm{N}}(x)+\mathrm{I}_{\mathrm{N}}(x)=x+x=2 x \text { is not onto. }
$$
:::

:::solution{label="Solution"}
Clearly $\mathrm{I}_{\mathrm{N}}$ is onto. But $\mathrm{I}_{\mathrm{N}}+\mathrm{I}_{\mathrm{N}}$ is not onto, as we can find an element 3 in the co-domain $\mathbf{N}$ such that there does not exist any $x$ in the domain $\mathbf{N}$ with $\left(\mathrm{I}_{\mathrm{N}}+\mathrm{I}_{\mathrm{N}}\right)(x)=2 x=3$.
:::

:::

:::example{number="1.26" kind="example" id="ex_1.26" topic="Sum of one-one functions not one-one"}
#### Example 1.26

:::prompt
Consider a function $f:\left[0, \frac{\pi}{2}\right] \rightarrow \mathbf{R}$ given by $f(x)=\sin x$ and $g:\left[0, \frac{\pi}{2}\right] \rightarrow \mathbf{R}$ given by $g(x)=\cos x$. Show that $f$ and $g$ are one-one, but $f+g$ is not one-one.
:::

:::solution{label="Solution"}
Since for any two distinct elements $x_{1}$ and $x_{2}$ in $\left[0, \frac{\pi}{2}\right], \sin x_{1} \neq \sin x_{2}$ and $\cos x_{1} \neq \cos x_{2}$, both $f$ and $g$ must be one-one. But $(f+g)(0)=\sin 0+\cos 0=1$ and $(f+g)\left(\frac{\pi}{2}\right)=\sin \frac{\pi}{2}+\cos \frac{\pi}{2}=1$. Therefore, $f+g$ is not one-one.
:::

:::

## Questions and Solutions

:::question{number="1.1" kind="exercise" id="q_1.1" topic="Reflexive symmetric transitive - five relations" corrections_applied="1"}
#### Question 1.1

:::prompt
Determine whether each of the following relations are reflexive, symmetric and transitive:
    (i) Relation R in the set $\mathrm{A}=\{1,2,3, \ldots, 13,14\}$ defined as
$$
\mathrm{R}=\{(x, y): 3 x-y=0\}
$$
    (ii) Relation R in the set N of natural numbers defined as
$$
\mathrm{R}=\{(x, y): y=x+5 \text { and } x<4\}
$$
    (iii) Relation R in the set $\mathrm{A}=\{1,2,3,4,5,6\}$ as
$$
\mathrm{R}=\{(x, y): y \text { is divisible by } x\}
$$
    (iv) Relation R in the set $\mathbf{Z}$ of all integers defined as
$$
\mathrm{R}=\{(x, y): x-y \text { is an integer }\}
$$
    (v) Relation R in the set A of human beings in a town at a particular time given by
        (a) $\mathrm{R}=\{(x, y): x$ and $y$ work at the same place $\}$
        (b) $\mathrm{R}=\{(x, y): x$ and $y$ live in the same locality $\}$
        (c) $\mathrm{R}=\{(x, y): x$ is exactly 7 cm taller than $y\}$
        (d) $\mathrm{R}=\{(x, y): x$ is wife of $y\}$
        (e) $\mathrm{R}=\{(x, y): x$ is father of $y\}$
:::

:::solution{label="Solution"}
(i) $R=\{(1,3),(2,6),(3,9),(4,12)\}$
$R$ is not reflexive because $(1,1),(2,2) \ldots$ and $(14,14) \notin R$.
R is not symmetric because $(1,3) \in R$, but $(3,1) \notin R$.[since $3(3) \neq 0]$.
R is not transitive because $(1,3),(3,9) \in R$, but $(1,9) \notin R .[3(1)-9 \neq 0]$.
Hence, R is neither reflexive nor symmetric nor transitive.
(ii) $R=\{(1,6),(2,7),(3,8)\}$
R is not reflexive because $(1,1) \notin R$.
R is not symmetric because $(1,6) \in R$ but $(6,1) \notin R$.
R is not transitive because there isn't any ordered pair in R such that $(x, y),(y, z) \in R$, so $(x, z) \notin R$.
Hence, R is neither reflexive nor symmetric nor transitive.
(iii) $R=\{(x, y): y$ is divisible by $x\}$
We know that any number other than 0 is divisible by itself.
Thus, $(x, x) \in R$
So, $R$ is reflexive.

$(2,4) \in R \quad$ [because 4 is divisible by 2 ]
But $(4,2) \notin R$ [since 2 is not divisible by 4]
So, R is not symmetric.
Let $(x, y)$ and $(y, z) \in R$. So, y is divisible by x and z is divisible by y .
So, z is divisible by $\mathrm{x} \Rightarrow(x, z) \in R$
So, R is transitive.
So, $R$ is reflexive and transitive but not symmetric.
(iv) $R=\{(x, y): x-y$ is an integer $\}$
For $x \in \mathrm{Z},(x, x) \notin R$ because $x-x=0$ is an integer.
So, R is reflexive.
For, $x, y \in Z$, if $x, y \in \mathrm{R}$, then $x-y$ is an integer $\Rightarrow(y-x)$ is an integer.
So, $(y, x) \in R$
So, R is symmetric.
Let $(x, y)$ and $(y, z) \in R$, where $x, y, z \in \mathrm{Z}$.
$\Rightarrow(x-y)$ and $(y-z)$ are integers.
$\Rightarrow x-z=(x-y)+(y-z)$ is an integer.
So, R is transitive.
So, $R$ is reflexive, symmetric and transitive.
(v)

a) $R=\{(x, y): x$ and $y$ work at the same place $\}$
R is reflexive because $(x, x) \in R$
R is symmetric because ,
If $(x, y) \in R$, then $x$ and y work at the same place and y and $x$ also work at the same place. $(y, x) \in R$.
R is transitive because,
Let $(x, y),(y, z) \in R$
$x$ and $y$ work at the same place and $y$ and $z$ work at the same place.

Then, $x$ and $z$ also works at the same place. $(x, z) \in R$.
Hence, R is reflexive, symmetric and transitive.

b) $R=\{(x, y): x$ and $y$ live in the same locality $\}$
R is reflexive because $(x, x) \in R$
R is symmetric because,
If $(x, y) \in R$, then $x$ and y live in the same locality and y and $x$ also live in the same locality $(y, x) \in R$.
R is transitive because,

Let $(x, y),(y, z) \in R$
$x$ and $y$ live in the same locality and $y$ and $z$ live in the same locality.

Then $x$ and $z$ also live in the same locality. $(x, z) \in R$.
Hence, R is reflexive, symmetric and transitive.

c) $R=\{(x, y): x$ is exactly 7 cm taller than $y\}$
R is not reflexive because $(x, x) \notin R$.
R is not symmetric because,
If $(x, y) \in R$, then $x$ is exactly $7 c m$ taller than y and y is clearly not taller than $x$ .$(y, x) \notin R$.
R is not transitive because,
Let $(x, y),(y, z) \in R$
$x$ is exactly $7 c m$ taller than y and $y$ is exactly $7 c m$ taller than $z$.
Then $x$ is exactly $14 c m$ taller than $z .(x, z) \notin R$
Hence, R is neither reflexive nor symmetric nor transitive.
d) $R=\{(x, y): x$ is wife of $y\}$
R is not reflexive because $(x, x) \notin R$.
R is not symmetric because,
Let $(x, y) \in R, x$ is the wife of $y$ and $y$ is not the wife of $x .(y, x) \notin R$.
R is not transitive because,
Let $(x, y),(y, z) \in R$
$x$ is wife of y and $y$ is wife of $z$, which is not possible.
$$
(x, z) \notin R .
$$
Hence, R is neither reflexive nor symmetric nor transitive.
e) $R=\{(x, y): x$ is father of $y\}$
R is not reflexive because $(x, x) \notin R$.
R is not symmetric because,
Let $(x, y) \in R, x$ is the father of $y$ and $y$ is not the father of $x .(y, x) \notin R$.
R is not transitive because,
Let $(x, y),(y, z) \in R$
$x$ is father of y and $y$ is father of $z, x$ is not father of $z .(x, z) \notin R$.
Hence, R is neither reflexive nor symmetric nor transitive.
:::

:::

:::question{number="1.2" kind="exercise" id="q_1.2" topic="Relation neither reflexive symmetric nor transitive"}
#### Question 1.2

:::prompt
Show that the relation R in the set $\mathbf{R}$ of real numbers, defined as $\mathrm{R}=\left\{(a, b): a \leq b^{2}\right\}$ is neither reflexive nor symmetric nor transitive.
:::

:::solution{label="Solution"}
$$
\begin{aligned}
& R=\left\{(a, b): a \leq b^{2}\right\} \\
& \left(\frac{1}{2}, \frac{1}{2}\right) \notin R \text { because } \frac{1}{2}>\left(\frac{1}{2}\right)^{2}
\end{aligned}
$$

R is not reflexive.

$$
\begin{aligned}
& (1,4) \in R \text { as } 1<4 \text {. But } 4 \text { is not less than } 1^{2} \text {. } \\
& (4,1) \notin R
\end{aligned}
$$

R is not symmetric.

$$
\begin{aligned}
& (3,2)(2,1.5) \in R \quad\left[\text { Because } 3<2^{2}=4 \text { and } 2<(1.5)^{2}=2.25\right] \\
& 3>(1.5)^{2}=2.25 \\
& \therefore(3,1.5) \notin R
\end{aligned}
$$

R is not transitive.
R is neither reflective nor symmetric nor transitive.
:::

:::

:::question{number="1.3" kind="exercise" id="q_1.3" topic="Relation b = a+1 properties"}
#### Question 1.3

:::prompt
Check whether the relation R defined in the set $\{1,2,3,4,5,6\}$ as $\mathrm{R}=\{(a, b): b=a+1\}$ is reflexive, symmetric or transitive.
:::

:::solution{label="Solution"}
$$
\begin{aligned}
& A=\{1,2,3,4,5,6\} \\
& R=\{(a, b): b=a+1\} \\
& R=\{(1,2),(2,3),(3,4),(4,5),(5,6)\}
\end{aligned}
$$

$$
\begin{aligned}
& (a, a) \notin R, a \in A \\
& (1,1),(2,2),(3,3),(4,4),(5,5) \notin R
\end{aligned}
$$

$R$ is not reflexive.

$$
(1,2) \in R \text {, but }(2,1) \notin R
$$

R is not symmetric.

$$
\begin{aligned}
& (1,2),(2,3) \in R \\
& (1,3) \notin R
\end{aligned}
$$

$R$ is not transitive.

R is neither reflective nor symmetric nor transitive.
:::

:::

:::question{number="1.4" kind="exercise" id="q_1.4" topic="Relation a <= b properties"}
#### Question 1.4

:::prompt
Show that the relation R in $\mathbf{R}$ defined as $\mathrm{R}=\{(a, b): a \leq b\}$, is reflexive and transitive but not symmetric.
:::

:::solution{label="Solution"}
$$
\begin{aligned}
& R=\{(a, b): a \leq b\} \\
& (a, a) \in R
\end{aligned}
$$

R is reflexive.

$$
\begin{aligned}
& (2,4) \in R(\text { as } 2<4) \\
& (4,2) \notin R(\text { as } 4>2)
\end{aligned}
$$

R is not symmetric.

$$
\begin{aligned}
& (a, b),(b, c) \in R \\
& a \leq b \text { and } b \leq c \\
& \Rightarrow a \leq c \\
& \Rightarrow(a, c) \in R
\end{aligned}
$$

R is transitive.
$R$ is reflexive and transitive but not symmetric.
:::

:::

:::question{number="1.5" kind="exercise" id="q_1.5" topic="Relation a <= b^3 properties"}
#### Question 1.5

:::prompt
Check whether the relation R in $\mathbf{R}$ defined by $\mathrm{R}=\left\{(a, b): a \leq b^{3}\right\}$ is reflexive, symmetric or transitive.
:::

:::solution{label="Solution"}
$$
\begin{aligned}
& R=\left\{(a, b): a \leq b^{3}\right\} \\
& \left(\frac{1}{2}, \frac{1}{2}\right) \notin R, \text { since } \frac{1}{2}>\left(\frac{1}{2}\right)^{3}
\end{aligned}
$$

R is not reflexive.

$$
\begin{aligned}
& (1,2) \in R\left(\text { as } 1<2^{3}=8\right) \\
& (2,1) \notin R\left(\text { as } 2^{3}>1=8\right)
\end{aligned}
$$

$R$ is not symmetric.

$$
\begin{aligned}
& \left(3, \frac{3}{2}\right),\left(\frac{3}{2}, \frac{6}{5}\right) \in R, \text { since } 3<\left(\frac{3}{2}\right)^{3} \text { and } \frac{2}{3}<\left(\frac{6}{2}\right)^{3} \\
& \left(3, \frac{6}{5}\right) \notin R 3>\left(\frac{6}{5}\right)^{3}
\end{aligned}
$$

R is not transitive.
R is neither reflexive nor symmetric nor transitive.
:::

:::

:::question{number="1.6" kind="exercise" id="q_1.6" topic="Symmetric relation on {1,2,3}"}
#### Question 1.6

:::prompt
Show that the relation R in the set $\{1,2,3\}$ given by $\mathrm{R}=\{(1,2),(2,1)\}$ is symmetric but neither reflexive nor transitive.
:::

:::solution{label="Solution"}
$$
\begin{aligned}
& A=\{1,2,3\} \\
& R=\{(1,2),(2,1)\} \\
& (1,1),(2,2),(3,3) \notin R
\end{aligned}
$$

R is not reflexive.

$$
(1,2) \in R \text { and }(2,1) \in R
$$

$R$ is symmetric.

$$
\begin{aligned}
& (1,2) \in R \text { and }(2,1) \in R \\
& (1,1) \in R
\end{aligned}
$$

R is not transitive.
R is symmetric, but not reflexive or transitive.
:::

:::

:::question{number="1.7" kind="exercise" id="q_1.7" topic="Equivalence relation - same page count"}
#### Question 1.7

:::prompt
Show that the relation R in the set A of all the books in a library of a college, given by $\mathrm{R}=\{(x, y): x$ and $y$ have same number of pages $\}$ is an equivalence relation.
:::

:::solution{label="Solution"}
$$
R=\{(x, y): x \text { and } y \text { have same number of pages }\}
$$

R is reflexive since $(x, x) \in R$ as $x$ and $x$ have same number of pages.

R is reflexive.

$$
(x, y) \in R
$$

$x$ and y have same number of pages and y and $x$ have same number of pages $(y, x) \in R$ R is symmetric.

$$
(x, y) \in R,(y, z) \in R
$$

$x$ and $y$ have same number of pages, $y$ and $z$ have same number of pages. Then $x$ and $z$ have same number of pages.

$$
(x, z) \in R
$$

R is transitive.
$R$ is an equivalence relation.
:::

:::

:::question{number="1.8" kind="exercise" id="q_1.8" topic="Equivalence relation - |a-b| even"}
#### Question 1.8

:::prompt
Show that the relation R in the set $\mathrm{A}=\{1,2,3,4,5\}$ given by
$\mathrm{R}=\{(a, b):|a-b|$ is even $\}$, is an equivalence relation. Show that all the elements of $\{1,3,5\}$ are related to each other and all the elements of \{2,4\} are related to each other. But no element of $\{1,3,5\}$ is related to any element of $\{2,4\}$.
:::

:::solution{label="Solution"}
$$
\begin{aligned}
& a \in A \\
& |a-a|=0(\text { which is even })
\end{aligned}
$$

R is reflective.

$$
\begin{aligned}
& (a, b) \in R \\
& \Rightarrow|a-b|[\text { is even }] \\
& \Rightarrow|-(a-b)|=|b-a|[\text { is even }] \\
& (b, a) \in R
\end{aligned}
$$

R is symmetric.

$$
\begin{aligned}
& (a, b) \in R \text { and }(b, c) \in \mathrm{R} \\
& \Rightarrow|a-b| \text { is even and }|b-c| \text { is even } \\
& \Rightarrow(a-b) \text { is even and }(b-c) \text { is even } \\
& \Rightarrow(a-c)=(a+b)+(b-c) \text { is even }
\end{aligned}
$$

$\Rightarrow|a-b|$ is even

$$
\Rightarrow(a, c) \in R
$$

R is transitive.
$R$ is an equivalence relation.
All elements of $\{1,3,5\}$ are related to each other because they are all odd. So, the modulus of the difference between any two elements is even.

Similarly, all elements $\{2,4\}$ are related to each other because they are all even.
No element of $\{1,3,5\}$ is related to any elements of $\{2,4\}$ as all elements of $\{1,3,5\}$ are odd and all elements of $\{2,4\}$ are even. So, the modulus of the difference between the two elements will not be even.
:::

:::

:::question{number="1.9" kind="exercise" id="q_1.9" topic="Equivalence relation - multiple of 4"}
#### Question 1.9

:::prompt
Show that each of the relation R in the set $\mathrm{A}=\{x \in \mathbf{Z}: 0 \leq x \leq 12\}$, given by
    (i) $\mathrm{R}=\{(a, b):|a-b|$ is a multiple of 4$\}$
    (ii) $\mathrm{R}=\{(a, b): a=b\}$
is an equivalence relation. Find the set of all elements related to 1 in each case.
:::

:::solution{label="Solution"}
$$
A=\{x \in Z: 0 \leq x \leq 12\}=\{0,1,2,3,4,5,6,7,8,9,10,11,12\}
$$

i. $$
\begin{aligned}
& R=\{(a, b):|a-b| \text { is a mutiple of } 4\} \\
& a \in A,(a, a) \in R \quad[|a-a|=0 \text { is a multiple of } 4]
\end{aligned}
$$
$R$ is reflexive.
$$
\begin{aligned}
& (a, b) \in R \Rightarrow|a-b|[\text { is a multiple of } 4] \\
& \Rightarrow|-(a-b)|=|b-a|[\text { is a multiple of } 4] \\
& (b, a) \in R
\end{aligned}
$$
$R$ is symmetric.
$$
\begin{aligned}
& (a, b) \in R \text { and }(b, c) \in R \\
& \Rightarrow|a-b| \text { is a multiple of } 4 \text { and }|b-c| \text { is a multiple of } 4 \\
& \Rightarrow(a-b) \text { is a multiple of } 4 \text { and }(b-c) \text { is a multiple of } 4 \\
& \Rightarrow(a-c)=(a-b)+(b-c) \text { is a multiple of } 4 \\
& \Rightarrow|a-c| \text { is a multiple of } 4
\end{aligned}
$$

$$
\Rightarrow(a, c) \in R
$$

R is transitive.
$R$ is an equivalence relation.
The set of elements related to 1 is $\{1,5,9\}$ as
$|1-1|=0$ is a multiple of 4 .
$|5-1|=4$ is a multiple of 4.
$|9-1|=8$ is a multiple of 4.
ii. $\quad R=\{(a, b): a=b\}$
$a \in A,(a, a) \in R \quad[$ since $\mathrm{a}=\mathrm{a}]$
$R$ is reflective.

$$
\begin{aligned}
& (a, b) \in R \\
& \Rightarrow a=b \\
& \Rightarrow b=a \\
& \Rightarrow(b, a) \in R
\end{aligned}
$$

$R$ is symmetric.

$$
\begin{aligned}
& (a, b) \in R \text { and }(b, c) \in \mathrm{R} \\
& \Rightarrow a=b \text { and } b=c \\
& \Rightarrow a=c \\
& \Rightarrow(a, c) \in R
\end{aligned}
$$

R is transitive.
R is an equivalence relation.
The set of elements related to 1 is $\{1\}$.
:::

:::

:::question{number="1.10" kind="exercise" id="q_1.10" topic="Examples of relations with given properties"}
#### Question 1.10

:::prompt
Give an example of a relation. Which is

(i) Symmetric but neither reflexive nor transitive.
(ii) Transitive but neither reflexive nor symmetric.
(iii) Reflexive and symmetric but not transitive.
(iv) Reflexive and transitive but not symmetric.
(v) Symmetric and transitive but not reflexive.
:::

:::solution{label="Solution"}
i.

$$
\begin{aligned}
& A=\{5,6,7\} \\
& R=\{(5,6),(6,5)\} \\
& (5,5),(6,6),(7,7) \notin R
\end{aligned}
$$
R is not reflexive as $(5,5),(6,6),(7,7) \notin R$ $(5,6),(6,5) \in R$ and $(6,5) \in R, R$ is symmetric.
$$
\Rightarrow(5,6),(6,5) \in R \text {, but }(5,5) \notin R
$$
R is not transitive.
Relation $R$ is symmetric but not reflexive or transitive.
ii. $\quad R=\{(a, b): a<b\}$
$$
a \in R,(a, a) \notin R[\text { since } a \text { cannot be less than itself }]
$$
R is not reflexive.
$$
(1,2) \in R(\text { as } 1<2)
$$
But 2 is not less than 1
$$
\therefore(2,1) \notin R
$$
R is not symmetric.
$$
\begin{aligned}
& (a, b),(b, c) \in R \\
& \Rightarrow a<b \text { and } b<c \\
& \Rightarrow a<c \\
& \Rightarrow(a, c) \in R
\end{aligned}
$$
R is transitive.
Relation $R$ is transitive but not reflexive and symmetric.
iii. $A=\{4,6,8\}$
$$
A=\{(4,4),(6,6),(8,8),(4,6),(6,8),(8,6)\}
$$
R is reflexive since $a \in A,(a, a) \in R$
$R$ is symmetric since $(a, b) \in R$
$$
\Rightarrow(b, a) \in R \quad \text { for } a, b \in R
$$
$R$ is not transitive since $(4,6),(6,8) \in R, \operatorname{but}(4,8) \notin R$
$R$ is reflexive and symmetric but not transitive.
iv. $R=\left\{(a, b): a^{3}>b^{3}\right\}$
$$
(a, a) \in R
$$
$R$ is reflexive.
$$
\begin{aligned}
& (2,1) \in R \\
& \operatorname{But}(1,2) \notin R
\end{aligned}
$$

∴ R is not symmetric.

$$
\begin{aligned}
& (a, b),(b, c) \in R \\
& \Rightarrow a^{3} \geq b^{3} \text { and } b^{3}<c^{3} \\
& \Rightarrow a^{3}<c^{3} \\
& \Rightarrow(a, c) \in R
\end{aligned}
$$

∴ R is transitive.
R is reflexive and transitive but not symmetric
v.

$$
A=\{1,3,5\} \quad \text { Define a Relation } \mathrm{R}
$$

On A.

$$
\begin{gathered}
R: A \rightarrow A \\
R=\{(1,3)(3,1)(1,1)(3,3)\}
\end{gathered}
$$

Relation $R$ is not Reflexive as $(5,5) \not \subset R$
Relation $R$ is Symmetric as

$$
(1,3) \in R \Rightarrow(3,1) \in R
$$

Relation $R$ is Transitive

$$
\begin{aligned}
& (a, b) \in R,(b, c) \in R \Rightarrow(a, c) \in R \\
& (3,1) \in R,(1,1) \in R \Rightarrow(3,1) \in R
\end{aligned}
$$

## Alternative Answer

$R=(a, b): a$ is brother of $b$ \{suppose $a$ and $b$ are male\}
Ref $\rightarrow a$ is not brother of $a$
So, $(a, a) \not \subset R$
Relation $R$ is not Reflexive
Symmetric → a is brother of b so
$b$ is brother of $a$

$$
a, b \in \mathrm{R} \Rightarrow(b, a) \in \mathrm{R}
$$

Transitive → a is brother of b and
$b$ is brother of $c$ so
$a$ is brother of $c$

$$
(a, b) \in R,(b, c) \in R \Rightarrow(a, c) \in R
$$
:::

:::

:::question{number="1.11" kind="exercise" id="q_1.11" topic="Equivalence relation - equidistant points"}
#### Question 1.11

:::prompt
Show that the relation R in the set A of points in a plane given by $\mathrm{R}=\{(\mathrm{P}, \mathrm{Q}):$ distance of the point P from the origin is same as the distance of the point Q from the origin\}, is an equivalence relation. Further, show that the set of all points related to a point $\mathrm{P} \neq(0,0)$ is the circle passing through P with origin as centre.
:::

:::solution{label="Solution"}
$R=\{(P, Q)$ : Distance of the point P from the origin is same as the distance of the point Q from the origin $\}$
Clearly, $(P, P) \in R$
R is reflexive.

$$
(P, Q) \in R
$$

Clearly R is symmetric.

$$
(P, Q),(Q, S) \in R
$$

⇒ The distance of $P$ and $Q$ from the origin is the same and also, the distance of $Q$ and $S$ from the origin is the same.
⇒ The distance of $P$ and $S$ from the origin is the same.

$$
(P, S) \in R
$$

R is transitive.
R is an equivalence relation.

The set of points related to $P \neq(0,0)$ will be those points whose distance from origin is same as distance of $P$ from the origin.

Set of points forms a circle with the centre as origin and this circle passes through $P$.
:::

:::

:::question{number="1.12" kind="exercise" id="q_1.12" topic="Equivalence relation - similar triangles"}
#### Question 1.12

:::prompt
Show that the relation $R$ defined in the set $A$ of all triangles as $R=\left\{\left(T_{1}, T_{2}\right): T_{1}\right.$ is similar to $\left.\mathrm{T}_{2}\right\}$, is equivalence relation. Consider three right angle triangles $\mathrm{T}_{1}$ with sides 3, 4, 5, $\mathrm{T}_{2}$ with sides 5, 12, 13 and $\mathrm{T}_{3}$ with sides 6, 8, 10. Which triangles among $\mathrm{T}_{1}, \mathrm{~T}_{2}$ and $\mathrm{T}_{3}$ are related?
:::

:::solution{label="Solution"}
$$
R=\left\{\left(T_{1}, T_{2}\right): T_{1} \text { is similar to } T_{2}\right\}
$$

R is reflexive since every triangle is similar to itself.

$$
\text { If }\left(T_{1}, T_{2}\right) \in R \text {, then } T_{1} \text { is similar to } T_{2} \text {. }
$$

$T_{2}$ is similar to $T_{1}$.

$$
\Rightarrow\left(T_{2}, T_{1}\right) \in R
$$

R is symmetric.

$$
\left(T_{1}, T_{2}\right),\left(T_{2}, T_{3}\right) \in R
$$

is similar to $T_{2}$ and $T_{2}$ is similar to $T_{3}$.
$\therefore T_{1}$ is similar to $T_{3}$.
$\Rightarrow\left(T_{1}, T_{3}\right) \in R$
∴ R is transitive.
$\frac{3}{6}=\frac{4}{8}=\frac{5}{10}=\left(\frac{1}{2}\right)$
∴ Corresponding sides of triangles $T_{1 \text { and }} T_{3}$ are in the same ratio.
Triangle $T_{1}$ is similar to triangle $T_{3}$.
Hence, $T_{1}$ is related to $T_{3}$.
:::

:::

:::question{number="1.13" kind="exercise" id="q_1.13" topic="Equivalence relation - polygon sides"}
#### Question 1.13

:::prompt
Show that the relation R defined in the set A of all polygons as $\mathrm{R}=\left\{\left(\mathrm{P}_{1}, \mathrm{P}_{2}\right)\right.$ : $P_{1}$ and $P_{2}$ have same number of sides\}, is an equivalence relation. What is the set of all elements in A related to the right angle triangle T with sides 3, 4 and 5?
:::

:::solution{label="Solution"}
$R=\left\{\left(P_{1}, P_{2}\right): P_{1}\right.$ and $P_{2}$ have same number of sides $\}$
$\left(P_{1}, P_{2}\right) \in R$ as same polygon has same number of sides.
∴ R is reflexive.

$$
\left(P_{1}, P_{2}\right) \in R
$$

$\Rightarrow P_{1}$ and $P_{2}$ have same number of sides.
$\Rightarrow P_{2}$ and $P_{1}$ have same number of sides.

$$
\Rightarrow\left(P_{2}, P_{1}\right) \in R
$$

∴ R is symmetric.

$$
\left(P_{1}, P_{2}\right),\left(P_{2}, P_{3}\right) \in R
$$

$\Rightarrow P_{1}$ and $P_{2}$ have same number of sides.
$P_{2}$ and $P_{3}$ have same number of sides.
$\Rightarrow P_{1}$ and $P_{3}$ have same number of sides.

$$
\Rightarrow\left(P_{1}, P_{3}\right) \in R
$$

$\therefore \mathrm{R}$ is transitive.
$R$ is an equivalence relation.
The elements in A related to right-angled triangle (T) with sides 3,4,5 are those polygons which have three sides.
Set of all elements in a related to triangle T is the set of all triangles.
:::

:::

:::question{number="1.14" kind="exercise" id="q_1.14" topic="Equivalence relation - parallel lines"}
#### Question 1.14

:::prompt
Let L be the set of all lines in XY plane and R be the relation in L defined as $\mathrm{R}=\left\{\left(\mathrm{L}_{1}, \mathrm{~L}_{2}\right): \mathrm{L}_{1}\right.$ is parallel to $\left.\mathrm{L}_{2}\right\}$. Show that R is an equivalence relation. Find the set of all lines related to the line $y=2 x+4$.
:::

:::solution{label="Solution"}
$$
R=\left\{\left(L_{1}, L_{2}\right): L_{1} \text { is parallel to } \mathrm{L}_{2}\right\}
$$

R is reflexive as any line $L_{1}$ is parallel to itself i.e., $\left(L_{1}, L_{2}\right) \in R$

$$
\begin{aligned}
& \text { If }\left(L_{1}, L_{2}\right) \in R, \text { then } \\
& \Rightarrow L_{1} \text { is parallel to } L_{2} . \\
& \Rightarrow L_{2} \text { is parallel to } L_{1} .
\end{aligned}
$$

$$
\Rightarrow\left(L_{2}, L_{1}\right) \in R
$$

∴ R is symmetric.

$$
\begin{aligned}
& \left(L_{1}, L_{2}\right),\left(L_{2}, L_{3}\right) \in R \\
& \Rightarrow L_{1} \text { is parallel to } L_{2} \\
& \Rightarrow L_{2} \text { is parallel to } L_{3} \\
& \therefore L_{1} \text { is parallel to } L_{3} . \\
& \Rightarrow\left(L_{1}, L_{3}\right) \in R \\
& \therefore R \text { is transitive. }
\end{aligned}
$$

R is an equivalence relation.
Set of all lines related to the line $y=2 x+4$ is the set of all lines that are parallel to the line $y=2 x+4$.
Slope of the line $y=2 x+4$ is $m=2$.
Line parallel to the given line is in the form $y=2 x+c$, where $c \in R$.
Set of all lines related to the given line is given by $y=2 x+c$, where $c \in R$.
:::

:::

:::question{number="1.15" kind="exercise" id="q_1.15" topic="MCQ - relation properties on {1,2,3,4}"}
#### Question 1.15

:::prompt
Let R be the relation in the set $\{1,2,3,4\}$ given by $\mathrm{R}=\{(1,2),(2,2),(1,1),(4,4)$, (1, 3), (3, 3), (3, 2)\}. Choose the correct answer.
    (A) R is reflexive and symmetric but not transitive.
    (B) R is reflexive and transitive but not symmetric.
    (C) R is symmetric and transitive but not reflexive.
    (D) R is an equivalence relation.
:::

:::solution{label="Solution"}
$$
\begin{aligned}
& R=\{(1,2)(2,2),(1,1),(4,4),(1,3),(3,3),(3,2)\} \\
& (a, a) \in R \text { for every } a \in\{1,2,3.4\}
\end{aligned}
$$

∴ R is reflexive.

$$
(1,2) \in R \text { but }(2,1) \notin R
$$

∴ R is not symmetric.

$$
(a, b),(b, c) \in R \text { for all } a, b, c \in\{1,2,3,4\}
$$

∴ R is not transitive.
R is reflexive and transitive but not symmetric.

The correct answer is B.
:::

:::answer
**Answer:** B
:::

:::

:::question{number="1.16" kind="exercise" id="q_1.16" topic="MCQ - relation membership a=b-2"}
#### Question 1.16

:::prompt
Let R be the relation in the set $\mathbf{N}$ given by $\mathrm{R}=\{(a, b): a=b-2, b>6\}$. Choose the correct answer.
(A) $(2,4) \in \mathrm{R}$
(B) $(3,8) \in \mathrm{R}$
(C) $(6,8) \in \mathrm{R}$
(D) $(8,7) \in \mathrm{R}$
:::

:::solution{label="Solution"}
$$
R=\{(a, b): a=b-2, b>6\}
$$

Now,

$$
\begin{aligned}
& b>6,(2,4) \notin R \\
& 3 \neq 8-2 \\
& \therefore(3,8) \notin R \text { and as } 8 \neq 7-2 \\
& \therefore(8,7) \notin R
\end{aligned}
$$

Consider $(6,8)$

$$
\begin{aligned}
& 8>6 \text { and } 6=8-2 \\
& \therefore(6,8) \in R
\end{aligned}
$$

The correct answer is C .
:::

:::answer
**Answer:** C
:::

:::

:::question{number="1.17" kind="exercise" id="q_1.17" topic="One-one onto - reciprocal function"}
#### Question 1.17

:::prompt
Show that the function $f: \mathbf{R}_{*} \rightarrow \mathbf{R}_{*}$ defined by $f(x)=\frac{1}{x}$ is one-one and onto, where $\mathbf{R}_{*}$ is the set of all non-zero real numbers. Is the result true, if the domain $\mathbf{R}_{*}$ is replaced by $\mathbf{N}$ with co-domain being same as $\mathbf{R}_{*}$ ?
:::

:::solution{label="Solution"}
$f: R_{\bullet} \rightarrow R_{\bullet}$ is by $f(x)=\frac{1}{x}$
For one-one:

$$
\begin{aligned}
& x, y \in R_{\cdot} \text { such that } f(x)=f(y) \\
& \Rightarrow \frac{1}{x}=\frac{1}{y} \\
& \Rightarrow x=y
\end{aligned}
$$

$\therefore f$ is one-one.
For onto:
For $y \in R$, there exists $x=\frac{1}{y} \in R_{\bullet}[$ as $y \notin 0]$ such that

$$
f(x)=\frac{1}{\left(\frac{1}{y}\right)}=y
$$

$\therefore f$ is onto.
Given function $f$ is one-one and onto.

Consider function $g: N \rightarrow R_{\bullet \text { defined by }} g(x)=\frac{1}{x}$
We have, $g\left(x_{1}\right)=g\left(x_{2}\right) \Rightarrow \frac{1}{x_{1}}=\frac{1}{x_{2}} \Rightarrow x_{1}=x_{2}$
$\therefore g$ is one-one.
$g$ is not onto as for $1.2 \in R_{\bullet}$ there exist any $x$ in $N$ such that $g(x)=\frac{1}{1.2}$
Function $g$ is one-one but not onto.
:::

:::

:::question{number="1.18" kind="exercise" id="q_1.18" topic="Injectivity and surjectivity of x^2, x^3"}
#### Question 1.18

:::prompt
Check the injectivity and surjectivity of the following functions:
    (i) $f: \mathbf{N} \rightarrow \mathbf{N}$ given by $f(x)=x^{2}$
    (ii) $f: \mathbf{Z} \rightarrow \mathbf{Z}$ given by $f(x)=x^{2}$
    (iii) $f: \mathbf{R} \rightarrow \mathbf{R}$ given by $f(x)=x^{2}$
    (iv) $f: \mathbf{N} \rightarrow \mathbf{N}$ given by $f(x)=x^{3}$
    (v) $f: \mathbf{Z} \rightarrow \mathbf{Z}$ given by $f(x)=x^{3}$
:::

:::solution{label="Solution"}
i. For $f: N \rightarrow N$ given by $f(x)=x^{2}$
$$
\begin{aligned}
& x, y \in N \\
& f(x)=f(y) \Rightarrow x^{2}=y^{2} \Rightarrow x=y
\end{aligned}
$$
$\therefore f$ is injective.

$2 \in N$. But, there does not exist any $x$ in $N$ such that $f(x)=x^{2}=2$
$\therefore f$ is not surjective
Function $f$ is injective but not surjective.
ii. $\quad f: Z \rightarrow Z$ given by $f(x)=x^{2}$
$f(-1)=f(1)=1$ but $-1 \neq 1$
$\therefore f$ is not injective.
$-2 \in Z$ But, there does not exist any $x \in Z$ such that $f(x)=-2 \Rightarrow x^{2}=-2$
$\therefore f$ is not surjective.
Function $f$ is neither injective nor surjective.
iii. $\quad f: R \rightarrow R$ given by $f(x)=x^{2}$
$f(-1)=f(1)=1$ but $-1 \neq 1$
$\therefore f$ is not injective.
$-2 \in Z$ But, there does not exist any $x \in Z$ such that $f(x)=-2 \Rightarrow x^{2}=-2$
$\therefore f$ is not surjective.
Function $f$ is neither injective nor surjective.
iv. $\quad f: N \rightarrow N$ given by $f(x)=x^{3}$
$x, y \in N$
$f(x)=f(y) \Rightarrow x^{3}=y^{3} \Rightarrow x=y$
$\therefore f$ is injective.
$2 \in N$. But, there does not exist any $x$ in $N$ such that $f(x)=x^{3}=2$
$\therefore f$ is not surjective
Function $f$ is injective but not surjective.
v. $\quad f: Z \rightarrow Z$ given by $f(x)=x^{3}$
$x, y \in Z$
$f(x)=f(y) \Rightarrow x^{3}=y^{3} \Rightarrow x=y$
$\therefore f$ is injective.
$2 \in Z$. But, there does not exist any $x$ in $Z$ such that $f(x)=x^{3}=2$
$\therefore f$ is not surjective.
Function $f$ is injective but not surjective.
:::

:::

:::question{number="1.19" kind="exercise" id="q_1.19" topic="Greatest integer function"}
#### Question 1.19

:::prompt
Prove that the Greatest Integer Function $f: \mathbf{R} \rightarrow \mathbf{R}$, given by $f(x)=[x]$, is neither one-one nor onto, where $[x]$ denotes the greatest integer less than or equal to $x$.
:::

:::solution{label="Solution"}
$f: R \rightarrow R$ given by $f(x)=[x]$

$$
f(1.2)=[1.2]=1, f(1.9)=[1.9]=1
$$

$\therefore f(1.2)=f(1.9)$, but $1.2 \neq 1.9$
$\therefore f$ is not one-one.
Consider $0.7 \in R$
$f(x)=[x]$ is an integer. There does not exist any element $x \in R$ such that $f(x)=0.7$
$\therefore f$ is not onto.
The greatest integer function is neither one-one nor onto.
:::

:::

:::question{number="1.20" kind="exercise" id="q_1.20" topic="Modulus function"}
#### Question 1.20

:::prompt
Show that the Modulus Function $f: \mathbf{R} \rightarrow \mathbf{R}$, given by $f(x)=|x|$, is neither oneone nor onto, where $|x|$ is $x$, if $x$ is positive or 0 and $|x|$ is $-x$, if $x$ is negative.
:::

:::solution{label="Solution"}
$f: R \rightarrow R$ is $f(x)=|x|=\left\{\begin{array}{l}\mathrm{x}, \text { if } \mathrm{x} \geq 0 \\ -x, \text { if } \mathrm{x}<0\end{array}\right\}$

$$
f(-1)=|-1|=1 \text { and } f(1)=|1|=1
$$

$\therefore f(-1)=f(1)$ but $-1 \neq 1$
$\therefore f$ is not one-one.
Consider $-1 \in R$
$f(x)=|x|$ is non-negative. There exist any element $x$ in domain $R$ such that $f(x)=|x|=-1$
$\therefore f$ is not onto.
The modulus function is neither one-one nor onto.
:::

:::

:::question{number="1.21" kind="exercise" id="q_1.21" topic="Signum function"}
#### Question 1.21

:::prompt
Show that the Signum Function $f: \mathbf{R} \rightarrow \mathbf{R}$, given by
$$
f(x)=\begin{array}{r}
1, \text { if } x>0 \\
0, \text { if } x=0 \\
1, \text { if } x<0
\end{array}
$$
is neither one-one nor onto.
:::

:::solution{label="Solution"}
$f: R \rightarrow R$ is

$$
f(x)=\left\{\begin{array}{l}
1, \text { if } \mathrm{x}>0 \\
0, \text { if } \mathrm{x}=0 \\
-1, \text { if } \mathrm{x}<0
\end{array}\right\}
$$

$f(1)=f(2)=1$, but $1 \neq 2$
$\therefore f$ is not one-one.
$f(x)$ takes only 3 values $(1,0,-1)$ for the element -2 in co-domain
R, there does not exist any $x$ in domain R such that $f(x)=-2$.
$\therefore f$ is not onto.
The signum function is neither one-one nor onto.
:::

:::

:::question{number="1.22" kind="exercise" id="q_1.22" topic="One-one function on finite sets"}
#### Question 1.22

:::prompt
Let $\mathrm{A}=\{1,2,3\}, \mathrm{B}=\{4,5,6,7\}$ and let $f=\{(1,4),(2,5),(3,6)\}$ be a function from A to B . Show that $f$ is one-one.
:::

:::solution{label="Solution"}
$$
A=\{1,2,3\}, B=\{4,5,6,7\}
$$

$f: A \rightarrow B$ is defined as $f=\{(1,4),(2,5),(3,6)\}$
$\therefore f(1)=4, f(2)=5, f(3)=6$
It is seen that the images of distinct elements of $A$ under $f$ are distinct.
$\therefore f$ is one-one.
:::

:::

:::question{number="1.23" kind="exercise" id="q_1.23" topic="One-one, onto or bijective functions"}
#### Question 1.23

:::prompt
In each of the following cases, state whether the function is one-one, onto or bijective. Justify your answer.
    (i) $f: \mathbf{R} \rightarrow \mathbf{R}$ defined by $f(x)=3-4 x$
    (ii) $f: \mathbf{R} \rightarrow \mathbf{R}$ defined by $f(x)=1+x^{2}$
:::

:::solution{label="Solution"}
i. $\quad f: R \rightarrow R$ defined by $f(x)=3-4 x$
$x_{1}, x_{2} \in R$ such that $f\left(x_{1}\right)=f\left(x_{2}\right)$
$\Rightarrow 3-4 x_{1}=3-4 x_{2}$
$\Rightarrow-4 x=-4 x_{2}$
$\Rightarrow x_{1}=x_{2}$
$\therefore f$ is one-one.
For any real number $(y)$ in $R$, there exists $\frac{3-y}{4}$ in $R$ such that $f\left(\frac{3-y}{4}\right)=3-4\left(\frac{3-y}{4}\right)=y$
$\therefore f$ is onto.
Hence, $f$ is bijective.
ii. $\quad f: R \rightarrow R$ defined by $f(x)=1+x^{2}$
$x_{1}, x_{2} \in R$ such that $f\left(x_{1}\right)=f\left(x_{2}\right)$
$\Rightarrow 1+x_{1}{ }^{2}=1+x_{2}{ }^{2}$
$\Rightarrow x_{1}{ }^{2}=x_{2}{ }^{2}$
$\Rightarrow x_{1}= \pm x_{2}$
$\therefore f\left(x_{1}\right)=f\left(x_{2}\right)$ does not imply that $x_{1}=x_{2}$
Consider $f(1)=f(-1)=2$
$\therefore f$ is not one-one.
Consider an element -2 in co domain $R$.
It is seen that $f(x)=1+x^{2}$ is positive for all $x \in R$.
$\therefore f$ is not onto.
Hence, $f$ is neither one-one nor onto.
:::

:::

:::question{number="1.24" kind="exercise" id="q_1.24" topic="Bijective function A x B to B x A"}
#### Question 1.24

:::prompt
Let A and B be sets. Show that $f: \mathrm{A} \times \mathrm{B} \rightarrow \mathrm{B} \times \mathrm{A}$ such that $f(a, b)=(b, a)$ is bijective function.
:::

:::solution{label="Solution"}
$f: A \times B \rightarrow B \times A$ is defined as $(a, b)=(b, a)$.
$\left(a_{1}, b_{1}\right),\left(a_{2}, b_{2}\right) \in A \times B$ such that $f\left(a_{1}, b_{1}\right)=f\left(a_{2}, b_{2}\right)$

$$
\begin{aligned}
& \Rightarrow\left(b_{1}, a_{1}\right)=\left(b_{2}, a_{2}\right) \\
& \Rightarrow b_{1}=b_{2} \text { and } a_{1}=a_{2} \\
& \Rightarrow\left(a_{1}, b_{1}\right)=\left(a_{2}, b_{2}\right) \\
& \therefore f \text { is one-one. } \\
& (b, a) \in B \times A \text { there exist }(a, b) \in A \times B \text { such that } f(a, b)=(b, a) \\
& \therefore f \text { is onto. } \\
& f \text { is bijective. }
\end{aligned}
$$
:::

:::

:::question{number="1.25" kind="exercise" id="q_1.25" topic="Bijective piecewise function (garbled source)" corrections_applied="1"}
#### Question 1.25

:::prompt
Let $f: \mathbf{N} \rightarrow \mathbf{N}$ be defined by $f(n)=\left\{\begin{array}{ll}\frac{n+1}{2}, & \text { if } n \text { is odd } \\\frac{n}{2}, & \text { if } n \text { is even }\end{array}\right.$ for all $n \in \mathbf{N}$.
State whether the function $f$ is bijective. Justify your answer.
:::

:::solution{label="Solution"}
$$
f(n)=\left\{\begin{array}{l}
\frac{n+1}{2}, \text { if } n \text { is odd } \\
\frac{n}{2}, \text { if } n \text { is even }
\end{array}\right\} \text { for all } n \in N .
$$

$$
\begin{aligned}
& f(1)=\frac{1+1}{2}=1 \text { and } f(2)=\frac{2}{2}=1 \\
& f(1)=f(2), \text { where } 1 \neq 2
\end{aligned}
$$

$\therefore f$ is not one-one.

Consider a natural number $n$ in co domain $N$.

Case I: $n$ is odd

$$
\begin{aligned}
& \therefore n=2 r+1 \text { for some } r \in N \text { there exists } 4 r+1 \in N \text { such that } \\
& f(4 r+1)=\frac{4 r+1+1}{2}=2 r+1
\end{aligned}
$$

Case II: $n$ is even

$$
\begin{aligned}
& \therefore n=2 r \text { for some } r \in N \text { there exists } 4 r \in N \text { such that } \\
& f(4 r)=\frac{4 r}{2}=2 r \\
& \therefore f \text { is onto. }
\end{aligned}
$$

$f$ is not a bijective function.
:::

:::

:::question{number="1.26" kind="exercise" id="q_1.26" topic="One-one onto - rational function"}
#### Question 1.26

:::prompt
Let $\mathrm{A}=\mathbf{R}-\{3\}$ and $\mathrm{B}=\mathbf{R}-\{1\}$. Consider the function $f: \mathrm{A} \rightarrow \mathrm{B}$ defined by $f(x)=\left(\frac{x-2}{x-3}\right)$. Is $f$ one-one and onto? Justify your answer.
:::

:::solution{label="Solution"}
$$
\begin{aligned}
& A=R-\{3\}, B=R-\{1\} \text { and } f: A \rightarrow B \text { defined by } f(x)=\left(\frac{x-2}{x-3}\right) \\
& x, y \in A \text { such that } f(x)=f(y) \\
& \Rightarrow \frac{x-2}{x-3}=\frac{y-2}{y-3} \\
& \Rightarrow(x-2)(y-3)=(y-2)(x-3) \\
& \Rightarrow x y-3 x-2 y+6=x y-3 y-2 x+6 \\
& \Rightarrow-3 x-2 y=-3 y-2 x \\
& \Rightarrow 3 x-2 x=3 y-2 y \\
& \Rightarrow x=y \\
& \therefore f \text { is one-one. }
\end{aligned}
$$

Let $y \in B=R-\{1\}$, then $y \neq 1$
The function $f$ is onto if there exists $x \in A$ such that $f(x)=y$.
Now,

$$
\begin{aligned}
& f(x)=y \\
& \Rightarrow \frac{x-2}{x-3}=y \\
& \Rightarrow x-2=x y-3 y \\
& \Rightarrow x(1-y)=-3 y+2 \\
& \Rightarrow x=\frac{2-3 y}{1-y} \in A \quad[y \neq 1]
\end{aligned}
$$

Thus, for any $y \in B$, there exists $\frac{2-3 y}{1-y} \in A$ such that

$$
f\left(\frac{2-3 y}{1-y}\right)=\frac{\left(\frac{2-3 y}{1-y}\right)-2}{\left(\frac{2-3 y}{1--y}\right)-3}=\frac{2-3 y-2+2 y}{2-3 y-3+3 y}=\frac{-y}{-1}=y
$$

$\therefore f$ is onto.
Hence, the function is one-one and onto.
:::

:::

:::question{number="1.27" kind="exercise" id="q_1.27" topic="MCQ - f(x) = x^4"}
#### Question 1.27

:::prompt
Let $f: \mathbf{R} \rightarrow \mathbf{R}$ be defined as $f(x)=x^{4}$. Choose the correct answer.
(A) $f$ is one-one onto
(B) $f$ is many-one onto
(C) $f$ is one-one but not onto
(D) $f$ is neither one-one nor onto.
:::

:::solution{label="Solution"}
$f: R \rightarrow R$ defined as $f(x)=x^{4}$
$x, y \in R$ such that $f(x)=f(y)$
$\Rightarrow x^{4}=y^{4}$
$\Rightarrow x= \pm y$
$\therefore f(x)=f(y)$ does not imply that $x=y$.
For example $f(1)=f(-1)=1$
$\therefore f$ is not one-one.
Consider an element 2 in co domain $R$ there does not exist any $x$ in domain $R$ such that $f(x)=2$.
$\therefore f$ is not onto.
Function $f$ is neither one-one nor onto.
The correct answer is D.
:::

:::answer
**Answer:** D
:::

:::

:::question{number="1.28" kind="exercise" id="q_1.28" topic="MCQ - f(x) = 3x"}
#### Question 1.28

:::prompt
Let $f: \mathbf{R} \rightarrow \mathbf{R}$ be defined as $f(x)=3 x$. Choose the correct answer.
(A) $f$ is one-one onto
(B) $f$ is many-one onto
(C) $f$ is one-one but not onto
(D) $f$ is neither one-one nor onto.
:::

:::solution{label="Solution"}
$f: R \rightarrow R$ defined as $f(x)=3 x$
$x, y \in R$ such that $f(x)=f(y)$
$\Rightarrow 3 x=3 y$
$\Rightarrow x=y$
$\therefore f$ is one-one.
For any real number $y$ in co domain R, there exist $\frac{y}{3}$ in R such that $f\left(\frac{y}{3}\right)=3\left(\frac{y}{3}\right)=y$
$\therefore f$ is onto.
Hence, function $f$ is one-one and onto.
The correct answer is A.
:::

:::answer
**Answer:** A
:::

:::

:::question{number="1.29" kind="exercise" id="q_1.29" topic="One-one onto function x/(1+|x|)"}
#### Question 1.29

:::prompt
Show that the function $f: \mathbf{R} \rightarrow\{x \in \mathbf{R}:-1<x<1\}$ defined by $f(x)=\frac{x}{1+|x|}$, $x \in \mathbf{R}$ is one one and onto function.
:::

:::solution{label="Solution"}
$f: R \rightarrow\{x \in R:-1<x<1\}$ is defined by $f(x)=\frac{x}{1+|x|}, x \in R$.
For one-one:

$$
f(x)=f(y) \quad \text { where } x, y \in R
$$

$$
\Rightarrow \frac{x}{1+|x|}=\frac{y}{1+|y|}
$$

If $x$ is positive and $y$ is negative,

$$
\begin{aligned}
& \frac{x}{1+|x|}=\frac{y}{1+|y|} \\
& \Rightarrow 2 x y=x-y
\end{aligned}
$$

Since, $x$ is positive and $y$ is negative,

$$
x>y \Rightarrow x-y>0
$$

$2 x y$ is negative.

$$
2 x y \neq x-y
$$

Case of $x$ being positive and $y$ being negative, can be ruled out.
$\therefore x$ and $y$ have to be either positive or negative.
If $x$ and $y$ are positive,

$$
\begin{aligned}
& f(x)=f(y) \\
& \Rightarrow \frac{x}{1+x}=\frac{y}{1+y} \\
& \Rightarrow x-x y=y-x y \\
& \Rightarrow x=y \\
& \therefore f \text { is one-one. }
\end{aligned}
$$

For onto:

Let $y \in R$ such that $-1<y<1$.
If $x$ is negative, then there exists $x=\frac{y}{1+y} \in R$ such that

$$
f(x)=f\left(\frac{y}{1+y}\right)=\frac{\left(\frac{y}{1+y}\right)}{1+\left|\frac{y}{1+y}\right|}=\frac{\frac{y}{1+y}}{1+\left(\frac{-y}{1+y}\right)}=\frac{y}{1+y-y}=y
$$

If $x$ is positive, then there exists $x=\frac{y}{1-y} \in R$ such that

$$
f(x)=f\left(\frac{y}{1-y}\right)=\frac{\left(\frac{y}{1-y}\right)}{1+\left|\frac{y}{1-y}\right|}=\frac{\frac{y}{1-y}}{1+\left(\frac{y}{1-y}\right)}=\frac{y}{1-y+y}=y
$$

$\therefore f$ is onto.
Hence, $f$ is one-one and onto.
:::

:::

:::question{number="1.30" kind="exercise" id="q_1.30" topic="Injective function x^3"}
#### Question 1.30

:::prompt
Show that the function $f: \mathbf{R} \rightarrow \mathbf{R}$ given by $f(x)=x^{3}$ is injective.
:::

:::solution{label="Solution"}
$$
f: R \rightarrow R \text { is defined by } f(x)=x^{3}
$$

For one-one:

$$
\begin{aligned}
& f(x)=f(y) \quad \text { where } x, y \in R \\
& x^{3}=y^{3} \ldots \ldots \ldots \ldots \ldots \ldots \ldots . .(1)
\end{aligned}
$$

We need to show that $x=y$
Suppose $x \neq y$, their cubes will also not be equal.

$$
\Rightarrow x^{3} \neq y^{3}
$$

This will be contradiction to (1).
$\therefore x=y$. Hence, $f$ is injective.
:::

:::

:::question{number="1.31" kind="exercise" id="q_1.31" topic="Equivalence relation on power set"}
#### Question 1.31

:::prompt
Given a non empty set X , consider $\mathrm{P}(\mathrm{X})$ which is the set of all subsets of X . Define the relation R in P(X) as follows:
For subsets A, B in P(X), ARB if and only if $\mathrm{A} \subset \mathrm{B}$. Is R an equivalence relation on P(X)? Justify your answer.
:::

:::solution{label="Solution"}
Since every set is a subset of itself, $A R A$ for all $A \in P(X)$.
$\therefore R$ is reflexive.

Let $A R B \Rightarrow A \subset B$
This cannot be implied to $B \subset A$.
If $A=\{1,2\}$ and $B=\{1,2,3\}$, then it cannot be implied that $B$ is related to $A$.
$\therefore R$ is not symmetric.
If $A R B$ and $B R C$, then $A \subset B$ and $B \subset C$.

$$
\begin{aligned}
& \Rightarrow A \subset C \\
& \Rightarrow A R C
\end{aligned}
$$

$\therefore R$ is transitive.
$R$ is not an equivalence relation as it is not symmetric.
:::

:::

:::question{number="1.32" kind="exercise" id="q_1.32" topic="Counting onto functions"}
#### Question 1.32

:::prompt
Find the number of all onto functions from the set $\{1,2,3, \ldots \ldots, n\}$ to itself.
:::

:::solution{label="Solution"}
Onto functions from the set $\{1,2,3, \ldots, n\}$ to itself is simply a permutation on $n$ symbols $1,2,3, \ldots, n$.
Thus, the total number of onto maps from $\{1,2,3, \ldots, n\}$ to itself is the same as the total number of permutations on $n$ symbols $1,2,3, \ldots, n$, which is $n!$.
:::

:::

:::question{number="1.33" kind="exercise" id="q_1.33" topic="Equal functions check"}
#### Question 1.33

:::prompt
Let $\mathrm{A}=\{-1,0,1,2\}, \mathrm{B}=\{-4,-2,0,2\}$ and $f, g: \mathrm{A} \rightarrow \mathrm{B}$ be functions defined by $f(x)=x^{2}-x, x \in \mathrm{~A}$ and $g(x)=2\left|x-\frac{1}{2}\right|-1, x \in \mathrm{~A}$. Are $f$ and $g$ equal? Justify your answer. (Hint: One may note that two functions $f: \mathrm{A} \rightarrow \mathrm{B}$ and $g: \mathrm{A} \rightarrow \mathrm{B}$ such that $f(a)=g(a) \forall a \in \mathrm{~A}$, are called equal functions).
:::

:::solution{label="Solution"}
It is given that $A=\{-1,0,1,2\}, B=\{-4,-2,0,2\}$
Also, $f, g: A \rightarrow B$ is defined by $x^{2}-x, x \in A$ and $g(x)=2\left|x-\frac{1}{2}\right|-1, x \in A$.

$$
\begin{aligned}
& f(-1)=(-1)^{2}-(-1)=1+1=2 \\
& g(-1)=2\left|(-1)-\frac{1}{2}\right|-1=2\left(\frac{3}{2}\right)-1=3-1=2 \\
& \Rightarrow f(-1)=g(-1) \\
& f(0)=(0)^{2}-0=0 \\
& g(0)=2\left|0-\frac{1}{2}\right|-1=2\left(\frac{1}{2}\right)-1=1-1=0 \\
& \Rightarrow f(0)=g(0)
\end{aligned}
$$

$$
\begin{aligned}
& f(1)=(1)^{2}-1=0 \\
& g(1)=2\left|1-\frac{1}{2}\right|-1=2\left(\frac{1}{2}\right)-1=1-1=0 \\
& \Rightarrow f(1)=g(1)
\end{aligned}
$$

$$
\begin{aligned}
& f(2)=(2)^{2}-2=2 \\
& g(2)=2\left|2-\frac{1}{2}\right|-1=2\left(\frac{3}{2}\right)-1=3-1=2 \\
& \Rightarrow f(2)=g(2) \\
& \therefore f(a)=g(a) \quad \forall a \in A
\end{aligned}
$$

Hence, the functions $f$ and $g$ are equal.
:::

:::

:::question{number="1.34" kind="exercise" id="q_1.34" topic="MCQ - reflexive symmetric not transitive count"}
#### Question 1.34

:::prompt
Let $\mathrm{A}=\{1,2,3\}$. Then number of relations containing $(1,2)$ and $(1,3)$ which are reflexive and symmetric but not transitive is
(A) 1
(B) 2
(C) 3
(D) 4
:::

:::solution{label="Solution"}
The given set is $A=\{1,2,3\}$.
The smallest relation containing $(1,2)$ and $(1,3)_{\text {which }}$ are reflexive and symmetric but not transitive is given by,

$$
R=\{(1,1),(2,2),(3,3),(1,2),(1,3),(2,1),(3,1)\}
$$

This is because relation $R$ is reflexive as $\{(1,1),(2,2),(3,3)\} \in R$.
Relation $R$ is symmetric as $\{(1,2),(2,1)\} \in R$ and $\{(1,3)(3,1)\} \in R$.
Relation $R$ is transitive as $\{(3,1),(1,2)\} \in R$ but $(3,2) \notin R$.
Now, if we add any two pairs $(3,2)$ and $(2,3)$ (or both) to relation $R$, then relation $R$ will become transitive.
Hence, the total number of desired relations is one.
The correct answer is A.
:::

:::answer
**Answer:** A
:::

:::

:::question{number="1.35" kind="exercise" id="q_1.35" topic="MCQ - equivalence relations containing (1,2)"}
#### Question 1.35

:::prompt
Let $\mathrm{A}=\{1,2,3\}$. Then number of equivalence relations containing $(1,2)$ is
(A) 1
(B) 2
(C) 3
(D) 4
:::

:::solution{label="Solution"}
The given set is $A=\{1,2,3\}$.
The smallest equivalence relation containing $(1,2)$ is given by;

$$
R_{1}=\{(1,1),(2,2),(3,3),(1,2),(2,1)\}
$$

Now, we are left with only four pairs i.e., $(2,3),(3,2),(1,3)$ and $(3,1)$.
If we odd any one pair $[$ say $(2,3)]$ to $R_{1}$, then for symmetry we must add $(3,2)$. Also, for transitivity we are required to add $(1,3)$ and $(3,1)$.

Hence, the only equivalence relation (bigger than $R_{1}$ ) is the universal relation.
This shows that the total number of equivalence relations containing $(1,2)$ is two. The correct answer is B.
:::

:::answer
**Answer:** B
:::

:::

## Additional Questions

:::question{number="EX1.3-1" kind="additional_exercise" id="sol_1.3.1" topic="Composition gof of finite functions"}
#### Additional Question EX1.3-1

:::prompt
Let $f:\{1,3,4\} \rightarrow\{1,2,5\}$ and $g:\{1,2,5\} \rightarrow\{1,3\}$ be given by $f=\{(1,2),(3,5),(4,1)\}$ and $g=\{(1,3),(2,3),(5,1)\}$. Write down gof .
:::

:::solution{label="Solution"}
The functions $f:\{1,3,4\} \rightarrow\{1,2,5\}$ and $g:\{1,2,5\} \rightarrow\{1,3\}$ are $f=\{(1,2),(3,5),(4,1)\}$ and $g=\{(1,3),(2,3),(5,1)\}$

$$
\begin{array}{ll}
g o f(1)=g[f(1)]=g(2)=3 & {[\text { as } f(1)=2 \text { and } g(2)=3]} \\
g o f(3)=g[f(3)]=g(5)=1 & {[\text { as } f(3)=5 \text { and } g(5)=1]} \\
\text { gof }(4)=g[f(4)]=g(1)=3 & {[\text { as } f(4)=1 \text { and } g(1)=3]} \\
\therefore \text { gof }=\{(1,3),(3,1),(4,3)\} &
\end{array}
$$
:::

:::

:::question{number="EX1.3-2" kind="additional_exercise" id="sol_1.3.2" topic="Composition distributes over sum and product"}
#### Additional Question EX1.3-2

:::prompt
Let $f, g, h$ be functions from $R$ to $R$. Show that

$$
\begin{aligned}
& (f+g) o h=f o h+g o h \\
& (f \cdot g) o h=(f o h) \cdot(g o h)
\end{aligned}
$$
:::

:::solution{label="Solution"}
$$
\begin{aligned}
&(f+g) o h=f o h+g o h \\
& \text { LHS }=[(f+g) o h](x) \\
&=(f+g)[h(x)]=f[h(x)]+g[h(x)] \\
&=(f o h)(x)+g o h(x) \\
&=\{(f o h)+(g o h)\}(x)=\text { RHS } \\
& \therefore\{(f+g) o h\}(x)=\{(f o h)+(g o h)\}(x) \text { for all } x \in R
\end{aligned}
$$

Hence, $(f+g) o h=f o h+g o h$

$$
\begin{aligned}
(f . g) o h & =(f o h) \cdot(g o h) \\
\text { LHS } & =[(f \cdot g) o h](x) \\
& =(f \cdot g)[h(x)]=f[h(x)] \cdot g[h(x)] \\
& =(f o h)(x) \cdot(g o h)(x) \\
& =\{(f o h) \cdot(g o h)\}(x)=\text { RHS }
\end{aligned}
$$

$\therefore[(f . g) o h](x)=\{(f o h) .(g o h)\}(x)$ for all $x \in R$
Hence, $(f . g) o h=(f o h) .(g o h)$
:::

:::

:::question{number="EX1.3-3" kind="additional_exercise" id="sol_1.3.3" topic="gof and fog - modulus and cube root"}
#### Additional Question EX1.3-3

:::prompt
Find $g o f$ and $f o g$, if

i. $\quad f(x)=|x|$ and $g(x)=|5 x-2|$
ii. $f(x)=8 x^{3}$ and $g(x)=x^{\frac{1}{3}}$
:::

:::solution{label="Solution"}
i. $$
\begin{aligned}
& f(x)=|x| \text { and } g(x)=|5 x-2| \\
& \therefore g o f(x)=g(f(x))=g(|x|)=|5| x|-2| \\
& f \circ g(x)=f(g(x))=f(|5 x-2|)=\|5 x-2\|=|5 x-2|
\end{aligned}
$$
ii. $f(x)=8 x^{3}$ and $g(x)=x^{\frac{1}{3}}$
$$
\begin{aligned}
& \therefore g o f(x)=g(f(x))=g\left(8 x^{3}\right)=\left(8 x^{3}\right)^{\frac{1}{3}}=2 x \\
& f o g(x)=f(g(x))=f\left(x^{\frac{1}{3}}\right)^{3}=8\left(x^{\frac{1}{3}}\right)^{3}=8 x
\end{aligned}
$$
:::

:::

:::question{number="EX1.3-4" kind="additional_exercise" id="sol_1.3.4" topic="Self-inverse rational function"}
#### Additional Question EX1.3-4

:::prompt
If $f(x)=\frac{(4 x+3)}{(6 x-4)}, x \neq \frac{2}{3}$, show that $f \circ f(x)=x$, for all $x \neq \frac{2}{3}$. What is the reverse of $f$ ?
:::

:::solution{label="Solution"}
$$
\begin{aligned}
& (f o f)(x)=f(f(x))=f\left(\frac{4 x+3}{6 x-4}\right) \\
& \quad=\frac{4\left(\frac{4 x+3}{6 x-4}\right)+3}{6\left(\frac{4 x+3}{6 x-4}\right)-4}=\frac{16 x+12+18 x-12}{24 x+18-24 x+16}=\frac{34 x}{34}=x \\
& \therefore \text { fof }(x)=x \text { for all } x \neq \frac{2}{3} \\
& \Rightarrow \text { fof }=1
\end{aligned}
$$

Hence, the given function $f$ is invertible and the inverse of $f$ is $f$ itself.
:::

:::

:::question{number="EX1.3-5" kind="additional_exercise" id="sol_1.3.5" topic="Checking existence of inverse - three functions"}
#### Additional Question EX1.3-5

:::prompt
State with reason whether the following functions have inverse.

i. $\quad f:\{1,2,3,4\} \rightarrow\{10\}_{\text {with }} f=\{(1,10),(2,10),(3,10),(4,10)\}$
ii. $g:\{5,6,7,8\} \rightarrow\{1,2,3,4\}$ with $g=\{(5,4),(6,3),(7,4),(8,2)\}$
iii. $\quad h:\{2,3,4,5\} \rightarrow\{7,9,11,13\}$ with $h=\{(2,7),(3,9),(4,11),(5,13)\}$
:::

:::solution{label="Solution"}
i. $\quad f:\{1,2,3,4\} \rightarrow\{10\}_{\text {with }} f=\{(1,10),(2,10),(3,10),(4,10)\}$
$f$ is a many one function as $f(1)=f(2)=f(3)=f(4)=10$
$\therefore f$ is not one-one.
Function $f$ does not have an inverse.
ii. $\quad g:\{5,6,7,8\} \rightarrow\{1,2,3,4\}$ with $g=\{(5,4),(6,3),(7,4),(8,2)\}$
$g$ is a many one function as $g(5)=g(7)=4$
$\therefore g$ is not one-one.
Function $g$ does not have an inverse.
iii. $\quad h:\{2,3,4,5\} \rightarrow\{7,9,11,13\}$ with $h=\{(2,7),(3,9),(4,11),(5,13)\}$
All distinct elements of the set \{2,3,4,5\} have distinct images under $h$.
$\therefore h$ is one-one.
$h$ is onto since for every element $y$ of the set \{7,9,11,13\}, there exists an element $x$ in the set \{2,3,4,5\}, such that $h(x)=y$.
$h$ is a one-one and onto function.
Function $h$ has an inverse.
:::

:::

:::question{number="EX1.3-6" kind="additional_exercise" id="sol_1.3.6" topic="Inverse of a rational function on [-1,1]"}
#### Additional Question EX1.3-6

:::prompt
Show that $f:[-1,1] \rightarrow R$, given by $f(x)=\frac{x}{(x+2)}$ is one-one. Find the inverse of the function $f:[-1,1] \rightarrow$ Range $f$.
(Hint: For $y \in$ Range $f, y=f(x)=\frac{x}{x+2}$, for some $x$ in $[-1,1], i, e ., \quad x=\frac{2 y}{(1-y)}$
:::

:::solution{label="Solution"}
$f:[-1,1] \rightarrow R$, given by $f(x)=\frac{x}{(x+2)}$
For one-one

$$
\begin{aligned}
& f(x)=f(y) \\
& \Rightarrow \frac{x}{x+2}=\frac{y}{y+2} \\
& \Rightarrow x y+2 x=x y+2 y \\
& \Rightarrow 2 x=2 y \\
& \Rightarrow x=y
\end{aligned}
$$

$\therefore f$ is a one-one function.
It is clear that $f:[-1,1] \rightarrow R$ is onto.

$$
f:[-1,1] \rightarrow R \text { is one-one and onto and therefore, the inverse of the function } f:[-1,1] \rightarrow R
$$

exists.

Let $g:$ Range $f \rightarrow[-1,1]$ be the inverse of $f$.
Let $y$ be an arbitrary element of range $f$.
Since $f:[-1,1] \rightarrow$ Range $f$ is onto, we have:

$$
\begin{aligned}
& y=f(x) \text { for same } x \in[-1,1] \\
& \Rightarrow y=\frac{x}{x+2} \\
& \Rightarrow x y+2 y=x \\
& \Rightarrow x(1-y)=2 y \\
& \Rightarrow x=\frac{2 y}{1-y}, y \neq 1
\end{aligned}
$$

Now, let us define $g:$ Range $f \rightarrow[-1,1]$ as

$$
g(y)=\frac{2 y}{1-y}, y \neq 1
$$

Now,

$$
\begin{aligned}
& (g o f)(x)=g(f(x))=g\left(\frac{x}{x+2}\right)=\frac{2\left(\frac{x}{x+2}\right)}{1-\frac{x}{x+2}}=\frac{2 x}{x+2-x}=\frac{2 x}{2}=x \\
& (f o g)(x)=f(g(y))=f\left(\frac{2 y}{1-y}\right)=\frac{\frac{2 y}{1-y}}{\frac{2 y}{1-y}+2}=\frac{2 y}{2 y+2-2 y}=\frac{2 y}{2}=y \\
& \therefore g o f=I_{[-1,1]} \text { and } f o g=I_{\text {Range } f} \\
& \therefore f^{-1}=g \\
& \Rightarrow f^{-1}(y)=\frac{2 y}{1-y}, y \neq 1
\end{aligned}
$$
:::

:::

:::question{number="EX1.3-7" kind="additional_exercise" id="sol_1.3.7" topic="Invertible linear function 4x+3"}
#### Additional Question EX1.3-7

:::prompt
Consider $f: R \rightarrow R$ given by $f(x)=4 x+3$. Show that $f$ is invertible. Find the inverse of $f$.
:::

:::solution{label="Solution"}
$$
f: R \rightarrow R \text { given by } f(x)=4 x+3
$$

For one-one

$$
\begin{aligned}
& f(x)=f(y) \\
& \Rightarrow 4 x+3=4 y+3 \\
& \Rightarrow 4 x=4 y \\
& \Rightarrow x=y
\end{aligned}
$$

$\therefore f$ is a one-one function.

For onto

$$
\begin{aligned}
& y \in R, \text { let } y=4 x+3 \\
& \Rightarrow x=\frac{y-3}{4} \in R
\end{aligned}
$$

Therefore, for any $y \in R$, there exists $x=\frac{y-3}{4} \in R$ such that

$$
f(x)=f\left(\frac{y-3}{4}\right)=4\left(\frac{y-3}{4}\right)+3=y
$$

$\therefore f$ is onto.

Thus, f is one-one and onto and therefore, $f^{-1}$ exists.
Let us define $g: R \rightarrow R$ by $g(x)=\frac{y-3}{4}$

Now,

$$
\begin{aligned}
& (g o f)(x)=g(f(x))=g(4 x+3)=\frac{(4 x+3)-3}{4}=x \\
& (f o g)(y)=f(g(y))=f\left(\frac{y-3}{4}\right)=4\left(\frac{y-3}{4}\right)+3=y-3+3=y \\
& \therefore g o f=f o g=\mathrm{I}_{R}
\end{aligned}
$$

Hence, $f$ is invertible and the inverse of $f$ is given by

$$
f^{-1}(y)=g(y)=\frac{y-3}{4} .
$$
:::

:::

:::question{number="EX1.3-8" kind="additional_exercise" id="sol_1.3.8" topic="Invertible function x^2+4 on non-negative reals"}
#### Additional Question EX1.3-8

:::prompt
Consider $f: R_{+} \rightarrow[4, \infty)$ given by $f(x)=x^{2}+4$. Show that $f$ is invertible with inverse $f^{-1}$ of given $f$ by $f^{-1}(y)=\sqrt{y-4}$, where $R_{+}$is the set of all non-negative real numbers.
:::

:::solution{label="Solution"}
$$
f: R_{+} \rightarrow[4, \infty) \text { given by } f(x)=x^{2}+4
$$

For one-one:

$$
\begin{aligned}
& \text { Let } f(x)=f(y) \\
& \Rightarrow x^{2}+4=y^{2}+4 \\
& \Rightarrow x^{2}=y^{2} \\
& \Rightarrow x=y \quad \quad[\text { as } x \in R]
\end{aligned}
$$

$\therefore f$ is a one -one function.
For onto:
For $y \in[4, \infty)$, let $y=x^{2}+4$

$$
\begin{aligned}
& \Rightarrow x^{2}=y-4 \geq 0 \quad[\text { as } y \geq 4] \\
& \Rightarrow x=\sqrt{y-4} \geq 0
\end{aligned}
$$

Therefore, for any $y \in R$, there exists $x=\sqrt{y-4} \in R$ such that

$$
\begin{aligned}
& f(x)=f(\sqrt{y-4})=(\sqrt{y-4})^{2}+4=y-4+4=y \\
& \therefore f \text { is an onto function. }
\end{aligned}
$$

Thus, $f$ is one-one and onto and therefore, $f^{-1}$ exists.

Let us define $g:[4, \infty) \rightarrow R_{+}$by

$$
g(y)=\sqrt{y-4}
$$

Now, $\operatorname{gof}(x)=g(f(x))=g\left(x^{2}+4\right)=\sqrt{\left(x^{2}+4\right)-4}=\sqrt{x^{2}}=x$
And $f o g(y)=f(g(y))=f(\sqrt{y-4})=(\sqrt{y-4})^{2}+4=(y-4)+4=y$

$$
\therefore g o f=f o g=\mathrm{I}_{R}
$$

Hence, $f$ is invertible and the inverse of $f$ is given by

$$
f^{-1}(y)=g(y)=\sqrt{y-4} .
$$
:::

:::

:::question{number="EX1.3-9" kind="additional_exercise" id="sol_1.3.9" topic="Invertible quadratic function 9x^2+6x-5"}
#### Additional Question EX1.3-9

:::prompt
Consider $f: R_{+} \rightarrow[-5, \infty)$ given by $f(x)=9 x^{2}+6 x-5$. Show that $f$ is invertible with $f^{-1}(y)=\left(\frac{(\sqrt{y+6})-1}{3}\right)$.
:::

:::solution{label="Solution"}
$$
f: R_{+} \rightarrow[-5, \infty) \text { given by } f(x)=9 x^{2}+6 x-5
$$

Let $y$ be an arbitrary element of $[-5, \infty)$.
Let $y=9 x^{2}+6 x-5$

$$
\begin{aligned}
& \Rightarrow y=(3 x+1)^{2}-1-5 \\
& \Rightarrow y=(3 x+1)^{2}-6 \\
& \Rightarrow(3 x+1)^{2}=y+6 \\
& \Rightarrow 3 x+1=\sqrt{y+6} \quad[\text { as } y \geq-5 \Rightarrow y+6>0] \\
& \Rightarrow x=\frac{\sqrt{y+6}-1}{3}
\end{aligned}
$$

$\therefore f$ is onto, thereby range $f=[-5, \infty)$.
Let us define $g:[-5, \infty) \rightarrow R_{+}$as $g(y)=\frac{\sqrt{y+6}-1}{3}$
We have,

$$
\begin{aligned}
(g \circ f)(x)=g(f(x)) & =g\left(9 x^{2}+6 x-5\right) \\
& =g\left((3 x+1)^{2}-6\right) \\
& =\frac{\sqrt{(3 x+1)^{2}-6+6}-1}{3} \\
& =\frac{3 x+1-1}{3}=x
\end{aligned}
$$

And,

$$
\begin{aligned}
& \begin{aligned}
(f o g)(y)=f(g(y)) & =f\left(\frac{\sqrt{y+6}-1}{3}\right) \\
& =\left[3\left(\frac{\sqrt{y+6}-1}{3}\right)+1\right]^{2}-6 \\
& =(\sqrt{y+6})^{2}-6=y+6-6=y
\end{aligned} \\
& \begin{aligned}
\therefore \text { gof }=\mathrm{I}_{R} \text { and } f o g & =\mathrm{I}_{[-5, \infty)}
\end{aligned}
\end{aligned}
$$

Hence, $f$ is invertible and the inverse of $f$ is given by

$$
f^{-1}(y)=g(y)=\frac{\sqrt{y+6}-1}{3} .
$$
:::

:::

:::question{number="EX1.3-10" kind="additional_exercise" id="sol_1.3.10" topic="Uniqueness of the inverse function"}
#### Additional Question EX1.3-10

:::prompt
Let $f: X \rightarrow Y$ be an invertible function. Show that $f$ has unique inverse.
(Hint: suppose $g_{1}$ and $g_{2}$ are two inverses of $f$. Then for all $y \in Y$, $f_{o g}(y)=\mathrm{I}_{Y}(y)=f_{o g}(y)$ . Use one-one ness of $f$.
:::

:::solution{label="Solution"}
Let $f: X \rightarrow Y$ be an invertible function.
Also suppose $f$ has two inverses ( $g_{1}$ and $g_{2}$ )
Then, for all $y \in Y$,

$$
\begin{array}{ll}
f o g_{1}(y)=\mathrm{I}_{Y}(y)=f o g_{2}(y) & \\
\Rightarrow f\left(g_{1}(y)\right)=f\left(g_{2}(y)\right) & \\
\Rightarrow g_{1}(y)=g_{2}(y) & {[f \text { is invertible } \Rightarrow f \text { is one-one }]} \\
\Rightarrow g_{1}=g_{2} & {[g \text { is one-one }]}
\end{array}
$$

Hence, $f$ has unique inverse.
:::

:::

:::question{number="EX1.3-11" kind="additional_exercise" id="sol_1.3.11" topic="Inverse of the inverse - finite function"}
#### Additional Question EX1.3-11

:::prompt
Consider $f:\{1,2,3\} \rightarrow\{a, b, c\}$ given by $f(1)=a, f(2)=b, f(3)=c$. Find $\left(f^{-1}\right)^{-1}=f$.
:::

:::solution{label="Solution"}
Function $f:\{1,2,3\} \rightarrow\{a, b, c\}$ given by $f(1)=a, f(2)=b, f(3)=c$
If we define $g:\{a, b, c\} \rightarrow\{1,2,3\}$ as $g(a)=1, g(b)=2, g(c)=3$

$$
\begin{aligned}
& (f o g)(a)=f(g(a))=f(1)=a \\
& (f o g)(b)=f(g(b))=f(2)=b \\
& (f o g)(c)=f(g(c))=f(3)=c
\end{aligned}
$$

And,

$$
\begin{aligned}
& (g \circ f)(1)=g(f(1))=g(a)=1 \\
& (g \circ f)(2)=g(f(2))=g(b)=2 \\
& (g \circ f)(3)=g(f(3))=g(c)=3
\end{aligned}
$$

$$
\therefore g o f=\mathrm{I}_{X} \quad \text { and } \quad f o g=\mathrm{I}_{Y} \quad \text { where } X=\{(1,2,3)\} \text { and } Y=\{a, b, c\}
$$

Thus, the inverse of $f$ exists and $f^{-1}=g$.

$$
\therefore f^{-1}:\{a, b, c\} \rightarrow\{1,2,3\} \text { is given by, } f^{-1}(a)=1, f^{-1}(b)=2, f^{-1}(c)=3
$$

We need to find the inverse of $f^{-1}$ i.e., inverse of $g$.
If we define $h:\{1,2,3\} \rightarrow\{a, b, c\}$ as $h(1)=a, h(2)=b, h(3)=c$

$$
\begin{aligned}
& (g o h)(1)=g(h(1))=g(a)=1 \\
& (g o h)(2)=g(h(2))=g(b)=2 \\
& (g o h)(3)=g(h(3))=g(c)=3
\end{aligned}
$$

And,

$$
\begin{aligned}
& (h o g)(a)=h(g(a))=h(1)=a \\
& (h o g)(b)=h(g(b))=h(2)=b \\
& (h o g)(c)=h(g(c))=h(3)=c
\end{aligned}
$$

$$
\therefore g o h=\mathrm{I}_{X} \quad \text { and } \quad h o g=\mathrm{I}_{Y} \quad \text { where } X=\{(1,2,3)\} \text { and } Y=\{a, b, c\}
$$

Thus, the inverse of $g$ exists and $g^{-1}=h \Rightarrow\left(f^{-1}\right)^{-1}=h$.
It can be noted that $h=f$.
Hence, $\left(f^{-1}\right)^{-1}=f$
:::

:::

:::question{number="EX1.3-12" kind="additional_exercise" id="sol_1.3.12" topic="Inverse of the inverse - general proof"}
#### Additional Question EX1.3-12

:::prompt
Let $f: X \rightarrow Y$ be an invertible function. Show that the inverse of $f^{-1}$ is $f$ i.e., $\left(f^{-1}\right)^{-1}=f$.
:::

:::solution{label="Solution"}
Let $f: X \rightarrow Y$ be an invertible function.
Then there exists a function $g: Y \rightarrow X$ such that $g o f=\mathrm{I}_{X}$ and $f o g=\mathrm{I}_{Y}$
Here, $f^{-1}=g$
Now, $g o f=\mathrm{I}_{X}$ and $f o g=\mathrm{I}_{Y}$

$$
\Rightarrow f^{-1} o f=\mathrm{I}_{X} \text { and } f o f^{-1}=\mathrm{I}_{Y}
$$

Hence, $f^{-1}: Y \rightarrow X$ is invertible and $f^{-1}$ is $f$ i.e., $\left(f^{-1}\right)^{-1}=f$.
:::

:::

:::question{number="EX1.3-13" kind="additional_exercise" id="sol_1.3.13" topic="MCQ - composition (3-x^3)^(1/3)"}
#### Additional Question EX1.3-13

:::prompt
If $f: R \rightarrow R$ is given by $f(x)=\left(3-x^{3}\right)^{\frac{1}{3}}$, then $f \circ f(x)$ is:

A. $\frac{1}{x^{3}}$
B. $x^{3}$
C. $x$
D. $\left(3-x^{3}\right)$
:::

:::solution{label="Solution"}
$f: R \rightarrow R$ is given by $f(x)=\left(3-x^{3}\right)^{\frac{1}{3}}$

$$
f(x)=\left(3-x^{3}\right)^{\frac{1}{3}}
$$

$$
\begin{aligned}
\therefore f o f(x)=f(f(x)) & =f\left(\left(3-x^{3}\right)^{\frac{1}{3}}\right)=\left[3-\left(\left(3-x^{3}\right)^{\frac{1}{3}}\right)^{3}\right]^{\frac{1}{3}} \\
& =\left[3-\left(3-x^{3}\right)\right]^{\frac{1}{3}}=\left(x^{3}\right)^{\frac{1}{3}}=x
\end{aligned}
$$

$$
\therefore f o f(x)=x
$$

The correct answer is C.
:::

:::answer
**Answer:** C
:::

:::

:::question{number="EX1.3-14" kind="additional_exercise" id="sol_1.3.14" topic="MCQ - inverse of a rational function"}
#### Additional Question EX1.3-14

:::prompt
If $f: R-\left\{-\frac{4}{3}\right\} \rightarrow R$ be a function defined as $f(x)=\frac{4 x}{3 x+4}$. The inverse of $f$ is the map $g:$ Range $f \rightarrow R-\left\{-\frac{4}{3}\right\}$ given by :

A. $g(y)=\frac{3 y}{3-4 y}$
B. $g(y)=\frac{4 y}{4-3 y}$
C. $g(y)=\frac{4 y}{3-4 y}$
D. $g(y)=\frac{3 y}{4-3 y}$
:::

:::solution{label="Solution"}
It is given that $f: R-\left\{-\frac{4}{3}\right\} \rightarrow R$ is defined as $f(x)=\frac{4 x}{3 x+4}$
Let $y$ be an arbitrary element of Range $f$.
Then, there exists $x \in R-\left\{-\frac{4}{3}\right\}$ such that $y=f(x)$.

$$
\begin{aligned}
& \Rightarrow y=\frac{4 x}{3 x+4} \\
& \Rightarrow 3 x y+4 y=4 x \\
& \Rightarrow x(4-3 y)=4 y \\
& \Rightarrow x=\frac{4 y}{4-3 y}
\end{aligned}
$$

Define $f: R-\left\{-\frac{4}{3}\right\} \rightarrow R \quad$ as $\quad g(y)=\frac{4 y}{4-3 y}$
Now,

$$
\begin{aligned}
(g o f)(x) & =g(f(x))=g\left(\frac{4 x}{3 x+4}\right) \\
& =\frac{4\left(\frac{4 x}{3 x+4}\right)}{4-3\left(\frac{4 x}{3 x+4}\right)}=\frac{16 x}{12 x+16-12 x} \\
& =\frac{16 x}{16}=x
\end{aligned}
$$

And

$$
\begin{aligned}
& (f o g)(x)=(g(x))=f\left(\frac{4 y}{4-3 y}\right) \\
& \quad=\frac{4\left(\frac{4 y}{4-3 y}\right)}{3\left(\frac{4 y}{4-3 y}\right)+4}=\frac{16 y}{12 y+16-12 y} \\
& \quad=\frac{16 y}{16}=y \\
& \therefore g o f=\mathrm{I}_{R-\left\{-\frac{4}{3}\right\}} \text { and } \text { fog }=\mathrm{I}_{\text {Range f }}
\end{aligned}
$$

Thus, $g$ is the inverse of $f$ i.e., $f^{-1}=g$
Hence, the inverse of $f$ is the map $g:$ Range $f \rightarrow R-\left\{-\frac{4}{3}\right\}$, which is given by $g(y)=\frac{4 y}{4-3 y}$.
The correct answer is B.
:::

:::answer
**Answer:** B
:::

:::

:::question{number="EX1.4-1" kind="additional_exercise" id="sol_1.4.1" topic="Checking binary operation validity"}
#### Additional Question EX1.4-1

:::prompt
Determine whether or not each of the definition of * given below gives a binary operation. In the event that $*$ is not a binary operation, give justification for this.

i. On $\mathbf{Z}^{+}$, define * by $a^{*} b=a-b$
ii. On $\mathbf{Z}^{+}$, define * by $a^{*} b=a b$
iii. On R, define *by $a * b=a b^{2}$
iv. On $\mathbf{Z}^{+}$, define $*$ by $a^{*} b=|a-b|$
v. On $\mathbf{Z}^{+}$, define * by $a^{*} b=a$
:::

:::solution{label="Solution"}
i. On $\mathbf{Z}^{+}$, define ${ }^{*}$ by $a^{*} b=a-b$
It is not a binary operation as the image of $(1,2)$ under * is
$$
\begin{aligned}
& 1^{*} 2=1-2 \\
& \Rightarrow-1 \notin \mathbf{Z}^{+} .
\end{aligned}
$$
Therefore, * is not a binary operation.
ii. On $\mathbf{Z}^{+}$,define * by $a^{*} b=a b$
It is seen that for each $a, b \in \mathbf{Z}^{+}$, there is a unique element $a b$ in $\mathbf{Z}^{+}$.
This means that * carries each pair $(a, b)$ to a unique element $a * b=a b$ in $\mathbf{Z}^{+}$.
Therefore, * is a binary operation.
iii. On R, define ${ }^{*} a * b=a b^{2}$
It is seen that for each $a, b \in \mathbf{R}$, there is a unique element $a b^{2}$ in R. This means that * carries each pair $(a, b)$ to a unique element $a * b=a b^{2}$ in $\mathbf{R}$.
Therefore, *is a binary operation.
iv. On $\mathbf{Z}^{+}, \quad$ define * by $a^{*} b=|a-b|$
It is seen that for each $a, b \in \mathbf{Z}^{+}$,there is a unique element $|a-b|$ in $\mathbf{Z}^{+}$. This means that * carries each pair $(a, b)$ to a unique element $a^{*} b=|a-b|$ in $\mathbf{Z}^{+}$. Therefore, *is a binary operation.
v. On $\mathbf{Z}^{+}$, define * by $a^{*} b=a$
*carries each pair $(a, b)$ to a unique element in $a^{*} b=a$ in $\mathbf{Z}^{+}$.
Therefore, * is a binary operation.
:::

:::

:::question{number="EX1.4-2" kind="additional_exercise" id="sol_1.4.2" topic="Commutativity and associativity of operations"}
#### Additional Question EX1.4-2

:::prompt
For each binary operation *defined below, determine whether * is commutative or associative.

i. On $\mathbf{Z}^{+}$, define $a * b=a-b$

ii. On $\mathbf{Q}$, define $a * b=a b+1$
iii. On $\mathbf{Q}$, define $a^{*} b=\frac{a b}{2}$
iv. On $\mathbf{Z}^{+}$, define $a * b=2^{a b}$
v. On $\mathbf{Z}^{+}$, define $a^{*} b=a^{b}$
vi. On $\mathbf{R}-\{-1\}$, define $a^{*} b=\frac{a}{b+1}$
:::

:::solution{label="Solution"}
i. On $\mathbf{Z}^{+}$, define $a * b=a-b$
It can be observed that $1 * 2=1-2=-1$ and $2 * 1=2-1=1$.
$$
\therefore 1^{*} 2 \neq 2^{*} 1 ; \text { where } 1,2 \in \mathbf{Z}
$$
Hence, the operation * is not commutative.
Also,
$$
\begin{aligned}
& (1 * 2) * 3=(1-2) * 3=-1 * 3=-1-3=-4 \\
& 1 *(2 * 3)=1 *(2-3)=1 *-1=1-(-1)=2 \\
& \therefore(1 * 2) * 3 \neq 1 *(2 * 3)
\end{aligned}
$$
where $1,2,3 \in \mathbf{Z}$
Hence, the operation * is not associative.
ii. On $\mathbf{Q}$, define $a * b=a b+1$
$$
\begin{array}{ll}
a b=b a & \text { for all } a, b \in Q \\
\Rightarrow a b+1=b a+1 & \text { for all } a, b \in Q \\
\Rightarrow a * b=b^{*} a & \text { for all } a, b \in Q
\end{array}
$$
Hence, the operation * is commutative.
$$
\begin{aligned}
& (1 * 2) * 3=(1 \times 2+1) * 3=3 * 3=3 \times 3+1=10 \\
& 1 *(2 * 3)=1 *(2 \times 3+1)=1 * 7=1 \times 7+1=8 \\
& \therefore(1 * 2) * 3 \neq 1 *(2 * 3)
\end{aligned}
$$
where $1,2,3 \in \mathbf{Q}$
Hence, the operation * is not associative.
iii. On $\mathbf{Q}$, define $a^{*} b=\frac{a b}{2}$
$$
\begin{array}{lr}
a b=b a & \text { for all } a, b \in Q \\
\Rightarrow \frac{a b}{2}=\frac{a b}{2} & \text { for all } a, b \in Q \\
\Rightarrow a * b=b^{*} a & \text { for all } a, b \in Q
\end{array}
$$
Hence, the operation * is commutative.

$$
(a * b) * c=\left(\frac{a b}{2}\right) * c=\frac{\left(\frac{a b}{2}\right) c}{2}=\frac{a b c}{4}
$$

And

$$
\begin{aligned}
& a *(b * c)=a *\left(\frac{b c}{2}\right)=\frac{a\left(\frac{b c}{2}\right)}{2}=\frac{a b c}{4} \\
& \therefore(a * b)^{*} c=a *(b * c)
\end{aligned}
$$

where $a, b, c \in \mathbf{Q}$
Hence, the operation * is associative.
iv. On $\mathbf{Z}^{+}$, define $a^{*} b=2^{a b}$

$$
\begin{aligned}
& a b=b a \quad \text { for all } a, b \in Z \\
& \Rightarrow 2^{a b}=2^{b a} \quad \text { for all } a, b \in Z \\
& \Rightarrow a^{*} b=b^{*} a \quad \text { for all } a, b \in Z
\end{aligned}
$$

Hence, the operation * is commutative.

$$
\begin{aligned}
& (1 * 2) * 3=2^{1 \times 2} * 3=4 * 3=2^{4 \times 3}=2^{12} \\
& 1 *(2 * 3)=1 * 2^{2 \times 3}=1 * 2^{6}=1 * 64=2^{64} \\
& \therefore(1 * 2) * 3 \neq 1 *(2 * 3)
\end{aligned}
$$

where $1,2,3 \in \mathbf{Z}^{+}$
Hence, the operation * is not associative.
v. On $\mathbf{Z}^{+}$, define $a * b=a^{b}$

$$
\begin{aligned}
& 1 * 2=1^{2}=1 \\
& 2 * 1=2^{1}=2 \\
& \therefore 1 * 2 \neq 2 * 1
\end{aligned}
$$

where $1,2, \in \mathbf{Z}^{+}$
Hence, the operation * is not commutative.

$$
\begin{aligned}
& (2 * 3) * 4=2^{3} * 4=8 * 4=8^{4}=2^{12} \\
& 2 *(3 * 4)=2 * 3^{4}=2 * 81=2^{81} \\
& \therefore(2 * 3) * 4 \neq 2 *(3 * 4)
\end{aligned}
$$

where $2,3,4 \in \mathbf{Z}^{+}$
Hence, the operation * is not associative.
vi. On $\mathbf{R}-\{-1\}$, define $a^{*} b=\frac{a}{b+1}$

$$
\begin{aligned}
& 1 * 2=\frac{1}{2+1}=\frac{1}{3} \\
& 2 * 1=\frac{2}{1+1}=\frac{2}{2}=1
\end{aligned}
$$

$$
\therefore 1 * 2 \neq 2 * 1
$$

$$
\text { where } 1,2, \in \mathbf{R}-\{-1\}
$$

Hence, the operation * is not commutative.

$$
\begin{aligned}
& (1 * 2) * 3=\frac{1}{3} * 3=\frac{\frac{1}{3}}{3+1}=\frac{1}{12} \\
& 1 *(2 * 3)=1 * \frac{2}{3+1}=1 * \frac{2}{4}=1 * \frac{1}{2}=\frac{1}{\frac{1}{2}+1}=\frac{1}{\frac{3}{2}}=\frac{2}{3} \\
& \therefore(1 * 2) * 3 \neq 1 *(2 * 3)
\end{aligned}
$$

$$
\text { where } 1,2,3 \in \mathbf{R}-\{-1\}
$$

Hence, the operation * is not associative.
:::

:::

:::question{number="EX1.4-3" kind="additional_exercise" id="sol_1.4.3" topic="Operation table - minimum function"}
#### Additional Question EX1.4-3

:::prompt
Consider the binary operation $\wedge$ on the set $\{1,2,3,4,5\}$ defined by $a \wedge b=\min \{a, b\}$. Write the operation table of the operation ^ .
:::

:::solution{label="Solution"}
The binary operation $\wedge$ on the set $\{1,2,3,4,5\}$ is defined by $a \wedge b=\min \{a, b\}$ for all $a, b \in\{1,2,3,4,5\}$.
The operation table for the given operation $\wedge$ can be given as:

| ^ | 1 | 2 | 3 | 4 | 5 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | 1 | 1 | 1 | 1 | 1 |
| 2 | 1 | 2 | 2 | 2 | 2 |
| 3 | 1 | 2 | 3 | 3 | 3 |
| 4 | 1 | 2 | 3 | 4 | 4 |
| 5 | 1 | 2 | 3 | 4 | 5 |
:::

:::

:::question{number="EX1.4-4" kind="additional_exercise" id="sol_1.4.4" topic="Operation table - given multiplication table"}
#### Additional Question EX1.4-4

:::prompt
Consider a binary operation * on the set $\{1,2,3,4,5\}$ given by the following multiplication table.

i. Compute $(2 * 3) * 4$ and $2 *(3 * 4)$
ii. Is *commutative?
iii. Compute $(2 * 3) *(4 * 5)$.
(Hint: Use the following table)

| * | 1 | 2 | 3 | 4 | 5 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | 1 | 1 | 1 | 1 | 1 |
| 2 | 1 | 2 | 1 | 2 | 1 |
| 3 | 1 | 1 | 3 | 1 | 1 |
| 4 | 1 | 2 | 1 | 4 | 1 |
| 5 | 1 | 1 | 1 | 1 | 5 |
:::

:::solution{label="Solution"}
$$
(2 * 3) * 4=1 * 4=1
$$

i. $2 *(3 * 4)=2 * 1=1$
ii. For every $a, b \in\{1,2,3,4,5\}$, we have $a^{*} b=b^{*} a$. Therefore, * is commutative.
iii. $(2 * 3) *(4 * 5)$
$$
\begin{aligned}
& (2 * 3)=1 \text { and }(4 * 5)=1 \\
& \therefore(2 * 3) *(4 * 5)=1 * 1=1
\end{aligned}
$$
:::

:::

:::question{number="EX1.4-5" kind="additional_exercise" id="sol_1.4.5" topic="Comparing HCF operation to a given table"}
#### Additional Question EX1.4-5

:::prompt
Let ${ }^{* \prime}$ be the binary operation on the set $\{1,2,3,4,5\}$ defined by $a^{* \prime} b=$ H.C.F. of $a$ and $b$. Is the operation *' same as the operation * defined in Exercise 4 above? Justify your answer.
:::

:::solution{label="Solution"}
The binary operation on the set $\{1,2,3,4,5\}$ is defined by $a^{* \prime} b=$ H.C.F. of $a$ and $b$. The operation table for the operation ${ }^{* \prime}$ can be given as:

| *' | 1 | 2 | 3 | 4 | 5 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | 1 | 1 | 1 | 1 | 1 |
| 2 | 1 | 2 | 1 | 2 | 1 |
| 3 | 1 | 1 | 3 | 1 | 1 |
| 4 | 1 | 2 | 1 | 4 | 1 |
| 5 | 1 | 1 | 1 | 1 | 5 |

The operation table for the operations *' and * are same. operation ${ }^{* \prime}$ is same as operation *.
:::

:::

:::question{number="EX1.4-6" kind="additional_exercise" id="sol_1.4.6" topic="LCM operation - properties and identity"}
#### Additional Question EX1.4-6

:::prompt
Let * be the binary operation on N defined by $a^{*} b=\mathrm{L} . \mathrm{C} . \mathrm{M}$. of $a$ and $b$. Find

i. 5*7,20*16
ii. Is *commutative?
iii. Is *associative?
iv. Find the identity of *in N
v. Which elements of N are invertible for the operation *?
:::

:::solution{label="Solution"}
The binary operation on N is defined by $a^{*} b=$ L.C.M. of $a$ and $b$.

i. $5^{*} 7=$ L.C.M of 5 and $7=35$
$20 * 16=$ LCM of 20 and $16=80$
ii. L.C.M. of $a$ and $b=\mathrm{LCM}$ of $b$ and $a$ for all $a, b \in N$
$$
\therefore a * b=b * a
$$
Operation * is commutative.
iii. For $a, b, c \in N$
$$
\begin{aligned}
& \left(a^{*} b\right)^{*} c=(\text { L.C.M. of } a \text { and } b)^{*} c=\text { L.C.M. of } a, b, c \\
& a^{*}\left(b^{*} c\right)=a^{*}(\text { L.C.M. of } b \text { and } c)=\text { L.C.M. of } a, b, c \\
& \therefore\left(a^{*} b\right)^{*} c=a^{*}\left(b^{*} c\right)
\end{aligned}
$$
Operation *is associative.
iv. L.C.M. of $a$ and $1=a=$ L.C.M. of 1 and $a$ for all $a \in N$
$$
a * 1=a=1 * a \text { for all } a \in N
$$
Therefore, 1 is the identity of *in N.
v. An element a in N is invertible with respect to the operation * if there exists an element b in N, such that $a * b=e=b^{*} a$
$$
e=1
$$
L.C.M. of $a$ and $b=1=\mathrm{LCM}$ of $b$ and $a$ possible only when $a$ and $b$ are equal to 1 .
1 is the only invertible element of N with respect to the operation *.
:::

:::

:::question{number="EX1.4-7" kind="additional_exercise" id="sol_1.4.7" topic="LCM on a finite set is not a binary operation"}
#### Additional Question EX1.4-7

:::prompt
Is * defined on the set \{1,2,3,4,5\} by $a^{*} b=\mathrm{LCM}$ of $a$ and $b$ a binary operation? Justify your answer.
:::

:::solution{label="Solution"}
The operation * on the set \{1,2,3,4,5\} is defined by $a^{*} b=\mathrm{LCM}$ of $a$ and $b$.
The operation table for the operation ${ }^{* \prime}$ can be given as:

| * | 1 | 2 | 3 | 4 | 5 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | 1 | 2 | 3 | 4 | 5 |
| 2 | 2 | 2 | 6 | 4 | 10 |
| 3 | 3 | 6 | 3 | 12 | 15 |
| 4 | 4 | 4 | 12 | 4 | 20 |
| 5 | 5 | 10 | 15 | 20 | 5 |

$$
\begin{aligned}
& 3 * 2=2 * 3=6 \notin A, \\
& 5 * 2=2 * 5=10 \notin A, \\
& 3 * 4=4 * 3=12 \notin A, \\
& 3 * 5=5 * 3=15 \notin A, \\
& 4 * 5=5 * 4=20 \notin A
\end{aligned}
$$

The given operation *is not a binary operation.
:::

:::

:::question{number="EX1.4-8" kind="additional_exercise" id="sol_1.4.8" topic="HCF operation - commutative, associative, no identity"}
#### Additional Question EX1.4-8

:::prompt
Let * be the binary operation on N defined by $a^{*} b=$ H.C.F. of $a$ and $b$. Is * commutative? Is * associative? Does there exist identity for this binary operation on N ?
:::

:::solution{label="Solution"}
The binary operation * on N defined by $a^{*} b=$ H.C.F. of $a$ and $b$.

$$
\therefore a^{*} b=b^{*} a
$$

Operation * is commutative.
For all $a, b, c \in N$,

$$
\begin{aligned}
& \left(a^{*} b\right)^{*} c=(\text { HCF of } a \text { and } b)^{*} c=\text { HCF of } a, b, c \\
& a^{*}\left(b^{*} c\right)=a^{*}(\text { HCF. of } b \text { and } c)=\text { HCF of } a, b, c \\
& \therefore\left(a^{*} b\right)^{*} c=a^{*}\left(b^{*} c\right)
\end{aligned}
$$

Operation * is associative.
$e \in N$ will be the identity for the operation ${ }^{*}$ if $a * e=a=e^{*} a$ for all $a \in N$. But this relation is not true for any $a \in N$.
Operation * does not have any identity in N.
:::

:::

:::question{number="EX1.4-9" kind="additional_exercise" id="sol_1.4.9" topic="Commutativity and associativity on Q"}
#### Additional Question EX1.4-9

:::prompt
Let * be the binary operation on Q of rational numbers as follows:

i. $\quad a * b=a-b$
ii. $a^{*} b=a^{2}+b^{2}$
iii. $\quad a * b=a+a b$
iv. $\quad a * b=(a-b)^{2}$
v. $a+b=\frac{a b}{4}$
vi. $a * b=a b^{2}$

Find which of the binary operations are commutative and which are associative.
:::

:::solution{label="Solution"}
i. On Q, the operation * is defined as $a^{*} b=a-b$
$$
\frac{1}{2} * \frac{1}{3}=\frac{1}{2}-\frac{1}{3}=\frac{3-2}{3}=\frac{1}{6}
$$
And
$$
\begin{aligned}
& \frac{1}{3} * \frac{1}{2}=\frac{1}{3}-\frac{1}{2}=\frac{2-3}{6}=\frac{-1}{6} \\
& \therefore\left(\frac{1}{2} * \frac{1}{3}\right) \neq\left(\frac{1}{3} * \frac{1}{2}\right)
\end{aligned}
$$
where $\frac{1}{2}, \frac{1}{3} \in Q$
Operation * is not commutative.
$$
\begin{aligned}
& \left(\frac{1}{2} * \frac{1}{3}\right) * \frac{1}{4}=\left(\frac{1}{2}-\frac{1}{3}\right) * \frac{1}{4}=\frac{1}{6} * \frac{1}{4}=\frac{1}{6}-\frac{1}{4}=\frac{2-3}{12}=\frac{-1}{12} \\
& \frac{1}{2} *\left(\frac{1}{3} * \frac{1}{4}\right)=\frac{1}{2} *\left(\frac{1}{3}-\frac{1}{4}\right)=\frac{1}{2} * \frac{1}{12}=\frac{1}{2}-\frac{1}{12}=\frac{6-1}{12}=\frac{5}{12} \\
& \therefore\left(\frac{1}{2} * \frac{1}{3}\right) * \frac{1}{4} \neq \frac{1}{2} *\left(\frac{1}{3} * \frac{1}{4}\right)
\end{aligned}
$$
Operation * is not associative.
ii. On Q, the operation * is defined as $a * b=a^{2}+b^{2}$
For $a, b \in Q$
$$
\begin{aligned}
& a * b=a^{2}+b^{2}=b^{2}+a^{2}=b^{*} a \\
& \therefore a * b=b * a
\end{aligned}
$$
Operation * is commutative.
$$
\begin{aligned}
& (1 * 2) * 3=\left(1^{2}+2^{2}\right) * 3=(1+4) * 3=5 * 3=5^{2}+3^{2}=25+9=34 \\
& 1 *(2 * 3)=1 *\left(2^{2}+3^{2}\right)=1 *(4+9)=1 * 13=1^{2}+13^{2}=1+169=170 \\
& \therefore(1 * 2) * 3 \neq 1 *(2 * 3) \quad \text { where } 1,2,3 \in Q
\end{aligned}
$$
Operation * is not associative.
iii. On Q, the operation * is defined as $a^{*} b=a+a b$
$$
\begin{aligned}
& 1 * 2=1+1 \times 2=1+2=3 \\
& 2 * 1=2+2 \times 1=2+2=4 \\
& \therefore 1 * 2 \neq 2 * 1
\end{aligned}
$$
where $1,2 \in Q$
Operation * is not commutative.
$$
\begin{aligned}
& (1 * 2) * 3=(1+1 \times 2) * 3=3 * 3=3+3 \times 3=3+9=12 \\
& 1 *(2 * 3)=1 *(2+2 \times 3)=1 * 8=1+1 \times 8=1+8=9 \\
& \therefore(1 * 2) * 3 \neq 1 *(2 * 3) \quad \text { where } 1,2,3 \in Q
\end{aligned}
$$
Operation * is not associative.

iv. On Q, the operation * is defined as $a * b=(a-b)^{2}$
For $a, b \in Q$
$$
\begin{aligned}
& a * b=(a-b)^{2} \\
& b * a=(b-a)^{2}=[-(a-b)]^{2}=(a-b)^{2} \\
& \therefore a * b=b * a
\end{aligned}
$$
Operation * is commutative.
$$
\begin{aligned}
& (1 * 2) * 3=(1-2)^{2} * 3=(-1)^{2} * 3=1 * 3=(1-3)^{2}=(-2)^{2}=4 \\
& 1 *(2 * 3)=1 *(2-3)^{2}=1 *(-1)^{2}=1 * 1=(1-1)^{2}=0 \\
& \therefore(1 * 2) * 3 \neq 1 *(2 * 3) \quad \text { where } 1,2,3 \in Q
\end{aligned}
$$
Operation * is not associative.
v. On Q, the operation * is defined as $a+b=\frac{a b}{4}$
For $a, b \in Q$
$$
\begin{aligned}
& a * b=\frac{a b}{4}=\frac{b a}{4}=b * a \\
& \therefore a * b=b * a
\end{aligned}
$$
Operation * is commutative.
For $a, b, c \in Q$
$$
\begin{aligned}
& (a * b) * c=\frac{a b}{4} * c=\frac{\frac{a b}{4} \cdot c}{4}=\frac{a b c}{16} \\
& a *(b * c)=a * \frac{a b}{4}=\frac{a \cdot \frac{a b}{4}}{4}=\frac{a b c}{16} \\
& \therefore(a * b) * c=a *(b * c)
\end{aligned}
$$
where $a, b, c \in Q$
Operation * is associative.
vi. On Q, the operation * is defined as $a * b=a b^{2}$
$$
\begin{aligned}
& \frac{1}{2} * \frac{1}{3}=\frac{1}{2} \cdot\left(\frac{1}{3}\right)^{2}=\frac{1}{2} \cdot \frac{1}{9}=\frac{1}{18} \\
& \frac{1}{3} * \frac{1}{2}=\frac{1}{3} \cdot\left(\frac{1}{2}\right)^{2}=\frac{1}{3} \cdot \frac{1}{4}=\frac{1}{12}
\end{aligned}
$$
$$
\therefore\left(\frac{1}{2} * \frac{1}{3}\right) \neq\left(\frac{1}{3} * \frac{1}{2}\right)
$$
where $\frac{1}{2}, \frac{1}{3} \in Q$
Operation * is not commutative.

$$
\begin{aligned}
& \left(\frac{1}{2} * \frac{1}{3}\right) * \frac{1}{4}=\left(\frac{1}{2} \cdot\left(\frac{1}{3}\right)^{2}\right) * \frac{1}{4}=\frac{1}{18} * \frac{1}{4}=\frac{1}{18} \cdot\left(\frac{1}{4}\right)^{2}=\frac{1}{18 \times 16} \\
& \frac{1}{2} *\left(\frac{1}{3} * \frac{1}{4}\right)=\frac{1}{2} *\left(\frac{1}{3} \cdot\left(\frac{1}{4}\right)^{2}\right)=\frac{1}{2} * \frac{1}{48}=\frac{1}{2} \cdot\left(\frac{1}{48}\right)^{2}=\frac{1}{2 \times(48)^{2}} \\
& \therefore\left(\frac{1}{2} * \frac{1}{3}\right) * \frac{1}{4} \neq \frac{1}{2} *\left(\frac{1}{3} * \frac{1}{4}\right)
\end{aligned}
$$

Operation * is not associative.
Operations defined in (ii), (iv), (v) are commutative and the operation defined in (v) is associative.
:::

:::

:::question{number="EX1.4-10" kind="additional_exercise" id="sol_1.4.10" topic="Identity element among operations on Q"}
#### Additional Question EX1.4-10

:::prompt
Find which of the operations given above has identity.
:::

:::solution{label="Solution"}
An element $e \in Q$ will be the identity element for the operation ${ }^{*}$ if

$$
\begin{aligned}
& a * e=a=e * a, \text { for all } a \in Q \\
& a * b=\frac{a b}{4} \\
& \Rightarrow a * e=a \\
& \Rightarrow \frac{a e}{4}=a \\
& \Rightarrow e=4
\end{aligned}
$$

Similarly, it can be checked for $e * a=a$, we get $e=4$ is the identity.
:::

:::

:::question{number="EX1.4-11" kind="additional_exercise" id="sol_1.4.11" topic="Componentwise addition on N x N"}
#### Additional Question EX1.4-11

:::prompt
$A=N \times N$ and $*$ be the binary operation on A defined by $(a, b)^{*}(c, d)=(a+c, b+d)$. Show that * is commutative and associative. Find the identity element for * on $A$, if any.
:::

:::solution{label="Solution"}
$A=N \times N$ and * be the binary operation on A defined by

$$
\begin{aligned}
& (a, b) *(c, d)=(a+c, b+d) \\
& (a, b) *(c, d) \in A \\
& a, b, c, d \in N \\
& (a, b) *(c, d)=(a+c, b+d) \\
& (c, d)^{*}(a, b)=(c+a, d+b)=(a+c, b+d) \\
& \therefore(a, b) *(c, d)=(c, d) *(a, b)
\end{aligned}
$$

Operation * is commutative.

Now, let $(a, b),(c, d),(e, f) \in A$

$$
\begin{aligned}
& a, b, c, d, e, f \in N \\
& {[(a, b) *(c, d)] *(e, f)=(a+c, b+d) *(e, f)=(a+c+e, b+d+f)} \\
& (a, b) *[(c, d) *(e, f)]=(a, b) *(c+e, d+f)=(a+c+e, b+d+f) \\
& \therefore[(a, b) *(c, d)] *(e, f)=(a, b) *[(c, d) *(e, f)]
\end{aligned}
$$

Operation * is associative.
An element $e=\left(e_{1}, e_{2}\right) \in A$ will be an identity element for the operation $*$ if $a+e=a=e^{*} a$ for all $a=\left(a_{1}, a_{2}\right) \in A$ i.e., $\left(a_{1}+e_{1}, a_{2}+e_{2}\right)=\left(a_{1}, a_{2}\right)=\left(e_{1}+a_{1}, e_{2}+a_{2}\right)$, which is not true for any element in A.

Therefore, the operation * does not have any identity element.
:::

:::

:::question{number="EX1.4-12" kind="additional_exercise" id="sol_1.4.12" topic="True or false - binary operation statements"}
#### Additional Question EX1.4-12

:::prompt
State whether the following statements are true or false. Justify.

i. For an arbitrary binary operation * on a set $\mathrm{N}, a * a=a$ for all $a \in N$.
ii. If * is a commutative binary operation on N, then $a *(b * c)=(c * b)^{*} a$
:::

:::solution{label="Solution"}
i. Define operation * on a set N as $a^{*} a=a$ for all $a \in N$.
In particular, for $a=3$,
$$
3 * 3=9 \neq 3
$$
Therefore, statement (i) is false.
ii. R.H.S. $=\left(c^{*} b\right)^{*} a$
$$
\begin{aligned}
& =\left(b^{*} c\right)^{*} a\left[{ }^{*} \text { is commutative }\right] \\
& =a^{*}\left(b^{*} c\right) \text { [Again, as } * \text { is commutative] } \\
& =\text { L.H.S. } \\
& \therefore a^{*}\left(b^{*} c\right)=\left(c^{*} b\right)^{*} a
\end{aligned}
$$
Therefore, statement (ii) is true.
:::

:::

:::question{number="EX1.4-13" kind="additional_exercise" id="sol_1.4.13" topic="MCQ - commutative but not associative operation"}
#### Additional Question EX1.4-13

:::prompt
Consider a binary operation * on N defined as $a^{*} b=a^{3}+b^{3}$. Choose the correct answer.

A. Is * both associative and commutative?
B. Is * commutative but not associative?
C. Is * associative but not commutative?
D. Is * neither commutative nor associative?
:::

:::solution{label="Solution"}
On N, operation *is defined as $a * b=a^{3}+b^{3}$.
For all $a, b \in N$

$$
a^{*} b=a^{3}+b^{3}=b^{3}+a^{3}=b * a
$$

Operation * is commutative.

$$
\begin{aligned}
& (1 * 2) * 3=\left(1^{3}+2^{3}\right) * 3=(1+8) * 3=9 * 3=9^{3}+3^{3}=729+27=756 \\
& 1 *(2 * 3)=1 *\left(2^{3}+3^{3}\right)=1 *(8+27)=1 * 35=1^{3}+35^{3}=1+42875=42876 \\
& \therefore(1 * 2) * 3 \neq 1 *(2 * 3)
\end{aligned}
$$

Operation *is not associative.

Therefore, Operation * is commutative, but not associative.
The correct answer is B.
:::

:::answer
**Answer:** B
:::

:::

:::question{number="MISC-1" kind="additional_exercise" id="sol_1.misc.1" topic="Inverse of f(x) = 10x+7"}
#### Additional Question MISC-1

:::prompt
Let $f: R \rightarrow R$ be defined as $f(x)=10 x+7$. Find the function $g: R \rightarrow R$ such that $g o f=f o g=\mathrm{I}_{R}$.
:::

:::solution{label="Solution"}
$f: R \rightarrow R$ is defined as $f(x)=10 x+7$
For one-one:

$$
\begin{aligned}
& f(x)=f(y) \text { where } x, y \in R \\
& \Rightarrow 10 x+7=10 y+7 \\
& \Rightarrow x=y \\
& \therefore f \text { is one-one. }
\end{aligned}
$$

For onto:

$$
\begin{aligned}
& y \in R, \text { Let } y=10 x+7 \\
& \Rightarrow x=\frac{y-7}{10} \in R
\end{aligned}
$$

For any $y \in R$, there exists $x=\frac{y-7}{10} \in R$ such that

$$
f(x)=f\left(\frac{y-7}{10}\right)=10\left(\frac{y-7}{10}\right)+7=y-7+7=y
$$

$\therefore f$ is onto.
Thus, $f$ is an invertible function.

Let us define $g: R \rightarrow R$ as $g(y)=\frac{y-7}{10}$.
Now,

$$
g o f(x)=g(f(x))=g(10 x+7)=\frac{(10 x+7)-7}{10}=\frac{10 x}{10}=10
$$

And,

$$
\begin{aligned}
& f o g(y)=f(g(y))=f\left(\frac{y-7}{10}\right)=10\left(\frac{y-7}{10}\right)+7=y-7+7=y \\
& \therefore g o f=\mathrm{I}_{R} \text { and } f o g=\mathrm{I}_{R}
\end{aligned}
$$

Hence, the required function $g: R \rightarrow R$ as $g(y)=\frac{y-7}{10}$.
:::

:::

:::question{number="MISC-2" kind="additional_exercise" id="sol_1.misc.2" topic="Invertible function on whole numbers"}
#### Additional Question MISC-2

:::prompt
Let $f: W \rightarrow W$ be defined as $f(n)=n-1$, if is odd and $f(n)=n+1$, if $n$ is even. Show that $f$ is invertible. Find the inverse of f. Here, W is the set of all whole numbers.
:::

:::solution{label="Solution"}
$f: W \rightarrow W$ is defined as $f(n)=\left\{\begin{array}{l}n-1, \text { If } n \text { is odd } \\ n+1, \text { If } n \text { is even }\end{array}\right\}$
For one-one:

$$
f(n)=f(m)
$$

If $n$ is odd and $m$ is even, then we will have $n-1=m+1$.

$$
\Rightarrow n-m=2
$$

Similarly, the possibility of $n$ being even and $m$ being odd can also be ignored under a similar argument.
∴ Both $n$ and $m$ must be either odd or even.
Now, if both $n$ and $m$ are odd, then we have:

$$
\begin{aligned}
& f(n)=f(m) \\
& \Rightarrow n-1=m-1 \\
& \Rightarrow n=m
\end{aligned}
$$

Again, if both $n$ and $m$ are even, then we have:

$$
\begin{aligned}
& f(n)=f(m) \\
& \Rightarrow n+1=m+1 \\
& \Rightarrow n=m
\end{aligned}
$$

$\therefore f$ is one-one.
For onto:
Any odd number $2 r+1$ in co-domain N is the image of $2 r$ in domain N and any even number $2 r$ in co-domain N is the image of $2 r+1$ in domain N .
$\therefore f$ is onto.
$f$ is an invertible function.
Let us define $g: W \rightarrow W$ as $f(m)=\left\{\begin{array}{l}m-1, \text { If } m \text { is odd } \\ m+1, \text { If } m \text { is even }\end{array}\right\}$
When $r$ is odd

$$
g o f(n)=g(f(n))=g(n-1)=n-1+1=n
$$

When $r$ is even
$\operatorname{gof}(n)=g(f(n))=g(n+1)=n+1-1=n$
When $m$ is odd

$$
f o g(n)=f(g(m))=f(m-1)=m-1+1=m
$$

When $m$ is even

$$
\begin{aligned}
& f o g(m)=f(g(m))=f(m+1)=m+1-1=m \\
& \therefore g o f=\mathrm{I}_{W} \text { and } f o g=\mathrm{I}_{W}
\end{aligned}
$$

$f$ is invertible and the inverse of $f$ is given by $f^{-1}=g$, which is the same as $f$. inverse of $f$ is $f$ itself.
:::

:::

:::question{number="MISC-3" kind="additional_exercise" id="sol_1.misc.3" topic="Composition f(f(x)) for a quadratic"}
#### Additional Question MISC-3

:::prompt
If $f: R \rightarrow R$ be defined as $f(x)=x^{2}-3 x+2$, find $f(f(x))$.
:::

:::solution{label="Solution"}
$f: R \rightarrow R$ is defined as $f(x)=x^{2}-3 x+2$.

$$
\begin{aligned}
& f(f(x))=f\left(x^{2}-3 x+2\right) \\
& =\left(x^{2}-3 x+2\right)^{2}-3\left(x^{2}-3 x+2\right)+2 \\
& =\left(x^{4}+9 x^{2}+4-6 x^{3}-12 x+4 x^{2}\right)+\left(-3 x^{2}+9 x-6\right)+2 \\
& =x^{4}-6 x^{3}+10 x^{2}-3 x
\end{aligned}
$$
:::

:::

:::question{number="MISC-6" kind="additional_exercise" id="sol_1.misc.6" topic="Injective composition with a non-injective g"}
#### Additional Question MISC-6

:::prompt
Give examples of two functions $f: N \rightarrow Z$ and $g: Z \rightarrow Z$ such that gof is injective but $g$ is not injective.
(Hint: Consider $f(x)=x$ and $g(x)=|x|$ )
:::

:::solution{label="Solution"}
Define $f: N \rightarrow Z$ as $f(x)=x$ and $g: Z \rightarrow Z$ as $g(x)=|x|$
Let us first show that $g$ is not injective.

$$
\begin{aligned}
& (-1)=|-1|=1 \\
& (1)=|1|=1 \\
& \therefore(-1)=g(1), \text { but }-1 \neq 1
\end{aligned}
$$

$\therefore g$ is not injective.
$g o f: N \rightarrow Z$ is defined as $g o f(x)=g(f(x))=g(x)=|x|$
$x, y \in N$ such that $g o f(x)=g o f(y)$

$$
\Rightarrow|x|=|y|
$$

Since $x, y \in N$, both are positive.
$\therefore|x|=|y|$
$\Rightarrow x=y$
∴ gof is injective.
:::

:::

:::question{number="MISC-7" kind="additional_exercise" id="sol_1.misc.7" topic="Onto composition with a non-onto f"}
#### Additional Question MISC-7

:::prompt
Given examples of two functions $f: N \rightarrow N$ and $g: N \rightarrow N$ such that gof is onto but $f$ is not onto.
(Hint: Consider $f(x)=x+1$ and $g(x)=\left\{\begin{array}{ll}x-1, & \text { if } x>1 \\ 1, & \text { if } x=1\end{array}\right\}$ )
:::

:::solution{label="Solution"}
Define $f: N \rightarrow Z$ as $f(x)=x+1$ and $g: Z \rightarrow Z$ as $g(x)=\left\{\begin{array}{ll}x-1, & \text { if } x>1 \\ 1, & \text { if } x=1\end{array}\right\}$
Let us first show that $g$ is not onto.
Consider element 1 in co-domain $N$. This element is not an image of any of the elements in domain $N$.
$\therefore f$ is not onto.
$g: N \rightarrow N$ is defined by

$$
\operatorname{gof}(x)=g(f(x))=g(x+1)=x+1-1=x \quad[x \in N \Rightarrow x+1>1]
$$

For $y \in N$, there exists $x=y \in N$ such that $\operatorname{gof}(x)=y$.
∴ gof is onto.
:::

:::

:::question{number="MISC-9" kind="additional_exercise" id="sol_1.misc.9" topic="Identity and invertible element in a power set"}
#### Additional Question MISC-9

:::prompt
Given a non-empty set $X$, consider the binary operation *: $\mathrm{P}(X) \times \mathrm{P}(X) \rightarrow \mathrm{P}(X)$ given by $A^{*} B=A \cap B \forall A, B$ in $P(X)$ is the power set of $X$. Show that $X$ is the identity element for this operation and $X$ is the only invertible element in $P(X)$ with respect to the operation *.
:::

:::solution{label="Solution"}
$$
\begin{aligned}
& \mathrm{P}(X) \times \mathrm{P}(X) \rightarrow \mathrm{P}(X) \text { given by } A^{*} B=A \cap B \forall A, B \text { in } P(X) \\
& A \cap X=A=X \cap A \text { for all } A \in P(X) \\
& \Rightarrow A^{*} X=A=X * A \text { for all } A \in P(X)
\end{aligned}
$$

$X$ is the identity element for the given binary operation *.
An element $A \in P(X)$ is invertible if there exists $B \in P(X)$ such that

$$
A^{*} B=X=B^{*} A \quad[\text { As } X \text { is the identity element }]
$$

Or

$$
A \cap B=X=B \cap A
$$

This case is possible only when $A=X=B$.
$X$ is the only invertible element in $P(X)$ with respect to the given operation *.
:::

:::

:::question{number="MISC-11" kind="additional_exercise" id="sol_1.misc.11" topic="Inverse of a function between finite sets"}
#### Additional Question MISC-11

:::prompt
Let $\mathrm{S}=\{a, b, c\}$ and $T=\{1,2,3\}$. Find $F^{-1}$ of the following functions $F$ from $S$ to $T$, if it exists.

i. $\quad F=\{(a, 3),(b, 2),(c, 1)\}$
ii. $\quad F=\{(a, 2),(b, 1),(c, 1)\}$
:::

:::solution{label="Solution"}
$\mathrm{S}=\{a, b, c\}, T=\{1,2,3\}$

i. $\quad F: S \rightarrow T$ is defined by $F=\{(a, 3),(b, 2),(c, 1)\}$
$$
\Rightarrow F(a)=3, F(b)=2, F(c)=1
$$
Therefore, $F^{-1}: T \rightarrow S$ is given by $F^{-1}=\{(3, a),(2, b),(1, c)\}$
ii. $\quad F: S \rightarrow T$ is defined by $F=\{(a, 2),(b, 1),(c, 1)\}$
Since, $F(b)=F(c)=1, F$ is not one-one.
Hence, $F$ is not invertible i.e., $F^{-1}$ does not exists.
:::

:::

:::question{number="MISC-12" kind="additional_exercise" id="sol_1.misc.12" topic="Commutative, associative, distributive operations"}
#### Additional Question MISC-12

:::prompt
Consider the binary operations*: $R \times R \rightarrow R$ and $o: R \times R \rightarrow R$ defined as $a^{*} b=|a-b|$ and $a o b=a, \forall a, b \in R$. Show that *is commutative but not associative 0 is associative but not commutative. Further, show that $\forall a, b, c \in R, a^{*}(b o c)=\left(a^{*} b\right) o\left(a^{*} c\right)$. [ If it is so, we say that the operation * distributes over the operation 0 ]. Does 0 distribute over*? Justify your answer.
:::

:::solution{label="Solution"}
It is given that ${ }^{*}: R \times R \rightarrow R$ and $o: R \times R \rightarrow R$ defined as $a^{*} b=|a-b|$ and $a o b=a, \forall a, b \in R$. For $a, b \in R$, we have $a^{*} b=|a-b|$ and $b^{*} a=|b-a|=|-(a-b)|=|a-b|$
$\therefore a^{*} b=b^{*} a$
∴ The operation * is commutative.

$$
\begin{aligned}
& (1 * 2) * 3=(|1-2|) * 3=1 * 3=|1-3|=2 \\
& 1 *(2 * 3)=1 *(|2-3|)=1 * 1=|1-1|=0 \\
& \therefore(1 * 2) * 3 \neq 1 *(2 * 3) \quad \text { where } 1,2,3 \in R \\
& \therefore \text { The operation } * \text { is not associative. }
\end{aligned}
$$

Now, consider the operation 0 :
It can be observed that $1 o 2=1$ and $2 o 1=2$.

$$
\therefore 1 o 2 \neq 2 o 1 \quad(\text { where } 1,2 \in R)
$$

∴ The operation 0 is not commutative.
Let $a, b, c \in R$. Then, we have:

$$
\begin{aligned}
& (a o b) o c=a o c=a \\
& a o(b o c)=a o b=a \\
& \Rightarrow(a o b) o c=a o(b o c)
\end{aligned}
$$

∴ The operation 0 is associative.
Now, let $a, b, c \in R$, then we have:

$$
\begin{aligned}
& a *(b o c)=a * b=|a-b| \\
& (a * b) o(a * c)=(|a-b|) o(|a-c|)=|a-b|
\end{aligned}
$$

Hence, $a^{*}(b o c)=\left(a^{*} b\right) o\left(a^{*} c\right)$
Now,

$$
\begin{aligned}
& 1 o(2 * 3)=1 o(|2-3|)=1 o 1=1 \\
& (1 o 2) *(1 o 3)=1 * 1=|1-1|=0
\end{aligned}
$$

$$
\therefore 1 o(2 * 3) \neq(1 o 2) *(1 o 3) \quad \text { where } 1,2,3 \in R
$$

∴ The operation 0 does not distribute over*.
:::

:::

:::question{number="MISC-13" kind="additional_exercise" id="sol_1.misc.13" topic="Identity and inverses under symmetric difference"}
#### Additional Question MISC-13

:::prompt
Given a non - empty set $X$, let $*: \mathrm{P}(X) \times \mathrm{P}(X) \rightarrow \mathrm{P}(X)$ be defined as $A^{*} B=(A-B) \cup(B-A)$, $\forall A, B \in P(X)$. Show that the empty set $\Phi$ is the identity for the operation * and all the elements $A$ of $P(X)$ are invertible with $A^{-1}=A$.
(Hint: $(A-\Phi) \cup(\Phi-A)=A$ and $(A-A) \cup(A-A)=A^{*} A=\Phi$ ) .
:::

:::solution{label="Solution"}
It is given that $*: \mathrm{P}(X) \times \mathrm{P}(X) \rightarrow \mathrm{P}(X)$ is defined as $A^{*} B=(A-B) \cup(B-A), \forall A, B \in P(X)$ $A \in P(X)$ then,

$$
\begin{aligned}
& A^{*} \Phi=(A-\Phi) \cup(\Phi-A)=A \cup \Phi=A \\
& \Phi^{*} A=(\Phi-A) \cup(A-\Phi)=\Phi \cup A=A \\
& \therefore A^{*} \Phi=A=\Phi^{*} A \quad \text { for all } A \in P(X)
\end{aligned}
$$

$\Phi$ is the identity for the operation *.
Element $A \in P(X)$ will be invertible if there exists $B \in P(X)$ such that $A^{*} B=\Phi=B^{*} A \quad[$ As $\Phi$ is the identity element $]$

$$
A^{*} A=(A-A) \cup(A-A)=\Phi \cup \Phi=\Phi \text { for all } A \in P(X) .
$$

All the elements $A$ of $P(X)$ are invertible with $A^{-1}=A$.
:::

:::

:::question{number="MISC-14" kind="additional_exercise" id="sol_1.misc.14" topic="Identity and inverses - modular addition"}
#### Additional Question MISC-14

:::prompt
Define a binary operation *on the set \{0,1,2,3,4,5\} as

$$
a+b=\left\{\begin{array}{ll}
a+b, & \text { if } a+b<6 \\
a+b-6 & \text { if } a+b \geq 6
\end{array}\right\}
$$

Show that zero is the identity for this operation and each element $a \neq 0$ of the set is invertible with $6-a$ being the inverse of $a$.
:::

:::solution{label="Solution"}
Let $X=\{0,1,2,3,4,5\}$
The operation *is defined as $a+b=\left\{\begin{array}{ll}a+b, & \text { if } a+b<6 \\ a+b-6, & \text { if } a+b \geq 6\end{array}\right\}$
An element $e \in X$ is the identity element for the operation ${ }^{*}$, if $a^{*} e=a=e^{*} a \quad \forall a \in X$ For $a \in X$,

$$
\begin{array}{ll}
a * 0=a+0=a & {[a \in X \Rightarrow a+0<6]} \\
0 * a=0+a=a & {[a \in X \Rightarrow 0+a<6]} \\
\therefore a * 0=a=0 * a & \forall a \in X
\end{array}
$$

Thus, 0 is the identity element for the given operation *.
An element $a \in X$ is invertible if there exists $b \in X$ such that $a * b=0=b^{*} a$.
i.e., $\left\{\begin{array}{l}a+b=0=b+a, \quad \text { if } a+b<6 \\ a+b-6=0=b+a-6 \quad \text { if } a+b \geq 6\end{array}\right\}$

$$
\Rightarrow a=-b \text { or } b=6-a
$$

$X=\{0,1,2,3,4,5\}$ and $a, b \in X$. Then $a \neq-b$.
$\therefore b=6-a$ is the inverse of $a$ for all $a \in X$.
Inverse of an element $a \in X, a \neq 0$ is $6-a$ i.e., $a-1=6-a$.
:::

:::

:::question{number="MISC-18" kind="additional_exercise" id="sol_1.misc.18" topic="Signum and greatest integer composition"}
#### Additional Question MISC-18

:::prompt
Let $f: R \rightarrow R$ be the Signum Function defined as

$$
f(x)=\left\{\begin{array}{l}
1, x>0 \\
0, x=0 \\
-1, x<0
\end{array}\right\} \text { and } g: R \rightarrow R \text { be the }
$$

greatest integer function given by $g(x)=[x]$, where $[x]$ is greatest integer less than or equal to $x$. Then does fog and gof coincide in $(0,1]$ ?
:::

:::solution{label="Solution"}
It is given that $f: R \rightarrow R$ be the Signum Function defined as

$$
f(x)=\left\{\begin{array}{l}
1, x>0 \\
0, x=0 \\
-1, x<0
\end{array}\right\}
$$

Also $g: R \rightarrow R$ is defined as $g(x)=[x]$, where $[x]$ is greatest integer less than or equal to $x$. Now let $x \in(0,1]$,

$$
[x]=1 \text { if } x=1 \text { and }[x]=0 \text { if } 0<x<1 .
$$

$$
\begin{aligned}
& \therefore f \circ g(x)=f(g(x))=f([x])=\left\{\begin{array}{ll}
f(1), & \text { if } x=1 \\
f(0), & \text { if } x \in(0,1)
\end{array}\right\}=\left\{\begin{array}{ll}
1, & \text { if } x=1 \\
0, & \text { if } x \in(0,1)
\end{array}\right\} \\
& \operatorname{gof}(x)=g(f(x)) \\
& =g(1) \\
& =[1]=1
\end{aligned}
$$

Thus, when $x \in(0,1)$, we have $f \circ g(x)=0$ and $g o f(x)=1$.
Hence, fog and gof does not coincide in (0,1].
:::

:::

:::question{number="MISC-19" kind="additional_exercise" id="sol_1.misc.19" topic="MCQ - number of binary operations on {a,b}"}
#### Additional Question MISC-19

:::prompt
Number of binary operations on the set $\{a, b\}$ are

A. 10
B. 16
C. 20
D. 8
:::

:::solution{label="Solution"}
A binary operation * on $\{a, b\}$ is a function from $\{a, b\} \times\{a, b\} \rightarrow\{a, b\}$ i.e., * is a function from $\{(a, a),(a, b),(b, a),(b, b)\} \rightarrow\{a, b\}$
Hence, the total number of binary operations on the set $\{a, b\}$ is $2^{4}=16$.
The correct answer is B.
:::

:::answer
**Answer:** B
:::

:::
