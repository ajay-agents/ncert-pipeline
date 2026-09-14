---
subject: physics
class: 12
chapter: 7
lang: hi
title: "प्रत्यावर्ती धारा"
---

# प्रत्यावर्ती धारा

## प्रश्न और हल

:::question{number="7.1" kind="exercise" id="q_7.1" topic="प्रतिरोधक में rms धारा व शक्ति क्षय"}
#### प्रश्न 7.1

:::prompt
एक $100 \Omega$ का प्रतिरोधक $200 \mathrm{~V}, 50 \mathrm{~Hz}$ आपूर्ति से संयोजित है। (a) परिपथ में धारा का rms मान कितना है? (b) एक पूरे चक्र में कितनी नेट शक्ति व्यय होती है।
:::

:::part{label="a"}
:::prompt
परिपथ में धारा का rms मान कितना है?
:::

:::solution
हल प्रतिरोध $R=100 \Omega$
$$
V_{\mathrm{ms}}=220 \mathrm{~V}
$$
जब कभी सप्लाई दी होती है, इसका अर्थ है कि वह वर्ग माध्य मूल मान है।
$$
\text { आवृत्ति }(f)=50 \mathrm{~Hz}
$$
परिपथ में धारा
$$
l_{\mathrm{rms}}=\frac{V_{\mathrm{ms}}}{R}=\frac{220}{100}=2.2 \mathrm{~A}
$$
:::

:::answer
**उत्तर:** $I_{rms}=2.2\ \mathrm{A}$
:::

:::

:::part{label="b"}
:::prompt
एक पूरे चक्र में कितनी नेट शक्ति व्यय होती है।
:::

:::solution
पूर्ण चक्र में शक्ति व्यय
$$
\begin{aligned}
P & =V_{\mathrm{rms}} \times l_{\mathrm{rms}} \\
& =220 \times 2.2=484 \mathrm{~W}
\end{aligned}
$$
:::

:::answer
**उत्तर:** $P=484\ \mathrm{W}$
:::

:::

:::answer
**उत्तर:** $I_{rms}=2.2\ \mathrm{A}$, $P=484\ \mathrm{W}$
:::

:::

:::question{number="7.2" kind="exercise" id="q_7.2" topic="शिखर व rms मानों का रूपांतरण"}
#### प्रश्न 7.2

:::prompt
(a) ac आपूर्ति का शिखर मान $300$ V है। rms वोल्टता कितनी है? (b) ac परिपथ में धारा का rms मान $10$ A है। शिखर धारा कितनी है?
:::

:::part{label="a"}
:::prompt
ac आपूर्ति का शिखर मान $300$ V है। rms वोल्टता कितनी है?
:::

:::solution
हल दिया है, वोल्टेज का उच्चतम मान $V_{0}=300 \mathrm{~V}$, धारा का वर्ग माध्य मूल मान $I_{\mathrm{ms}}=10 \mathrm{~A}$
वोल्टेज का वर्ग माध्य मूल मान $V_{\mathrm{rms}}=\frac{V_{0}}{\sqrt{2}}=\frac{300}{\sqrt{2}}=212.1 \mathrm{~V}$
:::

:::answer
**उत्तर:** $V_{rms}=212.1\ \mathrm{V}$
:::

:::

:::part{label="b"}
:::prompt
ac परिपथ में धारा का rms मान $10$ A है। शिखर धारा कितनी है?
:::

:::solution
सूत्र $l_{\mathrm{ms}}=\frac{l_{0}}{\sqrt{2}}$ प्रयुक्त करने पर
धारा का उच्चतम मान $l_{0}=\sqrt{2} l_{\text {mrs }}=\sqrt{2} \times 10=14.14 \mathrm{~A}$
:::

:::answer
**उत्तर:** $I_0=14.14\ \mathrm{A}$
:::

:::

:::answer
**उत्तर:** $V_{rms}=212.1\ \mathrm{V}$, $I_0=14.14\ \mathrm{A}$
:::

:::

:::question{number="7.3" kind="exercise" id="q_7.3" topic="प्रेरक की rms धारा"}
#### प्रश्न 7.3

