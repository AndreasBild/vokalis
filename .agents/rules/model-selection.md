# Model Selection & Task Allocation Framework

## 1. Core Philosophy: The Right Model for Every Task
To balance execution speed, token economy, and reasoning capability, tasks are routed across two distinct model tiers. Always use the most efficient model that reliably accomplishes the task.

```mermaid
flowchart TD
    Task["Incoming Task"] --> Complexity{"Task Nature?"}
    Complexity -->|"Standard HTML/CSS/JS,\nBug Fixes, Scripts,\nPRs, Validation, a11y"| Tier1["Tier 1: Gemini 3.8 Flash (Medium)\n• Ultra-fast execution\n• Minimal token consumption\n• Low latency response"]
    Complexity -->|"Multi-System Architecture,\nComplex Concurrency,\nDeep Algorithmic Refactoring"| Tier2["Tier 2: Gemini 2.5 Pro / Thinking\n• Maximum reasoning depth\n• High contextual synthesis\n• Complex architectural planning"]
```

---

## 2. Model Tier Matrix

| Tier | Recommended Model | Primary Scope & Workflows | Token & Latency Profile |
| :--- | :--- | :--- | :--- |
| **Tier 1: Workhorse (Default)** | **Gemini 3.8 Flash (Medium)** | • HTML5 semantic development & landmark structuring<br>• CSS design token updates & responsive layouts<br>• Vanilla JS event handlers, DOM safety, form validation<br>• Running local tests, validation scripts & linter execution<br>• Git branch management, commits & PR drafting<br>• SEO metadata, Schema.org updates, a11y audits | • **Ultra-Low Latency**<br>• **Minimal Token Cost**<br>• **Highest Throughput** |
| **Tier 2: Escalation (Deep Reasoning)** | **Gemini 2.5 Pro / Thinking Models** | • System-wide architectural migrations & re-platforming<br>• Complex concurrency & distributed state engines<br>• High-ambiguity initial project planning & security threat modeling<br>• Subtle race condition debugging & complex mathematical models | • High reasoning depth<br>• Extended thinking budget<br>• Selective invocation |

---

## 3. Allocation Rules & Invariants
1. **Default to Tier 1:** All standard web development tasks (HTML, CSS, JavaScript, Git, CI scripts, quality gates) default to **Gemini 3.8 Flash (Medium)**.
2. **Escalation Protocol:** Only escalate to Tier 2 if a task presents severe architectural ambiguity, multi-system architectural conflicts, or requires deep algorithmic proofs.
3. **De-escalation:** Once an architectural plan is established by a deep reasoning model, switch back to Tier 1 for rapid, token-efficient implementation and validation.
4. **Token Preservation:** Never use heavy reasoning models for routine file edits, formatting, or command execution.
