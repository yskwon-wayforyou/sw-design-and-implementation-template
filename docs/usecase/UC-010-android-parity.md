# UC-010 — Android 기능 패리티·승인 푸시


| 항목 | 내용 |
|------|------|
| TraceID | UC-010 |

| 우선순위 | P1 |

## 목적

Android 단말에서 macOS와 **동등한** 조회·주문·모드·AI 승인 기능을 제공한다.

## 아키텍처 옵션 (Phase 5~6에서 채택: 하이브리드 B)

| 옵션 | 설명 |
|------|------|
| A | Android WebView → 로컬 FastAPI(`ast_mobile`) |
| B | Android WebView + **동기 API**; 맥북 오프라인 시 제한 모드 |

**채택 방향**: v1은 **B** — 맥북이 `SyncHub` 호스트; 동일 LAN/VPN에서 REST+WebSocket.

## 기본 흐름

1. Android 앱 기동 → `SyncHub` 디스커버리(설정 URL).
2. JWT/페어링 토큰으로 세션.
3. UI: macOS와 동일 IA(반응형).
4. UC-006 승인 요청 → FCM/로컬 알림 → 승인/거부 API.
5. 주문·조회는 **맥북 경유 KIS** (키는 맥북 볼트에만).

## 대안

- 맥북 미가동: 읽기 전용 캐시 스냅샷 + “호스트 오프라인”.

## 비기능

- ASR-008; TLS(로컬 self-signed 또는 mTLS 후속)

## 추적

- [../doc/09-distribution-deliverables.md](../../doc/09-distribution-deliverables.md) FR-DEP-03
