---
subject: maths
class: 12
chapter: 1
lang: en
title: "Relations and Functions"
---

# Relations and Functions

## Examples

:::example{number="1.1" kind="example" id="ex_1.1" topic="Empty and universal relations"}
#### Example 1.1

:::prompt
Let A be the set of all students of a boys school. Show that the relation R in A given by $\mathrm{R}=\{(a, b): a$ is sister of $b\}$ is the empty relation and $\mathrm{R}^{\prime}=\{(a, b):$ the difference between heights of $a$ and $b$ is less than 3 meters\} is the universal relation.
:::

:::solution{label="Solution"}
Since the school is boys school, no student of the school can be sister of any student of the school. Hence, $\mathrm{R}=\phi$, showing that R is the empty relation. It is also obvious that the difference between heights of any two students of the school has to be less than 3 meters. This shows that $\mathrm{R}^{\prime}=\mathrm{A} \times \mathrm{A}$ is the universal relation.

Remark In Class XI, we have seen two ways of representing a relation, namely raster method and set builder method. However, a relation $R$ in the set $\{1,2,3,4\}$ defined by $R$ $=\{(a, b): b=a+1\}$ is also expressed as $a \mathrm{R} b$ if and only if $b=a+1$ by many authors. We may also use this notation, as and when convenient.

If $(a, b) \in \mathrm{R}$, we say that $a$ is related to $b$ and we denote it as $a \mathrm{R} b$.
One of the most important relation, which plays a significant role in Mathematics, is an equivalence relation. To study equivalence relation, we first consider three types of relations, namely reflexive, symmetric and transitive.
Definition 3 A relation R in a set A is called

(i) reflexive, if $(a, a) \in \mathrm{R}$, for every $a \in \mathrm{~A}$,
(ii) symmetric, if $\left(a_{1}, a_{2}\right) \in \mathrm{R}$ implies that $\left(a_{2}, a_{1}\right) \in \mathrm{R}$, for all $a_{1}, a_{2} \in \mathrm{~A}$.
(iii) transitive, if $\left(a_{1}, a_{2}\right) \in \mathrm{R}$ and $\left(a_{2}, a_{3}\right) \in \mathrm{R}$ implies that $\left(a_{1}, a_{3}\right) \in \mathrm{R}$, for all $a_{1}, a_{2}$, $a_{3} \in \mathrm{~A}$.

Definition 4 A relation R in a set A is said to be an equivalence relation if R is reflexive, symmetric and transitive.
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

:::example{number="1.5" kind="example" id="ex_1.5" topic="Equivalence relation - divisibility by 2"}
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

In Example 5, note that all even integers are related to zero, as $(0, \pm 2),(0, \pm 4)$ etc., lie in R and no odd integer is related to 0, as (0, ± 1), (0, ± 3) etc., do not lie in R. Similarly, all odd integers are related to one and no even integer is related to one. Therefore, the set E of all even integers and the set O of all odd integers are subsets of Z satisfying following conditions:

(i) All elements of E are related to each other and all elements of O are related to each other.
(ii) No element of E is related to any element of O and vice-versa.
(iii) E and O are disjoint and $\mathbf{Z}=\mathrm{E} \cup \mathrm{O}$.

The subset E is called the equivalence class containing zero and is denoted by [0]. Similarly, O is the equivalence class containing 1 and is denoted by [1]. Note that $[0] \neq[1],[0]=[2 r]$ and $[1]=[2 r+1], r \in \mathbf{Z}$. Infact, what we have seen above is true for an arbitrary equivalence relation R in a set X. Given an arbitrary equivalence relation R in an arbitrary set X, R divides X into mutually disjoint subsets $\mathrm{A}_{i}$ called partitions or subdivisions of X satisfying:

(i) all elements of $\mathrm{A}_{i}$ are related to each other, for all $i$.
(ii) no element of $\mathrm{A}_{i}$ is related to any element of $\mathrm{A}_{j}, i \neq j$.
(iii) $\cup \mathrm{A}_{j}=\mathrm{X}$ and $\mathrm{A}_{i} \cap \mathrm{~A}_{j}=\phi, i \neq j$.

The subsets $\mathrm{A}_{i}$ are called equivalence classes. The interesting part of the situation is that we can go reverse also. For example, consider a subdivision of the set $\mathbf{Z}$ given by three mutually disjoint subsets $\mathrm{A}_{1}, \mathrm{~A}_{2}$ and $\mathrm{A}_{3}$ whose union is $\mathbf{Z}$ with

$$
\begin{aligned}
& \mathrm{A}_{1}=\{x \in \mathbf{Z}: x \text { is a multiple of } 3\}=\{\ldots,-6,-3,0,3,6, \ldots\} \\
& \mathrm{A}_{2}=\{x \in \mathbf{Z}: x-1 \text { is a multiple of } 3\}=\{\ldots,-5,-2,1,4,7, \ldots\} \\
& \mathrm{A}_{3}=\{x \in \mathbf{Z}: x-2 \text { is a multiple of } 3\}=\{\ldots,-4,-1,2,5,8, \ldots\}
\end{aligned}
$$

