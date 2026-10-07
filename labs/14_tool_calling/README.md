# Lab 14: Tool Calling and Tool Design

Module doc: `docs/modules/14-tool-calling/index.md`

## Task

Build 3 tools (search notes, calculator, calendar stub) and measure tool-choice accuracy as you refine descriptions.

## Suggested structure

- `run.py`: the experiment, using `pem.llm`, `pem.prompts`, and `pem.evals`
- `prompts/`: prompt variants (YAML) or a reference to the top-level `prompts/`
- `outputs/`: run results (git-ignored)

See `labs/03_few_shot/` for a complete working example.
