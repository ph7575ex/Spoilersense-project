from __future__ import annotations
from typing import List
from .scoring import MatchResult

def build_explanation(result: MatchResult) -> str:
    parts: List[str] = []
    if result.matched_titles:
        shown = result.matched_titles[:3]
        parts.append(f"Matched title(s): {', '.join(shown)}" + ("…" if len(result.matched_titles) > 3 else ""))
    if result.matched_phrases:
        shown = result.matched_phrases[:3]
        parts.append(f"Matched spoiler phrase(s): {', '.join(shown)}" + ("…" if len(result.matched_phrases) > 3 else ""))
    if result.proximity_hits:
        parts.append(f"Proximity signal: {result.proximity_hits} nearby hit(s)")
    parts.append(f"Risk score: {result.score}/100")
    return " | ".join(parts)
