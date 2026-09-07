Stage 9 — design the final chapter page (hand-crafted, matching house style).

Build `chapters/$ARGUMENTS/09_design/final.<lang>.html`.

Before starting: check `manifest.unchanged_since(chapters/$ARGUMENTS/, "design",
structured_json_path)`. If true, stop and report.

There is one path — hand-designed, matching house style. There is no
fixed-code fallback; it was removed along with `css/`.

Read `08_tag/structured.<lang>.json` — every judgment call (each solution's
given/key-formula/substitute/conclusion structure, noise already stripped,
notes already labelled) is already made; this stage's job is templating
that onto the house style, not re-deciding structure.

**Hand-author the page as plain static HTML/CSS directly — do not use the
`design` skill for this stage.** That skill's output is a Claude Design
canvas: its artboards render inside a sandboxed iframe with no network
egress beyond Google Fonts, so a CDN script tag (MathJax included)
silently cannot load there, and its editor adds machinery (tweak props,
artboard layout, a live-editable component model) this stage has no use
for — the target here is an exact, fixed match to a reference file that
already exists, not an open design exploration. Writing the HTML/CSS
directly, the way `solutions-chapter-1.html`/`.css` itself was built, is
both simpler and gives byte-level control the canvas doesn't.

`09_design/final.<lang>.html` (+ its CSS) is the real deliverable — what
the checks below and the manifest gate against. Once it's finished and
verified, you may also publish it with the `Artifact` tool for a shareable
link (load the `artifact-design` skill first, as that tool requires; the
"how much design investment" calibration it asks for is minimal here,
since the visual design is already fully fixed by the exemplar, not an
open decision) — but that publish is a bonus on top of the file, never a
replacement for it.

`solutions-chapter-1.css` at the repo root is the **base stylesheet for
every chapter** — start from it, don't fork it. Add rules only for what it
genuinely doesn't cover yet (a chapter with more equations than Chemistry 12
Chapter 1 has needs hand-rendered math classes it doesn't define, for
example); never restyle something it already defines. `solutions-chapter-1.html`
is that same chapter's finished page, built this way, and is the exemplar:
the rotated number badge, rotating card accents across items, the four
consistently-colored labeled pills structuring each worked solution, the
Devanagari/STIX Two Text pairing, per-question illustrative doodles where
they genuinely help, and hand-drawn fraction display for simple one-line
ratios.

Reuse the exemplar's real classes, not lookalikes of your own:
- The per-color badge box + children, cycling teal/orange/pink/purple
  across items (`.s15`/`.s40`/`.s46`/`.s52` and their `Q`-tag/number/topic
  children); use the exemplar's own 38px number variants
  (`.s68`/`.s65`/`.s66`/`.s67`) instead of the 44px ones for an item whose
  number has a 2-digit part after the decimal, matching which variant the
  exemplar itself uses for its own longer numbers.
- `.s31`/`.s32`/`.s33` for every stacked one-line fraction — this chapter
  likely has many more ratios than the exemplar did; stack them broadly,
  same as the exemplar's own habit.
- The four fixed stage pills straight from the JSON's `stage` field —
  `.s24` given, `.s28` key_formula, `.s34` substitute, `.s35` conclusion —
  no numbered step markers anywhere; the exemplar doesn't use them, and
  the JSON already tells you which pill each block gets.
- `.s74`/`.s75` for recall/caution notes.
- `.s39`/`.s51`/`.s57`/`.s58` for item-to-item dividers, `.s10`/`.s11`/
  `.s12` + `.s69`/`.s70`/`.s71` for the two section dividers (Examples,
  then Exercises forcing a page break).
- `.s76`-`.s79` for figure rows/captions. Reference `<img src>` exactly as
  the JSON's `src` already reads (e.g. `images/fig_1_5.jpg`) — don't
  re-derive it to a bare filename; the images live in a subfolder next to
  this page, not beside it directly, and a bare filename 404s silently.

