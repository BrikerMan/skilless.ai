#!/usr/bin/env python3
"""Skilless CLI - Unified entry point with rich output."""

from __future__ import annotations

import sys
from pathlib import Path

from rich import box
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

try:
    from skilless.scripts.base import BaseTool
    from skilless.scripts.ffmpeg import FFmpegTool
    from skilless.scripts.search import SearchTool
    from skilless.scripts.web import WebTool
    from skilless.scripts.youtube import YouTubeTool
except ImportError:
    from base import BaseTool
    from ffmpeg import FFmpegTool
    from search import SearchTool
    from web import WebTool
    from youtube import YouTubeTool

console = Console(stderr=True)

TOOLS: dict[str, BaseTool] = {
    "web": WebTool(),
    "search": SearchTool(),
    "ytd": YouTubeTool(),
    "media": FFmpegTool(),
}


# ── Dynamic skill loading from SKILL.md files ──────────────────────────


def load_skills() -> dict[str, dict]:
    """Load skills from SKILL.md files in the skilless package directory."""
    skills = {}
    
    # Find SKILL.md files in the src/skilless directory and subdirectories
    src_dir = Path(__file__).parent.parent  # Go up from scripts/ to skilless/
    
    # Also check sibling directories (skilless.ai-* folders)
    base_dir = src_dir.parent  # src/
    
    skill_files = list(base_dir.glob("*/SKILL.md"))
    skill_files.extend(src_dir.glob("SKILL.md"))
    
    for skill_file in skill_files:
        try:
            content = skill_file.read_text()
            
            # Parse YAML frontmatter
            if content.startswith("---"):
                parts = content.split("---", 2)
                if len(parts) >= 3:
                    import yaml
                    frontmatter = yaml.safe_load(parts[1])
                    
                    skill_name = frontmatter.get("name", skill_file.parent.name)
                    description = frontmatter.get("description", "")
                    
                    # Extract trigger words from description for tools
                    tools = ["search", "web"]  # Default tools
                    if "YouTube" in description or "youtube" in description or "video" in description.lower():  # noqa: E501
                        if "ytd" not in tools:
                            tools.append("ytd")
                    if "FFmpeg" in description or "ffmpeg" in description or "media" in description.lower() or "convert" in description.lower() or "compress" in description.lower():  # noqa: E501
                        if "media" not in tools:
                            tools.append("media")

                    # Use folder name as key (remove skilless.ai- prefix if present)
                    key = skill_file.parent.name
                    if key.startswith("skilless.ai-"):
                        key = key[12:]  # Remove "skilless.ai-" prefix
                    
                    skills[key] = {
                        "name": skill_name.replace("skilless.ai-", "").title(),
                        "description": description,
                        "tools": tools,
                    }
        except Exception:
            continue
    
    return skills


SKILLS = load_skills()


# ── Status icons ──────────────────────────────────────────────────────

_STATUS_STYLE = {
    "OK": ("✓", "green bold"),
    "OFF": ("○", "yellow"),
    "SKIP": ("◐", "dim"),
    "FAIL": ("✗", "red bold"),
}


# ── Meta commands (rich output to stderr) ─────────────────────────────


def cmd_doctor(args: list[str]):
    """Check tool health status."""
    target = args[0] if args else None

    if target and target not in TOOLS:
        console.print(f"[red]Unknown tool: {target}[/]")
        sys.exit(1)

    items = {target: TOOLS[target]} if target else TOOLS

    table = Table(
        title="Skilless Tool Status",
        box=box.ROUNDED,
        title_style="bold blue",
    )
    table.add_column("Tool", style="cyan", min_width=10)
    table.add_column("Status", justify="center", min_width=8)
    table.add_column("Detail")

    for name, tool in items.items():
        result = tool.doctor()
        icon, style = _STATUS_STYLE.get(result.status, ("?", ""))
        status_text = Text(f"{icon} {result.status}", style=style)
        table.add_row(name, status_text, result.detail)

    console.print(table)


