# 구현·테스트·진행 (`docs/implementation/`)

| TraceID | IMPL-IDX-001 |

Phase 7 이후 **구현 정본**. 설계 변경은 ADR·DAT 선행.

## 읽는 순서

1. [INT-001-module-interfaces.md](INT-001-module-interfaces.md) — 모듈 포트·DTO
2. [DAT-003-data-schemas.md](../data/DAT-003-data-schemas.md) — 스키마
3. [PLAN-001-implementation-schedule.md](PLAN-001-implementation-schedule.md) — 일정·마일스톤
4. [TST-001-testing-strategy.md](TST-001-testing-strategy.md) — TDD·pytest·시나리오 테스트
5. [TST-002-scenario-html-report.md](TST-002-scenario-html-report.md) — 시나리오 HTML 리포트·스크린샷
6. **[TRACK-001-progress.md](TRACK-001-progress.md)** — **작업 상태 갱신 (구현 시 여기 기록)**

## 규칙

- 구현은 **TDD** — [.cursor/rules/tdd-implementation.mdc](../../.cursor/rules/tdd-implementation.mdc)
- 태스크 완료 시 `TRACK-001` 상태·날짜·PR/커밋 갱신

| TraceID | 문서 |
|---------|------|
| INT-001 | 모듈 인터페이스 |
| PLAN-001 | 구현 계획·일정 |
| TRACK-001 | 진행 체크리스트 |
| TST-001 | 테스트 전략 |
| TST-002 | 시나리오 HTML 리포트 |
