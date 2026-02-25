from dataclasses import dataclass
import re

# Simple word tokenizer for MVP
WORD_RE = re.compile(r"[A-Za-z0-9']+")


@dataclass
class ScoreResult:
    matched_titles: list
    matched_phrases: list
    proximity_bonus: int
    score: int


def clean_text(text: str) -> str:
    """Lowercase + collapse spaces."""
    return re.sub(r"\s+", " ", text.strip().lower())


def get_words(text: str) -> list:
    """Return a simple list of words."""
    return [m.group(0).lower() for m in WORD_RE.finditer(text)]


def find_title_matches(text_clean: str, watchlist: list) -> list:
    matches = []
    for title in watchlist:
        t = title.strip().lower()
        if t and t in text_clean:
            matches.append(title)
    return matches


def find_phrase_matches(text_clean: str, spoiler_phrases: list) -> list:
    matches = []
    for phrase in spoiler_phrases:
        p = phrase.strip().lower()
        if p and p in text_clean:
            matches.append(phrase)
    return matches


def simple_proximity_bonus(words: list, title_matches: list, phrase_matches: list) -> int:
    """
    Very simple MVP proximity check:
    - Looks at first word of a matched title and first word of a matched phrase.
    - If they appear within ~12 words, adds a bonus.
    """
    if not title_matches or not phrase_matches:
        return 0

    title_first_words = []
    for t in title_matches:
        parts = get_words(t)
        if parts:
            title_first_words.append(parts[0])

    phrase_first_words = []
    for p in phrase_matches:
        parts = get_words(p)
        if parts:
            phrase_first_words.append(parts[0])

    bonus_hits = 0

    for i, w in enumerate(words):
        if w in title_first_words:
            for j, other in enumerate(words):
                if other in phrase_first_words and abs(i - j) <= 12:
                    bonus_hits += 1

    # Keep bonus small so score doesn't explode
    if bonus_hits > 0:
        return min(10 * bonus_hits, 20)
    return 0


def score_text(text: str, watchlist: list, spoiler_phrases: list, strictness: str = "medium") -> ScoreResult:
    """
    MVP scoring (easy to explain in class):
    - +40 if any protected title is found
    - +15 for each spoiler phrase found (cap)
    - +proximity bonus if title + phrase are near each other
    - strictness changes score slightly
    """
    text_clean = clean_text(text)
    words = get_words(text)

    title_matches = find_title_matches(text_clean, watchlist)
    phrase_matches = find_phrase_matches(text_clean, spoiler_phrases)

    score = 0

    # Main signal: mention of protected title
    if title_matches:
        score += 40

    # Spoiler phrase signal
    score += min(len(phrase_matches) * 15, 30)

    # Bonus if title + spoiler phrase appear close together
    prox_bonus = simple_proximity_bonus(words, title_matches, phrase_matches)
    score += prox_bonus

    # Strictness tuning (simple)
    strictness = (strictness or "medium").lower()
    if strictness == "low":
        score -= 10
    elif strictness == "high":
        score += 10

    # Keep score in 0-100 range
    score = max(0, min(score, 100))

    return ScoreResult(
        matched_titles=title_matches,
        matched_phrases=phrase_matches,
        proximity_bonus=prox_bonus,
        score=score
    )