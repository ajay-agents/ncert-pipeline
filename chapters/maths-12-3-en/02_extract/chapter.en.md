---
subject: maths
class: 12
chapter: 3
lang: en
title: "Matrices"
---

# Matrices

## Examples

:::example{number="1" kind="example" id="ex_3.1" topic="Representing data as a matrix"}
#### Example 1

:::prompt
Consider the following information regarding the number of men and women workers in three factories I, II and III

|  | Men workers | Women workers |
| :--- | :--- | :--- |
| I | 30 | 25 |
| II | 25 | 31 |
| III | 27 | 26 |

Represent the above information in the form of a $3 \times 2$ matrix. What does the entry in the third row and second column represent?
:::

:::solution{label="Solution"}
The information is represented in the form of a $3 \times 2$ matrix as follows:

$$
A=\left[\begin{array}{ll}
30 & 25 \\
25 & 31 \\
27 & 26
\end{array}\right]
$$

The entry in the third row and second column represents the number of women workers in factory III.
:::

:::

:::example{number="2" kind="example" id="ex_3.2" topic="Possible orders for a given element count"}
#### Example 2

:::prompt
If a matrix has 8 elements, what are the possible orders it can have?
:::

:::solution{label="Solution"}
We know that if a matrix is of order $m \times n$, it has $m n$ elements. Thus, to find all possible orders of a matrix with 8 elements, we will find all ordered pairs of natural numbers, whose product is 8.
Thus, all possible ordered pairs are (1, 8), (8, 1), (4, 2), $(2,4)$
Hence, possible orders are 1 × 8, 8 × 1, 4 × 2, 2 × 4
:::

:::

:::example{number="3" kind="example" id="ex_3.3" topic="Constructing a matrix from a formula"}
#### Example 3

:::prompt
Construct a $3 \times 2$ matrix whose elements are given by $a_{i j}=\frac{1}{2}|i-3 j|$.
:::

:::solution{label="Solution"}
In general a $3 \times 2$ matrix is given by $\mathrm{A}=\left[\begin{array}{ll}a_{11} & a_{12} \\ a_{21} & a_{22} \\ a_{31} & a_{32}\end{array}\right]$.
Now

$$
a_{i j}=\frac{1}{2}|i-3 j|, i=1,2,3 \text { and } j=1,2 .
$$

Therefore

$$
\begin{array}{ll}
a_{11}=\frac{1}{2}|1-3 \times 1|=1 & a_{12}=\frac{1}{2}|1-3 \times 2|=\frac{5}{2} \\
a_{21}=\frac{1}{2}|2-3 \times 1|=\frac{1}{2} & a_{22}=\frac{1}{2}|2-3 \times 2|=2 \\
a_{31}=\frac{1}{2}|3-3 \times 1|=0 & a_{32}=\frac{1}{2}|3-3 \times 2|=\frac{3}{2}
\end{array}
$$

Hence the required matrix is given by $\mathrm{A}=\left[\begin{array}{cc}1 & \frac{5}{2} \\ \frac{1}{2} & 2 \\ 0 & \frac{3}{2}\end{array}\right]$.
:::

:::

:::example{number="4" kind="example" id="ex_3.4" topic="Solving for unknowns by matrix equality"}
#### Example 4

:::prompt
If $\left[\begin{array}{ccc}x+3 & z+4 & 2 y-7 \\ -6 & a-1 & 0 \\ b-3 & -21 & 0\end{array}\right]=\left[\begin{array}{ccc}0 & 6 & 3 y-2 \\ -6 & -3 & 2 c+2 \\ 2 b+4 & -21 & 0\end{array}\right]$
Find the values of $a, b, c, x, y$ and $z$.
:::

:::solution{label="Solution"}
As the given matrices are equal, therefore, their corresponding elements must be equal. Comparing the corresponding elements, we get

$$
\begin{array}{rlrlrl}
x+3 & =0, & z+4 & =6, & 2 y-7 & =3 y-2 \\
a-1 & =-3, & 0 & =2 c+2 & b-3 & =2 b+4,
\end{array}
$$

Simplifying, we get

$$
a=-2, b=-7, c=-1, x=-3, y=-5, z=2
$$
:::

:::

:::example{number="5" kind="example" id="ex_3.5" topic="Solving for unknowns by matrix equality"}
#### Example 5

:::prompt
Find the values of $a, b, c$, and $d$ from the following equation:

$$
\left[\begin{array}{cc}
2 a+b & a-2 b \\
5 c-d & 4 c+3 d
\end{array}\right]=\left[\begin{array}{cc}
4 & -3 \\
11 & 24
\end{array}\right]
$$
:::

:::solution{label="Solution"}
By equality of two matrices, equating the corresponding elements, we get

$$
\begin{array}{rlrl} 
& 2 a+b & =4 & 5 c-d
\end{array}=11 . ⿱ r d c+3 d=24
$$

Solving these equations, we get

$$
a=1, b=2, c=3 \text { and } d=4
$$
:::

:::

:::example{number="6" kind="example" id="ex_3.6" topic="Addition of matrices"}
#### Example 6

:::prompt
Given $\mathrm{A}=\left[\begin{array}{ccc}\sqrt{3} & 1 & -1 \\ 2 & 3 & 0\end{array}\right]$ and $\mathrm{B}=\left[\begin{array}{ccc}2 & \sqrt{5} & 1 \\ -2 & 3 & \frac{1}{2}\end{array}\right]$, find $\mathrm{A}+\mathrm{B}$
Since A, B are of the same order 2 × 3. Therefore, addition of A and B is defined and is given by

$$
A+B=\left[\begin{array}{ccc}
2+\sqrt{3} & 1+\sqrt{5} & 1-1 \\
2-2 & 3+3 & 0+\frac{1}{2}
\end{array}\right]=\left[\begin{array}{ccc}
2+\sqrt{3} & 1+\sqrt{5} & 0 \\
0 & 6 & \frac{1}{2}
\end{array}\right]
$$

- Note

1. We emphasise that if A and B are not of the same order, then $\mathrm{A}+\mathrm{B}$ is not defined. For example if $\mathrm{A}=\left[\begin{array}{ll}2 & 3 \\ 1 & 0\end{array}\right], \mathrm{B}=\left[\begin{array}{lll}1 & 2 & 3 \\ 1 & 0 & 1\end{array}\right]$, then $\mathrm{A}+\mathrm{B}$ is not defined.
2. We may observe that addition of matrices is an example of binary operation on the set of matrices of the same order.

###
:::

:::

:::example{number="7" kind="example" id="ex_3.7" topic="Scalar multiplication and subtraction of matrices"}
#### Example 7

:::prompt
If $\mathrm{A}=\left[\begin{array}{lll}1 & 2 & 3 \\ 2 & 3 & 1\end{array}\right]$ and $\mathrm{B}=\left[\begin{array}{rrr}3 & -1 & 3 \\ -1 & 0 & 2\end{array}\right]$, then find $2 \mathrm{~A}-\mathrm{B}$.
:::

:::solution{label="Solution"}
We have

$$
\begin{aligned}
2 A-B & =2 \begin{array}{lll}
1 & 2 & 3 \\
2 & 3 & 1
\end{array}-\begin{array}{rrr}
3 & -1 & 3 \\
-1 & 0 & 2
\end{array} \\
& =\left[\begin{array}{lll}
2 & 4 & 6 \\
4 & 6 & 2
\end{array}\right]+\left[\begin{array}{rrr}
-3 & 1 & -3 \\
1 & 0 & -2
\end{array}\right] \\
& =\left[\begin{array}{lll}
2-3 & 4+1 & 6-3 \\
4+1 & 6+0 & 2-2
\end{array}\right]=\left[\begin{array}{ccc}
-1 & 5 & 3 \\
5 & 6 & 0
\end{array}\right]
\end{aligned}
$$

###
:::

:::

:::example{number="8" kind="example" id="ex_3.8" topic="Solving a matrix equation for X"}
#### Example 8

:::prompt
If $\mathrm{A}=\left[\begin{array}{rr}8 & 0 \\ 4 & -2 \\ 3 & 6\end{array}\right]$ and $\mathrm{B}=\left[\begin{array}{cc}2 & -2 \\ 4 & 2 \\ -5 & 1\end{array}\right]$, then find the matrix $X$, such that $2 \mathrm{~A}+3 \mathrm{X}=5 \mathrm{~B}$.
:::

:::solution{label="Solution"}
We have $2 \mathrm{~A}+3 \mathrm{X}=5 \mathrm{~B}$
or

$$
2 A+3 A-2 A=5 B-2 A
$$

or

$$
2 \mathrm{~A}-2 \mathrm{~A}+3 \mathrm{X}=5 \mathrm{~B}-2 \mathrm{~A} \quad \text { (Matrix addition is commutative) }
$$

or

$$
\mathrm{O}+3 \mathrm{X}=5 \mathrm{~B}-2 \mathrm{~A} \quad(-2 \mathrm{~A} \text { is the additive inverse of } 2 \mathrm{~A})
$$

or

$$
3 \mathrm{X}=5 \mathrm{~B}-2 \mathrm{~A} \quad(\mathrm{O} \text { is the additive identity })
$$

or

$$
X=\frac{1}{3}(5 B-2 A)
$$

or

$$
X=\frac{1}{3}\left(5\left[\begin{array}{cc}
2 & -2 \\
4 & 2 \\
-5 & 1
\end{array}\right]-2\left[\begin{array}{cc}
8 & 0 \\
4 & -2 \\
3 & 6
\end{array}\right]\right)=\frac{1}{3}\left(\left[\begin{array}{cc}
10 & -10 \\
20 & 10 \\
-25 & 5
\end{array}\right]+\left[\begin{array}{cc}
-16 & 0 \\
-8 & 4 \\
-6 & -12
\end{array}\right]\right)
$$

$$
=\frac{1}{3}\left[\begin{array}{cc}
10-16 & -10+0 \\
20-8 & 10+4 \\
-25-6 & 5-12
\end{array}\right]=\frac{1}{3}\left[\begin{array}{cc}
-6 & -10 \\
12 & 14 \\
-31 & -7
\end{array}\right]=\left[\begin{array}{cc}
-2 & \frac{-10}{3} \\
4 & \frac{14}{3} \\
\frac{-31}{3} & \frac{-7}{3}
\end{array}\right]
$$
:::

:::

:::example{number="9" kind="example" id="ex_3.9" topic="Solving simultaneous matrix equations"}
#### Example 9

:::prompt
Find X and Y , if $\mathrm{X}+\mathrm{Y}=\left[\begin{array}{ll}5 & 2 \\ 0 & 9\end{array}\right]$ and $\mathrm{X}-\mathrm{Y}=\left[\begin{array}{cc}3 & 6 \\ 0 & -1\end{array}\right]$.
:::

:::solution{label="Solution"}
We have $(\mathrm{X}+\mathrm{Y})+(\mathrm{X}-\mathrm{Y})=\left[\begin{array}{ll}5 & 2 \\ 0 & 9\end{array}\right]+\left[\begin{array}{cc}3 & 6 \\ 0 & -1\end{array}\right]$.
or

$$
(\mathrm{X}+\mathrm{X})+(\mathrm{Y}-\mathrm{Y})=\left[\begin{array}{ll}
8 & 8 \\
0 & 8
\end{array}\right] \Rightarrow 2 \mathrm{X}=\left[\begin{array}{ll}
8 & 8 \\
0 & 8
\end{array}\right]
$$

or

$$
\mathrm{X}=\frac{1}{2}\left[\begin{array}{ll}
8 & 8 \\
0 & 8
\end{array}\right]=\left[\begin{array}{ll}
4 & 4 \\
0 & 4
\end{array}\right]
$$

Also

$$
(X+Y)-(X-Y)=\left[\begin{array}{ll}
5 & 2 \\
0 & 9
\end{array}\right]-\left[\begin{array}{rr}
3 & 6 \\
0 & -1
\end{array}\right]
$$

or

$$
(\mathrm{X}-\mathrm{X})+(\mathrm{Y}+\mathrm{Y})=\left[\begin{array}{cc}
5-3 & 2-6 \\
0 & 9+1
\end{array}\right] \Rightarrow 2 \mathrm{Y}=\left[\begin{array}{cc}
2 & -4 \\
0 & 10
\end{array}\right]
$$

or

$$
\mathrm{Y}=\frac{1}{2}\left[\begin{array}{rr}
2 & -4 \\
0 & 10
\end{array}\right]=\left[\begin{array}{rr}
1 & -2 \\
0 & 5
\end{array}\right]
$$
:::

:::

:::example{number="10" kind="example" id="ex_3.10" topic="Solving for unknowns in a matrix equation"}
#### Example 10

:::prompt
Find the values of $x$ and $y$ from the following equation:

$$
2\left[\begin{array}{cc}
x & 5 \\
7 & y-3
\end{array}\right]+\left[\begin{array}{cr}
3 & -4 \\
1 & 2
\end{array}\right]=\left[\begin{array}{cc}
7 & 6 \\
15 & 14
\end{array}\right]
$$
:::

:::solution{label="Solution"}
We have

$$
2\left[\begin{array}{cc}
x & 5 \\
7 & y-3
\end{array}\right]+\left[\begin{array}{cc}
3 & -4 \\
1 & 2
\end{array}\right]=\left[\begin{array}{cc}
7 & 6 \\
15 & 14
\end{array}\right] \Rightarrow\left[\begin{array}{cc}
2 x & 10 \\
14 & 2 y-6
\end{array}\right]+\left[\begin{array}{cc}
3 & -4 \\
1 & 2
\end{array}\right]=\left[\begin{array}{cc}
7 & 6 \\
15 & 14
\end{array}\right]
$$

or

$$
\left[\begin{array}{cc}
2 x+3 & 10-4 \\
14+1 & 2 y-6+2
\end{array}\right]=\left[\begin{array}{cc}
7 & 6 \\
15 & 14
\end{array}\right] \Rightarrow\left[\begin{array}{cc}
2 x+3 & 6 \\
15 & 2 y-4
\end{array}\right]=\left[\begin{array}{cc}
7 & 6 \\
15 & 14
\end{array}\right]
$$

or

$$
2 x+3=7 \quad \text { and } \quad 2 y-4=14 \quad \text { (Why?) }
$$

or

$$
2 x=7-3 \quad \text { and } \quad 2 y=18
$$

or

$$
x=\frac{4}{2} \quad \text { and } \quad y=\frac{18}{2}
$$

i.e.

$$
x=2 \quad \text { and } \quad y=9 \text {. }
$$
:::

:::

:::example{number="11" kind="example" id="ex_3.11" topic="Matrix addition and subtraction - rice sales"}
#### Example 11

:::prompt
Two farmers Ramkishan and Gurcharan Singh cultivates only three varieties of rice namely Basmati, Permal and Naura. The sale (in Rupees) of these varieties of rice by both the farmers in the month of September and October are given by the following matrices A and B.

September Sales (in Rupees)

$$
\mathrm{A}=\left[\begin{array}{ccc}
\text { Basmati } & \text { Permal } & \text { Naura } \\
10,000 & 20,000 & 30,000 \\
50,000 & 30,000 & 10,000
\end{array}\right] \begin{aligned}
& \text { Ramkishan } \\
& \text { Gurcharan Singh }
\end{aligned}
$$

October Sales (in Rupees)

$$
B=\left[\begin{array}{ccc}
\text { Basmati } & \text { Permal } & \text { Naura } \\
5000 & 10,000 & 6000 \\
20,000 & 10,000 & 10,000
\end{array}\right] \text { Ramkishan }
$$

(i) Find the combined sales in September and October for each farmer in each variety.
(ii) Find the decrease in sales from September to October.
(iii) If both farmers receive 2\% profit on gross sales, compute the profit for each farmer and for each variety sold in October.
:::

:::solution{label="Solution"}
(i) Combined sales in September and October for each farmer in each variety is given by
$$
\mathrm{A}+\mathrm{B}=\left[\begin{array}{ccc}
\text { Basmati } & \text { Permal } & \text { Naura } \\
15,000 & 30,000 & 36,000 \\
70,000 & 40,000 & 20,000
\end{array}\right] \begin{aligned}
& \text { Ramkishan } \\
& \text { Gurcharan Singh }
\end{aligned}
$$

(ii) Change in sales from September to October is given by
$$
A-B=\left[\begin{array}{ccc}
\text { Basmati } & \text { Permal } & \text { Naura } \\
5000 & 10,000 & 24,000 \\
30,000 & 20,000 & 0
\end{array}\right] \begin{aligned}
& \text { Ramkishan } \\
& \text { Gurcharan Singh }
\end{aligned}
$$
(iii) $$
\begin{aligned}
& 2 \% \text { of } \mathrm{B}=\frac{2}{100} \times \mathrm{B}=0.02 \times \mathrm{B} \\
&=0.02\left[\begin{array}{ccc}
\text { Basmati } & \text { Permal } & \text { Naura } \\
5000 & 10,000 & 6000 \\
20,000 & 10,000 & 10,000
\end{array}\right] \text { Ramkishan } \\
&=\left[\begin{array}{ccc}
\text { Basmati } & \text { Permal } & \text { Naura } \\
100 & 200 & 120 \\
400 & 200 & 200
\end{array}\right] \text { Ramkishan } \\
& \text { Gurcharan Singh }
\end{aligned}
$$

Thus, in October Ramkishan receives ₹ 100 , ₹ 200 and ₹ 120 as profit in the sale of each variety of rice, respectively, and Grucharan Singh receives profit of ₹400, ₹ 200 and ₹ 200 in the sale of each variety of rice, respectively.

###
:::

:::

:::example{number="12" kind="example" id="ex_3.12" topic="Associativity of matrix multiplication"}
#### Example 12

:::prompt
Find AB , if $\mathrm{A}=\left[\begin{array}{ll}6 & 9 \\ 2 & 3\end{array}\right]$ and $\mathrm{B}=\left[\begin{array}{lll}2 & 6 & 0 \\ 7 & 9 & 8\end{array}\right]$.
:::

:::solution{label="Solution"}
The matrix A has 2 columns which is equal to the number of rows of B. Hence AB is defined. Now

$$
\begin{aligned}
\mathrm{AB} & =\left[\begin{array}{lll}
6(2)+9(7) & 6(6)+9(9) & 6(0)+9(8) \\
2(2)+3(7) & 2(6)+3(9) & 2(0)+3(8)
\end{array}\right] \\
& =\left[\begin{array}{rrr}
12+63 & 36+81 & 0+72 \\
4+21 & 12+27 & 0+24
\end{array}\right]=\left[\begin{array}{ccc}
75 & 117 & 72 \\
25 & 39 & 24
\end{array}\right]
\end{aligned}
$$

Remark If AB is defined, then BA need not be defined. In the above example, AB is defined but BA is not defined because B has 3 column while A has only 2 (and not 3 ) rows. If A, B are, respectively $m \times n, k \times l$ matrices, then both AB and BA are defined if and only if $n=k$ and $l=m$. In particular, if both A and B are square matrices of the same order, then both AB and BA are defined.

##
:::

:::

:::example{number="13" kind="example" id="ex_3.13" topic="Non-commutativity of matrix multiplication"}
#### Example 13

:::prompt
If $\mathrm{A}=\left[\begin{array}{rrr}1 & -2 & 3 \\ -4 & 2 & 5\end{array}\right]$ and $\mathrm{B}=\left[\begin{array}{ll}2 & 3 \\ 4 & 5 \\ 2 & 1\end{array}\right]$, then find $\mathrm{AB}, \mathrm{BA}$. Show that $A B \neq B A$.
:::

:::solution{label="Solution"}
Since A is a $2 \times 3$ matrix and B is $3 \times 2$ matrix. Hence AB and BA are both defined and are matrices of order 2 × 2 and 3 × 3, respectively. Note that

$$
\mathrm{AB}=\left[\begin{array}{rrr}
1 & -2 & 3 \\
-4 & 2 & 5
\end{array}\right]\left[\begin{array}{ll}
2 & 3 \\
4 & 5 \\
2 & 1
\end{array}\right]=\left[\begin{array}{cc}
2-8+6 & 3-10+3 \\
-8+8+10 & -12+10+5
\end{array}\right]=\left[\begin{array}{cr}
0 & -4 \\
10 & 3
\end{array}\right]
$$

and

$$
\mathrm{BA}=\left[\begin{array}{ll}
2 & 3 \\
4 & 5 \\
2 & 1
\end{array}\right]\left[\begin{array}{rrr}
1 & -2 & 3 \\
-4 & 2 & 5
\end{array}\right]=\left[\begin{array}{ccc}
2-12 & -4+6 & 6+15 \\
4-20 & -8+10 & 12+25 \\
2-4 & -4+2 & 6+5
\end{array}\right]=\left[\begin{array}{ccc}
-10 & 2 & 21 \\
-16 & 2 & 37 \\
-2 & -2 & 11
\end{array}\right]
$$

Clearly $\mathrm{AB} \neq \mathrm{BA}$
:::

:::

:::example{number="14" kind="example" id="ex_3.14" topic="Non-commutativity of matrix multiplication"}
#### Example 14

:::prompt
If $\mathrm{A}=\left[\begin{array}{rr}1 & 0 \\ 0 & -1\end{array}\right]$ and $\mathrm{B}=\left[\begin{array}{ll}0 & 1 \\ 1 & 0\end{array}\right]$, then $\mathrm{AB}=\left[\begin{array}{rr}0 & 1 \\ -1 & 0\end{array}\right]$.
and

$$
\mathrm{BA}=\left[\begin{array}{rr}
0 & -1 \\
1 & 0
\end{array}\right] . \text { Clearly } \mathrm{AB} \neq \mathrm{BA} .
$$

Thus matrix multiplication is not commutative.
:::

:::

:::example{number="15" kind="example" id="ex_3.15" topic="Zero product of non-zero matrices"}
#### Example 15

:::prompt
Find AB , if $\mathrm{A}=\left[\begin{array}{rr}0 & -1 \\ 0 & 2\end{array}\right]$ and $\mathrm{B}=\left[\begin{array}{ll}3 & 5 \\ 0 & 0\end{array}\right]$.
:::

:::solution{label="Solution"}
We have $\mathrm{AB}=\left[\begin{array}{rr}0 & -1 \\ 0 & 2\end{array}\right]\left[\begin{array}{ll}3 & 5 \\ 0 & 0\end{array}\right]=\left[\begin{array}{ll}0 & 0 \\ 0 & 0\end{array}\right]$.
Thus, if the product of two matrices is a zero matrix, it is not necessary that one of the matrices is a zero matrix.
:::

:::

:::example{number="16" kind="example" id="ex_3.16" topic="Verifying associativity of multiplication"}
#### Example 16

:::prompt
If $\mathrm{A}=\left[\begin{array}{ccc}1 & 1 & -1 \\ 2 & 0 & 3 \\ 3 & -1 & 2\end{array}\right], \mathrm{B}=\left[\begin{array}{rr}1 & 3 \\ 0 & 2 \\ -1 & 4\end{array}\right]$ and $\mathrm{C}=\left[\begin{array}{cccc}1 & 2 & 3 & -4 \\ 2 & 0 & -2 & 1\end{array}\right]$, find A(BC), (AB)C and show that $(\mathrm{AB}) \mathrm{C}=\mathrm{A}(\mathrm{BC})$.
:::

:::solution{label="Solution"}
We have $\mathrm{AB}=\left[\begin{array}{rcr}1 & 1 & -1 \\ 2 & 0 & 3 \\ 3 & -1 & 2\end{array}\right]\left[\begin{array}{rr}1 & 3 \\ 0 & 2 \\ -1 & 4\end{array}\right]=\left[\begin{array}{ll}1+0+1 & 3+2-4 \\ 2+0-3 & 6+0+12 \\ 3+0-2 & 9-2+8\end{array}\right]=\left[\begin{array}{rc}2 & 1 \\ -1 & 18 \\ 1 & 15\end{array}\right]$
$(\mathrm{AB})(\mathrm{C})=\left[\begin{array}{rc}2 & 1 \\ -1 & 18 \\ 1 & 15\end{array}\right]\left[\begin{array}{rrrr}1 & 2 & 3 & -4 \\ 2 & 0 & -2 & 1\end{array}\right]=\left[\begin{array}{rrrr}2+2 & 4+0 & 6-2 & -8+1 \\ -1+36 & -2+0 & -3-36 & 4+18 \\ 1+30 & 2+0 & 3-30 & -4+15\end{array}\right]$

$$
=\left[\begin{array}{cccc}
4 & 4 & 4 & -7 \\
35 & -2 & -39 & 22 \\
31 & 2 & -27 & 11
\end{array}\right]
$$

Now

$$
\begin{aligned}
\mathrm{BC} & =\left[\begin{array}{rr}
1 & 3 \\
0 & 2 \\
-1 & 4
\end{array}\right]\left[\begin{array}{rrrr}
1 & 2 & 3 & -4 \\
2 & 0 & -2 & 1
\end{array}\right]=\left[\begin{array}{rrrr}
1+6 & 2+0 & 3-6 & -4+3 \\
0+4 & 0+0 & 0-4 & 0+2 \\
-1+8 & -2+0 & -3-8 & 4+4
\end{array}\right] \\
& =\left[\begin{array}{rrrr}
7 & 2 & -3 & -1 \\
4 & 0 & -4 & 2 \\
7 & -2 & -11 & 8
\end{array}\right]
\end{aligned}
$$

Therefore

$$
\mathrm{A}(\mathrm{BC})=\left[\begin{array}{rrr}
1 & 1 & -1 \\
2 & 0 & 3 \\
3 & -1 & 2
\end{array}\right]\left[\begin{array}{rrrr}
7 & 2 & -3 & -1 \\
4 & 0 & -4 & 2 \\
7 & -2 & -11 & 8
\end{array}\right]
$$

$$
\begin{aligned}
& =\left[\begin{array}{cccc}
7+4-7 & 2+0+2 & -3-4+11 & -1+2-8 \\
14+0+21 & 4+0-6 & -6+0-33 & -2+0+24 \\
21-4+14 & 6+0-4 & -9+4-22 & -3-2+16
\end{array}\right] \\
& =\left[\begin{array}{cccc}
4 & 4 & 4 & -7 \\
35 & -2 & -39 & 22 \\
31 & 2 & -27 & 11
\end{array}\right] . \text { Clearly, (AB) } \mathrm{C}=\mathrm{A}(\mathrm{BC})
\end{aligned}
$$
:::

:::

:::example{number="17" kind="example" id="ex_3.17" topic="Distributivity of matrix multiplication"}
#### Example 17

:::prompt
If $\mathrm{A}=\left[\begin{array}{rrr}0 & 6 & 7 \\ -6 & 0 & 8 \\ 7 & -8 & 0\end{array}\right], \mathrm{B}=\left[\begin{array}{lll}0 & 1 & 1 \\ 1 & 0 & 2 \\ 1 & 2 & 0\end{array}\right], \mathrm{C}=\left[\begin{array}{r}2 \\ -2 \\ 3\end{array}\right]$
Calculate AC, BC and $(\mathrm{A}+\mathrm{B}) \mathrm{C}$. Also, verify that $(\mathrm{A}+\mathrm{B}) \mathrm{C}=\mathrm{AC}+\mathrm{BC}$
:::

:::solution{label="Solution"}
Now, $\mathrm{A}+\mathrm{B}=\left[\begin{array}{ccc}0 & 7 & 8 \\ -5 & 0 & 10 \\ 8 & -6 & 0\end{array}\right]$

So

$$
(\mathrm{A}+\mathrm{B}) \mathrm{C}=\left[\begin{array}{rrc}
0 & 7 & 8 \\
-5 & 0 & 10 \\
8 & -6 & 0
\end{array}\right]\left[\begin{array}{r}
2 \\
-2 \\
3
\end{array}\right]=\left[\begin{array}{r}
0-14+24 \\
-10+0+30 \\
16+12+0
\end{array}\right]=\left[\begin{array}{l}
10 \\
20 \\
28
\end{array}\right]
$$

Further

$$
\mathrm{AC}=\left[\begin{array}{ccc}
0 & 6 & 7 \\
-6 & 0 & 8 \\
7 & -8 & 0
\end{array}\right]\left[\begin{array}{r}
2 \\
-2 \\
3
\end{array}\right]=\left[\begin{array}{r}
0-12+21 \\
-12+0+24 \\
14+16+0
\end{array}\right]=\left[\begin{array}{c}
9 \\
12 \\
30
\end{array}\right]
$$

and

$$
\mathrm{BC}=\left[\begin{array}{lll}
0 & 1 & 1 \\
1 & 0 & 2 \\
1 & 2 & 0
\end{array}\right]\left[\begin{array}{r}
2 \\
-2 \\
3
\end{array}\right]=\left[\begin{array}{l}
0-2+3 \\
2+0+6 \\
2-4+0
\end{array}\right]=\left[\begin{array}{r}
1 \\
8 \\
-2
\end{array}\right]
$$

So

$$
\mathrm{AC}+\mathrm{BC}=\left[\begin{array}{l}
9 \\
12 \\
30
\end{array}\right]+\left[\begin{array}{c}
1 \\
8 \\
-2
\end{array}\right]=\left[\begin{array}{l}
10 \\
20 \\
28
\end{array}\right]
$$

Clearly,

$$
(\mathrm{A}+\mathrm{B}) \mathrm{C}=\mathrm{AC}+\mathrm{BC}
$$
:::

:::

:::example{number="18" kind="example" id="ex_3.18" topic="Matrix polynomial identity"}
#### Example 18

:::prompt
If $\mathrm{A}=\left[\begin{array}{rrr}1 & 2 & 3 \\ 3 & -2 & 1 \\ 4 & 2 & 1\end{array}\right]$, then show that $\mathrm{A}^{3}-23 \mathrm{~A}-40 \mathrm{I}=\mathrm{O}$
:::

:::solution{label="Solution"}
We have $\mathrm{A}^{2}=\mathrm{A} . \mathrm{A}=\left[\begin{array}{rrr}1 & 2 & 3 \\ 3 & -2 & 1 \\ 4 & 2 & 1\end{array}\right]\left[\begin{array}{ccc}1 & 2 & 3 \\ 3 & -2 & 1 \\ 4 & 2 & 1\end{array}\right]=\left[\begin{array}{llr}19 & 4 & 8 \\ 1 & 12 & 8 \\ 14 & 6 & 15\end{array}\right]$

So

$$
A^{3}=A A^{2}=\left[\begin{array}{rrr}
1 & 2 & 3 \\
3 & -2 & 1 \\
4 & 2 & 1
\end{array}\right]\left[\begin{array}{llr}
19 & 4 & 8 \\
1 & 12 & 8 \\
14 & 6 & 15
\end{array}\right]=\left[\begin{array}{lll}
63 & 46 & 69 \\
69 & -6 & 23 \\
92 & 46 & 63
\end{array}\right]
$$

