# QLT-002 — 상용급 품질 기준선 (안정성 · 신뢰성 · 보안)

| 항목 | 내용 |
|------|------|
| TraceID | QLT-002 |
| 버전 | 0.1 |
| 상위 | [QLT-001](QLT-001-qualities.md) 확장 |
| ADR | [ADR-009](adr/ADR-009-commercial-quality-security-baseline.md) |

개인용이나 **실계좌·AI·모바일 키**를 다루므로, v1부터 아래 NFR·SLO·게이트를 **live/AI 릴리스 필수**로 둔다.

---

## 1. 품질 목표 (한 줄)

| 속성 | 목표 |
|------|------|
| **안전(Safety)** | 오주문·무승인 AI·프로필 혼선 **제로 허용(설계상)** |
| **신뢰성(Reliability)** | KIS 일시 장애 시 **자동 복구**·중복 주문 **없음** |
| **보안(Security)** | 비밀·감사·Hub **다층 방어** |
| **가용성(Availability)** | 부분 장애 시 **읽기·취소** 유지 |
| **유지보수** | 사고 **재현·추적** 가능 |

---

## 2. NFR 확장 (상용)

| ID | 속성 | 허용치/정책 | ASR | QS |
|----|------|-------------|-----|-----|
| NFR-R-02 | 신뢰성 | KIS 5xx: CB OPEN 후 30s; 사용자 메시지 명확 | ASR-016 | QS-016 |
| NFR-R-03 | 신뢰성 | 주문 `client_order_id` **필수**·중복 0 | ASR-015 | QS-015 |
| NFR-R-04 | 신뢰성 | EventStore RPO ≤ 24h (일 백업) | ASR-020 | QS-014 |
| NFR-A-01 | 가용성 | WS 단절 3s 내 REST 폴백 | — | QS-013 |
| NFR-A-02 | 가용성 | Hub 다운 시 Android **읽기 전용** | — | QS-012 |
| NFR-S-04 | 안전 | live + 시세 5s 초과 stale → 주문 차단 | ASR-019 | QS-013 |
| NFR-S-05 | 안전 | 전역 `live_trading_enabled=false` 즉시 차단 | ASR-022 | — |
| NFR-SEC-02 | 보안 | Hub 세션 토큰·페어링 | ASR-018 | QS-017 |
| NFR-SEC-03 | 보안 | 금전 감사 **append-only** 100% | ASR-017 | QS-018 |
| NFR-SEC-04 | 보안 | 릴리스 SBOM·lockfile | ASR-021 | QS-019 |
| NFR-M-02 | AI | 학습 코퍼스 `data_hash` 검증 | — | QS-020 |
| NFR-O-01 | 관측 | 주문 실패율·latency 로컬 집계 | — | REL-001 |

기존 [QLT-001](QLT-001-qualities.md) NFR은 **유지**·병행.

---

## 3. SLO (로컬·정상망)

| 서비스 | SLI | SLO (30일) | 제외 |
|--------|-----|------------|------|
| 주문 제출(로컬→KIS ack) | 성공/시도 | **99.5%** | KIS 전면 장애 공지 |
| 토큰 갱신 | 성공/401 | **99.9%** | — |
| 시세 표시 | `as_of` ≤ 5s 비율 | **95%** (장중 Tier A) | 장 마감 |
| Hub API | 2xx/요청 | **99%** (LAN) | — |

위반 시: [OPS-002](operations/OPS-002-devops-mlops.md) §Incident.

---

## 4. 릴리스 게이트 (live / AI)

| # | 제목 | 게이트 | 평가 근거 | 증거 |
|---|------|--------|-----------|------|
| G1 | ASR Must 검증 | ASR Must 전부 TC 통과 | 구조 요구 누락 시 live 불가 | CI + paper E2E |
| G2 | 안전·상용 QS | QS-002~004, 013~018 통과 | [QEV-001](quality/QEV-001-evaluations.md) Must | 테스트 리포트 |
| G3 | 비밀 누출 0 | `secrets.enc`만·평문 grep 0 | ASR-011·QS-009 | CI |
| G4 | paper soak | paper 7일 운용 체크 | KIS·UI 회귀·오류율 | 오너 서명 |
| G5 | ML paper 승격 | `promotion_stage=paper` eval | UC-007·무승인 기본 Off 전제 | [OPS-002](operations/OPS-002-devops-mlops.md) |

**live AI 무승인 On** 은 G1~G5 + 오너 명시 동의 추가.

---

## 5. QA 우선순위 (상용 재정렬)

| 순위 | QA | 신규/강화 |
|------|-----|-----------|
| 1 | 안전 | stale 차단, kill switch |
| 2 | 보안 | Hub, 감사, 공급망 |
| 3 | 신뢰성 | CB, 멱등, 백업 |
| 4 | 가용성 | 폴백, degraded |
| 5 | 실시간성 | 기존 |
| 6 | AI 품질 | QS-020 |

---

## 6. Phase 8 체크리스트 (설계 완료 기준)

- [x] NFR·SLO·릴리스 게이트 문서화
- [x] 횡단 아키텍처 [ARC-004](architecture/ARC-004-resilience-security-crosscut.md)
- [ ] 구현·테스트 매핑 (코드 단계)
- [ ] paper soak 기록

---

## 관련

- [QSC-001](quality/QSC-001-scenarios.md) (QS-013~020 추가)
- [SEC-001](security/SEC-001-threat-model-and-controls.md)
- [REL-001](reliability/REL-001-slo-resilience-patterns.md)
