"""Analyze scenario step screenshots and UI snapshots."""

from __future__ import annotations

from pathlib import Path
from typing import Any


def analyze_step(
    *,
    screenshot_path: Path | None,
    expectation: str,
    ui_snapshot: dict[str, Any],
    assertion: str,
) -> tuple[str, str]:
    """
    Returns (verdict, notes).
    verdict: pass | fail | review | inconclusive
    """
    notes: list[str] = []

    if assertion == "fail":
        return "fail", "pytest assertion or action failed before screenshot analysis"

    if screenshot_path is None or not screenshot_path.exists():
        return "fail", "screenshot missing"

    size = screenshot_path.stat().st_size
    if size < 1024:
        notes.append(f"screenshot very small ({size} bytes)")
        return "review", "; ".join(notes)

    if _is_likely_blank(screenshot_path):
        notes.append("image appears blank or uniform")
        return "review", "; ".join(notes)

    if expectation:
        ui_text = _collect_ui_text(ui_snapshot)
        keywords = _extract_keywords(expectation)
        missing = [k for k in keywords if k and k not in ui_text]
        if missing:
            notes.append(f"expected keywords not in UI snapshot: {missing}")
            return "review", "; ".join(notes)
        notes.append("UI snapshot contains expected keywords")

    notes.append("screenshot captured; assertion passed")
    return "pass", "; ".join(notes)


def _collect_ui_text(ui_snapshot: dict[str, Any]) -> str:
    parts: list[str] = []
    if title := ui_snapshot.get("window_title"):
        parts.append(str(title))
    for label in ui_snapshot.get("button_labels") or []:
        parts.append(str(label))
    return " ".join(parts).lower()


def _extract_keywords(expectation: str) -> list[str]:
    import re

    tokens = re.findall(r"[\w가-힣]+", expectation)
    return [t.lower() for t in tokens if len(t) >= 2][:10]


def _is_likely_blank(path: Path) -> bool:
    try:
        from PIL import Image
        import statistics

        img = Image.open(path).convert("L")
        pixels = list(img.getdata())
        if len(pixels) < 100:
            return True
        return statistics.pstdev(pixels) < 3.0
    except ImportError:
        return False
    except Exception:
        return False
