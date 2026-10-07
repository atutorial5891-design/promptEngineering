"""Provider-agnostic LLM calls via LiteLLM.

Model strings use LiteLLM's "provider/model" format and default to $PEM_MODEL.
API keys are read from the environment (load them from .env).
"""

from __future__ import annotations

import json
import os
from typing import Any

from pydantic import BaseModel, ValidationError

Messages = list[dict[str, Any]]


def _load_env() -> None:
    try:
        from dotenv import load_dotenv
    except ImportError:
        return
    load_dotenv()


def default_model() -> str:
    _load_env()
    model = os.getenv("PEM_MODEL")
    if not model:
        raise RuntimeError("Set PEM_MODEL in .env (see .env.example) or pass model=...")
    return model


def _as_messages(prompt: str | Messages, system: str | None = None) -> Messages:
    messages: Messages = [{"role": "user", "content": prompt}] if isinstance(prompt, str) else list(prompt)
    if system:
        messages = [{"role": "system", "content": system}, *messages]
    return messages


def complete(
    prompt: str | Messages,
    *,
    system: str | None = None,
    model: str | None = None,
    **kwargs: Any,
) -> str:
    """Return the text of a single completion.

    Extra kwargs (temperature, max_tokens, reasoning_effort, ...) are passed to LiteLLM.
    Reasoning models may reject sampling params; omit them there.
    """
    import litellm

    response = litellm.completion(
        model=model or default_model(),
        messages=_as_messages(prompt, system),
        **kwargs,
    )
    return response.choices[0].message.content or ""


def complete_structured[T: BaseModel](
    prompt: str | Messages,
    schema: type[T],
    *,
    system: str | None = None,
    model: str | None = None,
    max_retries: int = 2,
    **kwargs: Any,
) -> T:
    """Return a validated Pydantic object, retrying with the validation error on failure."""
    import litellm

    messages = _as_messages(prompt, system)
    last_error: Exception | None = None
    for _ in range(max_retries + 1):
        response = litellm.completion(
            model=model or default_model(),
            messages=messages,
            response_format=schema,
            **kwargs,
        )
        content = response.choices[0].message.content or ""
        try:
            return schema.model_validate(json.loads(content))
        except (json.JSONDecodeError, ValidationError) as exc:
            last_error = exc
            messages = [
                *messages,
                {"role": "assistant", "content": content},
                {
                    "role": "user",
                    "content": f"That output was invalid: {exc}. Return only valid JSON for the schema.",
                },
            ]
    raise ValueError(f"No valid {schema.__name__} after {max_retries + 1} attempts") from last_error
