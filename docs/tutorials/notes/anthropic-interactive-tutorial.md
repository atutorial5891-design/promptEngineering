# Course Notes: Anthropic Prompt Engineering Interactive Tutorial

| Field | Value |
| --- | --- |
| **Platform / instructor** | GitHub notebooks (Anthropic) |
| **Link** | [anthropics/prompt-eng-interactive-tutorial](https://github.com/anthropics/prompt-eng-interactive-tutorial) |
| **Course last updated** | Written for Claude 3 Haiku. The principles are still valid |
| **Status** | planned |
| **Progress** | 0% |
| **Started / finished** | |

## One-paragraph summary

The best free hands-on introduction to the craft. Each chapter teaches one principle, shows a playground, and ends with graded exercises.

## Section notes (mapped to modules)

| Chapter | Key points | Module(s) |
| --- | --- | --- |
| 1. Basic prompt structure | | [02](../../modules/02-prompt-anatomy/index.md) |
| 2. Being clear and direct | | [04](../../modules/04-clarity-and-structure/index.md) |
| 3. Assigning roles | | [02](../../modules/02-prompt-anatomy/index.md) |
| 4. Separating data and instructions | | [04](../../modules/04-clarity-and-structure/index.md) |
| 5. Formatting output and speaking for Claude | | [05](../../modules/05-structured-outputs/index.md) |
| 6. Precognition (thinking step by step) | | [07](../../modules/07-chain-of-thought/index.md) |
| 7. Using examples | | [03](../../modules/03-few-shot/index.md) |
| 8. Avoiding hallucinations | | [11](../../modules/11-rag-and-grounding/index.md) |
| 9. Complex prompts (industry cases) | | [24](../../modules/24-task-playbooks/index.md) |
| 10.1 Chaining prompts | | [06](../../modules/06-prompt-chaining/index.md) |
| 10.2 Tool use | | [14](../../modules/14-tool-calling/index.md) |
| 10.3 Search and retrieval | | [11](../../modules/11-rag-and-grounding/index.md) |

## Prompts worth keeping

## Disagreements and outdated points

- **Prefilling the assistant turn:** newer Claude models may not support prefill in every configuration. Use structured outputs where they're available.
- **Explicit "think step by step":** for models with adaptive or extended thinking, use the thinking or effort setting instead.

## Follow-up labs and questions

- [ ] Redo chapter 7's exercises with `labs/03_few_shot` and measure the results
