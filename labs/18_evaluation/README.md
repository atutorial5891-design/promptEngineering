# Lab 18: Evaluation

Module doc: `docs/modules/18-evaluation/index.md`

## Task

Use pem.evals: build a rubric judge, label 30 outputs yourself, measure judge agreement, then run as regression.

## Suggested structure

- `run.py`: the experiment, using `pem.llm`, `pem.prompts`, and `pem.evals`
- `prompts/`: prompt variants (YAML) or a reference to the top-level `prompts/`
- `outputs/`: run results (git-ignored)

See `labs/03_few_shot/` for a complete working example.
