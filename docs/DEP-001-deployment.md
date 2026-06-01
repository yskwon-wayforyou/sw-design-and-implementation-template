# DEP-001 — 배포·릴리스·운영 (deployment)

| 항목 | 내용 |
|------|------|
| TraceID | DEP-001 |
| 버전 | 0.1 |
| 상세 | [operations/OPS-001-github-cicd.md](operations/OPS-001-github-cicd.md), [operations/OPS-002-devops-mlops.md](operations/OPS-002-devops-mlops.md) |
| ADR | [ADR-008](adr/ADR-008-github-cicd-devops-mlops.md) |

구조(무엇이 돌아가는지): [ARC-002-deployment.md](architecture/ARC-002-deployment.md). 본 문서는 **어떻게 심고 유지하는지** 정본이다.

---

## 1. 배포 단위

| 유닛 | 아티팩트 | 프로세스 |
|------|----------|----------|
| **macOS Desktop** | `YSTrading.app` / `.dmg` | `yst_ui` + `trading_modes` + `kis_core` + 내장 `resources/secrets.enc` |
| **SyncHub** (선택) | 동일 번들 내 FastAPI 또는 별도 `yst-sync-hub` | 포트 8765 |
| **Android** | `.apk` / `.aab` | WebView UI + `assets/secrets.enc` |
| **ML 모델** | `artifacts/models/rnn_personal/{version}/` | 파일 복사 또는 앱 리소스 번들(후속) |

한 번에 올리는 **릴리스 단위**: Desktop **또는** Android **또는** 모델 버전 — 서로 독립 버전 가능, `metadata.json`에 호환 `app_min_version` 기록(로드맵).

---

## 2. 환경

| 환경 | URL/엔드포인트 | 데이터 | 배포 방식 |
|------|----------------|--------|-----------|
| local-dev | KIS paper(수동) | 샘플·소량 EventStore | 소스 실행 |
| ci | mock `127.0.0.1:18080` | 합성 | GHA — 배포 없음 |
| paper-runtime | KIS 모의 URL | 전체 로컬 DB | 오너 설치 빌드 |
| live-runtime | KIS 실전 URL | 동일 DB·프로필 분리 | 동일 빌드, 앱 내 전환 |
| release | — | — | GitHub Release 바이너리 |

환경 차이는 **KIS 프로필·설정**뿐이며 별도 클라우드 스테이지는 없다.

---

## 3. 선행 조건

| 항목 | macOS | Android |
|------|-------|---------|
| OS | macOS 13+ (Apple Silicon 권장) | Android 10+ |
| Python | 3.12 (개발·PyInstaller 빌드) | — |
| JDK | — | 17 (Gradle) |
| 디스크 | `~/.YSTrading` ≥ 2GB | 앱 200MB+ |
| 네트워크 | KIS 443 아웃바운드 | 동일 |
| 계정 | KIS Open API 키(암호화 blob) | 동일 blob |
| 도구 | Xcode CLT, PyInstaller(빌드 시) | Android SDK |

---

## 4. 설정·비밀

| 항목 | 위치 | 저장소 |
|------|------|--------|
| 앱 설정 | `~/.YSTrading/config.yaml` | ❌ |
| 암호화 자격증명 | `secrets.enc`, `resources/`, Android `assets/` | enc만 선택적 ✅ |
| 마스터 키 | `secrets/.master.key`, `_embedded.py` | ❌ gitignore |
| CI | mock만 — **KIS Secrets 없음** | — |

주입 경로: 빌드 PC에서 [scripts/encrypt_secrets.py](../scripts/encrypt_secrets.py) → blob 복사. 상세: [secrets/README.md](../secrets/README.md), [ADR-006](adr/ADR-006-personal-credentials-encryption.md).

---

## 5. 데이터·상태

| 데이터 | 경로 | 마이그레이션 |
|--------|------|--------------|
| EventStore | `~/.YSTrading/data/events.db` | `migrations/` 순번, 기동 시 적용 |
| 시장 캐시 | `~/.YSTrading/cache/` | 재구축 가능 |
| 학습 코퍼스 | `artifacts/datasets/` | 버전별 Parquet |
| 모델 | `artifacts/models/` | 파일 교체 |

