# 통합 설계 허브 — YSTrading

| 워크플로 진행 | Phase 1~8 **완료** (v1 명세·평가) · 구현은 P0~ 순 |
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
| 4 | 품질·ASR·AI | [QLT-001](QLT-001-qualities.md), [QLT-002 상용](QLT-002-commercial-quality-baseline.md), [ASR-001](ASR-001-asr.md), [AIQ-001](AIQ-001-ai_quality_profile.md) | 있음 |
| 4b | 보안·신뢰성 | [security/](security/), [reliability/](reliability/) | 있음 |
| 4c | 데이터 원천·RNN 수집 | [data/](data/) | 있음 |
| 4d | 후보 구조·채택 보완 | [candidate/](candidate/) | 있음 (CND v0.2) |
| 5~6 | 후보·결정·배치·모듈 | [candidate/](candidate/), [decision/](decision/), [architecture/](architecture/) | 있음 |
| ADR | 001~009 | [adr/](adr/) | 9건 |
| 7 | 구조 명세 (UI·로깅 포함) | [ARC-000-architecture.md](ARC-000-architecture.md) | 있음 |
| 7b | 배포·CI/CD·DevOps·MLOps | [DEP-001](DEP-001-deployment.md), [operations/](operations/) | 있음 |
| 8 | 구조 평가 | [evaluation/](evaluation/) EVL-001~002 | 있음 |
| UI | 그린필드·콘티 | [ui/](ui/) | 있음 (UI-000~003) |
| 그린필드 구조 | trading_modes · yst_ui | [architecture/ARC-003-trading-modes-greenfield.md](architecture/ARC-003-trading-modes-greenfield.md) | 있음 |
| 횡단 복원력·보안 | ARC-004 | [architecture/ARC-004-resilience-security-crosscut.md](architecture/ARC-004-resilience-security-crosscut.md) | 있음 |
| UI 용어·테마 | UI-004, UI-005 | [ui/](ui/) | 있음 |
| 조사 | 오픈 ML·데이터 서베이 | [survey/SRV-001](survey/SRV-001-open-ml-models-and-data-survey.md) | 반영 [ADR-010](adr/ADR-010-open-ml-data-and-crossmodal-training.md) |
| 구현 | 스키마·인터페이스·일정·진행·테스트 | [implementation/](implementation/) | 있음 |
| UC-013 | Android 음성·자연어 매매 | [UC-013](usecase/UC-013-voice-nl-trading-android.md), [ADR-011](adr/ADR-011-android-voice-nl-trading.md), [UI-006](ui/UI-006-android-voice-nl.md) | 있음 |

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
6. [QLT-002 상용 품질](QLT-002-commercial-quality-baseline.md) → [SEC-001](security/SEC-001-threat-model-and-controls.md) → [REL-001](reliability/REL-001-slo-resilience-patterns.md)
7. [ARC-000 구조 명세](ARC-000-architecture.md) → [OPS-003 로깅](operations/OPS-003-logging-observability.md) → [OPS-004 디버깅](operations/OPS-004-debugging-issue-intake.md)
8. [EVL-002 구조 평가](evaluation/EVL-002-architecture-evaluation.md)

---

## 설계 open-issues

**O-01~05 전부 확정** (2026-06-02). 요약: [DEC-001](decision/DEC-001-decisions.md) · [ADR-007](adr/ADR-007-connectivity-and-shared-math-v1.md).

| ID | 제목 | 확정 | 평가 근거 |
|----|------|------|-----------|
| O-01 | Hub 인증 | LAN + 페어링 토큰 | QS-017 · [DEC-001](decision/DEC-001-decisions.md) D-09 |
| O-02 | 승인 알림 | 폴링 15s + 로컬 알림 | UC-010 · D-10 |
| O-03 | 공통 수학 | `trading_modes/shared/` | D-11 |
| O-04 | 그린필드 | `trading_modes`·`yst_ui` | ADR-005 |
| O-05 | MVP 화면 | UI 콘티 전량 | UI-003 |
