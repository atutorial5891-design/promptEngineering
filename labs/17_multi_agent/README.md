# Lab 17: Multi-Agent Systems and Sub-Agent Prompts

Module doc: `docs/modules/17-multi-agent/index.md`

## Task

Orchestrator + 3 research sub-agents over local documents; compare to a single agent.

## Suggested structure

- `run.py`: the experiment, using `pem.llm`, `pem.prompts`, and `pem.evals`
- `prompts/`: prompt variants (YAML) or a reference to the top-level `prompts/`
- `outputs/`: run results (git-ignored)

See `labs/03_few_shot/` for a complete working example.
