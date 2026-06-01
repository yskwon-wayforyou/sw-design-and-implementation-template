"""Scenario test session: steps, screenshots, HTML report."""

from __future__ import annotations

import json
import subprocess
import time
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable

from .analyze import analyze_step
from .report_html import write_html_report
from .screenshot import capture_widget_png

REPO_ROOT = Path(__file__).resolve().parents[3]
REPORTS_ROOT = REPO_ROOT / "artifacts" / "test-reports"


@dataclass
class StepRecord:
    index: int
    title: str
    expectation: str = ""
    action_log: str = ""
    screenshot: str = ""
    ui_snapshot: dict[str, Any] = field(default_factory=dict)
    assertion: str = "pass"
    analysis_verdict: str = "inconclusive"
    analysis_notes: str = ""
    duration_ms: int = 0
    error: str = ""


@dataclass
class ScenarioSession:
    """Record scenario steps and emit HTML report on finish."""

    run_dir: Path | None = None
    uc: str = ""
    scr: str = ""
    nbde: str = ""
    test_nodeid: str = ""
    steps: list[StepRecord] = field(default_factory=list)
    _step_counter: int = 0
    _started_at: float = 0.0

    def begin(
        self,
        *,
        uc: str = "",
        scr: str = "",
        nbde: str = "",
        test_nodeid: str = "",
    ) -> None:
        self.uc = uc
        self.scr = scr
        self.nbde = nbde
        self.test_nodeid = test_nodeid
        self._started_at = time.time()
        ts = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
        slug_uc = (uc or "scenario").replace("-", "").lower()
        slug_nbde = (nbde or "x").lower()
        self.run_dir = REPORTS_ROOT / f"{ts}_{slug_uc}_{slug_nbde}_running"
        (self.run_dir / "steps").mkdir(parents=True, exist_ok=True)
        self.steps = []
        self._step_counter = 0

    def step(
        self,
        title: str,
        *,
        expectation: str = "",
        action: Callable[[], None] | None = None,
        capture_widget: Any = None,
        ui_snapshot: dict[str, Any] | None = None,
    ) -> None:
        if self.run_dir is None:
            raise RuntimeError("Call begin() before step()")

        self._step_counter += 1
        idx = self._step_counter
        t0 = time.time()
        record = StepRecord(index=idx, title=title, expectation=expectation)
        action_log: list[str] = []

        try:
            if action is not None:
                action()
                action_log.append("action:ok")
            record.assertion = "pass"
        except Exception as exc:
            record.assertion = "fail"
            record.error = f"{type(exc).__name__}: {exc}"
            action_log.append(f"action:fail:{type(exc).__name__}")
            raise
        finally:
            slug = _slug(title)
            rel_png = f"steps/{idx:02d}_{slug}.png"
            abs_png = self.run_dir / rel_png
            snap = dict(ui_snapshot or {})
            if capture_widget is not None:
                snap.update(_qt_ui_snapshot(capture_widget))
                capture_widget_png(capture_widget, abs_png)
                action_log.append("screenshot:capture")
            elif capture_widget is None and _qt_available():
                snap.setdefault("note", "no widget passed for screenshot")
            record.screenshot = rel_png if abs_png.exists() else ""
            record.ui_snapshot = snap
            record.action_log = "; ".join(action_log)
            record.duration_ms = int((time.time() - t0) * 1000)

            verdict, notes = analyze_step(
                screenshot_path=abs_png if record.screenshot else None,
                expectation=expectation,
                ui_snapshot=snap,
                assertion=record.assertion,
            )
            record.analysis_verdict = verdict
            record.analysis_notes = notes
            self.steps.append(record)

    def finish(self, *, passed: bool | None = None) -> Path:
        if self.run_dir is None:
            raise RuntimeError("Call begin() before finish()")

        outcome = "pass" if passed is not False else "fail"
        if passed is None:
            outcome = "pass" if all(s.assertion == "pass" for s in self.steps) else "fail"

        old = self.run_dir
        new_name = old.name.replace("_running", f"_{outcome}")
        self.run_dir = old.parent / new_name
        if old != self.run_dir:
            old.rename(self.run_dir)

        meta = {
            "uc": self.uc,
            "scr": self.scr,
            "nbde": self.nbde,
            "test_nodeid": self.test_nodeid,
            "outcome": outcome,
            "git_sha": _git_sha(),
            "finished_at": datetime.now(timezone.utc).isoformat(),
            "duration_ms": int((time.time() - self._started_at) * 1000),
            "steps": [asdict(s) for s in self.steps],
        }
        (self.run_dir / "steps.json").write_text(
            json.dumps(meta["steps"], ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        (self.run_dir / "report.json").write_text(
            json.dumps(meta, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        index = write_html_report(self.run_dir, meta)
        return index


def _slug(text: str, max_len: int = 40) -> str:
    import re

    s = re.sub(r"[^\w가-힣]+", "_", text.strip())[:max_len]
    return s.strip("_") or "step"


def _git_sha() -> str:
    try:
        out = subprocess.check_output(
            ["git", "rev-parse", "--short", "HEAD"],
            cwd=REPO_ROOT,
            stderr=subprocess.DEVNULL,
            text=True,
        )
        return out.strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return "unknown"


def _qt_available() -> bool:
    try:
        import PySide6  # noqa: F401

        return True
    except ImportError:
        return False


def _qt_ui_snapshot(widget: Any) -> dict[str, Any]:
    snap: dict[str, Any] = {"widget": type(widget).__name__}
    try:
        snap["window_title"] = widget.windowTitle()
        buttons = widget.findChildren(
            __import__("PySide6.QtWidgets", fromlist=["QAbstractButton"]).QAbstractButton
        )
        snap["button_labels"] = [b.text() for b in buttons if b.text()][:20]
    except Exception as exc:
        snap["snapshot_error"] = str(exc)
    return snap