:::prompt
एक $44 \mathrm{mH}$ का प्रेरित्र $220 \mathrm{~V}, 50 \mathrm{~Hz}$ आपूर्ति से जोड़ा गया है। परिपथ में धारा के rms मान को ज्ञात कीजिए।
:::

:::solution{label="हल"}
हल दिया है, प्रेरकत्व $L=44 \mathrm{mH}=44 \times 10^{-3} \mathrm{H}$
$$
V_{\mathrm{rms}}=220 \mathrm{~V}
$$
प्रेरक की आवृत्ति $f=50 \mathrm{~Hz}$
प्रेरणिक प्रतिघात $X_{L}=2 \pi f L$
$$
\begin{aligned}
& =2 \times 3.14 \times 50 \times 44 \times 10^{-3} \\
& =13.83 \Omega
\end{aligned}
$$
परिपथ में धारा का rms मान
$$
l_{\mathrm{rms}}=\frac{V_{\mathrm{rms}}}{X_{L}}=\frac{220}{13.83}=15.9 \mathrm{~A}
$$
:::

:::answer
**उत्तर:** $I_{rms}=15.9\ \mathrm{A}$
:::

:::

:::question{number="7.4" kind="exercise" id="q_7.4" topic="संधारित्र की rms धारा"}
#### प्रश्न 7.4

:::prompt
एक $60 \mu \mathrm{~F}$ का संधारित्र $110 \mathrm{~V}, 60 \mathrm{~Hz}$ ac आपूर्ति से जोड़ा गया है। परिपथ में धारा के rms मान को ज्ञात कीजिए।
:::

:::solution{label="हल"}
हल दिया है, संधारित्र की धारिता $C=60 \mu \mathrm{~F}=60 \times 10^{-6} \mathrm{~F}$
$$
V_{\mathrm{rms}}=110 \mathrm{~V}
$$
AC परिपथ की आवृत्ति $f=60 \mathrm{~Hz}$
धारितीय प्रतिघात $X_{C}=\frac{1}{2 \pi f C}=\frac{1}{2 \times 3.14 \times 60 \times 60 \times 10^{-6}}$
$$
=44.23 \Omega
$$
परिपथ में धारा का वर्ग माघ्य मूल मान
$$
\begin{aligned}
I_{\mathrm{ms}} & =\frac{V_{\mathrm{rms}}}{X_{c}} \\
& =\frac{110}{44.23}=2.49 \mathrm{~A}
\end{aligned}
$$
:::

:::answer
**उत्तर:** $I_{rms}=2.49\ \mathrm{A}$
:::

:::

:::question{number="7.5" kind="exercise" id="q_7.5" topic="प्रेरक व संधारित्र में शक्ति क्षय"}
#### प्रश्न 7.5

:::prompt
अभ्यास $7.3$ व $7.4$ में एक पूरे चक्र की अवधि में प्रत्येक परिपथ में कितनी नेट शक्ति अवशोषित होती है? अपने उत्तर का विवरण दीजिए।
:::

:::solution{label="हल"}
हल प्रश्न $3$ में औसत शक्ति $P=V_{\mathrm{rms}} I_{\mathrm{rms}} \cos \phi$
हम जानते हैं कि धारा तथा वोल्टेज के बीच कलान्तर $90^{\circ}$ है।
$$
P=V_{\mathrm{rms}} I_{\mathrm{rms}} \cos 90^{\circ}=0
$$
प्रश्न $4$ में औसत शक्ति $P=V_{\mathrm{ms}} \cdot I_{\mathrm{ms}} \cos \phi$
हम जानते हैं कि धारा तथा वोल्टेज के बीच कलान्तर $90^{\circ}$ है।
$$
P=V_{\mathrm{rms}} I_{\mathrm{rms}} \cos 90^{\circ}=0
$$
:::

:::answer
**उत्तर:** $P=0$ दोनों परिपथों में
:::

:::

:::question{number="7.6" kind="exercise" id="q_7.6" topic="LC परिपथ की मुक्त दोलन आवृत्ति"}
#### प्रश्न 7.6

