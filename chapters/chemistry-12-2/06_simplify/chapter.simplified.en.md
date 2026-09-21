---
subject: chemistry
class: 12
chapter: 2
lang: en
title: "Electrochemistry"
---

# Electrochemistry

## Examples

:::example{number="2.1" kind="example" id="ex_2.1" topic="Cell notation and Nernst equation"}
#### Example 2.1

:::prompt
Represent the cell in which the following reaction takes place $\mathrm{Mg}(\mathrm{s})+2 \mathrm{Ag}^{+}(0.0001 \mathrm{M}) \rightarrow \mathrm{Mg}^{2+}(0.130 \mathrm{M})+2 \mathrm{Ag}(\mathrm{s})$

Calculate its $E_{\text {(cell) }}$ if $E_{\text {(cell) }}^{\circ}=3.17 \mathrm{~V}$.
:::

:::solution{label="Solution"}
The cell can be written as $\mathrm{Mg}\left|\mathrm{Mg}^{2+}(0.130 \mathrm{M})\right|\left|\mathrm{Ag}^{+}(0.0001 \mathrm{M})\right| \mathrm{Ag}$

$$
\begin{aligned}
E_{\text {(cell) }} & =E_{\text {(cell) }}^{\mathrm{o}}-\frac{\mathrm{RT}}{2 \mathrm{~F}} \ln \frac{\mathrm{Mg}^{2+}}{\mathrm{Ag}^{+2}} \\
& =3.17 \mathrm{~V}-\frac{0.059 \mathrm{~V}}{2} \log \frac{0.130}{(0.0001)^{2}}=3.17 \mathrm{~V}-0.21 \mathrm{~V}=2.96 \mathrm{~V}
\end{aligned}
$$
:::

:::answer
**Answer:** $E_{\text {(cell) }} = 2.96 \mathrm{~V}$
:::

:::

:::example{number="2.2" kind="example" id="ex_2.2" topic="Equilibrium constant from standard cell potential"}
#### Example 2.2

:::prompt
Calculate the equilibrium constant of the reaction:

$$
\begin{aligned}
& \mathrm{Cu}(\mathrm{~s})+2 \mathrm{Ag}^{+}(\mathrm{aq}) \rightarrow \mathrm{Cu}^{2+}(\mathrm{aq})+2 \mathrm{Ag}(\mathrm{~s}) \\
& \mathrm{E}_{(\text {cell })}^{\mathrm{o}}=0.46 \mathrm{~V}
\end{aligned}
$$
:::

:::solution{label="Solution"}
$$
\begin{aligned}
E_{\text {(cell) }}^{\circ} & =\frac{0.059 \mathrm{~V}}{2} \log K_{C}=0.46 \mathrm{~V} \text { or } \\
\log \quad K_{C} & =\frac{0.46 \mathrm{~V} \times 2}{0.059 \mathrm{~V}}=15.6 \\
K_{C} & =3.92 \times 10^{15}
\end{aligned}
$$
:::

:::answer
**Answer:** $K_{C} = 3.92 \times 10^{15}$
:::

:::

:::example{number="2.3" kind="example" id="ex_2.3" topic="Standard Gibbs energy from cell potential"}
#### Example 2.3

:::prompt
The standard electrode potential for Daniell cell is 1.1V. Calculate the standard Gibbs energy for the reaction:

$$
\mathrm{Zn}(\mathrm{~s})+\mathrm{Cu}^{2+}(\mathrm{aq}) \longrightarrow \mathrm{Zn}^{2+}(\mathrm{aq})+\mathrm{Cu}(\mathrm{~s})
$$
:::

:::solution{label="Solution"}
$\Delta_{\mathrm{r}} G^{\circ}=-n F \mathrm{E}_{\text {(cell) }}^{\mathrm{o}}$
$n$ in the above equation is $2, \mathrm{~F}=96487 \mathrm{C} \mathrm{mol}^{-1}$ and $\mathrm{E}_{(\text {cell })}^{0}=1.1 \mathrm{~V}$

$$
\text { Therefore, } \begin{aligned}
\Delta_{\mathrm{r}} G^{0} & =-2 \times 1.1 \mathrm{~V} \times 96487 \mathrm{C} \mathrm{~mol}^{-1} \\
& =-21227 \mathrm{~J} \mathrm{~mol}^{-1} \\
& =-212.27 \mathrm{~kJ} \mathrm{~mol}^{-1}
\end{aligned}
$$
:::

:::answer
**Answer:** $\Delta_{\mathrm{r}} G^{0} = -212.27 \mathrm{~kJ} \mathrm{~mol}^{-1}$
:::

:::

:::example{number="2.4" kind="example" id="ex_2.4" topic="Conductivity and molar conductivity from cell constant"}
#### Example 2.4

:::prompt
Resistance of a conductivity cell filled with $0.1 \mathrm{~mol} \mathrm{~L}^{-1} \mathrm{KCl}$ solution is $100 \Omega$. If the resistance of the same cell when filled with $0.02 \mathrm{~mol} \mathrm{~L}^{-1}$ KCl solution is $520 \Omega$, calculate the conductivity and molar conductivity of $0.02 \mathrm{~mol} \mathrm{~L}^{-1} \mathrm{KCl}$ solution. The conductivity of $0.1 \mathrm{~mol} \mathrm{~L}^{-1} \mathrm{KCl}$ solution is 1.29 S/m.
:::

:::solution{label="Solution"}
The cell constant is given by the equation:
Cell constant $=G^{*}=$ conductivity × resistance

$$
=1.29 \mathrm{~S} / \mathrm{m} \times 100 \Omega=129 \mathrm{~m}^{-1}=1.29 \mathrm{~cm}^{-1}
$$

Conductivity of $0.02 \mathrm{~mol} \mathrm{~L}^{-1} \mathrm{KCl}$ solution = cell constant / resistance

$$
=\frac{G^{*}}{R}=\frac{129 \mathrm{~m}^{-1}}{520 \Omega}=0.248 \mathrm{~S} \mathrm{~m}^{-1}
$$

Concentration

$$
\begin{aligned}
& =0.02 \mathrm{~mol} \mathrm{~L}^{-1} \\
& =1000 \times 0.02 \mathrm{~mol} \mathrm{~m}^{-3}=20 \mathrm{~mol} \mathrm{~m}^{-3}
\end{aligned}
$$

Molar conductivity $=\Lambda_{m}=\frac{\kappa}{c}$

$$
=\frac{248 \times 10^{-3} \mathrm{~S} \mathrm{~m}^{-1}}{20 \mathrm{~mol} \mathrm{~m}^{-3}}=124 \times 10^{-4} \mathrm{~S} \mathrm{~m}^{2} \mathrm{~mol}^{-1}
$$

Alternatively,

$$
\kappa=\frac{1.29 \mathrm{~cm}^{-1}}{520 \Omega}=0.248 \times 10^{-2} \mathrm{~S} \mathrm{~cm}^{-1}
$$

and

$$
\begin{aligned}
\Lambda_{m} & =\kappa \times 1000 \mathrm{~cm}^{3} \mathrm{~L}^{-1} \text { molarity }{ }^{-1} \\
& =\frac{0.248 \times 10^{-2} \mathrm{~S} \mathrm{~cm}^{-1} \times 1000 \mathrm{~cm}^{3} \mathrm{~L}^{-1}}{0.02 \mathrm{~mol} \mathrm{~L}^{-1}} \\
& =124 \mathrm{~S} \mathrm{~cm}^{2} \mathrm{~mol}^{-1}
\end{aligned}
$$
:::

:::answer
**Answer:** Conductivity $= 0.248 \times 10^{-2} \mathrm{~S} \mathrm{~cm}^{-1}$ ($=0.248 \mathrm{~S} \mathrm{~m}^{-1}$); Molar conductivity $\Lambda_{m} = 124 \mathrm{~S} \mathrm{~cm}^{2} \mathrm{~mol}^{-1}$
:::

:::

:::example{number="2.5" kind="example" id="ex_2.5" topic="Resistivity, conductivity and molar conductivity of NaOH"}
#### Example 2.5

:::prompt
The electrical resistance of a column of $0.05 \mathrm{~mol} \mathrm{~L}^{-1} \mathrm{NaOH}$ solution of diameter 1 cm and length 50 cm is $5.55 \times 10^{3}$ ohm. Calculate its resistivity, conductivity and molar conductivity.
:::

:::solution{label="Solution"}
$A=\pi r^{2}=3.14 \times 0.5^{2} \mathrm{~cm}^{2}=0.785 \mathrm{~cm}^{2}=0.785 \times 10^{-4} \mathrm{~m}^{2}$ $l=50 \mathrm{~cm}=0.5 \mathrm{~m}$

$$
R=\frac{\rho l}{A} \quad \text { or } \quad \rho=\frac{R A}{l}=\frac{5.55 \times 10^{3} \Omega \times 0.785 \mathrm{~cm}^{2}}{50 \mathrm{~cm}}=87.135 \Omega \mathrm{~cm}
$$

$$
\begin{aligned}
\text { Conductivity }=\kappa & =\frac{1}{\rho}=\left(\frac{1}{87.135}\right) \mathrm{S} \mathrm{~cm}^{-1} \\
& =0.01148 \mathrm{~S} \mathrm{~cm}^{-1}
\end{aligned}
$$

Molar conductivity, $\Lambda_{m}=\frac{\kappa \times 1000}{\mathrm{c}} \mathrm{cm}^{3} \mathrm{~L}^{-1}$

$$
\begin{aligned}
& =\frac{0.01148 \mathrm{~S} \mathrm{~cm}^{-1} \times 1000 \mathrm{~cm}^{3} \mathrm{~L}^{-1}}{0.05 \mathrm{~mol} \mathrm{~L}^{-1}} \\
& =229.6 \mathrm{~S} \mathrm{~cm}^{2} \mathrm{~mol}^{-1}
\end{aligned}
$$

If we want to calculate the values of different quantities in terms of 'm' instead of 'cm',

$$
\begin{aligned}
& \rho=\frac{R A}{l} \\
&=\frac{5.55 \times 10^{3} \Omega \times 0.785 \times 10^{-4} \mathrm{~m}^{2}}{0.5 \mathrm{~m}}=87.135 \times 10^{-2} \Omega \mathrm{~m} \\
& \kappa=\frac{1}{\rho}=\frac{100}{87.135} \Omega \mathrm{~m}=1.148 \mathrm{~S} \mathrm{~m}^{-1} \\
& \text { and } \quad \Lambda_{m}=\frac{\kappa}{c}=\frac{1.148 \mathrm{~S} \mathrm{~m}^{-1}}{50 \mathrm{~mol} \mathrm{~m}^{-3}}=229.6 \times 10^{-4} \mathrm{~S} \mathrm{~m}^{2} \mathrm{~mol}^{-1} .
\end{aligned}
$$
:::

:::answer
**Answer:** Resistivity $\rho = 87.135 \Omega \mathrm{~cm}$; Conductivity $\kappa = 0.01148 \mathrm{~S} \mathrm{~cm}^{-1}$; Molar conductivity $\Lambda_{m} = 229.6 \mathrm{~S} \mathrm{~cm}^{2} \mathrm{~mol}^{-1}$
:::

:::

:::example{number="2.6" kind="example" id="ex_2.6" topic="Limiting molar conductivity of KCl by extrapolation" simplified="True"}
#### Example 2.6

:::prompt
The molar conductivity of KCl solutions at different concentrations at 298 K are given below:

