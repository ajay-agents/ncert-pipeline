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
Note that in the third column, two entries are zero. So we expand along the third column $\left(\mathrm{C}_{3}\right)$. We get

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
We expand along $\mathrm{R}_{1}$. We get

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
We have $\left|\begin{array}{ll}3 & x \\ x & 1\end{array}\right|=\left|\begin{array}{ll}3 & 2 \\ 4 & 1\end{array}\right|$.
That is,

$$
3-x^{2}=3-8
$$

That is,

$$
x^{2}=8
$$

So,

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
The area of the triangle is given by

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
Let $\mathrm{P}(x, y)$ be any point on AB. Then the area of triangle ABP is zero (Why?). So

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

This is the equation of the required line AB.
Also, since the area of the triangle ABD is 3 sq. units, we have

$$
\frac{1}{2}\left|\begin{array}{ccc}
1 & 3 & 1 \\
0 & 0 & 1 \\
k & 0 & 1
\end{array}\right|= \pm 3
$$

This gives $\frac{-3 k}{2}= \pm 3$, that is, $k=\mp 2$.
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

Definition 2: The cofactor of an element $a_{i j}$, denoted by $\mathrm{A}_{i j}$, is defined by

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
Remark: We expand the determinant $\Delta$ in Example 21, along $\mathrm{R}_{1}$. We get

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

Similarly, $\Delta$ can be calculated in five other ways, by expanding along $\mathrm{R}_{2}, \mathrm{R}_{3}$, $\mathrm{C}_{1}, \mathrm{C}_{2}$ and $\mathrm{C}_{3}$.

So, $\Delta=$ is the sum of the product of elements of any row (or column) with their corresponding cofactors.

- Note: If elements of a row (or column) are multiplied with cofactors of any other row (or column), then their sum is zero. For example,

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

:::example{number="12" kind="example" id="ex_4.12" topic="Finding the adjoint of a matrix" corrections_applied="1"}
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
:::

:::

:::example{number="13" kind="example" id="ex_4.13" topic="Verifying A(adj A) = |A| I" corrections_applied="2"}
#### Example 13

:::prompt
If $\mathrm{A}=\left[\begin{array}{lll}1 & 3 & 3 \\ 1 & 4 & 3 \\ 1 & 3 & 4\end{array}\right]$, then verify that A adj $\mathrm{A}=|\mathrm{A}| \mathrm{I}$. Also find $\mathrm{A}^{-1}$.
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

:::example{number="14" kind="example" id="ex_4.14" topic="Verifying (AB)^-1 = B^-1 A^-1" corrections_applied="2"}
#### Example 14

:::prompt
If $\mathrm{A}=\left[\begin{array}{cc}2 & 3 \\ 1 & -4\end{array}\right]$ and $\mathrm{B}=\left[\begin{array}{cc}1 & -2 \\ -1 & 3\end{array}\right]$, then verify that $(\mathrm{AB})^{-1}=\mathrm{B}^{-1} \mathrm{~A}^{-1}$.
:::

:::solution{label="Solution"}
We have $\mathrm{AB}=\left[\begin{array}{cc}2 & 3 \\ 1 & -4\end{array}\right]\left[\begin{array}{cc}1 & -2 \\ -1 & 3\end{array}\right]=\left[\begin{array}{cc}-1 & 5 \\ 5 & -14\end{array}\right]$
Since $|\mathrm{AB}|=-11 \neq 0,(\mathrm{AB})^{-1}$ exists, it is given by

$$
(\mathrm{AB})^{-1}=\frac{1}{|\mathrm{AB}|} \operatorname{adj}(\mathrm{AB})=-\frac{1}{11}\left[\begin{array}{cc}
-14 & -5 \\
-5 & -1
\end{array}\right]=\frac{1}{11}\left[\begin{array}{cc}
14 & 5 \\
5 & 1
\end{array}\right]
$$

Also, $|\mathrm{A}|=-11 \neq 0$ and $|\mathrm{B}|=1 \neq 0$. So $\mathrm{A}^{-1}$ and $\mathrm{B}^{-1}$ both exist. They are given by

$$
A^{-1}=-\frac{1}{11}\left[\begin{array}{cc}
-4 & -3 \\
-1 & 2
\end{array}\right], B^{-1}=\left[\begin{array}{cc}
3 & 2 \\
1 & 1
\end{array}\right]
$$

Therefore

$$
\mathrm{B}^{-1} \mathrm{~A}^{-1}=-\frac{1}{11}\left[\begin{array}{cc}
3 & 2 \\
1 & 1
\end{array}\right]\left[\begin{array}{cc}
-4 & -3 \\
-1 & 2
\end{array}\right]=-\frac{1}{11}\left[\begin{array}{cc}
-14 & -5 \\
-5 & -1
\end{array}\right]=\frac{1}{11}\left[\begin{array}{cc}
14 & 5 \\
5 & 1
\end{array}\right]
$$

Hence $(\mathrm{AB})^{-1}=\mathrm{B}^{-1} \mathrm{~A}^{-1}$
:::

:::

:::example{number="15" kind="example" id="ex_4.15" topic="Matrix polynomial identity and inverse via it" corrections_applied="1"}
#### Example 15

:::prompt
Show that the matrix $\mathrm{A}=\left[\begin{array}{ll}2 & 3 \\ 1 & 2\end{array}\right]$ satisfies the equation $\mathrm{A}^{2}-4 \mathrm{~A}+\mathrm{I}=\mathrm{O}$, where I is 2 × 2 identity matrix and O is 2 × 2 zero matrix. Using this equation, find $\mathrm{A}^{-1}$.
:::

:::solution{label="Solution"}
We have $\mathrm{A}^{2}=\mathrm{A} . \mathrm{A}=\left[\begin{array}{ll}2 & 3 \\ 1 & 2\end{array}\right]\left[\begin{array}{ll}2 & 3 \\ 1 & 2\end{array}\right]=\left[\begin{array}{cc}7 & 12 \\ 4 & 7\end{array}\right]$

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

Now, $|\mathrm{A}|=-11 \neq 0$. So A is a nonsingular matrix and has a unique solution.

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

Hence, A is nonsingular. So its inverse exists. Now

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
Let the first, second and third numbers be $x, y$ and $z$, respectively. Using the given conditions, we get

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

:::example{number="19" kind="example" id="ex_4.19" topic="Solving a system using a product of matrices" corrections_applied="3"}
#### Example 19

:::prompt
Use product $\left[\begin{array}{ccc}1 & 1 & 2 \\ 0 & 2 & 3 \\ 3 & 2 & 4\end{array}\right]\left[\begin{array}{ccc}2 & 0 & 1 \\ 9 & 2 & 3 \\ 6 & 1 & 2\end{array}\right]$ to solve the system of equations

$$
\begin{array}{rl}
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
\left[\begin{array}{ccc}
1 & -1 & 2
\end{array}\right]^{-1}=\left[\begin{array}{ccc}
-2 & 0 & 1 \\
9 & 2 & -3 \\
6 & 1 & -2
\end{array}\right]
$$

Hence
Now, the given system of equations can be written in matrix form as follows

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

## Questions and Solutions

:::question{number="1" kind="exercise" id="q_4.1" topic="Evaluating a 2x2 determinant"}
#### Question 1

:::prompt
Evaluate the determinants in Exercises 1 and 2.
$\left|\begin{array}{rr}2 & 4 \\ -5 & -1\end{array}\right|$
:::

:::solution{label="Solution"}
Evaluate the determinant $\left|\begin{array}{cc}2 & 4 \\ -5 & -1\end{array}\right|$

Solution:
Let $|A|=\left|\begin{array}{cc}2 & 4 \\ -5 & -1\end{array}\right|$
Hence,

$$
\begin{aligned}
|A| & =\left|\begin{array}{cc}
2 & 4 \\
-5 & -1
\end{array}\right| \\
& =2(-1)-4(-5) \\
& =-2+20 \\
& =18
\end{aligned}
$$
:::

:::

:::question{number="2" kind="exercise" id="q_4.2" topic="Evaluating trig 2x2 determinants"}
#### Question 2

:::prompt
Evaluate the determinants in Exercises 1 and 2.
:::

:::part{label="(i)"}
:::prompt
$\left|\begin{array}{cc}\cos \theta & -\sin \theta \\ \sin \theta & \cos \theta\end{array}\right|$
:::

:::

:::part{label="(ii)"}
:::prompt
$\left|\begin{array}{cc}x^{2}-x+1 & x-1 \\ x+1 & x+1\end{array}\right|$
:::

:::

:::solution{label="Solution"}
Evaluate the determinants:

(i) $\left|\begin{array}{cc}\cos \theta & -\sin \theta \\ \sin \theta & \cos \theta\end{array}\right|$
(ii) $\left|\begin{array}{cc}x^{2}-x+1 & x-1 \\ x+1 & x+1\end{array}\right|$

Solution:

(i) $$
\begin{aligned}
\left|\begin{array}{cc}
\cos \theta & -\sin \theta \\
\sin \theta & \cos \theta
\end{array}\right| & =(\cos \theta)(\cos \theta)-(-\sin \theta)(\sin \theta) \\
& =\cos ^{2} \theta+\sin ^{2} \theta \\
& =1
\end{aligned}
$$
(ii) $$
\begin{aligned}
\left|\begin{array}{cc}
x^{2}-x+1 & x-1 \\
x+1 & x+1
\end{array}\right| & =\left(x^{2}-x+1\right)(x+1)-(x-1)(x+1) \\
& =x^{3}-x^{2}+x+x^{2}-x+1-\left(x^{2}-1\right) \\
& =x^{3}+1-x^{2}+1 \\
& =x^{3}-x^{2}+2
\end{aligned}
$$
:::

:::

:::question{number="3" kind="exercise" id="q_4.3" topic="Verifying |3A|=27|A| for a 3x3 matrix"}
#### Question 3

:::prompt
If $\mathrm{A}=\left[\begin{array}{ll}1 & 2 \\ 4 & 2\end{array}\right]$, then show that $|2 \mathrm{~A}|=4|\mathrm{~A}|$
:::

:::solution{label="Solution"}
If $A=\left[\begin{array}{ll}1 & 2 \\ 4 & 2\end{array}\right]$, then show that $|2 A|=4|A|$
Solution:
The given matrix is $A=\left[\begin{array}{ll}1 & 2 \\ 4 & 2\end{array}\right]$
Therefore,

$$
\begin{aligned}
2 A & =2\left(\begin{array}{ll}
1 & 2 \\
4 & 2
\end{array}\right) \\
& =\left(\begin{array}{ll}
2 & 4 \\
8 & 4
\end{array}\right)
\end{aligned}
$$

Hence,

$$
\begin{aligned}
\text { LHS } & =|2 A| \\
& =\left|\begin{array}{cc}
2 & 4 \\
8 & 4
\end{array}\right| \\
& =2 \times 4-4 \times 8 \\
& =8-32 \\
& =-24
\end{aligned}
$$

Now,

$$
\begin{aligned}
|A| & =\left|\begin{array}{ll}
1 & 2 \\
4 & 2
\end{array}\right|=1 \times 2-2 \times 4 \\
& =2-8 \\
& =-6
\end{aligned}
$$

Therefore,

$$
\begin{aligned}
R H S & =4|A| \\
& =4(-6) \\
& =-24
\end{aligned}
$$

Thus, $|2 A|=4|A|$ proved.
:::

:::

:::question{number="4" kind="exercise" id="q_4.4" topic="Evaluating a 3x3 determinant"}
#### Question 4

:::prompt
If $\mathrm{A}=\left[\begin{array}{lll}1 & 0 & 1 \\ 0 & 1 & 2 \\ 0 & 0 & 4\end{array}\right]$, then show that $|3 \mathrm{~A}|=27|\mathrm{~A}|$
:::

:::solution{label="Solution"}
If $A=\left(\begin{array}{lll}1 & 0 & 1 \\ 0 & 1 & 2 \\ 0 & 0 & 4\end{array}\right)$, then show that $|3 A|=27|A|$
Solution:
The given matrix is

$$
A=\left(\begin{array}{lll}
1 & 0 & 1 \\
0 & 1 & 2 \\
0 & 0 & 4
\end{array}\right)
$$

In the first column, two entries are zero. So we expand along the first column $\left(C_{1}\right)$. This makes the calculation easier.

$$
\begin{aligned}
|A| & =1\left|\begin{array}{ll}
1 & 2 \\
0 & 4
\end{array}\right|-0\left|\begin{array}{ll}
0 & 1 \\
1 & 4
\end{array}\right|+0\left|\begin{array}{ll}
0 & 1 \\
1 & 2
\end{array}\right| \\
& =1(4-0)-0+0 \\
& =4
\end{aligned}
$$

Therefore,

$$
\begin{aligned}
27|A| & =27|4| \\
& =108
\end{aligned}
$$

Now,

$$
3 A=3\left(\begin{array}{lll}
1 & 0 & 1 \\
0 & 1 & 2 \\
0 & 0 & 4
\end{array}\right)=\left(\begin{array}{ccc}
3 & 0 & 3 \\
0 & 3 & 6 \\
0 & 0 & 12
\end{array}\right)
$$

Therefore,

$$
\begin{aligned}
|3 A| & =3\left|\begin{array}{cc}
3 & 6 \\
0 & 12
\end{array}\right|-0\left|\begin{array}{cc}
0 & 3 \\
0 & 12
\end{array}\right|+0\left|\begin{array}{ll}
0 & 3 \\
3 & 6
\end{array}\right| \\
& =3(36-0) \\
& =36(36) \\
& =108
\end{aligned}
$$

From equations (1) and (2),

$$
|3 A|=27|A|
$$

Thus, $|3 A|=27|A|$ proved.
:::

:::

:::question{number="5" kind="exercise" id="q_4.5" topic="Evaluating 3x3 determinants"}
#### Question 5

:::prompt
Evaluate the determinants
:::

:::part{label="(i)"}
:::prompt
$\left|\begin{array}{rrr}3 & -1 & -2 \\ 0 & 0 & -1 \\ 3 & -5 & 0\end{array}\right|$
:::

:::

:::part{label="(ii)"}
:::prompt
$\left|\begin{array}{rrr}3 & -4 & 5 \\ 1 & 1 & -2 \\ 2 & 3 & 1\end{array}\right|$
:::

:::

:::part{label="(iii)"}
:::prompt
$\left|\begin{array}{ccc}0 & 1 & 2 \\ -1 & 0 & -3 \\ -2 & 3 & 0\end{array}\right|$
:::

:::

:::part{label="(iv)"}
:::prompt
$\left|\begin{array}{rrr}2 & -1 & -2 \\ 0 & 2 & -1 \\ 3 & -5 & 0\end{array}\right|$
:::

:::

:::solution{label="Solution"}
Evaluate the determinants

(i) $\left|\begin{array}{ccc}3 & -1 & -2 \\ 0 & 0 & -1 \\ 3 & -5 & 0\end{array}\right|$
(ii) $\left|\begin{array}{ccc}3 & -4 & 5 \\ 1 & 1 & -2 \\ 2 & 3 & 1\end{array}\right|$
(iii) $\left|\begin{array}{ccc}0 & 1 & 2 \\ -1 & 0 & -3 \\ -2 & 3 & 0\end{array}\right|$
(iv) $\left|\begin{array}{ccc}2 & -1 & -2 \\ 0 & 2 & -1 \\ 3 & -5 & 0\end{array}\right|$

Solution:

(i) Let
$$
A=\left|\begin{array}{ccc}
3 & -1 & -2 \\
0 & 0 & -1 \\
3 & -5 & 0
\end{array}\right|
$$
In the second row, two entries are zero. So we expand along the second row. This makes the calculation easier.
Hence,
$$
\begin{aligned}
|A| & =-0\left|\begin{array}{cc}
-1 & -2 \\
-5 & 0
\end{array}\right|+0\left|\begin{array}{cc}
3 & -2 \\
3 & 0
\end{array}\right|-(-1)\left|\begin{array}{ll}
3 & -1 \\
3 & -5
\end{array}\right| \\
& =(-15+3) \\
& =-12
\end{aligned}
$$
(ii) Let $A=\left|\begin{array}{ccc}3 & -4 & 5 \\ 1 & 1 & -2 \\ 2 & 3 & 1\end{array}\right|$

Hence,

$$
\begin{aligned}
|A| & =3\left|\begin{array}{cc}
1 & -2 \\
3 & 1
\end{array}\right|+4\left|\begin{array}{cc}
1 & -2 \\
2 & 1
\end{array}\right|+5\left|\begin{array}{ll}
1 & 1 \\
2 & 3
\end{array}\right| \\
& =3(1+6)+4(1+4)+5(3-2) \\
& =3(7)+4(5)+5(1) \\
& =21+20+5 \\
& =46
\end{aligned}
$$

(iii) Let
$$
A=\left|\begin{array}{ccc}
0 & 1 & 2 \\
-1 & 0 & -3 \\
-2 & 3 & 0
\end{array}\right|
$$
Hence,
$$
\begin{aligned}
|A| & =0\left|\begin{array}{cc}
0 & -3 \\
3 & 0
\end{array}\right|-1\left|\begin{array}{cc}
-1 & -3 \\
-2 & 0
\end{array}\right|+2\left|\begin{array}{ll}
-1 & 0 \\
-2 & 3
\end{array}\right| \\
& =0-1(0-6)+2(-3-0) \\
& =-1(-6)+2(-3) \\
& =6-6=0
\end{aligned}
$$
(iv) Let
$$
A=\left|\begin{array}{ccc}
2 & -1 & -2 \\
0 & 2 & -1 \\
3 & -5 & 0
\end{array}\right|
$$
Hence,
$$
\begin{aligned}
|A| & =2\left|\begin{array}{cc}
2 & -1 \\
-5 & 0
\end{array}\right|-0\left|\begin{array}{cc}
-1 & -2 \\
-5 & 0
\end{array}\right|+3\left|\begin{array}{cc}
-1 & -2 \\
2 & -1
\end{array}\right| \\
& =2(0-5)-0+3(1+4) \\
& =-10+15=5
\end{aligned}
$$
:::

:::

:::question{number="6" kind="exercise" id="q_4.6" topic="Verifying |A|=|A transpose|"}
#### Question 6

:::prompt
If $\mathrm{A}=\left[\begin{array}{lll}1 & 1 & -2 \\ 2 & 1 & -3 \\ 5 & 4 & -9\end{array}\right]$, find $|\mathrm{A}|$
:::

:::solution{label="Solution"}
$$
A=\left(\begin{array}{rrr}
1 & 1 & -2 \\
2 & 1 & -3 \\
5 & 4 & -9
\end{array}\right) \text {, find }|A|
$$

Solution:
Let

$$
A=\left(\begin{array}{lll}
1 & 1 & -2 \\
2 & 1 & -3 \\
5 & 4 & -9
\end{array}\right)
$$

Hence,

$$
\begin{aligned}
|A| & =1\left|\begin{array}{ll}
1 & -3 \\
4 & -9
\end{array}\right|-1\left|\begin{array}{ll}
2 & -3 \\
5 & -9
\end{array}\right|-2\left|\begin{array}{ll}
2 & 1 \\
5 & 4
\end{array}\right| \\
& =1(-9+12)-1(-18+15)-2(8-5) \\
& =1(3)-1(-3)-2(3) \\
& =3+3-6 \\
& =0
\end{aligned}
$$
:::

:::

:::question{number="7" kind="exercise" id="q_4.7" topic="Solving for x from equal 2x2 determinants"}
#### Question 7

:::prompt
Find values of $x$, if
:::

:::part{label="(i)"}
:::prompt
$\left|\begin{array}{cc}2 & 4 \\ 5 & 1\end{array}\right|=\left|\begin{array}{cc}2 x & 4 \\ 6 & x\end{array}\right|$
:::

:::

:::part{label="(ii)"}
:::prompt
$\left|\begin{array}{ll}2 & 3 \\ 4 & 5\end{array}\right|=\left|\begin{array}{cc}x & 3 \\ 2 x & 5\end{array}\right|$
:::

:::

:::solution{label="Solution"}
Find the values of $x$, if

(i) $\left|\begin{array}{ll}2 & 4 \\ 5 & 1\end{array}\right|=\left|\begin{array}{cc}2 x & 4 \\ 6 & x\end{array}\right|$
(ii) $\left|\begin{array}{ll}2 & 3 \\ 4 & 5\end{array}\right|=\left|\begin{array}{cc}x & 3 \\ 2 x & 5\end{array}\right|$

Solution:

(i) $\left|\begin{array}{ll}2 & 4 \\ 5 & 1\end{array}\right|=\left|\begin{array}{cc}2 x & 4 \\ 6 & x\end{array}\right|$

Therefore,

$$
\begin{aligned}
& \Rightarrow 2 \times 1-5 \times 4=2 x \times x-6 \times 4 \\
& \Rightarrow 2-20=2 x^{2}-24 \\
& \Rightarrow 2 x^{2}=6 \\
& \Rightarrow x^{2}=3 \\
& \Rightarrow x= \pm \sqrt{3}
\end{aligned}
$$

(ii) $\left|\begin{array}{ll}2 & 3 \\ 4 & 5\end{array}\right|=\left|\begin{array}{cc}x & 3 \\ 2 x & 5\end{array}\right|$
Therefore,
$$
\begin{aligned}
& \Rightarrow 2 \times 5-3 \times 4=x \times 5-3 \times 2 x \\
& \Rightarrow 10-12=5 x-6 x \\
& \Rightarrow-2=-x \\
& \Rightarrow x=2
\end{aligned}
$$
:::

:::

:::question{number="8" kind="exercise" id="q_4.8" topic="MCQ - solving for x from equal 2x2 determinants"}
#### Question 8

:::prompt
If $\left|\begin{array}{cc}x & 2 \\ 18 & x\end{array}\right|=\left|\begin{array}{cc}6 & 2 \\ 18 & 6\end{array}\right|$, then $x$ is equal to
(A) 6
(B) ± 6
(C) -6
(D) 0
:::

:::solution{label="Solution"}
If $\left|\begin{array}{cc}x & 2 \\ 18 & x\end{array}\right|=\left|\begin{array}{cc}6 & 2 \\ 18 & 6\end{array}\right|$, the $x$ is equal to
(A) 6
(B) ±6
(C) -6
(D) 0

Solution:

$$
\left|\begin{array}{cc}
x & 2 \\
18 & x
\end{array}\right|=\left|\begin{array}{cc}
6 & 2 \\
18 & 6
\end{array}\right|
$$

Therefore,

$$
\begin{aligned}
& \Rightarrow x^{2}-36=36-36 \\
& \Rightarrow x^{2}-36=0 \\
& \Rightarrow x^{2}=36 \\
& \Rightarrow x=+6
\end{aligned}
$$

Thus, the correct option is B.
:::

:::

:::question{number="9" kind="exercise" id="q_4.9" topic="Area of a triangle from its vertices"}
#### Question 9

:::prompt
Find area of the triangle with vertices at the point given in each of the following:
:::

:::part{label="(i)"}
:::prompt
(1, 0), (6, 0), $(4,3)$
:::

:::

:::part{label="(ii)"}
:::prompt
(2, 7), (1, 1), $(10,8)$
:::

:::

:::part{label="(iii)"}
:::prompt
(-2, -3), (3, 2), (-1, -8)
:::

:::

:::solution{label="Solution"}
Find area of the triangle with vertices at the point given in each of the following:

(i) $(1,0),(6,0),(4,3)$
(ii) (2,7),(1,1),(10,8)
(iii) (-2,-3),(3,2),(-1,-8)

Solution:

(i) The area of the triangle with vertices $(1,0),(6,0),(4,3)$ is given by the relation,
$$
\begin{aligned}
\Delta & =\frac{1}{2}\left|\begin{array}{lll}
1 & 0 & 1 \\
6 & 0 & 1 \\
4 & 3 & 1
\end{array}\right| \\
& =\frac{1}{2}[1(0-3)-0(6-4)+1(18-0)] \\
& =\frac{1}{2}[-3+18] \\
& =\frac{1}{2}[15] \\
& =\frac{15}{2}
\end{aligned}
$$
Hence, area of the triangle is $\frac{15}{2}$ square units.
(ii) The area of the triangle with vertices $(2,7),(1,1),(10,8)$ is given by the relation,
$$
\begin{aligned}
\Delta & =\frac{1}{2}\left|\begin{array}{ccc}
2 & 7 & 1 \\
1 & 1 & 1 \\
10 & 8 & 1
\end{array}\right| \\
& =\frac{1}{2}[2(1-8)-7(1-10)+1(8-10)] \\
& =\frac{1}{2}[2(-7)-7(-9)+1(-2)] \\
& =\frac{1}{2}[-14+63-2] \\
& =\frac{1}{2}[47] \\
& =\frac{47}{2}
\end{aligned}
$$

Hence, area of the triangle is $\frac{47}{2}$ square units.
(iii) The area of the triangle with vertices $(-2,-3),(3,2),(-1,-8)$ is given by the relation,

$$
\begin{aligned}
\Delta & =\frac{1}{2}\left|\begin{array}{ccc}
-2 & -3 & 1 \\
3 & 2 & 1 \\
-1 & -8 & 1
\end{array}\right| \\
& =\frac{1}{2}[-2(2+8)+3(3+1)+1(-24+2)] \\
& =\frac{1}{2}[-2(10)+3(4)+1(-22)] \\
& =\frac{1}{2}[-20+12-22] \\
& =-\frac{1}{2}[30] \\
& =-15
\end{aligned}
$$

Hence, area of the triangle is 15 square units.
:::

:::

:::question{number="10" kind="exercise" id="q_4.10" topic="Showing three points are collinear"}
#### Question 10

:::prompt
Show that points
$$
\mathrm{A}(a, b+c), \mathrm{B}(b, c+a), \mathrm{C}(c, a+b) \text { are collinear. }
$$
:::

:::solution{label="Solution"}
Show that the points $A(a, b+c), B(b, c+a), C(c, a+b)$ are collinear.
Solution:
The area of the triangle with vertices $A(a, b+c), B(b, c+a), C(c, a+b)$ is given by the absolute value of the relation:

$$
\begin{aligned}
\Delta & =\frac{1}{2}\left|\begin{array}{lll}
a & b+c & 1 \\
b & c+a & 1 \\
c & a+b & 1
\end{array}\right| & \\
& =\frac{1}{2}\left|\begin{array}{ccc}
a & b+c & 1 \\
b-a & a-b & 0 \\
c-a & a-c & 0
\end{array}\right| & {\left[R_{2} \rightarrow R_{2}-R_{1} \text { and } R_{3} \rightarrow R_{3}-R_{1}\right] } \\
& =\frac{1}{2}(a-b)(c-a)\left|\begin{array}{ccc}
a & b+c & 1 \\
-1 & 1 & 0 \\
1 & -1 & 0
\end{array}\right| & \\
& =\frac{1}{2}(a-b)(c-a)\left|\begin{array}{ccc}
a & b+c & 1 \\
-1 & 1 & 0 \\
0 & 0 & 0
\end{array}\right| & {\left[R_{3} \rightarrow R_{3}+R_{2}\right] }
\end{aligned}
$$

Thus, the area of the triangle formed by points is zero.
Hence, the points are collinear.
:::

:::

:::question{number="11" kind="exercise" id="q_4.11" topic="Finding k from a given triangle area"}
#### Question 11

:::prompt
Find values of $k$ if area of triangle is 4 sq. units and vertices are
:::

:::part{label="(i)"}
:::prompt
( $k, 0),(4,0),(0,2)$
:::

:::

:::part{label="(ii)"}
:::prompt
(-2, 0), (0, 4), (0, k)
:::

:::

:::solution{label="Solution"}
Find values of $k$ if area of triangle is 4 square units and vertices are:

(i) $(k, 0),(4,0),(0,2)$
(ii) $(-2,0),(0,4),(0, k)$

Solution:
We know that the area of a triangle with vertices $\left(x_{1}, y_{1}\right),\left(x_{2}, y_{2}\right)$ and $\left(x_{3}, y_{3}\right)$ is the absolute value of the determinant $(\Delta)$. Here,

$$
\Delta=\frac{1}{2}\left|\begin{array}{lll}
x_{1} & y_{1} & 1 \\
x_{2} & y_{2} & 1 \\
x_{3} & y_{3} & 1
\end{array}\right|
$$

It is given that the area of triangle is 4 square units.
Hence, $\Delta= \pm 4$

(i) The area of the triangle with vertices $(k, 0),(4,0),(0,2)$ is given by the relation,

