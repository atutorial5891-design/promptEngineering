# Tutorials and Courses

This is your space for video courses and structured tutorials: Udemy, Coursera, DeepLearning.AI, YouTube, and free courses. The [Modules](../modules/index.md) are the *source of truth*. Courses feed into them, and every course gets a notes file that maps its sections back to module numbers.

!!! warning "Course content ages quickly"
    Prompting advice from 2023 and 2024 courses ("always say *think step by step*", heavy role-play personas, temperature tricks) is often outdated for current reasoning models. Always check the **last updated** date. Record outdated points in the "Disagreements" section of your notes.

## How to use a course here

1. Pick a course from a platform page below. It shows which modules the course covers.
2. Copy the [course-notes template](../templates/course-notes.md) to `docs/tutorials/notes/<course-slug>.md`.
3. Add a row to the tracker below.
4. While you watch, map each section to a module, and put the best prompts into `prompts/`.

## Tracker

| Course | Platform | Paid | Covers modules | Status | Progress | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [Prompt Engineering Interactive Tutorial](free-courses.md#anthropic-prompt-engineering-interactive-tutorial) | GitHub (Anthropic) | Free (API key) | 02-07, 11, 14 | planned | 0% | [notes](notes/anthropic-interactive-tutorial.md) |
| [ChatGPT Prompt Engineering for Developers](deeplearning-ai.md) | DeepLearning.AI | Free | 03, 04, 24 | planned | 0% | |
| [The Complete Prompt Engineering for AI Bootcamp (2026)](udemy.md#the-complete-prompt-engineering-for-ai-bootcamp-2026) | Udemy | Paid | 02-06, 13, 15, 24, 25 | planned | 0% | [notes](notes/udemy-prompt-engineering-bootcamp.md) |
| [AI Engineer Agentic Track](udemy.md#ai-engineer-agentic-track-the-complete-agent-mcp-course) | Udemy | Paid | 14-17 | planned | 0% | |
| *(add your own courses here)* | | | | | | |

## Platforms

| Page | Best for |
| --- | --- |
| [Udemy](udemy.md) | Long, project-based video bootcamps (paid, often on sale) |
| [DeepLearning.AI](deeplearning-ai.md) | Short (1-2 hour) focused courses on one technique or tool, mostly free |
| [Coursera](coursera.md) | Structured university- and Google-backed specializations |
| [YouTube and talks](youtube.md) | Mental models, deep dives, conference talks |
| [Free courses and interactive tutorials](free-courses.md) | Hands-on notebooks from Anthropic, Microsoft, Hugging Face, and others |
| [Live cohorts](cohorts.md) | Expensive, intensive, instructor-led (e.g. AI evals) |

## Selection criteria

A course is listed here only if it meets these criteria:

- It's taught by a credible practitioner or the model provider.
- It was updated within the last 12 months, or it teaches fundamentals that don't age.
- It covers what matters in 2026: reasoning models, context engineering, agents, evals, and security. A course of only "ChatGPT tips" doesn't qualify.
- The link was checked when it was added. CI also link-checks the whole site.
