# Web Standards & Code Quality Invariants

1. **Vanilla Architecture First:**
   - Implement solutions using semantic HTML5, modern CSS3, and ES6+ vanilla JavaScript.
   - Avoid pulling heavy external libraries unless explicitly approved.

2. **CSS Design Tokens & Styling Rules:**
   - Always reference predefined CSS variables in `css/style.css` (`var(--primary)`, `var(--text-main)`, etc.) instead of hardcoding raw color hex values.
   - Keep styling modular, readable, and responsive.
   - Use CSS Grid and Flexbox for layouts; avoid float or fixed-pixel absolute positioning that breaks on varying viewports.

3. **Performance & Core Web Vitals:**
   - Maintain fast LCP (Largest Contentful Paint) and INP (Interaction to Next Paint).
   - Use SVG for vector icons and modern WebP/optimized formats for raster imagery.
   - Defer non-critical JavaScript and ensure scripts load asynchronously (`defer`).
