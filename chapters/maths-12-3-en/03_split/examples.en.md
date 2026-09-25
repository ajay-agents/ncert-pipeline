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
