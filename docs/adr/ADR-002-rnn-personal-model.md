# ADR-002: 개인화 RNN (LSTM BC)

| 상태 | Accepted |
|------|----------|
| TraceID | ADR-002 |

## Context

AI 모드가 개인 매매 패턴 학습·승인 후 실행 필요.

## Decision

- **모델**: 2-layer LSTM, 3-class BC (BUY/SELL/HOLD)
- **데이터**: Tier1 OHLCV + Tier3 행동 라벨, walk-forward
- **배포**: `artifacts/models/rnn_personal/{version}/`
- **실행**: `AiTradingAddon` → `ApprovalGate` (**기본**; `ai_auto_without_approval=true` 시 생략 — [ADR-004](ADR-004-ai-auto-without-approval-setting.md))

## Options considered

1. LSTM BC — **채택**
2. Transformer — 기각 v1
3. FinRL — 후속

## Consequences

- 수익 보장 없음; paper 검증 필수
- `FeatureSnapshotter`·export 파이프라인 구현 필요

## Links

- UC-006, UC-007, [candidate/ml-rnn-architecture.md](../candidate/CND-003-ml-rnn-architecture.md)
