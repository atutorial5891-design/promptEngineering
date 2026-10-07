# Official Guides

Provider docs change with every model release. Re-read the relevant guide whenever you switch models, and log what changed in [What's new](../reference/whats-new.md).

## Anthropic (Claude)

| Guide | Modules | Why |
| --- | --- | --- |
| [Prompt engineering overview](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview) | 02-07 | The canonical technique list: clarity, examples, XML tags, chaining, thinking |
| [Claude prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices) | 04, 09, 15 | How newer models follow instructions more literally, and the shifts that follow from that |
| [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) | 06, 15 | **Essential.** Workflows vs. agents, the five workflow patterns, and "start simple" |
| [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) | 10, 12 | **Essential.** Context as a finite resource, compaction, note-taking, sub-agents, just-in-time retrieval |
| [Writing effective tools for agents](https://www.anthropic.com/engineering/writing-tools-for-agents) | 14 | Tool naming, descriptions, response design, and evaluating tools |
| [How we built our multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system) | 17 | An orchestrator-worker case study, with lessons on prompting sub-agents |
| [Equipping agents with Agent Skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills) | 16, 23 | Progressive disclosure, and packaging instructions as skills |
| [Claude Code best practices](https://code.claude.com/docs/en/best-practices) | 23 | CLAUDE.md, planning before coding, verification loops |
| [Contextual retrieval](https://www.anthropic.com/engineering/contextual-retrieval) | 11 | A retrieval improvement that works by adding context to chunks before embedding them |
| [Interactive tutorial and courses](../tutorials/free-courses.md#anthropic-prompt-engineering-interactive-tutorial) | 02-07 | Hands-on notebooks |

## OpenAI (GPT)

| Guide | Modules | Why |
| --- | --- | --- |
| [Latest model guide (prompting guidance)](https://developers.openai.com/api/docs/guides/latest-model) | 04, 09 | Current guidance for each GPT model: outcome-first prompts, stopping conditions, when to use absolute rules |
| [Reasoning best practices](https://developers.openai.com/api/docs/guides/reasoning-best-practices) | 09 | When to pick reasoning models vs. GPT models, and how to prompt each |
| [GPT-5 prompting guide (Cookbook)](https://developers.openai.com/cookbook/examples/gpt-5/gpt-5_prompting_guide) | 09, 15, 23 | Agentic eagerness, reasoning effort, verbosity, and Cursor's prompt-tuning lessons |
| [Prompt optimizer cookbook](https://developers.openai.com/cookbook/examples/gpt-5/prompt-optimization-cookbook) | 19 | Fixing contradictions and format ambiguity, and migrating prompts between models |
| [Structured outputs](https://developers.openai.com/api/docs/guides/structured-outputs) | 05 | JSON-schema-constrained decoding |
| [A practical guide to building agents (PDF)](https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf) | 15, 20 | Agent design foundations, orchestration, and guardrails |

## Google (Gemini)

| Guide | Modules | Why |
| --- | --- | --- |
| [Prompt design strategies](https://ai.google.dev/gemini-api/docs/prompting-strategies) | 02-04, 13 | Gemini-specific structure, examples, and multimodal tips |
| [Prompt Engineering whitepaper (Lee Boonstra, Kaggle)](https://www.kaggle.com/whitepaper-prompt-engineering) | 02-08 | A thorough 60+ page overview of techniques, with best practices |

## Protocols and standards

| Guide | Modules | Why |
| --- | --- | --- |
| [Model Context Protocol](https://modelcontextprotocol.io/) | 16 | The spec, SDKs, and server examples |
| [AGENTS.md](https://agents.md/) | 23 | An open format for giving instructions to coding agents |
| [OWASP Top 10 for LLM Applications](https://genai.owasp.org/llm-top-10/) | 20 | The standard risk taxonomy. Prompt injection is LLM01 |
