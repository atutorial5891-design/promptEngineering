---
tags:
  - template
---

# Prompt Card: <name>

| Field | Value |
| --- | --- |
| **ID** | `domain.task.v1`. Must match the file name in `prompts/` |
| **Task** | What the prompt does, in one sentence |
| **Models tested** | e.g. Claude Sonnet 5.5, GPT-6 Sol, Gemini 3.8 Flash |
| **Techniques** | e.g. few-shot, XML tags, structured output |
| **Eval score** | metric = value on `evals/datasets/<file>` (date) |
| **Status** | experimental / stable / deprecated |

## Prompt

```text
<system>
...
</system>

<user>
{{ input }}
</user>
```

## Variables

| Name | Type | Description |
| --- | --- | --- |
| `input` | string | ... |

## Why it works

The design decisions and the alternatives you tried.

## Known failure cases

- ...

## Changelog

- v1 (YYYY-MM-DD): initial
