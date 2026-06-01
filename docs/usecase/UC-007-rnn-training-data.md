# UC-007 — RNN 학습 데이터 수집·학습

| 항목 | 내용 |
|------|------|
| TraceID | UC-007 |
| 우선순위 | P1 |
| 액터 | Investor, MLPipeline, DataProvider |
| Flow 정본 | [DAT-002-rnn-training-collection-flow.md](../data/DAT-002-rnn-training-collection-flow.md) |

## 목적

개인 투자 패턴을 학습할 **시퀀스 데이터셋**을 수집·정제하고 RNN 모델을 학습·버전 관리한다.

## 데이터 소스 (Tier)

| Tier | 내용 | RNN 용도 | SRC (DAT-002) |
|------|------|----------|---------------|
| Tier1 | 1분봉 OHLCV·거래량·기술 피처 | 입력 **X** | KIS REST/WS, pykrx 백필 |
| Tier2 | paper API 스냅샷 | 분포 정렬·검증 | KIS paper |
| Tier3 | `order_request`, `ai_*`, GUI 스냅샷 | 라벨 **y** (BC) | EventStore + Parquet |

뉴스·공시(DART/RSS)는 **v1 RNN 미사용** — [DAT-001](../data/DAT-001-external-sources-catalog.md).

## 수집 흐름 (런타임) — 요약

1. UC-002/004/006 이벤트 → `FeatureSnapshotter.capture(symbol, ts)`.
2. `MarketSnapshotCache` 에서 60×1분 윈도우 조회; 미스 시 KIS 분봉 + pykrx 갭 보정.
3. KIS 잔고로 포지션·현금 비율 피처.
4. 라벨: 실제 BUY/SELL/HOLD (+ 선택 수락 가중치).
5. `~/.YSTrading/data/training_examples/YYYY-MM-DD.parquet` append + EventStore 메타.

상세 시퀀스: [DAT-002 §2](../data/DAT-002-rnn-training-collection-flow.md).

## Tier1 ETL (배치)

| Job | 주기 | 산출 |
|-----|------|------|
| `ingest_minute_bars.py` | 장중/장후 | `artifacts/datasets/bars_1m/` |
| `ingest_daily_ohlcv.py` | 1일 1회 | `artifacts/datasets/bars_1d/` |

## 학습 흐름 (오프라인)

1. `export_training_corpus` — Tier3 + bars 병합  
2. `build_sequences.py` — walk-forward split  
3. `train_rnn_personal.py` — LSTM BC  
4. `metadata.json`: `schema_version`, `data_hash`, `metrics`  
5. `artifacts/models/rnn_personal/{version}/`  
6. paper UC-006 백테스트 → live 승격 ([OPS-002](../operations/OPS-002-devops-mlops.md))

상세: [DAT-002 §4](../data/DAT-002-rnn-training-collection-flow.md).

## 라벨 정의 (v1)

- **BC**: 사용자 실제 BUY/SELL/HOLD at t  
- **보조**: 제안 수락=1, 거부=0 (가중치)

## 비기능

- ASR-006, ASR-007, NFR-04, QS-020  
- GUI는 torch/sklearn import 없음

## 모델 개요 (RNN)

```
Input: [batch, seq_len=60, feature_dim=F]
  F = returns, volume_z, position, time, cash_ratio, ...
RNN: LSTM(2 layers, hidden=128)
Head: 3-class BUY/SELL/HOLD
```

피처 목록: [DAT-002 §1](../data/DAT-002-rnn-training-collection-flow.md) · 도메인: [DOM-001](../domain/DOM-001-model.md) §ML

## 운영·MLOps

- [OPS-002](../operations/OPS-002-devops-mlops.md) · [OPS-001](../operations/OPS-001-github-cicd.md)