$$
\begin{aligned}
\Delta & =\frac{1}{2}\left|\begin{array}{ccc}
k & 0 & 1 \\
4 & 0 & 1 \\
0 & 2 & 1
\end{array}\right| \\
& =\frac{1}{2}[k(0-2)-0(4-0)+1(8-0)] \\
& =\frac{1}{2}[-2 k+8] \\
& =-k+4
\end{aligned}
$$

Therefore, $-k+4= \pm 4$

When $-k+4=-4$
Then $k=8$

When $-k+4=4$
Then $k=0$

Hence, $k=0,8$
(ii) The area of the triangle with vertices $(-2,0),(0,4),(0, k)$ is given by the relation,

$$
\begin{aligned}
\Delta & =\frac{1}{2}\left|\begin{array}{ccc}
-2 & 0 & 1 \\
0 & 4 & 1 \\
0 & k & 1
\end{array}\right| \\
& =\frac{1}{2}[-2(4-k)] \\
& =k-4
\end{aligned}
$$

Therefore, $-k+4= \pm 4$
When $k-4=4$
Then $k=8$

When $k-4=-4$
Then $k=0$

Hence, $k=0,8$
:::

:::

:::question{number="12" kind="exercise" id="q_4.12" topic="Equation of a line via determinants"}
#### Question 12

:::part{label="(i)"}
:::prompt
Find equation of line joining $(1,2)$ and $(3,6)$ using determinants.
:::

:::

:::part{label="(ii)"}
:::prompt
Find equation of line joining $(3,1)$ and $(9,3)$ using determinants.
:::

:::

:::solution{label="Solution"}
(i) Find equation of line joining $(1,2)$ and $(3,6)$ using determinants.
(ii) Find equation of line joining $(3,1)$ and $(9,3)$ using determinants.

Solution:

(i) Let $P(x, y)$ be any point on the line joining points $A(1,2)$ and $B(3,6)$.
Then, the points $A, B$ and $P$ are collinear.
Hence, the area of triangle $A B P$ will be zero.
Therefore,
$$
\begin{aligned}
& \Rightarrow \frac{1}{2}\left|\begin{array}{lll}
1 & 2 & 1 \\
3 & 6 & 1 \\
x & y & 1
\end{array}\right|=0 \\
& \Rightarrow \frac{1}{2}[1(6-y)-2(3-x)+1(3 y-6 x)]=0 \\
& \Rightarrow 6-y-6+2 x+3 y-6 x=0 \\
& \Rightarrow 2 y-4 x=0 \\
& \Rightarrow y=2 x
\end{aligned}
$$
Thus, the equation of the line joining the given points is $y=2 x$.
(ii) Let $P(x, y)$ be any point on the line joining points $A(3,1)$ and $B(9,3)$.
Then, the points $A, B$ and $P$ are collinear.
Hence, the area of triangle $A B P$ will be zero.
Therefore,
$$
\begin{aligned}
& \Rightarrow \frac{1}{2}\left|\begin{array}{lll}
3 & 1 & 1 \\
9 & 3 & 1 \\
x & y & 1
\end{array}\right|=0 \\
& \Rightarrow \frac{1}{2}[3(3-y)-1(9-x)+1(9 y-3 x)]=0 \\
& \Rightarrow 9-3 y-9+x+9 y-3 x=0 \\
& \Rightarrow 6 y-2 x=0 \\
& \Rightarrow x-3 y=0
\end{aligned}
$$
Thus, the equation of the line joining the given points is $x-3 y=0$.
:::

:::

:::question{number="13" kind="exercise" id="q_4.13" topic="MCQ - finding k from a given triangle area"}
#### Question 13

:::prompt
If area of triangle is 35 sq units with vertices $(2,-6),(5,4)$ and $(k, 4)$. Then $k$ is
(A) 12
(B) -2
(C) -12, -2
(D) 12,-2
:::

:::solution{label="Solution"}
If area of the triangle is 35 square units with vertices $(2,-6),(5,4),(k, 4)$. Then $k$ is
(A) 12
(B) -2
(C) -12,-2
(D) 12,-2

Solution:
The area of the triangle with vertices $(2,-6),(5,4),(k, 4)$ is given by the relation,

$$
\begin{aligned}
\Delta & =\frac{1}{2}\left|\begin{array}{ccc}
2 & -6 & 1 \\
5 & 4 & 1 \\
k & 4 & 1
\end{array}\right| \\
& =\frac{1}{2}[2(4-4)+6(5-k)+1(20-4 k)] \\
& =\frac{1}{2}[30-6 k+20-4 k] \\
& =\frac{1}{2}[50-10 k] \\
& =25-5 k
\end{aligned}
$$

It is given that the area of the triangle is 35 square units. Hence, $\Delta= \pm 35$.

Therefore,

$$
\begin{aligned}
& \Rightarrow 25-5 k= \pm 35 \\
& \Rightarrow 5(5-k)= \pm 35 \\
& \Rightarrow 5-k= \pm 7
\end{aligned}
$$

When, $5-k=-7$
Then, $k=12$
When, $5-k=7$
Then, $k=-2$
Hence, $k=12,-2$
Thus, the correct option is D.
:::

:::

:::question{number="14" kind="exercise" id="q_4.14" topic="Minors and cofactors of a 2x2 determinant"}
#### Question 14

:::prompt
Write Minors and Cofactors of the elements of following determinants:
:::

:::part{label="(i)"}
:::prompt
$\left|\begin{array}{rr}2 & -4 \\ 0 & 3\end{array}\right|$
:::

:::

:::part{label="(ii)"}
:::prompt
$\left|\begin{array}{cc}a & c \\ b & d\end{array}\right|$
:::

:::

:::solution{label="Solution"}
Write Minors and Cofactors of the elements of following determinants:

(i) $\left|\begin{array}{cc}2 & -4 \\ 0 & 3\end{array}\right|$
(ii) $\left|\begin{array}{ll}a & c \\ b & d\end{array}\right|$

Solution:

(i) The given determinant is $\left|\begin{array}{cc}2 & -4 \\ 0 & 3\end{array}\right|$
Minor of element $a_{i j}$ is $M_{i j}$.
$M_{11}=$ minor of element $a_{11}=3$
$M_{12}=$ minor of element $a_{12}=0$
$M_{21}=$ minor of element $a_{21}=-4$
$M_{22}=$ minor of element $a_{22}=2$
Cofactor of $a_{i j}$ is $A_{i j}=(-1)^{i+j} M_{i j}$
$$
\begin{aligned}
& A_{11}=(-1)^{1+1} M_{11}=(-1)^{2}(3)=3 \\
& A_{12}=(-1)^{1+2} M_{12}=(-1)^{3}(0)=0 \\
& A_{21}=(-1)^{2+1} M_{21}=(-1)^{3}(-4)=4 \\
& A_{22}=(-1)^{2+2} M_{22}=(-1)^{4}(2)=2
\end{aligned}
$$
(ii) The given determinant is $\left|\begin{array}{ll}a & c \\ b & d\end{array}\right|$
Minor of element $a_{i j}$ is $M_{i j}$.
$M_{11}=$ minor of element $a_{11}=d$
$M_{12}=$ minor of element $a_{12}=b$
$M_{21}=$ minor of element $a_{21}=c$
$M_{22}=$ minor of element $a_{22}=a$
Cofactor of $a_{i j}$ is $A_{i j}=(-1)^{i+j} M_{i j}$

$$
\begin{aligned}
& A_{11}=(-1)^{1+1} M_{11}=(-1)^{2}(d)=d \\
& A_{12}=(-1)^{1+2} M_{12}=(-1)^{3}(b)=-b \\
& A_{21}=(-1)^{2+1} M_{21}=(-1)^{3}(c)=-c \\
& A_{22}=(-1)^{2+2} M_{22}=(-1)^{4}(a)=a
\end{aligned}
$$
:::

:::

:::question{number="15" kind="exercise" id="q_4.15" topic="Minors and cofactors of a 3x3 determinant"}
#### Question 15

:::prompt
Write Minors and Cofactors of the elements of following determinants:
:::

:::part{label="(i)"}
:::prompt
$\left|\begin{array}{lll}1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1\end{array}\right|$
:::

:::

:::part{label="(ii)"}
:::prompt
$\left|\begin{array}{rrr}1 & 0 & 4 \\ 3 & 5 & -1 \\ 0 & 1 & 2\end{array}\right|$
:::

:::

:::solution{label="Solution"}
Write Minors and Cofactors of the elements of following determinants:

(i) $\left|\begin{array}{lll}1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1\end{array}\right|$
(ii) $\left|\begin{array}{ccc}1 & 0 & 4 \\ 3 & 5 & -1 \\ 0 & 1 & 2\end{array}\right|$

Solution:

(i) The given determinant is $\left|\begin{array}{lll}1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1\end{array}\right|$
Minor of element $a_{i j}$ is $M_{i j}$.
$$
\begin{aligned}
& M_{11}=\text { minor of element } a_{11}=\left|\begin{array}{ll}
1 & 0 \\
0 & 1
\end{array}\right|=1 \\
& M_{12}=\text { minor of element } a_{12}=\left|\begin{array}{ll}
0 & 0 \\
0 & 1
\end{array}\right|=0 \\
& M_{13}=\text { minor of element } a_{13}=\left|\begin{array}{ll}
0 & 1 \\
0 & 0
\end{array}\right|=0 \\
& M_{21}=\text { minor of element } a_{21}=\left|\begin{array}{ll}
0 & 0 \\
0 & 1
\end{array}\right|=0 \\
& M_{22}=\text { minor of element } a_{22}=\left|\begin{array}{ll}
1 & 0 \\
0 & 1
\end{array}\right|=1 \\
& M_{23}=\text { minor of element } a_{23}=\left|\begin{array}{ll}
1 & 0 \\
0 & 0
\end{array}\right|=0
\end{aligned}
$$

$$
\begin{aligned}
& M_{31}=\text { minor of element } a_{31}=\left|\begin{array}{ll}
0 & 0 \\
1 & 0
\end{array}\right|=0 \\
& M_{32}=\text { minor of element } a_{32}=\left|\begin{array}{ll}
1 & 0 \\
0 & 0
\end{array}\right|=0 \\
& M_{33}=\text { minor of element } \quad a_{33}=\left|\begin{array}{ll}
1 & 0 \\
0 & 1
\end{array}\right|=1
\end{aligned}
$$

Cofactor of $a_{i j}$ is $A_{i j}=(-1)^{i+j} M_{i j}$

$$
\begin{aligned}
& A_{11}=(-1)^{1+1} M_{11}=(-1)^{2}(1)=1 \\
& A_{12}=(-1)^{1+2} M_{12}=(-1)^{3}(0)=0 \\
& A_{13}=(-1)^{1+3} M_{13}=(-1)^{4}(0)=0 \\
& A_{21}=(-1)^{2+1} M_{21}=(-1)^{3}(0)=0 \\
& A_{22}=(-1)^{2+2} M_{22}=(-1)^{4}(1)=1 \\
& A_{23}=(-1)^{2+3} M_{23}=(-1)^{5}(0)=0 \\
& A_{31}=(-1)^{3+1} M_{31}=(-1)^{4}(0)=0 \\
& A_{32}=(-1)^{3+2} M_{32}=(-1)^{5}(0)=0 \\
& A_{33}=(-1)^{3+3} M_{33}=(-1)^{6}(1)=1
\end{aligned}
$$

(ii) The given determinant is $\left|\begin{array}{ccc}1 & 0 & 4 \\ 3 & 5 & -1 \\ 0 & 1 & 2\end{array}\right|$
Minor of element $a_{i j}$ is $M_{i j}$.
$$
\begin{aligned}
& M_{11}=\text { minor of element } a_{11}=\left|\begin{array}{cc}
5 & -1 \\
1 & 2
\end{array}\right|=11 \\
& M_{12}=\text { minor of element } a_{12}=\left|\begin{array}{cc}
3 & -1 \\
0 & 2
\end{array}\right|=6 \\
& M_{13}=\text { minor of element } a_{13}=\left|\begin{array}{ll}
3 & 5 \\
0 & 1
\end{array}\right|=3 \\
& M_{21}=\text { minor of element } a_{21}=\left|\begin{array}{ll}
0 & 4 \\
1 & 2
\end{array}\right|=-4 \\
& M_{22}=\text { minor of element } a_{22}=\left|\begin{array}{ll}
1 & 4 \\
0 & 2
\end{array}\right|=2
\end{aligned}
$$

$$
\begin{aligned}
& M_{23}=\text { minor of element } a_{23}=\left|\begin{array}{ll}
1 & 0 \\
0 & 1
\end{array}\right|=1 \\
& M_{31}=\text { minor of element } a_{31}=\left|\begin{array}{cc}
0 & 4 \\
5 & -1
\end{array}\right|=-20 \\
& M_{32}=\text { minor of element } a_{32}=\left|\begin{array}{cc}
1 & 4 \\
3 & -1
\end{array}\right|=-13 \\
& M_{33}=\text { minor of element } a_{33}=\left|\begin{array}{ll}
1 & 0 \\
3 & 5
\end{array}\right|=5
\end{aligned}
$$

Cofactor of $a_{i j}$ is $A_{i j}=(-1)^{i+j} M_{i j}$

$$
\begin{aligned}
& A_{11}=(-1)^{1+1} M_{11}=(-1)^{2}(11)=11 \\
& A_{12}=(-1)^{1+2} M_{12}=(-1)^{3}(6)=-6 \\
& A_{13}=(-1)^{1+3} M_{13}=(-1)^{4}(3)=3 \\
& A_{21}=(-1)^{2+1} M_{21}=(-1)^{3}(-4)=4 \\
& A_{22}=(-1)^{2+2} M_{22}=(-1)^{4}(2)=2 \\
& A_{23}=(-1)^{2+3} M_{23}=(-1)^{5}(1)=-1 \\
& A_{31}=(-1)^{3+1} M_{31}=(-1)^{4}(-20)=-20 \\
& A_{32}=(-1)^{3+2} M_{32}=(-1)^{5}(-13)=13 \\
& A_{33}=(-1)^{3+3} M_{33}=(-1)^{6}(5)=5
\end{aligned}
$$
:::

:::

:::question{number="16" kind="exercise" id="q_4.16" topic="Evaluating a determinant via row cofactors"}
#### Question 16

:::prompt
Using Cofactors of elements of second row, evaluate $\Delta=\left|\begin{array}{lll}5 & 3 & 8 \\ 2 & 0 & 1 \\ 1 & 2 & 3\end{array}\right|$.
:::

:::solution{label="Solution"}
Using Cofactors of elements of second row, evaluate $\Delta=\left|\begin{array}{lll}5 & 3 & 8 \\ 2 & 0 & 1 \\ 1 & 2 & 3\end{array}\right|$
Solution:
The given determinant is $\left|\begin{array}{lll}5 & 3 & 8 \\ 2 & 0 & 1 \\ 1 & 2 & 3\end{array}\right|$

$$
\begin{aligned}
& M_{21}=\text { minor of element } a_{21}=\left|\begin{array}{ll}
3 & 8 \\
2 & 3
\end{array}\right|=-7 \\
& A_{21}=(-1)^{2+1} M_{21}=(-1)^{3}(-7)=7
\end{aligned}
$$

$$
\begin{aligned}
& M_{22}=\text { minor of element } a_{22}=\left|\begin{array}{ll}
5 & 8 \\
1 & 3
\end{array}\right|=15-8=7 \\
& A_{22}=(-1)^{2+2} M_{22}=(-1)^{4}(7)=7
\end{aligned}
$$

$$
\begin{aligned}
& M_{23}=\text { minor of element } a_{23}=\left|\begin{array}{ll}
5 & 3 \\
1 & 2
\end{array}\right|=7 \\
& A_{23}=(-1)^{2+3} M_{21}=(-1)^{5}(7)=-7
\end{aligned}
$$

We know that $\Delta$ equals the sum of the products of the second row's elements and their corresponding cofactors.

Therefore,

$$
\begin{aligned}
\Delta & =a_{21} A_{21}+a_{22} A_{22}+a_{23} A_{23} \\
& =2(7)+0(7)+1(-7) \\
& =14-7 \\
& =7
\end{aligned}
$$
:::

:::

:::question{number="17" kind="exercise" id="q_4.17" topic="Evaluating a determinant via column cofactors"}
#### Question 17

:::prompt
Using Cofactors of elements of third column, evaluate $\Delta=\left|\begin{array}{lll}1 & x & y z \\ 1 & y & z x \\ 1 & z & x y\end{array}\right|$.
:::

:::solution{label="Solution"}
Using Cofactors of elements of third column, evaluate

$$
\Delta=\left|\begin{array}{ccc}
1 & x & y z \\
1 & y & z x \\
1 & z & x y
\end{array}\right|
$$

Solution:
The given determinant is $\left|\begin{array}{ccc}1 & x & y z \\ 1 & y & z x \\ 1 & z & x y\end{array}\right|$
Therefore,

$$
\begin{aligned}
& M_{13}=\left|\begin{array}{ll}
1 & y \\
1 & z
\end{array}\right|=z-y \\
& M_{23}=\left|\begin{array}{ll}
1 & x \\
1 & z
\end{array}\right|=z-x \\
& M_{33}=\left|\begin{array}{ll}
1 & x \\
1 & y
\end{array}\right|=y-x
\end{aligned}
$$

$$
\begin{aligned}
& A_{13}=(-1)^{1+3} M_{13}=(-1)^{4}(z-y)=z-y \\
& A_{23}=(-1)^{2+3} M_{23}=(-1)^{5}(z-x)=-(z-x)=x-z \\
& A_{33}=(-1)^{3+3} M_{33}=(-1)^{6}(y-x)=y-x
\end{aligned}
$$

We know that $\Delta$ equals the sum of the products of the third column's elements and their corresponding cofactors.

Therefore,

$$
\begin{aligned}
\Delta & =a_{13} A_{13}+a_{23} A_{23}+a_{33} A_{33} \\
& =y z(z-y)+z x(x-z)+x y(y-x) \\
& =y z^{2}-y^{2} z+x^{2} z-x z^{2}+x y^{2}-x^{2} y \\
& =\left(x^{2} z-y^{2} z\right)+\left(y z^{2}-x z^{2}\right)+\left(x y^{2}-x^{2} y\right) \\
& =z\left(x^{2}-y^{2}\right)+z^{2}(y-x)+x y(y-x) \\
& =z(x-y)(x+y)+z^{2}(y-x)+x y(y-x) \\
& =(x-y)\left[z x+z y-z^{2}-x y\right] \\
& =(x-y)[z(x-z)+y(z-x)] \\
& =(x-y)(z-x)[-z+y] \\
& =(x-y)(y-z)(z-x)
\end{aligned}
$$

Hence,

$$
\Delta=(x-y)(y-z)(z-x)
$$
:::

:::

:::question{number="18" kind="exercise" id="q_4.18" topic="Proving a determinant equals its cofactor-matrix determinant squared"}
#### Question 18

:::prompt
If $\Delta=\left|\begin{array}{lll}a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \\ a_{31} & a_{32} & a_{33}\end{array}\right|$ and $A_{i j}$ is Cofactors of $a_{i j}$, then value of $\Delta$ is given by
(A) $a_{11} \mathrm{~A}_{31}+a_{12} \mathrm{~A}_{32}+a_{13} \mathrm{~A}_{33}$
(B) $a_{11} \mathrm{~A}_{11}+a_{12} \mathrm{~A}_{21}+a_{13} \mathrm{~A}_{31}$
(C) $a_{21} \mathrm{~A}_{11}+a_{22} \mathrm{~A}_{12}+a_{23} \mathrm{~A}_{13}$
(D) $a_{11} \mathrm{~A}_{11}+a_{21} \mathrm{~A}_{21}+a_{31} \mathrm{~A}_{31}$
4.5 Adjoint and Inverse of a Matrix

In the previous chapter, we have studied inverse of a matrix. In this section, we shall discuss the condition for existence of inverse of a matrix.

To find inverse of a matrix A, i.e., $\mathrm{A}^{-1}$ we shall first define adjoint of a matrix.
4.5.1 Adjoint of a matrix

Definition 3 The adjoint of a square matrix $\mathrm{A}=\left[a_{i j}\right]_{n \times n}$ is defined as the transpose of the matrix $\left[\mathrm{A}_{i j}\right]_{n \times n}$, where $\mathrm{A}_{i j}$ is the cofactor of the element $a_{i j}$. Adjoint of the matrix A is denoted by adj A.

Let

$$
\mathrm{A}=\left[\begin{array}{lll}
a_{11} & a_{12} & a_{13} \\
a_{21} & a_{22} & a_{23} \\
a_{31} & a_{32} & a_{33}
\end{array}\right]
$$

Then

$$
\operatorname{adj} \mathrm{A}=\text { Transpose of }\left[\begin{array}{lll}
\mathrm{A}_{11} & \mathrm{~A}_{12} & \mathrm{~A}_{13} \\
\mathrm{~A}_{21} & \mathrm{~A}_{22} & \mathrm{~A}_{23} \\
\mathrm{~A}_{31} & \mathrm{~A}_{32} & \mathrm{~A}_{33}
\end{array}\right]=\left[\begin{array}{lll}
\mathrm{A}_{11} & \mathrm{~A}_{21} & \mathrm{~A}_{31} \\
\mathrm{~A}_{12} & \mathrm{~A}_{22} & \mathrm{~A}_{32} \\
\mathrm{~A}_{13} & \mathrm{~A}_{23} & \mathrm{~A}_{33}
\end{array}\right]
$$
:::

:::solution{label="Solution"}
If $\Delta=\left|\begin{array}{lll}a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \\ a_{31} & a_{32} & a_{33}\end{array}\right|$ and $A_{i j}$ is the cofactor of $a_{i j}$, then the value of $\Delta$ is given by:

A. $a_{11} A_{31}+a_{12} A_{32}+a_{13} A_{33}$
B. $a_{11} A_{11}+a_{12} A_{21}+a_{13} A_{31}$
C. $a_{21} A_{11}+a_{22} A_{12}+a_{23} A_{13}$
D. $a_{11} A_{11}+a_{21} A_{21}+a_{31} A_{31}$

Solution:
We know that $\Delta$ equals the sum of the products of the elements of a column or row and their corresponding cofactors.

$$
\Delta=a_{11} A_{11}+a_{21} A_{21}+a_{31} A_{31}
$$

Thus, the correct option is D.
:::

:::

:::question{number="19" kind="exercise" id="q_4.19" topic="Finding the adjoint of a 2x2 matrix"}
#### Question 19

:::prompt
Find adjoint of each of the matrices in Exercises 1 and 2.
$$\left[\begin{array}{cc}1 & 2 \\ 3 & 4\end{array}\right]$$
:::

:::solution{label="Solution"}
Find the adjoint of the matrix $\left(\begin{array}{ll}1 & 2 \\ 3 & 4\end{array}\right)$
Solution:

Let

$$
A=\left(\begin{array}{ll}
1 & 2 \\
3 & 4
\end{array}\right)
$$

Then,

$$
\begin{array}{ll}
A_{11}=4 & A_{12}=-3 \\
A_{21}=-2 & A_{22}=1
\end{array}
$$

Therefore,

$$
\begin{aligned}
\operatorname{adj} A & =\left(\begin{array}{ll}
A_{11} & A_{12} \\
A_{21} & A_{22}
\end{array}\right) \\
& =\left(\begin{array}{cc}
4 & -2 \\
-3 & 1
\end{array}\right)
\end{aligned}
$$
:::

:::

:::question{number="20" kind="exercise" id="q_4.20" topic="Finding the adjoint of a 3x3 matrix"}
#### Question 20

:::prompt
Find adjoint of each of the matrices in Exercises 1 and 2.
$$\left[\begin{array}{ccc}1 & -1 & 2 \\ 2 & 3 & 5 \\ -2 & 0 & 1\end{array}\right]$$
:::

:::solution{label="Solution"}
Find the adjoint of the matrix $\left(\begin{array}{ccc}1 & -1 & 2 \\ 2 & 3 & 5 \\ -2 & 0 & 1\end{array}\right)$
Solution:

Let

$$
A=\left(\begin{array}{ccc}
1 & -1 & 2 \\
2 & 3 & 5 \\
-2 & 0 & 1
\end{array}\right)
$$

Then,

$$
\begin{array}{lll}
A_{11}=\left|\begin{array}{ll}
3 & 5 \\
0 & 1
\end{array}\right|=3 & A_{12}=-\left|\begin{array}{cc}
2 & 5 \\
-2 & 1
\end{array}\right|=-12 & A_{13}=\left|\begin{array}{cc}
2 & 3 \\
-2 & 0
\end{array}\right|=6 \\
A_{21}=-\left|\begin{array}{cc}
-1 & 2 \\
0 & 1
\end{array}\right|=1 & A_{22}=\left|\begin{array}{cc}
1 & 2 \\
-2 & 1
\end{array}\right|=5 & A_{23}=-\left|\begin{array}{cc}
1 & -1 \\
-2 & 0
\end{array}\right|=2 \\
A_{31}=\left|\begin{array}{cc}
-1 & 2 \\
3 & 5
\end{array}\right|=-11 & A_{32}=-\left|\begin{array}{ll}
1 & 2 \\
2 & 5
\end{array}\right|=-1 & A_{33}=\left|\begin{array}{cc}
1 & -1 \\
2 & 3
\end{array}\right|=5
\end{array}
$$

Therefore,

$$
\operatorname{adj} A=\left(\begin{array}{ccc}
3 & 1 & -11 \\
-12 & 5 & -1 \\
6 & 2 & 5
\end{array}\right)
$$
:::

:::

:::question{number="21" kind="exercise" id="q_4.21" topic="Verifying A(adj A) = (adj A)A = |A|I (2x2)"}
#### Question 21

:::prompt
Verify A (adj A) = (adj A) A = |A| I in Exercises 3 and 4
$$\left[\begin{array}{cc}2 & 3 \\ -4 & -6\end{array}\right]$$
:::

:::solution{label="Solution"}
Verify $A(\operatorname{adj} A)=(\operatorname{adj} A) A=|A| I$ for

$$
\left(\begin{array}{cc}
2 & 3 \\
-4 & -6
\end{array}\right)
$$

Solution:

Let

$$
A=\left(\begin{array}{cc}
2 & 3 \\
-4 & -6
\end{array}\right)
$$

Then,

$$
\begin{aligned}
|A| & =-12-(-12) \\
& =0
\end{aligned}
$$

Also,

$$
\begin{aligned}
|A| I & =0\left(\begin{array}{ll}
1 & 0 \\
0 & 1
\end{array}\right) \\
& =\left(\begin{array}{ll}
0 & 0 \\
0 & 0
\end{array}\right)
\end{aligned}
$$

Now,

$$
\begin{array}{ll}
A_{11}=-6 & A_{12}=4 \\
A_{21}=-3 & A_{22}=2
\end{array}
$$

Hence,

$$
\operatorname{adj} A=\left(\begin{array}{cc}
-6 & -3 \\
4 & 2
\end{array}\right)
$$

Now,

$$
\begin{aligned}
A(\operatorname{adj} A) & =\left(\begin{array}{cc}
2 & 3 \\
-4 & -6
\end{array}\right)\left(\begin{array}{cc}
-6 & -3 \\
4 & 2
\end{array}\right) \\
& =\left(\begin{array}{cc}
-12+12 & -6+6 \\
24-24 & 12-12
\end{array}\right) \\
& =\left(\begin{array}{ll}
0 & 0 \\
0 & 0
\end{array}\right)
\end{aligned}
$$

Also,

$$
\begin{aligned}
(\operatorname{adj} A) A & =\left(\begin{array}{cc}
-6 & -3 \\
4 & 2
\end{array}\right)\left(\begin{array}{cc}
2 & 3 \\
-4 & -6
\end{array}\right) \\
& =\left(\begin{array}{cc}
-12+12 & -18+18 \\
8-8 & 12-12
\end{array}\right) \\
& =\left(\begin{array}{ll}
0 & 0 \\
0 & 0
\end{array}\right)
\end{aligned}
$$

Hence, $A(\operatorname{adj} A)=(\operatorname{adj} A) A=|A| I$.
:::

:::

:::question{number="22" kind="exercise" id="q_4.22" topic="Verifying A(adj A) = (adj A)A = |A|I (3x3)"}
#### Question 22

:::prompt
Verify A (adj A) = (adj A) A = |A| I in Exercises 3 and 4
$$\left[\begin{array}{ccc}1 & -1 & 2 \\ 3 & 0 & -2 \\ 1 & 0 & 3\end{array}\right]$$
:::

:::solution{label="Solution"}
Verify $A(\operatorname{adj} A)=(\operatorname{adj} A) A=|A| I$ for

