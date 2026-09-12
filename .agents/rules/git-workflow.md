# Git Workflow & Topic Branch Isolation Rules

## 1. Six-Stage Development Lifecycle
1. **Stage 1: Analysis:** Inspect existing tokens (`css/style.css`), JS logic (`js/main.js`), and `.agents/rules/`. Verify healthcare domain semantics and legal constraints (DSGVO/TMG).
2. **Stage 2: Architecture & Design:** Plan HTML5 landmark structure, reuse `:root` tokens, design for zero layout shift (CLS = 0) and WCAG 2.1 AA/AAA compliance.
3. **Stage 3: Branch Isolation:** Switch to dedicated topic branch (`feature/`, `fix/`, `chore/`, `perf/`). Never commit directly to `main`.
4. **Stage 4: TDD & Implementation:** Adhere to `.editorconfig`, write complete implementations with zero stubs, sanitize dynamic DOM (`escapeHtml()`), and pair state changes with ARIA attributes.
5. **Stage 5: Quality Gate:** Run `python3 scripts/validate.py` to verify secrets, HTML landmarks, Schema.org JSON-LD, links, CSS tokens, assets, and script syntax.
6. **Stage 6: Automated PR & Review:** Automate PR via `scripts/create_pr.py` or `gh pr create` using `.github/pull_request_template.md`.

## 2. Branch Hierarchy & Protection
* **`main` is Protected:** Direct commits or pushes to `main` are strictly forbidden.
* **Topic Branches:**
  - `feature/<name>`: New UI sections, interactive components, or features.
  - `fix/<name>`: Bug fixes, layout corrections, broken link repairs.
  - `chore/<name>`: Tooling, dependencies, repository governance, CI workflows.
  - `perf/<name>`: Performance optimizations (asset compression, caching, LCP/CLS tuning).

## 3. Selective Git Staging & Commits
* **Selective Staging:** Always stage specific modified files (`git add <path1> <path2>`). Never run indiscriminate bulk additions (`git add .` or `git add -A`).
* **Conventional Commits:** `feat: <summary>`, `fix: <summary>`, `chore: <summary>`, `perf: <summary>`, `docs: <summary>`. Keep summaries under 72 chars in present tense.

## 4. Pre-PR Quality Gate & Automation
* Prior to opening a Pull Request, run the local quality gate:
  ```bash
  python3 scripts/validate.py
  ```
* Once all checks pass, automate PR creation using `scripts/create_pr.py` or `gh pr create`.
* Ensure PR title and body strictly follow `.github/pull_request_template.md`.
