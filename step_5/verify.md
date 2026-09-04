# Stage 5 — verification prompt

You are comparing extracted items against the original NCERT PDF pages attached
to this message. The PDF is the authority; the extracted text is the suspect.

Return a list of corrections as markdown blocks, one per correction — no
preamble, no code fences. Return nothing (no blocks) if the batch is clean.
`pipeline/mdio.py`'s `markdown_to_corrections()` is the parser this must match:

```
### q_10.3 — question (en)
- **Confidence:** high
- **Reason:** OCR lost the exponent
- **Found:**
  > a pressure of 1 x 105 Pa
- **Should be:**
  > a pressure of $1 \times 10^5$ Pa
```

The heading line is always `### <item_id> — <field> (<lang>)` exactly, in
that order, with an em dash (`—`).

## Look for, in this order

1. **Numbers and units** — digits, exponents, subscripts, superscripts, units.
   This is where OCR fails and where a wrong value does the most damage.
2. **Missing sub-parts** — a question printed with (a)–(d) that extracted with
   three. A missing sub-part has no field to correct into — `found`/`should_be`
   can't create one. Note it in your stage summary instead of a correction
   block; the user adds the part to the chapter markdown directly.
3. **Question numbering** — items attributed to the wrong number.
4. **Truncation** — a statement that ends mid-sentence.
5. **Figure references** — an item that mentions "Fig. 10.4" with no figure attached.
6. **Wording** — only where meaning changed. Ignore whitespace and punctuation style.

## Language

Check `en` fields only against the English PDF pages, and `hi` fields only
against the Hindi PDF pages. NCERT's two editions are independent, not
translations of each other — never "fix" one language using the other as the
reference, and never justify a `hi` correction by what the English page says.

## Addressing a field

`field` is `"question"`, `"solution"`, or `"final_answer"` for the item
itself, or `"parts[N].question"` / `"parts[N].solution"` /
`"parts[N].final_answer"` for a labelled sub-part, `N` 0-indexed in source
order. There is no way to address a figure caption or a field that doesn't
exist — skip those rather than invent a field name.

## Rules

- `should_be` must be what the PDF actually shows. Never what you think is
  physically correct. If the textbook has an error, that is not your call.
- `found` must be an exact substring of the current field **and appear
  exactly once** — a correction whose `found` matches zero or multiple times
  is held back, not applied. If the same fragment occurs twice in a field,
  extend `found` with enough surrounding text to make it unique.
- If one field needs two separate fixes, return two `Correction` objects
  rather than one spanning both. They are applied in the order you return
  them, each against the text as already changed by the ones before it in
  the same batch — so the second `found` must still match after the first lands.
- `confidence: high` only when the PDF page is legible and the difference is
  unambiguous. Anything you are inferring is `medium` at best.
- Never return a corrected version of the whole field.
