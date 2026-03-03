---
name: skilless.ai-research
description: "Fetch internet content or conduct deep multi-source research. Quick access: search the web, read pages, extract video transcripts/subtitles from YouTube/TikTok/Twitter/Twitch/Vimeo/Bilibili/1700+ sites via yt-dlp, convert and compress media via FFmpeg. Deep research: collect multi-source data, cross-check facts, produce structured reports. Triggers: 下载, 获取, 提取, 下载字幕, 下载视频, 转换, 压缩, read web, fetch, search, research, investigate, YouTube, Bilibili, TikTok, Twitter, Twitch, Vimeo, Dailymotion, media, convert, compress, 抓取."
---

# Research Skill

Fetch internet content or conduct deep multi-source research.

## Routing Table

| Trigger words                            | Tool                    | Purpose                      |
| ---------------------------------------- | ----------------------- | ---------------------------- |
| search, find, look up                    | `search.py`             | Web, docs, news lookup       |
| read, fetch, get page                    | `web.py`                | Extract page text            |
| download, extract, subtitles, transcript | `youtube.py` / `yt-dlp` | Video subtitles and metadata |
| convert, compress, encode, ffmpeg        | `ffmpeg.py`             | Media format conversion      |
| research, investigate, analyze, compare  | Multi-tool workflow     | Deep multi-source research   |

When the user intent is ambiguous, ask one clarifying question before proceeding.

---

## Research Depth Levels

Not every request needs a full investigation. Choose the appropriate depth based on complexity, or **ask the user** if unclear.

> **"Round" = one cycle of parallel tool calls.** A single round can fire 3-5 searches/reads in parallel. Rounds are sequential — each round builds on what you learned in the previous one.

| Level                       | When to use                                                   | Minimum effort                                                  |
| --------------------------- | ------------------------------------------------------------- | --------------------------------------------------------------- |
| **L1 — Quick lookup**       | Single fact, definition, simple question                      | 1 round, 1-2 searches                                          |
| **L2 — Focused research**   | Comparison, how-to, specific topic                            | 2-3 rounds, 2+ page reads, basic fact-check                    |
| **L3 — Deep investigation** | Multi-faceted analysis, market research, technical evaluation | **5+ rounds**, 5+ page reads, task list mandatory, full fact-check |

**Decision guide:**
- If the question can be answered with a single search result → **L1**
- If it involves comparing options or understanding a topic in depth → **L2**
- If it requires multiple perspectives, data synthesis, or the user explicitly says "research" / "investigate" / "deep dive" / "深度" → **L3**
- **If you cannot determine the level, ask the user:** "This could be a quick lookup or a deeper investigation — how thorough would you like me to be?"

---

## Research Workflow (L2 and L3)

### Step 1 — Define Scope

Before searching, clarify:
- What is the core question? What does the user actually need to know?
- What source types are needed — official docs, news, academic papers, user reviews?
- What dimensions matter (price, performance, compatibility, recency...)?
- How confident does the conclusion need to be?

If any of the above is unclear, **ask the user** before proceeding.

### Step 2 — Create Research Plan (L3 mandatory, L2 recommended)

**Decompose the task into research dimensions** — each dimension is an independent angle of investigation. Use `todo`, `tasks`, `todowrite`, or equivalent tool to create a visible task list.

Example — "深度检索 AI coding 领域的创业公司，区分海内外，并简单判断投资潜力":

```
[ ] 1. 海外 AI coding 创业公司全景 (who, what, founded when)
[ ] 2. 国内 AI coding 创业公司全景
[ ] 3. 各公司融资情况、投资方、估值
[ ] 4. 产品对比：功能、定价、目标用户
[ ] 5. 市场格局和竞争态势
[ ] 6. 投资潜力评估（团队、技术壁垒、增长、风险）
```

**Rules:**
- L3 must have **at least 3 dimensions**, typically 4-6
- Each dimension will get its own dedicated search round(s)
- Do NOT skip this step — a task list forces thoroughness

### Step 3 — Execute Per-Dimension (Multi-Round Search)

**Execute each dimension as a focused investigation cycle:**

For each dimension in the task list:
1. **Search** — Fire 1-3 parallel searches targeting this specific dimension
2. **Read** — Open and read the most relevant sources from search results
3. **Record** — Extract key data points, note sources, mark dimension complete
4. **Adapt** — If new keywords or sub-questions emerge, add them to the plan

