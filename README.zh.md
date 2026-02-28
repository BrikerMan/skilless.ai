<h1 align="center">✨ skilless.ai</h1>

<p align="center">
  <strong>赋予 Agent 真实数据超能力</strong>
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge" alt="MIT License"></a>
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.12+-green.svg?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.12+"></a>
  <a href="https://github.com/brikerman/skilless.ai/stargazers"><img src="https://img.shields.io/github/stars/brikerman/skilless.ai?style=for-the-badge" alt="GitHub Stars"></a>
</p>

<p align="center">
  <a href="#快速安装">快速安装</a> · <a href="README.md">English</a> · <a href="#四大工具">核心工具</a> · <a href="#三大技能">AI 技能</a> · <a href="https://skilless.ai">官网</a>
</p>

---

## 为什么需要 Skilless？

你的 AI 写东西很厉害，但让它去网上找点信息，它就傻了：

- 🔍 "帮我搜一下这款产品的评价" → **没有好用的免费搜索**，要么付费要么质量差
- 🌐 "帮我看看这个网页写了啥" → **抓回来一堆 HTML 标签**，根本没法读
- 📺 "这个 YouTube 视频讲了什么" → **拿不到字幕**，手动处理太麻烦
- 📡 "帮我追踪这几个新闻源，有更新告诉我" → **要自己装库写代码**

**Skilless 把这件事变成一行命令：**

```bash
curl -LsSf https://skilless.ai/install | bash
```

自动检测环境、创建隔离虚拟环境、安装所有依赖。不污染系统，不需要 sudo，随时可卸载。

---

## 安装后能做什么

> 💡 **推荐搭配：** [OpenCode](https://opencode.ai) — 开源免费，和 Skilless 配合开箱即用。也支持 OpenClaw、Kilo Code、Cursor、Claude Code。

直接告诉你的 AI 你想要什么——它读完技能文件，自己知道该怎么做：

- "帮我在网上搜一下这款产品的口碑" → 直接搜索
- "帮我看看这个链接写了什么" → 提取任意网页的干净内容
- "这个 YouTube 视频讲了什么？" → 提取字幕文字
- "帮我看看这个订阅源最近有什么更新" → 解析并总结订阅内容

**你不需要记任何命令。** 这正是 Skilless 的意义所在。

---

## 三大技能

技能以 `SKILL.md` 形式安装到 `~/.agents/skills/`，Agent 自动读取，知道何时调用哪个能力：

| 技能 | 用途 |
|------|------|
| **头脑风暴** | 通过对话将模糊想法转化为可执行计划，提供 2-3 种方案及取舍分析 |
| **深度调研** | 多源交叉验证的深度调研——从静态文本生成器变为主动互联网研究员 |
| **专业写作** | 基于实际调研数据撰写文章、技术文档、报告 |

---

## 快速安装

**Mac / Linux**

```bash
curl -LsSf https://skilless.ai/install | bash
```

**Windows (PowerShell)**

```powershell
irm https://skilless.ai/install.ps1 | iex
```

<details>
<summary>这行命令实际安装了什么？（点击展开）</summary>

1. **安装 uv** — 极速 Python 包管理器，装到 `~/.local/bin`
2. **网络检测** — 自动识别网络环境，国内自动切换清华 TUNA 镜像源
3. **隔离部署** — 在 `~/.agents/skills/skilless.ai/` 创建完全隔离的虚拟环境，安装所有依赖：`yt-dlp` `fastmcp` `jina reader` `feedparser`
4. **暴露 CLI** — 生成 `skilless.ai` 可执行文件，即刻可用

*不污染系统环境 · 不需要 sudo · 随时可卸载*
</details>

---

## 技术栈

| 工具 | 用途 |
|------|------|
| [Jina Reader](https://github.com/jina-ai/reader) | 网页提取 |
| [Exa](https://exa.ai) | AI 语义搜索，免费，无需 Key |
| [yt-dlp](https://github.com/yt-dlp/yt-dlp) | 视频与字幕提取，支持 1700+ 站点 |
| [FFmpeg](https://ffmpeg.org) | 媒体转换与压缩 |
| [uv](https://github.com/astral-sh/uv) | 极速 Python 包管理器，隔离部署 |

---

## 常见问题

<details>
<summary><strong>需要 API Key 吗？</strong></summary>

不需要。所有工具均使用免费方案：Exa 搜索通过 MCP 免费接入，Jina Reader 无需 Key，yt-dlp 完全本地运行。
</details>

<details>
<summary><strong>会修改系统环境吗？</strong></summary>

不会。所有内容安装在 `~/.agents/skills/skilless.ai/` 目录的隔离虚拟环境中，不需要 sudo，不影响全局 Python 或 Node.js 环境。
</details>

<details>
<summary><strong>支持哪些 AI 工具？</strong></summary>

任何能读取 `~/.agents/skills/` 下 SKILL.md 文件的工具都支持。推荐使用 **[OpenCode](https://opencode.ai)** — 开源免费。也支持 OpenClaw、Kilo Code、Cursor、Claude Code。
</details>

<details>
<summary><strong>如何卸载？</strong></summary>

```bash
rm -rf ~/.agents/skills/skilless.ai
rm -rf ~/.agents/skills/skilless.ai-*
```
</details>

---

## License

[MIT](LICENSE)
