---
subject: physics
class: 12
chapter: 4
lang: en
title: "Moving Charges and Magnetism"
---

# Moving Charges and Magnetism

## Examples

:::example{number="4.1" kind="example" id="ex_4.1" topic="Magnetic field suspending a current-carrying wire"}
#### Example 4.1

:::prompt
A straight wire of mass 200 g and length 1.5 m carries a current of 2 A. It is suspended in mid-air by a uniform horizontal magnetic field B (Fig. 4.3). What is the magnitude of the magnetic field?
:::

:::figure{src="images/fig_physics-12-4_4.jpg" id="fig_physics-12-4_4"}
FIGURE 4.3
:::

:::solution{label="Solution"}
From Eq. (4.4), we find that there is an upward force F, of magnitude $Il B$. For mid-air suspension, this must be balanced by the force due to gravity:
$$
\begin{aligned}
m g & =I l B \\
B & =\frac{m g}{I l} \\
& =\frac{0.2 \times 9.8}{2 \times 1.5}=0.65 \mathrm{~T}
\end{aligned}
$$
Note that it would have been sufficient to specify $\mathrm{m} / \mathrm{l}$, the mass per unit length of the wire. The earth's magnetic field is approximately $4 \times 10^{-5} \mathrm{~T}$ and we have ignored it.
:::

:::answer
**Answer:** $B = 0.65\ \mathrm{T}$
:::

:::

:::example{number="4.2" kind="example" id="ex_4.2" topic="Direction of Lorentz force on electron and proton"}
#### Example 4.2

:::prompt
If the magnetic field is parallel to the positive $y$-axis and the charged particle is moving along the positive $x$-axis (Fig. 4.4), which way would the Lorentz force be for (a) an electron (negative charge), (b) a proton (positive charge).
:::

:::figure{src="images/fig_physics-12-4_5.jpg" id="fig_physics-12-4_5"}
FIGURE 4.4
:::

:::part{label="a"}
:::prompt
an electron (negative charge)
:::

:::solution
The velocity $\mathbf{v}$ of the particle is along the $x$-axis, while $\mathbf{B}$, the magnetic field, is along the $y$-axis, so $\mathbf{v} \times \mathbf{B}$ is along the $z$-axis (screw rule or right-hand thumb rule). So, for an electron the force will be along the $-z$ axis.
:::

:::answer
**Answer:** along the $-z$ axis
:::

:::

:::part{label="b"}
:::prompt
a proton (positive charge)
:::

:::solution
For a positive charge (proton) the force is along the $+z$ axis.
:::

:::answer
**Answer:** along the $+z$ axis
:::

:::

:::

:::example{number="4.3" kind="example" id="ex_4.3" topic="Radius, frequency and energy of an electron in a magnetic field"}
#### Example 4.3

:::prompt
What is the radius of the path of an electron (mass $9 \times 10^{-31} \mathrm{~kg}$ and charge $1.6 \times 10^{-19} \mathrm{C}$) moving at a speed of $3 \times 10^{7} \mathrm{~m} / \mathrm{s}$ in a magnetic field of $6 \times 10^{-4} \mathrm{~T}$ perpendicular to it? What is its frequency? Calculate its energy in keV. ($1 \mathrm{eV}=1.6 \times 10^{-19} \mathrm{~J}$).
:::

:::solution{label="Solution"}
Using Eq. (4.5) we find
$$
\begin{aligned}
r & =m v /(q B)=9 \times 10^{-31} \mathrm{~kg} \times 3 \times 10^{7} \mathrm{~m} \mathrm{~s}^{-1} /\left(1.6 \times 10^{-19} \mathrm{C} \times 6 \times 10^{-4} \mathrm{~T}\right) \\
& =28 \times 10^{-2} \mathrm{~m}=28 \mathrm{~cm} \\
v & =v /(2 \pi r)=17 \times 10^{6} \mathrm{~s}^{-1}=17 \times 10^{6} \mathrm{~Hz}=17 \mathrm{MHz} \\
E & =(1 / 2) m v^{2}=(1 / 2) 9 \times 10^{-31} \mathrm{~kg} \times 9 \times 10^{14} \mathrm{~m}^{2} / \mathrm{s}^{2}=40.5 \times 10^{-17} \mathrm{~J} \\
& \approx 4 \times 10^{-16} \mathrm{~J}=2.5 \mathrm{keV} .
\end{aligned}
$$
:::

:::answer
**Answer:** $r = 28\ \mathrm{cm}$; frequency $= 17\ \mathrm{MHz}$; energy $\approx 2.5\ \mathrm{keV}$
:::

:::

:::example{number="4.4" kind="example" id="ex_4.4" topic="Magnetic field from a current element on the y-axis"}
#### Example 4.4

:::prompt
An element $\Delta \boldsymbol{l}=\Delta x \hat{\mathbf{i}}$ is placed at the origin and carries a large current $I=10 \mathrm{~A}$ (Fig. 4.8). What is the magnetic field on the $y$ axis at a distance of $0.5 \mathrm{~m}$. $\Delta x=1 \mathrm{~cm}$.
:::

:::figure{src="images/fig_physics-12-4_8.jpg" id="fig_physics-12-4_8"}
FIGURE 4.8
:::

:::solution{label="Solution"}
$$
\begin{aligned}
& |\mathrm{d} \mathbf{B}|=\frac{\mu_{0}}{4 \pi} \frac{I \mathrm{~d} l \sin \theta}{r^{2}} \text { [using Eq. (4.7)] } \\
& \mathrm{d} l=\Delta x=10^{-2} \mathrm{~m}, I=10 \mathrm{~A}, \quad r=0.5 \mathrm{~m}=\mathrm{y}, \mu_{0} / 4 \pi=10^{-7} \frac{\mathrm{Tm}}{\mathrm{~A}} \\
& \theta=90^{\circ} ; \sin \theta=1 \\
& |\mathrm{~d} \mathbf{B}|=\frac{10^{-7} \times 10 \times 10^{-2}}{25 \times 10^{-2}}=4 \times 10^{-8} \mathrm{~T}
\end{aligned}
$$
The direction of the field is in the $+z$-direction. This is so since,
$$
\mathrm{d} \boldsymbol{l} \times \mathbf{r}=\Delta x \hat{\mathbf{i}} \times y \hat{\mathbf{j}}=y \Delta x(\hat{\mathbf{i}} \times \hat{\mathbf{j}})=y \Delta x \hat{\mathbf{k}}
$$
We remind you of the following cyclic property of cross-products,
$$
\hat{\mathbf{i}} \times \hat{\mathbf{j}}=\hat{\mathbf{k}} ; \hat{\mathbf{j}} \times \hat{\mathbf{k}}=\hat{\mathbf{i}} ; \hat{\mathbf{k}} \times \hat{\mathbf{i}}=\hat{\mathbf{j}}
$$
Note that the field is small in magnitude.
:::

:::answer
**Answer:** $|d\mathbf{B}| = 4 \times 10^{-8}\ \mathrm{T}$, along $+z$-direction
:::

:::

:::example{number="4.5" kind="example" id="ex_4.5" topic="Magnetic field at the centre of a semicircular arc"}
#### Example 4.5

:::prompt
A straight wire carrying a current of 12 A is bent into a semi-circular arc of radius 2.0 cm as shown in Fig. 4.11(a). Consider the magnetic field $\mathbf{B}$ at the centre of the arc. (a) What is the magnetic field due to the straight segments? (b) In what way the contribution to B from the semicircle differs from that of a circular loop and in what way does it resemble? (c) Would your answer be different if the wire were bent into a semi-circular arc of the same radius but in the opposite way as shown in Fig. 4.11(b)?
:::

:::figure{src="images/fig_physics-12-4_11.jpg" id="fig_physics-12-4_11"}
FIGURE 4.11
:::

:::part{label="a"}
:::prompt
What is the magnetic field due to the straight segments?
:::

:::solution
$\mathrm{d} \boldsymbol{l}$ and $\mathbf{r}$ for each element of the straight segments are parallel. Therefore, $\mathrm{d} \boldsymbol{l} \times \mathbf{r}=0$. Straight segments do not contribute to $|B|$.
:::

:::answer
**Answer:** zero
:::

:::

:::part{label="b"}
:::prompt
In what way the contribution to B from the semicircle differs from that of a circular loop and in what way does it resemble?
:::

:::solution
For all segments of the semicircular arc, $\mathrm{d} \boldsymbol{l} \times \mathbf{r}$ are all parallel to each other (into the plane of the paper). All such contributions add up in magnitude. Hence direction of B for a semicircular arc is given by the right-hand rule and magnitude is half that of a circular loop. Thus B is $1.9 \times 10^{-4} \mathrm{~T}$ normal to the plane of the paper going into it.
:::

:::answer
**Answer:** $1.9 \times 10^{-4}\ \mathrm{T}$, normal to the plane, into the page
:::

:::

:::part{label="c"}
:::prompt
Would your answer be different if the wire were bent into a semi-circular arc of the same radius but in the opposite way as shown in Fig. 4.11(b)?
:::

:::solution
Same magnitude of B but opposite in direction to that in (b).
:::

:::answer
**Answer:** same magnitude, opposite direction
:::

:::

:::

:::example{number="4.6" kind="example" id="ex_4.6" topic="Magnetic field at the centre of a tightly wound coil"}
#### Example 4.6

:::prompt
Consider a tightly wound 100 turn coil of radius 10 cm, carrying a current of 1 A. What is the magnitude of the magnetic field at the centre of the coil?
:::

:::solution{label="Solution"}
Since the coil is tightly wound, we may take each circular element to have the same radius $R=10 \mathrm{~cm}=0.1 \mathrm{~m}$. The number of turns $N=100$. The magnitude of the magnetic field is,
$$
B=\frac{\mu_{0} N I}{2 R}=\frac{4 \pi \times 10^{-7} \times 10^{2} \times 1}{2 \times 10^{-1}}=2 \pi \times 10^{-4}=6.28 \times 10^{-4} \mathrm{~T}
$$
:::

:::answer
**Answer:** $6.28 \times 10^{-4}\ \mathrm{T}$
:::

:::

:::example{number="4.7" kind="example" id="ex_4.7" topic="Magnetic field inside and outside a current-carrying wire"}
#### Example 4.7

:::prompt
Figure 4.13 shows a long straight wire of a circular cross-section (radius a) carrying steady current $I$. The current $I$ is uniformly distributed across this cross-section. Calculate the magnetic field in the region $r<a$ and $r>a$.
:::

