# Git Workflow & Topic Branch Isolation Rules

## 1. Branch Hierarchy & Protection
* **`main` is Protected:** Direct commits or pushes to `main` are strictly forbidden.
* **Topic Branches:** All modifications must be developed in isolated topic branches:
  - `feature/<name>`: New UI sections, interactive components, or features.
  - `fix/<name>`: Bug fixes, layout corrections, broken link repairs.
  - `chore/<name>`: Tooling, dependencies, repository governance, CI workflows.
  - `perf/<name>`: Performance optimizations (asset compression, caching, LCP/CLS tuning).

## 2. Commit Message Standards
* Follow Conventional Commits format:
  - `feat: <summary>`
  - `fix: <summary>`
  - `chore: <summary>`
  - `perf: <summary>`
  - `docs: <summary>`
  - `style: <summary>`
* Keep commit summaries under 72 characters, written in imperative present tense.

## 3. Pre-PR Quality Gate & Automation
* Prior to opening a Pull Request, run the local quality gate:
  ```bash
  python3 scripts/validate.py
  ```
* Once all checks pass, automate PR creation using `scripts/create_pr.py` or `gh pr create`.
* Ensure PR title and body strictly follow `.github/pull_request_template.md`.
