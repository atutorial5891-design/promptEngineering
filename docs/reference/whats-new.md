# What's New (Changelog of the Field)

Prompting advice is tied to specific model generations. Log changes here monthly, then update the affected modules and their "Last reviewed" dates.

**Entry format:** date, what changed, the source, which modules are affected, and the action taken.

## 2026

| Date | Change | Source | Modules | Action |
| --- | --- | --- | --- | --- |
| 2026-10 | OpenAI GPT-6 family (Astra, Sol, Luna; GPT-6.1 Sol) released, with a new model guide | [OpenAI](https://openai.com/index/gpt-6-astra/) | 09, 15, 23 | Re-read the per-model prompt guidance. Re-run the effort sweep |
| 2026-09 | Google announces Gemini 4 Argon (limited rollout), citing robustness to indirect prompt injection | [Google blog](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/) | 09, 20 | Watch for developer availability |
| 2026 | Reasoning-first prompting is now the norm. All three major providers expose an effort or thinking-level control and restrict sampling parameters while thinking | Provider docs ([Official guides](../resources/official-guides.md)) | 01, 07, 09 | Modules 01 and 09 reflect this |
| 2025-09 | Anthropic publishes "Effective context engineering for AI agents". "Context engineering" becomes the standard framing | [Anthropic](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) | 10, 12 | Module 10 is built around it |

!!! note
    Verify model names and parameters against the official docs before relying on them. This table is a reading list, not a spec.

## Monthly review routine

1. Check the changelogs and prompting guides from Anthropic, OpenAI, and Google.
2. Add rows above.
3. For each affected module, update its model-specific notes and its "Last reviewed" date.
4. Re-run one lab on the newest model, and write a journal entry about any difference.
