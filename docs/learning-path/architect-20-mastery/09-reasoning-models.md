# 09 · Reasoning Models (lite) — Mastery

!!! abstract "At a glance"
    **Tier:** C (ship and defend, light) · **Module:** [09 · Reasoning models](../../modules/09-reasoning-models/index.md) · **Back to:** [Workbook](index.md) · [Architect 20%](../architect-20.md)  
    **Say it in one line:** *Reasoning models "think" before answering. Give them clear goals and constraints rather than step-by-step recipes, and route only the hard steps to them, because thinking costs tokens and time.*  
    **Last reviewed:** 2026-10-07

## Explain it like I'm new

Classic LLMs answer straight away. You used to improve hard answers by writing "Let's think step by step" (**chain-of-thought**, CoT), so the model wrote out its reasoning.

**Reasoning models** (and "extended thinking" modes) do this **built in**. They spend extra hidden or summarised "thinking tokens" before the final answer. They are better at:

- Multi-step logic.
- Maths.
- Planning.
- Tricky analysis.

But:

- **Slower**, because there are more tokens to generate.
- **More expensive**, because thinking tokens are usually billed as output.
- **Overkill** for simple tasks like classification, extraction or formatting.

Prompting changes too. These models work best with **high-level goals, constraints and success criteria**. Micromanaging every step can make them worse.

**Analogy.** A senior expert vs a junior. With the junior, you give step-by-step instructions. With the senior, you explain the goal and the constraints and let them work out the steps.

## Key ideas to master

- **Effort / thinking budget controls.** Many APIs let you set the reasoning effort or a thinking-token budget, so you can trade quality for cost and latency.
- **Don't force CoT on reasoning models.** Adding "think step by step" is usually unnecessary. Give clear goals and the output format instead.
- **Use them where the reasoning is hard:**
    - Planning an investigation.
    - Weighing conflicting evidence.
    - Complex multi-hop analysis.
