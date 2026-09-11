Stage 10 — export the finished design page to a fixed PDF.

Build `chapters/$ARGUMENTS/10_pdf/final.<lang>.pdf` from
`09_design/final.<lang>.html` (+ its CSS, + the `images/` folder next to
it). Nothing about the page's content or design changes at this stage —
this is a mechanical export pass, not a second design pass.

Before starting: check `manifest.unchanged_since(chapters/$ARGUMENTS/, "pdf",
09_design/final.<lang>.html path(s))`. If true, stop and report.

## How to export

Render with a real browser engine, not a converter that reimplements CSS
on its own (`wkhtmltopdf`, most pure-Python HTML-to-PDF libraries) — this
page uses flexbox, CSS grid, `@media` breakpoints, `zoom`, `break-inside`
and a webfont `@import`, and a partial-CSS-support renderer will silently
drop or mis-lay-out some of that in a way that's easy to miss without a
side-by-side comparison. Playwright with Chromium (confirmed available in
this environment) is the same engine a human gets from a browser's own
"Print to PDF", so it renders the page identically:

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto(file_url, wait_until="networkidle")
    page.evaluate("document.fonts.ready.then(() => true)")  # see below
    page.pdf(path=out_path, print_background=True, prefer_css_page_size=True)
    browser.close()
```

- Navigate to the file's own `file://` path (not a copy elsewhere), so its
  relative `href="final.<lang>.css"` and `<img src="images/...">`
  references resolve exactly as they will for anyone else opening the
  same file — this is the same "actual output directory, not a scratch
  copy" rule stage 9's own checks already follow.
- `page.evaluate("document.fonts.ready...")` (or an equivalent explicit
  wait) matters: the chapter's webfonts (Noto Serif Devanagari / STIX Two
  Text) load asynchronously from the CSS's `@import`, and printing before
  they've resolved silently falls back to a generic serif font instead of
  failing loudly — the PDF would still "work", just render Devanagari
  wrong. `networkidle` alone is not the same guarantee.
- **Always call `page.emulate_media(media="screen")` immediately before
  `page.pdf()`.** Chromium's default print-media text-shaping pipeline has
  a real bug mis-rendering Devanagari pre-base vowel-sign reordering
  (े/ि) for text whose nearest explicitly-font-sized ancestor differs
  from its own font-size — caught for real on physics-12-2's own chapter
  title (`.s3` at 38px, nested under `.s1`'s 12.5px page-wide base):
  "स्थिरवैद्युत विभव तथा धारिता" came out visibly garbled in the exported
  PDF (extra/misplaced matra strokes) despite the underlying HTML text
  being byte-correct (confirmed with `repr()` — this is a rendering
  defect, not a data bug) and despite rendering perfectly on-screen and
  in a plain screenshot. Root-caused across ~10 isolated test pages
  before finding the fix: forcing screen-media emulation makes
  `page.pdf()` use the (unaffected) screen shaping path instead —
  `page.pdf()` still paginates via `@page` regardless of the emulated
  media type, so this doesn't reintroduce the "ignores `@page`" problem
  the `prefer_css_page_size` bullet above warns about; verified byte-
  identical page count and A4 dimensions with vs. without the call.
  physics-12-1 never hit this because none of its own title/heading text
  happened to need pre-base vowel reordering — this is a standing
  per-export fix for every future chapter, not a one-off patch, since any
  Hindi chapter's title or a `.s12`/`.s71`-style section-divider label
  could contain a word that needs it. Do this even if the chapter's own
  title looks fine in a quick check — the failure is invisible until you
  specifically zoom into the exported PDF's own rendered text (a live
  browser screenshot of the same HTML will NOT show it), so it's cheap
  enough to apply unconditionally rather than re-diagnose per chapter.
- `prefer_css_page_size=True` + `print_background=True` are what makes
  the export honor the `@page`/`@media print` rules already in the base
  CSS (A4, 9mm margins, colored backgrounds kept) instead of Playwright's
  own default page size, which would silently ignore the chapter's own
  print styling.
- Do not pass an explicit `format`/`width`/`height` — that overrides
  `prefer_css_page_size` and reintroduces the same "ignores `@page`"
  problem from the other direction.

## Gate

