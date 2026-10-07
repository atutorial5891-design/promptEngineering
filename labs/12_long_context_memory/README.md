# Lab 12: Long Context and Memory Strategies

Module doc: `docs/modules/12-long-context-memory/index.md`

## Task

Q&A over a 100+ page document: full-context vs. map-reduce vs. RAG - accuracy and cost.

## Suggested structure

- `run.py`: the experiment, using `pem.llm`, `pem.prompts`, and `pem.evals`
- `prompts/`: prompt variants (YAML) or a reference to the top-level `prompts/`
- `outputs/`: run results (git-ignored)

See `labs/03_few_shot/` for a complete working example.
