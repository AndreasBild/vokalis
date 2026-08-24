---
name: schema-verification
description: Verify Schema.org JSON-LD medical clinic and FAQ structured data contracts, XML sitemap sync, and HTML5 landmark accessibility.
---

# Domain & Schema Verification Skill

## Overview
Validates structured data schemas and search engine metadata for healthcare practice requirements.

## Key Verifications

### 1. Schema.org JSON-LD Verification
Verify that `index.html` contains valid `@context: "https://schema.org"` with `@type: MedicalBusiness` or `MedicalClinic`, `medicalSpecialty: SpeechPathology`, and `FAQPage`:
```bash
python3 -c "
import json, re
html = open('index.html', encoding='utf-8').read()
match = re.search(r'<script type=\"application/ld\+json\">(.*?)</script>', html, re.DOTALL)
assert match, 'Missing JSON-LD script tag'
data = json.loads(match.group(1))
assert data['@context'] == 'https://schema.org'
graph = data.get('@graph', [data])
types = [item.get('@type') for item in graph]
assert 'MedicalBusiness' in types or 'MedicalClinic' in types
assert 'FAQPage' in types
print('✅ Schema.org JSON-LD valid.')
"
```

### 2. Sitemap & Robots Verification
Verify that `sitemap.xml` references only existing, accessible production URLs and `robots.txt` points to `sitemap.xml`.

### 3. German Regulatory (DSGVO / TMG) Verification
Verify presence of `<a href="impressum.html">` and `<a href="datenschutz.html">` in the global footer.
