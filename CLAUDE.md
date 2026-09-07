# NCERT Solutions Pipeline — operating rules

Bilingual (English + Hindi) NCERT solutions for Physics, Chemistry, Maths and
Biology, Classes 11–12. Each chapter moves through ten stages, one stage
per session — never run two stages in one pass. The stage prompts live in
`step_1/` … `step_10/` (see README.md's chain table for what each does);
`.claude/commands/stageN-*.md` are thin wrappers over them so `/stage1-mathpix`
etc. still work.

@_shared/RULES.md

## Working directory per chapter

```
chapters/<subject>-<class>-<chapter>/
  00_raw/        chapter.en.pdf chapter.hi.pdf solutions.en.pdf solutions.hi.pdf
  01_mathpix/    *.mmd, images/
  02_extract/    extract.<lang>.md (intermediate)  chapter.en.md  chapter.hi.md  match_report.md
  03_split/      examples.<lang>.md  qa.<lang>.md
  04_combined/   combined.<lang>.md
  05_verify/     corrections.md  chapter.verified.en.md  chapter.verified.hi.md
  06_simplify/   chapter.simplified.en.md  chapter.simplified.hi.md
  07_format/     structured.<lang>.md
  08_tag/        structured.<lang>.json
  09_design/     final.<lang>.html  *.css
  10_pdf/        final.<lang>.pdf
  manifest.json
```

Every file above except `manifest.json`, the four raw PDFs,
`08_tag/structured.<lang>.json`, and `10_pdf/final.<lang>.pdf` is either
container markdown (`pipeline/mdio.py` reads it, `pipeline/render.py`
writes it) or plain markdown/HTML rendered from it. `08_tag/structured.
<lang>.json` is the **one deliberate exception** to "no JSON in a
chapter's working directory": a purpose-built, always machine-generated
handoff between stage 8's judgment (tagging each solution's given/key-
formula/substitute/conclusion structure) and stage 9's near-mechanical
HTML render — never hand-edited, always regenerated from
`07_format/structured.<lang>.md` whenever stage 8 reruns, never treated
as a second source of truth. `10_pdf/final.<lang>.pdf` is likewise never
hand-edited or a second source of truth — it is a mechanical export of
`09_design/final.<lang>.html`, regenerated whenever that HTML changes,
never the other way around. A chapter that only has one language (e.g. a
Hindi-only run) simply has only that language's file at each stage.

After every stage, append to `manifest.json`: stage name, timestamp, input
hashes, counts, gate results, model calls. A stage whose inputs are unchanged
should not be re-run.

Re-run `CALIBRATION/calibrate.py <chapter-dir>` after any stage whose output
changed — it measures the chapter (item/part/figure counts, gate history,
empty-field flags) and writes `CALIBRATION/<chapter>.md`, generated and never
hand-typed, the same way `manifest.json` is.

## Tagging (stage 8) and final design (stage 9)

Stage 8 reads `07_format/structured.<lang>.md` — already-gated content,
already structured into steps/notes/formulas/concepts by stage 7 — and
does the last piece of judgment work before rendering: assigning each
worked solution's blocks to the fixed given → key-formula → substitute →
conclusion pattern (see `_shared/RULES.md`'s container-vocabulary section),
stripping redundant textbook openers ("हल :" and the like), and
serializing the result to `08_tag/structured.<lang>.json`. This is the one
deliberate JSON file in the pipeline — see the working-directory note
above for why, and never hand-edit it; fix `structured.<lang>.md` or
stage 8's own logic, then regenerate.

Stage 9 is hand-designed only — there is no fixed-code fallback (there
used to be one, `pipeline/tag.py` + `css/`; both the fallback rendering
code and its stylesheet are gone, and `pipeline/tag.py` now holds only the
container parser `pipeline/mdio.py` depends on). It reads stage 8's JSON
(not the raw markdown — the judgment calls are already made) and hand-authors
a paginated page as plain static HTML/CSS — not via the `design` skill's
Claude Design canvas, whose sandboxed iframe can't load a CDN script
(MathJax included) and adds editor machinery this exact-match task doesn't
need. The finished file may optionally also be published with the
`Artifact` tool for a shareable link, but the file itself is the
deliverable. `solutions-chapter-1.css` at the
repo root is the base stylesheet for every chapter — start from it, don't
fork it; only add rules for things it genuinely doesn't cover yet
(hand-rendered math, decorative flourishes, whatever a given chapter needs
that Chemistry 12 Chapter 1 didn't — and see `step_9/PROMPT.md` for one
class, `.s22`, that looks reusable but isn't, for any content richer than
that exemplar chapter's own). `solutions-chapter-1.html` is that same
chapter's finished page — the exemplar every later chapter's design should
visually match. No code gate; correctness rests on the manual
answer-by-answer read-back in `step_9/PROMPT.md`.

## PDF export (stage 10)

Stage 10 is a mechanical export pass, not a design pass: it renders
`09_design/final.<lang>.html` to `10_pdf/final.<lang>.pdf` with a real
browser engine (Playwright/Chromium — confirmed available in this
environment), honoring the `@page`/`@media print` rules already in the
base CSS rather than picking its own page size. Unlike stage 9's HTML,
the PDF's actual content is mechanically checkable (page count, no blank
pages, the same numeric read-back stage 9 does but re-run against the
PDF's own extracted text) — see `step_10/PROMPT.md` for the exact gate,
including a real bug already caught there once: naively normalizing a
unicode superscript exponent back to ASCII digits can glue it onto the
preceding base number into one merged token, hiding a genuine number from
ever matching on its own.
