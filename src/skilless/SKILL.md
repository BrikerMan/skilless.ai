---
name: skilless.ai
description: "Meta skill for Skilless toolkit — manage, diagnose, and update the skilless CLI tools and AI skills. Use when user asks about skilless status, needs to verify installation, check tool availability, or run doctor/debug commands."
---

# Skilless

**Meta skill for Skilless — manage and diagnose your skilless installation.**

## Purpose

Skilless provides AI-powered tools (search, web, ytd, media) and AI skills (brainstorming, research, writing). This meta skill handles installation, diagnostics, and management.

> 💡 For detailed skill usage (brainstorming, research, writing), see each skill's own SKILL.md

## Usage

```bash
cd ~/.agents/skills/skilless/

# Check installation status and all tools
uv run scripts/cli.py doctor

# Check specific tool
uv run scripts/cli.py doctor web
uv run scripts/cli.py doctor search
uv run scripts/cli.py doctor ytd
uv run scripts/cli.py doctor media

# Update skilless to latest version
uv run scripts/cli.py update

# View available skills
uv run scripts/cli.py explain skilless.ai-brainstorming
uv run scripts/cli.py explain skilless.ai-research
uv run scripts/cli.py explain skilless.ai-writing

# Run CLI tools directly (see each skill for details)
uv run scripts/search.py "query"
uv run scripts/web.py <url>
uv run scripts/youtube.py <video_url>
uv run scripts/ffmpeg.py <input> <output>
```

## Tools

| Tool | Purpose |
|------|---------|
| `search` | Semantic web search (Exa) |
| `web` | Extract webpage content (Jina Reader) |
| `ytd` | Extract video subtitles (yt-dlp, 1700+ sites) |
| `media` | Convert & compress media (FFmpeg) |

## Skills

| Skill | File |
|-------|------|
| Brainstorming | `skilless.ai-brainstorming` |
| Research | `skilless.ai-research` |
| Writing | `skilless.ai-writing` |

## Troubleshooting

Run `cd ~/.agents/skills/skilless/ && uv run scripts/cli.py doctor` to diagnose:
- ✓ web (Jina Reader)
- ✓ search (Exa Search)
- ✓ ytd (yt-dlp)
- ✓ media (FFmpeg)