# Threat Model (Draft) — SpoilerSense (Person B)

## Assets to protect
- User browsing content (page text) and user watchlist (titles/keywords)
- User trust (avoid overclaiming and avoid silent data collection)

## Threats / risks
1. **Overbroad permissions** could allow reading more sites than intended.
2. **Data exfiltration** if the extension (or a dependency) makes network requests with page content.
3. **DOM injection issues** that break a page or create security risks (e.g., unsafe HTML insertion).
4. **False positives** that hide too much content and make the tool unusable.
5. **False negatives** that miss spoilers and reduce trust.

## Mitigations
- Least-privilege host permissions and clear per-site toggles.
- Local-only processing; no telemetry by default.
- Safe DOM handling (use text nodes; avoid innerHTML for untrusted content).
- Explainable blocking (“why blocked”) so users can understand decisions.
- Evaluation set + metrics; tune thresholds to reduce false positives.
