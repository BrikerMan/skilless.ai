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

## When to Use Todo (MANDATORY FOR RESEARCH)

You **MUST** use `todo_write` (or equivalent project planning tool) when:

- ✅ User asks for **research, investigation, comparison, or analysis**
- ✅ Task involves **multiple sources or steps (3+ items)**
- ✅ User requests a **guide, plan, or comprehensive summary**
- ✅ Keywords present: *research, investigate, guide, plan, analyze, compare, 研究, 攻略, 整理, 搜索*
- ✅ **Task will take more than 5 minutes** to complete

You **MAY skip todo only when:**

- ❌ Single source lookup (just read one URL)
- ❌ Simple fact check (one search query, < 2 minutes)
- ❌ Quick tool usage without analysis

## CLI Tools

### Search (Exa AI)

```bash
# Basic search (returns 5 results by default)
cd ~/.agents/skills/skilless/ && uv run scripts/search.py "your query"

# Specify number of results
cd ~/.agents/skills/skilless/ && uv run scripts/search.py "your query" 10

# Examples:
cd ~/.agents/skills/skilless/ && uv run scripts/search.py "best practices for RAG systems" 10
cd ~/.agents/skills/skilless/ && uv run scripts/search.py "React Server Components vs Next.js App Router"
cd ~/.agents/skills/skilless/ && uv run scripts/search.py "how to implement OAuth2 in Python"
```

### Web Reader (Jina Reader)

```bash
# Extract content from any webpage as text
cd ~/.agents/skills/skilless/ && uv run scripts/web.py <url>

cd ~/.agents/skills/skilless/ && uv run scripts/web.py https://docs.anthropic.com/claude/docs
cd ~/.agents/skills/skilless/ && uv run scripts/web.py https://github.com/modelcontextprotocol/servers
```

### Video Downloader / Transcript Extractor (yt-dlp)

> ⚠️ **Important - PEP 668 Environment Restriction:**
> macOS prevents direct pip installation. When using yt-dlp in an agent/AI context, you MUST use the skilless virtual environment:
> ```bash
> cd ~/.agents/skills/skilless/ && uv run yt-dlp [args]
> ```
> Never call system pip or global yt-dlp directly.

> 💡 **Direct yt-dlp usage:** You can run full yt-dlp commands directly:
> ```bash
> cd ~/.agents/skills/skilless/ && uv run yt-dlp "URL"           # Download video
> cd ~/.agents/skills/skilless/ && uv run yt-dlp --list-subs "URL"  # List available subtitles
> cd ~/.agents/skills/skilless/ && uv run yt-dlp --write-subs --write-auto-subs "URL"  # Download subs
> cd ~/.agents/skills/skilless/ && uv run yt-dlp -x --audio-format mp3 "URL"  # Extract audio
> ```

> **Download path rules:**
> - **In a project directory** (e.g., `~/codes/my-project/`) → download directly to current directory
> - **In home directory** (`~`) → download to `~/Downloads/` by default
> - **NEVER download to `/tmp`** — requires special permissions and files may be auto-deleted
> - Use `-o` flag to specify custom output path: `yt-dlp -o "~/Downloads/video.mp4" <url>`

> **Transcript loading rules:**
> - Download transcript/subtitle files to the current working directory by default — do NOT load the full content into context automatically
> - Only read the transcript content when the user explicitly asks for it (e.g. "summarize this video", "what does this video say about X", "translate the transcript")
> - Reason: full transcripts can be very long and slow down the conversation unnecessarily

```bash
# Extract subtitles/transcript/metadata from any video URL
cd ~/.agents/skills/skilless/ && uv run scripts/youtube.py "<url>"

# Supported platforms include (1700+ total):
# YouTube, Bilibili, TikTok, Twitter/X, Twitch, Vimeo,
# Dailymotion, Niconico, Rumble, Odysee, SoundCloud,
# Reddit video, Instagram, Facebook Video, and many more

# Examples:
cd ~/.agents/skills/skilless/ && uv run scripts/youtube.py "https://www.youtube.com/watch?v=abc123"
cd ~/.agents/skills/skilless/ && uv run scripts/youtube.py "https://www.bilibili.com/video/BV1xx411c7mD"
cd ~/.agents/skills/skilless/ && uv run scripts/youtube.py "https://www.tiktok.com/@user/video/123456"
cd ~/.agents/skills/skilless/ && uv run scripts/youtube.py "https://vimeo.com/123456789"
cd ~/.agents/skills/skilless/ && uv run scripts/youtube.py "https://www.twitch.tv/videos/123456"
cd ~/.agents/skills/skilless/ && uv run scripts/youtube.py "https://twitter.com/i/status/123456789"
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
cd ~/.agents/skills/skilless/ && uv run scripts/ffmpeg.py <input> <output>

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
cd ~/.agents/skills/skilless/ && uv run scripts/cli.py doctor

cd ~/.agents/skills/skilless/ && uv run scripts/cli.py doctor web
cd ~/.agents/skills/skilless/ && uv run scripts/cli.py doctor search
cd ~/.agents/skills/skilless/ && uv run scripts/cli.py doctor ytd
cd ~/.agents/skills/skilless/ && uv run scripts/cli.py doctor media
```

