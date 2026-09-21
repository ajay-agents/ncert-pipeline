---
subject: chemistry
class: 12
chapter: 3
lang: en
title: "Chemical Kinetics"
---

# Chemical Kinetics

## Examples

:::example{number="3.1" kind="example" id="ex_3.1" topic="Average and instantaneous rate from concentration data" corrections_applied="3"}
#### Example 3.1

:::prompt
From the concentrations of $\mathrm{C}_{4} \mathrm{H}_{9} \mathrm{Cl}$ (butyl chloride) at different times given below, calculate the average rate of the reaction:

$$
\mathrm{C}_{4} \mathrm{H}_{9} \mathrm{Cl}+\mathrm{H}_{2} \mathrm{O} \rightarrow \mathrm{C}_{4} \mathrm{H}_{9} \mathrm{OH}+\mathrm{HCl}
$$

during different intervals of time.

| t/s | 0 | 50 | 100 | 150 | 200 | 300 | 400 | 700 | 800 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| $\left[\mathrm{C}_{4} \mathrm{H}_{9} \mathrm{Cl}\right] / \mathrm{mol} \mathrm{L}^{-1}$ | 0.100 | 0.0905 | 0.0820 | 0.0741 | 0.0671 | 0.0549 | 0.0439 | 0.0210 | 0.017 |
:::

:::solution{label="Solution"}
We can determine the difference in concentration over different intervals of time and thus determine the average rate by dividing $\Delta[\mathrm{R}]$ by $\Delta t$ (Table 3.1).

Table 3.1: Average rates of hydrolysis of butyl chloride
| $\left[\mathrm{C}_{4} \mathrm{H}_{9} \mathrm{CI}\right]_{t_{1}} / \mathrm{mol} \mathrm{L}^{-1}$ | $\left[\mathrm{C}_{4} \mathrm{H}_{9} \mathrm{CI}\right]_{t_{2}} / \mathbf{m o l ~ L}^{\boldsymbol{-} \mathbf{1}}$ | $t_{1} / \mathrm{s}$ | $t_{2} / \mathrm{s}$ | $\begin{aligned} & r_{\mathrm{av}} \times 10^{4} / \mathrm{mol} \mathrm{~L}^{-1} \mathrm{~s}^{-1} \\ & =-\left\{\left[\mathrm{C}_{4} \mathrm{H}_{9} \mathrm{Cl}\right]_{\mathrm{t}_{2}}-\left[\mathrm{C}_{4} \mathrm{H}_{9} \mathrm{Cl}\right]_{\mathrm{t}_{1}} /\left(\mathrm{t}_{2}-\mathrm{t}_{1}\right)\right\} \times 10^{4} \end{aligned}$ |
| :--- | :--- | :--- | :--- | :--- |
| 0.100 | 0.0905 | 0 | 50 | 1.90 |
| 0.0905 | 0.0820 | 50 | 100 | 1.70 |
| 0.0820 | 0.0741 | 100 | 150 | 1.58 |
| 0.0741 | 0.0671 | 150 | 200 | 1.40 |
| 0.0671 | 0.0549 | 200 | 300 | 1.22 |
| 0.0549 | 0.0439 | 300 | 400 | 1.10 |
| 0.0439 | 0.0335 | 400 | 500 | 1.04 |
| 0.0210 | 0.017 | 700 | 800 | 0.4 |


It can be seen (Table 3.1) that the average rate falls from $1.90 \times 10^{-4} \mathrm{~mol} \mathrm{~L}^{-1} \mathrm{~s}^{-1}$ to $0.4 \times 10^{-4} \mathrm{~mol} \mathrm{~L}^{-1} \mathrm{~s}^{-1}$. However, average rate cannot be used to predict the rate of a reaction at a particular instant as it would be constant for the time interval for which it is calculated. So, to express the rate at a particular moment of time we determine the instantaneous rate. It is obtained when we consider the average rate at the smallest time interval say d$t$ (i.e. when $\Delta t$ approaches zero). Hence, mathematically for an infinitesimally small d$t$ instantaneous rate is given by

$$
r_{\mathrm{av}}=\frac{-\Delta[\mathrm{R}]}{\Delta t}=\frac{\Delta[\mathrm{P}]}{\Delta t} \quad (3.3)
$$

As $\Delta t \rightarrow 0$ or $\quad r_{\text {inst }}=\frac{-\mathrm{d}[\mathrm{R}]}{\mathrm{d} t}=\frac{\mathrm{d}[\mathrm{P}]}{\mathrm{d} t}$

![](images/fig_3_18.jpg)
Fig 3.2
Instantaneous rate of hydrolysis of butyl chloride $\left(\mathrm{C}_{4} \mathrm{H}_{9} \mathrm{Cl}\right)$

It can be determined graphically by drawing a tangent at time t on either of the curves for concentration of R and P vs time t and calculating its slope (Fig. 3.1). So in problem 3.1, $r_{\text {inst }}$ at 600s for example, can be calculated by plotting concentration of butyl chloride as a function of time. A tangent is drawn that touches the curve at $t=600 \mathrm{~s}$ (Fig. 3.2).

The slope of this tangent gives the instantaneous rate.

$$
\begin{aligned}
& \text { So, } r_{\text {inst }} \text { at } 600 \mathrm{~s}=-\left(\frac{0.0165-0.037}{(800-400) \mathrm{s}}\right) \mathrm{mol} \mathrm{~L}^{-1}=5.12 \times 10^{-5} \mathrm{~mol} \mathrm{~L}^{-1} \mathrm{~s}^{-1} \\
& \text { At } t=250 \mathrm{~s} \quad r_{\text {inst }}=1.22 \times 10^{-4} \mathrm{~mol} \mathrm{~L}^{-1} \mathrm{~s}^{-1} \\
& t=350 \mathrm{~s} \quad r_{\text {inst }}=1.0 \times 10^{-4} \mathrm{~mol} \mathrm{~L}^{-1} \mathrm{~s}^{-1} \\
& t=450 \mathrm{~s} \quad r_{\text {inst }}=6.4 \times 10^{-5} \mathrm{~mol} \mathrm{~L}^{-1} \mathrm{~s}^{-1}
\end{aligned}
$$
:::

:::

:::example{number="3.2" kind="example" id="ex_3.2" topic="Average rate of N2O5 decomposition in different time units" corrections_applied="1"}
#### Example 3.2

:::prompt
The decomposition of $\mathrm{N}_{2} \mathrm{O}_{5}$ in $\mathrm{CCl}_{4}$ at 318K has been studied by monitoring the concentration of $\mathrm{N}_{2} \mathrm{O}_{5}$ in the solution. Initially the concentration of $\mathrm{N}_{2} \mathrm{O}_{5}$ is $2.33 \mathrm{~mol} \mathrm{~L}^{-1}$ and after 184 minutes, it is reduced to $2.08 \mathrm{~mol} \mathrm{~L}^{-1}$. The reaction takes place according to the equation

$$
2 \mathrm{~N}_{2} \mathrm{O}_{5}(\mathrm{~g}) \rightarrow 4 \mathrm{NO}_{2}(\mathrm{~g})+\mathrm{O}_{2}(\mathrm{~g})
$$

Calculate the average rate of this reaction in terms of hours, minutes and seconds. What is the rate of production of $\mathrm{NO}_{2}$ during this period?
:::

:::solution{label="Solution"}
$$
\begin{aligned}
& \text { Average Rate }=\frac{1}{2}-\frac{\Delta\left[\mathrm{N}_{2} \mathrm{O}_{5}\right]}{\Delta t}=-\frac{1}{2} \frac{(2.08-2.33) \mathrm{mol} \mathrm{~L}^{-1}}{184 \mathrm{~min}} \\
& =6.79 \times 10^{-4} \mathrm{~mol} \mathrm{~L}^{-1} / \mathrm{min}=\left(6.79 \times 10^{-4} \mathrm{~mol} \mathrm{~L}^{-1} \mathrm{~min}^{-1}\right) \times(60 \mathrm{~min} / 1 \mathrm{~h}) \\
& =4.07 \times 10^{-2} \mathrm{~mol} \mathrm{~L}^{-1} / \mathrm{h} \\
& =6.79 \times 10^{-4} \mathrm{~mol} \mathrm{~L}^{-1} \times 1 \mathrm{~min} / 60 \mathrm{~s} \\
& =1.13 \times 10^{-5} \mathrm{~mol} \mathrm{~L}^{-1} \mathrm{~s}^{-1}
\end{aligned}
$$

It may be remembered that

$$
\begin{aligned}
& \text { Rate }=\frac{1}{4} \frac{\Delta\left[\mathrm{NO}_{2}\right]}{\Delta t} \\
\frac{\Delta\left[\mathrm{NO}_{2}\right]}{\Delta t} & =6.79 \times 10^{-4} \times 4 \mathrm{~mol} \mathrm{~L}^{-1} \mathrm{~min}^{-1}=2.72 \times 10^{-3} \mathrm{~mol} \mathrm{~L}^{-1} \mathrm{~min}^{-1}
\end{aligned}
$$
:::

:::answer
**Answer:** Average rate $=4.07 \times 10^{-2} \mathrm{~mol} \mathrm{~L}^{-1} \mathrm{~h}^{-1}=6.79 \times 10^{-4} \mathrm{~mol} \mathrm{~L}^{-1} \mathrm{~min}^{-1}=1.13 \times 10^{-5} \mathrm{~mol} \mathrm{~L}^{-1} \mathrm{~s}^{-1}$; rate of production of $\mathrm{NO}_{2}=2.72 \times 10^{-3} \mathrm{~mol} \mathrm{~L}^{-1} \mathrm{~min}^{-1}$
:::

:::

:::example{number="3.3" kind="example" id="ex_3.3" topic="Overall order from a fractional rate expression"}
#### Example 3.3

:::prompt
Calculate the overall order of a reaction which has the rate expression
:::

:::part{label="(a)"}
:::prompt
Rate $=k[\mathrm{~A}]^{1 / 2}[\mathrm{~B}]^{3 / 2}$
:::

:::solution
Rate $=k[\mathrm{~A}]^{\mathrm{x}}[\mathrm{B}]^{\mathrm{y}}$
order $=\mathrm{x}+\mathrm{y}$
So order $=1 / 2+3 / 2=2$, i.e., second order
:::

:::answer
**Answer:** Second order
:::

:::

:::part{label="(b)"}
:::prompt
Rate $=k[\mathrm{~A}]^{3 / 2}[\mathrm{~B}]^{-1}$
:::

:::solution
order $=3 / 2+(-1)=1 / 2$, i.e., half order.
:::

:::answer
**Answer:** Half order
:::

:::

:::

:::example{number="3.4" kind="example" id="ex_3.4" topic="Reaction order from rate constant units"}
#### Example 3.4

:::prompt
Identify the reaction order from each of the following rate constants.
:::

:::part{label="(i)"}
:::prompt
$k=2.3 \times 10^{-5} \mathrm{~L} \mathrm{~mol}^{-1} \mathrm{~s}^{-1}$
:::

:::solution
The unit of second order rate constant is $\mathrm{L} \mathrm{mol}^{-1} \mathrm{~s}^{-1}$, therefore $k=2.3 \times 10^{-5} \mathrm{~L} \mathrm{~mol}^{-1} \mathrm{~s}^{-1}$ represents a second order reaction.
:::

:::answer
**Answer:** Second order reaction
:::

:::

:::part{label="(ii)"}
:::prompt
$k=3 \times 10^{-4} \mathrm{~s}^{-1}$
:::

:::solution
The unit of a first order rate constant is $\mathrm{s}^{-1}$ therefore $k=3 \times 10^{-4} \mathrm{~s}^{-1}$ represents a first order reaction.
:::

:::answer
**Answer:** First order reaction
:::

:::

:::

:::example{number="3.5" kind="example" id="ex_3.5" topic="Rate constant of first order N2O5 decomposition"}
#### Example 3.5

:::prompt
The initial concentration of $\mathrm{N}_{2} \mathrm{O}_{5}$ in the following first order reaction $\mathrm{N}_{2} \mathrm{O}_{5}(\mathrm{~g}) \rightarrow 2 \mathrm{NO}_{2}(\mathrm{~g})+1 / 2 \mathrm{O}_{2}(\mathrm{~g})$ was $1.24 \times 10^{-2} \mathrm{~mol} \mathrm{~L}^{-1}$ at 318 K. The concentration of $\mathrm{N}_{2} \mathrm{O}_{5}$ after 60 minutes was $0.20 \times 10^{-2} \mathrm{~mol} \mathrm{~L}^{-1}$. Calculate the rate constant of the reaction at 318 K.
:::

:::solution{label="Solution"}
For a first order reaction

$$
\begin{aligned}
\log \frac{[\mathrm{R}]_{1}}{[\mathrm{R}]_{2}} & =\frac{k\left(t_{2}-t_{1}\right)}{2.303} \\
k & =\frac{2.303}{\left(t_{2}-t_{1}\right)} \log \frac{[R]_{1}}{[R]_{2}} \\
& =\frac{2.303}{(60 \mathrm{~min}-0 \mathrm{~min})} \log \frac{1.24 \times 10^{-2} \mathrm{~mol} \mathrm{~L}^{-1}}{0.20 \times 10^{-2} \mathrm{~mol} \mathrm{~L}^{-1}} \\
& =\frac{2.303}{60} \log 6.2 \mathrm{~min}^{-1} \\
k & =0.0304 \mathrm{~min}^{-1}
\end{aligned}
$$
:::

:::answer
**Answer:** $k=0.0304 \mathrm{~min}^{-1}$
:::

:::

:::example{number="3.6" kind="example" id="ex_3.6" topic="Rate constant from total pressure data"}
#### Example 3.6

