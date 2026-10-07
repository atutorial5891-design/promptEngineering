# Lab 21: PromptOps: Versioning, Caching, Cost, Observability

Module doc: `docs/modules/21-promptops/index.md`

## Task

Add Langfuse (or Phoenix) tracing to a lab; add a CI job that runs the lab 03 eval and fails below a threshold.

## Suggested structure

- `run.py`: the experiment, using `pem.llm`, `pem.prompts`, and `pem.evals`
- `prompts/`: prompt variants (YAML) or a reference to the top-level `prompts/`
- `outputs/`: run results (git-ignored)

See `labs/03_few_shot/` for a complete working example.