:::prompt
$30 \mu \mathrm{~F}$ का एक आवेशित संधारित्र $27 \mathrm{mH}$ के प्रेरित्र से जोड़ा गया है। परिपथ के मुक्त दोलनों की कोणीय आवृत्ति कितनी है?
:::

:::solution{label="हल"}
हल संधारित्र की धारिता $\mathrm{C}=30 \mu \mathrm{~F}=30 \times 10^{-6} \mathrm{~F}$
प्रेरकत्व $L=27 \mathrm{mH}=27 \times 10^{-3} \mathrm{H}$
स्वतन्त्र दोलन हेतु कोणीय आवृति
$$
\begin{aligned}
\omega_{r} & =\frac{1}{\sqrt{L C}} \\
& =\frac{1}{\sqrt{27 \times 10^{-3} \times 30 \times 10^{-6}}}=\frac{10^{4}}{9} \\
& =1.1 \times 10^{3} \mathrm{rad} / \mathrm{s}
\end{aligned}
$$
:::

:::answer
**उत्तर:** $\omega_r=1.1\times10^{3}\ \mathrm{rad/s}$
:::

:::

:::question{number="7.7" kind="exercise" id="q_7.7" topic="अनुनाद पर LCR परिपथ में माध्य शक्ति"}
#### प्रश्न 7.7

:::prompt
एक श्रेणीबद्ध $L C R$ परिपथ को, जिसमें $R=20 \Omega, L=1.5 \mathrm{H}$ तथा $C=35 \mu \mathrm{~F}$, एक परिवर्ती आवृत्ति की $200 \mathrm{~V} \mathrm{ac}$ आपूर्ति से जोड़ा गया है। जब आपूर्ति की आवृत्ति परिपथ की मूल आवृत्ति के बराबर होती है तो एक पूरे चक्र में परिपथ को स्थानांतरित की गई माध्य शक्ति कितनी होगी?
:::

:::solution{label="हल"}
हल दिया है, प्रतिरोध $R=20 \Omega$, प्रेरकत्व $L=1.5 \mathrm{H}$, धारिता $C=35 \mu \mathrm{~F}=35 \times 10^{-6} \mathrm{~F}$ तथा वोल्टेज $V_{\mathrm{ms}}=200 \mathrm{~V}$
जब परिपथ की आवृति आरोपित वोल्टेज की आवृत्ति के बराबर है तब यह अवस्था अनुनाद की अवस्था कहलाती है।
प्रतिबाधा $Z=R=20 \Omega$
परिपथ में धारा का rms मान
$$
\begin{aligned}
l_{\mathrm{ms}}=\frac{V_{\mathrm{rms}}}{Z} & =\frac{200}{20}=10 \mathrm{~A} \\
\phi & =0^{\circ}
\end{aligned}
$$
(अनुनाद हेतु)
एक चक्र में परिपथ में स्थानान्तरित शक्ति
$$
\begin{aligned}
P=I_{\mathrm{ms}} \cdot V_{\mathrm{ms}} \cos \phi & =10 \times 200 \times \cos 0^{\circ}=2000 \mathrm{~W} \\
& =2 \mathrm{~kW}
\end{aligned}
$$
:::

:::answer
**उत्तर:** $P=2\ \mathrm{kW}$
:::

:::

:::question{number="7.8" kind="exercise" id="q_7.8" topic="श्रेणीबद्ध LCR परिपथ: अनुनाद व घटकों पर वोल्टता"}
#### प्रश्न 7.8

:::prompt
चित्र $7.17$ में एक श्रेणीबद्ध $L C R$ परिपथ दिखलाया गया है जिसे परिवर्ती आवृत्ति के $230$ V के स्रोत से जोड़ा गया है। $L=5.0 \mathrm{H}, C=80 \mu \mathrm{~F}, R=40 \Omega$ (a) स्रोत की आवृत्ति निकालिए जो परिपथ में अनुनाद उत्पन्न करे। (b) परिपथ की प्रतिबाधा तथा अनुनादी आवृत्ति पर धारा का आयाम निकालिए। (c) परिपथ के तीनों अवयवों के सिरों पर विभवपात के rms मानों को निकालिए। दिखलाइए कि अनुनादी आवृत्ति पर $L C$ संयोग के सिरों पर विभवपात शून्य है।
:::

