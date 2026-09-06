---
name: html-development
description: Best practices, semantic patterns, accessibility checklists, and modern Web API recipes for top-notch HTML development.
---

# Modern HTML Development Skill

## Overview
Provides immediate access to production-grade HTML5 patterns, accessibility (WCAG 2.1 AA/AAA) standards, Core Web Vitals optimization, and German privacy compliance recipes for the Vokalis web application.

---

## 1. Landmark & Semantic Template
```html
<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Vokalis | Praxis für Logopädie</title>
</head>
<body>
  <!-- Accessible Skip Link -->
  <a href="#main-content" class="skip-link">Zum Hauptinhalt springen</a>

  <!-- Header Landmark -->
  <header class="header" role="banner">
    <nav class="nav" aria-label="Hauptnavigation">...</nav>
  </header>

  <!-- Main Content Landmark -->
  <main id="main-content" class="main">
    <section id="hero" aria-labelledby="hero-title">
      <h1 id="hero-title">Praxis für Logopädie</h1>
    </section>

    <section id="services" aria-labelledby="services-title">
      <h2 id="services-title">Unsere Therapiefelder</h2>
      <article class="service-card">
        <h3>Sprachtherapie</h3>
      </article>
    </section>
  </main>

  <!-- Footer Landmark -->
  <footer class="footer" role="contentinfo">
    <a href="impressum.html">Impressum</a>
    <a href="datenschutz.html">Datenschutz</a>
  </footer>
</body>
</html>
```

---

## 2. Accessible Form Recipe
```html
<form class="consultation-form" novalidate>
  <div class="form-group">
    <label for="patient-name">Vollständiger Name <span aria-hidden="true">*</span></label>
    <input 
      type="text" 
      id="patient-name" 
      name="name" 
      required 
      autocomplete="name" 
      aria-describedby="name-hint"
    >
    <span id="name-hint" class="field-hint">Vor- und Nachname</span>
  </div>

  <div class="form-group">
    <label for="patient-tel">Telefonnummer <span aria-hidden="true">*</span></label>
    <input 
      type="tel" 
      id="patient-tel" 
      name="tel" 
      required 
      inputmode="tel" 
      autocomplete="tel"
    >
  </div>
</form>
```

---

## 3. Native Interactive Elements

### Native Modal Dialog
```html
<dialog id="booking-modal" class="modal-dialog" aria-labelledby="modal-title">
  <div class="modal-content">
    <h2 id="modal-title">Termin vereinbaren</h2>
    <p>Wählen Sie Ihren Wunschtermin.</p>
    <button type="button" class="btn btn-close" onclick="this.closest('dialog').close()">Schließen</button>
  </div>
</dialog>
```

### Native Accordion / FAQ
```html
<details class="faq-item">
  <summary class="faq-summary">
    <span>Benötige ich eine ärztliche Verordnung?</span>
  </summary>
  <div class="faq-content">
    <p>Ja, für eine logopädische Behandlung ist ein Rezept Ihres Arztes erforderlich.</p>
  </div>
</details>
```

---

## 4. Speculation Rules for Instant Prerendering
```html
<script type="speculationrules">
{
  "prerender": [
    {
      "source": "list",
      "urls": ["impressum.html", "datenschutz.html"]
    }
  ]
}
</script>
```

---

## 5. Verification Checklist
- [ ] Exactly one `<h1>` per page.
- [ ] Sequential heading progression (`h1` → `h2` → `h3`, no skipped levels).
- [ ] Prominent skip link `<a href="#main-content" class="skip-link">`.
- [ ] Unique `id` attributes across the entire document.
- [ ] Explicit `<label for="...">` or `aria-label` on all inputs.
- [ ] All `<img>` elements have `alt` attributes.
- [ ] Decorative icons have `aria-hidden="true"`.
- [ ] Zero remote Google Fonts or external CDN script requests.
