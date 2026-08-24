# Domain Integrity & Healthcare Schema Guidelines

## 1. Healthcare & Speech Therapy Domain Model
* **Practice Specialty:** Speech-Language Pathology / Logopädie (Sprach-, Sprech-, Stimm- und Schlucktherapie).
* **Target Audiences:** Children (pädiatrische Sprachtherapie), Adolescents, and Adults (neurologische Sprachstörungen, Stimmtherapie, Schlucktherapie).
* **Clinical Vocabulary:** Clear distinction between diagnostic assessment (Diagnostik), therapy sessions (Therapie), prescription requirements (Heilmittelverordnung / Muster 13), and cost reimbursement (Gesetzliche / Private Krankenkassen).

## 2. Schema.org JSON-LD Structured Data
* Root document (`index.html`) must declare valid JSON-LD graph metadata:
  - `@type: "MedicalBusiness"` / `"MedicalClinic"`
  - `medicalSpecialty: "https://schema.org/SpeechPathology"`
  - `openingHoursSpecification`, `address`, `telephone`, `geo` coordinates
  - `@type: "FAQPage"` for frequently asked patient & billing questions
* Keep Structured Data synchronized with visible text content on the landing page.
