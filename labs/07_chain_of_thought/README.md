# Lab 07: Chain-of-Thought and Step-Back Prompting

Module doc: `docs/modules/07-chain-of-thought/index.md`

## Task

Run GSM8K-style word problems: direct answer vs. zero-shot CoT vs. step-back, across two model types.

## Suggested structure

- `run.py`: the experiment, using `pem.llm`, `pem.prompts`, and `pem.evals`
- `prompts/`: prompt variants (YAML) or a reference to the top-level `prompts/`
- `outputs/`: run results (git-ignored)

See `labs/03_few_shot/` for a complete working example.
