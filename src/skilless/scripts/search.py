#!/usr/bin/env python3
"""Search tool - Web search via Exa MCP or Tavily."""

from __future__ import annotations

import asyncio
import json
import os
import sys

try:
    from skilless.scripts.base import BaseTool, DoctorResult
except ImportError:
    from base import BaseTool, DoctorResult


def _get_search_provider() -> str:
    """Return the active search provider name ('tavily' or 'exa')."""
    provider = os.environ.get("SEARCH_PROVIDER", "").lower()
    if provider == "tavily":
        return "tavily"
    if os.environ.get("TAVILY_API_KEY") and provider != "exa":
        return "tavily"
    return "exa"


class SearchTool(BaseTool):
    name = "search"
    description = "AI semantic web search via Exa or Tavily"
    usage = "cd ~/.agents/skills/skilless/ && uv run scripts/search.py <query> [num_results]"
    how = "Connects to the Exa MCP endpoint via FastMCP or uses Tavily API for semantic search"

    MCP_URL = "https://mcp.exa.ai/mcp"

    def doctor(self) -> DoctorResult:
        provider = _get_search_provider()
        if provider == "tavily":
            return self._doctor_tavily()
        return self._doctor_exa()

    def _doctor_tavily(self) -> DoctorResult:
        try:
            from tavily import TavilyClient

            client = TavilyClient()
            # Quick connectivity check with minimal results
            client.search(query="test", max_results=1)
            return DoctorResult("OK", "Tavily API connected")
        except ImportError:
            return DoctorResult("OFF", "tavily-python not installed")
        except Exception as e:
            return DoctorResult("FAIL", f"Tavily error: {str(e)[:50]}")

    def _doctor_exa(self) -> DoctorResult:
        async def _check():
            try:
                from fastmcp import Client
                from fastmcp.client.transports import StreamableHttpTransport

                client = Client(StreamableHttpTransport(self.MCP_URL))
                async with client:
                    tools = await client.list_tools()
                    if any("search" in t.name.lower() for t in tools):
                        names = ", ".join(t.name for t in tools[:3])
                        return DoctorResult("OK", f"connected, tools: {names}...")
                    return DoctorResult("FAIL", "search tool not found in Exa MCP")
            except ImportError:
                return DoctorResult("OFF", "fastmcp not installed")
            except Exception as e:
                return DoctorResult("FAIL", f"connection failed: {str(e)[:50]}")

        return asyncio.run(_check())

    def run(self, args: list[str]) -> str:
        if not args:
            raise ValueError("Usage: cd ~/.agents/skills/skilless/ && uv run scripts/search.py <query> [num_results]")

        query = args[0]
        num_results = int(args[1]) if len(args) > 1 else 5

        provider = _get_search_provider()
        if provider == "tavily":
            return self._run_tavily(query, num_results)
        return self._run_exa(query, num_results)

    def _run_tavily(self, query: str, num_results: int) -> str:
        from tavily import TavilyClient

        client = TavilyClient()
        response = client.search(
            query=query,
            max_results=num_results,
            search_depth="advanced",
        )

        # Normalize to match Exa-style output shape
        results = []
        for r in response.get("results", []):
            results.append({
                "title": r.get("title", ""),
                "url": r.get("url", ""),
                "snippet": r.get("content", ""),
                "score": r.get("score", 0),
            })
        return json.dumps(results, indent=2)

    def _run_exa(self, query: str, num_results: int) -> str:
        async def _search():
            from fastmcp import Client
            from fastmcp.client.transports import StreamableHttpTransport

            client = Client(StreamableHttpTransport(self.MCP_URL))
            async with client:
                result = await client.call_tool(
                    "web_search_exa", {"query": query, "numResults": num_results}
                )
                return str(result)

        return asyncio.run(_search())

    @property
    def troubleshooting(self) -> list[tuple[str, str]]:
        from pathlib import Path
        _venv = Path.home() / ".agents/skills/skilless/.venv"
        _pip = f"uv pip install --python {_venv}"
        return [
            ("fastmcp not installed", f"Run: {_pip} fastmcp"),
            ("tavily-python not installed", f"Run: {_pip} tavily-python"),
            ("Connection failed", "Check network; verify Exa MCP endpoint is reachable"),
            ("Tavily error", "Check TAVILY_API_KEY is set correctly"),
            ("Rate limited", "Wait a moment and retry; Exa free tier has rate limits"),
        ]


def main():
    tool = SearchTool()
    try:
        print(tool.run(sys.argv[1:]))
    except (ValueError, RuntimeError) as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
