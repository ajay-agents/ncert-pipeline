"""End-to-end check of the deterministic stages: match -> render -> mdio -> gates."""
import json
import tempfile
from pathlib import Path

from pipeline.schema import Chapter, Item, Text, Part, Figure, Correction
from pipeline.match import norm_num, join_solutions, align_languages
from pipeline.render import render
from pipeline.tag import _parse, TagError
from pipeline.protect import freeze, restore, ProtectionError
from pipeline.verify import apply_corrections
from pipeline import gates, manifest, mdio

# --- number normalisation ---------------------------------------------------
assert norm_num("Q. 3", "10") == "10.3"
assert norm_num("प्रश्न 10.3।") == "10.3"
assert norm_num("Example 10.1", "10") == "10.1"
assert norm_num("3.", "10") == "10.3"
print("PASS  norm_num")

# --- protection round trip --------------------------------------------------
src = (r"The speed is $v = 3 \times 10^8$ m/s and the energy follows"
       "\n\n$$E = mc^2$$\n\n| a | b |\n|---|---|\n| 1 | 2 |\n")
masked, mapping = freeze(src)
assert "$" not in masked and "|" not in masked, masked
shuffled = masked.replace("The speed is", "The speed here is")   # simulate a rewrite
assert restore(shuffled, mapping).count("$$") == 2
try:
    restore(masked.split("\u27e6")[0], mapping)
except ProtectionError:
    print("PASS  protect (round trip + loss detection)")
else:
    raise AssertionError("dropped token was not detected")

# --- matching ---------------------------------------------------------------
qs = [Item(id="q_10.1", kind="exercise", number="1", topic=Text(en='Rest & "momentum"'),
           question=Text(en="A body of mass $2$ kg is at rest.")),
      Item(id="q_10.2", kind="exercise", number="2",
           question=Text(en="Find the work done."))]
sols = [Item(id="s2", kind="exercise", number="10.2",
             solution=Text(en="$W = Fd = 10$ J"), final_answer=Text(en="$10$ J")),
        Item(id="s1", kind="exercise", number="10.1",
             solution=Text(en="Its momentum is zero."), final_answer=Text(en="$0$"))]
merged, report = join_solutions(qs, sols, chapter="10")
assert report["matched"] == 2 and not report["needs_review"], report
print("PASS  join_solutions")

# --- language alignment -----------------------------------------------------
en = Chapter(subject="physics", class_level=11, chapter_number="10",
             title=Text(en="Work, Energy and Power"), items=merged)
hi = Chapter(subject="physics", class_level=11, chapter_number="10",
             title=Text(hi="कार्य, ऊर्जा और शक्ति"),
             items=[Item(id="q_10.1", kind="exercise", number="10.1",
                         question=Text(hi="$2$ किग्रा द्रव्यमान का पिंड विरामावस्था में है।"),
                         solution=Text(hi="इसका संवेग शून्य है।")),
                    Item(id="q_10.2", kind="exercise", number="10.2",
                         question=Text(hi="किया गया कार्य ज्ञात कीजिए।"),
                         solution=Text(hi="$W = Fd = 10$ जूल"))])
chapter, align_report = align_languages(en, hi)
assert align_report["aligned"] == 2, align_report
chapter.title.hi = "कार्य, ऊर्जा और शक्ति"
chapter.items[0].figures.append(
    Figure(id="fig_10_1", src="images/fig_10_1.png", caption=Text(en="Body at rest", hi="विरामावस्था में पिंड")))
print("PASS  align_languages")

# --- gates ------------------------------------------------------------------
gates.report("counts", gates.gate_counts(chapter, {"exercise": 2}))
gates.report("solutions en", gates.gate_solutions_present(chapter, "en"))
gates.report("solutions hi", gates.gate_solutions_present(chapter, "hi"))
gates.report("bilingual", gates.gate_bilingual(chapter))

# --- render (container markdown - stage 8 is hand-designed only now, no
# fixed-code fallback, so this only checks the markdown shape) -------------
out_dir = Path(tempfile.gettempdir())
for lang in ("en", "hi"):
    md = render(chapter, lang)
    assert ":::question" in md and ":::solution" in md and ":::figure" in md
    assert "$2$" in md or "किग्रा" in md
    if lang == "en":
        assert 'topic="Rest & \'momentum\'"' in md, md   # literal " sanitised to '
    (out_dir / f"chapter.{lang}.md").write_text(md, encoding="utf-8")
