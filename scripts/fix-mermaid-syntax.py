#!/usr/bin/env python3
"""Normalize Mermaid in docs/ for GitHub/Cursor preview compatibility."""
from __future__ import annotations

import re
from pathlib import Path

DOCS = Path(__file__).resolve().parents[1] / "docs"


def mindmap_to_flowchart(code: str) -> str:
    lines = [ln.rstrip() for ln in code.strip().splitlines()]
    if not lines or lines[0].strip() != "mindmap":
        return code
    indent_stack: list[tuple[int, str]] = []
    out = ["flowchart TB"]
    root = lines[1].strip() if len(lines) > 1 else "root((Root))"
    root_id = "root"
    if root.startswith("root"):
        out.append(f"  {root}")
    else:
        out.append(f"  {root_id}(({root}))")
    parent = root_id if root.startswith("root") else root_id

    def node_id(label: str) -> str:
        safe = re.sub(r"[^\w]", "_", label).strip("_") or "n"
        return safe[:40]

    for raw in lines[2:]:
        if not raw.strip():
            continue
        indent = len(raw) - len(raw.lstrip())
        label = raw.strip()
        nid = node_id(label)
        while indent_stack and indent_stack[-1][0] >= indent:
            indent_stack.pop()
        par = indent_stack[-1][1] if indent_stack else parent
        out.append(f'  {nid}["{label}"]')
        out.append(f"  {par} --> {nid}")
        indent_stack.append((indent, nid))
    return "\n".join(out) + "\n"


def gitgraph_to_flowchart(code: str) -> str:
    if not code.strip().startswith("gitGraph"):
        return code
    return (
        "flowchart LR\n"
        '  main["main"]\n'
        '  feat["feat/uc-002-order"]\n'
        '  wip["wip"]\n'
        '  tests["tests"]\n'
        '  tag["v0.2.0"]\n'
        "  main --> feat\n"
        "  feat --> wip\n"
        "  wip --> tests\n"
        "  tests --> tag\n"
        "  tag --> main\n"
    )


def fix_sequence_diagram(code: str) -> str:
    if not code.lstrip().startswith("sequenceDiagram"):
        return code
    code = re.sub(
        r"^(\s*participant)Dlg\b",
        r"\1 Dlg",
        code,
        flags=re.M,
    )
    code = re.sub(
        r"^(\s*participant\s+\w+\s+as\s+)Investor\b",
        r'\1"Investor"',
        code,
        flags=re.M,
    )

    def quote_msg(m: re.Match[str]) -> str:
        prefix, arrow, target, msg = m.group(1), m.group(2), m.group(3), m.group(4).strip()
        if msg.startswith('"') and msg.endswith('"'):
            return m.group(0)
        if "(" in msg or ")" in msg or "→" in msg or "/" in msg:
            msg = msg.replace('"', "'")
            return f"{prefix}{arrow}{target}: \"{msg}\""
        return m.group(0)

    code = re.sub(
        r"^(\s*)(->>|-->>)(\w+):\s*([^\n]+)$",
        quote_msg,
        code,
        flags=re.M,
    )
    code = re.sub(
        r"^(\s*Note over [^:]+:)\s*([^\n]+)$",
        lambda m: (
            f'{m.group(1)} "{m.group(2).strip()}"'
            if "→" in m.group(2) or "(" in m.group(2)
            else m.group(0)
        ),
        code,
        flags=re.M,
    )
    return code


def fix_state_diagram(code: str) -> str:
    if "stateDiagram" not in code:
        return code
    return re.sub(
        r"(-->\s*\w+:\s*)([^;\n\"]+[>=→][^;\n\"]*)$",
        lambda m: f'{m.group(1)}"{m.group(2).strip()}"',
        code,
        flags=re.M,
    )


def fix_flowchart_edges(code: str) -> str:
    if not code.lstrip().startswith("flowchart"):
        return code
    # Only quote edge labels: -->|label| or ---|label|
    return re.sub(
        r"(-->|---)\|([^"|]+)\|",
        lambda m: f'{m.group(1)}|"{m.group(2).strip()}"|'
        if re.search(r"[\s가-힣→/()]", m.group(2))
        else m.group(0),
        code,
    )


def fix_block(code: str) -> str:
    c = code
    if c.strip().startswith("mindmap"):
        c = mindmap_to_flowchart(c)
    elif c.strip().startswith("gitGraph"):
        c = gitgraph_to_flowchart(c)
    c = fix_sequence_diagram(c)
    c = fix_state_diagram(c)
    c = fix_flowchart_edges(c)
    return c


def main() -> None:
    changed = 0
    for md in sorted(DOCS.rglob("*.md")):
        text = md.read_text(encoding="utf-8")

        def repl(m: re.Match[str]) -> str:
            nonlocal changed
            old = m.group(1)
            new = fix_block(old)
            if new != old:
                changed += 1
            return f"```mermaid\n{new}```"

        new_text = re.sub(r"```mermaid\n(.*?)```", repl, text, flags=re.S)
        if new_text != text:
            md.write_text(new_text, encoding="utf-8")
            print("updated", md.relative_to(DOCS.parent))
    print(f"blocks modified: {changed}")


if __name__ == "__main__":
    main()
