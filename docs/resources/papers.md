# Papers

The research behind each technique, grouped by module. **Start with the surveys.**

**How to read a paper here:**

1. Read the abstract and look at Figure 1.
2. Find the exact prompt the authors used, usually in the appendix.
3. Re-run it in a lab.
4. Note whether it still helps on current models. Many 2022 and 2023 gains shrink on reasoning models.

## Surveys (start here)

- [The Prompt Report: A Systematic Survey of Prompting Techniques](https://arxiv.org/abs/2406.06608) (Schulhoff et al., 2024). A taxonomy of 58 text prompting techniques, with vocabulary and best practices. Supports all modules.
- [Lilian Weng: Prompt Engineering](https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/) (2023). A dense, well-cited overview.

## In-context learning (module 03)

- [Language Models are Few-Shot Learners](https://arxiv.org/abs/2005.14165) (Brown et al., 2020). The GPT-3 paper that introduced few-shot prompting.
- [Calibrate Before Use](https://arxiv.org/abs/2102.09690) (Zhao et al., 2021). The order of examples and majority-label bias change results.
- [Rethinking the Role of Demonstrations](https://arxiv.org/abs/2202.12837) (Min et al., 2022). Format and label space matter more than whether the labels are correct.
- [Many-Shot In-Context Learning](https://arxiv.org/abs/2404.11018) (Agarwal et al., 2024). Hundreds of examples in long context windows.

## Prompt format and sensitivity (modules 04, 05)

- [Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design](https://arxiv.org/abs/2310.11324) (Sclar et al., 2023). Formatting alone can swing accuracy a lot, so always evaluate.
- [Let Me Speak Freely?](https://arxiv.org/abs/2408.02442) (Tam et al., 2024). Strict format constraints can hurt reasoning. Reason first, then format.

## Decomposition and chaining (module 06)

- [Least-to-Most Prompting](https://arxiv.org/abs/2205.10625) (Zhou et al., 2022)
- [Self-Ask / Measuring the Compositionality Gap](https://arxiv.org/abs/2210.03350) (Press et al., 2022)
- [Plan-and-Solve Prompting](https://arxiv.org/abs/2305.04091) (Wang et al., 2023)

## Reasoning (modules 07, 08, 09)

- [Chain-of-Thought Prompting Elicits Reasoning](https://arxiv.org/abs/2201.11903) (Wei et al., 2022)
- [Large Language Models are Zero-Shot Reasoners](https://arxiv.org/abs/2205.11916) (Kojima et al., 2022). The paper behind "Let's think step by step".
- [Self-Consistency](https://arxiv.org/abs/2203.11171) (Wang et al., 2022)
- [Tree of Thoughts](https://arxiv.org/abs/2305.10601) (Yao et al., 2023)
- [Graph of Thoughts](https://arxiv.org/abs/2308.09687) (Besta et al., 2023)
- [Take a Step Back](https://arxiv.org/abs/2310.06117) (Zheng et al., 2023)
- [Self-Refine](https://arxiv.org/abs/2303.17651) (Madaan et al., 2023)
- [Reflexion](https://arxiv.org/abs/2303.11366) (Shinn et al., 2023)
- [Chain-of-Verification](https://arxiv.org/abs/2309.11495) (Dhuliawala et al., 2023). Reduces hallucination by planning verification questions.
- [Let's Verify Step by Step](https://arxiv.org/abs/2305.20050) (Lightman et al., 2023). Process supervision, background for how reasoning models are trained.

## Context, retrieval, and memory (modules 10, 11, 12)

- [Retrieval-Augmented Generation for Knowledge-Intensive NLP](https://arxiv.org/abs/2005.11401) (Lewis et al., 2020)
- [Lost in the Middle](https://arxiv.org/abs/2307.03172) (Liu et al., 2023). Models use information at the start and end of the context better than the middle.
- [Large Language Models Can Be Easily Distracted by Irrelevant Context](https://arxiv.org/abs/2302.00093) (Shi et al., 2023)
- [Context Rot (Chroma research)](https://www.trychroma.com/research/context-rot) (2025). Performance drops as input length grows, even on simple tasks.
- [MemGPT](https://arxiv.org/abs/2310.08560) (Packer et al., 2023). Memory managed like an operating system manages it.
- [Generative Agents](https://arxiv.org/abs/2304.03442) (Park et al., 2023). Memory streams, reflection, and planning.

## Tools and agents (modules 14, 15, 17)

- [ReAct](https://arxiv.org/abs/2210.03629) (Yao et al., 2022)
- [Toolformer](https://arxiv.org/abs/2302.04761) (Schick et al., 2023)

## Evaluation (module 18)

- [Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena](https://arxiv.org/abs/2306.05685) (Zheng et al., 2023). Judge biases: position, verbosity, and self-preference.
- [G-Eval](https://arxiv.org/abs/2303.16634) (Liu et al., 2023). Using chain-of-thought and form-filling for LLM judges.
- [Who Validates the Validators?](https://arxiv.org/abs/2404.12272) (Shankar et al., 2024). Aligning LLM judges with human preferences, including how evaluation criteria shift over time.

## Prompt optimization (module 19)

- [Large Language Models Are Human-Level Prompt Engineers (APE)](https://arxiv.org/abs/2211.01910) (Zhou et al., 2022)
- [Large Language Models as Optimizers (OPRO)](https://arxiv.org/abs/2309.03409) (Yang et al., 2023)
- [DSPy](https://arxiv.org/abs/2310.03714) (Khattab et al., 2023)
- [MIPRO: Optimizing Instructions and Demonstrations](https://arxiv.org/abs/2406.11695) (Opsahl-Ong et al., 2024)
- [TextGrad](https://arxiv.org/abs/2406.07496) (Yuksekgonul et al., 2024)
- [GEPA: Reflective Prompt Evolution](https://arxiv.org/abs/2507.19457) (Agrawal et al., 2025)

## Security (module 20)

- [Not What You've Signed Up For: Indirect Prompt Injection](https://arxiv.org/abs/2302.12173) (Greshake et al., 2023)
- [Prompt Injection Attack against LLM-integrated Applications](https://arxiv.org/abs/2306.05499) (Liu et al., 2023)
- [Universal and Transferable Adversarial Attacks](https://arxiv.org/abs/2307.15043) (Zou et al., 2023)
- [The Instruction Hierarchy](https://arxiv.org/abs/2404.13208) (Wallace et al., 2024)
- [Defeating Prompt Injections by Design (CaMeL)](https://arxiv.org/abs/2503.18813) (Debenedetti et al., 2025)
- [Design Patterns for Securing LLM Agents against Prompt Injections](https://arxiv.org/abs/2506.08837) (Beurer-Kellner et al., 2025)