| $\boldsymbol{c} \boldsymbol{/} \mathbf{m o l ~}^{\boldsymbol{-} \mathbf{1}}$ | $\Lambda_{m} / \mathrm{S} \mathbf{~ c m}^{\mathbf{2}} \mathbf{~ m o l}^{\boldsymbol{-} \mathbf{1}}$ |
| :--- | :--- |
| 0.000198 | 148.61 |
| 0.000309 | 148.29 |
| 0.000521 | 147.81 |
| 0.000989 | 147.09 |

Show that a plot between $\Lambda_{m}$ and $c^{1 / 2}$ is a straight line. Determine the values of $\Lambda_{m}^{\circ}$ and A for KCl.
:::

:::solution{label="Solution"}
Taking the square root of concentration, we get:

$$
\begin{array}{cc}
\boldsymbol{c}^{\mathbf{1 / 2}} /\left(\mathbf{m o l ~ L}^{-\mathbf{1}}\right)^{\mathbf{1 / 2}} & \Lambda \boldsymbol{m} / \mathbf{S} \mathbf{c m}^{\mathbf{2}} \mathbf{m o l}^{\mathbf{- 1}} \\
0.01407 & 148.61 \\
0.01758 & 148.29 \\
0.02283 & 147.81 \\
0.03145 & 147.09
\end{array}
$$

A plot of $\Lambda_{m}$ (y-axis) against $\mathrm{c}^{1 / 2}$ ($x$-axis) is shown in (Fig. 3.7). It is nearly a straight line. From the intercept $\left(c^{1 / 2}=0\right)$, we get:

$$
\begin{aligned}
& \Lambda_{m}^{\circ}=150.0 \mathrm{~S} \mathrm{~cm}^{2} \mathrm{~mol}^{-1} \text { and } \\
& A=- \text { slope }=87.46 \mathrm{~S} \mathrm{~cm}^{2} \mathrm{~mol}^{-1} /\left(\mathrm{mol} / \mathrm{L}^{-1}\right)^{1 / 2}
\end{aligned}
$$
:::

:::answer
**Answer:** $\Lambda_{m}^{\circ} = 150.0 \mathrm{~S} \mathrm{~cm}^{2} \mathrm{~mol}^{-1}$; $A = 87.46 \mathrm{~S} \mathrm{~cm}^{2} \mathrm{~mol}^{-1} /\left(\mathrm{mol} / \mathrm{L}^{-1}\right)^{1 / 2}$
:::

:::

:::example{number="2.7" kind="example" id="ex_2.7" topic="Limiting molar conductivity via Kohlrausch's law" corrections_applied="1"}
#### Example 2.7

:::prompt
Calculate $\Lambda_{m}^{0}$ for $\mathrm{CaCl}_{2}$ and $\mathrm{MgSO}_{4}$ from the data given in Table 3.4.
:::

:::solution{label="Solution"}
We know from Kohlrausch law that

$$
\begin{aligned}
\Lambda_{m\left(\mathrm{CaCl}_{2}\right)}^{\mathrm{o}} & =\lambda_{\mathrm{Ca}^{2+}}^{\mathrm{o}}+2 \lambda_{\mathrm{Cl}^{-}}^{\mathrm{o}}=119.0 \mathrm{~S} \mathrm{~cm}^{2} \mathrm{~mol}^{-1}+2(76.3) \mathrm{S} \mathrm{~cm}^{2} \mathrm{~mol}^{-1} \\
& =(119.0+152.6) \mathrm{S} \mathrm{~cm}^{2} \mathrm{~mol}^{-1} \\
& =271.6 \mathrm{~S} \mathrm{~cm}^{2} \mathrm{~mol}^{-1}
\end{aligned}
$$

$$
\begin{aligned}
\Lambda_{m\left(\mathrm{MgSO}_{4}\right)}^{o} & =\lambda_{\mathrm{Mg}^{2+}}^{o}+\lambda_{\mathrm{SO}_{4}^{2-}}^{o}=106.0 \mathrm{~S} \mathrm{~cm}^{2} \mathrm{~mol}^{-1}+160.0 \mathrm{~S} \mathrm{~cm}^{2} \mathrm{~mol}^{-1} \\
& =266 \mathrm{~S} \mathrm{~cm}^{2} \mathrm{~mol}^{-1}
\end{aligned}
$$
:::

:::answer
**Answer:** $\Lambda_{m}^{\circ}(\mathrm{CaCl}_{2}) = 271.6 \mathrm{~S} \mathrm{~cm}^{2} \mathrm{~mol}^{-1}$; $\Lambda_{m}^{\circ}(\mathrm{MgSO}_{4}) = 266 \mathrm{~S} \mathrm{~cm}^{2} \mathrm{~mol}^{-1}$
:::

:::

:::example{number="2.8" kind="example" id="ex_2.8" topic="Limiting molar conductivity of a weak electrolyte via Kohlrausch's law"}
#### Example 2.8

:::prompt
$\Lambda_{m}^{0}$ for NaCl, HCl and NaAc are 126.4, 425.9 and $91.0 \mathrm{~S} \mathrm{~cm}^{2} \mathrm{~mol}^{-1}$ respectively. Calculate $\Lambda^{0}$ for HAc.
:::

:::solution{label="Solution"}
$\Lambda_{m(\mathrm{HAc})}^{\circ}=\lambda_{\mathrm{H}^{+}}^{\circ}+\lambda_{\mathrm{Ac}^{-}}^{\circ}=\lambda_{\mathrm{H}^{+}}^{\circ}+\lambda_{\mathrm{Cl}^{-}}^{\circ}+\lambda_{\mathrm{Ac}^{-}}^{\circ}+\lambda_{\mathrm{Na}^{+}}^{\circ}-\lambda_{\mathrm{Cl}^{-}}^{\circ}-\lambda_{\mathrm{Na}^{+}}^{\circ}$

$$
\begin{aligned}
& =\Lambda_{m(\mathrm{HCl})}^{\mathrm{o}}+\Lambda_{m(\mathrm{NaAc})}^{\mathrm{o}}-\Lambda_{m(\mathrm{NaCl})}^{\mathrm{o}} \\
& =(425.9+91.0-126.4) \mathrm{S} \mathrm{~cm}^{2} \mathrm{~mol}^{-1} \\
& =390.5 \mathrm{~S} \mathrm{~cm}^{2} \mathrm{~mol}^{-1}
\end{aligned}
$$
:::

:::answer
**Answer:** $\Lambda_{m(\mathrm{HAc})}^{\circ} = 390.5 \mathrm{~S} \mathrm{~cm}^{2} \mathrm{~mol}^{-1}$
:::

:::

:::example{number="2.9" kind="example" id="ex_2.9" topic="Dissociation constant of acetic acid from conductivity"}
#### Example 2.9

:::prompt
The conductivity of $0.001028 \mathrm{~mol} \mathrm{~L}^{-1}$ acetic acid is $4.95 \times 10^{-5} \mathrm{~S} \mathrm{~cm}^{-1}$. Calculate its dissociation constant if $\Lambda_{m}^{0}$ for acetic acid is $390.5 \mathrm{~S} \mathrm{~cm}^{2} \mathrm{~mol}^{-1}$.
:::

:::solution{label="Solution"}
$\Lambda_{m}=\frac{\kappa}{c}=\frac{4.95 \times 10^{-5} \mathrm{Scm}^{-1}}{0.001028 \mathrm{~mol} \mathrm{~L}^{-1}} \times \frac{1000 \mathrm{~cm}^{3}}{\mathrm{~L}}=48.15 \mathrm{~S} \mathrm{~cm}^{3} \mathrm{~mol}^{-1}$

$$
\begin{aligned}
& \alpha=\frac{\Lambda_{m}}{\Lambda_{m}^{\mathrm{o}}}=\frac{48.15 \mathrm{Scm}^{2} \mathrm{~mol}^{-1}}{390.5 \mathrm{Scm}^{2} \mathrm{~mol}^{-1}}=0.1233 \\
& \mathrm{k}=\frac{\mathrm{c} \alpha^{2}}{(1-\alpha)}=\frac{0.001028 \mathrm{molL}^{-1} \times(0.1233)^{2}}{1-0.1233}=1.78 \times 10^{-5} \mathrm{~mol} \mathrm{~L}^{-1}
\end{aligned}
$$
:::

:::answer
**Answer:** $\alpha = 0.1233$; $K_{a} = 1.78 \times 10^{-5} \mathrm{~mol} \mathrm{~L}^{-1}$
:::

:::

:::example{number="2.10" kind="example" id="ex_2.10" topic="Mass of copper deposited via Faraday's law"}
#### Example 2.10

:::prompt
A solution of $\mathrm{CuSO}_{4}$ is electrolysed for 10 minutes with a current of 1.5 amperes. What is the mass of copper deposited at the cathode?
:::

:::solution{label="Solution"}
$t=600 \mathrm{~s}$ charge = current $\times$ time $=1.5 \mathrm{~A} \times 600 \mathrm{~s}=900 \mathrm{C}$
According to the reaction:

$$
\mathrm{Cu}^{2+}(\mathrm{aq})+2 \mathrm{e}^{-}=\mathrm{Cu}(\mathrm{~s})
$$

We require 2F or $2 \times 96487 \mathrm{C}$ to deposit 1 mol or 63 g of Cu .
For 900 C, the mass of Cu deposited

$$
=\left(63 \mathrm{~g} \mathrm{~mol}^{-1} \times 900 \mathrm{C}\right) /\left(2 \times 96487 \mathrm{C} \mathrm{~mol}^{-1}\right)=0.2938 \mathrm{~g} .
$$
:::

:::answer
**Answer:** Mass of Cu deposited $= 0.2938 \mathrm{~g}$
:::

:::

## Questions and Solutions

:::question{number="2.1" kind="exercise" id="q_2.1" topic="Metal displacement order" corrections_applied="2"}
#### Question 2.1

:::prompt
Arrange the following metals in the order in which they displace each other from the solution of their salts.
Al, Cu, Fe, Mg and Zn.
:::

:::solution{label="Solution"}
The following is the order in which the given metals displace each other from the solution of their salts.

Mg, Al, Zn, Fe, Cu
:::

:::answer
**Answer:** Mg, Al, Zn, Fe, Cu
:::

:::

:::question{number="2.2" kind="exercise" id="q_2.2" topic="Reducing power ranking"}
#### Question 2.2

:::prompt
Given the standard electrode potentials,
$\mathrm{K}^{+} / \mathrm{K}=-2.93 \mathrm{~V}, \mathrm{Ag}^{+} / \mathrm{Ag}=0.80 \mathrm{~V}$,
$\mathrm{Hg}^{2+} / \mathrm{Hg}=0.79 \mathrm{~V}$
$\mathrm{Mg}^{2+} / \mathrm{Mg}=-2.37 \mathrm{~V}, \mathrm{Cr}^{3+} / \mathrm{Cr}=-0.74 \mathrm{~V}$
Arrange these metals in their increasing order of reducing power.
:::

:::solution{label="Solution"}
The lower the reduction potential, the higher is the reducing power. The given standard electrode potentials increase in the order of $\mathrm{K}^{+} / \mathrm{K}<\mathrm{Mg}^{2+} / \mathrm{Mg}<\mathrm{Cr}^{3+} / \mathrm{Cr}<\mathrm{Hg}^{2+} / \mathrm{Hg}<$ $\mathrm{Ag}^{+} / \mathrm{Ag}$.

