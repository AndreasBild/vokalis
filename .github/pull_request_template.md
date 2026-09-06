## 📌 Pull Request Overview

<!-- Provide a concise description of what was changed, added, or fixed. -->

### 🎯 Type of Change
- [ ] 🚀 New Feature / Interactive Section (`feature/*`)
- [ ] 🎨 UI/UX & Styling Improvement
- [ ] ♿ Accessibility (a11y) Enhancement
- [ ] 📱 Responsive Design / Mobile Fix
- [ ] 🔍 SEO / Schema.org Update
- [ ] ⚖️ Legal / Compliance (DSGVO / Impressum)
- [ ] 🧹 Refactoring / Repository Governance (`chore/*`)
- [ ] ⚡ Performance & Caching Optimization (`perf/*`)

---

## 🔒 6-Stage Quality Gate Invariants

### 1. Analysis & Design Alignment
- [ ] Semantic HTML5 landmark structure maintained (`<header>`, `<nav>`, `<main id="main-content">`, `<footer>`).
- [ ] Single unique `<h1>` landmark per page with strict sequential heading hierarchy (no skipped levels).
- [ ] Unique HTML `id` attributes across every document (zero duplicate IDs).
- [ ] Accessible form bindings (`<label for="...">` or `aria-label`/`aria-labelledby`).
- [ ] CSS design tokens (`var(--...)`) used exclusively; zero raw hardcoded hex colors in components.

### 2. Branch Isolation, Model Selection & Token Efficiency
- [ ] Changes originated from a dedicated topic branch (`feature/*`, `fix/*`, `chore/*`, `perf/*`). Base branch is `main`.
- [ ] Commits follow Conventional Commits formatting with surgical, token-efficient diffs.
- [ ] Appropriate model tier utilized (Gemini 3.8 Flash default for web tasks, Pro/Thinking reserved for deep architecture).

### 3. Healthcare Domain & Legal Compliance (DSGVO / TMG)
- [ ] Zero remote fonts / zero remote CDNs (system font stack or local self-hosted assets).
- [ ] Zero unauthorized third-party trackers or cookies without consent.
- [ ] Permanent footer navigation to `impressum.html` (§ 5 TMG) and `datenschutz.html` (DSGVO).
- [ ] Schema.org JSON-LD structured data (`MedicalBusiness`, `MedicalClinic`, `FAQPage`) valid.

### 4. Accessibility (WCAG 2.1 Level AA/AAA)
- [ ] Focusable Skip-to-Content link present.
- [ ] Color contrast $\ge 4.5:1$ (normal text) and $\ge 3:1$ (large UI).
- [ ] Complete keyboard operability (`Tab`, `Enter`, `Space`, `Escape`) without keyboard traps.
- [ ] Dynamic output containers sanitized via `escapeHtml()` and announced via `aria-live`.

### 5. Performance & Asset Hygiene
- [ ] Explicit dimensions/viewBox on all images & SVGs (CLS = 0).
- [ ] `content-visibility: auto` applied on heavy below-the-fold sections.
- [ ] Pre-compression verified via Brotli Quality 11 (`scripts/deploy.py`).

### 6. Automated Quality Gate Pass
- [ ] Local quality gate validation suite passed (`python3 scripts/validate.py`).
- [ ] Zero credential or secret leaks detected.

---

## 📸 Screenshots / Visual Verification (Optional)
<!-- Add before/after screenshots or UI recordings if applicable -->
