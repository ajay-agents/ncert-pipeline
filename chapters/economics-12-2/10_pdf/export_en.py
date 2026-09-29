# -*- coding: utf-8 -*-
"""Stage 10 export script for economics-12-2: renders 09_design/final.en.html
to 10_pdf/final.en.pdf with Playwright/Chromium, per step_10/PROMPT.md."""
import pathlib
from playwright.sync_api import sync_playwright

CH = r"C:\Users\gunja\Downloads\ncert-pipeline\chapters\economics-12-2"
html_path = pathlib.Path(CH) / "09_design" / "final.en.html"
out_path = pathlib.Path(CH) / "10_pdf" / "final.en.pdf"
out_path.parent.mkdir(parents=True, exist_ok=True)

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto(html_path.as_uri(), wait_until="networkidle")
    page.evaluate("document.fonts.ready.then(() => true)")
    page.wait_for_timeout(300)
    # Standing fix for Chromium's print-media Devanagari pre-base vowel-sign
    # reordering bug (documented in step_10/PROMPT.md) - applied unconditionally
    # even though this page's own text is English, per that file's own
    # guidance to keep every chapter's export script the same shape.
    page.emulate_media(media="screen")
    page.pdf(path=str(out_path), print_background=True, prefer_css_page_size=True)
    browser.close()

print("wrote", out_path, out_path.stat().st_size, "bytes")
