# ADR-007: 연동·알림·공통 수학 v1 확정 (O-01~03)

| 상태 | Accepted |
|------|----------|
| TraceID | ADR-007 |
| 날짜 | 2026-06-02 |
| 근거 | 오너: 미결 O-01~03 **에이전트 권장안 전부 적용** |

## Context

[DEC-003](../decision/DEC-003-open-issues-guide.md)에서 설명한 O-01·O-02·O-03. 오너 검토 후 **v1 권장안**으로 확정.

## Decision

| ID | 결정 | 요약 |
|----|------|------|
| **O-01** | **LAN + 페어링 토큰** | SyncHub: QR/6자리 코드, `X-Session-Token`, 60s 갱신 가능. mTLS는 v2 |
| **O-02** | **로컬 알림 + 폴링** | Android `GET /approvals/pending` **15초** 주기; `NotificationCompat`. FCM은 설정 Off·v2 |
| **O-03** | **`trading_modes/shared/`** | `indicators.py`, `normalize.py` 등 소규모. 별도 `yst_analytics` 패키지는 v2 |

### O-01 구현 힌트

| 항목 | 값 |
|------|-----|
| 페어링 | `POST /pair` body `{ "code": "482910" }` |
| 세션 | 응답 `session_token`, 이후 헤더 `X-Session-Token` |
| 바인딩 | SyncHub **LAN only** `0.0.0.0:8765` (설정에서 변경) |
| UI | [UI-003](../ui/UI-003-storyboards-system-android.md) SCR-AND-PAIR |

> [ADR-006](ADR-006-personal-credentials-encryption.md)으로 Android **KIS 직접 호출**도 가능. SyncHub는 **맥북 연동·승인 보조** 경로.

### O-02 구현 힌트

| 항목 | 값 |
|------|-----|
| 폴링 주기 | 15s (백그라운드 `WorkManager` / foreground service) |
| 알림 채널 | `ai_approval` — 「매매 승인 요청」 |
| payload | 종목·방향만; 상세는 앱 열어 조회 |
| 설정 | `android_use_fcm` default **false** |

### O-03 구현 힌트

```text
trading_modes/
  shared/
    indicators.py    # MA, RSI helpers
    normalize.py
  daytrade/          # imports shared
  longterm/
```

## Options considered

각 항목의 대안은 [DEC-003](../decision/DEC-003-open-issues-guide.md) 참조. **권장안(A)** 전부 채택.

## Consequences

- Phase 7 구현 시 O-01~03 **재논의 불필요**
- mTLS·FCM·`yst_analytics`는 로드맵 **v2** ADR로 분리

## Links

- [DEC-001](../decision/DEC-001-decisions.md) D-09~D-11
- [ARC-003](../architecture/ARC-003-trading-modes-greenfield.md)
