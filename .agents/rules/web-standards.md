# Web Standards, Performance & Deployment Invariants

1. **Vanilla Architecture First:**
   - Implement all UI components with semantic HTML5, modern CSS3 custom properties, and lightweight ES6+ vanilla JavaScript.
   - Zero heavy external runtime frameworks (React, Vue, jQuery).

2. **CSS Design Tokens & Layout Rules:**
   - Always reference predefined CSS variables in `css/style.css` (`var(--primary)`, `var(--accent)`, `var(--text-main)`, etc.) instead of hardcoding raw hex values.
   - Use CSS Grid and Flexbox for responsive layouts.
   - Use `content-visibility: auto; contain-intrinsic-size: 1px 700px;` on offscreen sections.
   - Support `@media (prefers-reduced-motion: reduce)`.

3. **Core Web Vitals & Loading Performance:**
   - Zero layout shifts (CLS = 0) with explicit width/height/viewBox attributes.
   - Pure local system font stacks (0ms remote font network delay, 100% DSGVO compliant).
   - Use Speculation Rules API for instant subpage prerendering (`impressum.html`, `datenschutz.html`).
   - Passive event listeners (`{ passive: true }`) and RAF-throttled scroll handlers.

4. **Brotli & AWS S3/CloudFront Deployment:**
   - Pre-compress static assets using `scripts/deploy.py` with Brotli Quality 11 (`Content-Encoding: br`).
   - Set immutable cache headers for static assets and revalidation headers for HTML.
   - Automatically trigger CloudFront cache invalidation (`/*`) upon S3 synchronization.
