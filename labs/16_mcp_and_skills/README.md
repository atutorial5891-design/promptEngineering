# Lab 16: MCP and Agent Skills

Module doc: `docs/modules/16-mcp-and-skills/index.md`

## Task

Build a tiny MCP server (Python SDK) exposing your prompts/ library; write one skill for 'create a prompt card'.

## Suggested structure

- `run.py`: the experiment, using `pem.llm`, `pem.prompts`, and `pem.evals`
- `prompts/`: prompt variants (YAML) or a reference to the top-level `prompts/`
- `outputs/`: run results (git-ignored)

See `labs/03_few_shot/` for a complete working example.
