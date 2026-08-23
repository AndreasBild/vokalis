# Architecture & Technical Design – Vokalis Logopädie

## 1. Executive Summary
**Vokalis** (`vokalis.de`) is a high-performance, accessible, and responsive web presence for a specialized speech therapy clinic (Praxis für Logopädie & Sprachtherapie). It provides comprehensive patient information for children, adults, voice professionals, and neurological patients, complete with a structured treatment roadmap, interactive inquiry assistant, and schema-rich local SEO.

---

## 2. Technical Architecture

### 2.1 Design System & CSS Custom Properties
The styling architecture in [`css/style.css`](file:///Users/andreasbild/IdeaProjects/vokalis/css/style.css) is organized systematically around modular tokens:

* **Color Palette:**
  - Primary Brand (Teal): `--primary: #0f766e`, `--primary-light: #14b8a6`, `--primary-dark: #115e59`, `--primary-subtle: #f0fdfa`
  - Secondary (Slate & Sage): `--secondary: #334155`, `--secondary-light: #64748b`
  - Energy & Accent (Coral / Amber): `--accent: #f97316`, `--accent-hover: #ea580c`, `--accent-subtle: #fff7ed`
  - Neutral Backgrounds: `--bg-main: #ffffff`, `--bg-alt: #f8fafc`, `--bg-card: #ffffff`
  - Text: `--text-main: #0f172a`, `--text-muted: #475569`, `--text-light: #94a3b8`
* **Typography:**
  - Base Font: `'Plus Jakarta Sans', system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif`
  - Heading Scales: Dynamic `clamp()` fluid type scaling for optimal readability on all screen sizes.
* **Layout & Elevational Shadows:**
  - Max container width: `1280px`
  - Elevation tokens: `--shadow-sm`, `--shadow-md`, `--shadow-lg`, `--shadow-xl`, `--shadow-glow`
  - Border Radii: `--radius-sm (6px)`, `--radius-md (12px)`, `--radius-lg (20px)`, `--radius-full (9999px)`

---

## 3. Component Hierarchy & Sections

```
index.html
├── Header & Sticky Navigation
│   ├── Brand Logo (SVG Vector)
│   ├── Navigation Links (Über uns, Schwerpunkte, Ablauf, FAQ, Kontakt)
│   ├── Action CTA Button ("Termin anfragen")
│   └── Mobile Hamburger Toggle
├── Hero Section
│   ├── Value Pitch & Primary Headlines
│   ├── Quick Feature Badges (Alle Kassen, Barrierefrei, Hausbesuche)
│   ├── Dual Action CTAs (Erstberatung, Leistungen)
│   └── Floating Trust Metrics Card
├── Specialties / Therapiefelder (Interactive Filter)
│   ├── Filter Navigation Tabs (Alle, Kinder, Erwachsene, Stimme, Neurologie)
│   └── Category Cards with Micro-Interactions & Detail Lists
├── Process & Roadmap (Ablauf & Verordnung)
│   ├── 4-Step Patient Guide (Arzttermin ➔ Kontakt ➔ Diagnostik ➔ Therapie)
│   └── Prescription Guidelines (Muster 13, 28-Tage-Frist)
├── Practice & Philosophy (Über die Praxis)
│   ├── Modern Equipment & Relaxed Ambiance
│   └── Core Values (Empathie, Wissenschaft, Individualität)
├── Interactive Appointment & Inquiry Assistant
│   ├── Step-based Questionnaire (Patient, Ziel, Rezeptstatus)
│   └── Contact & Message Dispatch
├── FAQ Accordion
│   └── Expandable Questions (Kosten, Zuzahlung, Dauer, Absagen)
├── Contact & Location Details
│   ├── Direct Contact (Phone, Email, Hours)
│   └── Accessible Location Card & Public Transport Directions
└── Footer & Legal Navigation
    ├── Practice Details & Emergency Notice
    └── Links (Impressum, Datenschutz, Barrierefreiheit)
```

---

## 4. Performance & Core Web Vitals Optimization

* **Zero Render-Blocking Overhead:** No large external JavaScript frameworks.
* **Font Optimization:** Modern font loading strategy with `font-display: swap` and local fallbacks.
* **Image Delivery:** Scalable SVG vector icons and lightweight WebP visual assets.
* **Preloading & Resource Hints:** Efficient `dns-prefetch` and `preconnect` for essential external fonts.

---

## 5. Schema.org JSON-LD Structured Data

The website implements rich Schema.org metadata for local healthcare businesses:
```json
{
  "@context": "https://schema.org",
  "@type": "MedicalBusiness",
  "name": "Vokalis – Praxis für Logopädie & Sprachtherapie",
  "url": "https://vokalis.de",
  "medicalSpecialty": "SpeechPathology",
  "currenciesAccepted": "EUR",
  "paymentAccepted": "Gesetzliche und private Krankenversicherung, Selbstzahler"
}
```

---

## 6. Maintenance & Deployment
* **Static Hosting Ready:** Can be hosted on any modern CDN / static web hosting (e.g. AWS S3 + CloudFront, Netlify, Vercel, GitHub Pages, or standard Nginx/Apache servers).
* **Continuous Integration:** Validated on every PR via `.github/workflows/ci.yml`.
