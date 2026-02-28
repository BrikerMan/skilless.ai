#!/usr/bin/env python3
"""Web tool - Read webpage content via Jina Reader."""

from __future__ import annotations

import sys

try:
    from skilless.scripts.base import BaseTool, DoctorResult
except ImportError:
    from base import BaseTool, DoctorResult


class WebTool(BaseTool):
    name = "web"
    description = "Fetch any webpage and return clean Markdown text"
    usage = "skilless.ai web <url>"
    how = "Sends URL to Jina Reader API (r.jina.ai) which returns clean Markdown"

    def doctor(self) -> DoctorResult:
        try:
            import httpx

            r = httpx.get("https://r.jina.ai/http://example.com", timeout=15)
            if r.status_code == 200 and len(r.text) > 100:
                return DoctorResult("OK", f"fetched {len(r.text)} chars")
            return DoctorResult("FAIL", f"HTTP {r.status_code}")
        except Exception as e:
            return DoctorResult("FAIL", str(e))

    def run(self, args: list[str]) -> str:
        if not args:
            raise ValueError("Usage: skilless.ai web <url>")

        import httpx

        url = args[0]
        if not url.startswith(("http://", "https://")):
            url = "https://" + url

        r = httpx.get(f"https://r.jina.ai/{url}", timeout=30)
        if r.status_code != 200:
            raise RuntimeError(f"HTTP {r.status_code}")
        return r.text

    @property
    def troubleshooting(self) -> list[tuple[str, str]]:
        from pathlib import Path
        _venv = Path.home() / ".agents/skills/skilless.ai/.venv"
        _pip = f"uv pip install --python {_venv}"
        return [
            ("Connection timeout", "Check network; set proxy: export HTTPS_PROXY=http://127.0.0.1:<port>"),
            ("Empty content returned", "Site may block Jina Reader; try a different URL or tool"),
            ("HTTP 429", "Rate limited by Jina Reader; wait a moment and retry"),
            ("httpx not installed", f"Run: {_pip} httpx"),
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
