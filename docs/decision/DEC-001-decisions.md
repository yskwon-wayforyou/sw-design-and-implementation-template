# 채택·기각 설계 결정 (Phase 6.2)


| 항목 | 내용 |
|------|------|
| TraceID | DEC-001 |

| 버전 | 0.6 (평가표 제목·근거) |

---

## 채택

| ID | 제목 | 결정 | 평가 근거 | ADR |
|----|------|------|-----------|-----|
| D-01 | Desktop 시세 경로 | **KIS WebSocket + REST 폴백** | QS-001 Must; [DEC-002](DEC-002-evaluations.md) CA-PERF-B | — |
| D-02 | Android 동기 | **SyncHub on macOS** (WebView) — **오너 동의** | QS-010·012; 키·로직 집중 | [ADR-001](../adr/ADR-001-android-synchub.md) |
| D-03 | AI 모델 | **LSTM BC RNN** + Tier1/3 | QS-008·011; 데이터·설명 현실성 | [ADR-002](../adr/ADR-002-rnn-personal-model.md) |
| D-04 | 모드 패키지 | **`trading_modes` 신설** | CA-MOD-B; 변경 용이성 | [ADR-003](../adr/ADR-003-trading-modes-package.md) |
| D-05 | AI 승인 정책 | **ApprovalGate 기본**; 무승인은 설정 On | QS-004 Must; 오너 피드백 #2 | [ADR-004](../adr/ADR-004-ai-auto-without-approval-setting.md) |
| D-06 | Addon 경계 | **propose only** → OrderService | ASR-009; 실행 단일 경로 | doc/02 |
| D-07 | 단타 v1 | **IntradayPatternAnalyzer** 휴리스틱 | 오너 피드백 #3 확정 | [FBK-001](../FBK-001-design-owner-feedback.md) |
| D-08 | 데이터 Tier | **DataSourceRegistry + 배지** | ASR-001; 출처·지연 투명 | — |
| D-09 | Hub LAN 보안 | **LAN + 페어링 토큰** (O-01) | QS-017 Must | [ADR-007](../adr/ADR-007-connectivity-and-shared-math-v1.md) |
| D-10 | Android 승인 알림 | **15초 폴링 + 로컬 알림** (O-02) | FCM 없이 v1 실현; UC-010 | [ADR-007](../adr/ADR-007-connectivity-and-shared-math-v1.md) |
| D-11 | 공통 지표 | **`trading_modes/shared/`** (O-03) | Day/Long 수식 중복 제거 | [ADR-007](../adr/ADR-007-connectivity-and-shared-math-v1.md) |
| D-12 | GitHub CI/CD | **Actions**; live CI 금지 | ASR-014; 솔로 회귀 자동화 | [ADR-008](../adr/ADR-008-github-cicd-devops-mlops.md), [OPS-001](../operations/OPS-001-github-cicd.md) |
| D-13 | MLOps 레지스트리 | **`artifacts/models/`** + 승격 게이트 | UC-007·NFR-04 재현 | [OPS-002](../operations/OPS-002-devops-mlops.md), [UC-007](../usecase/UC-007-rnn-training-data.md) |
| D-14 | 상용 품질 기준선 | **CB·멱등·stale·감사·Hub** | QS-013~018 Must; [QEV-001](../quality/QEV-001-evaluations.md) | [ADR-009](../adr/ADR-009-commercial-quality-security-baseline.md), [ARC-004](../architecture/ARC-004-resilience-security-crosscut.md) |

## 기각

| ID | 제목 | 결정 | 평가 근거 |
|----|------|------|-----------|
| X-01 | Android KIS 평문 분산 | 독립 KIS **평문** (상용안) | 개인앱은 ADR-006 암호화 내장으로 대체; 상용 다인 배포 비목표 |
| X-02 | Transformer v1 | Transformer | 데이터 부족·설명 어려움; [DEC-002](DEC-002-evaluations.md) CA-ML-B |
| X-03 | MSA | 서비스 분리 | 솔로 규모 대비 운영 과다 |
| X-04 | OPA | 정책 엔진 OPA | [DEC-002](DEC-002-evaluations.md) CA-SEC-B 기각 |
| X-05 | AI 항상 무승인 | 무승인 **항상** 허용 | QS-004 위반; ADR-004 토글로 대체 |

## 오너 피드백 확정 (2026-06-02)

| # | 내용 |
|---|------|
| 1 | SyncHub — 동의 |
| 2 | `ai_auto_without_approval` — **기본 false**, On 시 무승인 허용 |
| 3 | 단타 휴리스틱 v1 — 확정 |

→ [design-owner-feedback.md](../FBK-001-design-owner-feedback.md)

## 확정 이력 (구 open-issues)

| ID | 제목 | 확정 내용 | 평가 근거 | ADR/문서 |
|----|------|-----------|-----------|----------|
| O-01 | Hub 인증 | **LAN + 페어링 토큰** | QS-017; 집 LAN 위협 완화 | D-09, [ADR-007](../adr/ADR-007-connectivity-and-shared-math-v1.md) |
| O-02 | 승인 알림 | **폴링 15s + 로컬 알림** | FCM v2·기본 Off; 구현 단순 | D-10, [ADR-007](../adr/ADR-007-connectivity-and-shared-math-v1.md) |
| O-03 | 공통 수학 | **`trading_modes/shared/`** | 중복 제거·테스트 일원화 | D-11, [ADR-007](../adr/ADR-007-connectivity-and-shared-math-v1.md) |
| O-04 | 그린필드 UI | `trading_modes`·`yst_ui` 신규 | PoC GUI 미사용·부채 제거 | [ADR-005](../adr/ADR-005-greenfield-ui-and-modes.md) |
| O-05 | MVP 화면 | 화면 전량 콘티 | 구현 범위 고정 | [UI-003](../ui/UI-003-storyboards-system-android.md) |

쉬운 설명(교육용): [DEC-003-open-issues-guide.md](DEC-003-open-issues-guide.md)

**다음**: [ARC-000](../ARC-000-architecture.md) · [EVL-002](../evaluation/EVL-002-architecture-evaluation.md)
