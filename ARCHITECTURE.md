# Architecture & Technical Design – Vokalis Logopädie

## 1. Executive Summary
**Vokalis** (`vokalis.de`) is a high-performance, accessible (WCAG 2.1 AA/AAA), and privacy-first (100% DSGVO compliant) web presence for a specialized speech therapy clinic (Praxis für Logopädie & Sprachtherapie). It provides structured patient guidance, interactive therapy filtering, an intelligent 4-step appointment/consultation assistant, comprehensive local SEO structured data, and an automated AWS S3/CloudFront deployment pipeline with maximum Brotli pre-compression.

---

## 2. Technical Architecture & Invariants

```
┌────────────────────────────────────────────────────────────────────────┐
│                              Vokalis Web Stack                         │
│                                                                        │
│   ┌─────────────────────┐   ┌───────────────────┐   ┌──────────────┐   │
│   │   HTML5 Semantic    │   │  CSS3 Custom Prop │   │  Vanilla JS  │   │
│   │ (Landmarks, Schema) │   │ (Design Tokens)   │   │ (ES6+, XSS)  │   │
│   └──────────┬──────────┘   └─────────┬─────────┘   └───────┬──────┘   │
│              │                        │                     │          │
│              └────────────────────────┼─────────────────────┘          │
│                                       ▼                                │
│                     ┌───────────────────────────────────┐              │
│                     │  scripts/deploy.py (Brotli Q11)   │              │
│                     └─────────────────┬─────────────────┘              │
│                                       │                                │
│                                       ▼                                │
│                     ┌───────────────────────────────────┐              │
│                     │ AWS S3 (s3://vokalis.de)          │              │
│                     │ (Content-Encoding: br)            │              │
│                     └─────────────────┬─────────────────┘              │
│                                       │ Invalidation (/*)              │
│                                       ▼                                │
│                     ┌───────────────────────────────────┐              │
│                     │ CloudFront CDN (E3QGOGTX8QE7DE)   │              │
│                     └───────────────────────────────────┘              │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Design System & CSS Custom Properties

The styling architecture in [`css/style.css`](file:///Users/andreasbild/IdeaProjects/vokalis/css/style.css) is organized around systematic tokens:

### 3.1 Color Palette
* **Primary Brand (Teal):** `--primary: #0f766e`, `--primary-light: #14b8a6`, `--primary-lighter: #2dd4bf`, `--primary-dark: #115e59`, `--primary-darkest: #134e4a`, `--primary-subtle: #f0fdfa`
* **Secondary (Slate & Navy):** `--secondary: #1e293b`, `--secondary-light: #334155`, `--secondary-muted: #64748b`
* **Energy & Warmth Accent (Amber / Coral):** `--accent: #f97316`, `--accent-light: #fb923c`, `--accent-dark: #ea580c`, `--accent-subtle: #fff7ed`
* **Feedback:** `--success: #16a34a`, `--success-subtle: #f0fdf4`, `--info: #0284c7`, `--info-subtle: #f0f9ff`
* **Backgrounds:** `--bg-page: #ffffff`, `--bg-subtle: #f8fafc`, `--bg-card: #ffffff`, `--bg-glass: rgba(255, 255, 255, 0.88)`

### 3.2 Typography & Font Rendering
* **Local System Font Stack:** `'Plus Jakarta Sans', system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif`
* **DSGVO Guarantee:** 0 remote font calls (no connections to Google Fonts servers).
* **Fluid Type Scaling:** `clamp()` scales for all heading levels.

### 3.3 Core Web Vitals & Performance Rules
* **`content-visibility: auto; contain-intrinsic-size: 1px 700px;`** applied to offscreen sections (`#therapien`, `#ablauf`, `#praxis`, `#assistent`, `#faq`, `#kontakt`) to minimize initial main-thread blocking time.
* **Speculation Rules API:** Instant pre-rendering of legal pages (`impressum.html`, `datenschutz.html`).
* **Passive Event Listeners:** All scroll and touch handlers use `{ passive: true }` and `requestAnimationFrame` throttling.
* **Zero Layout Shift (CLS = 0):** Explicit dimensions on all icons, SVGs, and containers.

---

## 4. Component Hierarchy & User Journeys

