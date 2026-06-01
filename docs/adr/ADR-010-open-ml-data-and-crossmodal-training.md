# ADR-010: 오픈 ML·Tier0·크로스모달 학습 (SRV-001 피드백 반영)

| 상태 | Accepted |
|------|----------|
| TraceID | ADR-010 |
| 날짜 | 2026-06-02 |
| 근거 | [SRV-001](../survey/SRV-001-open-ml-models-and-data-survey.md) 오너 피드백 §7 |

## Context

오픈 모델·데이터 서베이 후 오너가 v1 유지, Tier0·Alpha158류 피처, v2 FinGPT/Chronos, 백테스트 절차, DART/RSS↔KIS 연관 학습을 확정했다.

## Decision

| # | 오너 응답 | 결정 |
|---|-----------|------|
| 1 | 동의 | **v1 LSTM BC + Tier1/3 유지** ([ADR-002](ADR-002-rnn-personal-model.md)) |
| 2 | 응 | **Tier0** 일봉 백필(pykrx·FDR) — [DAT-003](../data/DAT-003-data-schemas.md) |
| 3 | 반영 | **Alpha158류 피처** — `trading_modes/shared/features_alpha.py` ([DAT-003](../data/DAT-003-data-schemas.md) §TrainingFeature) |
| 4 | v2 | **FinGPT 감성** 배치 — v2만; v1.5는 **구조적 크로스모달**만 |
| 5 | 포함 | **Chronos/TimesFM** — v2 `ml_pipeline/tsfm/` 보조 Addon |
| 6 | 넣음 | **백테스트 절차** — [OPS-005](../operations/OPS-005-backtest-procedure.md) |
| 7 | DART/RSS↔KIS | **시간 정렬 조인** + v2 FinGPT `sentiment_score` → RNN 피처; v1.5 `crossmodal_*` 플래그 |

### 크로스모달 학습 (요약)

- 스냅샷 시각 `t`, 종목 `symbol` 기준:
  - **KIS**: 분봉·포지션 (Tier1)
  - **DART**: `t-24h..t` 공시 건수·최근 `rcept_dt` 거리
  - **RSS**: 동일 창 헤드라인 건수 (본문 미저장)
  - **v2 FinGPT**: 헤드라인 배치 감성 → `sentiment_mean_24h`, `sentiment_last`
- **누수 방지**: `t` 이후 공시·뉴스 **조인 금지** (ASR-007)

## Options considered

1. FinGPT v1 즉시 — **기각** (GPU·라이선스·v2로)
2. Tier0 없이 KIS만 — **기각** (콜드스타트 약함)
3. 본 ADR 조합 — **채택**

## Consequences

- DAT-002·DAT-003·schema_version `2` 추가
- `ingest_daily_tier0.py`, `join_crossmodal.py` ETL
- v2 ADR 별도로 FinGPT 모델 ID 고정

## Links

- [PLAN-001](../implementation/PLAN-001-implementation-schedule.md)
- [TST-001](../implementation/TST-001-testing-strategy.md)