:::figure{src="images/fig_physics-12-4_15.jpg" id="fig_physics-12-4_15"}
FIGURE 4.13
:::

:::figure{src="images/fig_physics-12-4_16.jpg" id="fig_physics-12-4_16"}
FIGURE 4.14
:::

:::solution{label="Solution"}
(a) Consider the case $r>a$. The Amperian loop, labelled 2, is a circle concentric with the cross-section. For this loop,
$$
\begin{aligned}
& L=2 \pi r \\
& I_{e}=\text { Current enclosed by the loop }=I
\end{aligned}
$$
The result is the familiar expression for a long straight wire
$$
\begin{aligned}
& B(2 \pi r)=\mu_{0} I \\
& B=\frac{\mu_{0} I}{2 \pi r} \quad[4.15(\mathrm{a})] \\
& B \propto \frac{1}{r} \quad(r>a)
\end{aligned}
$$
Now the current enclosed $I_{e}$ is not $I$, but is less than this value. Since the current distribution is uniform, the current enclosed is,
$$
I_{e}=I \frac{\pi r^{2}}{\pi a^{2}}=\frac{I r^{2}}{a^{2}}
$$
Using Ampere's law, $B(2 \pi r)=\mu_{0} \frac{I r^{2}}{a^{2}}$
$$
\begin{aligned}
& B=\left(\frac{\mu_{0} I}{2 \pi a^{2}}\right) r \\
& B \propto r \quad(r<a)
\end{aligned}
$$

Figure (4.14) shows a plot of the magnitude of $\mathbf{B}$ with distance $r$ from the centre of the wire. The direction of the field is tangential to the respective circular loop (1 or 2) and given by the right-hand rule described earlier in this section.
:::

:::answer
**Answer:** $B = \mu_0 I / (2\pi r)$ for $r>a$; $B = (\mu_0 I / 2\pi a^2)\,r$ for $r<a$
:::

:::

:::example{number="4.8" kind="example" id="ex_4.8" topic="Magnetic field inside a long solenoid"}
#### Example 4.8

:::prompt
A solenoid of length 0.5 m has a radius of 1 cm and is made up of 500 turns. It carries a current of 5 A. What is the magnitude of the magnetic field inside the solenoid?
:::

:::solution{label="Solution"}
The number of turns per unit length is,
$$
n=\frac{500}{0.5}=1000 \text { turns } / \mathrm{m}
$$
The length $l=0.5 \mathrm{~m}$ and radius $r=0.01 \mathrm{~m}$. Thus, $l / a=50$ i.e., $l \gg a$. Hence, we can use the long solenoid formula, namely, Eq. (4.20)
$$
\begin{aligned}
B & =\mu_{o} n I \\
& =4 \pi \times 10^{-7} \times 10^{3} \times 5 \\
& =6.28 \times 10^{-3} \mathrm{~T}
\end{aligned}
$$
:::

:::answer
**Answer:** $6.28 \times 10^{-3}\ \mathrm{T}$
:::

:::

:::example{number="4.9" kind="example" id="ex_4.9" topic="Force per unit length on a wire in earth's magnetic field"}
#### Example 4.9

:::prompt
The horizontal component of the earth's magnetic field at a certain place is $3.0 \times 10^{-5} \mathrm{~T}$ and the direction of the field is from the geographic south to the geographic north. A very long straight conductor is carrying a steady current of 1A. What is the force per unit length on it when it is placed on a horizontal table and the direction of the current is (a) east to west; (b) south to north?
:::

:::part{label="a"}
:::prompt
east to west
:::

:::solution
$\mathbf{F}=I \boldsymbol{l} \times \mathbf{B}$
$$
F=I l B \sin \theta
$$
The force per unit length is
$$
f=F / l=I B \sin \theta
$$
When the current is flowing from east to west,
$$
\theta=90^{\circ}
$$
Hence,
$$
\begin{aligned}
f & =I \mathrm{~B} \\
& =1 \times 3 \times 10^{-5}=3 \times 10^{-5} \mathrm{~N} \mathrm{~m}^{-1}
\end{aligned}
$$
This is larger than the value $2 \times 10^{-7} \mathrm{Nm}^{-1}$ quoted in the definition of the ampere. Hence it is important to eliminate the effect of the earth's magnetic field and other stray fields while standardising the ampere.
The direction of the force is downwards. This direction may be obtained by the directional property of cross product of vectors.
:::

:::answer
**Answer:** $3 \times 10^{-5}\ \mathrm{N\,m^{-1}}$, directed downwards
:::

:::

:::part{label="b"}
:::prompt
south to north
:::

:::solution
When the current is flowing from south to north,
$$
\begin{aligned}
& \theta=0^{\circ} \\
& f=0
\end{aligned}
$$
Hence there is no force on the conductor.
:::

:::answer
**Answer:** zero
:::

:::

:::

:::example{number="4.10" kind="example" id="ex_4.10" topic="Field, moment, torque and angular speed of a rotating coil"}
#### Example 4.10

:::prompt
A 100 turn closely wound circular coil of radius 10 cm carries a current of 3.2 A. (a) What is the field at the centre of the coil? (b) What is the magnetic moment of this coil?
The coil is placed in a vertical plane and is free to rotate about a horizontal axis which coincides with its diameter. A uniform magnetic field of 2T in the horizontal direction exists such that initially the axis of the coil is in the direction of the field. The coil rotates through an angle of 90° under the influence of the magnetic field. (c) What are the magnitudes of the torques on the coil in the initial and final position? (d) What is the angular speed acquired by the coil when it has rotated by 90°? The moment of inertia of the coil is $0.1 \mathrm{~kg} \mathrm{~m}^{2}$.
:::

:::part{label="a"}
:::prompt
What is the field at the centre of the coil?
:::

:::solution
From Eq. (4.12)
$$
B=\frac{\mu_{0} N I}{2 R}
$$
Here, $N=100 ; I=3.2 \mathrm{~A}$, and $R=0.1 \mathrm{~m}$. Hence,
$$
\begin{aligned}
B & =\frac{4 \pi \times 10^{-7} \times 3.2}{2 \times 10^{-1}}=\frac{4 \times 10^{-5} \times 10}{2 \times 10^{-1}} \quad(\text { using } \pi \times 3.2=10) \\
& =2 \times 10^{-3} \mathrm{~T}
\end{aligned}
$$
The direction is given by the right-hand thumb rule.
:::

:::answer
**Answer:** $2 \times 10^{-3}\ \mathrm{T}$
:::

:::

:::part{label="b"}
:::prompt
What is the magnetic moment of this coil?
:::

:::solution
The magnetic moment is given by Eq. (4.24),
$$
m=N I A=N I \pi r^{2}=100 \times 3.2 \times 3.14 \times 10^{-2}=10 \mathrm{~A} \mathrm{~m}^{2}
$$
The direction is once again given by the right-hand thumb rule.
:::

:::answer
**Answer:** $10\ \mathrm{A\,m^2}$
:::

:::

:::part{label="c"}
:::prompt
What are the magnitudes of the torques on the coil in the initial and final position?
:::

:::solution
$\tau=|\mathbf{m} \times \mathbf{B}|$ [from Eq. (4.23)]
$$
=m B \sin \theta
$$
Initially, $\theta=0$. Thus, initial torque $\tau_{i}=0$. Finally, $\theta=\pi / 2$ (or 90°).
Thus, final torque $\tau_{f}=m B=10 \times 2=20 \mathrm{~N} \mathrm{~m}$.
:::

:::answer
**Answer:** initial torque $\tau_i = 0$; final torque $\tau_f = 20\ \mathrm{N\,m}$
:::

:::

:::part{label="d"}
:::prompt
What is the angular speed acquired by the coil when it has rotated by 90°? The moment of inertia of the coil is $0.1 \mathrm{~kg} \mathrm{~m}^{2}$.
:::

:::solution
From Newton's second law,
$$
9 \frac{\mathrm{~d} \omega}{\mathrm{~d} t}=m B \sin \theta
$$
where $\mathscr{g}$ is the moment of inertia of the coil. From chain rule,
$$
\frac{\mathrm{d} \omega}{\mathrm{~d} t}=\frac{\mathrm{d} \omega}{\mathrm{~d} \theta} \frac{\mathrm{~d} \theta}{\mathrm{~d} t}=\frac{\mathrm{d} \omega}{\mathrm{~d} \theta} \omega
$$
Using this,
$$
\vartheta \omega \mathrm{d} \omega=m B \sin \theta \mathrm{~d} \theta
$$
Integrating from $\theta=0$ to $\theta=\pi / 2$,
$$
\begin{aligned}
& g \int_{0}^{\omega f} \omega \mathrm{~d} \omega=m B \int_{0}^{\pi / 2} \sin \theta \mathrm{~d} \theta \\
& g \frac{\omega_{f}^{2}}{2}=-\left.m B \cos \theta\right|_{0} ^{\pi / 2}=m B \\
& \omega_{f}=\left(\frac{2 m B}{g}\right)^{1 / 2}=\left(\frac{2 \times 20}{10^{-1}}\right)^{1 / 2}=20 \mathrm{~s}^{-1}
\end{aligned}
$$
:::

:::answer
**Answer:** $\omega_f = 20\ \mathrm{s^{-1}}$
:::

:::

:::

:::example{number="4.11" kind="example" id="ex_4.11" topic="Conceptual questions on torque and equilibrium of a current loop"}
#### Example 4.11

:::prompt
(a) A current-carrying circular loop lies on a smooth horizontal plane. Can a uniform magnetic field be set up in such a manner that the loop turns around itself (i.e., turns about the vertical axis).
(b) A current-carrying circular loop is located in a uniform external magnetic field. If the loop is free to turn, what is its orientation of stable equilibrium? Show that in this orientation, the flux of the total field (external field + field produced by the loop) is maximum.
(c) A loop of irregular shape carrying current is located in an external magnetic field. If the wire is flexible, why does it change to a circular shape?
:::

:::part{label="a"}
:::prompt
A current-carrying circular loop lies on a smooth horizontal plane. Can a uniform magnetic field be set up in such a manner that the loop turns around itself (i.e., turns about the vertical axis).
:::

:::solution
No, because that would require $\tau$ to be in the vertical direction. But $\tau=I \mathbf{A} \times \mathbf{B}$, and since $\mathbf{A}$ of the horizontal loop is in the vertical direction, $\tau$ would be in the plane of the loop for any $\mathbf{B}$.
:::