**A trap already hit once, if reusing `solutions-chapter-1.css`'s own
`.s22` class**: it is a CSS grid (`grid-template-columns:135px 1fr`) built
for the exemplar's own content, which only ever paired a label cell with a
content cell, alternating. This chapter's content will usually be richer
(numbered concepts, notes, multi-part answers) — putting that directly
inside `.s22` scatters it across the two columns at random, since grid
auto-placement has no idea some children aren't part of a pair. Add two
new classes instead: one for a safe flex-column stack (`display:flex;
flex-direction:column` — arbitrary full-width children, none of `.s22`'s
column-count assumptions) and one self-contained flex row for each actual
label+content pair (`display:flex` with the label cell fixed-width and the
content cell `flex:1`) — never `.s22` itself for this chapter's content.
**That label+content flex row must have exactly two direct children — the
label cell and one wrapper holding everything else.** A conclusion pill
has both its ordinary derivation text (in `.s26`) and, on the final
conclusion, the boxed final-answer echo (in a separate `.s36`) — if both
land as direct children of the flex row instead of being wrapped together
in one child, flexbox lays out `.s26` and `.s36` as two side-by-side
columns in the *same* row (both are naturally top-aligned), so the boxed
answer floats up next to the first line of the derivation instead of
sitting below the last one, which is very obviously wrong once the
derivation is more than one line — wrap `.s26` and `.s36` together inside
one container and size *that* to `flex:1`, not the two of them
individually.

**A second trap, in `.s37`/`.s44`/`.s50`/`.s56` (the boxed final-answer
span inside a conclusion pill)**: its border is an organic blob
(`border-radius` given as percentages, e.g. `45% 55% 50% 50% / 60% 55% 45%
50%`), which only looks right around a short, single-line value — every
boxed answer in the exemplar itself is well under this. This chapter will
often have longer, multi-clause answers (several sub-results combined
into one line, e.g. `E_A = 7.2×10⁴ N C⁻¹; E_B = 3.2×10⁴ N C⁻¹; E_C = 9×10³
N C⁻¹`); once that wraps to two lines, the same percentage radius scales
into a much bigger absolute curve and visibly cuts into the wrapped text
at the corners — this happened for real, on exactly this kind of combined
answer. Add four matching plain rounded-rectangle variants (same border
colors, a small fixed-pixel `border-radius` instead of a percentage one,
safe at any height) and switch to them once the answer's plain-text
length passes a threshold (~30 characters is a reasonable cutoff) —
keep the blob for genuinely short answers, exactly as the exemplar uses
it, and use the plain box only past that length.

**A third trap: the base CSS has no mobile breakpoint at all** — only
`@media print`. `.s1` (the page's outer wrapper) is a fixed
`width:1080px` with `zoom:0.63`, a desktop/print-page simulation; opened
on a phone, that fixed-width block gets squeezed by the browser to fit
the narrow viewport on top of the already-reduced desktop zoom, shrinking
every s-class's own literal pixel font-size far past readable. Add a
`@media (max-width: 700px)` block (in the chapter's own CSS, same as the
other additions here) that, below that width: sets `.s1` to `width:100%;
zoom:1` (every class's own font-size then displays at its literal,
un-zoomed size, which reads fine on a phone without any other change);
reflows `.s13`'s item grid (`grid-template-columns:150px 1fr`) to a single
column (`1fr`) so the badge sits above the content instead of eating a
fixed 150px next to a squeezed content column; and reflows `.s82`'s
label+content row to stack vertically the same way, so a solution's
content actually gets the phone's full width. Add `overflow-x:auto` to
`.s26`/`.s36` too, as a safety net for the rare `white-space:nowrap`
fraction or derivation line still too wide for a narrow screen even after
reflowing — it should scroll within its own line rather than overflow the
page. This does not change how the page looks on desktop at all (the
breakpoint only applies below 700px); do this for every chapter, not just
when a student happens to report it.

**A fourth trap: converting LaTeX to plain HTML text can leave ordinary,
breakable spaces where the browser must never wrap.** Two concrete cases,
both caught for real on this chapter: (1) LaTeX's `~` (e.g. `\mathrm{~N}`,
`10~cm`) means "a space here that must never become a line break" — it is
not decorative, and converting it to an ordinary space lets a number split
from its unit across a line ("10" ending one line, "cm" starting the
next). Convert `~` to an actual non-breaking space character, not a plain
one. (2) A coefficient and its multiplier/divisor (`6.02 \times 10^{23}`,
`a \cdot b`) must stay on one line too — a bare space around `×`/`·`/`÷`
lets the browser wrap right after the operator, splitting a value from
its power of ten in a way that reads like a typo, not a line break. Wrap
the spaces immediately around these operators in non-breaking spaces as
well. Do this as a general pass over the final converted text (so it
also catches a `~` and an operator landing next to each other from
different source tokens), not just inside the LaTeX converter itself —
and watch for a run of an ordinary space next to a non-breaking one (e.g.
a literal source space beside a `~`-derived one); collapse that run to a
single non-breaking space rather than leaving a visibly doubled gap.

