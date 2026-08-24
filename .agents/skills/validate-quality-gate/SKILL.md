---
name: validate-quality-gate
description: Run the project-wide automated quality gate validation suite to verify HTML5 semantic structure, Schema.org JSON-LD, CSS design tokens, internal links, static assets, secret leaks, and script compilation.
---

# Quality Gate Validation Skill

## Overview
Executes the comprehensive automated quality gate suite for the Vokalis project.

## When to Run
- Before opening any Pull Request
- After modifying HTML landmarks, Schema.org metadata, or CSS tokens
- During Stage 5 (Quality Gate) of the 6-stage development lifecycle

## Execution Instructions
Run the validation script using Python 3:
```bash
python3 scripts/validate.py
```

## Validation Checks
1. **Secret Scanning:** Ensures zero AWS keys, GitHub tokens, or private keys in the repository.
2. **HTML5 Semantic & a11y:** Verifies single `<h1>`, `<header>`, `<footer>`, `<main id="main-content">`, and skip-to-content link.
3. **Schema.org Structured Data:** Validates JSON-LD `@graph` containing `MedicalBusiness` / `MedicalClinic` and `FAQPage`.
4. **Anchor & Link Integrity:** Validates that all internal anchor targets (`#id`) and referenced HTML pages exist.
5. **CSS Design Tokens:** Validates `:root` variables, `content-visibility`, and `@media (prefers-reduced-motion: reduce)`.
6. **Static & PWA Assets:** Ensures `manifest.json`, `sw.js`, `sitemap.xml`, and `favicon.svg` exist and are valid.
7. **Script Compilation:** Compiles Python deployment and PR automation scripts.
