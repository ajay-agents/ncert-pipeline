# Stage 2 — extraction prompt

You are extracting from a Mathpix conversion of an NCERT textbook. The markdown
is faithful but imperfect: headers repeat, page numbers leak in, subscripts are
sometimes lost, and figures appear as image references.

## Extract

For the requested pass only (examples, exercises, or solutions), return
container markdown: one `:::example{...}` or `:::question{...}` block per
item, in the vocabulary `_shared/RULES.md` defines. Nothing else — no
preamble, no fences. `pipeline/render.py`'s `render_item()` shows the exact
shape (`:::prompt`, `:::part{label="..."}`, `:::solution`, `:::answer`,
`:::figure{src="..." id="..."}`); match it exactly so
`pipeline/mdio.py`'s parser can read it back.

- `number=` attr: exactly as printed. Normalisation happens downstream.
- `:::prompt`: the full statement, including any table or figure reference.
- `:::part{label="..."}`: only when the question has labelled sub-parts. Do
  not invent parts from a multi-sentence question.
- `:::solution`: for examples, the textbook's own worked solution. For the
  exercises pass, leave it out — solutions come from the other document.
- `:::answer`: the boxed or stated result, with units, if one is given.
  Leave it out for proofs, derivations and descriptive answers.
- `:::figure{src="..." id="..."}`: every image reference inside the item,
  with its caption as the block's body text.
- `topic=` attr: a short (2–6 word) descriptive title for what the item is
  about, e.g. "Mole fraction", "Henry's law". **This is not printed in the
  textbook** — you are writing a short label, not transcribing one. Keep it
  factual and specific to what the item actually asks or shows; do not
  characterise it as something it isn't. This field is never checked against
  the PDF (stage 5 has nothing to check it against) and is not rewritten in
  stage 6 — write it once, here, correctly. Since it becomes a single-line
  `{k="v"}` attribute, never put a literal `"` or a newline in it.

## Do not

- Do not fix, complete or improve anything. Transcribe.
- Do not merge two questions that share a stem — emit both, repeating the stem.
- Do not drop a question because its text looks garbled. Extract it as-is; the
  verification stage repairs it against the PDF.
- Do not carry page headers, running footers or "Rationalised 2023-24" banners
  into any field.
- Do not try to reconcile the exercises pass's numbering against the
  solutions pass's numbering, even if you notice they've drifted apart (a
  "Rationalised" curriculum edition of the textbook can drop an exercise a
  same-vintage-mismatched solutions manual still numbers around). Extract
  each document exactly as printed in it, mention the mismatch in your
  stage report if you spot one, and leave the reconciliation to stage 3's
  `join_solutions()` — which still needs the untouched original numbers
  from both sides to do its job.

## Math

Keep `$...$` and `$$...$$` exactly as they appear, including spacing. If Mathpix
produced obviously broken LaTeX, keep it broken and continue.