- **Don't use them for** high-volume triage, extraction or formatting.
- **The reasoning trace is not an audit record.** Visible reasoning or summaries may not reflect the model's internal process faithfully. For audit, rely on **cited evidence and structured outputs**.
- **API differences.** Some reasoning modes restrict or ignore sampling settings like temperature, and parameters vary by provider and version. Check the current docs and date your notes (log them in [What's new](../../reference/whats-new.md)).

## In your resume project

- **Triage** (high volume, simple): a small, fast model with no extended thinking.
- **Supervisor planning** on complex, multi-pattern cases, and **pattern assessment** with conflicting evidence: a reasoning model or higher effort.
- **Case narrative**: a strong model at moderate effort. Quality comes from evidence and schema, not from long thinking.
- **Routing rule**: escalate to reasoning only when triage confidence is low or the case is complex (many entities, several patterns).

## Common mistakes

- Using a reasoning model everywhere: high cost, slow queues.
- Writing 20-step procedures for a reasoning model. Give goals and constraints instead.
- Treating the shown "thinking" as proof of why a decision was made.

---

## Practice questions

### Simple

??? question "S1. What is a reasoning model?"
    **Answer:** An LLM trained to spend extra "thinking" tokens working through a problem before giving its final answer. It is better at complex logic and planning, but slower and more expensive.

??? question "S2. What is chain-of-thought (CoT) prompting?"
    **Answer:** Asking a model to write out its intermediate reasoning steps before the final answer (for example "think step by step"). It improves results on multi-step problems for classic models.

??? question "S3. Why not use a reasoning model for everything?"
    **Answer:** Thinking tokens add **cost and latency**. For simple tasks (classify, extract, format), a regular or small model is just as good and much cheaper and faster.

### Medium

??? question "M1. How should prompts differ for reasoning models?"
    **Answer:**

    - Give a **clear goal, constraints, success criteria and the output format**.
    - Avoid rigid step-by-step procedures and "think step by step" phrases.
    - Provide the relevant context.
    - Let the model plan.
    - Keep the structured output requirements.

??? question "M2. What does a 'reasoning effort' or thinking budget setting do?"
    **Answer:** It controls how much thinking the model does before answering. Higher effort usually means better results on hard problems, with more tokens, cost and time. Tune it per step using evals.

??? question "M3. Which steps in an agent system benefit most from reasoning models?"
    **Answer:**

    - **Planning** and decomposition.
    - Judging **ambiguous or conflicting evidence**.
    - Complex multi-step analysis.
    - Hard tool-use decisions.

    Simple extraction, routing and formatting steps rarely benefit.

### Hard

??? question "H1. Design a routing policy for when to use reasoning in surveillance."
    **Answer:**

    - **Default**: a fast model, no extended thinking.
    - **Escalate to a reasoning model or higher effort** when:
        - Triage confidence is below the threshold.
        - More than N entities are involved, or the ownership graph has more than 2 hops.
        - Several candidate patterns are present.
        - Specialists return conflicting findings.
    - **Cap** the thinking budget per case.
    - **Measure**: quality uplift vs added cost and latency on the eval slices for "complex" cases.

??? question "H2. Why is the visible reasoning trace not enough for model-risk audit?"
    **Answer:** Research shows that stated reasoning may **not faithfully reflect** what actually drove the answer. It can also be summarised or hidden by the provider. Audit should rest on **verifiable artefacts**:

    - Cited evidence IDs.
    - Structured decisions.
    - Tool-call logs.
    - Validator results.
    - Human approvals.

??? question "H3. A reasoning step costs 8× more per call than the non-reasoning version. How do you decide whether it's worth it?"
    **Answer:** Compare on the **same eval slice** where the step matters (complex cases only):

    - **Quality uplift**: for example, correct pattern assessment rises from 82% to 91%.
    - **Added cost and latency**: per case, and per month at real volume.
    - **Business value of the uplift**: fewer missed cases, less analyst rework.

    If only 10% of cases are routed to it, the blended cost increase is about 1.7×, not 8×. Present it as **cost per extra correct decision**.

### Tricky

??? question "T1. 'Adding Think step by step to our reasoning model prompt will improve it further.' True?"
    **Answer:** Usually not. Reasoning models already reason internally. Extra CoT instructions are often unnecessary and can even hurt. Improve the goal, constraints and context instead, and test with evals.

??? question "T2. 'Reasoning models don't hallucinate because they think carefully.' True?"
    **Answer:** False. They can reason carefully from **wrong or missing** information, and still invent facts. Grounding, citations and validation remain essential.

### Scenario (resume-synced)

??? question "SC1. Leadership wants to switch all agents to the newest reasoning model 'for quality'. Respond as the architect."
    **Answer:** "Let's test it, not assume it. I'd run the full eval suite per agent:

    - Triage and extraction likely won't improve, and the cost and latency would rise a lot.
    - Supervisor planning and complex pattern assessment may improve.

    The proposal: route only complex cases (low confidence, multi-hop ownership, conflicting findings) to the reasoning model, with a capped budget. We'd measure quality uplift per dollar on the complex-case slice. That captures most of the gain at a fraction of the cost."

??? question "SC2. Analysts say the supervisor's investigation plans are shallow on cases with many linked accounts. What do you try, in order?"
    **Answer:**

    1. **Check the context first.** Did the supervisor actually receive the ownership graph summary and the specialist findings? Missing evidence looks like shallow reasoning.
    2. **Improve the goal and constraints** in the prompt. For example: "the plan must cover every linked account within 3 hops and say which specialist checks each".
    3. **Raise the reasoning effort** (or route to a reasoning model) for cases above a complexity threshold.
    4. **Measure** plan completeness on an eval slice of multi-entity cases, before and after.

    Don't jump to a bigger model before ruling out a context problem.

## Can you teach it?

- [ ] I can explain reasoning models vs CoT on classic models
- [ ] I can say how prompting changes (goals, not recipes) and when not to use them
- [ ] I can design an evidence-based routing rule for reasoning effort
