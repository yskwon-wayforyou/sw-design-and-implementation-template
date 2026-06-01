# tests/

| TraceID | TST-IDX-000 |

테스트 정본: [TST-001](../docs/implementation/TST-001-testing-strategy.md) · 시나리오 HTML 리포트: [TST-002](../docs/implementation/TST-002-scenario-html-report.md)

```bash
pip install -e ".[dev]"

# Unit + integration
pytest tests/unit tests/integration -v

# UI scenario + HTML report (권장)
./scripts/run_scenario_with_report.sh tests/scenario

# 최신 리포트 열기 (macOS)
open "$(ls -td artifacts/test-reports/*/index.html | head -1)"
```

산출: `artifacts/test-reports/{run_id}/index.html` (스크린샷·단계별 분석 포함, Git 제외)
