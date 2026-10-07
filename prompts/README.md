# Prompt Library

Versioned, reusable prompts stored as YAML and loaded with `pem.prompts.load_prompt("<file stem>")`.

## Conventions

- **File name:** `<domain>.<task>.v<N>.yaml`. The `id` field must match the file stem.
- **Never edit a prompt that's in use.** Copy it to `v<N+1>` and record the change in its prompt card (see `docs/templates/prompt-card.md`).
- **Fields:**
    - `id`, `description`, and `variables` are required.
    - `system` is optional.
    - `user` is required, and uses Jinja2 with strict undefined variables.

| ID | Task | Used by |
| --- | --- | --- |
| `sentiment.zero_shot.v1` | 3-way sentiment, zero-shot baseline | `labs/03_few_shot` |
| `sentiment.few_shot.v1` | 3-way sentiment with label definitions and examples | `labs/03_few_shot` |