Hence, the reducing power of the given metals increases in the following order: Ag $<\mathrm{Hg}<\mathrm{Cr}<\mathrm{Mg}<\mathrm{K}$
:::

:::answer
**Answer:** Ag $<\mathrm{Hg}<\mathrm{Cr}<\mathrm{Mg}<\mathrm{K}$
:::

:::

:::question{number="2.3" kind="exercise" id="q_2.3" topic="Zn-Ag galvanic cell setup" simplified="True"}
#### Question 2.3

:::prompt
Depict the galvanic cell in which the reaction
$\mathrm{Zn}(\mathrm{s})+2 \mathrm{Ag}^{+}(\mathrm{aq}) \rightarrow \mathrm{Zn}^{2+}(\mathrm{aq})+2 \mathrm{Ag}(\mathrm{s})$ takes place. Further show:
:::

:::part{label="(i)"}
:::prompt
Which of the electrode is negatively charged?
:::

:::

:::part{label="(ii)"}
:::prompt
The carriers of the current in the cell.
:::

:::

:::part{label="(iii)"}
:::prompt
Individual reaction at each electrode.
:::

:::

:::solution{label="Solution"}
The galvanic cell in which the given reaction takes place is depicted as:

$$
\mathrm{Zn}_{(s)}\left|\mathrm{Zn}_{(a q)}^{2+} \| \mathrm{Ag}_{(a q)}^{+}\right| \mathrm{Ag}_{(s)}
$$

(i) Zn electrode (anode) is negatively charged.
(ii) Ions carry the current in the cell. In the external circuit, current flows from silver to zinc.
(iii) The reaction taking place at the anode is given by,
$$
\mathrm{Zn}_{(s)} \longrightarrow \mathrm{Zn}_{(a q)}^{2+}+2 \mathrm{e}^{-}
$$
The reaction taking place at the cathode is given by,
$$
\mathrm{Ag}_{(\mathrm{aq})}^{+}+\mathrm{e}^{-} \longrightarrow \mathrm{Ag}_{(s)}
$$
:::

:::

:::question{number="2.4" kind="exercise" id="q_2.4" topic="Standard cell potential and Gibbs energy"}
#### Question 2.4

:::prompt
Calculate the standard cell potentials of galvanic cell in which the following reactions take place:
Calculate the $\Delta_{\mathrm{r}} G^{\circ}$ and equilibrium constant of the reactions.
:::

:::part{label="(i)"}
:::prompt
$2 \mathrm{Cr}(\mathrm{s})+3 \mathrm{Cd}^{2+}(\mathrm{aq}) \rightarrow 2 \mathrm{Cr}^{3+}(\mathrm{aq})+3 \mathrm{Cd}$
:::

:::

:::part{label="(ii)"}
:::prompt
$\mathrm{Fe}^{2+}(\mathrm{aq})+\mathrm{Ag}^{+}(\mathrm{aq}) \rightarrow \mathrm{Fe}^{3+}(\mathrm{aq})+\mathrm{Ag}(\mathrm{s})$
:::

:::

:::solution{label="Solution"}
(i) $E_{\mathrm{Cr}^{3+} / \mathrm{Cr}}^{\ominus}=0.74 \mathrm{~V}$
$$
E_{\mathrm{Cd}^{2+} / \mathrm{Cd}}^{\ominus}=-0.40 \mathrm{~V}
$$

The galvanic cell of the given reaction is depicted as:

$$
\mathrm{Cr}_{(s)}\left|\mathrm{Cr}_{(a q)}^{3+} \| \mathrm{Cd}_{(a q)}^{2+}\right| \mathrm{Cd}_{(s)}
$$

Now, the standard cell potential is

$$
\begin{aligned}
E_{\text {cell }}^{\ominus} & =E_{\mathrm{R}}^{\ominus}-E_{\mathrm{L}}^{\ominus} \\
& =-0.40-(-0.74) \\
& =+0.34 \mathrm{~V}
\end{aligned}
$$

$$
\Delta_{r} G^{\ominus}=-n \mathrm{~F} E_{\text {cell }}^{\ominus}
$$

In the given equation, $n$

$$
=6
$$

$$
\begin{aligned}
& \mathrm{F}=96487 \mathrm{C} \mathrm{~mol}^{-1} \\
& E_{\text {cell }}^{\ominus}=+0.34 \mathrm{~V}
\end{aligned}
$$

Then, $\Delta_{\mathrm{r}} G^{\ominus}=-6 \times 96487 \mathrm{C} \mathrm{mol}^{-1} \times 0.34 \mathrm{~V}$

$$
\begin{aligned}
& =-196833.48 \mathrm{CV} \mathrm{~mol}^{-1} \\
& =-196833.48 \mathrm{~J} \mathrm{~mol}^{-1} \\
& =-196.83 \mathrm{~kJ} \mathrm{~mol}^{-1}
\end{aligned}
$$

Again,

$$
\begin{aligned}
& \Delta_{\mathrm{r}} G^{\ominus}=-\mathrm{R} T \ln K \\
& \begin{aligned}
& \Rightarrow \Delta_{\mathrm{r}} G^{\ominus}=-2.303 \mathrm{R} T \ln K \\
& \Rightarrow \log K=-\frac{\Delta_{\mathrm{r}} G}{2.303 \mathrm{R} T} \\
& \quad=\frac{-196.83 \times 10^{3}}{2.303 \times 8.314 \times 298} \\
&=34.496 \\
& \therefore \mathrm{~K}=\text { antilog }(34.496)= \\
& 3.13 \times 10^{34}
\end{aligned}
\end{aligned}
$$

(ii)

$$
E_{\mathrm{Fe}^{3+} / \mathrm{Fe}^{2+}}=0.77 \mathrm{~V}
$$

$$
E_{\mathrm{Ag}^{+} / \mathrm{Ag}}^{\ominus}=0.80 \mathrm{~V}
$$

The galvanic cell of the given reaction is depicted as:

$$
\mathrm{Fe}_{(a q)}^{2+}\left|\mathrm{Fe}_{(a q)}^{3+}\right|\left|\mathrm{Ag}_{(a q)}^{+}\right| \mathrm{Ag}_{(s)}
$$

Now, the standard cell potential is

$$
\begin{aligned}
E_{\text {cell }}^{\ominus} & =E_{\mathrm{R}}^{\ominus}-E_{\mathrm{L}}^{\ominus} \\
& =0.80-0.77 \\
& =0.03 \mathrm{~V}
\end{aligned}
$$

Here, $n=1$.
Then, $\Delta_{\mathrm{r}} G^{\ominus}=-n \mathrm{~F} E_{\text {cell }}^{\ominus}$

$$
=-1 \times 96487 \mathrm{C} \mathrm{~mol}^{-1} \times 0.03 \mathrm{~V}
$$

$$
\begin{aligned}
& =-2894.61 \mathrm{~J} \mathrm{~mol}^{-1} \\
& =-2.89 \mathrm{~kJ} \mathrm{~mol}^{-1}
\end{aligned}
$$

Again, $\Delta_{\mathrm{r}} G^{\ominus}=-2.303 \mathrm{R} T \ln K$

$$
\begin{aligned}
& \Rightarrow \log K=-\frac{\Delta_{\mathrm{r}} G}{2.303 \mathrm{R} T} \\
& \quad=\frac{-2894.61}{2.303 \times 8.314 \times 298} \\
& =0.5073 \\
& \therefore \mathrm{~K}=\text { antilog (0.5073) } \\
& =3.2 \text { (approximately) }
\end{aligned}
$$
:::

:::answer
**Answer:** (i) $E_{\text{cell}}^{\ominus} = +0.34 \mathrm{~V}$, $\Delta_{r}G^{\ominus} = -196.83 \mathrm{~kJ} \mathrm{~mol}^{-1}$, $K = 3.13 \times 10^{34}$; (ii) $E_{\text{cell}}^{\ominus} = 0.03 \mathrm{~V}$, $\Delta_{r}G^{\ominus} = -2.89 \mathrm{~kJ} \mathrm{~mol}^{-1}$, $K = 3.2$ (approximately)
:::

:::

:::question{number="2.5" kind="exercise" id="q_2.5" topic="Nernst equation and emf of cells" corrections_applied="1"}
#### Question 2.5

:::prompt
Write the Nernst equation and emf of the following cells at 298 K:
:::

:::part{label="(i)"}
:::prompt
$\mathrm{Mg}(\mathrm{s})\left|\mathrm{Mg}^{2+}(0.001 \mathrm{M})\right|\left|\mathrm{Cu}^{2+}(0.0001 \mathrm{M})\right| \mathrm{Cu}(\mathrm{s})$
:::

:::

:::part{label="(ii)"}
:::prompt
$\mathrm{Fe}(\mathrm{s})\left|\mathrm{Fe}^{2+}(0.001 \mathrm{M})\right|\left|\mathrm{H}^{+}(1 \mathrm{M})\right| \mathrm{H}_{2}(\mathrm{~g})(1 \mathrm{bar}) \mid \mathrm{Pt}(\mathrm{s})$
:::

:::

:::part{label="(iii)"}
:::prompt
$\mathrm{Sn}(\mathrm{s})\left|\mathrm{Sn}^{2+}(0.050 \mathrm{M}) \| \mathrm{H}^{+}(0.020 \mathrm{M})\right| \mathrm{H}_{2}(\mathrm{~g})$ (1 bar) | Pt (s)
:::

:::

:::part{label="(iv)"}
:::prompt
$\operatorname{Pt}(\mathrm{s})\left|\mathrm{Br}^{-}(0.010 \mathrm{M})\right| \mathrm{Br}_{2}(l) \| \mathrm{H}^{+}(0.030 \mathrm{M}) \mid \mathrm{H}_{2}(\mathrm{~g})$ (1 bar) | Pt(s).
:::

:::

:::solution{label="Solution"}
(i) For the given reaction, the Nernst equation can be given as:
$$
\begin{aligned}
& E_{\text {cell }}=E_{\text {cell }}^{\ominus}-\frac{0.0591}{n} \log \frac{\left[\mathrm{Mg}^{2+}\right]}{\left[\mathrm{Cu}^{2+}\right]} \\
&=\{0.34-(-2.36)\}-\frac{0.0591}{2} \log \frac{.001}{.0001} \\
&=2.7-\frac{0.0591}{2} \log 10 \\
&=2.7-0.02955 \\
&=2.67 \mathrm{~V} \text { (approximately) }
\end{aligned}
$$
(ii) For the given reaction, the Nernst equation can be given as:

$$
\begin{aligned}
E_{\text {cell }} & =E_{\text {cell }}^{\ominus}-\frac{0.0591}{n} \log \frac{\left[\mathrm{Fe}^{2+}\right]}{\left[\mathrm{H}^{+}\right]^{2}} \\
& =\{0-(-0.44)\}-\frac{0.0591}{2} \log \frac{0.001}{1^{2}} \\
& =0.44-0.02955(-3) \\
= & 0.52865 \mathrm{~V} \\
= & 0.53 \mathrm{~V} \text { (approximately) }
\end{aligned}
$$

(iii) For the given reaction, the Nernst equation can be given as:

$$
\begin{aligned}
& E_{\text {cell }}=E_{\text {cell }}^{\ominus}-\frac{0.0591}{n} \log \frac{\left[\mathrm{Sn}^{2+}\right]}{\left[\mathrm{H}^{+}\right]^{2}} \\
& \quad=\{0-(-0.14)\}-\frac{0.0591}{2} \log \frac{0.050}{(0.020)^{2}} \\
& =0.14-0.0295 \times \log 125 \\
& =0.14-0.062 \\
& =0.078 \mathrm{~V} \\
& =0.08 \mathrm{~V} \text { (approximately) }
\end{aligned}
$$

(iv) For the given reaction, the Nernst equation can be given as:

$$
\begin{aligned}
E_{\text {cell }} & =E_{\text {cell }}^{\ominus}-\frac{0.0591}{n} \log \frac{1}{\left[\mathrm{Br}^{-}\right]^{2}\left[\mathrm{H}^{+}\right]^{2}} \\
& =(0-1.09)-\frac{0.0591}{2} \log \frac{1}{(0.010)^{2}(0.030)^{2}} \\
& =-1.09-0.02955 \times \log \frac{1}{0.00000009} \\
& =-1.09-0.02955 \times \log \frac{1}{9 \times 10^{-8}} \\
& =-1.09-0.02955 \times \log \left(1.11 \times 10^{7}\right) \\
& =-1.09-0.02955(0.0453+7) \\
& =-1.09-0.208 \\
& =-1.298 \mathrm{~V}
\end{aligned}
$$
:::

:::answer
**Answer:** (i) $2.67 \mathrm{~V}$ (approximately); (ii) $0.53 \mathrm{~V}$ (approximately); (iii) $0.08 \mathrm{~V}$ (approximately); (iv) $-1.298 \mathrm{~V}$
:::

:::

:::question{number="2.6" kind="exercise" id="q_2.6" topic="Gibbs energy and standard potential of button cell"}
#### Question 2.6

:::prompt
In the button cells widely used in watches and other devices the following reaction takes place:
$\mathrm{Zn}(\mathrm{s})+\mathrm{Ag}_{2} \mathrm{O}(\mathrm{s})+\mathrm{H}_{2} \mathrm{O}(\mathrm{l}) \rightarrow \mathrm{Zn}^{2+}(\mathrm{aq})+2 \mathrm{Ag}(\mathrm{s})+2 \mathrm{OH}^{-}(\mathrm{aq})$
Determine $\Delta_{r} G^{\circ}$ and $E^{\circ}$ for the reaction.
:::

:::solution{label="Solution"}
= 1.104 V
We know that,

$$
\begin{aligned}
& \Delta_{r} G^{\ominus}=-n \mathrm{~F} E^{\ominus} \\
& =-2 \times 96487 \times 1.04 \\
& =-213043.296 \mathrm{~J} \\
& =-213.04 \mathrm{~kJ}
\end{aligned}
$$
:::

:::answer
**Answer:** $E^{\ominus} = 1.104 \mathrm{~V}$ (as stated); $\Delta_{r}G^{\ominus} = -213.04 \mathrm{~kJ}$ (calculation shown uses $1.04$, not $1.104$ — see report)
:::

:::

:::question{number="2.7" kind="exercise" id="q_2.7" topic="Conductivity and molar conductivity definitions" simplified="True"}
#### Question 2.7

:::prompt
Define conductivity and molar conductivity for the solution of an electrolyte. Discuss their variation with concentration.
:::

:::figure{src="images/fig_2_29.jpg" id="fig_sol_2.7_1"}
The variation of $\Lambda_{m}$ with $\sqrt{\mathrm{c}}$ for strong and weak electrolytes.
:::

:::solution{label="Solution"}
Conductivity of a solution is the conductance of the solution kept between two electrodes 1 cm apart, each with an area of cross-section of 1 sq. cm. It is the inverse of resistivity, so it is also called specific conductance, and is written as $\kappa$. If $\rho$ is the resistivity, we can write:

$$
\kappa=\frac{1}{\rho}
$$

At any given concentration, the conductivity of a solution is the conductance $(G)$ of one unit volume of the solution. This volume is held between two platinum electrodes, each of unit area of cross-section, separated by unit length.
i.e.,

$$
G=\kappa \frac{a}{l}=\kappa \cdot 1=\kappa
$$

(Since $a=1, l=1$ )
Conductivity always decreases as concentration decreases, for both weak and strong electrolytes. This is because fewer ions per unit volume are available to carry the current as concentration falls.

## Molar conductivity:

At a given concentration, molar conductivity is the conductance of a volume V of solution that contains 1 mole of the electrolyte, kept between two electrodes with area of cross-section $A$ and unit length between them.

$$
\Lambda_{m}=\kappa \frac{A}{l}
$$

Now, $I=1$ and $A=\mathrm{V}$ (volume containing 1 mole of the electrolyte).

$$
\therefore \Lambda_{m}=\kappa \mathrm{V}
$$

Molar conductivity increases as concentration decreases. This happens because the total volume V of the solution containing one mole of the electrolyte increases on dilution.
The variation of $\Lambda_{m}$ with $\sqrt{\mathrm{c}}$ for strong and weak electrolytes is shown in the following plot:
:::

:::

:::question{number="2.8" kind="exercise" id="q_2.8" topic="Molar conductivity of KCl solution"}
#### Question 2.8

:::prompt
The conductivity of 0.20 M solution of KCl at 298 K is 0.0248 S cm ${ }^{-1}$. Calculate its molar conductivity.
:::

:::solution{label="Solution"}
Given, $\kappa$

$$
\begin{aligned}
& =0.0248 \mathrm{~S} \mathrm{~cm}^{-1} \mathrm{C} \\
& =0.20 \mathrm{M}
\end{aligned}
$$

$$
\begin{aligned}
& \therefore \text { Molar conductivity, } \Lambda_{m}=\frac{\kappa \times 1000}{\mathrm{c}} \\
& =\frac{0.0248 \times 1000}{0.2} \\
& =124 \mathrm{Scm}^{2} \mathrm{~mol}^{-1}
\end{aligned}
$$
:::

:::answer
**Answer:** $124 \mathrm{~S} \mathrm{~cm}^{2} \mathrm{~mol}^{-1}$
:::

:::

:::question{number="2.9" kind="exercise" id="q_2.9" topic="Cell constant from KCl conductivity"}
#### Question 2.9

:::prompt
The resistance of a conductivity cell containing 0.001M KCl solution at 298 K is $1500 \Omega$. What is the cell constant if conductivity of 0.001 M KCl solution at 298 K is $0.146 \times 10^{-3} \mathrm{~S} \mathrm{~cm}^{-1}$.
:::

:::solution{label="Solution"}
Given,

$$
\begin{aligned}
& \text { Conductivity, } \kappa=0.146 \times 10^{-3} \mathrm{~S} \mathrm{~cm}^{-1} \\
& \text { Resistance, } R=1500 \Omega \\
& \therefore \text { Cell constant }=\kappa \times R \\
& =0.146 \times 10^{-3} \times 1500 \\
& =0.219 \mathrm{~cm}^{-1}
\end{aligned}
$$
:::

:::answer
**Answer:** $0.219 \mathrm{~cm}^{-1}$
:::

:::

:::question{number="2.10" kind="exercise" id="q_2.10" topic="Molar conductivity of NaCl vs concentration"}
#### Question 2.10

:::prompt
The conductivity of sodium chloride at 298 K has been determined at different concentrations and the results are given below:

| Concentration/M | 0.001 | 0.010 | 0.020 | 0.050 | 0.100 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| $10^{2} \times \kappa / \mathrm{S} \mathrm{m}^{-1}$ | 1.237 | 11.85 | 23.15 | 55.53 | 106.74 |

Calculate $\Lambda_{m}$ for all concentrations and draw a plot between $\Lambda_{m}$ and $\mathrm{c}^{1 / 2}$. Find the value of $\Lambda_{m}^{0}$.
:::

:::figure{src="images/fig_2_30.jpg" id="fig_sol_2.10_1"}
Plot of $\Lambda_{m}$ against $c^{1/2}$ for the given NaCl concentration data.
:::

:::solution{label="Solution"}
Given,

$$
\kappa=1.237 \times 10^{-2} \mathrm{~S} \mathrm{~m}^{-1}, \mathrm{c}=0.001 \mathrm{M}
$$

Then, $\kappa=1.237 \times 10^{-4} \mathrm{~S} \mathrm{~cm}^{-1}, \mathrm{c}^{1 / 2}=0.0316 \mathrm{M}^{1 / 2}$

$$
\begin{aligned}
& \therefore \Lambda_{m}=\frac{\kappa}{c} \\
& =\frac{1.237 \times 10^{-4} \mathrm{~S} \mathrm{~cm}^{-1}}{0.001 \mathrm{~mol} \mathrm{~L}^{-1}} \times \frac{1000 \mathrm{~cm}^{3}}{\mathrm{~L}} \\
& =123.7 \mathrm{~S} \mathrm{~cm}^{2} \mathrm{~mol}^{-1} \text { Given, } \\
& \kappa=11.85 \times 10^{-2} \mathrm{~S} \mathrm{~m}^{-1}, \mathrm{c}=0.010 \mathrm{M}
\end{aligned}
$$

Then, $\mathrm{K}=11.85 \times 10^{-4} \mathrm{~S} \mathrm{~cm}^{-1}, \mathrm{c}^{1 / 2}=0.1 \mathrm{M}^{1 / 2}$

$$
\begin{aligned}
& \therefore \Lambda_{m}=\frac{\kappa}{c} \\
& =\frac{11.85 \times 10^{-4} \mathrm{~S} \mathrm{~cm}^{-1}}{0.010 \mathrm{~mol} \mathrm{~L}^{-1}} \times \frac{1000 \mathrm{~cm}^{3}}{\mathrm{~L}} \\
& =118.5 \mathrm{~S} \mathrm{~cm}^{2} \mathrm{~mol}^{-1} \text { Given, } \\
& \kappa=23.15 \times 10^{-2} \mathrm{~S} \mathrm{~m}^{-1}, \mathrm{c}=0.020 \mathrm{M}
\end{aligned}
$$

Then, $\kappa=23.15 \times 10^{-4} \mathrm{~S} \mathrm{~cm}^{-1}, \mathrm{c}^{1 / 2}=0.1414 \mathrm{M}^{1 / 2}$

$$
\begin{aligned}
& \therefore \Lambda_{m}=\frac{K}{c} \\
& =\frac{23.15 \times 10^{-4} \mathrm{~S} \mathrm{~cm}^{-1}}{0.020 \mathrm{~mol} \mathrm{~L}^{-1}} \times \frac{1000 \mathrm{~cm}^{3}}{\mathrm{~L}} \\
& =115.8 \mathrm{~S} \mathrm{~cm}^{2} \mathrm{~mol}^{-1} \text { Given, } \\
& \kappa=55.53 \times 10^{-2} \mathrm{~S} \mathrm{~m}^{-1}, \mathrm{c}=0.050 \mathrm{M}
\end{aligned}
$$

Then, $\kappa=55.53 \times 10^{-4} \mathrm{~S} \mathrm{~cm}^{-1}, \mathrm{c}^{1 / 2}=0.2236 \mathrm{M}^{1 / 2}$