Now

$$
\begin{aligned}
A^{3}-23 A-40 I & =\left[\begin{array}{lll}
63 & 46 & 69 \\
69 & -6 & 23 \\
92 & 46 & 63
\end{array}\right]-23\left[\begin{array}{ccc}
1 & 2 & 3 \\
3 & -2 & 1 \\
4 & 2 & 1
\end{array}\right]-40\left[\begin{array}{ccc}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{array}\right] \\
& =\left[\begin{array}{lll}
63 & 46 & 69 \\
69 & -6 & 23 \\
92 & 46 & 63
\end{array}\right]+\left[\begin{array}{ccc}
-23 & -46 & -69 \\
-69 & 46 & -23 \\
-92 & -46 & -23
\end{array}\right]+\left[\begin{array}{ccc}
-40 & 0 & 0 \\
0 & -40 & 0 \\
0 & 0 & -40
\end{array}\right] \\
& =\left[\begin{array}{lll}
63-23-40 & 46-46+0 & 69-69+0 \\
69-69+0 & -6+46-40 & 23-23+0 \\
92-92+0 & 46-46+0 & 63-23-40
\end{array}\right] \\
& =\left[\begin{array}{lll}
0 & 0 & 0 \\
0 & 0 & 0 \\
0 & 0 & 0
\end{array}\right]=\mathrm{O}
\end{aligned}
$$
:::

:::

:::example{number="19" kind="example" id="ex_3.19" topic="Matrix multiplication - campaign costs"}
#### Example 19

:::prompt
In a legislative assembly election, a political group hired a public relations firm to promote its candidate in three ways: telephone, house calls, and letters. The cost per contact (in paise) is given in matrix A as

$$
\mathrm{A}=\left[\begin{array}{c}
\text { Cost per contact } \\
40 \\
100 \\
50
\end{array}\right] \begin{aligned}
& \text { Telephone } \\
& \text { Housecall } \\
& \text { Letter }
\end{aligned}
$$

The number of contacts of each type made in two cities X and Y is given by
Telephone Housecall Letter
$B=\left[\begin{array}{ccc}1000 & 500 & 5000 \\ 3000 & 1000 & 10,000\end{array}\right] \rightarrow X$. Find the total amount spent by the group in the two cities X and Y.
:::

:::solution{label="Solution"}
We have

$$
\begin{aligned}
\mathrm{BA} & =\left[\begin{array}{c}
40,000+50,000+250,000 \\
120,000+100,000+500,000
\end{array}\right] \rightarrow \mathrm{X} \\
& =\left[\begin{array}{l}
340,000 \\
720,000
\end{array}\right] \rightarrow \mathrm{X}
\end{aligned}
$$

So the total amount spent by the group in the two cities is 340,000 paise and 720,000 paise, i.e., ₹3400 and ₹ 7200, respectively.

##
:::

:::

:::example{number="20" kind="example" id="ex_3.20" topic="Properties of transpose"}
#### Example 20

:::prompt
If $\mathrm{A}=\left[\begin{array}{lll}3 & \sqrt{3} & 2 \\ 4 & 2 & 0\end{array}\right]$ and $\mathrm{B}=\left[\begin{array}{rrr}2 & -1 & 2 \\ 1 & 2 & 4\end{array}\right]$, verify that
(i) $\left(\mathrm{A}^{\prime}\right)^{\prime}=\mathrm{A}$,
(ii) $(\mathrm{A}+\mathrm{B})^{\prime}=\mathrm{A}^{\prime}+\mathrm{B}^{\prime}$,
(iii) $(k \mathrm{~B})^{\prime}=k \mathrm{~B}^{\prime}$, where $k$ is any constant.
:::

:::solution{label="Solution"}
(i) We have
$$
\mathrm{A}=\left[\begin{array}{lll}
3 & \sqrt{3} & 2 \\
4 & 2 & 0
\end{array}\right] \Rightarrow \mathrm{A}^{\prime}=\left[\begin{array}{cc}
3 & 4 \\
\sqrt{3} & 2 \\
2 & 0
\end{array}\right] \Rightarrow\left(\mathrm{A}^{\prime}\right)^{\prime}=\left[\begin{array}{lll}
3 & \sqrt{3} & 2 \\
4 & 2 & 0
\end{array}\right]=\mathrm{A}
$$
Thus $\quad\left(\mathrm{A}^{\prime}\right)^{\prime}=\mathrm{A}$
(ii) We have
$$
\mathrm{A}=\left[\begin{array}{lll}
3 & \sqrt{3} & 2 \\
4 & 2 & 0
\end{array}\right], \mathrm{B}=\left[\begin{array}{rrr}
2 & -1 & 2 \\
1 & 2 & 4
\end{array}\right] \Rightarrow \mathrm{A}+\mathrm{B}=\left[\begin{array}{ccc}
5 & \sqrt{3}-1 & 4 \\
5 & 4 & 4
\end{array}\right]
$$
Therefore
$$
(\mathrm{A}+\mathrm{B})^{\prime}=\left[\begin{array}{cc}
5 & 5 \\
\sqrt{3}-1 & 4 \\
4 & 4
\end{array}\right]
$$
Now
$$
A^{\prime}=\left[\begin{array}{cc}
3 & 4 \\
\sqrt{3} & 2 \\
2 & 0
\end{array}\right], B^{\prime}=\left[\begin{array}{rr}
2 & 1 \\
-1 & 2 \\
2 & 4
\end{array}\right],
$$
So
$$
\mathrm{A}^{\prime}+\mathrm{B}^{\prime}=\left[\begin{array}{cr}
5 & 5 \\
\sqrt{3}-1 & 4 \\
4 & 4
\end{array}\right]
$$
Thus
$$
(\mathrm{A}+\mathrm{B})^{\prime}=\mathrm{A}^{\prime}+\mathrm{B}^{\prime}
$$
(iii) We have
$$
k \mathrm{~B}=k\left[\begin{array}{rrr}
2 & -1 & 2 \\
1 & 2 & 4
\end{array}\right]=\left[\begin{array}{lrr}
2 k & -k & 2 k \\
k & 2 k & 4 k
\end{array}\right]
$$
Then
$$
(k \mathrm{~B})^{\prime}=\left[\begin{array}{cc}
2 k & k \\
-k & 2 k \\
2 k & 4 k
\end{array}\right]=k\left[\begin{array}{rc}
2 & 1 \\
-1 & 2 \\
2 & 4
\end{array}\right]=k \mathrm{~B}^{\prime}
$$
Thus
$$
(k \mathrm{~B})^{\prime}=k \mathrm{~B}^{\prime}
$$
:::

:::

:::example{number="21" kind="example" id="ex_3.21" topic="Transpose of a matrix product"}
#### Example 21

:::prompt
If $\mathrm{A}=\left[\begin{array}{r}-2 \\ 4 \\ 5\end{array}\right], \mathrm{B}=\left[\begin{array}{lll}1 & 3 & -6\end{array}\right]$, verify that $(\mathrm{AB})^{\prime}=\mathrm{B}^{\prime} \mathrm{A}^{\prime}$.
:::

:::solution{label="Solution"}
We have

$$
A=\left[\begin{array}{r}
-2 \\
4 \\
5
\end{array}\right], B=\left[\begin{array}{lll}
1 & 3 & -6
\end{array}\right]
$$

then

$$
\mathrm{AB}=\left[\begin{array}{r}
-2 \\
4 \\
5
\end{array}\right]\left[\begin{array}{lll}
1 & 3 & -6
\end{array}\right]=\left[\begin{array}{ccc}
-2 & -6 & 12 \\
4 & 12 & -24 \\
5 & 15 & -30
\end{array}\right]
$$

Now

$$
\begin{aligned}
& \mathrm{A}^{\prime}=\left[\begin{array}{lll}
-2 & 4 & 5
\end{array}\right], \mathrm{B}^{\prime}=\left[\begin{array}{r}
1 \\
3 \\
-6
\end{array}\right] \\
& \mathrm{A}^{\prime}=\left[\begin{array}{r}
1 \\
3 \\
-6
\end{array}\right]\left[\begin{array}{lll}
-2 & 4 & 5
\end{array}\right]=\left[\begin{array}{ccc}
-2 & 4 & 5 \\
-6 & 12 & 15 \\
12 & -24 & -30
\end{array}\right]=(\mathrm{AB})^{\prime}
\end{aligned}
$$

Clearly

$$
(\mathrm{AB})^{\prime}=\mathrm{B}^{\prime} \mathrm{A}^{\prime}
$$
:::

:::

:::example{number="22" kind="example" id="ex_3.22" topic="Matrix as sum of symmetric and skew-symmetric parts"}
#### Example 22

:::prompt
Express the matrix $\mathrm{B}=\left[\begin{array}{rrr}2 & -2 & -4 \\ -1 & 3 & 4 \\ 1 & -2 & -3\end{array}\right]$ as the sum of a symmetric and a skew symmetric matrix.
:::

:::solution{label="Solution"}
Here

$$
\mathrm{B}^{\prime}=\left[\begin{array}{rrr}
2 & -1 & 1 \\
-2 & 3 & -2 \\
-4 & 4 & -3
\end{array}\right]
$$

Let

$$
\mathrm{P}=\frac{1}{2}\left(\mathrm{~B}+\mathrm{B}^{\prime}\right)=\frac{1}{2}\left[\begin{array}{rrr}
4 & -3 & -3 \\
-3 & 6 & 2 \\
-3 & 2 & -6
\end{array}\right]=\left[\begin{array}{ccc}
2 & \frac{-3}{2} & \frac{-3}{2} \\
\frac{-3}{2} & 3 & 1 \\
\frac{-3}{2} & 1 & -3
\end{array}\right],
$$

Now

$$
\mathrm{P}^{\prime}=\left[\begin{array}{ccc}
2 & \frac{-3}{2} & \frac{-3}{2} \\
\frac{-3}{2} & 3 & 1 \\
\frac{-3}{2} & 1 & -3
\end{array}\right]=\mathrm{P}
$$

Thus

$$
\mathrm{P}=\frac{1}{2}\left(\mathrm{~B}+\mathrm{B}^{\prime}\right) \text { is a symmetric matrix. }
$$

Also, let

$$
Q=\frac{1}{2}\left(B-B^{\prime}\right)=\frac{1}{2}\left[\begin{array}{rrr}
0 & -1 & -5 \\
1 & 0 & 6 \\
5 & -6 & 0
\end{array}\right]=\left[\begin{array}{ccc}
0 & \frac{-1}{2} & \frac{-5}{2} \\
\frac{1}{2} & 0 & 3 \\
\frac{5}{2} & -3 & 0
\end{array}\right]
$$

Then

$$
\mathrm{Q}^{\prime}=\left[\begin{array}{ccc}
0 & \frac{1}{2} & \frac{5}{3} \\
\frac{-1}{2} & 0 & -3 \\
\frac{-5}{2} & 3 & 0
\end{array}\right]=-\mathrm{Q}
$$

Thus

$$
Q=\frac{1}{2}\left(B-B^{\prime}\right) \text { is a skew symmetric matrix. }
$$

Now

$$
P+Q=\left[\begin{array}{ccc}
2 & \frac{-3}{2} & \frac{-3}{2} \\
\frac{-3}{2} & 3 & 1 \\
\frac{-3}{2} & 1 & -3
\end{array}\right]+\left[\begin{array}{ccc}
0 & \frac{-1}{2} & \frac{-5}{2} \\
\frac{1}{2} & 0 & 3 \\
\frac{5}{2} & -3 & 0
\end{array}\right]=\left[\begin{array}{rrr}
2 & -2 & -4 \\
-1 & 3 & 4 \\
1 & -2 & -3
\end{array}\right]=B
$$

Thus, B is represented as the sum of a symmetric and a skew symmetric matrix.

##
:::

:::

:::example{number="23" kind="example" id="ex_3.23" topic="Matrix power by induction"}
#### Example 23

:::prompt
If $\mathrm{A}=\left[\begin{array}{cc}\cos \theta & \sin \theta \\ -\sin \theta & \cos \theta\end{array}\right]$, then prove that $\mathrm{A}^{n}=\left[\begin{array}{cc}\cos n \theta & \sin n \theta \\ -\sin n \theta & \cos n \theta\end{array}\right], n \in \mathbf{N}$.
:::

:::solution{label="Solution"}
We shall prove the result by using principle of mathematical induction.

We have

$$
\begin{aligned}
& \mathrm{P}(n): \text { If } \mathrm{A}=\left[\begin{array}{cc}
\cos \theta & \sin \theta \\
-\sin \theta & \cos \theta
\end{array}\right] \text {, then } \mathrm{A}^{n}=\left[\begin{array}{cc}
\cos n \theta & \sin n \theta \\
-\sin n \theta & \cos n \theta
\end{array}\right], n \in \mathbf{N} \\
& \mathrm{P}(1): \mathrm{A}=\left[\begin{array}{cc}
\cos \theta & \sin \theta \\
-\sin \theta & \cos \theta
\end{array}\right] \text {, so } \mathrm{A}^{1}=\left[\begin{array}{cc}
\cos \theta & \sin \theta \\
-\sin \theta & \cos \theta
\end{array}\right]
\end{aligned}
$$

Therefore, the result is true for $n=1$.
Let the result be true for $n=k$. So

$$
\mathrm{P}(k): \mathrm{A}=\left[\begin{array}{cc}
\cos \theta & \sin \theta \\
-\sin \theta & \cos \theta
\end{array}\right] \text {, then } \mathrm{A}^{k}=\left[\begin{array}{cc}
\cos k \theta & \sin k \theta \\
-\sin k \theta & \cos k \theta
\end{array}\right]
$$

Now, we prove that the result holds for $n=k+1$

Now

$$
\begin{aligned}
\mathrm{A}^{k+1} & =\mathrm{A} \cdot \mathrm{~A}^{k}=\left[\begin{array}{cc}
\cos \theta & \sin \theta \\
-\sin \theta & \cos \theta
\end{array}\right]\left[\begin{array}{cc}
\cos k \theta & \sin k \theta \\
-\sin k \theta & \cos k \theta
\end{array}\right] \\
& =\left[\begin{array}{cc}
\cos \theta \cos k \theta-\sin \theta \sin k \theta & \cos \theta \sin k \theta+\sin \theta \cos k \theta \\
-\sin \theta \cos k \theta+\cos \theta \sin k \theta & -\sin \theta \sin k \theta+\cos \theta \cos k \theta
\end{array}\right] \\
& =\left[\begin{array}{cc}
\cos (\theta+k \theta) & \sin (\theta+k \theta) \\
-\sin (\theta+k \theta) & \cos (\theta+k \theta)
\end{array}\right]=\left[\begin{array}{cc}
\cos (k+1) \theta & \sin (k+1) \theta \\
-\sin (k+1) \theta & \cos (k+1) \theta
\end{array}\right]
\end{aligned}
$$

Therefore, the result is true for $n=k+1$. Thus by principle of mathematical induction, we have $\mathrm{A}^{n}=\left[\begin{array}{cc}\cos n \theta & \sin n \theta \\ -\sin n \theta & \cos n \theta\end{array}\right]$, holds for all natural numbers.
:::

:::

:::example{number="24" kind="example" id="ex_3.24" topic="Symmetric product commuting matrices"}
#### Example 24

:::prompt
If A and B are symmetric matrices of the same order, then show that AB is symmetric if and only if A and B commute, that is $\mathrm{AB}=\mathrm{BA}$.
:::

:::solution{label="Solution"}
Since A and B are both symmetric matrices, therefore $\mathrm{A}^{\prime}=\mathrm{A}$ and $\mathrm{B}^{\prime}=\mathrm{B}$.

Let $\quad \mathrm{AB}$ be symmetric, then $(\mathrm{AB})^{\prime}=\mathrm{AB}$
But

$$
(\mathrm{AB})^{\prime}=\mathrm{B}^{\prime} \mathrm{A}^{\prime}=\mathrm{BA} \text { (Why?) }
$$

Therefore

$$
\mathrm{BA}=\mathrm{AB}
$$

Conversely, if $\mathrm{AB}=\mathrm{BA}$, then we shall show that AB is symmetric.
Now

$$
\begin{aligned}
(\mathrm{AB})^{\prime} & =\mathrm{B}^{\prime} \mathrm{A}^{\prime} \\
& =\mathrm{BA} \text { (as } \mathrm{A} \text { and } \mathrm{B} \text { are symmetric) } \\
& =\mathrm{AB}
\end{aligned}
$$

Hence AB is symmetric.
:::

:::

:::example{number="25" kind="example" id="ex_3.25" topic="Solving a matrix equation for D"}
#### Example 25

:::prompt
Let $\mathrm{A}=\left[\begin{array}{rr}2 & -1 \\ 3 & 4\end{array}\right], \mathrm{B}=\left[\begin{array}{ll}5 & 2 \\ 7 & 4\end{array}\right], \mathrm{C}=\left[\begin{array}{ll}2 & 5 \\ 3 & 8\end{array}\right]$. Find a matrix D such that $\mathrm{CD}-\mathrm{AB}=\mathrm{O}$.
:::

:::solution{label="Solution"}
Since $\mathrm{A}, \mathrm{B}, \mathrm{C}$ are all square matrices of order 2, and $\mathrm{CD}-\mathrm{AB}$ is well defined, D must be a square matrix of order 2.
Let

$$
\begin{aligned}
& \mathrm{D}=\left[\begin{array}{ll}
a & b \\
c & d
\end{array}\right] \text {. Then } \mathrm{CD}-\mathrm{AB}=0 \text { gives } \\
& {\left[\begin{array}{ll}
2 & 5 \\
3 & 8
\end{array}\right]\left[\begin{array}{ll}
a & b \\
c & d
\end{array}\right]-\left[\begin{array}{rr}
2 & -1 \\
3 & 4
\end{array}\right]\left[\begin{array}{ll}
5 & 2 \\
7 & 4
\end{array}\right]=\mathrm{O}}
\end{aligned}
$$

or

$$
\left[\begin{array}{ll}
2 a+5 c & 2 b+5 d \\
3 a+8 c & 3 b+8 d
\end{array}\right]-\left[\begin{array}{ll}
3 & 0 \\
43 & 22
\end{array}\right]=\left[\begin{array}{ll}
0 & 0 \\
0 & 0
\end{array}\right]
$$

or

$$
\left[\begin{array}{cc}
2 a+5 c-3 & 2 b+5 d \\
3 a+8 c-43 & 3 b+8 d-22
\end{array}\right]=\left[\begin{array}{ll}
0 & 0 \\
0 & 0
\end{array}\right]
$$

By equality of matrices, we get

$$
\begin{array}{r}
2 a+5 c-3=0 \\
3 a+8 c-43=0 \\
2 b+5 d=0 \\
3 b+8 d-22=0
\end{array}
$$

Solving (1) and (2), we get $a=-191, c=77$. Solving (3) and (4), we get $b=-110$, $d=44$.

Therefore

$$
\mathrm{D}=\left[\begin{array}{ll}
a & b \\
c & d
\end{array}\right]=\left[\begin{array}{cc}
-191 & -110 \\
77 & 44
\end{array}\right]
$$

##
:::

:::

## Questions and Solutions

:::question{number="1" kind="exercise" id="q_3.1" topic="Order and elements of a matrix"}
#### Question 1

:::prompt
In the matrix $\mathrm{A}=\left[\begin{array}{cccc}2 & 5 & 19 & -7 \\ 35 & -2 & \frac{5}{2} & 12 \\ \sqrt{3} & 1 & -5 & 17\end{array}\right]$, write:
:::

:::part{label="(i)"}
:::prompt
The order of the matrix,
:::

:::

:::part{label="(ii)"}
:::prompt
The number of elements,
:::

:::

:::part{label="(iii)"}
:::prompt
Write the elements $a_{13}, a_{21}, a_{33}, a_{24}, a_{23}$.
:::

:::

:::solution{label="Solution"}
(i) Since, in the given matrix, the number of rows is 3 and the number of columns is 4 , the order of the matrix is $3 \times 4$.
(ii) Since the order of the matrix is $3 \times 4$, there are $3 \times 4=12$ elements.
(iii) Here,
$$
\begin{aligned}
& a_{13}=19 \\
& a_{21}=35 \\
& a_{33}=-5 \\
& a_{24}=12 \\
& a_{23}=\frac{5}{2}
\end{aligned}
$$
:::

:::

:::question{number="2" kind="exercise" id="q_3.2" topic="Possible orders for 24 or 13 elements"}
#### Question 2

:::prompt
If a matrix has 24 elements, what are the possible orders it can have? What, if it has 13 elements?
:::

:::solution{label="Solution"}
We know that if a matrix is of the order $m \times n$, it has $m n$ elements. Thus, to find all the possible orders of a matrix having 24 elements, we have to find all the ordered pairs of natural numbers whose product is 24 .

The ordered pairs are: $(1,24),(24,1),(2,12),(12,2),(3,8),(8,3),(4,6)$ and $(6,4)$.
Hence, the possible orders of a matrix having 24 elements are:

$$
(1 \times 24),(24 \times 1),(2 \times 12),(12 \times 2),(3 \times 8),(8 \times 3),(4 \times 6) \text { and }(6 \times 4) .
$$

$(1,13)$ and $(13,1)$ are the ordered pairs of natural numbers whose product is 13 .

Hence, the possible orders of a matrix having 13 elements are $(1 \times 13)$ and $(13 \times 1)$.
:::

:::

:::question{number="3" kind="exercise" id="q_3.3" topic="Possible orders for 18 or 5 elements"}
#### Question 3

:::prompt
If a matrix has 18 elements, what are the possible orders it can have? What, if it has 5 elements?
:::

:::solution{label="Solution"}
We know that if a matrix is of the order $m \times n$, it has $m n$ elements. Thus, to find all the possible orders of a matrix having 18 elements, we have to find all the ordered pairs of natural numbers whose product is 18 .

The ordered pairs are: $(1,18),(18,1),(2,9),(9,2),(3,6)$ and $(6,3)$.
Hence, the possible orders of a matrix having 18 elements are:

$$
(1 \times 18),(18 \times 1),(2 \times 9),(9 \times 2),(3 \times 6) \text { and }(6 \times 3) \text {. }
$$

$(1 \times 5)$ and $(5 \times 1)$ are the ordered pairs of natural numbers whose product is 5 .
Hence, the possible orders of a matrix having 5 elements are $(1 \times 5)$ and $(5 \times 1)$.
:::

:::

:::question{number="4" kind="exercise" id="q_3.4" topic="Constructing a 2x2 matrix from a formula"}
#### Question 4

:::prompt
Construct a $2 \times 2$ matrix, $\mathrm{A}=\left[a_{i j}\right]$, whose elements are given by:
:::

:::part{label="(i)"}
:::prompt
$a_{i j}=\frac{(i+j)^{2}}{2}$
:::

:::

:::part{label="(ii)"}
:::prompt
$a_{i j}=\frac{i}{j}$
:::

:::

:::part{label="(iii)"}
:::prompt
$a_{i j}=\frac{(i+2 j)^{2}}{2}$
:::

:::

:::solution{label="Solution"}
In general, a $2 \times 2$ matrix is given by $A=\left(\begin{array}{ll}a_{11} & a_{12} \\ a_{21} & a_{22}\end{array}\right)$

(i) $a_{i j}=\frac{(i+j)^{2}}{2} ; i, j=1,2$

Therefore,

$$
\begin{aligned}
& a_{11}=\frac{(1+1)^{2}}{2}=\frac{4}{2}=2 \\
& a_{12}=\frac{(1+2)^{2}}{2}=\frac{9}{2} \\
& a_{21}=\frac{(2+1)^{2}}{2}=\frac{9}{2} \\
& a_{22}=\frac{(2+2)^{2}}{2}=\frac{16}{2}=8
\end{aligned}
$$

Thus, the required matrix is
$$
A=\left(\begin{array}{cc}
2 & \frac{9}{2} \\
\frac{9}{2} & 8
\end{array}\right)
$$
(ii) $$
a_{i j}=\frac{i}{j} ; \quad i, j=1,2
$$
Therefore,
$$
\begin{aligned}
& a_{11}=\frac{1}{1}=1 \\
& a_{12}=\frac{1}{2} \\
& a_{21}=\frac{2}{1}=2 \\
& a_{22}=\frac{2}{2}=1
\end{aligned}
$$
Thus, the required matrix is
$$
A=\left(\begin{array}{ll}
1 & \frac{1}{2} \\
2 & 1
\end{array}\right)
$$
(iii) $$
a_{i j}=\frac{(i+2 j)^{2}}{2} ; \quad i, j=1,2
$$
Therefore,
$$
\begin{aligned}
& a_{11}=\frac{(1+2)^{2}}{2}=\frac{9}{2} \\
& a_{12}=\frac{(1+4)^{2}}{2}=\frac{25}{2} \\
& a_{21}=\frac{(2+2)^{2}}{2}=8 \\
& a_{22}=\frac{(2+4)^{2}}{2}=18
\end{aligned}
$$
Thus, the required matrix is
$$
A=\left(\begin{array}{cc}
\frac{9}{2} & \frac{25}{2} \\
8 & 18
\end{array}\right)
$$
:::

:::

:::question{number="5" kind="exercise" id="q_3.5" topic="Constructing a 3x4 matrix from a formula"}
#### Question 5

:::prompt
Construct a $3 \times 4$ matrix, whose elements are given by:
:::

:::part{label="(i)"}
:::prompt
$a_{i j}=\frac{1}{2}|-3 i+j|$
:::

:::

:::part{label="(ii)"}
:::prompt
$a_{i j}=2 i-j$
:::

:::

:::solution{label="Solution"}
In general, a $3 \times 4$ matrix is given by

$$
A=\left(\begin{array}{llll}
a_{11} & a_{12} & a_{13} & a_{14} \\
a_{21} & a_{22} & a_{23} & a_{24} \\
a_{31} & a_{32} & a_{33} & a_{34}
\end{array}\right)
$$

(i) Given $a_{i j}=\frac{1}{2}|-3 i+j| ; i=1,2,3 \quad j=1,2,3,4$
$$
\begin{aligned}
& a_{11}=\frac{1}{2}|-3(1)+1|=\frac{1}{2}|-3+1|=\frac{1}{2}|-2|=\frac{2}{2}=1 \\
& a_{21}=\frac{1}{2}|-3(2)+1|=\frac{1}{2}|-6+1|=\frac{1}{2}|-5|=\frac{5}{2} \\
& a_{31}=\frac{1}{2}|-3(3)+1|=\frac{1}{2}|-9+1|=\frac{1}{2}|-8|=\frac{8}{2}=4
\end{aligned}
$$
$$
\begin{aligned}
& a_{12}=\frac{1}{2}|-3(1)+2|=\frac{1}{2}|-3+2|=\frac{1}{2}|-1|=\frac{1}{2} \\
& a_{22}=\frac{1}{2}|-3(2)+2|=\frac{1}{2}|-6+2|=\frac{1}{2}|-4|=\frac{4}{2}=2 \\
& a_{32}=\frac{1}{2}|-3(3)+2|=\frac{1}{2}|-9+2|=\frac{1}{2}|-7|=\frac{7}{2}
\end{aligned}
$$
$$
\begin{aligned}
& a_{13}=\frac{1}{2}|-3(1)+3|=\frac{1}{2}|-3+3|=0 \\
& a_{23}=\frac{1}{2}|-3(2)+3|=\frac{1}{2}|-6+3|=\frac{1}{2}|-3|=\frac{3}{2} \\
& a_{33}=\frac{1}{2}|-3(3)+3|=\frac{1}{2}|-9+3|=\frac{1}{2}|-6|=\frac{6}{2}=3
\end{aligned}
$$
$$
\begin{aligned}
& a_{14}=\frac{1}{2}|-3(1)+4|=\frac{1}{2}|-3+4|=\frac{1}{2}|1|=\frac{1}{2} \\
& a_{24}=\frac{1}{2}|-3(2)+4|=\frac{1}{2}|-6+4|=\frac{1}{2}|-2|=\frac{2}{2}=1 \\
& a_{34}=\frac{1}{2}|-3(3)+4|=\frac{1}{2}|-9+4|=\frac{1}{2}|-5|=\frac{5}{2}
\end{aligned}
$$

Thus, the required matrix is

$$
A=\left(\begin{array}{cccc}
1 & \frac{1}{2} & 0 & \frac{1}{2} \\
\frac{5}{2} & 2 & \frac{3}{2} & 1 \\
4 & \frac{7}{2} & 3 & \frac{5}{2}
\end{array}\right)
$$

(ii) $a_{i j}=2 i-j ; i=1,2,3 \quad j=1,2,3,4$
$$
\begin{aligned}
& a_{11}=2(1)-1=2-1=1 \\
& a_{21}=2(2)-1=4-1=3 \\
& a_{31}=2(3)-1=6-1=5
\end{aligned}
$$
$$
\begin{aligned}
& a_{12}=2(1)-2=2-2=0 \\
& a_{22}=2(2)-2=4-2=2 \\
& a_{32}=2(3)-2=6-2=4
\end{aligned}
$$
$$
\begin{aligned}
& a_{13}=2(1)-3=2-3=-1 \\
& a_{23}=2(2)-3=4-3=1 \\
& a_{33}=2(3)-3=6-3=3
\end{aligned}
$$
$$
\begin{aligned}
& a_{14}=2(1)-4=2-4=-2 \\
& a_{24}=2(2)-4=4-4=0 \\
& a_{34}=2(3)-4=6-4=2
\end{aligned}
$$
Thus, the required matrix is
$$
A=\left(\begin{array}{cccc}
1 & 0 & -1 & -2 \\
3 & 2 & 1 & 0 \\
5 & 4 & 3 & 2
\end{array}\right)
$$
:::

:::

:::question{number="6" kind="exercise" id="q_3.6" topic="Solving for unknowns by matrix equality"}
#### Question 6

:::prompt
Find the values of $x, y$ and $z$ from the following equations:
:::

:::part{label="(i)"}
:::prompt
$\left[\begin{array}{ll}4 & 3 \\ x & 5\end{array}\right]=\left[\begin{array}{ll}y & z \\ 1 & 5\end{array}\right]$
:::

:::

:::part{label="(ii)"}
:::prompt
$\left[\begin{array}{cc}x+y & 2 \\ 5+z & x y\end{array}\right]=\left[\begin{array}{ll}6 & 2 \\ 5 & 8\end{array}\right]$
:::

:::

:::part{label="(iii)"}
:::prompt
$\left[\begin{array}{c}x+y+z \\ x+z \\ y+z\end{array}\right]=\left[\begin{array}{c}9 \\ 5 \\ 7\end{array}\right]$
:::

:::

