# Cheat Sheet

A one-page reminder for writing and debugging prompts.

## Before writing

- [ ] What's the **outcome**, who is the **audience**, and what's the **purpose**?
- [ ] Do I have **5-20 test inputs**, including hard cases, and a way to score them?
- [ ] Which **model type** am I targeting: instruct, reasoning, or small/open?

## Writing checklist

1. Role and goal: concrete context, not just a title.
2. The context the model can't guess: date, domain rules, user info.
3. Instructions: positive, specific, with a priority order and the *why*.
4. Examples: 1-5 diverse ones, balanced across labels, clearly delimited.
5. Output: a schema or exact format; nullable fields for missing data.
6. Data: delimited, and marked as data. Long documents go **first**, the question **last**.
7. Success criteria and stop conditions, especially for agents and reasoning models.
8. Static content first and dynamic content last, for caching.

## Debugging: symptom to fix

| Symptom | First thing to try |
| --- | --- |
| Generic, bland output | Add the audience, purpose, quality bar, and examples |
| Ignores a rule | Check for contradictions. Make the rule positive and explain the why. Move it to the end |
| Wrong format | Use schema-constrained output |
| Makes things up | Ground it in sources, allow abstention, use quote-first |
| Copies the examples too closely | Diversify the examples, and say they're illustrative |
| Inconsistent between runs | Lower temperature (if allowed). Clarify ambiguous criteria. Evaluate on more samples |
| Too slow or expensive | Smaller model, lower effort, shorter output, caching, routing |
| Overthinks simple tasks | Lower the effort, and add clear stopping criteria |
| Agent loops or stops early | Max steps, explicit success criteria, a verification step |
| Follows instructions found in documents | Delimit the data, add architectural defenses ([20](../modules/20-prompt-security/index.md)) |

## Reasoning models: do and don't

| Do | Don't |
| --- | --- |
| State the goal, constraints, success criteria, and evidence | Script every step |
| Tune the effort setting with evals | Add "think step by step" or tune temperature |
| Give a generous output budget | Ask it to reveal its raw chain of thought |
| Remove contradictions | Stack ALL-CAPS absolute rules |
