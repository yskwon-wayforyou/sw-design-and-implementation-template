#!/usr/bin/env python3
"""Assign TraceID to design docs, rename files, fix markdown links.

TraceID format (project-local): {CATEGORY}-{NNN} — no YST- prefix.
Example: SYS-001, UC-006, REG-001.
Filenames: {TraceID}-{slug}.md

Already applied to this repo. Re-run only when adding new docs from legacy names.
See scripts/migrate-remove-yst-prefix.py for prefix stripping.
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

# old relative path from docs/ -> (trace_id, new basename without dir)
MAPPING: dict[str, tuple[str, str]] = {
    "README.md": ("IDX-001", "IDX-001-README.md"),
    "DESIGN-INTEGRATED.md": ("HUB-001", "HUB-001-DESIGN-INTEGRATED.md"),
    "design-owner-feedback.md": ("FBK-001", "FBK-001-design-owner-feedback.md"),
    "system.md": ("SYS-001", "SYS-001-system.md"),
    "business.md": ("BUS-001", "BUS-001-business.md"),
    "usecases.md": ("UCL-001", "UCL-001-usecases.md"),
    "qualities.md": ("QLT-001", "QLT-001-qualities.md"),
    "asr.md": ("ASR-001", "ASR-001-asr.md"),
    "ai_quality_profile.md": ("AIQ-001", "AIQ-001-ai_quality_profile.md"),
    "usecase/UC-001-profile-connect.md": (
        "UC-001",
        "UC-001-profile-connect.md",
    ),
    "usecase/UC-002-manual-order.md": (
        "UC-002",
        "UC-002-manual-order.md",
    ),
    "usecase/UC-003-market-dashboard.md": (
        "UC-003",
        "UC-003-market-dashboard.md",
    ),
    "usecase/UC-004-daytrade-pattern.md": (
        "UC-004",
        "UC-004-daytrade-pattern.md",
    ),
    "usecase/UC-005-longterm-recommend.md": (
        "UC-005",
        "UC-005-longterm-recommend.md",
    ),
    "usecase/UC-006-ai-auto-approval.md": (
        "UC-006",
        "UC-006-ai-auto-approval.md",
    ),
    "usecase/UC-007-rnn-training-data.md": (
        "UC-007",
        "UC-007-rnn-training-data.md",
    ),
    "usecase/UC-008-pnl-history.md": (
        "UC-008",
        "UC-008-pnl-history.md",
    ),
    "usecase/UC-009-multi-source-data.md": (
        "UC-009",
        "UC-009-multi-source-data.md",
    ),
    "usecase/UC-010-android-parity.md": (
        "UC-010",
        "UC-010-android-parity.md",
    ),
    "usecase/UC-011-risk-guard.md": (
        "UC-011",
        "UC-011-risk-guard.md",
    ),
    "usecase/UC-012-news-disclosure.md": (
        "UC-012",
        "UC-012-news-disclosure.md",
    ),
    "domain/model.md": ("DOM-001", "DOM-001-model.md"),
    "domain/UC-004-daytrade-domain.md": (
        "DOM-004",
        "DOM-004-daytrade-domain.md",
    ),
    "domain/UC-006-ai-domain.md": (
        "DOM-006",
        "DOM-006-ai-domain.md",
    ),
    "quality/scenarios.md": ("QSC-001", "QSC-001-scenarios.md"),
    "quality/evaluations.md": ("QEV-001", "QEV-001-evaluations.md"),
    "quality/QS-001-realtime-market-data.md": (
        "QS-001",
        "QS-001-realtime-market-data.md",
    ),
    "quality/QS-004-ai-approval-gate.md": (
        "QS-004",
        "QS-004-ai-approval-gate.md",
    ),
    "candidate/candidates.md": ("CAT-001", "CAT-001-candidates.md"),
    "candidate/android-sync.md": ("CND-001", "CND-001-android-sync.md"),
    "candidate/layered-modularity.md": (
        "CND-002",
        "CND-002-layered-modularity.md",
    ),
    "candidate/ml-rnn-architecture.md": (
        "CND-003",
        "CND-003-ml-rnn-architecture.md",
    ),
    "candidate/performance-realtime.md": (
        "CND-004",
        "CND-004-performance-realtime.md",
    ),
    "candidate/security-safety.md": (
        "CND-005",
        "CND-005-security-safety.md",
    ),
    "decision/decisions.md": ("DEC-001", "DEC-001-decisions.md"),
    "decision/evaluations.md": ("DEC-002", "DEC-002-evaluations.md"),
    "architecture/module.md": ("ARC-001", "ARC-001-module.md"),
    "architecture/deployment.md": ("ARC-002", "ARC-002-deployment.md"),
    "adr/001-android-synchub.md": ("ADR-001", "ADR-001-android-synchub.md"),
    "adr/002-rnn-personal-model.md": (
        "ADR-002",
        "ADR-002-rnn-personal-model.md",
    ),
    "adr/003-trading-modes-package.md": (
        "ADR-003",
        "ADR-003-trading-modes-package.md",
    ),
    "adr/004-ai-auto-without-approval-setting.md": (
        "ADR-004",
        "ADR-004-ai-auto-without-approval-setting.md",
    ),
}

# Build link replacement: various old path forms -> new path from docs/
LINK_REPLACEMENTS: list[tuple[str, str]] = []


def new_rel(old_rel: str) -> str:
    trace_id, new_base = MAPPING[old_rel]
    parent = Path(old_rel).parent
    if str(parent) == ".":
        return new_base
    return str(parent / new_base)


def build_link_replacements() -> None:
    for old_rel, (_, new_base) in MAPPING.items():
        parent = Path(old_rel).parent
        new_path = new_rel(old_rel)
        old_name = Path(old_rel).name
        new_name = Path(new_path).name

        if str(parent) == ".":
            patterns = [
                (old_rel, new_path),
                (old_name, new_name),
            ]
        else:
            dir_name = str(parent)
            patterns = [
                (old_rel, new_path),
                (f"{dir_name}/{old_name}", new_path),
                (old_name, new_name),  # same-dir relative
            ]
        for old, new in patterns:
            if old != new:
                LINK_REPLACEMENTS.append((old, new))


def inject_trace_id(text: str, trace_id: str) -> str:
    row = f"| TraceID | {trace_id} |"
    if re.search(r"^\|\s*TraceID\s*\|", text, re.MULTILINE):
        return re.sub(
            r"^\|\s*TraceID\s*\|[^\n]*\n",
            row + "\n",
            text,
            count=1,
            flags=re.MULTILINE,
        )
    # After first metadata table header row (| xxx | yyy |)
    m = re.search(r"(^# .+\n\n)(\|.+\|\n\|[-:| ]+\|\n)", text, re.MULTILINE)
    if m:
        insert_at = m.end(2)
        return text[:insert_at] + row + "\n" + text[insert_at:]
    # After title + blank line
    m2 = re.search(r"^(# .+\n)\n", text, re.MULTILINE)
    if m2:
        insert_at = m2.end()
        block = f"\n| 항목 | 내용 |\n|------|------|\n{row}\n\n"
        return text[:insert_at] + block + text[insert_at:]
    return text


def fix_links(text: str) -> str:
    # Longest match first
    for old, new in sorted(LINK_REPLACEMENTS, key=lambda x: -len(x[0])):
        text = text.replace(f"]({old})", f"]({new})")
        text = text.replace(f"](../{old})", f"](../{new})")
        text = text.replace(f"](../../{old})", f"](../../{new})")
    # Directory-only links (trailing /)
    for old_rel in MAPPING:
        parent = Path(old_rel).parent
        if str(parent) != ".":
            dir_name = str(parent)
            # e.g. [usecase/](usecase/) -> still valid if dir unchanged
            pass
    return text


def write_registry() -> None:
    lines = [
        "# TraceID 레지스트리 — YSTrading 설계 문서",
        "",
        "| TraceID | 경로 | 제목(요약) |",
        "|---------|------|------------|",
    ]
    titles: dict[str, str] = {}
    for old_rel in sorted(MAPPING.keys()):
        path = DOCS / old_rel
        if path.exists():
            first = path.read_text(encoding="utf-8").split("\n")[0]
            titles[old_rel] = first.lstrip("# ").strip()
    for old_rel in sorted(MAPPING.keys(), key=lambda r: MAPPING[r][0]):
        trace_id, new_base = MAPPING[old_rel]
        new_path = new_rel(old_rel)
        title = titles.get(old_rel, "—")
        lines.append(f"| {trace_id} | `{new_path}` | {title} |")
    lines.extend(
        [
            "",
            "## 규칙",
            "",
            "- 형식: `{범주}-{일련}` — YSTrading 저장소 내부 전용",
            "- 파일명: `{TraceID}-{설명-slug}.md`",
            "- 본문 메타데이터 표에 `TraceID` 행 필수",
            "- 정본: REG-001-trace-registry.md",
            "",
        ]
    )
    reg_path = DOCS / "REG-001-trace-registry.md"
    reg_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    build_link_replacements()
    write_registry()

    # Update content before rename (paths still old on disk)
    for old_rel, (trace_id, _) in MAPPING.items():
        path = DOCS / old_rel
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        text = inject_trace_id(text, trace_id)
        text = fix_links(text)
        path.write_text(text, encoding="utf-8")

    reg = DOCS / "REG-001-trace-registry.md"
    reg.write_text(inject_trace_id(reg.read_text(encoding="utf-8"), "REG-001"), encoding="utf-8")

    # Rename files (deepest paths first)
    for old_rel in sorted(MAPPING.keys(), key=lambda r: -r.count("/")):
        old_path = DOCS / old_rel
        if not old_path.exists():
            continue
        new_path = DOCS / new_rel(old_rel)
        new_path.parent.mkdir(parents=True, exist_ok=True)
        old_path.rename(new_path)

    # Fix links again after rename (registry + any cross-refs)
    all_md = list(DOCS.rglob("*.md"))
    for path in all_md:
        text = path.read_text(encoding="utf-8")
        updated = fix_links(text)
        if updated != text:
            path.write_text(updated, encoding="utf-8")

    print(f"Done: {len(MAPPING)} documents, registry at docs/REG-001-trace-registry.md")


if __name__ == "__main__":
    main()
