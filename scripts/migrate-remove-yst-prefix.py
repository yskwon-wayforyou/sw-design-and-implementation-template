#!/usr/bin/env python3
"""Remove YST- prefix from design doc filenames, TraceIDs, and links."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

# Match YST- prefix but not inside YSTrading
YST_PREFIX = re.compile(r"(?<![a-zA-Z])YST-")


def strip_yst(text: str) -> str:
    return YST_PREFIX.sub("", text)


def main() -> None:
    # 1) Rename files: docs/**/YST-*.md (longest names first)
    to_rename: list[tuple[Path, Path]] = []
    for path in sorted(DOCS.rglob("YST-*.md"), key=lambda p: len(p.name), reverse=True):
        new_name = strip_yst(path.name)
        new_path = path.parent / new_name
        if path != new_path:
            to_rename.append((path, new_path))

    for old, new in to_rename:
        new.parent.mkdir(parents=True, exist_ok=True)
        old.rename(new)

    # 2) Replace YST- in markdown and scripts (protect YSTrading)
    targets = list(DOCS.rglob("*.md"))
    targets.append(ROOT / "README.md")
    for script in ROOT.glob("scripts/*.py"):
        if script.name != "migrate-remove-yst-prefix.py":
            targets.append(script)

    for path in targets:
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        updated = strip_yst(text)
        if updated != text:
            path.write_text(updated, encoding="utf-8")

    print(f"Renamed {len(to_rename)} files; updated content in {DOCS} and README")


if __name__ == "__main__":
    main()
