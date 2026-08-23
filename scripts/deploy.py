#!/usr/bin/env python3
"""
Vokalis – High Performance AWS S3 Deployment, Brotli Compression & CloudFront Invalidation Pipeline
- Pre-compresses all static assets (.html, .css, .js, .svg, .json, .xml, .txt) with Brotli (quality 11).
- Synchronizes files to AWS S3 bucket with proper Content-Type, Content-Encoding: br, and Cache-Control.
- Invalidates CloudFront cache (/*) upon successful S3 sync.
- Supports AWS Profile (via AWS_PROFILE or --profile), environment variables, .env, and --dry-run.
"""

import os
import sys
import time
import argparse
import mimetypes
from pathlib import Path

# Load .env if present
try:
    from dotenv import load_dotenv
    load_dotenv()
    # also try ~/.env if present
    home_env = Path.home() / ".env"
    if home_env.exists():
        load_dotenv(dotenv_path=home_env)
except ImportError:
    pass

try:
    import brotli
    import boto3
    from botocore.exceptions import ClientError
except ImportError:
    print("❌ Missing dependencies. Please run using the project virtual environment:")
    print("   .venv/bin/python scripts/deploy.py")
    sys.exit(1)

# Default configuration
DEFAULT_BUCKET = os.getenv("S3_BUCKET_NAME", "vokalis.de")
DEFAULT_REGION = os.getenv("AWS_REGION", "eu-central-1")
DEFAULT_PROFILE = os.getenv("AWS_PROFILE", None)
DEFAULT_DISTRIBUTION_ID = os.getenv("CLOUDFRONT_DISTRIBUTION_ID", "")

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
    # Service worker and HTML should always revalidate
    if file_path.name == "sw.js":
        return "public, max-age=0, must-revalidate"
    ext = file_path.suffix.lower()
    if ext == ".html":
        return "public, max-age=3600, must-revalidate"
    if ext in [".xml", ".txt", ".json"]:
        return "public, max-age=86400, must-revalidate"
    return "public, max-age=31536000, immutable"

def get_aws_session(profile_name: str, region_name: str):
    try:
        session = boto3.Session(profile_name=profile_name)
        return session
    except Exception as e:
        print(f"ℹ️ Profile '{profile_name}' not active/found, using default AWS credential chain: {e}")
        return boto3.Session()

def collect_deployable_files(root_dir: Path):
    exclude_dirs = {".git", ".idea", ".agents", ".github", ".junie", ".venv", "scratch", "__pycache__", "node_modules", "dist", "build"}
    exclude_files = {".DS_Store", "README.md", "AGENTS.md", "ARCHITECTURE.md", ".editorconfig", ".gitattributes", ".gitignore", "requirements.txt"}

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

def compress_and_upload(s3_client, bucket_name: str, region_name: str, root_dir: Path, dry_run: bool = False):
    files = collect_deployable_files(root_dir)
    mode_prefix = " [DRY-RUN]" if dry_run else ""
    print(f"\n🚀 Starting Deployment{mode_prefix} to AWS S3: s3://{bucket_name} ({region_name})")
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

            if not dry_run:
                s3_client.put_object(
                    Bucket=bucket_name,
                    Key=s3_key,
                    Body=br_data,
                    ContentType=mime_type,
                    ContentEncoding="br",
                    CacheControl=cache_control
                )
            print(f"  ⚡ [Brotli {ratio:4.1f}% saved] {s3_key:<30} ({orig_size} -> {br_size} bytes)")
        else:
            total_brotli_bytes += orig_size
            if not dry_run:
                s3_client.put_object(
                    Bucket=bucket_name,
                    Key=s3_key,
                    Body=raw_data,
                    ContentType=mime_type,
                    CacheControl=cache_control
                )
            print(f"  📄 [Uncompressed]     {s3_key:<30} ({orig_size} bytes)")

    overall_savings = (1 - (total_brotli_bytes / total_original_bytes)) * 100 if total_original_bytes > 0 else 0
    print("\n" + "=" * 60)
    print(f"✅ S3 Deployment{mode_prefix} & Brotli Compression Complete!")
    print(f"📊 Total Size: {total_original_bytes:,} bytes ➔ {total_brotli_bytes:,} bytes ({overall_savings:.1f}% reduction)")
    print(f"🌐 S3 Target: s3://{bucket_name}/")
    print("=" * 60)

def invalidate_cloudfront(cf_client, distribution_id: str, dry_run: bool = False):
    if not distribution_id:
        print("\nℹ️ CloudFront Invalidation: No CLOUDFRONT_DISTRIBUTION_ID provided.")
        print("   Set CLOUDFRONT_DISTRIBUTION_ID in your .env or pass --distribution-id <ID> to invalidate cache automatically.")
        return

    if dry_run:
        print(f"\nℹ️ [DRY-RUN] CloudFront Invalidation skipped for distribution: {distribution_id}")
        return

    print(f"\n🔄 Requesting CloudFront Cache Invalidation for distribution: {distribution_id}...")
    try:
        response = cf_client.create_invalidation(
            DistributionId=distribution_id,
            InvalidationBatch={
                "Paths": {
                    "Quantity": 1,
                    "Items": ["/*"]
                },
                "CallerReference": f"vokalis-deploy-{int(time.time())}"
            }
        )
        invalidation = response.get("Invalidation", {})
        inval_id = invalidation.get("Id", "N/A")
        status = invalidation.get("Status", "InProgress")
        print(f"✅ CloudFront Cache Invalidation initiated successfully!")
        print(f"   Invalidation ID: {inval_id} (Status: {status})")
        print(f"   Paths: ['/*']")
    except ClientError as e:
        print(f"⚠️ CloudFront Invalidation error: {e.response.get('Error', {}).get('Message', str(e))}")
    except Exception as e:
        print(f"⚠️ CloudFront Invalidation error: {e}")

def main():
    parser = argparse.ArgumentParser(description="Vokalis S3 Deploy, Brotli Compression & CloudFront Invalidation")
    parser.add_argument("--bucket", default=DEFAULT_BUCKET, help=f"S3 Bucket name (default: {DEFAULT_BUCKET})")
    parser.add_argument("--region", default=DEFAULT_REGION, help=f"AWS Region (default: {DEFAULT_REGION})")
    parser.add_argument("--profile", default=DEFAULT_PROFILE, help=f"AWS CLI profile name (default: {DEFAULT_PROFILE})")
    parser.add_argument("--distribution-id", default=DEFAULT_DISTRIBUTION_ID, help="CloudFront Distribution ID to invalidate cache")
    parser.add_argument("--dry-run", action="store_true", help="Simulate deployment and calculate Brotli compression savings without uploading to AWS")
    args = parser.parse_args()

    root_dir = Path(__file__).resolve().parent.parent

    session = get_aws_session(args.profile, args.region)
    s3_client = session.client("s3", region_name=args.region)
    cf_client = session.client("cloudfront", region_name=args.region)

    compress_and_upload(s3_client, args.bucket, args.region, root_dir, dry_run=args.dry_run)
    invalidate_cloudfront(cf_client, args.distribution_id, dry_run=args.dry_run)

    print(f"\n🎉 Deployment pipeline finished successfully!\n")

if __name__ == "__main__":
    main()