:::answer
**Answer:** no
:::

:::

:::part{label="b"}
:::prompt
A current-carrying circular loop is located in a uniform external magnetic field. If the loop is free to turn, what is its orientation of stable equilibrium? Show that in this orientation, the flux of the total field (external field + field produced by the loop) is maximum.
:::

:::solution
Orientation of stable equilibrium is one where the area vector A of the loop is in the direction of external magnetic field. In this orientation, the magnetic field produced by the loop is in the same direction as external field, both normal to the plane of the loop, thus giving rise to maximum flux of the total field.
:::

:::answer
**Answer:** area vector A aligned with the external field
:::

:::

:::part{label="c"}
:::prompt
A loop of irregular shape carrying current is located in an external magnetic field. If the wire is flexible, why does it change to a circular shape?
:::

:::solution
It assumes circular shape with its plane normal to the field to maximise flux, since for a given perimeter, a circle encloses greater area than any other shape.
:::

:::answer
**Answer:** a circle encloses the greatest area for a given perimeter, maximising flux
:::

:::

:::

:::example{number="4.12" kind="example" id="ex_4.12" topic="Galvanometer, ammeter and ideal-ammeter current readings"}
#### Example 4.12

:::prompt
In the circuit (Fig. 4.23) the current is to be measured. What is the value of the current if the ammeter shown (a) is a galvanometer with a resistance $R_{G}=60.00 \Omega$; (b) is a galvanometer described in (a) but converted to an ammeter by a shunt resistance $r_{s}=0.02 \Omega$; (c) is an ideal ammeter with zero resistance?
:::

:::figure{src="images/fig_physics-12-4_23.jpg" id="fig_physics-12-4_23"}
FIGURE 4.23
:::

:::part{label="a"}
:::prompt
is a galvanometer with a resistance $R_{G}=60.00 \Omega$
:::

:::solution
Total resistance in the circuit is, $R_{G}+3=63 \Omega$. Hence, $I=3 / 63=0.048 \mathrm{~A}$.
:::

:::answer
**Answer:** $0.048\ \mathrm{A}$
:::

:::

:::part{label="b"}
:::prompt
is a galvanometer described in (a) but converted to an ammeter by a shunt resistance $r_{s}=0.02 \Omega$
:::

:::solution
Resistance of the galvanometer converted to an ammeter is, $\frac{R_{G} r_{s}}{R_{G}+r_{s}}=\frac{60 \Omega \times 0.02 \Omega}{(60+0.02) \Omega} \simeq 0.02 \Omega$
Total resistance in the circuit is, $0.02 \Omega+3 \Omega=3.02 \Omega$. Hence, $I=3 / 3.02=0.99 \mathrm{~A}$.
:::

:::answer
**Answer:** $0.99\ \mathrm{A}$
:::

:::

:::part{label="c"}
:::prompt
is an ideal ammeter with zero resistance
:::

:::solution
For the ideal ammeter with zero resistance, $I=3 / 3=1.00 \mathrm{~A}$
:::

:::answer
**Answer:** $1.00\ \mathrm{A}$
:::

:::

:::

## Questions and Solutions

:::question{number="4.1" kind="exercise" id="q_4.1" topic="Magnetic field at centre of a circular coil"}
#### Question 4.1

:::prompt
A circular coil of wire consisting of 100 turns, each of radius 8.0 cm carries a current of 0.40 A. What is the magnitude of the magnetic field B at the centre of the coil?
:::

:::solution{label="Solution"}
Number of turns on the circular coil, $n=100$
Radius of each turn, $r=8.0 \mathrm{~cm}=0.08 \mathrm{~m}$
Current flowing in the coil, $I=0.4 \mathrm{~A}$
Magnitude of the magnetic field at the centre of the coil is given by the relation,
$$
|\mathbf{B}|=\frac{\mu_{0}}{4 \pi} \frac{2 \pi n I}{r}
$$
Where,
$$
\begin{aligned}
& \mu_{0}=\text { Permeability of free space } \\
& =4 \pi \times 10^{-7} \mathrm{~T} \mathrm{~m} \mathrm{~A}^{-1}
\end{aligned}
$$
$$
\begin{aligned}
|\mathbf{B}| & =\frac{4 \pi \times 10^{-7}}{4 \pi} \times \frac{2 \pi \times 100 \times 0.4}{0.08} \\
& =3.14 \times 10^{-4} \mathrm{~T}
\end{aligned}
$$
Hence, the magnitude of the magnetic field is $3.14 \times 10^{-4} \mathrm{~T}$.
:::

:::answer
**Answer:** $3.14 \times 10^{-4}\ \mathrm{T}$
:::

:::

:::question{number="4.2" kind="exercise" id="q_4.2" topic="Magnetic field near a long straight wire"}
#### Question 4.2

:::prompt
A long straight wire carries a current of 35 A. What is the magnitude of the field B at a point 20 cm from the wire?
:::

:::solution{label="Solution"}
Current in the wire, $I=35 \mathrm{~A}$
Distance of a point from the wire, $r=20 \mathrm{~cm}=0.2 \mathrm{~m}$
Magnitude of the magnetic field at this point is given as:
$$
{ }_{B}=\frac{\mu_{0}}{4 \pi} \frac{2 I}{r}
$$
Where,
$$
\mu_{0}=\text { Permeability of free space }=4 \pi \times 10^{-7} \mathrm{~T} \mathrm{~m} \mathrm{~A}^{-1}
$$
$$
\begin{aligned}
B & =\frac{4 \pi \times 10^{-7} \times 2 \times 35}{4 \pi \times 0.2} \\
& =3.5 \times 10^{-5} \mathrm{~T}
\end{aligned}
$$
Hence, the magnitude of the magnetic field at a point 20 cm from the wire is $3.5 \times 10^{-5} \mathrm{~T}$.
:::

:::answer
**Answer:** $3.5 \times 10^{-5}\ \mathrm{T}$
:::

:::

:::question{number="4.3" kind="exercise" id="q_4.3" topic="Field direction from a north-south wire"}
#### Question 4.3

:::prompt
A long straight wire in the horizontal plane carries a current of 50 A in north to south direction. Give the magnitude and direction of B at a point 2.5 m east of the wire.
:::

:::solution{label="Solution"}
Current in the wire, $I=50 \mathrm{~A}$
A point is 2.5 m away from the East of the wire.
∴ Magnitude of the distance of the point from the wire, $r=2.5 \mathrm{~m}$.
Magnitude of the magnetic field at that point is given by the relation, $B=\frac{\mu_{0} 2 I}{4 \pi r}$
Where,
$\mu_{0}$ = Permeability of free space $=4 \pi \times 10^{-7} \mathrm{Tm} \mathrm{A}^{-1}$
$$
\begin{aligned}
B & =\frac{4 \pi \times 10^{-7} \times 2 \times 50}{4 \pi \times 2.5} \\
& =4 \times 10^{-6} \mathrm{~T}
\end{aligned}
$$
The point is located normal to the wire length at a distance of 2.5 m. The direction of the current in the wire is vertically downward. Hence, according to the Maxwell's right hand thumb rule, the direction of the magnetic field at the given point is vertically upward.
:::

:::answer
**Answer:** $4 \times 10^{-6}\ \mathrm{T}$, vertically upward
:::

:::

:::question{number="4.4" kind="exercise" id="q_4.4" topic="Field below an overhead power line"}
#### Question 4.4

:::prompt
A horizontal overhead power line carries a current of 90 A in east to west direction. What is the magnitude and direction of the magnetic field due to the current 1.5 m below the line?
:::

:::solution{label="Solution"}
Current in the power line, $I=90 \mathrm{~A}$
Point is located below the power line at distance, $r=1.5 \mathrm{~m}$
Hence, magnetic field at that point is given by the relation,
$$
B=\frac{\mu_{0} 2 I}{4 \pi r}
$$
Where,
$$
\begin{aligned}
& \mu_{0}=\text { Permeability of free space }=4 \pi \times 10^{-7} \mathrm{Tm} \mathrm{~A}^{-1} \\
& B=\frac{4 \pi \times 10^{-7} \times 2 \times 90}{4 \pi \times 1.5}=1.2 \times 10^{-5} \mathrm{~T}
\end{aligned}
$$
The current is flowing from East to West. The point is below the power line. Hence, according to Maxwell's right hand thumb rule, the direction of the magnetic field is towards the South.
:::

:::answer
**Answer:** $1.2 \times 10^{-5}\ \mathrm{T}$, towards the South
:::

:::

:::question{number="4.5" kind="exercise" id="q_4.5" topic="Force per unit length on an angled wire"}
#### Question 4.5

:::prompt
What is the magnitude of magnetic force per unit length on a wire carrying a current of 8 A and making an angle of 30° with the direction of a uniform magnetic field of 0.15 T?
:::

:::solution{label="Solution"}
Current in the wire, $I=8 \mathrm{~A}$
Magnitude of the uniform magnetic field, $B=0.15 \mathrm{~T}$
Angle between the wire and magnetic field, $\theta=30^{\circ}$.
Magnetic force per unit length on the wire is given as:
$$
\begin{aligned}
& f=B I \sin \theta \\
& =0.15 \times 8 \times 1 \times \sin 30^{\circ} \\
& =0.6 \mathrm{~N} \mathrm{~m}^{-1}
\end{aligned}
$$
Hence, the magnetic force per unit length on the wire is $0.6 \mathrm{~N} \mathrm{~m}^{-1}$.
:::

:::answer
**Answer:** $0.6\ \mathrm{N\,m^{-1}}$
:::

:::

:::question{number="4.6" kind="exercise" id="q_4.6" topic="Force on a wire inside a solenoid"}
#### Question 4.6

:::prompt
A 3.0 cm wire carrying a current of 10 A is placed inside a solenoid perpendicular to its axis. The magnetic field inside the solenoid is given to be 0.27 T. What is the magnetic force on the wire?
:::

:::solution{label="Solution"}
Length of the wire, $l=3 \mathrm{~cm}=0.03 \mathrm{~m}$
Current flowing in the wire, $I=10 \mathrm{~A}$
Magnetic field, $B=0.27 \mathrm{~T}$
Angle between the current and magnetic field, $\theta=90^{\circ}$
Magnetic force exerted on the wire is given as:
$$
\begin{aligned}
& F=B I l \sin \theta \\
& =0.27 \times 10 \times 0.03 \sin 90^{\circ} \\
& =8.1 \times 10^{-2} \mathrm{~N}
\end{aligned}
$$
Hence, the magnetic force on the wire is $8.1 \times 10^{-2} \mathrm{~N}$. The direction of the force can be obtained from Fleming's left hand rule.
:::