:::prompt
The following data were obtained during the first order thermal decomposition of $\mathrm{N}_{2} \mathrm{O}_{5}(\mathrm{g})$ at constant volume:

| $2 \mathrm{~N}_{2} \mathrm{O}_{5}(\mathrm{~g}) \rightarrow 2 \mathrm{~N}_{2} \mathrm{O}_{4}(\mathrm{~g})+\mathrm{O}_{2}(\mathrm{~g})$ |
| :--- |


| S.No. | Time/s | Total Pressure/(atm) |
| :--- | :--- | :--- |
| 1. | 0 | 0.5 |
| 2. | 100 | 0.512 |

Calculate the rate constant.
:::

:::solution{label="Solution"}
Let the pressure of $\mathrm{N}_{2} \mathrm{O}_{5}(\mathrm{g})$ decrease by 2x atm. As two moles of $\mathrm{N}_{2} \mathrm{O}_{5}$ decompose to give two moles of $\mathrm{N}_{2} \mathrm{O}_{4}(\mathrm{g})$ and one mole of $\mathrm{O}_{2}(\mathrm{g})$, the pressure of $\mathrm{N}_{2} \mathrm{O}_{4}(\mathrm{g})$ increases by 2 x atm and that of $\mathrm{O}_{2}(\mathrm{g})$ increases by x atm.

|  | $2 \mathrm{~N}_{2} \mathrm{O}_{5}(\mathrm{~g})$ | → | $2 \mathrm{~N}_{2} \mathrm{O}_{4}(\mathrm{~g})$ | + | $\mathrm{O}_{2}(\mathrm{~g})$ |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Start $t=0$ | 0.5 atm |  | 0 atm |  | 0 atm |
| At time $t$ | (0.5-2x) atm |  | 2x atm |  | x atm |

$$
\begin{aligned}
p_{t} & =p_{\mathrm{N}_{2} \mathrm{O}_{5}}+p_{\mathrm{N}_{2} \mathrm{O}_{4}}+p_{\mathrm{O}_{2}} \\
& =(0.5-2 \mathrm{x})+2 \mathrm{x}+\mathrm{x}=0.5+\mathrm{x} \\
\mathrm{x} & =p_{t}-0.5
\end{aligned}
$$

$$
\begin{aligned}
p_{\mathrm{N}_{2} \mathrm{O}_{5}} & =0.5-2 \mathrm{x} \\
& =0.5-2\left(p_{\mathrm{t}}-0.5\right)=1.5-2 p_{t}
\end{aligned}
$$

At $\quad t=100 \mathrm{~s} ; p_{\mathrm{t}}=0.512 \mathrm{~atm}$

$$
p_{\mathrm{N}_{2} \mathrm{O}_{5}}=1.5-2 \times 0.512=0.476 \mathrm{~atm}
$$

Using equation (3.16)

$$
\begin{aligned}
k & =\frac{2.303}{t} \log \frac{p_{\mathrm{i}}}{p_{\mathrm{A}}}=\frac{2.303}{100 \mathrm{~s}} \log \frac{0.5 \mathrm{~atm}}{0.476 \mathrm{~atm}} \\
& =\frac{2.303}{100 \mathrm{~s}} \times 0.0216=4.98 \times 10^{-4} \mathrm{~s}^{-1}
\end{aligned}
$$
:::

:::answer
**Answer:** $k=4.98 \times 10^{-4} \mathrm{~s}^{-1}$
:::

:::

:::example{number="3.7" kind="example" id="ex_3.7" topic="Half-life of a first order reaction"}
#### Example 3.7

:::prompt
A first order reaction is found to have a rate constant, $k=5.5 \times 10^{-14} \mathrm{~s}^{-1}$. Find the half-life of the reaction.
:::

:::solution{label="Solution"}
Half-life for a first order reaction is

$$
\begin{aligned}
t_{1 / 2} & =\frac{0.693}{k} \\
t_{1 / 2} & =\frac{0.693}{5.5 \times 10^{-14} \mathrm{~s}^{-1}}=1.26 \times 10^{13} \mathrm{~s}
\end{aligned}
$$
:::

:::answer
**Answer:** $t_{1/2}=1.26 \times 10^{13} \mathrm{~s}$
:::

:::

:::example{number="3.8" kind="example" id="ex_3.8" topic="Proof: 99.9% completion time versus half-life"}
#### Example 3.8

:::prompt
Show that in a first order reaction, time required for completion of 99.9\% is 10 times of half-life ( $t_{1 / 2}$ ) of the reaction.
:::

:::solution{label="Solution"}
When reaction is completed $99.9 \%,[\mathrm{R}]_{\mathrm{n}}=[\mathrm{R}]_{0}-0.999[\mathrm{R}]_{0}$

$$
\begin{aligned}
k & =\frac{2.303}{t} \log \frac{[\mathrm{R}]_{0}}{[\mathrm{R}]} \\
& =\frac{2.303}{t} \log \frac{[\mathrm{R}]_{0}}{[\mathrm{R}]_{0}-0.999[\mathrm{R}]_{0}}=\frac{2.303}{t} \log 10^{3} \\
t & =6.909 / k
\end{aligned}
$$

For half-life of the reaction

$$
\begin{aligned}
t_{1 / 2} & =0.693 / k \\
\frac{t}{t_{1 / 2}} & =\frac{6.909}{k} \times \frac{k}{0.693}=10
\end{aligned}
$$
:::

:::

:::example{number="3.9" kind="example" id="ex_3.9" topic="Activation energy and Arrhenius factor from two temperatures"}
#### Example 3.9

:::prompt
The rate constants of a reaction at 500K and 700K are $0.02 \mathrm{~s}^{-1}$ and $0.07 \mathrm{~s}^{-1}$ respectively. Calculate the values of $E_{\mathrm{a}}$ and $A$.
:::

:::solution{label="Solution"}
$$
\begin{aligned}
\log \frac{k_{2}}{k_{1}} & =\frac{E_{\mathrm{a}}}{2.303 R}\left[\frac{T_{2}-T_{1}}{T_{1} T_{2}}\right] \\
\log \frac{0.07}{0.02} & =\left(\frac{E_{\mathrm{a}}}{2.303 \times 8.314 \mathrm{JK}^{-1} \mathrm{~mol}^{-1}}\right)\left[\frac{700-500}{700 \times 500}\right] \\
0.544 & =E_{\mathrm{a}} \times 5.714 \times 10^{-4} / 19.15 \\
E_{\mathrm{a}} & =0.544 \times 19.15 / 5.714 \times 10^{-4}=18230.8 \mathrm{~J} \\
k & =A \mathrm{e}^{-E a / R T} \\
0.02 & =A \mathrm{e}^{-18230.8 / 8.314 \times 500} \\
A & =0.02 / 0.012=1.61
\end{aligned}
$$
:::

:::answer
**Answer:** $E_{\mathrm{a}}=18230.8 \mathrm{~J}$; $A=1.61$
:::

:::

:::example{number="3.10" kind="example" id="ex_3.10" topic="Rate constant of ethyl iodide decomposition at a new temperature" corrections_applied="1"}
#### Example 3.10

:::prompt
The first order rate constant for the decomposition of ethyl iodide by the reaction

$$
\mathrm{C}_{2} \mathrm{H}_{5} \mathrm{I}(\mathrm{~g}) \rightarrow \mathrm{C}_{2} \mathrm{H}_{4}(\mathrm{~g})+\mathrm{HI}(\mathrm{~g})
$$

at 600K is $1.60 \times 10^{-5} \mathrm{~s}^{-1}$. Its energy of activation is 209 kJ/mol. Calculate the rate constant of the reaction at 700K.
:::

:::solution{label="Solution"}
We know that

$$
\log k_{2}-\log k_{1}=\frac{E_{\mathrm{a}}}{2.303 R}\left[\frac{1}{T_{1}}-\frac{1}{T_{2}}\right]
$$

$$
\begin{aligned}
\log k_{2} & =\log k_{1}+\frac{E_{\mathrm{a}}}{2.303 R}\left[\frac{1}{T_{1}}-\frac{1}{T_{2}}\right] \\
& =\log \left(1.60 \times 10^{-5}\right)+\frac{209000 \mathrm{~J} \mathrm{~mol} \mathrm{~L}^{-1}}{2.303 \times 8.314 \mathrm{~J} \mathrm{~mol} \mathrm{~L}^{-1} \mathrm{~K}^{-1}}\left[\frac{1}{600 \mathrm{~K}}-\frac{1}{700 \mathrm{~K}}\right]
\end{aligned}
$$

$$
\log k_{2}=-4.796+2.599=-2.197
$$

$$
k_{2}=6.36 \times 10^{-3} \mathrm{~s}^{-1}
$$
:::

:::answer
**Answer:** $k_2 = 6.36 \times 10^{-3} \mathrm{~s}^{-1}$
:::

:::

## Questions and Solutions

:::question{number="3.1" kind="exercise" id="q_3.1" topic="Order and rate constant dimensions"}
#### Question 3.1

:::prompt
From the rate expression for the following reactions, determine their order of reaction and the dimensions of the rate constants.
:::

:::part{label="(i)"}
:::prompt
$3 \mathrm{NO}(\mathrm{g}) \rightarrow \mathrm{N}_{2} \mathrm{O}(\mathrm{g}) \quad$ Rate $=k[\mathrm{NO}]^{2}$
:::

:::

:::part{label="(ii)"}
:::prompt
$\mathrm{H}_{2} \mathrm{O}_{2}(\mathrm{aq})+3 \mathrm{I}^{-}(\mathrm{aq})+2 \mathrm{H}^{+} \rightarrow 2 \mathrm{H}_{2} \mathrm{O}(\mathrm{l})+\mathrm{I}_{3}^{-} \quad$ Rate $=k\left[\mathrm{H}_{2} \mathrm{O}_{2}\right]\left[\mathrm{I}^{-}\right]$
:::

:::

:::part{label="(iii)"}
:::prompt
$\mathrm{CH}_{3} \mathrm{CHO}(\mathrm{g}) \rightarrow \mathrm{CH}_{4}(\mathrm{~g})+\mathrm{CO}(\mathrm{g}) \quad$ Rate $=k\left[\mathrm{CH}_{3} \mathrm{CHO}\right]^{3 / 2}$
:::

:::

:::part{label="(iv)"}
:::prompt
$\mathrm{C}_{2} \mathrm{H}_{5} \mathrm{Cl}(\mathrm{g}) \rightarrow \mathrm{C}_{2} \mathrm{H}_{4}(\mathrm{~g})+\mathrm{HCl}(\mathrm{g}) \quad$ Rate $=k\left[\mathrm{C}_{2} \mathrm{H}_{5} \mathrm{Cl}\right]$
:::

:::

:::solution{label="Solution"}
(i) Given rate $=k[\mathrm{NO}]^{2}$

Therefore, order of the reaction $=2$
Dimension of

$$
k=\frac{\text { Rate }}{[\mathrm{NO}]^{2}}
$$

$$
\begin{aligned}
& =\frac{\mathrm{mol} \mathrm{~L}^{-1} \mathrm{~s}^{-1}}{\left(\mathrm{~mol} \mathrm{~L}^{-1}\right)^{2}} \\
& =\frac{\mathrm{mol} \mathrm{~L}^{-1} \mathrm{~s}^{-1}}{\mathrm{~mol}^{2} \mathrm{~L}^{-2}} \\
& =\mathrm{L} \mathrm{~mol}^{-1} \mathrm{~s}^{-1}
\end{aligned}
$$

(ii) Given rate $=k\left[\mathrm{H}_{2} \mathrm{O}_{2}\right]\left[\mathrm{I}^{-}\right]$

Therefore, order of the reaction $=2$
Dimension of

$$
k=\frac{\text { Rate }}{\left[\mathrm{H}_{2} \mathrm{O}_{2}\right]\left[\mathrm{I}^{-}\right]}
$$

$$
\begin{aligned}
& =\frac{\mathrm{mol} \mathrm{~L}^{-1} \mathrm{~s}^{-1}}{\left(\mathrm{~mol} \mathrm{~L}^{-1}\right)\left(\mathrm{mol} \mathrm{~L}^{-1}\right)} \\
& =\mathrm{L} \mathrm{~mol}^{-1} \mathrm{~s}^{-1}
\end{aligned}
$$

(iii) Given rate $=k\left[\mathrm{CH}_{3} \mathrm{CHO}\right]^{3 / 2}$

Therefore, order of reaction $={ }^{\frac{3}{2}}$
Dimension of

$$
k=\frac{\text { Rate }}{\left[\mathrm{CH}_{3} \mathrm{CHO}\right]^{\frac{3}{2}}}
$$

$$
\begin{aligned}
& =\frac{\mathrm{mol} \mathrm{~L}^{-1} \mathrm{~s}^{-1}}{\left(\mathrm{~mol} \mathrm{~L}^{-1}\right)^{\frac{3}{2}}} \\
& =\frac{\mathrm{mol} \mathrm{~L}^{-1} \mathrm{~s}^{-1}}{\mathrm{~mol}^{\frac{3}{2}} \mathrm{~L}^{-\frac{3}{2}}} \\
& =\mathrm{L}^{\frac{1}{2}} \mathrm{~mol}^{-\frac{1}{2}} \mathrm{~s}^{-1}
\end{aligned}
$$

(iv) Given rate $=k\left[\mathrm{C}_{2} \mathrm{H}_{5} \mathrm{Cl}\right]$ Therefore, order of the reaction $=1$
Dimension of

$$
k=\frac{\text { Rate }}{\left[\mathrm{C}_{2} \mathrm{H}_{5} \mathrm{Cl}\right]}
$$

