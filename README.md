# Prompt Engineering Mastery

A private, docs-first learning hub. It holds:

- the prompt engineering learning path (levels L0 to L5)
- design docs for 25 modules
- architecture diagrams
- curated study materials and course notes
- small Python labs

The docs are published as a private MkDocs Material site.

> This is a learning repo. Real projects live in a separate account.

## Quick start

```bash
uv sync                          # creates .venv with docs + labs + dev deps
uv run mkdocs serve              # preview site at http://127.0.0.1:8000
cp .env.example .env             # add API keys only for the providers you use
uv run python labs/03_few_shot/run.py   # run a lab
uv run pytest                    # smoke tests for the helper library
```

## Layout

| Path | Purpose |
| --- | --- |
| `docs/` | Everything that becomes the website: learning path, modules, architectures, patterns, tutorials, resources, reference, journal |
| `docs/templates/` | Templates for module design docs, prompt cards, and course notes |
| `src/pem/` | Tiny helper library for labs: provider-agnostic LLM calls, prompt templates, evals |
| `labs/` | Runnable exercises. Folder numbers match the module numbers |
| `prompts/` | Versioned library of reusable prompts (YAML) |
| `evals/datasets/` | Small golden datasets used by labs |
| `scripts/new_module.py` | Scaffolds a new module doc (and lab folder) from the template |
| `.github/workflows/docs.yml` | CI: strict site build + link check |

## Common tasks

```bash
# New module (creates docs/modules/26-my-topic/index.md and labs/26_my_topic/)
uv run python scripts/new_module.py 26 "My Topic"

# New journal entry: copy docs/journal/entry-template.md to docs/journal/YYYY-MM-DD-topic.md

# Build static site into site/
uv run mkdocs build --strict
```

## Private deployment

The default is local only, using `uv run mkdocs serve`. To host the site, build it with `uv run mkdocs build`, then choose one option:

- **Cloudflare Pages + Cloudflare Access (free, fully private):**
    1. Run `npx wrangler pages deploy site --project-name prompt-engineering-mastery`.
    2. In the Cloudflare Zero Trust dashboard, add an Access application for the `*.pages.dev` domain. Use a policy that allows only your email.
- **Vercel:**
    1. Run `vercel deploy --prod` from the repo root. `vercel.json` installs MkDocs, builds the site, and serves the `site/` folder.
    2. Turn on Deployment Protection (Vercel Authentication).
    - Note: on the free Hobby plan, Standard Protection doesn't cover the production domain. Protecting every deployment needs a paid plan, so check the current plan rules.

GitHub Pages isn't recommended because Pages sites are public, even for private repos, on non-Enterprise plans.

## Secrets

- API keys go only in `.env`, which is git-ignored.
- Labs never run during the site build.
