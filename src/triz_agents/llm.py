"""LLM provider selection for TRIZ Agents.

- Supports OpenAI, Google (Gemini), DeepSeek, and xAI (Grok) via LangChain chat wrappers.
- Fails gracefully with a clear error if a provider library isn’t installed.
"""

from __future__ import annotations

from typing import Any, Dict, Literal, Optional

# Optional typing for return type (avoid hard dependency during import)
try:
    from langchain_core.language_models.chat_models import BaseChatModel  # type: ignore
except Exception:  # pragma: no cover
    BaseChatModel = Any  # type: ignore

# --- Optional provider imports (graceful fallbacks) ---
try:
    from langchain_openai import ChatOpenAI  # OpenAI (gpt-4o, o3, etc.)
except Exception:  # pragma: no cover
    ChatOpenAI = None  # type: ignore

try:
    from langchain_google_genai import ChatGoogleGenerativeAI  # Google (Gemini)
except Exception:  # pragma: no cover
    ChatGoogleGenerativeAI = None  # type: ignore

try:
    from langchain_deepseek import ChatDeepSeek  # DeepSeek
except Exception:  # pragma: no cover
    ChatDeepSeek = None  # type: ignore

try:
    from langchain_xai import ChatXAI  # xAI (Grok)
except Exception:  # pragma: no cover
    ChatXAI = None  # type: ignore


# ----------------------------
# Model → Provider mapping
# ----------------------------
MODEL_PROVIDER_MAP: Dict[str, Optional[type]] = {
    # Google Gemini
    "gemini-1.5-flash": ChatGoogleGenerativeAI,
    "gemini-1.5-pro": ChatGoogleGenerativeAI,
    "gemini-2.5-flash": ChatGoogleGenerativeAI,
    "gemini-2.5-pro": ChatGoogleGenerativeAI,
    # OpenAI
    "o1": ChatOpenAI,              # reasoning model, often ignores temperature
    "o3": ChatOpenAI,              # reasoning model
    "gpt-4o": ChatOpenAI,
    "gpt-4o-mini": ChatOpenAI,
    "gpt-4.1": ChatOpenAI,
    "gpt-4.1-mini": ChatOpenAI,
    "o4-mini": ChatOpenAI,         # often ignores temperature
    # DeepSeek
    "deepseek-chat": ChatDeepSeek,
    # xAI
    "grok-3": ChatXAI,
    "grok-3-mini": ChatXAI,
}

# The type hint is generated from the keys of our dictionary
ModelName = Literal[
    "gemini-1.5-flash", "gemini-1.5-pro", "gemini-2.5-flash", "gemini-2.5-pro",
    "gpt-4o", "gpt-4o-mini", "o3", "o1", "gpt-4.1", "gpt-4.1-mini", "o4-mini",
    "deepseek-chat",
    "grok-3", "grok-3-mini",
]


def _ensure_available(model_name: str) -> type:
    """Return the provider class for `model_name` or raise a helpful error."""
    model_class = MODEL_PROVIDER_MAP.get(model_name)
    if model_class is None:
        # Figure out which provider library is likely needed to help the user
        provider_hint = "the appropriate provider library"
        if model_name.startswith("gpt") or model_name in {"o1", "o3", "o4-mini"}:
            provider_hint = "langchain_openai"
        elif model_name.startswith("gemini"):
            provider_hint = "langchain_google_genai"
        elif model_name.startswith("deepseek"):
            provider_hint = "langchain_deepseek"
        elif model_name.startswith("grok"):
            provider_hint = "langchain_xai"

        raise ImportError(
            f"Model '{model_name}' is not available. Install {provider_hint} and ensure credentials are set."
        )
    return model_class


def get_llm(
    model: ModelName | str = "gpt-4o",
    temperature: float = 0.0,
    **kwargs: Any,
) -> BaseChatModel:
    """Instantiate and return a LangChain ChatModel.

    Args:
        model: Model name (see `ModelName` for supported values).
        temperature: Sampling temperature (some reasoning models may ignore this).
        **kwargs: Extra keyword args forwarded to the underlying chat model.
                  Useful for things like `timeout`, `max_tokens`, etc.

    Returns:
        A LangChain `BaseChatModel` instance.

    Raises:
        ImportError: If the mapped provider class isn’t installed/available.
    """
    # Back-compat: allow callers who used `model_name=` in older code
    model_name = kwargs.pop("model_name", model)

    model_class = _ensure_available(str(model_name))

    # Some models (e.g., o1, o4-mini) often ignore temperature or require special params.
    no_temp_models = {"o1", "o4-mini"}
    init_kwargs = {"model": model_name, **kwargs}
    if str(model_name) not in no_temp_models:
        init_kwargs["temperature"] = temperature

    # Optional: print a one-liner for visibility during dev
    print(f"--- ⚙️  Instantiating model: {model_name} ---")

    return model_class(**init_kwargs)  # type: ignore[arg-type]


__all__ = ["ModelName", "get_llm"]
