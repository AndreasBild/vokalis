# HTML Development Standards & Architecture

## 1. HTML5 Semantic Landmarks & Document Structure
* **Doctype & Root:** Every document must declare `<!DOCTYPE html>` and `<html lang="de">`.
* **Meta Standards:** Always include:
  - `<meta charset="utf-8">`
  - `<meta name="viewport" content="width=device-width, initial-scale=1.0">`
  - `<title>` with descriptive, page-specific text.
* **Landmarks Hierarchy:**
  - `<header>`: Contains site branding and top navigation.
  - `<nav role="navigation">`: Navigational link groups with descriptive `aria-label` when multiple navs exist.
  - `<main id="main-content">`: Single primary content landmark per page.
  - `<section aria-labelledby="section-heading-id">`: Group thematic content; always link to a section heading via `aria-labelledby`.
  - `<article>`: Self-contained content units (cards, posts, treatments).
  - `<aside>`: Complementary or secondary information.
  - `<footer>`: Closing landmark with copyright, address, and legal links (`impressum.html`, `datenschutz.html`).

## 2. Heading Structure & Document Outline
* **Single `<h1>` Invariant:** Exactly one `<h1>` element per page representing the document's primary subject.
* **Hierarchical Nesting:** Strict sequential progression (`<h1>` → `<h2>` → `<h3>`).
  - Never skip levels (e.g. `<h2>` directly jumping to `<h4>`).
  - Use CSS classes for visual typography scaling (`class="text-xl"`), never incorrect heading tags.

## 3. Accessible Forms & Interactive Controls
* **Input-Label Association:**
  - Every `<input>`, `<select>`, and `<textarea>` must have an explicit matching `<label for="id">` or `aria-label`/`aria-labelledby`.
* **Input Semantics & Autocomplete:**
  - Provide proper `type` (`text`, `email`, `tel`, `date`, `checkbox`, `radio`).
  - Provide `autocomplete` attributes (`name`, `email`, `tel`, `postal-code`, `address-level2`).
  - Provide `inputmode` (`numeric`, `tel`, `email`, `url`) to trigger optimal mobile keyboards.
* **Native Validation & Error Association:**
  - Use native HTML validation (`required`, `minlength`, `maxlength`, `pattern`).
  - Pair error or hint containers with inputs using `aria-describedby="field-hint-id"`.
  - Use `:user-valid` and `:user-invalid` CSS pseudo-classes for state indication.

## 4. Modern Interactive HTML Elements
* **Dialogs:** Use native `<dialog>` element with `::backdrop` styling and `.showModal()` / `.close()` methods.
* **Disclosure / Accordions:** Use native `<details>` and `<summary>` for FAQs and expandable content.
* **Popover API:** Use native `popover` and `popovertarget` attributes for tooltips, menus, and overlays without heavy JavaScript libraries.

## 5. Core Web Vitals & Media Optimization
* **Cumulative Layout Shift (CLS = 0):**
  - Always specify explicit `width` and `height` attributes on all `<img>` and `<svg>` elements.
  - Use CSS `aspect-ratio` for responsive image containers.
* **Largest Contentful Paint (LCP):**
  - Add `fetchpriority="high"` to above-the-fold hero images or key assets.
  - Add `loading="lazy"` and `decoding="async"` to all below-the-fold media.
* **Modern Formats:** Prefer `<picture>` with WebP/AVIF sources and SVG vector fallbacks.

## 6. Performance & Speculation Rules
* **Prerendering:** Implement the Speculation Rules API (`<script type="speculationrules">`) for instantaneous navigation to critical subpages (`impressum.html`, `datenschutz.html`).
* **Resource Optimization:** Keep inline critical CSS lean; defer non-critical scripts (`defer` attribute).

## 7. German Healthcare Privacy (DSGVO) & Security
* **Zero Remote Assets:** Never reference external CDNs or Google Fonts servers (`fonts.googleapis.com`). All fonts and icons must be local system fonts or self-hosted assets.
* **External Links:** All links with `target="_blank"` must include `rel="noopener noreferrer"`.
* **DOM Safety:** Never inject unescaped strings into the DOM. All dynamic insertions must use textContent or pass through `escapeHtml()`.