Define a relation R in $\mathbf{Z}$ given by $\mathrm{R}=\{(a, b): 3$ divides $a-b\}$. Following the arguments similar to those used in Example 5, we can show that R is an equivalence relation. Also, $\mathrm{A}_{1}$ coincides with the set of all integers in $\mathbf{Z}$ which are related to zero, $\mathrm{A}_{2}$ coincides with the set of all integers which are related to 1 and $\mathrm{A}_{3}$ coincides with the set of all integers in $\mathbf{Z}$ which are related to 2 . Thus, $\mathrm{A}_{1}=[0], \mathrm{A}_{2}=[1]$ and $\mathrm{A}_{3}=[2]$. In fact, $\mathrm{A}_{1}=[3 r], \mathrm{A}_{2}=[3 r+1]$ and $\mathrm{A}_{3}=[3 r+2]$, for all $r \in \mathbf{Z}$.
:::

:::

:::example{number="1.6" kind="example" id="ex_1.6" topic="Equivalence relation - odd/even parity"}
#### Example 1.6

:::prompt
Let R be the relation defined in the set $\mathrm{A}=\{1,2,3,4,5,6,7\}$ by $\mathrm{R}=\{(a, b):$ both $a$ and $b$ are either odd or even $\}$. Show that R is an equivalence relation. Further, show that all the elements of the subset \{1,3,5,7\} are related to each other and all the elements of the subset \{2, 4, 6\} are related to each other, but no element of the subset \{1, 3, 5, 7\} is related to any element of the subset \{2, 4, 6\}.
:::

:::solution{label="Solution"}
Given any element $a$ in A, both $a$ and $a$ must be either odd or even, so that $(a, a) \in \mathrm{R}$. Further, $(a, b) \in \mathrm{R} \Rightarrow$ both $a$ and $b$ must be either odd or even $\Rightarrow(b, a) \in \mathrm{R}$. Similarly, $(a, b) \in \mathrm{R}$ and $(b, c) \in \mathrm{R} \Rightarrow$ all elements $a, b, c$, must be either even or odd simultaneously $\Rightarrow(a, c) \in \mathrm{R}$. Hence, R is an equivalence relation. Further, all the elements of $\{1,3,5,7\}$ are related to each other, as all the elements of this subset are odd. Similarly, all the elements of the subset \{2, 4, 6\} are related to each other, as all of them are even. Also, no element of the subset \{1, 3, 5, 7\} can be related to any element of \{2, 4, 6\}, as elements of \{1, 3, 5, 7\} are odd, while elements of \{2, 4, 6\} are even.
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
Suppose $f\left(x_{1}\right)=f\left(x_{2}\right)$. Note that if $x_{1}$ is odd and $x_{2}$ is even, then we will have $x_{1}+1=x_{2}-1$, i.e., $x_{2}-x_{1}=2$ which is impossible. Similarly, the possibility of $x_{1}$ being even and $x_{2}$ being odd can also be ruled out, using the similar argument. Therefore, both $x_{1}$ and $x_{2}$ must be either odd or even. Suppose both $x_{1}$ and $x_{2}$ are odd. Then $f\left(x_{1}\right)=f\left(x_{2}\right) \Rightarrow x_{1}+1=x_{2}+1 \Rightarrow x_{1}=x_{2}$. Similarly, if both $x_{1}$ and $x_{2}$ are even, then also $f\left(x_{1}\right)=f\left(x_{2}\right) \Rightarrow x_{1}-1=x_{2}-1 \Rightarrow x_{1}=x_{2}$. Thus, $f$ is one-one. Also, any odd number $2 r+1$ in the co-domain $\mathbf{N}$ is the image of $2 r+2$ in the domain $\mathbf{N}$ and any even number $2 r$ in the co-domain $\mathbf{N}$ is the image of $2 r-1$ in the domain $\mathbf{N}$. Thus, $f$ is onto.
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

:::example{number="1.14" kind="example" id="ex_1.14" topic="One-one implies onto on finite set"}
#### Example 1.14

:::prompt
Show that a one-one function $f:\{1,2,3\} \rightarrow\{1,2,3\}$ must be onto.
:::

:::solution{label="Solution"}
Since $f$ is one-one, three elements of $\{1,2,3\}$ must be taken to 3 different elements of the co-domain $\{1,2,3\}$ under $f$. Hence, $f$ has to be onto.

Remark The results mentioned in Examples 13 and 14 are also true for an arbitrary finite set X, i.e., a one-one function $f: \mathrm{X} \rightarrow \mathrm{X}$ is necessarily onto and an onto map $f: \mathrm{X} \rightarrow \mathrm{X}$ is necessarily one-one, for every finite set X . In contrast to this, Examples 8 and 10 show that for an infinite set, this may not be true. In fact, this is a characteristic difference between a finite and an infinite set.
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

