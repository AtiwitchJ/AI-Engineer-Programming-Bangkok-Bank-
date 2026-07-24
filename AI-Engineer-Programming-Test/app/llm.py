"""Shared LLM client (LangChain)."""

from __future__ import annotations

import os

from langchain_openai import ChatOpenAI


def get_llm() -> ChatOpenAI:
    """Create the chat model used by both agents."""
    return ChatOpenAI(
        model=os.getenv("PROVIDER_MODEL"),
        base_url=os.getenv("PROVIDER_BASE_URL"),
        api_key=os.getenv("PROVIDER_API_KEY"),
        temperature=0,
    )
