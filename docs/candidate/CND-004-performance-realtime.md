# 후보 구조 — 성능·실시간 (QS-001)


| 항목 | 내용 |
|------|------|
| TraceID | CND-004 |

## 후보 A: REST 폴링만

- **구조**: `QuotePoller` 3s 주기 → `MarketSnapshotCache`
- **장점**: 단순, WS 인증 부담 없음
- **단점**: 지연·한도 소모

## 후보 B: KIS WebSocket + REST 폴백

- **구조**: `WsSubscriptionManager` + 실패 시 폴링
- **장점**: 저지연
- **단점**: 연결 관리·재연결 복잡

## 후보 C: 로컬 캐시 + 델타 푸시(SyncHub)

- macOS가 WS 수신 → Android에 델타 전파
- **장점**: Android 실시간 동기
- **단점**: 맥북 의존

## 권고 (Phase 6 입력)

- v1: **B for desktop**, Android는 **C** via SyncHub
- HTS급 틱 미보장은 문서화 유지
