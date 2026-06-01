# ADR-004: AI 무승인 자동 — 설정 On/Off (기본 Off)

| 상태 | Accepted (오너 피드백) |
|------|------------------------|
| TraceID | ADR-004 |
| 날짜 | 2026-06-02 |

## Context

AI 모드에서 매매 직전 승인은 기본이나, 사용자가 원할 때 승인 없이 자동 실행도 필요하다.

## Decision

- 설정 `ai_auto_without_approval` (**bool**, **`false` 기본**).
- **Off (기본)**: `ApprovalGate` 필수 → 승인 후 `RiskGuard` → `OrderService`.
- **On**: `ApprovalGate` 생략 → 즉시 `RiskGuard` → `OrderService`; `live`는 RiskGuard 확인 UI 유지.
- On으로 변경 시 1회 경고 + 감사 이벤트.

## Options considered

1. **설정 On/Off, 기본 Off** — **채택** (오너)
2. live에서 무승인 완전 금지 — 기각 (오너: 설정으로 허용)
3. 무승인 항상 허용 — 기각 (안전)

## Consequences

- QS-004·ASR-004 테스트는 **기본값 Off** 기준 유지; On 경로 별도 테스트.
- SyncHub·Android에서 동일 설정 동기화 필요(UC-010).

## Links

- [design-owner-feedback.md](../FBK-001-design-owner-feedback.md), UC-006