:::solution{label="Solution"}
(i) $\quad\left(\begin{array}{ll}4 & 3 \\ x & 5\end{array}\right)=\left(\begin{array}{ll}y & z \\ 1 & 5\end{array}\right)$
As the given matrices are equal, their corresponding elements are also equal.
Comparing the corresponding elements, we get:
$$
x=1, y=4 \text { and } z=3
$$
(ii) $\left(\begin{array}{cc}x+y & 2 \\ 5+z & x y\end{array}\right)=\left(\begin{array}{ll}6 & 2 \\ 5 & 8\end{array}\right)$
As the given matrices are equal, their corresponding elements are also equal.
Comparing the corresponding elements, we get:
$$
\begin{aligned}
& x+y=6 \\
& x y=8 \\
& 5+z=5
\end{aligned}
$$
Hence,
$$
\begin{aligned}
& \Rightarrow 5+z=5 \\
& \Rightarrow z=0
\end{aligned}
$$
We know that $(a-b)^{2}=(a+b)^{2}-4 a b$
$$
\begin{aligned}
& \Rightarrow(x-y)^{2}=(6)^{2}-8 \times 4 \\
& \Rightarrow(x-y)^{2}=36-32 \\
& \Rightarrow(x-y)^{2}=4 \\
& \Rightarrow(x-y)= \pm 2
\end{aligned}
$$
Equating $x-y=2$ and $x+y=6$, we get $x=4, y=2$
Similarly, Equating $x-y=-2$ and $x+y=6$, we get $x=2, y=4$
Thus, $x=4, y=2, z=0$ or $x=2, y=4, z=0$
(iii) $\left(\begin{array}{c}x+y+z \\ x+z \\ y+z\end{array}\right)=\left(\begin{array}{l}9 \\ 5 \\ 7\end{array}\right)$
As the given matrices are equal, their corresponding elements are also equal. Comparing the corresponding elements, we get:
$$
\begin{aligned}
& x+y+z=9 \\
& x+z=5 \\
& y+z=7
\end{aligned}
$$

From (1) and (2), we have

$$
\begin{aligned}
& \Rightarrow y+5=9 \\
& \Rightarrow y=4
\end{aligned}
$$

From (3), we have

$$
\begin{aligned}
& \Rightarrow 4+z=7 \\
& \Rightarrow z=3
\end{aligned}
$$

Therefore,

$$
\begin{aligned}
& \Rightarrow x+z=5 \\
& \Rightarrow x+3=5 \\
& \Rightarrow x=2
\end{aligned}
$$

Thus, $x=2, y=4, z=3$
:::

:::

:::question{number="7" kind="exercise" id="q_3.7" topic="Solving for unknowns by matrix equality"}
#### Question 7

:::prompt
Find the value of $a, b, c$ and $d$ from the equation:
$$
\left[\begin{array}{cc}
a-b & 2 a+c \\
2 a-b & 3 c+d
\end{array}\right]=\left[\begin{array}{cc}
-1 & 5 \\
0 & 13
\end{array}\right]
$$
:::

:::solution{label="Solution"}
$$
\left(\begin{array}{cc}
a-b & 2 a+c \\
2 a-b & 3 c+d
\end{array}\right)=\left(\begin{array}{cc}
-1 & 5 \\
0 & 13
\end{array}\right)
$$

As the two matrices are equal, their corresponding elements are also equal. Comparing the corresponding elements, we get:

$$
\begin{aligned}
& a-b=-1 \\
& 2 a-b=0 \\
& 2 a+c=5 \\
& 3 c+d=13
\end{aligned}
$$

From (2),

$$
b=2 a
$$

Putting this value in (1),

$$
\begin{aligned}
& \Rightarrow a-2 a=-1 \\
& \Rightarrow a=1
\end{aligned}
$$

Hence,

$$
\Rightarrow b=2
$$

Putting $a=1$ in (3),

$$
\begin{aligned}
& \Rightarrow 2(1)+c=5 \\
& \Rightarrow c=3
\end{aligned}
$$

Putting $c=3$ in (4),

$$
\begin{aligned}
& \Rightarrow 3(3)+d=13 \\
& \Rightarrow d=4
\end{aligned}
$$

Thus, $a=1, b=2, c=3$ and $d=4$.
:::

:::

:::question{number="8" kind="exercise" id="q_3.8" topic="MCQ - condition for a square matrix"}
#### Question 8

:::prompt
$\mathrm{A}=\left[a_{i j}\right]_{m \times n!}$ is a square matrix, if
(A) $m<n$
(B) $m>n$
(C) $m=n$
(D) None of these
:::

:::solution{label="Solution"}
It is known that a given matrix is said to be a square matrix if the number of rows is equal to the number of columns.

Therefore, $A=\left[a_{i j}\right]_{m \times n}$ is a square matrix, if $m=n$.
Thus, the correct option is C.
:::

:::

:::question{number="9" kind="exercise" id="q_3.9" topic="MCQ - values making two matrices equal"}
#### Question 9

:::prompt
Which of the given values of $x$ and $y$ make the following pair of matrices equal $\left[\begin{array}{cc}3 x+7 & 5 \\ y+1 & 2-3 x\end{array}\right],\left[\begin{array}{cc}0 & y-2 \\ 8 & 4\end{array}\right]$
(A) $x=\frac{-1}{3}, y=7$
(B) Not possible to find
(C) $y=7, \quad x=\frac{-2}{3}$
(D) $x=\frac{-1}{3}, y=\frac{-2}{3}$
:::

:::solution{label="Solution"}
The given matrices are $\left[\begin{array}{cc}3 x+7 & 5 \\ y+1 & 2-3 x\end{array}\right]$ and $\left[\begin{array}{cc}0 & y-2 \\ 8 & 4\end{array}\right]$
Equating the corresponding elements, we get:

$$
\begin{aligned}
& 3 x+7=0 \Rightarrow x=\frac{-7}{3} \\
& y-2=5 \Rightarrow y=7 \\
& y+1=8 \Rightarrow y=7 \\
& 2-3 x=4 \Rightarrow x=\frac{-2}{3}
\end{aligned}
$$

We find that on comparing the corresponding elements of the two matrices, we get two different values of $x$, which is not possible.

Hence, it is not possible to find the values of $x$ and $y$ for which the given matrices are equal.
Thus, the correct option is B.
:::

:::

:::question{number="10" kind="exercise" id="q_3.10" topic="MCQ - count of 0/1 matrices of order 3x3"}
#### Question 10

:::prompt
The number of all possible matrices of order $3 \times 3$ with each entry 0 or 1 is:
(A) 27
(B) 18
(C) 81
(D) 512
:::

:::solution{label="Solution"}
The given matrix of the order $3 \times 3$ has 9 elements and each of these elements can be either 0 or 1.

Now, each of the 9 elements can be filled in two possible ways.
Hence, by the multiplication principle, the required number of possible matrices is $2^{9}=512$.
Thus, the correct option is D.

## EXERCISE 3.2
:::

:::

:::question{number="11" kind="exercise" id="q_3.11" topic="Matrix addition, subtraction and multiplication"}
#### Question 11

:::prompt
Let $\mathrm{A}=\left[\begin{array}{ll}2 & 4 \\ 3 & 2\end{array}\right], \mathrm{B}=\left[\begin{array}{rr}1 & 3 \\ -2 & 5\end{array}\right], \mathrm{C}=\left[\begin{array}{rr}-2 & 5 \\ 3 & 4\end{array}\right]$
Find each of the following:
:::

:::part{label="(i)"}
:::prompt
$\mathrm{A}+\mathrm{B}$
:::

:::

:::part{label="(ii)"}
:::prompt
A - B
:::

:::

:::part{label="(iii)"}
:::prompt
3A - C
:::

:::

:::part{label="(iv)"}
:::prompt
AB
:::

:::

:::part{label="(v)"}
:::prompt
BA
:::

:::

:::solution{label="Solution"}
(i) $A+B$
$$
\begin{aligned}
& \Rightarrow\left(\begin{array}{ll}
2 & 4 \\
3 & 2
\end{array}\right)+\left(\begin{array}{cc}
1 & 3 \\
-2 & 5
\end{array}\right) \\
& \Rightarrow\left(\begin{array}{ll}
2+1 & 4+3 \\
3-2 & 2+5
\end{array}\right) \\
& \Rightarrow\left(\begin{array}{ll}
3 & 7 \\
1 & 7
\end{array}\right)
\end{aligned}
$$
(ii) $A-B$
$$
\begin{aligned}
& \Rightarrow\left(\begin{array}{ll}
2 & 4 \\
3 & 2
\end{array}\right)-\left(\begin{array}{cc}
1 & 3 \\
-2 & 5
\end{array}\right) \\
& \Rightarrow\left(\begin{array}{cc}
2-1 & 4-3 \\
3+2 & 2-5
\end{array}\right) \\
& \Rightarrow\left(\begin{array}{cc}
1 & 1 \\
5 & -3
\end{array}\right)
\end{aligned}
$$
(iii) $3 A-C$
$$
\begin{aligned}
& \Rightarrow 3\left(\begin{array}{ll}
2 & 4 \\
3 & 2
\end{array}\right)-\left(\begin{array}{cc}
-2 & 5 \\
3 & 4
\end{array}\right) \\
& \Rightarrow\left(\begin{array}{ll}
3 \times 2 & 3 \times 4 \\
3 \times 3 & 3 \times 2
\end{array}\right)-\left(\begin{array}{cc}
-2 & 5 \\
3 & 4
\end{array}\right) \\
& \Rightarrow\left(\begin{array}{cc}
6+2 & 12-5 \\
9-3 & 6-4
\end{array}\right) \\
& \Rightarrow\left(\begin{array}{ll}
8 & 7 \\
6 & 2
\end{array}\right)
\end{aligned}
$$

(iv) $A B$
$$
\begin{aligned}
& \Rightarrow\left(\begin{array}{ll}
2 & 4 \\
3 & 2
\end{array}\right)\left(\begin{array}{cc}
1 & 3 \\
-2 & 5
\end{array}\right) \\
& \Rightarrow\left(\begin{array}{ll}
2(1)+4(-2) & 2(3)+4(5) \\
3(1)+2(-2) & 3(3)+2(5)
\end{array}\right) \\
& \Rightarrow\left(\begin{array}{cc}
2-8 & 6+20 \\
3-4 & 9+10
\end{array}\right) \\
& \Rightarrow\left(\begin{array}{cc}
-6 & 26 \\
-1 & 19
\end{array}\right)
\end{aligned}
$$
(v) $B A$
$$
\begin{aligned}
& \Rightarrow\left(\begin{array}{cc}
1 & 3 \\
-2 & 5
\end{array}\right)\left(\begin{array}{ll}
2 & 4 \\
3 & 2
\end{array}\right) \\
& \Rightarrow\left(\begin{array}{cc}
1(2)+3(3) & 1(4)+3(2) \\
-2(2)+5(3) & -2(4)+5(2)
\end{array}\right) \\
& \Rightarrow\left(\begin{array}{cc}
2+9 & 4+6 \\
-4+15 & -8+10
\end{array}\right) \\
& \Rightarrow\left(\begin{array}{cc}
11 & 10 \\
11 & 2
\end{array}\right)
\end{aligned}
$$
:::

:::

:::question{number="12" kind="exercise" id="q_3.12" topic="Computing sums of matrices"}
#### Question 12

:::prompt
Compute the following:
:::

:::part{label="(i)"}
:::prompt
$\left[\begin{array}{cc}a & b \\ -b & a\end{array}\right]+\left[\begin{array}{cc}a & b \\ b & a\end{array}\right]$
:::

:::

:::part{label="(ii)"}
:::prompt
$\left[\begin{array}{ll}a^{2}+b^{2} & b^{2}+c^{2} \\ a^{2}+c^{2} & a^{2}+b^{2}\end{array}\right]+\left[\begin{array}{cc}2 a b & 2 b c \\ -2 a c & -2 a b\end{array}\right]$
:::

:::

:::part{label="(iii)"}
:::prompt
$\left[\begin{array}{rrr}-1 & 4 & -6 \\ 8 & 5 & 16 \\ 2 & 8 & 5\end{array}\right]+\left[\begin{array}{ccc}12 & 7 & 6 \\ 8 & 0 & 5 \\ 3 & 2 & 4\end{array}\right]$
:::

:::

:::part{label="(iv)"}
:::prompt
$\left[\begin{array}{cc}\cos ^{2} x & \sin ^{2} x \\ \sin ^{2} x & \cos ^{2} x\end{array}\right]+\left[\begin{array}{cc}\sin ^{2} x & \cos ^{2} x \\ \cos ^{2} x & \sin ^{2} x\end{array}\right]$
:::

:::

:::solution{label="Solution"}
(i) $$
\begin{aligned}
\left(\begin{array}{cc}
a & b \\
-b & a
\end{array}\right) & +\left(\begin{array}{cc}
a & b \\
b & a
\end{array}\right) \\
& \Rightarrow\left(\begin{array}{cc}
a+a & b+b \\
-b+b & a+a
\end{array}\right) \\
& \Rightarrow\left(\begin{array}{cc}
2 a & 2 b \\
0 & 2 a
\end{array}\right)
\end{aligned}
$$
(ii) $$
\begin{aligned}
&\left(\begin{array}{cc}
a^{2}+b^{2} & b^{2}+c^{2} \\
a^{2}+c^{2} & a^{2}+b^{2}
\end{array}\right)+\left(\begin{array}{cc}
2 a b & 2 b c \\
-2 a c & -2 a b
\end{array}\right) \\
& \Rightarrow\left(\begin{array}{ll}
a^{2}+b^{2}+2 a b & b^{2}+c^{2}+2 b c \\
a^{2}+c^{2}-2 a c & a^{2}+b^{2}-2 a b
\end{array}\right) \\
& \Rightarrow\left(\begin{array}{ll}
(a+b)^{2} & (b+c)^{2} \\
(a-c)^{2} & (a-b)^{2}
\end{array}\right)
\end{aligned}
$$
(iii) $$
\begin{aligned}
&\left(\begin{array}{ccc}
-1 & 4 & -6 \\
8 & 5 & 16 \\
2 & 8 & 5
\end{array}\right)+\left(\begin{array}{ccc}
12 & 7 & 6 \\
8 & 0 & 5 \\
3 & 2 & 4
\end{array}\right) \\
& \Rightarrow\left(\begin{array}{ccc}
-1+12 & 4+7 & -6+6 \\
8+8 & 5+0 & 16+5 \\
2+3 & 8+2 & 5+4
\end{array}\right) \\
& \Rightarrow\left(\begin{array}{ccc}
11 & 11 & 0 \\
16 & 5 & 21 \\
5 & 10 & 9
\end{array}\right)
\end{aligned}
$$
(iv) $$
\begin{aligned}
&\left(\begin{array}{cc}
\cos ^{2} x & \sin ^{2} x \\
\sin ^{2} x & \cos ^{2} x
\end{array}\right)+\left(\begin{array}{cc}
\sin ^{2} x & \cos ^{2} x \\
\cos ^{2} x & \sin ^{2} x
\end{array}\right) \\
& \Rightarrow\left(\begin{array}{ll}
\cos ^{2} x+\sin ^{2} x & \sin ^{2} x+\cos ^{2} x \\
\sin ^{2} x+\cos ^{2} x & \cos ^{2} x+\sin ^{2} x
\end{array}\right) \\
& \Rightarrow\left(\begin{array}{ll}
1 & 1 \\
1 & 1
\end{array}\right)
\end{aligned}
$$
:::

:::

:::question{number="13" kind="exercise" id="q_3.13" topic="Computing matrix products"}
#### Question 13

:::prompt
Compute the indicated products.
:::

:::part{label="(i)"}
:::prompt
$\left[\begin{array}{rr}a & b \\ -b & a\end{array}\right]\left[\begin{array}{rr}a & -b \\ b & a\end{array}\right]$
:::

:::

:::part{label="(ii)"}
:::prompt
$\left[\begin{array}{l}1 \\ 2 \\ 3\end{array}\right]\left[\begin{array}{lll}2 & 3 & 4\end{array}\right]$
:::

:::

:::part{label="(iii)"}
:::prompt
$\left[\begin{array}{rr}1 & -2 \\ 2 & 3\end{array}\right]\left[\begin{array}{lll}1 & 2 & 3 \\ 2 & 3 & 1\end{array}\right]$
:::

:::

:::part{label="(iv)"}
:::prompt
$\left[\begin{array}{lll}2 & 3 & 4 \\ 3 & 4 & 5 \\ 4 & 5 & 6\end{array}\right]\left[\begin{array}{rrr}1 & -3 & 5 \\ 0 & 2 & 4 \\ 3 & 0 & 5\end{array}\right]$
:::

:::

:::part{label="(v)"}
:::prompt
$\left[\begin{array}{rr}2 & 1 \\ 3 & 2 \\ -1 & 1\end{array}\right]\left[\begin{array}{rrr}1 & 0 & 1 \\ -1 & 2 & 1\end{array}\right]$
:::

:::

:::part{label="(vi)"}
:::prompt
$\left[\begin{array}{rrr}3 & -1 & 3 \\ -1 & 0 & 2\end{array}\right]\left[\begin{array}{rr}2 & -3 \\ 1 & 0 \\ 3 & 1\end{array}\right]$
:::

:::

:::solution{label="Solution"}
(i)

$$
\begin{aligned}
\left(\begin{array}{cc}
a & b \\
-b & a
\end{array}\right) & \left(\begin{array}{cc}
a & -b \\
b & a
\end{array}\right) \\
& \Rightarrow\left(\begin{array}{cc}
a(a)+b(b) & a(-b)+b(a) \\
-b(a)+a(b) & -b(-b)+a(a)
\end{array}\right) \\
& \Rightarrow\left(\begin{array}{cc}
a^{2}+b^{2} & -a b+a b \\
-a b+a b & b^{2}+a^{2}
\end{array}\right) \\
& \Rightarrow\left(\begin{array}{cc}
a^{2}+b^{2} & 0 \\
0 & a^{2}+b^{2}
\end{array}\right)
\end{aligned}
$$

(ii)

$$
\begin{aligned}
\left(\begin{array}{l}
1 \\
2 \\
3
\end{array}\right)\left(\begin{array}{lll}
2 & 3 & 4
\end{array}\right) & \\
& \Rightarrow\left(\begin{array}{ccc}
1(2) & 1(3) & 1(4) \\
2(2) & 2(3) & 2(4) \\
3(2) & 3(3) & 3(4)
\end{array}\right) \\
& \Rightarrow\left(\begin{array}{ccc}
2 & 3 & 4 \\
4 & 6 & 8 \\
6 & 9 & 12
\end{array}\right)
\end{aligned}
$$

(iii) $$
\begin{aligned}
\left(\begin{array}{cc}
1 & -2 \\
2 & 3
\end{array}\right) & \left(\begin{array}{ccc}
1 & 2 & 3 \\
2 & 3 & 1
\end{array}\right) \\
& \Rightarrow\left(\begin{array}{ccc}
1(1)-2(2) & 1(2)-2(3) & 1(3)-2(1) \\
2(1)+3(2) & 2(2)+3(3) & 2(3)+3(1)
\end{array}\right) \\
& \Rightarrow\left(\begin{array}{ccc}
-3 & -4 & 1 \\
8 & 13 & 9
\end{array}\right)
\end{aligned}
$$
(iv) $$
\begin{aligned}
&\left(\begin{array}{lll}
2 & 3 & 4 \\
3 & 4 & 5 \\
4 & 5 & 6
\end{array}\right)\left(\begin{array}{ccc}
1 & -3 & 5 \\
0 & 2 & 4 \\
3 & 0 & 5
\end{array}\right) \\
& \Rightarrow\left(\begin{array}{ccc}
2(1)+3(0)+4(3) & 2(-3)+3(2)+4(0) & 2(5)+3(4)+4(5) \\
3(1)+4(0)+5(3) & 3(-3)+4(2)+5(0) & 3(5)+4(4)+5(5) \\
4(1)+5(0)+6(3) & 4(-3)+5(2)+6(0) & 4(5)+5(4)+6(5)
\end{array}\right) \\
& \Rightarrow\left(\begin{array}{ccc}
14 & 0 & 42 \\
18 & -1 & 56 \\
22 & -2 & 70
\end{array}\right)
\end{aligned}
$$
(v) $$
\begin{aligned}
\left(\begin{array}{cc}
2 & 1 \\
3 & 2 \\
-1 & 1
\end{array}\right) & \left(\begin{array}{ccc}
1 & 0 & 1 \\
-1 & 2 & 1
\end{array}\right) \\
& \Rightarrow\left(\begin{array}{ccc}
2(1)+1(-1) & 2(0)+1(2) & 2(1)+1(1) \\
3(1)+2(-1) & 3(0)+2(2) & 3(1)+2(1) \\
-1(1)+1(-1) & -1(0)+1(2) & -1(1)+1(1)
\end{array}\right) \\
& \Rightarrow\left(\begin{array}{ccc}
1 & 2 & 3 \\
1 & 4 & 5 \\
-2 & 2 & 0
\end{array}\right)
\end{aligned}
$$
(vi) $$
\begin{aligned}
& \left(\begin{array}{ccc}
3 & -1 & 3 \\
-1 & 0 & 2
\end{array}\right)\left(\begin{array}{cc}
2 & -3 \\
1 & 0 \\
3 & 1
\end{array}\right) \\
& \quad \Rightarrow\left(\begin{array}{cc}
3(2)-1(1)+3(3) & 3(-3)-1(0)+3(1) \\
-1(2)+0(1)+2(3) & -1(-3)+0(0)+2(1)
\end{array}\right) \\
& \quad \Rightarrow\left(\begin{array}{cc}
14 & -6 \\
4 & 5
\end{array}\right)
\end{aligned}
$$
:::

:::

:::question{number="14" kind="exercise" id="q_3.14" topic="Verifying matrix addition associativity"}
#### Question 14

:::prompt
If $\mathrm{A}=\left[\begin{array}{rrr}1 & 2 & -3 \\ 5 & 0 & 2 \\ 1 & -1 & 1\end{array}\right], \mathrm{B}=\left[\begin{array}{rrr}3 & -1 & 2 \\ 4 & 2 & 5 \\ 2 & 0 & 3\end{array}\right]$ and $\mathrm{C}=\left[\begin{array}{rrr}4 & 1 & 2 \\ 0 & 3 & 2 \\ 1 & -2 & 3\end{array}\right]$, then compute $(\mathrm{A}+\mathrm{B})$ and $(\mathrm{B}-\mathrm{C})$. Also, verify that $\mathrm{A}+(\mathrm{B}-\mathrm{C})=(\mathrm{A}+\mathrm{B})-\mathrm{C}$.
:::

:::solution{label="Solution"}
$$
\begin{aligned}
(A+B) & =\left(\begin{array}{ccc}
1 & 2 & -3 \\
5 & 0 & 2 \\
1 & -1 & 1
\end{array}\right)+\left(\begin{array}{ccc}
3 & -1 & 2 \\
4 & 2 & 5 \\
2 & 0 & 3
\end{array}\right) \\
& =\left(\begin{array}{ccc}
4 & 1 & -1 \\
9 & 2 & 7 \\
3 & -1 & 4
\end{array}\right) \\
(B-C) & =\left(\begin{array}{ccc}
3 & -1 & 2 \\
4 & 2 & 5 \\
2 & 0 & 3
\end{array}\right)-\left(\begin{array}{ccc}
4 & 1 & 2 \\
0 & 3 & 2 \\
1 & -2 & 3
\end{array}\right) \\
& =\left(\begin{array}{ccc}
-1 & -2 & 0 \\
4 & -1 & 3 \\
1 & 2 & 0
\end{array}\right)
\end{aligned}
$$

Now,

$$
\begin{aligned}
A+(B-C) & =\left(\begin{array}{ccc}
1 & 2 & -3 \\
5 & 0 & 2 \\
1 & -1 & 1
\end{array}\right)+\left(\begin{array}{ccc}
-1 & -2 & 0 \\
4 & -1 & 3 \\
1 & 2 & 0
\end{array}\right) \\
& =\left(\begin{array}{ccc}
0 & 0 & -3 \\
9 & -1 & 5 \\
2 & 1 & 1
\end{array}\right) \\
(A+B)-C & =\left(\begin{array}{ccc}
4 & 1 & -1 \\
9 & 2 & 7 \\
3 & -1 & 4
\end{array}\right)-\left(\begin{array}{ccc}
4 & 1 & 2 \\
0 & 3 & 2 \\
1 & -2 & 3
\end{array}\right) \\
& =\left(\begin{array}{ccc}
0 & 0 & -3 \\
9 & -1 & 5 \\
2 & 1 & 1
\end{array}\right)
\end{aligned}
$$

Hence, $A+(B-C)=(A+B)-C$.
:::

:::

:::question{number="15" kind="exercise" id="q_3.15" topic="Computing 3A - 5B"}
#### Question 15

:::prompt
If $\mathrm{A}=\left[\begin{array}{ccc}\frac{2}{3} & 1 & \frac{5}{3} \\ \frac{1}{3} & \frac{2}{3} & \frac{4}{3} \\ \frac{7}{3} & 2 & \frac{2}{3}\end{array}\right]$ and $\mathrm{B}=\left[\begin{array}{ccc}\frac{2}{5} & \frac{3}{5} & 1 \\ \frac{1}{5} & \frac{2}{5} & \frac{4}{5} \\ \frac{7}{5} & \frac{6}{5} & \frac{2}{5}\end{array}\right]$, then compute $3 A-5 B$.
:::

:::solution{label="Solution"}
$3 A-5 B=3\left(\begin{array}{ccc}\frac{2}{3} & 1 & \frac{5}{3} \\ \frac{1}{3} & \frac{2}{3} & \frac{4}{3} \\ \frac{7}{3} & 2 & \frac{2}{3}\end{array}\right)-5\left(\begin{array}{ccc}\frac{2}{5} & \frac{3}{5} & 1 \\ \frac{1}{5} & \frac{2}{5} & \frac{4}{5} \\ \frac{7}{5} & \frac{6}{5} & \frac{2}{5}\end{array}\right)$

$$
=\left(\begin{array}{lll}
2 & 3 & 5 \\
1 & 2 & 4 \\
7 & 6 & 2
\end{array}\right)-\left(\begin{array}{lll}
2 & 3 & 5 \\
1 & 2 & 4 \\
7 & 6 & 2
\end{array}\right)=\left(\begin{array}{lll}
0 & 0 & 0 \\
0 & 0 & 0 \\
0 & 0 & 0
\end{array}\right)
$$
:::

:::

:::question{number="16" kind="exercise" id="q_3.16" topic="Simplifying a trigonometric matrix expression"}
#### Question 16

:::prompt
Simplify $\cos \theta\left[\begin{array}{rr}\cos \theta & \sin \theta \\ -\sin \theta & \cos \theta\end{array}\right]+\sin \theta\left[\begin{array}{rr}\sin \theta & -\cos \theta \\ \cos \theta & \sin \theta\end{array}\right]$
:::

:::solution{label="Solution"}
$$
\begin{aligned}
& \cos \theta\left(\begin{array}{cc}
\cos \theta & \sin \theta \\
-\sin \theta & \cos \theta
\end{array}\right)+\sin \theta\left(\begin{array}{cc}
\sin \theta & -\cos \theta \\
\cos \theta & \sin \theta
\end{array}\right) \\
& \Rightarrow\left(\begin{array}{cc}
\cos ^{2} \theta & \cos \theta \sin \theta \\
-\sin \theta \cos \theta & \cos ^{2} \theta
\end{array}\right)+\left(\begin{array}{cc}
\sin ^{2} \theta & -\sin \theta \cos \theta \\
\sin \theta \cos \theta & \sin ^{2} \theta
\end{array}\right) \\
& \Rightarrow\left(\begin{array}{cc}
\cos ^{2} \theta+\sin ^{2} \theta & \sin \theta \cos \theta-\sin \theta \cos \theta \\
-\sin \theta \cos \theta+\sin \theta \cos \theta & \cos ^{2} \theta+\sin ^{2} \theta
\end{array}\right) \\
& \Rightarrow\left(\begin{array}{ll}
1 & 0 \\
0 & 1
\end{array}\right)
\end{aligned}
$$
:::

:::

:::question{number="17" kind="exercise" id="q_3.17" topic="Solving simultaneous matrix equations for X, Y"}
#### Question 17

:::prompt
Find X and Y , if
:::

:::part{label="(i)"}
:::prompt
$\mathrm{X}+\mathrm{Y}=\left[\begin{array}{ll}7 & 0 \\ 2 & 5\end{array}\right]$ and $\mathrm{X}-\mathrm{Y}=\left[\begin{array}{ll}3 & 0 \\ 0 & 3\end{array}\right]$
:::

:::

:::part{label="(ii)"}
:::prompt
$2 \mathrm{X}+3 \mathrm{Y}=\left[\begin{array}{ll}2 & 3 \\ 4 & 0\end{array}\right]$ and $3 \mathrm{X}+2 \mathrm{Y}=\left[\begin{array}{rr}2 & -2 \\ -1 & 5\end{array}\right]$
:::

:::

:::solution{label="Solution"}
(i) $$
\begin{aligned}
& X+Y=\left(\begin{array}{ll}
7 & 0 \\
2 & 5
\end{array}\right) \\
& X-Y=\left(\begin{array}{ll}
3 & 0 \\
0 & 3
\end{array}\right)
\end{aligned}
$$
Adding equations (1) and (2),
$$
\begin{aligned}
2 X & =\left(\begin{array}{ll}
7 & 0 \\
2 & 5
\end{array}\right)+\left(\begin{array}{ll}
3 & 0 \\
0 & 3
\end{array}\right) \\
& =\left(\begin{array}{cc}
10 & 0 \\
2 & 8
\end{array}\right) \\
X & =\frac{1}{2}\left(\begin{array}{cc}
10 & 0 \\
2 & 8
\end{array}\right) \\
& =\left(\begin{array}{ll}
5 & 0 \\
1 & 4
\end{array}\right)
\end{aligned}
$$
Now,
$$
\begin{aligned}
& \Rightarrow X+Y=\left(\begin{array}{ll}
7 & 0 \\
2 & 5
\end{array}\right) \\
& \Rightarrow Y=\left(\begin{array}{ll}
7 & 0 \\
2 & 5
\end{array}\right)-\left(\begin{array}{ll}
5 & 0 \\
1 & 4
\end{array}\right) \\
& \Rightarrow Y=\left(\begin{array}{ll}
2 & 0 \\
1 & 1
\end{array}\right)
\end{aligned}
$$
(ii) $$
\begin{aligned}
& 2 X+3 Y=\left(\begin{array}{ll}
2 & 3 \\
4 & 0
\end{array}\right) \\
& 3 X+2 Y=\left(\begin{array}{cc}
2 & -2 \\
-1 & 5
\end{array}\right)
\end{aligned}
$$
Multiplying equation $(1)$ by 2 ,
$$
\begin{aligned}
& 2(2 X+3 Y)=2\left(\begin{array}{ll}
2 & 3 \\
4 & 0
\end{array}\right) \\
& 4 X+6 Y=\left(\begin{array}{ll}
4 & 6 \\
8 & 0
\end{array}\right)
\end{aligned}
$$

