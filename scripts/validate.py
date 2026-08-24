#!/usr/bin/env python3
"""
Vokalis – Automated Quality Gate & CI Validation Suite
Validates HTML semantic markup, Schema.org JSON-LD, CSS design tokens,
internal links/anchors, asset integrity, script compilation, and scans for secret leaks.
"""

import json
import os
import re
import subprocess
import sys


def run_secret_scan() -> bool:
    print("🔒 [1/7] Scanning for credentials and secret leaks...")
    suspicious_patterns = [
        re.compile(r"AKIA[0-9A-Z]{16}"),
        re.compile(r"ghp_[0-9a-zA-Z]{36}"),
        re.compile(r"-----BEGIN (?:RSA )?PRIVATE KEY-----"),
        re.compile(r"(?:aws_secret_access_key|aws_access_key_id)\s*=\s*['\"][A-Za-z0-9/+=]{20,}['\"]", re.IGNORECASE),
    ]
    leaks = []
    for root, dirs, files in os.walk("."):
        dirs[:] = [d for d in dirs if d not in {".git", ".venv", "__pycache__", ".idea", ".junie"}]
        for file in files:
            if file.endswith((".png", ".webp", ".ico", ".woff2", ".svg.br", ".html.br", ".css.br", ".js.br")):
                continue
            if file in {".env", ".env.local"}:
                continue
            filepath = os.path.join(root, file)
            try:
                with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
                    for line_num, line in enumerate(f, 1):
                        for pat in suspicious_patterns:
                            if pat.search(line):
                                leaks.append((filepath, line_num))
            except Exception as e:
                print(f"⚠️ Warning reading {filepath}: {e}")

    if leaks:
        print(f"❌ Credentials / secrets detected: {leaks}", file=sys.stderr)
        return False
    print("   ✅ Zero secret leaks detected.")
    return True


def validate_html_files() -> bool:
    print("📄 [2/7] Validating HTML5 semantic structure & accessibility landmarks...")
    required_files = ["index.html", "impressum.html", "datenschutz.html"]
    for f in required_files:
        if not os.path.exists(f):
            print(f"❌ Missing required file: {f}", file=sys.stderr)
            return False
        with open(f, "r", encoding="utf-8") as file:
            content = file.read()
            assert "<!DOCTYPE html>" in content, f"Missing <!DOCTYPE html> in {f}"
            assert '<html lang="de">' in content, f"Missing <html lang=\"de\"> in {f}"
            assert '<meta name="viewport"' in content, f"Missing viewport meta in {f}"
            assert "skip-link" in content, f"Missing skip-to-content link in {f}"
            assert "<header" in content, f"Missing <header> landmark in {f}"
            assert "<footer" in content, f"Missing <footer> landmark in {f}"
            assert '<main id="main-content"' in content, f"Missing <main id=\"main-content\"> in {f}"
            
            # Exactly one h1 per page
            h1_count = len(re.findall(r"<h1\b", content, re.IGNORECASE))
            assert h1_count == 1, f"Expected exactly 1 <h1> in {f}, found {h1_count}"
        print(f"   ✅ {f} conforms to HTML5 semantic structure.")
    return True


def validate_schema_jsonld() -> bool:
    print("🏷️ [3/7] Validating Schema.org JSON-LD structured data...")
    if not os.path.exists("index.html"):
        print("❌ index.html not found", file=sys.stderr)
        return False
    
    with open("index.html", "r", encoding="utf-8") as f:
        html = f.read()

    match = re.search(r'<script type="application/ld\+json">(.*?)</script>', html, re.DOTALL)
    if not match:
        print("❌ Missing Schema.org JSON-LD block in index.html", file=sys.stderr)
        return False

    try:
        data = json.loads(match.group(1))
    except json.JSONDecodeError as e:
        print(f"❌ Invalid JSON-LD syntax: {e}", file=sys.stderr)
        return False

    assert data.get("@context") == "https://schema.org", "Schema.org @context mismatch"
    graph = data.get("@graph", [data])
    types = [item.get("@type") for item in graph if isinstance(item, dict)]
    assert "MedicalBusiness" in types or "MedicalClinic" in types, "Missing MedicalBusiness/MedicalClinic in Schema.org"
    assert "FAQPage" in types, "Missing FAQPage in Schema.org"
    print(f"   ✅ Valid Schema.org structured data detected: {types}")
    return True


