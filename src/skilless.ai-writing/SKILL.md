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
3. **Get video content** — Use `ytd` for video transcripts
4. **Write** — Produce clear, well-structured content

## Tools Available

- `search` — Exa AI semantic search
- `web` — Jina Reader for any webpage
- `ytd` — yt-dlp for video transcripts (1700+ sites)
- `media` — FFmpeg for media conversion

## CLI Tools

**Use these CLI commands to research content for writing:**

### Search (Exa AI)
```bash
# Find sources, data, and references
cd ~/.agents/skills/skilless/ && uv run scripts/search.py "your query" [num_results]

# Examples:
cd ~/.agents/skills/skilless/ && uv run scripts/search.py "AI trends 2025" 10
cd ~/.agents/skills/skilless/ && uv run scripts/search.py "remote work statistics"
```

### Web Reader (Jina Reader)
```bash
# Read source materials
cd ~/.agents/skills/skilless/ && uv run scripts/web.py <url>

# Examples:
cd ~/.agents/skills/skilless/ && uv run scripts/web.py https://example.com/article
cd ~/.agents/skills/skilless/ && uv run scripts/web.py https://docs.example.com/guide
```

### Media Converter
```bash
# Convert and compress media files
cd ~/.agents/skills/skilless/ && uv run scripts/ffmpeg.py <input> <output>

# Examples:
cd ~/.agents/skills/skilless/ && uv run scripts/ffmpeg.py video.mkv output.mp4
cd ~/.agents/skills/skilless/ && uv run scripts/ffmpeg.py input.mp4 output.mp3
```

### Video Transcript Extractor

> ⚠️ **PEP 668 Environment Restriction:** Always use the skilless virtual environment:
> ```bash
> cd ~/.agents/skills/skilless/ && uv run yt-dlp [args]
> ```

## Output Guidelines

- Write clearly and concisely
- Support claims with sources
- Structure with headings and bullet points
- Match the user's requested tone (formal, casual, technical)