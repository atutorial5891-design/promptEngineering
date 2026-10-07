# 17 · Multi-Agent Systems — Mastery

!!! abstract "At a glance"
    **Tier:** B (core of your story) · **Module:** [17 · Multi-agent](../../modules/17-multi-agent/index.md) · **Back to:** [Workbook](index.md) · [Architect 20%](../architect-20.md)  
    **Say it in one line:** *Use several agents when the work splits into separate specialisms or parallel reading that would overload one context. Every extra agent adds cost, latency and coordination failure modes, so justify each one.*  
    **Last reviewed:** 2026-10-07

## Explain it like I'm new

One very capable person can do a whole investigation alone, but for a big case a team is faster:

- A data specialist.
- A communications reviewer.
- A pattern expert.
- A team lead who coordinates and writes up the case.

That is **multi-agent**: several LLM agents, each with its **own instructions, tools and context**, working together.

**Why teams help:**

- Each specialist has a **focused context and toolset**, which gives better tool choice and less clutter.
- Independent work runs **in parallel**, which is faster.
- Separation lets you apply **different permissions** per agent.

**Why teams hurt:**

- More calls mean much more **cost** (Anthropic reported its multi-agent research system used ~15× the tokens of a chat).
- **Handover loss**: information gets dropped between agents.
- **Coordination bugs**: duplicate work, contradictions, loops.
- **Harder debugging and evaluation.**

## Key ideas to master

| Topology | Shape | When |
| --- | --- | --- |
| **Supervisor (hierarchical)** | One lead agent delegates to specialists and combines the results | Most enterprise cases. Clear control and audit |
| **Pipeline / sequential** | Agent A → B → C | Known stages (often better as a workflow) |
| **Parallel fan-out / fan-in** | Many workers on independent parts, then merge | Lots of reading or searching |
| **Network / peer-to-peer (swarm)** | Agents hand off to each other directly | Conversational routing; harder to govern |
| **Debate / critic** | Agents argue or review each other | High-stakes judgement; costly |

- **Clear contracts between agents.** Each agent returns a **structured** result (schema) with evidence IDs, not free-form chat.
- **Clear delegation briefs.** The supervisor must give each worker:
    - The objective.
    - The scope.
    - The output format.
    - The limits.

    Vague delegation causes duplicate or missing work.
- **Shared state.** Use a central case state (for example the LangGraph state) instead of agents chatting endlessly.
- **Per-agent least privilege.** Separate agents let you separate permissions. Use this.
- **Start single-agent, then split** when you see context overload, tool confusion or a need for parallelism.

## In your resume project

