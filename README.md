# NCERT Solutions Pipeline

Bilingual NCERT solutions builder for Physics, Chemistry, Maths and Biology
(Classes 11–12), run as nine Claude Code stages over one chapter at a time.

```
ncert-pipeline/
  README.md                 ← this file
  CLAUDE.md                 ← auto-loaded rules; imports _shared/RULES.md
  _shared/RULES.md          ← the five rules + bilingual/subject/vocabulary notes
  CALIBRATION/calibrate.py  ← measures a chapter; writes <chapter>.md
  CALIBRATION/<chapter>.md  ← every measured number (generated, never typed)
  step_1 … step_9/PROMPT.md ← the stage instructions (orchestration: files, gates, manifest)
  step_2/extract.md, step_5/verify.md, step_6/simplify.md, step_7/format.md
                            ← the content-judgment instructions those four stages send the model
  .claude/commands/stageN-*.md ← thin wrappers so /stage1-mathpix etc. still work
  pipeline/                 ← the deterministic code every stage calls
  pipeline/mdio.py          ← markdown <-> Chapter/Item/Correction (the on-disk format)
  solutions-chapter-1.html/.css ← the house style base + exemplar every chapter's stage 9 matches
  chapters/<subject>-<class>-<chapter>/  ← one run's outputs (see CLAUDE.md)
```

**Prompts live in `step_N/`; outputs do not.** A run writes to
`chapters/<subject>-<class>-<chapter>/`.

## Setup

```bash
pip install -r requirements.txt
export MATHPIX_APP_ID=... MATHPIX_APP_KEY=...
python smoke_test.py          # verifies the deterministic stages
```

## Running a chapter

```bash
mkdir -p chapters/physics-11-10/00_raw
# drop in chapter.en.pdf chapter.hi.pdf solutions.en.pdf solutions.hi.pdf
```

Then, one session per stage:

```
/stage1-mathpix  physics-11-10
/stage2-extract  physics-11-10   (extract + match, one session)
/stage3-split    physics-11-10
/stage4-combine  physics-11-10
/stage5-verify   physics-11-10
/stage6-simplify physics-11-10
/stage7-format   physics-11-10
/stage8-tag      physics-11-10
/stage9-design   physics-11-10
```

**Re-run `CALIBRATION/calibrate.py` after any stage whose output changed** —
it measures the chapter (item/part/figure counts, bilingual coverage, empty
fields, gate history) and writes `CALIBRATION/<chapter>.md`:

```bash
python3 CALIBRATION/calibrate.py chapters/physics-11-10
```

## The chain

| stage | reads | writes | one-line job |
|---|---|---|---|
| **1** | `00_raw/*.pdf` | `01_mathpix/*.mmd` | convert both chapter and solutions PDFs (each language) via Mathpix |
| **2** | `01_mathpix/*.mmd` | `02_extract/chapter.<lang>.md`, `match_report.md` | extract examples/exercises/solutions, join solutions to questions, align English and Hindi into one `Chapter` |
| **3** | 2 | `03_split/examples.<lang>.md`, `qa.<lang>.md` | split the merged chapter into examples-only and Q&A-only markdown — pure function, no model |
| **4** | 3 | `04_combined/combined.<lang>.md` | combine both split files back into one — pure function, no model |
| **5** | 4 + `00_raw/*.pdf` | `05_verify/chapter.verified.<lang>.md` | check every field against the source pages; apply high-confidence corrections |
| **6** | 5 | `06_simplify/chapter.simplified.<lang>.md` | simplify solution language for readability; questions and answers stay frozen |
| **7** | 6 | `07_format/structured.<lang>.md` | wrap the content in the container vocabulary (`:::step`, `:::formula`, …) |
| **8** | 7 | `08_tag/structured.<lang>.json` | tag each solution's given/key-formula/substitute/conclusion structure and serialize to JSON — see `step_8/PROMPT.md` |
| **9** | 8 | `09_design/final.<lang>.html` | the hand-designed final page — see `step_9/PROMPT.md` |

Each stage's full instructions are in `step_N/PROMPT.md`; `_shared/RULES.md`
covers what's common to all of them.

## Which stages call the model

| Stage | Model | Why |
|---|---|---|
| 1 Mathpix | no | API call plus counts |
| 2 Extract + match | yes | reading unstructured markdown; only the join misses need model judgement |
| 3 Split | no | pure render from the merged chapter markdown |
| 4 Combine | no | pure render from the two split files |
| 5 Verify | yes | needs the PDF pages as evidence |
| 6 Simplify | yes | the actual rewriting |
| 7 Format | yes | judgement about structure |
| 8 Tag | yes (judgement) + code (serialization) | assigning the given/key-formula/substitute/conclusion structure is judgement; writing the JSON is deterministic |
| 9 Design | yes | hand-designed, matching house style — no fixed-code fallback |

Stage 9 is hand-designed only (see CLAUDE.md's "Tagging and final design"):
hand-authored as plain static HTML/CSS (not the `design` skill's Claude
Design canvas — its sandboxed iframe can't load MathJax and its editor
machinery isn't needed for an exact match to a fixed reference), matching
the house style in `solutions-chapter-1.html`/`.css`, optionally published
with the `Artifact` tool afterward for a shareable link — model-heavy and
gate-free, so the manual read-back in `step_9/PROMPT.md` is not optional.
Stage 8's JSON does the
heavy structural judgement ahead of time specifically so stage 9 can stay
close to mechanical templating.

## The two failure modes this guards against

**Lost questions.** Every stage carries an item count forward and `gate_counts`
compares it. A question cannot vanish silently between stages.

**Corrupted maths.** Stages 5–7 run text through `protect.freeze()`, and
`gate_math_parity` compares equation counts before and after. A simplification
pass that eats an exponent fails the stage instead of shipping.

Stage 8 has its own code gate too: it re-parses the JSON it just wrote and
confirms item/part/figure counts match a fresh count from
`structured.<lang>.md` directly — nothing gets silently dropped in the
tag-and-serialize step.

This coverage ends at stage 8. Stage 9 has no code gate on the final HTML —
`step_9/PROMPT.md`'s manual answer-by-answer read-back is what stands in for
`gate_math_parity` there, and it isn't optional just because it isn't code.

## Before your first real run

1. Run one chapter per subject end to end and read every output by hand. Physics
   and Maths stress the maths protection; Chemistry stresses reaction handling;
   Biology stresses figures and captions.
2. Only then batch.