Unlike stage 9's raw HTML, a fixed PDF's actual rendered content **is**
mechanically checkable, since export is now a real additional rendering
pass (fonts resolving, pagination, an image failing to embed) that can
independently drop or corrupt something even when the HTML itself was
correct — so this stage gets a real gate, not just a note. Using
`fitz`/PyMuPDF (already used elsewhere in this pipeline for reading
source PDF pages):

- **Page count is sane** for the chapter's item count (not 1 page, not
  triple digits) — a wildly wrong count usually means the print CSS
  didn't apply (`prefer_css_page_size` missing) or the page failed to
  load fully.
- **No fully blank page** (`page.get_text().strip()` empty) — a common
  symptom of a font or asset that failed to load in time.
- **The same numeric read-back stage 9 does, re-run against the PDF's own
  extracted text**, not assumed carried over from the HTML check: pull
  every numeric token out of each `final_answer`/`question` field in
  `06_simplify/chapter.simplified.<lang>.md` (via `mdio.markdown_to_chapter`,
  same as stage 9) and confirm each appears somewhere in the PDF's
  extracted text across all pages.
  **A trap already hit once here**: this chapter renders simple numeric
  exponents as literal unicode superscript characters (e.g. `10³⁹`), and
  a naive character-for-character translate of those back to ASCII digits
  glues the base number and the exponent into one merged token (`10³⁹` →
  `"1039"`) — which then hides a genuine `"39"` or `"36"` from ever
  matching on its own, an entirely false "missing" result (the content
  was correct; the check was wrong). Insert a separator before a run of
  superscript characters when normalizing, not a raw
  `str.translate()` with no separator, so a base number and its exponent
  normalize to two distinct tokens.

Any failure here is a hard stop, same as any other gate in this
pipeline — fix the underlying HTML/CSS (stage 9's own output) or the
export call, re-export, and re-check; never hand-edit the PDF.

**A known, currently-unresolved limitation, not a bug in this pipeline's
own code: Chromium's print-to-PDF pipeline generates an incorrect
ToUnicode CMap for Devanagari "र्" used as a pre-base reph (रेफ़) form —
"र्" + consonant — dropping that character from the exported PDF's
*extractable* text layer specifically, while the *visual* rendering stays
completely correct.** Caught for real on physics-12-2's final PDF: a user
reading the rendered pages found nothing wrong, but copying text out (or
re-extracting it, e.g. `fitz`/`pdftotext`) turned "निष्कर्ष" into
"निष्कष", "पदार्थ" into "पदाथ", "आघूर्ण" into "आघूण", "कार्य" into "काय" —
every instance of a "र्"-plus-consonant sequence loses the "र्", nothing
else. Root-caused with an isolated test page (plain "र्"-bearing words, no
other content) and confirmed with two independent extraction tools
(`fitz`/PyMuPDF *and* `pdftotext`/poppler both fail on the same text, in
different ways - `pdftotext` extracts nothing at all for the affected
run, `fitz` extracts everything except the reph) - this rules out a
single-tool extraction quirk and confirms the fault is baked into the
PDF's own embedded CMap at export time, not read-side. Also ruled out as
the cause: font choice (reproduces identically on both Noto Serif
Devanagari and Noto Sans Devanagari, regular and bold), the standing
`emulate_media(media="screen")` fix (reproduces identically with or
without it - this is a distinct bug from the visual pre-base-vowel-
reordering one that fix addresses), and Playwright's `tagged=True` PDF
option plus various Chromium font-rendering flags (none changed the
result). This means the numeric read-back gate above is unaffected (it
only checks digits), but any consumer relying on copy-paste, in-PDF
search, or a future pipeline stage re-reading this PDF's text should
expect "र्"-bearing words to come back one character short. No working
fix is known yet from within this pipeline (a real fix would mean either
post-processing the exported PDF's ToUnicode CMap directly - low-level
PDF surgery, not attempted - or a different PDF-generation pipeline
entirely); flag this to the user rather than silently shipping around it
if it matters for a specific chapter's use case.

## Manifest

Append a `manifest.py` entry: stage `"pdf"`, inputs the
`09_design/final.<lang>.html` hash(es), counts = page count, file size,
and the read-back result (numbers checked / missing), model_calls = 0
(this stage is fully mechanical — export and the checks above are code,
not judgment).

No `CALIBRATION/calibrate.py` re-run is needed — it only reads pre-stage-7
flat markdown and has nothing to say about a PDF export.