$$
\begin{aligned}
& \therefore \kappa=\frac{\kappa}{c} \\
& =\frac{55.53 \times 10^{-4} \mathrm{~S} \mathrm{~cm}^{-1}}{0.050 \mathrm{~mol} \mathrm{~L}^{-1}} \times \frac{1000 \mathrm{~cm}^{3}}{\mathrm{~L}} \\
& =111.11 \mathrm{~S} \mathrm{~cm}^{2} \mathrm{~mol}^{-1} \text { Given, } \\
& \kappa=106.74 \times 10^{-2} \mathrm{~S} \mathrm{~m}^{-1}, \mathrm{c}=0.100 \mathrm{M}
\end{aligned}
$$

Then, $\kappa=106.74 \times 10^{-4} \mathrm{~S} \mathrm{~cm}^{-1}, \mathrm{c}^{1 / 2}=0.3162 \mathrm{M}^{1 / 2}$

$$
\begin{aligned}
& \Lambda_{m}=\frac{K}{c} \\
= & \frac{106.74 \times 10^{-4} \mathrm{~S} \mathrm{~cm}^{-1}}{0.100 \mathrm{~mol} \mathrm{~L}^{-1}} \times \frac{1000 \mathrm{~cm}^{3}}{\mathrm{~L}} \\
= & 106.74 \mathrm{~S} \mathrm{~cm}^{2} \mathrm{~mol}^{-1} \text { Now, we }
\end{aligned}
$$

have the following data:

| $\mathrm{C}^{1 / 2} / \mathrm{M}^{1 / 2}$ | 0.0316 | 0.1 | 0.1414 | 0.2236 | 0.3162 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| $\Lambda_{m}\left(\mathrm{~S} \mathrm{~cm}^{2} \mathrm{~mol}^{-1}\right)$ | 123.7 | 118.5 | 115.8 | 111.1 | 106.74 |

Since the line interrupts ${ }^{\Lambda_{m}}$ at $124.0 \mathrm{~S} \mathrm{~cm}^{2} \mathrm{~mol}^{-1}, \Lambda_{m}^{0}=124.0 \mathrm{~S} \mathrm{~cm}^{2} \mathrm{~mol}^{-1}$.
:::

:::answer
**Answer:** $\Lambda_{m}^{0} = 124.0 \mathrm{~S} \mathrm{~cm}^{2} \mathrm{~mol}^{-1}$
:::

:::

:::question{number="2.11" kind="exercise" id="q_2.11" topic="Molar conductivity and dissociation constant of acetic acid"}
#### Question 2.11

:::prompt
Conductivity of 0.00241 M acetic acid is $7.896 \times 10^{-5} \mathrm{~S} \mathrm{~cm}^{-1}$. Calculate its molar conductivity. If $\Lambda_{m}^{0}$ for acetic acid is $390.5 \mathrm{~S} \mathrm{~cm}^{2} \mathrm{~mol}^{-1}$, what is its dissociation constant?
:::

:::solution{label="Solution"}
Given, $\kappa=7.896 \times 10^{-5} \mathrm{~S} \mathrm{~m}^{-1} \mathrm{c}$
$=0.00241 \mathrm{~mol} \mathrm{~L}^{-1}$
Then, molar conductivity,

$$
\Lambda_{m}=\frac{K}{\mathrm{c}}
$$

$$
\begin{aligned}
& =\frac{7.896 \times 10^{-5} \mathrm{~S} \mathrm{~cm}^{-1}}{0.00241 \mathrm{~mol} \mathrm{~L}^{-1}} \times \frac{1000 \mathrm{~cm}^{3}}{\mathrm{~L}} \\
& =32.76 \mathrm{~S} \mathrm{~cm}^{2} \mathrm{~mol}^{-1}
\end{aligned}
$$

$$
\begin{aligned}
& \Lambda_{m}^{0}=390.5 \mathrm{~S} \mathrm{~cm}^{2} \mathrm{~mol}^{-1} \quad \text { Again }, \\
& \alpha=\frac{\Lambda_{m}}{\Lambda_{m}^{0}}=\frac{32.76 \mathrm{~S} \mathrm{~cm}^{2} \mathrm{~mol}^{-1}}{390.5 \mathrm{~S} \mathrm{~cm}^{2} \mathrm{~mol}^{-1}}
\end{aligned}
$$

Now,

$$
\text { = } 0.084
$$

$$
\begin{aligned}
& \therefore K_{a}=\frac{\mathrm{c} \alpha^{2}}{(1-\alpha)} \\
& =\frac{\left(0.00241 \mathrm{~mol} \mathrm{~L}^{-1}\right)(0.084)^{2}}{(1-0.084)} \\
& =1.86 \times 10^{-5} \mathrm{~mol} \mathrm{~L}^{-1}
\end{aligned}
$$
:::

:::answer
**Answer:** $\Lambda_{m} = 32.76 \mathrm{~S} \mathrm{~cm}^{2} \mathrm{~mol}^{-1}$; $\alpha = 0.084$; $K_{a} = 1.86 \times 10^{-5} \mathrm{~mol} \mathrm{~L}^{-1}$
:::

:::

:::question{number="2.12" kind="exercise" id="q_2.12" topic="Charge required for reductions"}
#### Question 2.12

:::prompt
How much charge is required for the following reductions:
:::

:::part{label="(i)"}
:::prompt
1 mol of $\mathrm{Al}^{3+}$ to Al ?
:::

:::

:::part{label="(ii)"}
:::prompt
1 mol of $\mathrm{Cu}^{2+}$ to Cu ?
:::

:::

:::part{label="(iii)"}
:::prompt
1 mol of $\mathrm{MnO}_{4}^{-}$to $\mathrm{Mn}^{2+}$ ?
:::

:::

:::solution{label="Solution"}
(i)

$$
\mathrm{Al}^{3+}+3 \mathrm{e}^{-} \longrightarrow \mathrm{Al}
$$

∴ Required charge $=3 \mathrm{~F}$

$$
\begin{aligned}
& =3 \times 96487 \mathrm{C} \\
& =289461 \mathrm{C}
\end{aligned}
$$

(ii)

$$
\mathrm{Cu}^{2+}+2 \mathrm{e}^{-} \longrightarrow \mathrm{Cu}
$$

∴ Required charge $=2 \mathrm{~F}$

$$
\begin{aligned}
& =2 \times 96487 \mathrm{C} \\
& =192974 \mathrm{C}
\end{aligned}
$$

(iii)

$$
\mathrm{MnO}_{4}^{-} \longrightarrow \mathrm{Mn}^{2+}
$$

i.e.,

$$
\begin{aligned}
& \therefore \\
& =5 \times 96487 \mathrm{C} \\
& =482435 \mathrm{C}
\end{aligned}
$$
:::

:::answer
**Answer:** (i) $289461 \mathrm{C}$ (3 F); (ii) $192974 \mathrm{C}$ (2 F); (iii) $482435 \mathrm{C}$ (5 F)
:::

:::

:::question{number="2.13" kind="exercise" id="q_2.13" topic="Faraday charge for metal production" corrections_applied="1"}
#### Question 2.13

:::prompt
How much electricity in terms of Faraday is required to produce
:::

:::part{label="(i)"}
:::prompt
20.0 g of Ca from molten $\mathrm{CaCl}_{2}$ ?
:::

:::

:::part{label="(ii)"}
:::prompt
40.0 g of Al from molten $\mathrm{Al}_{2} \mathrm{O}_{3}$ ?
:::

:::

:::solution{label="Solution"}
(i) According to the question,

$$
\mathrm{Ca}^{2+}+2 \mathrm{e}^{-1} \longrightarrow \underset{40 \mathrm{~g}}{\mathrm{Ca}}
$$

Electricity required to produce 40 g of calcium $=2 \mathrm{~F}$
Therefore, electricity required to produce 20 g of calcium $=\frac{2 \times 20}{40} \mathrm{~F}$

$$
\text { = } 1 \text { F }
$$

(ii) According to the question,

$$
\mathrm{Al}^{3+}+3 \mathrm{e}^{-} \longrightarrow{ }_{27 \mathrm{~g}}
$$

Electricity required to produce 27 g of AI = 3 F
Therefore, electricity required to produce 40 g of $\mathrm{Al}=\frac{3 \times 40}{27} \mathrm{~F}$ $=4.44 \mathrm{~F}$
:::

:::answer
**Answer:** (i) $1 \mathrm{~F}$; (ii) $4.44 \mathrm{~F}$
:::

:::

:::question{number="2.14" kind="exercise" id="q_2.14" topic="Charge for oxidation reactions"}
#### Question 2.14

:::prompt
How much electricity is required in coulomb for the oxidation of
:::

:::part{label="(i)"}
:::prompt
1 mol of $\mathrm{H}_{2} \mathrm{O}$ to $\mathrm{O}_{2}$ ?
:::

:::

:::part{label="(ii)"}
:::prompt
1 mol of FeO to $\mathrm{Fe}_{2} \mathrm{O}_{3}$ ?
:::

:::

:::solution{label="Solution"}
(i) According to the question,

$$
\mathrm{H}_{2} \mathrm{O} \longrightarrow \mathrm{H}_{2}+\frac{1}{2} \mathrm{O}_{2}
$$

Now, we can write:

$$
\mathrm{O}^{2-} \longrightarrow \frac{1}{2} \mathrm{O}_{2}+2 \mathrm{e}^{-}
$$

Electricity required for the oxidation of 1 mol of $\mathrm{H}_{2} \mathrm{O}$ to $\mathrm{O}_{2}=2 \mathrm{~F}$

$$
\begin{aligned}
& =2 \times 96487 \mathrm{C} \\
& =192974 \mathrm{C}
\end{aligned}
$$

(ii) According to the question,

$$
\mathrm{Fe}^{2+} \longrightarrow \mathrm{Fe}^{3+}+\mathrm{e}^{-1}
$$

Electricity required for the oxidation of 1 mol of FeO to $\mathrm{Fe}_{2} \mathrm{O}_{3}=1 \mathrm{~F}$

$$
\text { = } 96487 \text { C }
$$
:::

:::answer
**Answer:** (i) $192974 \mathrm{C}$ (2 F); (ii) $96487 \mathrm{C}$ (1 F)
:::

:::

:::question{number="2.15" kind="exercise" id="q_2.15" topic="Mass of nickel deposited"}
#### Question 2.15

:::prompt
A solution of $\mathrm{Ni}\left(\mathrm{NO}_{3}\right)_{2}$ is electrolysed between platinum electrodes using a current of 5 amperes for 20 minutes. What mass of Ni is deposited at the cathode?
:::

:::solution{label="Solution"}
Given,
Current $=5 \mathrm{~A}$
Time $=20 \times 60=1200 \mathrm{~s}$
∴ Charge = current × time
$=5 \times 1200$
$=6000 \mathrm{C}$
According to the reaction,

$$
\begin{aligned}
\mathrm{Ni}_{(a q)}^{2+}+2 \mathrm{e}^{-} \longrightarrow & \mathrm{Ni}_{(s)} \\
& 58.7 \mathrm{~g}
\end{aligned}
$$

Nickel deposited by $2 \times 96487 \mathrm{C}=58.71 \mathrm{~g}$
Therefore, nickel deposited by $6000 \mathrm{C}=\frac{58.71 \times 6000}{2 \times 96487} \mathrm{~g}$
$=1.825 \mathrm{~g}$
Hence, 1.825 g of nickel will be deposited at the cathode.
:::

:::answer
**Answer:** $1.825 \mathrm{~g}$ of nickel
:::

:::

:::question{number="2.16" kind="exercise" id="q_2.16" topic="Series electrolytic cells deposition"}
#### Question 2.16

