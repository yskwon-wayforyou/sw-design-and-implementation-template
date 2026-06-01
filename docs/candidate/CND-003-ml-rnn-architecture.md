# 후보 구조 — ML RNN (QS-008, 011)


| 항목 | 내용 |
|------|------|
| TraceID | CND-003 |

## 후보 A: LSTM 2-layer BC (채택 후보)

- PyTorch, `ml_pipeline/rnn/`
- 입력: 60×F 분봉 윈도우
- 출력: 3-class

## 후보 B: Transformer 시퀀스

- **단점**: 데이터 적을 때 과적합; 설명 어려움

## 후보 C: FinRL RL 에이전트

- doc/04 로드맵; v1 BC 후 RL

## 데이터 수집 후보

| ID | 방식 |
|----|------|
| D1 | EventStore only Tier3 |
| D2 | Tier1+Tier3 Parquet (채택) |
| D3 | 실시간 스트림 학습 | 기각(복잡) |

## 권고

- **A + D2**; walk-forward; paper 검증 후 live
