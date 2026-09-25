---
subject: maths
class: 12
chapter: 4
lang: en
title: "Determinants"
---

# Determinants

## Examples

:::example{number="1" kind="example" id="ex_4.1" topic="Evaluating a 2x2 determinant"}
#### Example 1

:::prompt
Evaluate $\left|\begin{array}{cc}2 & 4 \\ -1 & 2\end{array}\right|$.
:::

:::solution{label="Solution"}
We have $\left|\begin{array}{cc}2 & 4 \\ -1 & 2\end{array}\right|=2(2)-4(-1)=4+4=8$.
:::

:::

:::example{number="2" kind="example" id="ex_4.2" topic="Evaluating a 2x2 determinant with variables"}
#### Example 2

:::prompt
Evaluate $\left|\begin{array}{cc}x & x+1 \\ x-1 & x\end{array}\right|$
:::

:::solution{label="Solution"}
We have

$$
\left|\begin{array}{cc}
x & x+1 \\
x-1 & x
\end{array}\right|=x(x)-(x+1)(x-1)=x^{2}-\left(x^{2}-1\right)=x^{2}-x^{2}+1=1
$$
:::

:::

:::example{number="3" kind="example" id="ex_4.3" topic="Evaluating a 3x3 determinant"}
#### Example 3

:::prompt
Evaluate the determinant $\Delta=\left|\begin{array}{rrr}1 & 2 & 4 \\ -1 & 3 & 0 \\ 4 & 1 & 0\end{array}\right|$.
:::

:::solution{label="Solution"}
Note that in the third column, two entries are zero. So expanding along third column $\left(\mathrm{C}_{3}\right)$, we get

$$
\begin{aligned}
\Delta & =4\left|\begin{array}{rr}
-1 & 3 \\
4 & 1
\end{array}\right|-0\left|\begin{array}{ll}
1 & 2 \\
4 & 1
\end{array}\right|+0\left|\begin{array}{rr}
1 & 2 \\
-1 & 3
\end{array}\right| \\
& =4(-1-12)-0+0=-52
\end{aligned}
$$
:::

:::

:::example{number="4" kind="example" id="ex_4.4" topic="Evaluating a 3x3 determinant with trig entries"}
#### Example 4

:::prompt
Evaluate $\Delta=\left|\begin{array}{ccc}0 & \sin \alpha & -\cos \alpha \\ -\sin \alpha & 0 & \sin \beta \\ \cos \alpha & -\sin \beta & 0\end{array}\right|$.
:::

:::solution{label="Solution"}
Expanding along $\mathrm{R}_{1}$, we get

$$
\begin{aligned}
\Delta & =0\left|\begin{array}{cc}
0 & \sin \beta \\
-\sin \beta & 0
\end{array}\right|-\sin \alpha\left|\begin{array}{cc}
-\sin \alpha & \sin \beta \\
\cos \alpha & 0
\end{array}\right|-\cos \alpha\left|\begin{array}{cc}
-\sin \alpha & 0 \\
\cos \alpha & -\sin \beta
\end{array}\right| \\
& =0-\sin \alpha(0-\sin \beta \cos \alpha)-\cos \alpha(\sin \alpha \sin \beta-0) \\
& =\sin \alpha \sin \beta \cos \alpha-\cos \alpha \sin \alpha \sin \beta=0
\end{aligned}
$$
:::

:::

:::example{number="5" kind="example" id="ex_4.5" topic="Solving for x from equal determinants"}
#### Example 5

:::prompt
Find values of $x$ for which $\left|\begin{array}{cc}3 & x \\ x & 1\end{array}\right|=\left|\begin{array}{ll}3 & 2 \\ 4 & 1\end{array}\right|$.
:::

:::solution{label="Solution"}
We have $\left|\begin{array}{ll}3 & x \\ x & 1\end{array}\right|=\left|\begin{array}{ll}3 & 2 \\ 4 & 1\end{array}\right|$
i.e.

$$
3-x^{2}=3-8
$$

i.e.

$$
x^{2}=8
$$

Hence

$$
x= \pm 2 \sqrt{2}
$$
:::

:::

:::example{number="6" kind="example" id="ex_4.6" topic="Area of a triangle using determinants"}
#### Example 6

:::prompt
Find the area of the triangle whose vertices are (3, 8), (- 4, 2) and (5, 1).
:::

:::solution{label="Solution"}
The area of triangle is given by

$$
\Delta=\frac{1}{2}\left|\begin{array}{rrr}
3 & 8 & 1 \\
-4 & 2 & 1 \\
5 & 1 & 1
\end{array}\right|
$$

$$
\begin{aligned}
& =\frac{1}{2}[3(2-1)-8(-4-5)+1(-4-10)] \\
& =\frac{1}{2}(3+72-14)=\frac{61}{2}
\end{aligned}
$$
:::

:::

:::example{number="7" kind="example" id="ex_4.7" topic="Equation of a line via determinants"}
#### Example 7