:::prompt
Three electrolytic cells A,B,C containing solutions of $\mathrm{ZnSO}_{4}, \mathrm{AgNO}_{3}$ and $\mathrm{CuSO}_{4}$, respectively are connected in series. A steady current of 1.5 amperes was passed through them until 1.45 g of silver deposited at the cathode of cell B. How long did the current flow? What mass of copper and zinc were deposited?
:::

:::solution{label="Solution"}
According to the reaction:

$$
\begin{aligned}
\mathrm{Ag}_{(a q)}^{+}+\mathrm{e}^{-} \longrightarrow & \mathrm{Ag}_{(s)} \\
& 108 \mathrm{~g}
\end{aligned}
$$

i.e., 108 g of Ag is deposited by 96487 C.
Therefore, 1.45 g of Ag is deposited by $=\frac{96487 \times 1.45}{108} \mathrm{C}$
= 1295.43 C
Given,
Current $=1.5 \mathrm{~A}$

$$
\begin{aligned}
& \therefore \text { Time }=\frac{1295.43}{1.5} \mathrm{~s} \\
& =863.6 \mathrm{~s} \\
& =864 \mathrm{~s} \\
& =14.40 \mathrm{~min}
\end{aligned}
$$

Again,

$$
\mathrm{Cu}_{(\mathrm{aq})}^{2+}+2 \mathrm{e}^{-} \longrightarrow \underset{63.5 \mathrm{~g}}{\mathrm{Cu}_{(\mathrm{s})}}
$$

i.e., $2 \times 96487 \mathrm{C}$ of charge deposit $=63.5 \mathrm{~g}$ of Cu
Therefore, 1295.43 C of charge will deposit $=\frac{63.5 \times 1295.43}{2 \times 96487} \mathrm{~g}$

$$
\begin{aligned}
& =0.426 \mathrm{~g} \text { of } \mathrm{Cu} \\
& \mathrm{Zn}_{(a q)}^{2+}+2 \mathrm{e}^{-} \longrightarrow \mathrm{Zn}_{(s)} \\
& 65.4 \mathrm{~g}
\end{aligned}
$$

i.e., $2 \times 96487 \mathrm{C}$ of charge deposit = 65.4 g of Zn
Therefore, 1295.43 C of charge will deposit $=\frac{65.4 \times 1295.43}{2 \times 96487} \mathrm{~g}$
$=0.439 \mathrm{~g}$ of Zn
:::

:::answer
**Answer:** Time $= 864 \mathrm{~s}$ ($14.40 \mathrm{~min}$); Cu deposited $= 0.426 \mathrm{~g}$; Zn deposited $= 0.439 \mathrm{~g}$
:::

:::

:::question{number="2.17" kind="exercise" id="q_2.17" topic="Feasibility of redox reactions" corrections_applied="2"}
#### Question 2.17

:::prompt
Using the standard electrode potentials given in Table 3.1, predict if the reaction between the following is feasible:
:::

:::part{label="(i)"}
:::prompt
$\mathrm{Fe}^{3+}(\mathrm{aq})$ and $\mathrm{I}^{-}(\mathrm{aq})$
:::

:::

:::part{label="(ii)"}
:::prompt
$\mathrm{Ag}^{+}(\mathrm{aq})$ and $\mathrm{Cu}(\mathrm{s})$
:::

:::

:::part{label="(iii)"}
:::prompt
$\mathrm{Fe}^{3+}(\mathrm{aq})$ and $\mathrm{Br}^{-}(\mathrm{aq})$
:::

:::

:::part{label="(iv)"}
:::prompt
$\mathrm{Ag}(\mathrm{s})$ and $\mathrm{Fe}^{3+}(\mathrm{aq})$
:::

:::

:::part{label="(v)"}
:::prompt
$\mathrm{Br}_{2}$ (aq) and $\mathrm{Fe}^{2+}$ (aq).
:::

:::

:::solution{label="Solution"}
(i) $$
\begin{array}{cl}
\left.\mathrm{Fe}^{3+}{ }_{(\mathrm{aq})}+\mathrm{e}^{-} \longrightarrow \mathrm{Fe}^{2+}{ }_{(\mathrm{aq})}\right] \times 2 ; & E^{0}=+0.77 \mathrm{~V} \\
2 \mathrm{I}_{(\mathrm{aq})}^{-} \longrightarrow \mathrm{I}_{2(\mathrm{~s})}+2 \mathrm{e}^{-} ; & E^{0}=-0.54 \mathrm{~V} \\
\hline 2 \mathrm{Fe}^{3+}{ }_{(\mathrm{aq})}+2 \mathrm{I}_{(\mathrm{aq})}^{-} \longrightarrow 2 \mathrm{Fe}^{2+}{ }_{(\mathrm{aq})}+\mathrm{I}_{2(\mathrm{~s})} ; & E^{0}=+0.23 \mathrm{~V}
\end{array}
$$
Since 3+(aq) and I-(aq) is feasible.
(ii) $$
\begin{array}{ll}
\left.\mathrm{Ag}_{(a q)}^{+}+\mathrm{e}^{-} \longrightarrow \mathrm{Ag}_{(s)}\right] \times 2 ; & E^{\circ}=+0.80 \mathrm{~V}, \mathrm{Fe} \\
\mathrm{Cu}_{(s)} \quad \longrightarrow \mathrm{Cu}_{(a q)}^{2+}+2 \mathrm{e}^{-} ; & E^{\circ}=-0.34 \mathrm{~V} \\
2 \mathrm{Ag}_{(a q)}^{+}+\mathrm{Cu}_{(s)} \longrightarrow 2 \mathrm{Ag}_{(s)}+\mathrm{Cu}_{(a q)}^{2+} ; & E^{\circ}=+0.46 \mathrm{~V}
\end{array}
$$
$E^{\circ}$ for the overall reaction is positive, the rea ction between Ag Since + (aq) and $\mathrm{Cu}_{(s)}$ is feasible.
(iii) $$
\begin{array}{ll}
\left.\mathrm{Fe}^{3+}{ }_{(a q)}+\mathrm{e}^{-} \longrightarrow \mathrm{Fe}^{2+}{ }_{(a q)}\right] \times 2 ; & E^{0}=+0.77 \mathrm{~V} \\
2 \mathrm{Br}^{-}{ }_{(a q)} \longrightarrow \mathrm{Br}_{2(q)}+2 \mathrm{e}^{-} \quad ; & E^{0}=-1.09 \mathrm{~V} \\
\hline 2 \mathrm{Fe}^{3+}{ }_{(a q)}+2 \mathrm{Br}^{-}{ }_{(a q)} \longrightarrow 2 \mathrm{Fe}^{2+}{ }_{(a q)} \text { and } \mathrm{Br}_{2(i)} ; & E^{0}=-0.32 \mathrm{~V}
\end{array}
$$
Since $E^{\circ}$ for the overall reaction is negative, the reaction between Fe 3+ - (aq) and Br (aq) is not feasible.
(iv) $$
\begin{array}{ll}
\mathrm{Ag}_{(s)} \longrightarrow \mathrm{Ag}_{(a q)}^{+}+\mathrm{e}^{-} & ; E^{0}=-0.80 \mathrm{~V} \\
\mathrm{Fe}^{3+}{ }_{(a q)}+\mathrm{e}^{-} \longrightarrow \mathrm{Fe}^{2+}(a q) & ; E^{0}=+0.77 \mathrm{~V} \\
\hline \mathrm{Ag}_{(s)}+\mathrm{Fe}^{3+}{ }_{(a q)} \longrightarrow \mathrm{Ag}_{(a q)}^{+}+\mathrm{Fe}^{2+}{ }_{(a q)} & ; E^{0}=-0.03 \mathrm{~V}
\end{array}
$$
(iv) $$
\mathrm{Br}_{2(a q)}+2 \mathrm{e}^{-} \longrightarrow 2 \mathrm{Br}_{(a q)}^{-} \quad ; E^{\circ}=+1.09 \mathrm{~V}
$$
!
$$
\begin{aligned}
& \left.\mathrm{Fe}^{2+}{ }_{(a q)} \longrightarrow \mathrm{Fe}^{3+}{ }_{(a q)}+\mathrm{e}^{-}\right] \times 2 \quad ; \quad E^{\circ}=-0.77 \mathrm{~V} \quad \text { en } \mathrm{Ag} \quad \text { (s) } \text { and } \mathrm{Fe}_{3+(a q)} \text { is } \\
& \mathrm{Br}_{2(a q)}+2 \mathrm{Fe}^{2+}{ }_{(a q)} \longrightarrow 2 \mathrm{Br}^{-}{ }_{(a q)}+2 \mathrm{Fe}^{3+}{ }_{(a q)} ; \quad E^{\circ}=+0.32 \mathrm{~V} \quad \text { not feasible. }
\end{aligned}
$$
$E^{\circ}$ for the overall reaction is positive, the reaction between Br Since 2(aq) and $\mathrm{Fe}_{2+(a q)}$ is feasible.
:::

:::

:::question{number="2.18" kind="exercise" id="q_2.18" topic="Products of electrolysis" simplified="True"}
#### Question 2.18

:::prompt
Predict the products of electrolysis in each of the following:
:::

:::part{label="(i)"}
:::prompt
An aqueous solution of $\mathrm{AgNO}_{3}$ with silver electrodes.
:::

:::

:::part{label="(ii)"}
:::prompt
An aqueous solution of $\mathrm{AgNO}_{3}$ with platinum electrodes.
:::

:::

:::part{label="(iii)"}
:::prompt
A dilute solution of $\mathrm{H}_{2} \mathrm{SO}_{4}$ with platinum electrodes.
:::

:::

:::part{label="(iv)"}
:::prompt
An aqueous solution of $\mathrm{CuCl}_{2}$ with platinum electrodes.
:::

:::

:::solution{label="Solution"}
(i) At cathode:

The following reduction reactions compete to take place at the cathode.

$$
\begin{aligned}
& \mathrm{Ag}_{(a q)}^{+}+\mathrm{e}^{-} \longrightarrow \mathrm{Ag}_{(s)} ; E^{0}=0.80 \mathrm{~V} \\
& \mathrm{H}_{(a q)}^{+}+\mathrm{e}^{-} \longrightarrow \frac{1}{2} \mathrm{H}_{2(g)} ; E^{0}=0.00 \mathrm{~V}
\end{aligned}
$$

The reaction with a higher value of $E^{\circ}$ takes place at the cathode. Therefore, deposition of silver will take place at the cathode.

At anode:
The Ag anode is attacked by $\mathrm{NO}_{3}^{-}$ions. Therefore, the silver electrode at the anode dissolves in the solution to form $\mathrm{Ag}^{+}$.
(ii) At cathode:

The following reduction reactions compete to take place at the cathode.

$$
\begin{aligned}
& \mathrm{Ag}_{(a q)}^{+}+\mathrm{e}^{-} \longrightarrow \mathrm{Ag}_{(s)} ; E^{0}=0.80 \mathrm{~V} \\
& \mathrm{H}_{(a q)}^{+}+\mathrm{e}^{-} \longrightarrow \frac{1}{2} \mathrm{H}_{2(g)} ; E^{0}=0.00 \mathrm{~V}
\end{aligned}
$$

The reaction with a higher value of $E^{\circ}$ takes place at the cathode. Therefore, deposition of silver will take place at the cathode.

