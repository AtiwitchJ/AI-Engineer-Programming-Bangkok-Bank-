"""Tool: tool_search_knowledge — simple keyword RAG over the local knowledge base."""

from __future__ import annotations

import re
from pathlib import Path

from langchain_core.tools import tool

# knowledge_base.txt lives at the project root (two levels above this file).
KNOWLEDGE_BASE_PATH = Path(__file__).resolve().parents[2] / "knowledge_base.txt"

STOPWORDS = {
    "a",
    "an",
    "the",
    "is",
    "are",
    "was",
    "were",
    "what",
    "which",
    "who",
    "whom",
    "on",
    "in",
    "at",
    "to",
    "for",
    "of",
    "and",
    "or",
    "do",
    "does",
    "did",
    "how",
    "about",
}


def tool_search_knowledge_base(query: str) -> str:
    """Read knowledge_base.txt and return paragraphs that match query keywords.

    Uses a simple regex keyword search (case-insensitive).
    """
    if not KNOWLEDGE_BASE_PATH.exists():
        return "ERROR: knowledge_base.txt not found."

    text = KNOWLEDGE_BASE_PATH.read_text(encoding="utf-8")
    paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]

    keywords = split_keywords(query)
    if not keywords:
        return "\n\n".join(paragraphs)

    matched: list[str] = []
    for paragraph in paragraphs:
        if any(
            re.search(rf"\b{re.escape(keyword)}\b", paragraph, re.IGNORECASE)
            for keyword in keywords
        ):
            matched.append(paragraph)

    if not matched:
        return "No relevant snippets found in the knowledge base."

    return "\n\n".join(matched)


def split_keywords(query: str) -> list[str]:
    """Pull meaningful word tokens from the query via regex."""
    tokens = re.findall(r"[A-Za-z0-9]+", query.lower())
    return [token for token in tokens if token not in STOPWORDS and len(token) >= 2]


@tool
def tool_search_knowledge(query: str) -> str:
    """Search the local knowledge base for snippets relevant to the query.

    Args:
        query: Keywords or a short description of what to look up.

    Returns:
        Raw relevant text snippets from knowledge_base.txt.
    """
    return tool_search_knowledge_base(query)
