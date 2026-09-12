---
name: test-suite
description: Execute and interpret the Vokalis test and validation suite via python3 scripts/validate.py.
---

# Test Suite & Validation Runner Skill

## Overview
Runs the complete automated quality gate and validation suite for the Vokalis project using `python3 scripts/validate.py`.

## Execution Instructions
Run the validation script directly from the project root:
```bash
python3 scripts/validate.py
```

## Test Suite Checks
1. **Secret Leak Scanner:** Scans all repository files for committed AWS keys, GitHub tokens, and private keys.
2. **HTML5 Semantic & a11y:** Verifies single `<h1>`, landmark tags (`<header>`, `<nav>`, `<main id="main-content">`, `<footer>`), and skip link across all HTML documents (`index.html`, `impressum.html`, `datenschutz.html`).
3. **Schema.org JSON-LD:** Validates clinic structured data (`MedicalBusiness`, `MedicalClinic`, `MedicalSpecialty: SpeechPathology`) and `FAQPage`.
4. **Link & Anchor Integrity:** Validates internal page links and `#id` anchor targets to prevent dead links.
5. **CSS Design Tokens:** Validates `:root` variables, `content-visibility: auto; contain-intrinsic-size`, and prefers-reduced-motion queries.
6. **Static & PWA Assets:** Ensures presence of `manifest.json`, `sw.js`, `sitemap.xml`, and `favicon.svg`.
7. **Python Script Compilation:** Compiles `scripts/validate.py`, `scripts/deploy.py`, and `scripts/create_pr.py` without syntax errors.

## Failure Remediation
- **Secret leak detected:** Remove raw credential immediately; ensure secrets reside strictly in `.env`.
- **Heading / landmark error:** Ensure exactly one `<h1>` per page and `<main id="main-content">` is present.
- **Anchor error:** Check `#id` target against section IDs in the relevant HTML document.
- **CSS token error:** Replace any raw hex colors with corresponding `var(--token)` custom properties.
