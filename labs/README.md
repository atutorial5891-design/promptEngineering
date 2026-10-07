# Labs

Each folder matches a module number in `docs/modules/`.

- `03_few_shot/` is a complete runnable example.
- The other folders hold a README with the task. Build each one out as you study that module.

```bash
uv sync
cp .env.example .env    # set PEM_MODEL and the provider key
uv run python labs/03_few_shot/run.py --dry-run
```

**Conventions:**

- Load prompts from `prompts/`. Don't hard-code them in scripts.
- Load data from `evals/datasets/`.
- Write results to `outputs/` (git-ignored).
- Log findings in `docs/journal/`.
- Capstones go in `labs/capstones/` (see `docs/capstones/index.md`).
