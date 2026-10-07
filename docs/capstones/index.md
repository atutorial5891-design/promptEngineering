# Capstones

These are practice projects that combine several modules. They live in this repo under `labs/capstones/`. They're for learning, not production. Each one ends with an eval report in the journal.

## Capstone A: Evaluated support bot

**Modules:** 03, 04, 05, 11, 18 · **After:** week 7

- **Build:** a support assistant for a fictional product that answers from a docs folder.
- **Requirements:**
    - Grounded answers with citations.
    - Abstains when the docs don't contain the answer.
    - Structured ticket triage for questions it can't answer.
- **Evals:**
    - 40 or more questions, at least 25% of them unanswerable.
    - Faithfulness judge, validated against your own labels.
    - Triage accuracy.
- **Done when:** abstention is at least 90% correct, faithfulness is at least 95%, and the eval runs with one command.

## Capstone B: Research agent with tools

**Modules:** 14, 15, 20 · **After:** week 10

- **Build:** a ReAct agent with tools to search local notes, fetch a URL, and write a report.
- **Requirements:**
    - Max-step and budget limits.
    - Progress notes.
    - An injection-resistant design: some test pages contain hidden instructions.
- **Evals:**
    - Task success on 15 research tasks.
    - Attack success rate on 10 injected pages, measured before and after adding defenses.
- **Done when:** task success is at least 80%, and the attack success rate after defenses is 0 out of 10.

## Capstone C: Prompt optimizer with DSPy

**Modules:** 18, 19 · **After:** week 11

- **Build:** take the lab 03 classifier (or Capstone A's triage) and optimize it with DSPy.
- **Requirements:**
    - Held-out evaluation.
    - A comparison against your best hand-written prompt.
    - A cost report for the optimization run.
- **Done when:** a write-up shows whether optimization beat manual prompting, and why.