$$
\begin{aligned}
& =\frac{\mathrm{mol} \mathrm{~L}^{-1} \mathrm{~s}^{-1}}{\mathrm{~mol} \mathrm{~L}^{-1}} \\
& =\mathrm{s}^{-1}
\end{aligned}
$$
:::

:::answer
**Answer:** (i) order $=2$, $k$ in $\mathrm{L} \mathrm{~mol}^{-1} \mathrm{~s}^{-1}$; (ii) order $=2$, $k$ in $\mathrm{L} \mathrm{~mol}^{-1} \mathrm{~s}^{-1}$; (iii) order $=\frac{3}{2}$, $k$ in $\mathrm{L}^{\frac{1}{2}} \mathrm{~mol}^{-\frac{1}{2}} \mathrm{~s}^{-1}$; (iv) order $=1$, $k$ in $\mathrm{s}^{-1}$
:::

:::

:::question{number="3.2" kind="exercise" id="q_3.2" topic="Initial rate calculation"}
#### Question 3.2

:::prompt
For the reaction:
$$
2 \mathrm{~A}+\mathrm{B} \rightarrow \mathrm{~A}_{2} \mathrm{~B}
$$
the rate $=k[\mathrm{~A}][\mathrm{B}]^{2}$ with $\mathrm{k}=2.0 \times 10^{-6} \mathrm{~mol}^{-2} \mathrm{~L}^{2} \mathrm{~s}^{-1}$. Calculate the initial rate of the reaction when $[\mathrm{A}]=0.1 \mathrm{~mol} \mathrm{~L}^{-1},[\mathrm{~B}]=0.2 \mathrm{~mol} \mathrm{~L}^{-1}$. Calculate the rate of reaction after [A] is reduced to $0.06 \mathrm{~mol} \mathrm{~L}^{-1}$.
:::

:::solution{label="Solution"}
The initial rate of the reaction is

$$
\begin{aligned}
& \text { Rate }=k[\mathrm{~A}][\mathrm{B}]^{2} \\
& =\left(2.0 \times 10^{-6} \mathrm{~mol}^{-2} \mathrm{~L}^{2} \mathrm{~s}^{-1}\right)\left(0.1 \mathrm{~mol} \mathrm{~L}^{-1}\right)\left(0.2 \mathrm{~mol} \mathrm{~L}^{-1}\right)^{2} \\
& =8.0 \times 10^{-9} \mathrm{~mol}^{-2} \mathrm{~L}^{2} \mathrm{~s}^{-1}
\end{aligned}
$$

When $[\mathrm{A}]$ is reduced from $0.1 \mathrm{~mol} \mathrm{~L}^{-1}$ to $0.06 \mathrm{~mol}^{-1}$, the concentration of A reacted = $(0.1-0.06) \mathrm{mol} \mathrm{L}^{-1}=0.04 \mathrm{~mol} \mathrm{~L}^{-1}$

Therefore, concentration of B reacted $\begin{aligned} & =\frac{1}{2} \times 0.04 \mathrm{~mol} \mathrm{~L}^{-1} \\ & =0.02 \mathrm{~mol} \mathrm{~L}^{-1}\end{aligned}$
Then, concentration of B available, $[\mathrm{B}]=(0.2-0.02) \mathrm{mol} \mathrm{L}^{-1}$

$$
=0.18 \mathrm{~mol} \mathrm{~L}^{-1}
$$

After $[\mathrm{A}]$ is reduced to $0.06 \mathrm{~mol} \mathrm{~L}^{-1}$, the rate of the reaction is given by,

$$
\begin{aligned}
& \text { Rate }=k[\mathrm{~A}][\mathrm{B}]^{2} \\
& =\left(2.0 \times 10^{-6} \mathrm{~mol}^{-2} \mathrm{~L}^{2} \mathrm{~s}^{-1}\right)\left(0.06 \mathrm{~mol} \mathrm{~L}^{-1}\right)\left(0.18 \mathrm{~mol} \mathrm{~L}^{-1}\right)^{2} \\
& =3.89 \mathrm{~mol} \mathrm{~L}^{-1} \mathrm{~s}^{-1}
\end{aligned}
$$
:::

:::answer
**Answer:** Initial rate $=8.0 \times 10^{-9} \mathrm{~mol}^{-2} \mathrm{~L}^{2} \mathrm{~s}^{-1}$; after $[\mathrm{A}]$ falls to $0.06 \mathrm{~mol} \mathrm{~L}^{-1}$, rate $=3.89 \mathrm{~mol} \mathrm{~L}^{-1} \mathrm{~s}^{-1}$
:::

:::

:::question{number="3.3" kind="exercise" id="q_3.3" topic="Zero order rate of production"}
#### Question 3.3

:::prompt
The decomposition of $\mathrm{NH}_{3}$ on platinum surface is zero order reaction. What are the rates of production of $\mathrm{N}_{2}$ and $\mathrm{H}_{2}$ if $k=2.5 \times 10^{-4} \mathrm{~mol}^{-1} \mathrm{~L} \mathrm{~s}^{-1}$ ?
:::

:::solution{label="Solution"}
The decomposition of $\mathrm{NH}_{3}$ on platinum surface is represented by the following equation.

$$
2 \mathrm{NH}_{3(\mathrm{~g})} \xrightarrow{\mathrm{Pt}} \mathrm{~N}_{2(\mathrm{~g})}+3 \mathrm{H}_{2(\mathrm{~g})}
$$

Therefore,

$$
\text { Rate }=-\frac{1}{2} \frac{d\left[\mathrm{NH}_{3}\right]}{d t}=\frac{d\left[\mathrm{~N}_{2}\right]}{d t}=\frac{1}{3} \frac{d\left[\mathrm{H}_{2}\right]}{d t}
$$

However, it is given that the reaction is of zero order. Therefore,

$$
\begin{aligned}
-\frac{1}{2} \frac{d\left[\mathrm{NH}_{3}\right]}{d t}=\frac{d\left[\mathrm{~N}_{2}\right]}{d t}=\frac{1}{3} \frac{d\left[\mathrm{H}_{2}\right]}{d t} & =k \\
& =2.5 \times 10^{-4} \mathrm{~mol} \mathrm{~L}^{-1} \mathrm{~s}^{-1}
\end{aligned}
$$

Therefore, the rate of production of $\mathrm{N}_{2}$ is

$$
\frac{d\left[\mathrm{~N}_{2}\right]}{d t}=2.5 \times 10^{-4} \mathrm{~mol} \mathrm{~L}^{-1} \mathrm{~s}^{-1}
$$

And, the rate of production of $\mathrm{H}_{2}$ is

$$
\begin{aligned}
& \frac{d\left[\mathrm{H}_{2}\right]}{d t}=3 \times 2.5 \times 10^{-4} \mathrm{~mol} \mathrm{~L}^{-1} \mathrm{~s}^{-1} \\
& =7.5 \times 10^{-4} \mathrm{~mol} \mathrm{~L}^{-1} \mathrm{~s}^{-1}
\end{aligned}
$$
:::

:::answer
**Answer:** Rate of production of $\mathrm{N}_2 = 2.5 \times 10^{-4} \mathrm{~mol} \mathrm{~L}^{-1} \mathrm{~s}^{-1}$; rate of production of $\mathrm{H}_2 = 7.5 \times 10^{-4} \mathrm{~mol} \mathrm{~L}^{-1} \mathrm{~s}^{-1}$
:::

:::

:::question{number="3.4" kind="exercise" id="q_3.4" topic="Units of rate and rate constant"}
#### Question 3.4

:::prompt
The decomposition of dimethyl ether leads to the formation of $\mathrm{CH}_{4}, \mathrm{H}_{2}$ and CO and the reaction rate is given by
$$
\text { Rate }=k\left[\mathrm{CH}_{3} \mathrm{OCH}_{3}\right]^{3 / 2}
$$
The rate of reaction is followed by increase in pressure in a closed vessel, so the rate can also be expressed in terms of the partial pressure of dimethyl ether, i.e.,
$$
\text { Rate }=k\left(p_{\mathrm{CH}_{3} \mathrm{OCH}_{3}}\right)^{3 / 2}
$$
If the pressure is measured in bar and time in minutes, then what are the units of rate and rate constants?
:::

:::solution{label="Solution"}
If pressure is measured in bar and time in minutes, then
Unit of rate = bar min-1

$$
\begin{aligned}
& \text { Rate }=k\left(p_{\mathrm{CH}_{3} \mathrm{OCH}_{3}}\right)^{3 / 2} \\
& \Rightarrow k=\frac{\text { Rate }}{\left(p_{\mathrm{CH}_{3} \mathrm{OCH}_{1}}\right)^{3 / 2}}
\end{aligned}
$$

Therefore, unit of rate constants

$$
(k)=\frac{\text { bar min }{ }^{-1}}{\text { bar }^{3 / 2}}
$$

$$
=\mathrm{bar}^{-1 / 2} \mathrm{~min}^{-1}
$$
:::

:::answer
**Answer:** Unit of rate $=\mathrm{bar} \mathrm{~min}^{-1}$; unit of rate constant $(k)=\mathrm{bar}^{-1 / 2} \mathrm{~min}^{-1}$
:::

:::

:::question{number="3.5" kind="exercise" id="q_3.5" topic="Factors affecting reaction rate"}
#### Question 3.5

:::prompt
Mention the factors that affect the rate of a chemical reaction.
:::

:::solution{label="Solution"}
The factors that affect the rate of a reaction are as follows.

(i) Concentration of reactants (pressure in case of gases)
(ii) Temperature

(iii) Presence of a catalyst
:::

:::

:::question{number="3.6" kind="exercise" id="q_3.6" topic="Second order concentration effect"}
#### Question 3.6

:::prompt
A reaction is second order with respect to a reactant. How is the rate of reaction affected if the concentration of the reactant is
:::

:::part{label="(i)"}
:::prompt
doubled
:::

:::

:::part{label="(ii)"}
:::prompt
reduced to half ?
:::

:::

:::solution{label="Solution"}
Let the concentration of the reactant be $[\mathrm{A}]=a$
Rate of reaction, $\mathrm{R}=k[\mathrm{~A}]^{2}$

$$
=k a^{2}
$$

(i) If the concentration of the reactant is doubled, i.e. $[\mathrm{A}]=2 a$, then the rate of the reaction would be

$$
\begin{aligned}
& \mathrm{R}^{\prime}=k(2 a)^{2} \\
& =4 k a^{2} \\
& =4 \mathrm{R}
\end{aligned}
$$

Therefore, the rate of the reaction would increase by 4 times.
(ii) If the concentration of the reactant is reduced to half, i.e. $[\mathrm{A}]=\frac{1}{2} a$, then the rate of the reaction would be

$$
\begin{aligned}
\mathrm{R}^{\prime \prime} & =k\left(\frac{1}{2} a\right)^{2} \\
& =\frac{1}{4} k a \\
& =\frac{1}{4} R
\end{aligned}
$$

Therefore, the rate of the reaction would be reduced to $\frac{1}{4}^{\text {th }}$.
:::

:::answer
**Answer:** (i) Rate increases by 4 times; (ii) rate is reduced to $\frac{1}{4}^{\text {th }}$
:::

:::

:::question{number="3.7" kind="exercise" id="q_3.7" topic="Temperature dependence of rate constant"}
#### Question 3.7

:::prompt
What is the effect of temperature on the rate constant of a reaction? How can this effect of temperature on rate constant be represented quantitatively?
:::

:::solution{label="Solution"}
The rate constant is nearly doubled with a rise in temperature by 10° for a chemical reaction.

The temperature effect on the rate constant can be represented quantitatively by Arrhenius equation,

$$
k=\mathrm{A} e^{-E_{s} / \mathrm{R} T}
$$

where, $k$ is the rate constant,
A is the Arrhenius factor or the frequency factor,
$R$ is the gas constant,
$T$ is the temperature, and
$E_{a}$ is the energy of activation for the reaction
:::

:::

:::question{number="3.8" kind="exercise" id="q_3.8" topic="Pseudo first order average rate"}
#### Question 3.8

:::prompt
In a pseudo first order reaction in water, the following results were obtained:

| t/s | 0 | 30 | 60 | 90 |
| :--- | :--- | :--- | :--- | :--- |
| [A]/ $\mathrm{mol} \mathrm{L}^{-1}$ | 0.55 | 0.31 | 0.17 | 0.085 |

Calculate the average rate of reaction between the time interval 30 to 60 seconds.
:::

:::solution{label="Solution"}
(i) Average rate of reaction between the time interval, 30 to 60 seconds, $=\frac{d[\text { Ester }]}{d t}$
$$
\begin{aligned}
& =\frac{0.31-0.17}{60-30} \\
& =\frac{0.14}{30} \\
& =4.67 \times 10^{-3} \mathrm{~mol} \mathrm{~L}^{-1} \mathrm{~s}^{-1}
\end{aligned}
$$
(ii) For a pseudo first order reaction,

$$
k=\frac{2.303}{t} \log \frac{[\mathrm{R}]_{0}}{[\mathrm{R}]}
$$

For

$$
k_{1}=\frac{2.303}{30} \log \frac{0.55}{0.31} t=30 \mathrm{~s},
$$

For $t=60 \mathrm{~s}$,

$$
k_{2}=\frac{2.303}{60} \log \frac{0.55}{0.17}
$$

$=1.957 \times 10^{-2} \mathrm{~s}^{-1}$
For $t=90 \mathrm{~s}$,

$$
k_{3}=\frac{2.303}{90} \log \frac{0.55}{0.085}
$$

$$
=2.075 \times 10^{-2} \mathrm{~s}^{-1}
$$

Then, average rate constant,

$$
k=\frac{k_{1}+k_{2}+k_{3}}{3}
$$

