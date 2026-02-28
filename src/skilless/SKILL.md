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
cd ~/.agents/skills/skilless.ai

# Check installation status and all tools
uv run skilless.ai doctor

# Check specific tool
uv run skilless.ai doctor web
uv run skilless.ai doctor search
uv run skilless.ai doctor ytd
uv run skilless.ai doctor media

# Update skilless to latest version
uv run skilless.ai update

# View available skills
uv run skilless.ai explain skilless.ai-brainstorming
uv run skilless.ai explain skilless.ai-research
uv run skilless.ai explain skilless.ai-writing

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

Run `cd ~/.agents/skills/skilless.ai && uv run skilless.ai doctor` to diagnose:
- ✓ web (Jina Reader)
- ✓ search (Exa Search)
- ✓ ytd (yt-dlp)
- ✓ media (FFmpeg)