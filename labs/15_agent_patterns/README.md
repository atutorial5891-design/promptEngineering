# Lab 15: Agent Patterns

Module doc: `docs/modules/15-agent-patterns/index.md`

## Task

Implement a ReAct agent from scratch (no framework) with 2 tools; then the same task as a fixed chain - compare.

## Suggested structure

- `run.py`: the experiment, using `pem.llm`, `pem.prompts`, and `pem.evals`
- `prompts/`: prompt variants (YAML) or a reference to the top-level `prompts/`
- `outputs/`: run results (git-ignored)

See `labs/03_few_shot/` for a complete working example.