Multiplying equation (2) by 3,

$$
\begin{aligned}
& 3(3 X+2 Y)=3\left(\begin{array}{cc}
2 & -2 \\
-1 & 5
\end{array}\right) \\
& 9 X+6 Y=\left(\begin{array}{cc}
6 & -6 \\
-3 & 15
\end{array}\right)
\end{aligned}
$$

From (3) and (4),

$$
\begin{aligned}
&(4 X+6 Y)-(9 X+6 Y)=\left(\begin{array}{ll}
4 & 6 \\
8 & 0
\end{array}\right)-\left(\begin{array}{cc}
6 & -6 \\
-3 & 15
\end{array}\right) \\
&-5 X=\left(\begin{array}{cc}
4-6 & 6+6 \\
8+3 & 0-15
\end{array}\right) \\
&-5 X=\left(\begin{array}{cc}
-2 & 12 \\
11 & -15
\end{array}\right) \\
& X=\frac{-1}{5}\left(\begin{array}{cc}
-2 & 12 \\
11 & -15
\end{array}\right) \\
&=\left(\begin{array}{cc}
\frac{2}{5} & \frac{-12}{5} \\
\frac{-11}{5} & 3
\end{array}\right)
\end{aligned}
$$

Now

$$
\begin{aligned}
& \Rightarrow 2 X+3 Y=\left(\begin{array}{ll}
2 & 3 \\
4 & 0
\end{array}\right) \\
& \Rightarrow 2\left(\begin{array}{cc}
\frac{2}{5} & \frac{-12}{5} \\
\frac{-11}{5} & 3
\end{array}\right)+3 Y=\left(\begin{array}{ll}
2 & 3 \\
4 & 0
\end{array}\right) \\
& \Rightarrow\left(\begin{array}{cc}
\frac{4}{5} & \frac{-24}{5} \\
\frac{-22}{5} & 6
\end{array}\right)+3 Y=\left(\begin{array}{ll}
2 & 3 \\
4 & 0
\end{array}\right) \\
& \Rightarrow 3 Y=\left(\begin{array}{ll}
2 & 3 \\
4 & 0
\end{array}\right)-\left(\begin{array}{cc}
\frac{4}{5} & \frac{-24}{5} \\
\frac{-22}{5} & 6
\end{array}\right) \\
& \Rightarrow 3 Y=\left(\begin{array}{cc}
\frac{6}{5} & \frac{39}{5} \\
\frac{42}{5} & -6
\end{array}\right) \\
& \Rightarrow Y=\frac{1}{3}\left(\begin{array}{cc}
\frac{6}{5} & \frac{39}{5} \\
\frac{42}{5} & -6
\end{array}\right) \\
& \Rightarrow Y=\left(\begin{array}{cc}
\frac{2}{5} & \frac{13}{5} \\
\frac{14}{5} & -2
\end{array}\right)
\end{aligned}
$$
:::

:::

:::question{number="18" kind="exercise" id="q_3.18" topic="Solving a matrix equation for X"}
#### Question 18

:::prompt
Find X , if $\mathrm{Y}=\left[\begin{array}{ll}3 & 2 \\ 1 & 4\end{array}\right]$ and $2 \mathrm{X}+\mathrm{Y}=\left[\begin{array}{rr}1 & 0 \\ -3 & 2\end{array}\right]$
:::

:::solution{label="Solution"}
$$
\begin{aligned}
& 2 X+Y=\left(\begin{array}{cc}
1 & 0 \\
-3 & 2
\end{array}\right) \\
& \Rightarrow 2 X+\left(\begin{array}{ll}
3 & 2 \\
1 & 4
\end{array}\right)=\left(\begin{array}{ll}
1 & 0 \\
-3 & 2
\end{array}\right) \\
& \Rightarrow 2 X=\left(\begin{array}{cc}
1 & 0 \\
-3 & 2
\end{array}\right)-\left(\begin{array}{ll}
3 & 2 \\
1 & 4
\end{array}\right) \\
& \Rightarrow 2 X=\left(\begin{array}{ll}
-2 & -2 \\
-4 & -2
\end{array}\right) \\
& \Rightarrow X=\frac{1}{2}\left(\begin{array}{ll}
-2 & -2 \\
-4 & -2
\end{array}\right) \\
& \Rightarrow X=\left(\begin{array}{ll}
-1 & -1 \\
-2 & -1
\end{array}\right)
\end{aligned}
$$
:::

:::

:::question{number="19" kind="exercise" id="q_3.19" topic="Solving for x and y in a matrix equation"}
#### Question 19

:::prompt
Find $x$ and $y$, if $2\left[\begin{array}{cc}1 & 3 \\ 0 & x\end{array}\right]+\left[\begin{array}{ll}y & 0 \\ 1 & 2\end{array}\right]=\left[\begin{array}{ll}5 & 6 \\ 1 & 8\end{array}\right]$
:::

:::solution{label="Solution"}
$$
\begin{aligned}
& \Rightarrow 2\left(\begin{array}{ll}
1 & 3 \\
0 & x
\end{array}\right)+\left(\begin{array}{ll}
y & 0 \\
1 & 2
\end{array}\right)=\left(\begin{array}{ll}
5 & 6 \\
1 & 8
\end{array}\right) \\
& \Rightarrow\left(\begin{array}{cc}
2 & 6 \\
0 & 2 x
\end{array}\right)+\left(\begin{array}{ll}
y & 0 \\
1 & 2
\end{array}\right)=\left(\begin{array}{ll}
5 & 6 \\
1 & 8
\end{array}\right) \\
& \Rightarrow\left(\begin{array}{cc}
2+y & 6 \\
1 & 2 x+2
\end{array}\right)=\left(\begin{array}{ll}
5 & 6 \\
1 & 8
\end{array}\right)
\end{aligned}
$$

Comparing the corresponding elements of these two matrices,

$$
\begin{aligned}
& 2+y=5 \\
& \Rightarrow y=3
\end{aligned}
$$

$$
\begin{aligned}
& 2 x+2=8 \\
& \Rightarrow x=3
\end{aligned}
$$

Therefore, $x=3$ and $y=3$.
:::

:::

:::question{number="20" kind="exercise" id="q_3.20" topic="Solving for x, y, z, t in a matrix equation"}
#### Question 20

:::prompt
Solve the equation for $x, y, z$ and $t$, if $2\left[\begin{array}{cc}x & z \\ y & t\end{array}\right]+3\left[\begin{array}{rr}1 & -1 \\ 0 & 2\end{array}\right]=3\left[\begin{array}{ll}3 & 5 \\ 4 & 6\end{array}\right]$
:::

:::solution{label="Solution"}
$$
\begin{aligned}
& \Rightarrow 2\left(\begin{array}{ll}
x & z \\
y & t
\end{array}\right)+3\left(\begin{array}{cc}
1 & -1 \\
0 & 2
\end{array}\right)=3\left(\begin{array}{cc}
3 & 5 \\
4 & 6
\end{array}\right) \\
& \Rightarrow\left(\begin{array}{cc}
2 x & 2 z \\
2 y & 2 t
\end{array}\right)+\left(\begin{array}{cc}
3 & -3 \\
0 & 6
\end{array}\right)=\left(\begin{array}{cc}
9 & 15 \\
12 & 18
\end{array}\right) \\
& \Rightarrow\left(\begin{array}{cc}
2 x+3 & 2 z-3 \\
2 y & 2 t+6
\end{array}\right)=\left(\begin{array}{cc}
9 & 15 \\
12 & 18
\end{array}\right)
\end{aligned}
$$

Comparing the corresponding elements of these two matrices,

$$
\begin{aligned}
& 2 x+3=9 \\
& \Rightarrow 2 x=6 \\
& \Rightarrow x=3
\end{aligned}
$$

$$
\begin{aligned}
& 2 y=12 \\
& \Rightarrow y=6
\end{aligned}
$$

$$
\begin{aligned}
& 2 z-3=15 \\
& \Rightarrow 2 z=18 \\
& \Rightarrow z=9
\end{aligned}
$$

$$
\begin{aligned}
& 2 t+6=18 \\
& \Rightarrow 2 t=12 \\
& \Rightarrow t=6
\end{aligned}
$$

Therefore, $x=3, y=6, z=9$ and $t=6$.
:::

:::

:::question{number="21" kind="exercise" id="q_3.21" topic="Solving for x and y using a vector equation"}
#### Question 21

:::prompt
If $x\left[\begin{array}{l}2 \\ 3\end{array}\right]+y\left[\begin{array}{c}-1 \\ 1\end{array}\right]=\left[\begin{array}{l}10 \\ 5\end{array}\right]$, find the values of $x$ and $y$.
:::

:::solution{label="Solution"}
$$
\begin{aligned}
& \Rightarrow x\binom{2}{3}+y\binom{-1}{1}=\binom{10}{5} \\
& \Rightarrow\binom{2 x}{3 x}+\binom{-y}{y}=\binom{10}{5} \\
& \Rightarrow\binom{2 x-y}{3 x+y}=\binom{10}{5}
\end{aligned}
$$

Comparing the corresponding elements of these two matrices,

$$
\begin{aligned}
& 2 x-y=10 \\
& 3 x+y=5
\end{aligned}
$$

By adding these two equations, we get

$$
\begin{aligned}
& 5 x=15 \\
& \Rightarrow x=3
\end{aligned}
$$

Now, putting this value in (2)

$$
\begin{aligned}
& \Rightarrow 3 x+y=5 \\
& \Rightarrow y=5-3 x \\
& \Rightarrow y=5-3(3) \\
& \Rightarrow y=5-9 \\
& \Rightarrow y=-4
\end{aligned}
$$

Therefore, $x=3$ and $y=4$.
:::

:::

:::question{number="22" kind="exercise" id="q_3.22" topic="Solving for x, y, z, w in a matrix equation"}
#### Question 22

:::prompt
Given $3\left[\begin{array}{ll}x & y \\ z & w\end{array}\right]=\left[\begin{array}{rl}x & 6 \\ -1 & 2 w\end{array}\right]+\left[\begin{array}{cc}4 & x+y \\ z+w & 3\end{array}\right]$, find the values of $x, y, z$ and $w$.
:::

:::solution{label="Solution"}
$$
\begin{aligned}
& \Rightarrow 3\left(\begin{array}{ll}
x & y \\
z & w
\end{array}\right)=\left(\begin{array}{cc}
x & 6 \\
-1 & 2 w
\end{array}\right)+\left(\begin{array}{cc}
4 & x+y \\
z+w & 3
\end{array}\right) \\
& \Rightarrow\left(\begin{array}{ll}
3 x & 3 y \\
3 z & 3 w
\end{array}\right)=\left(\begin{array}{cc}
x+4 & 6+x+y \\
-1+z+w & 2 w+3
\end{array}\right)
\end{aligned}
$$

Comparing the corresponding elements of these two matrices,

$$
\begin{aligned}
& \Rightarrow 3 x=x+4 \\
& \Rightarrow 2 x=4 \\
& \Rightarrow x=2
\end{aligned}
$$

$$
\begin{aligned}
& \Rightarrow 3 y=6+x+y \\
& \Rightarrow 2 y=6+x \\
& \Rightarrow 2 y=6+2 \\
& \Rightarrow 2 y=8 \\
& \Rightarrow y=4
\end{aligned}
$$

$$
\begin{aligned}
& \Rightarrow 3 w=2 w+3 \\
& \Rightarrow w=3
\end{aligned}
$$

$$
\begin{aligned}
& \Rightarrow 3 z=-1+z+w \\
& \Rightarrow 2 z=w-1 \\
& \Rightarrow 2 z=3-1 \\
& \Rightarrow 2 z=-2 \\
& \Rightarrow z=1
\end{aligned}
$$

Therefore, $x=2, y=4, z=1$ and $w=3$
:::

:::

:::question{number="23" kind="exercise" id="q_3.23" topic="Matrix function identity F(x)F(y)=F(x+y)"}
#### Question 23

:::prompt
If $\mathrm{F}(x)=\left[\begin{array}{ccc}\cos x & -\sin x & 0 \\ \sin x & \cos x & 0 \\ 0 & 0 & 1\end{array}\right]$, show that $\mathrm{F}(x) \mathrm{F}(y)=\mathrm{F}(x+y)$.
:::

:::solution{label="Solution"}
It is given that

$$
F(x)=\left(\begin{array}{ccc}
\cos x & -\sin x & 0 \\
\sin x & \cos x & 0 \\
0 & 0 & 1
\end{array}\right)
$$

Then,

$$
F(y)=\left(\begin{array}{ccc}
\cos y & -\sin y & 0 \\
\sin y & \cos y & 0 \\
0 & 0 & 1
\end{array}\right)
$$

Now,

$$
F(x+y)=\left(\begin{array}{ccc}
\cos (x+y) & -\sin (x+y) & 0 \\
\sin (x+y) & \cos (x+y) & 0 \\
0 & 0 & 1
\end{array}\right)
$$

$$
\begin{aligned}
F(x) F(y) & =\left(\begin{array}{ccc}
\cos x & -\sin x & 0 \\
\sin x & \cos x & 0 \\
0 & 0 & 1
\end{array}\right)\left(\begin{array}{ccc}
\cos y & -\sin y & 0 \\
\sin y & \cos y & 0 \\
0 & 0 & 1
\end{array}\right) \\
& =\left(\begin{array}{ccc}
\cos x \cos y-\sin x \sin y+0 & -\cos x \sin y-\sin x \cos y+0 & 0 \\
\sin x \cos y+\cos x \sin y+0 & -\sin x \sin y+\cos x \cos y+0 & 0 \\
0 & 0 & 0
\end{array}\right) \\
& =\left(\begin{array}{ccc}
\cos (x+y) & -\sin (x+y) & 0 \\
\sin (x+y) & \cos (x+y) & 0 \\
0 & 0 & 1
\end{array}\right) \\
& =F(x+y)
\end{aligned}
$$

Therefore, $F(x) F(y)=F(x+y)$
:::

:::

:::question{number="24" kind="exercise" id="q_3.24" topic="Showing matrix multiplication is non-commutative"}
#### Question 24

:::prompt
Show that
:::

:::part{label="(i)"}
:::prompt
$\left[\begin{array}{rr}5 & -1 \\ 6 & 7\end{array}\right]\left[\begin{array}{ll}2 & 1 \\ 3 & 4\end{array}\right] \neq\left[\begin{array}{ll}2 & 1 \\ 3 & 4\end{array}\right]\left[\begin{array}{rr}5 & -1 \\ 6 & 7\end{array}\right]$
:::

:::

:::part{label="(ii)"}
:::prompt
$\left[\begin{array}{lll}1 & 2 & 3 \\ 0 & 1 & 0 \\ 1 & 1 & 0\end{array}\right]\left[\begin{array}{rrr}-1 & 1 & 0 \\ 0 & -1 & 1 \\ 2 & 3 & 4\end{array}\right] \neq\left[\begin{array}{rrr}-1 & 1 & 0 \\ 0 & -1 & 1 \\ 2 & 3 & 4\end{array}\right]\left[\begin{array}{lll}1 & 2 & 3 \\ 0 & 1 & 0 \\ 1 & 1 & 0\end{array}\right]$
:::

:::

:::solution{label="Solution"}
(i) $\quad\left(\begin{array}{cc}5 & -1 \\ 6 & 7\end{array}\right)\left(\begin{array}{ll}2 & 1 \\ 3 & 4\end{array}\right) \neq\left(\begin{array}{ll}2 & 1 \\ 3 & 4\end{array}\right)\left(\begin{array}{cc}5 & -1 \\ 6 & 7\end{array}\right)$

$$
\begin{aligned}
\left(\begin{array}{cc}
5 & -1 \\
6 & 7
\end{array}\right)\left(\begin{array}{ll}
2 & 1 \\
3 & 4
\end{array}\right) & =\left(\begin{array}{cc}
5(2)-1(3) & 5(1)-1(4) \\
6(2)+7(3) & 6(1)+7(4)
\end{array}\right) \\
& =\left(\begin{array}{cc}
10-3 & 5-4 \\
12+21 & 6+28
\end{array}\right) \\
& =\left(\begin{array}{cc}
7 & 1 \\
33 & 34
\end{array}\right)
\end{aligned}
$$

$$
\begin{aligned}
\left(\begin{array}{ll}
2 & 1 \\
3 & 4
\end{array}\right)\left(\begin{array}{cc}
5 & -1 \\
6 & 7
\end{array}\right) & =\left(\begin{array}{cc}
2(5)+1(6) & 2(-1)+1(7) \\
3(5)+4(6) & 3(-1)+4(7)
\end{array}\right) \\
& =\left(\begin{array}{cc}
10+6 & -2+7 \\
15+24 & -3+28
\end{array}\right) \\
& =\left(\begin{array}{cc}
16 & 5 \\
39 & 25
\end{array}\right)
\end{aligned}
$$

Thus, $\left(\begin{array}{cc}5 & -1 \\ 6 & 7\end{array}\right)\left(\begin{array}{ll}2 & 1 \\ 3 & 4\end{array}\right) \neq\left(\begin{array}{ll}2 & 1 \\ 3 & 4\end{array}\right)\left(\begin{array}{cc}5 & -1 \\ 6 & 7\end{array}\right)$
(ii) $\left(\begin{array}{lll}1 & 2 & 3 \\ 0 & 1 & 0 \\ 1 & 1 & 0\end{array}\right)\left(\begin{array}{ccc}-1 & 1 & 0 \\ 0 & -1 & 1 \\ 2 & 3 & 4\end{array}\right) \neq\left(\begin{array}{ccc}-1 & 1 & 0 \\ 0 & -1 & 1 \\ 2 & 3 & 4\end{array}\right)\left(\begin{array}{lll}1 & 2 & 3 \\ 0 & 1 & 0 \\ 1 & 1 & 0\end{array}\right)$

$$
\begin{aligned}
&\left(\begin{array}{lll}
1 & 2 & 3 \\
0 & 1 & 0 \\
1 & 1 & 0
\end{array}\right)\left(\begin{array}{ccc}
-1 & 1 & 0 \\
0 & -1 & 1 \\
2 & 3 & 4
\end{array}\right)=\left(\begin{array}{ccc}
1(-1)+2(0)+3(2) & 1(1)+2(-1)+3(3) & 1(0)+2(1)+3(4) \\
0(-1)+1(0)+0(2) & 0(1)+1(-1)+0(3) & 0(0)+1(1)+0(4) \\
1(-1)+1(0)+0(2) & 1(1)+1(-1)+0(3) & 1(0)+1(1)+0(4)
\end{array}\right) \\
&=\left(\begin{array}{ccc}
5 & 8 & 14 \\
0 & -1 & 1 \\
-1 & 0 & 1
\end{array}\right) \\
&\left(\begin{array}{ccc}
-1 & 1 & 0 \\
0 & -1 & 1 \\
2 & 3 & 4
\end{array}\right)\left(\begin{array}{lll}
1 & 2 & 3 \\
0 & 1 & 0 \\
1 & 1 & 0
\end{array}\right)=\left(\begin{array}{ccc}
-1(1)+1(0)+0(1) & -1(2)+1(1)+0(1) & -1(3)+1(0)+0(0) \\
0(1)+(-1)(0)+1(1) & 0(2)+(-1)(1)+1(1) & 0(3)+-1(0)+1(0) \\
2(1)+3(0)+4(1) & 2(2)+3(1)+4(1) & 2(3)+3(0)+4(0)
\end{array}\right) \\
&=\left(\begin{array}{ccc}
-1 & -1 & -3 \\
1 & 0 & 0 \\
6 & 11 & 6
\end{array}\right) \\
& \text { Thus, }\left(\begin{array}{lll}
1 & 2 & 3 \\
0 & 1 & 0 \\
1 & 1 & 0
\end{array}\right)\left(\begin{array}{ccc}
-1 & 1 & 0 \\
0 & -1 & 1 \\
2 & 3 & 4
\end{array}\right) \neq\left(\begin{array}{ccc}
-1 & 1 & 0 \\
0 & -1 & 1 \\
2 & 3 & 4
\end{array}\right)\left(\begin{array}{lll}
1 & 2 & 3 \\
0 & 1 & 0 \\
1 & 1 & 0
\end{array}\right)
\end{aligned}
$$
:::

:::

:::question{number="25" kind="exercise" id="q_3.25" topic="Evaluating a matrix polynomial"}
#### Question 25

:::prompt
Find $\mathrm{A}^{2}-5 \mathrm{~A}+6 \mathrm{I}$, if $\mathrm{A}=\left[\begin{array}{rrr}2 & 0 & 1 \\ 2 & 1 & 3 \\ 1 & -1 & 0\end{array}\right]$
:::

:::solution{label="Solution"}
$$
\begin{aligned}
A^{2} & =A \cdot A \\
& =\left(\begin{array}{ccc}
2 & 0 & 1 \\
2 & 1 & 3 \\
1 & -1 & 0
\end{array}\right)\left(\begin{array}{ccc}
2 & 0 & 1 \\
2 & 1 & 3 \\
1 & -1 & 0
\end{array}\right) \\
& =\left(\begin{array}{ccc}
2(2)+0(2)+1(1) & 2(0)+0(1)+1(-1) & 2(1)+0(3)+1(0) \\
2(2)+1(2)+3(1) & 2(0)+1(1)+1(1) & 2(1)+1(3)+3(0) \\
1(2)+(-1)(2)+0(1) & 1(0)+(-1)(1)+0(-1) & 1(1)+(-1)(3)+0(0)
\end{array}\right) \\
& =\left(\begin{array}{ccc}
4+0+1 & 0+0-1 & 2+0+0 \\
4+2+3 & 0+1-3 & 2+3+0 \\
2-2+0 & 0-1+0 & 1-3+0
\end{array}\right) \\
& =\left(\begin{array}{ccc}
5 & -1 & 2 \\
9 & -2 & 5 \\
0 & -1 & -2
\end{array}\right)
\end{aligned}
$$

Therefore,

$$
\begin{aligned}
A^{2}-5 A+6 I & =\left(\begin{array}{ccc}
5 & -1 & 2 \\
9 & -2 & 5 \\
0 & -1 & -2
\end{array}\right)-5\left(\begin{array}{ccc}
2 & 0 & 1 \\
2 & 1 & 3 \\
1 & -1 & 0
\end{array}\right)+6\left(\begin{array}{lll}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{array}\right) \\
& =\left(\begin{array}{ccc}
5 & -1 & 2 \\
9 & -2 & 5 \\
0 & -1 & -2
\end{array}\right)-\left(\begin{array}{ccc}
10 & 0 & 5 \\
10 & 5 & 15 \\
5 & -5 & 0
\end{array}\right)+\left(\begin{array}{ccc}
6 & 0 & 0 \\
0 & 6 & 0 \\
0 & 0 & 6
\end{array}\right) \\
& =\left(\begin{array}{ccc}
5-10 & -1-0 & 2-5 \\
9-10 & -2-5 & 5-15 \\
0-5 & -1+5 & -2-0
\end{array}\right)+\left(\begin{array}{lll}
6 & 0 & 0 \\
0 & 6 & 0 \\
0 & 0 & 6
\end{array}\right) \\
& =\left(\begin{array}{ccc}
-5 & -1 & -3 \\
-1 & -7 & -10 \\
-5 & 4 & -2
\end{array}\right)+\left(\begin{array}{lll}
6 & 0 & 0 \\
0 & 6 & 0 \\
0 & 0 & 6
\end{array}\right) \\
& =\left(\begin{array}{ccc}
1 & -1 & -3 \\
-1 & -1 & -10 \\
-5 & 4 & 4
\end{array}\right)
\end{aligned}
$$
:::

:::

:::question{number="26" kind="exercise" id="q_3.26" topic="Proving a matrix polynomial identity"}
#### Question 26

:::prompt
If $\mathrm{A}=\left[\begin{array}{lll}1 & 0 & 2 \\ 0 & 2 & 1 \\ 2 & 0 & 3\end{array}\right]$, prove that $\mathrm{A}^{3}-6 \mathrm{~A}^{2}+7 \mathrm{~A}+2 \mathrm{I}=0$
:::

:::solution{label="Solution"}
$$
\begin{aligned}
A^{2} & =A \cdot A \\
& =\left(\begin{array}{lll}
1 & 0 & 2 \\
0 & 2 & 1 \\
2 & 0 & 3
\end{array}\right)\left(\begin{array}{lll}
1 & 0 & 2 \\
0 & 2 & 1 \\
2 & 0 & 3
\end{array}\right) \\
& =\left(\begin{array}{ccc}
1+0+4 & 0+0+0 & 2+0+6 \\
0+0+2 & 0+4+0 & 0+2+3 \\
2+0+6 & 0+0+0 & 4+0+9
\end{array}\right) \\
& =\left(\begin{array}{ccc}
5 & 0 & 8 \\
2 & 4 & 5 \\
8 & 0 & 13
\end{array}\right)
\end{aligned}
$$

Now,

$$
\begin{aligned}
A^{3} & =A^{2} . A \\
& =\left(\begin{array}{ccc}
5 & 0 & 8 \\
2 & 4 & 5 \\
8 & 0 & 13
\end{array}\right)\left(\begin{array}{ccc}
1 & 0 & 2 \\
0 & 2 & 1 \\
2 & 0 & 3
\end{array}\right) \\
& =\left(\begin{array}{ccc}
5+0+16 & 0+0+0 & 10+0+24 \\
2+0+10 & 0+8+0 & 4+4+15 \\
8+0+26 & 0+0+0 & 16+0+39
\end{array}\right) \\
& =\left(\begin{array}{lll}
21 & 0 & 34 \\
12 & 8 & 23 \\
34 & 0 & 55
\end{array}\right)
\end{aligned}
$$

Therefore,

$$
\begin{aligned}
A^{3}-6 A^{2}+7 A+2 I & =\left(\begin{array}{lll}
21 & 0 & 34 \\
12 & 8 & 23 \\
34 & 0 & 55
\end{array}\right)-6\left(\begin{array}{ccc}
5 & 0 & 8 \\
2 & 4 & 5 \\
8 & 0 & 13
\end{array}\right)+7\left(\begin{array}{ccc}
1 & 0 & 2 \\
0 & 2 & 1 \\
2 & 0 & 3
\end{array}\right)+2\left(\begin{array}{lll}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{array}\right) \\
& =\left(\begin{array}{lll}
21 & 0 & 34 \\
12 & 8 & 23 \\
34 & 0 & 55
\end{array}\right)-\left(\begin{array}{ccc}
30 & 0 & 48 \\
12 & 24 & 30 \\
48 & 0 & 78
\end{array}\right)+\left(\begin{array}{ccc}
7 & 0 & 14 \\
0 & 14 & 7 \\
14 & 0 & 21
\end{array}\right)+\left(\begin{array}{ccc}
2 & 0 & 0 \\
0 & 2 & 0 \\
0 & 0 & 2
\end{array}\right) \\
& =\left(\begin{array}{ccc}
21+7+2 & 0+0+0 & 34+14+0 \\
12+0+0 & 8+14+2 & 23+7+0 \\
34+14+0 & 0+0+0 & 55+21+2
\end{array}\right)-\left(\begin{array}{ccc}
30 & 0 & 48 \\
12 & 24 & 30 \\
48 & 0 & 78
\end{array}\right)
\end{aligned}
$$

$$
\begin{aligned}
& =\left(\begin{array}{ccc}
30 & 0 & 48 \\
12 & 24 & 30 \\
48 & 0 & 78
\end{array}\right)-\left(\begin{array}{ccc}
30 & 0 & 48 \\
12 & 24 & 30 \\
48 & 0 & 78
\end{array}\right) \\
& =\left(\begin{array}{lll}
0 & 0 & 0 \\
0 & 0 & 0 \\
0 & 0 & 0
\end{array}\right)=0
\end{aligned}
$$

Hence, $A^{3}-6 A^{2}+7 A+2 I=0$.
:::

:::

:::question{number="27" kind="exercise" id="q_3.27" topic="Finding k in a matrix equation A^2=kA-2I"}
#### Question 27

:::prompt
If $\mathrm{A}=\left[\begin{array}{ll}3 & -2 \\ 4 & -2\end{array}\right]$ and $\mathrm{I}=\left[\begin{array}{ll}1 & 0 \\ 0 & 1\end{array}\right]$, find $k$ so that $\mathrm{A}^{2}=k \mathrm{~A}-2 \mathrm{I}$
:::

:::solution{label="Solution"}
$$
\begin{aligned}
A^{2} & =A \cdot A \\
& =\left(\begin{array}{ll}
3 & -2 \\
4 & -2
\end{array}\right)\left(\begin{array}{ll}
3 & -2 \\
4 & -2
\end{array}\right) \\
& =\left(\begin{array}{ll}
3(3)+(-2)(4) & 3(-2)+(-2)(-2) \\
4(3)+(-2)(4) & 4(-2)+(-2)(-2)
\end{array}\right) \\
& =\left(\begin{array}{ll}
1 & -2 \\
4 & -4
\end{array}\right)
\end{aligned}
$$

Now,

$$
\begin{aligned}
& \Rightarrow A^{2}=k A-2 I \\
& \Rightarrow\left(\begin{array}{ll}
1 & -2 \\
4 & -4
\end{array}\right)=k\left(\begin{array}{ll}
3 & -2 \\
4 & -2
\end{array}\right)-2\left(\begin{array}{cc}
1 & 0 \\
0 & 1
\end{array}\right) \\
& \Rightarrow\left(\begin{array}{ll}
1 & -2 \\
4 & -4
\end{array}\right)=\left(\begin{array}{ll}
3 k & -2 k \\
4 k & -2 k
\end{array}\right)-\left(\begin{array}{cc}
2 & 0 \\
0 & 2
\end{array}\right) \\
& \Rightarrow\left(\begin{array}{ll}
1 & -2 \\
4 & -4
\end{array}\right)=\left(\begin{array}{cc}
3 k-2 & -2 k \\
4 k & -2 k-2
\end{array}\right)
\end{aligned}
$$

Comparing the corresponding elements, we have:

$$
\begin{aligned}
& 3 k-2=1 \\
& \Rightarrow 3 k=3 \\
& \Rightarrow k=1
\end{aligned}
$$

Therefore, the value of $k=1$.
:::

:::

:::question{number="28" kind="exercise" id="q_3.28" topic="Matrix identity with tan(alpha/2)"}
#### Question 28

