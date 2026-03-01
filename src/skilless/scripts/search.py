#!/usr/bin/env python3
"""Search tool - Web search via Exa MCP."""

from __future__ import annotations

import asyncio
import sys

try:
    from skilless.scripts.base import BaseTool, DoctorResult
except ImportError:
    from base import BaseTool, DoctorResult


class SearchTool(BaseTool):
    name = "search"
    description = "AI semantic web search via Exa"
    usage = "cd ~/.agents/skills/skilless/ && uv run scripts/search.py <query> [num_results]"
    how = "Connects to the Exa MCP endpoint via FastMCP for semantic search"

    MCP_URL = "https://mcp.exa.ai/mcp"

    def doctor(self) -> DoctorResult:
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
            ("Connection failed", "Check network; verify Exa MCP endpoint is reachable"),
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
