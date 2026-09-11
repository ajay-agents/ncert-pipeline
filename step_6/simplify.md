# Stage 6 — language simplification prompt

Audience: Class 11–12 board and NEET/JEE aspirants, many in Hindi medium, many
reading a technical explanation in their second language.

Text arriving here has protected regions replaced by tokens like `⟦M3⟧`, `⟦T0⟧`.
**Reproduce every token exactly once, in a position where it still makes sense.**
Never edit a token, never drop one, never create one.

## Do

- Break long sentences into short ones.
- State what is being found before the working starts.
- Name the principle or formula being used at the step where it is used.
- Replace textbook register with plain register: "we obtain" becomes "we get".
- In Hindi: Devanagari for English technical terms, no hyphens, short
  sentences, active voice.
- Simplify each language against its own source solution, independently. Do
  not rewrite the Hindi text to mirror a change you just made to the English
  text, or vice versa — matching the two languages to each other is not the goal.

## Do not

- Do not touch question text — example or exercise, item-level or in a
  sub-part. It arrives unchanged and leaves unchanged either way. The
  *solution* may be simplified for both examples and exercises; the
  *question* is off limits for both.
- Do not touch figure captions. They are short factual labels tied to a
  specific textbook diagram, not explanatory prose — rewriting one risks
  losing a precise term, not gaining clarity.
- Do not change any number, unit, sign or final answer.
- Do not add a step that was not in the original working, even a correct one.
- Do not remove a step because it looks obvious.
- Do not add encouragement, study tips, mnemonics or commentary.
- Do not expand a one-line answer into a paragraph.
- Do not touch the container attrs (`id=`, `number=`, `kind=`,
  `verified=`, `simplified=`, `corrections_applied=`) or a `:::figure{...}`
  block's `src=`/`id=` — leave every container, heading and attribute you
  didn't rewrite exactly as given.

Length should stay within roughly 130% of the original. If a solution is
already clear, return it unchanged — that is a valid outcome and better than
churn.

**Reordering a comparative sentence ("X से Y कम/अधिक है" and its like) can
silently reverse which quantity the sentence is actually claiming, even
though not a single number or sign character changed.** Caught for real,
after the chapter had already gone all the way to final PDF: physics-12-2's
ex_2.3(a) originally read "$V_{A}$ से $V_{B}$ कम ऋणात्मक है" (V_B is less
negative than V_A) — correct, and consistent with the very next sentence's
stated conclusion ($V_B>V_A$). Stage 6 "simplified" this to "$V_{A}$,
$V_{B}$ से कम ऋणात्मक है" (V_A is less negative than V_B) — a small,
innocent-looking reordering of the same three tokens that flips which
quantity is which, producing a premise that directly contradicts the
conclusion sitting right next to it. Nothing here trips
`gate_answers_unchanged`/`gate_math_parity` (no number, unit or protected
token was touched) — this is a plain-language comparison, and the gates
have nothing to check it against. When rewording a sentence that compares
two named quantities (X vs Y, more/less, before/after), re-read the
rewritten sentence against **the conclusion or result it leads into**, not
just against the original wording in isolation — a locally-plausible
rephrasing can still reverse the relationship the surrounding solution
depends on.

Return the same container markdown you were given, with only the text
inside `:::solution` blocks (item-level and part-level) rewritten.
`:::answer` blocks are copied through unchanged — a boxed result is not
prose, and there is nothing in it to simplify. No preamble, no code fences.
