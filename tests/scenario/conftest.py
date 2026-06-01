"""pytest fixtures for scenario tests with HTML reports."""

from __future__ import annotations

import pytest

from tests.scenario.support.session import ScenarioSession


@pytest.fixture
def scenario_session(request: pytest.FixtureRequest) -> ScenarioSession:
    session = ScenarioSession()
    yield session
    if session.run_dir is not None and session.run_dir.name.endswith("_running"):
        rep = getattr(request.node, "rep_call", None)
        passed = rep is not None and rep.passed
        index = session.finish(passed=passed)
        print(f"\n[scenario-report] file://{index}")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)
