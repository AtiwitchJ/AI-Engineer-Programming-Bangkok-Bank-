"""Data Retriever agent — RAG search only; returns raw snippets."""

from __future__ import annotations

from langchain.agents import create_agent

from app.llm import get_llm
from app.tools.tool_search_knowledge import tool_search_knowledge

DATA_RETRIEVER_PROMPT = """You are an information retrieval specialist (RAG).
Your ONLY job is to find relevant raw text from the knowledge base.

Steps:
1. Call the tool_search_knowledge tool with a focused query derived from the user's request.
2. If needed, call the tool again with different keywords to collect ALL relevant snippets.
3. Reply with ONLY the raw relevant text snippets (no summary, no final answer).

Critical rules:
- Do NOT answer or summarize for the user yourself.
- Return only raw relevant text snippets from the tool results.
"""


def agent_data_retriever():
    """Build the Data Retriever agent with the tool_search_knowledge tool."""
    return create_agent(
        model=get_llm(),
        tools=[tool_search_knowledge],
        system_prompt=DATA_RETRIEVER_PROMPT,
        name="data_retriever",
    )
