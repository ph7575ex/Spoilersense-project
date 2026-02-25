# Spoilersense-project
**Role:** Person B — Spoiler Detection & Privacy (Content Classification & Policy)

This repository is my **initial code base** for the SpoilerSense senior seminar project.  
My responsibility is the **spoiler detection and privacy/policy side** of the project.

SpoilerSense is a browser extension that will hide likely spoiler content behind a warning card
(e.g., “Possible spoiler for [Title]. Reveal anyway?”). The full extension UI and browser integration are part of Siyeon Park role. This repository contains **my independent contribution**: the detection
logic, explainability output, privacy notes, and an evaluation harness.

## What is included in this bundle
- `detection/`  
  Rule-based spoiler detection logic (watchlist + spoiler-intent phrase matching + simple scoring)
- `evaluation/`  
  Sample labeled dataset and evaluation script (`run_eval.py`) for testing performance
- `docs/`  
  Repository overview, privacy notes, threat model, and online code/reference documentation
- `examples/`  
  Placeholder files for collecting future spoiler/non-spoiler samples from target sites

## What the current code does (MVP)
This initial version uses a simple rule-based approach:
- checks whether a user-protected title appears in the text
- checks whether spoiler-intent phrases appear (examples: “ending explained”, “dies”, “revealed”)
- adds a proximity bonus if title and spoiler phrase appear near each other
- calculates a score (0–100)
- returns one of three actions:
  - `ALLOW`
  - `WARN`
  - `HIDE`

The code also generates a short explanation of *why* a block was triggered.

## How to run the evaluation
Requirements: **Python 3.10+**

```bash
cd evaluation
python run_eval.py