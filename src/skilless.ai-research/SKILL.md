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

## Mode 2: Deep Research

多源对比、事实核查、结构化输出。

### ⚠️ 必须使用 Todo（强制）

**创建 todo list 的场景**：

- ✅ 任务涉及 **多个来源或步骤（3+项）**
- ✅ 用户要求 **研究、调查、对比、分析**
- ✅ 关键词：*research, investigate, guide, plan, analyze, compare, 研究, 攻略, 整理*
- ✅ **任务耗时 > 5 分钟**

**可跳过 todo 的场景**：

- ❌ 单源查询（仅读取一个URL）
- ❌ 简单事实核查（单个搜索查询，< 2 分钟）

---

### 研究工作流

#### Step 1: 明确范围

- 核心问题是什么？
- 需要什么类型的来源（官方文档、媒体报道、论文、评测）？
- 时间范围和数据维度有哪些？

#### Step 2: 多维搜索

- 不同关键词组合
- 宽泛和具体的搜索词
- 多语言查询（必要时）

#### Step 3: 提取核心来源

- 优先权威来源（官网、官方文档）
- 记录关键发现
- 保存 URL 用于引用

#### Step 4: 提取视频内容（如需）

- 从 talks、tutorials、interviews 提取字幕

#### Step 5: 交叉验证

- 至少 **3 个独立来源**验证关键事实
- 标记冲突信息

#### Step 6: 综合输出

- 编译结构化报告
- **表格优先，简洁清晰**

---

## Output Format: Professional Research Report

> **核心原则**：
> - **表格优先** — 用对比表、推荐表、可视化条快速传达结论
> - **来源标注** — 每个数据点标注 `[src]` 或 `[1]`
> - **简洁可扫描** — 避免冗长文字，用要点和表格

---

### 模板 1：产品对比报告

```markdown
# [产品类别] 对比（2026）

> **研究日期**：YYYY-MM-DD  
> **数据来源**：[来源类型]

## 🎯 快速推荐

| 需求 | 推荐 | 价格 | 推荐度 |
|------|------|------|--------|
| **🏆 综合最佳** | [Product] | ¥XXX | ⭐⭐⭐⭐⭐ |
| **💰 性价比** | [Product] | ¥XXX | ⭐⭐⭐⭐⭐ |
| **🏢 企业级** | [Product] | ¥XXX | ⭐⭐⭐⭐ |

---

## 📊 核心对比

| 产品 | 价格 | 核心指标1 | 核心指标2 | 推荐度 |
|------|------|----------|----------|--------|
| **[Product A]** | ¥XX [src] | 数据 | 数据 | ⭐⭐⭐⭐⭐ |
| [Product B] | ¥XX [src] | 数据 | 数据 | ⭐⭐⭐⭐ |
| [Product C] | ¥XX [src] | 数据 | 数据 | ⭐⭐⭐ |

### 价格可视化

| 产品 | 价格 | 对比 |
|------|------|------|
| [Product A] | ¥XXX | ████████░░░░░░░░░░░░ 最优 |
| [Product B] | ¥XXX | ████████████░░░░░░░░ |
| [Product C] | ¥XXX | ████████████████████ 最高 |

---

## 重点推荐

### 🏆 [Product A] — [标语]

**核心优势**：[一句话总结]

- **价格**：¥XXX [src]
- **优点**：✅ [Pro 1]、✅ [Pro 2]
- **缺点**：❌ [Con 1]
- **适用场景**：[Target users]

---

## 🔍 关键发现

1. **[发现1]** — [数据点] [src]
2. **[发现2]** — [数据点] [src]
3. **[发现3]** — [数据点] [src]

---

## 来源

[1] [Title](URL) — [Key data]  
[2] [Title](URL) — [Key data]
```

---

### 模板 2：事实核查报告

