# Architectures

These system designs are reused across modules. For each one, the notes say when to use it, where the prompts live, and what to evaluate.

!!! tip "The simplicity ladder"
    Climb only as far as your evals require. Each rung adds capability, but also cost, latency, and failure modes:

    1. Single call
    2. Chain
    3. Router
    4. Parallel steps
    5. Orchestrator-workers or evaluator-optimizer
    6. Autonomous agent

| Architecture | Use when | Modules |
| --- | --- | --- |
| [Single call](#1-single-call) | One well-defined task | 02-05 |
| [Prompt chain pipeline](#2-prompt-chain-pipeline) | Fixed sub-steps, each needing validation | 06 |
| [Router + specialists](#3-router-specialists) | Distinct input types need different handling | 06, 15 |
| [Parallelization](#4-parallelization-sectioning-and-voting) | Independent sub-tasks, or a need for confidence by voting | 08, 15 |
| [RAG pipeline](#5-rag-pipeline) | Answers must come from private or fresh knowledge | 10, 11 |
| [ReAct agent loop](#6-react-agent-loop) | Open-ended tasks with an unpredictable number of steps | 14, 15 |
| [Orchestrator-workers](#7-orchestrator-workers) | Breadth-heavy tasks that split dynamically | 15, 17 |
| [Evaluator-optimizer](#8-evaluator-optimizer-loop) | Clear quality criteria, and iteration helps | 08, 15 |
| [Guardrail sandwich](#9-guardrail-sandwich) | Any user-facing or tool-using app | 20 |
| [Dual-LLM / quarantine](#10-dual-llm-quarantine) | Agents that read untrusted content and have tools | 20 |
| [Eval harness in CI](#11-eval-harness-in-ci) | Every production prompt | 18, 21 |

## 1. Single call

```mermaid
flowchart LR
  Input --> Template["Prompt template + schema"] --> Model --> Validate --> Output
```

- **Prompt lives in:** one versioned template.
- **Evaluate:** task metric, schema validity.

## 2. Prompt chain pipeline

```mermaid
flowchart LR
  In[Input] --> A[Extract] --> G1{Gate} --> B[Transform] --> G2{Gate} --> C[Generate] --> Out[Output]
  G1 -->|fail| Fix1[Retry / abort]
  G2 -->|fail| Fix2[Retry / abort]
```

- **Prompts:** one per step, each narrow.
- **Evaluate:** each step on its own, plus end to end.

## 3. Router + specialists

```mermaid
flowchart LR
  In[Input] --> Router["Router (cheap model or classifier)"]
  Router -->|billing| P1[Billing prompt]
  Router -->|technical| P2[Tech prompt + tools]
  Router -->|other| P3[General prompt]
  P1 --> Out[Output]
  P2 --> Out
  P3 --> Out
```

- **Prompts:** a router prompt with clear category definitions, and one specialist prompt per route.
- **Evaluate:** routing accuracy (a confusion matrix), plus quality for each route.

## 4. Parallelization (sectioning and voting)

```mermaid
flowchart LR
  In[Input] --> S1[Aspect 1]
  In --> S2[Aspect 2]
  In --> S3[Aspect 3]
  S1 --> Agg[Aggregate / vote]
  S2 --> Agg
  S3 --> Agg
  Agg --> Out[Output]
```

- **Sectioning:** each branch checks a different aspect, e.g. one guardrail and one answer.
- **Voting:** the same task is run N times, and the results are combined by majority or by a judge.

## 5. RAG pipeline

```mermaid
flowchart LR
  Q[Question] --> QR[Query rewrite]
  QR --> Ret[Retrieve]
  KB[(Index)] --> Ret
  Ret --> RR[Rerank]
  RR --> Gen["Grounded generation (sources with IDs)"]
  Q --> Gen
  Gen --> Cite[Citation check]
  Cite --> A[Answer or abstain]
```

- **Prompts:** query rewrite, then grounded answer (with citation and abstain rules).
- **Evaluate:** retrieval recall@k, faithfulness, abstention on unanswerable questions.

## 6. ReAct agent loop

```mermaid
flowchart LR
  Goal --> Reason[Reason about next step]
  Reason --> Act[Tool call]
  Act --> Obs[Observation]
  Obs --> Reason
  Reason -->|"done or max steps"| Final[Answer]
```

- **Prompts:** an agent system prompt (goal, autonomy boundaries, stop conditions) and tool descriptions.
- **Evaluate:** task success, steps per success, trajectory error analysis.

## 7. Orchestrator-workers

```mermaid
flowchart TB
  Lead["Orchestrator: plan + delegate"] --> W1[Worker 1]
  Lead --> W2[Worker 2]
  Lead --> W3[Worker N]
  W1 --> Synth[Orchestrator: synthesize]
  W2 --> Synth
  W3 --> Synth
```

- **Prompts:** orchestrator planning, worker briefs (objective, format, boundaries), and synthesis.
- **Evaluate:** quality against a rubric, cost multiplier vs. a single agent.

## 8. Evaluator-optimizer loop

```mermaid
flowchart LR
  Task --> Gen[Generator]
  Gen --> Eval["Evaluator (rubric / tests)"]
  Eval -->|"feedback"| Gen
  Eval -->|"passes bar"| Out[Output]
```

- **Prompts:** a generator, and an evaluator with an explicit rubric. Use tests or tools as the evaluator wherever possible.
- **Evaluate:** score per iteration, how quickly it converges, cost.

## 9. Guardrail sandwich

```mermaid
flowchart LR
  User --> InF["Input checks: moderation, injection heuristics, PII"]
  InF --> LLM[Main LLM]
  LLM --> OutF["Output checks: schema, policy, PII, grounding"]
  OutF --> Resp[Response]
  OutF -->|violation| Safe[Safe fallback]
```

## 10. Dual-LLM / quarantine

```mermaid
flowchart LR
  Untrusted[Untrusted content] --> QLLM["Quarantined LLM (no tools)"]
  QLLM --> Vars["Structured values / references"]
  User[User request] --> PLLM["Privileged LLM (plans, has tools)"]
  Vars --> PLLM
  PLLM --> Policy{"Policy + human confirmation"}
  Policy --> Tools
```

The privileged model never reads raw untrusted text. It only handles structured values or symbolic references. See CaMeL and the design-patterns paper in [Papers](../resources/papers.md#security-module-20).

## 11. Eval harness in CI

```mermaid
flowchart LR
  Change["Prompt / model change (PR)"] --> Run[Run eval suite]
  Data[(Golden + regression datasets)] --> Run
  Run --> Score[Assertions + validated judges]
  Score --> Gate{"Above thresholds?"}
  Gate -->|yes| Merge
  Gate -->|no| Block[Block + report diffs]
```