def cmd_explain(args: list[str]):
    """Explain a tool or skill."""
    if not args:
        console.print(
            Panel.fit(
                "[bold]Skilless[/] — AI-powered tools",
                border_style="blue",
            )
        )
        console.print("\n[bold]Skills:[/]")
        for key, skill in SKILLS.items():
            console.print(f"  [cyan]{key:<16}[/] {skill['description']}")
        console.print("\n[bold]Tools:[/]")
        for key, tool in TOOLS.items():
            console.print(f"  [cyan]{key:<16}[/] {tool.description}")
        return

    key = args[0]
    # Normalize: accept both "brainstorming" and "skilless.ai-brainstorming"
    normalized_key = key[12:] if key.startswith("skilless.ai-") else key
    if normalized_key in TOOLS:
        tool = TOOLS[normalized_key]
        content = (
            f"[bold]Description:[/]  {tool.description}\n"
            f"[bold]Usage:[/]        {tool.usage}\n"
            f"[bold]How it works:[/] {tool.how}"
        )
        console.print(Panel(content, title=f"[bold]{tool.name}[/]", border_style="blue"))
    elif normalized_key in SKILLS:
        skill = SKILLS[normalized_key]
        tool_names = ", ".join(skill["tools"])
        content = (
            f"[bold]Description:[/] {skill['description']}\n"
            f"[bold]Tools:[/]       {tool_names}"
        )
        console.print(
            Panel(content, title=f"[bold]{skill['name']}[/]", border_style="green")
        )
    else:
        console.print(f"[red]Unknown: {key}[/]")
        sys.exit(1)


def cmd_guidance(args: list[str]):
    """Show usage guidance for a tool."""
    if not args:
        console.print(
            Panel.fit(
                "[bold]Skilless[/] — Quick Start Guide",
                border_style="blue",
            )
        )
        console.print("\n[bold]Commands:[/]")
        console.print("  scripts/cli.py doctor             Check all tools")
        console.print("  scripts/cli.py explain [name]     Explain a skill or tool")
        console.print("  scripts/cli.py guidance [tool]    Show usage guidance")
        console.print("  scripts/cli.py troubleshoot [tool] Show troubleshooting help")
        console.print("\n[bold]Tools:[/]")
        for tool in TOOLS.values():
            console.print(f"  cd ~/.agents/skills/skilless/ && uv run {tool.usage}")
        return

    key = args[0]
    if key in TOOLS:
        tool = TOOLS[key]
        console.print(
            Panel(
                f"[bold]Usage:[/]\n  {tool.usage}\n\n[bold]How it works:[/]\n  {tool.how}",
                title=f"[bold]{tool.name} Guide[/]",
                border_style="blue",
            )
        )
    else:
        console.print(f"[red]Unknown tool: {key}[/]")
        sys.exit(1)


def cmd_troubleshoot(args: list[str]):
    """Show troubleshooting info for tools."""
    if not args:
        has_any = False
        for name, tool in TOOLS.items():
            if not tool.troubleshooting:
                continue
            has_any = True
            table = Table(
                title=f"{name} Troubleshooting",
                box=box.SIMPLE,
                title_style="bold yellow",
            )
            table.add_column("Problem", style="yellow")
            table.add_column("Solution", style="green")
            for problem, solution in tool.troubleshooting:
                table.add_row(problem, solution)
            console.print(table)
            console.print()
        if not has_any:
            console.print("[dim]No troubleshooting info available.[/]")
        return

    key = args[0]
    if key not in TOOLS:
        console.print(f"[red]Unknown tool: {key}[/]")
        sys.exit(1)

    tool = TOOLS[key]
    if not tool.troubleshooting:
        console.print(f"[dim]No troubleshooting info for {key}.[/]")
        return

    table = Table(
        title=f"{tool.name} Troubleshooting",
        box=box.SIMPLE,
        title_style="bold yellow",
    )
    table.add_column("Problem", style="yellow")
    table.add_column("Solution", style="green")
    for problem, solution in tool.troubleshooting:
        table.add_row(problem, solution)
    console.print(table)


# ── Version & Update ─────────────────────────────────────────────────


def cmd_version(args: list[str]):
    """Print the installed version."""
    version_file = Path(__file__).parent.parent / "VERSION"
    if version_file.exists():
        console.print(version_file.read_text().strip())
    else:
        console.print("[yellow]unknown (VERSION file not found)[/]")


