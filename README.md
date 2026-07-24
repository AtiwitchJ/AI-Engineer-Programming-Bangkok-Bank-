# Agentic AI + RAG Demo

Bangkok Bank AI Engineer Programming Test — multi-agent RAG system with a sequential workflow:

```text
User → Data Retriever (tool_search_knowledge) → Report Generator → Answer
```

## Requirements

- Python `>= 3.11`
- An OpenAI-compatible LLM endpoint (API key required)
- [uv](https://github.com/astral-sh/uv) (recommended) or pip

## Setup

```bash
# from the AI-Engineer-Programming-Test/ directory
uv sync
cp .env.example .env
```

Edit `.env` and set:

| Variable | Meaning | Example |
|----------|---------|---------|
| `PROVIDER_BASE_URL` | OpenAI-compatible API base URL | `https://ollama.com/v1` |
| `PROVIDER_MODEL` | Model id available on that provider | `gpt-oss:20b` |
| `PROVIDER_API_KEY` | API key / bearer token | `...` |

All three variables are required.

## Run

```bash
# sample query from the test brief
uv run python main.py

# custom queries
uv run python main.py "What is the policy on international travel?"
uv run python main.py "What is the interest rate on SmartSave?"
uv run python main.py "How many hours do domestic cats sleep?"
```

## Project layout

```text
AI-Engineer-Programming-Test/
├── main.py                           # CLI entry point
├── knowledge_base.txt                # Local knowledge base
├── .env.example                      # Provider env template
├── pyproject.toml
└── app/
    ├── llm.py                        # Shared ChatOpenAI client
    ├── workflow.py                   # Sequential agent orchestration
    ├── tools/
    │   └── tool_search_knowledge.py  # Keyword search tool (@tool)
    └── agents/
        ├── agent_data_retriever.py   # RAG retriever agent
        └── agent_report_generator.py # Final answer writer agent
```

## Architecture

| Piece | Choice |
|-------|--------|
| Framework | LangChain |
| Orchestration | Sequential calls: Data Retriever → Report Generator |
| LLM | OpenAI-compatible API via `langchain-openai` (`ChatOpenAI`) |
| RAG | Custom `tool_search_knowledge` reading `knowledge_base.txt` |
| Search | Simple keyword match with stopword filtering |

### Agent roles

- **Data Retriever** — calls `tool_search_knowledge`, returns raw relevant snippets only (does not answer the user)
- **Report Generator** — synthesizes snippets into a clear bullet-point answer (no tools)

## Knowledge base topics

`knowledge_base.txt` currently includes:

1. Company international travel policy
2. SmartSave savings account product
3. General facts about domestic cats# AI-Engineer-Programming-Bangkok-Bank-
