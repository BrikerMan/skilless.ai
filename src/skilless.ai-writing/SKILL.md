---
name: skilless.ai-writing
description: "Help produce written content by researching topics and gathering references. Use when user needs to write articles, emails, documentation, reports, or any content requiring research. Triggers: write, draft, compose, create content, report, article, blog, documentation, summarize, brief, memo."
---

# Writing Skill

**Produce professional, research-backed written content.**

Use when user needs to: write reports, articles, emails, documentation, briefs, memos, or any content that requires research and structured presentation.

## When to Use

- User asks to "write", "draft", "compose", "create content"
- User needs a report, analysis, or documentation
- User wants an article, blog post, brief, or memo
- Any writing task that benefits from research-backed data and citations

---

## Core Principle

Every piece of writing produced by this skill must be **research-first, evidence-based, and professionally structured.** Do not write from general knowledge alone — always gather real data, verify claims, and cite sources.

---

## Writing Process

### Step 1 — Understand the Brief

Before writing anything, clarify:
- **What type of content?** Report, article, email, documentation, memo, etc.
- **Who is the audience?** Executive, technical, general public, etc.
- **What tone?** Formal, conversational, technical, persuasive, etc.
- **What is the desired length?** Brief (1-2 pages), standard (3-5 pages), comprehensive (5+ pages)
- **Are there specific points or questions to address?**

If any of the above is unclear, **use the question tool** to batch-ask the user before proceeding.

### Step 2 — Research (Invoke Research Skill)

**Always research before writing.** Invoke `skilless.ai-research` to gather data:

1. **Determine research depth** based on the writing task:
   - Quick email or short summary → **L1** (1-2 searches)
   - Standard article or comparison → **L2** (3-5 searches, 2-4 page reads)
   - Full report or deep analysis → **L3** (5+ searches, 5+ page reads, cross-source fact-check)

2. **Let the research skill handle tool selection** — it owns all CLI tools (search, web reader, video transcript extractor, media converter) and will choose the right ones based on the task.

3. **Fact-check all key claims** following the research skill's fact-check protocol:
   - Cross-verify key data from 2-3 independent sources
   - Note contradictions and resolve or flag them
   - Mark unverified claims explicitly

4. **Collect citation data** for every fact, statistic, and claim:
   - Source title, URL, publication date
   - Specific data points with original phrasing
   - Author/organization credibility

### Step 3 — Outline

Before writing prose, create a structured outline:
- Start with the conclusion / key finding
- Organize supporting sections logically
- Identify where each data point and citation will go
- Ensure every major claim has a source assigned

### Step 4 — Write

Follow the report structure defined below. Write clearly, concisely, and professionally.

### Step 5 — Review

Before delivering:
- Verify every citation is real and correctly referenced
- Check that the executive summary accurately reflects the full content
- Ensure no unsupported claims remain
- Confirm the output follows the format rules

---

## Report Structure

All reports and substantial writing follow this structure. Adjust section depth based on content length.

### 1. Executive Summary

**Always lead with this.** A self-contained summary that a busy reader can use without reading the full report.

Must include:
- **Key finding or recommendation** — the single most important takeaway, in 1-2 sentences
- **Critical data points** — the 3-5 most important numbers or facts, with citations
- **Context** — why this matters, in 1-2 sentences
- **Recommended action** (if applicable) — what the reader should do

Length: 150-300 words for standard reports, 50-100 words for short briefs.

### 2. Background / Context

- Why this research was conducted
- Scope and limitations
- Key definitions or assumptions

### 3. Findings / Analysis

The detailed body of the report. Organize by theme, question, or comparison dimension.

Requirements:
- **Every claim backed by specific data** — not vague statements like "many users prefer X", but "67% of surveyed users preferred X [3]"
- **Concrete numbers** — prices, percentages, dates, version numbers, performance metrics
- **Source citations on every data point** — inline `[1]`, `[2]`, etc.
- **Comparisons use tables** when data fits single-line cells
- **Contradictions addressed explicitly** — "Source A reports X [1], while Source B reports Y [2]. The discrepancy likely stems from [reason]. Source A is considered more reliable because [reason]."

### 4. Conclusion / Recommendations

- Summarize findings (not a copy of the executive summary — this is more detailed)
- Provide actionable recommendations with rationale
- Note limitations and areas needing further investigation

### 5. Sources

Full citation list at the end:

```markdown
## Sources

[1] [Title](URL) — Key data point used
[2] [Title](URL) — Key data point used
[3] [Title](URL) — Key data point used
```

---

## Writing Standards

### Data Quality