```markdown
# [主题] 核实报告

> **研究日期**：YYYY-MM-DD

## 🎯 核心结论

| 事实 | 核实结果 | 置信度 |
|------|----------|--------|
| [Claim 1] | ✅ 确认 | 100% |
| [Claim 2] | ⚠️ 部分正确 | 80% |
| [Claim 3] | ❌ 不准确 | 95% |

---

## 详细核实

### [Claim 1]
- **核实结果**：✅ 确认
- **证据**：[具体数据] [1][2]
- **来源独立性**：通过 [Source A] 和 [Source B] 双重确认

### [Claim 2]
- **核实结果**：⚠️ 部分正确
- **实际数据**：[正确数据] [3]
- **差异说明**：[解释]

---

## 来源验证

| 来源 | 类型 | 置信度 |
|------|------|--------|
| [Official Site] | 官方 | 100% |
| [News Article] | 媒体 | 85% |
| [Community Wiki] | 社区 | 80% |

---

## 来源

[1] [Title](URL)  
[2] [Title](URL)
```

---

### 模板 3：行业分析报告

```markdown
# [行业/主题] 市场分析

> **研究日期**：YYYY-MM-DD  
> **数据来源**：[来源类型]

## 📊 市场概览

| 指标 | 数据 | 年份 | 来源 |
|------|------|------|------|
| 市场规模 | $XXB | 2025 | [1] |
| 增长率 | XX% CAGR | 2024-2028 | [2] |
| Top 1 厂商 | Company A (XX%) | 2025 | [3] |

---

## 🏆 竞争格局

| 厂商 | 市占率 | 优势 | 劣势 | 推荐度 |
|------|--------|------|------|--------|
| **Company A** | XX% [src] | ✅ [Strength] | ❌ [Weakness] | ⭐⭐⭐⭐⭐ |
| Company B | XX% [src] | ✅ [Strength] | ❌ [Weakness] | ⭐⭐⭐⭐ |

### 市占率可视化

| 厂商 | 份额 | 分布 |
|------|------|------|
| Company A | XX% | ████████████████░░░░ |
| Company B | XX% | ████████████░░░░░░░░ |

---

## 🔍 关键发现

1. **[发现1]** — [数据点] [src]
2. **[发现2]** — [数据点] [src]

---

## 来源

[1] [Title](URL) — [Data]  
[2] [Title](URL) — [Data]
```

---

### 模板 4：场景分析报告

```markdown
# [场景名称] 分析

> **研究日期**：YYYY-MM-DD  
> **场景描述**：[一句话描述场景需求]

## 🎯 场景推荐

| 方案 | 模型/产品 | 总成本 | 推荐度 |
|------|----------|--------|--------|
| **成本最优** | [Product] | ¥XXX | ⭐⭐⭐⭐⭐ |
| **平衡方案** | [Product] | ¥XXX | ⭐⭐⭐⭐ |
| **效果优先** | [Product] | ¥XXX | ⭐⭐⭐ |

---

## 方案详情

### 方案一：成本最优 🏆

**[Product Name]**

| 项目 | 成本 | 说明 |
|------|------|------|
| [项目1] | ¥XXX | [说明] |
| [项目2] | ¥XXX | [说明] |
| **总计** | **¥XXX** | **[优势]** |

**优点**：
- ✅ [Pro 1]
- ✅ [Pro 2]

**缺点**：
- ❌ [Con 1]

---

## 🔍 关键发现

1. **[发现1]** — [数据点] [src]
2. **[发现2]** — [数据点] [src]

---

## 来源

[1] [Title](URL)  
[2] [Title](URL)
```

---

## 视觉元素指南

### 星级评分

```
⭐⭐⭐⭐⭐ (5星) — 顶级/最优
⭐⭐⭐⭐ (4星) — 优秀
⭐⭐⭐ (3星) — 良好/可用
⭐⭐ (2星) — 一般
⭐ (1星) — 较差
```

### 可视化条

```
████████████████████░░░░ 80% — 数值对比
████████░░░░░░░░░░░░░░░░ 40% — 成本/份额
```

### 状态指示器

```
✅ 支持/有/是
❌ 不支持/无/否
⚠️ 部分/需注意
```

### 推荐标签

```
🏆 最佳/最强
💰 性价比
🆓 免费
🏢 企业级
⭐ 推荐
```

---

## 质量检查清单

提交前确认：

- [ ] **表格优先** — 第一眼看到对比表或总结表
- [ ] **数据有源** — 格式：`数据 [1]` 或 `数据 [src]`
- [ ] **星级评分** — 用 ⭐ 快速评估质量
- [ ] **可视化对比** — 用进度条或方块字符对比
- [ ] **快速结论** — 3-5 行表格展示顶级推荐
- [ ] **简洁无冗余** — 去除冗长叙述，保持可扫描性

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