$$
\begin{aligned}
& =\frac{\left(1.911 \times 10^{-2}\right)+\left(1.957 \times 10^{-2}\right)+\left(2.075 \times 10^{-2}\right)}{3} \\
& =1.98 \times 10^{-2} \mathrm{~s}^{-1}
\end{aligned}
$$
:::

:::answer
**Answer:** (i) Average rate (30–60 s) $=4.67 \times 10^{-3} \mathrm{~mol} \mathrm{~L}^{-1} \mathrm{~s}^{-1}$; (ii) average pseudo first order $k=1.98 \times 10^{-2} \mathrm{~s}^{-1}$
:::

:::

:::question{number="3.9" kind="exercise" id="q_3.9" topic="Mixed order rate equation"}
#### Question 3.9

:::prompt
A reaction is first order in A and second order in B.
:::

:::part{label="(i)"}
:::prompt
Write the differential rate equation.
:::

:::

:::part{label="(ii)"}
:::prompt
How is the rate affected on increasing the concentration of B three times?
:::

:::

:::part{label="(iii)"}
:::prompt
How is the rate affected when the concentrations of both A and B are doubled?
:::

:::

:::solution{label="Solution"}
(i) The differential rate equation will be
$$
-\frac{d[\mathrm{R}]}{d t}=k[\mathrm{~A}][\mathrm{B}]^{2}
$$
(ii) If the concentration of B is increased three times, then
$$
\begin{aligned}
-\frac{d[\mathrm{R}]}{d t} & =k[\mathrm{~A}][3 \mathrm{~B}]^{2} \\
& =9 \cdot k[\mathrm{~A}][\mathrm{B}]^{2}
\end{aligned}
$$

Therefore, the rate of reaction will increase 9 times.
(iii) When the concentrations of both A and B are doubled,

$$
\begin{aligned}
-\frac{d[\mathrm{R}]}{d t} & =k[\mathrm{~A}][\mathrm{B}]^{2} \\
& =k[2 \mathrm{~A}][2 \mathrm{~B}]^{2} \\
& =8 \cdot k[\mathrm{~A}][\mathrm{B}]^{2}
\end{aligned}
$$

Therefore, the rate of reaction will increase 8 times.
:::

:::answer
**Answer:** (i) $-\frac{d[\mathrm{R}]}{d t}=k[\mathrm{~A}][\mathrm{B}]^{2}$; (ii) rate increases 9 times; (iii) rate increases 8 times
:::

:::

:::question{number="3.10" kind="exercise" id="q_3.10" topic="Order determination from data"}
#### Question 3.10

:::prompt
In a reaction between A and B, the initial rate of reaction $\left(\mathrm{r}_{0}\right)$ was measured for different initial concentrations of A and B as given below:

| A/ $\mathrm{mol} \mathrm{L}^{-1}$ | 0.20 | 0.20 | 0.40 |
| :--- | :--- | :--- | :--- |
| B/ $\mathrm{mol} \mathrm{L}^{-1}$ | 0.30 | 0.10 | 0.05 |
| $\mathrm{r}_{0} / \mathrm{mol} \mathrm{L}^{-1} \mathrm{~s}^{-1}$ | $5.07 \times 10^{-5}$ | $5.07 \times 10^{-5}$ | $1.43 \times 10^{-4}$ |

What is the order of the reaction with respect to A and B?
:::

:::solution{label="Solution"}
Let the order of the reaction with respect to A be $x$ and with respect to B be $y$.
Therefore,

$$
\begin{aligned}
& \mathrm{r}_{0}=k[\mathrm{~A}]^{x}[\mathrm{~B}]^{y} \\
& 5.07 \times 10^{-5}=k[0.20]^{x}[0.30]^{y} \\
& 5.07 \times 10^{-5}=k[0.20]^{x}[0.10]^{y} \\
& 1.43 \times 10^{-4}=k[0.40]^{x}[0.05]^{y}
\end{aligned}
$$

Dividing equation (i) by (ii), we obtain

$$
\begin{aligned}
& \frac{5.07 \times 10^{-5}}{5.07 \times 10^{-5}}=\frac{k[0.20]^{x}[0.30]^{y}}{k[0.20]^{x}[0.10]^{y}} \\
& \Rightarrow 1=\frac{[0.30]^{y}}{[0.10]^{y}} \\
& \Rightarrow\left(\frac{0.30}{0.10}\right)^{0}=\left(\frac{0.30}{0.10}\right)^{y} \\
& \Rightarrow y=0
\end{aligned}
$$

Dividing equation (iii) by (ii), we obtain

$$
\begin{aligned}
& \frac{1.43 \times 10^{-4}}{5.07 \times 10^{-5}}=\frac{k[0.40]^{x}[0.05]^{y}}{k[0.20]^{x}[0.30]^{y}} \\
& \Rightarrow \frac{1.43 \times 10^{-4}}{5.07 \times 10^{-5}}=\frac{[0.40]^{x}}{[0.20]^{x}} \quad\left[\begin{array}{l}
\text { Since } y=0, \\
{[0.05]^{y}=[0.30]^{y}=1}
\end{array}\right] \\
& \Rightarrow 2.821=2^{x} \\
& \Rightarrow \log 2.821=x \log 2 \quad \text { (Taking log on both sides) } \\
& \Rightarrow x=\frac{\log 2.821}{\log 2} \\
& =1.496 \\
& =1.5 \text { (approximately) }
\end{aligned}
$$

Hence, the order of the reaction with respect to A is 1.5 and with respect to B is zero.
:::

:::answer
**Answer:** Order with respect to A $=1.5$; order with respect to B $=0$
:::

:::

:::question{number="3.11" kind="exercise" id="q_3.11" topic="Rate law from kinetic data"}
#### Question 3.11

:::prompt
The following results have been obtained during the kinetic studies of the reaction:

$$
2 \mathrm{~A}+\mathrm{B} \rightarrow \mathrm{C}+\mathrm{D}
$$

| Experiment | $[\mathrm{A}] / \mathrm{mol} \mathrm{L}^{-1}$ | [B]/mol $\mathrm{L}^{-1}$ | Initial rate of formation of $\mathrm{D} / \mathrm{mol} \mathrm{L}^{-1} \mathrm{~min}^{-1}$ |
| :--- | :--- | :--- | :--- |
| I | 0.1 | 0.1 | $6.0 \times 10^{-3}$ |
| II | 0.3 | 0.2 | $7.2 \times 10^{-2}$ |
| III | 0.3 | 0.4 | $2.88 \times 10^{-1}$ |
| IV | 0.4 | 0.1 | $2.40 \times 10^{-2}$ |

Determine the rate law and the rate constant for the reaction.
:::

:::solution{label="Solution"}
Let the order of the reaction with respect to A be $x$ and with respect to B be $y$.
Therefore, rate of the reaction is given by,

$$
\text { Rate }=k[\mathrm{~A}]^{x}[\mathrm{~B}]^{y}
$$

According to the question,

$$
\begin{aligned}
& 6.0 \times 10^{-3}=k[0.1]^{x}[0.1]^{y} \\
& 7.2 \times 10^{-2}=k[0.3]^{x}[0.2]^{y} \\
& 2.88 \times 10^{-1}=k[0.3]^{x}[0.4]^{y} \\
& 2.40 \times 10^{-2}=k[0.4]^{x}[0.1]^{y}
\end{aligned}
$$

Dividing equation (iv) by (i), we obtain

$$
\begin{aligned}
& \frac{2.40 \times 10^{-2}}{6.0 \times 10^{-3}}=\frac{k[0.4]^{x}[0.1]^{y}}{k[0.1]^{x}[0.1]^{y}} \\
& \Rightarrow 4=\frac{[0.4]^{x}}{[0.1]^{x}} \\
& \Rightarrow 4=\left(\frac{0.4}{0.1}\right)^{x} \\
& \Rightarrow(4)^{1}=4^{x} \\
& \Rightarrow x=1
\end{aligned}
$$

Dividing equation (iii) by (ii), we obtain

$$
\begin{aligned}
& \frac{2.88 \times 10^{-1}}{7.2 \times 10^{-2}}=\frac{k[0.3]^{x}[0.4]^{y}}{k[0.3]^{x}[0.2]^{y}} \\
& \Rightarrow 4=\left(\frac{0.4}{0.2}\right)^{y} \\
& \Rightarrow 4=2^{y} \\
& \Rightarrow 2^{2}=2^{y} \\
& \Rightarrow y=2
\end{aligned}
$$

Therefore, the rate law is

$$
\begin{aligned}
\text { Rate } & =k[\mathrm{~A}][\mathrm{B}]^{2} \\
k & =\frac{\text { Rate }}{[\mathrm{A}][\mathrm{B}]^{2}}
\end{aligned}
$$

From experiment I, we obtain

$$
\begin{aligned}
& k=\frac{6.0 \times 10^{-3} \mathrm{~mol} \mathrm{~L}^{-1} \mathrm{~min}^{-1}}{\left(0.1 \mathrm{~mol} \mathrm{~L}^{-1}\right)\left(0.1 \mathrm{~mol} \mathrm{~L}^{-1}\right)^{2}} \\
& =6.0 \mathrm{~L}^{2} \mathrm{~mol}^{-2} \mathrm{~min}^{-1}
\end{aligned}
$$

From experiment II, we obtain

$$
\begin{aligned}
& k=\frac{7.2 \times 10^{-2} \mathrm{~mol} \mathrm{~L}^{-1} \mathrm{~min}^{-1}}{\left(0.3 \mathrm{~mol} \mathrm{~L}^{-1}\right)\left(0.2 \mathrm{~mol} \mathrm{~L}^{-1}\right)^{2}} \\
& =6.0 \mathrm{~L}^{2} \mathrm{~mol}^{-2} \mathrm{~min}^{-1}
\end{aligned}
$$

From experiment III, we obtain

$$
\begin{aligned}
& k=\frac{2.88 \times 10^{-1} \mathrm{~mol} \mathrm{~L}^{-1} \mathrm{~min}^{-1}}{\left(0.3 \mathrm{~mol} \mathrm{~L}^{-1}\right)\left(0.4 \mathrm{~mol} \mathrm{~L}^{-1}\right)^{2}} \\
& =6.0 \mathrm{~L}^{2} \mathrm{~mol}^{-2} \mathrm{~min}^{-1}
\end{aligned}
$$

From experiment IV, we obtain

$$
\begin{aligned}
& k=\frac{2.40 \times 10^{-2} \mathrm{~mol} \mathrm{~L}^{-1} \mathrm{~min}^{-1}}{\left(0.4 \mathrm{~mol} \mathrm{~L}^{-1}\right)\left(0.1 \mathrm{~mol} \mathrm{~L}^{-1}\right)^{2}} \\
& =6.0 \mathrm{~L}^{2} \mathrm{~mol}^{-2} \mathrm{~min}^{-1}
\end{aligned}
$$

Therefore, rate constant, $k=6.0 \mathrm{~L}^{2} \mathrm{~mol}^{-2} \mathrm{~min}^{-1}$
:::

:::answer
**Answer:** Rate law $=k[\mathrm{~A}][\mathrm{B}]^{2}$; $k=6.0 \mathrm{~L}^{2} \mathrm{~mol}^{-2} \mathrm{~min}^{-1}$
:::

:::

:::question{number="3.12" kind="exercise" id="q_3.12" topic="Fill in rate table"}
#### Question 3.12

:::prompt
The reaction between A and B is first order with respect to A and zero order with respect to B. Fill in the blanks in the following table:

| Experiment | [A]/ $\mathrm{mol} \mathrm{L}^{-1}$ | [B]/ $\mathrm{mol} \mathrm{L}^{-1}$ | Initial rate/ $\mathrm{mol} \mathrm{L}^{-1} \mathrm{~min}^{-1}$ |
| :--- | :--- | :--- | :--- |
| I | 0.1 | 0.1 | $2.0 \times 10^{-2}$ |
| II | - | 0.2 | $4.0 \times 10^{-2}$ |
| III | 0.4 | 0.4 | - |
| IV | - | 0.2 | $2.0 \times 10^{-2}$ |
:::

:::solution{label="Solution"}
The given reaction is of the first order with respect to $A$ and of zero order with respect to B.

Therefore, the rate of the reaction is given by,

$$
\begin{aligned}
& \text { Rate }=k[\mathrm{~A}]^{1}[\mathrm{~B}]^{0} \\
& \Rightarrow \text { Rate }=k[\mathrm{~A}]
\end{aligned}
$$

From experiment I, we obtain

$$
\begin{aligned}
& 2.0 \times 10^{-2} \mathrm{~mol} \mathrm{~L}^{-1} \mathrm{~min}^{-1}=\mathrm{k}\left(0.1 \mathrm{~mol} \mathrm{~L}^{-1}\right) \\
& \Rightarrow k=0.2 \mathrm{~min}^{-1}
\end{aligned}
$$

From experiment II, we obtain

$$
\begin{aligned}
& 4.0 \times 10^{-2} \mathrm{~mol} \mathrm{~L}^{-1} \mathrm{~min}^{-1}=0.2 \mathrm{~min}^{-1}[\mathrm{~A}] \\
& \Rightarrow[\mathrm{A}]=0.2 \mathrm{~mol} \mathrm{~L}^{-1}
\end{aligned}
$$

From experiment III, we obtain Rate

$$
\begin{aligned}
& =0.2 \mathrm{~min}^{-1} \times 0.4 \mathrm{~mol} \mathrm{~L}^{-1} \\
& =0.08 \mathrm{~mol} \mathrm{~L}^{-1} \mathrm{~min}^{-1}
\end{aligned}
$$

From experiment IV, we obtain

