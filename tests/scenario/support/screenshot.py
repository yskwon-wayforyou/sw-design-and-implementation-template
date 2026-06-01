"""Capture Qt widgets as PNG for scenario reports."""

from __future__ import annotations

from pathlib import Path
from typing import Any


def capture_widget_png(widget: Any, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    try:
        from PySide6.QtCore import QSize
        from PySide6.QtGui import QImage
        from PySide6.QtWidgets import QApplication, QWidget

        if not isinstance(widget, QWidget):
            _write_placeholder(path, "not a QWidget")
            return

        app = QApplication.instance()
        if app is None:
            _write_placeholder(path, "no QApplication")
            return

        widget.grab().save(str(path))
        if path.stat().st_size < 100:
            _write_placeholder(path, "grab empty")
    except ImportError:
        _write_placeholder(path, "PySide6 not installed")
    except Exception as exc:
        _write_placeholder(path, f"capture error: {exc}")


def _write_placeholder(path: Path, message: str) -> None:
    try:
        from PIL import Image, ImageDraw

        img = Image.new("RGB", (640, 360), color=(240, 240, 240))
        draw = ImageDraw.Draw(img)
        draw.text((20, 160), message, fill=(80, 80, 80))
        img.save(path)
    except ImportError:
        path.write_bytes(b"")