:::answer
**Answer:** $8.1 \times 10^{-2}\ \mathrm{N}$
:::

:::

:::question{number="4.7" kind="exercise" id="q_4.7" topic="Force between two parallel current-carrying wires"}
#### Question 4.7

:::prompt
Two long and parallel straight wires A and B carrying currents of 8.0 A and 5.0 A in the same direction are separated by a distance of 4.0 cm. Estimate the force on a 10 cm section of wire A.
:::

:::solution{label="Solution"}
Current flowing in wire $\mathrm{A}, I_{\mathrm{A}}=8.0 \mathrm{~A}$
Current flowing in wire $\mathrm{B}, I_{\mathrm{B}}=5.0 \mathrm{~A}$
Distance between the two wires, $r=4.0 \mathrm{~cm}=0.04 \mathrm{~m}$
Length of a section of wire A, $l=10 \mathrm{~cm}=0.1 \mathrm{~m}$
Force exerted on length $l$ due to the magnetic field is given as:
$$
B=\frac{\mu_{0} 2 I_{\mathrm{A}} I_{\mathrm{B}} l}{4 \pi r}
$$
Where,
$$
\mu_{0}=\text { Permeability of free space }=4 \pi \times 10^{-7} \mathrm{~T} \mathrm{~m} \mathrm{~A}^{-1}
$$
$$
\begin{aligned}
B & =\frac{4 \pi \times 10^{-7} \times 2 \times 8 \times 5 \times 0.1}{4 \pi \times 0.04} \\
& =2 \times 10^{-5} \mathrm{~N}
\end{aligned}
$$
The magnitude of force is $2 \times 10^{-5} \mathrm{~N}$. This is an attractive force normal to A towards B because the direction of the currents in the wires is the same.
:::

:::answer
**Answer:** $2 \times 10^{-5}\ \mathrm{N}$, attractive
:::

:::

:::question{number="4.8" kind="exercise" id="q_4.8" topic="Magnetic field inside a multi-layer solenoid"}
#### Question 4.8

:::prompt
A closely wound solenoid 80 cm long has 5 layers of windings of 400 turns each. The diameter of the solenoid is 1.8 cm. If the current carried is 8.0 A, estimate the magnitude of B inside the solenoid near its centre.
:::

:::solution{label="Solution"}
Length of the solenoid, $l=80 \mathrm{~cm}=0.8 \mathrm{~m}$
There are five layers of windings of 400 turns each on the solenoid.
∴ Total number of turns on the solenoid, $N=5 \times 400=2000$
Diameter of the solenoid, $D=1.8 \mathrm{~cm}=0.018 \mathrm{~m}$
Current carried by the solenoid, $I=8.0 \mathrm{~A}$
Magnitude of the magnetic field inside the solenoid near its centre is given by the relation,
$$
B=\frac{\mu_{0} N I}{l}
$$
Where,
$$
\mu_{0}=\text { Permeability of free space }=4 \pi \times 10^{-7} \mathrm{~T} \mathrm{~m} \mathrm{~A}^{-1}
$$
$$
\begin{aligned}
B & =\frac{4 \pi \times 10^{-7} \times 2000 \times 8}{0.8} \\
& =8 \pi \times 10^{-3}=2.512 \times 10^{-2} \mathrm{~T}
\end{aligned}
$$
Hence, the magnitude of the magnetic field inside the solenoid near its centre is $2.512 \times$ $10^{-2} \mathrm{~T}$.
:::

:::answer
**Answer:** $2.512 \times 10^{-2}\ \mathrm{T}$
:::

:::

:::question{number="4.9" kind="exercise" id="q_4.9" topic="Torque on a suspended square coil"}
#### Question 4.9

:::prompt
A square coil of side 10 cm consists of 20 turns and carries a current of 12 A. The coil is suspended vertically and the normal to the plane of the coil makes an angle of 30° with the direction of a uniform horizontal magnetic field of magnitude 0.80 T. What is the magnitude of torque experienced by the coil?
:::

:::solution{label="Solution"}
Length of a side of the square coil, $l=10 \mathrm{~cm}=0.1 \mathrm{~m}$
Current flowing in the coil, $I=12 \mathrm{~A}$
Number of turns on the coil, $n=20$
Angle made by the plane of the coil with magnetic field, $\theta=30^{\circ}$
Strength of magnetic field, $B=0.80 \mathrm{~T}$
Magnitude of the magnetic torque experienced by the coil in the magnetic field is given by the relation,
$$
\tau=n B I A \sin \theta
$$
Where,
$$
\begin{aligned}
& A=\text { Area of the square coil } \\
& \Rightarrow l \times l=0.1 \times 0.1=0.01 \mathrm{~m}^{2} \\
& \therefore \tau=20 \times 0.8 \times 12 \times 0.01 \times \sin 30^{\circ} \\
& =0.96 \mathrm{~N} \mathrm{~m}
\end{aligned}
$$
Hence, the magnitude of the torque experienced by the coil is 0.96 N m.
:::

:::answer
**Answer:** $0.96\ \mathrm{N\,m}$
:::

:::

:::question{number="4.10" kind="exercise" id="q_4.10" topic="Comparing sensitivity of two moving-coil meters"}
#### Question 4.10

:::prompt
Two moving coil meters, $\mathrm{M}_{1}$ and $\mathrm{M}_{2}$ have the following particulars:
$$
\begin{aligned}
& R_{1}=10 \Omega, \quad N_{1}=30 \\
& A_{1}=3.6 \times 10^{-3} \mathrm{~m}^{2}, B_{1}=0.25 \mathrm{~T} \\
& R_{2}=14 \Omega, \quad N_{2}=42 \\
& A_{2}=1.8 \times 10^{-3} \mathrm{~m}^{2}, B_{2}=0.50 \mathrm{~T}
\end{aligned}
$$
(The spring constants are identical for the two meters).
Determine the ratio of (a) current sensitivity and (b) voltage sensitivity of $\mathrm{M}_{2}$ and $\mathrm{M}_{1}$.
:::

:::solution{label="Solution"}
For moving coil meter $\mathrm{M}_{1}$:
Resistance, $R_{1}=10 \Omega$
Number of turns, $N_{1}=30$
Area of cross-section, $A_{1}=3.6 \times 10^{-3} \mathrm{~m}^{2}$
Magnetic field strength, $B_{1}=0.25 \mathrm{~T}$
Spring constant $K_{1}=K$
For moving coil meter $\mathrm{M}_{2}$:
Resistance, $R_{2}=14 \Omega$
Number of turns, $N_{2}=42$
Area of cross-section, $A_{2}=1.8 \times 10^{-3} \mathrm{~m}^{2}$
Magnetic field strength, $B_{2}=0.50 \mathrm{~T}$
Spring constant, $K_{2}=K$
Current sensitivity of $\mathrm{M}_{1}$ is given as:
$$
I_{\mathrm{s} 1}=\frac{N_{1} B_{1} A_{1}}{K_{1}}
$$
And, current sensitivity of $\mathrm{M}_{2}$ is given as:
$$
\begin{aligned}
& I_{\mathrm{s} 2}=\frac{N_{2} B_{2} A_{2}}{K_{2}} \\
& \therefore \text { Ratio } \frac{I_{\mathrm{s} 2}}{I_{\mathrm{s} 1}}=\frac{N_{2} B_{2} A_{2} K_{1}}{K_{2} N_{1} B_{1} A_{1}} \\
& =\frac{42 \times 0.5 \times 1.8 \times 10^{-3} \times K}{K \times 30 \times 0.25 \times 3.6 \times 10^{-3}}=1.4
\end{aligned}
$$
Hence, the ratio of current sensitivity of $\mathrm{M}_{2}$ to $\mathrm{M}_{1}$ is 1.4.
Voltage sensitivity for $\mathrm{M}_{2}$ is given as:
$$
V_{\mathrm{s} 2}=\frac{N_{2} B_{2} A_{2}}{K_{2} R_{2}}
$$
And, voltage sensitivity for $\mathrm{M}_{1}$ is given as:
$$
\begin{aligned}
& V_{\mathrm{s} 1}=\frac{N_{1} B_{1} A_{1}}{K_{1}} \\
& \therefore \text { Ratio } \frac{V_{\mathrm{s} 2}}{V \mathrm{~s} 1}=\frac{N_{2} B_{2} A_{2} K_{1} R_{1}}{K_{2} R_{2} N_{1} B_{1} A_{1}} \\
& =\frac{42 \times 0.5 \times 1.8 \times 10^{-3} \times 10 \times K}{K \times 14 \times 30 \times 0.25 \times 3.6 \times 10^{-3}}=1
\end{aligned}
$$
Hence, the ratio of voltage sensitivity of $\mathrm{M}_{2}$ to $\mathrm{M}_{1}$ is 1.
:::

:::answer
**Answer:** current sensitivity ratio $= 1.4$; voltage sensitivity ratio $= 1$
:::

:::

:::question{number="4.11" kind="exercise" id="q_4.11" topic="Radius of an electron's circular orbit"}
#### Question 4.11

:::prompt
In a chamber, a uniform magnetic field of 6.5 $\mathrm{G}\left(1 \mathrm{G}=10^{-4} \mathrm{~T}\right)$ is maintained. An electron is shot into the field with a speed of $4.8 \times 10^{6} \mathrm{~m} \mathrm{~s}^{-1}$ normal to the field. Explain why the path of the electron is a circle. Determine the radius of the circular orbit. ( $e=1.5 \times 10^{-19} \mathrm{C}, m_{e}=9.1 \times 10^{-31} \mathrm{~kg}$ )
:::