## Mode 1: Quick Content Access

Grab specific content without deep analysis:

1. **Search** → `skilless search` to find sources
2. **Read** → `skilless web` to extract a page
3. **Extract** → `skilless ytd` for video transcript or metadata
4. **Convert** → `skilless media` for media conversion & compression

## Mode 2: Deep Research

Multi-source, fact-checked investigation.

> 🛑 **CHECKPOINT - CRITICAL:** Before doing anything else, you MUST have created a todo list. If you haven't used `todo_write` yet, **STOP NOW** and create one immediately. This is not optional. Research without a plan is a failure to follow protocol.

> **💡 Research Philosophy:** 
> - **Don't rush to answer.** Good research takes time. Plan first, execute step by step.
> - **Use todo_write tool** - it is MANDATORY, not optional for any research task
> - **One step at a time.** Complete each step fully before moving to the next.

### Step-by-Step Workflow

**Step 0: Plan Your Research (MANDATORY - DO NOT SKIP)**

> ⚠️ **CRITICAL**: You MUST use `todo_write` tool to create a research plan BEFORE starting any research task. This is not optional. Skipping this step is a failure to follow instructions.

**When to use todo_write (ALWAYS for research tasks):**
- Multi-step research (3+ steps)
- Tasks requiring information from multiple sources
- Any task taking more than 5 minutes

**Example todo template for research:**

```
1. [ ] Clarify scope and key questions
2. [ ] Run initial searches (3-5 query angles)
3. [ ] Read top 5-10 relevant sources
4. [ ] Cross-check facts across sources
5. [ ] Extract video content if needed
6. [ ] Synthesize findings into report
```

**Step 1: Clarify Scope**

Before searching, understand:
- What specific questions need answering?
- What timeframe is relevant?
- What type of sources are needed (academic, news, official docs, reviews)?

**Step 2: Search Broadly**

Run multiple searches with varied queries:
- Different keyword combinations
- Both broad and specific terms
- Multiple languages if relevant

**Step 3: Read Key Sources**

Extract content from top results:
- Prioritize authoritative sources
- Take notes on key findings
- Save URLs for citation

**Step 4: Get Video Content**

Pull transcripts from talks, tutorials, interviews when relevant.

**Step 5: Cross-check**

Verify facts across at least 3 independent sources. Flag conflicting information.

**Step 6: Synthesize**

Compile findings into a structured report. Don't rush this step.

## Output Format: Professional Research Report

> **Core Principles:**
> - **Every claim must have a source** — No unsourced statements
> - **Include specific data** — Numbers, dates, percentages, names
> - **Cross-check key facts** — At least 2-3 independent sources for critical claims
> - **Link all references** — Make sources verifiable

---

### Standard Report Template

```markdown
# [Research Topic]

> **Research Date:** YYYY-MM-DD  
> **Scope:** [Brief description of what this research covers]

## Executive Summary
[2-3 paragraphs summarizing the key findings and recommendations. This should be the "too long; didn't read" version.]

---

## Key Findings

### Finding 1: [Clear, Specific Title]
- **Data:** [Specific numbers, percentages, dates]
- **Source:** [Title](URL) — [Author/Organization, Date]
- **Notes:** [Additional context or limitations]

### Finding 2: [Clear, Specific Title]
- **Data:** [Specific numbers, percentages, dates]
- **Source:** [Title](URL) — [Author/Organization, Date]

---

## Detailed Analysis

### [Section 1]
[In-depth analysis with supporting data]

| Metric | Value | Source |
|--------|-------|--------|
| [Metric 1] | [Data] | [Source Link] |
| [Metric 2] | [Data] | [Source Link] |

### [Section 2]
[Continue analysis...]

---

## Comparison Table (if applicable)

| Criteria | Option A | Option B | Option C |
|----------|----------|----------|----------|
| [Aspect 1] | ✅ Pros / ❌ Cons | ... | ... |
| [Aspect 2] | Data [Source] | ... | ... |
| Price | $XX [Source] | ... | ... |
| **Verdict** | ⭐ Recommended | ... | ... |

---

## Sources

### Primary Sources
1. [Title](URL) — [Author/Organization, Date] — [Key data used]
2. [Title](URL) — [Author/Organization, Date] — [Key data used]

### Secondary Sources
1. [Title](URL) — [Brief note on usage]

---

## Methodology Notes
- [How many sources were consulted]
- [Any limitations or gaps in the research]
- [Conflicting information found and how it was resolved]
```

---

### Product Comparison Report