:::prompt
Find the equation of the line joining $\mathrm{A}(1,3)$ and $\mathrm{B}(0,0)$ using determinants and find $k$ if $\mathrm{D}(k, 0)$ is a point such that area of triangle ABD is 3sq units.
:::

:::solution{label="Solution"}
Let $\mathrm{P}(x, y)$ be any point on AB . Then, area of triangle ABP is zero (Why?). So

$$
\frac{1}{2}\left|\begin{array}{lll}
0 & 0 & 1 \\
1 & 3 & 1 \\
x & y & 1
\end{array}\right|=0
$$

This gives

$$
\frac{1}{2}(y-3 x)=0 \text { or } y=3 x
$$

which is the equation of required line AB.
Also, since the area of the triangle ABD is 3 sq. units, we have

$$
\frac{1}{2}\left|\begin{array}{ccc}
1 & 3 & 1 \\
0 & 0 & 1 \\
k & 0 & 1
\end{array}\right|= \pm 3
$$

This gives, $\frac{-3 k}{2}= \pm 3$, i.e., $k=\mp 2$.
:::

:::

:::example{number="8" kind="example" id="ex_4.8" topic="Minor of a determinant element"}
#### Example 8

:::prompt
Find the minor of element 6 in the determinant $\Delta=\left|\begin{array}{lll}1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9\end{array}\right|$
:::

:::solution{label="Solution"}
Since 6 lies in the second row and third column, its minor $\mathrm{M}_{23}$ is given by

$$
\mathrm{M}_{23}=\left|\begin{array}{ll}
1 & 2 \\
7 & 8
\end{array}\right|=8-14=-6\left(\text { obtained by deleting } \mathrm{R}_{2} \text { and } \mathrm{C}_{3} \text { in } \Delta\right) .
$$

Definition 2 Cofactor of an element $a_{i j}$, denoted by $\mathrm{A}_{i j}$ is defined by

$$
\mathrm{A}_{i j}=(-1)^{i+j} \mathrm{M}_{i j} \text {, where } \mathrm{M}_{i j} \text { is minor of } a_{i j} .
$$
:::

:::

:::example{number="9" kind="example" id="ex_4.9" topic="Minors and cofactors of a 2x2 determinant"}
#### Example 9

:::prompt
Find minors and cofactors of all the elements of the determinant $\left|\begin{array}{rr}1 & -2 \\ 4 & 3\end{array}\right|$
:::

:::solution{label="Solution"}
Minor of the element $a_{i j}$ is $\mathrm{M}_{i j}$
Here $a_{11}=1$. So $\mathrm{M}_{11}=$ Minor of $a_{11}=3$
$\mathrm{M}_{12}=$ Minor of the element $a_{12}=4$
$\mathrm{M}_{21}=$ Minor of the element $a_{21}=-2$
$\mathrm{M}_{22}=$ Minor of the element $a_{22}=1$
Now, cofactor of $a_{i j}$ is $\mathrm{A}_{i j}$. So

$$
\begin{aligned}
& A_{11}=(-1)^{1+1} \quad M_{11}=(-1)^{2}(3)=3 \\
& A_{12}=(-1)^{1+2} \quad M_{12}=(-1)^{3}(4)=-4 \\
& A_{21}=(-1)^{2+1} \quad M_{21}=(-1)^{3}(-2)=2 \\
& A_{22}=(-1)^{2+2} \quad M_{22}=(-1)^{4}(1)=1
\end{aligned}
$$
:::

:::

:::example{number="10" kind="example" id="ex_4.10" topic="Minors and cofactors of a 3x3 determinant"}
#### Example 10

:::prompt
Find minors and cofactors of the elements $a_{11}, a_{21}$ in the determinant

$$
\Delta=\left|\begin{array}{lll}
a_{11} & a_{12} & a_{13} \\
a_{21} & a_{22} & a_{23} \\
a_{31} & a_{32} & a_{33}
\end{array}\right|
$$
:::

:::solution{label="Solution"}
By definition of minors and cofactors, we have

$$
\text { Minor of } a_{11}=\mathrm{M}_{11}=\left|\begin{array}{ll}
a_{22} & a_{23} \\
a_{32} & a_{33}
\end{array}\right|=a_{22} a_{33}-a_{23} a_{32}
$$

Cofactor of $a_{11}=\mathrm{A}_{11}=(-1)^{1+1} \quad \mathrm{M}_{11}=a_{22} a_{33}-a_{23} a_{32}$
Minor of $a_{21}=\mathrm{M}_{21}=\left|\begin{array}{ll}a_{12} & a_{13} \\ a_{32} & a_{33}\end{array}\right|=a_{12} a_{33}-a_{13} a_{32}$
Cofactor of $a_{21}=\mathrm{A}_{21}=(-1)^{2+1} \quad \mathrm{M}_{21}=(-1)\left(a_{12} a_{33}-a_{13} a_{32}\right)=-a_{12} a_{33}+a_{13} a_{32}$
Remark Expanding the determinant $\Delta$, in Example 21, along $\mathrm{R}_{1}$, we have

