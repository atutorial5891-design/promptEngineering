from pathlib import Path

import pytest

from pem.evals import exact_match, load_jsonl, run_eval
from pem.prompts import PROMPTS_DIR, load_prompt

ROOT = Path(__file__).resolve().parents[1]


def test_all_prompts_load_and_ids_match_filenames():
    files = sorted(PROMPTS_DIR.glob("*.yaml"))
    assert files
    for path in files:
        prompt = load_prompt(path)
        assert prompt.id == path.stem


def test_render_fills_variables_and_rejects_missing():
    prompt = load_prompt("sentiment.few_shot.v1")
    messages = prompt.render(review="Great value.")
    assert [m["role"] for m in messages] == ["system", "user"]
    assert "Great value." in messages[-1]["content"]
    with pytest.raises(KeyError):
        prompt.render()


def test_eval_runner_scores_and_groups_by_label():
    dataset = load_jsonl(ROOT / "evals" / "datasets" / "sentiment.jsonl")
    scorers = {"accuracy": exact_match}
    report = run_eval("oracle", dataset, lambda ex: f" {ex['label'].upper()}. ", scorers)
    assert report.scores["accuracy"] == 1.0
    assert set(report.per_label("accuracy")) == {"positive", "negative", "mixed"}

    report = run_eval("constant", dataset, lambda ex: "positive", scorers)
    assert report.per_label("accuracy")["positive"] == 1.0
    assert report.per_label("accuracy")["negative"] == 0.0
    assert len(report.failures("accuracy")) == 20


def test_few_shot_examples_not_in_eval_set():
    dataset = {ex["input"] for ex in load_jsonl(ROOT / "evals" / "datasets" / "sentiment.jsonl")}
    prompt_text = load_prompt("sentiment.few_shot.v1").user
    assert not any(review in prompt_text for review in dataset)
