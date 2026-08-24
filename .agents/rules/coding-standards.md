# Web Standards & Coding Guidelines

## 1. Zero-Bloat Vanilla Architecture
* **Pure Vanilla HTML5 / CSS3 / ES2024:**
  - Build UI components using standard Web APIs without heavy framework overhead (React, Vue, jQuery).
  - Use semantic landmarks: `<header>`, `<nav>`, `<main id="main-content">`, `<section>`, `<article>`, `<footer>`.
  - Maintain exactly one `<h1>` per HTML page.

## 2. CSS Architecture & Design Tokens (`css/style.css`)
* **Strict Token Usage:**
  - Use `:root` custom properties (`var(--primary)`, `var(--accent)`, `var(--text-main)`, `var(--radius-md)`).
  - Never hardcode raw hex values inside component styles.
* **Layouts:**
  - Mobile-first responsive Grid and Flexbox layouts.
  - Test breakpoints: Mobile (360–480px), Tablet (768–1024px), Desktop (1200px+).

## 3. Accessibility (WCAG 2.1 Level AA/AAA)
* Prominent skip link: `<a href="#main-content" class="skip-link">` as first body element.
* Contrast ratio: $\ge 4.5:1$ for normal text, $\ge 3:1$ for large UI elements.
* Complete keyboard accessibility (`Tab`, `Enter`, `Space`, `Escape`).
* Explicit ARIA attributes (`aria-expanded`, `aria-selected`, `aria-live="polite"`, `role="tab"`).
* Respect reduced motion preferences: `@media (prefers-reduced-motion: reduce)`.

## 4. Code Formatting
* UTF-8 encoding, LF line endings, 2 spaces indentation (configured in `.editorconfig`).
* Production-ready complete implementations; zero placeholder stubs (`// TODO`).
