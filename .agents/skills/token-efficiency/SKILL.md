---
name: token-efficiency
description: Operational patterns and workflows for maximizing token efficiency, conserving context window, and minimizing model compute.
---

# Token Efficiency Skill

## Overview
Guides agents through token-saving workflows, targeted inspection techniques, compact editing, and concise communication to maximize throughput and minimize latency.

---

## 1. Targeted Code Inspection Workflow

### Step 1: Find Line Numbers with Ripgrep
Never read an entire file to locate a snippet. Use `grep_search` with specific query terms and `Includes` globs:
```json
{
  "Query": "modal-dialog",
  "SearchPath": "/Users/andreasbild/IdeaProjects/vokalis",
  "Includes": ["*.html", "*.js"],
  "MatchPerLine": true
}
```

### Step 2: Slice-Based Inspection
Read only the relevant lines (30–80 lines) using `view_file`:
```json
{
  "AbsolutePath": "/Users/andreasbild/IdeaProjects/vokalis/index.html",
  "StartLine": 120,
  "EndLine": 170
}
```

---

## 2. Surgical File Edits
* **Single Contiguous Edits:** Use `replace_file_content` with concise anchors (3–10 lines above and below).
* **Multi-Point Edits:** Use `multi_replace_file_content` in a single tool call rather than sequential calls.
* **Avoid Whole File Rewrites:** Overwriting an entire file with `write_to_file` unnecessarily consumes thousands of output tokens.

---

## 3. Command Execution Best Practices
* Use quiet/silent flags: `git status -s`, `pytest -q`, `python3 -m py_compile ...`.
* Avoid commands that stream infinite output or require interactive paging.
* Check exit codes (`0` vs `1`) directly instead of parsing long logs.

---

## 4. Response Guidelines
* Deliver direct, bulleted answers.
* Cite exact file paths and line ranges with markdown links: `[file.html](file:///path/to/file.html#L50-L65)`.
* Do not duplicate information already present in artifacts or tool outputs.
