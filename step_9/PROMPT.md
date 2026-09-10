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

**A trap in `.s23` (the label cell holding a pill plus, for given/key-
formula, a decorative arrow doodle after it)**: `.s23`'s own base rule is
just `text-align:center` — the pill span and the doodle SVG that follows
it are left as plain inline content. When the pill text is short enough
that it and an ~86px-tall doodle both fit on one shared line, ordinary
inline baseline alignment puts the doodle's bottom edge on the text
baseline and lets the (much taller) doodle extend *upward* above that
line — which pushes the pill down to the *bottom* of the combined line
instead of level with the first line of its paired content, and the
doodle ends up rendering above the pill rather than trailing below it as
intended. Caught for real: the "जानकारी" label rendering visibly below
where its content starts, with the arrow floating in the gap above it.
Give `.s23` `display:flex; flex-direction:column; align-items:center;`
(plus a small `gap`) so the pill always renders first/top regardless of
the doodle's height, with the doodle trailing below it — harmless when
there's no doodle, since a lone pill is then just a one-item column.

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
`a \cdot b`, and just as much a plain `/` typed directly in source rather
than a proper `\frac` — e.g. `(250 / 18) \times 6.02 \times 10^{23}`,
caught for real on this chapter) must stay on one line too — a bare space
around `×`/`·`/`÷`/`/` lets the browser wrap right after the operator,
splitting a value from its power of ten (or a numerator from its
denominator) in a way that reads like a typo, not a line break. Wrap
the spaces immediately around these operators in non-breaking spaces as
well. Do this as a general pass over the final converted text (so it
also catches a `~` and an operator landing next to each other from
different source tokens), not just inside the LaTeX converter itself —
and watch for a run of an ordinary space next to a non-breaking one (e.g.
a literal source space beside a `~`-derived one); collapse that run to a
single non-breaking space rather than leaving a visibly doubled gap.

`=` gets the same non-breaking padding, for a related but distinct
reason: LaTeX source very often has *no* space at all on either side of
it (`\phi=\frac{...}{...}`), which reads visually cramped once converted,
especially right before a stacked fraction that's already its own
distinct visual block. Always emit a non-breaking space on both sides of
a literal `=` regardless of whether the source had one there or not (the
same run-collapsing rule above keeps this from doubling up when the
source already had a plain space next to it) — this both fixes the
cramped spacing and, as a side effect, keeps `=` from ever starting a
line break right before the value it equals.

**A literal `/` typed directly in source (rather than `\frac{}{}`) should
render the same way `\frac` does — as a proper stacked fraction, not a
bare slash — and this chapter's source writes divisions this way
constantly** (`8.987 \times 10^{9} \mathrm{Nm}^{2} / \mathrm{C}^{2}`,
`(250 / 18)`, a value divided by a value in almost every worked solution).
Rewrite a bare `/` into `\frac{numerator}{denominator}` syntax before the
main conversion, so the existing `\frac` handling renders it — this is
far more reliable than trying to draw a second stacked-fraction
implementation from scratch. Finding the numerator/denominator boundaries
correctly is the hard part, and every case below was a real bug caught on
this chapter, not a hypothetical:

- A paren that wraps *exactly* one clean division and nothing else, e.g.
  `(250 / 18)`, becomes the fraction directly (drop the now-redundant
  parens — the fraction bar already shows the grouping). A `/` anywhere
  else counts as "top level" only outside all parens/braces — track
  bracket depth over the whole string first, and only split at depth 0.
- Within one factor, the numerator/denominator each extend back/forward
  to the nearest depth-0 `=`, `\times`/`×`, or start/end of string — so
  `A / B \times C / D` becomes two separate fractions around the
  `\times`, not one fraction swallowing the whole expression.
- **A `\times` that's gluing a coefficient to its own power of ten
  (`2.3 \times 10^{-8}`) must never count as one of those boundaries** —
  otherwise the numerator/denominator search stops right there and
  swallows only the exponent, leaving the coefficient behind (caught for
  real: `2.3 \times 10^{-8} \mathrm{~N} / 9.11 \times 10^{-31}
  \mathrm{~kg}` came out as `10⁻⁸ N` over `9.11`, dropping both
  coefficients). Detect this specifically — a `\times`/`×` immediately
  followed by `10^` — and skip it as a boundary candidate; it's still
  converted normally afterward, just not treated as a factor separator.