$$
2.0 \times 10^{-2} \mathrm{~mol} \mathrm{~L}^{-1} \mathrm{~min}^{-1}=0.2 \mathrm{~min}^{-1}[\mathrm{~A}]
$$

$$
\Rightarrow[\mathrm{A}]=0.1 \mathrm{~mol} \mathrm{~L}^{-1}
$$
:::

:::answer
**Answer:** $k=0.2 \mathrm{~min}^{-1}$; experiment II $[\mathrm{A}]=0.2 \mathrm{~mol} \mathrm{~L}^{-1}$; experiment III rate $=0.08 \mathrm{~mol} \mathrm{~L}^{-1} \mathrm{~min}^{-1}$; experiment IV $[\mathrm{A}]=0.1 \mathrm{~mol} \mathrm{~L}^{-1}$
:::

:::

:::question{number="3.13" kind="exercise" id="q_3.13" topic="Half-life from rate constant"}
#### Question 3.13

:::prompt
Calculate the half-life of a first order reaction from their rate constants given below:
:::

:::part{label="(i)"}
:::prompt
$200 \mathrm{~s}^{-1}$
:::

:::

:::part{label="(ii)"}
:::prompt
$2 \mathrm{~min}^{-1}$
:::

:::

:::part{label="(iii)"}
:::prompt
4 years ${ }^{-1}$
:::

:::

:::solution{label="Solution"}
$$
\begin{aligned}
& \text { (i) Half life, } t_{1 / 2}=\frac{0.693}{k} \\
& =\frac{0.693}{200 \mathrm{~s}^{-1}} \\
& =3.47 \mathrm{~s} \text { (approximately) }
\end{aligned}
$$

(ii) Half life, $t_{1 / 2}=\frac{0.693}{k}$

$$
\begin{aligned}
& =\frac{0.693}{2 \mathrm{~min}^{-1}} \\
& =0.35 \text { min (approximately) }
\end{aligned}
$$

(iii) Half life, $t_{1 / 2}=\frac{0.693}{k}$

$$
\begin{aligned}
& =\frac{0.693}{4 \text { years }^{-1}} \\
& =0.173 \text { years (approximately) }
\end{aligned}
$$
:::

:::answer
**Answer:** (i) $t_{1/2}=3.47 \mathrm{~s}$; (ii) $t_{1/2}=0.35$ min; (iii) $t_{1/2}=0.173$ years
:::

:::

:::question{number="3.14" kind="exercise" id="q_3.14" topic="Radiocarbon dating"}
#### Question 3.14

:::prompt
The half-life for radioactive decay of ${ }^{14} \mathrm{C}$ is 5730 years. An archaeological artifact containing wood had only 80\% of the ${ }^{14} \mathrm{C}$ found in a living tree. Estimate the age of the sample.
:::

:::solution{label="Solution"}
Here,

$$
k=\frac{0.693}{t_{1 / 2}}
$$

$$
=\frac{0.693}{5730} \text { years }^{-1}
$$

It is known that,

$$
\begin{aligned}
t & =\frac{2.303}{k} \log \frac{[\mathrm{R}]_{0}}{[\mathrm{R}]} \\
& =\frac{2.303}{\frac{0.693}{5730}} \log \frac{100}{80} \\
= & 1845 \text { years (approximately) }
\end{aligned}
$$

Hence, the age of the sample is 1845 years.
:::

:::answer
**Answer:** Age of the sample $\approx 1845$ years
:::

:::

:::question{number="3.15" kind="exercise" id="q_3.15" topic="N2O5 decomposition kinetics"}
#### Question 3.15

:::prompt
The experimental data for decomposition of $\mathrm{N}_{2} \mathrm{O}_{5}$

$$
\left[2 \mathrm{~N}_{2} \mathrm{O}_{5} \rightarrow 4 \mathrm{NO}_{2}+\mathrm{O}_{2}\right]
$$

in gas phase at 318K are given below:

| t/s | 0 | 400 | 800 | 1200 | 1600 | 2000 | 2400 | 2800 | 3200 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| $\begin{aligned} & 10^{2} \times\left[\mathrm{N}_{2} \mathrm{O}_{5}\right] / \\ & \mathrm{mol} \mathrm{~L}^{-1} \end{aligned}$ | 1.63 | 1.36 | 1.14 | 0.93 | 0.78 | 0.64 | 0.53 | 0.43 | 0.35 |
:::

:::figure{src="images/fig_3_27.jpg" id="fig_3_27"}
Plot of $\left[\mathrm{N}_{2} \mathrm{O}_{5}\right]$ against $t$
:::

:::figure{src="images/fig_3_28.jpg" id="fig_3_28"}
Plot of $\log \left[\mathrm{N}_{2} \mathrm{O}_{5}\right]$ against $t$
:::

:::part{label="(i)"}
:::prompt
Plot $\left[\mathrm{N}_{2} \mathrm{O}_{5}\right]$ against $t$.
:::

:::

:::part{label="(ii)"}
:::prompt
Find the half-life period for the reaction.
:::

:::

:::part{label="(iii)"}
:::prompt
Draw a graph between $\log \left[\mathrm{N}_{2} \mathrm{O}_{5}\right]$ and $t$.
:::

:::

:::part{label="(iv)"}
:::prompt
What is the rate law ?
:::

:::

:::part{label="(v)"}
:::prompt
Calculate the rate constant.
:::

:::

:::part{label="(vi)"}
:::prompt
Calculate the half-life period from $k$ and compare it with (ii).
:::

:::

:::solution{label="Solution"}
(ii) Time corresponding to the concentration, $\frac{1.630 \times 10^{2}}{2} \mathrm{~mol} \mathrm{~L}^{-1}=81.5 \mathrm{molL}^{-1}$, is the half life. From the graph, the half life is obtained as 1450 s.
(iii)
| t(s) | $10^{2} \times\left[\mathrm{N}_{2} \mathrm{O}_{5}\right] / \mathrm{mol} \mathrm{L}^{-1}$ | $\boldsymbol{\log}\left[\mathrm{N}_{2} \mathrm{O}_{5}\right]$ |
| :--- | :--- | :--- |
| 0 | 1.63 | - 1.79 |
| 400 | 1.36 | - 1.87 |
| 800 | 1.14 | - 1.94 |
| 1200 | 0.93 | - 2.03 |
| 1600 | 0.78 | - 2.11 |
| 2000 | 0.64 | - 2.19 |
| 2400 | 0.53 | - 2.28 |
| 2800 | 0.43 | - 2.37 |
| 3200 | 0.35 | - 2.46 |

(iv) The given reaction is of the first order as the plot, $\log \left[\mathrm{N}_{2} \mathrm{O}_{5}\right]_{\mathrm{V} / \mathrm{s}} t$, is a straight line. Therefore, the rate law of the reaction is

$$
\text { Rate }=k\left[\mathrm{~N}_{2} \mathrm{O}_{5}\right]
$$

(v) From the plot, $\log \left[\mathrm{N}_{2} \mathrm{O}_{5}\right]$

$$
\begin{aligned}
\text { Slope } & =\frac{-2.46-(-1.79)}{3200-0} \\
& =\frac{-0.67}{3200}
\end{aligned}
$$

v/s $t$, we obtain
Again, slope of the line of the plot $\log \left[\mathrm{N}_{2} \mathrm{O}_{5}\right]_{\mathrm{V} / \mathrm{s}} t$ is given by

$$
-\frac{k}{2.303} .
$$

Therefore, we obtain,

$$
\begin{aligned}
& -\frac{k}{2.303}=-\frac{0.67}{3200} \\
& \Rightarrow k=4.82 \times 10^{-4} \mathrm{~s}^{-1}
\end{aligned}
$$

(vi) Half-life is given by,

$$
\begin{aligned}
t_{1 / 2} & =\frac{0.639}{k} \\
& =\frac{0.693}{4.82 \times 10^{-4}} \mathrm{~s} \\
& =1.438 \times 10^{3} \mathrm{~s} \\
& =1438 \mathrm{~s}
\end{aligned}
$$

This value, 1438 s, is very close to the value that was obtained from the graph.
:::

:::answer
**Answer:** (ii) $t_{1/2}$ (from graph) $=1450$ s; (iv) Rate $=k[\mathrm{N}_2\mathrm{O}_5]$; (v) $k=4.82 \times 10^{-4} \mathrm{~s}^{-1}$; (vi) $t_{1/2}$ (from $k$) $=1438$ s
:::

:::

:::question{number="3.16" kind="exercise" id="q_3.16" topic="First order concentration reduction time"}
#### Question 3.16

:::prompt
The rate constant for a first order reaction is $60 \mathrm{~s}^{-1}$. How much time will it take to reduce the initial concentration of the reactant to its $1 / 16^{\text {th }}$ value?
:::

:::solution{label="Solution"}
It is known that,

$$
\begin{aligned}
t & =\frac{2.303}{k} \log \frac{[\mathrm{R}]_{0}}{[\mathrm{R}]} \\
& =\frac{2.303}{60 \mathrm{~s}^{-1}} \log \frac{1}{1 / 16} \\
& =\frac{2.303}{60 \mathrm{~s}^{-1}} \log 16 \\
& =4.6 \times 10^{-2} \mathrm{~s} \text { (approximately) }
\end{aligned}
$$

Hence, the required time is $4.6 \times 10^{-2} \mathrm{~s}$.
:::

:::answer
**Answer:** $t=4.6 \times 10^{-2} \mathrm{~s}$
:::

:::

:::question{number="3.17" kind="exercise" id="q_3.17" topic="Radioactive decay remaining amount"}
#### Question 3.17

:::prompt
During nuclear explosion, one of the products is ${ }^{90} \mathrm{Sr}$ with half-life of 28.1 years. If $1 \mu \mathrm{~g}$ of ${ }^{90} \mathrm{Sr}$ was absorbed in the bones of a newly born baby instead of calcium, how much of it will remain after 10 years and 60 years if it is not lost metabolically.
:::

:::solution{label="Solution"}
Here,

$$
k=\frac{0.693}{t_{1 / 2}}=\frac{0.693}{28.1} \mathrm{y}^{-1}
$$

It is known that,

$$
\begin{aligned}
& t=\frac{2.303}{k} \log \frac{[\mathrm{R}]_{0}}{[\mathrm{R}]} \\
& \Rightarrow 10=\frac{2.303}{\frac{0.693}{28.1}} \log \frac{1}{[\mathrm{R}]} \\
& \Rightarrow 10=\frac{2.303}{\frac{0.693}{28.1}}(-\log [\mathrm{R}]) \\
& \Rightarrow \log [\mathrm{R}]=-\frac{10 \times 0.693}{2.303 \times 28.1} \\
& \Rightarrow[\mathrm{R}]=\operatorname{antilog}(-0.1071) \\
& \quad=\operatorname{antilog}(\overline{1} .8929) \\
& \quad=0.7814 \mu \mathrm{~g}
\end{aligned}
$$

Therefore, $0.7814 \mu \mathrm{~g}$ of ${ }^{90} \mathrm{Sr}$ will remain after 10 years.
Again,

$$
\begin{aligned}
& t=\frac{2.303}{k} \log \frac{[\mathrm{R}]_{0}}{[\mathrm{R}]} \\
& \Rightarrow 60=\frac{2.303}{\frac{0.693}{28.1}} \log \frac{1}{[\mathrm{R}]} \\
& \Rightarrow \log [\mathrm{R}]=-\frac{60 \times 0.693}{2.303 \times 28.1} \\
& \Rightarrow[\mathrm{R}]=\operatorname{antilog}(-0.6425) \\
& \quad=\operatorname{antilog}(\overline{1} .3575) \\
& \quad=0.2278 \mu \mathrm{~g}
\end{aligned}
$$

Therefore, $0.2278 \mu \mathrm{~g}$ of ${ }^{90} \mathrm{Sr}$ will remain after 60 years.
:::

:::answer
**Answer:** After 10 years, $0.7814\ \mu\mathrm{g}$ of ${}^{90}\mathrm{Sr}$ remains; after 60 years, $0.2278\ \mu\mathrm{g}$ remains
:::

:::

:::question{number="3.18" kind="exercise" id="q_3.18" topic="First order completion time proof"}
#### Question 3.18

:::prompt
For a first order reaction, show that time required for 99\% completion is twice the time required for the completion of 90\% of reaction.
:::

:::solution{label="Solution"}
For a first order reaction, the time required for 99\% completion is

$$
\begin{aligned}
t_{1} & =\frac{2.303}{k} \log \frac{100}{100-99} \\
& =\frac{2.303}{k} \log 100 \\
& =2 \times \frac{2.303}{k}
\end{aligned}
$$

For a first order reaction, the time required for 90\% completion is

$$
\begin{aligned}
t_{2} & =\frac{2.303}{k} \log \frac{100}{100-90} \\
& =\frac{2.303}{k} \log 10 \\
& =\frac{2.303}{k}
\end{aligned}
$$

Therefore, $t_{1}=2 t_{2}$
Hence, the time required for 99\% completion of a first order reaction is twice the time required for the completion of 90\% of the reaction.
:::

:::

:::question{number="3.19" kind="exercise" id="q_3.19" topic="Half-life from decomposition data"}
#### Question 3.19

:::prompt
A first order reaction takes 40 min for 30\% decomposition. Calculate $\mathrm{t}_{1 / 2}$.
:::

:::solution{label="Solution"}
For a first order reaction,

$$
\begin{aligned}
t & =\frac{2.303}{k} \log \frac{[\mathrm{R}]_{0}}{[\mathrm{R}]} \\
k & =\frac{2.303}{40 \mathrm{~min}} \log \frac{100}{100-30} \\
& =\frac{2.303}{40 \mathrm{~min}} \log \frac{10}{7} \\
& =8.918 \times 10^{-3} \mathrm{~min}^{-1}
\end{aligned}
$$

