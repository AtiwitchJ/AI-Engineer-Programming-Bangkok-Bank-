"""Entry point: sequential multi-agent workflow (Retriever -> Report Generator)."""

from __future__ import annotations

import argparse
import os
import sys
import urllib.error
import urllib.request

from dotenv import load_dotenv

from app.workflow import run_workflow

DEFAULT_QUERY = "What is the policy on international travel?"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Multi-agent RAG demo (LangChain): "
        "Data Retriever -> Report Generator"
    )
    parser.add_argument(
        "query",
        nargs="?",
        default=DEFAULT_QUERY,
        help="User question to ask the agent system",
    )
    return parser.parse_args()


def ensure_provider() -> None:
    """Load env and verify PROVIDER_* settings are present."""
    load_dotenv()

    base_url = os.getenv("PROVIDER_BASE_URL")
    model = os.getenv("PROVIDER_MODEL")
    api_key = os.getenv("PROVIDER_API_KEY")
    if not base_url or not model or not api_key:
        print(
            "Missing PROVIDER_BASE_URL, PROVIDER_MODEL, or PROVIDER_API_KEY.\n"
            "Copy .env.example to .env and set all values.",
            file=sys.stderr,
        )
        sys.exit(1)


def main() -> None:
    args = parse_args()
    ensure_provider()

    # Avoid Windows console UnicodeEncodeError when printing answers.
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    print("=" * 60)
    print("Query:", args.query)
    print("Model:", os.getenv("PROVIDER_MODEL"))
    print("=" * 60)

    answer = run_workflow(args.query)

    print("\nFinal Answer\n" + "-" * 60)
    print(answer)
    print("-" * 60)


if __name__ == "__main__":
    main()
