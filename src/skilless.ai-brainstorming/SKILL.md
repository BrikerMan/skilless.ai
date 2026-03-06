---
name: skilless.ai-brainstorming
description: "Help turn ideas into fully formed plans through collaborative dialogue. Use before starting any project - product features, business ideas, creative projects, or process improvements."
---

# Brainstorming: From Idea to Plan

**Help turn ideas into fully formed plans through natural collaborative dialogue.**

Works for: product features, business ideas, creative projects, process improvements, technical designs, or any new initiative.

## Process

**Explore context → Ask questions → Propose approaches → Get approval → Document plan**

### 1. Understand the Idea

- Check any existing context first (files, docs, prior notes, recent work)
- Gather all clarifying questions upfront — use `ask_questions`, `ask`, or `questions` tool if available; plain text otherwise
- Focus on: purpose, who it's for, constraints, success criteria, timeline

### 2. Clarify Context

- Timeline, budget, resources, technical constraints
- Who is the audience? What does success look like?

### 3. Explore Approaches

- Propose 2-3 different approaches with trade-offs
- Lead with your recommended option and explain why

### 4. Get Approval

- Present plan section by section, get approval before moving on
- Scale depth to complexity of the idea
- Cover dimensions relevant to the domain: structure, key decisions, risks, next steps

### 5. Document the Plan

- Create a clear, actionable plan based on the agreed direction

<HARD-GATE>
Do NOT start implementing until the user has approved the plan. Even "simple" ideas need clarity first.
</HARD-GATE>

## Principles

- **Batch questions by dependency** — Ask independent questions together in one round; hold dependent ones for the next round after getting answers
- **Use question tools first** — If `ask_questions`, `ask`, or `questions` tools are available, use them; otherwise ask in plain text
- **Multiple choice preferred** — Easier to answer than open-ended when possible
- **Start broad, then narrow** — Understand the big picture first
- **No assumptions** — "Simple" ideas often have hidden complexity
- **YAGNI ruthlessly** — Remove unnecessary scope from all plans
- **Explore alternatives** — Always propose 2-3 approaches before settling
- **Incremental validation** — Present plan section by section, get approval before moving on
- **Be flexible** — Go back and clarify when something doesn't make sense

## Cross-References

- **Need research?** → Invoke `skilless.ai-research` to search the web, read pages, extract video transcripts, or conduct deep multi-source investigations
- **Ready to document the plan?** → Invoke `skilless.ai-writing` to produce a professional, structured design doc or report from the approved plan