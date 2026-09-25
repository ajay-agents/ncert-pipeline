## Chapter 4 Determinants

## EXERCISE 4.1

Question 1:
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

Question 2:
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

Question 3:
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

Question 4:
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

It can be observed that in the first column, two entries are zero. Thus, we expand along the first column $\left(C_{1}\right)$ for easier calculation.

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

Question 5:
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
It can be observed that in the second row, two entries are zero. Thus, we expand along the second row for easier calculation.
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

Question 6:

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

Question 7:
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

Question 8:
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

## EXERCISE 4.2

Question 1:
Using the property of determinants and without expanding, prove that:

$$
\left|\begin{array}{lll}
x & a & x+a \\
y & b & y+b \\
z & c & z+c
\end{array}\right|=0
$$

Solution:

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

Question 2:
Using the property of determinants and without expanding, prove that:

$$
\left|\begin{array}{lll}
a-b & b-c & c-a \\
b-c & c-a & a-b \\
c-a & a-b & b-c
\end{array}\right|=0
$$

Solution:

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
Question 3:
Using the property of determinants and without expanding, prove that:

$$
\left|\begin{array}{lll}
2 & 7 & 65 \\
3 & 8 & 75 \\
5 & 9 & 86
\end{array}\right|=0
$$

Solution:

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

Question 4:
Using the property of determinants and without expanding, prove that:

$$
\left|\begin{array}{lll}
1 & b c & a(b+c) \\
1 & c a & b(c+a) \\
1 & a b & c(a+b)
\end{array}\right|=0
$$

Solution:

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

Question 5:
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

Solution:

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
\Delta_{2} & =(-1)^{2}\left|\begin{array}{cc}
a & p \\
c & y \\
c & r \\
z
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

Question 6:

Using the property of determinants and without expanding, prove that:

$$
\left|\begin{array}{ccc}
0 & a & -b \\
-a & 0 & -c \\
b & c & 0
\end{array}\right|=0
$$

Solution:

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

Question 7:
Using the property of determinants and without expanding, prove that:

$$
\left|\begin{array}{ccc}
-a^{2} & a b & a c \\
b a & -b^{2} & b c \\
c a & c b & -c^{2}
\end{array}\right|=4 a^{2} b^{2} c^{2}
$$

Solution:

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
\end{array}\right| & \\
& =a^{2} b^{2} c^{2}\left|\begin{array}{ccc}
-1 & 1 & 1 \\
1 & -1 & 1 \\
1 & 1 & -1
\end{array}\right| & \text { [Taking out factors } \left.a, b, c \text { from } R_{1}, R_{2}, R_{3}\right] \\
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

Question 8:
By using properties of determinants show that:

(i) $\left|\begin{array}{lll}1 & a & a^{2} \\ 1 & b & b^{2} \\ 1 & c & c^{2}\end{array}\right|=(a-b)(b-c)(c-a)$
(ii) $\left|\begin{array}{ccc}1 & 1 & 1 \\ a & b & c \\ a^{3} & b^{3} & c^{3}\end{array}\right|=(a-b)(b-c)(c-a)(a+b+c)$

Solution:

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

Question 9:
By using properties of determinants show that:

$$
\left|\begin{array}{lll}
x & x^{2} & y z \\
y & y^{2} & z x \\
z & z^{2} & x y
\end{array}\right|=(x-y)(y-z)(z-x)(x y+y z+z x)
$$

Solution:

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

Question 10:
By using properties of determinants show that:

(i) $\left|\begin{array}{ccc}x+4 & 2 x & 2 x \\ 2 x & x+4 & 2 x \\ 2 x & 2 x & x+4\end{array}\right|=(5 x+4)(4-x)^{2}$
(ii) $\left|\begin{array}{ccc}y+k & y & y \\ y & y+k & y \\ y & y & y+k\end{array}\right|=k^{2}(3 y+k)$

Solution:
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