:::solution{label="Solution"}
Magnetic field strength, $B=6.5 \mathrm{G}=6.5 \times 10^{-4} \mathrm{~T}$
Speed of the electron, $v=4.8 \times 10^{6} \mathrm{~m} / \mathrm{s}$
Charge on the electron, $e=1.6 \times 10^{-19} \mathrm{C}$
Mass of the electron, $m_{e}=9.1 \times 10^{-31} \mathrm{~kg}$
Angle between the shot electron and magnetic field, $\theta=90^{\circ}$
Magnetic force exerted on the electron in the magnetic field is given as:
$$
F=e v B \sin \theta
$$
This force provides centripetal force to the moving electron. Hence, the electron starts moving in a circular path of radius $r$.
Hence, centripetal force exerted on the electron,
$$
F_{\mathrm{c}}=\frac{m v^{2}}{r}
$$
In equilibrium, the centripetal force exerted on the electron is equal to the magnetic force i.e.,
$$
\begin{aligned}
F_{\mathrm{c}} & =F \\
\frac{m v^{2}}{r} & =e v B \sin \theta \\
r & =\frac{m v}{B e \sin \theta} \\
& =\frac{9.1 \times 10^{-31} \times 4.8 \times 10^{6}}{6.5 \times 10^{-4} \times 1.6 \times 10^{-19} \times \sin 90^{\circ}} \\
& =4.2 \times 10^{-2} \mathrm{~m}=4.2 \mathrm{~cm}
\end{aligned}
$$
Hence, the radius of the circular orbit of the electron is 4.2 cm.
:::

:::answer
**Answer:** $4.2\ \mathrm{cm}$
:::

:::

:::question{number="4.12" kind="exercise" id="q_4.12" topic="Frequency of revolution of an orbiting electron"}
#### Question 4.12

:::prompt
In Exercise 4.11 obtain the frequency of revolution of the electron in its circular orbit. Does the answer depend on the speed of the electron? Explain.
:::

:::solution{label="Solution"}
Magnetic field strength, $B=6.5 \times 10^{-4} \mathrm{~T}$
Charge of the electron, $e=1.6 \times 10^{-19} \mathrm{C}$
Mass of the electron, $m_{e}=9.1 \times 10^{-31} \mathrm{~kg}$
Velocity of the electron, $v=4.8 \times 10^{6} \mathrm{~m} / \mathrm{s}$
Radius of the orbit, $r=4.2 \mathrm{~cm}=0.042 \mathrm{~m}$
Frequency of revolution of the electron $=v$
Angular frequency of the electron $=\omega=2 \pi \nu$
Velocity of the electron is related to the angular frequency as:
$$
v=r \omega
$$
In the circular orbit, the magnetic force on the electron is balanced by the centripetal force. Hence, we can write:
$$
\begin{aligned}
& e v B=\frac{m v^{2}}{r} \\
& e B=\frac{m}{r}(r \omega)=\frac{m}{r}(r 2 \pi v) \\
& v=\frac{B e}{2 \pi m}
\end{aligned}
$$
This expression for frequency is independent of the speed of the electron.
On substituting the known values in this expression, we get the frequency as:
$$
\begin{aligned}
v & =\frac{6.5 \times 10^{-4} \times 1.6 \times 10^{-19}}{2 \times 3.14 \times 9.1 \times 10^{-31}} \\
& =18.2 \times 10^{6} \mathrm{~Hz} \\
& \approx 18 \mathrm{MHz}
\end{aligned}
$$
Hence, the frequency of the electron is around 18 MHz and is independent of the speed of the electron.
:::

:::answer
**Answer:** $\approx 18\ \mathrm{MHz}$, independent of speed
:::

:::

:::question{number="4.13" kind="exercise" id="q_4.13" topic="Counter torque on a suspended circular coil"}
#### Question 4.13

:::prompt
(a) A circular coil of 30 turns and radius 8.0 cm carrying a current of 6.0 A is suspended vertically in a uniform horizontal magnetic field of magnitude 1.0 T. The field lines make an angle of 60° with the normal of the coil. Calculate the magnitude of the counter torque that must be applied to prevent the coil from turning.
(b) Would your answer change, if the circular coil in (a) were replaced by a planar coil of some irregular shape that encloses the same area? (All other particulars are also unaltered.)
:::

:::solution{label="Solution"}
Number of turns on the circular coil, $n=30$
Radius of the coil, $r=8.0 \mathrm{~cm}=0.08 \mathrm{~m}$
Area of the coil $=\pi r^{2}=\pi(0.08)^{2}=0.0201 \mathrm{~m}^{2}$
Current flowing in the coil, $I=6.0 \mathrm{~A}$
Magnetic field strength, $B=1 \mathrm{~T}$
Angle between the field lines and normal with the coil surface,
$$
\theta=60^{\circ}
$$
The coil experiences a torque in the magnetic field. Hence, it turns. The counter torque applied to prevent the coil from turning is given by the relation,
$$
\begin{aligned}
& \tau=n I B A \sin \theta \ldots(i) \\
& =30 \times 6 \times 1 \times 0.0201 \times \sin 60^{\circ} \\
& =3.133 \mathrm{~N} \mathrm{~m}
\end{aligned}
$$
It can be inferred from relation (i) that the magnitude of the applied torque is not dependent on the shape of the coil. It depends on the area of the coil. Hence, the answer would not change if the circular coil in the above case is replaced by a planar coil of some irregular shape that encloses the same area.
:::

:::answer
**Answer:** $3.133\ \mathrm{N\,m}$; unchanged for any planar coil of the same area
:::

:::

## Additional Questions

:::question{number="4.14" kind="additional_exercise" id="sol_4.14" topic="Net field from two concentric opposing coils"}
#### Additional Question 4.14

:::prompt
Two concentric circular coils X and Y of radii 16 cm and 10 cm, respectively, lie in the same vertical plane containing the north to south direction. Coil X has 20 turns and carries a current of 16 A; coil Y has 25 turns and carries a current of 18 A. The sense of the current in X is anticlockwise, and clockwise in Y, for an observer looking at the coils facing west. Give the magnitude and direction of the net magnetic field due to the coils at their centre.
:::

:::solution{label="Solution"}
Radius of coil X, $r_{1}=16 \mathrm{~cm}=0.16 \mathrm{~m}$
Radius of coil Y, $r_{2}=10 \mathrm{~cm}=0.1 \mathrm{~m}$
Number of turns of on coil X, $n_{1}=20$
Number of turns of on coil Y, $n_{2}=25$
Current in coil X, $I_{1}=16 \mathrm{~A}$
Current in coil Y, $I_{2}=18 \mathrm{~A}$
Magnetic field due to coil X at their centre is given by the relation,
$$
B_{1}=\frac{\mu_{0} n_{1} I_{1}}{2 r_{1}}
$$
Where,
$$
\mu_{0}=\text { Permeability of free space }=4 \pi \times 10^{-7} \mathrm{TmA}^{-1}
$$
$$
\begin{aligned}
\therefore B_{1} & =\frac{4 \pi \times 10^{-7} \times 20 \times 16}{2 \times 0.16} \\
& =4 \pi \times 10^{-4} \mathrm{~T}(\text { towards East })
\end{aligned}
$$
Magnetic field due to coil Y at their centre is given by the relation,
$$
\begin{aligned}
B_{2} & =\frac{\mu_{0} n_{2} I_{2}}{2 r_{2}} \\
& =\frac{4 \pi \times 10^{-7} \times 25 \times 18}{2 \times 0.10} \\
& =9 \pi \times 10^{-4} \mathrm{~T} \text { (towards West) }
\end{aligned}
$$
Hence, net magnetic field can be obtained as:
$$
\begin{aligned}
B & =B_{2}-B_{1} \\
& =9 \pi \times 10^{-4}-4 \pi \times 10^{-4} \\
& =5 \pi \times 10^{-4} \mathrm{~T} \\
& =1.57 \times 10^{-3} \mathrm{~T} \text { (towards West) }
\end{aligned}
$$
:::

:::answer
**Answer:** $1.57 \times 10^{-3}\ \mathrm{T}$, towards West
:::

:::

:::question{number="4.15" kind="additional_exercise" id="sol_4.15" topic="Designing a solenoid for a target field"}
#### Additional Question 4.15

:::prompt
A magnetic field of $100 \mathrm{G}\left(1 \mathrm{G}=10^{-4} \mathrm{~T}\right)$ is required which is uniform in a region of linear dimension about 10 cm and area of cross-section about $10^{-3} \mathrm{~m}^{2}$. The maximum current-carrying capacity of a given coil of wire is 15 A and the number of turns per unit length that can be wound round a core is at most 1000 turns $\mathrm{m}^{-1}$. Suggest some appropriate design particulars of a solenoid for the required purpose. Assume the core is not ferromagnetic
:::

:::solution{label="Solution"}
Magnetic field strength, $B=100 \mathrm{G}=100 \times 10^{-4} \mathrm{~T}$
Number of turns per unit length, $n=1000$ turns $\mathrm{m}^{-1}$
Current flowing in the coil, $I=15 \mathrm{~A}$
Permeability of free space, $\mu_{0}=4 \pi \times 10^{-7} \mathrm{TmA}^{-1}$
Magnetic field is given by the relation,
$$
B=\mu_{0} n I
$$
$$
\begin{aligned}
& \therefore n I=\frac{B}{\mu_{0}} \\
& \quad=\frac{100 \times 10^{-4}}{4 \pi \times 10^{-7}}=7957.74 \\
& \approx 8000 \mathrm{~A} / \mathrm{m}
\end{aligned}
$$
If the length of the coil is taken as 50 cm, radius 4 cm, number of turns 400, and current 10 A, then these values are not unique for the given purpose. There is always a possibility of some adjustments with limits.
:::

:::answer
**Answer:** e.g. length 50 cm, radius 4 cm, 400 turns, current 10 A (not a unique solution)
:::

:::

:::question{number="4.16" kind="additional_exercise" id="sol_4.16" topic="Field on the axis of Helmholtz coils"}
#### Additional Question 4.16

:::prompt
For a circular coil of radius $R$ and $N$ turns carrying current $I$, the magnitude of the magnetic field at a point on its axis at a distance $x$ from its centre is given by,
$$
B=\frac{\mu_{0} I R^{2} N}{2\left(x^{2}+R^{2}\right)^{\frac{3}{2}}}
$$
Show that this reduces to the familiar result for field at the centre of the coil.
Consider two parallel co-axial circular coils of equal radius $R$, and number of turns $N$, carrying equal currents in the same direction, and separated by a distance $R$. Show that the field on the axis around the mid-point between the coils is uniform over a distance that is small as compared to $R$, and is given by,
$$
B=0.72-\frac{\mu_{0} B N I}{R}, \text { approximately. }
$$
[Such an arrangement to produce a nearly uniform magnetic field over a small region is known as Helmholtz coils.]
:::

