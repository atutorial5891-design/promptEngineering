"""Lab 03: zero-shot vs. few-shot sentiment classification."""

from __future__ import annotations

import argparse
import json
from datetime import datetime
from pathlib import Path

from pem.evals import exact_match, load_jsonl, run_eval
from pem.prompts import load_prompt

ROOT = Path(__file__).resolve().parents[2]
DATASET = ROOT / "evals" / "datasets" / "sentiment.jsonl"
VARIANTS = ["sentiment.zero_shot.v1", "sentiment.few_shot.v1"]
OUTPUTS = Path(__file__).parent / "outputs"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--model", help="LiteLLM model string (default: $PEM_MODEL)")
    parser.add_argument("--limit", type=int, help="Only use the first N examples")
    parser.add_argument("--dry-run", action="store_true", help="Print rendered prompts; no API calls")
    args = parser.parse_args()

    dataset = load_jsonl(DATASET)[: args.limit]

    if args.dry_run:
        for variant in VARIANTS:
            messages = load_prompt(variant).render(review=dataset[0]["input"])
            print(f"=== {variant} ===")
            for m in messages:
                print(f"[{m['role']}]\n{m['content']}\n")
        return

    from pem.llm import complete

    OUTPUTS.mkdir(exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")

    for variant in VARIANTS:
        prompt = load_prompt(variant)
        report = run_eval(
            variant,
            dataset,
            predict=lambda ex, p=prompt: complete(p.render(review=ex["input"]), model=args.model),
            scorers={"accuracy": exact_match},
        )
        print(report.summary())
        for label, recall in report.per_label("accuracy").items():
            print(f"  recall[{label}] = {recall:.2f}")
        for row in report.failures("accuracy"):
            ex = row["example"]
            print(f"  x #{ex['id']} gold={ex['label']} got={row['output']!r}: {ex['input']}")
        (OUTPUTS / f"{stamp}-{variant}.json").write_text(json.dumps(report.rows, indent=2))


if __name__ == "__main__":
    main()
