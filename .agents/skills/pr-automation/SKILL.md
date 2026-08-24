---
name: pr-automation
description: Automate GitHub Pull Request creation and quality review checklist verification for topic branches in Vokalis.
---

# Pull Request Automation Skill

## Overview
Automates the submission and validation of Pull Requests targeting `main` after local quality gates pass.

## Workflow

### 1. Pre-requisite Check
- Ensure working tree is clean (`git status`).
- Ensure current branch is not `main` (`git branch --show-current`).
- Run the local quality gate:
  ```bash
  python3 scripts/validate.py
  ```

### 2. Autonomous PR Creation
Use the GitHub CLI (`gh`) or the fallback automation script:
```bash
# Option A: via GitHub CLI (recommended if installed & authenticated)
gh pr create --base main --title "feat/fix/chore: <title>" --body-file .github/pull_request_template.md

# Option B: via Python automation helper
python3 scripts/create_pr.py --title "feat/fix/chore: <title>" --body "Detailed summary following PR template"
```

### 3. Review Checklist Verification
Confirm all items in `.github/pull_request_template.md` are fulfilled:
- Topic branch isolation verified.
- Semantic HTML5 structure with single `<h1>`.
- WCAG 2.1 Level AA accessibility compliant.
- CI quality gate checks passing.