Question 11:
By using properties of determinants show that:
(i) $\left|\begin{array}{ccc}a-b-c & 2 a & 2 a \\ 2 b & b-c-a & 2 b \\ 2 c & 2 c & c-a-b\end{array}\right|=(a+b+c)^{3}$
(ii) $\left|\begin{array}{ccc}x+y+2 z & x & y \\ z & y+z+2 x & y \\ z & x & z+x+2 y\end{array}\right|=2(x+y+z)^{3}$

Solution:
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
\Delta & =\left|\begin{array}{cc}
2(x+y+z) & x \\
2(x+y+z) & y+z+2 x \\
2(x+y+z) & x \\
z+x+2 y
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

Question 12:
By using properties of determinants show that:

$$
\left|\begin{array}{ccc}
1 & x & x^{2} \\
x^{2} & 1 & x \\
x & x^{2} & 1
\end{array}\right|=\left(1-x^{3}\right)^{2}
$$

Solution:

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

Question 13:
By using properties of determinants show that:

$$
\left|\begin{array}{ccc}
1+a^{2}-b^{2} & 2 a b & -2 b \\
2 a b & 1-a^{2}+b^{2} & 2 a \\
2 b & -2 a & 1-a^{2}-b^{2}
\end{array}\right|=\left(1+a^{2}+b^{2}\right)^{3}
$$

Solution:

$$
\begin{aligned}
\Delta & =\left|\begin{array}{ccc}
1+a^{2}-b^{2} & 2 a b & -2 b \\
2 a b & 1-a^{2}+b^{2} & 2 a \\
2 b & -2 a & 1-a^{2}-b^{2}
\end{array}\right| \\
& =\left|\begin{array}{cc}
1+a^{2}+b^{2} & 0 \\
0 & -b\left(1+a^{2}+b^{2}\right) \\
2 b & -2 a
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

Question 14:
By using properties of determinants show that:

$$
\left|\begin{array}{ccc}
a^{2}+1 & a b & a c \\
a b & b^{2}+1 & b c \\
c a & c b & c^{2}+1
\end{array}\right|=1+a^{2}+b^{2}+c^{2}
$$

Solution:

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
& =\left|\begin{array}{cc}
a^{2}+1 & b^{2} \\
-1 & 1 \\
-1 & 0 \\
1 & 1
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

Question 15:
Let $A$ be a square matrix of order 3 × 3 , then $|k A|$ is equal to:
(A) $k|A|$
(B) $k^{2}|A|$
(C) $k^{3}|A|$
(D) $3^{k|A|}$

Solution:

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

Question 16:
Which of the following is correct?

(A) Determinant is a square matrix.
(B) Determinant is a number associated to a matrix.
(C) Determinant is a number associated to a square matrix.
(D) None of the above.

Solution:
We know that to every square matrix, $A=\left[a_{i j}\right]$ of order $n$, we can associate a number called the determinant of square matrix $A$, where $a_{i j}=(i, j)^{\text {th }}$ element of $A$.

Thus, the determinant is a number associated to a square matrix.
Hence, the correct option is C.

## EXERCISE 4.3

Question 1:
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

Question 2:
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

Question 3:
Find values of $k$ if area of triangle is 4 square units and vertices are:

(i) $(k, 0),(4,0),(0,2)$
(ii) $(-2,0),(0,4),(0, k)$

Solution:
We know that the area of a triangle whose vertices are $\left(x_{1}, y_{1}\right),\left(x_{2}, y_{2}\right)$ and $\left(x_{3}, y_{3}\right)$ is the absolute value of the determinant $(\Delta)$, where

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

Question 4:

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

Question 5:
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

It is given that the area of the triangle is 35 square units Hence, $\Delta= \pm 35$.

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

## EXERCISE 4.4

Question 1:
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

Question 2:
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

Question 3:
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

We know that $\Delta$ is equal to the sum of the product of the elements of the second row with their corresponding cofactors.

Therefore,

$$
\begin{aligned}
\Delta & =a_{21} A_{21}+a_{22} A_{22}+a_{23} A_{23} \\
& =2(7)+0(7)+1(-7) \\
& =14-7 \\
& =7
\end{aligned}
$$

Question 4:

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

We know that $\Delta$ is equal to the sum of the product of the elements of the third column with their corresponding cofactors.

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

