# UC-007 — RNN 학습 데이터 수집·학습


| 항목 | 내용 |
|------|------|
| TraceID | UC-007 |

| 우선순위 | P1 |
| 액터 | Investor, MLPipeline, DataProvider |

## 목적

개인 투자 패턴을 학습할 **시퀀스 데이터셋**을 수집·정제하고 RNN 모델을 학습·버전 관리한다.

## 데이터 소스 (Tier)

| Tier | 내용 | RNN 용도 |
|------|------|----------|
| Tier1 | OHLCV, 거래량, 기술지표 | 입력 시퀀스 X |
| Tier2 | paper API 스냅샷 | 분포 정렬 |
| Tier3 | `order_request`, GUI 컨텍스트, `ai_*` | 라벨 y (행동 복제) |

## 수집 흐름 (런타임)

1. UC-002/006 모든 주문·제안 시 `FeatureSnapshotter` 가 직전 윈도우(예: 60×분봉 + 포지션) 직렬화.
2. EventStore 또는 `training_examples` Parquet에 append.
3. PII·토큰 마스킹.

## 학습 흐름 (오프라인)

1. `export_training_corpus --from events --tier3` 
2. `build_sequences.py`: walk-forward split
3. `train_rnn_personal.py`: LSTM/GRU, 손실=행동 CE + (선택) PnL proxy
4. 메타데이터: `schema_version`, `data_hash`, `metrics.json`
5. `artifacts/models/rnn_personal/{version}/` 배포
6. paper에서 UC-006 백테스트 → live 승인 정책

## 라벨 정의 (v1)

- **BC(Behavior Cloning)**: 사용자 실제 매수/매도/홀드 at t
- **보조**: 제안 수락=1, 거부=0 (가중치)

## 비기능

- ASR-006, ASR-007, NFR-04
- GUI는 sklearn/torch import 없음

## 모델 개요 (RNN)

```
Input: [batch, seq_len, feature_dim]
  feature_dim = price_returns, volume_z, position_flag, time_of_day, ...
RNN: LSTM(2 layers, hidden=128)
Head: Dense → 3-class (BUY/SELL/HOLD)
```

상세: [domain/model.md](../domain/DOM-001-model.md) §ML

## 운영·MLOps

- 파이프라인·승격 게이트: [OPS-002-devops-mlops.md](../operations/OPS-002-devops-mlops.md)
- CI smoke: [OPS-001-github-cicd.md](../operations/OPS-001-github-cicd.md)
