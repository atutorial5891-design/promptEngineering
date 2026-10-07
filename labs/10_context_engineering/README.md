# Lab 10: Context Engineering

Module doc: `docs/modules/10-context-engineering/index.md`

## Task

Needle-in-haystack and distractor experiment: measure accuracy as irrelevant context grows.

## Suggested structure

- `run.py`: the experiment, using `pem.llm`, `pem.prompts`, and `pem.evals`
- `prompts/`: prompt variants (YAML) or a reference to the top-level `prompts/`
- `outputs/`: run results (git-ignored)

See `labs/03_few_shot/` for a complete working example.