**백업**: 주 1회 `events.db` → `~/.YSTrading/backups/` (수동 또는 `launchd`).

---

## 6. 배포 절차

### 6.1 최초 설치 (macOS)

1. GitHub Release에서 `.dmg` 다운로드 또는 로컬 `make release-macos`.
2. `secrets.enc`가 번들에 없으면 `~/.YSTrading/secrets.enc` 배치.
3. 앱 실행 → 프로필 **모의** 연결 확인 → paper 주문 smoke.
4. live 전환 전 [UC-011](usecase/UC-011-risk-guard.md) 설정 확인.

### 6.2 업그레이드

1. 앱 종료 → DB 백업.
2. 새 DMG 설치(덮어쓰기).
3. 기동 시 migrate 자동 → 로그에 `schema_version` 확인.
4. ML 모델 변경 시 `config.yaml` `ml.active_version` 갱신.

**다운타임**: 단일 사용자 — 수 초~수 분(재시작).

### 6.3 Android

1. `assembleRelease` → APK.
2. sideload 설치(이전 APK 제거 또는 덮어쓰기).
3. 동일 `secrets.enc` blob.

### 6.4 ML 모델만 배포

1. 로컬 `train` → `eval_rnn_paper` 게이트 통과.
2. `artifacts/models/.../metadata.json` `promotion_stage: paper`.
3. paper 검증 후 `ml.active_version` 변경 — **앱 재시작**.

---

## 7. 헬스·준비

| 서비스 | probe | 성공 조건 |
|--------|-------|-----------|
| SyncHub | `GET /healthz` | 200, `kis_profile` 필드 |
| Desktop | 내부 heartbeat | WS 연결 또는 REST 폴백 OK |
| ML | `infer` smoke | <500ms, 유효 tensor |

로드밸런서: 해당 없음(단일 호스트).

---

## 8. 롤백

1. **앱**: 이전 Release DMG/APK 재설치.
2. **DB**: migrate 이후 구버전 앱 **사용 금지** — 백업 DB로 복원 후 구버전.
3. **모델**: `ml.active_version` 이전 값.
4. **secrets**: KIS 키 문제 시 포털 재발급 → `encrypt_secrets` 재실행.

---

## 9. 관측

| 신호 | 위치 |
|------|------|
| 앱 로그 | `~/.YSTrading/logs/` (JSON line, 마스킹) |
| 감사 | EventStore `audit_events` append-only |
| SLO 롤업 | `~/.YSTrading/metrics/` |
| CI | GitHub Actions Summary |

알람: v1 수동(로그 tail). SLO 위반·S1~S4: [REL-001](reliability/REL-001-slo-resilience-patterns.md) §8.

**RPO/RTO**: RPO 24h, RTO 15min — [REL-001](reliability/REL-001-slo-resilience-patterns.md) §5.

---

## 10. CI/CD 개요

| 단계 | 트리거 | 결과 |
|------|--------|------|
| Validate | PR, push `main` | merge gate |
| ML smoke | 동일 + ml 경로 | merge gate |
| Release | tag `v*`, manual | GitHub Release assets |

**프로덕션 배포 트리거**: 오너가 Release 바이너리를 **수동 설치** — 자동 live 배포 없음.

상세: [OPS-001](operations/OPS-001-github-cicd.md).

---

## 11. 보안·네트워크

| 항목 | 정책 |
|------|------|
| TLS | KIS·HTTPS 클라이언트 기본 |
| SyncHub | 기본 LAN; 페어링 토큰([ADR-007](adr/ADR-007-connectivity-and-shared-math-v1.md)) |
| CI | live 주문 API **호출 금지** |
| 키 회전 | KIS 포털 폐기 → blob 재생성 → 재빌드 |
| APK | 개인 sideload; 스토어 공개 비목표 |
| 위협·통제 | [SEC-001](security/SEC-001-threat-model-and-controls.md) |
| Hub | 세션 토큰·rate limit ([QS-017](quality/QS-017-hub-session-security.md)) |

---

## 변경 이력

| 날짜 | 내용 |
|------|------|
| 2026-06-02 | 초안 — ADR-008, OPS-001/002 연동 |