$$
\begin{aligned}
\Delta & =(-1)^{1+1} a_{11}\left|\begin{array}{ll}
a_{22} & a_{23} \\
a_{32} & a_{33}
\end{array}\right|+(-1)^{1+2} a_{12}\left|\begin{array}{ll}
a_{21} & a_{23} \\
a_{31} & a_{33}
\end{array}\right|+(-1)^{1+3} a_{13}\left|\begin{array}{ll}
a_{21} & a_{22} \\
a_{31} & a_{32}
\end{array}\right| \\
& =a_{11} \mathrm{~A}_{11}+a_{12} \mathrm{~A}_{12}+a_{13} \mathrm{~A}_{13}, \text { where } \mathrm{A}_{i j} \text { is cofactor of } a_{i j} \\
& =\text { sum of product of elements of } \mathrm{R}_{1} \text { with their corresponding cofactors }
\end{aligned}
$$

Similarly, $\Delta$ can be calculated by other five ways of expansion that is along $\mathrm{R}_{2}, \mathrm{R}_{3}$, $\mathrm{C}_{1}, \mathrm{C}_{2}$ and $\mathrm{C}_{3}$.

Hence $\Delta=$ sum of the product of elements of any row (or column) with their corresponding cofactors.

- Note If elements of a row (or column) are multiplied with cofactors of any other row (or column), then their sum is zero. For example,

$$
\begin{aligned}
\Delta & =a_{11} \mathrm{~A}_{21}+a_{12} \mathrm{~A}_{22}+a_{13} \mathrm{~A}_{23} \\
& =a_{11}(-1)^{1+1}\left|\begin{array}{ll}
a_{12} & a_{13} \\
a_{32} & a_{33}
\end{array}\right|+a_{12}(-1)^{1+2}\left|\begin{array}{ll}
a_{11} & a_{13} \\
a_{31} & a_{33}
\end{array}\right|+a_{13}(-1)^{1+3}\left|\begin{array}{ll}
a_{11} & a_{12} \\
a_{31} & a_{32}
\end{array}\right| \\
& =\left|\begin{array}{lll}
a_{11} & a_{12} & a_{13} \\
a_{11} & a_{12} & a_{13} \\
a_{31} & a_{32} & a_{33}
\end{array}\right|=0 \text { (since } \mathrm{R}_{1} \text { and } \mathrm{R}_{2} \text { are identical) }
\end{aligned}
$$

Similarly, we can try for other rows and columns.
:::

:::

:::example{number="11" kind="example" id="ex_4.11" topic="Verifying a cofactor expansion identity"}
#### Example 11

:::prompt
Find minors and cofactors of the elements of the determinant $\left|\begin{array}{ccc}2 & -3 & 5 \\ 6 & 0 & 4 \\ 1 & 5 & -7\end{array}\right|$ and verify that $a_{11} \mathrm{~A}_{31}+a_{12} \mathrm{~A}_{32}+a_{13} \mathrm{~A}_{33}=0$
:::

:::solution{label="Solution"}
We have $M_{11}=\left|\begin{array}{cc}0 & 4 \\ 5 & -7\end{array}\right|=0-20=-20 ; A_{11}=(-1)^{1+1}(-20)=-20$

$$
\begin{array}{ll}
M_{12}=\left|\begin{array}{cc}
6 & 4 \\
1 & -7
\end{array}\right|=-42-4=-46 ; & A_{12}=(-1)^{1+2}(-46)=46 \\
M_{13}=\left|\begin{array}{cc}
6 & 0 \\
1 & 5
\end{array}\right|=30-0=30 ; & A_{13}=(-1)^{1+3}(30)=30 \\
M_{21}=\left|\begin{array}{cc}
-3 & 5 \\
5 & -7
\end{array}\right|=21-25=-4 ; \quad A_{21}=(-1)^{2+1}(-4)=4 \\
M_{22}=\left|\begin{array}{cc}
2 & 5 \\
1 & -7
\end{array}\right|=-14-5=-19 ; \quad A_{22}=(-1)^{2+2}(-19)=-19 \\
M_{23}=\left|\begin{array}{cc}
2 & -3 \\
1 & 5
\end{array}\right|=10+3=13 ; & A_{23}=(-1)^{2+3}(13)=-13 \\
M_{31}=\left|\begin{array}{cc}
-3 & 5 \\
0 & 4
\end{array}\right|=-12-0=-12 ; \quad A_{31}=(-1)^{3+1}(-12)=-12 \\
M_{32}=\left|\begin{array}{cc}
2 & 5 \\
6 & 4
\end{array}\right|=8-30=-22 ; \quad A_{32}=(-1)^{3+2}(-22)=22
\end{array}
$$

and

$$
\mathrm{M}_{33}=\left|\begin{array}{cc}
2 & -3 \\
6 & 0
\end{array}\right|=0+18=18 ; \quad \mathrm{A}_{33}=(-1)^{3+3}(18)=18
$$

Now

$$
a_{11}=2, a_{12}=-3, a_{13}=5 ; \mathrm{A}_{31}=-12, \mathrm{~A}_{32}=22, \mathrm{~A}_{33}=18
$$

