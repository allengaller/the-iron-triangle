#!/usr/bin/env python3
"""Read-only structural inventory for the comprehensive book review."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MD = sorted(p for p in ROOT.rglob("*.md") if ".git" not in p.parts)


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def table_issues(path: Path, lines: list[str]) -> list[dict]:
    issues = []
    in_fence = False
    block: list[tuple[int, str]] = []

    def check(rows: list[tuple[int, str]]) -> None:
        if len(rows) < 2 or not re.match(r"^\|(?:\s*:?-+:?\s*\|)+$", rows[1][1]):
            return
        expected = rows[0][1].count("|")
        for line_no, text in rows:
            if text.count("|") != expected:
                issues.append({"file": rel(path), "line": line_no, "expected_pipes": expected, "actual_pipes": text.count("|")})

    for line_no, line in enumerate(lines + [""], 1):
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
        is_table = not in_fence and line.startswith("|") and line.endswith("|")
        if is_table:
            block.append((line_no, line))
        else:
            check(block)
            block = []
    return issues


def main() -> None:
    files = []
    malformed_tables = []
    for path in MD:
        text = path.read_text(encoding="utf-8")
        lines = text.splitlines()
        name = rel(path)
        files.append({
            "file": name,
            "lines": len(lines),
            "bytes": len(text.encode("utf-8")),
            "h1_count": sum(line.startswith("# ") for line in lines),
            "has_review_recap": "本章要点回顾" in text,
            "has_template_time": "时点：" in text,
            "has_version_log": "版本记录" in text,
            "http_occurrences": len(re.findall(r"https?://", text)),
            "unclosed_code_fence": sum(line.lstrip().startswith("```") for line in lines) % 2 == 1,
        })
        malformed_tables.extend(table_issues(path, lines))

    manuscript = [f for f in files if f["file"].startswith("manuscript/")]
    templates = [f for f in files if f["file"].startswith("templates/")]
    output = {
        "markdown_files_including_root_reports": len(files),
        "total_markdown_lines": sum(f["lines"] for f in files),
        "total_markdown_bytes": sum(f["bytes"] for f in files),
        "chapters": len([f for f in manuscript if re.search(r"/ch\d{2}-", f["file"])]),
        "appendices": len([f for f in manuscript if "/appx-" in f["file"]]),
        "templates": len(templates),
        "manuscript_other": len(manuscript) - len([f for f in manuscript if re.search(r"/ch\d{2}-|/appx-", f["file"])]),
        "h1_not_exactly_one": [f["file"] for f in files if f["h1_count"] != 1],
        "chapters_without_recap": [f["file"] for f in manuscript if re.search(r"/ch\d{2}-", f["file"]) and not f["has_review_recap"]],
        "appendices_without_recap": [f["file"] for f in manuscript if "/appx-" in f["file"] and not f["has_review_recap"]],
        "templates_without_time": [f["file"] for f in templates if not f["has_template_time"]],
        "templates_without_version_log": [f["file"] for f in templates if not f["has_version_log"]],
        "unclosed_code_fences": [f["file"] for f in files if f["unclosed_code_fence"]],
        "malformed_table_rows": malformed_tables,
        "http_occurrences_by_file": {f["file"]: f["http_occurrences"] for f in files if f["http_occurrences"]},
        "files": files,
    }
    (ROOT / ".tmp" / "review-structure-results.json").write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in output.items() if k != "files"}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