$$
\left(\begin{array}{ccc}
1 & -1 & 2 \\
3 & 0 & -2 \\
1 & 0 & 3
\end{array}\right)
$$

Solution:

$$
A=\left(\begin{array}{ccc}
1 & -1 & 2 \\
3 & 0 & -2 \\
1 & 0 & 3
\end{array}\right)
$$

Then,

$$
\begin{aligned}
|A| & =1(0-0)+1(9+2)+2(0-0) \\
& =11
\end{aligned}
$$

Also,

$$
\begin{aligned}
|A| I & =11\left(\begin{array}{lll}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{array}\right) \\
& =\left(\begin{array}{ccc}
11 & 0 & 0 \\
0 & 11 & 0 \\
0 & 0 & 11
\end{array}\right)
\end{aligned}
$$

Now,

$$
\begin{array}{lll}
A_{11}=0 & A_{12}=-11 & A_{13}=0 \\
A_{21}=3 & A_{22}=1 & A_{23}=-1 \\
A_{31}=2 & A_{32}=8 & A_{33}=3
\end{array}
$$

Hence,

$$
\operatorname{adj} A=\left(\begin{array}{ccc}
0 & 3 & 2 \\
-11 & 1 & 8 \\
0 & -1 & 3
\end{array}\right)
$$

Now,

$$
\begin{aligned}
A(\operatorname{adj} A) & =\left(\begin{array}{ccc}
1 & -1 & 2 \\
3 & 0 & -2 \\
1 & 0 & 3
\end{array}\right)\left(\begin{array}{ccc}
0 & 3 & 2 \\
-11 & 1 & 8 \\
0 & -1 & 3
\end{array}\right) \\
& =\left(\begin{array}{ccc}
0+11+0 & 3-1-2 & 2-8+6 \\
0+0+0 & 9+0+2 & 6+0-6 \\
0+0+0 & 3+0-3 & 2+0+9
\end{array}\right)=\left(\begin{array}{ccc}
11 & 0 & 0 \\
0 & 11 & 0 \\
0 & 0 & 11
\end{array}\right)
\end{aligned}
$$

Also,

$$
\begin{aligned}
(\operatorname{adj} A) A & =\left(\begin{array}{ccc}
0 & 3 & 2 \\
-11 & 1 & 8 \\
0 & -1 & 3
\end{array}\right)\left(\begin{array}{ccc}
1 & -1 & 2 \\
3 & 0 & -2 \\
1 & 0 & 3
\end{array}\right) \\
& =\left(\begin{array}{ccc}
0+9+2 & 0+0+0 & 0-6+6 \\
-11+3+8 & 11+0+0 & -22-2+24 \\
0-3+3 & 0+0+0 & 2+0+9
\end{array}\right) \\
& =\left(\begin{array}{ccc}
11 & 0 & 0 \\
0 & 11 & 0 \\
0 & 0 & 11
\end{array}\right)
\end{aligned}
$$

Hence, $A(\operatorname{adj} A)=(\operatorname{adj} A) A=|A| I$.
:::

:::

:::question{number="23" kind="exercise" id="q_4.23" topic="Finding the inverse of a 2x2 matrix"}
#### Question 23

:::prompt
Find the inverse of each of the matrices (if it exists) given in Exercises 5 to 11.
$$\left[\begin{array}{cc}2 & -2 \\ 4 & 3\end{array}\right]$$
:::

:::solution{label="Solution"}
Find the inverse of each of the matrix $\left(\begin{array}{cc}2 & -2 \\ 4 & 3\end{array}\right)$ (if it exists).

Solution:
Let $A=\left(\begin{array}{cc}2 & -2 \\ 4 & 3\end{array}\right)$
Then,

$$
\begin{aligned}
|A| & =6+8 \\
& =14
\end{aligned}
$$

Now,

$$
\begin{array}{ll}
A_{11}=3 & A_{12}=-4 \\
A_{21}=2 & A_{22}=2
\end{array}
$$

Therefore,

$$
\operatorname{adj} A=\left(\begin{array}{cc}
3 & 2 \\
-4 & 2
\end{array}\right)
$$

Hence,

$$
\begin{aligned}
A^{-1} & =\frac{1}{|A|} \operatorname{adj} A \\
& =\frac{1}{14}\left(\begin{array}{cc}
3 & 2 \\
-4 & 2
\end{array}\right)
\end{aligned}
$$
:::

:::

:::question{number="24" kind="exercise" id="q_4.24" topic="Finding the inverse of a 2x2 matrix"}
#### Question 24

:::prompt
Find the inverse of each of the matrices (if it exists) given in Exercises 5 to 11.
$$\left[\begin{array}{cc}-1 & 5 \\ -3 & 2\end{array}\right]$$
:::

:::solution{label="Solution"}
Find the inverse of each of the matrix $\left(\begin{array}{ll}-1 & 5 \\ -3 & 2\end{array}\right)$ (if it exists)
Solution:
Let $A=\left(\begin{array}{ll}-1 & 5 \\ -3 & 2\end{array}\right)$
Then,

$$
|A|=-2+15=13
$$

Now,

$$
\begin{array}{ll}
A_{11}=2 & A_{12}=3 \\
A_{21}=-5 & A_{22}=-1
\end{array}
$$

Therefore,

$$
\operatorname{adj} A=\left(\begin{array}{ll}
2 & -5 \\
3 & -1
\end{array}\right)
$$

Hence,

$$
\begin{aligned}
A^{-1} & =\frac{1}{|A|} \operatorname{adj} A \\
& =\frac{1}{13}\left(\begin{array}{ll}
2 & -5 \\
3 & -1
\end{array}\right)
\end{aligned}
$$
:::

:::

:::question{number="25" kind="exercise" id="q_4.25" topic="Finding the inverse of a 3x3 matrix (upper triangular)"}
#### Question 25

:::prompt
Find the inverse of each of the matrices (if it exists) given in Exercises 5 to 11.
$$\left[\begin{array}{ccc}1 & 2 & 3 \\ 0 & 2 & 4 \\ 0 & 0 & 5\end{array}\right]$$
:::

:::solution{label="Solution"}
Find the inverse of each of the matrix $\left(\begin{array}{lll}1 & 2 & 3 \\ 0 & 2 & 4 \\ 0 & 0 & 5\end{array}\right)$ (if it exists)
Solution:

Let

$$
A=\left(\begin{array}{lll}
1 & 2 & 3 \\
0 & 2 & 4 \\
0 & 0 & 5
\end{array}\right)
$$

Then,

$$
\begin{aligned}
|A| & =1(10-0)-2(0-0)+3(0-0) \\
& =10
\end{aligned}
$$

Now,

$$
\begin{array}{lll}
A_{11}=10 & A_{12}=0 & A_{13}=0 \\
A_{21}=-10 & A_{22}=5 & A_{23}=0 \\
A_{31}=2 & A_{32}=-4 & A_{33}=2
\end{array}
$$

Therefore,

$$
\operatorname{adj} A=\left(\begin{array}{ccc}
10 & -10 & 2 \\
0 & 5 & -4 \\
0 & 0 & 2
\end{array}\right)
$$

Hence,

$$
\begin{aligned}
A^{-1} & =\frac{1}{|A|} \operatorname{adj} A \\
& =\frac{1}{10}\left(\begin{array}{ccc}
10 & -10 & 2 \\
0 & 5 & -4 \\
0 & 0 & 2
\end{array}\right)
\end{aligned}
$$
:::

:::

:::question{number="26" kind="exercise" id="q_4.26" topic="Finding the inverse of a 3x3 matrix"}
#### Question 26

:::prompt
Find the inverse of each of the matrices (if it exists) given in Exercises 5 to 11.
$$\left[\begin{array}{ccc}1 & 0 & 0 \\ 3 & 3 & 0 \\ 5 & 2 & -1\end{array}\right]$$
:::

:::solution{label="Solution"}
Find the inverse of each of the matrix $\left(\begin{array}{ccc}1 & 0 & 0 \\ 3 & 3 & 0 \\ 5 & 2 & -1\end{array}\right)$ (if it exists)
Solution:

Let

$$
A=\left(\begin{array}{ccc}
1 & 0 & 0 \\
3 & 3 & 0 \\
5 & 2 & -1
\end{array}\right)
$$

Then,

$$
|A|=1(-3-0)-0+0=-3
$$

Now,

$$
\begin{array}{lll}
A_{11}=-3 & A_{12}=3 & A_{13}=-9 \\
A_{21}=0 & A_{22}=-1 & A_{23}=-2 \\
A_{31}=0 & A_{32}=0 & A_{33}=3
\end{array}
$$

Therefore,

$$
\operatorname{adj} A=\left(\begin{array}{ccc}
-3 & 0 & 0 \\
3 & -1 & 0 \\
-9 & -2 & 3
\end{array}\right)
$$

Hence,

$$
\begin{aligned}
A^{-1} & =\frac{1}{|A|} \operatorname{adj} A \\
& =\frac{-1}{3}\left(\begin{array}{ccc}
-3 & 0 & 0 \\
3 & -1 & 0 \\
-9 & -2 & 3
\end{array}\right)
\end{aligned}
$$
:::

:::

:::question{number="27" kind="exercise" id="q_4.27" topic="Finding the inverse of a 3x3 matrix"}
#### Question 27

:::prompt
Find the inverse of each of the matrices (if it exists) given in Exercises 5 to 11.
$$\left[\begin{array}{ccc}2 & 1 & 3 \\ 4 & -1 & 0 \\ -7 & 2 & 1\end{array}\right]$$
:::

:::solution{label="Solution"}
Find the inverse of each of the matrix $\left(\begin{array}{ccc}2 & 1 & 3 \\ 4 & -1 & 0 \\ -7 & 2 & 1\end{array}\right)$ (if it exists)

Solution:

Let

$$
A=\left(\begin{array}{ccc}
2 & 1 & 3 \\
4 & -1 & 0 \\
-7 & 2 & 1
\end{array}\right)
$$

Then,

$$
\begin{aligned}
|A| & =2(-1-0)-1(4-0)+3(8-7) \\
& =2(-1)-1(4)+3(1) \\
& =-3
\end{aligned}
$$

Now,

$$
\begin{array}{lll}
A_{11}=-1 & A_{12}=-4 & A_{13}=1 \\
A_{21}=5 & A_{22}=23 & A_{23}=-11 \\
A_{31}=3 & A_{32}=12 & A_{33}=-6
\end{array}
$$

Therefore,

$$
\operatorname{adj} A=\left(\begin{array}{ccc}
-1 & 5 & 3 \\
-4 & 23 & 12 \\
1 & -11 & -6
\end{array}\right)
$$

Hence,

$$
\begin{aligned}
A^{-1} & =\frac{1}{|A|} \operatorname{adj} A \\
& =-\frac{1}{3}\left(\begin{array}{ccc}
-1 & 5 & 3 \\
-4 & 23 & 12 \\
1 & -11 & -6
\end{array}\right)
\end{aligned}
$$
:::

:::

:::question{number="28" kind="exercise" id="q_4.28" topic="Finding the inverse of a 3x3 matrix"}
#### Question 28

:::prompt
Find the inverse of each of the matrices (if it exists) given in Exercises 5 to 11.
$$\left[\begin{array}{ccc}1 & -1 & 2 \\ 0 & 2 & -3 \\ 3 & -2 & 4\end{array}\right]$$
:::

:::solution{label="Solution"}
Find the inverse of each of the matrix $\left(\begin{array}{ccc}1 & -1 & 2 \\ 0 & 2 & -3 \\ 3 & -2 & 4\end{array}\right)$ (if it exists)
Solution:

Let

$$
A=\left(\begin{array}{ccc}
1 & -1 & 2 \\
0 & 2 & -3 \\
3 & -2 & 4
\end{array}\right)
$$

Then, expanding along $C_{1}$,

$$
\begin{aligned}
|A| & =1(8-6)-0+3(3-4)=2-3 \\
& =-1
\end{aligned}
$$

Now,

$$
\begin{array}{llr}
A_{11}=2 & A_{12}=-9 & A_{13}=-6 \\
A_{21}=0 & A_{22}=-2 & A_{23}=-1 \\
A_{31}=-1 & A_{32}=3 & A_{33}=2
\end{array}
$$

Therefore,

$$
\operatorname{adj} A=\left(\begin{array}{ccc}
2 & 0 & -1 \\
-9 & -2 & 3 \\
-6 & -1 & 2
\end{array}\right)
$$

Hence,

$$
\begin{aligned}
A^{-1} & =\frac{1}{|A|} \operatorname{adj} A \\
& =-1\left(\begin{array}{ccc}
2 & 0 & -1 \\
-9 & -2 & 3 \\
-6 & -1 & 2
\end{array}\right) \\
& =\left(\begin{array}{ccc}
-2 & 0 & 1 \\
9 & 2 & -3 \\
6 & 1 & -2
\end{array}\right)
\end{aligned}
$$
:::

:::

:::question{number="29" kind="exercise" id="q_4.29" topic="Finding the inverse of a 3x3 rotation-type matrix"}
#### Question 29

:::prompt
Find the inverse of each of the matrices (if it exists) given in Exercises 5 to 11.
$\left[\begin{array}{ccc}1 & 0 & 0 \\ 0 & \cos \alpha & \sin \alpha \\ 0 & \sin \alpha & -\cos \alpha\end{array}\right]$
:::

:::solution{label="Solution"}
Find the inverse of each of the matrix $\left(\begin{array}{ccc}1 & 0 & 0 \\ 0 & \cos \alpha & \sin \alpha \\ 0 & \sin \alpha & -\cos \alpha\end{array}\right)$ (if it exists)
Solution:

Let

$$
A=\left(\begin{array}{ccc}
1 & 0 & 0 \\
0 & \cos \alpha & \sin \alpha \\
0 & \sin \alpha & -\cos \alpha
\end{array}\right)
$$

Then,

$$
\begin{aligned}
|A| & =1\left(-\cos ^{2} \alpha-\sin ^{2} \alpha\right)=-\left(\cos ^{2} \alpha+\sin ^{2} \alpha\right) \\
& =-1
\end{aligned}
$$

Now,

$$
\begin{array}{lll}
A_{11}=-\cos ^{2} \alpha-\sin ^{2} \alpha=-1 & A_{12}=0 & A_{13}=0 \\
A_{21}=0 & A_{22}=-\cos \alpha & A_{23}=-\sin \alpha \\
A_{31}=0 & A_{32}=-\sin \alpha & A_{33}=\cos \alpha
\end{array}
$$

Therefore,

$$
\operatorname{adj} A=\left(\begin{array}{ccc}
-1 & 0 & 0 \\
0 & -\cos \alpha & -\sin \alpha \\
0 & -\sin \alpha & \cos \alpha
\end{array}\right)
$$

Hence,

$$
\begin{aligned}
A^{-1} & =\frac{1}{|A|} \text { adjA } \\
& =-1\left(\begin{array}{ccc}
-1 & 0 & 0 \\
0 & -\cos \alpha & -\sin \alpha \\
0 & -\sin \alpha & \cos \alpha
\end{array}\right) \\
& =\left(\begin{array}{ccc}
1 & 0 & 0 \\
0 & \cos \alpha & \sin \alpha \\
0 & \sin \alpha & -\cos \alpha
\end{array}\right)
\end{aligned}
$$
:::

:::

:::question{number="30" kind="exercise" id="q_4.30" topic="Verifying (AB)^-1 = B^-1 A^-1"}
#### Question 30

:::prompt
Let $\mathrm{A}=\left[\begin{array}{ll}3 & 7 \\ 2 & 5\end{array}\right]$ and $\mathrm{B}=\left[\begin{array}{ll}6 & 8 \\ 7 & 9\end{array}\right]$. Verify that $(\mathrm{AB})^{-1}=\mathrm{B}^{-1} \mathrm{~A}^{-1}$.
:::

:::solution{label="Solution"}
Let $A=\left(\begin{array}{ll}3 & 7 \\ 2 & 5\end{array}\right)$ and $B=\left(\begin{array}{ll}6 & 8 \\ 7 & 9\end{array}\right)$. Verify that $(A B)^{-1}=B^{-1} A^{-1}$.
Solution:
Let $A=\left(\begin{array}{ll}3 & 7 \\ 2 & 5\end{array}\right)$
Then,

$$
\begin{aligned}
|A| & =15-14 \\
& =1
\end{aligned}
$$

Now,

$$
\begin{array}{ll}
A_{11}=5 & A_{12}=-2 \\
A_{21}=-7 & A_{22}=3
\end{array}
$$

Then,

$$
\operatorname{adj} A=\left(\begin{array}{cc}
5 & -7 \\
-2 & 3
\end{array}\right)
$$

Therefore,

$$
\begin{aligned}
A^{-1} & =\frac{1}{|A|} \operatorname{adj} A \\
& =\left(\begin{array}{cc}
5 & -7 \\
-2 & 3
\end{array}\right)
\end{aligned}
$$

Now,
Let $B=\left(\begin{array}{ll}6 & 8 \\ 7 & 9\end{array}\right)$
Then,

$$
\begin{aligned}
|B| & =54-56 \\
& =-2
\end{aligned}
$$

Now,

$$
\begin{array}{ll}
A_{11}=9 & A_{12}=-7 \\
A_{21}=-8 & A_{22}=6
\end{array}
$$

Then,

$$
\operatorname{adj} B=\left(\begin{array}{cc}
9 & -8 \\
-7 & 6
\end{array}\right)
$$

Therefore,

$$
\begin{aligned}
B^{-1} & =\frac{1}{|B|} \operatorname{adjB} \\
& =-\frac{1}{2}\left(\begin{array}{cc}
9 & -8 \\
-7 & 6
\end{array}\right) \\
& =\left(\begin{array}{cc}
-\frac{9}{2} & 4 \\
\frac{7}{2} & -3
\end{array}\right)
\end{aligned}
$$

Now,

$$
\begin{aligned}
B^{-1} A^{-1} & =\left(\begin{array}{cc}
-\frac{9}{2} & 4 \\
\frac{7}{2} & -3
\end{array}\right)\left(\begin{array}{cc}
5 & -7 \\
-2 & 3
\end{array}\right) \\
& =\left(\begin{array}{cc}
-\frac{45}{2}-8 & \frac{63}{2}+12 \\
\frac{35}{2}+6 & -\frac{49}{2}-9
\end{array}\right) \\
& =\left(\begin{array}{cc}
-\frac{61}{2} & \frac{87}{2} \\
\frac{47}{2} & \frac{-67}{2}
\end{array}\right)
\end{aligned}
$$

Also,

$$
\begin{aligned}
A B & =\left(\begin{array}{ll}
3 & 7 \\
2 & 5
\end{array}\right)\left(\begin{array}{ll}
6 & 8 \\
7 & 9
\end{array}\right) \\
& =\left(\begin{array}{ll}
18+49 & 24+63 \\
12+35 & 16+45
\end{array}\right) \\
& =\left(\begin{array}{ll}
67 & 87 \\
47 & 61
\end{array}\right)
\end{aligned}
$$

Then, we have

$$
\begin{aligned}
|A B| & =67(61)-87(47) \\
& =4087-4089 \\
& =-2
\end{aligned}
$$

Therefore,

$$
\operatorname{adj}(A B)=\left(\begin{array}{cc}
61 & -87 \\
-47 & 67
\end{array}\right)
$$

Thus,

$$
\begin{aligned}
(A B)^{-1} & =\frac{1}{|A B|} \operatorname{adj}(A B) \\
& =-\frac{1}{2}\left(\begin{array}{cc}
61 & -87 \\
-47 & 67
\end{array}\right) \\
& =\left(\begin{array}{cc}
-\frac{61}{2} & \frac{87}{2} \\
\frac{47}{2} & -\frac{67}{2}
\end{array}\right)
\end{aligned}
$$

From (1) and (2),

$$
(A B)^{-1}=B^{-1} A^{-1}
$$

Hence, proved.
:::

:::

:::question{number="31" kind="exercise" id="q_4.31" topic="Matrix polynomial identity and inverse via it"}
#### Question 31

:::prompt
If $\mathrm{A}=\left[\begin{array}{cc}3 & 1 \\ -1 & 2\end{array}\right]$, show that $\mathrm{A}^{2}-5 \mathrm{~A}+7 \mathrm{I}=\mathrm{O}$. Hence find $\mathrm{A}^{-1}$.
:::

:::solution{label="Solution"}
If $A=\left(\begin{array}{cc}3 & 1 \\ -1 & 2\end{array}\right)$, show that $A^{2}-5 A+7 I=0$. Hence find $A^{-1}$.
Solution:
Let $A=\left(\begin{array}{cc}3 & 1 \\ -1 & 2\end{array}\right)$
Therefore,

$$
\begin{aligned}
A^{2} & =A \cdot A=\left(\begin{array}{cc}
3 & 1 \\
-1 & 2
\end{array}\right)\left(\begin{array}{cc}
3 & 1 \\
-1 & 2
\end{array}\right) \\
& =\left(\begin{array}{cc}
9-1 & 3+2 \\
-3-2 & -1+4
\end{array}\right) \\
& =\left(\begin{array}{cc}
8 & 5 \\
-5 & 3
\end{array}\right)
\end{aligned}
$$

Now,

$$
\begin{aligned}
A^{2}-5 A+7 I & =\left(\begin{array}{cc}
8 & 5 \\
-5 & 3
\end{array}\right)-5\left(\begin{array}{cc}
3 & 1 \\
-1 & 2
\end{array}\right)+7\left(\begin{array}{ll}
1 & 0 \\
0 & 1
\end{array}\right) \\
& =\left(\begin{array}{cc}
8 & 5 \\
-5 & 3
\end{array}\right)-\left(\begin{array}{cc}
15 & 5 \\
-5 & 10
\end{array}\right)+\left(\begin{array}{ll}
7 & 0 \\
0 & 7
\end{array}\right) \\
& =\left(\begin{array}{cc}
-7 & 0 \\
0 & -7
\end{array}\right)+\left(\begin{array}{ll}
7 & 0 \\
0 & 7
\end{array}\right) \\
& =\left(\begin{array}{ll}
0 & 0 \\
0 & 0
\end{array}\right)
\end{aligned}
$$

Hence, $A^{2}-5 A+7 I=0$.
Now,

$$
\begin{aligned}
& \Rightarrow A \cdot A-5 A=-7 I \\
& \Rightarrow A \cdot A\left(A^{-1}\right)-5 A \cdot A^{-1}=-7 I A^{-1} \quad\left[\text { post-multiplying by } A^{-1} \text { as }|A| \neq 0\right] \\
& \Rightarrow A\left(A A^{-1}\right)-5 I=-7 A^{-1} \\
& \Rightarrow A I-5 I=-7 A^{-1} \\
& \Rightarrow A^{-1}=-\frac{1}{7}(A-5 I) \\
& \Rightarrow A^{-1}=\frac{1}{7}(5 I-A) \\
& \Rightarrow A^{-1}=\frac{1}{7}\left[\left(\begin{array}{cc}
5 & 0 \\
0 & 5
\end{array}\right)-\left(\begin{array}{cc}
3 & 1 \\
-1 & 2
\end{array}\right)\right] \\
& \Rightarrow A^{-1}=\frac{1}{7}\left(\begin{array}{cc}
2 & -1 \\
1 & 3
\end{array}\right)
\end{aligned}
$$

Thus,

$$
A^{-1}=\frac{1}{7}\left(\begin{array}{cc}
2 & -1 \\
1 & 3
\end{array}\right)
$$
:::

:::

:::question{number="32" kind="exercise" id="q_4.32" topic="Finding a, b from a matrix polynomial identity"}
#### Question 32

:::prompt
For the matrix $\mathrm{A}=\left[\begin{array}{ll}3 & 2 \\ 1 & 1\end{array}\right]$, find the numbers $a$ and $b$ such that $\mathrm{A}^{2}+a \mathrm{~A}+b \mathrm{I}=\mathrm{O}$.
:::

:::solution{label="Solution"}
For the matrix $A=\left(\begin{array}{ll}3 & 2 \\ 1 & 1\end{array}\right)$, find the numbers $a$ and $b$ such that $A^{2}+a A+b I=0$.
Solution:
Let $A=\left(\begin{array}{ll}3 & 2 \\ 1 & 1\end{array}\right)$

Therefore,

$$
\begin{aligned}
A^{2} & =A \cdot A=\left(\begin{array}{ll}
3 & 2 \\
1 & 1
\end{array}\right)\left(\begin{array}{ll}
3 & 2 \\
1 & 1
\end{array}\right) \\
& =\left(\begin{array}{ll}
9+2 & 6+2 \\
3+1 & 2+1
\end{array}\right)=\left(\begin{array}{cc}
11 & 8 \\
4 & 3
\end{array}\right)
\end{aligned}
$$

Now, $A^{2}+a A+b I=0$.
Hence,

$$
\begin{aligned}
& \Rightarrow(A \cdot A) A^{-1}+a A \cdot A^{-1}+b I A^{-1}=0 \quad\left[\text { post-multiplying by } A^{-1} \text { as }|A| \neq 0\right] \\
& \Rightarrow A\left(A A^{-1}\right)+a I+b\left(I A^{-1}\right)=0 \\
& \Rightarrow A I+a I+b A^{-1}=0 \\
& \Rightarrow A+a I=-b A^{-1} \\
& \Rightarrow A^{-1}=-\frac{1}{b}(A+a I) \quad \ldots(1)
\end{aligned}
$$

Now,

$$
\begin{aligned}
A^{-1} & =\frac{1}{|A|} \operatorname{adj} A \\
& =\frac{1}{1}\left(\begin{array}{cc}
1 & -2 \\
-1 & 3
\end{array}\right) \\
& =\left(\begin{array}{cc}
1 & -2 \\
-1 & 3
\end{array}\right)
\end{aligned}
$$

From (1) and (2), we have,

$$
\begin{aligned}
& \Rightarrow\left(\begin{array}{cc}
1 & -2 \\
-1 & 3
\end{array}\right)=\frac{1}{b}\left[\left(\begin{array}{ll}
3 & 2 \\
1 & 1
\end{array}\right)+\left(\begin{array}{ll}
a & 0 \\
0 & a
\end{array}\right)\right] \\
& \Rightarrow\left(\begin{array}{cc}
1 & -2 \\
-1 & 3
\end{array}\right)=-\frac{1}{b}\left(\begin{array}{cc}
3+a & 2 \\
1 & a
\end{array}\right) \\
& \Rightarrow\left(\begin{array}{cc}
1 & -2 \\
-1 & 3
\end{array}\right)=\left(\begin{array}{cc}
\frac{-3-a}{b} & -\frac{2}{b} \\
-\frac{1}{b} & \frac{-1-a}{b}
\end{array}\right)
\end{aligned}
$$

Comparing the corresponding elements of the two matrices, we have:

$$
\begin{aligned}
& \Rightarrow-\frac{1}{b}=-1 \\
& \Rightarrow b=1
\end{aligned}
$$

Also,

$$
\begin{aligned}
& \Rightarrow \frac{-3-a}{b}=1 \\
& \Rightarrow-3-a=1 \\
& \Rightarrow a=-4
\end{aligned}
$$

Thus, $a=-4$ and $b=1$.
:::

:::

:::question{number="33" kind="exercise" id="q_4.33" topic="Matrix polynomial identity and inverse via it (3x3)"}
#### Question 33

:::prompt
For the matrix $\mathrm{A}=\left[\begin{array}{ccc}1 & 1 & 1 \\ 1 & 2 & -3 \\ 2 & -1 & 3\end{array}\right]$
Show that $\mathrm{A}^{3}-6 \mathrm{~A}^{2}+5 \mathrm{~A}+11 \mathrm{I}=\mathrm{O}$. Hence, find $\mathrm{A}^{-1}$.

$$
2-11
$$
:::

:::solution{label="Solution"}
For the matrix

$$
A=\left(\begin{array}{ccc}
1 & 1 & 1 \\
1 & 2 & -3 \\
2 & -1 & 3
\end{array}\right) \text {, show that } A^{3}-6 A^{2}+5 A+11 I=0 \text {. Hence, find } A^{-1} \text {. }
$$

Solution:

Let

$$
A=\left(\begin{array}{ccc}
1 & 1 & 1 \\
1 & 2 & -3 \\
2 & -1 & 3
\end{array}\right)
$$

Therefore,

