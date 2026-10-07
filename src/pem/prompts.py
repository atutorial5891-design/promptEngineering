"""Versioned prompt templates stored as YAML in prompts/.

File format:

    id: sentiment.few_shot.v1
    description: ...
    variables: [review]
    system: |
      ...           # optional, Jinja2
    user: |
      ... {{ review }} ...
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml
from jinja2 import Environment, StrictUndefined

PROMPTS_DIR = Path(__file__).resolve().parents[2] / "prompts"

_env = Environment(undefined=StrictUndefined, keep_trailing_newline=False, autoescape=False)


@dataclass(frozen=True)
class PromptTemplate:
    id: str
    user: str
    system: str | None = None
    description: str = ""
    variables: list[str] = field(default_factory=list)

    def render(self, **values: Any) -> list[dict[str, str]]:
        """Render to a chat messages list. Missing variables raise an error."""
        missing = [v for v in self.variables if v not in values]
        if missing:
            raise KeyError(f"Prompt {self.id} missing variables: {missing}")
        messages = []
        if self.system:
            messages.append({"role": "system", "content": _render(self.system, values)})
        messages.append({"role": "user", "content": _render(self.user, values)})
        return messages


def _render(template: str, values: dict[str, Any]) -> str:
    return _env.from_string(template).render(**values).strip()


def load_prompt(name_or_path: str | Path) -> PromptTemplate:
    """Load by file path, or by id/file stem from the top-level prompts/ directory."""
    path = Path(name_or_path)
    if path.suffix not in {".yaml", ".yml"}:
        path = PROMPTS_DIR / f"{name_or_path}.yaml"
    data = yaml.safe_load(path.read_text())
    return PromptTemplate(
        id=data["id"],
        user=data["user"],
        system=data.get("system"),
        description=data.get("description", ""),
        variables=list(data.get("variables", [])),
    )
