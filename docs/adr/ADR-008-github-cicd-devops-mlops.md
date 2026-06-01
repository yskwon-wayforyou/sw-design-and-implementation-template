# ADR-008: GitHub CI/CD · DevOps · MLOps 도구체인

| 상태 | Accepted |
|------|----------|
| TraceID | ADR-008 |
| 날짜 | 2026-06-02 |
| 관련 | [OPS-001](../operations/OPS-001-github-cicd.md), [OPS-002](../operations/OPS-002-devops-mlops.md), [DEP-001](../DEP-001-deployment.md) |

## Context

YSTrading은 **개인 단독** macOS(PySide6) + Android(WebView/SyncHub) 앱이다. 저장소는 **GitHub**(`yskwon-wayforyou/YSTrading`)를 정본으로 하며, KIS 실전 주문·개인 API 키는 [ADR-006](ADR-006-personal-credentials-encryption.md)에 따라 **CI에 평문을 두지 않는다**. UC-007·ADR-002에 따라 **오프라인 RNN 학습·모델 버전** 파이프라인이 필요하다.

## Decision drivers

| 우선순위 | 목표 |
|----------|------|
| 1 | **안전** — CI에서 live 주문·실계좌 호출 금지 |
| 2 | **재현성** — ML 아티팩트·메트릭·데이터 해시 추적 (ASR-007, NFR-04) |
| 3 | **단순성** — 솔로 개발자가 유지 가능한 워크플로 수 |
| 4 | **비용** — GitHub Free 티어·self-hosted runner 없이 macOS 빌드는 **로컬/수동** 허용 |

## Options considered

### 1. GitHub Actions 중심 (채택)

- PR/`main`에서 lint·단위·계약·ML smoke; 릴리스는 **태그 + workflow_dispatch**.
- macOS 네이티브 빌드는 GHA `macos-latest`에서 **선택적**(시간·시크릿 제약) 또는 로컬 `make release`.
- **기각 사유 없음** — 저장소 호스팅과 일치.

### 2. GitLab CI / Jenkins self-hosted

- macOS 빌드 에이전트 운영 부담, 개인 프로젝트에 과함.
- **기각**.

### 3. CI 없음(로컬만)

- 회귀·ML smoke 누락 위험; 협업·이력 부재.
- **기각** — 최소 GHA는 유지, 무거운 작업만 로컬.

## Decision

| 영역 | 결정 |
|------|------|
| **CI/CD 플랫폼** | **GitHub Actions** (`.github/workflows/`) |
| **브랜치** | `main` 보호(필수 status check); 기능은 `feat/*`, `fix/*` |
| **환경** | `ci`(GHA), `local-dev`, `release`(태그 산출물) — **클라우드 prod 없음** |
| **비밀** | KIS 평문 **GitHub Secrets 미사용(기본)**; `secrets.enc`는 **빌드 PC·로컬**에서 [encrypt_secrets](../../scripts/encrypt_secrets.py) |
| **DevOps** | 로그·헬스·롤백은 [OPS-002](../operations/OPS-002-devops-mlops.md) §DevOps |
| **MLOps** | `ml_pipeline/` + GHA `ml-smoke` + 로컬 `train`/`promote`; 모델 레지스트리 = `artifacts/models/` + 메타 JSON |
| **배포** | 개인 설치: macOS 앱 번들·Android APK/AAB — [DEP-001](../DEP-001-deployment.md) |

## Consequences

### Positive

- PR마다 자동 품질 게이트; live 주문 경로는 CI 밖으로 격리.
- UC-007 학습·승격 절차를 문서·워크플로로 고정.

### Negative

- macOS 공증·notarize, Android 서명은 **오너 로컬** 또는 수동 시크릿 주입 필요.
- GHA에서 대용량 학습은 비용·시간상 **로컬 우선**.

## Compliance

| ASR | 반영 |
|-----|------|
| ASR-002 | CI 통합 테스트는 **mock KIS** 또는 paper URL 고정 fixture |
| ASR-004 | AI live 경로 E2E는 CI **금지**; ApprovalGate 단위 테스트만 |
| ASR-007 | ML 워크플로 walk-forward·`data_hash` 게이트 |
| ASR-011 | 워크플로 로그에 키 마스킹; `secrets/plain/` 미체크인 |

## Links

- [ARC-002](../architecture/ARC-002-deployment.md) §7
- [UC-007](../usecase/UC-007-rnn-training-data.md)
- [AIQ-001](../AIQ-001-ai_quality_profile.md)
