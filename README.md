<h1 align="center">✨ skilless.ai</h1>

<p align="center">
  <strong>Empower Your Agent with Real Data</strong>
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge" alt="MIT License"></a>
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.12+-green.svg?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.12+"></a>
  <a href="https://github.com/brikerman/skilless.ai/stargazers"><img src="https://img.shields.io/github/stars/brikerman/skilless.ai?style=for-the-badge" alt="GitHub Stars"></a>
</p>

<p align="center">
  <a href="#quick-install">Quick Install</a> · <a href="README.zh.md">中文</a> · <a href="#four-core-tools">Core Tools</a> · <a href="#three-ai-skills">AI Skills</a> · <a href="https://skilless.ai">Website</a>
</p>

---

## Why Skilless?

Your AI is great at writing and thinking — but ask it to go look something up, and it hits a wall:

- 🔍 "Find recent reviews of this product" → **no good free search**, everything useful costs money
- 🌐 "Read what's on this webpage" → **returns raw HTML soup**, completely unreadable
- 📺 "What does this YouTube video cover?" → **can't extract subtitles**, too much manual work
- 📡 "Follow these news feeds and summarize updates" → **have to write the code yourself**

**Skilless turns this into one command:**

```bash
curl -LsSf https://skilless.ai/install | bash
```

Auto-detects your environment, creates an isolated virtual environment, installs all dependencies. Zero system pollution, no sudo required, uninstalls cleanly.

---

## What You Can Do After Installing

> 💡 **Recommended:** Use [OpenCode](https://opencode.ai) — open source, free, works great with Skilless out of the box. Also compatible with OpenClaw, Kilo Code, Cursor, and Claude Code.

Just tell your AI what you need — it reads the skill files and figures out the rest:

- "Find reviews of this product online" → searches the web
- "Read what's on this page and summarize it" → extracts clean content from any URL
- "What does this YouTube video talk about?" → pulls the transcript
- "What's new in this RSS feed?" → parses and summarizes the feed

**You don't need to remember any commands.** That's the point.

---

## Three AI Skills

Skills are installed as `SKILL.md` files under `~/.agents/skills/`. Your Agent reads them automatically and knows when to use which capability:

| Skill | Purpose |
|-------|---------|
| **Brainstorming** | Turn vague ideas into actionable plans through dialogue — proposes 2-3 options with trade-offs |
| **Research** | Multi-source cross-validated deep research — transforms AI from text generator to active researcher |
| **Writing** | Produce articles, docs, and reports backed by real research data |

---

## Quick Install

**Mac / Linux**

```bash
curl -LsSf https://skilless.ai/install | bash
```

**Windows (PowerShell)**

```powershell
irm https://skilless.ai/install.ps1 | iex
```

<details>
<summary>What does this command actually install?</summary>

1. **Installs uv** — ultra-fast Python package manager, placed in `~/.local/bin`
2. **Network detection** — auto-detects your environment and switches to local mirrors (Tsinghua TUNA in China) if needed
3. **Isolated deployment** — creates a fully isolated virtual environment in `~/.agents/skills/skilless.ai/` with all dependencies: `yt-dlp` `fastmcp` `jina reader` `feedparser`
4. **Exposes CLI** — generates the `skilless.ai` executable, ready to use immediately

*Zero system pollution · No sudo required · Easy to uninstall*
</details>

---

## Technology Stack

| Tool | Purpose |
|------|---------|
| [Jina Reader](https://github.com/jina-ai/reader) | Web page extraction |
| [Exa](https://exa.ai) | AI semantic search, free, no key needed |
| [yt-dlp](https://github.com/yt-dlp/yt-dlp) | Video & subtitle extraction, 1700+ sites |
| [feedparser](https://github.com/kurtmckee/feedparser) | RSS/Atom parsing |
| [uv](https://github.com/astral-sh/uv) | Ultra-fast Python package manager, isolated deployment |

---

## FAQ

<details>
<summary><strong>Do I need API keys?</strong></summary>

No. All tools use free tiers: Exa search is accessed for free via MCP, Jina Reader requires no key, yt-dlp runs entirely locally.
</details>

<details>
<summary><strong>Does this modify my system environment?</strong></summary>

No. Everything is installed in an isolated virtual environment under `~/.agents/skills/skilless.ai/`. No sudo, no changes to global Python or Node.js.
</details>

<details>
<summary><strong>Which AI tools are supported?</strong></summary>

Any tool that reads SKILL.md files from `~/.agents/skills/` will work. We recommend **[OpenCode](https://opencode.ai)** — it's open source and free. Also works with OpenClaw, Kilo Code, Cursor, and Claude Code.
</details>

<details>
<summary><strong>How do I uninstall?</strong></summary>

```bash
rm -rf ~/.agents/skills/skilless.ai
rm -rf ~/.agents/skills/skilless.ai-*
```
</details>

---

## License

[MIT](LICENSE)