def cmd_update(args: list[str]):
    """Self-update scripts to the latest GitHub release."""
    import httpx

    GITHUB_REPO = "brikerman/skilless.ai"
    install_dir = Path(__file__).parent.parent
    version_file = install_dir / "VERSION"
    current = version_file.read_text().strip() if version_file.exists() else "unknown"

    console.print(f"Current version: [cyan]{current}[/]")
    console.print("Checking for updates...")

    try:
        resp = httpx.get(
            f"https://api.github.com/repos/{GITHUB_REPO}/releases/latest",
            timeout=15,
            headers={"Accept": "application/vnd.github+json"},
        )
        resp.raise_for_status()
        latest_tag = resp.json()["tag_name"]
    except Exception as e:
        console.print(f"[red]Failed to check for updates: {e}[/]")
        return 1

    if current == latest_tag:
        console.print(f"[green]Already up to date ({current})[/]")
        return 0

    console.print(f"Updating [yellow]{current}[/] → [green]{latest_tag}[/] ...")

    github_raw = f"https://raw.githubusercontent.com/{GITHUB_REPO}/{latest_tag}"
    scripts_dir = install_dir / "scripts"
    skills_parent = install_dir.parent

    try:
        for fname in ["base.py", "cli.py", "search.py", "web.py", "youtube.py", "ffmpeg.py"]:
            r = httpx.get(f"{github_raw}/src/skilless/scripts/{fname}", timeout=30)
            r.raise_for_status()
            (scripts_dir / fname).write_bytes(r.content)

        r = httpx.get(f"{github_raw}/src/skilless/SKILL.md", timeout=15)
        if r.status_code == 200:
            (install_dir / "SKILL.md").write_bytes(r.content)

        for skill in ["skilless.ai-brainstorming", "skilless.ai-research", "skilless.ai-writing"]:
            skill_dir = skills_parent / skill
            skill_dir.mkdir(parents=True, exist_ok=True)
            r = httpx.get(f"{github_raw}/src/{skill}/SKILL.md", timeout=15)
            if r.status_code == 200:
                (skill_dir / "SKILL.md").write_bytes(r.content)

        version_file.write_text(latest_tag + "\n")
    except Exception as e:
        console.print(f"[red]Update failed: {e}[/]")
        return 1

    console.print(f"[green]✓ Updated to {latest_tag}[/]")
    console.print("[dim]Restart any agents using skilless.ai to pick up changes.[/]")
    return 0


# ── Help ──────────────────────────────────────────────────────────────


def show_help():
    console.print(
        Panel.fit(
            "[bold blue]Skilless.ai[/] — AI-powered tools for research & writing",
            border_style="blue",
        )
    )
    console.print()

    table = Table(box=box.SIMPLE, show_header=False, padding=(0, 2))
    table.add_column("Command", style="cyan bold", min_width=24)
    table.add_column("Description")

    table.add_row("doctor [tool]", "Check tool status")
    table.add_row("explain [name]", "Explain a skill or tool")
    table.add_row("guidance [tool]", "Show usage guidance")
    table.add_row("troubleshoot [tool]", "Show troubleshooting help")
    table.add_row("version", "Show installed version")
    table.add_row("update", "Update to latest GitHub release")
    table.add_row("", "")
    table.add_row("search <query>", "Search the web (Exa)")
    table.add_row("web <url>", "Read a webpage (Jina Reader)")
    table.add_row("ytd <url>", "Extract video/transcript (yt-dlp, 1700+ sites)")
    table.add_row("media <input> <output>", "Convert/compress media (FFmpeg)")

    console.print(table)


# ── Entry point ───────────────────────────────────────────────────────

META_COMMANDS = {
    "doctor": cmd_doctor,
    "explain": cmd_explain,
    "guidance": cmd_guidance,
    "troubleshoot": cmd_troubleshoot,
    "version": cmd_version,
    "update": cmd_update,
}


def main():
    if len(sys.argv) < 2:
        show_help()
        sys.exit(1)

    command = sys.argv[1]
    args = sys.argv[2:]

    # Meta commands → rich output to stderr
    if command in META_COMMANDS:
        META_COMMANDS[command](args)
        return 0

    # Tool commands → plain text to stdout
    if command in TOOLS:
        tool = TOOLS[command]
        try:
            output = tool.run(args)
            if output:
                print(output)
            return 0
        except ValueError as e:
            console.print(f"[red]{e}[/]")
            return 1
        except Exception as e:
            console.print(f"[red]Error: {e}[/]")
            return 1

    console.print(f"[red]Unknown command: {command}[/]")
    show_help()
    return 1


if __name__ == "__main__":
    sys.exit(main() or 0)
