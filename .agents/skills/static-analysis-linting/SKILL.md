---
name: static-analysis-linting
description: Perform static analysis, linting, syntax verification, and secret scanning on HTML, CSS, JavaScript, and Python scripts across the Vokalis repository.
---

# Static Analysis & Linting Skill

## Overview
Inspects the repository for syntax correctness, code hygiene, CSS token compliance, and sensitive credentials without running live browser instances.

## Execution Checklist

### 1. Python Syntax & Bytecode Compilation
```bash
python3 -m py_compile scripts/deploy.py scripts/create_pr.py scripts/validate.py
```

### 2. Secret Leak Scanning
Scan for leaked access keys and credentials:
```bash
python3 -c "
import os, re, sys
patterns = [r'AKIA[0-9A-Z]{16}', r'ghp_[0-9a-zA-Z]{36}', r'-----BEGIN']
leaks = []
for root, dirs, files in os.walk('.'):
    dirs[:] = [d for d in dirs if d not in {'.git', '.venv', '__pycache__'}]
    for file in files:
        if file.endswith(('.png', '.webp', '.ico', '.woff2')):
            continue
        p = os.path.join(root, file)
        with open(p, 'r', encoding='utf-8', errors='ignore') as f:
            for i, line in enumerate(f, 1):
                if any(re.search(pat, line) for pat in patterns):
                    leaks.append((p, i))
if leaks:
    print('❌ Leaks detected:', leaks)
    sys.exit(1)
print('✅ Zero secret leaks detected.')
"
```

### 3. CSS Token Verification
Ensure that no raw hex colors are introduced in component styles:
- Verify that color rules reference `var(--primary)`, `var(--accent)`, `var(--text-main)`, etc.
- Verify `contain-intrinsic-size` is paired with `content-visibility: auto`.
