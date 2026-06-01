# ADR-003: trading_modes 패키지 신설

| 상태 | Accepted |
|------|----------|
| TraceID | ADR-003 |

## Context

Manual/Day/Long/AI 모드가 `gui_desktop`에 섞이면 유지보수성 저하.

## Decision

`packages/trading_modes/` Application 레이어에 모드별 로직·ApprovalGate·Orchestrator 배치.

## Options considered

1. GUI 비대 — 기각
2. **trading_modes** — 채택
3. MSA — 기각

## Consequences

- `gui_desktop`는 뷰·바인딩 위주 리팩터 *(superseded by [ADR-005](ADR-005-greenfield-ui-and-modes.md): `yst_ui` 신규)*
- 단계적 마이그레이션 *(superseded: 이전 없음)*

## Links

- [architecture/module.md](../architecture/ARC-001-module.md)
- [ARC-003](../architecture/ARC-003-trading-modes-greenfield.md)
