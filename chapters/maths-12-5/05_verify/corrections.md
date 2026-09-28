### q_5.2.7 — solution (en)
- **Confidence:** high
- **Reason:** solutions.en.pdf page 43 (file page) clearly shows "cosec^2(x^2)" (cosecant squared of x-squared) as a standard superscript, with no letter "e" between "cosec" and its exponent. The extracted text instead shows "cosec e^{2}", inserting a spurious "e" - a genuine mathpix OCR defect, confirmed by direct page-image inspection.
- **Found:**
  > \operatorname{cosec} e^{2}\left(x^{2}\right)
- **Should be:**
  > \operatorname{cosec}^{2}\left(x^{2}\right)

### ex_5.12 — solution (en)
- **Confidence:** high
- **Reason:** chapter.en.pdf page 8 (file page, printed page 111) shows the sentence "Graph of this function is given in the Fig 5.6. Note that to graph this function we need to lift the pen from the plane of the paper, but we need to do that only for those points where the function is not defined." A mathpix OCR dropout cut this off mid-sentence at "Note that to graph" - the rest of the sentence never made it into 01_mathpix/chapter.en.md at all (the very next line in the raw mathpix output jumps straight to "Example 13"), confirmed by direct page-image inspection.
- **Found:**
  > Note that to graph
- **Should be:**
  > Note that to graph this function we need to lift the pen from the plane of the paper, but we need to do that only for those points where the function is not defined.

### q_5.1.32 — solution (en)
- **Confidence:** high
- **Reason:** solutions.en.pdf page 33 (file page) shows this justification remark set off in a plain square bracket, not a ceiling-function delimiter - confirmed by direct page-image inspection. mathpix mis-OCR'd the bracket as `\lceil`/`\rceil` (ceiling notation), which this chapter never otherwise uses and which makes no mathematical sense here (a composition-of-functions justification note, not a ceiling function applied to any argument). Caught while checking stage 9's own converter output for unhandled LaTeX commands.
- **Found:**
  > \lceil\because(g o h)(x)=g(h(x))=g(\cos x)=|\cos x|=f(x)\rceil
- **Should be:**
  > [\because(g o h)(x)=g(h(x))=g(\cos x)=|\cos x|=f(x)]

### q_5.1.33 — solution (en)
- **Confidence:** high
- **Reason:** Same defect class as q_5.1.32 immediately above (confirmed on the same page image) - identical justification-remark shape, this time for g(x)=|x|, h(x)=sin x.
- **Found:**
  > \lceil\because(g o h)(x)=g(h(x))=g(\sin x)=|\sin x|=f(x)\rceil
- **Should be:**
  > [\because(g o h)(x)=g(h(x))=g(\sin x)=|\sin x|=f(x)]

### q_5.5.9 — solution (en)
- **Confidence:** high
- **Reason:** solutions.en.pdf page 72 (file page) shows du/dx = x^sin x [cos x log x + sin x/x] with a plain square bracket, matching the second bracket later in the same formula ([cot x cos x - sin x log(sin x)]) - confirmed by direct page-image inspection. mathpix mis-OCR'd only this first bracket as `\left\lceil`/`\right\rceil` (ceiling notation), inconsistent with its own sibling bracket in the identical formula.
- **Found:**
  > \left\lceil\cos x \log x+\frac{\sin x}{x}\right\rceil
- **Should be:**
  > \left[\cos x \log x+\frac{\sin x}{x}\right]

### q_5.5.11 — solution (en)
- **Confidence:** high
- **Reason:** Same defect class as q_5.5.9 above - a logarithmic-differentiation formula's own grouping bracket mis-OCR'd as ceiling notation.
- **Found:**
  > \left\lceil\frac{x \cot x+1-\log (x \sin x)}{x^{2}}\right\rceil
- **Should be:**
  > \left[\frac{x \cot x+1-\log (x \sin x)}{x^{2}}\right]

### q_5.misc.11 — solution (en)
- **Confidence:** high
- **Reason:** Same defect class as q_5.5.9/q_5.5.11 above - a logarithmic-differentiation formula's own grouping bracket mis-OCR'd as ceiling notation.
- **Found:**
  > \left\lceil\frac{x^{2}-3}{x}+2 x \log x\right\rceil
- **Should be:**
  > \left[\frac{x^{2}-3}{x}+2 x \log x\right]
