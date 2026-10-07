# Lab 08: Advanced Reasoning: Self-Consistency, Tree of Thoughts, Self-Refine, Reflexion

Module doc: `docs/modules/08-advanced-reasoning/index.md`

## Task

Self-consistency voting on a reasoning set; self-refine loop on a writing task scored by an LLM judge.

## Suggested structure

- `run.py`: the experiment, using `pem.llm`, `pem.prompts`, and `pem.evals`
- `prompts/`: prompt variants (YAML) or a reference to the top-level `prompts/`
- `outputs/`: run results (git-ignored)

See `labs/03_few_shot/` for a complete working example.
