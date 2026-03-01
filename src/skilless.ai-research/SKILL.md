---
name: skilless.ai-research
description: "Fetch internet content or conduct deep multi-source research. Quick access: search the web, read pages, extract video transcripts/subtitles from YouTube/TikTok/Twitter/Twitch/Vimeo/Bilibili/1700+ sites via yt-dlp, convert and compress media via FFmpeg. Deep research: collect multi-source data, cross-check facts, produce structured reports. Triggers: 下载, 获取, 提取, 下载字幕, 下载视频, 转换, 压缩, read web, fetch, search, research, investigate, YouTube, Bilibili, TikTok, Twitter, Twitch, Vimeo, Dailymotion, media, convert, compress, 抓取."
---

# Research Skill

**Fetch internet content or conduct deep multi-source research.**

Two operating modes:

- **Quick content access** — Search, read a page, extract video transcripts, or parse a feed on the spot
- **Deep research** — Combine multiple sources, cross-check facts, and synthesize a structured fact-checked report

## When to Use

- "search", "find", "look up" → quick lookup with `search`
- "read", "fetch", "get page" → extract content with `web`
- "download", "extract", "get subtitles/transcript" → use `ytd`
- "convert", "compress", "encode", "media", "ffmpeg" → use `media`
- "research", "investigate", "analyze", "compare" → deep multi-source research

## CLI Tools

### Search (Exa AI)

```bash
# Basic search (returns 5 results by default)
~/.agents/skills/skilless.ai/skilless.ai search "your query"

# Specify number of results
cd ~/.agents/skills/skilless.ai && uv run scripts/search.py "your query" 10

# Examples:
skilless.ai search "best practices for RAG systems" 10
skilless.ai search "React Server Components vs Next.js App Router"
skilless.ai search "how to implement OAuth2 in Python"
```

### Web Reader (Jina Reader)

```bash
# Extract content from any webpage as text
cd ~/.agents/skills/skilless.ai && uv run scripts/web.py <url>

skilless.ai web https://docs.anthropic.com/claude/docs
skilless.ai web https://github.com/modelcontextprotocol/servers
```

### Video Downloader / Transcript Extractor (yt-dlp)

> ⚠️ **Important - PEP 668 Environment Restriction:**
> macOS prevents direct pip installation. When using yt-dlp in an agent/AI context, you MUST use the skilless virtual environment:
> ```bash
> cd ~/.agents/skills/skilless.ai && uv run yt-dlp [args]
> ```
> Never call system pip or global yt-dlp directly.

> **Transcript loading rules:**
> - Download transcript/subtitle files to the current working directory by default — do NOT load the full content into context automatically
> - Only read the transcript content when the user explicitly asks for it (e.g. "summarize this video", "what does this video say about X", "translate the transcript")
> - Reason: full transcripts can be very long and slow down the conversation unnecessarily

```bash
# Extract subtitles/transcript/metadata from any video URL
cd ~/.agents/skills/skilless.ai && uv run scripts/youtube.py "<url>"

# Supported platforms include (1700+ total):
# YouTube, Bilibili, TikTok, Twitter/X, Twitch, Vimeo,
# Dailymotion, Niconico, Rumble, Odysee, SoundCloud,
# Reddit video, Instagram, Facebook Video, and many more

# Examples:
skilless.ai ytd "https://www.youtube.com/watch?v=abc123"
skilless.ai ytd "https://www.bilibili.com/video/BV1xx411c7mD"
skilless.ai ytd "https://www.tiktok.com/@user/video/123456"
skilless.ai ytd "https://vimeo.com/123456789"
skilless.ai ytd "https://www.twitch.tv/videos/123456"
skilless.ai ytd "https://twitter.com/i/status/123456789"
```

> ⚠️ **YouTube 故障排查：**
> - 如果遇到 "Sign in to confirm you're not a bot"，说明 IP 被 YouTube 反爬
> - 如果在国内网络直接连接失败（超时/拒绝），说明需要代理才能访问 YouTube
> - **解决方案：**
>   1. 将代理客户端切换为 **TUN 模式**（全局流量接管，最省事）
>   2. 或手动设置环境变量：`export HTTPS_PROXY=http://127.0.0.1:<port>`
>   3. 从浏览器导出 cookies：`yt-dlp --cookies-from-browser chrome "URL"`
>   4. 使用 Bilibili 替代（通常更稳定，无需代理）
> - 详细文档：https://github.com/yt-dlp/yt-dlp/wiki/FAQ#how-do-i-pass-cookies-to-yt-dlp

### FFmpeg (Media Converter & Compressor)

```bash
# Convert or compress video/audio files
cd ~/.agents/skills/skilless.ai && uv run scripts/ffmpeg.py <input> <output>

# Examples:
# Convert video format
uv run scripts/ffmpeg.py video.mkv output.mp4

# Convert audio
uv run scripts/ffmpeg.py audio.wav output.mp3

# Compress video (lower quality, smaller file)
uv run scripts/ffmpeg.py input.mp4 output.mp4 -crf 28

# Supported formats: mp4, mkv, avi, mov, webm, mp3, aac, wav, flac, ogg
```

### Doctor (Check Tool Status)

```bash
cd ~/.agents/skills/skilless.ai && uv run skilless.ai doctor

cd ~/.agents/skills/skilless.ai && uv run skilless.ai doctor web
cd ~/.agents/skills/skilless.ai && uv run skilless.ai doctor search
cd ~/.agents/skills/skilless.ai && uv run skilless.ai doctor ytd
cd ~/.agents/skills/skilless.ai && uv run skilless.ai doctor media
```

## Mode 1: Quick Content Access

Grab specific content without deep analysis:

1. **Search** → `skilless search` to find sources
2. **Read** → `skilless web` to extract a page
3. **Extract** → `skilless ytd` for video transcript or metadata
4. **Convert** → `skilless media` for media conversion & compression

## Mode 2: Deep Research

Multi-source, fact-checked investigation:

1. **Search broadly** — Run multiple searches with varied queries
2. **Read key sources** — Extract content from top results
3. **Get video content** — Pull transcripts from talks, tutorials, interviews
4. **Cross-check** — Verify facts across at least 3 independent sources
5. **Synthesize** — Compile findings into a structured report

## Output Format

```
# [Topic]

## Key Findings
- Finding 1 [Source](url)
- Finding 2 [Source](url)

## Sources
- [Source 1](url)
- [Source 2](url)

## Summary
[2-3 sentence summary]
```

## Example

```
User: Research the best LLM frameworks for building AI agents

# Research: LLM Frameworks for AI Agents

## Key Findings
- LangChain: Most popular, good documentation, but can be complex
- LlamaIndex: Better for data-centric applications
- AutoGen: Microsoft's framework, good for multi-agent systems

## Sources
- ...

## Summary
For building AI agents, LangChain is the most established choice...
```

## Video Format Conversion

If you need to convert video formats (e.g., mp4 to mp3, extract audio, merge subtitles), use `media` tool.

### Usage
```bash
# Convert video format
cd ~/.agents/skills/skilless.ai && uv run scripts/ffmpeg.py -i input.webm output.mp4

# Convert to specific format
cd ~/.agents/skills/skilless.ai && uv run scripts/ffmpeg.py -i input.mp4 output.avi

# Extract audio
cd ~/.agents/skills/skilless.ai && uv run scripts/ffmpeg.py -i input.mp4 output.mp3

# Compress video
cd ~/.agents/skills/skilless.ai && uv run scripts/ffmpeg.py -i input.mp4 output.mp4 -crf 28
```