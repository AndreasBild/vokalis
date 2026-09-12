---
name: optimize-context
description: Self-auditing routine to detect rule bloat, audit context budgets, prune obsolete rules, and adapt to new model releases.
---

# Optimize Context & Rule Audit Skill

## Overview
Periodic maintenance routine to audit root kernel size, prevent rule bloat, verify prompt token budgets, and adjust model tier configurations.

## 1. Kernel Budget Audit
* **Line & Token Threshold:**
  - Verify that the root `AGENTS.md` stays around ~35 lines (< 400 tokens).
  - Any procedural execution guides, code snippets, or extensive examples added to `AGENTS.md` must be extracted into `.agents/rules/` or dedicated `.agents/skills/`.
* **Verification Command:**
  ```bash
  wc -l AGENTS.md
  ```
  Ensure line count remains $\le 40$.

## 2. Rule & Skill Bloat Detection
* **Redundancy Check:** Scan `.agents/rules/` and `.agents/skills/` for overlapping instructions or conflicting constraints.
* **Progressive Disclosure:** Ensure heavy operational workflows (e.g. deployments, complete checklists, schema contracts) are referenced via the Progressive Skill Router rather than loaded unconditionally into root context.
* **Dead Code / Stale Guides:** Remove deprecated practices, dead URLs, or legacy configurations.

## 3. Subagent Context Offloading Audit
* Confirm that verbose operations (e.g., full-page scrapes, massive CI/CD log parsing) are delegated to subagents returning executive memos rather than flooding the main agent context.

## 4. Model Tier Adaptation
* Review model capabilities and update the Dynamic Model Tier matrix when newer model versions are released:
  - Verify if Tier 1 (e.g., Flash/Medium) can handle expanded reasoning tasks.
  - Reserve Tier 2 (Pro/Thinking) strictly for complex architectural refactoring and ambiguous system design.