$$
\begin{aligned}
A^{2} & =A \cdot A=\left(\begin{array}{ccc}
1 & 1 & 1 \\
1 & 2 & -3 \\
2 & -1 & 3
\end{array}\right)\left(\begin{array}{ccc}
1 & 1 & 1 \\
1 & 2 & -3 \\
2 & -1 & 3
\end{array}\right) \\
& =\left(\begin{array}{ccc}
1+1+2 & 1+2-1 & 1-3+3 \\
1+2-6 & 1+4+3 & 1-6-9 \\
2-1+6 & 2-2-3 & 2+3+9
\end{array}\right)=\left(\begin{array}{ccc}
4 & 2 & 1 \\
-3 & 8 & -14 \\
7 & -3 & 14
\end{array}\right)
\end{aligned}
$$

And,

$$
\begin{aligned}
A^{3} & =A^{2} \cdot A=\left(\begin{array}{ccc}
4 & 2 & 1 \\
-3 & 8 & -14 \\
7 & -3 & 14
\end{array}\right)\left(\begin{array}{ccc}
1 & 1 & 1 \\
1 & 2 & -3 \\
2 & -1 & 3
\end{array}\right) \\
& =\left(\begin{array}{ccc}
4+2+2 & 4+4-1 & 4-6+3 \\
-3+8-28 & -3+16+14 & -3-24-42 \\
7-3+28 & 7-6-14 & 7+9+42
\end{array}\right)=\left(\begin{array}{ccc}
8 & 7 & 1 \\
-23 & 27 & -69 \\
32 & -13 & 58
\end{array}\right)
\end{aligned}
$$

Hence,

$$
\begin{aligned}
A^{3}-6 A^{2}+5 A+11 I & =\left(\begin{array}{ccc}
8 & 7 & 1 \\
-23 & 27 & -69 \\
32 & -13 & 58
\end{array}\right)-6\left(\begin{array}{ccc}
4 & 2 & 1 \\
-3 & 8 & -14 \\
7 & -3 & 14
\end{array}\right)+5\left(\begin{array}{ccc}
1 & 1 & 1 \\
1 & 2 & -3 \\
2 & -1 & 3
\end{array}\right)+11\left(\begin{array}{ccc}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{array}\right) \\
& =\left(\begin{array}{ccc}
8 & 7 & 1 \\
-23 & 27 & -69 \\
32 & -13 & 58
\end{array}\right)-\left(\begin{array}{ccc}
24 & 12 & 6 \\
-18 & 48 & -84 \\
42 & -18 & 84
\end{array}\right)+\left(\begin{array}{ccc}
5 & 5 & 5 \\
5 & 10 & -15 \\
10 & -5 & 15
\end{array}\right)+\left(\begin{array}{ccc}
11 & 0 & 0 \\
0 & 11 & 0 \\
0 & 0 & 11
\end{array}\right) \\
& =\left(\begin{array}{ccc}
24 & 12 & 6 \\
-18 & 48 & -84 \\
42 & -18 & 84
\end{array}\right)-\left(\begin{array}{ccc}
24 & 12 & 6 \\
-18 & 48 & -84 \\
42 & -18 & 84
\end{array}\right) \\
& =\left(\begin{array}{ccc}
0 & 0 & 0 \\
0 & 0 & 0 \\
0 & 0 & 0
\end{array}\right) \\
& =0
\end{aligned}
$$

Thus, $A^{3}-6 A^{2}+5 A+11 I=0$
Now,

$$
\begin{aligned}
& \Rightarrow A^{3}-6 A^{2}+5 A+11 I=0 \\
& \Rightarrow(A A A) A^{-1}-6(A A) A^{-1}+5 A A^{-1}+11 L A^{-1}=0 \quad\left[\text { post-multiplying by } A^{-1} \text { as }|A| \neq 0\right] \\
& \Rightarrow A A\left(A A^{-1}\right)-6 A\left(A A^{-1}\right)+5\left(A A^{-1}\right)=-11\left(I A^{-1}\right) \\
& \Rightarrow A^{2}-6 A+5 I=-11 A^{-1} \\
& \Rightarrow A^{-1}=-\frac{1}{11}\left(A^{2}-6 A+5 I\right)
\end{aligned}
$$

Now,

$$
\begin{aligned}
A^{2}-6 A+5 I & =\left(\begin{array}{ccc}
4 & 2 & 1 \\
-3 & 8 & -14 \\
7 & -3 & 14
\end{array}\right)-6\left(\begin{array}{ccc}
1 & 1 & 1 \\
1 & 2 & -3 \\
2 & -1 & 3
\end{array}\right)+5\left(\begin{array}{ccc}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{array}\right) \\
& =\left(\begin{array}{ccc}
4 & 2 & 1 \\
-3 & 8 & -14 \\
7 & -3 & 14
\end{array}\right)-\left(\begin{array}{ccc}
6 & 6 & 6 \\
6 & 12 & -18 \\
12 & -6 & 18
\end{array}\right)+\left(\begin{array}{ccc}
5 & 0 & 0 \\
0 & 5 & 0 \\
0 & 0 & 5
\end{array}\right) \\
& =\left(\begin{array}{ccc}
9 & 2 & 1 \\
-3 & 13 & -14 \\
7 & -3 & 19
\end{array}\right)-\left(\begin{array}{ccc}
6 & 6 & 6 \\
6 & 12 & -18 \\
12 & -6 & 18
\end{array}\right) \\
& =\left(\begin{array}{ccc}
3 & -4 & -5 \\
-9 & 1 & 4 \\
-5 & 3 & 1
\end{array}\right)
\end{aligned}
$$

From equation (1) and (2)

$$
\begin{aligned}
A^{-1} & =-\frac{1}{11}\left(\begin{array}{ccc}
3 & -4 & -5 \\
-9 & 1 & 4 \\
-5 & 3 & 1
\end{array}\right) \\
& =\frac{1}{11}\left(\begin{array}{ccc}
-3 & 4 & 5 \\
9 & -1 & -4 \\
5 & -3 & -1
\end{array}\right)
\end{aligned}
$$
:::

:::

:::question{number="34" kind="exercise" id="q_4.34" topic="Matrix polynomial identity and inverse via it (3x3)"}
#### Question 34

:::prompt
If $\mathrm{A}=\left[\begin{array}{ccc}-1 & 2 & -1 \\ 1 & -1 & 2\end{array}\right]$
Verify that $\mathrm{A}^{3}-6 \mathrm{~A}^{2}+9 \mathrm{~A}-4 \mathrm{I}=\mathrm{O}$ and hence find $\mathrm{A}^{-1}$
:::

:::solution{label="Solution"}
$$
A=\left(\begin{array}{ccc}
2 & -1 & 1 \\
-1 & 2 & -1 \\
1 & -1 & 2
\end{array}\right), \text { verify that } A^{3}-6 A^{2}+9 A-4 I=0 . \text { Hence, find } A^{-1} .
$$

Solution:
Let

$$
A=\left(\begin{array}{ccc}
2 & -1 & 1 \\
-1 & 2 & -1 \\
1 & -1 & 2
\end{array}\right)
$$

Therefore,

$$
\begin{aligned}
A^{2} & =A . A \\
& =\left(\begin{array}{ccc}
2 & -1 & 1 \\
-1 & 2 & -1 \\
1 & -1 & 2
\end{array}\right)\left(\begin{array}{ccc}
2 & -1 & 1 \\
-1 & 2 & -1 \\
1 & -1 & 2
\end{array}\right) \\
& =\left(\begin{array}{ccc}
4+1+1 & -2-2-1 & 2+1+2 \\
-2-2-1 & 1+4+1 & -1-2-2 \\
2+1+2 & -1-2-2 & 1+1+4
\end{array}\right) \\
& =\left(\begin{array}{ccc}
6 & -5 & 5 \\
-5 & 6 & -5 \\
5 & -5 & 6
\end{array}\right)
\end{aligned}
$$

And

$$
\begin{aligned}
A^{3} & =A^{2} \cdot A \\
& =\left(\begin{array}{ccc}
6 & -5 & 5 \\
-5 & 6 & -5 \\
5 & -5 & 6
\end{array}\right)\left(\begin{array}{ccc}
2 & -1 & 1 \\
-1 & 2 & -1 \\
1 & -1 & 2
\end{array}\right) \\
& =\left(\begin{array}{ccc}
12+5+5 & -6-10-5 & 6+5+10 \\
-10-6-5 & 5+12+5 & -5-6-10 \\
10+5+6 & -5-10-6 & 5+5+12
\end{array}\right) \\
& =\left(\begin{array}{ccc}
22 & -21 & 21 \\
-21 & 22 & -21 \\
21 & -21 & 22
\end{array}\right)
\end{aligned}
$$

Now,

$$
\begin{aligned}
A^{3}-6 A^{2}+9 A-4 I & =\left(\begin{array}{ccc}
22 & -21 & 21 \\
-21 & 22 & -21 \\
21 & -21 & 22
\end{array}\right)-6\left(\begin{array}{ccc}
6 & -5 & 5 \\
-5 & 6 & -5 \\
5 & -5 & 6
\end{array}\right)+9\left(\begin{array}{ccc}
2 & -1 & 1 \\
-1 & 2 & -1 \\
1 & -1 & 2
\end{array}\right)-4\left(\begin{array}{ccc}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{array}\right) \\
& =\left(\begin{array}{ccc}
22 & -21 & 21 \\
-21 & 22 & -21 \\
21 & -21 & 22
\end{array}\right)-\left(\begin{array}{ccc}
36 & -30 & 30 \\
-30 & 36 & -30 \\
30 & -30 & 36
\end{array}\right)+\left(\begin{array}{ccc}
18 & -9 & 9 \\
-9 & 18 & -9 \\
9 & -9 & 18
\end{array}\right)-\left(\begin{array}{ccc}
4 & 0 & 0 \\
0 & 4 & 0 \\
0 & 0 & 4
\end{array}\right) \\
& =\left(\begin{array}{ccc}
40 & -30 & 30 \\
-30 & 40 & -30 \\
30 & -30 & 40
\end{array}\right)-\left(\begin{array}{ccc}
40 & -30 & 30 \\
-30 & 40 & -30 \\
30 & -30 & 40
\end{array}\right) \\
& =\left(\begin{array}{ccc}
0 & 0 & 0 \\
0 & 0 & 0 \\
0 & 0 & 0
\end{array}\right) \\
& =0
\end{aligned}
$$

Thus,

$$
A^{3}-6 A^{2}+9 A-4 I=0
$$

Now,

$$
\begin{aligned}
& \Rightarrow A^{3}-6 A^{2}+9 A-4 I=0 \\
& \Rightarrow(A A A) A^{-1}-6(A A) A^{-1}+9 A A^{-1}-4 I A^{-1}=0 \quad\left[\text { post-multiplying by } A^{-1} \text { as }|A| \neq 0\right] \\
& \Rightarrow A A\left(A A^{-1}\right)-6 A\left(A A^{-1}\right)+9\left(A A^{-1}\right)=4\left(I A^{-1}\right) \\
& \Rightarrow A A I-6 A I+9 I=4 A^{-1} \\
& \Rightarrow A^{2}-6 A+9 I=4 A^{-1} \\
& \Rightarrow A^{-1}=\frac{1}{4}\left(A^{2}-6 A+9 I\right)
\end{aligned}
$$

Now,

$$
\begin{aligned}
A^{2}-6 A+9 I & =\left(\begin{array}{ccc}
6 & -5 & 5 \\
-5 & 6 & -5 \\
5 & -5 & 6
\end{array}\right)-6\left(\begin{array}{ccc}
2 & -1 & 1 \\
-1 & 2 & -1 \\
1 & -1 & 2
\end{array}\right)+9\left(\begin{array}{lll}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{array}\right) \\
& =\left(\begin{array}{ccc}
6 & -5 & 5 \\
-5 & 6 & -5 \\
5 & -5 & 6
\end{array}\right)-\left(\begin{array}{ccc}
12 & -6 & 6 \\
-6 & 12 & -6 \\
6 & -6 & 12
\end{array}\right)+\left(\begin{array}{ccc}
9 & 0 & 0 \\
0 & 9 & 0 \\
0 & 0 & 9
\end{array}\right) \\
& =\left(\begin{array}{ccc}
3 & 1 & -1 \\
1 & 3 & 1 \\
-1 & 1 & 3
\end{array}\right)
\end{aligned}
$$

From equations (1) and (2),

$$
A^{-1}=\frac{1}{4}\left(\begin{array}{ccc}
3 & 1 & -1 \\
1 & 3 & 1 \\
-1 & 1 & 3
\end{array}\right)
$$
:::

:::

:::question{number="35" kind="exercise" id="q_4.35" topic="MCQ - |adj A| for a nonsingular 3x3 matrix"}
#### Question 35

:::prompt
Let A be a nonsingular square matrix of order $3 \times 3$. Then $|\operatorname{adj} \mathrm{A}|$ is equal to
(A) $|\mathrm{A}|$
(B) $|\mathrm{A}|^{2}$
(C) $|\mathrm{A}|^{3}$
(D) $3|\mathrm{~A}|$
:::

:::solution{label="Solution"}
Let $A$ be a non-singular square matrix of order $3 \times 3$. Then $|\operatorname{adj} A|$ is equal to:
(A) $|A|$
(B) $|A|^{2}$
(C) $|A|^{3}$
(D) $3|A|$

Solution:
Since $A$ is a non-singular square matrix of order $3 \times 3$

$$
\begin{aligned}
(\operatorname{adj} A) A & =|A| I \\
& =\left(\begin{array}{ccc}
|A| & 0 & 0 \\
0 & |A| & 0 \\
0 & 0 & |A|
\end{array}\right)
\end{aligned}
$$

Therefore,

$$
\begin{aligned}
|(\operatorname{adj} A) A| & =\left|\begin{array}{ccc}
A \mid & 0 & 0 \\
0 & |A| & 0 \\
0 & 0 & |A|
\end{array}\right| \\
|\operatorname{adj} A||A| & =|A|^{3}\left|\begin{array}{ccc}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{array}\right| \\
& =|A|^{3} I \\
|\operatorname{adj} A| & =|A|^{2}
\end{aligned}
$$

Thus, the correct option is B.
:::

:::

:::question{number="36" kind="exercise" id="q_4.36" topic="MCQ - det(A^-1) for an invertible 2x2 matrix"}
#### Question 36

:::prompt
If A is an invertible matrix of order 2 , then $\operatorname{det}\left(\mathrm{A}^{-1}\right)$ is equal to
(A) $\operatorname{det}(\mathrm{A})$
(B) $\frac{1}{\operatorname{det}(\mathrm{~A})}$
(C) 1
(D) 0
:::

:::solution{label="Solution"}
If $A$ is an invertible matrix of order 2 , the $\operatorname{det}\left(A^{-1}\right)$ is equal to:
(A) $\operatorname{det}(A)$
(B) $\frac{1}{\operatorname{det}(A)}$
(C) 1
(D) 0

Solution:
Since $A$ is an invertible matrix, $A^{-1}$ exists. Also, $A^{-1}=\frac{1}{|A|}$ adj $A$. As matrix $A$ is of order 2, let $A=\left(\begin{array}{ll}a & b \\ c & d\end{array}\right)$

Then,

$$
|A|=a d-b c
$$

And

$$
\operatorname{adj} A=\left(\begin{array}{cc}
d & -b \\
-c & a
\end{array}\right)
$$

Now,

$$
\begin{aligned}
A^{-1} & =\frac{1}{|A|} \operatorname{adj} A \\
& =\left(\begin{array}{cc}
\frac{d}{|A|} & \frac{-b}{|A|} \\
\frac{-c}{|A|} & \frac{a}{|A|}
\end{array}\right)
\end{aligned}
$$

Hence,

$$
\begin{aligned}
\left|A^{-1}\right| & =\left|\begin{array}{cc}
\frac{d}{|A|} & \frac{-b}{|A|} \\
\frac{-c}{|A|} & \frac{a}{|A|}
\end{array}\right| \\
\left|A^{-1}\right| & =\frac{1}{|A|^{2}}\left|\begin{array}{cc}
d & -b \\
-c & a
\end{array}\right| \\
& =\frac{1}{|A|^{2}}(a d-b c) \\
& =\frac{1}{|A|^{2}} \cdot|A| \\
& =\frac{1}{|A|}
\end{aligned}
$$

Hence,

$$
\operatorname{det}\left(A^{-1}\right)=\frac{1}{\operatorname{det}(A)}
$$

Thus, the correct option is B.
:::

:::

:::question{number="37" kind="exercise" id="q_4.37" topic="Examining consistency of a linear system"}
#### Question 37

:::prompt
Examine the consistency of the system of equations in Exercises 1 to 6.
$$
\begin{aligned}
& x+2 y=2 \\
& 2 x+3 y=3
\end{aligned}
$$
:::

:::solution{label="Solution"}
Examine the consistency of the system of equations:

$$
\begin{aligned}
& x+2 y=2 \\
& 2 x+3 y=3
\end{aligned}
$$

Solution:

$$
x+2 y=2
$$

The given system of equations is: $2 x+3 y=3$
We can write the given system of equations in the form $A X=B$, where

$$
A=\left(\begin{array}{ll}
1 & 2 \\
2 & 3
\end{array}\right), X=\left[\begin{array}{l}
x \\
y
\end{array}\right] \text { and } B=\left[\begin{array}{l}
2 \\
3
\end{array}\right]
$$

Hence,

$$
\begin{aligned}
|A| & =1(3)-2(2) \\
& =3-4 \\
& =-1 \\
& \neq 0
\end{aligned}
$$

So, $A$ is non-singular.
Therefore, $A^{-1}$ exists.
Thus, the given system of equations is consistent.
:::

:::

:::question{number="38" kind="exercise" id="q_4.38" topic="Examining consistency of a linear system"}
#### Question 38

:::prompt
Examine the consistency of the system of equations in Exercises 1 to 6.
$$
\begin{aligned}
& 2 x-y=5 \\
& x+y=4
\end{aligned}
$$
:::

:::solution{label="Solution"}
Examine the consistency of the system of equations:

$$
\begin{aligned}
& 2 x-y=5 \\
& x+y=4
\end{aligned}
$$

Solution:

$$
2 x-y=5
$$

The given system of equations is: $x+y=4$
We can write the given system of equations in the form $A X=B$, where

$$
A=\left(\begin{array}{cc}
2 & -1 \\
1 & 1
\end{array}\right), X=\left[\begin{array}{l}
x \\
y
\end{array}\right] \text { and } B=\left[\begin{array}{l}
5 \\
4
\end{array}\right]
$$

Hence,

$$
\begin{aligned}
|A| & =2(1)-1(-1) \\
& =2+1 \\
& =3 \\
& \neq 0
\end{aligned}
$$

So, $A$ is non-singular.
Therefore, $A^{-1}$ exists.
Hence, the given system of equations is consistent.
:::

:::

:::question{number="39" kind="exercise" id="q_4.39" topic="Examining consistency of a linear system"}
#### Question 39

:::prompt
Examine the consistency of the system of equations in Exercises 1 to 6.
$$
\begin{aligned}
& x+3 y=5 \\
& 2 x+6 y=8
\end{aligned}
$$
:::

:::solution{label="Solution"}
Examine the consistency of the system of equations:

$$
\begin{aligned}
& x+3 y=5 \\
& 2 x+6 y=8
\end{aligned}
$$

Solution:

$$
x+3 y=5
$$

The given system of equations is: $2 x+6 y=8$
We can write the given system of equations in the form $A X=B$, where

$$
A=\left(\begin{array}{ll}
1 & 3 \\
2 & 6
\end{array}\right), X=\left[\begin{array}{l}
x \\
y
\end{array}\right] \text { and } B=\left[\begin{array}{l}
5 \\
8
\end{array}\right]
$$

Hence,

$$
\begin{aligned}
|A| & =1(6)-3(2) \\
& =6-6 \\
& =0
\end{aligned}
$$

So, $A$ is a singular matrix.
Now,

$$
(\operatorname{adj} A)=\left(\begin{array}{cc}
6 & -3 \\
-2 & 1
\end{array}\right)
$$

Therefore,

$$
\begin{aligned}
(\operatorname{adj} A) B & =\left(\begin{array}{cc}
6 & -5 \\
-2 & 1
\end{array}\right)\left[\begin{array}{l}
5 \\
8
\end{array}\right] \\
& =\binom{30-24}{-10+8} \\
& =\left[\begin{array}{c}
6 \\
-2
\end{array}\right] \\
& \neq 0
\end{aligned}
$$

Thus, the solution of the given system of equations does not exist.
Hence, the system of equations is inconsistent.
:::

:::

:::question{number="40" kind="exercise" id="q_4.40" topic="Examining consistency of a linear system with a parameter"}
#### Question 40

:::prompt
Examine the consistency of the system of equations in Exercises 1 to 6.
$$
\begin{aligned}
& x+y+z=1 \\
& 2 x+3 y+2 z=2 \\
& a x+a y+2 a z=4
\end{aligned}
$$
:::

:::solution{label="Solution"}
Examine the consistency of the system of equations:

$$
\begin{aligned}
& x+y+z=1 \\
& 2 x+3 y+2 z=2 \\
& a x+a y+2 a z=4
\end{aligned}
$$

Solution:

$$
\begin{aligned}
& x+y+z=1 \\
& 2 x+3 y+2 z=2
\end{aligned}
$$

The given system of equations is: $a x+a y+2 a z=4$
We can write the given system of equations in the form $A X=B$, where

$$
A=\left(\begin{array}{ccc}
1 & 1 & 1 \\
2 & 3 & 2 \\
a & a & 2 a
\end{array}\right), X=\left[\begin{array}{l}
x \\
y \\
z
\end{array}\right] \text { and } B=\left[\begin{array}{l}
1 \\
2 \\
4
\end{array}\right]
$$

Hence,

$$
\begin{aligned}
|A| & =1(6 a-2 a)-1(4 a-2 a)+1(2 a-3 a) \\
& =4 a-2 a-a \\
& =4 a-3 a \\
& =a \neq 0
\end{aligned}
$$

So, $A$ is non-singular.
Therefore, $A^{-1}$ exists.
Thus, the given system of equations is consistent.
:::

:::

:::question{number="41" kind="exercise" id="q_4.41" topic="Examining consistency of a linear system"}
#### Question 41

:::prompt
Examine the consistency of the system of equations in Exercises 1 to 6.
$$
\begin{aligned}
& 3 x-y-2 z=2 \\
& 2 y-z=-1 \\
& 3 x-5 y=3
\end{aligned}
$$
:::

:::solution{label="Solution"}
Examine the consistency of the system of equations:

$$
\begin{aligned}
& 3 x-y-2 z=2 \\
& 2 y-z=-1 \\
& 3 x-5 y=3
\end{aligned}
$$

Solution:

$$
\begin{aligned}
& 3 x-y-2 z=2 \\
& 2 y-z=-1
\end{aligned}
$$

The given system of equations is: $3 x-5 y=3$
We can write the given system of equations in the form $A X=B$, where

$$
A=\left(\begin{array}{ccc}
3 & -1 & -2 \\
0 & 2 & -1 \\
3 & -5 & 0
\end{array}\right), X=\left[\begin{array}{l}
x \\
y \\
z
\end{array}\right] \text { and } B=\left[\begin{array}{c}
2 \\
-1 \\
3
\end{array}\right]
$$

Hence,

$$
\begin{aligned}
|A| & =3(0-5)-0+3(1+4) \\
& =-15+15 \\
& =0
\end{aligned}
$$

So, $A$ is a singular matrix.
Now,

$$
(\operatorname{adj} A)=\left(\begin{array}{ccc}
-5 & 10 & 5 \\
-3 & 6 & 3 \\
-6 & 12 & 6
\end{array}\right)
$$

Therefore,

$$
\begin{aligned}
(\operatorname{adj} A) B & =\left(\begin{array}{ccc}
-5 & 10 & 5 \\
-3 & 6 & 3 \\
-6 & 12 & 6
\end{array}\right)\left[\begin{array}{c}
2 \\
-1 \\
3
\end{array}\right] \\
& =\left[\begin{array}{c}
-10-10+15 \\
-6-6+9 \\
-12-12+18
\end{array}\right] \\
& =\left[\begin{array}{c}
-5 \\
-3 \\
-6
\end{array}\right] \\
& \neq 0
\end{aligned}
$$

Thus, the solution of the given system of equations does not exist.
Hence, the system of equations is inconsistent.
:::

:::

:::question{number="42" kind="exercise" id="q_4.42" topic="Examining consistency of a linear system" corrections_applied="1"}
#### Question 42

:::prompt
Examine the consistency of the system of equations in Exercises 1 to 6.
$$
\begin{aligned}
& 5 x-y+4 z=5 \\
& 2 x+3 y+5 z=2 \\
& 5 x-2 y+6 z=-1
\end{aligned}
$$
:::

:::solution{label="Solution"}
Examine the consistency of the system of equations:

$$
\begin{aligned}
& 5 x-y+4 z=5 \\
& 2 x+3 y+5 z=2 \\
& 5 x-2 y+6 z=-1
\end{aligned}
$$

Solution:

$$
\begin{aligned}
& 5 x-y+4 z=5 \\
& 2 x+3 y+5 z=2
\end{aligned}
$$

The given system of equations is: $5 x-2 y+6 z=-1$
We can write the given system of equations in the form $A X=B$, where

$$
A=\left(\begin{array}{ccc}
5 & -1 & 4 \\
2 & 3 & 5 \\
5 & -2 & 6
\end{array}\right), X=\left[\begin{array}{l}
x \\
y \\
z
\end{array}\right] \text { and } B=\left[\begin{array}{c}
5 \\
2 \\
-1
\end{array}\right]
$$

Hence,

$$
\begin{aligned}
|A| & =5(18+10)+1(12-25)+4(-4-15) \\
& =5(28)+1(-13)+4(-19) \\
& =140-13-76 \\
& =51 \neq 0
\end{aligned}
$$

So, $A$ is nonsingular.

Therefore, $A^{-1}$ exists.
Hence, the given system of equations is consistent.
:::

:::

:::question{number="43" kind="exercise" id="q_4.43" topic="Solving a linear system by matrix method"}
#### Question 43

:::prompt
Solve system of linear equations, using matrix method, in Exercises 7 to 14.
$$
\begin{aligned}
& 5 x+2 y=4 \\
& 7 x+3 y=5
\end{aligned}
$$
:::

:::solution{label="Solution"}
Solve system of linear equations, using matrix method.

$$
\begin{aligned}
& 5 x+2 y=4 \\
& 7 x+3 y=5
\end{aligned}
$$

Solution:

$$
5 x+2 y=4
$$

The given system of equations is: $7 x+3 y=5$
We can write the given system of equations in the form $A X=B$, where

$$
A=\left(\begin{array}{ll}
5 & 2 \\
7 & 3
\end{array}\right), X=\left[\begin{array}{l}
x \\
y
\end{array}\right] \text { and } B=\left[\begin{array}{l}
4 \\
5
\end{array}\right]
$$

Hence,

$$
\begin{aligned}
|A| & =15-14 \\
& =1 \\
& \neq 0
\end{aligned}
$$

So, $A$ is non-singular.
Therefore, $A^{-1}$ exists.
Now,

$$
\begin{aligned}
A^{-1} & =\frac{1}{|A|}(\operatorname{adj} A) \\
& =\left(\begin{array}{cc}
3 & -2 \\
-7 & 5
\end{array}\right)
\end{aligned}
$$

Then,

$$
\begin{aligned}
& \Rightarrow X=A^{-1} B \\
& \Rightarrow\left[\begin{array}{l}
x \\
y
\end{array}\right]=\left(\begin{array}{cc}
3 & -2 \\
-7 & 5
\end{array}\right)\left[\begin{array}{l}
4 \\
5
\end{array}\right] \\
& \Rightarrow\left[\begin{array}{l}
x \\
y
\end{array}\right]=\left[\begin{array}{c}
12-10 \\
-28+25
\end{array}\right] \\
& \Rightarrow\left[\begin{array}{l}
x \\
y
\end{array}\right]=\left[\begin{array}{c}
2 \\
-3
\end{array}\right]
\end{aligned}
$$

Hence, $x=2$ and $y=-3$
:::

:::

:::question{number="44" kind="exercise" id="q_4.44" topic="Solving a linear system by matrix method"}
#### Question 44

:::prompt
Solve system of linear equations, using matrix method, in Exercises 7 to 14.
$$
\begin{aligned}
& 2 x-y=-2 \\
& 3 x+4 y=3
\end{aligned}
$$
:::

:::solution{label="Solution"}
Solve system of linear equations, using matrix method.

$$
\begin{aligned}
& 2 x-y=-2 \\
& 3 x+4 y=3
\end{aligned}
$$

Solution:

$$
2 x-y=-2
$$

The given system of equations is: $3 x+4 y=3$
We can write the given system of equations in the form $A X=B$, where