Therefore, $t_{1 / 2}$ of the decomposition reaction is

$$
\begin{aligned}
t_{1 / 2} & =\frac{0.693}{k} \\
& =\frac{0.693}{8.918 \times 10^{-3}} \mathrm{~min} \\
= & 77.7 \text { min (approximately) }
\end{aligned}
$$
:::

:::answer
**Answer:** $t_{1/2} \approx 77.7$ min
:::

:::

:::question{number="3.20" kind="exercise" id="q_3.20" topic="Rate constant from pressure data" corrections_applied="1"}
#### Question 3.20

:::prompt
For the decomposition of azoisopropane to hexane and nitrogen at 543 K, the following data are obtained.

| $t(\mathrm{sec})$ | $\mathrm{P}(\mathrm{mm}$ of Hg$)$ |
| :--- | :--- |
| 0 | 35.0 |
| 360 | 54.0 |
| 720 | 63.0 |

Calculate the rate constant.
:::

:::solution{label="Solution"}
The decomposition of azoisopropane to hexane and nitrogen at 543 K is represented by the following equation.

$$
\left(\mathrm{CH}_{3}\right)_{2} \mathrm{CHN}=\mathrm{NCH}\left(\mathrm{CH}_{3}\right)_{2(g)} \longrightarrow \mathrm{N}_{2(g)}+\mathrm{C}_{6} \mathrm{H}_{14(g)}
$$

At $t=0 \quad \mathrm{P}_{0} \quad 0 \quad 0$
At $t=t \quad \mathrm{P}_{0}-p \quad p \quad p$

$$
\mathrm{P}_{l}=\left(\mathrm{P}_{0}-p\right)+p+p
$$

After time, $t$, total pressure,

$$
\begin{aligned}
& \Rightarrow \mathrm{P}_{1}=\mathrm{P}_{0}+p \\
& \Rightarrow p=\mathrm{P}_{1}-\mathrm{P}_{0}
\end{aligned}
$$

Therefore, $\mathrm{P}_{\mathrm{o}}-p=\mathrm{P}_{\mathrm{o}}-\left(\mathrm{P}_{\mathrm{t}}-\mathrm{P}_{\mathrm{o}}\right)$

$$
=2 \mathrm{P}_{0}-\mathrm{P}_{t}
$$

For a first order reaction,

$$
\begin{aligned}
k & =\frac{2.303}{t} \log \frac{\mathrm{P}_{0}}{\mathrm{P}_{0}-p} \\
& =\frac{2.303}{t} \log \frac{\mathrm{P}_{0}}{2 \mathrm{P}_{0}-\mathrm{P}_{t}}
\end{aligned}
$$

When $t=360 \mathrm{~s}$,

$$
k=\frac{2.303}{360 \mathrm{~s}} \log \frac{35.0}{2 \times 35.0-54.0}
$$

$=2.175 \times 10^{-3} \mathrm{~s}^{-1}$
When $t=720 \mathrm{~s}$,

$$
k=\frac{2.303}{720 \mathrm{~s}} \log \frac{35.0}{2 \times 35.0-63.0}
$$

$=2.235 \times 10^{-3} \mathrm{~s}^{-1}$
Hence, the average value of rate constant is

$$
\begin{aligned}
& k=\frac{\left(2.175 \times 10^{-3}\right)+\left(2.235 \times 10^{-3}\right)}{2} \mathrm{~s}^{-1} \\
& =2.21 \times 10^{-3} \mathrm{~s}^{-1}
\end{aligned}
$$

Note: There is a slight variation in this answer and the one given in the NCERT textbook.
:::

:::answer
**Answer:** Average $k = 2.21 \times 10^{-3} \mathrm{~s}^{-1}$
:::

:::

:::question{number="3.21" kind="exercise" id="q_3.21" topic="Rate from total pressure data"}
#### Question 3.21

:::prompt
The following data were obtained during the first order thermal decomposition of $\mathrm{SO}_{2} \mathrm{Cl}_{2}$ at a constant volume.

$$
\mathrm{SO}_{2} \mathrm{Cl}_{2}(\mathrm{~g}) \rightarrow \mathrm{SO}_{2}(\mathrm{~g})+\mathrm{Cl}_{2}(\mathrm{~g})
$$

| Experiment | Time $/ \mathrm{s}^{-1}$ | Total pressure/atm |
| :--- | :--- | :--- |
| 1 | 0 | 0.5 |
| 2 | 100 | 0.6 |

Calculate the rate of the reaction when total pressure is 0.65 atm.
:::

:::solution{label="Solution"}
The thermal decomposition of $\mathrm{SO}_{2} \mathrm{Cl}_{2}$ at a constant volume is represented by the following equation.

$$
\mathrm{SO}_{2} \mathrm{Cl}_{2(g)} \longrightarrow \mathrm{SO}_{2(g)}+\mathrm{Cl}_{2(g)}
$$

At $t=0 \quad \mathrm{P}_{0} \quad 0 \quad 0$
At $t=t \quad \mathrm{P}_{0}-\mathrm{p} \quad \mathrm{p} \quad \mathrm{p}$

$$
\mathrm{P}_{l}=\left(\mathrm{P}_{0}-p\right)+p+p
$$

After time, $t$, total pressure,

$$
\begin{aligned}
& \Rightarrow \mathrm{P}_{t}=\mathrm{P}_{0}+p \\
& \Rightarrow p=\mathrm{P}_{\mathrm{t}}-\mathrm{P}_{0}
\end{aligned}
$$

$$
\mathrm{P}_{0}-p=\mathrm{P}_{0}-\left(\mathrm{P}_{1}-\mathrm{P}_{0}\right)
$$

Therefore,

$$
=2 P_{0}-P_{t}
$$

For a first order reaction,

$$
\begin{aligned}
k & =\frac{2.303}{t} \log \frac{\mathrm{P}_{0}}{\mathrm{P}_{0}-p} \\
& =\frac{2.303}{t} \log \frac{\mathrm{P}_{0}}{2 \mathrm{P}_{0}-\mathrm{P}_{t}}
\end{aligned}
$$

When

$$
k=\frac{2.303}{100 \mathrm{~s}} \log \frac{0.5}{2 \times 0.5-0.6} t=100 \mathrm{~s},
$$

$$
=2.231 \times 10^{-3} \mathrm{~s}^{-1}
$$

When $\mathrm{P}_{t}=0.65 \mathrm{~atm}$,

$$
\begin{aligned}
& \mathrm{P}_{0}+p=0.65 \\
& \Rightarrow p=0.65-\mathrm{P}_{0} \\
& =0.65-0.5 \\
& =0.15 \text { atm }
\end{aligned}
$$

Therefore, when the total pressure is 0.65 atm, pressure of $\mathrm{SOCl}_{2}$ is

$$
\begin{aligned}
& p_{\mathrm{SOCl}_{2}}=\mathrm{P}_{0}-\mathrm{p} \\
& =0.5-0.15 \\
& =0.35 \mathrm{~atm}
\end{aligned}
$$

Therefore, the rate of equation, when total pressure is 0.65 atm, is given by,

$$
\begin{aligned}
& \text { Rate }=k\left(p_{\mathrm{SoCl}_{2}}\right) \\
& =\left(2.23 \times 10^{-3} \mathrm{~s}^{-1}\right)(0.35 \mathrm{~atm}) \\
& =7.8 \times 10^{-4} \mathrm{~atm} \mathrm{~s}^{-1}
\end{aligned}
$$
:::

:::answer
**Answer:** Rate (at total pressure 0.65 atm) $=7.8 \times 10^{-4} \mathrm{~atm} \mathrm{~s}^{-1}$
:::

:::

:::question{number="3.22" kind="exercise" id="q_3.22" topic="Arrhenius plot and prediction" corrections_applied="4"}
#### Question 3.22

:::prompt
The rate constant for the decomposition of $\mathrm{N}_{2} \mathrm{O}_{5}$ at various temperatures is given below:

| $T /{ }^{\circ} \mathrm{C}$ | 0 | 20 | 40 | 60 | 80 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| $10^{5} \times \mathrm{k} / \mathrm{s}^{-1}$ | 0.0787 | 1.70 | 25.7 | 178 | 2140 |

Draw a graph between $\ln k$ and $1 / T$ and calculate the values of $A$ and $E_{\mathrm{a}}$. Predict the rate constant at 30° and 50°C.
:::

:::solution{label="Solution"}
From the given data, we obtain

| T/ °C | 0 | 20 | 40 | 60 | 80 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| T/K | 273 | 293 | 313 | 333 | 353 |

| $10^{3} \times \frac{1}{T}\left(\mathrm{~K}^{-1}\right) \longrightarrow$ | $3.66 \times 10^{-3}$ | $3.41 \times 10^{-3}$ | $3.19 \times 10^{-3}$ | $3.0 \times 10^{-3}$ | $2.83 \times 10^{-3}$ |
| :--- | :--- | :--- | :--- | :--- | :--- |
|  $10^{5} \times k/\mathrm{s}^{-1}$ | 0.0787 | 1.70 | 25.7 | 178 | 2140 |
|  $\ln k$ | -7.147 | - 4.075 | -1.359 | -0.577 | 3.063 |
|  

Slope of the line,

$$
\frac{y_{2}-y_{1}}{x_{2}-x_{1}}=-12.301 \mathrm{~K}
$$

According to Arrhenius equation,

$$
\begin{aligned}
& \text { Slope }=-\frac{E_{a}}{\mathrm{R}} \\
& \Rightarrow E_{a}=- \text { Slope } \times \mathrm{R} \\
& =-(-12.301 \mathrm{~K}) \times\left(8.314 \mathrm{JK}^{-1} \mathrm{~mol}^{-1}\right) \\
& =102.27 \mathrm{~kJ} \mathrm{~mol}^{-1}
\end{aligned}
$$

Again,

$$
\begin{aligned}
& \ln k=\ln A-\frac{E_{a}}{\mathrm{R} T} \\
& \ln A=\ln k+\frac{E_{a}}{\mathrm{R} T}
\end{aligned}
$$

When $T=273 \mathrm{~K}$,
$\ln k=-7.147$

$$
\text { Then, } \begin{aligned}
\ln A & =-7.147+\frac{102.27 \times 10^{3}}{8.314 \times 273} \\
& =37.911
\end{aligned}
$$

Therefore, $A=2.91 \times 10^{6}$
When $T=30+273 \mathrm{~K}=303 \mathrm{~K}$,

$$
\frac{1}{T}=0.0033 \mathrm{~K}=3.3 \times 10^{-3} \mathrm{~K}
$$

Then, ${ }^{\text {at }} \frac{1}{T}=3.3 \times 10^{-3} \mathrm{~K}$,

$$
\ln k=-2.8
$$

Therefore, $k=6.08 \times 10^{-2} \mathrm{~s}^{-1}$
Again, when $T=50+273 \mathrm{~K}=323 \mathrm{~K}$

$$
\frac{1}{T}=0.0031 \mathrm{~K}=3.1 \times 10^{-3} \mathrm{~K}
$$

Then, at $\frac{1}{T}=3.1 \times 10^{-3} \mathrm{~K}$

$$
\operatorname{In} k=-0.5
$$

Therefore, $k=0.607 \mathrm{~s}^{-1}$
:::

:::answer
**Answer:** $E_{a}=102.27 \mathrm{~kJ} \mathrm{~mol}^{-1}$; $A=2.91 \times 10^{6}$; $k(30^{\circ}\mathrm{C})=6.08 \times 10^{-2} \mathrm{~s}^{-1}$; $k(50^{\circ}\mathrm{C})=0.607 \mathrm{~s}^{-1}$
:::

:::

:::question{number="3.23" kind="exercise" id="q_3.23" topic="Pre-exponential factor calculation"}
#### Question 3.23

:::prompt
The rate constant for the decomposition of hydrocarbons is $2.418 \times 10^{-5} \mathrm{~s}^{-1}$ at 546 K. If the energy of activation is $179.9 \mathrm{~kJ} / \mathrm{mol}$, what will be the value of pre-exponential factor.
:::

:::solution{label="Solution"}
$k=2.418 \times 10^{-5} \mathrm{~s}^{-1}$

$$
\begin{aligned}
& T=546 \mathrm{~K} \\
& E_{\mathrm{a}}=179.9 \mathrm{~kJ} \mathrm{~mol}^{-1}=179.9 \times 10^{3} \mathrm{~J} \mathrm{~mol}^{-1}
\end{aligned}
$$

According to the Arrhenius equation,

$$
\begin{aligned}
& k=\mathrm{Ae}^{-E_{a} / \mathrm{R} T} \\
& \Rightarrow \ln k=\ln \mathrm{A}-\frac{E_{a}}{\mathrm{R} T} \\
& \begin{aligned}
& \Rightarrow \log k=\log \mathrm{A}-\frac{E_{a}}{2.303 \mathrm{R} T} \\
& \Rightarrow \log \mathrm{~A}=\log k+\frac{E_{a}}{2.303 \mathrm{R} T} \\
&=\log \left(2.418 \times 10^{-5} \mathrm{~s}^{-1}\right)+\frac{179.9 \times 10^{3} \mathrm{~J} \mathrm{~mol}^{-1}}{2.303 \times 8.314 \mathrm{Jk}^{-1} \mathrm{~mol}^{-1} \times 546 \mathrm{~K}} \\
&=(0.3835-5)+17.2082 \\
&=12.5917
\end{aligned}
\end{aligned}
$$

Therefore, A = antilog (12.5917)

$$
=3.9 \times 10^{12} \mathrm{~s}^{-1} \text { (approximately) }
$$
:::

