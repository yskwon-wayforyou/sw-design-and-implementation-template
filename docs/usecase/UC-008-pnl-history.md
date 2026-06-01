# UC-008 — 손익·투자·매매 이력 관리


| 항목 | 내용 |
|------|------|
| TraceID | UC-008 |

| 우선순위 | P0 |

## 목적

주문·체결·보유·실현/평가 손익을 기간별로 조회·export 한다.

## 기본 흐름

1. `거래·손익` 탭: 기간 필터(당일/주/월/사용자).
2. `HistoryAggregator` 가 KIS 체결 TR + EventStore 교차.
3. 표: 일시, 종목, 매매, 수량, 가격, 수수료(가능 시), 손익.
4. KPI: 실현손익, 평가손익, 승률(정의 명시).
5. JSONL/CSV export.

## 데이터 원천

| 항목 | 원천 |
|------|------|
| 체결 | KIS `daily_ccld` 등 TR |
| 주문 시도 | EventStore |
| AI/단타 제안 | EventStore `daytrade_suggestion`, `ai_proposal` |

## 대안

- KIS TR 미구현 필드: “—” + Tier 배지

## 비기능

- ASR-006; correlation_id로 주문↔승인↔체결 추적

## 추적

- SCR-HISTORY, FR-EXT-02