**The same trap also has a layout-shaped version: a stacked one-line
fraction (`.s31`/`.s32`/`.s33`) is itself two rows tall (numerator over
denominator).** That's fine loose in running prose — it just sits taller
than the surrounding line — but wrapped in plain `(`/`)` characters (a
square root of a fraction, e.g. `\sqrt{\frac{2h}{a}}`, which this chapter
has more than once, including two in a single sentence) the browser can
place a line break between the `(` and the fraction, or between the
fraction and the `)`, tearing the expression visibly apart rather than
just wrapping it. Wrap the radical sign, its parentheses and their
contents in one `display:inline-flex; white-space:nowrap` span so they
always move as a unit; give that span `overflow-x:auto` (and a sane
`max-width`) as a safety net for the rare case where even the whole glued
unit doesn't fit a line — let it scroll within its own line rather than
overflow the page, the same reasoning as the mobile breakpoint's
`overflow-x:auto`, just not limited to mobile there.

**This page is routinely exported to a fixed PDF (the `@page`/A4 rules at
the top of the base CSS), not only read in a browser — the same tearing-
apart failure has a page-break-shaped version, not just a line-break-
shaped one.** A fraction or a glued `sqrt(fraction)` unit that survives
line-wrapping intact can still be split across a *page* boundary once
that page happens to end partway through it, which looks just as broken
in the exported PDF. The base CSS already protects `img`/`figure`/`svg`
this way (`break-inside: avoid`) — extend the same rule to `.s31` and
`.s90` (or whatever ends up holding a fraction/sqrt in this chapter), so
they never split across a page either. This is worth doing for every
chapter, since every chapter's page ends up exported the same way, not
only when a user happens to notice a split fraction in their PDF.

**This path has no code gate on the final HTML.** The check is manual and
not optional: before calling the chapter done, read every `final_answer`
and every `question` in `06_simplify/chapter.simplified.<lang>.md` (not
the stage-8 JSON — the simplified chapter markdown is the actual gated
source of truth for content; the JSON is a derived, regeneratable
convenience) and confirm each appears, unchanged, somewhere in the
designed page. A wrong number or a dropped question is not caught
automatically here the way stages 1–8 catch it — that's the price of
hand-design, so the read-back has to actually happen. A small script
pulling every numeric token out of each `final_answer`/`question` (via
`mdio.markdown_to_chapter` against the stage-6 file) and confirming each
appears somewhere in the rendered HTML text is worth writing — it's not a
replacement for actually reading the page, but it catches a dropped
question or a transposed digit far more reliably than eyeballing 30+ items
one time, and it's cheap to re-run after any later edit.

Export the finished page and its stylesheet into `09_design/final.<lang>.html`
+ `09_design/*.css`.

## Checks before finishing

Every figure `src` resolves — verify with `os.path.exists` against the
**actual output directory** (`09_design/`), not a scratch copy of the
images sitting somewhere convenient; a scratch copy placed next to the
HTML instead of in its own `images/` subfolder will pass a check that the
real deployed file fails, exactly as happened this session. The Hindi page
carries `lang="hi"` and the Devanagari font stack; every final answer
matches `chapter.simplified.<lang>.md` verbatim (the manual read-back
above, re-run against the file at its real path after any later edit).

Append a `manifest.py` entry: stage `"design"`, inputs the
structured.<lang>.json hash, counts = html size, model_calls = however many
the design pass took.
