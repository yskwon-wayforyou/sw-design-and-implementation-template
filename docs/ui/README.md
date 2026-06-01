# UI 설계 (그린필드) — YSTrading

| TraceID | UI-IDX-000 |
|---------|----------------|

## 이 폴더에서 답하는 질문

- PoC의 **요구사항만** 가져오고, **기존 `gui_desktop`는 쓰지 않을 때** 화면은 어떻게 구성하는가?
- 매매 모드(Manual·Day·Long·AI)마다 **무엇이 보이고**, 사용자가 **어떤 순서로** 행동하는가?
- 구현 전에 **모든 화면 콘티**로 이해할 수 있는가?

## 전제 (오너 확정 방향)

| 항목 | 결정 |
|------|------|
| PoC 코드 | **요구·품질·KIS 연동 지식만** 참조; UI·모드 로직 **재사용 안 함** |
| Presentation | 신규 패키지 **`yst_ui`** (PySide6), `gui_desktop` **미의존** |
| Application | **`trading_modes`** 완전 재설계 — [ARC-003-trading-modes-greenfield.md](../architecture/ARC-003-trading-modes-greenfield.md) |
| 시각 스타일 | **[Cursor Light](UI-005-cursor-light-theme.md)**; 모의/실전 **색·배너** |
| 화면 용어 | **[일반 사용자용 라벨만](UI-004-plain-language-and-labels.md)** |
| 자격증명 | **[암호화·Android 내장](ADR-006-personal-credentials-encryption.md)** (개인 전용) |

## 읽는 순서

1. [UI-000-greenfield-principles.md](./UI-000-greenfield-principles.md) — IA·내비·디자인 원칙
2. [UI-QT6-layout-conventions.md](./UI-QT6-layout-conventions.md) — **PySide6 위젯 트리 정본**
3. [UI-001-storyboards-shell-common.md](./UI-001-storyboards-shell-common.md) — 셸·온보딩·공통 HTS
4. [UI-002-storyboards-trading-modes.md](./UI-002-storyboards-trading-modes.md) — 4매매 모드
5. [UI-003-storyboards-system-android.md](./UI-003-storyboards-system-android.md) — 설정·승인·Android·예외
6. [UI-004-plain-language-and-labels.md](./UI-004-plain-language-and-labels.md) — 화면 한글 용어
7. [UI-005-cursor-light-theme.md](./UI-005-cursor-light-theme.md) — Cursor Light QPalette
8. O-01~03 확정: [ADR-007](../adr/ADR-007-connectivity-and-shared-math-v1.md) (배경 설명 [DEC-003](../decision/DEC-003-open-issues-guide.md))

## 관련 설계

- [ARC-003-trading-modes-greenfield.md](../architecture/ARC-003-trading-modes-greenfield.md)
- [ADR-005-greenfield-ui-and-modes.md](../adr/ADR-005-greenfield-ui-and-modes.md)
- UC·모드 정의: [SYS-001-system.md](../SYS-001-system.md) §4
