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

:::figure{src="images/fig_physics-12-4_12.jpg" id="fig_physics-12-4_12"}
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
