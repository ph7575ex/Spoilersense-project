import csv
import sys
from pathlib import Path

# Let this script import from ../detection
sys.path.append(str(Path(__file__).resolve().parents[1]))

from detection.rules import load_spoiler_phrases
from detection.classifier import classify_text


def load_samples(csv_path):
    rows = []
    with open(csv_path, "r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append({
                "label": row["label"].strip(),
                "text": row["text"].strip()
            })
    return rows


def main():
    # TODO: later load this from extension settings
    watchlist = ["The Last of Us", "Elden Ring", "Spider-Man"]

    phrases_file = Path(__file__).resolve().parents[1] / "detection" / "spoiler_phrases.txt"
    spoiler_phrases = load_spoiler_phrases(phrases_file)

    samples_file = Path(__file__).resolve().parent / "samples.csv"
    samples = load_samples(samples_file)

    tp = fp = tn = fn = 0
    false_positives = []
    misses = []

    print("Running SpoilerSense Person B evaluation...")
    print(f"Samples: {len(samples)}")
    print(f"Watchlist: {watchlist}")
    print("-" * 60)

    for row in samples:
        label = row["label"]          # spoiler / not_spoiler
        text = row["text"]

        decision = classify_text(text, watchlist, spoiler_phrases, strictness="medium")
        predicted_flag = decision.action in ("WARN", "HIDE")
        actual_spoiler = (label == "spoiler")

        # Confusion matrix counts
        if actual_spoiler and predicted_flag:
            tp += 1
        elif (not actual_spoiler) and predicted_flag:
            fp += 1
            false_positives.append((decision, text))
        elif (not actual_spoiler) and (not predicted_flag):
            tn += 1
        elif actual_spoiler and (not predicted_flag):
            fn += 1
            misses.append((decision, text))

        # Debug print (good for prototype / professor sees it working)
        print(f"[{label}] -> {decision.action} (score={decision.score})")
        print(f"  {decision.explanation}")
        print(f"  Text: {text}")
        print()

    # Basic metrics
    precision = tp / (tp + fp) if (tp + fp) else 0
    recall = tp / (tp + fn) if (tp + fn) else 0

    # Write simple results file
    out_path = Path(__file__).resolve().parent / "results.md"
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("# SpoilerSense Evaluation Results (Person B)\n\n")
        f.write("## Summary\n")
        f.write(f"- TP: {tp}\n")
        f.write(f"- FP: {fp}\n")
        f.write(f"- TN: {tn}\n")
        f.write(f"- FN: {fn}\n")
        f.write(f"- Precision: {precision:.2f}\n")
        f.write(f"- Recall: {recall:.2f}\n\n")

        f.write("## False Positives (flagged but not spoiler)\n")
        if not false_positives:
            f.write("- None\n\n")
        else:
            for d, text in false_positives[:5]:
                f.write(f"- {d.action} | score={d.score} | {d.explanation}\n")
                f.write(f"  - Text: {text}\n")

        f.write("\n## Misses (spoilers not flagged)\n")
        if not misses:
            f.write("- None\n")
        else:
            for d, text in misses[:5]:
                f.write(f"- {d.action} | score={d.score} | {d.explanation}\n")
                f.write(f"  - Text: {text}\n")

        f.write("\n## Notes\n")
        f.write("- MVP rules are intentionally simple.\n")
        f.write("- TODO: add more samples and tune thresholds.\n")

    print("=" * 60)
    print("Done.")
    print(f"TP={tp}, FP={fp}, TN={tn}, FN={fn}")
    print(f"Precision={precision:.2f}, Recall={recall:.2f}")
    print(f"Results written to: {out_path}")


if __name__ == "__main__":
    main()