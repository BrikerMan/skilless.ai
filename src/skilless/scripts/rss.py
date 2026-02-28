#!/usr/bin/env python3
"""RSS tool - Read RSS/Atom feeds."""

from __future__ import annotations

import sys

try:
    from skilless.scripts.base import BaseTool, DoctorResult
except ImportError:
    from base import BaseTool, DoctorResult


class RssTool(BaseTool):
    name = "rss"
    description = "Read RSS/Atom feed entries"
    usage = "skilless.ai rss <url> [num_entries]"
    how = "Parses RSS/Atom feeds using feedparser"

    def doctor(self) -> DoctorResult:
        try:
            import feedparser

            feed = feedparser.parse("https://hnrss.org/frontpage")
            if feed.entries and len(feed.entries) > 0:
                return DoctorResult("OK", f"parsed {len(feed.entries)} entries from HN")
            return DoctorResult("FAIL", "no entries found")
        except Exception as e:
            return DoctorResult("FAIL", str(e))

    def run(self, args: list[str]) -> str:
        if not args:
            raise ValueError("Usage: skilless.ai rss <url> [num_entries]")

        import feedparser

        url = args[0]
        num_entries = int(args[1]) if len(args) > 1 else 10
        feed = feedparser.parse(url)

        lines = [f"# {feed.feed.get('title', 'Untitled')}\n"]
        for entry in feed.entries[:num_entries]:
            title = entry.get("title", "Untitled")
            link = entry.get("link", "")
            published = entry.get("published", "")
            summary = entry.get("summary", "")[:200]

            lines.append(f"## {title}")
            if published:
                lines.append(f"Published: {published}")
            lines.append(f"Link: {link}")
            if summary:
                lines.append(f"Summary: {summary}...")
            lines.append("")

        return "\n".join(lines)

    @property
    def troubleshooting(self) -> list[tuple[str, str]]:
        from pathlib import Path
        _venv = Path.home() / ".agents/skills/skilless.ai/.venv"
        _pip = f"uv pip install --python {_venv}"
        return [
            ("feedparser not installed", f"Run: {_pip} feedparser"),
            ("Parse failed", "Verify the URL points to a valid RSS/Atom feed"),
            ("Empty feed", "Feed may be temporarily unavailable or no longer updated"),
        ]


def main():
    tool = RssTool()
    try:
        print(tool.run(sys.argv[1:]))
    except (ValueError, RuntimeError) as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
