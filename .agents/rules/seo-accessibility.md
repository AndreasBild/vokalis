# SEO, Schema.org, Accessibility & Security Invariants

1. **Accessibility (WCAG 2.1 Level AA/AAA):**
   - Provide a prominent Skip-to-Content link (`<a href="#main-content" class="skip-link">`) at the top of every page.
   - Maintain minimum color contrast of 4.5:1 for standard text and 3:1 for large UI elements.
   - Full keyboard accessibility (`Tab`, `Enter`, `Space`, `Escape` for dismissal).
   - Use `aria-live="polite"` on interactive dynamic output containers.

2. **Schema.org Structured Data & SEO:**
   - Maintain valid Schema.org JSON-LD metadata for `MedicalBusiness` / `MedicalClinic` with `SpeechPathology` specialty.
   - Keep `sitemap.xml` and `robots.txt` in sync with all live URLs.
   - Include Open Graph and Twitter Card metadata for rich social sharing.

3. **Privacy & Legal Compliance (Germany / DSGVO / TMG):**
   - Permanent footer access to `impressum.html` (§ 5 TMG) and `datenschutz.html` (DSGVO).
   - No unauthorized third-party trackers or remote analytics without consent.
   - Contact and consultation forms must include explicit privacy consent checkboxes.

4. **Security & XSS Prevention:**
   - Always sanitize dynamic DOM inputs using `escapeHtml()`.
   - Maintain HTTP equivalent security headers (CSP, nosniff, strict-origin-when-cross-origin).
   - Ensure all external links include `rel="noopener noreferrer"`.
   - Never commit API keys or AWS credentials (enforce via gitignore and CI secret scan).
