# Lab 11: RAG Prompt Design and Hallucination Control

Module doc: `docs/modules/11-rag-and-grounding/index.md`

## Task

Grounded Q&A over a small doc set with citations; include 30% unanswerable questions and measure correct abstention.

## Suggested structure

- `run.py`: the experiment, using `pem.llm`, `pem.prompts`, and `pem.evals`
- `prompts/`: prompt variants (YAML) or a reference to the top-level `prompts/`
- `outputs/`: run results (git-ignored)

See `labs/03_few_shot/` for a complete working example.
