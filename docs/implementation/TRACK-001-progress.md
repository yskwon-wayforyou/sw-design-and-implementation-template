# TRACK-001 — 구현 진행 체크리스트

| 항목 | 내용 |
|------|------|
| TraceID | TRACK-001 |
| 버전 | 0.1 |
| 계획 | [PLAN-001-implementation-schedule.md](PLAN-001-implementation-schedule.md) |
| **갱신 방법** | 구현 착수·완료 시 **본 파일만** 상태·날짜·비고·커밋 갱신 |

## 상태 값

| 상태 | 의미 |
|------|------|
| `todo` | 미착수 |
| `in_progress` | 작업 중 |
| `blocked` | 막힘 (비고에 이유) |
| `done` | 구현·테스트 완료 |
| `verified` | CI·시나리오 통과 확인 |

---

## 요약 대시보드

| 마일스톤 | 목표일 | 완료 | 진행 | blocked | todo |
|----------|--------|------|------|---------|------|
| M0 | 2026-06-09 | 0 | 0 | 0 | 5 |
| M1 | 2026-06-30 | 0 | 0 | 0 | 7 |
| M2 | 2026-07-21 | 0 | 0 | 0 | 5 |
| M3 | 2026-08-11 | 0 | 0 | 0 | 7 |
| M1.5 | — | 0 | 0 | 0 | 2 |
| M4 | 2026-09-01 | 0 | 0 | 0 | 7 |
| M5 | 2026-09-22 | 0 | 0 | 0 | 9 |
| v2 | 2026-11+ | 0 | 0 | 0 | 3 |

*위 숫자는 구현 시작 시 수동 갱신.*

---

## Phase 0 — M0

| ID | 작업 | 상태 | 시작 | 완료 | 커밋/PR | 테스트 | 비고 |
|----|------|------|------|------|---------|--------|------|
| P0-01 | pyproject·pytest | todo | | | | | |
| P0-02 | yst_logging | todo | | | | | |
| P0-03 | config·migrate | todo | | | | | |
| P0-04 | GHA ci.yml | todo | | | | | |
| P0-05 | tests/ 트리 | done | 2026-06-02 | 2026-06-02 | | scenario+report | TST-002 |

---

## Phase 1 — M1

| ID | 작업 | 상태 | 시작 | 완료 | 커밋/PR | 테스트 | 비고 |
|----|------|------|------|------|---------|--------|------|
| P1-01 | kis OAuth·REST | todo | | | | unit+kis | |
| P1-02 | CircuitBreaker | todo | | | | N/A/E | |
| P1-03 | WS 폴백 | todo | | | | integration | |
| P1-04 | EventStore | todo | | | | unit | |
| P1-05 | RiskGuard | todo | | | | unit NBDE | |
| P1-06 | OrderService | todo | | | | unit+scenario | |
| P1-07 | MarketSnapshotCache | todo | | | | boundary | |

---

## Phase 2 — M2

| ID | 작업 | 상태 | 시작 | 완료 | 커밋/PR | 테스트 | 비고 |
|----|------|------|------|------|---------|--------|------|
| P2-01 | shell·mode rail | todo | | | | scenario | |
| P2-02 | 프로필 paper/live | todo | | | | UC-001 | |
| P2-03 | SCR-ORDER | todo | | | | UC-002 | |
| P2-04 | SCR-HOME | todo | | | | UC-003 | |
| P2-05 | TierFooter | todo | | | | | |

---

## Phase 3 — M3 + M1.5

| ID | 작업 | 상태 | 시작 | 완료 | 커밋/PR | 테스트 | 비고 |
|----|------|------|------|------|---------|--------|------|
| P3-01 | Tier0 ETL | todo | | | | DAT-003 | ADR-010 #2 |
| P3-02 | Tier1 minute | todo | | | | | |
| P3-03 | DART/RSS | todo | | | | UC-012 | |
| P3-04 | CrossmodalJoiner | todo | | | | leak test | ADR-010 #7 |
| P3-05 | Daytrade | todo | | | | UC-004 | |
| P3-06 | Longterm | todo | | | | UC-005 | |
| P3-07 | features_alpha | todo | | | | | ADR-010 #3 |

---

## Phase 4 — M4

| ID | 작업 | 상태 | 시작 | 완료 | 커밋/PR | 테스트 | 비고 |
|----|------|------|------|------|---------|--------|------|
| P4-01 | FeatureSnapshotter | todo | | | | UC-007 | |
| P4-02 | export·sequences | todo | | | | walk-forward | |
| P4-03 | train_rnn | todo | | | | smoke | ADR-002 |
| P4-04 | ApprovalGate | todo | | | | UC-006 scen | |
| P4-05 | AiAddon | todo | | | | | |
| P4-06 | backtest OPS-005 | todo | | | | BT-01~03 | #6 |
| P4-07 | AI UI | todo | | | | scenario | |

---

## Phase 5 — M5

| ID | 작업 | 상태 | 시작 | 완료 | 커밋/PR | 테스트 | 비고 |
|----|------|------|------|------|---------|--------|------|
| P5-01 | Hub pair | todo | | | | | |
| P5-02 | approvals API | todo | | | | | |
| P5-03 | quote delta | todo | | | | | |
| P5-04 | Android | todo | | | | UC-010 | |
| P5-05 | diagnostic pack | todo | | | | | |
| P5-06 | nl_command | todo | | | | UC-013 | ADR-011 |
| P5-07 | Hub nl API | todo | | | | | |
| P5-08 | Android voice UI | todo | | | | scenario | |
| P5-09 | TTS confirm | todo | | | | optional | |

---

## Phase v2

| ID | 작업 | 상태 | 시작 | 완료 | 커밋/PR | 테스트 | 비고 |
|----|------|------|------|------|---------|--------|------|
| V2-01 | FinGPT batch | todo | | | | | #4 |
| V2-02 | Chronos Addon | todo | | | | | #5 |
| V2-03 | corpus v2 full | todo | | | | | sentiment join |

---

## 주간 로그 (선택)

| 주 (월요일) | 완료 ID | 메모 |
|-------------|---------|------|
| 2026-06-02 | — | 설계·TRACK 초기화 |

---

## 변경 이력

| 날짜 | 내용 |
|------|------|
| 2026-06-02 | v0.1 — 전 태스크 todo |
