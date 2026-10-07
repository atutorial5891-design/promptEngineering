# AGENTS.md

These are instructions for AI coding agents working in this repo. It's a private, docs-first learning hub for prompt engineering. Real projects live elsewhere.

## Commands

```bash
uv sync                          # install
uv run mkdocs serve              # preview the site
uv run mkdocs build --strict     # must pass before committing
uv run pytest && uv run ruff check .
```

## Conventions

- **Module docs** live in `docs/modules/NN-slug/index.md`.
    - Each one follows `docs/templates/module-design-doc.md`, with all 12 sections in order.
    - Create new modules with `scripts/new_module.py`. Then add each one to `docs/modules/.nav.yml`, `docs/modules/index.md`, and `docs/learning-path/progress.md`.
    - When you edit a module, update its "Last reviewed" date and status (`stub`, `draft`, or `complete`).
- **Navigation** is controlled by the `.nav.yml` file in each docs folder (awesome-nav).
- **Prompts** live in `prompts/` as YAML. The `id` must equal the file stem. Never edit a version that's in use; create `vN+1` instead.
- **Eval data** lives in `evals/datasets/`. Never reuse eval items as few-shot examples. A test enforces this for the sentiment lab.
- **Lab folders** match module numbers: `labs/NN_slug/`.
- **Links:**
    - Link to official docs and arXiv `abs` pages.
    - Verify that links resolve. CI runs lychee weekly.
    - Model names and API parameters change fast. Note the date, and log changes in `docs/reference/whats-new.md`.
- **Secrets:** never put API keys anywhere except `.env`, which is git-ignored.
