# ADR-005: 그린필드 UI(yst_ui) 및 trading_modes 재설계

| 상태 | Accepted |
|------|----------|
| TraceID | ADR-005 |
| 날짜 | 2026-06-02 |

## Context

- PoC 과제에서 **요구사항·품질 속성·KIS 연동**만 계승하고, **화면·매매 모드 구현은 처음부터** 다시 만든다.
- 기존 `gui_desktop`는 PoC 산출물이며 **재사용·점진 이전 대상이 아니다** (오너 방향).
- [ADR-003](ADR-003-trading-modes-package.md)은 `trading_modes` 신설을 채택했으나, GUI를 `gui_desktop` 리팩터 전제로 두었다.

## Decision

1. **Presentation**: 신규 패키지 **`yst_ui`** (PySide6). `gui_desktop` import **금지**.
2. **Application**: **`trading_modes`** 를 포트·도메인·모드 서비스로 **신규 구현** (PoC 모드 로직 이전 없음).
3. **Infrastructure**: `kis_core`, `event_store`, `ml_pipeline`, `data_ingestion` 는 **어댑터로만** 연결.
4. **UI 설계 정본**: [docs/ui/](../ui/) 콘티(UI-000~003); 구현은 콘티와 **화면 ID(SCR-*)** 로 추적.
5. **오너 피드백 #4·#5**:
   - #4 `trading_modes` 범위 → **신규 패키지 전체**; PoC GUI 리팩터 **없음** (O-04 close).
   - #5 누락 화면 → UI-003 §「화면 목록」MVP 22건 정의 (O-05 close for MVP).

## Options considered

1. **PoC `gui_desktop` 점진 리팩터** — 기각(오너: 전면 재설계).
2. **yst_ui + trading_modes 그린필드** — **채택**.
3. **웹 UI(Electron/Tauri) 전환** — 기각(v1: PySide6·맥북 우선, Android SyncHub).

## Consequences

### Positive

- 모드·승인·Tier 표시가 처음부터 일관된 UX.
- `trading_modes` 테스트가 Qt 없이 가능.
- PoC와 설계 문서 추적이 분리됨.

### Negative

- 초기 구현량 증가(화면 전량 신규).
- PoC와 **병행 실행 불가**(동일 진입점 하나만).

### Neutral

- ADR-003은 **부분 supersede** — `trading_modes` 채택은 유지, GUI 전제만 본 ADR로 대체.
- ARC-001 §5 GUI 매핑 표는 **역사 참고**; 정본은 ARC-003 + ui/.

## Compliance

| ASR | 대응 |
|-----|------|
| ASR-001 | `tier_footer` 위젯 공통 |
| ASR-004 | SCR-SETTINGS + SCR-MODE-AI 정책 UI |
| ASR-005 | 제안 카드·SCR-APPROVAL 근거 패널 |
| ASR-009 | `OrderPort` 단일 실행 경로 |

## Links

- [ARC-003-trading-modes-greenfield.md](../architecture/ARC-003-trading-modes-greenfield.md)
- [UI-000-greenfield-principles.md](../ui/UI-000-greenfield-principles.md)
- [FBK-001-design-owner-feedback.md](../FBK-001-design-owner-feedback.md)
