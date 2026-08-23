# Vokalis – Praxis für Logopädie & Sprachtherapie

Offizielles Repository für die moderne, barrierefreie und performante Webpräsenz der **Praxis für Logopädie Vokalis** (`vokalis.de`).

---

## 🌟 Features & Highlights

* **Modernes & Vertrauensvolles UI/UX:**
  - Ruhige, medizinische Farbgebung (Tiefsee-Teal, Mint-Nuancen und warme Korall-Akzente).
  - Glassmorphism Header mit dynamischem Blur.
  - Dynamischer Kategorie-Filter für Therapiefelder (Kindersprache, Stimmtherapie, Neurologie, Redefluss).
  - Interaktiver 4-Schritte-Bedarfs- und Terminanfrage-Assistent für Patienten.
  - Barrierefreie FAQ-Akkordeons.
* **Maximale Performance & Zero Bloat:**
  - Reines Semantic HTML5, CSS3 Custom Properties und Vanilla ES6+ JavaScript.
  - Keine schweren Frontend-Frameworks oder unnötigen externen Laufzeit-Abhängigkeiten.
* **Barrierefreiheit (a11y) & SEO:**
  - WCAG 2.1 Level AA Konformität (hohe Kontraste, Tastatur-Navigierbarkeit, ARIA-Attribute).
  - Vollständiges Schema.org JSON-LD structured data (`MedicalBusiness` / `MedicalClinic`).
* **Datenschutz & Rechtssicherheit:**
  - 100 % DSGVO- & TMG-konform.
  - Impressum & Datenschutzerklärung für Heilberufe.

---

## 📁 Projektstruktur

```
vokalis/
├── AGENTS.md                  # AI Agent Governance & Invarianten
├── ARCHITECTURE.md            # Technische Architektur & Design Tokens
├── README.md                  # Projektübersicht
├── .editorconfig              # Editor Invarianten (UTF-8, LF, 2 Spaces)
├── .gitattributes             # Line-Ending & Binary Normalisierung
├── .gitignore                 # Ignorierte Dateien (OS, IDE, Agent-Scratchpads)
├── .agents/
│   └── rules/                 # Modulare Agentenregeln (A11y, Web Standards)
├── .github/
│   ├── pull_request_template.md # PR Review-Checkliste
│   └── workflows/
│       └── ci.yml             # GitHub Actions CI Workflow
├── css/
│   └── style.css              # Modulares CSS Design System
├── js/
│   └── main.js                # Interaktive Vanilla JS Logik
├── index.html                 # Haupt-Landingpage
├── impressum.html             # Impressum (§ 5 TMG)
└── datenschutz.html           # Datenschutzerklärung & Barrierefreiheit
```

---

## 🚀 Lokale Entwicklung & Vorschau

Da es sich um eine moderne statische Webapplikation handelt, ist kein Build-Schritt erforderlich. 

Starten Sie einfach einen lokalen Webserver:
```bash
# Mit Python:
python3 -m http.server 8000

# Oder mit Node / npx:
npx serve .
```
Öffnen Sie anschließend `http://localhost:8000` im Browser.

---

## 🤖 AI Agent Governance

Dieses Repository nutzt standardisierte Governance-Regeln für AI-Agenten (z. B. Antigravity, Jules):
- Details zu Rollen, Workflows und Branch-Regeln: siehe [`AGENTS.md`](file:///Users/andreasbild/IdeaProjects/vokalis/AGENTS.md).
- Technische Spezifikationen und Design-Tokens: siehe [`ARCHITECTURE.md`](file:///Users/andreasbild/IdeaProjects/vokalis/ARCHITECTURE.md).