$$
A=\left(\begin{array}{cc}
2 & -1 \\
3 & 4
\end{array}\right), X=\left[\begin{array}{l}
x \\
y
\end{array}\right] \text { and } B=\left[\begin{array}{c}
-2 \\
3
\end{array}\right]
$$

Hence,

$$
\begin{aligned}
|A| & =8+3 \\
& =11 \\
& \neq 0
\end{aligned}
$$

So, $A$ is non-singular.
Therefore, $A^{-1}$ exists.
Now,

$$
\begin{aligned}
A^{-1} & =\frac{1}{|A|}(\operatorname{adj} A) \\
& =\frac{1}{11}\left(\begin{array}{cc}
4 & 1 \\
-3 & 2
\end{array}\right)
\end{aligned}
$$

Therefore,

$$
\begin{aligned}
& \Rightarrow X=A^{-1} B \\
& \Rightarrow\left[\begin{array}{l}
x \\
y
\end{array}\right]=\frac{1}{11}\left(\begin{array}{cc}
4 & 1 \\
-3 & 2
\end{array}\right)\left[\begin{array}{c}
-2 \\
3
\end{array}\right] \\
& \Rightarrow\left[\begin{array}{l}
x \\
y
\end{array}\right]=\frac{1}{11}\left[\begin{array}{c}
-8+3 \\
6+6
\end{array}\right] \\
& \Rightarrow\left[\begin{array}{l}
x \\
y
\end{array}\right]=\frac{1}{11}\left[\begin{array}{c}
-5 \\
12
\end{array}\right] \\
& \Rightarrow\left[\begin{array}{l}
x \\
y
\end{array}\right]=\left[\begin{array}{c}
\frac{-5}{11} \\
\frac{12}{11}
\end{array}\right]
\end{aligned}
$$

Hence, $x=\frac{-5}{11}$ and $y=\frac{12}{11}$
:::

:::

:::question{number="45" kind="exercise" id="q_4.45" topic="Solving a linear system by matrix method"}
#### Question 45

:::prompt
Solve system of linear equations, using matrix method, in Exercises 7 to 14.
$$
\begin{aligned}
& 4 x-3 y=3 \\
& 3 x-5 y=7
\end{aligned}
$$
:::

:::solution{label="Solution"}
Solve system of linear equations, using matrix method.

$$
\begin{aligned}
& 4 x-3 y=3 \\
& 3 x-5 y=7
\end{aligned}
$$

Solution:

$$
4 x-3 y=3
$$

The given system of equations is: $3 x-5 y=7$
We can write the given system of equations in the form $A X=B$, where

$$
A=\left(\begin{array}{ll}
4 & -3 \\
3 & -5
\end{array}\right), X=\left[\begin{array}{l}
x \\
y
\end{array}\right] \text { and } B=\left[\begin{array}{l}
3 \\
7
\end{array}\right]
$$

Hence,

$$
\begin{aligned}
|A| & =-20+9 \\
& =-11 \\
& \neq 0
\end{aligned}
$$

So, $A$ is nonsingular.

Therefore, $A^{-1}$ exists.

Now,

$$
\begin{aligned}
A^{-1} & =\frac{1}{|A|}(\operatorname{adj} A) \\
& =-\frac{1}{11}\left(\begin{array}{ll}
-5 & 3 \\
-3 & 4
\end{array}\right)=\frac{1}{11}\left(\begin{array}{ll}
5 & -3 \\
3 & -4
\end{array}\right)
\end{aligned}
$$

Therefore,

$$
\begin{aligned}
& \Rightarrow X=A^{-1} B \\
& \Rightarrow\left[\begin{array}{l}
x \\
y
\end{array}\right]=\frac{1}{11}\left(\begin{array}{ll}
5 & -3 \\
3 & -4
\end{array}\right)\left[\begin{array}{l}
3 \\
7
\end{array}\right] \\
& \Rightarrow\left[\begin{array}{l}
x \\
y
\end{array}\right]=\frac{1}{11}\left(\begin{array}{ll}
5 & -3 \\
3 & -4
\end{array}\right)\left[\begin{array}{l}
3 \\
7
\end{array}\right] \\
& \Rightarrow\left[\begin{array}{l}
x \\
y
\end{array}\right]=\frac{1}{11}\left[\begin{array}{c}
15-21 \\
9-28
\end{array}\right] \\
& \Rightarrow\left[\begin{array}{l}
x \\
y
\end{array}\right]=\frac{1}{11}\left[\begin{array}{c}
-6 \\
-19
\end{array}\right] \\
& \Rightarrow\left[\begin{array}{l}
x \\
y
\end{array}\right]=\left[\begin{array}{c}
\frac{-6}{11} \\
\frac{-19}{11}
\end{array}\right]
\end{aligned}
$$

Hence, $x=\frac{-6}{11}$ and $y=\frac{-19}{11}$
:::

:::

:::question{number="46" kind="exercise" id="q_4.46" topic="Solving a linear system by matrix method"}
#### Question 46

:::prompt
Solve system of linear equations, using matrix method, in Exercises 7 to 14.
$$
\begin{aligned}
& 5 x+2 y=3 \\
& 3 x+2 y=5
\end{aligned}
$$
:::

:::solution{label="Solution"}
Solve system of linear equations, using matrix method.

$$
\begin{aligned}
& 5 x+2 y=3 \\
& 3 x+2 y=5
\end{aligned}
$$

Solution:

$$
5 x+2 y=3
$$

The given system of equations is: $3 x+2 y=5$
We can write the given system of equations in the form $A X=B$, where

$$
A=\left(\begin{array}{ll}
5 & 2 \\
3 & 2
\end{array}\right), X=\left[\begin{array}{l}
x \\
y
\end{array}\right] \text { and } B=\left[\begin{array}{l}
3 \\
5
\end{array}\right]
$$

Hence,

$$
\begin{aligned}
|A| & =10-6 \\
& =4 \\
& \neq 0
\end{aligned}
$$

So, $A$ is non-singular.
Therefore, $A^{-1}$ exists.
Now,

$$
\begin{aligned}
A^{-1} & =\frac{1}{|A|}(\operatorname{adj} A) \\
& =\frac{1}{4}\left(\begin{array}{cc}
2 & -2 \\
-3 & 5
\end{array}\right)
\end{aligned}
$$

Therefore,

$$
\begin{aligned}
& \Rightarrow X=A^{-1} B \\
& \Rightarrow\left[\begin{array}{l}
x \\
y
\end{array}\right]=\frac{1}{4}\left(\begin{array}{cc}
2 & -2 \\
-3 & 5
\end{array}\right)\left[\begin{array}{l}
3 \\
5
\end{array}\right] \\
& \Rightarrow\left[\begin{array}{l}
x \\
y
\end{array}\right]=\frac{1}{4}\left(\begin{array}{cc}
2 & -2 \\
-3 & 5
\end{array}\right)\left[\begin{array}{l}
3 \\
5
\end{array}\right] \\
& \Rightarrow\left[\begin{array}{l}
x \\
y
\end{array}\right]=\frac{1}{4}\left[\begin{array}{c}
6-10 \\
-9+25
\end{array}\right] \\
& \Rightarrow\left[\begin{array}{l}
x \\
y
\end{array}\right]=\frac{1}{4}\left[\begin{array}{c}
-4 \\
16
\end{array}\right] \\
& \Rightarrow\left[\begin{array}{l}
x \\
y
\end{array}\right]=\left[\begin{array}{c}
-1 \\
4
\end{array}\right]
\end{aligned}
$$

Hence, $x=-1$ and $y=4$
:::

:::

:::question{number="47" kind="exercise" id="q_4.47" topic="Solving a 3-variable linear system by matrix method"}
#### Question 47

:::prompt
Solve system of linear equations, using matrix method, in Exercises 7 to 14.
$$
\begin{gathered}
2 x+y+z=1 \\
x-2 y-z=\frac{3}{2} \\
3 y-5 z=9
\end{gathered}
$$
:::

:::solution{label="Solution"}
Solve system of linear equations, using matrix method.

$$
\begin{aligned}
& 2 x+y+z=1 \\
& x-2 y-z=\frac{3}{2} \\
& 3 y-5 z=9
\end{aligned}
$$

Solution:

$$
\begin{aligned}
& 2 x+y+z=1 \\
& x-2 y-z=\frac{3}{2}
\end{aligned}
$$

The given system of equations is: $3 y-5 z=9$
We can write the given system of equations in the form $A X=B$, where

$$
A=\left(\begin{array}{ccc}
2 & 1 & 1 \\
1 & -2 & -1 \\
0 & 3 & -5
\end{array}\right), X=\left[\begin{array}{c}
x \\
y \\
z
\end{array}\right] \text { and } B=\left[\begin{array}{c}
1 \\
\frac{3}{2} \\
9
\end{array}\right]
$$

Hence,

$$
\begin{aligned}
|A| & =2(10+3)-1(-5-3)+0 \\
& =2(13)-1(-8) \\
& =26+8 \\
& =34 \\
& \neq 0
\end{aligned}
$$

So, $A$ is non-singular.
Therefore, $A^{-1}$ exists.
Now,

$$
\begin{array}{lll}
A_{11}=13 & A_{12}=5 & A_{13}=3 \\
A_{21}=8 & A_{22}=-10 & A_{23}=-6 \\
a_{31}=1 & A_{32}=3 & A_{33}=-5
\end{array}
$$

Hence,

$$
\begin{aligned}
A^{-1} & =\frac{1}{|A|}(\operatorname{adj} A) \\
& =\frac{1}{34}\left(\begin{array}{ccc}
13 & 8 & 1 \\
5 & -10 & 3 \\
3 & -6 & -5
\end{array}\right)
\end{aligned}
$$

Therefore,

$$
\begin{aligned}
& \Rightarrow X=A^{-1} B \\
& \Rightarrow\left[\begin{array}{l}
x \\
y \\
z
\end{array}\right]=\frac{1}{34}\left(\begin{array}{ccc}
13 & 8 & 1 \\
5 & -10 & 3 \\
3 & -6 & -5
\end{array}\right)\left[\begin{array}{l}
1 \\
\frac{3}{2} \\
9
\end{array}\right] \\
& \Rightarrow\left[\begin{array}{l}
x \\
y \\
z
\end{array}\right]=\frac{1}{34}\left(\begin{array}{ccc}
13 & 8 & 1 \\
5 & -10 & 3 \\
3 & -6 & -5
\end{array}\right)\left[\begin{array}{l}
1 \\
\frac{3}{2} \\
9
\end{array}\right] \\
& \Rightarrow\left[\begin{array}{l}
x \\
y \\
z
\end{array}\right]=\frac{1}{34}\left[\begin{array}{c}
13+12+9 \\
5-15+27 \\
3-9-45
\end{array}\right] \\
& \Rightarrow\left[\begin{array}{l}
x \\
y \\
z
\end{array}\right]=\frac{1}{34}\left[\begin{array}{c}
34 \\
17 \\
-51
\end{array}\right] \\
& \Rightarrow\left[\begin{array}{l}
x \\
y \\
z
\end{array}\right]=\left[\begin{array}{c}
1 \\
\frac{1}{2} \\
-\frac{3}{2}
\end{array}\right]
\end{aligned}
$$

Hence, $x=1, y=\frac{1}{2}$ and $z=\frac{-3}{2}$
:::

:::

:::question{number="48" kind="exercise" id="q_4.48" topic="Solving a 3-variable linear system by matrix method"}
#### Question 48

:::prompt
Solve system of linear equations, using matrix method, in Exercises 7 to 14.
$$
\begin{gathered}
x-y+z=4 \\
2 x+y-3 z=0 \\
x+y+z=2
\end{gathered}
$$
:::

:::solution{label="Solution"}
Solve system of linear equations, using matrix method.

$$
\begin{aligned}
& x-y+z=4 \\
& 2 x+y-3 z=0 \\
& x+y+z=2
\end{aligned}
$$

Solution:

$$
\begin{aligned}
& x-y+z=4 \\
& 2 x+y-3 z=0
\end{aligned}
$$

The given system of equations is: $x+y+z=2$
We can write the given system of equations in the form $A X=B$, where $A=\left(\begin{array}{ccc}1 & -1 & 1 \\ 2 & 1 & -3 \\ 1 & 1 & 1\end{array}\right), X=\left[\begin{array}{l}x \\ y \\ z\end{array}\right]$ and $B=\left[\begin{array}{l}4 \\ 0 \\ 2\end{array}\right]$

Hence,

$$
\begin{aligned}
|A| & =1(1+3)+1(2+3)+1(2-1) \\
& =4+5+1 \\
& =10 \\
& \neq 0
\end{aligned}
$$

So, $A$ is nonsingular.
Therefore, $A^{-1}$ exists.
Now,

$$
\begin{array}{lll}
A_{11}=4 & A_{12}=-5 & A_{13}=1 \\
A_{21}=2 & A_{22}=0 & A_{23}=-2 \\
a_{31}=2 & A_{32}=5 & A_{33}=3
\end{array}
$$

Hence,

$$
\begin{aligned}
A^{-1} & =\frac{1}{|A|}(\operatorname{adj} A) \\
& =\frac{1}{10}\left(\begin{array}{ccc}
4 & 2 & 2 \\
-5 & 0 & 5 \\
1 & -2 & 3
\end{array}\right)
\end{aligned}
$$

Therefore,

$$
\begin{aligned}
& \Rightarrow X=A^{-1} B \\
& \Rightarrow\left[\begin{array}{l}
x \\
y \\
z
\end{array}\right]=\frac{1}{10}\left(\begin{array}{ccc}
4 & 2 & 2 \\
-5 & 0 & 5 \\
1 & -2 & 3
\end{array}\right)\left[\begin{array}{l}
4 \\
0 \\
2
\end{array}\right] \\
& \Rightarrow\left[\begin{array}{l}
x \\
y \\
z
\end{array}\right]=\frac{1}{10}\left(\begin{array}{ccc}
4 & 2 & 2 \\
-5 & 0 & 5 \\
1 & -2 & 3
\end{array}\right)\left[\begin{array}{l}
4 \\
0 \\
2
\end{array}\right] \\
& \Rightarrow\left[\begin{array}{l}
x \\
y \\
z
\end{array}\right]=\frac{1}{10}\left[\begin{array}{c}
16+0+4 \\
-20+0+10 \\
4+0+6
\end{array}\right] \\
& \Rightarrow\left[\begin{array}{l}
x \\
y \\
z
\end{array}\right]=\frac{1}{10}\left[\begin{array}{c}
20 \\
-10 \\
10
\end{array}\right] \\
& \Rightarrow\left[\begin{array}{l}
x \\
y \\
z
\end{array}\right]=\left[\begin{array}{c}
2 \\
-1 \\
1
\end{array}\right]
\end{aligned}
$$

Hence, $x=2, y=-1$ and $z=1$
:::

:::

:::question{number="49" kind="exercise" id="q_4.49" topic="Solving a 3-variable linear system by matrix method"}
#### Question 49

:::prompt
Solve system of linear equations, using matrix method, in Exercises 7 to 14.
$$
\begin{aligned}
& 2 x+3 y+3 z=5 \\
& x-2 y+z=-4 \\
& 3 x-y-2 z=3
\end{aligned}
$$
:::

:::solution{label="Solution"}
Solve system of linear equations, using matrix method.

$$
\begin{aligned}
& 2 x+3 y+3 z=5 \\
& x-2 y+z=-4 \\
& 3 x-y-2 z=3
\end{aligned}
$$

Solution:

$$
\begin{aligned}
& 2 x+3 y+3 z=5 \\
& x-2 y+z=-4
\end{aligned}
$$

The given system of equations is: $3 x-y-2 z=3$
We can write the given system of equations in the form $A X=B$, where

$$
A=\left(\begin{array}{ccc}
2 & 3 & 3 \\
1 & -2 & 1 \\
3 & -1 & -2
\end{array}\right), X=\left[\begin{array}{l}
x \\
y \\
z
\end{array}\right] \text { and } B=\left[\begin{array}{c}
5 \\
-4 \\
3
\end{array}\right]
$$

Hence,

$$
\begin{aligned}
|A| & =2(4+1)-3(-2-3)+3(-1+6) \\
& =10+15+15 \\
& =40 \\
& \neq 0
\end{aligned}
$$

So, $A$ is non-singular.
Therefore, $A^{-1}$ exists.
Now,

$$
\begin{array}{lll}
A_{11}=5 & A_{12}=5 & A_{13}=5 \\
A_{21}=3 & A_{22}=-13 & A_{23}=11 \\
A_{31}=9 & A_{32}=1 & A_{33}=-7
\end{array}
$$

Hence,

$$
\begin{aligned}
A^{-1} & =\frac{1}{|A|}(\operatorname{adj} A) \\
& =\frac{1}{40}\left(\begin{array}{ccc}
5 & 3 & 9 \\
5 & -13 & 1 \\
5 & 11 & -7
\end{array}\right)
\end{aligned}
$$

Therefore,

$$
\begin{aligned}
& \Rightarrow X=A^{-1} B \\
& \Rightarrow\left[\begin{array}{l}
x \\
y \\
z
\end{array}\right]=\frac{1}{40}\left(\begin{array}{ccc}
5 & 3 & 9 \\
5 & -13 & 1 \\
5 & 11 & -7
\end{array}\right)\left[\begin{array}{c}
5 \\
-4 \\
3
\end{array}\right] \\
& \Rightarrow\left[\begin{array}{l}
x \\
y \\
z
\end{array}\right]=\frac{1}{40}\left(\begin{array}{ccc}
5 & 3 & 9 \\
5 & -13 & 1 \\
5 & 11 & -7
\end{array}\right)\left[\begin{array}{c}
5 \\
-4 \\
3
\end{array}\right] \\
& \Rightarrow\left[\begin{array}{l}
x \\
y \\
z
\end{array}\right]=\frac{1}{40}\left[\begin{array}{ccc}
25-12+27 \\
25+52+3 \\
25-44-21
\end{array}\right] \\
& \Rightarrow\left[\begin{array}{l}
x \\
y \\
z
\end{array}\right]=\frac{1}{40}\left[\begin{array}{c}
40 \\
80 \\
-40
\end{array}\right] \\
& \Rightarrow\left[\begin{array}{l}
x \\
y \\
z
\end{array}\right]=\left[\begin{array}{c}
1 \\
2 \\
-1
\end{array}\right]
\end{aligned}
$$

Hence, $x=1, y=2$ and $z=-1$
:::

:::

:::question{number="50" kind="exercise" id="q_4.50" topic="Solving a 3-variable linear system by matrix method"}
#### Question 50

:::prompt
Solve system of linear equations, using matrix method, in Exercises 7 to 14.
$$
\begin{aligned}
& x-y+2 z=7 \\
& 3 x+4 y-5 z=-5 \\
& 2 x-y+3 z=12
\end{aligned}
$$
:::

:::solution{label="Solution"}
Solve system of linear equations, using matrix method.

$$
\begin{aligned}
& x-y+2 z=7 \\
& 3 x+4 y-5 z=-5 \\
& 2 x-y+3 z=12
\end{aligned}
$$

Solution:

$$
\begin{aligned}
& x-y+2 z=7 \\
& 3 x+4 y-5 z=-5
\end{aligned}
$$

The given system of equations is: $2 x-y+3 z=12$
We can write the given system of equations in the form $A X=B$, where

$$
A=\left(\begin{array}{ccc}
1 & -1 & 2 \\
3 & 4 & -5 \\
2 & -1 & 3
\end{array}\right), X=\left[\begin{array}{l}
x \\
y \\
z
\end{array}\right] \text { and } B=\left[\begin{array}{c}
7 \\
-5 \\
12
\end{array}\right]
$$

Hence,

$$
\begin{aligned}
|A| & =1(12-5)+1(9+10)+2(-3-8) \\
& =7+19-22 \\
& =4 \\
& \neq 0
\end{aligned}
$$

So, $A$ is non-singular.
Therefore, $A^{-1}$ exists.
Now,

$$
\begin{array}{lll}
A_{11}=7 & A_{12}=-19 & A_{13}=-11 \\
A_{21}=1 & A_{22}=-1 & A_{23}=-1 \\
a_{31}=-3 & A_{32}=11 & A_{33}=7
\end{array}
$$

Hence,

$$
\begin{aligned}
A^{-1} & =\frac{1}{|A|}(\operatorname{adj} A) \\
& =\frac{1}{4}\left(\begin{array}{ccc}
7 & 1 & -3 \\
-19 & -1 & 11 \\
-11 & -1 & 7
\end{array}\right)
\end{aligned}
$$

Therefore,

$$
\begin{aligned}
& \Rightarrow X=A^{-1} B \\
& \Rightarrow\left[\begin{array}{l}
x \\
y \\
z
\end{array}\right]=\frac{1}{4}\left(\begin{array}{ccc}
7 & 1 & -3 \\
-19 & -1 & 11 \\
-11 & -1 & 7
\end{array}\right)\left[\begin{array}{c}
7 \\
-5 \\
12
\end{array}\right] \\
& \Rightarrow\left[\begin{array}{l}
x \\
y \\
z
\end{array}\right]=\frac{1}{4}\left(\begin{array}{ccc}
7 & 1 & -3 \\
-19 & -1 & 11 \\
-11 & -1 & 7
\end{array}\right)\left[\begin{array}{c}
7 \\
-5 \\
12
\end{array}\right] \\
& \Rightarrow\left[\begin{array}{l}
x \\
y \\
z
\end{array}\right]=\frac{1}{4}\left[\begin{array}{c}
49-5-36 \\
-133+5+132 \\
-77+5+84
\end{array}\right] \\
& \Rightarrow\left[\begin{array}{l}
x \\
y \\
z
\end{array}\right]=\frac{1}{4}\left[\begin{array}{c}
49-5-36 \\
-133+5+132 \\
-77+5+84
\end{array}\right] \\
& \Rightarrow\left[\begin{array}{l}
x \\
y \\
z
\end{array}\right]=\frac{1}{4}\left[\begin{array}{c}
8 \\
4 \\
12
\end{array}\right] \\
& \Rightarrow\left[\begin{array}{l}
x \\
y \\
z
\end{array}\right]=\left[\begin{array}{c}
2 \\
1 \\
3
\end{array}\right]
\end{aligned}
$$

Hence, $x=2, y=1$ and $z=3$
:::

:::

:::question{number="51" kind="exercise" id="q_4.51" topic="Solving a system using a given inverse matrix"}
#### Question 51

:::prompt
If $\mathrm{A}=\left[\begin{array}{rrr}2 & -3 & 5 \\ 3 & 2 & -4 \\ 1 & 1 & -2\end{array}\right]$, find $\mathrm{A}^{-1}$. Using $\mathrm{A}^{-1}$ solve the system of equations
$$
\begin{aligned}
2 x-3 y+5 z & =11 \\
3 x+2 y-4 z & =-5 \\
x+y-2 z & =-3
\end{aligned}
$$
:::

:::solution{label="Solution"}
$$
A=\left(\begin{array}{ccc}
2 & -3 & 5 \\
3 & 2 & -4 \\
1 & 1 & -2
\end{array}\right) \text {, find } A^{-1} \text {. Using } A^{-1} \text { solve the system of equations }
$$

$$
\begin{aligned}
& 2 x-3 y+5 z=11 \\
& 3 x+2 y-4 z=-5 \\
& x+y-2 z=-3
\end{aligned}
$$

Solution:
It is given that

$$
A=\left(\begin{array}{ccc}
2 & -3 & 5 \\
3 & 2 & -4 \\
1 & 1 & -2
\end{array}\right)
$$

Therefore,

$$
\begin{aligned}
|A| & =2(-4+4)+3(-6+4)+5(3-2) \\
& =0-6+5 \\
& =-1 \\
& \neq 0
\end{aligned}
$$

Now,

$$
\begin{array}{lll}
A_{11}=0 & A_{12}=2 & A_{13}=1 \\
A_{21}=-1 & A_{22}=-9 & A_{23}=-5 \\
a_{31}=2 & A_{32}=23 & A_{33}=13
\end{array}
$$

Hence,

$$
\begin{aligned}
A^{-1} & =\frac{1}{|A|}(\operatorname{adj} A) \\
& =-\left(\begin{array}{ccc}
0 & -1 & 2 \\
2 & -9 & 23 \\
1 & -5 & 13
\end{array}\right)=\left(\begin{array}{ccc}
0 & 1 & -2 \\
-2 & 9 & -23 \\
-1 & 5 & -13
\end{array}\right)
\end{aligned}
$$

We can write the given system of equations in the form $A X=B$, where

$$
A=\left(\begin{array}{ccc}
2 & -3 & 5 \\
3 & 2 & -4 \\
1 & 1 & -2
\end{array}\right), X=\left[\begin{array}{l}
x \\
y \\
z
\end{array}\right] \text { and } B=\left[\begin{array}{c}
11 \\
-5 \\
-3
\end{array}\right]
$$

The solution of the system of equations is $X=A^{-1} B$.
Therefore,

$$
\begin{aligned}
& \Rightarrow X=A^{-1} B \\
& \Rightarrow\left[\begin{array}{l}
x \\
y \\
z
\end{array}\right]=\left(\begin{array}{ccc}
0 & 1 & -2 \\
-2 & 9 & -23 \\
-1 & 5 & -13
\end{array}\right)\left[\begin{array}{l}
11 \\
-5 \\
-3
\end{array}\right] \\
& \Rightarrow\left[\begin{array}{l}
x \\
y \\
z
\end{array}\right]=\left(\begin{array}{ccc}
0 & 1 & -2 \\
-2 & 9 & -23 \\
-1 & 5 & -13
\end{array}\right)\left[\begin{array}{l}
11 \\
-5 \\
-3
\end{array}\right] \\
& \Rightarrow\left[\begin{array}{l}
x \\
y \\
z
\end{array}\right]=\left[\begin{array}{c}
0-5+6 \\
-22-45+69 \\
-11-25+39
\end{array}\right] \\
& \Rightarrow\left[\begin{array}{l}
x \\
y \\
z
\end{array}\right]=\left[\begin{array}{l}
1 \\
2 \\
3
\end{array}\right]
\end{aligned}
$$

Hence, $x=1, y=2$ and $z=3$
:::

:::

:::question{number="52" kind="exercise" id="q_4.52" topic="Word problem - cost per kg via matrix method"}
#### Question 52

:::prompt
The cost of 4 kg onion, 3 kg wheat and 2 kg rice is ₹ 60 . The cost of 2 kg onion, 4 kg wheat and 6 kg rice is ₹ 90 . The cost of 6 kg onion 2 kg wheat and 3 kg rice is ₹ 70. Find cost of each item per kg by matrix method.
:::

:::solution{label="Solution"}
The cost of 4 kg onion, 3 kg wheat and 2 kg rice is $₹ 60$. The cost of 2 kg onion, 4 kg wheat and 6 kg rice is ₹ 90 . The cost of 6 kg onion 2 kg wheat and 3 kg rice is ₹ 70 . Find cost of each item per kg by matrix method.

Solution:
Let the cost of onions, wheat, and rice per kg in ₹ be $x, y$ and $z$ respectively.
We can write this situation as a system of equations:

$$
\begin{aligned}
& 4 x+3 y+2 z=60 \\
& 2 x+4 y+6 z=90 \\
& 6 x+2 y+3 z=70
\end{aligned}
$$

We can write the given system of equations in the form $A X=B$, where

$$
A=\left(\begin{array}{lll}
4 & 3 & 2 \\
2 & 4 & 6 \\
6 & 2 & 3
\end{array}\right), X=\left[\begin{array}{l}
x \\
y \\
z
\end{array}\right] \text { and } B=\left[\begin{array}{l}
60 \\
90 \\
70
\end{array}\right]
$$

Therefore,

$$
\begin{aligned}
|A| & =4(12-12)-3(6-36)+2(4-24) \\
& =0+90-40 \\
& =50 \\
& \neq 0
\end{aligned}
$$

So, $A$ is non-singular.
Therefore, $A^{-1}$ exists.
Now,

$$
\begin{array}{lll}
A_{11}=0 & A_{12}=30 & A_{13}=-20 \\
A_{21}=-5 & A_{22}=0 & A_{23}=10 \\
A_{31}=10 & A_{32}=-20 & A_{33}=10
\end{array}
$$

Therefore,

$$
\begin{aligned}
A^{-1} & =\frac{1}{|A|}(\operatorname{adj} A) \\
& =\frac{1}{50}\left(\begin{array}{ccc}
0 & -5 & 10 \\
30 & 0 & -20 \\
-20 & 10 & 10
\end{array}\right)
\end{aligned}
$$

Hence,