def validate_internal_links() -> bool:
    print("🔗 [4/7] Validating internal links and anchor integrity...")
    html_files = ["index.html", "impressum.html", "datenschutz.html"]
    for f in html_files:
        with open(f, "r", encoding="utf-8") as file:
            content = file.read()
        ids = set(re.findall(r'id=["\']([a-zA-Z0-9_-]+)["\']', content))
        anchors = re.findall(r'href=["\']#([a-zA-Z0-9_-]+)["\']', content)
        for anchor in anchors:
            if anchor not in ids:
                print(f"❌ Broken anchor #{anchor} in {f}", file=sys.stderr)
                return False

        links = re.findall(r'href=["\']([a-zA-Z0-9_.-]+\.html)["\']', content)
        for link in links:
            if not os.path.exists(link):
                print(f"❌ Broken file link {link} in {f}", file=sys.stderr)
                return False
    print("   ✅ All internal links and section anchors are 100% valid.")
    return True


def validate_css_tokens() -> bool:
    print("🎨 [5/7] Verifying CSS design system tokens and performance rules...")
    css_path = "css/style.css"
    if not os.path.exists(css_path):
        print(f"❌ Missing CSS file: {css_path}", file=sys.stderr)
        return False
    
    with open(css_path, "r", encoding="utf-8") as f:
        css = f.read()

    assert ":root" in css, "Missing :root CSS design token definitions"
    assert "--primary:" in css, "Missing --primary token"
    assert "--accent:" in css, "Missing --accent token"
    assert "content-visibility: auto" in css, "Missing content-visibility performance optimization"
    assert "@media (prefers-reduced-motion: reduce)" in css, "Missing prefers-reduced-motion a11y media query"
    print("   ✅ CSS design tokens, a11y, and performance rules verified.")
    return True


def validate_static_assets() -> bool:
    print("📦 [6/7] Verifying PWA, SEO, Service Worker & Favicon assets...")
    required_assets = [
        "sitemap.xml",
        "robots.txt",
        "manifest.json",
        "sw.js",
        "assets/icons/favicon.svg",
    ]
    for asset in required_assets:
        if not os.path.exists(asset):
            print(f"❌ Missing required asset: {asset}", file=sys.stderr)
            return False

    with open("manifest.json", "r", encoding="utf-8") as f:
        manifest = json.load(f)
    assert manifest.get("name"), "Manifest missing name"
    assert manifest.get("theme_color"), "Manifest missing theme_color"

    print("   ✅ Static assets, PWA manifest, and sitemap verified.")
    return True


def validate_script_syntax() -> bool:
    print("⚙️ [7/7] Compiling automation scripts and checking syntax...")
    scripts = ["scripts/deploy.py", "scripts/create_pr.py", "scripts/validate.py"]
    for script in scripts:
        if os.path.exists(script):
            res = subprocess.run([sys.executable, "-m", "py_compile", script], capture_output=True, text=True)
            if res.returncode != 0:
                print(f"❌ Syntax error in {script}:\n{res.stderr}", file=sys.stderr)
                return False
    print("   ✅ Automation scripts compiled cleanly.")
    return True


def main():
    print("=" * 60)
    print("🚀 Vokalis Quality Gate & CI Validation Suite")
    print("=" * 60)

    checks = [
        run_secret_scan,
        validate_html_files,
        validate_schema_jsonld,
        validate_internal_links,
        validate_css_tokens,
        validate_static_assets,
        validate_script_syntax,
    ]

    for check in checks:
        if not check():
            print("\n❌ Quality gate validation FAILED.")
            sys.exit(1)

    print("\n" + "=" * 60)
    print("🎉 ALL QUALITY GATE CHECKS PASSED SUCCESSFULLY!")
    print("=" * 60)


if __name__ == "__main__":
    main()
