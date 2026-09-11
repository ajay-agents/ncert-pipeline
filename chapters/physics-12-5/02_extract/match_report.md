# Match report — physics-12-5 exercises

**Not produced by `match.join_solutions()`** — a plain number-match would
have been badly wrong for this chapter, worse than any prior case. The
current rationalised chapter has only 7 exercises (5.1-5.7). The solutions
manual's own "अभ्यास प्रश्न" section numbers प्रश्न 1-25 — a whole earlier
edition's worth of content, most of it on topics (Earth's magnetism, the
hysteresis/domain "अतिरिक्त प्रश्न" set, Curie's-law paramagnetism, a
Rowland ring, electron orbital/spin magnetic moment) that NCERT's 2023-24
rationalisation removed from this chapter entirely. Only 7 of the 25
solutions-manual entries have any home in the current chapter at all, and
they are not even a contiguous run — प्रश्न 1-2 precede the first real
match, प्रश्न 9-11 are inserted between two real matches, and प्रश्न 13-25
are all orphaned after the last real match.

`match.norm_num()` would additionally have made a silent wrong-pairing
actively worse here, not just missed a mismatch: the solutions manual's
own numbers are bare ("1", "2", "3"...), so `norm_num(raw, chapter='5')`
prepends the chapter number to any number with no "." in it — प्रश्न 3
normalises to "5.3", प्रश्न 4 to "5.4", and so on. That would have
collided प्रश्न 3 (a bar-magnet torque question, the real match for
q_5.1) with the chapter's own exercise 5.3 (a solenoid question) purely
because both normalise to the id "5.3" - a wrong pairing `needs_review`
would never have flagged, since every number "matched" something.

Every pairing below was verified by direct content comparison (numeric
values, not just position) before merging - see the coordinator's own
build script (`extract_ch5.py`) and the stage manifest note.

| chapter exercise | solutions manual entry | content check |
|---|---|---|
| q_5.1 | प्रश्न 3 | 0.25T field, 30°, torque 4.5e-2 J - confirmed directly against the solutions PDF page (page 94), which prints "4.5e-2 J" clearly; mathpix's own OCR transcription of that same question-restatement text read "45e-2 J" (a dropped decimal point introduced by OCR, not present in the source), but that text was never carried into any extracted field, so no correction is needed - matches |
| q_5.2 | प्रश्न 4 | m=0.32 JT⁻¹, 0.15T field, stable/unstable equilibrium energies - matches |
| q_5.3 | प्रश्न 5 | solenoid, 800 turns, 2.5e-4 m², 3.0A - matches |
| q_5.4 | प्रश्न 6 | same solenoid (references "प्रश्न 5" = this document's own प्रश्न 5), 0.25T at 30° - matches |
| q_5.5 | प्रश्न 7 | m=1.5 JT⁻¹, 0.22T field, work + torque at perpendicular/antiparallel - matches |
| q_5.6 | प्रश्न 8 | solenoid, 2000 turns, 1.6e-4 m², 4.0A, hung horizontally - matches |
| q_5.7 | प्रश्न 12 | m=0.48 JT⁻¹, point 10cm from centre, axial + equatorial field - matches |

**Orphan solutions, discarded per Rule 5 (nothing invented)** — 18 of the
25 solutions-manual entries, none of them present anywhere in this
rationalised chapter:
- प्रश्न 1, 2 — Earth's magnetism conceptual questions (dip angle,
  declination, geomagnetic field source) — the entire "Earth's magnetism"
  topic was cut from this chapter in the 2023-24 rationalisation.
- प्रश्न 9, 10, 11 — a circular-coil oscillation/moment-of-inertia problem
  and two more Earth's-magnetism numeric problems (dip angle → total
  field; South African declination/dip) — inserted between the real
  matches for q_5.6 and q_5.7, the same "scattered insertion" pattern
  documented for physics-12-3, not just a trailing block this time.
- प्रश्न 13-15 — more Earth's-magnetism neutral-point/oscillation problems.
- प्रश्न 16-17 (the "अतिरिक्त प्रश्न" heading in the solutions manual) —
  conceptual dia/para/ferromagnetism and hysteresis-loop questions.
- प्रश्न 18-21 — more Earth's-magnetism numeric problems (neutral point
  under a current-carrying cable, telephone-cable field, tangent
  galvanometer, dipole in two fields).
- प्रश्न 22-25 — electron-beam deflection in a magnetic field, a
  paramagnetic-salt Curie's-law problem, a Rowland ring, and the
  classical/quantum electron magnetic-moment derivation.

All 18 are genuine curriculum cuts (confirmed against the chapter's own
mathpix text, which has no Earth's-magnetism section, no additional-
exercises block, and stops at exercise 5.7), not extraction gaps — left
untouched per Rule 5, never invented into the current chapter.

needs_review: none (every pairing resolved by direct content verification
before this report was written, not deferred; only_en/only_hi/kind_mismatch
do not apply — Hindi-only chapter).
