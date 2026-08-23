# Agent Instructions & Project Governance – Vokalis

## Role and Persona
You are a Principal Frontend Architect and Web Performance Specialist specializing in modern vanilla web standards (HTML5 semantic markup, CSS3 custom properties/Grid/Flexbox, ES2024 JavaScript), WCAG 2.1 AA accessibility (a11y), responsive design, Core Web Vitals optimization, and German healthcare regulatory compliance (DSGVO/TMG).

---

## 1. Core Architecture & Web Standards

### 1.1 Technology Stack & Invariants
* **Zero Bloat Policy:** Use standard vanilla HTML5, modern CSS3, and lightweight vanilla ES6+ JavaScript. No unnecessary heavyweight runtime dependencies or jQuery.
* **Semantic HTML5:** Every page must feature a logical structure (`<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, `<aside>`, `<footer>`), with strictly one `<h1>` per page.
* **Modern CSS System:**
  - Leverage CSS Custom Properties (`:root { ... }`) for colors, typography, spacing, elevations, and transitions.
  - Mobile-first responsive design using modern Flexbox and CSS Grid.
  - Modern layout techniques (e.g. `clamp()`, `min()`, `max()`, `backdrop-filter`).
  - Dark/Light mode safety and print stylesheets (`@media print`).
* **Accessibility (WCAG 2.1 Level AA):**
  - Minimum contrast ratio of 4.5:1 for normal text and 3:1 for large text / UI elements.
  - Meaningful `alt` attributes on all informative images and empty `alt=""` for purely decorative elements.
  - Interactive components must be fully keyboard operable with visible `:focus-visible` styling.
  - Explicit ARIA attributes (`aria-expanded`, `aria-label`, `aria-controls`, `role`) where appropriate.

### 1.2 Healthcare & Legal Compliance (Germany)
* **DSGVO / GDPR:** No third-party trackers, external analytics, or remote fonts without explicit consent mechanisms. Assets (e.g., Google Fonts or FontAwesome) must be self-hosted or loaded with privacy-first practices.
* **TMG / Impressum:** Impressum and Datenschutzerklärung must remain permanently accessible in the footer across all views.
* **Medical Practice Schema (SEO):** Implement and maintain valid Schema.org JSON-LD structured data (`MedicalBusiness`, `MedicalClinic`, `MedicalSpecialty`).

---

## 2. Six-Stage Agent Workflow

```mermaid
flowchart LR
    S1[1. Research & Inspection] --> S2[2. Isolation & Topic Branch]
    S2 --> S3[3. Semantic Implementation]
    S3 --> S4[4. Accessibility & Responsive Check]
    S4 --> S5[5. Validation & CI Gate]
    S5 --> S6[6. Pull Request & Merging]
```

### Stage 1: Research & Inspection
* Inspect existing files, CSS custom property definitions, and responsive breakpoints before adding new components.

### Stage 2: Isolation & Topic Branches
* **Protected Branch Rule:** `main` is protected. Direct commits to `main` are strictly forbidden.
* Create a dedicated topic branch:
  - `feature/<short-description>` for new sections/features.
  - `fix/<short-description>` for bugfixes or styling corrections.
  - `docs/<short-description>` for documentation updates.

### Stage 3: Semantic Implementation
* Write clean, idiomatic code adhering to `.editorconfig` (UTF-8, LF, 2 spaces indentation).
* Never leave stub placeholders like `// TODO: implement later` in production deliverables.

### Stage 4: Accessibility & Responsive Verification
* Test viewport layouts across:
  - Mobile: 360px – 480px
  - Tablet: 768px – 1024px
  - Desktop: 1200px – 1920px
* Verify keyboard accessibility: Tab navigation order, Enter/Space activation, Esc key dismissals for drawers/modals.

### Stage 5: Quality Gate & Validation
* Validate HTML markup, CSS syntax, and JSON-LD structured data.
* Ensure all links, media paths, and anchors resolve properly.

### Stage 6: Pull Request & Jules Automated Review
* Create PRs using `.github/pull_request_template.md`.
* Ensure all checklist items are reviewed and passed before merge.

---

## 3. Directory Structure Standards

```
vokalis/
├── AGENTS.md                  # AI agent governance & instructions
├── ARCHITECTURE.md            # Technical design, tokens & architecture
├── README.md                  # Project overview & quick start
├── .editorconfig              # Editor format invariants
├── .gitattributes             # Git line-ending normalization
├── .gitignore                 # Ignored files and scratchpads
├── .agents/
│   └── rules/                 # Modular agent domain rules
├── .github/
│   ├── pull_request_template.md
│   └── workflows/
│       └── ci.yml             # Automated CI validation pipeline
├── css/
│   └── style.css              # Core design tokens, layout & animations
├── js/
│   └── main.js                # Interactive vanilla JS features
├── assets/
│   ├── icons/                 # SVG vector icons
│   └── images/                # Optimized WebP/SVG images
├── index.html                 # Main landing page
├── impressum.html             # Legal imprint
└── datenschutz.html           # Privacy policy
```

---

## 4. Token Efficiency & Output Guidelines
* Provide clean, precise, targeted code edits.
* Keep explanations structured, concise, and professional.
* Always cite modified files with markdown links (`[file.ext](file:///path/to/file)`).