$$
\begin{aligned}
& \Rightarrow X=A^{-1} B \\
& \Rightarrow\left[\begin{array}{l}
x \\
y \\
z
\end{array}\right]=\frac{1}{50}\left(\begin{array}{ccc}
0 & -5 & 10 \\
30 & 0 & -20 \\
-20 & 10 & 10
\end{array}\right)\left[\begin{array}{l}
60 \\
90 \\
70
\end{array}\right] \\
& \Rightarrow\left[\begin{array}{l}
x \\
y \\
z
\end{array}\right]=\frac{1}{50}\left(\begin{array}{ccc}
0 & -5 & 10 \\
30 & 0 & -20 \\
-20 & 10 & 10
\end{array}\right)\left[\begin{array}{l}
60 \\
90 \\
70
\end{array}\right] \\
& \Rightarrow\left[\begin{array}{l}
x \\
y \\
z
\end{array}\right]=\frac{1}{50}\left[\begin{array}{c}
0-450+700 \\
1800+0-1400 \\
-1200+900+700
\end{array}\right] \\
& \Rightarrow\left[\begin{array}{l}
x \\
y \\
z
\end{array}\right]=\frac{1}{50}\left[\begin{array}{c}
250 \\
400 \\
400
\end{array}\right] \\
& \Rightarrow\left[\begin{array}{l}
x \\
y \\
z
\end{array}\right]=\left[\begin{array}{l}
5 \\
8 \\
8
\end{array}\right]
\end{aligned}
$$

Thus, $x=5, y=8$ and $z=8$
Hence, the cost of onions is ₹ 5 per kg the cost of wheat is ₹ 8 per kg, and the cost of rice is ₹ 8 per kg.
:::

:::

:::question{number="53" kind="exercise" id="q_4.53" topic="Determinant independent of theta"}
#### Question 53

:::prompt
Prove that the determinant $\left|\begin{array}{ccc}x & \sin \theta & \cos \theta \\ -\sin \theta & -x & 1 \\ \cos \theta & 1 & x\end{array}\right|$ is independent of $\theta$.
:::

:::solution{label="Solution"}
Prove that the determinant $\left|\begin{array}{ccc}x & \sin \theta & \cos \theta \\ -\sin \theta & -x & 1 \\ \cos \theta & 1 & x\end{array}\right|$ is independent of $\theta$.
Solution:

$$
\begin{aligned}
\Delta & =\left|\begin{array}{ccc}
x & \sin \theta & \cos \theta \\
-\sin \theta & -x & 1 \\
\cos \theta & 1 & x
\end{array}\right| \\
& =x\left(-x^{2}-1\right)-\sin \theta(-x \sin \theta-\cos \theta)+\cos \theta(-\sin \theta+x \cos \theta) \\
& =-x^{3}-x+x \sin ^{2} \theta+\sin \theta \cos \theta-\sin \theta \cos \theta+x \cos ^{2} \theta \\
& =-x^{3}-x+x\left(\sin ^{2} \theta+\cos ^{2} \theta\right) \\
& =-x^{3}-x+x \\
& =-x^{3}
\end{aligned}
$$

Hence, $\Delta$ is independent of $\theta$.
:::

:::

:::question{number="54" kind="exercise" id="q_4.54" topic="Evaluating a determinant with trig entries"}
#### Question 54

:::prompt
Evaluate $\left|\begin{array}{ccc}\cos \alpha \cos \beta & \cos \alpha \sin \beta & -\sin \alpha \\ -\sin \beta & \cos \beta & 0 \\ \sin \alpha \cos \beta & \sin \alpha \sin \beta & \cos \alpha\end{array}\right|$.
:::

:::solution{label="Solution"}
Evaluate $\left|\begin{array}{ccc}\cos \alpha \cos \beta & \cos \alpha \sin \beta & -\sin \alpha \\ -\sin \beta & \cos \beta & 0 \\ \sin \alpha \cos \beta & \sin \alpha \sin \beta & \cos \alpha\end{array}\right|$.

Solution:

Let

$$
\Delta=\left|\begin{array}{ccc}
\cos \alpha \cos \beta & \cos \alpha \sin \beta & -\sin \alpha \\
-\sin \beta & \cos \beta & 0 \\
\sin \alpha \cos \beta & \sin \alpha \sin \beta & \cos \alpha
\end{array}\right|
$$

Expanding along $C_{3}$,

$$
\begin{aligned}
\Delta & =-\sin \alpha\left(-\sin \alpha \sin ^{2} \beta-\cos ^{2} \beta \sin \alpha\right)+\cos \alpha\left(\cos \alpha \cos ^{2} \beta+\cos \alpha \sin ^{2} \beta\right) \\
& =\sin ^{2} \alpha\left(\sin ^{2} \beta+\cos ^{2} \beta\right)+\cos ^{2} \alpha\left(\cos ^{2} \beta+\sin ^{2} \beta\right) \\
& =\sin ^{2} \alpha(1)+\cos ^{2} \alpha(1) \\
& =1
\end{aligned}
$$
:::

:::

:::question{number="55" kind="exercise" id="q_4.55" topic="Finding (AB)^-1 from A^-1 and B"}
#### Question 55

:::prompt
If $\mathrm{A}^{-1}=\left[\begin{array}{ccc}3 & -1 & 1 \\ -15 & 6 & -5 \\ 5 & -2 & 2\end{array}\right]$ and $\mathrm{B}=\left[\begin{array}{ccc}1 & 2 & -2 \\ -1 & 3 & 0 \\ 0 & -2 & 1\end{array}\right]$, find $(\mathrm{AB})^{-1}$
:::

:::solution{label="Solution"}
$$
A^{-1}=\left|\begin{array}{ccc}
3 & -1 & 1 \\
-15 & 6 & -5 \\
5 & -2 & 2
\end{array}\right| \text { and } B=\left|\begin{array}{ccc}
1 & 2 & -2 \\
-1 & 3 & 0 \\
0 & -2 & 1
\end{array}\right| \text {, find }(A B)^{-1} .
$$

Solution:
We know that $(A B)^{-1}=B^{-1} A^{-1}$.

It is given that

$$
B=\left|\begin{array}{ccc}
1 & 2 & -2 \\
-1 & 3 & 0 \\
0 & -2 & 1
\end{array}\right|
$$

Therefore,

$$
\begin{aligned}
|B| & =1(3)-2(-1)-2(-2) \\
& =3+2-4 \\
& =5-4 \\
& =1
\end{aligned}
$$

Now,

$$
\begin{array}{lll}
B_{11}=3 & B_{12}=1 & B_{13}=2 \\
B_{21}=2 & B_{22}=1 & B_{23}=2 \\
B_{31}=6 & B_{32}=2 & B_{33}=5
\end{array}
$$

Hence,

$$
\operatorname{adj} B=\left(\begin{array}{lll}
3 & 2 & 6 \\
1 & 1 & 2 \\
2 & 2 & 5
\end{array}\right)
$$

Now,

$$
\begin{aligned}
B^{-1} & =\frac{1}{|B|} \operatorname{adj} B \\
& =\left(\begin{array}{lll}
3 & 2 & 6 \\
1 & 1 & 2 \\
2 & 2 & 5
\end{array}\right)
\end{aligned}
$$

Therefore,

$$
\begin{aligned}
(A B)^{-1} & =B^{-1} A^{-1} \\
& =\left(\begin{array}{lll}
3 & 2 & 6 \\
1 & 1 & 2 \\
2 & 2 & 5
\end{array}\right)\left(\begin{array}{ccc}
3 & -1 & 1 \\
-15 & 6 & -5 \\
5 & -2 & 2
\end{array}\right) \\
& =\left(\begin{array}{ccc}
9-30+30 & -3+12-12 & 3-10+12 \\
3-15+10 & -1+6-4 & 1-5+4 \\
6-30+25 & -2+12-10 & 2-10+10
\end{array}\right) \\
& =\left(\begin{array}{ccc}
9 & -3 & 5 \\
-2 & 1 & 0 \\
1 & 0 & 2
\end{array}\right)
\end{aligned}
$$

Thus,

$$
(A B)^{-1}=\left(\begin{array}{ccc}
9 & -3 & 5 \\
-2 & 1 & 0 \\
1 & 0 & 2
\end{array}\right) .
$$
:::

:::

:::question{number="56" kind="exercise" id="q_4.56" topic="Verifying adjoint/inverse identities"}
#### Question 56

:::prompt
Let $\mathrm{A}=\left[\begin{array}{ccc}1 & 2 & 1 \\ 2 & 3 & 1 \\ 1 & 1 & 5\end{array}\right]$. Verify that
:::

:::part{label="(i)"}
:::prompt
[adj
$\mathrm{A}]^{-1}=a d j$
$\left(\mathrm{A}^{-1}\right)$
:::

:::

:::part{label="(ii)"}
:::prompt
$\left(\mathrm{A}^{-1}\right)^{-1}=\mathrm{A}$
:::

:::

:::solution{label="Solution"}
$$
A=\left(\begin{array}{ccc}
1 & -2 & 1 \\
-2 & 3 & 1 \\
1 & 1 & 5
\end{array}\right) \text { verify that }
$$

(i) $[\operatorname{adj} A]^{-1}=\operatorname{adj}(A)^{-1}$
(ii) $\left(A^{-1}\right)^{-1}=A$

Solution:

$$
A=\left(\begin{array}{ccc}
1 & -2 & 1 \\
-2 & 3 & 1 \\
1 & 1 & 5
\end{array}\right)
$$

Therefore,

$$
\begin{aligned}
|A| & =1(15-1)+2(-10-1)+1(-2-3) \\
& =14-22-5 \\
& =-13
\end{aligned}
$$

Now,

$$
\begin{array}{lll}
A_{11}=14 & A_{12}=11 & A_{13}=-5 \\
A_{21}=11 & A_{22}=4 & A_{23}=-3 \\
A_{31}=-5 & A_{32}=-3 & A_{33}=-1
\end{array}
$$

Hence,

$$
\operatorname{adj} A=\left(\begin{array}{ccc}
14 & 11 & -5 \\
11 & 4 & -3 \\
-5 & -3 & -1
\end{array}\right)
$$

Now,

$$
\begin{aligned}
A^{-1} & =\frac{1}{|A|}(\operatorname{adj} A) \\
& =-\frac{1}{13}\left(\begin{array}{ccc}
14 & 11 & -5 \\
11 & 4 & -3 \\
-5 & -3 & -1
\end{array}\right) \\
& =\frac{1}{13}\left(\begin{array}{ccc}
-14 & -11 & 5 \\
-11 & -4 & 3 \\
5 & 3 & 1
\end{array}\right)
\end{aligned}
$$

(i)

$$
\begin{aligned}
|\operatorname{adj} A| & =14(-4-9)-11(-11-15)-5(-33+20) \\
& =14(-13)-11(-26)-5(-13) \\
& =-182+286+65 \\
& =169
\end{aligned}
$$

We have,

$$
\operatorname{adj}(\operatorname{adj} A)=\left(\begin{array}{ccc}
-13 & 26 & -13 \\
26 & -39 & -13 \\
-13 & -13 & -65
\end{array}\right)
$$

Therefore,

$$
\begin{aligned}
{[\operatorname{adj} A]^{-1} } & =\frac{1}{|\operatorname{adj} A|}(\operatorname{adj}(\operatorname{adj} A)) \\
& =\frac{1}{169}\left(\begin{array}{ccc}
-13 & 26 & -13 \\
26 & -39 & -13 \\
-13 & -13 & -65
\end{array}\right) \\
& =\left(\begin{array}{ccc}
\frac{-1}{13} & \frac{2}{13} & \frac{-1}{13} \\
\frac{2}{13} & \frac{-3}{13} & \frac{-1}{13} \\
\frac{-1}{13} & \frac{-1}{13} & \frac{-5}{13}
\end{array}\right)
\end{aligned}
$$

Now,

$$
A^{-1}=-\frac{1}{13}\left(\begin{array}{ccc}
14 & 11 & -5 \\
11 & 4 & -3 \\
-5 & -3 & -1
\end{array}\right)=\left(\begin{array}{ccc}
\frac{-14}{13} & \frac{-11}{13} & \frac{5}{13} \\
\frac{-11}{13} & \frac{-4}{13} & \frac{3}{13} \\
\frac{5}{13} & \frac{3}{13} & \frac{1}{13}
\end{array}\right)
$$

Therefore,

$$
\begin{aligned}
\operatorname{adj}(A)^{-1} & =\left(\begin{array}{lll}
\frac{-13}{169} & \frac{26}{169} & \frac{-13}{169} \\
\frac{26}{169} & \frac{-39}{169} & \frac{-13}{169} \\
\frac{-13}{169} & \frac{-13}{169} & \frac{-65}{169}
\end{array}\right) \\
& =\left(\begin{array}{lll}
\frac{-1}{13} & \frac{2}{13} & \frac{-1}{13} \\
\frac{2}{13} & \frac{-3}{13} & \frac{-1}{13} \\
\frac{-1}{13} & \frac{-1}{13} & \frac{-5}{13}
\end{array}\right)
\end{aligned}
$$

Hence, $[\operatorname{adj} A]^{-1}=\operatorname{adj}(A)^{-1}$ proved.
(ii)

$$
A^{-1}=\frac{1}{13}\left(\begin{array}{ccc}
-14 & -11 & 5 \\
-11 & -4 & 3 \\
5 & 3 & 1
\end{array}\right)
$$

Hence,

$$
\operatorname{adj}(A)^{-1}=\left(\begin{array}{ccc}
\frac{-1}{13} & \frac{2}{13} & \frac{-1}{13} \\
\frac{2}{13} & \frac{-3}{13} & \frac{-1}{13} \\
\frac{-1}{13} & \frac{-1}{13} & \frac{-5}{13}
\end{array}\right)
$$

Now,

$$
\begin{aligned}
\left|A^{-1}\right| & =\left(\frac{1}{13}\right)^{3}[-14(-4-9)+11(-11-26)+5(-33+20)] \\
& =\left(\frac{1}{13}\right)^{3}[-169] \\
& =-\frac{1}{13}
\end{aligned}
$$

Therefore,

$$
\begin{aligned}
\left(A^{-1}\right)^{-1} & =\frac{\operatorname{adj} A^{-1}}{|A|}=\frac{1}{\left(-\frac{1}{13}\right)} \times\left(\begin{array}{ccc}
\frac{-1}{13} & \frac{2}{13} & \frac{-1}{13} \\
\frac{2}{13} & \frac{-3}{13} & \frac{-1}{13} \\
\frac{-1}{13} & \frac{-1}{13} & \frac{-5}{13}
\end{array}\right) \\
& =\left(\begin{array}{ccc}
1 & -2 & 1 \\
-2 & 3 & 1 \\
1 & 1 & 5
\end{array}\right)=A
\end{aligned}
$$

Hence, $\left(A^{-1}\right)^{-1}=A$ proved.
:::

:::

:::question{number="57" kind="exercise" id="q_4.57" topic="Evaluating a symmetric-sum determinant"}
#### Question 57

:::prompt
Evaluate $\left|\begin{array}{ccc}x & y & x+y \\ y & x+y & x \\ x+y & x & y\end{array}\right|$
:::

:::solution{label="Solution"}
Evaluate $\left|\begin{array}{ccc}x & y & x+y \\ y & x+y & x \\ x+y & x & y\end{array}\right|$.

Solution:

$$
\begin{array}{rlrl}
\Delta & =\left|\begin{array}{ccc}
x & y & x+y \\
y & x+y & x \\
x+y & x & y
\end{array}\right| & \\
& =\left|\begin{array}{ccc}
2(x+y) & 2(x+y) & 2(x+y) \\
y & x+y & x \\
x+y & x & y
\end{array}\right| & & {\left[R_{1} \rightarrow R_{1}+R_{2}+R_{3}\right]} \\
& =2(x+y)\left|\begin{array}{ccc}
1 & 1 & 1 \\
y & x+y & x \\
x+y & x & y
\end{array}\right| & & \\
& =2(x+y)\left|\begin{array}{ccc}
1 & 0 & 0 \\
y & x & x-y \\
x+y & -y & -x
\end{array}\right| & & {\left[C_{2} \rightarrow C_{2}-C_{1} \text { and } C_{3} \rightarrow C_{3}-C_{1}\right]} \\
& =2(x+y)\left[-x^{2}+y(x-y)\right] & & {\left[\text { Expanding along } R_{1}\right]} \\
& =-2(x+y)\left(x^{2}+y^{2}-y x\right) & & \\
& =-2\left(x^{3}+y^{3}\right) & &
\end{array}
$$
:::

:::

:::question{number="58" kind="exercise" id="q_4.58" topic="Evaluating a determinant with x, y entries" corrections_applied="1"}
#### Question 58

:::prompt
Evaluate $\left|\begin{array}{ccc}1 & x & y \\ 1 & x+y & y \\ 1 & x & x+y\end{array}\right|$
:::

:::solution{label="Solution"}
Evaluate $\left|\begin{array}{ccc}1 & x & y \\ 1 & x+y & y \\ 1 & x & x+y\end{array}\right|$.

## Solution:

$$
\begin{array}{rlr}
\Delta & =\left|\begin{array}{ccc}
1 & x & y \\
1 & x+y & y \\
1 & x & x+y
\end{array}\right| & \\
& =\left|\begin{array}{ccc}
1 & x & y \\
0 & y & 0 \\
0 & 0 & x
\end{array}\right| & \\
& =1(x y-0) & {\left[R_{2} \rightarrow R_{2}-R_{1} \text { and } R_{3} \rightarrow R_{3}-R_{1}\right]} \\
& =x y & {\left[\text { Expanding along } C_{1}\right]}
\end{array}
$$
:::

:::

:::question{number="59" kind="exercise" id="q_4.59" topic="Solving a system of reciprocal equations" corrections_applied="1"}
#### Question 59

:::prompt
Solve the system of equations
$$
\begin{aligned}
& \frac{2}{x}+\frac{3}{y}+\frac{10}{z}=4 \\
& \frac{4}{x}-\frac{6}{y}+\frac{5}{z}=1 \\
& \frac{6}{x}+\frac{9}{y}-\frac{20}{z}=2
\end{aligned}
$$
Choose the correct answer in Exercise 17 to 19 .
:::

:::solution{label="Solution"}
Solve the system of the following equations:

$$
\begin{aligned}
& \frac{2}{x}+\frac{3}{y}+\frac{10}{z}=4 \\
& \frac{4}{x}-\frac{6}{y}+\frac{5}{z}=1 \\
& \frac{6}{x}+\frac{9}{y}-\frac{20}{z}=2
\end{aligned}
$$

Solution:
Let $\frac{1}{x}=p, \frac{1}{y}=q$ and $\frac{1}{z}=r$.
Then the given system of equations is as follows:

$$
\begin{aligned}
& 2 p+3 q+10 r=4 \\
& 4 p-6 q+5 r=1 \\
& 6 p+9 q-20 r=2
\end{aligned}
$$

This system can be written in the form of $A X=B$, where

$$
A=\left(\begin{array}{ccc}
2 & 3 & 10 \\
4 & -6 & 5 \\
6 & 9 & -20
\end{array}\right), X=\left[\begin{array}{c}
p \\
q \\
r
\end{array}\right] \text { and } B=\left[\begin{array}{l}
4 \\
1 \\
2
\end{array}\right]
$$

Therefore,

$$
\begin{aligned}
|A| & =2(120-45)-3(-80-30)+10(36+36) \\
& =150+330+720 \\
& =1200
\end{aligned}
$$

Thus, $A$ is non-singular.
Therefore, $A^{-1}$ exists.
Now,

$$
\begin{array}{lll}
A_{11}=75 & A_{12}=110 & A_{13}=72 \\
A_{21}=150 & A_{22}=-100 & A_{23}=0 \\
A_{31}=75 & A_{32}=30 & A_{33}=-24
\end{array}
$$

Hence,

$$
\begin{aligned}
A^{-1} & =\frac{1}{|A|}(\operatorname{adj} A) \\
& =\frac{1}{1200}\left(\begin{array}{ccc}
75 & 150 & 75 \\
110 & -100 & 30 \\
72 & 0 & -24
\end{array}\right)
\end{aligned}
$$

Now,

$$
\begin{aligned}
& \Rightarrow X=A^{-1} B \\
& \Rightarrow\left[\begin{array}{l}
p \\
q \\
r
\end{array}\right]=\frac{1}{1200}\left(\begin{array}{ccc}
75 & 150 & 75 \\
110 & -100 & 30 \\
72 & 0 & -24
\end{array}\right)\left[\begin{array}{l}
4 \\
1 \\
2
\end{array}\right] \\
& \Rightarrow\left[\begin{array}{l}
p \\
q \\
r
\end{array}\right]=\frac{1}{1200}\left[\begin{array}{c}
300+150+150 \\
440-100+60 \\
288+0-48
\end{array}\right] \\
& \Rightarrow\left[\begin{array}{l}
p \\
q \\
r
\end{array}\right]=\frac{1}{1200}\left[\begin{array}{l}
600 \\
400 \\
240
\end{array}\right] \\
& \Rightarrow\left[\begin{array}{l}
p \\
q \\
r
\end{array}\right]=\left[\begin{array}{l}
\frac{1}{2} \\
\frac{1}{3} \\
\frac{1}{5}
\end{array}\right]
\end{aligned}
$$

Therefore,

$$
p=\frac{1}{2}, q=\frac{1}{3} \text { and } r=\frac{1}{5}
$$

Hence, $x=2, y=3$ and $z=5$.
:::

:::

:::question{number="60" kind="exercise" id="q_4.60" topic="MCQ - inverse of a diagonal matrix"}
#### Question 60

:::prompt
Choose the correct answer in Exercise 17 to 19.
If $x, y, z$ are nonzero real numbers, then the inverse of matrix $\mathrm{A}=\left[\begin{array}{ccc}x & 0 & 0 \\ 0 & y & 0 \\ 0 & 0 & z\end{array}\right]$ is
(A) $\left[\begin{array}{ccc}x^{-1} & 0 & 0 \\ 0 & y^{-1} & 0 \\ 0 & 0 & z^{-1}\end{array}\right]$
(B) $x y z\left[\begin{array}{ccc}x^{-1} & 0 & 0 \\ 0 & y^{-1} & 0 \\ 0 & 0 & z^{-1}\end{array}\right]$
(C) $\frac{1}{x y z}\left[\begin{array}{ccc}x & 0 & 0 \\ 0 & y & 0 \\ 0 & 0 & z\end{array}\right]$
(D) $\frac{1}{x y z}\left[\begin{array}{lll}1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1\end{array}\right]$
:::

:::solution{label="Solution"}
$$
A=\left(\begin{array}{lll}
x & 0 & 0 \\
0 & y & 0 \\
0 & 0 & z
\end{array}\right)_{\text {is }}
$$

(A) $\left(\begin{array}{ccc}x^{-1} & 0 & 0 \\ 0 & y^{-1} & 0 \\ 0 & 0 & z^{-1}\end{array}\right)$
(B) $x y z\left(\begin{array}{ccc}x^{-1} & 0 & 0 \\ 0 & y^{-1} & 0 \\ 0 & 0 & z^{-1}\end{array}\right)$
(C) $\frac{1}{x y z}\left(\begin{array}{lll}x & 0 & 0 \\ 0 & y & 0 \\ 0 & 0 & z\end{array}\right)$
(D) $\frac{1}{x y z}\left(\begin{array}{lll}1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1\end{array}\right)$

Solution:

It is given that

$$
A=\left(\begin{array}{lll}
x & 0 & 0 \\
0 & y & 0 \\
0 & 0 & z
\end{array}\right)
$$

Hence,

$$
\begin{aligned}
|A| & =x(y z-0) \\
& =x y z \\
& \neq 0
\end{aligned}
$$

Now,

$$
\begin{array}{lll}
A_{11}=y z & A_{12}=0 & A_{13}=0 \\
A_{21}=0 & A_{22}=x z & A_{23}=0 \\
A_{31}=0 & A_{32}=0 & A_{33}=x y
\end{array}
$$

Therefore,

$$
\begin{aligned}
A^{-1} & =\frac{1}{|A|}(\operatorname{adj} A) \\
& =\frac{1}{x y z}\left(\begin{array}{ccc}
y z & 0 & 0 \\
0 & x z & 0 \\
0 & 0 & x y
\end{array}\right) \\
& =\left(\begin{array}{ccc}
\frac{y z}{x y z} & 0 & 0 \\
0 & \frac{x z}{x y z} & 0 \\
0 & 0 & \frac{x y}{x y z}
\end{array}\right) \\
& =\left(\begin{array}{ccc}
\frac{1}{x} & 0 & 0 \\
0 & \frac{1}{y} & 0 \\
0 & 0 & \frac{1}{z}
\end{array}\right) \\
& =\left(\begin{array}{ccc}
x^{-1} & 0 & 0 \\
0 & y^{-1} & 0 \\
0 & 0 & z^{-1}
\end{array}\right)
\end{aligned}
$$

Thus, the correct option is A.
:::

:::

:::question{number="61" kind="exercise" id="q_4.61" topic="MCQ - range of a determinant with trig entries"}
#### Question 61

:::prompt
Choose the correct answer in Exercise 17 to 19.
Let $\mathrm{A}=\left[\begin{array}{ccc}1 & \sin \theta & 1 \\ -\sin \theta & 1 & \sin \theta \\ -1 & -\sin \theta & 1\end{array}\right]$, where $0 \leq \theta \leq 2 \pi$. Then
(A) $\operatorname{Det}(\mathrm{A})=0$
(B) $\operatorname{Det}(\mathrm{A}) \in(2, \infty)$
(C) $\operatorname{Det}(\mathrm{A}) \in(2,4)$
(D) $\operatorname{Det}(\mathrm{A}) \in[2,4]$
:::

:::solution{label="Solution"}
$$
A=\left(\begin{array}{ccc}
1 & \sin \theta & 1 \\
-\sin \theta & 1 & \sin \theta \\
-1 & -\sin \theta & 1
\end{array}\right), \text { where } 0 \leq \theta \leq 2 \pi, \text { then: }
$$

(A) $\operatorname{Det}(A)=0$
(B) $\operatorname{Det}(A) \in(2, \infty)$
(C) $\operatorname{Det}(A) \in(2,4)$
(D) $\operatorname{Det}(A) \in[2,4]$

Solution:
It is given that

$$
A=\left(\begin{array}{ccc}
1 & \sin \theta & 1 \\
-\sin \theta & 1 & \sin \theta \\
-1 & -\sin \theta & 1
\end{array}\right)
$$

Hence,

$$
\begin{aligned}
|A| & =1\left(1+\sin ^{2} \theta\right)-\sin \theta(-\sin \theta+\sin \theta)+1\left(\sin ^{2} \theta+1\right) \\
& =1+\sin ^{2} \theta+\sin ^{2} \theta+1 \\
& =2+2 \sin ^{2} \theta \\
& =2\left(1+\sin ^{2} \theta\right)
\end{aligned}
$$

Now,

$$
\begin{aligned}
& \Rightarrow 0 \leq \theta \leq 2 \pi \\
& \Rightarrow-1 \leq \sin \theta \leq 1 \\
& \Rightarrow 0 \leq \sin ^{2} \theta \leq 1 \\
& \Rightarrow 1 \leq 1+\sin ^{2} \theta \leq 2 \\
& \Rightarrow 2 \leq 2\left(1+\sin ^{2} \theta\right) \leq 4
\end{aligned}
$$

Therefore,

$$
\operatorname{Det}(A) \in[2,4]
$$

Thus, the correct option is D.
:::

:::

## Additional Questions

:::question{number="EX4.OLD-1" kind="additional_exercise" id="sol_4.d.1" topic="Properties of determinants"}
#### Additional Question EX4.OLD-1

:::prompt
Using the property of determinants and without expanding, prove that:

$$
\left|\begin{array}{lll}
x & a & x+a \\
y & b & y+b \\
z & c & z+c
\end{array}\right|=0
$$
:::

:::solution{label="Solution"}
$$
\begin{aligned}
\Delta & =\left|\begin{array}{lll}
x & a & x+a \\
y & b & y+b \\
z & c & z+c
\end{array}\right| \\
& =\left|\begin{array}{lll}
x & a & x \\
y & b & y \\
z & c & z
\end{array}\right|+\left|\begin{array}{lll}
x & a & a \\
y & b & b \\
z & c & c
\end{array}\right|
\end{aligned}
$$

Here, two columns of each determinant are identical.
Hence,

$$
\begin{aligned}
\Delta & =0+0 \\
& =0
\end{aligned}
$$
:::

:::

