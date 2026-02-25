# Privacy Notes — SpoilerSense (Person B)

## Privacy goals
- **Local-only processing:** SpoilerSense should score page text on-device.
- **No content uploads:** No page text, URLs, or screenshots are sent to a server.
- **Data minimization:** Store only what is needed (watchlist + settings), not browsing history.
- **Least privilege:** Limit host permissions to user-selected sites whenever possible.

## Data processed (in scope)
- Visible page text blocks (headlines, snippets, titles, comment text) for scoring.
- User-provided watchlist titles and optional keywords.

## Data not collected (out of scope)
- Private messages, account passwords, form inputs, or keystrokes.
- Full-page captures or continuous screen recording.
- Any analytics about what the user reads, clicks, or watches.

## Storage plan
- Store watchlist and settings locally (extension storage).
- Optional: store per-title “allow” choices (e.g., “Always allow for this title”).

## Transparency
- The UI should include a short privacy statement: “Runs locally. No browsing content is uploaded.”