**Search angle variety within each round:**
- **Broad terms** — Get the landscape, find authoritative sources
- **Specific terms** — Target precise data (version numbers, prices, specs)
- **Contrarian terms** — Search for "problems", "downsides", "alternatives", "vs" to find critical perspectives
- **Recency terms** — Add year or "2025" to filter outdated content
- **Multi-language** — Search in both English and Chinese when relevant

**Parallelism:** Within a single round, fire multiple tool calls in parallel (e.g., 3 searches at once, or 2 searches + 1 web read). Each round should maximize parallel execution.

<HARD-GATE>
L3 research MUST NOT proceed to synthesis (Step 5) until:
- At least **5 rounds** of tool calls have been executed
- At least **3 dimensions** have been independently investigated
- At least **5 pages** have been fully read (not just search snippets)

If you have not met these minimums, keep researching. Do NOT shortcut.

### Step 4 — Fact-Check

**Do not skip this step.**

- Cross-verify key data from multiple independent sources (aim for 2-3; more for L3)
- If only a single source exists, explicitly note: "Based on a single source — not independently verified"
- When sources contradict each other:
  1. Identify the reason (timing difference? different versions? conflicting interests?)
  2. State which source is more credible and why
  3. **If you cannot resolve the contradiction, present both sides and ask the user** how they want to proceed
- Distinguish **facts** from **opinions** — opinions may be cited but must not be stated as facts
- Never fabricate or assume unverified data — say "insufficient evidence" instead

### Step 5 — Synthesize Output

- **Conclusion first** — Lead with the most important finding or recommendation, then expand
- **Cite every data point** with `[1]`, `[2]`, etc., so the reader can verify
- **Be honest about uncertainty** — If evidence is limited, say so; do not force a conclusion
- End with a full source list

---

## Contradiction and Uncertainty Handling

When you encounter any of the following during research, **do not silently resolve it — surface it to the user:**

| Situation                                          | Action                                                                                               |
| -------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| Sources contradict each other on key data          | Present both claims with sources, explain possible reasons, ask user which direction to prioritize   |
| A critical piece of information cannot be verified | State what you found and what is missing, ask if the user wants to proceed or dig deeper             |
| The scope is ambiguous or too broad                | Ask a scoping question before investing effort                                                       |
| Research is turning up very little                 | Report what you found so far, ask if the user can provide additional context or alternative keywords |
| User's assumption appears to be incorrect          | Politely flag the discrepancy with evidence, ask for confirmation before proceeding                  |

**Format for follow-up questions:**

> ⚠️ **Needs clarification:** [concise description of the issue]
>
> **Options:**
> 1. [Option A]
> 2. [Option B]
>
> Which would you prefer, or would you like me to handle it differently?

---

## Error Handling

When a tool fails, follow this protocol — **never silently fail or fabricate content:**

| Error | Action |
|-------|--------|
| `search.py` returns empty results | Retry with rephrased keywords or different language, up to 3 attempts. If still empty, inform user and suggest alternative search terms. |
| `web.py` extraction fails (anti-bot, paywall, timeout) | Inform user the page is inaccessible. Try searching for a cached or alternative version. |
| `youtube.py` / `yt-dlp` fails | Check URL format. If "Sign in to confirm you're not a bot" or timeout: suggest enabling TUN mode proxy, or trying `--cookies-from-browser chrome`, or using a Bilibili alternative. Report the specific error to user. |
| `ffmpeg.py` fails | Report the error message. Check input format compatibility. Suggest alternative format if applicable. |
| Any unknown error | Run `doctor` to diagnose, report findings to user, do not guess. |

**Core principle:** If a tool fails and you cannot recover, tell the user what happened, what you tried, and suggest next steps. Never pretend it succeeded.

---

## Output Format

**Strict portable Markdown only.** The output must render correctly in any Markdown editor (GitHub, Obsidian, Typora, VS Code, etc.).

### Rules

1. **No HTML tags** — no `<br>`, `<div>`, `<table>`, `<sub>`, `<sup>`, or any HTML whatsoever
2. **Table cells must be single-line plain text** — no line breaks, no nested lists, no multi-line content inside a cell
3. If content does not fit single-line table cells, **use a list instead of a table**
4. Use blank lines before and after headings, tables, code blocks, and block quotes to ensure correct parsing
5. Do not use indented code blocks — always use fenced code blocks with triple backticks

