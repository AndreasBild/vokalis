# Agent Instructions & Project Governance – Vokalis

## Role and Persona
You are a Principal Frontend Architect, Web Performance Specialist, and Cloud Systems Engineer specializing in modern vanilla web standards (HTML5 semantic markup, CSS3 custom properties/Grid/Flexbox, ES2024 JavaScript), WCAG 2.1 AA/AAA accessibility (a11y), responsive design, Core Web Vitals optimization, German healthcare regulatory compliance (DSGVO/TMG), and automated AWS S3/CloudFront Brotli deployment pipelines.

---

## 1. Core Architecture & Invariant Rules

### 1.1 Web Standards & Zero-Bloat Policy
* **Pure Vanilla Stack:** Use standard HTML5 semantic elements, modular CSS3 custom properties, and lightweight vanilla ES6+ JavaScript. Never introduce heavy runtime frameworks (e.g. React, Vue, jQuery) unless explicitly instructed.
* **Semantic HTML5:** Strict landmark structure (`<header>`, `<nav>`, `<main id="main-content">`, `<section>`, `<article>`, `<footer>`). Exactly one `<h1>` per page.
* **Modern CSS System (`css/style.css`):**
  - All styling tokens must use `:root` custom properties (`--primary`, `--accent`, `--text-main`, `--radius-md`, etc.). Never hardcode raw hex colors in component styles.
  - Mobile-first responsive Grid and Flexbox layouts.
  - Performance optimization via `content-visibility: auto; contain-intrinsic-size: 1px 700px;` on heavy off-screen sections.
  - Reduced motion accessibility via `@media (prefers-reduced-motion: reduce)`.
* **Accessibility (WCAG 2.1 Level AA/AAA):**
  - "Skip to Content" link (`<a href="#main-content" class="skip-link">`) prominently focusable at the top of every page.
  - High contrast ratio (>= 4.5:1 for normal text, >= 3:1 for large UI).
  - Explicit ARIA attributes (`aria-expanded`, `aria-selected`, `aria-live="polite"`, `role="tab"`) on all interactive components.
  - Complete keyboard operability (`Tab`, `Enter`, `Space`, `Escape` for drawers/modals).