:::figure{src="images/fig_physics-12-7_14.jpg" id="fig_physics-12-7_14"}
चित्र 7.17
:::

:::part{label="a"}
:::prompt
स्रोत की आवृत्ति निकालिए जो परिपथ में अनुनाद उत्पन्न करे।
:::

:::solution
हल दिया है, वोल्टेज का rms मान $V_{\mathrm{ms}}=230 \mathrm{~V}$, प्रेरकत्व $L=5 \mathrm{H}$, धारिता $C=80 \mu \mathrm{~F}=80 \times 10^{-6} \mathrm{~F}$, प्रतिरोध $R=40 \Omega$

परिपथ की अनुनाद आवृत्ति
$$
\omega_{r}=\frac{1}{\sqrt{L C}}=\frac{1}{\sqrt{5 \times 80 \times 10^{-6}}}=50 \mathrm{rad} / \mathrm{s}
$$
अनुनाद में स्रोत की आवृत्ति
$$
\begin{aligned}
v_{0}=\frac{\omega_{0}}{2 \pi} & =\frac{50}{2 \times 3.14} \\
& =7.76 \mathrm{~Hz}
\end{aligned}
$$
:::

:::answer
**उत्तर:** $v_0=7.76\ \mathrm{Hz}$
:::

:::

:::part{label="b"}
:::prompt
परिपथ की प्रतिबाधा तथा अनुनादी आवृत्ति पर धारा का आयाम निकालिए।
:::

:::solution
अनुनादीय अवस्था में, $X_{L}=X_{C}$
परिपथ की प्रतिबाधा $Z=R$
$$
\therefore \quad \text { प्रतिबाघा } Z=40 \Omega
$$
परिपथ में धारा का rms मान
$$
l_{\mathrm{ms}}=\frac{V_{\mathrm{rms}}}{Z}=\frac{230}{40}=5.75 \mathrm{~A}
$$
धारा का आयाम $I_{0}=I_{\mathrm{ms}} \sqrt{2}$
$$
=5.75 \times \sqrt{2}=8.13 \mathrm{~A}
$$
:::

:::answer
**उत्तर:** $Z=40\ \Omega$, $I_0=8.13\ \mathrm{A}$
:::

:::

:::part{label="c"}
:::prompt
परिपथ के तीनों अवयवों के सिरों पर विभवपात के rms मानों को निकालिए। दिखलाइए कि अनुनादी आवृत्ति पर $L C$ संयोग के सिरों पर विभवपात शून्य है।
:::

:::solution
$L$ में rms विभव पतन
$$
\begin{aligned}
V_{L} & =I_{\mathrm{rms}} \times X_{L}=I_{\mathrm{rms}} \times \omega_{r} L \\
& =5.75 \times 50 \times 5=1437.5 \mathrm{~V}
\end{aligned}
$$
$R$ में rms विभव पतन
$$
V_{R}=I_{\mathrm{rms}} R=5.75 \times 40=230 \mathrm{~V}
$$
C में rms विभव पतन
$$
\begin{aligned}
V_{C} & =I_{\mathrm{rms}} \times X_{C}=I_{\mathrm{rms}} \times \frac{1}{\omega_{r}} \\
& =5.75 \times \frac{1}{50 \times 80 \times 10^{-6}} \\
& =1437.5 \mathrm{~V}
\end{aligned}
$$
L-C समायोजन में विभव पतन
$$
\begin{aligned}
& =I_{\text {rms }}\left(X_{L}-X_{C}\right) \\
& =I_{\text {rms }}\left(X_{L}-X_{L}\right)=0 \quad\left(\because X_{L}=X_{C} \text { अनुनाद में }\right)
\end{aligned}
$$
:::

:::answer
**उत्तर:** $V_L=V_C=1437.5\ \mathrm{V}$, $V_R=230\ \mathrm{V}$, $L\text{-}C$ पर विभवपात $=0$
:::

:::

:::