At anode:
Since Pt electrodes are inert, the anode is not attacked by $\mathrm{NO}_{3}^{-}$ions. Therefore, $\mathrm{OH}^{-}$or $\mathrm{NO}_{3}^{-}$ions can be oxidized at the anode. But $\mathrm{OH}^{-}$ions have a lower discharge potential, so they get preference and decompose to liberate $\mathrm{O}_{2}$.

$$
\begin{aligned}
& \mathrm{OH}^{-} \longrightarrow \mathrm{OH}+\mathrm{e}^{-} \\
& 4 \mathrm{OH}^{-} \longrightarrow 2 \mathrm{H}_{2} \mathrm{O}+\mathrm{O}_{2}
\end{aligned}
$$

(iii) At the cathode, the following reduction reaction occurs to produce $\mathrm{H}_{2}$ gas.

$$
\mathrm{H}^{+}{ }_{(a q)}+\mathrm{e}^{-} \longrightarrow \frac{1}{2} \mathrm{H}_{2(g)}
$$

At the anode, the following processes are possible.

$$
\begin{aligned}
& 2 \mathrm{H}_{2} \mathrm{O}_{(i)} \longrightarrow \mathrm{O}_{2(g)}+4 \mathrm{H}_{(a q)}^{+}+4 \mathrm{e}^{-} ; E^{\circ}=+1.23 \mathrm{~V} \\
& 2 \mathrm{SO}_{4(a q)}^{2-} \longrightarrow \mathrm{S}_{2} \mathrm{O}_{6(a q)}^{2-}+2 \mathrm{e}^{-} ; E^{\circ}=+1.96 \mathrm{~V}
\end{aligned}
$$

For dilute sulphuric acid, reaction (i) is preferred to produce $\mathrm{O}_{2}$ gas. But for concentrated sulphuric acid, reaction (ii) occurs.
(iv) At cathode:

The following reduction reactions compete to take place at the cathode.

$$
\begin{array}{cc}
\mathrm{Cu}_{(a q)}^{2+}+2 \mathrm{e}^{-} \longrightarrow \mathrm{Cu}_{(s)} ; & E^{0}=0.34 \mathrm{~V} \\
\mathrm{H}_{(a q)}^{+}+\mathrm{e}^{-} \longrightarrow 1 / 2 \mathrm{H}_{2(g)} ; & E^{0}=0.00 \mathrm{~V}
\end{array}
$$

The reaction with a higher value of $E^{\circ}$ takes place at the cathode. Therefore, deposition of copper will take place at the cathode.
At anode:

The following oxidation reactions are possible at the anode.
At the anode, the reaction with a lower value of

$$
\begin{aligned}
& \mathrm{Cl}_{(a q)}^{-} \longrightarrow 1 / 2 \mathrm{Cl}_{2(g)}+\mathrm{e}^{-1} ; E^{0}=1.36 \mathrm{~V} \\
& 2 \mathrm{H}_{2} \mathrm{O}_{(i)} \longrightarrow \mathrm{O}_{2(g)}+4 \mathrm{H}_{(a q)}^{+}+4 \mathrm{e}^{-} ; E^{0}=+1.23 \mathrm{~V}
\end{aligned}
$$

$E^{\circ}$ is preferred. But due to the overpotential of oxygen, $\mathrm{Cl}^{-}$gets oxidized at the anode to produce $\mathrm{Cl}_{2}$ gas.
:::

:::

## Additional Questions

:::question{number="2.1" kind="additional_exercise" id="it_2.1" topic="Standard electrode potential of Mg" simplified="True" corrections_applied="1"}
#### Additional Question 2.1

:::prompt
How would you determine the standard electrode potential of the system $\mathrm{Mg}^{2+}$ | Mg?
:::

:::solution{label="Solution"}
The standard electrode potential of $\mathrm{Mg}^{2+} \mid \mathrm{Mg}$ can be measured with respect to the standard hydrogen electrode, represented by $\mathrm{Pt}_{(s)}, \mathrm{H}_{2(g)}$ (1 atm) | $\mathrm{H}^{+}{ }_{(a q)}(1 \mathrm{M})$.

We set up a cell with $\mathrm{Mg} \mid \mathrm{MgSO}_{4}(a q 1 \mathrm{M})$ as the anode and the standard hydrogen electrode as the cathode.

$$
\mathrm{Mg}\left|\mathrm{Mg}^{2+}(\mathrm{aq}, 1 \mathrm{M}) \| \mathrm{H}^{+}(\mathrm{aq}, 1 \mathrm{M})\right| \mathrm{H}_{2}(\mathrm{~g}, 1 \text { bar }), \mathrm{Pt}_{(\mathrm{s})}
$$

We then measure the emf of the cell. This measured emf is the standard electrode potential of the magnesium electrode.

$$
E^{\ominus}=E_{R}^{\ominus}-E_{L}^{\ominus}
$$

Here, $E_{R}^{\ominus}$ for the standard hydrogen electrode is zero.

$$
\begin{aligned}
& \therefore E^{\ominus}=0-E_{L}^{\ominus} \\
& =-E_{L}^{\ominus}
\end{aligned}
$$
:::

:::

:::question{number="2.2" kind="additional_exercise" id="it_2.2" topic="Zinc pot with copper sulphate" simplified="True"}
#### Additional Question 2.2

:::prompt
Can you store copper sulphate solutions in a zinc pot?
:::

:::solution{label="Solution"}
Zinc is more reactive than copper. So zinc displaces copper from its salt solution. If copper sulphate solution is stored in a zinc pot, zinc will displace the copper from it.

$$
\mathrm{Zn}+\mathrm{CuSO}_{4} \longrightarrow \mathrm{ZnSO}_{4}+\mathrm{Cu}
$$

So, copper sulphate solution cannot be stored in a zinc pot.
:::

:::

:::question{number="2.3" kind="additional_exercise" id="it_2.3" topic="Oxidising agents for ferrous ions"}
#### Additional Question 2.3

:::prompt
Consult the table of standard electrode potentials and suggest three substances that can oxidise ferrous ions under suitable conditions.
:::

:::solution{label="Solution"}
Substances that are stronger oxidising agents than ferrous ions can oxidise ferrous ions.

$$
\mathrm{Fe}^{2+} \longrightarrow \mathrm{Fe}^{3+}+\mathrm{e}^{-1} ; E^{\ominus}=-0.77 \mathrm{~V}
$$

This implies that the substances having higher reduction potentials than +0.77 V can oxidise ferrous ions to ferric ions. Three substances that can do so are $\mathrm{F}_{2}$, $\mathrm{Cl}_{2}$, and $\mathrm{O}_{2}$.
:::

:::answer
**Answer:** $\mathrm{F}_{2}$, $\mathrm{Cl}_{2}$, and $\mathrm{O}_{2}$
:::

:::

:::question{number="2.4" kind="additional_exercise" id="it_2.4" topic="Hydrogen electrode potential at pH 10"}
#### Additional Question 2.4

:::prompt
Calculate the potential of hydrogen electrode in contact with a solution whose pH is 10.
:::

:::solution{label="Solution"}
For hydrogen electrode,

$$
\mathrm{H}^{+}+\mathrm{e}^{-} \longrightarrow \frac{1}{2} \mathrm{H}_{2} \text {, it is given that } \mathrm{pH}=10
$$

$$
\therefore\left[\mathrm{H}^{+}\right]=10^{-10} \mathrm{M}
$$

Now, using Nernst equation:

$$
\begin{aligned}
& \mathrm{H}_{\left(\mathrm{H}^{+}, \frac{1}{2} \mathrm{H}_{2}\right)}=E_{\left(\mathrm{H}^{+}, \frac{1}{2} \mathrm{H}_{2}\right)}^{\ominus}-\frac{\mathrm{R} T}{n \mathrm{~F}} \ln \frac{1}{\left[\mathrm{H}^{+}\right]} \\
& =E_{\left(\mathrm{H}^{+}, \frac{1}{2} \mathrm{H}_{2}\right)}^{\ominus}-\frac{0.0591}{1} \log \frac{1}{\left[\mathrm{H}^{+}\right]} \\
& =0-\frac{0.0591}{1} \log \frac{1}{\left[10^{-10}\right]} \\
& =-0.0591 \log 10^{10} \\
& =-0.591 \mathrm{~V}
\end{aligned}
$$
:::

:::answer
**Answer:** $-0.591 \mathrm{~V}$
:::

:::

:::question{number="2.5" kind="additional_exercise" id="it_2.5" topic="EMF from Nernst equation" corrections_applied="1"}
#### Additional Question 2.5

:::prompt
Calculate the emf of the cell in which the following reaction takes place:
$$
\mathrm{Ni}(\mathrm{~s})+2 \mathrm{Ag}^{+}(0.002 \mathrm{M}) \rightarrow \mathrm{Ni}^{2+}(0.160 \mathrm{M})+2 \mathrm{Ag}(\mathrm{~s})
$$
Given that $E_{\text {cell }}^{\mathrm{o}}=1.05 \mathrm{~V}$
:::

:::solution{label="Solution"}
Applying Nernst equation we have:

$$
\begin{aligned}
& \mathrm{Ni}_{(s)}+2 \mathrm{Ag}^{+}(0.002 \mathrm{M}) \rightarrow \mathrm{Ni}^{2+}(0.160 \mathrm{M})+2 \mathrm{Ag}_{(s)} \\
& E_{(\text {cell) }}^{\ominus}=1.05 \mathrm{~V} \\
& E_{\text {(cell) }}=E_{\text {(cell) }}^{\ominus}-\frac{0.0591}{n} \log \frac{\left[\mathrm{Ni}^{2+}\right]}{\left[\mathrm{Ag}^{+}\right]^{2}} \\
& =1.05-\frac{0.0591}{2} \log \frac{(0.160)}{(0.002)^{2}} \\
& =1.05-0.02955 \log \frac{0.16}{0.000004} \\
& =1.05-0.02955 \log 4 \times 10^{4} \\
& =1.05-0.02955(\log 10000+\log 4) \\
& =1.05-0.02955(4+0.6021) \\
& =0.914 \mathrm{~V}
\end{aligned}
$$
:::

:::answer
**Answer:** $0.914 \mathrm{~V}$
:::

:::

:::question{number="2.6" kind="additional_exercise" id="it_2.6" topic="Gibbs energy and equilibrium constant"}
#### Additional Question 2.6

:::prompt
The cell in which the following reaction occurs:
$$
2 \mathrm{Fe}^{3+}(\mathrm{aq})+2 \mathrm{I}^{-}(\mathrm{aq}) \rightarrow 2 \mathrm{Fe}^{2+}(\mathrm{aq})+\mathrm{I}_{2}(\mathrm{~s}) \text { has } E_{\text {cell }}^{\mathrm{o}}=0.236 \mathrm{~V} \text { at } 298 \mathrm{~K} .
$$
Calculate the standard Gibbs energy and the equilibrium constant of the cell reaction.
:::

:::solution{label="Solution"}
$$
\text { Here, } n=2, E_{\text {cell }}^{\ominus}=0.236 \mathrm{~V}, \mathrm{~T}=298 \mathrm{~K}
$$

We know that:

$$
\begin{aligned}
& \Delta_{r} \mathrm{G}^{\ominus}=-n \mathrm{FE}_{\mathrm{cell}}^{\ominus} \\
& =-2 \times 96487 \times 0.236 \\
& =-45541.864 \mathrm{~J} \mathrm{~mol}^{-1} \\
& =-45.54 \mathrm{~kJ} \mathrm{~mol}^{-1}
\end{aligned}
$$

