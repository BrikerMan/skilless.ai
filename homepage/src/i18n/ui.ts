export const languages = {
    en: 'English',
    zh: '中文',
};

export const defaultLang = 'en';

export const ui = {
    en: {
        // Meta
        'meta.title': 'skilless.ai — Empower Your Agent with Real Data',
        'meta.description': 'Give your AI agent real-world data capabilities: search the web, read pages, extract video transcripts, and parse RSS feeds. One command, zero config, no API keys.',

        // Nav
        'nav.github': 'GitHub',
        'nav.docs': 'Docs',
        'nav.lang': '中文',
        'nav.langHref': '/zh/',
        'nav.cta': 'Get Started',

        // Hero
        'hero.title.1': 'Empower Your Agent',
        'hero.title.2': 'with Real Data',
        'hero.subtitle': 'No dependencies. No API keys. No environment setup.',
        'hero.subtitle2': 'One command, ready to go.',
        'hero.desc.1': 'Most AI tools out there need missing dependencies, API keys, or complex configs just to get started.',
        'hero.desc.2': 'Skilless is a',
        'hero.desc.strong': 'trusted, curated skill library',
        'hero.desc.3': 'built for regular people — zero hassle, just works.',
        'hero.tab.mac': 'Mac / Linux',
        'hero.tab.win': 'Windows',
        'hero.copy': 'Copy',
        'hero.install.toggle': 'What does this command actually install?',
        'hero.install.step1.title': 'Downloads latest release',
        'hero.install.step1.desc': '— fetches the latest zip from GitHub Releases at',
        'hero.install.step2.title': 'Installs uv',
        'hero.install.step2.desc': '— sets up uv (ultra-fast Python package manager) if not already installed',
        'hero.install.step3.title': 'Isolated deployment',
        'hero.install.step3.desc': '— creates a fully isolated virtual environment in',
        'hero.install.step3.desc2': 'with all dependencies:',
        'hero.install.step4.title': 'Exposes CLI',
        'hero.install.step4.desc': '— generates the',
        'hero.install.step4.desc2': 'executable, ready to use immediately',
        'hero.install.footer': 'Re-run to upgrade · Zero system pollution · No sudo required',

        // Tools
        'tools.title': 'Four Core Tools',
        'tools.subtitle': 'A complete CLI toolkit that gives your AI Agent direct access to real-world data',
        'tools.search.name': 'search — Semantic Search',
        'tools.search.desc': 'Deep semantic search powered by Exa, optimized for AI use cases. Supports multi-source cross-validation and fact-checking.',
        'tools.search.cmd': 'skilless.ai search "AI trends 2026"',
        'tools.web.name': 'web — Web Reading',
        'tools.web.desc': 'Extracts any webpage into clean Markdown via Jina Reader, ready for LLM context input.',
        'tools.web.cmd': 'skilless.ai web https://example.com',
        'tools.ytd.name': 'ytd — Video Download & Subtitles',
        'tools.ytd.desc': 'Powered by yt-dlp, supports video download and subtitle extraction from YouTube, Bilibili, and 1700+ sites.',
        'tools.ytd.cmd': 'skilless.ai ytd "https://youtube.com/watch?v=xxx"',
        'tools.rss.name': 'rss — RSS Feeds',
        'tools.rss.desc': 'Parse any RSS/Atom feed to track industry trends, breaking news, and stay ahead of the curve.',
        'tools.rss.cmd': 'skilless.ai rss https://example.com/feed.xml',

        // Skills
        'skills.title': 'Three AI Skills',
        'skills.subtitle': 'Use tools individually, or let skills orchestrate them into complete workflows',
        'skills.brainstorm.name': 'Brainstorming',
        'skills.brainstorm.desc': 'Transform vague ideas into actionable plans through natural dialogue. Proposes 2-3 approaches with trade-offs, and acts only after your approval.',
        'skills.research.name': 'Deep Research',
        'skills.research.desc': 'Leverages all four tools for multi-source, cross-validated deep investigation. Turns your AI from a static text generator into an active internet researcher.',
        'skills.writing.name': 'Professional Writing',
        'skills.writing.desc': 'Produces articles, emails, docs, and reports backed by real research data. Ensures every claim is verifiable, well-structured, and tone-matched.',

        // Highlights
        'highlights.zero.title': 'Zero Configuration',
        'highlights.zero.desc': 'One command, fully isolated environment. No Node.js, Homebrew, or global Python required.',
        'highlights.secure.title': 'Secure & Private',
        'highlights.secure.desc': 'Fully open-source and auditable. All credentials and data stored locally. Nothing uploaded to external servers.',
        'highlights.free.title': 'Completely Free',
        'highlights.free.desc': 'MIT licensed. Uses only free and open-source tools. No hidden costs, no subscriptions.',

        // FAQ
        'faq.title': 'FAQ',
        'faq.q1': 'What is Skilless and how is it different from other AI tools?',
        'faq.a1': 'Skilless is a curated AI skill library. Most AI tools require missing dependencies, API keys, or complex setup just to get started. Skilless is built for regular people — one command to install, zero configuration, covering 90% of daily needs including search, web reading, video download & subtitles, and RSS parsing.',
        'faq.q2': 'Do I need to install any dependencies or API keys?',
        'faq.a2': "No. You don't need to manually install anything or configure API keys. The install script automatically downloads uv (an ultra-fast Python package manager) and sets up a completely isolated virtual environment with all dependencies (yt-dlp, fastmcp, jina reader, etc.) — your system stays clean.",
        'faq.q3': 'Which operating systems are supported?',
        'faq.a3': 'macOS, Windows, and Linux. Mac/Linux uses a curl command, Windows uses a native PowerShell script — no Git Bash or WSL required.',
        'faq.q4': 'How do I use it with my AI Agent?',
        'faq.a4': 'After installation, Skilless exposes four CLI commands: search, web, ytd, and rss. Integrate them into any AI agent that supports tool calling (Claude, GPT, Gemini, etc.) to give it real-world information gathering capabilities.',
        'faq.q5': 'What if I run into issues?',
        'faq.a5.prefix': 'Run',
        'faq.a5.cmd': 'skilless.ai doctor',
        'faq.a5.mid': 'to check your system status. For common issues, see the',
        'faq.a5.link': 'Troubleshooting Guide',
        'faq.a5.suffix': ', or report issues on GitHub.',

        // About
        'about.label.author': 'Built with ❤️ by',
        'about.label.company': 'Supported by',
        'about.name': 'Eliyar Eziz',
        'about.role': 'Head of AI Product Development',
        'about.tags': 'Google Developers Expert · AI Builder · Engineer',
        'about.yodo1.badge': 'Forbes Top 30 Companies for Remote Jobs',
        'about.yodo1.desc': 'Yodo1 is your one partner for growing your games, publishing them and launching IP collaborations.',
        'about.yodo1.pitch': 'We are building amazing AI products, join us.',
        'about.yodo1.cta': 'View Open Positions',

        // Hero - LLM tab
        'hero.tab.llm': 'LLM Guide',
        'hero.copy.llm': 'Copy prompt',

        // Footer
        'footer.license': 'MIT License',
    },

    zh: {
        // Meta
        'meta.title': 'skilless.ai — 赋予 Agent 真实数据超能力',
        'meta.description': '赋予 AI Agent 真实世界数据能力：搜索网页、提取内容、下载视频、解析订阅。一行命令，零配置，无需 API Key。',

        // Nav
        'nav.github': 'GitHub',
        'nav.docs': '文档',
        'nav.lang': 'EN',
        'nav.langHref': '/',
        'nav.cta': '免费使用',

        // Hero
        'hero.title.1': '赋予 Agent',
        'hero.title.2': '真实数据超能力',
        'hero.subtitle': '不装依赖，不要 API Key，不折腾环境。',
        'hero.subtitle2': '一行命令，开箱即用。',
        'hero.desc.1': '市面上的 AI 工具要么缺依赖，要么要 API Key，配置半天跑不起来。',
        'hero.desc.2': 'Skilless 是给',
        'hero.desc.strong': '普通人',
        'hero.desc.3': '用的，可信赖的精选技能库 — 无脑上手，直接好用。',
        'hero.tab.mac': 'Mac / Linux',
        'hero.tab.win': 'Windows',
        'hero.copy': '复制',
        'hero.install.toggle': '这行命令实际安装了什么？',
        'hero.install.step1.title': '下载最新版本',
        'hero.install.step1.desc': '— 从 GitHub Releases 下载最新的 zip 包',
        'hero.install.step2.title': '安装 uv',
        'hero.install.step2.desc': '— 如尚未安装，自动设置 uv（极速 Python 包管理器）',
        'hero.install.step3.title': '隔离部署',
        'hero.install.step3.desc': '— 在',
        'hero.install.step3.desc2': '创建完全隔离的虚拟环境，安装所有依赖：',
        'hero.install.step4.title': '暴露 CLI',
        'hero.install.step4.desc': '— 生成',
        'hero.install.step4.desc2': '可执行文件，即刻可用',
        'hero.install.footer': '重新运行即可升级 · 不污染系统环境 · 不需要 sudo',

        // Tools
        'tools.title': '四大核心工具',
        'tools.subtitle': '一套完整的 CLI 工具包，让 AI Agent 直接操作真实世界数据',
        'tools.search.name': 'search — 语义搜索',
        'tools.search.desc': '基于 Exa 的深度语义搜索引擎，专为 AI 场景优化。支持多源交叉验证和事实核查。',
        'tools.search.cmd': 'skilless.ai search "AI trends 2026"',
        'tools.web.name': 'web — 网页读取',
        'tools.web.desc': '通过 Jina Reader 将任意网页提取为干净的 Markdown 格式，用于 LLM 上下文输入。',
        'tools.web.cmd': 'skilless.ai web https://example.com',
        'tools.ytd.name': 'ytd — 视频下载与字幕',
        'tools.ytd.desc': '基于 yt-dlp，支持 YouTube、Bilibili 等 1700+ 站点的视频下载和字幕提取。',
        'tools.ytd.cmd': 'skilless.ai ytd "https://youtube.com/watch?v=xxx"',
        'tools.rss.name': 'rss — RSS 订阅',
        'tools.rss.desc': '解析任意 RSS/Atom feed，追踪行业趋势和实时资讯，掌握前沿动态。',
        'tools.rss.cmd': 'skilless.ai rss https://example.com/feed.xml',

        // Skills
        'skills.title': '三大 AI 技能',
        'skills.subtitle': '工具可独立使用，也可通过技能自动编排为完整的工作流',
        'skills.brainstorm.name': '头脑风暴',
        'skills.brainstorm.desc': '通过自然对话和迭代提问，将模糊想法转化为可执行的完整计划。提出 2-3 种方案及取舍，获得你的确认后再行动。',
        'skills.research.name': '深度调研',
        'skills.research.desc': '调用 search、web、ytd、rss 全部工具，进行多源交叉验证的深度调研。从静态文本生成器变为主动的互联网研究员。',
        'skills.writing.name': '专业写作',
        'skills.writing.desc': '基于实际调研数据撰写文章、邮件、技术文档或报告。确保内容有据可查，结构完整，语气匹配。',

        // Highlights
        'highlights.zero.title': '零配置安装',
        'highlights.zero.desc': '一行命令，自动创建隔离环境。无需 Node.js、Homebrew 或全局 Python。',
        'highlights.secure.title': '安全与隐私',
        'highlights.secure.desc': '完全开源可审计，所有凭证和数据本地存储，不向任何外部服务器上传敏感信息。',
        'highlights.free.title': '完全免费',
        'highlights.free.desc': 'MIT 协议开源。利用免费和开源本地工具，无隐藏费用，无订阅。',

        // FAQ
        'faq.title': '常见问题',
        'faq.q1': 'Skilless 是什么？和市面上的 AI 工具有什么不同？',
        'faq.a1': 'Skilless 是一个精选的 AI 核心技能库。市面上很多 AI 工具要么缺依赖跑不起来，要么需要 API Key 和复杂配置。Skilless 的定位是给普通人用的 — 一行命令安装，零配置开箱即用，覆盖搜索、网页读取、视频下载与字幕、RSS 解析等 90% 的日常需求。',
        'faq.q2': '需要安装哪些依赖？需要 API Key 吗？',
        'faq.a2': '不需要手动安装任何依赖，也不需要 API Key。安装脚本会自动下载 uv（极速 Python 包管理器），并在完全隔离的虚拟环境中安装所有依赖（yt-dlp、fastmcp、jina reader 等），不会污染你的系统环境。',
        'faq.q3': '支持哪些操作系统？',
        'faq.a3': '支持 macOS、Windows 和 Linux。Mac/Linux 使用 curl 命令安装，Windows 使用原生 PowerShell 脚本安装，无需 Git Bash 或 WSL。',
        'faq.q4': '如何与 AI Agent 配合使用？',
        'faq.a4': '安装后，Skilless 暴露 search、web、ytd、rss 四个 CLI 命令。你可以将这些命令集成到任意支持工具调用的 AI Agent 中（Claude、GPT、Gemini 等），使其具备真实世界的信息获取能力。',
        'faq.q5': '遇到问题怎么办？',
        'faq.a5.prefix': '运行',
        'faq.a5.cmd': 'skilless.ai doctor',
        'faq.a5.mid': '检查系统状态。常见问题请查看',
        'faq.a5.link': '排障指南',
        'faq.a5.suffix': '，或在 GitHub Issues 中反馈。',

        // About
        'about.label.author': '本工具由以下作者用心构建',
        'about.label.company': '由以下公司倾情支持',
        'about.name': 'Eliyar Eziz',
        'about.role': 'Head of AI Product Development',
        'about.tags': 'Google Developers Expert · AI Builder · Engineer',
        'about.yodo1.badge': 'Forbes 全球远程办公 Top 30 企业',
        'about.yodo1.desc': 'Yodo1 是您游戏增长、发行和 IP 合作的一站式合作伙伴。',
        'about.yodo1.pitch': '我们正在打造令人惊叹的 AI 产品，加入我们。',
        'about.yodo1.cta': '查看开放职位',

        // Hero - LLM tab
        'hero.tab.llm': 'LLM 指南',
        'hero.copy.llm': '复制提示词',

        // Footer
        'footer.license': 'MIT License',
    },
} as const;