:::solution{label="Solution"}
Radius of circular coil $=R$
Number of turns on the coil $=N$
Current in the coil $=I$
Magnetic field at a point on its axis at distance $x$ is given by the relation,
$$
B=\frac{\mu_{0} I R^{2} N}{2\left(x^{2}+R^{2}\right)^{\frac{3}{2}}}
$$
Where,
$$
\mu_{0}=\text { Permeability of free space }
$$
If the magnetic field at the centre of the coil is considered, then $x=0$.
$$
\therefore B=\frac{\mu_{0} I R^{2} N}{2 R^{3}}=\frac{\mu_{0} I N}{2 R}
$$
This is the familiar result for magnetic field at the centre of the coil.
Radii of two parallel co-axial circular coils $=R$
Number of turns on each coil $=N$
Current in both coils $=I$
Distance between both the coils $=R$
Let us consider point Q at distance $d$ from the centre.
Then, one coil is at a distance of ${ }^{\frac{R}{2}+d}$ from point Q.
∴ Magnetic field at point Q is given as:
$$
B_{1}=\frac{\mu_{0} N I R^{2}}{2\left[\left(\frac{R}{2}+d\right)^{2}+R^{2}\right]^{\frac{3}{2}}}
$$
Also, the other coil is at a distance of $2^{\frac{R}{2}-d}$ from point Q.
∴ Magnetic field due to this coil is given as:
$$
B_{2}=\frac{\mu_{0} N I R^{2}}{2\left[\left(\frac{R}{2}-d\right)^{2}+R^{2}\right]^{\frac{3}{2}}}
$$
Total magnetic field,
$$
\begin{aligned}
B & =B_{1}+B_{2} \\
& =\frac{\mu_{0} I R^{2}}{2}\left[\left\{\left(\frac{R}{2}-d\right)^{2}+R^{2}\right\}^{-\frac{3}{2}}+\left\{\left(\frac{R}{2}+d\right)^{2}+R^{2}\right\}^{-\frac{3}{2}}\right] \\
& =\frac{\mu_{0} I R^{2}}{2}\left[\left(\frac{5 R^{2}}{4}+d^{2}-R d\right)^{-\frac{3}{2}}+\left(\frac{5 R^{2}}{4}+d^{2}+R d\right)^{-\frac{3}{2}}\right] \\
& =\frac{\mu_{0} I R^{2}}{2} \times\left(\frac{5 R^{2}}{4}\right)^{-\frac{3}{2}}\left[\left(1+\frac{4}{5} \frac{d^{2}}{R^{2}}-\frac{4}{5} \frac{d}{R}\right)^{-\frac{3}{2}}+\left(1+\frac{4}{5} \frac{d^{2}}{R^{2}}+\frac{4}{5} \frac{d}{R}\right)^{-\frac{3}{2}}\right]
\end{aligned}
$$
For $d \ll R$, neglecting the factor $\frac{d^{2}}{R^{2}}$, we get:
$$
\begin{aligned}
& \approx \frac{\mu_{0} I R^{2}}{2} \times\left(\frac{5 R^{2}}{4}\right)^{-\frac{3}{2}} \times\left[\left(1-\frac{4 d}{5 R}\right)^{-\frac{3}{2}}+\left(1+\frac{4 d}{5 R}\right)^{-\frac{3}{2}}\right] \\
& \approx \frac{\mu_{0} I R^{2} N}{2 R^{3}} \times\left(\frac{4}{5}\right)^{\frac{3}{2}}\left[1-\frac{6 d}{5 R}+1+\frac{6 d}{5 R}\right] \\
& B=\left(\frac{4}{5}\right)^{\frac{3}{2}} \frac{\mu_{0} I N}{R}=0.72\left(\frac{\mu_{0} I N}{R}\right)
\end{aligned}
$$
Hence, it is proved that the field on the axis around the mid-point between the coils is uniform.
:::

:::answer
**Answer:** $B \approx 0.72\left(\mu_0 I N / R\right)$
:::

:::

:::question{number="4.17" kind="additional_exercise" id="sol_4.17" topic="Magnetic field inside and outside a toroid"}
#### Additional Question 4.17

:::prompt
A toroid has a core (non-ferromagnetic) of inner radius 25 cm and outer radius 26 cm, around which 3500 turns of a wire are wound. If the current in the wire is 11 A, what is the magnetic field (a) outside the toroid, (b) inside the core of the toroid, and (c) in the empty space surrounded by the toroid.
:::

:::solution{label="Solution"}
Inner radius of the toroid, $r_{1}=25 \mathrm{~cm}=0.25 \mathrm{~m}$
Outer radius of the toroid, $r_{2}=26 \mathrm{~cm}=0.26 \mathrm{~m}$
Number of turns on the coil, $N=3500$
Current in the coil, $I=11 \mathrm{~A}$
Magnetic field outside a toroid is zero. It is non-zero only inside the core of a toroid.
Magnetic field inside the core of a toroid is given by the relation,
$$
B=\frac{\mu_{0} N I}{l}
$$
Where,
$$
\mu_{0}=\text { Permeability of free space }=4 \pi \times 10^{-7} \mathrm{TmA}^{-1}
$$
$l=$ length of toroid
$$
\begin{aligned}
& =2 \pi\left[\frac{r_{1}+r_{2}}{2}\right] \\
& =\pi(0.25+0.26) \\
& =0.51 \pi \\
& \therefore B=\frac{4 \pi \times 10^{-7} \times 3500 \times 11}{0.51 \pi} \\
& \approx 3.0 \times 10^{-2} \mathrm{~T}
\end{aligned}
$$
Magnetic field in the empty space surrounded by the toroid is zero.
:::

:::answer
**Answer:** outside zero; inside core $\approx 3.0 \times 10^{-2}\ \mathrm{T}$; empty space enclosed zero
:::

:::

:::question{number="4.18" kind="additional_exercise" id="sol_4.18" topic="Conceptual questions on charged particles in fields"}
#### Additional Question 4.18

:::prompt
Answer the following questions:
A magnetic field that varies in magnitude from point to point but has a constant direction (east to west) is set up in a chamber. A charged particle enters the chamber and travels undeflected along a straight path with constant speed. What can you say about the initial velocity of the particle?
A charged particle enters an environment of a strong and non-uniform magnetic field varying from point to point both in magnitude and direction, and comes out of it following a complicated trajectory. Would its final speed equal the initial speed if it suffered no collisions with the environment?
An electron travelling west to east enters a chamber having a uniform electrostatic field in north to south direction. Specify the direction in which a uniform magnetic field should be set up to prevent the electron from deflecting from its straight line path.
:::

:::solution{label="Solution"}
The initial velocity of the particle is either parallel or anti-parallel to the magnetic field. Hence, it travels along a straight path without suffering any deflection in the field.
Yes, the final speed of the charged particle will be equal to its initial speed. This is because magnetic force can change the direction of velocity, but not its magnitude.
An electron travelling from West to East enters a chamber having a uniform electrostatic field in the North-South direction. This moving electron can remain undeflected if the electric force acting on it is equal and opposite of magnetic field. Magnetic force is directed towards the South. According to Fleming's left hand rule, magnetic field should be applied in a vertically downward direction.
:::

:::answer
**Answer:** initial velocity parallel/anti-parallel to B; final speed = initial speed; magnetic field applied vertically downward
:::

:::

:::question{number="4.19" kind="additional_exercise" id="sol_4.19" topic="Trajectory of an accelerated electron in a field"}
#### Additional Question 4.19

:::prompt
An electron emitted by a heated cathode and accelerated through a potential difference of 2.0 kV, enters a region with uniform magnetic field of 0.15 T. Determine the trajectory of the electron if the field (a) is transverse to its initial velocity, (b) makes an angle of $30^{\circ}$ with the initial velocity.
:::

:::solution{label="Solution"}
Magnetic field strength, $B=0.15 \mathrm{~T}$
Charge on the electron, $e=1.6 \times 10^{-19} \mathrm{C}$
Mass of the electron, $m=9.1 \times 10^{-31} \mathrm{~kg}$
Potential difference, $V=2.0 \mathrm{kV}=2 \times 10^{3} \mathrm{~V}$
Thus, kinetic energy of the electron $=e V$
$$
\begin{aligned}
& \Rightarrow e V=\frac{1}{2} m v^{2} \\
& v=\sqrt{\frac{2 e V}{m}}
\end{aligned}
$$
Where,
$$
v=\text { velocity of the electron }
$$
Magnetic force on the electron provides the required centripetal force of the electron. Hence, the electron traces a circular path of radius $r$.
Magnetic force on the electron is given by the relation,
$$
\text { Magnetic force } = B e v
$$
$$
\text { Centripetal force }=\frac{m v^{2}}{r}
$$
$$
\begin{aligned}
& \therefore B e v=\frac{m v^{2}}{r} \\
& r=\frac{m v}{B e}
\end{aligned}
$$
From equations (1) and (2), we get
$$
\begin{aligned}
r & =\frac{m}{B e}\left[\frac{2 e V}{m}\right]^{\frac{1}{2}} \\
& =\frac{9.1 \times 10^{-31}}{0.15 \times 1.6 \times 10^{-19}} \times\left(\frac{2 \times 1.6 \times 10^{-19} \times 2 \times 10^{3}}{9.1 \times 10^{-31}}\right)^{\frac{1}{2}} \\
& =100.55 \times 10^{-5} \\
& =1.01 \times 10^{-3} \mathrm{~m} \\
& =1 \mathrm{~mm}
\end{aligned}
$$
Hence, the electron has a circular trajectory of radius 1.0 mm normal to the magnetic field.
When the field makes an angle $\theta$ of 30° with initial velocity, the initial velocity will be,
$$
v_{1}=v \sin \theta
$$
From equation (2), we can write the expression for new radius as:
$$
\begin{aligned}
r_{1 .} & =\frac{m v_{1}}{B e} \\
& =\frac{m v \sin \theta}{B e} \\
& =\frac{9.1 \times 10^{-31}}{0.15 \times 1.6 \times 10^{-19}} \times\left[\frac{2 \times 1.6 \times 10^{-19} \times 2 \times 10^{3}}{9 \times 10^{-31}}\right]^{\frac{1}{2}} \times \sin 30^{\circ} \\
& =0.5 \times 10^{-3} \mathrm{~m} \\
& =0.5 \mathrm{~mm}
\end{aligned}
$$
Hence, the electron has a helical trajectory of radius 0.5 mm along the magnetic field direction.
:::

:::answer
**Answer:** (a) circular, radius 1.0 mm; (b) helical, radius 0.5 mm
:::

:::

:::question{number="4.20" kind="additional_exercise" id="sol_4.20" topic="Identifying a charged particle from field balance"}
#### Additional Question 4.20