So

$$
\begin{aligned}
& a_{11} \mathrm{~A}_{31}+a_{12} \mathrm{~A}_{32}+a_{13} \mathrm{~A}_{33} \\
& =2(-12)+(-3)(22)+5(18)=-24-66+90=0
\end{aligned}
$$
:::

:::

:::example{number="12" kind="example" id="ex_4.12" topic="Finding the adjoint of a matrix"}
#### Example 12

:::prompt
Find $\operatorname{adj} \mathrm{A}$ for $\mathrm{A}=\left[\begin{array}{ll}2 & 3 \\ 1 & 4\end{array}\right]$
:::

:::solution{label="Solution"}
We have $\mathrm{A}_{11}=4, \mathrm{~A}_{12}=-1, \mathrm{~A}_{21}=-3, \mathrm{~A}_{22}=2$

Hence

$$
\operatorname{adj} \mathrm{A}=\left[\begin{array}{ll}
\mathrm{A}_{11} & \mathrm{~A}_{21} \\
\mathrm{~A}_{12} & \mathrm{~A}_{22}
\end{array}\right]=\left[\begin{array}{cc}
4 & -3 \\
-1 & 2
\end{array}\right]
$$

Remark For a square matrix of order 2, given by

$$
\mathrm{A}=\left[\begin{array}{ll}
a_{11} & a_{12} \\
a_{21} & a_{22}
\end{array}\right]
$$

The $\operatorname{adj}$ A can also be obtained by interchanging $a_{11}$ and $a_{22}$ and by changing signs of $a_{12}$ and $a_{21}$, i.e.,

$$
\operatorname{adj} \mathrm{A}=\left[\begin{array}{cc}
a_{11} & a_{12} \\
a_{21} & a_{22}
\end{array}\right]=\left[\begin{array}{cc}
a_{22} & -a_{12} \\
-a_{21} & a_{11}
\end{array}\right]
$$
Change sign Interchange

We state the following theorem without proof.
Theorem 1 If A be any given square matrix of order $n$, then

$$
\mathrm{A}(\operatorname{adj} \mathrm{~A})=(\operatorname{adj} \mathrm{A}) \mathrm{A}=|\mathrm{A}| \mathrm{I},
$$

where I is the identity matrix of order $n$
Verification

Let

$$
\mathrm{A}=\left[\begin{array}{lll}
a_{11} & a_{12} & a_{13} \\
a_{21} & a_{22} & a_{23} \\
a_{31} & a_{32} & a_{33}
\end{array}\right] \text {, then } \text { adj } \mathrm{A}=\left[\begin{array}{lll}
\mathrm{A}_{11} & \mathrm{~A}_{21} & \mathrm{~A}_{31} \\
\mathrm{~A}_{12} & \mathrm{~A}_{22} & \mathrm{~A}_{32} \\
\mathrm{~A}_{13} & \mathrm{~A}_{23} & \mathrm{~A}_{33}
\end{array}\right]
$$

Since sum of product of elements of a row (or a column) with corresponding cofactors is equal to $|\mathrm{A}|$ and otherwise zero, we have

$$
\mathrm{A}(\operatorname{adj} \mathrm{~A})=\left[\begin{array}{ccc}
|\mathrm{A}| & 0 & 0 \\
0 & |\mathrm{~A}| & 0 \\
0 & 0 & |\mathrm{~A}|
\end{array}\right]=|\mathrm{A}|\left[\begin{array}{lll}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{array}\right]=|\mathrm{A}| \mathrm{I}
$$

Similarly, we can show $(\operatorname{adj} \mathrm{A}) \mathrm{A}=|\mathrm{A}| \mathrm{I}$
Hence $\mathrm{A}(\operatorname{adj} \mathrm{A})=(\operatorname{adj} \mathrm{A}) \mathrm{A}=|\mathrm{A}| \mathrm{I}$
Definition 4 A square matrix A is said to be singular if $|\mathrm{A}|=0$.
For example, the determinant of matrix $\mathrm{A}=\begin{array}{ll}1 & 2 \\ 4 & 8\end{array}$ is zero
Hence A is a singular matrix.
Definition 5 A square matrix A is said to be non-singular if $|\mathrm{A}| \neq 0$

Let

$$
\mathrm{A}=\left[\begin{array}{ll}
1 & 2 \\
3 & 4
\end{array}\right] . \text { Then }|\mathrm{A}|=\left|\begin{array}{ll}
1 & 2 \\
3 & 4
\end{array}\right|=4-6=-2 \neq 0 .
$$

Hence A is a nonsingular matrix
We state the following theorems without proof.
Theorem 2 If A and B are nonsingular matrices of the same order, then AB and BA are also nonsingular matrices of the same order.
Theorem 3 The determinant of the product of matrices is equal to product of their respective determinants, that is, $|\mathrm{AB}|=|\mathrm{A}||\mathrm{B}|$, where A and B are square matrices of the same order

$$
|\mathrm{A}| \quad 0 \quad 0
$$

