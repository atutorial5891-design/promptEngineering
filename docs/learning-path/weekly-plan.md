# 12-Week Plan

!!! tip "Shorter Architecture track"
    Prefer the five sprints in [Architect 20%](architect-20.md) if you only need role-aligned depth. Use this 12-week plan when you want the full catalog, including the deferred 80%.

The plan assumes about 6 to 8 hours a week:

- 2 to 3 hours of reading the module and its references
- 2 hours of tutorials
- 2 to 3 hours of labs and journaling

Stretch it as needed. Consistency beats speed.

!!! note "Tutorial picks"
    "Udemy core" means [The Complete Prompt Engineering for AI Bootcamp](../tutorials/udemy.md#the-complete-prompt-engineering-for-ai-bootcamp-2026).
    "Udemy agents" means [AI Engineer Agentic Track](../tutorials/udemy.md#ai-engineer-agentic-track-the-complete-agent-mcp-course).
    You can swap in any course from the [Tutorials](../tutorials/index.md) section.

| Week | Modules | Lab / deliverable | Tutorials |
| --- | --- | --- | --- |
| 1 | 01, 02 | Set up the repo and `.env`, then run the lab 01 sampling experiment | Karpathy "Intro to LLMs"; Anthropic interactive tutorial ch. 1-3 |
| 2 | 03 | Lab 03: zero-shot vs. few-shot on the sentiment dataset | DeepLearning.AI "ChatGPT Prompt Engineering for Developers"; Anthropic tutorial ch. 7 |
| 3 | 04 | Rewrite three weak prompts with XML structure and measure the difference | Udemy core: fundamentals and Five Principles; Anthropic tutorial ch. 4-5 |
| 4 | 05, 06 | Extraction chain with Pydantic validation | Udemy core: structured output sections |
| 5 | 07, 08 | Chain-of-thought vs. none vs. self-consistency on a reasoning set | Anthropic tutorial ch. 6; promptingguide.ai techniques |
| 6 | 09 | Effort sweep (low, medium, high) on one task: cost vs. accuracy | OpenAI prompt guidance; Claude prompting best practices. **Mid-point self-assessment** |
| 7 | 10, 11 | Grounded Q&A with citations and refusal | Anthropic "Effective context engineering"; Anthropic tutorial ch. 8 and appendix 10.3 |
| 8 | 12, 13 | Long-document Q&A; image-description prompt | DeepLearning.AI "Large Multimodal Model Prompting with Gemini" |
| 9 | 14, 15 | Build a ReAct agent from scratch, without a framework | Udemy agents: weeks 1-2; Anthropic "Building effective agents" |
| 10 | 16, 17 | MCP server plus one skill | Udemy agents: MCP week; Hugging Face Agents course |
| 11 | 18, 19 | Eval suite plus a DSPy optimization | DeepLearning.AI "Evaluating AI Agents" and "DSPy"; Hamel Husain's evals posts |
| 12 | 20, 21, 22 | Red-team your capstone; add tracing; **final self-assessment** | OWASP LLM Top 10; Simon Willison on prompt injection |

**Applied tracks (23-25):** do one week of these whenever a topic is directly useful for work.

**Capstones:**

- [Capstone A](../capstones/index.md#capstone-a-evaluated-support-bot) after week 7
- Capstone B after week 10
- Capstone C after week 11
