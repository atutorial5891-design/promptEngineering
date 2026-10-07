# Lab 25: Generative Media Prompting (Image and Video)

Module doc: `docs/modules/25-generative-media/index.md`

## Task

Build an LLM prompt-expander + judge loop for product images.

## Suggested structure

- `run.py`: the experiment, using `pem.llm`, `pem.prompts`, and `pem.evals`
- `prompts/`: prompt variants (YAML) or a reference to the top-level `prompts/`
- `outputs/`: run results (git-ignored)

See `labs/03_few_shot/` for a complete working example.
