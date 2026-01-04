# Terminology Guide

This document defines the standard terminology used throughout this repository to ensure clarity and consistency.

## AI-Related Terms

### Core Concepts

**AI tool** ✅
- **Definition:** Any software application that uses artificial intelligence
- **Use when:** Referring generally to AI-powered software
- **Examples:** "AI tools can help you code faster" / "Choose the right AI tool for your task"

**AI assistant** ✅
- **Definition:** An AI tool designed to help users with tasks through interaction
- **Use when:** Referring to conversational or interactive AI systems
- **Examples:** "ChatGPT is an AI assistant" / "Ask your AI assistant for help"
- **Note:** More specific than "AI tool" - implies interactive help

**AI agent** ✅
- **Definition:** An AI system that can take actions autonomously or semi-autonomously
- **Use when:** Referring to AI with capabilities beyond simple responses (like browser control, code execution, multi-step tasks)
- **Examples:** "Use an AI agent to help resolve complex merge conflicts" / "Agent-assisted resolution"
- **Note:** Most specialized term - implies autonomous capability

### Product Names

**GitHub Copilot** ✅
- Always use full name on first reference
- Can use "Copilot" after first reference if context is clear
- Capitalize both words: "GitHub Copilot" not "Github Copilot" or "github copilot"
- **Incorrect:** "Copilot" (when first mention), "Github Copilot", "github copilot"
- **Correct:** "GitHub Copilot helps you code" then "Copilot suggests completions"

**GitHub Copilot Chat** ✅
- The conversational interface for GitHub Copilot
- Don't abbreviate to "Copilot Chat" on first use
- **Correct:** "GitHub Copilot Chat can explain code"

**GitHub Copilot Workspace** ✅
- The browser-based environment for complex changes
- Always use full name
- **Correct:** "GitHub Copilot Workspace handles multi-file edits"

**ChatGPT** ✅
- One word, camelCase: "ChatGPT" not "Chat GPT" or "chatGPT"
- By OpenAI (can mention when relevant)
- **Incorrect:** "Chat GPT", "chatgpt", "Chat-GPT"
- **Correct:** "ChatGPT can explain concepts"

**Claude** ✅
- One word, capitalize first letter only
- By Anthropic (can mention when relevant)
- **Incorrect:** "CLAUDE", "claude"
- **Correct:** "Claude excels at code review"

**Cursor** ✅
- AI-native code editor
- One word, capitalize first letter
- **Correct:** "Cursor is an AI-powered editor"

**Windsurf** ✅
- AI-native code editor
- One word, capitalize first letter
- **Correct:** "Windsurf offers AI assistance"

### Usage Hierarchy

```
AI tool (most general)
    ↓
AI assistant (interactive, conversational)
    ↓
AI agent (autonomous actions, complex tasks)
```

**Examples in context:**
- "Many **AI tools** are available for coding" (general category)
- "**AI assistants** like ChatGPT can answer questions" (interactive help)
- "**AI agents** can help resolve complex merge conflicts by taking multiple steps" (autonomous actions)

## GitHub/Git Terms

### Repository

**Repository** ✅
- Full term, don't abbreviate on first use
- Can use "repo" after first reference
- **Correct:** "A repository stores your code" then "clone the repo"

**Repo** ✅
- Informal short form
- OK to use after first mention of "repository"
- **Avoid:** Using "repo" on first mention in formal documentation

### Branches and Commits

**branch** ✅ (lowercase when general)
- "Create a feature branch"
- "Switch to the main branch"

**Branch names** ✅ (as written in repository)
- `main` not "Main" (unless it's actually capitalized in the repo)
- `feature/auth` not "Feature/Auth"
- Use code formatting: `main` not main

**commit** ✅ (lowercase when used as noun or verb)
- "Make a commit"
- "Commit your changes"

**Commit message** ✅
- Two words, not hyphenated
- **Correct:** "Write a clear commit message"

### Conflicts and Issues

**Merge conflict** ✅
- Two words, not hyphenated
- Lowercase unless starting sentence
- **Correct:** "Resolve the merge conflict"

**Pull request** or **PR** ✅
- Two words or abbreviation
- Capitalize in titles: "Pull Request"
- Lowercase in body: "Create a pull request" or "open a PR"

## Workflow Terms

**Single-agent workflow** ✅
- Hyphenated when used as adjective
- **Correct:** "Use a single-agent workflow" / "single-agent approach"

**Multi-agent workflow** ✅
- Hyphenated when used as adjective
- **Correct:** "A multi-agent workflow uses multiple AI tools"

**Pair programming** ✅
- Two words, not hyphenated
- **Correct:** "AI pair programming"

## Common Mistakes to Avoid

### ❌ Incorrect Terminology

**"Github"** → ✅ **"GitHub"** (capital H)

**"Git Hub"** → ✅ **"GitHub"** (one word)

**"ChatGPT-4"** → ✅ **"ChatGPT" or "GPT-4"** (don't combine)

**"Co-pilot"** → ✅ **"Copilot"** (one word, no hyphen)

**"Copilot AI"** → ✅ **"GitHub Copilot"** (full product name)

**"claude"** → ✅ **"Claude"** (capital C)

**"AI-assistant"** → ✅ **"AI assistant"** (no hyphen when noun)

**"git"** → ✅ **"Git"** (capital G when referring to the tool)

**"git hub"** → ✅ **"GitHub"** (one word, capital H)

### ❌ Inconsistent Usage

**Don't mix:**
- "AI tool" and "AI assistant" when referring to the same thing in the same context
- "agent" and "assistant" interchangeably (they have specific meanings)
- Full product names and abbreviations in the same paragraph

**Do:**
- Use "AI tool" for general references
- Use "AI assistant" for interactive/conversational systems
- Use "AI agent" for autonomous/complex task systems
- Introduce full product names before using abbreviations

## Context-Specific Guidelines

### In Documentation

**First reference:** Use full, formal term
- "GitHub Copilot is an AI assistant..."
- "A repository contains your project files..."

**Subsequent references:** OK to use short form if clear
- "Copilot can suggest..."
- "Clone the repo..."

### In Examples

**Code comments:** Can be informal
```python
# Ask Copilot to complete this
```

**User prompts:** Natural language OK
```
"Hey ChatGPT, explain this function"
```

### In Titles and Headers

**Use formal names:**
- ✅ "GitHub Copilot" not "Copilot"
- ✅ "AI-Assisted Development" not "AI Assisted Development" (hyphenate compound adjectives)

## When in Doubt

1. **Check the official product website** for correct capitalization and spacing
2. **Be consistent within the same document**
3. **Err on the side of being more formal/complete** rather than abbreviated
4. **Use the hierarchy:** tool → assistant → agent (most to least general)

## Updates

This guide may be updated as:
- New AI tools emerge
- Product names change
- Community conventions evolve

Last updated: 2024-01-04
