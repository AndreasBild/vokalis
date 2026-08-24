# Performance, Core Web Vitals & Asset Guidelines

## 1. Core Web Vitals Optimization
* **Cumulative Layout Shift (CLS = 0):**
  - Explicit `width`, `height`, and `viewBox` attributes on all images and SVG vectors.
  - Reserve space for dynamic content to avoid unexpected reflows.
* **Largest Contentful Paint (LCP < 1.2s):**
  - Local typography stack with system fonts (0ms remote font delay).
  - High-priority preloading for critical above-the-fold hero assets.
* **Interaction to Next Paint (INP < 100ms):**
  - Event listeners with `{ passive: true }` for scroll/touch.
  - Throttle scroll handlers via `requestAnimationFrame`.

## 2. Rendering Optimization
* **`content-visibility`:**
  - Apply `content-visibility: auto; contain-intrinsic-size: 1px 700px;` on heavy below-the-fold sections to skip initial layout computation.
* **Speculation Rules API:**
  - Instant pre-rendering of internal pages (`datenschutz.html`, `impressum.html`) on user hover/intent.

## 3. Asset Compression & Caching
* **Brotli Quality 11 Pre-Compression:**
  - Static assets pre-compressed using `scripts/deploy.py`.
* **Cache-Control Headers:**
  - HTML documents: `public, max-age=3600, must-revalidate`
  - Static assets (`.css`, `.js`, `.svg`, `.webp`): `public, max-age=31536000, immutable`