Question 5:
If $\Delta=\left|\begin{array}{lll}a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \\ a_{31} & a_{32} & a_{33}\end{array}\right|$ and $A_{i j}$ is the cofactor of $a_{i j}$, then the value of $\Delta$ is given by:

A. $a_{11} A_{31}+a_{12} A_{32}+a_{13} A_{33}$
B. $a_{11} A_{11}+a_{12} A_{21}+a_{13} A_{31}$
C. $a_{21} A_{11}+a_{22} A_{12}+a_{23} A_{13}$
D. $a_{11} A_{11}+a_{21} A_{21}+a_{31} A_{31}$

Solution:
We know that $\Delta$ is equal to the sum of the product of the elements of a column or row with their corresponding cofactors.

$$
\Delta=a_{11} A_{11}+a_{21} A_{21}+a_{31} A_{31}
$$

Thus, the correct option is D.

## EXERCISE 4.5

Question 1:
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

Question 2:
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

Question 3:
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

Question 4:
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

Question 5:
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

Question 6:
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

Question 7:
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

Question 8:
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

Question 9:
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

Question 10:
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

Question 11:
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

Question 12:
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

Question 13:
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

Question 14:
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
& \Rightarrow h=1
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

Question 15:

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

Question 16:

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

Question 17:
Let $A$ be a non-singular square matrix of order $3 \times 3$. Then $|\operatorname{adj} A|$ is equal to:
(A) $|A|$
(B) $|A|^{2}$
(C) $|A|^{3}$
(D) $3|A|$

Solution:
Since $A$ be a non-singular square matrix of order $3 \times 3$

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

Question 18:
If $A$ is an invertible matrix of order 2 , the $\operatorname{det}\left(A^{-1}\right)$ is equal to:
(A) $\operatorname{det}(A)$
(B) $\frac{1}{\operatorname{det}(A)}$
(C) 1
(D) 0

Solution:
Since $A$ is an invertible matrix, $A^{-1}$ exists and $A^{-1}=\frac{1}{|A|}$ adj $A$. As matrix $A$ is of order 2, let $A=\left(\begin{array}{ll}a & b \\ c & d\end{array}\right)$

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

## EXERCISE 4.6

Question 1:
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
The given system of equations can be written in the form of $A X=B$, where

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

Question 2:
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
The given system of equations can be written in the form of $A X=B$, where

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

Question 3:
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
The given system of equations can be written in the form of $A X=B$, where

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

Question 4:
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
The given system of equations can be written in the form of $A X=B$, where

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

Question 5:
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
The given system of equations can be written in the form of $A X=B$, where

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

Question 6:
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
The given system of equations can be written in the form of $A X=B$, where

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

Question 7:
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
The given system of equations can be written in the form of $A X=B$, where

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

Question 8:
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
The given system of equations can be written in the form of $A X=B$, where

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

Question 9:
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
The given system of equations can be written in the form of $A X=B$, where

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

Question 10:
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
The given system of equations can be written in the form of $A X=B$, where

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

Question 11:
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
The given system of equations can be written in the form of $A X=B$, where

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

Question 12:
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
The given system of equations can be written in the form of $A X=B$, where $A=\left(\begin{array}{ccc}1 & -1 & 1 \\ 2 & 1 & -3 \\ 1 & 1 & 1\end{array}\right), X=\left[\begin{array}{l}x \\ y \\ z\end{array}\right]$ and $B=\left[\begin{array}{l}4 \\ 0 \\ 2\end{array}\right]$

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

Question 13:
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
The given system of equations can be written in the form of $A X=B$, where

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

Question 14:
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
The given system of equations can be written in the form of $A X=B$, where

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

Question 15:

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

The given system of equations can be written in the form of $A X=B$, where

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

The solution of the system of equations is given by $X=A^{-1} B$.
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

Question 16:

The cost of 4 kg onion, 3 kg wheat and 2 kg rice is $₹ 60$. The cost of 2 kg onion, 4 kg wheat and 6 kg rice is ₹ 90 . The cost of 6 kg onion 2 kg wheat and 3 kg rice is ₹ 70 . Find cost of each item per kg by matrix method.

