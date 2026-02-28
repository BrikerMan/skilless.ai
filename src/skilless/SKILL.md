---
name: skilless.ai
description: "Meta skill for Skilless toolkit — manage, diagnose, and update the skilless CLI tools and AI skills. Use when user asks about skilless status, needs to verify installation, check tool availability, or run doctor/debug commands."
---

# Skilless

**Meta skill for Skilless — manage and diagnose your skilless installation.**

## Purpose

Skilless provides AI-powered tools (search, web, ytd, rss) and AI skills (brainstorming, research, writing). This meta skill handles installation, diagnostics, and management.

> 💡 For detailed skill usage (brainstorming, research, writing), see each skill's own SKILL.md

## Usage

```bash
# Check installation status and all tools
skilless.ai doctor

# Check specific tool
skilless.ai doctor web
skilless.ai doctor search
skilless.ai doctor ytd
skilless.ai doctor rss

# Update skilless to latest version
skilless.ai update

# View available skills
skilless.ai explain skilless.ai-brainstorming
skilless.ai explain skilless.ai-research
skilless.ai explain skilless.ai-writing

# Run CLI tools directly (see each skill for details)
skilless.ai search "query"
skilless.ai web <url>
skilless.ai ytd <video_url>
skilless.ai rss <feed_url>
```

## Tools

| Tool | Purpose |
|------|---------|
| `search` | Semantic web search (Exa) |
| `web` | Extract webpage content (Jina Reader) |
| `ytd` | Extract video subtitles (yt-dlp, 1700+ sites) |
| `rss` | Parse RSS/Atom feeds |

## Skills

| Skill | File |
|-------|------|
| Brainstorming | `skilless.ai-brainstorming` |
| Research | `skilless.ai-research` |
| Writing | `skilless.ai-writing` |

## Troubleshooting

Run `skilless.ai doctor` to diagnose:
- ✓ web (Jina Reader)
- ✓ search (Exa Search)
- ✓ ytd (yt-dlp)
- ✓ rss (feedparser)