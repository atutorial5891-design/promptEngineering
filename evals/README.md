# Evals

Small golden datasets for the labs, in JSONL format with one example per line. Each example has an `id`, an `input`, and gold fields such as `label`.

| Dataset | n | Used by | Notes |
| --- | --- | --- | --- |
| `datasets/sentiment.jsonl` | 30 | lab 03 | 3 labels, balanced. Includes sarcasm and mixed cases. Keep it separate from the few-shot examples |

**Rules:**

- Never reuse eval items as prompt examples.
- Add the hard cases you find in production or in labs.
- Version a dataset when its labels change, e.g. `sentiment.v2.jsonl`.