Solution:
Let the cost of onions, wheat, and rice per kg in ₹ be $x, y$ and $z$ respectively.
Then, the given situation can be represented by a system of equations as:

$$
\begin{aligned}
& 4 x+3 y+2 z=60 \\
& 2 x+4 y+6 z=90 \\
& 6 x+2 y+3 z=70
\end{aligned}
$$

The given system of equations can be written in the form of $A X=B$, where

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

## MISCELLANEOUS EXERCISE

Question 1:
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

Question 2:
Without expanding the determinant, prove that $\left|\begin{array}{lll}a & a^{2} & b c \\ b & b^{2} & c a \\ c & c^{2} & a b\end{array}\right|=\left|\begin{array}{lll}1 & a^{2} & a^{3} \\ 1 & b^{2} & b^{3} \\ 1 & c^{2} & c^{3}\end{array}\right|$.

Solution:

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

Question 3:
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

Question 4:

If $a, b, c$ are real numbers and $\Delta=\left|\begin{array}{lll}b+c & c+a & a+b \\ c+a & a+b & b+c \\ a+b & b+c & c+a\end{array}\right|=0 \quad$, show that either $a+b+c=0$ or $a=b=c$.

Solution:

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

Question 5:
Solve the equations $\left|\begin{array}{ccc}x+a & x & x \\ x & x+a & x \\ x & x & x+a\end{array}\right|=0, a \neq 0 \quad$.
Solution:

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

Question 6:
Prove that $\left|\begin{array}{ccc}a^{2} & b c & a c+c^{2} \\ a^{2}+a b & b^{2} & a c \\ a b & b^{2}+b c & c^{2}\end{array}\right|=4 a^{2} b^{2} c^{2} \quad$.

Solution:

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

Question 7:

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

Question 8:

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

Question 9:
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

## Question 10:

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

## Question 11:

Using properties of determinants prove that:

$$
\left|\begin{array}{lll}
\alpha & \alpha^{2} & \beta+\gamma \\
\beta & \beta^{2} & \gamma+\alpha \\
\gamma & \gamma^{2} & \alpha+\beta
\end{array}\right|=(\beta-\gamma)(\gamma-\alpha)(\alpha-\beta)(\alpha+\beta+\gamma)
$$

## Solution:

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

## Question 12:

Using properties of determinants prove that:

$$
\left|\begin{array}{lll}
x & x^{2} & 1+p x^{3} \\
y & y^{2} & 1+p y^{3} \\
z & z^{2} & 1+p z^{3}
\end{array}\right|=(1+p x y z)(x-y)(y-z)(z-x)
$$

Solution:

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

Question 13:
Using properties of determinants prove that:

$$
\left|\begin{array}{ccc}
3 a & -a+b & -a+c \\
-b+a & 3 b & -b+c \\
-c+a & -c+b & 3 c
\end{array}\right|=3(a+b+c)(a b+b c+c a)
$$

Solution:

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

Question 14:
Using properties of determinants prove that:

$$
\left|\begin{array}{ccc}
1 & 1+p & 1+p+q \\
2 & 3+2 p & 4+3 p+2 q \\
3 & 6+3 p & 10+6 p+3 q
\end{array}\right|=1
$$

Solution:

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

Question 15:
Using properties of determinants prove that:

$$
\left|\begin{array}{ccc}
\sin \alpha & \cos \alpha & \cos (\alpha+\delta) \\
\sin \beta & \cos \beta & \cos (\beta+\delta) \\
\sin \gamma & \cos \gamma & \cos (\gamma+\delta)
\end{array}\right|=0
$$

Solution:

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

Question 16:
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
10 & -100 & 30 \\
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

Question 17:
If $a, b, c$ are in A.P, then the determinant $\left|\begin{array}{lll}x+2 & x+3 & x+2 a \\ x+3 & x+4 & x+2 b \\ x+4 & x+5 & x+2 c\end{array}\right|$ is
(A) 0
(B) 1
(C) $x$
(D) $2 x$

Solution:

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

Question 18:

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

Question 19:

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

