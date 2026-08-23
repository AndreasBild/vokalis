# Vokalis – Praxis für Logopädie & Sprachtherapie

Offizielles Repository für die moderne, barrierefreie und performante Webpräsenz der **Praxis für Logopädie Vokalis** (`vokalis.de`).

---

## 🌟 Highlights & Features

* **Modernes & Vertrauensvolles UI/UX:**
  - Ruhiges, medizinisches Farbsystem (Tiefsee-Teal, Mint-Nuancen, warme Bernstein-/Korall-Akzente).
  - Glassmorphism-Header mit dynamischem Blur.
  - Dynamischer Kategorie-Filter für Therapiefelder (Kindersprache, Stimmtherapie, Neurologie, Redefluss/Stottern).
  - Interaktiver 4-Schritte-Bedarfs- und Terminanfrage-Assistent mit clientseitiger Validierung und XSS-Sanitization.
  - Barrierefreie FAQ-Akkordeons und Notfall-Hinweise.
* **100% DSGVO- & TMG-Konformität:**
  - Reiner, hochoptimierter lokaler System-Font-Stack (keine Verbindungen zu externen Google-Servern).
  - Null externe Tracker oder Drittanbieter-Skripte.
  - Rechtssicheres Impressum und Datenschutzerklärung für Heilberufe.
* **Core Web Vitals & Performance (100/100 Lighthouse Ready):**
  - Reines Semantic HTML5, CSS3 Custom Properties und Vanilla ES6+ JavaScript (Zero Bloat).
  - `content-visibility: auto` für sofortiges initiales Rendering.
  - Speculation Rules API für 0ms Sofort-Navigation zu Unterseiten.
  - Vollständige Unterstützung von `@media (prefers-reduced-motion: reduce)`.
* **SEO, PWA & Discovery:**
  - Validierte `sitemap.xml` und `robots.txt`.
  - PWA Web App Manifest (`manifest.json`) und gestochen scharfes SVG-Favicon (`assets/icons/favicon.svg`).
  - Schema.org JSON-LD structured data (`MedicalBusiness`, `MedicalClinic`, `SpeechPathology`).
* **Automatisierte AWS S3 & CloudFront Deployment Pipeline:**
  - Pre-Compression aller Web-Dateien mit **Brotli Quality 11** (über 80% Datenreduktion).
  - Synchronisation nach `s3://vokalis.de` mit `Content-Encoding: br` und `Cache-Control`-Headern.
  - Automatische CloudFront-Cache-Invalidierung (`/*`).

---

## 📁 Projektstruktur

```
vokalis/
├── AGENTS.md                  # AI Agent Governance & Invarianten
├── ARCHITECTURE.md            # Technische Architektur & System Design
├── README.md                  # Projektübersicht & Schnellstart
├── requirements.txt           # Python-Abhängigkeiten (Dependabot getrackt)
├── manifest.json              # PWA Web App Manifest
├── sitemap.xml                # SEO XML Sitemap
├── robots.txt                 # Suchmaschinen-Crawler-Steuerung
├── .editorconfig              # Editor-Formatierung (UTF-8, LF, 2 Spaces)
├── .gitattributes             # Line-Ending & Binary Normalisierung
├── .gitignore                 # Ignorierte Dateien (OS, IDE, .env, .venv, Scratchpads)
├── .agents/
│   └── rules/                 # Modulare Workspace-Regeln
├── .github/
│   ├── dependabot.yml         # Wöchentliche Dependabot-Updates
│   ├── pull_request_template.md # PR Review-Checkliste (A11y, Performance, SEO)
│   └── workflows/
│       └── ci.yml             # GitHub Actions CI & Secret-Scanning Pipeline
├── css/
│   └── style.css              # Modulares CSS Design System & Tokens
├── js/
│   └── main.js                # Interaktive Vanilla JS Logik (XSS-geschützt)
├── assets/
│   └── icons/                 # SVG Icons & Favicon
├── scripts/
│   └── deploy.py              # S3 Deploy + Brotli Q11 + CloudFront Invalidation
├── index.html                 # Haupt-Landingpage & Bedarfs-Assistent
├── impressum.html             # Impressum (§ 5 TMG)
└── datenschutz.html           # Datenschutzerklärung & Barrierefreiheit
```

---

## 🚀 Lokale Entwicklung & Vorschau

Da es sich um eine moderne statische Webapplikation handelt, ist kein Build-Schritt erforderlich:

```bash
# Mit Python Webserver:
python3 -m http.server 8000

# Oder mit Node / npx:
npx serve .
```
Öffnen Sie `http://localhost:8000` im Browser.

---

## ☁️ AWS S3 & CloudFront Deployment

### 1. Umgebungsvariablen (`.env`)
Erstellen Sie eine lokale `.env`-Datei im Projekt-Root (wird nicht in Git versioniert):
```env
S3_BUCKET_NAME=vokalis.de
AWS_REGION=eu-central-1
AWS_PROFILE=default
CLOUDFRONT_DISTRIBUTION_ID=E1234567890EXAMPLE
```

### 2. Deployment ausführen
```bash
# Virtuelle Umgebung aufsetzen (falls noch nicht vorhanden):
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt

# Deployment & Cache-Invalidierung starten:
.venv/bin/python scripts/deploy.py
```

---

## 🤖 AI Agent Governance & Richtlinien

Für die Zusammenarbeit mit AI-Agenten (Antigravity, Jules) gelten strenge Qualitätsstandards:
* **Workflow & Rollen:** siehe [`AGENTS.md`](file:///Users/andreasbild/IdeaProjects/vokalis/AGENTS.md).
* **Technische Spezifikation:** siehe [`ARCHITECTURE.md`](file:///Users/andreasbild/IdeaProjects/vokalis/ARCHITECTURE.md).
* **PR-Checkliste:** siehe [`.github/pull_request_template.md`](file:///Users/andreasbild/IdeaProjects/vokalis/.github/pull_request_template.md).
