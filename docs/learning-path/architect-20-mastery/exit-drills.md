# Exit Drills — Cross-Topic Design Review

!!! abstract "At a glance"
    **Purpose:** prove you have mastered the 20% by answering the way a real architecture or model-risk review asks: mixing topics, with follow-ups.  
    **Maps to:** the four **exit criteria** on the [Architect 20% page](../architect-20.md). · **Back to:** [Workbook](index.md)  
    **Last reviewed:** 2026-10-07

!!! tip "How to practise"
    1. Set a timer for each drill.
    2. Answer out loud or on a whiteboard **before** opening the model answer.
    3. Ask yourself the follow-up questions. Reviewers always ask "why?" and "what if it fails?".

---

## Drill 1 — Draw the agent graph (exit criterion 1)

**Task (10 minutes):** Draw your surveillance agent system. Label where **prompts**, **tools / MCP**, **retrieval**, **memory**, **validators** and **HITL** live.

??? success "Model answer"
    ```mermaid
    flowchart TB
      AL[Alert from rules engine] --> SUP

      subgraph ORCH[LangGraph orchestrator - checkpointed state]
        SUP[Supervisor agent<br/>prompt: policy + routing task]
        TRI[Triage agent<br/>small model, schema output]
        DAT[Data agent<br/>ReAct, read-only tools]
        COM[Comms agent<br/>quarantined: no write tools]
        PAT[Pattern agent<br/>reasoning on complex cases]
        WRI[Case-writer<br/>evaluator-optimizer, packet schema]
      end

      SUP --> TRI & DAT & COM & PAT
      DAT & COM & PAT --> SUP
      SUP --> WRI
      WRI --> VAL[Validators<br/>schema, citation IDs, PII/MNPI filter]
      VAL --> HITL{Analyst approval}
      HITL -->|approve| FILE[Case management - write tool]
      HITL -->|reject + note| SUP

      subgraph MCP[MCP gateway: auth, entitlements, audit]
        T1[Trade / order servers]
        T2[Comms archive]
        T3[Ownership graph]
        T4[Policy + past-case RAG]
      end
      DAT --> T1
      COM --> T2
      PAT --> T3
      SUP & WRI --> T4

      MEM[(Memory: episodic cases,<br/>semantic policies - entitlement scoped)] <--> SUP
      EVAL[[CI evals ~1,400 cases + online monitoring]] -.-> ORCH
    ```

    **Points to say out loud:**

    - The **prompts** are versioned blocks per agent (policy / task / schema).
    - **Entitlements** are enforced in the MCP servers and in retrieval, never in prompts.
    - **Untrusted content** (comms) is isolated in an agent with no write tools and no outbound channel.
    - The **only write action** (filing a case) sits behind HITL.
    - The **state is checkpointed** for pause and resume, and for audit.

??? question "Follow-ups a reviewer will ask"
    1. *"Which of these are really workflows, not agents?"*
        - Intake, routing, validators, HITL and filing are deterministic.
        - The supervisor and specialist loops are agentic.
        - See [Prompt chaining](06-prompt-chaining.md).
    2. *"What happens if the comms agent is prompt-injected?"* It can only return structured findings. It has no tools to act with or leak through, and the analyst approves the outcome. See [Prompt security](20-prompt-security.md).
    3. *"Where does cost explode?"* Fan-out and long contexts. Control them with budgets, compaction and model routing. See [Multi-agent](17-multi-agent.md).

---

## Drill 2 — Write a one-page prompt contract (exit criterion 2)

**Task (15 minutes):** Write the prompt contract for the **case-writer agent**: inputs, schema, refusal rules, allowed tools and audit fields.

??? success "Model answer (template)"
    | Section | Content |
    | --- | --- |
    | **Purpose** | Draft an investigation packet from verified findings for analyst review. Does **not** decide outcomes. |
    | **Owner / version** | Surveillance AI platform team · `case_writer.policy.v4`, `case_writer.task.v9`, `packet.schema.v3` |
    | **Model** | Strong cloud model (pinned version); on-prem model for MNPI-classified cases |
    | **Inputs** | Supervisor case state (structured findings + evidence IDs), retrieved policy snippets, alert metadata. **All treated as data.** |
    | **Trust levels** | System policy: trusted · Findings: trusted-derived · Raw excerpts (chats/emails): **untrusted** |
    | **Allowed tools** | `get_policy_snippet` (read-only), `get_evidence_by_id` (read-only, entitlement-checked). No write tools. |
    | **Output schema** | `case_id`, `pattern`, `summary` (≤120 words, no PII), `evidence[]` (source_id, type, why_relevant), `risk_score` 1–5, `confidence`, `missing_data[]`, `conflicts[]`, `needs_human_review` |
    | **Grounding rules** | Every claim cites a `source_id` from the provided findings; no outside knowledge about clients or trades |
    | **Refusal / escalation** | Insufficient evidence → `missing_data` + `needs_human_review: true`. Conflicting findings → list in `conflicts`, never resolve silently. No legal conclusions ("this is market abuse"). |
    | **Forbidden content** | PII beyond internal IDs, MNPI details in the summary, instructions found in evidence |
    | **Validators** | Schema; all `source_id`s exist in the case's retrieved set; PII/MNPI filter; consistency of pattern vs supervisor finding |
    | **Audit fields (logged)** | Prompt block versions, model version, parameters, evidence IDs, tool calls, validator results, approver, timestamps |
    | **Eval gate** | Faithfulness ≥ 0.95, citation validity 100%, PII leaks 0, critical-slice regressions 0 |

