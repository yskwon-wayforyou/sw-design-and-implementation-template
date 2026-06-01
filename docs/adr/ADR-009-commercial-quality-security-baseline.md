# ADR-009: 상용급 품질·보안 기준선 (SRE · Defense-in-Depth)

| 상태 | Accepted |
|------|----------|
| TraceID | ADR-009 |
| 날짜 | 2026-06-02 |
| 관련 | [QLT-002](../QLT-002-commercial-quality-baseline.md), [SEC-001](../security/SEC-001-threat-model-and-controls.md), [REL-001](../reliability/REL-001-slo-resilience-patterns.md), [ARC-004](../architecture/ARC-004-resilience-security-crosscut.md) |

## Context

YSTrading은 개인용이지만 **실계좌 금전 거래**·**AI 자동화**·**LAN SyncHub**·**Android 키 내장**으로 인해 HTS에 준하는 **안전·신뢰·보안** 기대가 있다. 기존 QS/ASR은 v0.1 수준으로 **복원력·멱등·감사·위협 대응·SLO**가 분산·미흡하다.

## Decision drivers

| 우선순위 | 목표 |
|----------|------|
| 1 | 금전 손실·오주문 **불가능에 가깝게** |
| 2 | 장애 시 **예측 가능한 저하**(degraded) |
| 3 | 사고 **추적·감사** 가능 |
| 4 | 솔로 개발 **유지 가능**한 범위 |

## Options considered

### 1. 기존 RiskGuard + ASR만 확장 (채택 기반)

- 문서·패턴 표준화([QLT-002](../QLT-002-commercial-quality-baseline.md), [ARC-004](../architecture/ARC-004-resilience-security-crosscut.md)).
- **채택**.

### 2. 마이크로서비스 + 중앙 정책(O PA/K8s)

- 개인 앱 규모 대비 과함 — **기각** ([DEC-001](../decision/DEC-001-decisions.md) X-04).

### 3. 외부 SRE SaaS(Datadog/Sentry) 필수

- v1 비용·복잡 — **보류**; 구조화 로그·로컬 메트릭 우선, SaaS는 로드맵.

## Decision

| 영역 | v1 결정 |
|------|---------|
| **신뢰성** | KIS **Circuit Breaker**, 지수 백오프, **멱등 주문 ID**, WS↓→REST 폴백, SQLite **WAL+백업** |
| **안정성** | 호출 **타임아웃 예산**, 프로세스 **헬스/워치독**, 크래시 후 EventStore **정합 재검** |
| **보안** | **Defense-in-Depth**: 암호화 저장 + Hub **세션 토큰** + 감사 로그 + CI live 금지 + 공급망 **lock/SBOM** |
| **AI** | stale 시세·저신뢰 시 **주문 차단**; 데이터 `data_hash` 무결성 |
| **SLO** | [REL-001](../reliability/REL-001-slo-resilience-patterns.md) — 로컬 경로 기준 |
| **검증** | QS-013~020, ASR-015~022, Phase 8 체크리스트 |

## Consequences

- 구현 범위 증가 — **kis_core**, **OrderService**, **SyncHub**, **event_store** 우선.
- 상용 HTS 100% 패리티는 **비목표**; 금전·감사·복원력은 **동등 의도**.

## Links

- [UC-011](../usecase/UC-011-risk-guard.md), [OPS-002](../operations/OPS-002-devops-mlops.md)