- **`\text{...}` (marking prose inside a math span, e.g. a trailing
  "है।" or "है") must also be a hard boundary**, or a denominator search
  running past the end of the actual math content swallows the prose
  whole into the fraction (caught for real: a `/` before `\mathrm{s}^{2}
  \text { है। }` produced a denominator of `s² है।` instead of stopping
  at `s²`). Note LaTeX allows a space between `\text` and its brace
  (`\text { ... }`) — match that too, not just the no-space form.
- **A `/` inside a superscript exponent (`x^{1 / 2}`, a fractional power)
  must stay a compact superscript, never get promoted to a full two-row
  stacked fraction crammed inside a `<sup>` tag** — this looks broken,
  not readable. The superscript handler's fallback path must bypass the
  division-rewrite entirely for its own content (call the inner converter
  directly, not the public entry point that always rewrites divisions
  first) — this is not a boundary/depth issue like the others; it's that
  the exponent's braces already got stripped away by the time that
  content is a standalone string, so depth-tracking alone can't tell it
  apart from ordinary running text anymore.

**A `=` immediately followed by a `\frac`/`\sqrt` needs more than the
non-breaking padding above — a non-breaking space does not stop the
browser breaking the line right at the boundary between plain text and
an *adjacent inline-block-like element* (a fraction's `.s31` span, a
sqrt's `.s90` span) the way it does between two ordinary characters.**
Caught for real: `a = <fraction1> = <fraction2>` still split with `=
<fraction2>` alone on the next line even after `=` had non-breaking
spaces on both sides — because nothing was stopping the line from
wrapping *before* that `=`, only at the space characters immediately
touching it. When `=` is directly followed by a `\frac{}{}` or
`\sqrt{...}`, render that construct right there and glue the `=` to it
inside one more `.s90` span, the same device already used for a bare
radical sign's own parentheses. **And don't stop at one `=` — chain
through every further `= <frac/sqrt>` that immediately follows into the
*same* span** (`a = X = Y = Z` is one glued unit, not three). Gluing only
the first `=` still leaves the later ones free to wrap away from each
other, which looks exactly as broken as the original problem: one part
of a single computed result stranded above, the rest below, an uneven
split rather than the whole equation moving to a fresh line together.

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
The same reasoning applies to `.s14` (the item's badge + topic-text +
doodle column): it's compact (~150-200px) regardless of how long the
item's own content is, so unlike the item card as a whole (`.s13` —
genuinely too tall to force onto one page for a long multi-part item,
so leave that one alone) there's no good reason for it to ever split.
Caught for real: an item's topic text wrapping to two lines with the
page break landing between them, stranding the second line and the
item's doodle alone at the top of the next page while the badge number
stayed behind on the page before. Give `.s14` `break-inside: avoid` too.