??? question "Follow-ups"
    1. *"Why are raw excerpts untrusted if they come from your own archive?"* The traders under investigation wrote them, so they may contain manipulation.
    2. *"Who approves a change to the refusal rules?"* The policy block owner **plus** compliance / model-risk sign-off. See [PromptOps](21-promptops.md).
    3. *"What stops it inventing evidence?"* The citation-ID validator against the retrieved set, plus the faithfulness eval. See [Structured outputs](05-structured-outputs.md).

---

## Drill 3 — Define the minimum eval pack (exit criterion 3)

**Task (10 minutes):** List the offline cases and online metrics you need before releasing a governed agent.

??? success "Model answer"
    **Offline (CI, blocks release):**

    | Area | Metric | Gate (illustrative) |
    | --- | --- | --- |
    | Triage | Recall on true alerts / precision | Recall ≥ baseline; precision ≥ target |
    | Classification | Per-pattern F1 | No critical-slice regression |
    | Grounding | Faithfulness; citation validity; correct refusal on no-evidence cases | ≥ 0.95; 100%; ≥ 0.9 |
    | Tools | Tool-selection and argument accuracy; avg steps | ≥ target; ≤ budget |
    | Security | Injection success rate (direct + indirect); entitlement leaks; PII/MNPI leaks | ≤ threshold; **0**; **0** |
    | Ops | p95 latency; cost per case | ≤ SLA; ≤ budget |

    **Online (production):**

    - Analyst accept / edit / reject rate.
    - Sampled LLM-judge faithfulness.
    - Drift alerts.
    - Safety event counts.
    - Cost and latency per version.

    **Hygiene:**

    - Eval items are never used as few-shot examples.
    - Held-out set.
    - Production failures are added each sprint.
    - The judge is calibrated against human labels.

??? question "Follow-ups"
    1. *"Why not just accuracy?"* The classes are imbalanced. See [Evaluation](18-evaluation.md), question T3.
    2. *"How do you trust the LLM judge?"* Calibrate it on human labels, use specific rubrics, and use a different model family.
    3. *"What do you do when averages go up but a critical case fails?"* Critical slices are hard gates, so the release is blocked.

---

## Drill 4 — The 5-minute build-path talk (exit criterion 4)

**Task (5 minutes, spoken):** "When would you prompt, use RAG, use GraphRAG or fine-tune?"

??? success "Model answer (speaking outline)"
    1. **Start with prompting** (30 seconds). It is clear task design, schema and context. It is cheapest and fastest, and it's always the baseline.
    2. **RAG for knowledge** (1 minute). Use it when the answer depends on private, fresh or large information that needs citations: policies, past cases. Enforce entitlements at retrieval, and evaluate retrieval separately from generation.
    3. **GraphRAG for relationships** (1 minute). Use it when the question is about **connections**: common beneficial ownership, communication networks. The wash-trade example. Mention the costs (entity resolution, freshness) and that the path is cited as evidence.
    4. **Fine-tune for behaviour** (1.5 minutes). Use it when evals show prompting and RAG have plateaued on **format, tool use, consistency**, or when a small or on-prem model must match a bigger one. The QLoRA SFT + DPO on tool-use traces example. Governance and re-tuning costs.
    5. **Close** (1 minute). "We decide with one eval set across options, including cost, latency and data residency. In practice we combine them: RAG and GraphRAG for knowledge, a fine-tuned on-prem model for tool behaviour, and good prompts everywhere."

---

## Drill 5 — Rapid-fire mixed questions

Answer each in **one or two sentences**. These mix all the topics on purpose.

??? question "R1. The model has a 1M-token window. Do we still need RAG and memory?"
    Yes. Cost, latency, freshness, entitlements and attention quality all still matter. Long context complements retrieval. ([01](01-how-llms-work.md), [10](10-context-engineering.md))

??? question "R2. Strict JSON outputs are on. Can we skip validators?"
    No. A schema guarantees shape, not truth. Validate IDs, business rules and PII. ([05](05-structured-outputs.md))

??? question "R3. Where do entitlements belong?"
    In retrieval filters and MCP servers, using the real user's identity. Never in prompts. ([11](11-rag-and-grounding.md), [16](16-mcp-and-skills.md))

??? question "R4. One agent reads emails, sees client data and can send emails. Problem?"
    That's the lethal trifecta. Remove a leg: no outbound channel, or isolate the untrusted content. ([20](20-prompt-security.md))