Remark We know that $(\operatorname{adj} \mathrm{A}) \mathrm{A}=|\mathrm{A}| \mathrm{I}=0 \quad|\mathrm{~A}| \quad 0,|\mathrm{~A}| \neq 0$

$$
0 \quad 0 \quad|\mathrm{~A}|
$$

Writing determinants of matrices on both sides, we have

$$
|(\operatorname{adj} \mathrm{A}) \mathrm{A}|=\left|\begin{array}{ccc}
|\mathrm{A}| & 0 & 0 \\
0 & |\mathrm{~A}| & 0 \\
0 & 0 & |\mathrm{~A}|
\end{array}\right|
$$

i.e.

$$
|(\operatorname{adj} \mathrm{A})||\mathrm{A}|=|\mathrm{A}|^{3}\left|\begin{array}{lll}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{array}\right|
$$

i.e.

$$
|(\operatorname{adj} \mathrm{A})||\mathrm{A}|=|\mathrm{A}|^{3}
$$

i.e.

$$
|(\operatorname{adj} \mathrm{A})|=|\mathrm{A}|^{2}
$$

In general, if A is $a$ square matrix of order $n$, then $|\operatorname{adj}(\mathrm{A})|=|\mathrm{A}|^{n-1}$.
Theorem 4 A square matrix A is invertible if and only if A is nonsingular matrix.
Proof Let A be invertible matrix of order $n$ and I be the identity matrix of order $n$.
Then, there exists a square matrix B of order $n$ such that $\mathrm{AB}=\mathrm{BA}=\mathrm{I}$
Now

$$
\mathrm{AB}=\mathrm{I} . \text { So }|\mathrm{AB}|=|\mathrm{I}| \quad \text { or } \quad|\mathrm{A}| \quad|\mathrm{B}|=1 \quad(\text { since }|\mathrm{I}|=1,|\mathrm{AB}|=|\mathrm{A}||\mathrm{B}|)
$$

This gives

$$
|\mathrm{A}| \neq 0 . \text { Hence } \mathrm{A} \text { is nonsingular. }
$$

Conversely, let A be nonsingular. Then $|\mathrm{A}| \neq 0$
Now

$$
\mathrm{A}(\operatorname{adj} \mathrm{~A})=(\operatorname{adj} \mathrm{A}) \mathrm{A}=|\mathrm{A}| \mathrm{I}
$$

or

$$
\mathrm{A}\left(\frac{1}{|\mathrm{~A}|} \operatorname{adj} \mathrm{A}\right)=\left(\frac{1}{|\mathrm{~A}|} \operatorname{adj} \mathrm{A}\right) \mathrm{A}=\mathrm{I}
$$

or

$$
\mathrm{AB}=\mathrm{BA}=\mathrm{I} \text {, where } \mathrm{B}=\frac{1}{|\mathrm{~A}|} \text { adj } \mathrm{A}
$$

Thus

$$
\mathrm{A} \text { is invertible and } \mathrm{A}^{-1}=\frac{1}{|\mathrm{~A}|} \text { adj } \mathrm{A}
$$

$$
133
$$
:::

:::

:::example{number="13" kind="example" id="ex_4.13" topic="Verifying A(adj A) = |A| I"}
#### Example 13

:::prompt
If $\mathrm{A}=143$, then verify that A adj $\mathrm{A}=|\mathrm{A}| \mathrm{I}$. Also find $\mathrm{A}^{-1}$.

$$
134
$$
:::

:::solution{label="Solution"}
We have $|\mathrm{A}|=1(16-9)-3(4-3)+3(3-4)=1 \neq 0$
Now $\mathrm{A}_{11}=7, \mathrm{~A}_{12}=-1, \mathrm{~A}_{13}=-1, \mathrm{~A}_{21}=-3, \mathrm{~A}_{22}=1, \mathrm{~A}_{23}=0, \mathrm{~A}_{31}=-3, \mathrm{~A}_{32}=0$, $\mathrm{A}_{33}=1$

Therefore

$$
\operatorname{adj} \mathrm{A}=\left[\begin{array}{rrr}
7 & -3 & -3 \\
-1 & 1 & 0 \\
-1 & 0 & 1
\end{array}\right]
$$

Now

$$
\begin{aligned}
\mathrm{A}(\operatorname{adj} \mathrm{~A}) & =\left[\begin{array}{lll}
1 & 3 & 3 \\
1 & 4 & 3 \\
1 & 3 & 4
\end{array}\right]\left[\begin{array}{rrr}
7 & -3 & -3 \\
-1 & 1 & 0 \\
-1 & 0 & 1
\end{array}\right] \\
& =\left[\begin{array}{rrr}
7-3-3 & -3+3+0 & -3+0+3 \\
7-4-3 & -3+4+0 & -3+0+3 \\
7-3-4 & -3+3+0 & -3+0+4
\end{array}\right] \\
& =\left[\begin{array}{lll}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{array}\right]=(1)\left[\begin{array}{lll}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{array}\right]=|\mathrm{A}| . \mathrm{I}
\end{aligned}
$$

Also

