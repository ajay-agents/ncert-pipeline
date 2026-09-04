Stage 7 — apply component structure to the markdown.

Turn `chapters/$ARGUMENTS/06_simplify/chapter.simplified.<lang>.md` into
structured markdown at `07_format/structured.<lang>.md` — read per language
directly, no merge needed, since this stage works one language at a time.

Before starting: check `manifest.unchanged_since(chapters/$ARGUMENTS/, "format",
*the chapter.simplified.<lang>.md files present)`. If true, stop and report.

`render.render()` already emits the outer containers. This stage adds the
*inner* structure the model has to judge, following `step_7/format.md`:

- split multi-step solutions into `:::step{n="..."}` blocks
- wrap standalone derivations in `:::formula{label="..."}`
- wrap tables in `:::table`
- attach `:::note{type="tip|caution|recall" label="..."}` where the textbook has a remark
- wrap definitions/principles the source sets apart in `:::concept{label="..."}`
- link figures to the point in the solution where they are referenced

`label` is a short, freeform caption (see `step_7/format.md`) — not a fixed
set of words, and optional.

Rules: use only the vocabulary in `_shared/RULES.md`, never change wording while
adding structure, never add a note whose content is not in the source.

Gate: `tag._parse` on each output must succeed, and `protect.parity` between the
stage 6 text and the stage 7 text must show no drift.

Append a `manifest.py` entry: stage `"format"`, inputs the
chapter.simplified.<lang>.md hash(es), counts = output sizes per language,
gate_results from both checks above, model_calls = number of languages/batches.