**A multi-part item's own combined prompt is sometimes nothing but one
part's own question again**, occasionally with a leading `"(a)"`/`"(i)"`-
style marker that part's own field doesn't itself carry (so a naive exact
match misses it — strip a leading `(x)` marker before comparing) — rather
than genuinely shared setup text distinct from every part. Rendering it
then is pure word-for-word repetition of the very next paragraph, not
missing content (every part's own text is shown under its own भाग heading
either way, so nothing is lost by leaving it out). This is a genuine data
gap upstream (the item-level field should have held real shared context,
or the full original combined question, and doesn't) — but it isn't
stage 9's job to invent what it should have said, only to not needlessly
repeat what's already there twice. Skip the item-level prompt only when
it duplicates a part's own prompt this way; keep it whenever it's
genuinely distinct (shared setup not repeated in any part, e.g. a general
principle statement before each part asks something different about it) —
check every multi-part item against this, don't assume it applies to none
of them just because a couple of items look fine.

**A related but distinct shape: the item-level prompt can telescope BOTH
(or all) parts' asks into one combined enumeration sentence** —
`"...(a) X, तथा (b) Y परिकलित कीजिए।"` — sharing one trailing verb across
every clause, so only the LAST clause reads as a complete sentence on its
own; the earlier ones are bare noun/verb phrases. This is near-total
repetition of the individual भाग headings that immediately follow (each
of which reconstructs the full sentence for its own clause), but it will
never trip the exact-equality check above, since the enumeration matches
NEITHER part alone — it's the concatenation of both. Detect this
separately: find each `(label)` marker in the item prompt, take the text
between consecutive markers (or between the last marker and the
sentence's closing punctuation) as that clause, and confirm — for every
single labelled clause found — that it's a substring of that
same-labelled part's own prompt. Only strip the whole enumerated span
from the *displayed* item prompt (never the underlying data — this is a
display-only trim, the immutable question-text rule still applies in
full) when every clause passes; if even one clause can't be confirmed
this way, leave the entire item prompt untouched rather than risk
cutting real, non-redundant content on a guess. Some items turn out to
have an item-level prompt that is *purely* this enumeration with no other
shared context at all — after stripping, nothing is left to show, which
is correct: skip the item-level line entirely rather than render an empty
one, exactly as the plain-duplicate case above already does.

**A block of solution text written as one flowing paragraph — no explicit line break, only sentence-ending punctuation between its sentences — renders as one dense run-on paragraph, not one line per sentence**, even though the house style (every well-structured item on the exemplar page) is one short line per sentence. The line-splitting function's own job is to split text into one-line-per-sentence output, but if it only ever splits on a literal newline character and never on sentence-ending punctuation, a block that happens to have been written (by an earlier stage, or by the source itself) as continuous prose with no inline breaks stays exactly that — continuous prose — no matter how clean the rest of the page looks. Caught for real on an example whose worked solution was two paragraphs of 3-4 sentences each, with a blank line between the two paragraphs but nothing at all separating the sentences within either one; every other item on the same page, whose own text happened to already contain line breaks between sentences, looked fine, so this was easy to miss without specifically comparing a "does this look wrong" item against a "does this look right" one side by side. Fix at the line-splitting step, not by hand-editing the affected item's source text: split on a language's own unambiguous sentence-ending punctuation (a Devanagari purna viram `।` is never used for anything else; an ASCII `.` needs a guard against splitting a decimal point, e.g. don't split when the character immediately before it is a digit) wherever it falls outside an inline math span, in addition to any existing newline-based split. Re-verify page count is unchanged after this fix (a sentence-splitting change that suddenly reflows content across many more pages than before would indicate something over-split, e.g. a decimal point inside a formula wrongly treated as a sentence boundary).

**A "simple parenthesized division" shortcut regex (`(a/b)` → a stacked fraction) that matches bare `(`/`)` characters has no idea `\left(`/`\right)` is a different, matched pair of delimiters, and can silently steal one half of it.** LaTeX often writes the *same* shape — a value divided by a value, wrapped in parens — with auto-sizing `\left(`/`\right)` delimiters instead of bare ones, especially when several such factors sit side by side (e.g. `(q/2)\left(q^{\prime}/2\right)`, two halved charges multiplied together). A bare-paren regex scanning for "opening paren, division, closing paren" can match starting at the `(` that's actually part of `\left(` (stealing it and leaving the bare text `\left` orphaned immediately before, with nothing to consume it) and matching through to the `)` that's actually part of an unrelated `\right)` elsewhere (swallowing the literal text `\right` into what should have been a clean captured value) — producing visibly garbled/truncated output (a real case: a second factor's value collapsed into a single stray character plus leftover delimiter text). Fix by treating `\left(...\right)` as its own complete unit, matched and converted *first*, before the bare-paren shortcut runs on whatever's left — and have the bare-paren pass explicitly refuse any match that would start right after a `\left` token or whose span contains a `\right`, so a case the first pass doesn't catch fails safe (left as plain text) rather than corrupting output. Once fixed, confirm every such factor in a multi-factor expression renders with the *same* visual treatment (all stacked fractions, or all plain inline) — a fix that resolves the corruption but leaves one factor styled differently from its sibling (one small stacked fraction next to one plain-text fraction of the exact same shape) is still visibly inconsistent and worth completing to match, since the two factors are doing the same job in the same expression.

**A unit expression (`m/s²`, `N/C`, `Nm²/C²`) must never render as the same two-row stacked fraction a genuine value division gets** — visually they carry the same weight on the page, but a unit is meant to read as compact inline text trailing the number, not as its own oversized box. This is the same root cause as the fractional-exponent trap already documented above (a division-rewrite pass re-run on content whose protecting braces are already gone once it's pulled out as a standalone string) — it shows up wherever LaTeX marks a unit as upright/roman text (`\mathrm{...}`, `\text{...}`, `\mbox{...}`, `\operatorname{...}`): (1) a unit written as *one* such block containing its own `/` (e.g. `\mathrm{~m/s^2}`) gets `_rewrite_divisions` re-applied fresh to that isolated content once extracted, turning `m/s²` into a stacked fraction; (2) a unit split across *two* such blocks joined by a literal `/` at the top level (e.g. `\mathrm{~m} / \mathrm{s}^{2}`, or Coulomb's-constant-style `\mathrm{Nm}^{2} / \mathrm{C}^{2}` where the first unit itself carries an exponent) is a genuine depth-0 slash that the division-rewrite boundary logic has no way to tell apart from an actual value division. Fix both: make the `\mathrm`/`\text`/`\mbox`/`\operatorname` handler call the *inner* converter directly (bypassing the division-rewrite) for its own content, the same bypass the exponent handler already uses; and add a structural check — does the token immediately before a candidate `/` end a `\mathrm{...}` group (walking back past any chained exponent/subscript first), and does a `\mathrm{` token start immediately after it? — that excludes such a slash from the fraction-rewrite candidates entirely, leaving it as a plain inline `/`. Verify no regression on genuine value divisions (a bare `250/18`, a fraction whose two sides are numeric expressions like `N/kg`) — those must still become stacked fractions exactly as before; only a slash structurally sitting between two unit-marking wrappers should be spared.

**A hand-rolled LaTeX-to-HTML converter built against one chapter's own content will only handle the notation that chapter happened to use — a different subject can silently expose gaps that look like content bugs but are really missing symbol support.** Caught for real: a converter built and fully debugged against a Physics chapter (arithmetic-heavy: `\times`, Greek letters, `°`, `±`) had no handling at all for set-theory/relations/logic notation once reused for a Maths chapter on Relations and Functions — `\in`, `\notin`, `\Rightarrow`, `\rightarrow`, `\subset`, `\cup`, `\cap`, `\forall`, `\neq`, `\leq`, `\geq` all fell through to literal leftover command-name text ("in", "Rightarrow", etc.) instead of their Unicode symbols, on nearly every line of nearly every item — invisible to a numeric-only read-back check (which only verifies digits), since this kind of chapter is mostly symbolic, not numeric. Separately, a bare `\{...\}` (set-builder braces not wrapped in `\left\{`/`\right.`) was silently dropped entirely — the existing code only special-cased the `\left\{`/`\right.` form, and an un-decorated backslash-brace fell through the same "unrecognized command → single space" path that ate the digits, then the bare `{`/`}` that followed got silently consumed by the ordinary "this is just LaTeX grouping syntax" brace-skip rule. Before treating any new chapter's converter as ready, actually exercise it against a full read-back pass (below) rather than trusting that a `\command` producing *some* output means it produced the *right* output — an unhandled command silently degrading to its own bare name is easy to miss by skimming, especially in a language the reviewer may not read fluently themselves.

A related trap: `\begin{cases}...\end{cases}` / `\begin{array}...\end{array}` (a piecewise function definition, e.g. `f(x)=\begin{cases}x+1, & x>0\\...\end{cases}`) appearing **inline** (single `$...$`, not only inside a `$$...$$` display block) needs its own handling in the main character-by-character converter loop, not just in whatever helper only fires for display-math blocks — this construct is common enough in a Maths chapter's piecewise-function questions that it needs to render as a genuinely readable stacked list of rows (one row per line, sharing one radical-sign-style glued unit), not the block-only helper's blind spot. Render each row through the normal converter recursively (so a `\frac`/subscript/etc inside a case still works), and consume any mandatory column-spec group right after `\begin{array}` (e.g. the `{cc}` in `\begin{array}{cc}`) — not meaningful once rendered as stacked rows, but must still be parsed and discarded or it leaks into the first row's text.

Also watch a solution whose blocks never reach the `conclusion` stage — a short solution can legitimately end at `key_formula` or `substitute` with the actual numeric result stated only in the item's own separate `answer` field, never restated as its own concluding sentence. If the boxed-answer-echo logic only ever fires for a block tagged `conclusion`, an item shaped this way loses its answer box entirely — nothing wrong is visible on the page, the answer simply never appears anywhere. Fall back to attaching the boxed answer to the solution's last real stage group whenever no block is tagged `conclusion`, so a genuine answer is never silently dropped just because the solution happened to be short.

One more: `\circ` is genuinely ambiguous in real LaTeX — a degree sign (`30^\circ`) in a Physics chapter, function composition (`g\circ f`) in a Maths chapter on relations/functions. A converter that maps it to one meaning will misrender the other subject's use of it. Before assuming this is fine to leave as-is for a new chapter, actually check whether `\circ` appears anywhere in that chapter's own used content (not just the raw source, which may include discarded/orphaned exercise sections that never make it into the final item set) — only truly disambiguate (e.g. by what precedes/follows it) if a single chapter genuinely needs both meanings at once; don't add that complexity speculatively.

**The LaTeX→HTML converter's macro table is chapter-content-dependent, not
complete just because it works on the first chapter or two.** A Physics
chapter's own test content never exercises set-theory/relations/logic
notation at all, so a converter built and debugged only against it can
have zero handling for `\in`, `\notin`, `\leq`, `\geq`, `\neq`,
`\Rightarrow`, `\rightarrow`, `\subset`, `\cup`, `\cap`, `\forall`,
`\exists`, `\wedge`, `\vee`, `\emptyset` — an unknown bare-letter command
falls through to printing its literal name as text ("in", "notin",
"Rightarrow"), silently, with no error. Caught for real: a Maths chapter
on relations and functions hit this hundreds of times across the chapter
(`\in` alone 334 times) — invisible to the numeric-only read-back script,
since none of these are digits. The general lesson: before trusting a
reused converter on a new chapter, grep the chapter's own
`06_simplify/chapter.simplified.<lang>.md` for every `\[a-zA-Z]+` command
actually used and diff that list against the converter's own macro table,
rather than assuming coverage transfers between subjects.

This isn't only a cross-subject risk — it recurred **within Physics
itself**: a second Physics chapter (electrostatic potential and
capacitance) used `\oint` (closed-surface-integral sign, Gauss's law) and
`\sum` (summation, a hexagon-of-charges potential formula) that the first
Physics chapter's own content never happened to need, and both fell
through to literal "oint"/"sum" text the same way the Maths chapter's
set-theory gap did. Run the same grep-and-diff check even between two
chapters of the *same* subject — "it's Physics again" is not the same
guarantee as "this specific chapter's own notation is covered."

**A bare `\{`/`\}` (a set-builder brace not part of a `\left\{...\right.`
pair) needs the same literal-brace treatment in TWO separate code paths,
not one.** Fixing it only inside the LaTeX-math converter (so `$\{(a,b):
...\}$` renders correctly) misses a real, recurring case: Mathpix
sometimes fragments one set-builder expression into several separate
`$...$` spans around an embedded Hindi word (a math-boundary
mis-segmentation), stranding one side's escaped brace in the surrounding
PLAIN PROSE text, outside any `$...$` span entirely. Prose text is
html-escaped directly, never passed through the math converter — so the
literal backslash-brace shows up verbatim on the page unless the same
substitution is also applied to the prose-handling code path. Caught for
real: 7 occurrences chapter-wide, all in one chapter, none caught by a
read-back that only checked text *inside* `$...$` spans.

**A `\begin{array}`/`\begin{cases}` piecewise-function definition can
appear INLINE (single `$...$`), not just inside a `$$...$$` display
block** — e.g. `f(x)=\left\{\begin{array}{l}x+1,...\\x-1,...\end{array}
\right.$` written as one inline expression. A converter whose only
`\begin`/`\end` handling lives in the display-block preprocessing helper
never sees this at all, and it falls through to the general char-by-char
loop with no special handling, producing unreadable run-on text
("begin", "array", "l", "end" as literal words, rows glued together with
no line break). Handle `\begin{env}` as its own command inside the main
converter loop (reading the environment name, consuming an optional
`{colspec}` for `array`, finding the matching `\end{env}`, splitting the
body on `\\`), not only in the display-block helper — this covers both
the inline and display cases in one place.

**`\begin{aligned}`/`\begin{array}` are not the only multi-row display
environment LaTeX source uses — `\begin{gathered}` (a stack of centered
equations with no alignment column) needs the exact same row-splitting
treatment, and a converter whose display-block helper only special-cases
`aligned`/`array` by name will silently mishandle it.** Caught for real:
a chapter's own drift-velocity derivation used `\begin{gathered}...
\end{gathered}` inside a `$$...$$` block for the first time (physics-
12-1/12-2 only ever used `aligned`/`array`) — the display-block helper's
row-splitting regex didn't match the name `gathered`, so it fell through
to a generic fallback that still produces correctly-separated `<span>`
elements per row (via the main-loop's own generic `\begin{env}` handler,
built for the inline case), but those span classes had never been given
CSS rules (nothing needed them before this chapter), so the rows
rendered with **no line break between them at all** — two stacked
equations ran together onto one visual line. Two independent fixes, do
both: (1) extend the display-block helper's row-splitting regex to
treat `gathered` identically to `aligned`/`array` (same proven path,
rather than trusting the untested fallback), and (2) give the generic
`\begin{env}` handler's own wrapper/row classes real CSS (a flex-column
container for the whole block, `display:block` for each row) as a
backstop for any *inline* `$...$` occurrence of `\begin{cases}`/
`\begin{gathered}` that never reaches the display-block helper at all.
Don't assume "the environment name I've seen before is the only one a
new chapter will use" — grep the chapter's own content for every
`\begin{...}` name actually present, the same discipline already
established for bare LaTeX commands.

**A part label already wrapped in parens from stage 7 (`label="(i)"`)
must not be wrapped again when rendering "भाग (label)".** An earlier
exemplar chapter's part labels were bare letters (`label="a"`), so
`भाग ({label})` was correct there — a different chapter whose stage 7
already emits `(i)`, `(ii)` produces a visible "भाग ((i))" double-paren
bug if the template blindly wraps every label. Check whether the label
already starts with `(` before adding another pair, rather than assuming
one convention across every chapter.

**A solution shaped as several independent, parallel case analyses (e.g.
5 sub-cases (a)–(e), each proving or disproving a property for a
different concrete relation) does not fit the fixed given → key-formula →
substitute → conclusion sequence well.** Stage 8's position-based
inference (first block = given, last = conclusion, everything between =
substitute) merges ALL the middle cases into one anonymous "मान रखो" pill
with no visible boundary between them — a reader can tell where the
first and last case are, but not where case (b) ends and (c) begins.
This is not a text bug (nothing is dropped, wrong, or mislabeled) and
current house style has no better place to put it — flagging it here as
a known limitation of the four-stage model for this specific content
shape, worth a real design solution in a future session (e.g. a fifth,
freeform "case" stage), not something to silently reshape at stage 9
without a decision from the user.

**A figure referenced mid-solution (not just an item-level `:::figure`
before any part) can be silently dropped by the render script itself, not
just by stage 8's serialization.** Stage 8's JSON schema correctly nests a
figure inside whichever block's `flow` it belongs to (already documented
above), but a render script that builds each block's text via a
`flow_text_join()`-style helper which explicitly skips `type: "figure"`
segments (reasonable for a prompt/answer flow, where a nested figure would
be unusual) will keep doing that when the SAME helper is reused for a
solution block's own flow — silently omitting the figure from the page
with nothing else indicating anything is missing. Caught for real:
physics-12-2's ex_2.2 has "चित्र 2.7 देखिए" referenced mid-sentence inside
its own `:::concept`, not as an item-level figure before the parts — the
figure vanished from the first render entirely. physics-12-1 never
exercised this path (no item in its own JSON has a figure nested inside a
solution flow), so the gap was latent, not previously caught. Fix: give
solution/note rendering its own flow-walker that renders a `type:
"figure"` segment as a proper figure element in its correct position
(same markup as the item-level figure row), and keep the simpler
text-only join for prompt/answer flows where it's still correct. The
figure-src-count check already mandated below (JSON's distinct count vs.
what actually resolves in the rendered HTML) is exactly what catches
this — treat a mismatch there as a render-script bug to fix, not just a
JSON bug, before assuming stage 8 is at fault.

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
