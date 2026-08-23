# SEO, Schema.org & Accessibility Invariants

1. **Accessibility (WCAG 2.1 Level AA):**
   - Ensure semantic landmark roles (`header`, `nav`, `main`, `footer`, `section`, `article`).
   - Use meaningful text for link labels (avoid vague text like "hier klicken").
   - Maintain color contrast compliance (at least 4.5:1 for standard text).
   - Ensure all interactive elements have focused states (`:focus-visible`).
   - Modals and drawers must support keyboard dismissal via `Escape` key and close focus return.

2. **Schema.org Structured Data:**
   - Maintain accurate `MedicalBusiness` / `MedicalClinic` JSON-LD structured data.
   - Include opening hours, accepted insurances (GKV & PKV), location, telephone, and medical specialties (`SpeechPathology`).

3. **Privacy & Data Security (GDPR/DSGVO):**
   - No unauthorized third-party tracking scripts.
   - Contact forms must provide explicit data privacy consent checkboxes.
   - Ensure TLS/HTTPS ready asset paths.
