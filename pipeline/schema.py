"""Canonical data model. Every stage reads and writes this, never raw markdown."""
from __future__ import annotations

from typing import Literal, Optional
from pydantic import BaseModel, Field

Lang = Literal["en", "hi"]
Kind = Literal["example", "exercise", "additional_exercise"]


class Text(BaseModel):
    """A single field in both languages. Either side may be missing mid-pipeline."""
    en: Optional[str] = None
    hi: Optional[str] = None

    def get(self, lang: Lang) -> str:
        return getattr(self, lang) or ""

    def has_both(self) -> bool:
        return bool(self.en) and bool(self.hi)


class Figure(BaseModel):
    id: str                      # fig_10_4
    src: str                     # images/fig_10_4.png
    caption: Text = Field(default_factory=Text)


class Part(BaseModel):
    """Sub-part of a question: (a), (i), etc."""
    label: str
    question: Text = Field(default_factory=Text)
    solution: Text = Field(default_factory=Text)
    final_answer: Text = Field(default_factory=Text)


class SourceRef(BaseModel):
    chapter_pages: list[int] = Field(default_factory=list)
    solutions_pages: list[int] = Field(default_factory=list)


class Item(BaseModel):
    id: str                      # ex_10.1  |  q_10.3
    kind: Kind
    number: str                  # normalised: "10.3"
    question: Text = Field(default_factory=Text)
    # A short (2-6 word) descriptive label, e.g. "Mole fraction" — not printed
    # in the textbook, so not exam question text (Rule 4 doesn't apply) and
    # not checked against the PDF (stage 5 has no field to verify it against).
    # Written once at extraction, carried through unchanged after. See
    # CLAUDE.md's "Item topics" section.
    topic: Text = Field(default_factory=Text)
    parts: list[Part] = Field(default_factory=list)
    solution: Text = Field(default_factory=Text)
    final_answer: Text = Field(default_factory=Text)
    figures: list[Figure] = Field(default_factory=list)
    source: SourceRef = Field(default_factory=SourceRef)

    # provenance flags set by later stages
    verified: bool = False
    simplified: bool = False
    corrections_applied: int = 0


class Chapter(BaseModel):
    subject: Literal["physics", "chemistry", "maths", "biology"]
    class_level: int             # 11 or 12
    chapter_number: str          # "10"
    title: Text = Field(default_factory=Text)
    items: list[Item] = Field(default_factory=list)

    def by_kind(self, kind: Kind) -> list[Item]:
        return [i for i in self.items if i.kind == kind]

    def index(self) -> dict[str, Item]:
        return {i.id: i for i in self.items}


class Correction(BaseModel):
    """Stage 5 output. Applied programmatically — the model never rewrites files."""
    item_id: str
    lang: Lang
    field: str                   # "question" | "solution" | "final_answer" | "parts[0].solution"
    found: str
    should_be: str
    reason: str
    confidence: Literal["high", "medium", "low"]
