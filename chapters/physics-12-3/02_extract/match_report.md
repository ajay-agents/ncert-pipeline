# Match report — physics-12-3 exercises

**Not produced by `match.join_solutions()`** — a plain number-match would
have been silently wrong for this chapter. The solutions manual's own
"अभ्यास प्रश्न" section numbers 1-13, but 4 of those (प्रश्न 3, 4, 10, 12)
are questions that do not exist in this rationalised chapter's own 9
exercises (3.1-3.9) at all - they are inserted WITHIN the main section,
not just appended at the end the way the usual "additional exercises"
mismatch works. Matching by number alone would have paired q_3.3 with
प्रश्न 3 (wrong content entirely - a resistors-in-series question, not the
room-temperature one) and every question from q_3.3 onward would have
been off by a growing offset.

Every pairing below was verified by direct content comparison (charge/
resistance/voltage values, not just number) before merging - see the
coordinator's own build script and manifest note for the verification.

| chapter exercise | solutions manual entry | content check |
|---|---|---|
| q_3.1 | प्रश्न 1 | car battery emf 12V, r=0.4 ohm - matches |
| q_3.2 | प्रश्न 2 | 10V battery, 3 ohm internal, 0.5A - matches |
| q_3.3 | प्रश्न 5 | room temp 27C, 100 ohm -> 117 ohm - matches |
| q_3.4 | प्रश्न 6 | 15m wire, 6.0e-7 m^2, 5.0 ohm - matches |
| q_3.5 | प्रश्न 7 | silver wire, 27.5C/2.1 ohm, 100C/2.7 ohm - matches |
| q_3.6 | प्रश्न 8 | nichrome, 230V, 3.2A -> 2.8A - matches |
| q_3.7 | प्रश्न 9 | network branch currents, चित्र - matches |
| q_3.8 | प्रश्न 11 | 8V battery, 0.5 ohm, 15.5 ohm, 120V dc - matches |
| q_3.9 | प्रश्न 13 | copper conductor, n=8.5e28, 3m wire - matches |

**Orphan solutions, discarded per Rule 5 (nothing invented)**: प्रश्न 3, 4,
10, 12 (extra questions within "अभ्यास प्रश्न" not present in this
rationalised chapter) and प्रश्न 14-24 (the entire "अतिरिक्त प्रश्न"
section) - 15 orphans total, matching this pipeline's established
"Rationalised edition has fewer exercises than its solutions manual"
pattern, just with a more scattered orphan distribution than previously
seen.

needs_review: none (every pairing resolved by direct verification before
this report was written, not deferred).