$$
\mathrm{A}^{-1}=\frac{1}{|\mathrm{~A}|} \text { adj } \mathrm{A}=\frac{1}{1}\left[\begin{array}{rrr}
7 & -3 & -3 \\
-1 & 1 & 0 \\
-1 & 0 & 1
\end{array}\right]=\left[\begin{array}{rrr}
7 & -3 & -3 \\
-1 & 1 & 0 \\
-1 & 0 & 1
\end{array}\right]
$$
:::

:::

:::example{number="14" kind="example" id="ex_4.14" topic="Verifying (AB)^-1 = B^-1 A^-1"}
#### Example 14

:::prompt
If $\mathrm{A}=\left[\begin{array}{cc}2 & 3 \\ 1 & -4\end{array}\right]$ and $\mathrm{B}=\left[\begin{array}{cc}1 & -2 \\ -1 & 3\end{array}\right]$, then verify that $(\mathrm{AB})^{-1}=\mathrm{B}^{-1} \mathrm{~A}^{-1}$.
:::

:::solution{label="Solution"}
We have $\mathrm{AB}=\left[\begin{array}{cc}2 & 3 \\ 1 & -4\end{array}\right]\left[\begin{array}{cc}1 & -2 \\ -1 & 3\end{array}\right]=\left[\begin{array}{cc}-1 & 5 \\ 5 & -14\end{array}\right]$
Since, $|\mathrm{AB}|=-11 \neq 0,(\mathrm{AB})^{-1}$ exists and is given by

$$
(\mathrm{AB})^{-1}=\frac{1}{|\mathrm{AB}|} \operatorname{adj}(\mathrm{AB})=-\frac{1}{11}\left[\begin{array}{cc}
-14 & -5 \\
-5 & -1
\end{array}\right]=\frac{1}{11}\left[\begin{array}{cc}
14 & 5 \\
5 & 1
\end{array}\right]
$$

Further, $|\mathrm{A}|=-11 \neq 0$ and $|\mathrm{B}|=1 \neq 0$. Therefore, $\mathrm{A}^{-1}$ and $\mathrm{B}^{-1}$ both exist and are given by

$$
A^{-1}=-\frac{1}{11} \quad \begin{array}{cc}
-4 & -3 \\
-1 & 2
\end{array}, B^{-1}=\begin{array}{cc}
3 & 2 \\
1 & 1
\end{array}
$$

Therefore

$$
\mathrm{B}^{-1} \mathrm{~A}^{-1}=-\frac{1}{11} \quad \frac{3}{1} \quad 2 \quad 1 \quad-4 \quad-3 \quad=-\frac{1}{11} \quad \begin{array}{cc}
-14 & -5 \\
-5 & -1
\end{array} \quad=\frac{1}{11}\left[\begin{array}{cc}
14 & 5 \\
5 & 1
\end{array}\right]
$$

Hence $(\mathrm{AB})^{-1}=\mathrm{B}^{-1} \mathrm{~A}^{-1}$
:::

:::

:::example{number="15" kind="example" id="ex_4.15" topic="Matrix polynomial identity and inverse via it"}
#### Example 15

:::prompt
Show that the matrix $\mathrm{A}=\left[\begin{array}{ll}2 & 3 \\ 1 & 2\end{array}\right]$ satisfies the equation $\mathrm{A}^{2}-4 \mathrm{~A}+\mathrm{I}=\mathrm{O}$, where I is 2 × 2 identity matrix and O is 2 × 2 zero matrix. Using this equation, find $\mathrm{A}^{-1}$.
:::

:::solution{label="Solution"}
We have $\mathrm{A}^{2}=\mathrm{A} . \mathrm{A}=\left[\left[\begin{array}{ll}2 & 3 \\ 1 & 2\end{array}\right]\right]\left[\left[\begin{array}{ll}2 & 3 \\ 1 & 2\end{array}\right]\right]=\left[\begin{array}{cc}7 & 12 \\ 4 & 7\end{array}\right]$

Hence

$$
A^{2}-4 A+I=\left[\begin{array}{cc}
7 & 12 \\
4 & 7
\end{array}\right]-\left[\begin{array}{cc}
8 & 12 \\
4 & 8
\end{array}\right]+\left[\begin{array}{ll}
1 & 0 \\
0 & 1
\end{array}\right]=\left[\begin{array}{ll}
0 & 0 \\
0 & 0
\end{array}\right]=O
$$

Now

$$
A^{2}-4 A+I=O
$$

Therefore

$$
A A-4 A=-I
$$

or

$$
\left.\mathrm{A} \mathrm{~A}\left(\mathrm{~A}^{-1}\right)-4 \mathrm{AA}^{-1}=-\mathrm{IA}^{-1} \text { (Post multiplying by } \mathrm{A}^{-1} \text { because }|\mathrm{A}| \neq 0\right)
$$

or

$$
\mathrm{A}\left(\mathrm{~A} \mathrm{~A}^{-1}\right)-4 \mathrm{I}=-\mathrm{A}^{-1}
$$

or