:::answer
**Answer:** $A=3.9 \times 10^{12} \mathrm{~s}^{-1}$
:::

:::

:::question{number="3.24" kind="exercise" id="q_3.24" topic="Concentration remaining after time"}
#### Question 3.24

:::prompt
Consider a certain reaction A → Products with $k=2.0 \times 10^{-2} \mathrm{~s}^{-1}$. Calculate the concentration of $A$ remaining after 100 s if the initial concentration of $A$ is $1.0 \mathrm{~mol} \mathrm{~L}^{-1}$.
:::

:::solution{label="Solution"}
$k=2.0 \times 10^{-2} \mathrm{~s}^{-1} T=100 \mathrm{~s}$

$$
[\mathrm{A}]_{\mathrm{o}}=1.0 \mathrm{moL}^{-1}
$$

Since the unit of $k$ is $\mathrm{s}^{-1}$, the given reaction is a first order reaction.
Therefore,

$$
k=\frac{2.303}{t} \log \frac{[\mathrm{~A}]_{0}}{[\mathrm{~A}]}
$$

$$
\begin{aligned}
& \Rightarrow 2.0 \times 10^{-2} \mathrm{~s}^{-1}=\frac{2.303}{100 \mathrm{~s}} \log \frac{1.0}{[\mathrm{~A}]} \\
& \Rightarrow 2.0 \times 10^{-2} \mathrm{~s}^{-1}=\frac{2.303}{100 \mathrm{~s}}(-\log [\mathrm{A}]) \\
& \Rightarrow-\log [\mathrm{A}]=\frac{2.0 \times 10^{-2} \times 100}{2.303} \\
& \Rightarrow[\mathrm{~A}]=\operatorname{anti} \log \left(-\frac{2.0 \times 10^{-2} \times 100}{2.303}\right) \\
& =0.135 \mathrm{~mol} \mathrm{~L}^{-1} \text { (approximately) }
\end{aligned}
$$

Hence, the remaining concentration of A is $0.135 \mathrm{~mol} \mathrm{~L}^{-1}$.
:::

:::answer
**Answer:** $[\mathrm{A}]=0.135 \mathrm{~mol} \mathrm{~L}^{-1}$
:::

:::

:::question{number="3.25" kind="exercise" id="q_3.25" topic="Fraction remaining after decay"}
#### Question 3.25

:::prompt
Sucrose decomposes in acid solution into glucose and fructose according to the first order rate law, with $t_{1 / 2}=3.00$ hours. What fraction of sample of sucrose remains after 8 hours ?
:::

:::solution{label="Solution"}
For a first order reaction,

$$
k=\frac{2.303}{t} \log \frac{[\mathrm{R}]_{0}}{[\mathrm{R}]}
$$

It is given that, $t_{1 / 2}=3.00$ hours
Therefore,

$$
k=\frac{0.693}{t_{1 / 2}}
$$

$$
\begin{aligned}
& =\frac{0.693}{3} \mathrm{~h}^{-1} \\
& =0.231 \mathrm{~h}^{-1}
\end{aligned}
$$

Then, $0.231 \mathrm{~h}^{-1}=\frac{2.303}{8 \mathrm{~h}} \log \frac{[\mathrm{R}]_{0}}{[\mathrm{R}]}$

$$
\begin{gathered}
\Rightarrow \log \frac{[\mathrm{R}]_{0}}{[\mathrm{R}]}=\frac{0.231 \mathrm{~h}^{-1} \times 8 \mathrm{~h}}{2.303} \\
\Rightarrow \frac{[\mathrm{R}]_{0}}{[\mathrm{R}]}=\operatorname{antilog}(0.8024) \\
\Rightarrow \frac{[\mathrm{R}]_{0}}{[\mathrm{R}]}=6.3445 \\
\Rightarrow \frac{[\mathrm{R}]}{[\mathrm{R}]_{0}}=0.1576 \text { (approx) } \\
=0.158
\end{gathered}
$$

Hence, the fraction of sample of sucrose that remains after 8 hours is 0.158 .
:::

:::answer
**Answer:** Fraction of sucrose remaining after 8 hours $=0.158$
:::

:::

:::question{number="3.26" kind="exercise" id="q_3.26" topic="Activation energy from Arrhenius form"}
#### Question 3.26

:::prompt
The decomposition of hydrocarbon follows the equation
$$
k=\left(4.5 \times 10^{11} \mathrm{~s}^{-1}\right) \mathrm{e}^{-28000 K / T}
$$
Calculate $E_{\mathrm{a}}$.
:::

:::solution{label="Solution"}
The given equation is $k=(4.5 \times$

$$
\left.10_{11} \mathrm{~S}-1\right) \mathrm{e}-28000 \mathrm{~K} / T(\mathrm{i})
$$

Arrhenius equation is given by,

$$
k=\mathrm{Ae}^{-E_{\alpha} / \mathrm{RT}}(\mathrm{ii})
$$

From equation (i) and (ii), we obtain

$$
\begin{aligned}
& \frac{E_{a}}{\mathrm{R} T}=\frac{28000 \mathrm{~K}}{T} \\
& \Rightarrow E_{a}=\mathrm{R} \times 28000 \mathrm{~K} \\
& =8.314 \mathrm{~J} \mathrm{~K}^{-1} \mathrm{~mol}^{-1} \times 28000 \mathrm{~K} \\
& =232792 \mathrm{~J} \mathrm{~mol}^{-1} \\
& =232.792 \mathrm{~kJ} \mathrm{~mol}^{-1}
\end{aligned}
$$
:::

:::answer
**Answer:** $E_{a}=232.792 \mathrm{~kJ} \mathrm{~mol}^{-1}$
:::

:::

:::question{number="3.27" kind="exercise" id="q_3.27" topic="Ea and temperature from rate equation"}
#### Question 3.27

:::prompt
The rate constant for the first order decomposition of $\mathrm{H}_{2} \mathrm{O}_{2}$ is given by the following equation:
$$
\log k=14.34-1.25 \times 10^{4} K / T
$$
Calculate $E_{\mathrm{a}}$ for this reaction and at what temperature will its half-period be 256 minutes?
:::

:::solution{label="Solution"}
Arrhenius equation is given by,

$$
\begin{aligned}
& k=\mathrm{Ae}^{-E_{s} / \mathrm{R} T} \\
& \Rightarrow \ln k=\ln \mathrm{A}-\frac{E_{a}}{\mathrm{R} T} \\
& \Rightarrow \ln k=\log \mathrm{A}-\frac{E_{a}}{\mathrm{R} T} \\
& \Rightarrow \log k=\log \mathrm{A}-\frac{E_{a}}{2.303 \mathrm{R} T}
\end{aligned}
$$

The given equation is

$$
\log k=14.34-1.25 \times 10^{4} \mathrm{~K} / T
$$

From equation (i) and (ii), we obtain

$$
\begin{aligned}
& \frac{E_{a}}{2.303 \mathrm{R} T}=\frac{1.25 \times 10^{4} \mathrm{~K}}{T} \\
& \Rightarrow E_{a}=1.25 \times 10^{4} \mathrm{~K} \times 2.303 \times \mathrm{R} \\
& =1.25 \times 10^{4} \mathrm{~K} \times 2.303 \times 8.314 \mathrm{~J} \mathrm{~K}^{-1} \mathrm{~mol}^{-1} \\
& =239339.3 \mathrm{~J} \mathrm{~mol}^{-1} \text { (approximately) } \\
& =239.34 \mathrm{~kJ} \mathrm{~mol}^{-1}
\end{aligned}
$$

Also, when $t_{1 / 2}=256$ minutes,

$$
\begin{aligned}
k & =\frac{0.693}{t_{1 / 2}} \\
& =\frac{0.693}{256} \\
= & 2.707 \times 10^{-3} \mathrm{~min}^{-1} \\
= & 4.51 \times 10^{-5} \mathrm{~s}^{-1}
\end{aligned}
$$

It is also given that, $\log k=14.34-1.25 \times 10^{4} \mathrm{~K} / T$

$$
\begin{aligned}
& \Rightarrow \log \left(4.51 \times 10^{-5}\right)=14.34-\frac{1.25 \times 10^{4} \mathrm{~K}}{T} \\
& \Rightarrow \log (0.654-05)=14.34-\frac{1.25 \times 10^{4} \mathrm{~K}}{T} \\
& \Rightarrow \frac{1.25 \times 10^{4} \mathrm{~K}}{T}=18.686 \\
& \Rightarrow T=\frac{1.25 \times 10^{4} \mathrm{~K}}{18.686} \\
& =668.95 \mathrm{~K} \\
& =669 \mathrm{~K} \text { (approximately) }
\end{aligned}
$$
:::

:::answer
**Answer:** $E_{a}=239.34 \mathrm{~kJ} \mathrm{~mol}^{-1}$; $T=669$ K (for $t_{1/2}=256$ min)
:::

:::

:::question{number="3.28" kind="exercise" id="q_3.28" topic="Temperature from Arrhenius equation"}
#### Question 3.28

:::prompt
The decomposition of A into product has value of $k$ as $4.5 \times 10^{3} \mathrm{~s}^{-1}$ at $10^{\circ} \mathrm{C}$ and energy of activation $60 \mathrm{~kJ} \mathrm{~mol}^{-1}$. At what temperature would $k$ be $1.5 \times 10^{4} \mathrm{~s}^{-1}$ ?
:::

:::solution{label="Solution"}
From Arrhenius equation, we obtain

$$
\log \frac{k_{2}}{k_{1}}=\frac{E_{a}}{2.303 \mathrm{R}}\left(\frac{T_{2}-T_{1}}{T_{1} T_{2}}\right)
$$

Also, $k_{1}=4.5 \times 10^{3} \mathrm{~s}^{-1}$

$$
\begin{aligned}
& T_{1}=273+10=283 \mathrm{Kk}_{2} \\
& =1.5 \times 10^{4} \mathrm{~s}^{-1} \\
& E_{a}=60 \mathrm{~kJ} \mathrm{~mol}^{-1}=6.0 \times 10^{4} \mathrm{~J} \mathrm{~mol}^{-1}
\end{aligned}
$$

Then,

$$
\begin{aligned}
& \log \frac{1.5 \times 10^{4}}{4.5 \times 10^{3}}=\frac{6.0 \times 10^{4} \mathrm{~J} \mathrm{~mol}^{-1}}{2.303 \times 8.314 \mathrm{~J} \mathrm{~K}^{-1} \mathrm{~mol}^{-1}}\left(\frac{T_{2}-283}{283 T_{2}}\right) \\
& \Rightarrow 0.5229=3133.627\left(\frac{T_{2}-283}{283 T_{2}}\right) \\
& \Rightarrow \frac{0.5229 \times 283 T_{2}}{3133.627}=T_{2}-283 \\
& \Rightarrow 0.0472 T_{2}=T_{2}-283 \\
& \Rightarrow 0.9528 T_{2}=283 \\
& \Rightarrow T_{2}=297.019 \mathrm{~K} \text { (approximately) } \\
& =297 \mathrm{~K} \\
& =24^{\circ} \mathrm{C}
\end{aligned}
$$

Hence, $k$ would be $1.5 \times 10^{4} \mathrm{~s}^{-1}$ at $24^{\circ} \mathrm{C}$.
Note: There is a slight variation in this answer and the one given in the NCERT textbook.
:::

:::answer
**Answer:** $T_{2}=297$ K $=24^{\circ}\mathrm{C}$
:::

:::

:::question{number="3.29" kind="exercise" id="q_3.29" topic="k and Ea from completion times"}
#### Question 3.29

:::prompt
The time required for 10\% completion of a first order reaction at 298K is equal to that required for its 25\% completion at 308K. If the value of $A$ is $4 \times 10^{10} \mathrm{~s}^{-1}$. Calculate $k$ at 318K and $E_{\mathrm{a}}$.
:::

:::solution{label="Solution"}
For a first order reaction,

$$
t=\frac{2.303}{k} \log \frac{a}{a-x}
$$

At 298 K,

$$
t=\frac{2.303}{k} \log \frac{100}{90}
$$

$=\frac{0.1054}{k}$
At 308 K,

$$
t^{\prime}=\frac{2.303}{k^{\prime}} \log \frac{100}{75}
$$

$$
=\frac{2.2877}{k^{\prime}}
$$

According to the question,

$$
\begin{aligned}
& t=t^{\prime} \\
& \Rightarrow \frac{0.1054}{k}=\frac{0.2877}{k^{\prime}} \\
& \Rightarrow \frac{k^{\prime}}{k}=2.7296
\end{aligned}
$$

From Arrhenius equation, we obtain

$$
\begin{aligned}
& \log \frac{k^{\prime}}{k}=\frac{E_{a}}{2.303 \mathrm{R}}\left(\frac{T^{\prime}-T}{T T^{\prime}}\right) \\
& \log (2.7296)=\frac{E_{a}}{2.303 \times 8.314}\left(\frac{308-298}{298 \times 308}\right) \\
& \begin{aligned}
E_{a} & =\frac{2.303 \times 8.314 \times 298 \times 308 \times \log (2.7296)}{308-298} \\
& =76640.096 \mathrm{~J} \mathrm{~mol}^{-1} \\
& =76.64 \mathrm{~kJ} \mathrm{~mol}^{-1}
\end{aligned}
\end{aligned}
$$

To calculate $k$ at 318 K ,
It is given that, $A=4 \times 10^{10} \mathrm{~s}^{-1}, T=318 \mathrm{~K}$
Again, from Arrhenius equation, we obtain

$$
\begin{aligned}
\log k & =\log A-\frac{E_{a}}{2.303 \mathrm{R} T} \\
& =\log \left(4 \times 10^{10}\right)-\frac{76.64 \times 10^{3}}{2.303 \times 8.314 \times 318} \\
& =(0.6021+10)-12.5876 \\
& =-1.9855
\end{aligned}
$$

