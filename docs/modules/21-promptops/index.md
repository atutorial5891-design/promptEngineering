---
tags:
  - L5
  - production
---

# 21. PromptOps: Versioning, Caching, Cost, Observability

!!! abstract "At a glance"
    **Level:** L5 · **Status:** stub · **Last reviewed:** 2026-10-07
    **Prerequisites:** [18](../18-evaluation/index.md) · **Lab:** `labs/21_promptops/`

!!! note "Stub module"
    The outline, references, and checklist are ready. As you study, expand each section using the [module template](../../templates/module-design-doc.md), add good/bad prompt examples, and change the status to `draft`, then `complete`.

## 1. Why it matters

Prompts in production are code: they need versions, reviews, tests, rollbacks, monitoring, and cost control. PromptOps is the discipline that keeps prompt changes safe and cheap.

## 2. Core concepts (outline)

- Prompts as versioned artifacts (files in git or a prompt registry), with IDs and changelogs
- Eval gates in CI for prompt and model changes
- Prompt caching: stable prefix first; measure cache hit rate
- Cost/latency levers: model routing, effort settings, output length, batching
- Tracing and observability: inputs, outputs, tool calls, tokens, latency per span
- Model upgrades: re-run evals, re-tune effort, diff behaviors

## 3. Architecture / flow

```mermaid
flowchart LR
  Edit[Edit prompt] --> PR[Pull request]
  PR --> CI[Eval suite in CI]
  CI -->|pass| Deploy[Deploy version]
  Deploy --> Trace[Tracing + monitoring]
  Trace --> Analyze[Error analysis]
  Analyze --> Edit
```

## 4. Prompt patterns

*To write: add at least one bad vs. good prompt pair from your own experiments.*

## 5. Failure modes and mitigations

| Failure mode | Symptom | Mitigation |
| --- | --- | --- |
| Untracked prompt edits | Silent regressions | Prompts in version control; eval gate |
| Cache-busting dynamic prefix | No caching savings | Move dynamic content after static prefix |
| Silent model upgrade | Behavior drift | Pin model versions; re-run evals on upgrade |

## 6. How to evaluate it

Track cost per successful task, p95 latency, cache hit rate, regression pass rate over time.

## 7. Lab and exercises

- Lab: `labs/21_promptops/`
- Add Langfuse (or Phoenix) tracing to a lab; add a CI job that runs the lab 03 eval and fails below a threshold.

## 8. Model-specific notes

| Provider | Notes |
| --- | --- |
| Anthropic (Claude) | *to fill* |
| OpenAI (GPT) | *to fill* |
| Google (Gemini) | *to fill* |
| Open models | *to fill* |

## 9. Must-read references

- [Langfuse](https://langfuse.com/)
- [Arize Phoenix](https://arize.com/phoenix/)
- [Anthropic: Prompt caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)
- [OpenAI: Prompt caching](https://developers.openai.com/api/docs/guides/prompt-caching)
- [Applied LLMs](https://applied-llms.org/)

## 10. Tutorials covering this module

- Udemy Bootcamp - production Python sections
- AI Engineer talks on LLMOps (YouTube)

## 11. Key takeaways (flashcards)

??? question "How to maximize prompt cache hits?"
    Keep a stable static prefix first; place dynamic content at the end.

??? question "What must happen on a model upgrade?"
    Re-run evals, re-tune effort/settings, and compare behavior before switching.

## 12. Mastery checklist

- [ ] I can explain this to someone else without notes
- [ ] I ran the lab and recorded results in the journal
- [ ] I can name two failure modes and how to detect them
- [ ] I applied it to a new task outside the lab
- [ ] I expanded this stub to `complete`