:::prompt
If $\mathrm{A}=\left[\begin{array}{cc}0 & -\tan \frac{\alpha}{2} \\ \tan \frac{\alpha}{2} & 0\end{array}\right]$ and I is the identity matrix of order 2, show that $\mathrm{I}+\mathrm{A}=(\mathrm{I}-\mathrm{A})\left[\begin{array}{cc}\cos \alpha & -\sin \alpha \\ \sin \alpha & \cos \alpha\end{array}\right]$
:::

:::solution{label="Solution"}
$$
\begin{aligned}
L H S & =I+A \\
& =\left(\begin{array}{ll}
1 & 0 \\
0 & 1
\end{array}\right)+\left(\begin{array}{cc}
0 & -\tan \frac{\alpha}{2} \\
\tan \frac{\alpha}{2} & 0
\end{array}\right) \\
& =\left(\begin{array}{cc}
1 & -\tan \frac{\alpha}{2} \\
\tan \frac{\alpha}{2} & 1
\end{array}\right)
\end{aligned}
$$

$$
\begin{aligned}
\text { RHS } & =(I-A)\left(\begin{array}{cc}
\cos \alpha & -\sin \alpha \\
\sin \alpha & \cos \alpha
\end{array}\right) \\
& =\left(\begin{array}{cc}
1 & 0 \\
0 & 1
\end{array}\right)-\left(\begin{array}{cc}
0 & -\tan \frac{\alpha}{2} \\
\tan \frac{\alpha}{2} & 0
\end{array}\right)\left(\begin{array}{cc}
\cos \alpha & -\sin \alpha \\
\sin \alpha & \cos \alpha
\end{array}\right) \\
& =\left(\begin{array}{cc}
1 & \tan \frac{\alpha}{2} \\
-\tan \frac{\alpha}{2} & 1
\end{array}\right)\left(\begin{array}{cc}
\cos \alpha & -\sin \alpha \\
\sin \alpha & \cos \alpha
\end{array}\right) \\
& =\left(\begin{array}{cc}
\cos \alpha+\sin \alpha \tan \frac{\alpha}{2} & -\sin \alpha+\cos \alpha \tan \frac{\alpha}{2} \\
-\cos \alpha \tan \frac{\alpha}{2}+\sin \alpha & \sin \alpha \tan \frac{\alpha}{2}+\cos \alpha
\end{array}\right) \\
& =\left(\begin{array}{cc}
1-2 \sin ^{2} \frac{\alpha}{2}+2 \sin \frac{\alpha}{2} \cos \frac{\alpha}{2} \tan \frac{\alpha}{2} & -2 \sin \frac{\alpha}{2} \cos \frac{\alpha}{2}+\left(2 \cos ^{2} \frac{\alpha}{2}-1\right) \tan \frac{\alpha}{2} \\
-\left(2 \cos ^{2} \frac{\alpha}{2}-1\right) \tan \frac{\alpha}{2}+2 \sin \frac{\alpha}{2} \cos \frac{\alpha}{2} & 2 \sin \frac{\alpha}{2} \cos \frac{\alpha}{2} \tan \frac{\alpha}{2}+1-2 \sin ^{2} \frac{\alpha}{2}
\end{array}\right) \\
& =\left(\begin{array}{cc}
1-2 \sin ^{2} \frac{\alpha}{2}+2 \sin ^{2} \frac{\alpha}{2} & -2 \sin \frac{\alpha}{2} \cos \frac{\alpha}{2}+2 \sin ^{2} \frac{\alpha}{2} \cos ^{2}-\tan \frac{\alpha}{2} \\
-2 \sin \frac{\alpha}{2} \cos \frac{\alpha}{2}+\tan \frac{\alpha}{2}+2 \sin \frac{\alpha}{2} \cos \frac{\alpha}{2} & 2 \sin ^{2} \frac{\alpha}{2}+1-2 \sin ^{2} \frac{\alpha}{2}
\end{array}\right) \\
& =\left(\begin{array}{cc}
1 & -\tan \frac{\alpha}{2} \\
\tan \frac{\alpha}{2} & 1
\end{array}\right)
\end{aligned}
$$

Thus, from ${ }^{(1)}$ and (2), we get

$$
I+A=(I-A)\left(\begin{array}{cc}
\cos \alpha & -\sin \alpha \\
\sin \alpha & \cos \alpha
\end{array}\right)
$$
:::

:::

:::question{number="29" kind="exercise" id="q_3.29" topic="Matrix multiplication - trust fund investment"}
#### Question 29

:::prompt
A trust fund has ₹ 30,000 that must be invested in two different types of bonds. The first bond pays $5 \%$ interest per year, and the second bond pays $7 \%$ interest per year. Using matrix multiplication, determine how to divide ₹ 30,000 among the two types of bonds. If the trust fund must obtain an annual total interest of:
:::

:::part{label="(a)"}
:::prompt
₹ 1800
:::

:::

:::part{label="(b)"}
:::prompt
₹2000
:::

:::

:::solution{label="Solution"}
(i) Let ₹ $x$ be invested in the first bond. Then, the sum of money invested in the second bond will be ₹ $(30000-x)$.
It is given that the first bond pays $5 \%$ interest per year and the second bond pays $7 \%$ interest per year.
Therefore, in order to obtain an annual total interest of ₹1800, we have:
$$
\begin{aligned}
& {[x(30000-x)]\left[\begin{array}{c}
\frac{5}{100} \\
\frac{7}{100}
\end{array}\right]=1800 \quad \quad\left[\text { S.I for } 1 \text { year }=\frac{\text { Principal × Rate }}{100}\right]} \\
& \Rightarrow \frac{5 x}{100}+\frac{7(30000-x)}{100}=1800 \\
& \Rightarrow 5 x+210000-7 x=180000 \\
& \Rightarrow 210000-2 x=180000 \\
& \Rightarrow 2 x=210000-180000 \\
& \Rightarrow 2 x=30000 \\
& \Rightarrow x=15000
\end{aligned}
$$
Thus, in order to obtain an annual total interest of ₹1800, the trust fund should invest ₹15000 in the first bond and the remaining ₹15000 in the second bond.
(ii) Let ₹ $x$ be invested in the first bond. Then, the sum of money invested in the second bond will be ₹ ( $30000-x)$.
Therefore, in order to obtain an annual total interest of ₹2000, we have:
$$
\begin{aligned}
& {[x(30000-x)]\left[\begin{array}{c}
\frac{5}{100} \\
\frac{7}{100}
\end{array}\right]=2000} \\
& \Rightarrow \frac{5 x}{100}+\frac{7(30000-x)}{100}=2000 \\
& \Rightarrow 5 x+210000-7 x=200000 \\
& \Rightarrow 210000-2 x=200000 \\
& \Rightarrow 2 x=210000-200000 \\
& \Rightarrow 2 x=10000 \\
& \Rightarrow x=5000
\end{aligned}
$$
Thus, in order to obtain an annual total interest of ₹1800, the trust fund should invest ₹5000 in the first bond and the remaining ₹25000 in the second bond.
:::

:::

:::question{number="30" kind="exercise" id="q_3.30" topic="Matrix multiplication - bookshop revenue"}
#### Question 30

:::prompt
The bookshop of a particular school has 10 dozen chemistry books, 8 dozen physics books, 10 dozen economics books. Their selling prices are ₹ 80, ₹ 60 and ₹ 40 each respectively. Find the total amount the bookshop will receive from selling all the books using matrix algebra.

Assume X, Y, Z, W and P are matrices of order $2 \times n, 3 \times k, 2 \times p, n \times 3$ and $p \times k$, respectively. Choose the correct answer in Exercises 21 and 22.
:::

:::solution{label="Solution"}
The total amount of money that will be received from the sale of all these books can be represented in the form of a matrix as:

$$
\begin{aligned}
12\left[\begin{array}{lll}
10 & 8 & 10
\end{array}\right]\left[\begin{array}{l}
80 \\
60 \\
40
\end{array}\right] & =12[10(80)+8(60)+10(40)] \\
& =12(800+480+400) \\
& =12(1680) \\
& =20160
\end{aligned}
$$

Thus, the bookshop will receive ₹ 20160 from the sale of all these books.
:::

:::

:::question{number="31" kind="exercise" id="q_3.31" topic="MCQ - restriction on matrix order for a sum"}
#### Question 31

:::prompt
The restriction on $n, k$ and $p$ so that $\mathrm{PY}+\mathrm{WY}$ will be defined are:
(A) $k=3, p=n$
(B) $k$ is arbitrary, $p=2$
(C) $p$ is arbitrary, $k=3$
(D) $k=2, p=3$
:::

:::solution{label="Solution"}
Matrices $P$ and $Y$ are of the orders $p \times k$ and $3 \times k$ respectively.
Therefore, matrix $P Y$ will be defined if $k=3$.
Consequently, $P Y$ will be of the order $p \times k$.
Matrices $W$ and $Y$ are of the orders $n \times 3$ and $3 \times k$ respectively.
Since the number of columns in $W$ is equal to the number of rows in $Y$, matrix $W Y$ is welldefined and is of the order $n \times k$.

Matrices $P Y$ and $W Y$ can be added only when their orders are the same.
However, $P Y$ is of the order $p \times k$ and $W Y$ is of the order $n \times k$.
Therefore, we must have $p=n$.

Thus, $k=3$ and $p=n$ are the restrictions on $n, k$ and $p$ so that $P Y+W Y$ will be defined.
The correct option is A.
:::

:::

:::question{number="32" kind="exercise" id="q_3.32" topic="MCQ - order of a matrix combination"}
#### Question 32

:::prompt
If $n=p$, then the order of the matrix $7 \mathrm{X}-5 \mathrm{Z}$ is:
(A) $p \times 2$
(B) $2 \times n$
(C) $n \times 3$
(D) $p \times n$
:::

:::solution{label="Solution"}
Matrix $X$ is of the order $2 \times n$.
Therefore, matrix $7 X$ is also of the same order.
Matrix $Z$ is of the order $2 \times p$, i.e., $2 \times n$ [Since $n=p$ ]
Therefore, matrix $5 Z$ is also of the same order.
Now, both the matrices $7 X$ and 5 Z are of the order $2 \times n$.

Thus, matrix $7 X-5 Z$ is well-defined and is of the order $2 \times n$.
The correct option is B.

## EXERCISE 3.3
:::

:::

:::question{number="33" kind="exercise" id="q_3.33" topic="Transpose of given matrices"}
#### Question 33

:::prompt
Find the transpose of each of the following matrices:
:::

:::part{label="(i)"}
:::prompt
$\left[\begin{array}{c}5 \\ \frac{1}{2} \\ -1\end{array}\right]$
:::

:::

:::part{label="(ii)"}
:::prompt
$\left[\begin{array}{rr}1 & -1 \\ 2 & 3\end{array}\right]$
:::

:::

:::part{label="(iii)"}
:::prompt
$\left[\begin{array}{ccc}-1 & 5 & 6 \\ \sqrt{3} & 5 & 6 \\ 2 & 3 & -1\end{array}\right]$
:::

:::

:::solution{label="Solution"}
(i) Let
$$
A=\left(\begin{array}{c}
5 \\
\frac{1}{2} \\
-1
\end{array}\right)
$$
Then $A^{T}=\left(\begin{array}{lll}5 & \frac{1}{2} & -1\end{array}\right)$
(ii) Let $A=\left(\begin{array}{cc}1 & -1 \\ 2 & 3\end{array}\right)$
Then $A^{T}=\left(\begin{array}{cc}1 & 2 \\ -1 & 3\end{array}\right)$
(iii) Let
$$
A^{T}=\left(\begin{array}{ccc}
-1 & \sqrt{3} & 2 \\
5 & 5 & 3 \\
6 & 6 & -1
\end{array}\right)
$$
:::

:::

:::question{number="34" kind="exercise" id="q_3.34" topic="Verifying transpose of sum and difference"}
#### Question 34

:::prompt
If $\mathrm{A}=\left[\begin{array}{rrr}-1 & 2 & 3 \\ 5 & 7 & 9 \\ -2 & 1 & 1\end{array}\right]$ and $\mathrm{B}=\left[\begin{array}{rrr}-4 & 1 & -5 \\ 1 & 2 & 0 \\ 1 & 3 & 1\end{array}\right]$, then verify that
:::

:::part{label="(i)"}
:::prompt
$(\mathrm{A}+\mathrm{B})^{\prime}=\mathrm{A}^{\prime}+\mathrm{B}^{\prime}$,
:::

:::

:::part{label="(ii)"}
:::prompt
$(\mathrm{A}-\mathrm{B})^{\prime}=\mathrm{A}^{\prime}-\mathrm{B}^{\prime}$
:::

:::

:::solution{label="Solution"}
It is given that

$$
A=\left(\begin{array}{ccc}
-1 & 2 & 3 \\
5 & 7 & 9 \\
-2 & 1 & 1
\end{array}\right) \text { and } B=\left(\begin{array}{ccc}
-4 & 1 & -5 \\
1 & 2 & 0 \\
1 & 3 & 1
\end{array}\right)
$$

Hence, we have

$$
A^{\prime}=\left(\begin{array}{ccc}
-1 & 5 & -2 \\
2 & 7 & 1 \\
3 & 9 & 1
\end{array}\right) \text { and } B^{\prime}=\left(\begin{array}{ccc}
-4 & 1 & 1 \\
1 & 2 & 3 \\
-5 & 0 & 1
\end{array}\right)
$$

(i) $$
(A+B)=\left(\begin{array}{ccc}
-1 & 2 & 3 \\
5 & 7 & 9 \\
-2 & 1 & 1
\end{array}\right)+\left(\begin{array}{ccc}
-4 & 1 & -5 \\
1 & 2 & 0 \\
1 & 3 & 1
\end{array}\right)=\left(\begin{array}{ccc}
-5 & 3 & -2 \\
6 & 9 & 9 \\
-1 & 4 & 2
\end{array}\right)
$$
Hence,
$$
(A+B)^{\prime}=\left(\begin{array}{ccc}
-5 & 6 & -1 \\
3 & 9 & 4 \\
-2 & 9 & 2
\end{array}\right)
$$
Now,
$$
\begin{aligned}
A^{\prime}+B^{\prime} & =\left(\begin{array}{ccc}
-1 & 5 & -2 \\
2 & 7 & 1 \\
3 & 9 & 1
\end{array}\right)+\left(\begin{array}{ccc}
-4 & 1 & 1 \\
1 & 2 & 3 \\
-5 & 0 & 1
\end{array}\right) \\
& =\left(\begin{array}{ccc}
-5 & 6 & -1 \\
3 & 9 & 4 \\
-2 & 9 & 2
\end{array}\right)
\end{aligned}
$$
Thus, $(A+B)^{\prime}=A^{\prime}+B^{\prime}$.

(ii) $$
(A-B)=\left(\begin{array}{ccc}
-1 & 2 & 3 \\
5 & 7 & 9 \\
-2 & 1 & 1
\end{array}\right)-\left(\begin{array}{ccc}
-4 & 1 & -5 \\
1 & 2 & 0 \\
1 & 3 & 1
\end{array}\right)=\left(\begin{array}{ccc}
3 & 1 & 8 \\
4 & 5 & 9 \\
-3 & -2 & 0
\end{array}\right)
$$
Hence,
$$
(A-B)^{\prime}=\left(\begin{array}{ccc}
3 & 4 & -3 \\
1 & 5 & -2 \\
8 & 9 & 0
\end{array}\right)
$$
Now,
$$
\begin{aligned}
A^{\prime}-B^{\prime} & =\left(\begin{array}{ccc}
-1 & 5 & -2 \\
2 & 7 & 1 \\
3 & 9 & 1
\end{array}\right)-\left(\begin{array}{ccc}
-4 & 1 & 1 \\
1 & 2 & 3 \\
-5 & 0 & 1
\end{array}\right) \\
& =\left(\begin{array}{ccc}
3 & 4 & -3 \\
1 & 5 & -2 \\
8 & 9 & 0
\end{array}\right)
\end{aligned}
$$
Thus, $(A-B)^{\prime}=A^{\prime}-B^{\prime}$.
:::

:::

:::question{number="35" kind="exercise" id="q_3.35" topic="Verifying transpose of sum and difference"}
#### Question 35

:::prompt
If $\mathrm{A}^{\prime}=\left[\begin{array}{rr}3 & 4 \\ -1 & 2 \\ 0 & 1\end{array}\right]$ and $\mathrm{B}=\left[\begin{array}{rrr}-1 & 2 & 1 \\ 1 & 2 & 3\end{array}\right]$, then verify that
:::

:::part{label="(i)"}
:::prompt
$(\mathrm{A}+\mathrm{B})^{\prime}=\mathrm{A}^{\prime}+\mathrm{B}^{\prime}$
:::

:::

:::part{label="(ii)"}
:::prompt
$(\mathrm{A}-\mathrm{B})^{\prime}=\mathrm{A}^{\prime}-\mathrm{B}^{\prime}$
:::

:::

:::solution{label="Solution"}
It is known that $A=\left(A^{\prime}\right)^{\prime}$
Hence,

$$
A=\left(\begin{array}{ccc}
3 & -1 & 0 \\
4 & 2 & 1
\end{array}\right) \text { and } B^{\prime}=\left(\begin{array}{cc}
-1 & 1 \\
2 & 2 \\
1 & 3
\end{array}\right)
$$

(i) $\quad A+B=\left(\begin{array}{ccc}3 & -1 & 0 \\ 4 & 2 & 1\end{array}\right)+\left(\begin{array}{ccc}-1 & 2 & 1 \\ 1 & 2 & 3\end{array}\right)=\left(\begin{array}{lll}2 & 1 & 1 \\ 5 & 4 & 4\end{array}\right)$

Therefore,

$$
(A+B)^{\prime}=\left(\begin{array}{ll}
2 & 5 \\
1 & 4 \\
1 & 4
\end{array}\right)
$$

Now,

$$
A^{\prime}+B^{\prime}=\left(\begin{array}{cc}
3 & 4 \\
-1 & 2 \\
0 & 1
\end{array}\right)+\left(\begin{array}{cc}
-1 & 1 \\
2 & 2 \\
1 & 3
\end{array}\right)=\left(\begin{array}{ll}
2 & 5 \\
1 & 4 \\
1 & 4
\end{array}\right)
$$

Hence, $(A+B)^{\prime}=A^{\prime}+B^{\prime}$.
(ii)

$$
A-B=\left(\begin{array}{ccc}
3 & -1 & 0 \\
4 & 2 & 1
\end{array}\right)-\left(\begin{array}{ccc}
-1 & 2 & 1 \\
1 & 2 & 3
\end{array}\right)=\left(\begin{array}{ccc}
4 & -3 & -1 \\
3 & 0 & -2
\end{array}\right)
$$

Therefore,

$$
(A-B)^{\prime}=\left(\begin{array}{cc}
4 & 3 \\
-3 & 0 \\
-1 & -2
\end{array}\right)
$$

Now,

$$
A^{\prime}-B^{\prime}=\left(\begin{array}{cc}
3 & 4 \\
-1 & 2 \\
0 & 1
\end{array}\right)-\left(\begin{array}{cc}
-1 & 1 \\
2 & 2 \\
1 & 3
\end{array}\right)=\left(\begin{array}{cc}
4 & 3 \\
-3 & 0 \\
-1 & -2
\end{array}\right)
$$

Hence, $(A-B)^{\prime}=A^{\prime}-B^{\prime}$.
:::

:::

:::question{number="36" kind="exercise" id="q_3.36" topic="Finding the transpose of (A+2B)"}
#### Question 36

:::prompt
If $\mathrm{A}^{\prime}=\left[\begin{array}{cc}-2 & 3 \\ 1 & 2\end{array}\right]$ and $\mathrm{B}=\left[\begin{array}{rr}-1 & 0 \\ 1 & 2\end{array}\right]$, then find $(\mathrm{A}+2 \mathrm{~B})^{\prime}$
:::

:::solution{label="Solution"}
It is known that $A=\left(A^{\prime}\right)^{\prime}$.
Therefore,

$$
A=\left(\begin{array}{cc}
-2 & 1 \\
3 & 2
\end{array}\right)
$$

Now,

$$
\begin{aligned}
A+2 B & =\left(\begin{array}{cc}
-2 & 1 \\
3 & 2
\end{array}\right)+2\left(\begin{array}{cc}
-1 & 0 \\
1 & 2
\end{array}\right) \\
& =\left(\begin{array}{cc}
-2 & 1 \\
3 & 2
\end{array}\right)+\left(\begin{array}{cc}
-2 & 0 \\
2 & 4
\end{array}\right) \\
& =\left(\begin{array}{cc}
-4 & 1 \\
5 & 6
\end{array}\right)
\end{aligned}
$$
:::

:::

:::question{number="37" kind="exercise" id="q_3.37" topic="Verifying (AB)'=B'A'"}
#### Question 37

:::prompt
For the matrices A and B, verify that $(\mathrm{AB})^{\prime}=\mathrm{B}^{\prime} \mathrm{A}^{\prime}$, where
:::

:::part{label="(i)"}
:::prompt
$\mathrm{A}=\left[\begin{array}{r}1 \\ -4 \\ 3\end{array}\right], \mathrm{B}=[-1$
2 1]
:::

:::

:::part{label="(ii)"}
:::prompt
$\mathrm{A}=\left[\begin{array}{l}0 \\ 1 \\ 2\end{array}\right], \mathrm{B}=\left[\begin{array}{lll}1 & 5 & 7\end{array}\right]$
:::

:::

:::solution{label="Solution"}
(i)

$$
A=\left[\begin{array}{c}
1 \\
-4 \\
3
\end{array}\right] \text { and } B=\left[\begin{array}{lll}
-1 & 2 & 1
\end{array}\right]
$$

Hence,

$$
\begin{aligned}
A B & =\left[\begin{array}{c}
1 \\
-4 \\
3
\end{array}\right]\left[\begin{array}{lll}
-1 & 2 & 1
\end{array}\right] \\
& =\left[\begin{array}{ccc}
-1 & 2 & 1 \\
4 & -8 & -4 \\
-3 & 6 & 3
\end{array}\right]
\end{aligned}
$$

Therefore,

$$
(A B)^{\prime}=\left[\begin{array}{ccc}
-1 & 4 & -3 \\
2 & -8 & 6 \\
1 & -4 & 3
\end{array}\right]
$$

Now,

$$
A^{\prime}=\left[\begin{array}{lll}
1 & -4 & 3
\end{array}\right] \text { and } B^{\prime}=\left[\begin{array}{c}
-1 \\
2 \\
1
\end{array}\right]
$$

Hence,

$$
\begin{aligned}
B^{\prime} A^{\prime} & =\left[\begin{array}{c}
-1 \\
2 \\
1
\end{array}\right]\left[\begin{array}{lll}
1 & -4 & 3
\end{array}\right] \\
& =\left[\begin{array}{ccc}
-1 & 4 & -3 \\
2 & -8 & 6 \\
1 & -4 & 3
\end{array}\right]
\end{aligned}
$$

Thus, $(A B)^{\prime}=B^{\prime} A^{\prime}$

(ii) It is given that It is given that and $B=\left[\begin{array}{lll}1 & 5 & 7\end{array}\right]$ Hence,
$$
\begin{aligned}
A B & =\left[\begin{array}{l}
0 \\
1 \\
2
\end{array}\right]\left[\begin{array}{lll}
1 & 5 & 7
\end{array}\right] \\
& =\left[\begin{array}{ccc}
0 & 0 & 0 \\
1 & 5 & 7 \\
2 & 10 & 14
\end{array}\right]
\end{aligned}
$$
Therefore,
$$
(A B)^{\prime}=\left[\begin{array}{ccc}
0 & 1 & 2 \\
0 & 5 & 10 \\
0 & 7 & 14
\end{array}\right]
$$
Now,
$$
A^{\prime}=\left[\begin{array}{lll}
0 & 1 & 2
\end{array}\right] \text { and } B^{\prime}=\left[\begin{array}{l}
1 \\
5 \\
7
\end{array}\right]
$$
Therefore,
$$
\begin{aligned}
B^{\prime} A^{\prime} & =\left[\begin{array}{l}
1 \\
5 \\
7
\end{array}\right]\left[\begin{array}{lll}
0 & 1 & 2
\end{array}\right] \\
& =\left[\begin{array}{ccc}
0 & 1 & 2 \\
0 & 5 & 10 \\
0 & 7 & 14
\end{array}\right]
\end{aligned}
$$

Thus, $(A B)^{\prime}=B^{\prime} A^{\prime}$.
:::

:::

:::question{number="38" kind="exercise" id="q_3.38" topic="Verifying A'A=I for a rotation-type matrix"}
#### Question 38

:::prompt
If (i) $\mathrm{A}=\left[\begin{array}{cc}\cos \alpha & \sin \alpha \\ -\sin \alpha & \cos \alpha\end{array}\right]$, then verify that $\mathrm{A}^{\prime} \mathrm{A}=\mathrm{I}$

(ii) If $\mathrm{A}=\left[\begin{array}{cc}\sin \alpha & \cos \alpha \\ -\cos \alpha & \sin \alpha\end{array}\right]$, then verify that $\mathrm{A}^{\prime} \mathrm{A}=\mathrm{I}$
:::

