# Security, Privacy & German Regulatory Compliance (DSGVO / TMG)

## 1. Healthcare Privacy & GDPR / DSGVO Compliance
* **Zero Remote Tracking & No Remote CDNs:**
  - No external tracking scripts, Google Analytics, or third-party pixels without explicit user consent.
  - Zero Google Fonts or CDN requests. All typography must use local system fonts or self-hosted WOFF2 assets.
* **Legal Landmarks (TMG / DSGVO):**
  - Footer must link directly to `impressum.html` (§ 5 TMG) and `datenschutz.html` (Art. 13 DSGVO).
  - All contact and booking inquiry forms must feature explicit privacy consent checkboxes.

## 2. Security Invariants
* **XSS Prevention & DOM Sanitization:**
  - Dynamic user inputs or calculated consultation results injected into the DOM must be sanitized via `escapeHtml()`.
* **Security Headers & Meta Tags:**
  - Strict Content-Security-Policy (CSP) meta tag.
  - `X-Content-Type-Options: nosniff`.
  - `Referrer-Policy: strict-origin-when-cross-origin`.
* **Safe External Linking:**
  - Always include `rel="noopener noreferrer"` on external hyperlinks.
* **Zero Secret Leaks:**
  - Secrets strictly reside in `.env` (git-ignored).
  - Automated secret scan via `scripts/validate.py` runs before commit and in CI.