$$
\text { Therefore, } \begin{aligned}
k & =\operatorname{Antilog}(-1.9855) \\
& =1.034 \times 10^{-2} \mathrm{~s}^{-1}
\end{aligned}
$$
:::

:::answer
**Answer:** $E_{a}=76.64 \mathrm{~kJ} \mathrm{~mol}^{-1}$; $k$ (at 318 K) $=1.034 \times 10^{-2} \mathrm{~s}^{-1}$
:::

:::

:::question{number="3.30" kind="exercise" id="q_3.30" topic="Activation energy from rate quadrupling" corrections_applied="1"}
#### Question 3.30

:::prompt
The rate of a reaction quadruples when the temperature changes from 293 K to 313 K. Calculate the energy of activation of the reaction assuming that it does not change with temperature.
:::

:::solution{label="Solution"}
From Arrhenius equation, we obtain

$$
\log \frac{k_{2}}{k_{1}}=\frac{E_{a}}{2.303 \mathrm{R}}\left(\frac{T_{2}-T_{1}}{T_{1} T_{2}}\right)
$$

It is given that, $k_{2}=4 k_{1}$

$$
\begin{aligned}
& T_{1}=293 \mathrm{~K} \\
& T_{2}=313 \mathrm{~K}
\end{aligned}
$$

$$
\begin{aligned}
& \text { Therefore, } \log \frac{4 k_{1}}{k_{2}}=\frac{E_{a}}{2.303 \times 8.314}\left(\frac{313-293}{293 \times 313}\right. \\
& \begin{aligned}
& \Rightarrow 0.6021=\frac{20 \times E_{a}}{2.303 \times 8.314 \times 293 \times 313} \\
& \Rightarrow E_{\alpha}=\frac{0.6021 \times 2.303 \times 8.314 \times 293 \times 313}{20} \\
& \quad=52863.33 \mathrm{~J} \mathrm{~mol}^{-1} \\
&=52.86 \mathrm{~kJ} \mathrm{~mol}^{-1}
\end{aligned}
\end{aligned}
$$

Hence, the required energy of activation is $52.86 \mathrm{kJmol}^{-1}$.
:::

:::answer
**Answer:** $E_{a}=52.86 \mathrm{~kJ} \mathrm{~mol}^{-1}$
:::

:::

## Additional Questions

:::question{number="3.1" kind="additional_exercise" id="it_3.1" topic="Average rate calculation"}
#### Additional Question 3.1

:::prompt
For the reaction R → P, the concentration of a reactant changes from 0.03M to 0.02M in 25 minutes. Calculate the average rate of reaction using units of time both in minutes and seconds.
:::

:::solution{label="Solution"}
$$
=-\frac{\Delta[\mathrm{R}]}{\Delta t}
$$

$$
\begin{aligned}
& =-\frac{[\mathrm{R}]_{2}-[\mathrm{R}]_{1}}{t_{2}-t_{1}} \\
& =-\frac{0.02-0.03}{25} \mathrm{M} \mathrm{~min}^{-1} \\
& =-\frac{-0.01}{25} \mathrm{M} \mathrm{~min}^{-1} \\
& =4 \times 10^{-4} \mathrm{M} \mathrm{~min}^{-1} \\
& =\frac{4 \times 10^{-4}}{60} \mathrm{M} \mathrm{~s}^{-1} \\
& =6.67 \times 10^{-6} \mathrm{M} \mathrm{~s}^{-1}
\end{aligned}
$$
:::

:::answer
**Answer:** $4 \times 10^{-4} \mathrm{M} \mathrm{~min}^{-1} = 6.67 \times 10^{-6} \mathrm{M} \mathrm{~s}^{-1}$
:::

:::

:::question{number="3.2" kind="additional_exercise" id="it_3.2" topic="Rate from concentration change"}
#### Additional Question 3.2

:::prompt
In a reaction, 2A → Products, the concentration of A decreases from 0.5 $\mathrm{mol} \mathrm{L}^{-1}$ to $0.4 \mathrm{~mol} \mathrm{L}^{-1}$ in 10 minutes. Calculate the rate during this interval?
:::

:::solution{label="Solution"}
$$
\text { Average rate }=-\frac{1}{2} \frac{\Delta[\mathrm{~A}]}{\Delta t}
$$

$$
\begin{aligned}
& =-\frac{1}{2} \frac{[\mathrm{~A}]_{2}-[\mathrm{~A}]_{1}}{t_{2}-t_{1}} \\
& =-\frac{1}{2} \frac{0.4-0.5}{10} \\
& =-\frac{1}{2} \frac{-0.1}{10} \\
& =0.005 \mathrm{~mol} \mathrm{~L}^{-1} \mathrm{~min}^{-1} \\
& =5 \times 10^{-3} \mathrm{M} \mathrm{~min}^{-1}
\end{aligned}
$$
:::

:::answer
**Answer:** $5 \times 10^{-3} \mathrm{M} \mathrm{~min}^{-1}$
:::

:::

:::question{number="3.3" kind="additional_exercise" id="it_3.3" topic="Order from rate law"}
#### Additional Question 3.3

:::prompt
For a reaction, $\mathrm{A}+\mathrm{B} \rightarrow$ Product; the rate law is given by, $r=k[\mathrm{~A}]^{1 / 2}[\mathrm{~B}]^{2}$. What is the order of the reaction?
:::

:::solution{label="Solution"}
$$
\begin{aligned}
& \qquad=\frac{1}{2}+2 \\
& \text { The order of the reaction } \\
& =2 \frac{1}{2} \\
& =2.5
\end{aligned}
$$
:::

:::answer
**Answer:** The order of the reaction $= 2.5$
:::

:::

:::question{number="3.4" kind="additional_exercise" id="it_3.4" topic="Second order rate effect"}
#### Additional Question 3.4

:::prompt
The conversion of molecules X to Y follows second order kinetics. If concentration of X is increased to three times how will it affect the rate of formation of Y ?
:::

:::solution{label="Solution"}
The reaction $X \rightarrow Y$ follows second order kinetics.
Therefore, the rate equation for this reaction will be:
Rate $=k[\mathrm{X}]^{2}(1)$
Let $[\mathrm{X}]=a \mathrm{~mol} \mathrm{~L}^{-1}$, then equation (1) can be written as:
Rate $_{1}=k .(a)^{2}$

$$
=k a^{2}
$$

If the concentration of X is increased to three times, then $[\mathrm{X}]=3 a \mathrm{~mol} \mathrm{~L}^{-1}$
Now, the rate equation will be:

$$
\begin{aligned}
& \text { Rate }=k(3 a)^{2} \\
& =9\left(k a^{2}\right)
\end{aligned}
$$

Hence, the rate of formation will increase by 9 times.
:::

:::answer
**Answer:** The rate of formation of Y will increase by 9 times.
:::

:::

:::question{number="3.5" kind="additional_exercise" id="it_3.5" topic="First order half-life time"}
#### Additional Question 3.5

:::prompt
A first order reaction has a rate constant $1.15 \times 10^{-3} \mathrm{~s}^{-1}$. How long will 5 g of this reactant take to reduce to 3 g?
:::

:::solution{label="Solution"}
From the question, we can write down the following information:
Initial amount = 5 g
Final concentration $=3 \mathrm{~g}$
Rate constant $=1.1510^{-3} \mathrm{~s}^{-1}$
We know that for a $1^{\text {st }}$ order reaction,

$$
\begin{aligned}
t & =\frac{2.303}{k} \log \frac{[\mathrm{R}]_{0}}{[\mathrm{R}]} \\
& =\frac{2.303}{1.15 \times 10^{-3}} \log \frac{5}{3} \\
& =\frac{2.303}{1.15 \times 10^{-3}} \times 0.2219 \\
= & 444.38 \mathrm{~s} \\
= & 444 \mathrm{~s} \text { (approx) }
\end{aligned}
$$
:::

:::answer
**Answer:** $t = 444 \mathrm{~s}$ (approx)
:::

:::

:::question{number="3.6" kind="additional_exercise" id="it_3.6" topic="Rate constant from half-life"}
#### Additional Question 3.6

:::prompt
Time required to decompose $\mathrm{SO}_{2} \mathrm{Cl}_{2}$ to half of its initial amount is 60 minutes. If the decomposition is a first order reaction, calculate the rate constant of the reaction.
:::

:::solution{label="Solution"}
We know that for a $1^{\text {st }}$ order reaction,

$$
t_{1 / 2}=\frac{0.693}{k}
$$

It is given that $\mathrm{t}_{1 / 2}=60 \mathrm{~min}$

$$
\begin{aligned}
\therefore k & =\frac{0.693}{t_{1 / 2}} \\
& =\frac{0.693}{60} \\
& =0.01155 \mathrm{~min}^{-1} \\
& =1.155 \mathrm{~min}^{-1}
\end{aligned}
$$

$$
\text { Or } k=1.925 \times 10^{-4} \mathrm{~s}^{-1}
$$
:::

:::answer
**Answer:** $k = 1.925 \times 10^{-4} \mathrm{~s}^{-1}$
:::

:::

:::question{number="3.7" kind="additional_exercise" id="it_3.7" topic="Temperature effect on rate constant"}
#### Additional Question 3.7

:::prompt
What will be the effect of temperature on rate constant ?
:::

:::solution{label="Solution"}
The rate constant of a reaction is nearly doubled with a $10^{\circ}$ rise in temperature. However, the exact dependence of the rate of a chemical reaction on temperature is given by Arrhenius equation,

$$
k=\mathrm{Ae}^{-\mathrm{Ea} / R T}
$$

Where,
A is the Arrhenius factor or the frequency factor
$T$ is the temperature
$R$ is the gas constant
$E_{\mathrm{a}}$ is the activation energy
:::

:::

:::question{number="3.8" kind="additional_exercise" id="it_3.8" topic="Activation energy calculation"}
#### Additional Question 3.8

:::prompt
The rate of the chemical reaction doubles for an increase of 10K in absolute temperature from 298K. Calculate $E_{\mathrm{a}}$.
:::

:::solution{label="Solution"}
It is given that $T_{1}=298 \mathrm{~K}$

$$
\begin{aligned}
& \therefore T_{2}=(298+10) \mathrm{K} \\
& =308 \mathrm{~K}
\end{aligned}
$$

We also know that the rate of the reaction doubles when temperature is increased by 10°.
Therefore, let us take the value of $k_{1}=k$ and that of $k_{2}=2 k$
Also, $R=8.314 \mathrm{~J} \mathrm{~K}^{-1} \mathrm{~mol}^{-1}$
Now, substituting these values in the equation:

$$
\log \frac{k_{2}}{k_{1}}=\frac{E_{a}}{2.303 R}\left[\frac{T_{2}-T_{1}}{T_{1} T_{2}}\right]
$$

We get:

$$
\begin{aligned}
& \log \frac{2 k}{k}=\frac{E_{\mathrm{a}}}{2.303 \times 8.314}\left[\frac{10}{298 \times 308}\right] \\
& \Rightarrow \log 2=\frac{E_{\mathrm{a}}}{2.303 \times 8.314}\left[\frac{10}{298 \times 308}\right] \\
& \Rightarrow E_{\mathrm{a}}=\frac{2.303 \times 8.314 \times 298 \times 308 \times \log 2}{10} \\
& =52897.78 \mathrm{~J} \mathrm{~mol}^{-1} \\
& =52.9 \mathrm{~kJ} \mathrm{~mol}^{-1}
\end{aligned}
$$

Note: There is a slight variation in this answer and the one given in the NCERT textbook.
:::

:::answer
**Answer:** $E_{a} = 52.9 \mathrm{~kJ} \mathrm{~mol}^{-1}$
:::

:::

:::question{number="3.9" kind="additional_exercise" id="it_3.9" topic="Fraction of molecules with activation energy"}
#### Additional Question 3.9

:::prompt
The activation energy for the reaction
$$
2 \mathrm{HI}(\mathrm{g}) \rightarrow \mathrm{H}_{2}+\mathrm{I}_{2}(\mathrm{g})
$$
is $209.5 \mathrm{~kJ} \mathrm{~mol}^{-1}$ at 581 K .Calculate the fraction of molecules of reactants having energy equal to or greater than activation energy?
:::

:::solution{label="Solution"}
In the given case:

$$
\begin{aligned}
& E_{\mathrm{a}}=209.5 \mathrm{~kJ} \mathrm{~mol}^{-1}=209500 \mathrm{~J} \mathrm{~mol}^{-1} \\
& T=581 \mathrm{~K} \\
& R=8.314 \mathrm{JK}^{-1} \mathrm{~mol}^{-1}
\end{aligned}
$$

Now, the fraction of molecules of reactants having energy equal to or greater than activation energy is given as:

$$
\begin{aligned}
& x=\mathrm{e}^{-E a / R T} \\
& \Rightarrow \ln x=-E_{\mathrm{a}} / R T
\end{aligned}
$$

$$
\Rightarrow \log x=-\frac{E_{\mathrm{a}}}{2.303 R T}
$$

$$
\Rightarrow \log x=\frac{209500 \mathrm{~J} \mathrm{~mol}^{-1}}{2.303 \times 8.314 \mathrm{JK}^{-1} \mathrm{~mol}^{-1} \times 581}=18.8323
$$

Now, $x=\operatorname{Antilog}(18.8323)$

$$
\begin{aligned}
& =\text { Anti } \log \overline{19} .1677 \\
& =1.471 \times 10^{-19}
\end{aligned}
$$
:::

:::answer
**Answer:** $x = 1.471 \times 10^{-19}$
:::

:::
