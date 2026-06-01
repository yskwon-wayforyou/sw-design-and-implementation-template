# 통합 설계 허브 — YSTrading

| 워크플로 진행 | Phase 1~6 **완료** · 오너 피드백 **#1~3 반영** · Phase 7~8 예정 |
|---------------|----------------------------------------------------------------|
| TraceID | HUB-001 |
| 방법론 | [sw-design template workflow](../../sw-design-and-implementation-template/.cursor/rules/design-principles/workflow.md) |
| 레거시 요구 | [doc/](../doc/) (01, 02, 11, 12, …) |
| 피드백 기록 | [design-owner-feedback.md](FBK-001-design-owner-feedback.md) |
| TraceID 레지스트리 | [REG-001-trace-registry.md](REG-001-trace-registry.md) |

---

## 산출물 색인

| Phase | 산출물 | 경로 | 상태 |
|-------|--------|------|------|
| 1 | 시스템 정의 | [system.md](SYS-001-system.md) | 있음 (피드백 반영) |
| 1 | 비즈니스 | [business.md](BUS-001-business.md) | 있음 |
| 2 | UC 목록 | [usecases.md](UCL-001-usecases.md) | 있음 |
| 2 | UC 상세 ×12 | [usecase/](usecase/) | 있음 (UC-006 갱신) |
| 3 | 도메인 통합 | [domain/model.md](domain/DOM-001-model.md) | 있음 |
| 4 | 품질·ASR·AI | [qualities.md](QLT-001-qualities.md), [asr.md](ASR-001-asr.md), [ai_quality_profile.md](AIQ-001-ai_quality_profile.md) | 있음 (ASR-004 갱신) |
| 5~6 | 후보·결정·배치·모듈 | [candidate/](candidate/), [decision/](decision/), [architecture/](architecture/) | 있음 |
| ADR | 001~008 | [adr/](adr/) | 8건 |
| 7 | architecture.md | — | **예정** |
| 7b | 배포·CI/CD·DevOps·MLOps | [DEP-001](DEP-001-deployment.md), [operations/](operations/) | 있음 |
| 8 | 평가 | — | **예정** |
| UI | 그린필드·콘티 | [ui/](ui/) | 있음 (UI-000~003) |
| 그린필드 구조 | trading_modes · yst_ui | [architecture/ARC-003-trading-modes-greenfield.md](architecture/ARC-003-trading-modes-greenfield.md) | 있음 |
| ADR | 001~008 | [adr/](adr/) | 8건 |
| UI 용어·테마 | UI-004, UI-005 | [ui/](ui/) | 있음 |

---

## 오너 피드백 확정 요약

| # | 결정 |
|---|------|
| 1 | Android **SyncHub** — 동의 |
| 2 | AI 무승인 자동 — **`ai_auto_without_approval` 설정**, **기본 Off** |
| 3 | 단타 **휴리스틱 v1** — 확정 |

그린필드(#4·#5): [ADR-005](adr/ADR-005-greenfield-ui-and-modes.md) — PoC GUI 미사용, MVP 화면은 [ui/UI-003](ui/UI-003-storyboards-system-android.md) 목록.

---

## 권장 읽기 순서

1. [design-owner-feedback.md](FBK-001-design-owner-feedback.md)
2. [ADR-005 그린필드](adr/ADR-005-greenfield-ui-and-modes.md) → [ui/README.md](ui/README.md) (콘티 UI-000~003)
3. [ARC-003 trading_modes](architecture/ARC-003-trading-modes-greenfield.md)
4. [system.md](SYS-001-system.md) → [usecase/UC-006-ai-auto-approval.md](usecase/UC-006-ai-auto-approval.md)
5. [DEP-001 배포](DEP-001-deployment.md) → [OPS-001 CI/CD](operations/OPS-001-github-cicd.md) → [OPS-002 DevOps·MLOps](operations/OPS-002-devops-mlops.md)

---

## 설계 open-issues

**O-01~05 전부 확정** (2026-06-02). 요약: [DEC-001](decision/DEC-001-decisions.md) · [ADR-007](adr/ADR-007-connectivity-and-shared-math-v1.md).

| ID | 확정 |
|----|------|
| O-01 | LAN + 페어링 토큰 |
| O-02 | 폴링 15s + 로컬 알림 |
| O-03 | `trading_modes/shared/` |
| O-04~05 | 그린필드 UI·화면 — ADR-005, UI-003 |