$$
\mathrm{AI}-4 \mathrm{I}=-\mathrm{A}^{-1}
$$

or

$$
\mathrm{A}^{-1}=4 \mathrm{I}-\mathrm{A}=\left[\begin{array}{ll}
4 & 0 \\
0 & 4
\end{array}\right]-\left[\begin{array}{ll}
2 & 3 \\
1 & 2
\end{array}\right]=\left[\begin{array}{cc}
2 & -3 \\
-1 & 2
\end{array}\right]
$$

Hence

$$
A^{-1}=\left[\begin{array}{cc}
2 & -3 \\
-1 & 2
\end{array}\right]
$$
:::

:::

:::example{number="16" kind="example" id="ex_4.16" topic="Solving a system of equations by matrix method"}
#### Example 16

:::prompt
Solve the system of equations

$$
\begin{aligned}
& 2 x+5 y=1 \\
& 3 x+2 y=7
\end{aligned}
$$
:::

:::solution{label="Solution"}
The system of equations can be written in the form $\mathrm{AX}=\mathrm{B}$, where

$$
\mathrm{A}=\left[\begin{array}{ll}
2 & 5 \\
3 & 2
\end{array}\right], \mathrm{X}=\left[\begin{array}{l}
x \\
y
\end{array}\right] \text { and } \mathrm{B}=\left[\begin{array}{l}
1 \\
7
\end{array}\right]
$$

Now, $|\mathrm{A}|=-11 \neq 0$, Hence, A is nonsingular matrix and so has a unique solution.

Note that

$$
\mathrm{A}^{-1}=-\frac{1}{11} \begin{array}{cc}
2 & -5 \\
-3 & 2
\end{array}
$$

Therefore

$$
\mathrm{X}=\mathrm{A}^{-1} \mathrm{~B}=-\frac{1}{11} \quad \begin{array}{ccc}
2 & -5 & 1 \\
-3 & 2 & 7
\end{array}
$$

i.e.

$$
\left[\begin{array}{l}
x \\
y
\end{array}\right]=-\frac{1}{11} \quad \begin{array}{cc}
-33 \\
11
\end{array}=\begin{gathered}
3 \\
-1
\end{gathered}
$$

Hence

$$
x=3, y=-1
$$
:::

:::

:::example{number="17" kind="example" id="ex_4.17" topic="Equation of a line and finding k via matrix method"}
#### Example 17

:::prompt
Solve the following system of equations by matrix method.

$$
\begin{array}{r}
3 x-2 y+3 z=8 \\
2 x+y-z=1 \\
4 x-3 y+2 z=4
\end{array}
$$
:::

:::solution{label="Solution"}
The system of equations can be written in the form $\mathrm{AX}=\mathrm{B}$, where

$$
\mathrm{A}=\left[\begin{array}{ccc}
3 & -2 & 3 \\
2 & 1 & -1 \\
4 & -3 & 2
\end{array}\right], \mathrm{X}=\left[\begin{array}{l}
x \\
y \\
z
\end{array}\right] \text { and } \mathrm{B}=\left[\begin{array}{l}
8 \\
1 \\
4
\end{array}\right]
$$

We see that

$$
|A|=3(2-3)+2(4+4)+3(-6-4)=-17 \neq 0
$$

Hence, A is nonsingular and so its inverse exists. Now

$$
\begin{array}{lll}
\mathrm{A}_{11}=-1, & \mathrm{~A}_{12}=-8, & \mathrm{~A}_{13}=-10 \\
\mathrm{~A}_{21}=-5, & \mathrm{~A}_{22}=-6, & \mathrm{~A}_{23}=1 \\
\mathrm{~A}_{31}=-1, & \mathrm{~A}_{32}=9, & \mathrm{~A}_{33}=7
\end{array}
$$

Therefore

$$
A^{-1}=-\frac{1}{17}\left[\begin{array}{ccc}
-1 & -5 & -1 \\
-8 & -6 & 9 \\
-10 & 1 & 7
\end{array}\right]
$$

So

$$
\mathrm{X}=\mathrm{A}^{-1} \mathrm{~B}=-\frac{1}{17}\left[\begin{array}{ccc}
-1 & -5 & -1 \\
-8 & -6 & 9 \\
-10 & 1 & 7
\end{array}\right]\left[\begin{array}{l}
8 \\
1 \\
4
\end{array}\right]
$$

i.e.

$$
\left[\begin{array}{l}
x \\
y \\
z
\end{array}\right]=-\frac{1}{17}\left[\begin{array}{l}
-17 \\
-34 \\
-51
\end{array}\right]=\left[\begin{array}{l}
1 \\
2 \\
3
\end{array}\right]
$$

Hence

$$
x=1, y=2 \text { and } z=3 .
$$
:::

:::

:::example{number="18" kind="example" id="ex_4.18" topic="Solving a word problem via matrix method"}
#### Example 18

:::prompt
The sum of three numbers is 6 . If we multiply third number by 3 and add second number to it, we get 11 . By adding first and third numbers, we get double of the second number. Represent it algebraically and find the numbers using matrix method.
:::