:::example{number="1.16" kind="example" id="ex_1.16" topic="gof not equal to fog"}
#### Example 1.16

:::prompt
Find $g o f$ and $f o g$, if $f: \mathbf{R} \rightarrow \mathbf{R}$ and $g: \mathbf{R} \rightarrow \mathbf{R}$ are given by $f(x)=\cos x$ and $g(x)=3 x^{2}$. Show that $g o f \neq f o g$.
:::

:::solution{label="Solution"}
We have $g o f(x)=g(f(x))=g(\cos x)=3(\cos x)^{2}=3 \cos ^{2} x$. Similarly, $f o g(x)=f(g(x))=f\left(3 x^{2}\right)=\cos \left(3 x^{2}\right)$. Note that $3 \cos ^{2} x \neq \cos 3 x^{2}$, for $x=0$. Hence, gof $\neq$ fog .
Definition 9 A function $f: \mathrm{X} \rightarrow \mathrm{Y}$ is defined to be invertible, if there exists a function $g: \mathrm{Y} \rightarrow \mathrm{X}$ such that $g \circ f=\mathrm{I}_{\mathrm{X}}$ and fog $=\mathrm{I}_{\mathrm{Y}}$. The function $g$ is called the inverse of $f$ and is denoted by $f^{-1}$.

Thus, if $f$ is invertible, then $f$ must be one-one and onto and conversely, if $f$ is one-one and onto, then $f$ must be invertible. This fact significantly helps for proving a function $f$ to be invertible by showing that $f$ is one-one and onto, specially when the actual inverse of $f$ is not to be determined.
:::

:::

:::example{number="1.17" kind="example" id="ex_1.17" topic="Invertible function and its inverse"}
#### Example 1.17

:::prompt
Let $f: \mathbf{N} \rightarrow \mathrm{Y}$ be a function defined as $f(x)=4 x+3$, where, $\mathrm{Y}=\{y \in \mathbf{N}: y=4 x+3$ for some $x \in \mathbf{N}\}$. Show that $f$ is invertible. Find the inverse.
:::

:::solution{label="Solution"}
Consider an arbitrary element $y$ of Y. By the definition of Y, $y=4 x+3$, for some $x$ in the domain $\mathbf{N}$. This shows that $x=\frac{(y-3)}{4}$. Define $g: \mathrm{Y} \rightarrow \mathbf{N}$ by

$$
g(y)=\frac{(y-3)}{4} . \text { Now, } g \circ f(x)=g(f(x))=g(4 x+3)=\frac{(4 x+3-3)}{4}=x \text { and }
$$

$f o g(y)=f(g(y))=f\left(\frac{(y-3)}{4}\right)=\frac{4(y-3)}{4}+3=y-3+3=y$. This shows that $g o f=\mathrm{I}_{\mathrm{N}}$ and $f o g=\mathrm{I}_{\mathrm{Y}}$, which implies that $f$ is invertible and $g$ is the inverse of $f$.
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
The smallest relation $\mathrm{R}_{1}$ containing $(1,2)$ and $(2,3)$ which is reflexive and transitive but not symmetric is \{(1, 1), (2, 2), (3, 3), (1, 2), (2, 3), (1, 3)\}. Now, if we add the pair $(2,1)$ to $\mathrm{R}_{1}$ to get $\mathrm{R}_{2}$, then the relation $\mathrm{R}_{2}$ will be reflexive, transitive but not symmetric. Similarly, we can obtain $\mathrm{R}_{3}$ by adding $(3,2)$ to $\mathrm{R}_{1}$ to get the desired relation. However, we can not add two pairs $(2,1),(3,2)$ or single pair $(3,1)$ to $\mathrm{R}_{1}$ at a time, as by doing so, we will be forced to add the remaining pair in order to maintain transitivity and in the process, the relation will become symmetric also which is not required. Thus, the total number of desired relations is three.
:::

:::

:::example{number="1.24" kind="example" id="ex_1.24" topic="Counting equivalence relations"}
#### Example 1.24

:::prompt
Show that the number of equivalence relation in the set $\{1,2,3\}$ containing $(1,2)$ and $(2,1)$ is two.
:::

:::solution{label="Solution"}
The smallest equivalence relation $\mathrm{R}_{1}$ containing ( 1,2 ) and ( 2,1 ) is $\{(1,1)$, $(2,2),(3,3),(1,2),(2,1)\}$. Now we are left with only 4 pairs namely $(2,3),(3,2)$, $(1,3)$ and $(3,1)$. If we add any one, say $(2,3)$ to $\mathrm{R}_{1}$, then for symmetry we must add $(3,2)$ also and now for transitivity we are forced to add $(1,3)$ and $(3,1)$. Thus, the only equivalence relation bigger than $\mathrm{R}_{1}$ is the universal relation. This shows that the total number of equivalence relations containing $(1,2)$ and $(2,1)$ is two.
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
