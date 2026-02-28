---
name: skilless.ai-writing
description: "Help produce written content by researching topics and gathering references. Use when user needs to write articles, emails, documentation, reports, or any content requiring research. Triggers: write, draft, compose, create content."
---

# Writing Skill

**Help produce written content by researching topics and gathering references.**

Use when user needs to: write articles, emails, documentation, reports, or any content that requires research.

## When to Use

- User asks to "write", "draft", "compose", "create content"
- User needs to create documentation or reports
- User wants to write an article or blog post

## Writing Process

1. **Research** — Use `search` to find relevant information
2. **Read references** — Use `web` to extract content from sources
3. **Stay updated** — Use `rss` to follow latest news on topic
4. **Write** — Produce clear, well-structured content

## Tools Available

- `search` — Exa AI semantic search
- `web` — Jina Reader for any webpage
- `rss` — feedparser for RSS/Atom feeds

## CLI Tools

**Use these CLI commands to research content for writing:**

### Search (Exa AI)
```bash
# Find sources, data, and references
cd ~/.agents/skills/skilless.ai && uv run scripts/search.py "your query" [num_results]

# Examples:
skilless.ai search "AI trends 2025" 10
skilless.ai search "remote work statistics"
```

### Web Reader (Jina Reader)
```bash
# Read source materials
cd ~/.agents/skills/skilless.ai && uv run scripts/web.py <url>

# Examples:
skilless.ai web https://example.com/article
skilless.ai web https://docs.example.com/guide
```

### RSS Feed Reader
```bash
# Follow latest news on your topic
cd ~/.agents/skills/skilless.ai && uv run scripts/rss.py <feed_url>

# Examples:
skilless.ai rss https://feeds.arstechnica.com/arstechnica/index
skilless.ai rss https://hnrss.org/frontpage
```

### Video Transcript Extractor
```bash
# Get video content for research (YouTube, Bilibili, TikTok, Vimeo, Twitch, 1700+ sites)
cd ~/.agents/skills/skilless.ai && uv run scripts/youtube.py <video_url>

# Examples:
skilless.ai ytd https://www.youtube.com/watch?v=abc123
```

## Output Guidelines

- Write clearly and concisely
- Support claims with sources
- Structure with headings and bullet points
- Match the user's requested tone (formal, casual, technical)