:::solution{label="Solution"}
(i) $$
\text { It is given that } A=\left(\begin{array}{cc}
\cos \alpha & \sin \alpha \\
-\sin \alpha & \cos \alpha
\end{array}\right)
$$
Therefore,
$$
A^{\prime}=\left(\begin{array}{cc}
\cos \alpha & -\sin \alpha \\
\sin \alpha & \cos \alpha
\end{array}\right)
$$
Now,
$$
\begin{aligned}
A^{\prime} A & =\left(\begin{array}{cc}
\cos \alpha & -\sin \alpha \\
\sin \alpha & \cos \alpha
\end{array}\right)\left(\begin{array}{cc}
\cos \alpha & \sin \alpha \\
-\sin \alpha & \cos \alpha
\end{array}\right) \\
& =\left(\begin{array}{cc}
\cos \alpha \cos \alpha+(-\sin \alpha)(-\sin \alpha) & \sin \alpha \cos \alpha+(-\sin \alpha) \cos \alpha \\
\sin \alpha \cos \alpha+\cos \alpha(-\sin \alpha) & \sin \alpha \sin \alpha+\cos \alpha \cos \alpha
\end{array}\right) \\
& =\left(\begin{array}{cc}
\cos ^{2} \alpha+\sin ^{2} \alpha & \sin \alpha \cos \alpha-\sin \alpha \cos \alpha \\
\sin \alpha \cos \alpha-\sin \alpha \cos \alpha & \sin ^{2} \alpha+\cos ^{2} \alpha
\end{array}\right) \\
& =\left(\begin{array}{ll}
1 & 0 \\
0 & 1
\end{array}\right) \\
& =I
\end{aligned}
$$
Thus, $A^{\prime} A=I$
(ii) $$
\begin{aligned}
& \text { It is given that } \quad(-\cos \alpha \\
& \text { Therefore, } \\
& \qquad A^{\prime}=\left(\begin{array}{cc}
\sin \alpha & -\cos \alpha \\
\cos \alpha & \sin \alpha
\end{array}\right)
\end{aligned}
$$
Now,

$$
\begin{aligned}
A^{\prime} A & =\left(\begin{array}{cc}
\sin \alpha & -\cos \alpha \\
\cos \alpha & \sin \alpha
\end{array}\right)\left(\begin{array}{cc}
\sin \alpha & \cos \alpha \\
-\cos \alpha & \sin \alpha
\end{array}\right) \\
& =\left(\begin{array}{cc}
\sin \alpha \sin \alpha+(-\cos \alpha)(-\cos \alpha) & \sin \alpha \cos \alpha+(-\cos \alpha) \sin \alpha \\
\sin \alpha \cos \alpha+\sin \alpha(-\cos \alpha) & \sin \alpha \sin \alpha+\cos \alpha \cos \alpha
\end{array}\right) \\
& =\left(\begin{array}{cc}
\cos ^{2} \alpha+\sin ^{2} \alpha & \sin \alpha \cos \alpha-\sin \alpha \cos \alpha \\
\sin \alpha \cos \alpha-\sin \alpha \cos \alpha & \sin ^{2} \alpha+\cos ^{2} \alpha
\end{array}\right) \\
& =\left(\begin{array}{ll}
1 & 0 \\
0 & 1
\end{array}\right) \\
& =I
\end{aligned}
$$

Thus, $A^{\prime} A=I$
:::

:::

:::question{number="39" kind="exercise" id="q_3.39" topic="Showing a matrix is symmetric or skew symmetric"}
#### Question 39

:::part{label="(i)"}
:::prompt
Show that the matrix $\mathrm{A}=\left[\begin{array}{rrr}1 & -1 & 5 \\ -1 & 2 & 1 \\ 5 & 1 & 3\end{array}\right]$ is a symmetric matrix.
:::

:::

:::part{label="(ii)"}
:::prompt
Show that the matrix $\mathrm{A}=\left[\begin{array}{rrr}0 & 1 & -1 \\ -1 & 0 & 1 \\ 1 & -1 & 0\end{array}\right]$ is a skew symmetric matrix.
:::

:::

:::solution{label="Solution"}
(i) $A=\left(\begin{array}{ccc}1 & -1 & 5 \\ -1 & 2 & 1 \\ 5 & 1 & 3\end{array}\right)$
Now,
$$
\begin{aligned}
A^{\prime} & =\left(\begin{array}{ccc}
1 & -1 & 5 \\
-1 & 2 & 1 \\
5 & 1 & 3
\end{array}\right) \\
& =A
\end{aligned}
$$
Hence, A is a symmetric matrix.
(ii) $A=\left(\begin{array}{ccc}0 & 1 & -1 \\ -1 & 0 & 1 \\ 1 & -1 & 0\end{array}\right)$

$$
\begin{aligned}
A^{\prime} & =\left(\begin{array}{ccc}
0 & -1 & 1 \\
1 & 0 & -1 \\
-1 & 1 & 0
\end{array}\right) \\
& =-\left(\begin{array}{ccc}
0 & 1 & -1 \\
-1 & 0 & 1 \\
1 & -1 & 0
\end{array}\right) \\
& =-A
\end{aligned}
$$

Hence, A is a skew symmetric matrix.
:::

:::

:::question{number="40" kind="exercise" id="q_3.40" topic="Verifying A+A' symmetric, A-A' skew symmetric"}
#### Question 40

:::prompt
For the matrix $\mathrm{A}=\left[\begin{array}{cc}1 & 5 \\ 6 & 7\end{array}\right]$, verify that
:::

:::part{label="(i)"}
:::prompt
( $\mathrm{A}+\mathrm{A}^{\prime}$ ) is a symmetric matrix
:::

:::

:::part{label="(ii)"}
:::prompt
(A - A') is a skew symmetric matrix
:::

:::

:::solution{label="Solution"}
It is given that $A=\left(\begin{array}{ll}1 & 5 \\ 6 & 7\end{array}\right)$
Hence, $A^{\prime}=\left(\begin{array}{ll}1 & 6 \\ 5 & 7\end{array}\right)$

(i) $\quad\left(A+A^{\prime}\right)=\left(\begin{array}{ll}1 & 5 \\ 6 & 7\end{array}\right)+\left(\begin{array}{ll}1 & 6 \\ 5 & 7\end{array}\right)=\left(\begin{array}{cc}2 & 11 \\ 11 & 14\end{array}\right)$
Therefore,
$$
\begin{aligned}
\left(A+A^{\prime}\right)^{\prime} & =\left(\begin{array}{cc}
2 & 11 \\
11 & 14
\end{array}\right) \\
& =\left(A+A^{\prime}\right)
\end{aligned}
$$
Thus, $\left(A+A^{\prime}\right)$ is a symmetric matrix.
(ii) $\quad\left(A-A^{\prime}\right)=\left(\begin{array}{ll}1 & 5 \\ 6 & 7\end{array}\right)-\left(\begin{array}{ll}1 & 6 \\ 5 & 7\end{array}\right)=\left(\begin{array}{cc}0 & -1 \\ -1 & 0\end{array}\right)$
Therefore,
$$
\begin{aligned}
\left(A-A^{\prime}\right)^{\prime} & =\left(\begin{array}{cc}
0 & 1 \\
-1 & 0
\end{array}\right) \\
& =-\left(\begin{array}{cc}
0 & -1 \\
1 & 0
\end{array}\right) \\
& =-\left(A-A^{\prime}\right)
\end{aligned}
$$

Thus, $\left(A-A^{\prime}\right)$ is a skew symmetric matrix.
:::

:::

:::question{number="41" kind="exercise" id="q_3.41" topic="Finding symmetric and skew-symmetric parts"}
#### Question 41

:::prompt
Find $\frac{1}{2}\left(\mathrm{~A}+\mathrm{A}^{\prime}\right)$ and $\frac{1}{2}\left(\mathrm{~A}-\mathrm{A}^{\prime}\right)$, when $\mathrm{A}=\left[\begin{array}{rrr}0 & a & b \\ -a & 0 & c \\ -b & -c & 0\end{array}\right]$
:::

:::solution{label="Solution"}
It is given that

$$
A=\left(\begin{array}{ccc}
0 & a & b \\
-a & 0 & c \\
-b & -c & 0
\end{array}\right)
$$

Hence,

$$
A^{\prime}=\left(\begin{array}{ccc}
0 & -a & -b \\
a & 0 & -c \\
b & c & 0
\end{array}\right)
$$

Now,

$$
\begin{aligned}
\left(A+A^{\prime}\right) & =\left(\begin{array}{ccc}
0 & a & b \\
-a & 0 & c \\
-b & -c & 0
\end{array}\right)+\left(\begin{array}{ccc}
0 & -a & -b \\
a & 0 & -c \\
b & c & 0
\end{array}\right) \\
& =\left(\begin{array}{lll}
0 & 0 & 0 \\
0 & 0 & 0 \\
0 & 0 & 0
\end{array}\right)
\end{aligned}
$$

Therefore,

$$
\frac{1}{2}\left(A+A^{\prime}\right)=\left(\begin{array}{lll}
0 & 0 & 0 \\
0 & 0 & 0 \\
0 & 0 & 0
\end{array}\right)
$$

Now,

$$
\begin{array}{r}
\left(A-A^{\prime}\right)=\left(\begin{array}{ccc}
0 & a & b \\
-a & 0 & c \\
-b & -c & 0
\end{array}\right)-\left(\begin{array}{ccc}
0 & -a & -b \\
a & 0 & -c \\
b & c & 0
\end{array}\right) \\
=\left(\begin{array}{ccc}
0 & 2 a & 2 b \\
-2 a & 0 & 2 c \\
-2 b & -2 c & 0
\end{array}\right)
\end{array}
$$

Thus,

$$
\begin{aligned}
\frac{1}{2}\left(A-A^{\prime}\right)= & \left(\begin{array}{ccc}
0 & 2 a & 2 b \\
-2 a & 0 & 2 c \\
-2 b & -2 c & 0
\end{array}\right) \\
& =\left(\begin{array}{ccc}
0 & a & b \\
-a & 0 & c \\
-b & -c & 0
\end{array}\right)
\end{aligned}
$$
:::

:::

:::question{number="42" kind="exercise" id="q_3.42" topic="Expressing matrices as symmetric plus skew-symmetric parts"}
#### Question 42

:::prompt
Express the following matrices as the sum of a symmetric and a skew symmetric matrix:
:::

:::part{label="(i)"}
:::prompt
$\left[\begin{array}{rr}3 & 5 \\ 1 & -1\end{array}\right]$
:::

:::

:::part{label="(ii)"}
:::prompt
$\left[\begin{array}{rrr}6 & -2 & 2 \\ -2 & 3 & -1 \\ 2 & -1 & 3\end{array}\right]$
:::

:::

:::part{label="(iii)"}
:::prompt
$\left[\begin{array}{rrr}3 & 3 & -1 \\ -2 & -2 & 1 \\ -4 & -5 & 2\end{array}\right]$
:::

:::

:::part{label="(iv)"}
:::prompt
$\left[\begin{array}{rr}1 & 5 \\ -1 & 2\end{array}\right]$

Choose the correct answer in the Exercises 11 and 12 .
:::

:::

:::solution{label="Solution"}
(i) Let $A=\left(\begin{array}{cc}3 & 5 \\ 1 & -1\end{array}\right)$
Hence,
$$
A^{\prime}=\left(\begin{array}{cc}
3 & 1 \\
5 & -1
\end{array}\right)
$$
Now,
$$
\begin{aligned}
\left(A+A^{\prime}\right) & =\left(\begin{array}{cc}
3 & 5 \\
1 & -1
\end{array}\right)+\left(\begin{array}{cc}
3 & 1 \\
5 & -1
\end{array}\right) \\
& =\left(\begin{array}{cc}
6 & 6 \\
6 & -2
\end{array}\right)
\end{aligned}
$$
Let

$$
\begin{aligned}
P & =\frac{1}{2}\left(A+A^{\prime}\right) \\
& =\frac{1}{2}\left(\begin{array}{cc}
6 & 6 \\
6 & -2
\end{array}\right) \\
& =\left(\begin{array}{cc}
3 & 3 \\
3 & -1
\end{array}\right)
\end{aligned}
$$

Now,

$$
\begin{aligned}
P^{\prime} & =\left(\begin{array}{cc}
3 & 3 \\
3 & -1
\end{array}\right) \\
& =P
\end{aligned}
$$

Thus, $P=\frac{1}{2}\left(A+A^{\prime}\right)$ is a symmetric matrix.

Now,

$$
\begin{aligned}
\left(A-A^{\prime}\right) & =\left(\begin{array}{cc}
3 & 5 \\
1 & -1
\end{array}\right)-\left(\begin{array}{cc}
3 & 1 \\
5 & -1
\end{array}\right) \\
& =\left(\begin{array}{cc}
0 & 4 \\
-4 & 0
\end{array}\right)
\end{aligned}
$$

Let

$$
\begin{aligned}
Q & =\frac{1}{2}\left(A-A^{\prime}\right) \\
& =\frac{1}{2}\left(\begin{array}{cc}
0 & 4 \\
-4 & 0
\end{array}\right) \\
& =\left(\begin{array}{cc}
0 & 2 \\
-2 & 0
\end{array}\right)
\end{aligned}
$$

Now,

$$
\begin{aligned}
Q^{\prime} & =\left(\begin{array}{cc}
0 & -2 \\
2 & 0
\end{array}\right) \\
& =-Q
\end{aligned}
$$

Thus, $Q=\frac{1}{2}\left(A-A^{\prime}\right)$ is a skew symmetric matrix.
Representing $A$ as the sum of $P$ and $Q$ :

$$
\begin{aligned}
P+Q & =\left(\begin{array}{cc}
3 & 3 \\
3 & -1
\end{array}\right)+\left(\begin{array}{cc}
0 & 2 \\
-2 & 0
\end{array}\right) \\
& =\left(\begin{array}{cc}
3 & 5 \\
1 & -1
\end{array}\right) \\
& =A
\end{aligned}
$$
(ii) Let
$$
A=\left(\begin{array}{ccc}
6 & -2 & 2 \\
-2 & 3 & -1 \\
2 & -1 & 3
\end{array}\right)
$$
Hence,
$$
A^{\prime}=\left(\begin{array}{ccc}
6 & -2 & 2 \\
-2 & 3 & -1 \\
2 & -1 & 3
\end{array}\right)
$$
Now,
$$
\left(A+A^{\prime}\right)=\left(\begin{array}{ccc}
6 & -2 & 2 \\
-2 & 3 & -1 \\
2 & -1 & 3
\end{array}\right)+\left(\begin{array}{ccc}
6 & -2 & 2 \\
-2 & 3 & -1 \\
2 & -1 & 3
\end{array}\right)=\left(\begin{array}{ccc}
12 & -4 & 4 \\
-4 & 6 & -2 \\
4 & -2 & 6
\end{array}\right)
$$
Let
$$
\begin{aligned}
P & =\frac{1}{2}\left(A+A^{\prime}\right) \\
& =\frac{1}{2}\left(\begin{array}{ccc}
12 & -4 & 4 \\
-4 & 6 & -2 \\
4 & -2 & 6
\end{array}\right) \\
& =\left(\begin{array}{ccc}
6 & -2 & 2 \\
-2 & 3 & -1 \\
2 & -1 & 3
\end{array}\right)
\end{aligned}
$$
Now,
$$
\begin{aligned}
P^{\prime} & =\left(\begin{array}{ccc}
6 & -2 & 2 \\
-2 & 3 & -1 \\
2 & -1 & 3
\end{array}\right) \\
& =P
\end{aligned}
$$
Thus, $P=\frac{1}{2}\left(A+A^{\prime}\right)$ is a symmetric matrix.

Now,

$$
\begin{aligned}
\left(A-A^{\prime}\right) & =\left(\begin{array}{ccc}
6 & -2 & 2 \\
-2 & 3 & -1 \\
2 & -1 & 3
\end{array}\right)-\left(\begin{array}{ccc}
6 & -2 & 2 \\
-2 & 3 & -1 \\
2 & -1 & 3
\end{array}\right) \\
& =\left(\begin{array}{lll}
0 & 0 & 0 \\
0 & 0 & 0 \\
0 & 0 & 0
\end{array}\right)
\end{aligned}
$$

Let

$$
\begin{aligned}
Q & =\frac{1}{2}\left(A-A^{\prime}\right) \\
& =\frac{1}{2}\left(\begin{array}{lll}
0 & 0 & 0 \\
0 & 0 & 0 \\
0 & 0 & 0
\end{array}\right) \\
& =\left(\begin{array}{lll}
0 & 0 & 0 \\
0 & 0 & 0 \\
0 & 0 & 0
\end{array}\right)
\end{aligned}
$$

Now,

$$
\begin{aligned}
Q^{\prime} & =\left(\begin{array}{lll}
0 & 0 & 0 \\
0 & 0 & 0 \\
0 & 0 & 0
\end{array}\right) \\
& =-Q
\end{aligned}
$$

Thus, $Q=\frac{1}{2}\left(A-A^{\prime}\right)$ is a skew symmetric matrix.
Representing $A$ as the sum of $P$ and $Q$ :

$$
\begin{aligned}
P+Q & =\left(\begin{array}{ccc}
6 & -2 & 2 \\
-2 & 3 & -1 \\
2 & -1 & 3
\end{array}\right)+\left(\begin{array}{lll}
0 & 0 & 0 \\
0 & 0 & 0 \\
0 & 0 & 0
\end{array}\right) \\
& =\left(\begin{array}{ccc}
6 & -2 & 2 \\
-2 & 3 & -1 \\
2 & -1 & 3
\end{array}\right) \\
& =A
\end{aligned}
$$

(iii) Let

$$
A=\left(\begin{array}{ccc}
3 & 3 & -1 \\
-2 & -2 & 1 \\
-4 & -5 & 2
\end{array}\right)
$$

Hence,

$$
A^{\prime}=\left(\begin{array}{ccc}
3 & -2 & -4 \\
3 & -2 & -5 \\
-1 & 1 & 2
\end{array}\right)
$$

Now,

$$
\begin{aligned}
\left(A+A^{\prime}\right) & =\left(\begin{array}{ccc}
3 & 3 & -1 \\
-2 & -2 & 1 \\
-4 & -5 & 2
\end{array}\right)+\left(\begin{array}{ccc}
3 & -2 & -4 \\
3 & -2 & -5 \\
-1 & 1 & 2
\end{array}\right) \\
& =\left(\begin{array}{ccc}
6 & 1 & -5 \\
1 & -4 & -4 \\
-5 & -4 & 4
\end{array}\right)
\end{aligned}
$$

Let

$$
\begin{aligned}
P & =\frac{1}{2}\left(A+A^{\prime}\right) \\
& =\frac{1}{2}\left(\begin{array}{ccc}
6 & 1 & -5 \\
1 & -4 & -4 \\
-5 & -4 & 4
\end{array}\right) \\
& =\left(\begin{array}{ccc}
3 & \frac{1}{2} & \frac{-5}{2} \\
\frac{1}{2} & -2 & -2 \\
\frac{-5}{2} & -2 & 2
\end{array}\right)
\end{aligned}
$$

Now,

$$
\begin{aligned}
P^{\prime} & =\left(\begin{array}{ccc}
3 & \frac{1}{2} & \frac{-5}{2} \\
\frac{1}{2} & -2 & -2 \\
\frac{-5}{2} & -2 & 2
\end{array}\right) \\
& =P
\end{aligned}
$$

Thus, $P=\frac{1}{2}\left(A+A^{\prime}\right)$ is a symmetric matrix.
Now,

$$
\begin{aligned}
\left(A-A^{\prime}\right) & =\left(\begin{array}{ccc}
3 & 3 & -1 \\
-2 & -2 & 1 \\
-4 & -5 & 2
\end{array}\right)-\left(\begin{array}{ccc}
3 & -2 & -4 \\
3 & -2 & -5 \\
-1 & 1 & 2
\end{array}\right) \\
& =\left(\begin{array}{ccc}
0 & 5 & 3 \\
-5 & 0 & 6 \\
-3 & -6 & 0
\end{array}\right)
\end{aligned}
$$

Let

$$
\begin{aligned}
Q & =\frac{1}{2}\left(A-A^{\prime}\right) \\
& =\frac{1}{2}\left(\begin{array}{ccc}
0 & 5 & 3 \\
-5 & 0 & 6 \\
-3 & -6 & 0
\end{array}\right) \\
& =\left(\begin{array}{ccc}
0 & \frac{5}{2} & \frac{3}{2} \\
\frac{-5}{2} & 0 & 3 \\
\frac{-3}{2} & -3 & 0
\end{array}\right)
\end{aligned}
$$

Now,

$$
\begin{aligned}
Q^{\prime} & =\left(\begin{array}{ccc}
0 & \frac{-5}{2} & \frac{-3}{2} \\
\frac{5}{2} & 0 & -3 \\
\frac{3}{2} & 3 & 0
\end{array}\right) \\
& =-Q
\end{aligned}
$$

Thus, $Q=\frac{1}{2}\left(A-A^{\prime}\right)$ is a skew symmetric matrix.
Representing $A$ as the sum of $P$ and $Q$ :

$$
\begin{aligned}
P+Q & =\left(\begin{array}{ccc}
3 & \frac{1}{2} & \frac{-5}{2} \\
\frac{1}{2} & -2 & -2 \\
\frac{-5}{2} & -2 & 2
\end{array}\right)+\left(\begin{array}{ccc}
0 & \frac{5}{2} & \frac{3}{2} \\
\frac{-5}{2} & 0 & 3 \\
\frac{-3}{2} & -3 & 0
\end{array}\right) \\
& =\left(\begin{array}{ccc}
3 & 3 & -1 \\
-2 & -2 & 1 \\
-4 & -5 & 2
\end{array}\right) \\
& =A
\end{aligned}
$$

(iv) Let $A=\left(\begin{array}{cc}1 & 5 \\ -1 & 2\end{array}\right)$
Hence,
$$
A^{\prime}=\left(\begin{array}{cc}
1 & -1 \\
5 & 2
\end{array}\right)
$$
Now,
$$
\begin{aligned}
\left(A+A^{\prime}\right) & =\left(\begin{array}{cc}
1 & 5 \\
-1 & 2
\end{array}\right)+\left(\begin{array}{cc}
1 & -1 \\
5 & 2
\end{array}\right) \\
& =\left(\begin{array}{ll}
2 & 4 \\
4 & 4
\end{array}\right)
\end{aligned}
$$
Let
$$
\begin{aligned}
P & =\frac{1}{2}\left(A+A^{\prime}\right) \\
& =\frac{1}{2}\left(\begin{array}{ll}
2 & 4 \\
4 & 4
\end{array}\right) \\
& =\left(\begin{array}{ll}
1 & 2 \\
2 & 2
\end{array}\right)
\end{aligned}
$$
Now,
$$
\begin{aligned}
P^{\prime} & =\left(\begin{array}{ll}
1 & 2 \\
2 & 2
\end{array}\right) \\
& =P
\end{aligned}
$$
Thus, $P=\frac{1}{2}\left(A+A^{\prime}\right)$ is a symmetric matrix.

Now,

$$
\begin{aligned}
\left(A-A^{\prime}\right) & =\left(\begin{array}{cc}
1 & 5 \\
-1 & 2
\end{array}\right)-\left(\begin{array}{cc}
1 & -1 \\
5 & 2
\end{array}\right) \\
& =\left(\begin{array}{cc}
0 & 6 \\
-6 & 0
\end{array}\right)
\end{aligned}
$$

Let

$$
\begin{aligned}
Q & =\frac{1}{2}\left(A-A^{\prime}\right) \\
& =\frac{1}{2}\left(\begin{array}{cc}
0 & 6 \\
-6 & 0
\end{array}\right) \\
& =\left(\begin{array}{cc}
0 & 3 \\
-3 & 0
\end{array}\right)
\end{aligned}
$$

Now,

$$
\begin{aligned}
Q^{\prime} & =\left(\begin{array}{cc}
0 & -3 \\
3 & 0
\end{array}\right) \\
& =-Q
\end{aligned}
$$

Thus, $Q=\frac{1}{2}\left(A-A^{\prime}\right)$ is a skew symmetric matrix.
Representing $A$ as the sum of $P$ and $Q$ :

$$
\begin{aligned}
P+Q & =\left(\begin{array}{ll}
1 & 2 \\
2 & 2
\end{array}\right)+\left(\begin{array}{cc}
0 & 3 \\
-3 & 0
\end{array}\right) \\
& =\left(\begin{array}{cc}
1 & 5 \\
-1 & 2
\end{array}\right) \\
& =A
\end{aligned}
$$
:::

:::

:::question{number="43" kind="exercise" id="q_3.43" topic="MCQ - nature of AB-BA for symmetric A, B"}
#### Question 43

:::prompt
If $\mathrm{A}, \mathrm{B}$ are symmetric matrices of same order, then $\mathrm{AB}-\mathrm{BA}$ is a
(A) Skew symmetric matrix
(B) Symmetric matrix
(C) Zero matrix
(D) Identity matrix
:::

:::solution{label="Solution"}
If $A$ and $B$ are symmetric matrices of the same order, then

$$
A^{\prime}=A \text { and } B^{\prime}=B
$$

Now consider,

$$
\begin{aligned}
(A B-B A)^{\prime} & =(A B)^{\prime}-(B A)^{\prime} & & {\left[\because(A-B)^{\prime}=A^{\prime}-B^{\prime}\right] } \\
& =B^{\prime} A^{\prime}-A^{\prime} B & & {\left[\because(A B)^{\prime}=B^{\prime} A^{\prime}\right] } \\
& =B A-A B & & {[\text { from }(1)] } \\
& =-(A B-B A) & &
\end{aligned}
$$

Therefore,

$$
(A B-B A)^{\prime}=-(A B-B A)
$$

Thus, $A B-B A$ is a skew symmetric matrix.
The Correct option is A.
:::

:::

:::question{number="44" kind="exercise" id="q_3.44" topic="MCQ - value of alpha given A+A'=I"}
#### Question 44

:::prompt
If $\mathrm{A}=\left[\begin{array}{cc}\cos \alpha & -\sin \alpha \\ \sin \alpha & \cos \alpha\end{array}\right]$, and $\mathrm{A}+\mathrm{A}^{\prime}=\mathrm{I}$, then the value of $\alpha$ is
(A) $\frac{\pi}{6}$
(B) $\frac{\pi}{3}$
(C) $\pi$
(D) $\frac{3 \pi}{2}$
:::

:::solution{label="Solution"}
It is given that $A=\left(\begin{array}{cc}\cos \alpha & -\sin \alpha \\ \sin \alpha & \cos \alpha\end{array}\right)$
Hence,

$$
A^{\prime}=\left(\begin{array}{cc}
\cos \alpha & \sin \alpha \\
-\sin \alpha & \cos \alpha
\end{array}\right)
$$

Now,

$$
A+A^{\prime}=I
$$

Therefore,

$$
\begin{aligned}
& \left(\begin{array}{cc}
\cos \alpha & -\sin \alpha \\
\sin \alpha & \cos \alpha
\end{array}\right)+\left(\begin{array}{cc}
\cos \alpha & \sin \alpha \\
-\sin \alpha & \cos \alpha
\end{array}\right)=\left(\begin{array}{ll}
1 & 0 \\
0 & 1
\end{array}\right) \\
& \left(\begin{array}{cc}
2 \cos \alpha & 0 \\
0 & 2 \cos \alpha
\end{array}\right)=\left(\begin{array}{ll}
1 & 0 \\
0 & 1
\end{array}\right)
\end{aligned}
$$

Comparing the corresponding elements of the two matrices, we have:

$$
\begin{aligned}
& \Rightarrow 2 \cos \alpha=1 \\
& \Rightarrow \cos \alpha=\frac{1}{2} \\
& \Rightarrow \alpha=\cos ^{-1} \frac{1}{2} \\
& \Rightarrow \alpha=\frac{\pi}{3}
\end{aligned}
$$

Thus, the correct option is B.

## EXERCISE 3.4
:::

:::

:::question{number="45" kind="exercise" id="q_3.45" topic="MCQ - condition for A and B to be inverses"}
#### Question 45

:::prompt
Matrices A and B will be inverse of each other only if
(A) $\mathrm{AB}=\mathrm{BA}(\mathrm{B}) \mathrm{AB}=\mathrm{BA}=0$
(C) $\mathrm{AB}=0, \mathrm{BA}=\mathrm{I}(\mathrm{D}) \mathrm{AB}=\mathrm{BA}=\mathrm{I}$

## Miscellaneous Examples
:::

:::solution{label="Solution"}
We know that if $A$ is a square matrix of order $m$, and if there exists another square matrix $B$ of the same order $m$, such that $A B=B A=I$, then $B$ is said to be the inverse of $A$.

In this case, it is clear that $A$ is the inverse of $B$.
Thus, matrices $A$ and $B$ will be inverses of each other only if $A B=B A=I$.
The correct option is D.

## MISCELLANEOUS EXERCISE
:::

:::

:::question{number="46" kind="exercise" id="q_3.46" topic="Skew symmetry of AB-BA for symmetric A, B"}
#### Question 46

:::prompt
If A and B are symmetric matrices, prove that $\mathrm{AB}-\mathrm{BA}$ is a skew symmetric matrix.
:::

:::solution{label="Solution"}
It is given that $A$ and $B$ are symmetric matrices.
Therefore, we have:

$$
A^{\prime}=A \text { and } B^{\prime}=B
$$

Now,

$$
\begin{aligned}
(A B-B A)^{\prime} & =(A B)^{\prime}-(B A)^{\prime} & & {\left[(A-B)^{\prime}=A^{\prime}-B^{\prime}\right] } \\
& =B^{\prime} A^{\prime}-A^{\prime} B^{\prime} & & {\left[(A B)^{\prime}=B^{\prime} A^{\prime}\right] } \\
& =B A-A B & & {[\text { Using }(1)] } \\
& =-(A B-B A) & &
\end{aligned}
$$

Hence,

$$
(A B-B A)^{\prime}=-(A B-B A)
$$

Thus, $A B-B A$ is a skew symmetric matrix.
:::

:::

:::question{number="47" kind="exercise" id="q_3.47" topic="Symmetry of B'AB"}
#### Question 47

:::prompt
Show that the matrix $\mathrm{B}^{\prime} \mathrm{AB}$ is symmetric or skew symmetric according as A is symmetric or skew symmetric.
:::

:::solution{label="Solution"}
We suppose that $A$ is a symmetric matrix, then

$$
A^{\prime}=A
$$

Consider,

$$
\begin{aligned}
\left(B^{\prime} A B\right)^{\prime} & =\left\{B^{\prime}(A B)\right\}^{\prime} & & \\
& =(A B)^{\prime}\left(B^{\prime}\right)^{\prime} & & {\left[\because(A B)^{\prime}=B^{\prime} A^{\prime}\right] } \\
& =B^{\prime} A^{\prime}(B) & & {\left[\because\left(B^{\prime}\right)^{\prime}=B\right] } \\
& =B^{\prime}\left(A^{\prime} B\right) & & \\
& =B^{\prime}(A B) & & {[\text { Using }(1)] }
\end{aligned}
$$

Therefore,

$$
\left(B^{\prime} A B\right)^{\prime}=B^{\prime} A B
$$

Thus, if $A$ is symmetric matrix, then $B^{\prime} A B$ is a symmetric matrix.
Now, we suppose that $A$ is a skew symmetric matrix, then

$$
A^{\prime}=-A
$$

Consider,

$$
\begin{aligned}
\left(B^{\prime} A B\right)^{\prime} & =\left\{B^{\prime}(A B)\right\}^{\prime} \\
& =(A B)^{\prime}\left(B^{\prime}\right)^{\prime} \\
& =\left(B^{\prime} A^{\prime}\right) B \\
& =B^{\prime}(-A) B \quad \text { [Using (2)] } \\
& =-B^{\prime} A B
\end{aligned}
$$

Therefore,

$$
\left(B^{\prime} A B\right)^{\prime}=-B^{\prime} A B
$$

Thus, if $A$ is a skew symmetric matrix, then $B^{\prime} A B$ is a skew symmetric matrix.
Hence, if $A$ is symmetric or skew symmetric matrix, then $B^{\prime} A B$ is symmetric or skew symmetric accordingly.
:::

:::

:::question{number="48" kind="exercise" id="q_3.48" topic="Solving for x, y, z given A'A=I"}
#### Question 48

:::prompt
Find the values of $x, y, z$ if the matrix $\mathrm{A}=\left[\begin{array}{ccr}0 & 2 y & z \\ x & y & -z \\ x & -y & z\end{array}\right]$ satisfy the equation $\mathrm{A}^{\prime} \mathrm{A}=\mathrm{I}$.
:::

:::solution{label="Solution"}
It is given that

$$
A=\left(\begin{array}{ccc}
0 & 2 y & z \\
x & y & -z \\
x & -y & z
\end{array}\right)
$$

Therefore,

$$
A^{\prime}=\left(\begin{array}{ccc}
0 & x & x \\
2 y & y & -y \\
z & -z & z
\end{array}\right)
$$

Now, $A^{\prime} A=I$

Hence,

$$
\begin{aligned}
& \Rightarrow\left(\begin{array}{ccc}
0 & x & x \\
2 y & y & -y \\
z & -z & z
\end{array}\right)\left(\begin{array}{ccc}
0 & 2 y & z \\
x & y & -z \\
x & -y & z
\end{array}\right)=\left(\begin{array}{ccc}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{array}\right) \\
& \Rightarrow\left(\begin{array}{ccc}
0+x^{2}+x^{2} & 0+x y-x y & 0-x z+x z \\
0+x y-x y & 4 y^{2}+y^{2}+y^{2} & 2 y z-y z-y z \\
0-x z+z x & 2 y z-y z-y z & z^{2}+z^{2}+z^{2}
\end{array}\right)=\left(\begin{array}{ccc}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{array}\right) \\
& \Rightarrow\left(\begin{array}{ccc}
2 x^{2} & 0 & 0 \\
0 & 6 y^{2} & 0 \\
0 & 0 & 3 z^{2}
\end{array}\right)=\left(\begin{array}{ccc}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{array}\right)
\end{aligned}
$$

On comparing the corresponding elements, we have:

$$
\begin{aligned}
& 2 x^{2}=1 \\
& \Rightarrow x= \pm \frac{1}{\sqrt{2}}
\end{aligned}
$$

$$
\begin{aligned}
& 6 y^{2}=1 \\
& \Rightarrow y= \pm \frac{1}{\sqrt{6}}
\end{aligned}
$$

$$
\begin{aligned}
& 3 z^{2}=1 \\
& \Rightarrow z= \pm \frac{1}{\sqrt{3}}
\end{aligned}
$$

Thus, $x= \pm \frac{1}{\sqrt{2}}, y= \pm \frac{1}{\sqrt{6}}$ and $z= \pm \frac{1}{\sqrt{3}}$
:::

:::

:::question{number="49" kind="exercise" id="q_3.49" topic="Solving a matrix product equation for x"}
#### Question 49

:::prompt
For what values of $x$ : $\left[\begin{array}{lll}1 & 2 & 1\end{array}\right]\left[\begin{array}{lll}1 & 2 & 0 \\ 2 & 0 & 1 \\ 1 & 0 & 2\end{array}\right]\left[\begin{array}{l}0 \\ 2 \\ x\end{array}\right]=\mathrm{O}$ ?
:::

:::solution{label="Solution"}
We have:

$$
\left[\begin{array}{lll}
1 & 2 & 1
\end{array}\right]\left[\begin{array}{lll}
1 & 2 & 0 \\
2 & 0 & 1 \\
1 & 0 & 2
\end{array}\right]\left[\begin{array}{l}
0 \\
2 \\
x
\end{array}\right]=0
$$

Hence,

$$
\begin{aligned}
& \Rightarrow\left[\begin{array}{lll}
1+4+1 & 2+0+0 & 0+2+2
\end{array}\right]\left[\begin{array}{l}
0 \\
2 \\
x
\end{array}\right]=0 \\
& \Rightarrow\left[\begin{array}{lll}
6 & 2 & 4
\end{array}\right]\left[\begin{array}{l}
0 \\
2 \\
x
\end{array}\right]=0 \\
& \Rightarrow[6(0)+2(2)+4(x)]=0 \\
& \Rightarrow[4+4 x]=0 \\
& \Rightarrow 4 x=-4 \\
& \Rightarrow x=-1
\end{aligned}
$$

Thus, the required value of $x=-1$.
:::

:::

:::question{number="50" kind="exercise" id="q_3.50" topic="Verifying a matrix polynomial identity"}
#### Question 50

:::prompt
If $\mathrm{A}=\left[\begin{array}{rr}3 & 1 \\ -1 & 2\end{array}\right]$, show that $\mathrm{A}^{2}-5 \mathrm{~A}+7 \mathrm{I}=0$.
:::

:::solution{label="Solution"}
It is given that $A=\left(\begin{array}{cc}3 & 1 \\ -1 & 2\end{array}\right)$
Therefore,

$$
\begin{aligned}
A^{2} & =A \cdot A \\
& =\left(\begin{array}{cc}
3 & 1 \\
-1 & 2
\end{array}\right)\left(\begin{array}{cc}
3 & 1 \\
-1 & 2
\end{array}\right) \\
& =\left(\begin{array}{cc}
3(3)+1(-1) & 3(1)+1(2) \\
-1(3)+2(-1) & -1(1)+2(2)
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
L H S & =A^{2}-5 A+7 I \\
& =\left(\begin{array}{cc}
8 & 5 \\
-5 & 3
\end{array}\right)-5\left(\begin{array}{cc}
3 & 1 \\
-1 & 2
\end{array}\right)+7\left(\begin{array}{cc}
1 & 0 \\
0 & 1
\end{array}\right) \\
& =\left(\begin{array}{cc}
8 & 5 \\
-5 & 3
\end{array}\right)-\left(\begin{array}{cc}
15 & 5 \\
-5 & 10
\end{array}\right)+\left(\begin{array}{cc}
7 & 0 \\
0 & 7
\end{array}\right) \\
& =\left(\begin{array}{cc}
-7 & 0 \\
0 & -7
\end{array}\right)+\left(\begin{array}{cc}
7 & 0 \\
0 & 7
\end{array}\right) \\
& =0 \\
& =\text { RHS }
\end{aligned}
$$

Thus, $A^{2}-5 A+7 I=0$
:::

:::

:::question{number="51" kind="exercise" id="q_3.51" topic="Solving a matrix product equation for x"}
#### Question 51

:::prompt
Find $x$, if $\left[\begin{array}{lll}x & -5 & -1\end{array}\right]\left[\begin{array}{lll}1 & 0 & 2 \\ 0 & 2 & 1 \\ 2 & 0 & 3\end{array}\right]\left[\begin{array}{l}x \\ 4 \\ 1\end{array}\right]=\mathrm{O}$
:::

:::solution{label="Solution"}
We have

$$
\left[\begin{array}{lll}
x & -5 & -1
\end{array}\right]\left[\begin{array}{lll}
1 & 0 & 2 \\
0 & 2 & 1 \\
2 & 0 & 3
\end{array}\right]\left[\begin{array}{l}
x \\
4 \\
1
\end{array}\right]=0
$$

Hence,

$$
\begin{aligned}
& \Rightarrow\left[\begin{array}{lll}
x+0-2 & 0-10+0 & 2 x-5-3
\end{array}\right]\left[\begin{array}{c}
x \\
4 \\
1
\end{array}\right]=0 \\
& \Rightarrow\left[\begin{array}{lll}
x-2 & -10 & 2 x-8
\end{array}\right]\left[\begin{array}{c}
x \\
4 \\
1
\end{array}\right]=0 \\
& \Rightarrow[x(x-2)-40+2 x-8]=0 \\
& \Rightarrow\left[x^{2}-2 x-40+2 x-8\right]=0 \\
& \Rightarrow\left[x^{2}-48\right]=0 \\
& \Rightarrow x^{2}-48=0 \\
& \Rightarrow x^{2}=48 \\
& \Rightarrow x= \pm 4 \sqrt{3}
\end{aligned}
$$

Thus, $x= \pm 4 \sqrt{3}$.
:::

:::

:::question{number="52" kind="exercise" id="q_3.52" topic="Matrix algebra - sales revenue and profit"}
#### Question 52

:::prompt
A manufacturer produces three products $x, y, z$ which he sells in two markets. Annual sales are indicated below:

| Market | Products |  |  |
| :--- | :--- | :--- | :--- |
| I | 10,000 | 2,000 | 18,000 |
| II | 6,000 | 20,000 | 8,000 |
:::

:::part{label="(a)"}
:::prompt
If unit sale prices of $x, y$ and $z$ are ₹ 2.50 , ₹ 1.50 and ₹ 1.00 , respectively, find the total revenue in each market with the help of matrix algebra.
:::

:::

:::part{label="(b)"}
:::prompt
If the unit costs of the above three commodities are ₹ 2.00 , ₹ 1.00 and 50 paise respectively. Find the gross profit.
:::

:::

:::solution{label="Solution"}
(a) The unit sale prices of $x, y$ and $z$ are ₹ 2.50 , ₹ 1.50 and ₹ 1.00 respectively.
Consequently, the total revenue in market I can be represented in the form of a matrix as:
$$
\begin{aligned}
{\left[\begin{array}{lll}
10000 & 2000 & 18000
\end{array}\right]\left[\begin{array}{l}
2.50 \\
1.50 \\
1.00
\end{array}\right] } & =10000 \times 2.50+2000 \times 1.50+18000 \times 1.00 \\
& =25000+3000+18000 \\
& =46000
\end{aligned}
$$
The total revenue in market II can be represented in the form of a matrix as:
$$
\begin{aligned}
{\left[\begin{array}{lll}
6000 & 20000 & 8000
\end{array}\right]\left[\begin{array}{l}
2.50 \\
1.50 \\
1.00
\end{array}\right] } & =6000 \times 2.50+20000 \times 1.50+8000 \times 1.00 \\
& =15000+30000+8000 \\
& =53000
\end{aligned}
$$
Thus, the total revenue in market I is ₹46000 and the total revenue in market II is ₹ 53000.
(b) The unit costs of $x, y$ and $z$ are ₹ 2.00 , ₹ 1.00 and 50 paise respectively.
Consequently, the total cost prices of all the products in market I can be represented in the form of a matrix as:

$$
\begin{aligned}
{\left[\begin{array}{lll}
10000 & 2000 & 18000
\end{array}\right]\left[\begin{array}{l}
2.00 \\
1.00 \\
0.50
\end{array}\right] } & =10000 \times 2.00+2000 \times 1.00+18000 \times 0.50 \\
& =20000+2000+9000 \\
& =31000
\end{aligned}
$$

Since the total revenue in market I is ₹ 46000 , the gross profit in this market in ₹ is

$$
46000-31000=15000
$$

The total cost prices of all the products in market II can be represented in the form of a matrix as:

$$
\begin{aligned}
{\left[\begin{array}{lll}
6000 & 20000 & 8000
\end{array}\right]\left[\begin{array}{l}
2.00 \\
1.00 \\
0.50
\end{array}\right] } & =6000 \times 2.00+20000 \times 1.00+8000 \times 0.50 \\
& =12000+20000+4000 \\
& =36000
\end{aligned}
$$

Since the total revenue in market I is ₹ 53000, the gross profit in this market in ₹ is

$$
53000-36000=17000
$$

Thus, the gross profit in market I is ₹15000 and in market II is ₹17000.
:::

:::

:::question{number="53" kind="exercise" id="q_3.53" topic="Finding a matrix X from a matrix equation"}
#### Question 53

:::prompt
Find the matrix X so that $\mathrm{X}\left[\begin{array}{ccc}1 & 2 & 3 \\ 4 & 5 & 6\end{array}\right]=\left[\begin{array}{rrr}-7 & -8 & -9 \\ 2 & 4 & 6\end{array}\right]$

Choose the correct answer in the following questions:
:::

:::solution{label="Solution"}
It is given that $X\left[\begin{array}{lll}1 & 2 & 3 \\ 4 & 5 & 6\end{array}\right]=\left[\begin{array}{ccc}-7 & -8 & -9 \\ 2 & 4 & 6\end{array}\right]$
The matrix given on the R.H.S. of the equation is a $2 \times 3$ matrix and the one given on the L.H.S. of the equation is a $2 \times 3$ matrix.

Therefore, $X$ has to be a $2 \times 2$ matrix.

Now, let

$$
X=\left[\begin{array}{ll}
a & c \\
b & d
\end{array}\right]
$$

Therefore,

$$
\begin{aligned}
& \Rightarrow\left[\begin{array}{ll}
a & c \\
b & d
\end{array}\right]\left[\begin{array}{lll}
1 & 2 & 3 \\
4 & 5 & 6
\end{array}\right]=\left[\begin{array}{ccc}
-7 & -8 & -9 \\
2 & 4 & 6
\end{array}\right] \\
& \Rightarrow\left[\begin{array}{ccc}
a+4 c & 2 a+5 c & 3 a+6 c \\
b+4 d & 2 b+5 d & 3 b+6 d
\end{array}\right]=\left|\begin{array}{ccc}
-7 & -8 & -9 \\
2 & 4 & 6
\end{array}\right|
\end{aligned}
$$

Equating the corresponding elements of the two matrices, we have:

$$
\begin{array}{lll}
a+4 c=7 & 2 a+5 c=-8 & 3 a+6 c=-9 a \\
b+4 d=2 & 2 b+5 d=4 & 3 b+6 d=6
\end{array}
$$

Now,

$$
\begin{aligned}
& a+4 c=-7 \\
& \Rightarrow a=-7-4 c
\end{aligned}
$$

Therefore,

$$
\begin{aligned}
& 2 a+5 c=-8 \\
& \Rightarrow 2(-7-4 c)+5 c=-8 \\
& \Rightarrow-14-8 c+5 c=-8 \\
& \Rightarrow-3 c=6 \\
& \Rightarrow c=-2
\end{aligned}
$$

Hence,

$$
\begin{aligned}
& \Rightarrow a=-7-4(-2) \\
& \Rightarrow a=-7+8 \\
& \Rightarrow a=1
\end{aligned}
$$

Now,

$$
\begin{aligned}
& b+4 d=2 \\
& \Rightarrow b=2-4 d
\end{aligned}
$$

Therefore,

$$
\begin{aligned}
& 2 b+5 d=4 \\
& \Rightarrow 2(2-4 d)+5 d=4 \\
& \Rightarrow 4-8 d+5 d=4 \\
& \Rightarrow-3 d=0 \\
& \Rightarrow d=0
\end{aligned}
$$

Hence,

$$
\begin{aligned}
& b=2-4 d \\
& \Rightarrow b=2
\end{aligned}
$$

Thus, $a=1, b=2, c=-2$ and $d=0$
Hence, the required matrix $X=\left[\begin{array}{cc}1 & -2 \\ 2 & 0\end{array}\right]$
:::

:::

:::question{number="54" kind="exercise" id="q_3.54" topic="MCQ - condition on alpha, beta, gamma given A^2=I"}
#### Question 54

:::prompt
If $\mathrm{A}=\begin{array}{cc}\alpha & \beta \\ \gamma & -\alpha\end{array}$ is such that $\mathrm{A}^{2}=\mathrm{I}$, then
(A) $1+\alpha^{2}+\beta \gamma=0$
(B) $1-\alpha^{2}+\beta \gamma=0$
(C) $1-\alpha^{2}-\beta \gamma=0$
(D) $1+\alpha^{2}-\beta \gamma=0$
:::

:::solution{label="Solution"}
It is given that $A=\left[\begin{array}{cc}\alpha & \beta \\ \gamma & -\alpha\end{array}\right]$

Therefore,

$$
\begin{aligned}
A^{2} & =A . A \\
& =\left(\begin{array}{cc}
\alpha & \beta \\
\gamma & -\alpha
\end{array}\right)\left(\begin{array}{cc}
\alpha & \beta \\
\gamma & -\alpha
\end{array}\right) \\
& =\left(\begin{array}{cc}
\alpha^{2}+\beta \gamma & \alpha \beta-\alpha \beta \\
\alpha \gamma-\alpha \gamma & \beta \gamma+\alpha^{2}
\end{array}\right) \\
& =\left(\begin{array}{cc}
\alpha^{2}+\beta \gamma & 0 \\
0 & \beta \gamma+\alpha^{2}
\end{array}\right)
\end{aligned}
$$

Now, $A^{2}=I$
Hence,

$$
\left(\begin{array}{cc}
\alpha^{2}+\beta \gamma & 0 \\
0 & \beta \gamma+\alpha^{2}
\end{array}\right)=\left(\begin{array}{ll}
1 & 0 \\
0 & 1
\end{array}\right)
$$

On comparing the corresponding elements, we have:

$$
\begin{aligned}
& \alpha^{2}+\beta \gamma=1 \\
& \Rightarrow \alpha^{2}+\beta \gamma-1=0 \\
& \Rightarrow 1-\alpha^{2}-\beta \gamma=0
\end{aligned}
$$

Thus, the correct option is C.
:::

:::

:::question{number="55" kind="exercise" id="q_3.55" topic="MCQ - matrix both symmetric and skew symmetric"}
#### Question 55

:::prompt
If the matrix A is both symmetric and skew symmetric, then
(A) A is a diagonal matrix
(B) A is a zero matrix
(C) A is a square matrix
(D) None of these
:::

:::solution{label="Solution"}
If the matrix $A$ is both symmetric and skew symmetric, then

$$
A^{\prime}=A \text { and } A^{\prime}=-A
$$

Hence,

$$
\begin{aligned}
& \Rightarrow A=-A \\
& \Rightarrow A+A=0 \\
& \Rightarrow 2 A=0 \\
& \Rightarrow A=0
\end{aligned}
$$

Therefore, $A$ is a zero matrix.
Thus, the correct option is B.
:::

:::

:::question{number="56" kind="exercise" id="q_3.56" topic="MCQ - simplifying (I+A)^3-7A given A^2=A"}
#### Question 56

:::prompt
If A is square matrix such that $\mathrm{A}^{2}=\mathrm{A}$, then $(\mathrm{I}+\mathrm{A})^{3}-7 \mathrm{~A}$ is equal to
(A) A
(B) $\mathrm{I}-\mathrm{A}$
(C) I
(D) 3A
:::

:::solution{label="Solution"}
It is given that $A$ is a square matrix such that $A^{2}=A$.
Now,

$$
\begin{aligned}
(I+A)^{3}-7 A & =I^{3}+A^{3}+3 I^{2} A+3 A^{2} I-7 A & & \\
& =I+A^{2} \cdot A+3 A+3 A^{2}-7 A & & \\
& =I+A \cdot A+3 A+3 A-7 A & & {\left[\because A^{2}=A\right] } \\
& =I+A^{2}-A & & \\
& =I+A-A & & {\left[\because A^{2}=A\right] } \\
& =I & &
\end{aligned}
$$

Hence,

$$
(I+A)^{3}-7 A=I
$$

Thus, the correct option is C.
:::

:::

## Additional Questions

:::question{number="EX3.OLD-1" kind="additional_exercise" id="sol_3.d.1" topic="Inverse via elementary row operations"}
#### Additional Question EX3.OLD-1

:::prompt
Using elementary transformation, Find the inverse of the matrix $\left(\begin{array}{cc}1 & -1 \\ 2 & 3\end{array}\right)$, if exists.
:::

:::solution{label="Solution"}
Let $A=\left(\begin{array}{cc}1 & -1 \\ 2 & 3\end{array}\right)$
We know that $A=I A$
Therefore,

$$
\begin{array}{ll}
\Rightarrow\left(\begin{array}{cc}
1 & -1 \\
2 & 3
\end{array}\right)=\left(\begin{array}{cc}
1 & 0 \\
0 & 1
\end{array}\right) A & \\
\Rightarrow\left(\begin{array}{cc}
1 & -1 \\
0 & 5
\end{array}\right)=\left(\begin{array}{cc}
1 & 0 \\
-2 & 1
\end{array}\right) A & \left(R_{2} \rightarrow R_{2}-2 R_{1}\right) \\
\Rightarrow\left(\begin{array}{cc}
1 & -1 \\
0 & 1
\end{array}\right)=\left(\begin{array}{cc}
1 & 0 \\
\frac{-2}{5} & \frac{1}{5}
\end{array}\right) A & \left(R_{2} \rightarrow \frac{1}{5} R_{2}\right) \\
\Rightarrow\left(\begin{array}{ll}
1 & 0 \\
0 & 1
\end{array}\right)=\left(\begin{array}{cc}
\frac{3}{5} & \frac{1}{5} \\
\frac{-2}{5} & \frac{1}{5}
\end{array}\right) A & \left(R_{1} \rightarrow R_{1}+R_{2}\right) \\
\Rightarrow A^{-1}=\left(\begin{array}{cc}
\frac{3}{5} & \frac{1}{5} \\
\frac{-2}{5} & \frac{1}{5}
\end{array}\right)
\end{array}
$$
:::

:::

:::question{number="EX3.OLD-2" kind="additional_exercise" id="sol_3.d.2" topic="Inverse via elementary row operations"}
#### Additional Question EX3.OLD-2

:::prompt
Using elementary transformation, Find the inverse of the matrix $\left(\begin{array}{ll}2 & 1 \\ 1 & 1\end{array}\right)$, if exists.
:::

:::solution{label="Solution"}
Let $A=\left(\begin{array}{ll}2 & 1 \\ 1 & 1\end{array}\right)$
We know that $A=I A$
Therefore,

$$
\begin{aligned}
& \Rightarrow\left(\begin{array}{ll}
2 & 1 \\
1 & 1
\end{array}\right)=\left(\begin{array}{ll}
1 & 0 \\
0 & 1
\end{array}\right) A \\
& \Rightarrow\left(\begin{array}{ll}
1 & 0 \\
1 & 1
\end{array}\right)=\left(\begin{array}{cc}
1 & -1 \\
0 & 1
\end{array}\right) A \\
& \Rightarrow\left(\begin{array}{ll}
1 & 0 \\
0 & 1
\end{array}\right)=\left(\begin{array}{cc}
1 & -1 \\
-1 & 2
\end{array}\right) A \\
& \Rightarrow A^{-1}=\left(\begin{array}{cc}
1 & -1 \\
-1 & 2
\end{array}\right)
\end{aligned} \quad\left(R_{1} \rightarrow R_{1}-R_{2}\right)
$$
:::

:::

:::question{number="EX3.OLD-3" kind="additional_exercise" id="sol_3.d.3" topic="Inverse via elementary row operations"}
#### Additional Question EX3.OLD-3

:::prompt
Using elementary transformation, Find the inverse of the matrix $\left(\begin{array}{ll}1 & 3 \\ 2 & 7\end{array}\right)$, if exists.
:::

:::solution{label="Solution"}
Let $A=\left(\begin{array}{ll}1 & 3 \\ 2 & 7\end{array}\right)$
We know that $A=I A$
Therefore,

$$
\begin{array}{ll}
\Rightarrow\left(\begin{array}{ll}
1 & 3 \\
2 & 7
\end{array}\right)=\left(\begin{array}{cc}
1 & 0 \\
0 & 1
\end{array}\right) A & \\
\Rightarrow\left(\begin{array}{ll}
1 & 3 \\
0 & 1
\end{array}\right)=\left(\begin{array}{cc}
1 & 0 \\
-2 & 1
\end{array}\right) A & \left(R_{2} \rightarrow R_{2}-2 R_{1}\right) \\
\Rightarrow\left(\begin{array}{ll}
1 & 0 \\
0 & 1
\end{array}\right)=\left(\begin{array}{cc}
7 & -3 \\
-2 & 1
\end{array}\right) A & \left(R_{1} \rightarrow R_{1}-3 R_{2}\right) \\
\Rightarrow A^{-1}=\left(\begin{array}{cc}
7 & -3 \\
-2 & 1
\end{array}\right)
\end{array}
$$
:::

:::

:::question{number="EX3.OLD-4" kind="additional_exercise" id="sol_3.d.4" topic="Inverse via elementary row operations"}
#### Additional Question EX3.OLD-4

:::prompt
Using elementary transformation, Find the inverse of the matrix $\left(\begin{array}{ll}2 & 3 \\ 5 & 7\end{array}\right)$, if exists.
:::

:::solution{label="Solution"}
Let $A=\left(\begin{array}{ll}2 & 3 \\ 5 & 7\end{array}\right)$
We know that $A=I A$

Therefore,

$$
\begin{aligned}
& \Rightarrow\left(\begin{array}{ll}
2 & 3 \\
5 & 7
\end{array}\right)=\left(\begin{array}{cc}
1 & 0 \\
0 & 1
\end{array}\right) A \\
& \Rightarrow\left(\begin{array}{cc}
1 & \frac{3}{2} \\
5 & 7
\end{array}\right)=\left(\begin{array}{cc}
\frac{1}{2} & 0 \\
0 & 1
\end{array}\right) A \\
& \Rightarrow\left(\begin{array}{cc}
1 & \frac{3}{2} \\
0 & \frac{-1}{2}
\end{array}\right)=\left(\begin{array}{cc}
\frac{1}{2} & 0 \\
\frac{-5}{2} & 1
\end{array}\right) A \\
& \Rightarrow\left(\begin{array}{cc}
1 & 0 \\
0 & \frac{-1}{2}
\end{array}\right)=\left(\begin{array}{cc}
-7 & 3 \\
\frac{-5}{2} & 1
\end{array}\right) A \\
& \Rightarrow\left(\begin{array}{cc}
1 & 0 \\
0 & 1
\end{array}\right)=\left(\begin{array}{cc}
-7 & 3 \\
5 & -2
\end{array}\right) A \\
& \Rightarrow A^{-1}=\left(\begin{array}{cc}
-7 & 3 \\
5 & -2
\end{array}\right)
\end{aligned}
$$
:::

:::

:::question{number="EX3.OLD-5" kind="additional_exercise" id="sol_3.d.5" topic="Inverse via elementary row operations"}
#### Additional Question EX3.OLD-5

:::prompt
Using elementary transformation, Find the inverse of the matrix $\left(\begin{array}{ll}2 & 1 \\ 7 & 4\end{array}\right)$, if exists.
:::

:::solution{label="Solution"}
Let $A=\left(\begin{array}{ll}2 & 1 \\ 7 & 4\end{array}\right)$
We know that $A=I A$
Therefore,

$$
\begin{aligned}
& \Rightarrow\left(\begin{array}{ll}
2 & 1 \\
7 & 4
\end{array}\right)=\left(\begin{array}{ll}
1 & 0 \\
0 & 1
\end{array}\right) A \\
& \Rightarrow\left(\begin{array}{ll}
1 & \frac{1}{2} \\
7 & 4
\end{array}\right)=\left(\begin{array}{cc}
\frac{1}{2} & 0 \\
0 & 1
\end{array}\right) A \\
& \Rightarrow\left(\begin{array}{ll}
1 & \frac{1}{2} \\
0 & \frac{1}{2}
\end{array}\right)=\left(\begin{array}{cc}
\frac{1}{2} & 0 \\
\frac{-7}{2} & 1
\end{array}\right) A \\
& \Rightarrow\left(\begin{array}{ll}
1 & 0 \\
0 & \frac{1}{2}
\end{array}\right)=\left(\begin{array}{cc}
4 & -1 \\
\frac{-7}{2} & 1
\end{array}\right) A \\
& \Rightarrow\left(\begin{array}{ll}
1 & 0 \\
0 & 1
\end{array}\right)=\left(\begin{array}{cc}
4 & -1 \\
-7 & 2
\end{array}\right) A \\
& \Rightarrow A^{-1}=\left(\begin{array}{cc}
4 & -1 \\
-7 & 2
\end{array}\right)
\end{aligned} \quad\left(R_{2} \rightarrow R_{2}-7 R_{1}\right) .{\left(R_{2} \rightarrow 2 R_{1}\right)}
$$
:::

:::

:::question{number="EX3.OLD-6" kind="additional_exercise" id="sol_3.d.6" topic="Inverse via elementary row operations"}
#### Additional Question EX3.OLD-6

:::prompt
Using elementary transformation, Find the inverse of the matrix $\left(\begin{array}{ll}2 & 5 \\ 1 & 3\end{array}\right)$, if exists.
:::

:::solution{label="Solution"}
Let $A=\left(\begin{array}{ll}2 & 5 \\ 1 & 3\end{array}\right)$
We know that $A=I A$
Therefore,

$$
\left.\left.\begin{array}{l}
\Rightarrow\left(\begin{array}{ll}
2 & 5 \\
1 & 3
\end{array}\right)=\left(\begin{array}{ll}
1 & 0 \\
0 & 1
\end{array}\right) A \\
\Rightarrow\left(\begin{array}{ll}
1 & \frac{5}{2} \\
1 & 3
\end{array}\right)=\left(\begin{array}{cc}
\frac{1}{2} & 0 \\
0 & 1
\end{array}\right) A \\
\Rightarrow\left(\begin{array}{ll}
1 & \frac{5}{2} \\
0 & \frac{1}{2}
\end{array}\right)=\left(\begin{array}{cc}
\frac{1}{2} & 0 \\
\frac{-1}{2} & 1
\end{array}\right) A \\
\Rightarrow\left(\begin{array}{cc}
1 & 0 \\
0 & \frac{1}{2}
\end{array}\right)=\left(\begin{array}{cc}
3 & -5 \\
\frac{-1}{2} & 1
\end{array}\right) A \\
\Rightarrow\left(\begin{array}{cc}
1 & 0 \\
0 & 1
\end{array}\right)=\left(\begin{array}{cc}
3 & -5 \\
-1 & 2
\end{array}\right) A \\
\Rightarrow A^{-1}=\left(\begin{array}{cc}
3 & -5 \\
-1 & 2
\end{array}\right)
\end{array} \quad\left(R_{2} \rightarrow R_{2}-R_{1}\right) R_{1}-5 R_{2}\right) . \text { (R } R_{2}\right) .
$$
:::

:::

:::question{number="EX3.OLD-7" kind="additional_exercise" id="sol_3.d.7" topic="Inverse via elementary row operations"}
#### Additional Question EX3.OLD-7

:::prompt
Using elementary transformation, Find the inverse of the matrix $\left(\begin{array}{ll}3 & 1 \\ 5 & 2\end{array}\right)$, if exists.
:::

:::solution{label="Solution"}
Let $A=\left(\begin{array}{ll}3 & 1 \\ 5 & 2\end{array}\right)$
We know that $A=I A$

Therefore,

$$
\begin{array}{ll}
\Rightarrow\left(\begin{array}{ll}
3 & 1 \\
5 & 2
\end{array}\right)=A\left(\begin{array}{ll}
1 & 0 \\
0 & 1
\end{array}\right) & \\
\Rightarrow\left(\begin{array}{ll}
1 & 1 \\
1 & 2
\end{array}\right)=A\left(\begin{array}{cc}
1 & 0 \\
-2 & 1
\end{array}\right) & \left(C_{1} \rightarrow C_{1}-2 C_{2}\right) \\
\Rightarrow\left(\begin{array}{ll}
1 & 0 \\
1 & 1
\end{array}\right)=A\left(\begin{array}{cc}
1 & -1 \\
-2 & 3
\end{array}\right) & \left(C_{2} \rightarrow C_{2}-C_{1}\right) \\
\Rightarrow\left(\begin{array}{ll}
1 & 0 \\
0 & 1
\end{array}\right)=A\left(\begin{array}{cc}
2 & -1 \\
-5 & 3
\end{array}\right) & \left(C_{1} \rightarrow C_{1}-C_{2}\right) \\
\Rightarrow A^{-1}=\left(\begin{array}{cc}
2 & -1 \\
-5 & 3
\end{array}\right) &
\end{array}
$$
:::

:::

:::question{number="EX3.OLD-8" kind="additional_exercise" id="sol_3.d.8" topic="Inverse via elementary row operations"}
#### Additional Question EX3.OLD-8

:::prompt
Using elementary transformation, Find the inverse of the matrix $\left(\begin{array}{ll}4 & 5 \\ 3 & 4\end{array}\right)$, if exists.
:::

:::solution{label="Solution"}
Let $A=\left(\begin{array}{ll}4 & 5 \\ 3 & 4\end{array}\right)$
We know that $A=I A$
Therefore,

$$
\begin{array}{ll}
\Rightarrow\left(\begin{array}{ll}
4 & 5 \\
3 & 4
\end{array}\right)=\left(\begin{array}{ll}
1 & 0 \\
0 & 1
\end{array}\right) A & \\
\Rightarrow\left(\begin{array}{ll}
1 & 1 \\
3 & 4
\end{array}\right)=\left(\begin{array}{cc}
1 & -1 \\
0 & 1
\end{array}\right) A & \left(R_{1} \rightarrow R_{1}-R_{2}\right) \\
\Rightarrow\left(\begin{array}{ll}
1 & 1 \\
0 & 1
\end{array}\right)=\left(\begin{array}{cc}
1 & -1 \\
-3 & 4
\end{array}\right) A & \left(R_{2} \rightarrow R_{2}-3 R_{1}\right) \\
\Rightarrow\left(\begin{array}{cc}
1 & 0 \\
0 & 1
\end{array}\right)=\left(\begin{array}{cc}
4 & -5 \\
-3 & 4
\end{array}\right) A & \left(R_{1} \rightarrow R_{1}-R_{2}\right) \\
\Rightarrow A^{-1}=\left(\begin{array}{cc}
4 & -5 \\
-3 & 4
\end{array}\right) &
\end{array}
$$
:::

:::

:::question{number="EX3.OLD-9" kind="additional_exercise" id="sol_3.d.9" topic="Inverse via elementary row operations"}
#### Additional Question EX3.OLD-9

:::prompt
Using elementary transformation, Find the inverse of the matrix $\left(\begin{array}{ll}3 & 10 \\ 2 & 7\end{array}\right)$, if exists.
:::

:::solution{label="Solution"}
Let $A=\left(\begin{array}{lc}3 & 10 \\ 2 & 7\end{array}\right)$
We know that $A=I A$
Therefore,

$$
\begin{array}{ll}
\Rightarrow\left(\begin{array}{ll}
3 & 10 \\
2 & 7
\end{array}\right)=\left(\begin{array}{ll}
1 & 0 \\
0 & 1
\end{array}\right) A & \\
\Rightarrow\left(\begin{array}{ll}
1 & 3 \\
2 & 7
\end{array}\right)=\left(\begin{array}{cc}
1 & -1 \\
0 & 1
\end{array}\right) A & \left(R_{1} \rightarrow R_{1}-R_{2}\right) \\
\Rightarrow\left(\begin{array}{ll}
1 & 3 \\
0 & 1
\end{array}\right)=\left(\begin{array}{cc}
1 & -1 \\
-2 & 3
\end{array}\right) A & \left(R_{2} \rightarrow R_{2}-2 R_{1}\right) \\
\Rightarrow\left(\begin{array}{ll}
1 & 0 \\
0 & 1
\end{array}\right)=\left(\begin{array}{cc}
7 & -10 \\
-2 & 3
\end{array}\right) A & \left(R_{1} \rightarrow R_{1}-3 R_{2}\right) \\
\Rightarrow A^{-1}=\left(\begin{array}{cc}
7 & -10 \\
-2 & 3
\end{array}\right) &
\end{array}
$$
:::

:::

:::question{number="EX3.OLD-10" kind="additional_exercise" id="sol_3.d.10" topic="Inverse via elementary row operations"}
#### Additional Question EX3.OLD-10

:::prompt
Using elementary transformation, Find the inverse of the matrix $\left(\begin{array}{cc}3 & -1 \\ -4 & 2\end{array}\right)$, if exists.
:::

:::solution{label="Solution"}
Let $A=\left(\begin{array}{cc}3 & -1 \\ -4 & 2\end{array}\right)$
We know that $A=I A$
Therefore,

$$
\begin{array}{ll}
\Rightarrow\left(\begin{array}{cc}
3 & -1 \\
-4 & 2
\end{array}\right)=A\left(\begin{array}{ll}
1 & 0 \\
0 & 1
\end{array}\right) & \\
\Rightarrow\left(\begin{array}{cc}
1 & -1 \\
0 & 2
\end{array}\right)=A\left(\begin{array}{ll}
1 & 0 \\
2 & 1
\end{array}\right) & \left(C_{1} \rightarrow C_{1}+2 C_{2}\right) \\
\Rightarrow\left(\begin{array}{cc}
1 & 0 \\
0 & 2
\end{array}\right)=A\left(\begin{array}{ll}
1 & 1 \\
2 & 3
\end{array}\right) & \left(C_{2} \rightarrow C_{2}+C_{1}\right) \\
\Rightarrow\left(\begin{array}{ll}
1 & 0 \\
0 & 1
\end{array}\right)=A\left(\begin{array}{ll}
1 & \frac{1}{2} \\
2 & \frac{3}{2}
\end{array}\right) & \left(C_{2} \rightarrow \frac{1}{2} C_{2}\right) \\
\Rightarrow A^{-1}=\left(\begin{array}{ll}
1 & \frac{1}{2} \\
2 & \frac{3}{2}
\end{array}\right) &
\end{array}
$$
:::

:::

:::question{number="EX3.OLD-11" kind="additional_exercise" id="sol_3.d.11" topic="Inverse via elementary row operations"}
#### Additional Question EX3.OLD-11

:::prompt
Using elementary transformation, Find the inverse of the matrix $\left(\begin{array}{ll}2 & -6 \\ 1 & -2\end{array}\right)$, if exists.
:::

:::solution{label="Solution"}
Let $A=\left(\begin{array}{ll}2 & -6 \\ 1 & -2\end{array}\right)$
We know that $A=I A$
Therefore,

$$
\begin{array}{ll}
\Rightarrow\left(\begin{array}{cc}
2 & -6 \\
1 & -2
\end{array}\right)=A\left(\begin{array}{ll}
1 & 0 \\
0 & 1
\end{array}\right) & \\
\Rightarrow\left(\begin{array}{ll}
2 & 0 \\
1 & 1
\end{array}\right)=A\left(\begin{array}{ll}
1 & 3 \\
0 & 1
\end{array}\right) & \left(C_{2} \rightarrow C_{2}+3 C_{1}\right) \\
\Rightarrow\left(\begin{array}{ll}
2 & 0 \\
0 & 1
\end{array}\right)=A\left(\begin{array}{ll}
-2 & 3 \\
-1 & 1
\end{array}\right) & \left(C_{1} \rightarrow C_{1}-C_{2}\right) \\
\Rightarrow\left(\begin{array}{ll}
1 & 0 \\
0 & 1
\end{array}\right)=A\left(\begin{array}{rr}
-1 & 3 \\
-\frac{1}{2} & 1
\end{array}\right) & \left(C_{1} \rightarrow \frac{1}{2} C_{1}\right) \\
\Rightarrow A^{-1}=\left(\begin{array}{rr}
-1 & 3 \\
-\frac{1}{2} & 1
\end{array}\right) &
\end{array}
$$
:::

:::

:::question{number="EX3.OLD-12" kind="additional_exercise" id="sol_3.d.12" topic="Inverse via elementary row operations"}
#### Additional Question EX3.OLD-12

:::prompt
Using elementary transformation, Find the inverse of the matrix $\left(\begin{array}{cc}6 & -3 \\ -2 & 1\end{array}\right)$, if exists.
:::

:::solution{label="Solution"}
Let

$$
A=\left(\begin{array}{cc}
6 & -3 \\
-2 & 1
\end{array}\right)
$$

We know that $A=I A$
Therefore,

$$
\begin{array}{ll}
\Rightarrow\left(\begin{array}{cc}
6 & -3 \\
-2 & 1
\end{array}\right)=\left(\begin{array}{cc}
1 & 0 \\
0 & 1
\end{array}\right) A & \\
\Rightarrow\left(\begin{array}{cc}
1 & \frac{-1}{2} \\
-2 & 1
\end{array}\right)=\left(\begin{array}{cc}
\frac{1}{6} & 0 \\
0 & 1
\end{array}\right) A & \left(R_{1} \rightarrow \frac{1}{6} R_{1}\right) \\
\Rightarrow\left(\begin{array}{cc}
1 & \frac{-1}{2} \\
0 & 0
\end{array}\right)=\left(\begin{array}{cc}
\frac{1}{6} & 0 \\
\frac{1}{3} & 1
\end{array}\right) A & \left(R_{2} \rightarrow R_{2}+2 R_{1}\right)
\end{array}
$$

In the above equation, we can see all the zeros in the second row of the matrix on the L.H.S.
Thus, $A^{-1}$ does not exist.
:::

:::

:::question{number="EX3.OLD-13" kind="additional_exercise" id="sol_3.d.13" topic="Inverse via elementary row operations"}
#### Additional Question EX3.OLD-13

:::prompt
Using elementary transformation, Find the inverse of the matrix $\left(\begin{array}{cc}2 & -3 \\ -1 & 2\end{array}\right)$, if exists.
:::

:::solution{label="Solution"}
Let $A=\left(\begin{array}{cc}2 & -3 \\ -1 & 2\end{array}\right)$
We know that $A=I A$
Therefore,

$$
\begin{array}{ll}
\Rightarrow\left(\begin{array}{cc}
2 & -3 \\
-1 & 2
\end{array}\right)=\left(\begin{array}{ll}
1 & 0 \\
0 & 1
\end{array}\right) A & \\
\Rightarrow\left(\begin{array}{cc}
1 & -1 \\
-1 & 2
\end{array}\right)=\left(\begin{array}{ll}
1 & 1 \\
0 & 1
\end{array}\right) A & \left(R_{1} \rightarrow R_{1}+R_{2}\right) \\
\Rightarrow\left(\begin{array}{cc}
1 & -1 \\
0 & 1
\end{array}\right)=\left(\begin{array}{ll}
1 & 1 \\
1 & 2
\end{array}\right) A & \left(R_{2} \rightarrow R_{2}+R_{1}\right) \\
\Rightarrow\left(\begin{array}{cc}
1 & 0 \\
0 & 1
\end{array}\right)=\left(\begin{array}{ll}
2 & 3 \\
1 & 2
\end{array}\right) A & \left(R_{1} \rightarrow R_{1}+R_{2}\right) \\
\Rightarrow A^{-1}=\left(\begin{array}{ll}
2 & 3 \\
1 & 2
\end{array}\right) &
\end{array}
$$
:::

:::

:::question{number="EX3.OLD-14" kind="additional_exercise" id="sol_3.d.14" topic="Inverse via elementary row operations"}
#### Additional Question EX3.OLD-14

:::prompt
Using elementary transformation, Find the inverse of the matrix $\left(\begin{array}{ll}2 & 1 \\ 4 & 2\end{array}\right)$, if exists.
:::

:::solution{label="Solution"}
Let $A=\left(\begin{array}{ll}2 & 1 \\ 4 & 2\end{array}\right)$
We know that $A=I A$
Therefore,

$$
\begin{aligned}
& \Rightarrow\left(\begin{array}{ll}
2 & 1 \\
4 & 2
\end{array}\right)=\left(\begin{array}{ll}
1 & 0 \\
0 & 1
\end{array}\right) A \\
& \Rightarrow\left(\begin{array}{ll}
0 & 0 \\
4 & 2
\end{array}\right)=\left(\begin{array}{ll}
1 & \frac{-1}{2} \\
0 & 1
\end{array}\right) A \quad\left(R_{1} \rightarrow R_{1}-\frac{1}{2} R_{2}\right)
\end{aligned}
$$

In the above equation, we can see all the zeros in the first row of the matrix on the L.H.S.
Thus, $A^{-1}$ does not exist.
:::

:::

:::question{number="EX3.OLD-15" kind="additional_exercise" id="sol_3.d.15" topic="Inverse via elementary row operations"}
#### Additional Question EX3.OLD-15

:::prompt
Using elementary transformation, Find the inverse of the matrix $\left(\begin{array}{ccc}2 & -3 & 3 \\ 2 & 2 & 3 \\ 3 & -2 & 2\end{array}\right)$, if exists.
:::

:::solution{label="Solution"}
Let

$$
A=\left(\begin{array}{ccc}
2 & -3 & 3 \\
2 & 2 & 3 \\
3 & -2 & 2
\end{array}\right)
$$

We know that $A=I A$
Therefore,

$$
\begin{array}{ll}
\Rightarrow\left(\begin{array}{ccc}
2 & -3 & 3 \\
2 & 2 & 3 \\
3 & -2 & 2
\end{array}\right)=\left(\begin{array}{ccc}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{array}\right) A & \\
\Rightarrow\left(\begin{array}{ccc}
2 & -3 & 3 \\
0 & 5 & 0 \\
3 & -2 & 2
\end{array}\right)=\left(\begin{array}{ccc}
1 & 0 & 0 \\
-1 & 1 & 0 \\
0 & 0 & 1
\end{array}\right) A & \left(R_{2} \rightarrow R_{2}-R_{1}\right) \\
\Rightarrow\left(\begin{array}{ccc}
2 & -3 & 3 \\
0 & 1 & 0 \\
3 & -2 & 2
\end{array}\right)=\left(\begin{array}{ccc}
1 & 0 & 0 \\
\frac{-1}{5} & \frac{1}{5} & 0 \\
0 & 0 & 1
\end{array}\right) A & \left(R_{2} \rightarrow \frac{1}{5} R_{2}\right) \\
\Rightarrow\left(\begin{array}{ccc}
-1 & -1 & 1 \\
0 & 1 & 0 \\
3 & -2 & 2
\end{array}\right)=\left(\begin{array}{ccc}
1 & 0 & -1 \\
\frac{-1}{5} & \frac{1}{5} & 0 \\
0 & 0 & 1
\end{array}\right) A & \left(R_{1} \rightarrow R_{1}-R_{3}\right) \\
\Rightarrow\left(\begin{array}{ccc}
-1 & 0 & 1 \\
0 & 1 & 0 \\
3 & 0 & 2
\end{array}\right)=\left(\begin{array}{ccc}
\frac{4}{5} & \frac{1}{5} & -1 \\
\frac{-1}{5} & \frac{1}{5} & 0 \\
\frac{-2}{5} & \frac{2}{5} & 1
\end{array}\right) A & \left(R_{1} \rightarrow R_{1}+R_{2} \text { and } R_{3} \rightarrow R_{3}+2 R_{2}\right) \\
\Rightarrow\left(\begin{array}{ccc}
-1 & 0 & 1 \\
0 & 1 & 0 \\
0 & 0 & 5
\end{array}\right)=\left(\begin{array}{ccc}
\frac{4}{5} & \frac{1}{5} & -1 \\
\frac{-1}{5} & \frac{1}{5} & 0 \\
2 & 1 & -2
\end{array}\right) A & \left(R_{3} \rightarrow R_{3}+3 R_{1}\right)
\end{array}
$$

$$
\begin{array}{ll}
\Rightarrow\left(\begin{array}{ccc}
-1 & 0 & 1 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{array}\right)=\left(\begin{array}{ccc}
\frac{4}{5} & \frac{1}{5} & -1 \\
\frac{-1}{5} & \frac{1}{5} & 0 \\
\frac{2}{5} & \frac{1}{5} & \frac{-2}{5}
\end{array}\right) A & \left(R_{3} \rightarrow \frac{1}{5} R_{3}\right) \\
\Rightarrow\left(\begin{array}{ccc}
-1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{array}\right)=\left(\begin{array}{ccc}
\frac{2}{5} & 0 & \frac{-3}{5} \\
\frac{-1}{5} & \frac{1}{5} & 0 \\
\frac{2}{5} & \frac{1}{5} & \frac{-2}{5}
\end{array}\right) A & \left(R_{1} \rightarrow R_{1}-R_{3}\right) \\
\Rightarrow\left(\begin{array}{lll}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{array}\right)=\left(\begin{array}{ccc}
\frac{-2}{5} & 0 & \frac{3}{5} \\
\frac{-1}{5} & \frac{1}{5} & 0 \\
\frac{2}{5} & \frac{1}{5} & \frac{-2}{5}
\end{array}\right) A & \left(R_{1} \rightarrow(-1) R_{1}\right) \\
\Rightarrow A^{-1}=\left(\begin{array}{ccc}
\frac{-2}{5} & 0 & \frac{3}{5} \\
\frac{-1}{5} & \frac{1}{5} & 0 \\
\frac{2}{5} & \frac{1}{5} & \frac{-2}{5}
\end{array}\right)
\end{array}
$$
:::

:::

:::question{number="EX3.OLD-16" kind="additional_exercise" id="sol_3.d.16" topic="Inverse via elementary row operations"}
#### Additional Question EX3.OLD-16

:::prompt
Using elementary transformation, Find the inverse of the matrix $\left(\begin{array}{ccc}1 & 3 & -2 \\ -3 & 0 & -5 \\ 2 & 5 & 0\end{array}\right)$, if exists.
:::

:::solution{label="Solution"}
Let

$$
A=\left(\begin{array}{ccc}
1 & 3 & -2 \\
-3 & 0 & -5 \\
2 & 5 & 0
\end{array}\right)
$$

We know that $A=I A$
Therefore,

$$
\begin{aligned}
& \Rightarrow\left(\begin{array}{ccc}
1 & 3 & -2 \\
-3 & 0 & -5 \\
2 & 5 & 0
\end{array}\right)=\left(\begin{array}{ccc}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{array}\right) A \\
& \Rightarrow\left(\begin{array}{ccc}
1 & 3 & -2 \\
0 & 9 & -11 \\
0 & -1 & 4
\end{array}\right)=\left(\begin{array}{ccc}
1 & 0 & 0 \\
3 & 1 & 0 \\
-2 & 0 & 1
\end{array}\right) A \\
& \Rightarrow\left(\begin{array}{ccc}
1 & 0 & 10 \\
0 & 1 & 21 \\
0 & -1 & 4
\end{array}\right)=\left(\begin{array}{ccc}
-5 & 0 & 3 \\
-13 & 1 & 8 \\
-2 & 0 & 1
\end{array}\right) A \\
& \Rightarrow\left(\begin{array}{ccc}
1 & 0 & 10 \\
0 & 1 & 21 \\
0 & 0 & 25
\end{array}\right)=\left(\begin{array}{ccc}
-5 & 0 & 3 \\
-13 & 1 & 8 \\
-15 & 1 & 9
\end{array}\right) A \\
& \left.\Rightarrow\left(\begin{array}{ccc}
1 & 0 & 10 \\
0 & 1 & 21 \\
0 & 0 & 1
\end{array}\right)=\left(\begin{array}{ccc}
-5 & 0 & 3 \\
-13 & 1 & 8 \\
\frac{-3}{5} & \frac{1}{25} & \frac{9}{25}
\end{array}\right) A R_{2}+3 R_{1} \text { and } R_{3} \rightarrow R_{3}-2 R_{1}\right) \\
& \Rightarrow\left(\begin{array}{ccc}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{array}\right)=\left(\begin{array}{ccc}
1 & \frac{-2}{5} & \frac{-3}{5} \\
\frac{-2}{5} & \frac{4}{25} & \frac{11}{25} \\
\frac{-3}{5} & \frac{1}{25} & \frac{9}{25}
\end{array}\right) A \\
& \Rightarrow A^{-1}=\left(R_{3} \rightarrow R_{3}+3 R_{3} \text { and } R_{2} \rightarrow R_{2}+8 R_{3}\right) \\
& \frac{-2}{5} \frac{\frac{-2}{5}}{\frac{-3}{25}} \frac{\frac{11}{25}}{\frac{-3}{5}} \frac{1}{25} \frac{\frac{9}{25}}{25}
\end{aligned}
$$
:::

:::

:::question{number="EX3.OLD-17" kind="additional_exercise" id="sol_3.d.17" topic="Inverse via elementary row operations"}
#### Additional Question EX3.OLD-17

:::prompt
Using elementary transformation, Find the inverse of the matrix $\left(\begin{array}{ccc}2 & 0 & -1 \\ 5 & 1 & 0 \\ 0 & 1 & 3\end{array}\right)$, if exists.
:::

:::solution{label="Solution"}
Let

$$
A=\left(\begin{array}{ccc}
2 & 0 & -1 \\
5 & 1 & 0 \\
0 & 1 & 3
\end{array}\right)
$$

We know that $A=I A$

Therefore,

$$
\begin{aligned}
& \Rightarrow\left(\begin{array}{ccc}
2 & 0 & -1 \\
5 & 1 & 0 \\
0 & 1 & 3
\end{array}\right)=\left(\begin{array}{ccc}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{array}\right) A \\
& \Rightarrow\left(\begin{array}{lll}
1 & 0 & \frac{-1}{2} \\
5 & 1 & 0 \\
0 & 1 & 3
\end{array}\right)=\left(\begin{array}{ccc}
\frac{1}{2} & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{array}\right) A \\
& \Rightarrow\left(\begin{array}{lll}
1 & 0 & \frac{-1}{2} \\
0 & 1 & \frac{5}{2} \\
0 & 1 & 3
\end{array}\right)=\left(\begin{array}{ccc}
\frac{1}{2} & 0 & 0 \\
\frac{-5}{2} & 1 & 0 \\
0 & 0 & 1
\end{array}\right) A \\
& \Rightarrow\left(\begin{array}{ccc}
1 & 0 & \frac{-1}{2} \\
0 & 1 & \frac{5}{2} \\
0 & 0 & \frac{1}{2}
\end{array}\right)=\left(\begin{array}{ccc}
\frac{1}{2} & 0 & 0 \\
\frac{-5}{2} & 1 & 0 \\
\frac{5}{2} & -1 & 1
\end{array}\right) A \\
& \Rightarrow\left(\begin{array}{ccc}
1 & 0 & \frac{-1}{2} \\
0 & 1 & \frac{5}{2} \\
0 & 0 & 1
\end{array}\right)=\left(\begin{array}{ccc}
\frac{1}{2} & 0 & 0 \\
\frac{-5}{2} & 1 & 0 \\
5 & -2 & 2
\end{array}\right) A \\
& \Rightarrow\left(\begin{array}{ccc}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{array}\right)=\left(\begin{array}{ccc}
3 & -1 & 1 \\
-15 & 6 & -5 \\
5 & -2 & 2
\end{array}\right) A
\end{aligned} \quad\left(R_{3} \rightarrow R_{3}-R_{2}\right){ }^{\left(R_{1} \rightarrow R_{1} \rightarrow R_{1}+\frac{1}{2} R_{3} \text { and } R_{2} \rightarrow R_{2}-\frac{5}{2} R_{3}\right)} . \quad\left(R_{1}\right) A^{-1}=\left(\begin{array}{cc}
3 & 1 \\
-15 & -5 \\
5 & -2
\end{array}\right) . \quad\left(R_{1}\right) A
$$
:::

:::

:::question{number="MISC-1" kind="additional_exercise" id="sol_3.misc.1" topic="Matrix power by induction"}
#### Additional Question MISC-1

:::prompt
Let $A=\left(\begin{array}{ll}0 & 1 \\ 0 & 0\end{array}\right)$, show that $(a I+b A)^{n}=a^{n} I+n a^{n-1} b A$, where $I$ is the identity matrix of order 2 and $n \in N$.
:::

:::solution{label="Solution"}
It is given that $A=\left(\begin{array}{ll}0 & 1 \\ 0 & 0\end{array}\right)$
We shall prove the result by using the principle of mathematical induction.
For $n=1$, we have:

$$
P(1):(a I+b A)=a I+b a^{0} A=a I+b A
$$

Therefore, the result is true for $n=1$.
Let the result be true for $n=k$

That is, $P(k):(a I+b A)^{k}=a^{k} I+k a^{k-1} b A$
Now, we have to prove that the result is true for $n=k+1$.
Consider,

$$
\begin{aligned}
(a I+b A)^{k+1} & =(a I+b A)^{k}(a I+b A) \\
& =\left(a^{k} I+k a^{k-1} b A\right)(a I+b A) \\
& =a^{k+1} I+k a^{k} b A I+a^{k} b I A+k a^{k-1} b^{2} A^{2} \\
& =a^{k+1} I+(k+1) a^{k} b A+k a^{k-1} b^{2} A^{2}
\end{aligned}
$$

Now,

$$
A^{2}=\left(\begin{array}{ll}
0 & 1 \\
0 & 0
\end{array}\right)\left(\begin{array}{ll}
0 & 1 \\
0 & 0
\end{array}\right)=\left(\begin{array}{ll}
0 & 0 \\
0 & 0
\end{array}\right)=0
$$

From (1), we have

$$
\begin{aligned}
(a I+b A)^{k+1} & =a^{k+1} I+(k+1) a^{k} b A+0 \\
& =a^{k+1} I+(k+1) a^{k} b A
\end{aligned}
$$

Therefore, the result is true for $n=k+1$.
Thus, by the principle of mathematical induction, we have:

$$
(a I+b A)^{n}=a^{n} I+n a^{n-1} b A \text { where } A=\left(\begin{array}{ll}
0 & 1 \\
0 & 0
\end{array}\right)_{, n \in N}
$$
:::

:::

:::question{number="MISC-2" kind="additional_exercise" id="sol_3.misc.2" topic="Matrix power by induction"}
#### Additional Question MISC-2

:::prompt
If

$$
A=\left(\begin{array}{lll}
1 & 1 & 1 \\
1 & 1 & 1 \\
1 & 1 & 1
\end{array}\right) \text {, prove that } A^{n}=\left(\begin{array}{lll}
3^{n-1} & 3^{n-1} & 3^{n-1} \\
3^{n-1} & 3^{n-1} & 3^{n-1} \\
3^{n-1} & 3^{n-1} & 3^{n-1}
\end{array}\right), n \in N
$$
:::

:::solution{label="Solution"}
It is given that

$$
A=\left(\begin{array}{lll}
1 & 1 & 1 \\
1 & 1 & 1 \\
1 & 1 & 1
\end{array}\right)
$$

We shall prove the result by using the principle of mathematical induction.
For $n=1$, we have:

$$
P(1):\left(\begin{array}{lll}
3^{n-1} & 3^{n-1} & 3^{n-1} \\
3^{n-1} & 3^{n-1} & 3^{n-1} \\
3^{n-1} & 3^{n-1} & 3^{n-1}
\end{array}\right)=\left(\begin{array}{lll}
3^{0} & 3^{0} & 3^{0} \\
3^{0} & 3^{0} & 3^{0} \\
3^{0} & 3^{0} & 3^{0}
\end{array}\right)=\left(\begin{array}{lll}
1 & 1 & 1 \\
1 & 1 & 1 \\
1 & 1 & 1
\end{array}\right)=A
$$

Therefore, the result is true for $n=1$.
Let the result be true for $n=k$.

$$
P(k): A^{k}=\left(\begin{array}{lll}
3^{k-1} & 3^{k-1} & 3^{k-1} \\
3^{k-1} & 3^{k-1} & 3^{k-1} \\
3^{k-1} & 3^{k-1} & 3^{k-1}
\end{array}\right)
$$

Now, we have to prove that the result is true for $n=k+1$.
Since,

$$
\begin{aligned}
A^{k+1} & =A \cdot A^{k} \\
& =\left(\begin{array}{lll}
1 & 1 & 1 \\
1 & 1 & 1 \\
1 & 1 & 1
\end{array}\right)\left(\begin{array}{lll}
3^{k-1} & 3^{k-1} & 3^{k-1} \\
3^{k-1} & 3^{k-1} & 3^{k-1} \\
3^{k-1} & 3^{k-1} & 3^{k-1}
\end{array}\right) \\
& =\left(\begin{array}{lll}
3 \cdot 3^{k-1} & 3 \cdot 3^{k-1} & 3 \cdot 3^{k-1} \\
3 \cdot 3^{k-1} & 3 \cdot 3^{k-1} & 3 \cdot 3^{k-1} \\
3 \cdot 3^{k-1} & 3 \cdot 3^{k-1} & 3 \cdot 3^{k-1}
\end{array}\right) \\
& =\left(\begin{array}{lll}
3^{(k+1)-1} & 3^{(k+1)-1} & 3^{(k+1)-1} \\
3^{(k+1)-1} & 3^{(k+1)-1} & 3^{(k+1)-1} \\
3^{(k+1)-1} & 3^{(k+1)-1} & 3^{(k+1)-1}
\end{array}\right)
\end{aligned}
$$

Therefore, the result is true for $n=k+1$.

Thus, by the principle of mathematical induction, we have:

$$
A^{n}=\left(\begin{array}{ccc}
3^{n-1} & 3^{n-1} & 3^{n-1} \\
3^{n-1} & 3^{n-1} & 3^{n-1} \\
3^{n-1} & 3^{n-1} & 3^{n-1}
\end{array}\right), n \in N
$$
:::

:::

:::question{number="MISC-3" kind="additional_exercise" id="sol_3.misc.3" topic="Matrix power by induction"}
#### Additional Question MISC-3

:::prompt
If $A=\left(\begin{array}{ll}3 & -4 \\ 1 & -1\end{array}\right)$, prove that $A^{n}=\left(\begin{array}{cc}1+2 n & -4 n \\ n & 1-2 n\end{array}\right)$, where $n$ is any positive integer.
:::

:::solution{label="Solution"}
It is given that $A=\left(\begin{array}{ll}3 & -4 \\ 1 & -1\end{array}\right)$
We shall prove the result by using the principle of mathematical induction.
For $n=1$, we have:

$$
\begin{aligned}
P(1) & : A^{1}=\left(\begin{array}{cc}
1+2 n & -4 n \\
n & 1-2 n
\end{array}\right) \\
& =\left(\begin{array}{ll}
3 & -4 \\
1 & -1
\end{array}\right) \\
& =A
\end{aligned}
$$

Therefore, the result is true for $n=1$.
Let the result be true for $n=k$.

$$
P(k): A^{k}=\left(\begin{array}{cc}
1+2 k & -4 k \\
k & 1-2 k
\end{array}\right), n \in N
$$

Now, we have to prove that the result is true for $n=k+1$.
Since,

$$
\begin{aligned}
A^{k+1} & =A \cdot A^{k} \\
& =\left(\begin{array}{cc}
1+2 k & -4 k \\
k & 1-2 k
\end{array}\right)\left(\begin{array}{ll}
3 & -4 \\
1 & -1
\end{array}\right) \\
& =\left(\begin{array}{cc}
3(1+2 k)-4 k & -4(1+2 k)+4 k \\
3 k+1-2 k & -4 k-1(1-2 k)
\end{array}\right) \\
& =\left(\begin{array}{cc}
3+6 k-4 k & -4-8 k+4 k \\
3 k+1-2 k & -4 k-1+2 k
\end{array}\right) \\
& =\left(\begin{array}{cc}
3+2 k & -4-4 k \\
1+k & -1-2 k
\end{array}\right) \\
& =\left(\begin{array}{cc}
1+2(k+1) & -4(k+1) \\
1+k & 1-2(k+1)
\end{array}\right)
\end{aligned}
$$

Therefore, the result is true for $n=k+1$.
Thus, by the principle of mathematical induction, we have:

$$
A^{n}=\left(\begin{array}{cc}
1+2 n & -4 n \\
n & 1-2 n
\end{array}\right) ; n \in N
$$
:::

:::

:::question{number="MISC-12" kind="additional_exercise" id="sol_3.misc.12" topic="Commuting matrices and induction"}
#### Additional Question MISC-12

:::prompt
If $A$ and $B$ are square matrices of the same order such that $A B=B A$, then prove by induction that $A B^{n}=B^{n} A$. Further, prove that $(A B)^{n}=A^{n} B^{n}$ for all $n \in N$.
:::

:::solution{label="Solution"}
Given: $A$ and $B$ are square matrices of the same order such that $A B=B A$.
To prove: $P(n): A B^{n}=B^{n} A, n \in N$
For $\mathrm{n}=1$, we have:

$$
\begin{array}{rlrl}
P(1) & : & A B=B A & \\
& \Rightarrow & \text { [Given] }
\end{array}
$$

Therefore, the result is true for $n=1$.
Let the result be true for $n=k$.

$$
P(k)=A B^{k}=B^{k} A
$$

Now, we prove that the result is true for $n=k+1$.

$$
\begin{aligned}
A B^{k+1} & =A B^{k} \cdot B & & \\
& =\left(B^{k} A\right) B & & {[B y(1)] } \\
& =B^{k}(A B) & & {[\text { Associative law }] } \\
& =B^{k}(B A) & & {[A B=B A(\text { Given })] } \\
& =\left(B^{k} B\right) A & & {[\text { Associative law }] } \\
& =B^{k+1} A & &
\end{aligned}
$$

Therefore, the result is true for $n=k+1$.

Thus, by the principle of mathematical induction, we have $A B^{n}=B^{n} A, n \in N$

Now, we have to prove that $(A B)^{n}=A^{n} B^{n}$ for all $n \in N$
For $n=1$, we have:

$$
(A B)^{1}=A^{1} B^{1}=A B
$$

Therefore, the result is true for $n=1$.
Let the result be true for $n=k$.

$$
(A B)^{k}=A^{k} B^{k}
$$

Now, we prove that the result is true for $n=k+1$.

$$
\begin{aligned}
A B^{k+1} & =(A B)^{k} \cdot(A B) & & \\
& =\left(A^{k} B^{k}\right) \cdot(A B) & & {[\text { By }(2)] } \\
& =A^{k}\left(B^{k} A\right) B & & {[\text { Associative law }] } \\
& =A^{k}\left(A B^{k}\right) B & & {\left[A B^{n}=B^{n} A, n \in N\right] } \\
& =\left(A^{k} A\right) \cdot\left(B^{k} B\right) & & {[\text { Associative law }] } \\
& =A^{k+1} B^{k+1} & &
\end{aligned}
$$

Therefore, the result is true for $n=k+1$.
Thus, by the principle of mathematical induction, we have $(A B)^{n}=A^{n} B^{n}, n \in N$
:::

:::
