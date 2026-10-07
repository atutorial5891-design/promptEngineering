# Lab 01: How LLMs Work

Module doc: `docs/modules/01-how-llms-work/index.md`

## Task

Sampling experiment: run one prompt 10 times at several temperatures and count unique outputs; compare token counts across languages and formats; compare a reasoning vs. non-reasoning model on a multi-step problem.

## Suggested structure

- `run.py`: the experiment, using `pem.llm`, `pem.prompts`, and `pem.evals`
- `prompts/`: prompt variants (YAML) or a reference to the top-level `prompts/`
- `outputs/`: run results (git-ignored)

See `labs/03_few_shot/` for a complete working example.
