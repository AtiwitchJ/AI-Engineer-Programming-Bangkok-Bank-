"""Sequential LangChain workflow: Data Retriever → Report Generator."""

from __future__ import annotations

from app.agents.agent_data_retriever import agent_data_retriever
from app.agents.agent_report_generator import agent_report_generator


def run_workflow(query: str) -> str:
    """Run Data Retriever, then pass snippets to Report Generator."""
    # Step 1: Data Retriever (RAG tool) → raw snippets
    retriever = agent_data_retriever()
    retrieve_result = retriever.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": (
                        "Find ALL knowledge-base snippets relevant to this "
                        f"question:\n{query}"
                    ),
                }
            ]
        }
    )
    snippets = retrieve_result["messages"][-1].content

    # Step 2: Report Generator → final answer
    generator = agent_report_generator()
    generate_result = generator.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": (
                        f"User question:\n{query}\n\n"
                        f"Retrieved snippets:\n{snippets}\n\n"
                        "Write the final answer for the user."
                    ),
                }
            ]
        }
    )
    return generate_result["messages"][-1].content
