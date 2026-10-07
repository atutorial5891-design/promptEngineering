# Lab 19: Automatic Prompt Optimization

Module doc: `docs/modules/19-prompt-optimization/index.md`

## Task

Optimize the lab 03 classifier with DSPy (BootstrapFewShot, then MIPROv2) and compare to your best manual prompt.

## Suggested structure

- `run.py`: the experiment, using `pem.llm`, `pem.prompts`, and `pem.evals`
- `prompts/`: prompt variants (YAML) or a reference to the top-level `prompts/`
- `outputs/`: run results (git-ignored)

See `labs/03_few_shot/` for a complete working example.