:::question{number="EX4.OLD-2" kind="additional_exercise" id="sol_4.d.2" topic="Properties of determinants"}
#### Additional Question EX4.OLD-2

:::prompt
Using the property of determinants and without expanding, prove that:

$$
\left|\begin{array}{lll}
a-b & b-c & c-a \\
b-c & c-a & a-b \\
c-a & a-b & b-c
\end{array}\right|=0
$$
:::

:::solution{label="Solution"}
$$
\begin{aligned}
\Delta & =\left|\begin{array}{lll}
a-b & b-c & c-a \\
b-c & c-a & a-b \\
c-a & a-b & b-c
\end{array}\right| \\
& =\left|\begin{array}{ccc}
a-c & b-a & c-b \\
b-c & c-a & a-b \\
-(a-c) & -(b-a) & -(c-b)
\end{array}\right| \\
& =\left|\begin{array}{lll}
a-c & b-a & c-b \\
b-c & c-a & a-b \\
a-c & b-a & c-b
\end{array}\right|
\end{aligned}
$$

Here, the two rows $R_{1}$ and $R_{3}$ are identical.

Hence, $\Delta=0$
:::

:::

:::question{number="EX4.OLD-3" kind="additional_exercise" id="sol_4.d.3" topic="Properties of determinants"}
#### Additional Question EX4.OLD-3

:::prompt
Using the property of determinants and without expanding, prove that:

$$
\left|\begin{array}{lll}
2 & 7 & 65 \\
3 & 8 & 75 \\
5 & 9 & 86
\end{array}\right|=0
$$
:::

:::solution{label="Solution"}
$$
\begin{aligned}
\Delta & =\left|\begin{array}{lll}
2 & 7 & 65 \\
3 & 8 & 75 \\
5 & 9 & 86
\end{array}\right| \\
& =\left|\begin{array}{lll}
2 & 7 & 63+2 \\
3 & 8 & 72+3 \\
5 & 9 & 81+5
\end{array}\right| \\
& =\left|\begin{array}{lll}
2 & 7 & 63 \\
3 & 8 & 72 \\
5 & 9 & 81
\end{array}\right|+\left|\begin{array}{lll}
2 & 7 & 2 \\
3 & 8 & 3 \\
5 & 9 & 5
\end{array}\right| \\
& =\left|\begin{array}{ccc}
2 & 7 & 9(7) \\
3 & 8 & 9(8) \\
5 & 9 & 9(9)
\end{array}\right|+0 \\
& =9\left|\begin{array}{ccc}
2 & 7 & 7 \\
3 & 8 & 8 \\
5 & 9 & 9
\end{array}\right| \\
& =0
\end{aligned} \quad \text { [∵ Two columns are identical] }
$$
:::

:::

:::question{number="EX4.OLD-4" kind="additional_exercise" id="sol_4.d.4" topic="Properties of determinants"}
#### Additional Question EX4.OLD-4

:::prompt
Using the property of determinants and without expanding, prove that:

$$
\left|\begin{array}{lll}
1 & b c & a(b+c) \\
1 & c a & b(c+a) \\
1 & a b & c(a+b)
\end{array}\right|=0
$$
:::

:::solution{label="Solution"}
$$
\begin{aligned}
\Delta & =\left|\begin{array}{lll}
1 & b c & a(b+c) \\
1 & c a & b(c+a) \\
1 & a b & c(a+b)
\end{array}\right| \\
& =\left|\begin{array}{lll}
1 & b c & a b+b c+c a \\
1 & c a & a b+b c+c a \\
1 & a b & a b+b c+c a
\end{array}\right|
\end{aligned} \quad\left[C_{3} \rightarrow C_{3}+C_{2}\right] .
$$

Here, the two columns $C_{1}$ and $C_{3}$ are proportional.
Hence, $\Delta=0$
:::

:::

:::question{number="EX4.OLD-5" kind="additional_exercise" id="sol_4.d.5" topic="Properties of determinants" corrections_applied="1"}
#### Additional Question EX4.OLD-5

:::prompt
Using the property of determinants and without expanding, prove that:

$$
\left|\begin{array}{lll}
b+c & q+r & y+z \\
c+a & r+p & z+x \\
a+b & p+q & x+y
\end{array}\right|=2\left|\begin{array}{lll}
a & p & x \\
b & q & y \\
c & r & z
\end{array}\right|
$$
:::

:::solution{label="Solution"}
$$
\begin{aligned}
\Delta & =\left|\begin{array}{ccc}
b+c & q+r & y+z \\
c+a & r+p & z+x \\
a+b & p+q & x+y
\end{array}\right| \\
& =\left|\begin{array}{ccc}
b+c & q+r & y+z \\
c+a & r+p & z+x \\
a & p & x
\end{array}\right|+\left|\begin{array}{ccc}
b+c & q+r & y+z \\
c+a & r+p & z+x \\
b & q & y
\end{array}\right| \\
& =\Delta_{1}+\Delta_{2}
\end{aligned}
$$

Now,

$$
\begin{array}{rlr}
\Delta_{1} & =\left|\begin{array}{ccc}
b+c & q+r & y+z \\
c+a & r+p & z+x \\
a & p & x
\end{array}\right| & \\
& =\left|\begin{array}{ccc}
b+c & q+r & y+z \\
c & r & z \\
a & p & x
\end{array}\right| & {\left[R_{2} \rightarrow R_{2}-R_{3}\right]} \\
& =\left|\begin{array}{ccc}
b & q & y \\
c & r & z \\
a & p & x
\end{array}\right| \\
& =(-1)^{2}\left|\begin{array}{ccc}
a & p & x \\
b & q & y \\
c & r & z
\end{array}\right| & {\left[R_{1} \rightarrow R_{1}-R_{2}\right]} \\
\Delta_{1} & =\left|\begin{array}{ccc}
a & p & x \\
b & q & y \\
c & r & z
\end{array}\right| & {\left[R_{1} \leftrightarrow R_{3} \text { and } R_{2} \leftrightarrow R_{3}\right]} \\
\Delta_{2} & =\left|\begin{array}{ccc}
b+c & q+r & y+z \\
c+a & r+p & z+x \\
b & q & y
\end{array}\right| & \quad\left[R_{1} \rightarrow R_{1}-R_{3}\right] \\
\Delta_{2} & =\left|\begin{array}{ccc}
c & r & z \\
c+a & r+p & z+x \\
b & q & y
\end{array}\right| & \quad\left[R_{2} \rightarrow R_{2}-R_{1}\right] \\
\Delta_{2} & =\left|\begin{array}{ccc}
c & r & z \\
a & p & x \\
b & q & y
\end{array}\right| \\
\Delta_{2} & =(-1)^{2}\left|\begin{array}{ccc}
a & p & x \\
b & q & y \\
c & r & z
\end{array}\right| & \quad\left[R_{1} \leftrightarrow R_{2} \text { and } R_{2} \leftrightarrow R_{3}\right]
\end{array}
$$

From (1),(2) and (3), we have

$$
\begin{aligned}
\Delta & =\left|\begin{array}{lll}
a & p & x \\
b & q & y \\
c & r & z
\end{array}\right|+\left|\begin{array}{lll}
a & p & x \\
b & q & y \\
c & r & z
\end{array}\right| \\
& =2\left|\begin{array}{lll}
a & p & x \\
b & q & y \\
c & r & z
\end{array}\right|
\end{aligned}
$$

Hence, $\left|\begin{array}{lll}b+c & q+r & y+z \\ c+a & r+p & z+x \\ a+b & p+q & x+y\end{array}\right|=2\left|\begin{array}{lll}a & p & x \\ b & q & y \\ c & r & z\end{array}\right|$ proved.
:::

:::

:::question{number="EX4.OLD-6" kind="additional_exercise" id="sol_4.d.6" topic="Properties of determinants"}
#### Additional Question EX4.OLD-6

:::prompt
Using the property of determinants and without expanding, prove that:

$$
\left|\begin{array}{ccc}
0 & a & -b \\
-a & 0 & -c \\
b & c & 0
\end{array}\right|=0
$$
:::

:::solution{label="Solution"}
$$
\begin{aligned}
\Delta & =\left|\begin{array}{ccc}
0 & a & -b \\
-a & 0 & -c \\
b & c & 0
\end{array}\right| & \\
& =\frac{1}{c}\left|\begin{array}{ccc}
0 & a c & -b c \\
-a & 0 & -c \\
b & c & 0
\end{array}\right| & {\left[R_{1} \rightarrow c R_{1}\right] } \\
& =\frac{1}{c}\left|\begin{array}{ccc}
a b & a c & 0 \\
-a & 0 & -c \\
b & c & 0
\end{array}\right| & {\left[R_{1} \rightarrow R_{1}-b R_{2}\right] } \\
& =\frac{a}{c}\left|\begin{array}{ccc}
b & c & 0 \\
-a & 0 & -c \\
b & c & 0
\end{array}\right| &
\end{aligned}
$$

Here, the two rows $R_{1}$ and $R_{3}$ are identical.
Hence, $\Delta=0$
:::

:::

:::question{number="EX4.OLD-7" kind="additional_exercise" id="sol_4.d.7" topic="Properties of determinants" corrections_applied="2"}
#### Additional Question EX4.OLD-7

:::prompt
Using the property of determinants and without expanding, prove that:

$$
\left|\begin{array}{ccc}
-a^{2} & a b & a c \\
b a & -b^{2} & b c \\
c a & c b & -c^{2}
\end{array}\right|=4 a^{2} b^{2} c^{2}
$$
:::

:::solution{label="Solution"}
$$
\begin{array}{rlr}
\Delta & =\left|\begin{array}{ccc}
-a^{2} & a b & a c \\
b a & -b^{2} & b c \\
c a & c b & -c^{2}
\end{array}\right| & \\
& =a b c\left|\begin{array}{ccc}
-a & b & c \\
a & -b & c \\
a & b & -c
\end{array}\right| & \text { [Taking out factors } \left.a, b, c \text { from } R_{1}, R_{2}, R_{3}\right] \\
& =a^{2} b^{2} c^{2}\left|\begin{array}{ccc}
-1 & 1 & 1 \\
1 & -1 & 1 \\
1 & 1 & -1
\end{array}\right| & \text { [Taking out factors } \left.a, b, c \text { from } C_{1}, C_{2}, C_{3}\right] \\
& =a^{2} b^{2} c^{2}\left|\begin{array}{ccc}
-1 & 1 & 1 \\
0 & 0 & 2 \\
0 & 2 & 0
\end{array}\right| & {\left[R_{2} \rightarrow R_{2}+R_{1} \text { and } R_{3} \rightarrow R_{3}+R_{1}\right]} \\
& =a^{2} b^{2} c^{2}(-1)\left|\begin{array}{cc}
0 & 2 \\
2 & 0
\end{array}\right| & \\
& =-a^{2} b^{2} c^{2}(0-4) & \\
& =4 a^{2} b^{2} c^{2} &
\end{array}
$$
:::

:::

:::question{number="EX4.OLD-8" kind="additional_exercise" id="sol_4.d.8" topic="Properties of determinants"}
#### Additional Question EX4.OLD-8

:::prompt
By using properties of determinants show that:

(i) $\left|\begin{array}{lll}1 & a & a^{2} \\ 1 & b & b^{2} \\ 1 & c & c^{2}\end{array}\right|=(a-b)(b-c)(c-a)$
(ii) $\left|\begin{array}{ccc}1 & 1 & 1 \\ a & b & c \\ a^{3} & b^{3} & c^{3}\end{array}\right|=(a-b)(b-c)(c-a)(a+b+c)$
:::

:::solution{label="Solution"}
(i) Let $\Delta=\left|\begin{array}{lll}1 & a & a^{2} \\ 1 & b & b^{2} \\ 1 & c & c^{2}\end{array}\right|$

$$
\begin{array}{rlr}
\Delta & =\left|\begin{array}{ccc}
0 & a-c & a^{2}-c^{2} \\
0 & b-c & b^{2}-c^{2} \\
1 & c & c^{2}
\end{array}\right| & {\left[R_{1} \rightarrow R_{1}-R_{3} \text { and } R_{2} \rightarrow R_{2}-R_{3}\right]} \\
& =(c-a)(b-c)\left|\begin{array}{ccc}
0 & -1 & -a-c \\
0 & 1 & b+c \\
1 & c & c^{2}
\end{array}\right| & \\
& =(b-c)(c-a)\left|\begin{array}{ccc}
0 & 0 & -a+b \\
0 & 1 & b+c \\
1 & c & c^{2}
\end{array}\right| & {\left[R_{1} \rightarrow R_{1}+R_{2}\right]} \\
& =(a-b)(b-c)(c-a)\left|\begin{array}{ccc}
0 & 0 & -1 \\
0 & 1 & b+c \\
1 & c & c^{2}
\end{array}\right| & \\
& =(a-b)(b-c)(c-a)\left|\begin{array}{cc}
0 & -1 \\
1 & b+c
\end{array}\right| &
\end{array}=(a-b)(b-c)(c-a) \text { }
$$

Hence, $\left|\begin{array}{lll}1 & a & a^{2} \\ 1 & b & b^{2} \\ 1 & c & c^{2}\end{array}\right|=(a-b)(b-c)(c-a)$ proved.
(ii) Let

$$
\Delta=\left|\begin{array}{ccc}
1 & 1 & 1 \\
a & b & c \\
a^{3} & b^{3} & c^{3}
\end{array}\right|
$$

$$
\begin{aligned}
\Delta & =\left|\begin{array}{ccc}
0 & 0 & 1 \\
a-c & b-c & c \\
a^{3}-c^{3} & b^{3}-c^{3} & c^{3}
\end{array}\right| \quad\left[C_{1} \rightarrow C_{1}-C_{3} \text { and } C_{2} \rightarrow C_{2}-C_{3}\right] \\
& =\left|\begin{array}{ccc}
0 & 0 & 1 \\
a-c & b-c & c \\
(a-c)\left(a^{2}+a c+c^{2}\right) & (b-c)\left(b^{2}+b c+c^{2}\right) & c^{3}
\end{array}\right| \\
& =(c-a)(b-c)\left|\begin{array}{ccc}
0 & 0 & 1 \\
-1 & 1 & c \\
-\left(a^{2}+a c+c^{2}\right) & \left(b^{2}+b c+c^{2}\right) & c^{3}
\end{array}\right|
\end{aligned}
$$

Applying $C_{1} \rightarrow C_{1}+C_{2}$,

$$
\begin{aligned}
\Delta & =(c-a)(b-c)\left|\begin{array}{ccc}
0 & 0 & 1 \\
0 & 1 & c \\
\left(b^{2}-a^{2}\right)+(b c-a c) & \left(b^{2}+b c+c^{2}\right) & c^{3}
\end{array}\right| \\
& =(b-c)(c-a)(a-b)\left|\begin{array}{ccc}
0 & 0 & 1 \\
0 & 1 & c \\
-(a+b+c) & \left(b^{2}+b c+c^{2}\right) & c^{3}
\end{array}\right| \\
& =(a-b)(b-c)(c-a)(a+b+c)\left|\begin{array}{ccc}
0 & 0 & 1 \\
0 & 1 & c \\
-1 & \left(b^{2}+b c+c^{2}\right) & c^{3}
\end{array}\right| \\
& =(a-b)(b-c)(c-a)(a+b+c)(-1)\left|\begin{array}{ll}
0 & 1 \\
1 & c
\end{array}\right| \\
& =(a-b)(b-c)(c-a)(a+b+c)
\end{aligned}
$$

Hence, $\left|\begin{array}{lll}1 & 1 & 1 \\ a & b & c \\ a^{3} & b^{3} & c^{3}\end{array}\right|=(a-b)(b-c)(c-a)(a+b+c) \quad$ proved.
:::

:::

:::question{number="EX4.OLD-9" kind="additional_exercise" id="sol_4.d.9" topic="Properties of determinants"}
#### Additional Question EX4.OLD-9

:::prompt
By using properties of determinants show that:

$$
\left|\begin{array}{lll}
x & x^{2} & y z \\
y & y^{2} & z x \\
z & z^{2} & x y
\end{array}\right|=(x-y)(y-z)(z-x)(x y+y z+z x)
$$
:::

:::solution{label="Solution"}
Let

$$
\Delta=\left|\begin{array}{lll}
x & x^{2} & y z \\
y & y^{2} & z x \\
z & z^{2} & x y
\end{array}\right|
$$

$$
\begin{aligned}
\Delta & =\left|\begin{array}{ccc}
x & x^{2} & y z \\
y-x & y^{2}-x^{2} & z x-y z \\
z-x & z^{2}-x^{2} & x y-y z
\end{array}\right| \quad\left[R_{2} \rightarrow R_{2}-R_{1} \text { and } R_{3} \rightarrow R_{3}-R_{1}\right] \\
& =\left|\begin{array}{ccc}
x & x^{2} & y z \\
-(x-y) & -(x-y)(x+y) & z(x-y) \\
(z-x) & (z-x)(z+x) & -y(z-x)
\end{array}\right| \\
& =(x-y)(z-x)\left|\begin{array}{ccc}
x & x^{2} & y z \\
-1 & -x-y & z \\
1 & (z+x) & -y
\end{array}\right| \\
\Delta & =(x-y)(z-x)\left|\begin{array}{ccc}
x & x^{2} & y z \\
-1 & -x-y & z \\
0 & z-y & z-y
\end{array}\right| \\
& =(x-y)(z-x)(z-y)\left|\begin{array}{ccc}
x & x^{2} & y z \\
-1 & -x-y & z \\
0 & 1 & 1
\end{array}\right| \\
& =[(x-y)(z-x)(z-y)]\left[(-1)\left|\begin{array}{cc}
x & y z \\
-1 & z
\end{array}\right|+1\left|\begin{array}{cc}
x & x^{2} \\
-1 & -x-y
\end{array}\right|\right] \\
& =(x-y)(z-x)(z-y)\left[(-x z-y z)+\left(-x^{2}-x y+x^{2}\right)\right] \\
& =-(x-y)(z-x)(z-y)(x y+y z+z x) \\
& =(x-y)(y-z)(z-x)(x y+y z+z x)
\end{aligned}
$$

Hence, $\left|\begin{array}{ccc}x & x^{2} & y z \\ y & y^{2} & z x \\ z & z^{2} & x y\end{array}\right|=(x-y)(y-z)(z-x)(x y+y z+z x)$ proved.
:::

:::

:::question{number="EX4.OLD-10" kind="additional_exercise" id="sol_4.d.10" topic="Properties of determinants"}
#### Additional Question EX4.OLD-10

:::prompt
By using properties of determinants show that:

(i) $\left|\begin{array}{ccc}x+4 & 2 x & 2 x \\ 2 x & x+4 & 2 x \\ 2 x & 2 x & x+4\end{array}\right|=(5 x+4)(4-x)^{2}$
(ii) $\left|\begin{array}{ccc}y+k & y & y \\ y & y+k & y \\ y & y & y+k\end{array}\right|=k^{2}(3 y+k)$
:::

:::solution{label="Solution"}
(i)

$$
\Delta=\left|\begin{array}{ccc}
x+4 & 2 x & 2 x \\
2 x & x+4 & 2 x \\
2 x & 2 x & x+4
\end{array}\right|
$$

$$
\begin{array}{rlr}
\Delta & =\left|\begin{array}{ccc}
5 x+4 & 5 x+4 & 5 x+4 \\
2 x & x+4 & 2 x \\
2 x & 2 x & x+4
\end{array}\right| & {\left[R_{1} \rightarrow R_{1}+R_{2}+R_{3}\right]} \\
& =(5 x+4)\left|\begin{array}{ccc}
1 & 1 & 1 \\
2 x & x+4 & 2 x \\
2 x & 2 x & x+4
\end{array}\right| & \\
& =(5 x+4)\left|\begin{array}{ccc}
1 & 0 & 0 \\
2 x & -x+4 & 0 \\
2 x & 0 & -x+4
\end{array}\right| & {\left[C_{2} \rightarrow C_{2}-C_{1} \text { and } C_{3} \rightarrow C_{3}-C_{1}\right]} \\
& =(5 x+4)(4-x)(4-x)\left|\begin{array}{ccc}
1 & 0 & 0 \\
2 x & 1 & 0 \\
2 x & 0 & 1
\end{array}\right| & \\
& =(5 x+4)(4-x)^{2}\left|\begin{array}{cc}
1 & 0 \\
2 x & 1
\end{array}\right| & \\
& =(5 x+4)(4-x)^{2} &
\end{array}
$$

proved.
(ii)

$$
\Delta=\left|\begin{array}{ccc}
y+k & y & y \\
y & y+k & y \\
y & y & y+k
\end{array}\right|
$$

$$
\begin{array}{rlr}
\Delta & =\left|\begin{array}{ccc}
3 y+k & 3 y+k & 3 y+k \\
y & y+k & y \\
y & y & y+k
\end{array}\right| & {\left[R_{1} \rightarrow R_{1}+R_{2}+R_{3}\right]} \\
& =(3 y+k)\left|\begin{array}{ccc}
1 & 1 & 1 \\
y & y+k & y \\
y & y & y+k
\end{array}\right| & \\
& =(3 y+k)\left|\begin{array}{ccc}
1 & 0 & 0 \\
y & k & 0 \\
y & 0 & k
\end{array}\right| & {\left[C_{2} \rightarrow C_{2}-C_{1} \text { and } C_{3} \rightarrow C_{3}-C_{1}\right]} \\
& =k^{2}(3 y+k)\left|\begin{array}{ccc}
1 & 0 & 0 \\
y & 1 & 0 \\
y & 0 & 1
\end{array}\right| &
\end{array}
$$

Expanding along $C_{3}$

$$
\begin{aligned}
\Delta & =k^{2}(3 y+k)\left|\begin{array}{ll}
1 & 0 \\
y & 1
\end{array}\right| \\
& =k^{2}(3 y+k)
\end{aligned}
$$

Hence, $\left|\begin{array}{ccc}y+k & y & y \\ y & y+k & y \\ y & y & y+k\end{array}\right|=k^{2}(3 y+k) \quad$ proved.
:::

:::

:::question{number="EX4.OLD-11" kind="additional_exercise" id="sol_4.d.11" topic="Properties of determinants" corrections_applied="1"}
#### Additional Question EX4.OLD-11

:::prompt
By using properties of determinants show that:
(i) $\left|\begin{array}{ccc}a-b-c & 2 a & 2 a \\ 2 b & b-c-a & 2 b \\ 2 c & 2 c & c-a-b\end{array}\right|=(a+b+c)^{3}$
(ii) $\left|\begin{array}{ccc}x+y+2 z & x & y \\ z & y+z+2 x & y \\ z & x & z+x+2 y\end{array}\right|=2(x+y+z)^{3}$
:::

:::solution{label="Solution"}
(i) $\Delta=\left|\begin{array}{ccc}a-b-c & 2 a & 2 a \\ 2 b & b-c-a & 2 b \\ 2 c & 2 c & c-a-b\end{array}\right|$

$$
\begin{array}{rlr}
\Delta & =\left|\begin{array}{ccc}
a+b+c & a+b+c & a+b+c \\
2 b & b-c-a & 2 b \\
2 c & 2 c & c-a-b
\end{array}\right| & {\left[R_{1} \rightarrow R_{1}+R_{2}+R_{3}\right]} \\
& =(a+b+c)\left|\begin{array}{ccc}
1 & 1 & 1 \\
2 b & b-c-a & 2 b \\
2 c & 2 c & c-a-b
\end{array}\right| & \\
& =(a+b+c)\left|\begin{array}{ccc}
1 & 0 & 0 \\
2 b & -(a+b+c) & 0 \\
2 c & 0 & -(a+b+c)
\end{array}\right| & {\left[C_{2} \rightarrow C_{2}-C_{1} \text { and } C_{3} \rightarrow C_{3}-C_{1}\right]} \\
& =(a+b+c)^{3}\left|\begin{array}{ccc}
1 & 0 & 0 \\
2 b & -1 & 0 \\
2 c & 0 & -1
\end{array}\right| & \\
& =(a+b+c)^{3}(-1)(-1) & \\
& =(a+b+c)^{3} &
\end{array}
$$

Hence, proved.
(ii)

$$
\begin{aligned}
\Delta & =\left|\begin{array}{ccc}
x+y+2 z & x & y \\
z & y+z+2 x & y \\
z & x & z+x+2 y
\end{array}\right| \\
\Delta & =\left|\begin{array}{ccc}
2(x+y+z) & x & y \\
2(x+y+z) & y+z+2 x & y \\
2(x+y+z) & x & z+x+2 y
\end{array}\right| \quad\left[C_{1} \rightarrow C_{1}+C_{2}+C_{3}\right] \\
& =2(x+y+z)\left|\begin{array}{ccc}
1 & x & y \\
1 & y+z+2 x & y \\
1 & x & z+x+2 y
\end{array}\right| \\
& =2(x+y+z)\left|\begin{array}{ccc}
1 & x & y \\
0 & x+y+z & 0 \\
0 & 0 & x+y+z
\end{array}\right| \quad\left[R_{2} \rightarrow R_{2}-R_{1} \text { and } R_{3} \rightarrow R_{3}-R_{1}\right] \\
& =2(x+y+z)^{3}\left|\begin{array}{ccc}
1 & x & y \\
0 & 1 & 0 \\
0 & 0 & 1
\end{array}\right| \\
& =2(x+y+z)^{3}(1)(1-0) \\
& =2(x+y+z)^{3}
\end{aligned}
$$

Hence, proved.
:::

:::

:::question{number="EX4.OLD-12" kind="additional_exercise" id="sol_4.d.12" topic="Properties of determinants"}
#### Additional Question EX4.OLD-12

:::prompt
By using properties of determinants show that:

$$
\left|\begin{array}{ccc}
1 & x & x^{2} \\
x^{2} & 1 & x \\
x & x^{2} & 1
\end{array}\right|=\left(1-x^{3}\right)^{2}
$$
:::

:::solution{label="Solution"}
$$
\begin{aligned}
\Delta & =\left|\begin{array}{ccc}
1 & x & x^{2} \\
x^{2} & 1 & x \\
x & x^{2} & 1
\end{array}\right| \\
& =\left|\begin{array}{ccc}
1+x+x^{2} & 1+x+x^{2} & 1+x+x^{2} \\
x^{2} & 1 & x \\
x & x^{2} & 1
\end{array}\right| \quad\left[R_{1} \rightarrow R_{1}+R_{2}+R_{3}\right] \\
& =\left(1+x+x^{2}\right)\left|\begin{array}{ccc}
1 & 1 & 1 \\
x^{2} & 1 & x \\
x & x^{2} & 1
\end{array}\right| \\
\Delta & =\left(1+x+x^{2}\right)\left|\begin{array}{ccc}
1 & 0 & 0 \\
x^{2} & 1-x^{2} & x-x^{2} \\
x & x^{2}-x & 1-x
\end{array}\right| \quad\left[C_{2} \rightarrow C_{2}-C_{1} \text { and } C_{3} \rightarrow C_{3}-C_{1}\right] \\
\Delta & =\left(1+x+x^{2}\right)(1-x)(1-x)\left|\begin{array}{ccc}
1 & 0 & 0 \\
x^{2} & 1+x & x \\
x & -x & 1
\end{array}\right| \\
& =\left(1-x^{3}\right)(1-x)\left|\begin{array}{ccc}
1 & 0 & 0 \\
x^{2} & 1+x & x \\
x & -x & 1
\end{array}\right|
\end{aligned}
$$

Expanding along $R_{1}$

$$
\begin{aligned}
\Delta & =\left(1-x^{3}\right)(1-x)(1)\left|\begin{array}{cc}
1+x & x \\
-x & 1
\end{array}\right| \\
& =\left(1-x^{3}\right)(1-x)\left(1+x+x^{2}\right) \\
& =\left(1-x^{3}\right)\left(1-x^{3}\right) \\
& =\left(1-x^{3}\right)^{2}
\end{aligned}
$$

Hence, proved.
:::

:::

:::question{number="EX4.OLD-13" kind="additional_exercise" id="sol_4.d.13" topic="Properties of determinants" corrections_applied="1"}
#### Additional Question EX4.OLD-13

:::prompt
By using properties of determinants show that:

$$
\left|\begin{array}{ccc}
1+a^{2}-b^{2} & 2 a b & -2 b \\
2 a b & 1-a^{2}+b^{2} & 2 a \\
2 b & -2 a & 1-a^{2}-b^{2}
\end{array}\right|=\left(1+a^{2}+b^{2}\right)^{3}
$$
:::