```
index.html
├── Skip to Content Link (<a href="#main-content" class="skip-link">)
├── Sticky Header & Glassmorphism Navigation
│   ├── Vector Brand Logo (assets/icons/favicon.svg)
│   ├── Desktop Nav Links (Therapiefelder, Ablauf, Über Vokalis, Bedarfs-Check, FAQ, Kontakt)
│   ├── Quick CTA ("Termin anfragen")
│   └── Mobile Hamburger & Off-Canvas Drawer (Focus Trap & ARIA Expanded)
├── Main Landmark (<main id="main-content">)
│   ├── Hero Section (#hero)
│   │   ├── Badge, High-Impact Headline & Lead Text
│   │   ├── Dual CTAs (Erstberatung, Leistungen)
│   │   ├── Trust Feature Pills (Alle Kassen, Hausbesuche, Barrierefrei, Zertifiziert)
│   │   └── Floating Showcase Card
│   ├── Interactive Therapy Specialties (#therapien)
│   │   ├── Category Filter Tabs (Alle, Kinder, Stimme, Neurologie, Redefluss)
│   │   └── 6 Detail Cards (SES, MFT, Dysphonie, Aphasie, Dysphagie, Stottern)
│   ├── 4-Step Treatment Roadmap (#ablauf)
│   │   ├── Steps: Verordnung ➔ Termin ➔ Diagnostik ➔ Therapie
│   │   └── Prescription Notice Banner (28-Tage-Regel)
│   ├── Practice & Philosophy (#praxis)
│   │   ├── Practice Values (Empathie, Evidenz, Hausbesuche, Interdisziplinär)
│   │   └── Facility Highlights Box (Helle Räume, Diagnostik, Barrierefreiheit)
│   ├── Interactive Consultation & Inquiry Assistant (#assistent)
│   │   ├── Step 1: Patient Selection (Kind, Jugendlicher, Erwachsener, Neurologie)
│   │   ├── Step 2: Symptom Area (Aussprache, Wortschatz, Stimme, Schlucken, Redefluss)
│   │   ├── Step 3: Prescription Status (Rezept liegt vor, bestellt, Privat, Unklar)
│   │   └── Step 4: Summary (Sanitized) & Contact Dispatch Form
│   ├── FAQ Accordion (#faq)
│   │   └── Expandable Q&A (Kostenübernahme, Gültigkeit, Dauer, Hausbesuche, Absagen)
│   └── Contact & Location (#kontakt)
│       ├── Direct Info Cards (Telefon, E-Mail, Adresse, Behandlungszeiten)
│       └── Location & Public Transit Card + Google Maps Direct Route Link
├── Footer
│   ├── Brand & Philosophy Overview
│   ├── Specialty & Navigation Links
│   ├── Emergency Notice (116 117 / 112)
│   └── Legal Links (Impressum, Datenschutz, Barrierefreiheit)
└── Floating Mobile Action Bar
    ├── Call Button (tel:+49...)
    └── Appointment Inquiry Button (#assistent)
```

---

## 5. Security Architecture & Data Protection

1. **XSS Sanitization:** `js/main.js` processes all dynamic strings through `escapeHtml()` before rendering to DOM.
2. **HTTP Equivalent Security Meta Tags:**
   - `Content-Security-Policy: default-src 'self'; script-src 'self' 'unsafe-inline'; style-src 'self' 'unsafe-inline'; img-src 'self' data: https:; font-src 'self'; connect-src 'self'; frame-ancestors 'self';`
   - `X-Content-Type-Options: nosniff`
   - `Referrer-Policy: strict-origin-when-cross-origin`
3. **Secret Isolation:**
   - Credentials reside in `.env` (git-ignored).
   - Automated secret-scanning step in CI workflow ([`.github/workflows/ci.yml`](file:///Users/andreasbild/IdeaProjects/vokalis/.github/workflows/ci.yml)).

---

## 6. AWS S3 & CloudFront Deployment Pipeline

### 6.1 Automation Script ([`scripts/deploy.py`](file:///Users/andreasbild/IdeaProjects/vokalis/scripts/deploy.py))
* **Brotli Quality 11:** Encodes text files to `.br` in-memory and uploads to S3 with `Content-Encoding: br`.
* **Payload Reduction:** Consistently achieves **> 80% compression** (121 KB -> 23.8 KB).
* **MIME Types & Cache Headers:** Configures appropriate MIME types and immutable caching headers for static assets.
* **CloudFront Invalidation:** Automatically creates an invalidation batch (`/*`) for distribution `E3QGOGTX8QE7DE`.

### 6.2 Execution
```bash
# Standard deployment (uses .env or environment variables):
.venv/bin/python scripts/deploy.py

# With custom parameters:
.venv/bin/python scripts/deploy.py --bucket vokalis.de --distribution-id E3QGOGTX8QE7DE
```

---

## 7. SEO, PWA & Discovery

* **Structured Data:** Embedded Schema.org `MedicalBusiness` / `MedicalClinic` JSON-LD.
* **Sitemap & Robots:** Validated [`sitemap.xml`](file:///Users/andreasbild/IdeaProjects/vokalis/sitemap.xml) and [`robots.txt`](file:///Users/andreasbild/IdeaProjects/vokalis/robots.txt).
* **PWA Support:** Validated [`manifest.json`](file:///Users/andreasbild/IdeaProjects/vokalis/manifest.json) and scalable SVG favicon ([`assets/icons/favicon.svg`](file:///Users/andreasbild/IdeaProjects/vokalis/assets/icons/favicon.svg)).
