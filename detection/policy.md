# SpoilerSense Detection Policy (Person B)

## Goal
Flag **likely spoilers** for user-protected titles with minimal false positives.

## Inputs
- `watchlist`: titles the user wants to protect (movies/shows/games)
- `text`: a visible text block from a web page (title, snippet, comment, etc.)

## Signals
1. **Watchlist match**
   - The text contains a protected title (or an alias/keyword pack in future work).
2. **Spoiler-intent match**
   - The text contains spoiler-intent phrases (e.g., “dies”, “ending explained”).
3. **Proximity**
   - If both signals appear within a close window (default ~12 words), risk increases.

## Output actions
- `ALLOW`: safe, do not modify content
- `WARN`: show consent card (“Possible spoiler… reveal?”)
- `HIDE`: hide content by default (strict mode)

## Default thresholds (tunable)
- `WARN` if title matched AND risk score >= 50
- `HIDE` if title matched AND risk score >= 75