print(f"PASS  render (wrote {out_dir / 'chapter.en.md'}, {out_dir / 'chapter.hi.md'})")

# --- markdown <-> Chapter round trip (the on-disk format from stage 2 on) ---
for lang in ("en", "hi"):
    back = mdio.markdown_to_chapter(render(chapter, lang), lang)
    orig_item = chapter.index()["q_10.1"]
    got_item = back.index()["q_10.1"]
    assert got_item.question.get(lang) == orig_item.question.get(lang)
    assert got_item.solution.get(lang) == orig_item.solution.get(lang)
    assert back.index()["q_10.2"].final_answer.get(lang) == chapter.index()["q_10.2"].final_answer.get(lang)
    fig = back.index()["q_10.1"].figures[0]
    assert fig.id == "fig_10_1" and fig.caption.get(lang) == chapter.index()["q_10.1"].figures[0].caption.get(lang)
print("PASS  mdio markdown <-> Chapter round trip")

# --- mdio stage-2 shape round trip (examples/exercises/solutions lists) -----
by_section = {"examples": [], "exercises": qs, "solutions": []}
ext_md = mdio.items_to_markdown(by_section, "en")
assert "## Exercise Questions" in ext_md
ext_back = mdio.markdown_to_extraction(ext_md, "en")
assert len(ext_back["exercises"]) == 2 and not ext_back["examples"] and not ext_back["solutions"]
assert ext_back["exercises"][0].question.en == qs[0].question.en
print("PASS  mdio stage-2 extraction round trip")

# --- correction application --------------------------------------------------
before = chapter.model_copy(deep=True)
corr = Correction(item_id="q_10.2", lang="en", field="solution",
                  found="10", should_be="10.0", reason="unit precision", confidence="high")
after, applied, held = apply_corrections(before, [corr])
assert applied and not held, (applied, held)
assert after.index()["q_10.2"].solution.en == "$W = Fd = 10.0$ J"
assert after.index()["q_10.2"].corrections_applied == 1
low_conf = Correction(item_id="q_10.1", lang="en", field="solution",
                      found="zero", should_be="0", reason="style", confidence="low")
_, applied2, held2 = apply_corrections(before, [low_conf])
assert held2 and not applied2, (applied2, held2)
print("PASS  apply_corrections (applies high confidence, holds low confidence)")

corr_md = mdio.corrections_to_markdown([corr])
corr_back = mdio.markdown_to_corrections(corr_md)
assert len(corr_back) == 1 and corr_back[0].found == "10" and corr_back[0].should_be == "10.0"
assert corr_back[0].confidence == "high" and corr_back[0].item_id == "q_10.2"
print("PASS  mdio corrections round trip")

# --- unbalanced containers must fail ---------------------------------------
try:
    _parse(":::question{number=\"1\"}\nhello\n".splitlines())
except TagError as exc:
    print(f"PASS  unbalanced container rejected: {exc}")
else:
    raise AssertionError("unbalanced container slipped through")

# --- manifest ----------------------------------------------------------------
with tempfile.TemporaryDirectory() as td:
    src = Path(td) / "chapter.en.pdf"
    src.write_bytes(b"%PDF-fake")
    hashes = manifest.input_hashes(src)
    assert hashes == {"chapter.en.pdf": hashes["chapter.en.pdf"]} and len(hashes["chapter.en.pdf"]) == 16
    assert not manifest.unchanged_since(td, "mathpix", src)
    manifest.append(td, "mathpix", inputs=hashes, counts={"pages": 12},
                     gate_results={"counts": []}, model_calls=0)
    assert manifest.unchanged_since(td, "mathpix", src)
    src.write_bytes(b"%PDF-fake-edited")
    assert not manifest.unchanged_since(td, "mathpix", src)
    entries = json.loads((Path(td) / "manifest.json").read_text(encoding="utf-8"))
    assert len(entries) == 1 and entries[0]["stage"] == "mathpix" and entries[0]["gates_passed"] == ["counts"]
print("PASS  manifest (hash, append, unchanged_since)")

print("\nAll deterministic stages OK.")
