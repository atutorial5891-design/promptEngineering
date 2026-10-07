# Lab 06: Prompt Chaining and Decomposition

Module doc: `docs/modules/06-prompt-chaining/index.md`

## Task

Build a 3-step chain: extract facts from a document -> verify against source -> write summary. Compare with a single prompt.

## Suggested structure

- `run.py`: the experiment, using `pem.llm`, `pem.prompts`, and `pem.evals`
- `prompts/`: prompt variants (YAML) or a reference to the top-level `prompts/`
- `outputs/`: run results (git-ignored)

See `labs/03_few_shot/` for a complete working example.