Again, $\Delta_{r} G^{\ominus}=-2.303 \mathrm{R} T \log K_{\mathrm{c}}$

$$
\begin{aligned}
& \Rightarrow \log K_{\mathrm{c}}=-\frac{\Delta_{r} G^{\ominus}}{2.303 \mathrm{R} T} \\
& \quad=-\frac{-45.54 \times 10^{3}}{2.303 \times 8.314 \times 298} \\
& =7.981 \\
& \therefore K_{\mathrm{c}}=\text { Antilog }(7.981) \\
& =9.57 \times 10^{7}
\end{aligned}
$$
:::

:::answer
**Answer:** $\Delta_{r}G^{\ominus} = -45.54 \mathrm{~kJ} \mathrm{~mol}^{-1}$; $K_{c} = 9.57 \times 10^{7}$
:::

:::

:::question{number="2.7" kind="additional_exercise" id="it_2.7" topic="Conductivity and dilution"}
#### Additional Question 2.7

:::prompt
Why does the conductivity of a solution decrease with dilution?
:::

:::solution{label="Solution"}
The conductivity of a solution is the conductance of ions present in a unit volume of the solution. The number of ions (responsible for carrying current) decreases when the solution is diluted. As a result, the conductivity of a solution decreases with dilution.
:::

:::

:::question{number="2.8" kind="additional_exercise" id="it_2.8" topic="Limiting molar conductivity of water" corrections_applied="1"}
#### Additional Question 2.8

:::prompt
Suggest a way to determine the $\Lambda_{m}^{\circ}$ value of water.
:::

:::solution{label="Solution"}
Applying Kohlrausch's law of independent migration of ions, the $\Lambda^{0}$ value of water can be determined as follows:

$$
\begin{aligned}
\Lambda_{m\left(\mathrm{H}_{2} \mathrm{O}\right)}^{0} & =\lambda_{\mathrm{H}^{+}}^{0}+\lambda_{\mathrm{OH}}^{0} \\
& =\left(\lambda_{\mathrm{H}^{+}}^{0}+\lambda_{\mathrm{Cl}^{-}}^{0}\right)+\left(\lambda_{\mathrm{Na}^{+}}^{0}+\lambda_{\mathrm{OH}^{-}}^{0}\right)-\left(\lambda_{\mathrm{Na}^{+}}^{0}+\lambda_{\mathrm{Cl}^{-}}^{0}\right) \\
\Lambda_{m(\mathrm{HCl})}^{0} & +\Lambda_{m(\mathrm{NaOH})}^{0}-\Lambda_{m(\mathrm{NaCl})}^{0}
\end{aligned}
$$

$$
\Lambda_{m}^{0}
$$

Hence, by knowing the values of $\mathrm{HCl}, \mathrm{NaOH}$, and NaCl , the $\Lambda_{m}^{0}$ value of water can be determined.
:::

:::

:::question{number="2.9" kind="additional_exercise" id="it_2.9" topic="Degree of dissociation of methanoic acid"}
#### Additional Question 2.9

:::prompt
The molar conductivity of $0.025 \mathrm{~mol} \mathrm{~L}^{-1}$ methanoic acid is $46.1 \mathrm{~S} \mathrm{~cm}^{2} \mathrm{~mol}^{-1}$. Calculate its degree of dissociation and dissociation constant. Given $\lambda^{0}\left(\mathrm{H}^{+}\right)$ $=349.6 \mathrm{~S} \mathrm{~cm}^{2} \mathrm{~mol}^{-1}$ and $\lambda^{0}\left(\mathrm{HCOO}^{-}\right)=54.6 \mathrm{~S} \mathrm{~cm}^{2} \mathrm{~mol}^{-1}$.
:::

:::solution{label="Solution"}
$$
\begin{aligned}
& C=0.025 \mathrm{~mol} \mathrm{~L}^{-1} \\
& \Lambda_{m}=46.1 \mathrm{~S} \mathrm{~cm}^{2} \mathrm{~mol}^{-1} \\
& \begin{aligned}
& \lambda^{0}\left(\mathrm{H}^{+}\right)=349.6 \mathrm{~S} \mathrm{~cm}^{2} \mathrm{~mol}^{-1} \\
& \lambda^{0}(\mathrm{HCOO}-)=54.6 \mathrm{Scm}^{2} \mathrm{~mol}^{-1} \\
& \Lambda_{m}^{0}(\mathrm{HCOOH})=\lambda^{0}\left(\mathrm{H}^{+}\right)+\lambda^{0}\left(\mathrm{HCOO}^{-}\right) \\
&=349.6+54.6 \\
&=404.2 \mathrm{Scm}^{2} \mathrm{~mol}^{-1}
\end{aligned}
\end{aligned}
$$

Now, degree of dissociation:

$$
\begin{aligned}
\alpha & =\frac{\Lambda_{m}(\mathrm{HCOOH})}{\Lambda_{m}^{0}(\mathrm{HCOOH})} \\
& =\frac{46.1}{404.2} \\
& =0.114(\text { approximately })
\end{aligned}
$$

Thus, dissociation constant:

$$
\begin{aligned}
K & =\frac{c \propto c^{2}}{(1-\propto)} \\
& =\frac{\left(0.025 \mathrm{~mol} \mathrm{~L}^{-1}\right)(0.114)^{2}}{(1-0.114)} \\
& =3.67 \times 10^{-4} \mathrm{~mol} \mathrm{~L}^{-1}
\end{aligned}
$$
:::

:::answer
**Answer:** $\alpha = 0.114$ (approximately); $K = 3.67 \times 10^{-4} \mathrm{~mol} \mathrm{~L}^{-1}$
:::

:::

:::question{number="2.10" kind="additional_exercise" id="it_2.10" topic="Electrons from current and time" simplified="True"}
#### Additional Question 2.10

:::prompt
If a current of 0.5 ampere flows through a metallic wire for 2 hours, then how many electrons would flow through the wire?
:::

:::solution{label="Solution"}
The current is:

$$
\begin{aligned}
& =0.5 \mathrm{~A} \\
& t=2 \text { hours }=2 \times 60 \times 60 \mathrm{~s}=7200 \mathrm{~s}
\end{aligned}
$$

Thus, $Q=I t$

$$
\begin{aligned}
& =0.5 \mathrm{~A} \times 7200 \mathrm{~s} \\
& =3600 \mathrm{C}
\end{aligned}
$$

We know that $96487 \mathrm{C}=6.023 \times 10^{23}$ gives the number of electrons. So:

$$
\begin{aligned}
3600 \mathrm{C} & =\frac{6.023 \times 10^{23} \times 3600}{96487} \text { number of electrons } \\
& =2.25 \times 10^{22} \text { number of electrons }
\end{aligned}
$$

Hence, $2.25 \times 10^{22}$ number of electrons will flow through the wire.
:::

:::answer
**Answer:** $2.25 \times 10^{22}$ electrons
:::

:::

:::question{number="2.11" kind="additional_exercise" id="it_2.11" topic="Metals extracted electrolytically"}
#### Additional Question 2.11

:::prompt
Suggest a list of metals that are extracted electrolytically.
:::

:::solution{label="Solution"}
Metals that are on the top of the reactivity series such as sodium, potassium, calcium, lithium, magnesium, aluminium are extracted electrolytically.
:::

:::answer
**Answer:** Sodium, potassium, calcium, lithium, magnesium, aluminium
:::

:::

:::question{number="2.12" kind="additional_exercise" id="it_2.12" topic="Charge to reduce dichromate"}
#### Additional Question 2.12

:::prompt
Consider the reaction: $\mathrm{Cr}_{2} \mathrm{O}_{7}{ }^{2-}+14 \mathrm{H}^{+}+6 \mathrm{e}^{-} \rightarrow 2 \mathrm{Cr}^{3+}+7 \mathrm{H}_{2} \mathrm{O}$
What is the quantity of electricity in coulombs needed to reduce 1 mol of $\mathrm{Cr}_{2} \mathrm{O}_{7}{ }^{2-}$ ?
:::

:::solution{label="Solution"}
The given reaction is as follows:

$$
\begin{aligned}
& \mathrm{Cr}_{2} \mathrm{O}_{7}^{2-}+14 \mathrm{H}^{+}+6 \mathrm{e}^{-} \rightarrow 2 \mathrm{Cr}^{3+}+7 \mathrm{H}_{2} \mathrm{O} \text {, the required quantity of electricity will } \\
& \text { Therefore, to reduce } 1 \text { mole of } \mathrm{Cr}_{2} \mathrm{O}_{7}^{2-}=6 \mathrm{~F} \\
& =6 \times 96487 \mathrm{C} \\
& =578922 \mathrm{C}
\end{aligned}
$$
:::

:::answer
**Answer:** $578922 \mathrm{C}$ (6 F)
:::

:::

:::question{number="2.13" kind="additional_exercise" id="it_2.13" topic="Recharging lead storage battery"}
#### Additional Question 2.13

:::prompt
Write the chemistry of recharging the lead storage battery, highlighting all the materials that are involved during recharging.
:::

:::

:::question{number="2.14" kind="additional_exercise" id="it_2.14" topic="Alternative fuel cell materials"}
#### Additional Question 2.14

:::prompt
Suggest two materials other than hydrogen that can be used as fuels in fuel cells.
:::

:::solution{label="Solution"}
Methane and methanol can be used as fuels in fuel cells.
:::

:::answer
**Answer:** Methane and methanol
:::

:::

:::question{number="2.15" kind="additional_exercise" id="it_2.15" topic="Rusting as electrochemical cell" simplified="True"}
#### Additional Question 2.15

:::prompt
Explain how rusting of iron is envisaged as setting up of an electrochemical cell.
:::

:::solution{label="Solution"}
In corrosion, air and moisture cause oxidation at one spot on an iron object. This spot acts as the anode. The anode reaction is:

$$
\mathrm{Fe}_{(s)} \longrightarrow \mathrm{Fe}_{(a q)}^{2+}+2 \mathrm{e}^{-}
$$

Electrons released at this anodic spot travel through the metal to another spot on the same object.

At that spot, in the presence of $\mathrm{H}^{+}$ ions, the electrons reduce oxygen. This spot acts as the cathode. These $\mathrm{H}^{+}$ ions come either from $\mathrm{H}_{2} \mathrm{CO}_{3}$, formed when carbon dioxide from air dissolves in water, or from other acidic oxides in the atmosphere dissolving in water.

The cathode reaction is:

$$
\mathrm{O}_{2(\mathrm{~g})}+4 \mathrm{H}_{(a q)}^{+}+4 \mathrm{e}^{-} \longrightarrow 2 \mathrm{H}_{2} \mathrm{O}_{(l)}
$$

The overall reaction is:

$$
2 \mathrm{Fe}_{(s)}+\mathrm{O}_{2(g)}+4 \mathrm{H}_{(a q)}^{+} \longrightarrow 2 \mathrm{Fe}_{(a q)}^{2+}+2 \mathrm{H}_{2} \mathrm{O}_{(l)}
$$

Atmospheric oxygen then oxidises the ferrous ions further to ferric ions. These ferric ions combine with moisture in the surroundings to form hydrated ferric oxide, $\left(\mathrm{Fe}_{2} \mathrm{O}_{3}, x \mathrm{H}_{2} \mathrm{O}\right)_{\text {i.e., rust. }}$.

So, rusting of iron can be seen as the setting up of an electrochemical cell.
:::

:::
