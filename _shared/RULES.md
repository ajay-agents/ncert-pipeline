# NCERT Solutions Pipeline — cross-cutting rules

Read this before any step. It applies across all ten stages; each
`step_N/PROMPT.md` adds only what's specific to that stage.

## The five rules

1. **The chapter markdown is the source of truth.** `chapter.<lang>.md` /
   `chapter.verified.<lang>.md` / `chapter.simplified.<lang>.md` (stages
   3/5/6) are container markdown — the same `:::example{...}`/`:::prompt`/
   `:::solution` vocabulary stages 4/7/8 already rendered in, now used as
   the on-disk format everywhere, not just the later stages.
   `07_format/structured.<lang>.md` and `08_tag/final.<lang>.html` are
   still downstream rendered artefacts. Never hand-edit any of these files
   to fix content — fix the data via `pipeline/mdio.py`'s
   `markdown_to_chapter()`/the stage's own logic, then re-render with
   `pipeline/render.py`'s `render()`.
2. **Deterministic work runs in Python.** Number matching, joining, rendering
   and all gates (stages 1–8, 10) are code in `pipeline/`. Do not do them by
   reading and retyping. If a helper is missing, write the helper. Stage 9 is
   the one exception — see `step_9/PROMPT.md`'s "Final design". (Stage 8's
   own judgement call — assigning each solution's given/key-formula/
   substitute/conclusion structure — is model work, same as stage 7's
   structural judgement; only its JSON serialization is code. Stage 10's
   export and its checks are code too, not judgement — see `step_10/PROMPT.md`.)
3. **Gates are hard stops.** If a gate fails, fix the data or report the problem
   to the user. Do not relax a threshold, skip a gate, or edit `gates.py` to pass.
   (Stage 9's hand-designed path has no code gate on the final HTML; its
   correctness check is the manual read-back in `step_9/PROMPT.md` — treat that
   as no less mandatory for being manual. Stage 10, one step later, exports a
   *fixed* artefact whose content is mechanically checkable again — it gets a
   real gate, not just a note; see `step_10/PROMPT.md`.)
4. **NCERT exercise question text is immutable.** It may be corrected against the
   textbook (stage 5) but never reworded, shortened or simplified (stage 6).
   Example *solutions* may be simplified; example *questions* may not.
5. **Nothing is invented.** If a solution is missing from the solutions PDF,
   leave it empty and list it in the stage report. Never write an answer from
   your own knowledge of the physics.

## Bilingual handling

NCERT publishes official Hindi editions. **Always extract from both PDFs and
align by question number** (`match.align_languages`). Do not machine-translate
when an official Hindi source exists — translate only the gaps, and mark
translated fields in the stage report so they can be reviewed.

Hindi text follows the house style already in use: Devanagari for English
technical terms, no hyphens, simple sentence structure.

## Subject notes

- **Physics / Maths** — dense inline math; the protection layer matters most here.
- **Chemistry** — reactions may arrive as `\ce{}` or as images; both are protected.
- **Biology** — figure-heavy and low on math; caption accuracy is the main risk.

## Container vocabulary (stages 7–9)

`example` `question` `part` `prompt` `solution` `step` `answer` `formula`
`table` `note` `figure` `concept` `lang`

Opened with `:::name{attr="value"}`, closed with a bare `:::`. No other
component names — `tag.py` fails the build on an unknown one.

`formula`, `note`, `concept` and `step` may carry a `label="..."` attribute
— a short caption naming what that specific block is.

For a **standalone** definition, named note or principle (not part of one
worked solution's own flow — e.g. a `concept` explaining what "Molarity"
means), this is freeform: write whatever short noun phrase actually fits
("Molarity", "Classification"), or omit it.

For the blocks that make up **one worked solution's own step-by-step
structure**, prefer this fixed 4-stage pattern instead of a freeform
caption, in the chapter's own language — it's the house style stage 9
renders as four consistently-colored pills, and a freeform caption here
(a specific law's name, an English word in a Hindi chapter) has repeatedly
had to be collapsed back to these four downstream. Label what you can with
it directly here at stage 7; stage 8 infers the same fixed stage by
position for any `:::step` you leave unlabelled, so nothing downstream
depends on every single step being labelled by hand:

| stage | container | label (Hindi) | label (English) |
|---|---|---|---|
| what's known | `:::concept` | `"जानकारी"` | `"Given"` |
| the governing equation | `:::formula` | `"मुख्य सूत्र"` | `"Key formula"` |
| substituting/calculating | `:::step` | `"मान रखो"` | `"Substitute"` |
| the concluding line | `:::step` | `"निष्कर्ष"` | `"Conclusion"` |

Not every solution has all four (a two-line solution may only need
substitute+conclusion); never force a stage that isn't genuinely there.
This is a labelling convention, not a new schema requirement — a `:::step`
with no `label` is still valid and common.

## Item topics

`schema.Item.topic` is a short (2–6 word) descriptive title per item, e.g.
"Mole fraction". Unlike `question`, it is not transcribed from the textbook —
it's written once at extraction (stage 2) as a categorising label for the
stage 9 badge. It is never checked against the source PDF (stage 5 has no
field to verify it against) and is not simplified (stage 6); it does not
fall under Rule 4's immutability, since it isn't exam question text. Rule 5
(nothing invented) still applies to what it *claims* about the item, even
though the label itself doesn't exist in the textbook.

## Sub-agent dispatch scope

When a stage's work is split across several dispatched sub-agents (batches
of items, parallel languages), **never point a sub-agent at its own
`step_N/PROMPT.md`.** That file is written second-person for whoever is
running the *whole* stage; a sub-agent handed only a narrow slice (a
specific batch of items, writing to its own scratch file) that reads it
anyway will reliably misread it as personal instructions and re-run the
entire stage itself — including gates and the manifest append — racing
every other batch to overwrite the shared output file. This happened three
times in one stage in this pipeline's own history before the fix: give a
sub-agent only the narrower content-judgment file (e.g. `step_6/simplify.md`,
never `step_6/PROMPT.md`), state its exact scope explicitly ("simplify only
these N items; write only to `<scratch path>`; do not touch any file under
`chapters/`; do not run gates or append to the manifest — the coordinator
does that after merging every batch"), and verify each batch's actual
output file against its assigned keys before merging — don't trust a
batch's self-reported completion.

## Model-call discipline

- Stages 2, 5, 6, 7, 8 call the model. Stages 1, 3, 4, 10 do not.
- Stage 8's model work is the given/key-formula/substitute/conclusion
  judgement call (where stage 7 left a step unlabelled); writing the
  resulting JSON is code, not a model call.
- Stage 9 is hand-designed only, almost entirely model judgement — there
  is no fixed-code fallback (removed along with `css/`; see CLAUDE.md).
- Stage 10 is a mechanical export pass (a real browser engine rendering
  stage 9's finished HTML to a fixed PDF) plus code-checked gates — no
  model judgement at all; see `step_10/PROMPT.md`.
- Chunk by section heading, never by token count, so no question is split.
- Cache the system prompt and JSON schema across chunks.
- Stage 5 returns a **correction list**, not rewritten prose.
- Stage 6 operates on text that has been through `protect.freeze()`.