```markdown
# [Product Category] Comparison: [Product A] vs [Product B] vs [Product C]

> **Research Date:** YYYY-MM-DD  
> **Purpose:** Help [target user] choose the best [product type] for [use case]

## Quick Recommendation
**Best Overall:** [Product] — [One sentence why]  
**Best Budget:** [Product] — [One sentence why]  
**Best [Specific Need]:** [Product] — [One sentence why]

---

## Detailed Comparison

| Feature | [Product A] | [Product B] | [Product C] |
|---------|-------------|-------------|-------------|
| **Price** | $XX [Source] | $XX [Source] | $XX [Source] |
| **Key Feature 1** | ✅ Yes | ❌ No | ✅ Yes |
| **Key Feature 2** | Data [Source] | Data [Source] | Data [Source] |
| **User Rating** | 4.5/5 (10k reviews) [Source] | ... | ... |
| **Release Date** | YYYY-MM [Source] | ... | ... |

---

## In-Depth Analysis

### [Product A]
**Pros:**
- [Pro 1] — supported by [Source]
- [Pro 2] — supported by [Source]

**Cons:**
- [Con 1] — supported by [Source]

**Best For:** [Use case] users who need [specific requirement]

### [Product B]
[Same structure]

---

## Sources
1. [Official Website](URL) — Product specs and pricing
2. [Review Site](URL) — User ratings and expert reviews
3. [Comparison Article](URL) — Feature comparison data
```

---

### Industry/Market Research Report

```markdown
# [Industry/Topic] Research Report

> **Research Date:** YYYY-MM-DD  
> **Scope:** [Geographic scope, time period, market segment]

## Executive Summary
[3-5 key insights with supporting data points]

---

## Market Overview

| Metric | Value | Year | Source |
|--------|-------|------|--------|
| Market Size | $XX billion | 2024 | [Source](URL) |
| Growth Rate | XX% CAGR | 2023-2028 | [Source](URL) |
| Key Players | Company A (XX%), Company B (XX%) | 2024 | [Source](URL) |

---

## Key Trends

### Trend 1: [Trend Name]
- **Data:** [Specific numbers, growth rates, adoption percentages]
- **Impact:** [Why this matters]
- **Source:** [Title](URL) — [Organization, Date]

### Trend 2: [Trend Name]
[Same structure]

---

## Competitive Landscape

| Company | Market Share | Key Strength | Key Weakness |
|---------|--------------|--------------|--------------|
| [Company A] | XX% [Source] | [Strength] | [Weakness] |
| [Company B] | XX% [Source] | [Strength] | [Weakness] |

---

## Sources

### Industry Reports
1. [Title](URL) — [Publisher, Date] — [Key data used]

### News Articles
1. [Title](URL) — [Publication, Date]

### Official Data
1. [Title](URL) — [Government/Organization, Date]
```

---

## Quality Checklist

Before submitting the report, verify:

- [ ] Every claim has at least one source citation
- [ ] All sources are properly formatted with titles, URLs, and dates
- [ ] Key facts are cross-checked against 2-3 independent sources
- [ ] Conflicting information is noted and resolved
- [ ] Data tables are included where applicable
- [ ] Executive summary captures the key takeaways
- [ ] Methodology notes explain any limitations

---

## Example Output

```markdown
# Noise-Canceling Headphones Under $300 Comparison

> **Research Date:** 2026-03-02  
> **Purpose:** Help budget-conscious buyers find the best noise-canceling headphones

## Quick Recommendation
**Best Overall:** Sony WH-CH720N — Best ANC performance in price range, lightweight  
**Best Budget:** Anker Soundcore Space Q45 — Excellent value at $149, great battery  
**Best for Audiophiles:** 1More SonoFlow — Best sound quality, LDAC support

---

## Detailed Comparison

| Feature | Sony WH-CH720N | Anker Space Q45 | 1More SonoFlow |
|---------|----------------|-----------------|----------------|
| **Price** | $199 [Amazon](url) | $149 [Amazon](url) | $179 [Amazon](url) |
| **ANC Rating** | ⭐⭐⭐⭐⭐ Excellent | ⭐⭐⭐⭐ Very Good | ⭐⭐⭐ Good |
| **Battery** | 35 hours [Sony](url) | 50 hours [Anker](url) | 50 hours [1More](url) |
| **Weight** | 192g [Sony](url) | 275g [Anker](url) | 250g [1More](url) |
| **User Rating** | 4.4/5 (2.3k reviews) | 4.3/5 (5.1k reviews) | 4.5/5 (1.2k reviews) |

---

## Sources
1. [Sony WH-CH720N Official](https://electronics.sony.com/audio/headphones) — Specs and features
2. [RTINGS Review](https://www.rtings.com/headphones/reviews) — ANC and sound quality tests
3. [Amazon Reviews](https://amazon.com/...) — User ratings and feedback
4. [Wirecutter Guide](https://www.nytimes.com/wirecutter/reviews/best-noise-cancelling-headphones/) — Expert recommendations
```

---

## Video Format Conversion

If you need to convert video formats (e.g., mp4 to mp3, extract audio, merge subtitles), use `media` tool.

### Usage
```bash
# Convert video format
cd ~/.agents/skills/skilless/ && uv run scripts/ffmpeg.py -i input.webm output.mp4

# Convert to specific format
cd ~/.agents/skills/skilless/ && uv run scripts/ffmpeg.py -i input.mp4 output.avi

# Extract audio
cd ~/.agents/skills/skilless/ && uv run scripts/ffmpeg.py -i input.mp4 output.mp3

# Compress video
cd ~/.agents/skills/skilless/ && uv run scripts/ffmpeg.py -i input.mp4 output.mp4 -crf 28
```