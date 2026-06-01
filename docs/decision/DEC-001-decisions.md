# 채택·기각 설계 결정 (Phase 6.2)


| 항목 | 내용 |
|------|------|
| TraceID | DEC-001 |

| 버전 | 0.4 (CI/CD·DevOps·MLOps) |

---

## 채택

| ID | 결정 | ADR |
|----|------|-----|
| D-01 | Desktop 시세: **KIS WebSocket + REST 폴백** | — |
| D-02 | Android: **SyncHub on macOS** (WebView UI) — **오너 동의** | [adr/001-android-synchub.md](../adr/ADR-001-android-synchub.md) |
| D-03 | AI: **LSTM BC RNN** + Tier1/3 학습 | [adr/002-rnn-personal-model.md](../adr/ADR-002-rnn-personal-model.md) |
| D-04 | 모드 로직: **`trading_modes` 패키지** | [adr/003-trading-modes-package.md](../adr/ADR-003-trading-modes-package.md) |
| D-05 | AI 주문: **ApprovalGate 기본(Off=승인 필수)**; 무승인 자동은 설정 On | [adr/004](../adr/ADR-004-ai-auto-without-approval-setting.md) |
| D-06 | Addon: **propose only** → OrderService | 기존 doc/02 유지 |
| D-07 | 단타: **IntradayPatternAnalyzer** 휴리스틱 v1 — **오너 확정** | [design-owner-feedback.md](../FBK-001-design-owner-feedback.md) |
| D-08 | 데이터: **DataSourceRegistry + Tier 배지** | — |
| D-09 | SyncHub 보안: **LAN + 페어링 토큰** (O-01) | [adr/007](../adr/ADR-007-connectivity-and-shared-math-v1.md) |
| D-10 | Android 승인 알림: **15초 폴링 + 로컬 알림** (O-02) | [adr/007](../adr/ADR-007-connectivity-and-shared-math-v1.md) |
| D-11 | 공통 수학: **`trading_modes/shared/`** (O-03) | [adr/007](../adr/ADR-007-connectivity-and-shared-math-v1.md) |
| D-12 | CI/CD: **GitHub Actions**; live 주문 CI 금지; ML smoke 분리 | [adr/008](../adr/ADR-008-github-cicd-devops-mlops.md), [OPS-001](../operations/OPS-001-github-cicd.md) |
| D-13 | MLOps: **파일 레지스트리** `artifacts/models/` + 승격 게이트; full train 로컬 | [OPS-002](../operations/OPS-002-devops-mlops.md), [UC-007](../usecase/UC-007-rnn-training-data.md) |

## 기각

| ID | 결정 | 사유 |
|----|------|------|
| X-01 | Android 독립 KIS **평문** 분산 (상용안) | ADR-006 **암호화 APK 내장**으로 개인앱은 별도 |
| X-02 | Transformer v1 | 데이터·설명 |
| X-03 | MSA 분리 | 규모 |
| X-04 | OPA 정책 엔진 | 복잡도 |
| X-05 | AI 무승인 **항상** 허용(설정 없음) | 기본 Off·토글 필수로 대체 ([ADR-004](../adr/ADR-004-ai-auto-without-approval-setting.md)) |

## 오너 피드백 확정 (2026-06-02)

| # | 내용 |
|---|------|
| 1 | SyncHub — 동의 |
| 2 | `ai_auto_without_approval` — **기본 false**, On 시 무승인 허용 |
| 3 | 단타 휴리스틱 v1 — 확정 |

→ [design-owner-feedback.md](../FBK-001-design-owner-feedback.md)

## 확정 이력 (구 open-issues)

| ID | 확정 내용 | ADR/문서 |
|----|-----------|----------|
| O-01 | **LAN + 페어링 토큰** | D-09, [ADR-007](../adr/ADR-007-connectivity-and-shared-math-v1.md) |
| O-02 | **폴링 15s + 로컬 알림** | D-10, [ADR-007](../adr/ADR-007-connectivity-and-shared-math-v1.md) |
| O-03 | **`trading_modes/shared/`** | D-11, [ADR-007](../adr/ADR-007-connectivity-and-shared-math-v1.md) |
| O-04 | 그린필드 `trading_modes`·`yst_ui` | [ADR-005](../adr/ADR-005-greenfield-ui-and-modes.md) |
| O-05 | MVP 화면 전량 콘티 | [UI-003](../ui/UI-003-storyboards-system-android.md) |

쉬운 설명(교육용): [DEC-003-open-issues-guide.md](DEC-003-open-issues-guide.md)

**다음**: [ARC-003](../architecture/ARC-003-trading-modes-greenfield.md), Phase 7 `architecture.md`
