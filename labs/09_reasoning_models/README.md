# Lab 09: Prompting Reasoning Models

Module doc: `docs/modules/09-reasoning-models/index.md`

## Task

Take a long legacy prompt, simplify it to outcome-first, and compare on evals across effort levels.

## Suggested structure

- `run.py`: the experiment, using `pem.llm`, `pem.prompts`, and `pem.evals`
- `prompts/`: prompt variants (YAML) or a reference to the top-level `prompts/`
- `outputs/`: run results (git-ignored)

See `labs/03_few_shot/` for a complete working example.
