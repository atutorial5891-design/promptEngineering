# Lab 20: Prompt Security

Module doc: `docs/modules/20-prompt-security/index.md`

## Task

Build a summarizer that reads 'emails' containing injected instructions; measure attack success; add layered defenses.

## Suggested structure

- `run.py`: the experiment, using `pem.llm`, `pem.prompts`, and `pem.evals`
- `prompts/`: prompt variants (YAML) or a reference to the top-level `prompts/`
- `outputs/`: run results (git-ignored)

See `labs/03_few_shot/` for a complete working example.