:::prompt
A magnetic field set up using Helmholtz coils (described in Exercise 4.16) is uniform in a small region and has a magnitude of 0.75 T. In the same region, a uniform electrostatic field is maintained in a direction normal to the common axis of the coils. A narrow beam of (single species) charged particles all accelerated through 15 kV enters this region in a direction perpendicular to both the axis of the coils and the electrostatic field. If the beam remains undeflected when the electrostatic field is $9.0 \times 10^{-5} \mathrm{~V} \mathrm{~m}^{-1}$, make a simple guess as to what the beam contains. Why is the answer not unique?
:::

:::solution{label="Solution"}
Magnetic field, $B=0.75 \mathrm{~T}$
Accelerating voltage, $V=15 \mathrm{kV}=15 \times 10^{3} \mathrm{~V}$
Electrostatic field, $E=9 \times 10^{5} \mathrm{~V} \mathrm{~m}^{-1}$
Mass of the electron $=m$
Charge of the electron $=e$
Velocity of the electron $=v$
Kinetic energy of the electron $=e V$
$$
\begin{aligned}
& \Rightarrow \frac{1}{2} m v^{2}=e V \\
& \therefore \frac{e}{m}=\frac{v^{2}}{2 V}
\end{aligned}
$$
Since the particle remains undeflected by electric and magnetic fields, we can infer that the electric field is balancing the magnetic field.
$$
\begin{aligned}
& \therefore e E=e v B \\
& v=\frac{E}{B}
\end{aligned}
$$
Putting equation (2) in equation (1), we get
$$
\begin{aligned}
\frac{e}{m} & =\frac{1}{2} \frac{\left(\frac{E}{B}\right)^{2}}{V}=\frac{E^{2}}{2 V B^{2}} \\
& =\frac{\left(9.0 \times 10^{5}\right)^{2}}{2 \times 15000 \times(0.75)^{2}}=4.8 \times 10^{7} \mathrm{C} / \mathrm{kg}
\end{aligned}
$$
This value of specific charge $e / m$ is equal to the value of deuteron or deuterium ions. This is not a unique answer. Other possible answers are $\mathrm{He}^{++} \mathrm{Li}^{++}$, etc.
:::

:::answer
**Answer:** $e/m = 4.8 \times 10^{7}\ \mathrm{C/kg}$; consistent with a deuteron (also $\mathrm{He}^{++}$, $\mathrm{Li}^{++}$, etc. - not unique)
:::

:::

:::question{number="4.21" kind="additional_exercise" id="sol_4.21" topic="Magnetic field balancing a suspended rod's weight"}
#### Additional Question 4.21

:::prompt
A straight horizontal conducting rod of length 0.45 m and mass 60 g is suspended by two vertical wires at its ends. A current of 5.0 A is set up in the rod through the wires.
What magnetic field should be set up normal to the conductor in order that the tension in the wires is zero?
What will be the total tension in the wires if the direction of current is reversed keeping the magnetic field same as before? (Ignore the mass of the wires.) $\mathrm{g}=9.8 \mathrm{~m} \mathrm{~s}^{-2}$.
:::

:::solution{label="Solution"}
Length of the rod, $l=0.45 \mathrm{~m}$
Mass suspended by the wires, $m=60 \mathrm{~g}=60 \times 10^{-3} \mathrm{~kg}$
Acceleration due to gravity, $\mathrm{g}=9.8 \mathrm{~m} / \mathrm{s}^{2}$
Current in the rod flowing through the wire, $I=5 \mathrm{~A}$
Magnetic field $(B)$ is equal and opposite to the weight of the wire i.e.,
$$
\begin{aligned}
B I l & =m \mathrm{~g} \\
\therefore B & =\frac{m \mathrm{~g}}{l l} \\
& =\frac{60 \times 10^{-3} \times 9.8}{5 \times 0.45}=0.26 \mathrm{~T}
\end{aligned}
$$
A horizontal magnetic field of 0.26 T normal to the length of the conductor should be set up in order to get zero tension in the wire. The magnetic field should be such that Fleming's left hand rule gives an upward magnetic force.
If the direction of the current is revered, then the force due to magnetic field and the weight of the wire acts in a vertically downward direction.
∴ Total tension in the wire $=B I l+m \mathrm{~g}$
$$
\begin{aligned}
& =0.26 \times 5 \times 0.45+\left(60 \times 10^{-3}\right) \times 9.8 \\
& =1.176 \mathrm{~N}
\end{aligned}
$$
:::

:::answer
**Answer:** $B = 0.26\ \mathrm{T}$; total tension after reversing current $= 1.176\ \mathrm{N}$
:::

:::

:::question{number="4.22" kind="additional_exercise" id="sol_4.22" topic="Force per unit length between starter-motor wires"}
#### Additional Question 4.22

:::prompt
The wires which connect the battery of an automobile to its starting motor carry a current of 300 A (for a short time). What is the force per unit length between the wires if they are 70 cm long and 1.5 cm apart? Is the force attractive or repulsive?
:::

:::solution{label="Solution"}
Current in both wires, $I=300 \mathrm{~A}$
Distance between the wires, $r=1.5 \mathrm{~cm}=0.015 \mathrm{~m}$
Length of the two wires, $l=70 \mathrm{~cm}=0.7 \mathrm{~m}$
Force between the two wires is given by the relation,
$$
F=\frac{\mu_{0} I^{2}}{2 \pi r}
$$
Where,
$$
\mu_{0}=\text { Permeability of free space }=4 \pi \times 10^{-7} \mathrm{TmA}^{-1}
$$
$$
\begin{aligned}
\therefore F & =\frac{4 \pi \times 10^{-7} \times(300)^{2}}{2 \pi \times 0.015} \\
& =1.2 \mathrm{~N} / \mathrm{m}
\end{aligned}
$$
Since the direction of the current in the wires is opposite, a repulsive force exists between them.
:::

:::answer
**Answer:** $1.2\ \mathrm{N/m}$, repulsive
:::

:::

:::question{number="4.23" kind="additional_exercise" id="sol_4.23" topic="Force on a wire through a cylindrical field"}
#### Additional Question 4.23

:::prompt
A uniform magnetic field of 1.5 T exists in a cylindrical region of radius 10.0 cm, its direction parallel to the axis along east to west. A wire carrying current of 7.0 A in the north to south direction passes through this region. What is the magnitude and direction of the force on the wire if,
the wire intersects the axis,
the wire is turned from N-S to northeast-northwest direction,
the wire in the N-S direction is lowered from the axis by a distance of 6.0 cm?
:::

:::solution{label="Solution"}
Magnetic field strength, $B=1.5 \mathrm{~T}$
Radius of the cylindrical region, $r=10 \mathrm{~cm}=0.1 \mathrm{~m}$
Current in the wire passing through the cylindrical region, $I=7 \mathrm{~A}$
If the wire intersects the axis, then the length of the wire is the diameter of the cylindrical region.
Thus, $l=2 r=0.2 \mathrm{~m}$
Angle between magnetic field and current, $\theta=90^{\circ}$
Magnetic force acting on the wire is given by the relation,
$$
\begin{aligned}
& F=B I l \sin \theta \\
& =1.5 \times 7 \times 0.2 \times \sin 90^{\circ} \\
& =2.1 \mathrm{~N}
\end{aligned}
$$
Hence, a force of 2.1 N acts on the wire in a vertically downward direction.
New length of the wire after turning it to the Northeast-Northwest direction can be given as::
$$
l_{1}=\frac{l}{\sin \theta}
$$
Angle between magnetic field and current, $\theta=45^{\circ}$
Force on the wire,
$$
\begin{aligned}
F & =B I l_{1} \sin \theta \\
& =B I l \\
& =1.5 \times 7 \times 0.2 \\
& =2.1 \mathrm{~N}
\end{aligned}
$$
Hence, a force of 2.1 N acts vertically downward on the wire. This is independent of angle $\theta$ because $l \sin \theta$ is fixed.
The wire is lowered from the axis by distance, $d=6.0 \mathrm{~cm}$
Let $l_{2}$ be the new length of the wire.
$$
\begin{aligned}
& \therefore\left(\frac{l_{2}}{2}\right)^{2}=4(d+r) \\
& \quad=4(10+6)=4(16) \\
& \therefore l_{2}=8 \times 2=16 \mathrm{~cm}=0.16 \mathrm{~m}
\end{aligned}
$$
Magnetic force exerted on the wire,
$$
\begin{aligned}
F_{2} & =B I l_{2} \\
& =1.5 \times 7 \times 0.16 \\
& =1.68 \mathrm{~N}
\end{aligned}
$$
Hence, a force of 1.68 N acts in a vertically downward direction on the wire.
:::

:::answer
**Answer:** 2.1 N (intersects axis); 2.1 N (turned NE-NW, unchanged); 1.68 N (lowered 6 cm)
:::

:::

:::question{number="4.24" kind="additional_exercise" id="sol_4.24" topic="Torque and equilibrium of a rectangular loop"}
#### Additional Question 4.24

:::prompt
A uniform magnetic field of 3000 G is established along the positive $z$-direction. A rectangular loop of sides 10 cm and 5 cm carries a current of 12 A. What is the torque on the loop in the different cases shown in Fig. 4.28? What is the force on each case? Which case corresponds to stable equilibrium?
:::

:::figure{src="images/fig_physics-12-4_25.jpg" id="fig_physics-12-4_25"}
(a)
:::

:::figure{src="images/fig_physics-12-4_26.jpg" id="fig_physics-12-4_26"}
(b)
:::

:::figure{src="images/fig_physics-12-4_27.jpg" id="fig_physics-12-4_27"}
(c)
:::

:::figure{src="images/fig_physics-12-4_28.jpg" id="fig_physics-12-4_28"}
(d)
:::

:::figure{src="images/fig_physics-12-4_29.jpg" id="fig_physics-12-4_29"}
(e)
:::

:::figure{src="images/fig_physics-12-4_30.jpg" id="fig_physics-12-4_30"}
(f)
:::

