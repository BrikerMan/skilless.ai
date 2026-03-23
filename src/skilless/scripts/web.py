#!/usr/bin/env python3
"""Web tool - Read webpage content via Jina Reader or Tavily Extract."""

from __future__ import annotations

import os
import sys

try:
    from skilless.scripts.base import BaseTool, DoctorResult
except ImportError:
    from base import BaseTool, DoctorResult


def _get_web_provider() -> str:
    """Return the configured web provider ('jina' or 'tavily')."""
    return os.environ.get("WEB_PROVIDER", "jina").lower()


class WebTool(BaseTool):
    name = "web"
    description = "Fetch any webpage and return clean Markdown text"
    usage = "cd ~/.agents/skills/skilless/ && uv run scripts/web.py <url>"
    how = "Sends URL to Jina Reader API or Tavily Extract (set WEB_PROVIDER=tavily) which returns clean Markdown"

    def doctor(self) -> DoctorResult:
        provider = _get_web_provider()
        if provider == "tavily":
            return self._doctor_tavily()
        return self._doctor_jina()

    def _doctor_jina(self) -> DoctorResult:
        try:
            import httpx

            r = httpx.get("https://r.jina.ai/http://example.com", timeout=15)
            if r.status_code == 200 and len(r.text) > 100:
                return DoctorResult("OK", f"jina: fetched {len(r.text)} chars")
            return DoctorResult("FAIL", f"jina: HTTP {r.status_code}")
        except Exception as e:
            return DoctorResult("FAIL", f"jina: {e}")

    def _doctor_tavily(self) -> DoctorResult:
        try:
            import os
            from tavily import TavilyClient  # noqa: F401 — verify library importable
            if not os.environ.get("TAVILY_API_KEY"):
                return DoctorResult("FAIL", "tavily: TAVILY_API_KEY not set")
            return DoctorResult("OK", "tavily: API key present, library installed")
        except ImportError as e:
            return DoctorResult("FAIL", f"tavily: {e}")

    def run(self, args: list[str]) -> str:
        if not args:
            raise ValueError("Usage: cd ~/.agents/skills/skilless/ && uv run scripts/web.py <url>")

        url = args[0]
        if not url.startswith(("http://", "https://")):
            url = "https://" + url

        provider = _get_web_provider()
        if provider == "tavily":
            return self._run_tavily(url)
        return self._run_jina(url)

    def _run_jina(self, url: str) -> str:
        import httpx

        r = httpx.get(f"https://r.jina.ai/{url}", timeout=30)
        if r.status_code != 200:
            raise RuntimeError(f"HTTP {r.status_code}")
        return r.text

    def _run_tavily(self, url: str) -> str:
        if not os.environ.get("TAVILY_API_KEY"):
            raise RuntimeError("TAVILY_API_KEY environment variable not set.")
        from tavily import TavilyClient

        client = TavilyClient()
        result = client.extract(urls=[url])
        results = result.get("results", [])
        if not results:
            raise RuntimeError("Tavily Extract returned no content for this URL")
        content = results[0].get("raw_content", "")
        if not content:
            raise RuntimeError("Tavily Extract returned empty content for this URL")
        return content

    @property
    def troubleshooting(self) -> list[tuple[str, str]]:
        from pathlib import Path
        _venv = Path.home() / ".agents/skills/skilless/.venv"
        _pip = f"uv pip install --python {_venv}"
        return [
            ("Connection timeout", "Check network; set proxy: export HTTPS_PROXY=http://127.0.0.1:<port>"),
            ("Empty content returned", "Site may block Jina Reader; try a different URL or tool"),
            ("HTTP 429", "Rate limited by Jina Reader; wait a moment and retry"),
            ("httpx not installed", f"Run: {_pip} httpx"),
            ("Tavily: TAVILY_API_KEY not set", "Set TAVILY_API_KEY env var; get a key at https://app.tavily.com"),
            ("Tavily: no content returned", "URL may be blocked or inaccessible; try a different URL"),
            ("tavily-python not installed", f"Run: {_pip} tavily-python"),
        ]


def main():
    tool = WebTool()
    try:
        print(tool.run(sys.argv[1:]))
    except (ValueError, RuntimeError) as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
