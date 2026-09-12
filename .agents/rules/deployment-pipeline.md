# AWS S3 & CloudFront Deployment Pipeline

## 1. Automated Deployment Invariants
* **Pre-Deployment Gate:** Run `python3 scripts/validate.py` before executing any deployment.
* **Brotli Quality 11 Pre-Compression:**
  - Pre-compress static assets (`.html`, `.css`, `.js`, `.svg`, `.json`, `.xml`) using Brotli quality 11 (`Content-Encoding: br`) via `scripts/deploy.py`.
* **CloudFront Edge Invalidation:**
  - Automatically invalidate edge cache paths (`/*`) using `CLOUDFRONT_DISTRIBUTION_ID` upon successful S3 synchronization.
* **Zero Secret Leakage:**
  - AWS credentials (`AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `AWS_REGION`) must strictly reside in `.env` (git-ignored) or CI environment variables. Never commit credentials.

## 2. HTTP Caching Headers
* **HTML Documents:**
  - `Cache-Control: public, max-age=3600, must-revalidate`
* **Static Assets (`.css`, `.js`, `.svg`, images, fonts):**
  - `Cache-Control: public, max-age=31536000, immutable`
