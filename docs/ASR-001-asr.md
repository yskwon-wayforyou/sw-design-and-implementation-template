# 아키텍처 유의 요구사항 (ASR)


| 항목 | 내용 |
|------|------|
| TraceID | ASR-001 |

| 버전 | 0.2 |

---

## ASR 목록

| ID | 요구 | 우선순위 | 검증 힌트 | 관련 UC/NFR |
|----|------|----------|-----------|-------------|
| **ASR-001** | 시세·주문 관련 UI 데이터는 **KIS Tier A** 우선; 표시 시 **수집 시각·Tier** 필수 | Must | UI 스냅샷 테스트; 배지 | UC-003, NFR 실시간 |
| **ASR-002** | `paper` 프로필이 실전 URL/키와 결합되면 **기동 거부** | Must | TC-P0-01 | UC-001, NFR-01 |
| **ASR-003** | `live` 주문은 **확인 UI + 감사 로그** | Must | TC-P0-06 | UC-002, UC-011 |
| **ASR-004** | AI 매매: `ai_auto_without_approval` **기본 false** — false일 때 승인 없이 주문 금지; true일 때 ApprovalGate 생략(RiskGuard 유지) | Must | 기본값·On/Off 경로 테스트 | UC-006, ADR-004 |
| **ASR-005** | 승인 UI에 **근거 요약**(피처·패턴·신뢰도) 제공 | Should | 스냅샷·필드 존재 | UC-006 |
| **ASR-006** | Tier3 이벤트는 **PII 마스킹·append-only** | Must | event_store 테스트 | UC-007, UC-008 |
| **ASR-007** | RNN 학습은 **시간 기준 walk-forward**; 라벨 누수 방지 | Must | ml_pipeline 단위 테스트 | UC-007 |
| **ASR-008** | Android가 macOS **기능 집합 동등**(승인·조회·주문·모드) | Should | 계약 테스트·체크리스트 | UC-010 |
| **ASR-009** | Addon/AI는 `propose_action`만; 실행은 **OrderService+RiskGuard** | Must | addons 프로토콜 | UC-006 |
| **ASR-010** | ML·GUI 의존 분리; GUI는 아티팩트 **read-only** 로드 | Should | 패키지 import 그래프 | UC-007 |
| **ASR-011** | KIS 자격증명: **암호화 blob**만 저장·배포; Git·UI·로그 **평문 금지**; Android `assets/secrets.enc` | Must | `encrypt_secrets`·`.gitignore`·스냅샷 | UC-001, UC-010, [ADR-006](adr/ADR-006-personal-credentials-encryption.md) |
| **ASR-012** | 사용자 대면 UI 문자열: **일반 용어만** ([UI-004](ui/UI-004-plain-language-and-labels.md)) | Must | 라벨 감사·금지어 grep | 전 화면 |
| **ASR-013** | macOS UI: **Cursor Light** 팔레트 ([UI-005](ui/UI-005-cursor-light-theme.md)) | Must | `QPalette` 토큰 테스트 | yst_ui |
| **ASR-014** | CI/CD: **live 주문·실계좌 KIS 호출 금지**; mock/paper fixture만; KIS 평문 Secrets 금지 | Must | GHA workflow grep·`not live` 마커 | [ADR-008](adr/ADR-008-github-cicd-devops-mlops.md), [OPS-001](operations/OPS-001-github-cicd.md) |
| **ASR-015** | 주문 **`client_order_id` 필수**; 재시도·중복 제출 시 이중 체결 방지 | Must | QS-015, RG-08 | UC-002, [ARC-004](architecture/ARC-004-resilience-security-crosscut.md) |
| **ASR-016** | KIS 호출 **Circuit Breaker**·타임아웃·백오프([REL-001](reliability/REL-001-slo-resilience-patterns.md)) | Must | QS-016 | UC-003 |
| **ASR-017** | 금전·승인·토큰 이벤트 **append-only 감사** 100% | Must | QS-018 | UC-008, [SEC-001](security/SEC-001-threat-model-and-controls.md) |
| **ASR-018** | SyncHub: **페어링·세션 토큰**·무토큰 쓰기 API 거부 | Must | QS-017 | UC-010, ADR-007 |
| **ASR-019** | **live** 주문: 시세 `as_of` stale(기본 5s) 시 차단 | Must | QS-013, RG-07 | UC-002 |
| **ASR-020** | EventStore **WAL**·기동 `integrity_check`·일 백업 | Must | QS-014 | UC-008 |
| **ASR-021** | 릴리스 **lockfile/SBOM**·critical CVE 미패치 0 | Must | QS-019 | [OPS-001](operations/OPS-001-github-cicd.md) |
| **ASR-022** | **`live_trading_enabled`** 전역 kill switch — false 시 live 주문 전경로 거부 | Must | 설정·단위 | UC-011 |
| **ASR-023** | 음성·자연어(UC-013): **확인 화면·confirm API** 없이 주문 금지; AI(UC-006) ApprovalGate **우회 금지**; 전사문 기본 미저장 | Must | QS-021, Hub 403 테스트 | UC-013, [ADR-011](adr/ADR-011-android-voice-nl-trading.md) |

---

## 우선순위 규칙

- **Must**: Phase 6 구조에 반드시 반영; 미충족 시 live/AI 릴리스 보류.
- **Should**: 로드맵 C/D; 문서화된 갭 허용.
