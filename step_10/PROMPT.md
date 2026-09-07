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

## Manifest

Append a `manifest.py` entry: stage `"pdf"`, inputs the
`09_design/final.<lang>.html` hash(es), counts = page count, file size,
and the read-back result (numbers checked / missing), model_calls = 0
(this stage is fully mechanical — export and the checks above are code,
not judgment).

No `CALIBRATION/calibrate.py` re-run is needed — it only reads pre-stage-7
flat markdown and has nothing to say about a PDF export.
