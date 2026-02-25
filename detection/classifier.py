from dataclasses import dataclass
from .scoring import score_text
from .explain import make_explanation


@dataclass
class Decision:
    action: str   # ALLOW / WARN / HIDE
    score: int
    explanation: str


def classify_text(text: str, watchlist: list, spoiler_phrases: list, strictness: str = "medium") -> Decision:
    """
    Simple policy:
    - If no title match -> ALLOW
    - Score >= 75 -> HIDE
    - Score >= 50 -> WARN
    - else ALLOW
    """
    result = score_text(text, watchlist, spoiler_phrases, strictness=strictness)

    # If no protected title is mentioned, do not flag
    if not result.matched_titles:
        action = "ALLOW"
    elif result.score >= 75:
        action = "HIDE"
    elif result.score >= 50:
        action = "WARN"
    else:
        action = "ALLOW"

    explanation = make_explanation(result)

    return Decision(
        action=action,
        score=result.score,
        explanation=explanation
    )