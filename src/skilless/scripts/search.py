#!/usr/bin/env python3
"""Search tool - Web search via Exa MCP or Tavily."""

from __future__ import annotations

import asyncio
import os
import sys

try:
    from skilless.scripts.base import BaseTool, DoctorResult
except ImportError:
    from base import BaseTool, DoctorResult


def _get_search_provider() -> str:
    """Return the active search provider ('exa' or 'tavily')."""
    provider = os.environ.get("SEARCH_PROVIDER", "").lower()
    if provider in ("exa", "tavily"):
        return provider
    # Auto-detect: if TAVILY_API_KEY is set and no explicit provider, use tavily
    if os.environ.get("TAVILY_API_KEY"):
        return "tavily"
    return "exa"


class SearchTool(BaseTool):
    name = "search"
    description = "AI semantic web search via Exa or Tavily"
    usage = "cd ~/.agents/skills/skilless/ && uv run scripts/search.py <query> [num_results]"
    how = "Connects to Exa MCP or Tavily API for semantic search (set SEARCH_PROVIDER=tavily to use Tavily)"

    MCP_URL = "https://mcp.exa.ai/mcp"

    def doctor(self) -> DoctorResult:
        provider = _get_search_provider()

        if provider == "tavily":
            return self._doctor_tavily()
        return self._doctor_exa()

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
                        return DoctorResult("OK", f"[exa] connected, tools: {names}...")
                    return DoctorResult("FAIL", "[exa] search tool not found in Exa MCP")
            except ImportError:
                return DoctorResult("OFF", "[exa] fastmcp not installed")
            except Exception as e:
                return DoctorResult("FAIL", f"[exa] connection failed: {str(e)[:50]}")

        return asyncio.run(_check())

    def _doctor_tavily(self) -> DoctorResult:
        try:
            from tavily import TavilyClient
        except ImportError:
            return DoctorResult("OFF", "[tavily] tavily-python not installed")

        api_key = os.environ.get("TAVILY_API_KEY")
        if not api_key:
            return DoctorResult("FAIL", "[tavily] TAVILY_API_KEY env var not set")

        if not api_key.startswith("tvly-"):
            return DoctorResult("FAIL", "[tavily] TAVILY_API_KEY looks malformed (expected 'tvly-' prefix)")

        try:
            client = TavilyClient(api_key=api_key)
            # Perform a simple, low-cost search to verify API key and connectivity.
            client.search(query="Tavily API test", search_depth="basic", max_results=1)
            return DoctorResult("OK", "[tavily] API key is valid and connection successful")
        except Exception as e:
            return DoctorResult("FAIL", f"[tavily] API call failed: {str(e)[:100]}")

    def run(self, args: list[str]) -> str:
        if not args:
            raise ValueError("Usage: cd ~/.agents/skills/skilless/ && uv run scripts/search.py <query> [num_results]")

        query = args[0]
        num_results = int(args[1]) if len(args) > 1 else 5
        provider = _get_search_provider()

        if provider == "tavily":
            return self._run_tavily(query, num_results)
        return self._run_exa(query, num_results)

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

    def _run_tavily(self, query: str, num_results: int) -> str:
        try:
            from tavily import TavilyClient

            client = TavilyClient()
            response = client.search(query=query, max_results=num_results, search_depth="basic")
        except Exception as e:
            raise RuntimeError(f"Tavily search failed: {e}") from e

        results = response.get("results", [])
        if not results:
            return "No results found."
        lines = []
        for r in results:
            lines.append(f"**{r.get('title', 'Untitled')}**")
            lines.append(f"URL: {r.get('url', '')}")
            if r.get("content"):
                lines.append(r["content"])
            lines.append("")
        return "\n".join(lines)

    @property
    def troubleshooting(self) -> list[tuple[str, str]]:
        from pathlib import Path
        _venv = Path.home() / ".agents/skills/skilless/.venv"
        _pip = f"uv pip install --python {_venv}"
        return [
            ("fastmcp not installed", f"Run: {_pip} fastmcp"),
            ("Connection failed", "Check network; verify Exa MCP endpoint is reachable"),
            ("Rate limited", "Wait a moment and retry; Exa free tier has rate limits"),
            ("tavily-python not installed", f"Run: {_pip} tavily-python"),
            ("TAVILY_API_KEY not set", "Set TAVILY_API_KEY env var with your Tavily API key"),
            ("Tavily quota exceeded", "Check your Tavily plan usage at https://app.tavily.com"),
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
