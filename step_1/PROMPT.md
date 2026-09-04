Stage 1 — convert chapter and solutions PDFs to markdown via Mathpix.

Convert the PDFs in `chapters/$ARGUMENTS/00_raw/` to markdown.

Before starting: check `manifest.unchanged_since(chapters/$ARGUMENTS/, "mathpix", *the
four PDFs)`. If true, this stage already ran against these exact files —
report that and stop; do not reconvert.

1. Confirm the PDFs are present: `chapter.en.pdf`, `chapter.hi.pdf`,
   `solutions.en.pdf`, `solutions.hi.pdf`. NCERT publishes an official
   Hindi edition for every chapter but not always an English one in this
   pipeline's own PDF set — a **Hindi-only** chapter (only `chapter.hi.pdf`
   + `solutions.hi.pdf` in `00_raw/`, no `.en.pdf` files at all) is valid
   and every later stage already handles it; just convert the two files
   that exist. If a **Hindi** PDF is missing (with or without an English
   one present), stop and ask — that's the one configuration this pipeline
   doesn't support silently.
2. Run `pipeline.mathpix.convert()` for each, passing the subject and chapter
   number from the directory name so the right Mathpix options are used and
   figures are named `fig_<chapter>_<n>`.
3. Write outputs to `01_mathpix/`. `convert()` already downloads every figure
   referenced in the markdown into `01_mathpix/images/` and rewrites the
   image links to point at the local copy — do not fetch images yourself.
   Note the real extension varies (`.jpg`/`.png` from the Mathpix CDN); do not
   rename or re-encode to force `.png`.
4. Sanity check each `.mmd`: report page count, character count, number of `$`
   spans, number of markdown tables, number of image references.
5. Flag anything suspicious — a chapter file under 5000 characters, zero tables
   in a Chemistry chapter, Devanagari appearing in the English file.

No model reasoning about content in this stage. Convert, count, report.

Append a `manifest.py` entry: `manifest.append(chapters/$ARGUMENTS/, "mathpix",
inputs=manifest.input_hashes(*the four PDFs), counts={"pages": ..., "chars": ...},
model_calls=0)`.
