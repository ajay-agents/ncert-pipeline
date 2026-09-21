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

:::example{number="2.6" kind="example" id="ex_2.6" topic="Limiting molar conductivity of KCl by extrapolation"}
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
Taking the square root of concentration we obtain:

$$
\begin{array}{cc}
\boldsymbol{c}^{\mathbf{1 / 2}} /\left(\mathbf{m o l ~ L}^{-\mathbf{1}}\right)^{\mathbf{1 / 2}} & \Lambda \boldsymbol{m} / \mathbf{S} \mathbf{c m}^{\mathbf{2}} \mathbf{m o l}^{\mathbf{- 1}} \\
0.01407 & 148.61 \\
0.01758 & 148.29 \\
0.02283 & 147.81 \\
0.03145 & 147.09
\end{array}
$$

A plot of $\Lambda_{m}$ ( y -axis) and $\mathrm{c}^{1 / 2}$ ( $x$-axis) is shown in (Fig. 3.7). It can be seen that it is nearly a straight line. From the intercept $\left(c^{1 / 2}=0\right)$, we find that

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

:::example{number="2.7" kind="example" id="ex_2.7" topic="Limiting molar conductivity via Kohlrausch's law"}
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
\Lambda_{m\left(\mathrm{MgSO}_{4}\right)}^{o} & =\lambda_{\mathrm{Mg}^{2+}}^{o}+\lambda_{\mathrm{So}_{4}^{2-}}^{o}=106.0 \mathrm{~S} \mathrm{~cm}^{2} \mathrm{~mol}^{-1}+160.0 \mathrm{~S} \mathrm{~cm}^{2} \mathrm{~mol}^{-1} \\
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
