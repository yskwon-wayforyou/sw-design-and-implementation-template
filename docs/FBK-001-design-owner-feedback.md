# 오너 설계 피드백 확정

| 일자 | 2026-06-02 |
|------|------------|
| TraceID | FBK-001 |
| 상태 | Phase 6 보강 반영 |

---

## 확정 항목

| # | 주제 | 결정 |
|---|------|------|
| **1** | Android **SyncHub on macOS** | **동의** — [ADR-001](adr/ADR-001-android-synchub.md) 유지 |
| **2** | AI **무승인 자동** | **설정 On/Off 가능**, **기본 Off**. On일 때만 ApprovalGate 생략 → RiskGuard·OrderService. Off(기본)는 승인 필수 |
| **3** | 단타 v1 **휴리스틱** (`IntradayPatternAnalyzer`) | **괜찮음** — D-07 확정 |

## 그린필드 반영 (2026-06-02)

| # | 주제 | 결정 |
|---|------|------|
| **4** | `trading_modes` 범위 | PoC GUI **이전 없음**; `trading_modes` + `yst_ui` **신규** — [ADR-005](adr/ADR-005-greenfield-ui-and-modes.md) |
| **5** | 누락 UC/화면 | MVP 화면 **SCR-* 전량** 콘티 — [ui/UI-003](ui/UI-003-storyboards-system-android.md) |
| **6** | UI 용어 | 화면은 **일반 사용자 한글만** — [UI-004](../ui/UI-004-plain-language-and-labels.md) |
| **7** | Look & Feel | **Cursor Light** — [UI-005](../ui/UI-005-cursor-light-theme.md) |
| **8** | KIS 키 | 오너 제공 → **암호화**; Android **APK 포함** (개인 단독) — [ADR-006](../adr/ADR-006-personal-credentials-encryption.md) |
| **9** | O-01 SyncHub | **LAN + 페어링 토큰** (권장안 확정) — [ADR-007](../adr/ADR-007-connectivity-and-shared-math-v1.md) |
| **10** | O-02 알림 | **15초 폴링 + 로컬 알림** — [ADR-007](../adr/ADR-007-connectivity-and-shared-math-v1.md) |
| **11** | O-03 수학 모듈 | **`trading_modes/shared/`** — [ADR-007](../adr/ADR-007-connectivity-and-shared-math-v1.md) |

---

## 설정 키 (구현 스펙)

`gui_settings.json` (schema ≥ 5 권장):

| 키 | 타입 | 기본값 | 설명 |
|----|------|--------|------|
| `ai_auto_without_approval` | bool | **`false`** | `true`: AI BUY/SELL 시 승인 단계 생략 |
| `ai_approval_ttl_sec` | int | `60` | 승인 대기 만료(초); 무승인 Off일 때만 적용 |

**UI (화면 문구)**: **설정 → 자동 매매** — 「**승인 없이 자동 주문**」 토글, 기본 **끔** ([UI-004](../ui/UI-004-plain-language-and-labels.md)).

**live 추가**: `ai_auto_without_approval=true` 저장 시 **1회 경고 확인** + EventStore `ai_policy_change` 기록. `live` 주문은 UC-011 RiskGuard(확인 대화상자) **유지**.

---

## 추적

- UC-006, ASR-004, [ADR-004](adr/ADR-004-ai-auto-without-approval-setting.md)
- [decision/decisions.md](decision/DEC-001-decisions.md) D-02, D-05, D-07
