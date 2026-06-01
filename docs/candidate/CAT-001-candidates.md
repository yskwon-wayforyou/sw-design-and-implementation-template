# 후보 구조 통합 목록

| 후보 ID | 관심사 | 문서 | 상충 |
|---------|--------|------|------|
| TraceID | CAT-001 |
| CA-PERF | 실시간 | [performance-realtime.md](CND-004-performance-realtime.md) | A vs B |
| CA-SEC | 안전·AI | [security-safety.md](CND-005-security-safety.md) | — |
| CA-ML | RNN | [ml-rnn-architecture.md](CND-003-ml-rnn-architecture.md) | A vs B |
| CA-AND | Android | [android-sync.md](CND-001-android-sync.md) | A vs B |
| CA-MOD | 모듈 | [layered-modularity.md](CND-002-layered-modularity.md) | A vs B |

## 상충 요약

| 상충 | 해결 방향 |
|------|-----------|
| REST vs WS | Desktop WS + REST fallback |
| GUI 비대 vs 신규 패키지 | `trading_modes` 신설 |
| Android 독립 vs SyncHub | SyncHub (키 로컬 단일) |

**다음**: [decision/evaluations.md](../decision/DEC-002-evaluations.md)
