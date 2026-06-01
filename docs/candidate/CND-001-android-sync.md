# 후보 구조 — Android 동기 (QS-010, 012)


| 항목 | 내용 |
|------|------|
| TraceID | CND-001 |

## 후보 A: 독립 Android KIS 클라이언트

- 키가 모바일에 복제 → **보안 기각**

## 후보 B: WebView + SyncHub on macOS (채택 후보)

- FastAPI/Starlette `ast_mobile`
- LAN HTTPS, 페어링 토큰

## 후보 C: 클라우드 릴레이

- **기각**: 개인 프라이버시·비용

## 권고

- **B**: 기능 패리티; 호스트 오프라인 시 읽기 전용