:::solution{label="Solution"}
Magnetic field strength, $B=3000 \mathrm{G}=3000 \times 10^{-4} \mathrm{~T}=0.3 \mathrm{~T}$
Length of the rectangular loop, $l=10 \mathrm{~cm}$
Width of the rectangular loop, $b=5 \mathrm{~cm}$
Area of the loop,
$$
A=l \times b=10 \times 5=50 \mathrm{~cm}^{2}=50 \times 10^{-4} \mathrm{~m}^{2}
$$
Current in the loop, $I=12 \mathrm{~A}$
Now, taking the anti-clockwise direction of the current as positive and vise-versa:
Torque, $\vec{\tau}=I \vec{A} \times \vec{B}$
From the given figure, it can be observed that $A$ is normal to the $y-z$ plane and $B$ is directed along the $z$-axis.
$$
\begin{aligned}
\therefore \tau & =12 \times\left(50 \times 10^{-4}\right) \hat{i} \times 0.3 \hat{k} \\
& =-1.8 \times 10^{-2} \hat{j} \mathrm{~N} \mathrm{~m}
\end{aligned}
$$
The torque is $1.8 \times 10^{-2} \mathrm{~N} \mathrm{~m}$ along the negative $y$-direction. The force on the loop is zero because the angle between $A$ and $B$ is zero.
This case is similar to case (a). Hence, the answer is the same as (a).
Torque $\tau=I \vec{A} \times \vec{B}$
From the given figure, it can be observed that $A$ is normal to the $x-z$ plane and $B$ is directed along the $z$-axis.
$$
\begin{aligned}
\therefore \tau & =-12 \times\left(50 \times 10^{-4}\right) \hat{j} \times 0.3 \hat{k} \\
& =-1.8 \times 10^{-2} \hat{i} \mathrm{~N} \mathrm{~m}
\end{aligned}
$$
The torque is $1.8 \times 10^{-2} \mathrm{~N} \mathrm{~m}$ along the negative $x$ direction and the force is zero.
Magnitude of torque is given as:
$$
\begin{aligned}
|\tau| & =I A B \\
& =12 \times 50 \times 10^{-4} \times 0.3 \\
& =1.8 \times 10^{-2} \mathrm{~N} \mathrm{~m}
\end{aligned}
$$
Torque is $1.8 \times 10^{-2} \mathrm{~N} \mathrm{~m}$ at an angle of 240° with positive $x$ direction. The force is zero.
Torque $\tau=I \vec{A} \times \vec{B}$
$$
\begin{aligned}
& =\left(50 \times 10^{-4} \times 12\right) \hat{k} \times 0.3 \hat{k} \\
& =0
\end{aligned}
$$
Hence, the torque is zero. The force is also zero.
Torque $\tau=I \vec{A} \times \vec{B}$
$$
\begin{aligned}
& =\left(50 \times 10^{-4} \times 12\right) \hat{k} \times 0.3 \hat{k} \\
& =0
\end{aligned}
$$
Hence, the torque is zero. The force is also zero.
In case (e), the direction of $I \vec{A}$ and $\vec{B}$ is the same and the angle between them is zero. If displaced, they come back to an equilibrium. Hence, its equilibrium is stable.
Whereas, in case (f), the direction of $I \vec{A}$ and $\vec{B}$ is opposite. The angle between them is $180^{\circ}$. If disturbed, it does not come back to its original position. Hence, its equilibrium is unstable.
:::

:::answer
**Answer:** torques $1.8 \times 10^{-2}$ N m (cases a,b,c), zero (cases d,e,f); force zero in all cases; case (e) is stable equilibrium
:::

:::

:::question{number="4.25" kind="additional_exercise" id="sol_4.25" topic="Torque, force and per-electron force on a coil"}
#### Additional Question 4.25

:::prompt
A circular coil of 20 turns and radius 10 cm is placed in a uniform magnetic field of 0.10 T normal to the plane of the coil. If the current in the coil is 5.0 A, what is the
total torque on the coil,
total force on the coil,
average force on each electron in the coil due to the magnetic field?
(The coil is made of copper wire of cross-sectional area $10^{-5} \mathrm{~m}^{2}$, and the free electron density in copper is given to be about $10^{29} \mathrm{~m}^{-3}$.)
:::

:::solution{label="Solution"}
Number of turns on the circular coil, $n=20$
Radius of the coil, $r=10 \mathrm{~cm}=0.1 \mathrm{~m}$
Magnetic field strength, $B=0.10 \mathrm{~T}$
Current in the coil, $I=5.0 \mathrm{~A}$
The total torque on the coil is zero because the field is uniform.
The total force on the coil is zero because the field is uniform.
Cross-sectional area of copper coil, $A=10^{-5} \mathrm{~m}^{2}$
Number of free electrons per cubic meter in copper, $N=10^{29} / \mathrm{m}^{3}$
Charge on the electron, $e=1.6 \times 10^{-19} \mathrm{C}$
Magnetic force, $F=B e v_{d}$
Where,
$$
\begin{aligned}
v_{d} & =\text { Drift velocity of electrons } \\
& =\frac{I}{N e A} \\
\therefore F & =\frac{B e I}{N e A} \\
& =\frac{0.10 \times 5.0}{10^{29} \times 10^{-5}}=5 \times 10^{-25} \mathrm{~N}
\end{aligned}
$$
Hence, the average force on each electron is $5 \times 10^{-25} \mathrm{~N}$.
:::

:::answer
**Answer:** total torque zero; total force zero; force on each electron $5 \times 10^{-25}\ \mathrm{N}$
:::

:::

:::question{number="4.26" kind="additional_exercise" id="sol_4.26" topic="Solenoid current needed to support a wire's weight"}
#### Additional Question 4.26

:::prompt
A solenoid 60 cm long and of radius 4.0 cm has 3 layers of windings of 300 turns each. A 2.0 cm long wire of mass 2.5 g lies inside the solenoid (near its centre) normal to its axis; both the wire and the axis of the solenoid are in the horizontal plane. The wire is connected through two leads parallel to the axis of the solenoid to an external battery which supplies a current of 6.0 A in the wire. What value of current (with appropriate sense of circulation) in the windings of the solenoid can support the weight of the wire? $g$ $=9.8 \mathrm{~m} \mathrm{~s}^{-2}$
:::

:::solution{label="Solution"}
Length of the solenoid, $L=60 \mathrm{~cm}=0.6 \mathrm{~m}$
Radius of the solenoid, $r=4.0 \mathrm{~cm}=0.04 \mathrm{~m}$
It is given that there are 3 layers of windings of 300 turns each.
∴ Total number of turns, $n=3 \times 300=900$
Length of the wire, $l=2 \mathrm{~cm}=0.02 \mathrm{~m}$
Mass of the wire, $m=2.5 \mathrm{~g}=2.5 \times 10^{-3} \mathrm{~kg}$
Current flowing through the wire, $i=6 \mathrm{~A}$
Acceleration due to gravity, $\mathrm{g}=9.8 \mathrm{~m} / \mathrm{s}^{2}$
Magnetic field produced inside the solenoid, $B=\frac{\mu_{0} n I}{L}$
Where,
$$
\mu_{0}=\text { Permeability of free space }=4 \pi \times 10^{-7} \mathrm{TmA}^{-1}
$$
$I=$ Current flowing through the windings of the solenoid
Magnetic force is given by the relation,
$$
\begin{aligned}
F & =B i l \\
& =\frac{\mu_{0} n I}{L} i l
\end{aligned}
$$
Also, the force on the wire is equal to the weight of the wire.
$$
\begin{aligned}
\therefore m \mathrm{~g} & =\frac{\mu_{0} n I i l}{L} \\
I & =\frac{m \mathrm{~g} L}{\mu_{0} n i l} \\
& =\frac{2.5 \times 10^{-3} \times 9.8 \times 0.6}{4 \pi \times 10^{-7} \times 900 \times 0.02 \times 6}=108 \mathrm{~A}
\end{aligned}
$$
Hence, the current flowing through the solenoid is 108 A.
:::

:::answer
**Answer:** $108\ \mathrm{A}$
:::

:::

:::question{number="4.27" kind="additional_exercise" id="sol_4.27" topic="Converting a galvanometer into a voltmeter"}
#### Additional Question 4.27

:::prompt
A galvanometer coil has a resistance of $12 \Omega$ and the metre shows full scale deflection for a current of 3 mA. How will you convert the metre into a voltmeter of range 0 to 18 V?
:::

:::solution{label="Solution"}
Resistance of the galvanometer coil, $G=12 \Omega$
Current for which there is full scale deflection, ${ }^{I} \mathrm{~g}=3 \mathrm{~mA}=3 \times 10^{-3} \mathrm{~A}$
Range of the voltmeter is 0, which needs to be converted to 18 V.
$$
\therefore V=18 \mathrm{~V}
$$
Let a resistor of resistance $R$ be connected in series with the galvanometer to convert it into a voltmeter. This resistance is given as:
$$
\begin{aligned}
R & =\frac{V}{I_{\mathrm{g}}}-\mathrm{G} \\
& =\frac{18}{3 \times 10^{-3}}-12=6000-12=5988 \Omega
\end{aligned}
$$
Hence, a resistor of resistance $5988 \Omega$ is to be connected in series with the galvanometer.
:::

:::answer
**Answer:** $5988\ \Omega$ in series
:::

:::

:::question{number="4.28" kind="additional_exercise" id="sol_4.28" topic="Converting a galvanometer into an ammeter"}
#### Additional Question 4.28

:::prompt
A galvanometer coil has a resistance of $15 \Omega$ and the metre shows full scale deflection for a current of 4 mA. How will you convert the metre into an ammeter of range 0 to 6 A?
:::

:::solution{label="Solution"}
Resistance of the galvanometer coil, $G=15 \Omega$
Current for which the galvanometer shows full scale deflection,
$$
I_{\mathrm{g}}=4 \mathrm{~mA}=4 \times 10^{-3} \mathrm{~A}
$$
Range of the ammeter is 0, which needs to be converted to 6 A.
$$
\text { ∴ Current, } I=6 \mathrm{~A}
$$
A shunt resistor of resistance $S$ is to be connected in parallel with the galvanometer to convert it into an ammeter. The value of $S$ is given as:
$$
\begin{aligned}
S & =\frac{I_{g} G}{I-I_{g}} \\
& =\frac{4 \times 10^{-3} \times 15}{6-4 \times 10^{-3}} \\
S & =\frac{6 \times 10^{-2}}{6-0.004}=\frac{0.06}{5.996} \\
\approx & 0.01 \Omega=10 \mathrm{~m} \Omega
\end{aligned}
$$
Hence, a $10 \mathrm{~m} \Omega$ shunt resistor is to be connected in parallel with the galvanometer.
:::

:::answer
**Answer:** $10\ \mathrm{m}\Omega$ in parallel
:::

:::
