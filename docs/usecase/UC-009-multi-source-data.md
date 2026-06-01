# UC-009 — 다원 시장 정보 수집·표시


| 항목 | 내용 |
|------|------|
| TraceID | UC-009 |

| 우선순위 | P1 |

## 목적

KIS 외 원천(지수, 환율, 뉴스, pykrx)을 **신뢰·실시간 정책**에 맞게 수집·캐시·UI에 표시한다.

## 기본 흐름

1. `DataSourceRegistry` 에 원천 등록(priority, tier, ttl).
2. `IngestScheduler` 폴링/ETL.
3. `MarketSnapshotCache` 갱신.
4. UI: 출처·수집시각·Tier 배지.

## 원천 (v1)

| 원천 | Tier | 용도 |
|------|------|------|
| KIS REST/WS | A/B | 시세·주문 |
| pykrx | C | 차트·장기 피처 |
| 공개 지수 API | External | 현황 |
| DART/뉴스 | External | 링크·헤드라인 |

## 실패

- 원천 장애 시 마지막 good 스냅샷 + 회색 “지연/실패”

## 비기능

- ASR-001; 약관 준수 doc/08
