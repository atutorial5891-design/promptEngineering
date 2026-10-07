# Tools

## Calling models

| Tool | Modules | Notes |
| --- | --- | --- |
| [LiteLLM](https://docs.litellm.ai/) | all labs | One interface for 100+ providers. The labs in this repo use it |
| [Ollama](https://ollama.com/) | 01, 22 | Run open models locally, free, for unlimited experiments |
| [Instructor](https://python.useinstructor.com/) | 05 | Pydantic-validated structured outputs with retries |

## Evaluation

| Tool | Modules | Notes |
| --- | --- | --- |
| [promptfoo](https://www.promptfoo.dev/) | 18, 20 | YAML-driven prompt evals and red-teaming. Good for CI |
| [DeepEval](https://deepeval.com/) | 18 | Pytest-style LLM evals with built-in metrics |
| [Inspect](https://inspect.aisi.org.uk/) | 18 | The UK AI Security Institute's eval framework. Rigorous and agent-friendly |

## Prompt optimization

| Tool | Modules | Notes |
| --- | --- | --- |
| [DSPy](https://dspy.ai/) | 19 | Program LLMs with signatures and modules, then optimize the prompts automatically |

## Observability and PromptOps

| Tool | Modules | Notes |
| --- | --- | --- |
| [Langfuse](https://langfuse.com/) | 21 | Open-source tracing, prompt management, and evals |
| [Arize Phoenix](https://phoenix.arize.com/) | 18, 21 | Open-source tracing and eval UI |
| [LangSmith](https://docs.smith.langchain.com/) | 21 | Tracing and datasets for the LangChain ecosystem |

## Security

| Tool | Modules | Notes |
| --- | --- | --- |
| [garak](https://github.com/NVIDIA/garak) | 20 | An LLM vulnerability scanner from NVIDIA |
| [promptfoo red teaming](https://www.promptfoo.dev/docs/red-team/) | 20 | Automated injection and jailbreak probes |

## Agents and protocols

| Tool | Modules | Notes |
| --- | --- | --- |
| [MCP SDKs](https://modelcontextprotocol.io/) | 16 | Build MCP servers and clients |
| [OpenAI Agents SDK](https://openai.github.io/openai-agents-python/) | 15, 17 | A lightweight multi-agent framework |
| [LangGraph](https://langchain-ai.github.io/langgraph/) | 15, 17 | A graph-based agent orchestration framework |
