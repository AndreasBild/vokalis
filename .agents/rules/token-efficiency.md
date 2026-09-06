# Token Efficiency Guidelines & Invariants

## 1. Context Window Conservation
* **Targeted File Inspection:**
  - Never dump an entire large file into context. Use `view_file` with explicit `StartLine` and `EndLine` slices (typically 30–80 lines at a time).
  - Use `grep_search` with specific query patterns and `Includes` file filters to locate line numbers before viewing files.
* **Directory Search Economy:**
  - Avoid wide recursive directory listings. Use targeted subpaths (`scripts/`, `css/`, `.agents/rules/`).
  - Maintain `.agentignore` to exclude build artifacts, logs, caches, and test fixtures from agent ingestion.
* **On-Demand Skill Loading:**
  - Inspect skills only when directly activated for the task at hand. Avoid indiscriminately loading multiple skills in a single session.

## 2. Surgical Tool & Edit Economy
* **Surgical Content Replacements:**
  - Use `replace_file_content` for single contiguous changes with compact target blocks (5–20 lines).
  - Use `multi_replace_file_content` strictly when making multiple non-adjacent changes in the same file.
  - Never overwrite an entire file (`write_to_file` with `Overwrite=true`) unless creating a new file or replacing a tiny configuration file (< 50 lines).
* **Pre-Flight Validation:**
  - Inspect exact lines and indentation before calling replace tools to avoid failed match errors and wasteful retry cycles.
* **Compact Terminal Output:**
  - Run CLI commands with flags that suppress verbosity when detail is not needed (e.g., `--quiet`, `-q`, piping to `head` or `grep`).
  - Rely on return exit codes rather than streaming hundreds of verbose lines.

## 3. Communication & Output Conciseness
* **Direct Answers:**
  - Keep conversational responses concise, structured, and focused.
  - Avoid conversational filler, apologies, or verbose preambles.
* **Zero Artifact Redundancy:**
  - When creating or modifying an artifact (`implementation_plan.md`, `walkthrough.md`), do not re-summarize its entire text in the chat response. Provide a clickable link and highlight only decisions or open questions requiring attention.
* **Clickable Navigation Links:**
  - Always link files and code symbols using markdown links with the `file://` scheme (e.g. `[filename.ext](file:///path/to/file#L10-L25)`).
