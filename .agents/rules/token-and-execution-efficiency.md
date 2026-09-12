# Token and Execution Efficiency Guidelines

## 1. Context Window & Dataset Boundaries
* **Targeted File Inspection:**
  - Never dump entire large files into context. Use `view_file` with explicit `StartLine` and `EndLine` slices (30–80 lines).
  - Use `grep_search` with specific query patterns and file filters to locate lines before viewing.
* **Dataset & Cache Isolation:**
  - Never ingest massive data payloads, minified bundles, or large cache dumps into the prompt context.
  - Rely on targeted grep queries, bounded file slices, or offline processing.
* **On-Demand Progressive Skill Loading:**
  - Inspect skills only when directly activated for the task. Avoid indiscriminately loading multiple skills.

## 2. Subagent Boundary Isolation
* **Heavy Operation Offloading:**
  - Offload verbose test runs, extensive log analysis, bulk builds, and large-scale repository scans to dedicated subagents.
* **Executive Memo Pattern:**
  - Subagents must operate within isolated context windows and return concise executive summaries (status, root cause, exact line numbers, and actionable diffs) rather than raw command dumps.
  - Protects primary agent context from pollution by repetitive stack traces and verbose build output.

## 3. Surgical Tool & Edit Economy
* **Compact Modifications:**
  - Use `replace_file_content` for single contiguous edits (5–25 lines) and `multi_replace_file_content` for non-adjacent edits.
  - Never overwrite entire files unless creating a new file or updating tiny configs (< 50 lines).
* **CLI & Output Economy:**
  - Execute commands with quiet flags (`-q`, `--quiet`) and rely on return exit codes.
  - Pipe or limit output when running commands that produce extensive logs.

## 4. Communication & Artifact Discipline
* **Concise Reporting:** Direct answers without filler, generic preambles, or conversational repetition.
* **Zero Artifact Redundancy:** When creating/modifying artifacts (`implementation_plan.md`, `walkthrough.md`), do not duplicate contents in chat responses; reference the artifact link directly.
* **Symbol Linking:** Use clickable markdown file links with `file://` URIs and line anchors.