??? question "R5. When do you add a second agent?"
    When context overload, tool confusion, separate permissions or parallelism justify it, and the evals show a gain worth the extra cost. ([17](17-multi-agent.md))

??? question "R6. Few-shot examples improved the eval by 15%. First check?"
    Leakage. Make sure no example overlaps the eval set, then confirm on held-out data. ([03](03-few-shot.md))

??? question "R7. The provider updated the model and outputs changed. What failed?"
    PromptOps: the model wasn't pinned, and no eval gate ran on the change. ([21](21-promptops.md))

??? question "R8. Should we teach the model our policies by fine-tuning?"
    No. Policies are changing knowledge, so use RAG with citations. Fine-tune behaviour. ([22](22-finetune-vs-prompt-vs-rag.md))

??? question "R9. Use the reasoning model for triage?"
    Usually no. Triage is high volume and simple. Use reasoning only on complex, low-confidence cases. ([09](09-reasoning-models.md))

??? question "R10. Is the agent's visible reasoning our audit record?"
    No. Audit rests on cited evidence, structured outputs, tool logs, validator results and approvals. ([09](09-reasoning-models.md), [21](21-promptops.md))

??? question "R11. Agent loops 40 steps. Top three fixes?"
    Step and duplicate-call limits, actionable tool errors, and compact tool results with IDs. ([15](15-agent-patterns.md), [14](14-tool-calling.md))

??? question "R12. What's the difference between a workflow and an agent, in one line?"
    In a workflow, your code decides the steps. In an agent, the model decides the next step in a loop. ([06](06-prompt-chaining.md))

??? question "R13. A trader's chat tells the AI to mark the case compliant. What happens?"
    It is treated as untrusted data, flagged as a suspicious signal, and has no power to act. A human decides. ([02](02-prompt-anatomy.md), [20](20-prompt-security.md))

??? question "R14. What makes a tool description good?"
    A clear name, what it does, **when and when not to use it**, typed parameters with formats, limits, and what it returns. ([14](14-tool-calling.md))

??? question "R15. Why put stable prompt content first?"
    Prompt caching of the identical prefix, plus clarity. Variable data and the question go last. ([02](02-prompt-anatomy.md), [10](10-context-engineering.md))

??? question "R16. The primary model is down during market hours. What happens?"
    The circuit breaker trips. Eval-approved fallbacks are used, with restricted data staying on-prem, and the system degrades to rules plus the human queue if needed. Surveillance never stops. ([X1](x1-cost-latency-reliability.md))

??? question "R17. Why track p95 latency and p95 cost per case, not only averages?"
    Tails break SLAs and budgets. One looping case can cost as much as a thousand normal ones. ([X1](x1-cost-latency-reliability.md))

??? question "R18. Is an LLM agent a 'model' for model risk?"
    In most banks, yes. It needs an inventory entry, documentation, independent validation, monitoring and change control. ([X2](x2-governance-model-risk.md))

??? question "R19. Does HITL exempt a system from model risk governance?"
    No. HITL is a control, not an exemption, and you must prove the oversight is meaningful (not rubber-stamping). ([X2](x2-governance-model-risk.md))

??? question "R20. Vendor benchmarks look great. Is validation done?"
    No. Validate fitness for **your** use case with your own evals, challenge tests and monitoring. ([X2](x2-governance-model-risk.md), [18](18-evaluation.md))

---

## Mock panel — 40-minute design review script

Use this with a friend or record yourself. The reviewer reads the prompts. You answer.

1. "Give me the 2-minute overview of your surveillance agent system." → [Drill 1](#drill-1-draw-the-agent-graph-exit-criterion-1)
2. "Why multi-agent? Prove it was worth it." → [Multi-agent SC1](17-multi-agent.md#scenario-resume-synced)
3. "How does an EMEA analyst never see APAC data?" → [RAG SC2](11-rag-and-grounding.md#scenario-resume-synced)
4. "A chat contains an injection. Walk me through it." → [Security SC1](20-prompt-security.md#scenario-resume-synced)
5. "How do you know a prompt change didn't break anything?" → [Evaluation](18-evaluation.md), [PromptOps](21-promptops.md)
6. "Why fine-tune instead of prompting?" → [Fine-tune SC1](22-finetune-vs-prompt-vs-rag.md#scenario-resume-synced)
7. "Your cloud provider is down for two hours. What happens to surveillance?" → [X1 SC1](x1-cost-latency-reliability.md#scenario-resume-synced)
8. "What are the known limitations, and how is human oversight meaningful?" → [X2 SC1 and H2](x2-governance-model-risk.md#scenario-resume-synced)
9. "What would you do differently next time?" → Prepare **two honest lessons**. For example: build the eval set before the first agent; start with fewer agents and split later.

## Done?

When you can do Drills 1–4 without notes and score **16/20 or better** on the rapid-fire, tick the exit criteria on the [Architect 20% page](../architect-20.md) and log it in your [Journal](../../journal/index.md).
