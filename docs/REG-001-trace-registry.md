# TraceID 레지스트리 — YSTrading 설계 문서

| 항목 | 내용 |
|------|------|
| TraceID | REG-001 |

| TraceID | 경로 | 제목(요약) |
|---------|------|------------|
| REG-001 | `REG-001-trace-registry.md` | TraceID 레지스트리 (본 문서) |
| ADR-001 | `adr/ADR-001-android-synchub.md` | ADR-001: Android 동기 — SyncHub on macOS |
| ADR-002 | `adr/ADR-002-rnn-personal-model.md` | ADR-002: 개인화 RNN (LSTM BC) |
| ADR-003 | `adr/ADR-003-trading-modes-package.md` | ADR-003: trading_modes 패키지 신설 |
| ADR-004 | `adr/ADR-004-ai-auto-without-approval-setting.md` | ADR-004: AI 무승인 자동 — 설정 On/Off (기본 Off) |
| AIQ-001 | `AIQ-001-ai_quality_profile.md` | AI 품질 프로파일 — YSTrading |
| ARC-001 | `architecture/ARC-001-module.md` | 모듈 구조 (개발 뷰) |
| ARC-002 | `architecture/ARC-002-deployment.md` | 배치 구조 (동작 뷰) |
| ASR-001 | `ASR-001-asr.md` | 아키텍처 유의 요구사항 (ASR) |
| BUS-001 | `BUS-001-business.md` | 비즈니스 요구 — YSTrading |
| CAT-001 | `candidate/CAT-001-candidates.md` | 후보 구조 통합 목록 |
| CND-001 | `candidate/CND-001-android-sync.md` | 후보 구조 — Android 동기 (QS-010, 012) |
| CND-002 | `candidate/CND-002-layered-modularity.md` | 후보 구조 — 레이어·모듈 (변경 용이성) |
| CND-003 | `candidate/CND-003-ml-rnn-architecture.md` | 후보 구조 — ML RNN (QS-008, 011) |
| CND-004 | `candidate/CND-004-performance-realtime.md` | 후보 구조 — 성능·실시간 (QS-001) |
| CND-005 | `candidate/CND-005-security-safety.md` | 후보 구조 — 보안·안전 (QS-002~004, 009) |
| DEC-001 | `decision/DEC-001-decisions.md` | 채택·기각 설계 결정 (Phase 6.2) |
| DEC-002 | `decision/DEC-002-evaluations.md` | 후보 구조 평가 |
| DOM-001 | `domain/DOM-001-model.md` | 통합 도메인 모델 |
| DOM-004 | `domain/DOM-004-daytrade-domain.md` | UC-004 도메인 분석 — 단타 패턴 |
| DOM-006 | `domain/DOM-006-ai-domain.md` | UC-006 도메인 분석 — AI 자동·승인 |
| FBK-001 | `FBK-001-design-owner-feedback.md` | 오너 설계 피드백 확정 |
| HUB-001 | `HUB-001-DESIGN-INTEGRATED.md` | 통합 설계 허브 — YSTrading |
| IDX-001 | `IDX-001-README.md` | YSTrading — 구조 설계 산출물 (`docs/`) |
| QEV-001 | `quality/QEV-001-evaluations.md` | 품질 시나리오 평가 |
| QLT-001 | `QLT-001-qualities.md` | 선정된 품질 요구사항 |
| QS-001 | `quality/QS-001-realtime-market-data.md` | QS-001 — 장중 시세 실시간성 |
| QS-004 | `quality/QS-004-ai-approval-gate.md` | QS-004 — AI 승인 게이트 |
| QSC-001 | `quality/QSC-001-scenarios.md` | 품질 시나리오 목록 |
| SYS-001 | `SYS-001-system.md` | 시스템 정의 — YSTrading |
| UC-001 | `usecase/UC-001-profile-connect.md` | UC-001 — 프로필 연결 및 paper/live 전환 |
| UC-002 | `usecase/UC-002-manual-order.md` | UC-002 — HTS형 수동 주문 |
| UC-003 | `usecase/UC-003-market-dashboard.md` | UC-003 — 현황·시세·차트 조회 |
| UC-004 | `usecase/UC-004-daytrade-pattern.md` | UC-004 — 단타 모드: 당일 등락 패턴 분석·제안 |
| UC-005 | `usecase/UC-005-longterm-recommend.md` | UC-005 — 장기 투자 모드: 종목 추천 |
| UC-006 | `usecase/UC-006-ai-auto-approval.md` | UC-006 — AI 자동 매매: 추론·승인·실행 |
| UC-007 | `usecase/UC-007-rnn-training-data.md` | UC-007 — RNN 학습 데이터 수집·학습 |
| UC-008 | `usecase/UC-008-pnl-history.md` | UC-008 — 손익·투자·매매 이력 관리 |
| UC-009 | `usecase/UC-009-multi-source-data.md` | UC-009 — 다원 시장 정보 수집·표시 |
| UC-010 | `usecase/UC-010-android-parity.md` | UC-010 — Android 기능 패리티·승인 푸시 |
| UC-011 | `usecase/UC-011-risk-guard.md` | UC-011 — RiskGuard 및 실전 안전장치 |
| UC-012 | `usecase/UC-012-news-disclosure.md` | UC-012 — 뉴스·공시·시장 맥락 |
| UCL-001 | `UCL-001-usecases.md` | Use Case 목록 — YSTrading |
| IDX-000 | `README.md` | `docs/` 진입 (짧은 색인) |
| UI-IDX-000 | `ui/README.md` | UI 설계 폴더 진입 |
| UI-000 | `ui/UI-000-greenfield-principles.md` | UI 그린필드 원칙·IA |
| UI-001 | `ui/UI-001-storyboards-shell-common.md` | 셸·공통 HTS 화면 콘티 |
| UI-002 | `ui/UI-002-storyboards-trading-modes.md` | Day·Long·AI·ML 콘티 |
| UI-003 | `ui/UI-003-storyboards-system-android.md` | 설정·승인·Android·예외 콘티 |
| ARC-003 | `architecture/ARC-003-trading-modes-greenfield.md` | trading_modes · yst_ui 그린필드 |
| ADR-005 | `adr/ADR-005-greenfield-ui-and-modes.md` | 그린필드 UI·모드 ADR |
| UI-QT6-000 | `ui/UI-QT6-layout-conventions.md` | PySide6 레이아웃·공통 위젯 정본 |
| DEC-003 | `decision/DEC-003-open-issues-guide.md` | O-01~03 쉬운 설명 (확정됨) |
| ADR-007 | `adr/ADR-007-connectivity-and-shared-math-v1.md` | O-01~03 v1 확정 |
| UI-004 | `ui/UI-004-plain-language-and-labels.md` | UI 일반 사용자 용어 |
| UI-005 | `ui/UI-005-cursor-light-theme.md` | Cursor Light Look and Feel |
| ADR-006 | `adr/ADR-006-personal-credentials-encryption.md` | 개인용 KIS 키 암호화·Android 내장 |
| ADR-008 | `adr/ADR-008-github-cicd-devops-mlops.md` | GitHub CI/CD · DevOps · MLOps 도구체인 |
| DEP-001 | `DEP-001-deployment.md` | 배포·릴리스·운영 (11절) |
| OPS-IDX-001 | `operations/README.md` | 운영·CI/CD·MLOps 폴더 진입 |
| OPS-001 | `operations/OPS-001-github-cicd.md` | GitHub Actions CI/CD 설계 |
| OPS-002 | `operations/OPS-002-devops-mlops.md` | DevOps · MLOps 적용 설계 |

## 규칙

- 형식: `{범주}-{일련}` — **YSTrading 저장소 내부 전용**(외부 시스템·글로벌 TraceID와 무관)
- 파일명: `{TraceID}-{설명-slug}.md`
- 본문 메타데이터 표에 `TraceID` 행 필수
- 정본 목록: 본 레지스트리(`REG-001`)
- UI 도식: **Mermaid만**; Qt6 위젯: `UI-QT6-000`
