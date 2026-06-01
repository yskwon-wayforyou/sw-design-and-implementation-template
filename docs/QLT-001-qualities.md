# 선정된 품질 요구사항


| 항목 | 내용 |
|------|------|
| TraceID | QLT-001 |

| 버전 | 0.1 |

입력: [quality/scenarios.md](quality/QSC-001-scenarios.md), [quality/evaluations.md](quality/QEV-001-evaluations.md), [ai_quality_profile.md](AIQ-001-ai_quality_profile.md)

---

## 1. NFR (허용치)

| ID | 속성 | 허용치/정책 | ASR |
|----|------|-------------|-----|
| NFR-T-01 | 실시간성 | Tier A 시세: 폴링 기본 3s, WS 시 1s; UI에 `as_of` 표시 | ASR-001 |
| NFR-S-01 | 안전 | paper/live 혼선 기동 거부 | ASR-002 |
| NFR-S-02 | 안전 | live 주문 확인 100% | ASR-003 |
| NFR-S-03 | 안전 | AI 기본 무승인 주문 0 | ASR-004 |
| NFR-R-01 | 신뢰성 | 401 → 1회 재시도 | QS-005 |
| NFR-U-01 | 사용성 | paper=blue, live=amber/red 배너 | QS-006 |
| NFR-P-01 | 성능 | 주문 로컬 검증 후 전송 <500ms | QS-007 |
| NFR-M-01 | 재현성 | ML lock + data_hash | NFR-04 |
| NFR-SEC-01 | 보안 | 로그 마스킹 | QS-009 |

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
