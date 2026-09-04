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