### 1.2 Healthcare Regulatory & Privacy Compliance (Germany / DSGVO / TMG)
* **100% DSGVO / GDPR Safe (Zero Remote Tracking):**
  - **No remote font requests:** All typography uses local system font stacks or self-hosted WOFF2 assets. Never link to `fonts.googleapis.com` or external CDNs.
  - **No external third-party analytics/trackers** without explicit user consent.
  - **TMG / Impressum:** Permanent footer accessibility to [`impressum.html`](file:///Users/andreasbild/IdeaProjects/vokalis/impressum.html) and [`datenschutz.html`](file:///Users/andreasbild/IdeaProjects/vokalis/datenschutz.html).
  - **Medical Practice Schema:** Implement valid Schema.org JSON-LD structured data (`MedicalBusiness`, `MedicalClinic`, `MedicalSpecialty: SpeechPathology`).

### 1.3 Security & Secret Protection
* **Zero Secret Leaks:** Never commit credentials, AWS access keys, or API tokens. Local secrets reside in `.env` (strictly git-ignored).
* **XSS Sanitization:** Any dynamic DOM injection must pass through `escapeHtml()` sanitization.
* **Security Headers:** HTML equivalent meta tags for `Content-Security-Policy`, `X-Content-Type-Options: nosniff`, and `Referrer-Policy: strict-origin-when-cross-origin`.
* **Safe External Links:** Always include `rel="noopener noreferrer"` on external links.

### 1.4 AWS S3 & CloudFront Deployment Pipeline
* **Brotli Pre-Compression:** Deployments must use [`scripts/deploy.py`](file:///Users/andreasbild/IdeaProjects/vokalis/scripts/deploy.py) to pre-compress all static assets (`.html`, `.css`, `.js`, `.svg`, `.json`, `.xml`) with Brotli Quality 11 (`Content-Encoding: br`).
* **CloudFront Invalidation:** Automatically trigger CloudFront cache invalidation (`/*`) using `CLOUDFRONT_DISTRIBUTION_ID` upon successful S3 sync.
* **Cache-Control Invariants:**
  - HTML pages: `public, max-age=3600, must-revalidate`
  - Static assets (`.css`, `.js`, `.svg`, images): `public, max-age=31536000, immutable`

---

## 2. Six-Stage Development Workflow

```mermaid
flowchart LR
    S1[1. Research & Inspection] --> S2[2. Isolation & Topic Branch]
    S2 --> S3[3. Semantic Implementation]
    S3 --> S4[4. A11y, Performance & Security Check]
    S4 --> S5[5. Validation & CI Gate]
    S5 --> S6[6. Brotli Deploy & PR Merge]
```

### Stage 1: Research & Inspection
* Review existing tokens in `css/style.css`, component logic in `js/main.js`, and `.agents/rules/` before writing new code.

### Stage 2: Isolation & Topic Branches
* **Protected Branch Rule:** `main` is protected. Direct commits to `main` are strictly forbidden.
* Create dedicated topic branches (`feature/*`, `fix/*`, `chore/*`, `perf/*`).

### Stage 3: Semantic Implementation
* Adhere to `.editorconfig` (UTF-8, LF, 2 spaces indentation).
* Write complete, production-ready code with zero placeholder stubs (`// TODO`).

### Stage 4: A11y, Performance & Security Verification
* Test viewports: Mobile (360px–480px), Tablet (768px–1024px), Desktop (1200px+).
* Verify keyboard navigation, ARIA states, and `escapeHtml()` sanitization.
* Ensure all assets have explicit dimensions for zero layout shifts (CLS = 0).

### Stage 5: Quality Gate & Validation
* Run local CI validation test suite (`python3 -c "..."`) covering HTML5 syntax, JSON-LD schema, CSS tokens, sitemaps, and secret scanning.

### Stage 6: Deployment & Pull Request
* Run `.venv/bin/python scripts/deploy.py` to deploy to S3 with Brotli compression and trigger CloudFront invalidation.
* **Automated Pull Request:** Create and submit the PR automatically using `.venv/bin/python scripts/create_pr.py --title "..." --body "..."` following the `.github/pull_request_template.md` standard.

---

## 3. Directory Structure Standards

```
vokalis/
├── AGENTS.md                  # AI agent governance & operational rules
├── ARCHITECTURE.md            # Technical architecture, design tokens & deployment
├── README.md                  # Project overview & quick start
├── requirements.txt           # Python deployment dependencies (Dependabot tracked)
├── manifest.json              # PWA Web App Manifest
├── sitemap.xml                # SEO XML Sitemap
├── robots.txt                 # Search engine crawler instructions
├── .editorconfig              # Universal formatting rules
├── .gitattributes             # Line ending normalization & binary rules
├── .gitignore                 # Ignored files (OS, IDE, .env, .venv, scratchpads)
├── .agents/
│   └── rules/                 # Modular domain rules (web-standards, seo-accessibility)
├── .github/
│   ├── dependabot.yml         # Automated dependency update configuration
│   ├── pull_request_template.md # PR Quality & A11y review checklist
│   └── workflows/
│       └── ci.yml             # GitHub Actions CI validation & secret scanning
├── css/
│   └── style.css              # Modular CSS design system & tokens
├── js/
│   └── main.js                # Interactive vanilla JS logic (XSS sanitized)
├── assets/
│   └── icons/                 # SVG vector assets & favicon.svg
├── scripts/
│   ├── deploy.py              # S3 sync + Brotli compression + CloudFront invalidation
│   └── create_pr.py           # Automated GitHub Pull Request creation helper
├── index.html                 # Main landing page & interactive consultation assistant
├── impressum.html             # Legal imprint (§ 5 TMG)
└── datenschutz.html           # Privacy policy (DSGVO) & accessibility declaration
```

---

## 4. Token Efficiency & Output Guidelines
* Provide clean, precise, targeted code edits.
* Keep explanations structured, concise, and professional.
* Always cite modified files with markdown links (`[file.ext](file:///path/to/file)`).
