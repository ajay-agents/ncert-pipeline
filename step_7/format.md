# Stage 7 — structural formatting prompt

Add component structure to already-final text. You are marking up, not
writing. If you find yourself changing a word — or a digit, a symbol, or a
table cell — stop.

The markdown you receive already carries the outer containers stage 4 emitted
(`:::example`/`:::question`, `:::prompt`, `:::part`, `:::solution`, `:::answer`,
the `#### ...` heading, any `:::figure` block). **Preserve every existing
container line, attribute and heading exactly as given.** Your job is only to
insert new containers around content that's already there — never to
regenerate the outer structure.

## Vocabulary

`:::step{n="1"}` numbered stage of a worked solution
`:::formula{label="..."}` a standalone derivation or result line worth setting apart
`:::table` wrapper around a markdown table
`:::note{type="tip|caution|recall" label="..."}` a remark that is already in the source
`:::figure{src="..." id="..."}` a diagram, placed where the text refers to it
`:::concept{label="..."}` a definition or principle statement the source sets out separately

Open with `:::name{...}`, close with a bare `:::`. Containers nest. No other names.

**The opening tag, and the bare closing `:::`, must each be the ONLY thing
on their line** — no prose before or after either one on the same line
(`हल : :::concept{label="..."}` is invalid and will fail the build; put the
prose on its own line before the tag instead). This is a hard parser
requirement (`tag.py`'s `OPEN_RE` matches the whole line), not a style
preference — a dispatched batch has produced exactly this mistake before,
seventeen times in one run, because it read as a minor formatting choice
rather than a build-breaking one.

`label` is optional on `formula`/`note`/`concept`/`step` — a short (2–4
word) caption naming *what this specific block is*, **in the same language
as the surrounding chapter text** (a Hindi chapter's labels are Hindi words,
never English ones — `label="जानकारी"`, not `label="Given"`; this has
leaked English labels into Hindi chapters before, because every example in
this file happens to be in English). For a block that's part of one worked
solution's own given→formula→substitute→conclusion structure, use the
fixed 4-word vocabulary `_shared/RULES.md`'s container-vocabulary section
gives, in-language, rather than a freeform caption — this is what
downstream rendering keys its four label colors on. For a standalone
definition/note not part of that flow, a freeform caption is still right:
write whatever short noun phrase actually describes it. Add a label when it
would genuinely help a student scanning the page; skip it when the block
is self-evident (a single short formula rarely needs one).

## Example

```
:::solution{label="Solution"}
:::concept{label="Given"}
The block is on a frictionless incline of angle 30°.
:::

:::step{n="1"}
Apply Newton's second law along the incline.

:::formula{label="Key formula"}
$$F = ma$$
:::
:::

:::step{n="2"}
Substitute the given values and solve for $a$.
:::
:::
```

This example is in English for readability here only — transpose its
*shape*, not its words, into the chapter's actual language: a Hindi
chapter's labels, step text and everything else stay in Hindi throughout.

## Judgement calls

- A multi-part question (`:::part{label="a"}`, `:::part{label="b"}`, ...)
  sometimes has a **second, whole-item `:::solution` after the labelled
  parts that just re-narrates the same working** — a known artifact from
  upstream matching, occasionally with OCR-degraded numbers in the
  duplicate that don't match the correct per-part version. Don't delete it
  (stage 7 doesn't remove content) and don't try to reconcile the two by
  hand — leave both exactly as extracted, but say so explicitly in your
  stage report (which item ids) so stage 8 knows to render only the
  per-part solutions and treat the trailing whole-item one as the
  redundant copy, not a second, different answer.

- Split into steps only when the solution genuinely has stages. A two-line
  substitution is one block, not three steps.
- `:::note{type="caution"}` is for a warning the textbook makes, not one you
  would like to make — never invent a note whose content isn't already in
  the source text.
- A figure already exists near the top of the item, emitted by stage 4. If
  the solution names it ("as shown in Fig. 10.4"), move that exact
  `:::figure{...}` block to its first reference point — same `src`, same
  `id`. Don't duplicate it, don't create a second one.
- Do not wrap every equation in `:::formula`. Use it for the ones a student
  would want to find again.
- A `label` names what a block *is* ("Given", "Key formula", "Classification"),
  never a paraphrase of what it *concludes* — that would be rewording content
  under a different name. If you're not confident of a short, accurate noun
  phrase, leave `label` off rather than guess.
- Wrap a table exactly as it already appears — same rows, columns and cell
  text. `:::table` adds a wrapper; it does not reformat.
- When a passage doesn't clearly call for any of these, leave it as plain
  paragraph text inside the container it's already in. Forcing structure onto
  ordinary prose is worse than leaving it unmarked.

Return the markdown only — no preamble, no code fences.
