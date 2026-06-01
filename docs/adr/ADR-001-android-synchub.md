# ADR-001: Android 동기 — SyncHub on macOS

| 상태 | Accepted (Phase 6) |
|------|---------------------|
| TraceID | ADR-001 |
| 날짜 | 2026-06-01 |

## Context

Android에서 macOS와 동등 기능·AI 승인 필요. KIS 키를 모바일에 두고 싶지 않음.

## Decision

Android WebView → LAN `ast_mobile` SyncHub → macOS `trading_modes`/`kis_core`.

> **개인 배포(2026-06)**: Android에 **암호화된 KIS 자격증명**을 APK에 포함해 **폰 단독 API**도 허용 — [ADR-006](ADR-006-personal-credentials-encryption.md). SyncHub는 **선택** 동기 경로.

## Options considered

1. **독립 Android KIS** — 상용안에서는 기각; **개인 앱**에서는 ADR-006으로 암호화 내장 허용
2. **SyncHub (채택)**
3. **클라우드 릴레이** — 기각(프라이버시)

## Consequences

- 맥북 오프라인 시 Android 제한 모드
- 페어링·토큰 보안 구현 필요

## Links

- UC-010, [architecture/deployment.md](../architecture/ARC-002-deployment.md)
