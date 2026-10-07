# Lab 02: Anatomy of a Prompt

Module doc: `docs/modules/02-prompt-anatomy/index.md`

## Task

Ablation: run the incident-summary prompt from the module with one component removed at a time and score each variant.

## Suggested structure

- `run.py`: the experiment, using `pem.llm`, `pem.prompts`, and `pem.evals`
- `prompts/`: prompt variants (YAML) or a reference to the top-level `prompts/`
- `outputs/`: run results (git-ignored)

See `labs/03_few_shot/` for a complete working example.
