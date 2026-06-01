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

| TraceID | 제목 | Tier | 용도 |
|---------|------|------|------|
| KIS-* | KIS REST/WS | A/B | 시세·주문·지수 |
| PYK-* | pykrx | C | 차트·RNN Tier1 백필 |
| DART-* | OpenDART | External | 공시 목록 |
| RSS-* | RSS 뉴스 | External | 헤드라인만 |
| ECOS-FX | 한국은행 (v1.1) | External | 환율 |

**정본 표**(엔드포인트·주기·키): [DAT-001-external-sources-catalog.md](../data/DAT-001-external-sources-catalog.md)

## 실패

- 원천 장애 시 마지막 good 스냅샷 + 회색 “지연/실패”

## 비기능

- ASR-001; 약관 준수 doc/08
