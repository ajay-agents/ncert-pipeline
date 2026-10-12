"""Stage 9/10 helper for Hindi-medium chapter titles.

Chromium's print/PDF export (`page.pdf()`) — and even plain
`page.screenshot()` in some configurations — has a reproducible defect
rendering the chapter title (`.s3`, 38px Devanagari, nested under a
smaller zoomed base `.s1` at 12.5px + `zoom:0.63`): vowel signs and
anusvara/chandrabindu marks are silently dropped from specific letters,
visually clipping the title ("विचारक" renders as "िवचारक" with the top
of several glyphs cut away).

Root-caused (after extensive trial-and-error - several hundred repeated
export/screenshot attempts across many isolated CSS variations, binary-
searching one property at a time) to TWO separate, compounding factors:

1. **`line-height:1.2` on `.s3` itself.** Isolated by binary search:
   the identical title, identical `.s1` zoom/size nesting, identical
   font, with `line-height:1.2` on `.s3` reproduced the defect 6/6
   repeated trials; removing only that one declaration (leaving `.s3`
   at its default line-height) made the same markup render correctly
   10/10 repeated trials, repeated again across all four titles tested.
   This is the dominant factor - do not set `line-height` on this
   element at all.
2. **Font weight**: independently, Google Fonts' served *700 (bold)*
   file for Noto Serif Devanagari also has its own real, reproducible
   defect for this glyph combination at this size, separate from (1).
   *600 (semi-bold)* does not - confirmed clean across dozens of
   repeated trials, and visually close enough to bold for this use.
   Use weight 600, never 700, for this title.

Also confirmed NOT to matter, despite each initially looking like a
plausible cause and costing real investigation time: a `zoom` ancestor
combined with a horizontal width constraint (CSS `width` on `.s1`, or a
matching Playwright viewport width) - looked like a strong signal in
isolation but stopped correlating once `line-height` was controlled
for; `'STIX Two Text'` present vs. absent in the font-family fallback
list; Google Fonts' async `@import` vs. a locally self-hosted
`font-display:block` file; `document.fonts.ready` vs. an additional
fixed delay; GPU rendering vs. `--disable-gpu`; a fresh, never-before-
used browser profile/disk-cache directory. None of these reproduced or
fixed the defect once (1) and (2) above were controlled for - ruling
out a font-loading race or a persistent on-disk/GPU cache as the real
cause.

The title is rendered at the browser's default (unconstrained) viewport
width (confirmed not to matter once (1)/(2) were fixed, and simplest to
keep that way), so the resulting PNG is cropped to its own ink bounding
box, then spliced into the real page sized by HEIGHT ONLY
(`height:...px; width:auto;`), preserving its aspect ratio - never
force both width and height independently, which stretches/squashes
the text non-uniformly.

Use from a stage 10 export script:

    from pipeline.pdf_title import splice_title_image

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(file_url, wait_until="networkidle")
        page.evaluate("document.fonts.ready.then(() => true)")
        splice_title_image(page, title_text, subtitle_text)
        page.emulate_media(media="screen")
        page.pdf(path=out_path, print_background=True, prefer_css_page_size=True)
        browser.close()

`title_text`/`subtitle_text` must match the chapter's own `.s3`/`.s4`
content exactly (the chapter title and the "अध्याय N · ..." line) -
pass them as plain strings, not HTML.

Only needed for the Hindi PDF. The English page's title uses the same
`.s3`/`.s4` classes but plain Latin text, which has never shown this
defect in any export across this entire pipeline - do not call this
for lang == "en".
"""
from __future__ import annotations

import io

from playwright.sync_api import Page

_TITLE_TEMPLATE = """<!DOCTYPE html>
<html lang="hi">
<head>
<meta charset="utf-8">
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Serif+Devanagari:wght@400;600&display=swap');
body {{ margin:0; font-family:'Noto Serif Devanagari',serif; color:#1b1b1b; }}
.s1 {{ font-size:12.5px; zoom:0.63; }}
.s2 {{ text-align:center; margin:0; }}
.s3 {{ font-family:'Noto Serif Devanagari',serif; font-weight:600; font-size:46px; }}
.s4 {{ font-size:21px; color:#0c5b5e; margin-top:4px; }}
.s5 {{ display:flex; justify-content:center; gap:8px; margin-top:12px; }}
.s6 {{ width:9px; height:9px; border-radius:50%; background:#10989e; }}
.s7 {{ width:9px; height:9px; border-radius:50%; background:#f5820b; }}
.s8 {{ width:9px; height:9px; border-radius:50%; background:#e42a63; }}
.s9 {{ width:9px; height:9px; border-radius:50%; background:#7a3df0; }}
</style>
</head>
<body>
<div class="s1">
  <div class="s2">
    <div class="s3">{title}</div>
    <div class="s4">{subtitle}</div>
    <div class="s5"><span class="s6"></span><span class="s7"></span><span class="s8"></span><span class="s9"></span></div>
  </div>
</div>
</body>
</html>
"""