- **Use specific numbers, not vague language.** Instead of "significant growth", write "42% year-over-year growth [2]"
- **Include dates and versions.** Instead of "the latest version supports X", write "v3.2 (released March 2025) supports X [4]"
- **Attribute opinions.** Instead of "X is considered the best", write "Gartner ranked X as the market leader in their 2025 report [5]"
- **Flag uncertainty.** If data is limited, write "Based on available data (single source), X appears to be Y — further verification recommended"

### Tone Matching

Adapt tone to the user's request and audience:

| Audience | Tone | Example phrasing |
|----------|------|-------------------|
| Executive / decision-maker | Formal, concise, action-oriented | "We recommend adopting X based on 35% cost reduction [1]" |
| Technical team | Precise, detailed, specification-focused | "Latency reduced from 120ms to 45ms (p99) under 10K concurrent connections [3]" |
| General public | Clear, accessible, jargon-free | "This means your battery will last about twice as long as the previous model" |
| Internal memo | Direct, brief, bullet-point heavy | "Action needed: approve budget by Friday" |

If the user does not specify tone, **default to professional/formal** for reports and analysis.

### Length Calibration

- Do not pad with filler — every sentence should carry information
- Do not over-compress to the point of losing important nuance
- If the user asks for a "brief" or "summary", aim for 300-500 words
- If the user asks for a "full report" or "detailed analysis", aim for 1000-3000 words
- When in doubt, use the question tool to ask about desired depth

---

## Handling Different Content Types

| Content type | Research depth | Structure | Key focus |
|--------------|---------------|-----------|-----------|
| Full report / analysis | L3 | Full report structure (exec summary through sources) | Data depth, cross-verification, actionable recommendations |
| Article / blog post | L2-L3 | Hook, body sections, conclusion, sources | Engaging narrative, supported claims, clear takeaways |
| Documentation / guide | L2 | Overview, steps/sections, examples, references | Accuracy, completeness, practical examples |
| Email / memo | L1-L2 | Key point first, supporting details, action items | Brevity, clarity, specific asks |
| Comparison / evaluation | L2-L3 | Exec summary, comparison table, detailed analysis, recommendation | Fair representation, concrete metrics, clear winner/tradeoffs |

---

## Asking the User

Use your environment's built-in question/ask tool when needed. Batch related questions into a single call.

| Situation | Example question(s) |
|-----------|---------------------|
| Content type or audience unclear | "To write this effectively: 1) Who is the target audience? 2) What tone — formal report or casual article? 3) Desired length?" |
| Scope too broad to cover well | "This topic is quite broad. Would you like me to: 1) Cover all aspects at a high level 2) Focus deeply on [specific area] 3) Something else?" |
| Research found contradictory data | "My research found conflicting data on [topic]: Source A says X, Source B says Y. How should I handle this in the report? 1) Present both with analysis 2) Go with the more credible source 3) Flag for further investigation" |
| Missing critical information | "I could not find reliable data on [specific point]. Should I: 1) Proceed without it and note the gap 2) Try alternative search approaches 3) Adjust the scope?" |
| Draft complete — follow-up | After delivering the content: "What would you like me to do next? 1) Expand a specific section 2) Adjust tone or format 3) Research additional aspects 4) Create a shorter summary version 5) Something else" |

---

## Output Format

**Strict portable Markdown only.** Must render correctly in any Markdown editor (GitHub, Obsidian, Typora, VS Code, etc.).

### Rules

1. **No HTML tags** — no `<br>`, `<div>`, `<table>`, `<sub>`, `<sup>`, or any HTML whatsoever
2. **Table cells must be single-line plain text** — no line breaks, no nested lists, no multi-line content
3. If content does not fit single-line table cells, **use a list instead of a table**
4. **Blank lines before and after** headings, tables, code blocks, and block quotes
5. **Fenced code blocks only** (triple backticks) — no indented code blocks
6. **No trailing spaces** for line breaks — use separate paragraphs instead

### Formatting Toolkit

| Element | Usage |
|---------|-------|
| **Bold** | Key conclusions, important numbers, recommendations |
| Lists (`-` or `1.`) | Pros/cons, steps, supporting points |
| `✅ ❌ ⚠️` | Supported / not supported / caution |
| `> quote block` | Direct quotes from sources |
| `` `inline code` `` | Technical terms, tool names, commands |

### Source Citations

Inline: `[1]`, `[2]`, etc. — placed immediately after the data point they support.

At the end of every document:

```markdown
## Sources

[1] [Title](URL) — Key data point used
[2] [Title](URL) — Key data point used
```

---

## Cross-References

- **Research & data gathering** → Invoke `skilless.ai-research` for all search, web reading, video transcript extraction, and media operations. The research skill owns all CLI tools (search, web, youtube, ffmpeg) and defines research depth levels (L1–L3)
- **Brief unclear?** → Invoke `skilless.ai-brainstorming` to clarify scope, audience, and direction before starting the writing process