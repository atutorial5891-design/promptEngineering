# Lab 03: Zero-Shot vs. Few-Shot

Module doc: `docs/modules/03-few-shot/index.md`

This lab compares `prompts/sentiment.zero_shot.v1.yaml` with `prompts/sentiment.few_shot.v1.yaml` on `evals/datasets/sentiment.jsonl`. The dataset has 30 reviews, including sarcasm and mixed cases.

```bash
uv run python labs/03_few_shot/run.py --dry-run          # show rendered prompts, no API calls
uv run python labs/03_few_shot/run.py                    # uses PEM_MODEL from .env
uv run python labs/03_few_shot/run.py --model ollama/llama3.1 --limit 10
```

The lab prints accuracy and per-label recall for each variant and the reviews it got wrong. It saves full results to `labs/03_few_shot/outputs/` (git-ignored).

## Exercises

1. **Add a misleading example:** put a wrong-label example into a copy of the few-shot prompt (`v2`). How much does accuracy drop?
2. **Test order bias:** reverse the example order. Does the last example's label get predicted more often?
3. **Try a reasoning model:** run both variants on a reasoning model and on a small model. Which one benefits more from the examples?
4. **Log it:** write up the results with `docs/journal/entry-template.md`.
