"""Stage 1. The only external service in the pipeline."""
from __future__ import annotations

import json
import os
import re
import time
from pathlib import Path

import requests

BASE = "https://api.mathpix.com/v3"
IMG_RE = re.compile(r"!\[([^\]]*)\]\((https?://[^)\s]+)\)")

SUBJECT_OPTIONS = {
    "physics":   {"include_smiles": False},
    "maths":     {"include_smiles": False},
    "chemistry": {"include_smiles": True, "include_chemistry_as_image": False},
    "biology":   {"include_smiles": False, "enable_tables_fallback": True},
}


def _headers() -> dict:
    app_id, key = os.environ.get("MATHPIX_APP_ID"), os.environ.get("MATHPIX_APP_KEY")
    if not (app_id and key):
        raise RuntimeError("set MATHPIX_APP_ID and MATHPIX_APP_KEY")
    return {"app_id": app_id, "app_key": key}


def _download_images(md_text: str, images_dir: Path, chapter: str) -> str:
    """Replace Mathpix CDN image URLs with local copies under images_dir.

    Figure numbering continues across calls (chapter + solutions PDFs share
    one images/ dir) by counting files already on disk for this chapter.
    """
    images_dir.mkdir(parents=True, exist_ok=True)
    counter = len(list(images_dir.glob(f"fig_{chapter}_*")))
    seen: dict[str, str] = {}

    def _sub(m: re.Match) -> str:
        nonlocal counter
        alt, url = m.group(1), m.group(2)
        if url not in seen:
            ext = Path(url.split("?", 1)[0]).suffix or ".png"
            name = f"fig_{chapter}_{counter}{ext}"
            counter += 1
            resp = requests.get(url)
            resp.raise_for_status()
            (images_dir / name).write_bytes(resp.content)
            seen[url] = f"images/{name}"
        return f"![{alt}]({seen[url]})"

    return IMG_RE.sub(_sub, md_text)


def convert(pdf_path: str | Path, out_dir: str | Path, subject: str,
            lang: str = "en", chapter: str = "", poll_seconds: int = 5,
            timeout: int = 900) -> Path:
    """Upload a PDF, wait for conversion, write <stem>.mmd into out_dir.

    Also pulls every embedded figure down into out_dir/images/, since a page
    referencing cdn.mathpix.com is not usable once the conversion job expires.
    """
    pdf_path, out_dir = Path(pdf_path), Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    chapter = chapter or pdf_path.stem

    options = {
        "conversion_formats": {"md": True},
        "math_inline_delimiters": ["$", "$"],
        "math_display_delimiters": ["$$", "$$"],
        "rm_spaces": True,
        "enable_tables_fallback": True,
        "page_ranges": "1-",
        **SUBJECT_OPTIONS.get(subject, {}),
    }
    if lang == "hi":
        options["numbers_default_to_math"] = True   # protects Devanagari digits

    with pdf_path.open("rb") as fh:
        r = requests.post(f"{BASE}/pdf", headers=_headers(),
                          files={"file": fh}, data={"options_json": json.dumps(options)})
    r.raise_for_status()
    pdf_id = r.json()["pdf_id"]

    deadline = time.time() + timeout
    while time.time() < deadline:
        status = requests.get(f"{BASE}/pdf/{pdf_id}", headers=_headers()).json()
        if status.get("status") == "completed":
            break
        if status.get("status") == "error":
            raise RuntimeError(f"mathpix failed: {status}")
        time.sleep(poll_seconds)
    else:
        raise TimeoutError(f"mathpix timed out on {pdf_path.name}")

    md = requests.get(f"{BASE}/pdf/{pdf_id}.md", headers=_headers())
    md.raise_for_status()
    text = _download_images(md.text, out_dir / "images", chapter)
    # pdf_path.stem is already e.g. "chapter.hi" (only .pdf is stripped) — the
    # source filename convention bakes the language in, so don't append it twice.
    target = out_dir / f"{pdf_path.stem}.md"
    target.write_text(text, encoding="utf-8")
    return target