A **supervisor** topology with specialist agents. The six-agent design is shown on the [workbook overview](index.md#the-running-scenario-used-on-every-page).

- **Why multi-agent here:**
    - Data, comms and ownership analysis need different tools, permissions and context.
    - Comms review is heavy reading, so it gets its own clean context.
    - Parallel fan-out reduces time-to-packet.
- **Wash-trade example:** the supervisor fans out to the data agent (matched trades), the graph or pattern agent (common ownership path) and the comms agent (coordination language). It then fans in, and the case-writer builds the packet.
- **Controls:**
    - Each agent's outputs follow a schema.
    - The supervisor's state is checkpointed.
    - HITL comes before filing.
    - There is a per-case cost budget.

## Common mistakes

- Six agents for a task one agent plus three tools could handle.
- Agents passing free-text summaries that drop evidence IDs.
- No overall budget, so fan-out explodes the cost.
- Evaluating only the final output, so you can't tell which agent failed.

---

## Practice questions

### Simple

??? question "S1. What is a multi-agent system?"
    **Answer:** A system where several LLM-based agents, each with its own role, instructions, tools and context, work together on a task, usually coordinated by a supervisor or a workflow.

??? question "S2. What is the supervisor pattern?"
    **Answer:** A lead agent receives the task, delegates sub-tasks to specialist agents, collects their results and decides the next steps or the final answer.

??? question "S3. Give two benefits and two costs of multi-agent."
    **Answer:**

    - **Benefits**: focused contexts and tools per agent; parallel work; separate permissions.
    - **Costs**: much higher token use and latency; handover and coordination errors; harder debugging.

### Medium

??? question "M1. When should you split one agent into several?"
    **Answer:** When you see:

    - Context overflowing with mixed concerns.
    - Too many tools causing wrong selection.
    - Clearly separate specialisms needing different permissions.
    - Independent sub-tasks that would benefit from parallel work.

    If none of these apply, stay single-agent.

??? question "M2. What should a delegation brief from supervisor to worker contain?"
    **Answer:**

    - The objective.
    - The scope (accounts, time window).
    - What **not** to do (avoid overlap with other workers).
    - The tools to use.
    - The output schema (including evidence IDs).
    - Limits (steps, time).
    - What to do if blocked.

??? question "M3. Why should agents communicate through structured state rather than free chat?"
    **Answer:** Structured state (schemas, evidence IDs, status fields) is **checkable**, **compact** and **auditable**. Free chat between agents loses details, grows the context and makes it hard to see who decided what.

??? question "M4. How do you evaluate a multi-agent system?"
    **Answer:** At two levels:

    1. **End-to-end**: packet quality, analyst acceptance, time and cost per case.
    2. **Per agent**: each specialist's output against labelled expectations (did the comms agent find the key message? did the graph agent find the ownership path?).

    Also look at the trajectory: unnecessary delegations and duplicated work.

### Hard

??? question "H1. Supervisor vs peer-to-peer network for surveillance: which and why?"
    **Answer:** **Supervisor.**

    - It gives one place for control flow.
    - It gives a clear audit trail ("supervisor delegated X to the comms agent at step 4").
    - It is easier to set budgets and HITL checkpoints.
    - Its behaviour is more predictable.

    Peer-to-peer handoffs suit conversational routing (support bots), but they are harder to govern and test in a regulated setting.

??? question "H2. How do you control cost in a fan-out design?"
    **Answer:**

    - **Budgets** per case and per agent (tokens, calls).
    - **Model routing**: small models for workers doing extraction, strong models for the supervisor and writer.
    - **Limit the fan-out width**.
    - **Early exit**: if triage says low risk, don't fan out.
    - **Cache** shared prefixes.
    - Return **compact results**.

    Track the cost per case as a release metric.

??? question "H3. Two specialists return contradictory findings. How should the system handle it?"
    **Answer:**

    - The supervisor must **surface** the conflict, not hide it. Record both findings with their evidence IDs.
    - Optionally, ask a targeted follow-up ("comms agent: re-check messages M-12 to M-20 for the time window").
    - If it is still unresolved, mark `conflict: true` in the packet and route the case to a human with both views.

    Never let the writer "average" the two into a confident narrative.

### Tricky

??? question "T1. 'More agents means more intelligence.' True?"
    **Answer:** No. More agents mean more **parallelism and specialisation**, along with more cost and more coordination failures. Many tasks are done better by one well-equipped agent. Add agents only for a measured benefit.

??? question "T2. Should every agent use the strongest model?"
    **Answer:** No. Route by role. Extraction and search workers can often use smaller, faster models. Planning, judgement and final writing benefit from stronger ones. Prove each choice with per-agent evals.

??? question "T3. Is a multi-agent system safer because work is split?"
    **Answer:** Only if you **use** the split, by giving each agent least-privilege tools and isolating untrusted content in agents with no sensitive tools. Otherwise, more agents just means more attack surface and more places for injected text to spread.

### Scenario (resume-synced)

??? question "SC1. Interviewer: 'Why six agents? Couldn't one agent do it?'"
    **Answer (sample):** "We started from one agent and split only where we saw problems:

    - **Mixed concerns.** Trades, comms and ownership needed different tools and permissions. One agent with every tool chose tools badly and carried too much context.
    - **Heavy reading.** Comms review needed its own clean context.
    - **Speed.** Parallel fan-out on data, comms and graph cut the time-to-packet.

    The supervisor gives us one control point for budgets, checkpoints and HITL. Each split was justified with evals and cost per case. If a split hadn't improved quality or latency, we'd have merged it back."

??? question "SC2. The case-writer sometimes omits the comms finding. Where do you look?"
    **Answer:**

    1. Did the comms agent return its finding in the **schema** with evidence IDs?
    2. Did the supervisor **include** it in the state passed to the writer, or drop it during compaction?
    3. Does the writer's prompt require covering every finding category?
    4. Add a validator: every finding in the state must appear in the packet or be explicitly dismissed with a reason.
    5. Add an eval case.

## Can you teach it?

- [ ] I can compare supervisor, pipeline, fan-out and network topologies
- [ ] I can list when to split agents and the cost of doing it
- [ ] I can defend my six-agent design with evidence, not hype