:::solution{label="Solution"}
$$
\begin{aligned}
\Delta & =\left|\begin{array}{ccc}
1+a^{2}-b^{2} & 2 a b & -2 b \\
2 a b & 1-a^{2}+b^{2} & 2 a \\
2 b & -2 a & 1-a^{2}-b^{2}
\end{array}\right| \\
& =\left|\begin{array}{ccc}
1+a^{2}+b^{2} & 0 & -b\left(1+a^{2}+b^{2}\right) \\
0 & 1+a^{2}+b^{2} & a\left(1+a^{2}+b^{2}\right) \\
2 b & -2 a & 1-a^{2}-b^{2}
\end{array}\right| \quad\left[R_{1} \rightarrow R_{1}+b R_{3} \text { and } R_{2} \rightarrow R_{2}-a R_{3}\right] \\
& =\left(1+a^{2}+b^{2}\right)^{2}\left|\begin{array}{ccc}
1 & 0 & -b \\
0 & 1 & a \\
2 b & -2 a & 1-a^{2}-b^{2}
\end{array}\right| \\
& =\left(1+a^{2}+b^{2}\right)^{2}\left[(1)\left|\begin{array}{cc}
1 & a \\
-2 a & 1-a^{2}-b^{2}
\end{array}\right|-b\left|\begin{array}{cc}
0 & 1 \\
2 b & -2 a
\end{array}\right|\right] \\
& =\left(1+a^{2}+b^{2}\right)^{2}\left[\begin{array}{cc}
1-a^{2}-b^{2}+2 a^{2}-b(-2 b)
\end{array}\right] \\
& =\left(1+a^{2}+b^{2}\right)^{2}\left(1+a^{2}+b^{2}\right) \\
& =\left(1+a^{2}+b^{2}\right)^{3}
\end{aligned}
$$

Hence, proved.
:::

:::

:::question{number="EX4.OLD-14" kind="additional_exercise" id="sol_4.d.14" topic="Properties of determinants" corrections_applied="1"}
#### Additional Question EX4.OLD-14

:::prompt
By using properties of determinants show that:

$$
\left|\begin{array}{ccc}
a^{2}+1 & a b & a c \\
a b & b^{2}+1 & b c \\
c a & c b & c^{2}+1
\end{array}\right|=1+a^{2}+b^{2}+c^{2}
$$
:::

:::solution{label="Solution"}
$$
\Delta=\left|\begin{array}{ccc}
a^{2}+1 & a b & a c \\
a b & b^{2}+1 & b c \\
c a & c b & c^{2}+1
\end{array}\right|
$$

Taking out common factors $a, b, c$ from $R_{1}, R_{2}, R_{3}$ respectively,

$$
\begin{aligned}
\Delta & =a b c\left|\begin{array}{ccc}
a+\frac{1}{a} & b & c \\
a & b+\frac{1}{b} & c \\
a & b & c+\frac{1}{c}
\end{array}\right| \\
& =a b c\left|\begin{array}{ccc}
a+\frac{1}{a} & b & c \\
-\frac{1}{a} & \frac{1}{b} & 0 \\
-\frac{1}{a} & 0 & \frac{1}{c}
\end{array}\right| \quad\left[R_{2} \rightarrow R_{2}-R_{1} \text { and } R_{3} \rightarrow R_{3}-R_{1}\right] \\
& =a b c \times \frac{1}{a b c}\left|\begin{array}{ccc}
a^{2}+1 & b^{2} & c^{2} \\
-1 & 1 & 0 \\
-1 & 0 & 1
\end{array}\right| \quad\left[C_{1} \rightarrow a C_{1}, C_{2} \rightarrow b C_{2} \text { and } C_{3} \rightarrow c C_{3}\right] \\
& =\left|\begin{array}{ccc}
a^{2}+1 & b^{2} & c^{2} \\
-1 & 1 & 0 \\
-1 & 0 & 1
\end{array}\right| \\
& =-1\left|\begin{array}{cc}
b^{2} & c^{2} \\
1 & 0
\end{array}\right|+1\left|\begin{array}{cc}
a^{2}+1 & b^{2} \\
-1 & 1
\end{array}\right| \\
& =-1\left(-c^{2}\right)+\left(a^{2}+1+b^{2}\right) \\
& =1+a^{2}+b^{2}+c^{2}
\end{aligned}
$$

Hence, proved.
:::

:::

:::question{number="EX4.OLD-15" kind="additional_exercise" id="sol_4.d.15" topic="Properties of determinants"}
#### Additional Question EX4.OLD-15

:::prompt
Let $A$ be a square matrix of order 3 × 3 , then $|k A|$ is equal to:
(A) $k|A|$
(B) $k^{2}|A|$
(C) $k^{3}|A|$
(D) $3^{k|A|}$
:::

:::solution{label="Solution"}
Let

$$
A=\left(\begin{array}{lll}
a_{1} & b_{1} & c_{1} \\
a_{2} & b_{2} & c_{2} \\
a_{3} & b_{3} & c_{3}
\end{array}\right)
$$

Then,

$$
\begin{aligned}
k A & =\left(\begin{array}{lll}
k a_{1} & k b_{1} & k c_{1} \\
k a_{2} & k b_{2} & k c_{2} \\
k a_{3} & k b_{3} & k c_{3}
\end{array}\right) \\
|k A| & =\left|\begin{array}{lll}
k a_{1} & k b_{1} & k c_{1} \\
k a_{2} & k b_{2} & k c_{2} \\
k a_{3} & k b_{3} & k c_{3}
\end{array}\right|
\end{aligned}
$$

Taking out common factors $k$ from each row

$$
\begin{aligned}
|k A| & =k^{3}\left|\begin{array}{lll}
a_{1} & b_{1} & c_{1} \\
a_{2} & b_{2} & c_{2} \\
a_{3} & b_{3} & c_{3}
\end{array}\right| \\
& =k^{3}|A|
\end{aligned}
$$

The correct option is C.
:::

:::

:::question{number="EX4.OLD-16" kind="additional_exercise" id="sol_4.d.16" topic="Properties of determinants"}
#### Additional Question EX4.OLD-16

:::prompt
Which of the following is correct?

(A) Determinant is a square matrix.
(B) Determinant is a number associated to a matrix.
(C) Determinant is a number associated to a square matrix.
(D) None of the above.
:::

:::solution{label="Solution"}
Every square matrix $A=\left[a_{i j}\right]$ of order $n$ has an associated number. This number is called the determinant of the square matrix $A$, where $a_{i j}=(i, j)^{\text {th }}$ element of $A$.

Thus, the determinant is a number associated to a square matrix.
Hence, the correct option is C.
:::

:::

:::question{number="MISC-2" kind="additional_exercise" id="sol_4.misc.2" topic="Evaluating a determinant without expanding"}
#### Additional Question MISC-2

:::prompt
Without expanding the determinant, prove that $\left|\begin{array}{lll}a & a^{2} & b c \\ b & b^{2} & c a \\ c & c^{2} & a b\end{array}\right|=\left|\begin{array}{lll}1 & a^{2} & a^{3} \\ 1 & b^{2} & b^{3} \\ 1 & c^{2} & c^{3}\end{array}\right|$.
:::

:::solution{label="Solution"}
$$
\begin{array}{rlrl}
\text { LHS } & =\left|\begin{array}{lll}
a & a^{2} & b c \\
b & b^{2} & c a \\
c & c^{2} & a b
\end{array}\right| & \\
& =\frac{1}{a b c}\left|\begin{array}{lll}
a^{2} & a^{3} & a b c \\
b^{2} & b^{3} & a b c \\
c^{2} & c^{3} & a b c
\end{array}\right| & & {\left[R_{1} \rightarrow a R_{1}, R_{2} \rightarrow b R_{2}, R_{3} \rightarrow c R_{3}\right]} \\
& =\frac{1}{a b c} \cdot a b c\left|\begin{array}{lll}
a^{2} & a^{3} & 1 \\
b^{2} & b^{3} & 1 \\
c^{2} & c^{3} & 1
\end{array}\right| & & \text { [Taking out factor } \left.a b c \text { from } C_{3}\right] \\
& =\left|\begin{array}{lll}
a^{2} & a^{3} & 1 \\
b^{2} & b^{3} & 1 \\
c^{2} & c^{3} & 1
\end{array}\right| & & \\
& =\left|\begin{array}{lll}
1 & a^{2} & a^{3} \\
1 & b^{2} & b^{3} \\
1 & c^{2} & c^{3}
\end{array}\right| & & {\left[C_{1} \leftrightarrow C_{3} \text { and } C_{2} \leftrightarrow C_{3}\right]} \\
& =R H S & &
\end{array}
$$

Hence, proved.
:::

:::

:::question{number="MISC-4" kind="additional_exercise" id="sol_4.misc.4" topic="Determinant identity with a+b+c symmetry"}
#### Additional Question MISC-4

:::prompt
If $a, b, c$ are real numbers and $\Delta=\left|\begin{array}{lll}b+c & c+a & a+b \\ c+a & a+b & b+c \\ a+b & b+c & c+a\end{array}\right|=0 \quad$, show that either $a+b+c=0$ or $a=b=c$.
:::

:::solution{label="Solution"}
$$
\begin{array}{rlr}
\Delta & =\left|\begin{array}{ccc}
b+c & c+a & a+b \\
c+a & a+b & b+c \\
a+b & b+c & c+a
\end{array}\right| & \\
& =\left|\begin{array}{ccc}
2(a+b+c) & 2(a+b+c) & 2(a+b+c) \\
c+a & a+b & b+c \\
a+b & b+c & c+a
\end{array}\right| & {\left[R_{1} \rightarrow R_{1}+R_{2}+R_{3}\right]} \\
& =2(a+b+c)\left|\begin{array}{ccc}
1 & 1 & 1 \\
c+a & a+b & b+c \\
a+b & b+c & c+a
\end{array}\right| & \\
& =2(a+b+c)\left|\begin{array}{ccc}
1 & 0 & 0 \\
c+a & b-c & b-a \\
a+b & c-a & c-b
\end{array}\right| & {\left[C_{2} \rightarrow C_{2}-C_{1} \text { and } C_{3} \rightarrow C_{3}-C_{1}\right]}
\end{array}
$$

Expanding $R_{1}$,

$$
\begin{aligned}
\Delta & =2(a+b+c)(1)[(b-c)(c-b)-(b-a)(c-a)] \\
& =2(a+b+c)\left[-b^{2}-c^{2}+2 b c-b c+b a+a c-a^{2}\right] \\
& =2(a+b+c)\left[a b+b c+c a-a^{2}-b^{2}-c^{2}\right]
\end{aligned}
$$

It is given that $\Delta=0$.
Hence,

$$
2(a+b+c)\left[a b+b c+c a-a^{2}-b^{2}-c^{2}\right]=0
$$

Either $(a+b+c)=0$ or $\left[a b+b c+c a-a^{2}-b^{2}-c^{2}\right]=0$
Now,

$$
\begin{aligned}
& \Rightarrow a b+b c+c a-a^{2}-b^{2}-c^{2}=0 \\
& \Rightarrow-2 a b-2 a c-2 c a+2 a^{2}+2 b^{2}+2 c^{2}=0 \\
& \Rightarrow(a-b)^{2}+(b-c)^{2}+(c-a)^{2}=0 \\
& \Rightarrow(a-b)^{2}=(b-c)^{2}=(c-a)^{2}=0 \quad\left[(a-b)^{2},(b-c)^{2},(c-a)^{2} \text { are non-negative }\right] \\
& \Rightarrow(a-b)=(b-c)=(c-a)=0 \\
& \Rightarrow a=b=c
\end{aligned}
$$

Hence, if $\Delta=0$, then either $(a+b+c)=0$ or $a=b=c$.
:::

:::

:::question{number="MISC-5" kind="additional_exercise" id="sol_4.misc.5" topic="Solving a determinant equation for x"}
#### Additional Question MISC-5

:::prompt
Solve the equations $\left|\begin{array}{ccc}x+a & x & x \\ x & x+a & x \\ x & x & x+a\end{array}\right|=0, a \neq 0 \quad$.
:::

:::solution{label="Solution"}
$$
\begin{aligned}
& \Rightarrow\left|\begin{array}{ccc}
x+a & x & x \\
x & x+a & x \\
x & x & x+a
\end{array}\right|=0 \\
& \Rightarrow\left|\begin{array}{ccc}
3 x+a & 3 x+a & 3 x+a \\
x & x+a & x \\
x & x & x+a
\end{array}\right|=0 \quad\left[R_{1} \rightarrow R_{1}+R_{2}+R_{3}\right] \\
& \Rightarrow(3 x+a)\left|\begin{array}{ccc}
1 & 1 & 1 \\
x & x+a & x \\
x & x & x+a
\end{array}\right|=0 \\
& \Rightarrow(3 x+a)\left|\begin{array}{ccc}
1 & 0 & 0 \\
x & a & 0 \\
x & 0 & a
\end{array}\right|=0 \quad\left[C_{2} \rightarrow C_{2}-C_{1} \text { and } C_{3} \rightarrow C_{3}-C_{1}\right]
\end{aligned}
$$

Expanding along $R_{1}$,

$$
\begin{aligned}
& \Rightarrow(3 x+a)\left[1 \times a^{2}\right]=0 \\
& \Rightarrow a^{2}(3 x+a)=0
\end{aligned}
$$

Since $a \neq 0$
Therefore,

$$
\begin{aligned}
& \Rightarrow 3 x+a=0 \\
& \Rightarrow x=-\frac{a}{3}
\end{aligned}
$$
:::

:::

:::question{number="MISC-6" kind="additional_exercise" id="sol_4.misc.6" topic="Proving a determinant identity"}
#### Additional Question MISC-6

:::prompt
Prove that $\left|\begin{array}{ccc}a^{2} & b c & a c+c^{2} \\ a^{2}+a b & b^{2} & a c \\ a b & b^{2}+b c & c^{2}\end{array}\right|=4 a^{2} b^{2} c^{2} \quad$.
:::

:::solution{label="Solution"}
$$
\begin{aligned}
\Delta & =\left|\begin{array}{ccc}
a^{2} & b c & a c+c^{2} \\
a^{2}+a b & b^{2} & a c \\
a b & b^{2}+b c & c^{2}
\end{array}\right| & & \\
& =a b c\left|\begin{array}{ccc}
a & c & a+c \\
a+b & b & a \\
b & b+c & c
\end{array}\right| & & {\left[\text { Taking out common factors } a, b \text { and } c \text { from } C_{1}, C_{2} \text { and } C_{3}\right] } \\
& =a b c\left|\begin{array}{ccc}
a & c & a+c \\
b & b-c & -c \\
b-a & b & -a
\end{array}\right| & & {\left[R_{2} \rightarrow R_{2}-R_{1} \text { and } R_{3} \rightarrow R_{3}-R_{1}\right] } \\
& =a b c\left|\begin{array}{ccc}
a & c & a+c \\
a+b & b & a \\
b-a & b & -a
\end{array}\right| & & {\left[R_{2} \rightarrow R_{2}+R_{1}\right] } \\
& =a b c\left|\begin{array}{ccc}
a & c & a+c \\
a+b & b & a \\
2 b & 2 b & 0
\end{array}\right| & & {\left[R_{3} \rightarrow R_{3}+R_{2}\right] } \\
& =2 a b^{2} c\left|\begin{array}{ccc}
a & c & a+c \\
a+b & b & a \\
1 & 1 & 0
\end{array}\right| & & \\
\Delta & =2 a b^{2} c\left|\begin{array}{ccc}
a & c-a & a+c \\
a+b & -a & a \\
1 & 0 & 0
\end{array}\right| & & {\left[C_{2} \rightarrow C_{2}-C_{1}\right] }
\end{aligned}
$$

Expanding along $R_{3}$,

$$
\begin{aligned}
\Delta & =2 a b^{2} c[a(c-a)+a(a+c)] \\
& =2 a b^{2} c\left[a c-a^{2}+a^{2}+a c\right] \\
& =2 a b^{2} c(2 a c) \\
& =4 a^{2} b^{2} c^{2}
\end{aligned}
$$

Hence, proved.
:::

:::

:::question{number="MISC-11" kind="additional_exercise" id="sol_4.misc.11" topic="Using properties of determinants to prove an identity"}
#### Additional Question MISC-11

:::prompt
Using properties of determinants prove that:

$$
\left|\begin{array}{lll}
\alpha & \alpha^{2} & \beta+\gamma \\
\beta & \beta^{2} & \gamma+\alpha \\
\gamma & \gamma^{2} & \alpha+\beta
\end{array}\right|=(\beta-\gamma)(\gamma-\alpha)(\alpha-\beta)(\alpha+\beta+\gamma)
$$
:::

:::solution{label="Solution"}
$$
\begin{array}{rlrl}
\Delta & =\left|\begin{array}{ccc}
\alpha & \alpha^{2} & \beta+\gamma \\
\beta & \beta^{2} & \gamma+\alpha \\
\gamma & \gamma^{2} & \alpha+\beta
\end{array}\right| & \\
& =\left|\begin{array}{ccc}
\alpha & \alpha^{2} & \beta+\gamma \\
\beta-\alpha & \beta^{2}-\alpha^{2} & \alpha-\beta \\
\gamma-\alpha & \gamma^{2}-\alpha^{2} & \alpha-\gamma
\end{array}\right| & & {\left[R_{2} \rightarrow R_{2}-R_{1} \text { and } R_{3} \rightarrow R_{3}-R_{1}\right]} \\
& =(\beta-\alpha)(\gamma-\alpha)\left|\begin{array}{ccc}
\alpha & \alpha^{2} & \beta+\gamma \\
1 & \beta+\alpha & -1 \\
1 & \gamma+\alpha & -1
\end{array}\right| & \\
& =(\beta-\alpha)(\gamma-\alpha)\left|\begin{array}{ccc}
\alpha & \alpha^{2} & \beta+\gamma \\
1 & \beta+\alpha & -1 \\
0 & \gamma-\beta & 0
\end{array}\right| & {\left[R_{3} \rightarrow R_{3}-R_{2}\right]} \\
& =(\beta-\alpha)(\gamma-\alpha)[-(\gamma-\beta)(-\alpha-\beta-\gamma)] & {\left[\text { Expanding along } R_{3}\right]} \\
& =(\beta-\alpha)(\gamma-\alpha)(\gamma-\beta)(\alpha+\beta+\gamma) &
\end{array} .=(\alpha-\beta)(\beta-\gamma)(\gamma-\alpha)(\alpha+\beta+\gamma),{ }=\frac{}{}
$$

Hence, proved.
:::

:::

:::question{number="MISC-12" kind="additional_exercise" id="sol_4.misc.12" topic="Using properties of determinants to prove an identity"}
#### Additional Question MISC-12

:::prompt
Using properties of determinants prove that:

$$
\left|\begin{array}{lll}
x & x^{2} & 1+p x^{3} \\
y & y^{2} & 1+p y^{3} \\
z & z^{2} & 1+p z^{3}
\end{array}\right|=(1+p x y z)(x-y)(y-z)(z-x)
$$
:::

:::solution{label="Solution"}
$$
\begin{aligned}
\Delta & =\left|\begin{array}{lll}
x & x^{2} & 1+p x^{3} \\
y & y^{2} & 1+p y^{3} \\
z & z^{2} & 1+p z^{3}
\end{array}\right| \\
\Delta & =\left|\begin{array}{ccc}
x & x^{2} & 1+p x^{3} \\
y-x & y^{2}-x^{2} & p\left(y^{3}-x^{3}\right) \\
z-x & z^{2}-x^{2} & p\left(z^{3}-x^{3}\right)
\end{array}\right| \quad\left[R_{2} \rightarrow R_{2}-R_{1} \text { and } R_{3} \rightarrow R_{3}-R_{1}\right] \\
\Delta & =(y-x)(z-x)\left|\begin{array}{ccc}
x & x^{2} & 1+p x^{3} \\
1 & y+x & p\left(y^{2}+x^{2}+x y\right) \\
1 & z+x & p\left(z^{2}+x^{2}+x z\right)
\end{array}\right| \\
\Delta & =(y-x)(z-x)\left|\begin{array}{ccc}
x & x^{2} & 1+p x^{3} \\
1 & y+x & p\left(y^{2}+x^{2}+x y\right) \\
0 & z-y & p(z-y)(x+y+z)
\end{array}\right| \quad\left[R_{3} \rightarrow R_{3}-R_{2}\right] \\
\Delta & =(y-x)(z-x)(z-y)\left|\begin{array}{ccc}
x & x^{2} & 1+p x^{3} \\
1 & y+x & p\left(y^{2}+x^{2}+x y\right) \\
0 & 1 & p(x+y+z)
\end{array}\right| \\
\Delta & \left.=(x-y)(z-y)(z-x)\left[(-1)(p)\left(x y^{2}+x^{3}+x^{2} y\right)+1+p x^{3}+p(x+y+z)(x y)\right] \quad \text { [Expanding along } R_{3}\right] \\
& =(x-y)(y-z)(z-x)\left[-p x y^{2}-p x^{3}-p x^{2} y+1+p x^{3}+p x^{2} y+p x y^{2}+p x y z\right] \\
& =(x-y)(y-z)(z-x)(1+p x y z)
\end{aligned}
$$

Hence, proved.
:::

:::

:::question{number="MISC-13" kind="additional_exercise" id="sol_4.misc.13" topic="Using properties of determinants to prove an identity"}
#### Additional Question MISC-13

:::prompt
Using properties of determinants prove that:

$$
\left|\begin{array}{ccc}
3 a & -a+b & -a+c \\
-b+a & 3 b & -b+c \\
-c+a & -c+b & 3 c
\end{array}\right|=3(a+b+c)(a b+b c+c a)
$$
:::

:::solution{label="Solution"}
$$
\begin{aligned}
\Delta & =\left|\begin{array}{ccc}
3 a & -a+b & -a+c \\
-b+a & 3 b & -b+c \\
-c+a & -c+b & 3 c
\end{array}\right| \\
& =\left|\begin{array}{cc}
a+b+c & -a+b \\
a+b+c & 3 b \\
a+b+c & -b+c
\end{array}\right| \quad\left[C_{1} \rightarrow C_{1}+C_{2}+C_{3}\right] \\
& =(a+b+c)\left|\begin{array}{ccc}
1 & -a+b & -a+c \\
1 & 3 b & -b+c \\
1 & -c+b & 3 c
\end{array}\right| \\
& =(a+b+c)\left|\begin{array}{ccc}
1 & -a+b & -a+c \\
0 & 2 b+a & a-b \\
0 & a-c & 2 c+a
\end{array}\right| \quad\left[R_{2} \rightarrow R_{2}-R_{1} \text { and } R_{3} \rightarrow R_{3}-R_{1}\right] \\
& =(a+b+c)[(2 b+a)(2 c+a)-(a-b)(a-c)] \quad\left[\text { Expanding along } C_{1}\right] \\
& =(a+b+c)\left[\begin{array}{cc}
\left.4 b c+2 a b+2 a c+a^{2}-a^{2}+a c+b a-b c\right] &
\end{array}\right. \\
& =(a+b+c)(3 a b+3 b c+3 a c) \\
& =3(a+b+c)(a b+b c+c a)
\end{aligned}
$$

Hence, proved.
:::

:::

:::question{number="MISC-14" kind="additional_exercise" id="sol_4.misc.14" topic="Using properties of determinants to prove an identity"}
#### Additional Question MISC-14

:::prompt
Using properties of determinants prove that:

$$
\left|\begin{array}{ccc}
1 & 1+p & 1+p+q \\
2 & 3+2 p & 4+3 p+2 q \\
3 & 6+3 p & 10+6 p+3 q
\end{array}\right|=1
$$
:::

:::solution{label="Solution"}
$$
\begin{aligned}
\Delta & =\left|\begin{array}{ccc}
1 & 1+p & 1+p+q \\
2 & 3+2 p & 4+3 p+2 q \\
3 & 6+3 p & 10+6 p+3 q
\end{array}\right| & & \\
& =\left|\begin{array}{ccc}
1 & 1+p & 1+p+q \\
0 & 1 & 2+p \\
0 & 3 & 7+3 p
\end{array}\right| & & {\left[R_{2} \rightarrow R_{2}-2 R_{1} \text { and } R_{3} \rightarrow R_{3}-3 R_{1}\right] } \\
& =\left|\begin{array}{ccc}
1 & 1+p & 1+p+q \\
0 & 1 & 2+p \\
0 & 0 & 1
\end{array}\right| & & {\left[R_{3} \rightarrow R_{3}-3 R_{2}\right] } \\
& =1\left|\begin{array}{cc}
1 & 2+p \\
0 & 1
\end{array}\right| & & {\left[\text { Expanding along } C_{1}\right] } \\
& =1(1-0)=1 & &
\end{aligned}
$$

Hence, proved.
:::

:::

:::question{number="MISC-15" kind="additional_exercise" id="sol_4.misc.15" topic="Using properties of determinants to prove an identity"}
#### Additional Question MISC-15

:::prompt
Using properties of determinants prove that:

$$
\left|\begin{array}{ccc}
\sin \alpha & \cos \alpha & \cos (\alpha+\delta) \\
\sin \beta & \cos \beta & \cos (\beta+\delta) \\
\sin \gamma & \cos \gamma & \cos (\gamma+\delta)
\end{array}\right|=0
$$
:::

:::solution{label="Solution"}
$$
\begin{aligned}
\Delta & =\left|\begin{array}{lll}
\sin \alpha & \cos \alpha & \cos (\alpha+\delta) \\
\sin \beta & \cos \beta & \cos (\beta+\delta) \\
\sin \gamma & \cos \gamma & \cos (\gamma+\delta)
\end{array}\right| \\
& =\frac{1}{\sin \delta \cos \delta}\left|\begin{array}{lll}
\sin \alpha \sin \delta & \cos \alpha \cos \delta & \cos \alpha \cos \delta-\sin \alpha \sin \delta \\
\sin \beta \sin \delta & \cos \beta \cos \delta & \cos \beta \cos \delta-\sin \beta \sin \delta \\
\sin \gamma \sin \delta & \cos \gamma \cos \delta & \cos \gamma \cos \delta-\sin \gamma \sin \delta
\end{array}\right| \\
& =\frac{1}{\sin \delta \cos \delta}\left|\begin{array}{lll}
\cos \alpha \cos \delta & \cos \alpha \cos \delta & \cos \alpha \cos \delta-\sin \alpha \sin \delta \\
\cos \beta \cos \delta & \cos \beta \cos \delta & \cos \beta \cos \delta-\sin \beta \sin \delta \\
\cos \gamma \cos \delta & \cos \gamma \cos \delta & \cos \gamma \cos \delta-\sin \gamma \sin \delta
\end{array}\right| \quad\left[C_{1} \rightarrow C_{1}+C_{3}\right]
\end{aligned}
$$

Here, two columns $C_{1}$ and $C_{2}$ are identical.
Therefore, $\Delta=0$
Hence, proved.
:::

:::

:::question{number="MISC-17" kind="additional_exercise" id="sol_4.misc.17" topic="Determinant identity for terms in A.P."}
#### Additional Question MISC-17

:::prompt
If $a, b, c$ are in A.P, then the determinant $\left|\begin{array}{lll}x+2 & x+3 & x+2 a \\ x+3 & x+4 & x+2 b \\ x+4 & x+5 & x+2 c\end{array}\right|$ is
(A) 0
(B) 1
(C) $x$
(D) $2 x$
:::

:::solution{label="Solution"}
$$
\begin{aligned}
\Delta & =\left|\begin{array}{ccc}
x+2 & x+3 & x+2 a \\
x+3 & x+4 & x+2 b \\
x+4 & x+5 & x+2 c
\end{array}\right| & \\
& =\left|\begin{array}{ccc}
x+2 & x+3 & x+2 a \\
x+3 & x+4 & x+(a+c) \\
x+4 & x+5 & x+2 c
\end{array}\right| & (2 b=a+c \text { as } a, b, c \text { are in A.P }) \\
& =\left|\begin{array}{ccc}
-1 & -1 & a-c \\
x+3 & x+4 & x+(a+c) \\
1 & 1 & c-a
\end{array}\right| & {\left[R_{1} \rightarrow R_{1}-R_{2} \text { and } R_{3} \rightarrow R_{3}-R_{2}\right] } \\
& =\left|\begin{array}{ccc}
0 & 0 & 0 \\
x+3 & x+4 & x+a+c \\
1 & 1 & c-a
\end{array}\right| & {\left[R_{1} \rightarrow R_{1}+R_{3}\right] }
\end{aligned}
$$

Here, all the elements of the first row are zero.

Hence, we have $\Delta=0$
Thus, the correct option is A.
:::

:::
