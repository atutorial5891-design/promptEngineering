# Lab 22: Fine-Tuning vs. Prompting vs. RAG

Module doc: `docs/modules/22-finetune-vs-prompt-vs-rag/index.md`

## Task

Decision memo: pick one task, estimate cost/quality of each approach, and run the prompt and RAG variants.

## Suggested structure

- `run.py`: the experiment, using `pem.llm`, `pem.prompts`, and `pem.evals`
- `prompts/`: prompt variants (YAML) or a reference to the top-level `prompts/`
- `outputs/`: run results (git-ignored)

See `labs/03_few_shot/` for a complete working example.
