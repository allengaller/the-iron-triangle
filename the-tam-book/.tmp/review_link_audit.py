#!/usr/bin/env python3
"""Inventory and optionally probe Markdown HTTP links for the 2026-10-25 review."""
from __future__ import annotations

import argparse
import concurrent.futures
import json
import re
import urllib.error
import urllib.request
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LINK_RE = re.compile(r"\[[^\]]*\]\((https?://[^)\s]+)\)")


def inventory() -> list[dict]:
    rows = []
    for path in sorted(ROOT.rglob("*.md")):
        if ".git" in path.parts:
            continue
        for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            for url in LINK_RE.findall(line):
                rows.append({
                    "file": path.relative_to(ROOT).as_posix(),
                    "line": line_no,
                    "url": url.rstrip(".,;，。；"),
                })
    return rows


def probe(row: dict, timeout: int) -> dict:
    result = dict(row)
    request = urllib.request.Request(
        row["url"],
        headers={
            "User-Agent": "Mozilla/5.0 (compatible; TAM-Book-Link-Review/1.0)",
            "Range": "bytes=0-2047",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            response.read(1)
            result.update(status=response.status, final_url=response.geturl(), result="reachable")
    except urllib.error.HTTPError as exc:
        result.update(status=exc.code, final_url=exc.geturl(), result="http_error_or_blocked")
    except Exception as exc:  # Network failures are explicitly not proof of a dead link.
        result.update(status=None, final_url=None, result="unverified", error=f"{type(exc).__name__}: {exc}")
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--timeout", type=int, default=15)
    parser.add_argument("--workers", type=int, default=8)
    args = parser.parse_args()
    rows = inventory()
    output = {
        "root": str(ROOT),
        "markdown_link_occurrences": len(rows),
        "unique_urls": len({row["url"] for row in rows}),
        "per_file": dict(Counter(row["file"] for row in rows)),
        "links": rows,
    }
    print(json.dumps({k: v for k, v in output.items() if k != "links"}, ensure_ascii=False, indent=2))
    if args.check:
        unique = {row["url"]: row for row in rows}
        with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as pool:
            checked = list(pool.map(lambda row: probe(row, args.timeout), unique.values()))
        by_url = {row["url"]: row for row in checked}
        output["links"] = [by_url[row["url"]] | {"file": row["file"], "line": row["line"]} for row in rows]
        output["probe_summary"] = dict(Counter(row["result"] for row in checked))
        output["http_status_summary"] = dict(Counter(str(row["status"]) for row in checked))
        print(json.dumps({"probe_summary": output["probe_summary"], "http_status_summary": output["http_status_summary"]}, ensure_ascii=False, indent=2))
        for row in checked:
            print(f"{row['result']}\t{row['status']}\t{row['url']}")
    (ROOT / ".tmp" / "review-link-results.json").write_text(
        json.dumps(output, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    main()
