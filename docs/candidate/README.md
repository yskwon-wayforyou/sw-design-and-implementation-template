# 후보 구조 (Candidate) — 이해용 문서

## 이 폴더에서 답하는 질문

- 아키텍처 **대안**은 무엇이 있었고, 각각 어떻게 동작하는가?
- **왜** 하나를 채택하고 나머지를 기각했는가?
- 채택한 구조의 **단점**을 무엇으로, 어디서 보완하는가?

## 읽는 순서

1. [CAT-001-candidates.md](CAT-001-candidates.md) — 후보 목록·상충 요약
2. 관심사별 CND 문서 (아래) — 후보별 도식·설명
3. [CND-006-mitigation-adopted.md](CND-006-mitigation-adopted.md) — 채택 조합 보완 설계 통합표
4. [DEC-002-evaluations.md](../decision/DEC-002-evaluations.md) — 평가표
5. [DEC-001-decisions.md](../decision/DEC-001-decisions.md) — 최종 채택·기각

## 문서 목록

| TraceID | 파일 | 주제 |
|---------|------|------|
| CAT-001 | [CAT-001-candidates.md](CAT-001-candidates.md) | 통합 인덱스 |
| CND-001 | [CND-001-android-sync.md](CND-001-android-sync.md) | Android 동기 |
| CND-002 | [CND-002-layered-modularity.md](CND-002-layered-modularity.md) | 레이어·모듈 |
| CND-003 | [CND-003-ml-rnn-architecture.md](CND-003-ml-rnn-architecture.md) | ML RNN |
| CND-004 | [CND-004-performance-realtime.md](CND-004-performance-realtime.md) | 실시간 시세 |
| CND-005 | [CND-005-security-safety.md](CND-005-security-safety.md) | 보안·안전 |
| CND-006 | [CND-006-mitigation-adopted.md](CND-006-mitigation-adopted.md) | 채택 구조 단점 보완 |

## 관련 결정·아키텍처

- ADR: [ADR-001](../adr/ADR-001-android-synchub.md) ~ [ADR-009](../adr/ADR-009-commercial-quality-security-baseline.md)
- 횡단: [ARC-004](../architecture/ARC-004-resilience-security-crosscut.md)