# Visual (effective, on-page, POST-zoom) size of the spliced-in title
# image, in CSS px - the .s2 box's own apparent height as a reader
# would see it. Scaled up from the real page's own un-enlarged .s3/.s4
# (38px/17px, giving a 61.4375px-tall .s2 - this is maths-12-1's own
# live-text title, measured directly, and the reference size the user
# pointed back to as "not too small") by the same ratio as
# _TITLE_TEMPLATE's own enlarged 46px/21px sizes, so the title doesn't
# look stretched relative to its own line spacing - increased once
# already at the user's request (the original 38px/17px/61.4375px read
# as too small once the title-clipping fix's weight/line-height
# constraints were applied).
_TARGET_EFFECTIVE_HEIGHT_PX = 61.4375 * (46 / 38)

# The real page's own `.s1 { zoom:0.63 }` wrapper (see final.*.css)
# applies to the spliced `<img>` too, since it lives inside `.s2` which
# lives inside `.s1` - so a CSS `height` set directly to the value
# above would get shrunk by this factor AGAIN on screen/in the PDF,
# landing well under the intended size (confirmed: economics-12-1's
# first splice attempt rendered .s2 at an effective 46.8px - smaller
# than even the un-enlarged 61.4375px baseline above, despite nominally
# targeting 74.4px - exactly _TARGET_EFFECTIVE_HEIGHT_PX * 0.63). The
# CSS height actually assigned to the <img> must counteract that by
# dividing by this same zoom factor first.
_PAGE_ZOOM = 0.63
_TARGET_HEIGHT_PX = _TARGET_EFFECTIVE_HEIGHT_PX / _PAGE_ZOOM


def _crop_to_content(png_bytes: bytes) -> bytes:
    from PIL import Image, ImageChops

    im = Image.open(io.BytesIO(png_bytes)).convert("RGB")
    bg = Image.new("RGB", im.size, (255, 255, 255))
    diff = ImageChops.difference(im, bg)
    bbox = diff.getbbox()
    if bbox is None:
        return png_bytes
    cropped = im.crop(bbox)
    out = io.BytesIO()
    cropped.save(out, format="PNG")
    return out.getvalue()


def render_title_png(title_text: str, subtitle_text: str, browser=None) -> bytes:
    """Render the .s2 title block reliably and return it as PNG bytes,
    already cropped tight to its own content (no surrounding
    whitespace).

    `browser` is optional: pass an already-launched Playwright
    `Browser` (e.g. `page.context.browser` from your main export page)
    to open a temporary page on it - Playwright's sync API cannot open
    a second, nested `sync_playwright()` context inside an already-open
    one. Without `browser`, launches and closes its own short-lived
    one - only safe to call this way OUTSIDE any other open
    `sync_playwright()`/browser context (e.g. before opening the real
    export page, not with it open).

    See this module's own docstring for the two confirmed trigger
    conditions this template deliberately avoids (`.s3`'s own
    `line-height`, and font-weight 700)."""
    html = _TITLE_TEMPLATE.format(title=title_text, subtitle=subtitle_text)

    def _capture(b):
        page = b.new_page()
        try:
            page.set_content(html, wait_until="networkidle")
            page.evaluate("document.fonts.ready.then(() => true)")
            return page.locator(".s2").screenshot()
        finally:
            page.close()

    if browser is not None:
        png_bytes = _capture(browser)
    else:
        from playwright.sync_api import sync_playwright

        with sync_playwright() as p:
            b = p.chromium.launch()
            try:
                png_bytes = _capture(b)
            finally:
                b.close()
    return _crop_to_content(png_bytes)


def splice_title_image(page: Page, title_text: str, subtitle_text: str) -> None:
    """Replace the real, already-loaded page's live `.s2` title block
    with a static image of itself, rendered reliably in isolation and
    scaled by height only (aspect ratio preserved, never stretched).
    Call after `document.fonts.ready` and before `page.pdf()`.

    Renders the title on a temporary page opened on `page`'s own
    browser (`page.context.browser`), not a second nested
    `sync_playwright()` context - safe to call with `page` already
    open, unlike calling `render_title_png()` directly mid-session."""
    import base64

    png_bytes = render_title_png(title_text, subtitle_text, browser=page.context.browser)
    b64 = base64.b64encode(png_bytes).decode("ascii")
    page.evaluate(
        """(args) => {
            const [b64, targetHeight] = args;
            const el = document.querySelector('.s2');
            el.innerHTML = '<img src="data:image/png;base64,' + b64 +
                '" style="height:' + targetHeight + 'px;width:auto;display:block;margin:0 auto;" alt="">';
        }""",
        [b64, _TARGET_HEIGHT_PX],
    )
