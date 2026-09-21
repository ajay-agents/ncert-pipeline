---
subject: chemistry
class: 12
chapter: 3
lang: en
title: "Chemical Kinetics"
---

# Chemical Kinetics

## Examples

:::example{number="3.1" kind="example" id="ex_3.1" topic="Average and instantaneous rate from concentration data"}
#### Example 3.1

:::prompt
From the concentrations of $\mathrm{C}_{4} \mathrm{H}_{9} \mathrm{Cl}$ (butyl chloride) at different times given Example 3.1 below, calculate the average rate of the reaction:

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


![](images/fig_3_16.jpg)
Fig 3.2
Instantaneous rate of hydrolysis of butyl chloride $\left(\mathrm{C}_{4} \mathrm{H}_{9} \mathrm{Cl}\right)$

![](images/fig_3_17.jpg)
(3.3)

(3.3)
![](images/fig_3_18.jpg)

It can be determined graphically by drawing a tangent at time t on either of the curves for concentration of R and P vs time t and calculating its slope (Fig. 3.1). So in problem 3.1, $r_{\text {inst }}$ at 600s for example, can be calculated by plotting concentration of butyl chloride as a function of time. A tangent is drawn that touches the curve at $t=600 \mathrm{~s}$ (Fig. 3.2).

The slope of this tangent gives the instantaneous rate.

$$
\begin{aligned}
& \text { So, } r_{\text {inst }} \text { at } 600 \mathrm{~s}=-\left(\frac{0.0165-0.037}{(800-400) \mathrm{s}}\right) \mathrm{mol} \\
& \text { At } t=250 \mathrm{~s} \quad r_{\text {inst }}=1.22 \times 10^{-4} \mathrm{~mol} \mathrm{~L}^{-1} \mathrm{~s}^{-1} \\
& t=350 \mathrm{~s} \quad r_{\text {inst }}=1.0 \times 10^{-4} \mathrm{~mol} \mathrm{~L}^{-1} \mathrm{~s}^{-1} \\
& t=450 \mathrm{~s} \quad r_{\text {inst }}=6.4 \times 10^{-5} \mathrm{~mol} \mathrm{~L}^{-1} \mathrm{~s}^{-1}
\end{aligned}
$$
:::

:::

:::example{number="3.2" kind="example" id="ex_3.2" topic="Average rate of N2O5 decomposition in different time units"}
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
& \text { Average Rate }=\frac{1}{2}-\frac{\Delta\left[\mathrm{N}_{2} \mathrm{O}_{5}\right]}{\Delta t}=-\frac{1}{2} \frac{(2.08-2.33) \mathrm{mol} \mathrm{~L}^{-1}}{184 \mathrm{~min}^{-1}} \\
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

:::example{number="3.10" kind="example" id="ex_3.10" topic="Rate constant of ethyl iodide decomposition at a new temperature"}
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
& =\log \left(1.60 \times 10^{-5}\right)+\frac{209000 \mathrm{~J} \mathrm{~mol}^{-1}}{2.303 \times 8.314 \mathrm{~J} \mathrm{~mol}^{-1} \mathrm{~K}^{-1}}\left[\frac{1}{600 \mathrm{~K}}-\frac{1}{700 \mathrm{~K}}\right]
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
