"""Report Generator agent — synthesizes retrieved snippets into a final answer."""

from __future__ import annotations

from langchain.agents import create_agent

from app.llm import get_llm

REPORT_GENERATOR_PROMPT = """You are an expert writer and information synthesizer.
You receive raw text snippets retrieved from a knowledge base.
Your job is to produce a complete, clear, non-redundant, and well-formatted
answer for the end user.

Rules:
- Use ONLY the provided snippets. Do not invent facts.
- If snippets are insufficient, say what is missing.
- Write in the same language as the user's question.
- Always format the answer as bullet points.
- Keep each bullet concise and focused on one idea.
- Do not mention internal agent names or tool calls.
"""


def agent_report_generator():
    """Build the Report Generator agent (no tools)."""
    return create_agent(
        model=get_llm(),
        system_prompt=REPORT_GENERATOR_PROMPT,
        name="report_generator",
    )