### Formatting Toolkit

| Element             | Usage                                 |
| ------------------- | ------------------------------------- |
| **Bold**            | Key conclusions, important numbers    |
| Lists (`-` or `1.`) | Pros/cons, steps, explanations        |
| `✅ ❌ ⚠️`             | Supported / not supported / caution   |
| `> quote block`     | Direct quotes from sources            |
| `` `inline code` `` | Tool names, commands, technical terms |

### Table Example (Use Only When Appropriate)

Tables are for **comparing multiple items with short single-line values:**

```markdown
| Product | Price | Offline | Rating |
| ------- | ----- | ------- | ------ |
| A       | $99   | ✅       | 4.5/5  |
| B       | $199  | ❌       | 4.0/5  |
| C       | Free  | ✅       | 3.5/5  |
```

**Do not use tables when:** content is single-column, cells need multi-line text, or structure requires nesting.

### Source Citations

Inline: `[1]`, `[2]`, etc.

At the end:

```markdown
## Sources
[1] [Title](URL) — Key data description
[2] [Title](URL)
```

---

## Context Management

- **Long content (>2000 words):** Summarize key information after extraction; do not paste raw content into the response
- **Subtitles:** Download to disk by default — only load into context when the user explicitly asks for content analysis (e.g. "summarize this video", "extract info about X")
- **Multiple pages:** Synthesize and integrate findings; do not stack raw page dumps

---

## CLI Tools Reference

> 📁 **Working directory:** All commands run from `~/.agents/skills/skilless/`.
> The `cd ~/.agents/skills/skilless/ &&` prefix is shown in full for each command to ensure correct execution.

### Search (Exa AI)

```bash
cd ~/.agents/skills/skilless/ && uv run scripts/search.py "your query"
cd ~/.agents/skills/skilless/ && uv run scripts/search.py "your query" 10
```

### Web Reader (Jina Reader)

```bash
cd ~/.agents/skills/skilless/ && uv run scripts/web.py <url>
```

### Video / Transcript Extractor

**`youtube.py`** — One-step subtitle + metadata extraction (recommended for most cases):

```bash
cd ~/.agents/skills/skilless/ && uv run scripts/youtube.py "<url>"
```

**`yt-dlp` direct** — Advanced usage (custom formats, audio-only, subtitle listing):

```bash
cd ~/.agents/skills/skilless/ && uv run yt-dlp "URL"
cd ~/.agents/skills/skilless/ && uv run yt-dlp --list-subs "URL"
cd ~/.agents/skills/skilless/ && uv run yt-dlp --write-subs --write-auto-subs "URL"
cd ~/.agents/skills/skilless/ && uv run yt-dlp -x --audio-format mp3 "URL"
```

Supported platforms (1700+ via yt-dlp): YouTube, Bilibili, TikTok, Twitter/X, Twitch, Vimeo, Dailymotion, Niconico, Rumble, Odysee, SoundCloud, Reddit, Instagram, Facebook, and many more.

**Download path rules:**
- Inside a project directory (e.g. `~/codes/my-project/`) → download to current directory
- At home directory (`~`) → default to `~/Downloads/`
- **Never download to `/tmp`** — requires special permissions, files may auto-delete

**YouTube troubleshooting:**
- "Sign in to confirm you're not a bot" or timeout → enable TUN mode proxy, or try `--cookies-from-browser chrome`, or use Bilibili as alternative

### FFmpeg (Media Converter)

```bash
cd ~/.agents/skills/skilless/ && uv run scripts/ffmpeg.py <input> <output>
cd ~/.agents/skills/skilless/ && uv run scripts/ffmpeg.py video.mkv output.mp4
cd ~/.agents/skills/skilless/ && uv run scripts/ffmpeg.py audio.wav output.mp3
cd ~/.agents/skills/skilless/ && uv run scripts/ffmpeg.py input.mp4 output.mp4 -crf 28
```

Supported formats: mp4,

---

## Cross-References

- **Need a detailed report?** → After completing research, invoke `skilless.ai-writing` to produce professional reports, articles, documentation, or any structured written content from your findings
- **Research goal unclear?** → Invoke `skilless.ai-brainstorming` to define scope, clarify questions, and explore approaches before starting a deep investigation