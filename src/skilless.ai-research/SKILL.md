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

---

## Mode 1: Quick Content Access

| 操作 | 工具 | 用途 |
|------|------|------|
| **Search** | `search.py` | 查找网页、文档、新闻 |
| **Read** | `web.py` | 提取网页文本内容 |
| **Extract** | `youtube.py` | 提取视频字幕/元数据 |
| **Convert** | `ffmpeg.py` | 转换/压缩媒体文件 |

---

## Mode 2: Research

多源研究、深度 fact-check、结构化输出。任务涉及多步骤或多来源时使用 todo list 跟踪进度。

---

### 研究工作流

#### Step 1: 明确范围

开始搜索前先想清楚：

- 核心问题是什么？用户真正想知道的是什么？
- 需要什么类型的来源 — 官方文档、媒体报道、学术论文、用户评测？
- 哪些维度重要（价格、性能、兼容性、时效性...）？
- 结论需要多高的可信度？

#### Step 2: 多轮搜索

**不止搜一次**。分多轮从不同角度逼近答案：

- **宽泛词** — 先了解全貌，找头部来源（如 `site:reddit.com`、官网）
- **具体词** — 定向找精确数据（版本号、价格、规格）
- **反向词** — 搜"问题/缺点/对比/alternatives"，找批评性信息
- **时效词** — 加上年份或"2025"过滤过期内容
- **多语言** — 必要时用中英文分别搜索

每轮结果如果指向新的关键词或来源，继续深挖。

#### Step 3: 深读核心来源

找到来源不等于研究完成，需要真正读进去：

- 优先顺序：官网 > 官方文档 > 权威报告 > 知名媒体 > 社区讨论
- 读完整页面，不只看标题和摘要
- 注意发布时间 — 技术类内容超过 1-2 年可能已过时
- 记录关键数据的原始表述和来源 URL

#### Step 4: Fact-check

研究中最重要的一步，不能跳过：

- **关键数据**至少从 3 个独立来源交叉验证
- 发现来源互相矛盾时，分析原因（时间差？不同版本？利益立场？），说明哪个更可信
- 区分"事实"和"观点"——观点可以引用，但不能当作事实陈述
- 无法核实的数据明确标注"未经独立验证"，不要假装已确认

#### Step 5: 综合输出

- **结论优先** — 开头直接给出最重要的发现或推荐，再展开细节
- **每个数据点附来源** `[1]`，让读者可以自行核实
- **如实呈现不确定性** — 证据不足时说"目前数据有限"，不要强行下结论
- 末尾列出所有引用来源

---

## Output Format

纯 Markdown，**不包含任何 HTML 标签**。

### 表格

适合用表格的情况 — 横向对比多个对象，且每格都是单行短文本：

```markdown
| 产品 | 价格 | 支持离线 | 评分 |
|------|------|----------|------|
| A    | ¥99  | ✅       | ⭐⭐⭐⭐⭐ |
| B    | ¥199 | ❌       | ⭐⭐⭐⭐ |
| C    | 免费  | ✅       | ⭐⭐⭐ |
```

不适合用表格：单列内容、格子里有多行文字、需要嵌套结构 — 改用列表。

### 其他格式

- **加粗** — 关键结论、重要数字
- 列表 — 优缺点、步骤、说明性内容
- `✅ ❌ ⚠️` — 支持/不支持/需注意
- `⭐⭐⭐⭐⭐` — 评分
- `> 引用块` — 来源原文摘录

### 来源

文内用 `[1]` 标注，末尾附完整列表：

```markdown
## 来源

[1] [Title](URL) — 关键数据说明
[2] [Title](URL)
```

---

## CLI Tools Reference

### Search (Exa AI)

```bash
# Basic search (returns 5 results by default)
cd ~/.agents/skills/skilless/ && uv run scripts/search.py "your query"

# Specify number of results
cd ~/.agents/skills/skilless/ && uv run scripts/search.py "your query" 10
```

### Web Reader (Jina Reader)

```bash
# Extract content from any webpage as text
cd ~/.agents/skills/skilless/ && uv run scripts/web.py <url>
```

### Video Downloader / Transcript Extractor (yt-dlp)

> ⚠️ **PEP 668 限制**：macOS 防止直接 pip 安装。必须使用 skilless 虚拟环境：
> ```bash
> cd ~/.agents/skills/skilless/ && uv run yt-dlp [args]
> ```

> 💡 **直接使用 yt-dlp**：
> ```bash
> cd ~/.agents/skills/skilless/ && uv run yt-dlp "URL"           # Download video
> cd ~/.agents/skills/skilless/ && uv run yt-dlp --list-subs "URL"  # List subtitles
> cd ~/.agents/skills/skilless/ && uv run yt-dlp --write-subs --write-auto-subs "URL"
> cd ~/.agents/skills/skilless/ && uv run yt-dlp -x --audio-format mp3 "URL"
> ```

> **下载路径规则**：
> - **项目目录**（如 `~/codes/my-project/`）→ 下载到当前目录
> - **家目录**（`~`）→ 默认下载到 `~/Downloads/`
> - **禁止下载到 `/tmp`** — 需要特殊权限，文件可能自动删除

> **字幕加载规则**：
> - 默认下载字幕文件到当前目录 — **不要自动加载内容到 context**
> - 仅在用户明确要求时读取字幕内容（如"总结这个视频"、"提取关于X的内容"）
> - 原因：完整字幕可能很长，会不必要地拖慢对话

```bash
# Extract subtitles/transcript/metadata from any video URL
cd ~/.agents/skills/skilless/ && uv run scripts/youtube.py "<url>"

# Supported platforms (1700+):
# YouTube, Bilibili, TikTok, Twitter/X, Twitch, Vimeo,
# Dailymotion, Niconico, Rumble, Odysee, SoundCloud,
# Reddit video, Instagram, Facebook Video, and many more
```

> ⚠️ **YouTube 故障排查**：
> - 错误 "Sign in to confirm you're not a bot" → IP 被 YouTube 反爬
> - 国内网络直接连接失败（超时/拒绝）→ 需要代理
> - **解决方案**：
>   1. 代理客户端切换为 **TUN 模式**（全局流量接管）
>   2. 或设置环境变量：`export HTTPS_PROXY=http://127.0.0.1:<port>`
>   3. 从浏览器导出 cookies：`yt-dlp --cookies-from-browser chrome "URL"`
>   4. 使用 Bilibili 替代（通常更稳定，无需代理）

### FFmpeg (Media Converter)

```bash
# Convert or compress video/audio files
cd ~/.agents/skills/skilless/ && uv run scripts/ffmpeg.py <input> <output>

# Examples:
uv run scripts/ffmpeg.py video.mkv output.mp4        # Convert video
uv run scripts/ffmpeg.py audio.wav output.mp3        # Convert audio
uv run scripts/ffmpeg.py input.mp4 output.mp4 -crf 28  # Compress

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