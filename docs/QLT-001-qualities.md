# 선정된 품질 요구사항


| 항목 | 내용 |
|------|------|
| TraceID | QLT-001 |

| 버전 | 0.3 |

입력: [quality/scenarios.md](quality/QSC-001-scenarios.md), [quality/evaluations.md](quality/QEV-001-evaluations.md), [ai_quality_profile.md](AIQ-001-ai_quality_profile.md)

**상용급 확장**: [QLT-002-commercial-quality-baseline.md](QLT-002-commercial-quality-baseline.md) (SLO·릴리스 게이트·QS-013~020)

---

## 1. NFR (허용치)

시나리오 평가(제목·근거): [QEV-001](quality/QEV-001-evaluations.md)

| ID | 제목 | 속성 | 허용치/정책 | ASR |
|----|------|------|-------------|-----|
| NFR-T-01 | 시세 실시간 표시 | 실시간성 | Tier A: 폴링 3s, WS 1s; `as_of` 표시 | ASR-001 |
| NFR-S-01 | paper/live 혼선 차단 | 안전 | paper/live 혼선 기동 거부 | ASR-002 |
| NFR-S-02 | live 주문 확인 | 안전 | live 주문 확인 100% | ASR-003 |
| NFR-S-03 | AI 무승인 차단 | 안전 | AI 기본 무승인 주문 0 | ASR-004 |
| NFR-R-01 | 401 토큰 갱신 | 신뢰성 | 401 → 1회 재시도 | QS-005 |
| NFR-U-01 | 프로필 배너 | 사용성 | paper=blue, live=amber/red | QS-006 |
| NFR-P-01 | 주문 UI 지연 | 성능 | 로컬 검증 후 <500ms | QS-007 |
| NFR-M-01 | ML 재현 | 재현성 | lock + data_hash | QS-008 |
| NFR-SEC-01 | 로그 마스킹 | 보안 | 시크릿 패턴 0 | QS-009 |

## 2. QA 우선순위 (아키텍처 driving)

| 순위 | QA | 이유 |
|------|-----|------|
| 1 | **안전(Safety)** | 금전 손실·약관 |
| 2 | **보안** | API 키 |
| 3 | **신뢰성** | 토큰·네트워크 |
| 4 | **실시간성** | 매매 UX (설계 한계 명시) |
| 5 | **사용성** | HTS 패리티 체감 |
| 6 | **유지보수·재현** | ML |
| 7 | **이식성** | Android |

## 3. Phase 4 체크포인트

- [x] NFR 허용치 명시
- [x] QA 우선순위
- [x] AI 프로파일 분리 문서