:::solution{label="Solution"}
Let first, second and third numbers be denoted by $x, y$ and $z$, respectively. Then, according to given conditions, we have

$$
\begin{aligned}
x+y+z & =6 \\
y+3 z & =11 \\
x+z & =2 y \text { or } x-2 y+z=0
\end{aligned}
$$

This system can be written as $\mathrm{A} \mathrm{X}=\mathrm{B}$, where

$$
\mathrm{A}=\begin{array}{ccc}
1 & 1 & 1 \\
0 & 1 & 3 \\
1 & 2 & 1
\end{array}, \mathrm{X}=\begin{gathered}
x \\
y \\
z
\end{gathered} \text { and } \mathrm{B}=\begin{gathered}
6 \\
11 \\
0
\end{gathered}
$$

Here $|\mathrm{A}|=1(1+6)-(0-3)+(0-1)=9 \neq 0$. Now we find $\operatorname{adj} \mathrm{A}$

$$
\begin{array}{lll}
A_{11}=1(1+6)=7, & A_{12}=-(0-3)=3, & A_{13}=-1 \\
A_{21}=-(1+2)=-3, & A_{22}=0, & A_{23}=-(-2-1)=3 \\
A_{31}=(3-1)=2, & A_{32}=-(3-0)=-3, & A_{33}=(1-0)=1
\end{array}
$$

Hence

$$
\operatorname{adj} \mathrm{A}=\left[\begin{array}{ccc}
7 & -3 & 2 \\
3 & 0 & -3 \\
-1 & 3 & 1
\end{array}\right]
$$

Thus

$$
\mathrm{A}^{-1}=\frac{1}{|\mathrm{~A}|} \operatorname{adj}(\mathrm{A})=\frac{1}{9}\left[\begin{array}{ccc}
7 & -3 & 2 \\
3 & 0 & -3 \\
-1 & 3 & 1
\end{array}\right]
$$

Since

$$
\begin{aligned}
X & =A^{-1} B \\
X & =\frac{1}{9}\left[\begin{array}{ccc}
7 & -3 & 2 \\
3 & 0 & -3 \\
-1 & 3 & 1
\end{array}\right]\left[\begin{array}{c}
6 \\
11 \\
0
\end{array}\right]
\end{aligned}
$$

or

$$
\begin{aligned}
& x \\
& y \\
& z
\end{aligned}=\frac{1}{9}\left[\begin{array}{c}
42-33+0 \\
18+0+0 \\
-6+33+0
\end{array}\right]=\frac{1}{9} \begin{gathered}
9 \\
18 \\
27
\end{gathered}=\begin{gathered}
1 \\
2 \\
3
\end{gathered}
$$

Thus

$$
x=1, y=2, z=3
$$
:::

:::

:::example{number="19" kind="example" id="ex_4.19" topic="Solving a system using a product of matrices"}
#### Example 19

:::prompt
Use product 023923 to solve the system of equations

$$
\begin{array}{rl}
3 \quad 2 & 4 \\
x-y+2 z & =1 \\
2 y-3 z & =1 \\
3 x-2 y+4 z & =2
\end{array}
$$
:::

:::solution{label="Solution"}
Consider the product $\left[\begin{array}{ccc}1 & -1 & 2 \\ 0 & 2 & -3 \\ 3 & -2 & 4\end{array}\right]\left[\begin{array}{ccc}-2 & 0 & 1 \\ 9 & 2 & -3 \\ 6 & 1 & -2\end{array}\right]$

$$
=\left[\begin{array}{ccc}
-2-9+12 & 0-2+2 & 1+3-4 \\
0+18-18 & 0+4-3 & 0-6+6 \\
-6-18+24 & 0-4+4 & 3+6-8
\end{array}\right]=\begin{array}{ccc}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{array}
$$

$$
\begin{array}{lllll}
1 & -1 & 2^{-1} & -2 & 0
\end{array}
$$

Hence
Now, given system of equations can be written, in matrix form, as follows

$$
\left[\begin{array}{ccc}
1 & -1 & 2 \\
0 & 2 & -3 \\
3 & -2 & 4
\end{array}\right]\left[\begin{array}{l}
x \\
y \\
z
\end{array}\right]=\left[\begin{array}{l}
1 \\
1 \\
2
\end{array}\right]
$$

or

$$
\begin{aligned}
x & =\left[\begin{array}{rrr}
1 & -1 & 2 \\
0 & 2 & -3 \\
3 & -2 & 4
\end{array}\right]^{-1}\left[\begin{array}{l}
1 \\
1 \\
2
\end{array}\right]=\begin{array}{rrrr}
2 & 0 & 1 & 1 \\
9 & 2 & 3 & 1 \\
6 & 1 & 2 & 2
\end{array} \\
& =\left[\begin{array}{r}
-2+0+2 \\
9+2-6 \\
6+1-4
\end{array}\right]=\left[\begin{array}{l}
0 \\
5 \\
3
\end{array}\right]
\end{aligned}
$$

Hence

$$
x=0, y=5 \text { and } z=3
$$
:::

:::
