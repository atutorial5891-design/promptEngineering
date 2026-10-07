# 03 · Zero-shot and Few-shot (light) — Mastery

!!! abstract "At a glance"
    **Tier:** A (foundations, light) · **Module:** [03 · Few-shot](../../modules/03-few-shot/index.md) · **Back to:** [Workbook](index.md) · [Architect 20%](../architect-20.md)  
    **Say it in one line:** *Start with clear instructions (zero-shot). Add a few well-chosen examples only when the format, style or edge-case judgement still drifts, and never take examples from your eval set.*  
    **Last reviewed:** 2026-10-07

## Explain it like I'm new

- **Zero-shot**: "Classify this alert as high, medium or low." No examples, just instructions.
- **Few-shot**: the same instruction, **plus 2 to 5 worked examples** (input → correct output) placed in the prompt.

Examples are like showing a new joiner three finished case write-ups. They copy the **format and tone** very well. They also copy any **mistakes or bias** in your examples: if all three examples say "high", the model leans towards "high".

For an architect, this is a **light** topic. You need to know *when* examples help, the risks, and the rule about eval data.

## Key ideas to master

- **Instructions first.** Modern models do well zero-shot on many tasks. Add examples only when the evals show a gap.
- **Examples teach format and style most strongly.** Research (Min et al., 2022) found that the format and the kind of inputs in examples mattered more than whether the labels in them were correct. Treat that finding as a reason to be careful, not as permission to use sloppy labels.
- **Diversity.** Cover different labels and edge cases, so the model does not latch on to one pattern.
- **Balance and order.** Unbalanced labels or the order of examples can bias the output.
- **Never reuse eval items as few-shot examples.** That leaks the test answers and inflates your scores. In this repo a test enforces this for the sentiment lab.
- **Cost.** Examples are sent on every call. 5 examples × 400 tokens × 200,000 calls adds up.
- **Dynamic few-shot.** Retrieve the most similar labelled examples per input from an example bank. This is powerful, but the bank must stay separate from the eval data.

## In your resume project

Zero-shot triage struggled with **edge cases**, such as legitimate market-making that looks like wash trading. You added **three short examples**:

1. A true wash trade.
2. Legitimate market-making.
3. A `needs_more_data` case.

They were taken from an example bank that is **disjoint** from the 1,400 CI eval cases.

## Common mistakes

- All examples from one class, which biases the predictions.
- Examples copied from the test set, which gives fake-high eval scores.
- Long examples that cost more tokens than the task itself.
- Examples that contradict the written instructions. The model follows the examples.

---

## Practice questions

### Simple

??? question "S1. What is the difference between zero-shot and few-shot prompting?"
    **Answer:**

    - **Zero-shot** gives only instructions.
    - **Few-shot** adds a few input → output examples in the prompt, so the model can copy the pattern.

??? question "S2. What do few-shot examples teach most strongly?"
    **Answer:** The **format, structure, length and style** of the output, and roughly how hard calls should be judged. The model imitates what it sees.

??? question "S3. How many examples is 'few'?"
    **Answer:** Typically 1 to 5. More is not always better. Each example costs tokens on every call, and the gains flatten quickly. Let evals decide.

### Medium

??? question "M1. When would you choose few-shot over just improving the instructions?"
    **Answer:** When the desired output is **easier to show than to describe**: a specific tone, an unusual format, or subtle edge-case judgement. Do it when the evals show instructions alone have plateaued. Try clear instructions first, because they are cheaper and easier to maintain.

??? question "M2. Why must few-shot examples never come from the eval set?"
    **Answer:** If the model sees the exact test items (with answers) in its prompt, it simply copies them. The eval score goes up, but real-world quality does not. That is **data leakage**, and it makes your release gate meaningless.

??? question "M3. All your examples are labelled 'high'. What happens?"
    **Answer:** The model becomes biased towards predicting "high" (a majority-label bias). Balance the labels, include a negative and a "needs more data" example, and vary the order.

### Hard

??? question "H1. Design dynamic few-shot for triage. What are the risks?"
    **Answer:**

    **Design:**

    - Build a labelled **example bank** of reviewed past alerts.
    - Embed the examples.
    - For each new alert, retrieve the top 3 most similar examples, ensuring label diversity, and insert them.

    **Risks:**

    1. **Leakage** if the bank overlaps the eval set. Enforce disjoint IDs with a test.
    2. **Entitlement leaks.** Examples may contain data the current analyst should not see. Anonymise them or filter by entitlement.
    3. **Stale or wrong labels** spread. Version and review the bank.
    4. Higher latency from the extra retrieval.

??? question "H2. How do you prove examples are worth their token cost?"
    **Answer:** Run an A/B on the eval set: zero-shot vs 1, 3 and 5 shots. Measure the quality metric (for example recall on true alerts) **and** the cost per call.

    Keep the smallest number of examples that reaches the target. Re-test when the model changes, because newer models often need fewer examples.

### Tricky

??? question "T1. 'If the example labels are wrong, it doesn't matter much — research says labels barely matter.' Is that safe to rely on?"
    **Answer:** No. That finding concerned classification benchmarks, and it mainly shows that models lean heavily on **format**. In a regulated workflow, wrong examples teach wrong judgement and fail audit review. Always use correct, reviewed examples.

??? question "T2. Can examples override your written instructions?"
    **Answer:** Yes. When examples and instructions disagree, models often follow the **examples**. If the instructions say "max 3 reasons" but the examples show 5, expect 5. Keep them consistent.

### Scenario (resume-synced)

??? question "SC1. Your triage eval jumped from 82% to 97% after adding examples. What do you check before celebrating?"
    **Answer:**

    1. Do the examples **overlap the eval items** (same alert IDs or near duplicates)? That would be leakage.
    2. Did the label balance of the examples change the predictions in a way the evals happen to reward?
    3. Check performance on a **held-out** set and on recent production samples.
    4. Check the cost per call.

    Only then promote the change.

??? question "SC2. A new analyst asks why the prompt has 'three random old cases' in it. Explain simply."
    **Answer:** "They're not random. They're worked examples showing the model what a good triage answer looks like, including a tricky legitimate case and a 'need more data' case. It's like showing a new joiner three model answers. They come from a separate example library, never from our test cases, so our quality scores stay honest."

## Can you teach it?

- [ ] I can say when to use few-shot and when to fix the instructions instead
- [ ] I can explain eval leakage and how to prevent it with a test
- [ ] I can describe dynamic few-shot and its entitlement risk
