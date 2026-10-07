"""Minimal eval runner: dataset -> predictions -> scores -> report."""

from __future__ import annotations

import json
from collections import defaultdict
from collections.abc import Callable
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from pydantic import BaseModel, Field

Example = dict[str, Any]
Scorer = Callable[[Example, str], float]


def load_jsonl(path: str | Path) -> list[Example]:
    lines = Path(path).read_text().splitlines()
    return [json.loads(line) for line in lines if line.strip()]


def normalize(text: str) -> str:
    return text.strip().strip(".").strip().lower()


def exact_match(example: Example, output: str, key: str = "label") -> float:
    return float(normalize(output) == normalize(str(example[key])))


@dataclass
class EvalReport:
    name: str
    rows: list[dict[str, Any]] = field(default_factory=list)

    @property
    def scores(self) -> dict[str, float]:
        totals: dict[str, list[float]] = defaultdict(list)
        for row in self.rows:
            for metric, value in row["scores"].items():
                totals[metric].append(value)
        return {m: sum(v) / len(v) for m, v in totals.items() if v}

    def per_label(self, metric: str, label_key: str = "label") -> dict[str, float]:
        """Mean of a metric grouped by gold label (e.g., per-class recall for exact_match)."""
        groups: dict[str, list[float]] = defaultdict(list)
        for row in self.rows:
            groups[str(row["example"][label_key])].append(row["scores"][metric])
        return {label: sum(v) / len(v) for label, v in sorted(groups.items())}

    def failures(self, metric: str) -> list[dict[str, Any]]:
        return [r for r in self.rows if r["scores"].get(metric, 1.0) < 1.0]

    def summary(self) -> str:
        parts = [f"{m}={v:.3f}" for m, v in self.scores.items()]
        return f"{self.name}: n={len(self.rows)} " + " ".join(parts)


def run_eval(
    name: str,
    dataset: list[Example],
    predict: Callable[[Example], str],
    scorers: dict[str, Scorer],
) -> EvalReport:
    report = EvalReport(name=name)
    for example in dataset:
        output = predict(example)
        scores = {metric: scorer(example, output) for metric, scorer in scorers.items()}
        report.rows.append({"example": example, "output": output, "scores": scores})
    return report


class JudgeVerdict(BaseModel):
    reasoning: str = Field(description="Brief critique against the rubric, citing the output.")
    passed: bool = Field(description="True only if the output meets every rubric criterion.")


def llm_judge(rubric: str, *, model: str | None = None, input_key: str = "input") -> Scorer:
    """Build a pass/fail LLM-as-judge scorer. Validate it against human labels before trusting it."""
    from pem.llm import complete_structured

    def score(example: Example, output: str) -> float:
        prompt = (
            "You are grading an AI output against a rubric.\n\n"
            f"<rubric>\n{rubric}\n</rubric>\n\n"
            f"<input>\n{example.get(input_key, '')}\n</input>\n\n"
            f"<output>\n{output}\n</output>\n\n"
            "Critique first, then decide pass/fail."
        )
        verdict = complete_structured(prompt, JudgeVerdict, model=model or _judge_model())
        return float(verdict.passed)

    return score


def _judge_model() -> str | None:
    import os

    from pem.llm import _load_env

    _load_env()
    return os.getenv("PEM_JUDGE_MODEL") or None
