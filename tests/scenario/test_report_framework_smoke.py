"""Smoke test for scenario HTML report framework (no yst_ui required)."""

from __future__ import annotations

import pytest

try:
    from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget
except ImportError:
    QWidget = None  # type: ignore


pytestmark = [pytest.mark.scenario, pytest.mark.normal]


@pytest.mark.skipif(QWidget is None, reason="PySide6 required for scenario screenshot smoke")
def test_scenario_report_smoke(scenario_session, qtbot):
    """Validates step recording, screenshot, analysis, and index.html generation."""
    scenario_session.begin(
        uc="UC-SMOKE",
        scr="SCR-SMOKE",
        nbde="N",
        test_nodeid="test_report_framework_smoke",
    )

    window = QWidget()
    layout = QVBoxLayout(window)
    banner = QLabel("모의투자")
    banner.setObjectName("paper_live_banner")
    layout.addWidget(banner)
    window.setWindowTitle("YSTrading Smoke")
    window.resize(480, 320)
    window.show()
    qtbot.addWidget(window)

    def _check_banner() -> None:
        assert "모의투자" in banner.text()

    scenario_session.step(
        title="1. 모의투자 배너 표시",
        expectation="화면에 모의투자 문구",
        capture_widget=window,
        action=_check_banner,
    )

    def _check_title() -> None:
        assert "Smoke" in window.windowTitle()

    scenario_session.step(
        title="2. 창 제목 확인",
        expectation="YSTrading Smoke",
        capture_widget=window,
        action=_check_title,
    )

    scenario_session.finish(passed=True)
