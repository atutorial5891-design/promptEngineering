# Lab 04: Clarity, Structure, and Delimiters

Module doc: `docs/modules/04-clarity-and-structure/index.md`

## Task

Rewrite three vague prompts with structure; measure rule violations across 20 runs; test question-first vs. question-last on a long document.

## Suggested structure

- `run.py`: the experiment, using `pem.llm`, `pem.prompts`, and `pem.evals`
- `prompts/`: prompt variants (YAML) or a reference to the top-level `prompts/`
- `outputs/`: run results (git-ignored)

See `labs/03_few_shot/` for a complete working example.
