# Lab 13: Multimodal Prompting

Module doc: `docs/modules/13-multimodal/index.md`

## Task

Extract structured data (invoice fields, chart values) from images using a Pydantic schema.

## Suggested structure

- `run.py`: the experiment, using `pem.llm`, `pem.prompts`, and `pem.evals`
- `prompts/`: prompt variants (YAML) or a reference to the top-level `prompts/`
- `outputs/`: run results (git-ignored)

See `labs/03_few_shot/` for a complete working example.
