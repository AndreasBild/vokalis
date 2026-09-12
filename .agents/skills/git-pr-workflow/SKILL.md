---
name: git-pr-workflow
description: End-to-end 6-stage development lifecycle, branch isolation, selective staging, and automated PR handoff.
---

# Git PR Workflow & Branch Lifecycle Skill

## 1. Six-Stage Lifecycle Execution
1. **Analysis:** Review requirements, tokens (`css/style.css`), DOM handlers (`js/main.js`), and domain rules.
2. **Architecture:** Plan HTML5 landmark structure, verify contrast/a11y, and reuse `:root` tokens.
3. **Branch Isolation:** Never work on `main`. Create a topic branch:
   ```bash
   git checkout -b <type>/<descriptive-name>
   ```
   Valid types: `feature/`, `fix/`, `chore/`, `perf/`.
4. **Implementation:** Write clean, complete vanilla code without stubs or placeholders.
5. **Quality Gate:** Run regression test suite:
   ```bash
   python3 scripts/validate.py
   ```
6. **Automated PR & Review:** Stage selectively and submit PR.

## 2. Selective Staging & Commits
* **Selective Staging:** Never use `git add .` or `git add -A`. Stage files explicitly:
  ```bash
  git add index.html css/style.css
  ```
* **Conventional Commits:** Write concise imperative commit messages:
  ```bash
  git commit -m "feat: add accessibility enhancement to navigation menu"
  ```

## 3. Automated PR Creation
* Create the PR using `scripts/create_pr.py` or GitHub CLI:
  ```bash
  gh pr create --title "feat: descriptive title" --body-file .github/pull_request_template.md
  ```
* Verify that all quality gate checklist items in the template are checked.
