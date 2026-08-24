#!/usr/bin/env python3
"""
Vokalis – Automated GitHub Pull Request Creation Helper
Creates a pull request for the current topic branch to 'main' using either
the GitHub CLI (`gh pr create`) or direct GitHub REST API with osxkeychain/env tokens.
"""

import argparse
import json
import os
import shutil
import subprocess
import sys
import urllib.error
import urllib.request


def get_git_output(cmd: list[str]) -> str:
    return subprocess.check_output(cmd, text=True).strip()


def try_gh_cli(title: str, body: str, base: str = "main", draft: bool = False) -> bool:
    """Attempts to create a PR via GitHub CLI if available and authenticated."""
    if not shutil.which("gh"):
        return False

    cmd = ["gh", "pr", "create", "--base", base, "--title", title, "--body", body]
    if draft:
        cmd.append("--draft")

    try:
        res = subprocess.run(cmd, capture_output=True, text=True)
        if res.returncode == 0:
            print("✅ Pull Request successfully created via GitHub CLI:")
            print(res.stdout.strip())
            return True
        else:
            # gh CLI failed (e.g. not authenticated or PR already exists), fall back to REST API
            print(f"ℹ️ GitHub CLI attempt returned code {res.returncode}: {res.stderr.strip() or res.stdout.strip()}")
            return False
    except Exception as e:
        print(f"ℹ️ gh CLI execution error ({e}), falling back to GitHub API...")
        return False


def get_github_token() -> str:
    env_token = os.getenv("GITHUB_TOKEN") or os.getenv("GH_TOKEN")
    if env_token:
        return env_token

    # Fall back to git credential helper
    try:
        proc = subprocess.Popen(
            ["git", "credential", "fill"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        out, _ = proc.communicate("protocol=https\nhost=github.com\n")
        creds = dict(line.split("=", 1) for line in out.strip().splitlines() if "=" in line)
        token = creds.get("password")
        if token:
            return token
    except Exception:
        pass

    raise RuntimeError("No GitHub token found in GITHUB_TOKEN/GH_TOKEN or git credential helper.")


def get_repo_owner_and_name() -> tuple[str, str]:
    remote_url = get_git_output(["git", "config", "--get", "remote.origin.url"])
    if "github.com" in remote_url:
        path = remote_url.split("github.com")[-1].lstrip(":").lstrip("/")
        if path.endswith(".git"):
            path = path[:-4]
        parts = path.split("/")
        if len(parts) == 2:
            return parts[0], parts[1]
    raise ValueError(f"Could not parse GitHub owner and repository from remote URL: {remote_url}")


def create_pull_request_api(title: str, body: str, base: str = "main", draft: bool = False) -> dict:
    branch = get_git_output(["git", "branch", "--show-current"])
    if not branch or branch == base:
        raise ValueError(f"Cannot create PR: current branch is '{branch}' (must be a topic branch targeting '{base}').")

    owner, repo = get_repo_owner_and_name()
    token = get_github_token()

    url = f"https://api.github.com/repos/{owner}/{repo}/pulls"
    payload = {
        "title": title,
        "head": branch,
        "base": base,
        "body": body,
        "draft": draft,
    }

    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github+json",
            "User-Agent": "Vokalis-Agent-Automation",
            "Content-Type": "application/json",
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(req) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        err_msg = e.read().decode("utf-8")
        try:
            err_json = json.loads(err_msg)
            message = err_json.get("message", err_msg)
            errors = err_json.get("errors", [])
            if errors:
                message += f" ({errors})"
        except Exception:
            message = err_msg
        raise RuntimeError(f"GitHub API error ({e.code}): {message}")


def main():
    parser = argparse.ArgumentParser(description="Create a GitHub Pull Request for current branch")
    parser.add_argument("--title", required=True, help="Pull Request Title")
    parser.add_argument("--body", default="", help="Pull Request Description / Body")
    parser.add_argument("--body-file", help="Path to body markdown file (optional)")
    parser.add_argument("--base", default="main", help="Base branch (default: main)")
    parser.add_argument("--draft", action="store_true", help="Create as draft PR")
    args = parser.parse_args()

    body = args.body
    if args.body_file and os.path.exists(args.body_file):
        with open(args.body_file, "r", encoding="utf-8") as bf:
            body = bf.read()

    # 1. Try gh CLI
    if try_gh_cli(args.title, body, args.base, args.draft):
        return

    # 2. Fall back to direct REST API
    try:
        pr = create_pull_request_api(args.title, body, args.base, args.draft)
        print(f"✅ Pull Request successfully created via GitHub API: {pr.get('html_url')}")
        print(f"   PR #{pr.get('number')}: {pr.get('title')} ({pr.get('state')})")
    except Exception as e:
        print(f"❌ Error creating PR: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
