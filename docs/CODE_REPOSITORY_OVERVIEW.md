# CODE REPOSITORY OVERVIEW — SpoilerSense (Person B)

## Purpose of this repository
This repository contains my initial code base for the SpoilerSense senior seminar project.
My responsibility is **Spoiler Detection & Privacy (Content Classification & Policy)**.

## What is implemented so far
1. **Spoiler risk scoring (rule-based):** combines user watchlist matches with spoiler-intent phrases.
2. **Policy engine:** maps a score to an action: `ALLOW`, `WARN`, or `HIDE`.
3. **Explainability:** generates a short “why blocked” explanation listing matched items.
4. **Evaluation harness:** runs the detector on labeled examples and outputs precision/recall plus error examples.
5. **Privacy documentation:** privacy notes and a brief threat model draft.

## How this code relates to SpoilerSense
SpoilerSense is a browser extension that hides suspected spoilers behind a consent card (“Reveal anyway?”).
The extension UI (Person A) needs a module that decides when to show that card. This repository provides
that decision logic: scoring, policy, and explanation output.

## Where my contribution is located
- Detection rules/scoring: `detection/`
- Evaluation: `evaluation/`
- Privacy/threat model: `docs/`

## How to run/test the current code
1. Install Python 3.10+
2. Run: `python evaluation/run_eval.py`
3. Review: `evaluation/results.md`

## Known limitations / next steps
- Current detection is rule-based (no ML).
- Dataset is small and will be expanded with more real examples from target sites.
- Next step is integration into a browser extension content script to score real DOM text blocks.
