# Glossary

Abstention
:   The model declining to answer when the evidence is insufficient ("not found in sources").

Agent
:   An LLM system that decides its own next steps in a loop, using tools, until a goal is met.

Chain-of-thought (CoT)
:   Prompting a model to reason step by step before giving its final answer.

Compaction
:   Summarizing or condensing conversation history so a long-running agent stays within its context limits.

Context engineering
:   Curating the full set of tokens a model sees (instructions, tools, examples, history, retrieved data, memory) to get the behavior you want.

Context rot
:   Model performance degrading as the input gets longer, even on simple tasks.

Context window
:   The maximum number of tokens (input plus output) that a model can process in one call.

DSPy
:   A framework for writing LLM programs as modules with signatures, then optimizing their prompts automatically.

Effort / thinking level
:   A setting that controls how much a reasoning model thinks before answering.

Few-shot prompting
:   Including example input and output pairs in the prompt.

Grounding
:   Tying model outputs to provided sources, so claims can be verified.

Hallucination
:   Fluent output that's unsupported by, or contradicts, the facts or sources.

Indirect prompt injection
:   Malicious instructions hidden in content the model reads (web pages, emails, documents, tool outputs).

Instruction hierarchy
:   The trained priority of system or developer messages over user messages, and of user messages over tool outputs.

LLM-as-judge
:   Using an LLM with a rubric to grade outputs. It must be validated against human labels.

MCP (Model Context Protocol)
:   An open protocol for connecting AI applications to tools, resources, and prompts served by MCP servers.

Prefill
:   Writing the start of the assistant's reply to steer its format. Not every model or setting supports it.

Prompt caching
:   Reusing the processed prefix of a prompt across calls to cut cost and latency.

Prompt chaining
:   Splitting a task into several sequential LLM calls, with checks between them.

RAG (retrieval-augmented generation)
:   Retrieving relevant documents and putting them in the prompt so the model can answer from them.

ReAct
:   An agent pattern that interleaves reasoning, an action (a tool call), and an observation.

Reasoning model
:   A model trained, often with reinforcement learning, to think internally before producing its answer.

Self-consistency
:   Sampling several reasoning paths and taking a majority vote on the answer.

Skill
:   A packaged set of instructions and resources that an agent loads on demand. Usually a folder with a `SKILL.md` file.

Structured output
:   Model output constrained to a schema, such as JSON Schema or a Pydantic model.

System prompt
:   A high-priority message that sets identity, rules, tools, and format for a conversation.

Temperature
:   A sampling parameter that controls randomness. It's often restricted on reasoning models.

Token
:   The sub-word unit that models read and write.

Tool calling (function calling)
:   The model emitting structured requests to run functions, which the application executes.
