#!/usr/bin/env python3
"""
Vokalis – High Performance AWS S3 Deployment & Brotli Compression Pipeline
- Pre-compresses all static assets (.html, .css, .js, .svg, .json) with Brotli (quality 11) and Gzip.
- Synchronizes files to AWS S3 bucket 'vokalis.de' with proper Content-Type, Content-Encoding, and Cache-Control.
- Uses AWS Profile 'JavaSDKUser' (or environment variables).
"""

import os
import sys
import gzip
import mimetypes
from pathlib import Path

try:
    import brotli
    import boto3
except ImportError:
    print("❌ Missing dependencies. Please run using the project virtual environment:")
    print("   .venv/bin/python scripts/deploy.py")
    sys.exit(1)

BUCKET_NAME = os.getenv("S3_BUCKET_NAME", "vokalis.de")
AWS_REGION = os.getenv("AWS_REGION", "eu-central-1")
AWS_PROFILE = os.getenv("AWS_PROFILE", "JavaSDKUser")

# Content types mapping
MIME_MAP = {
    ".html": "text/html; charset=utf-8",
    ".css": "text/css; charset=utf-8",
    ".js": "application/javascript; charset=utf-8",
    ".json": "application/json; charset=utf-8",
    ".svg": "image/svg+xml; charset=utf-8",
    ".xml": "application/xml; charset=utf-8",
    ".txt": "text/plain; charset=utf-8",
    ".png": "image/png",
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".webp": "image/webp",
    ".ico": "image/x-icon",
    ".woff2": "font/woff2",
    ".woff": "font/woff",
}

def get_mime_type(file_path: Path) -> str:
    ext = file_path.suffix.lower()
    return MIME_MAP.get(ext, mimetypes.guess_type(str(file_path))[0] or "application/octet-stream")

def get_cache_control(file_path: Path) -> str:
    ext = file_path.suffix.lower()
    if ext == ".html":
        return "public, max-age=3600, must-revalidate"
    return "public, max-age=31536000, immutable"

def get_s3_client():
    try:
        session = boto3.Session(profile_name=AWS_PROFILE)
        return session.client("s3", region_name=AWS_REGION)
    except Exception as e:
        print(f"⚠️ Could not load profile '{AWS_PROFILE}', attempting default credentials: {e}")
        return boto3.client("s3", region_name=AWS_REGION)

def collect_deployable_files(root_dir: Path):
    exclude_dirs = {".git", ".idea", ".agents", ".github", ".junie", ".venv", "scratch", "__pycache__", "node_modules", "dist", "build"}
    exclude_files = {".DS_Store", "README.md", "AGENTS.md", "ARCHITECTURE.md", ".editorconfig", ".gitattributes", ".gitignore"}

    files = []
    for path in root_dir.rglob("*"):
        if path.is_file():
            parts = path.relative_to(root_dir).parts
            if any(p in exclude_dirs for p in parts[:-1]):
                continue
            if path.name in exclude_files or path.name.startswith("."):
                continue
            if path.suffix.lower() in [".py", ".sh", ".tmp", ".log"]:
                continue
            files.append(path)
    return files

def compress_and_upload(s3_client, root_dir: Path):
    files = collect_deployable_files(root_dir)
    print(f"\n🚀 Starting Deployment to AWS S3: s3://{BUCKET_NAME} ({AWS_REGION})")
    print(f"📦 Total files to process: {len(files)}\n")

    compressible_exts = {".html", ".css", ".js", ".json", ".svg", ".xml", ".txt"}
    total_original_bytes = 0
    total_brotli_bytes = 0

    for file_path in sorted(files):
        s3_key = str(file_path.relative_to(root_dir)).replace("\\", "/")
        raw_data = file_path.read_bytes()
        mime_type = get_mime_type(file_path)
        cache_control = get_cache_control(file_path)
        ext = file_path.suffix.lower()
        orig_size = len(raw_data)
        total_original_bytes += orig_size

        if ext in compressible_exts:
            # High-compression Brotli (quality 11)
            br_data = brotli.compress(raw_data, quality=11, mode=brotli.MODE_TEXT)
            br_size = len(br_data)
            total_brotli_bytes += br_size
            ratio = (1 - (br_size / orig_size)) * 100

            # Upload Brotli-compressed version to S3 with Content-Encoding: br
            s3_client.put_object(
                Bucket=BUCKET_NAME,
                Key=s3_key,
                Body=br_data,
                ContentType=mime_type,
                ContentEncoding="br",
                CacheControl=cache_control
            )
            print(f"  ⚡ [Brotli {ratio:4.1f}% saved] {s3_key:<30} ({orig_size} -> {br_size} bytes)")
        else:
            total_brotli_bytes += orig_size
            s3_client.put_object(
                Bucket=BUCKET_NAME,
                Key=s3_key,
                Body=raw_data,
                ContentType=mime_type,
                CacheControl=cache_control
            )
            print(f"  📄 [Uncompressed]     {s3_key:<30} ({orig_size} bytes)")

    overall_savings = (1 - (total_brotli_bytes / total_original_bytes)) * 100 if total_original_bytes > 0 else 0
    print("\n" + "=" * 60)
    print(f"✅ S3 Deployment & Brotli Compression Complete!")
    print(f"📊 Total Size: {total_original_bytes:,} bytes ➔ {total_brotli_bytes:,} bytes ({overall_savings:.1f}% reduction)")
    print(f"🌐 Website Live Target: https://{BUCKET_NAME}/")
    print("=" * 60 + "\n")

def main():
    root_dir = Path(__file__).resolve().parent.parent
    s3_client = get_s3_client()
    compress_and_upload(s3_client, root_dir)

if __name__ == "__main__":
    main()
