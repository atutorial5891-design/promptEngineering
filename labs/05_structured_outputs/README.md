# Lab 05: Structured Outputs

Module doc: `docs/modules/05-structured-outputs/index.md`

## Task

Ticket triage with the TicketTriage Pydantic schema via pem.llm.complete_structured(); measure validity, field accuracy, and hallucinated-field rate.

## Suggested structure

- `run.py`: the experiment, using `pem.llm`, `pem.prompts`, and `pem.evals`
- `prompts/`: prompt variants (YAML) or a reference to the top-level `prompts/`
- `outputs/`: run results (git-ignored)

See `labs/03_few_shot/` for a complete working example.
