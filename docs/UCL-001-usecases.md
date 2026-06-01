# Use Case 목록 — YSTrading

| 버전 | 0.1 (Phase 2) |
|------|----------------|
| TraceID | UCL-001 |
| 입력 | [system.md](SYS-001-system.md), [business.md](BUS-001-business.md), [../doc/12-requirements-and-quality-attributes-ko.md](../doc/12-requirements-and-quality-attributes-ko.md) |

---

## 1. 액터 요약

| 액터 | 설명 |
|------|------|
| **Investor** | 개인 투자자 |
| **KIS** | 한국투자증권 Open API |
| **DataProvider** | pykrx·공시·뉴스 등 외부 원천 |
| **MLPipeline** | 오프라인 학습·배치 (동일인 운영) |

---

## 2. Use Case 카탈로그

| ID | 제목 | 우선순위 | 모드 | 상세 |
|----|------|----------|------|------|
| UC-001 | 프로필 연결 및 paper/live 전환 | P0 | 공통 | [usecase/UC-001-profile-connect.md](usecase/UC-001-profile-connect.md) |
| UC-002 | HTS형 수동 주문 | P0 | Manual | [usecase/UC-002-manual-order.md](usecase/UC-002-manual-order.md) |
| UC-003 | 현황·시세·차트 조회 | P0 | Manual | [usecase/UC-003-market-dashboard.md](usecase/UC-003-market-dashboard.md) |
| UC-004 | 단타 모드 — 당일 패턴 제안 | P1 | Day | [usecase/UC-004-daytrade-pattern.md](usecase/UC-004-daytrade-pattern.md) |
| UC-005 | 장기 투자 모드 — 종목 추천 | P1 | Long | [usecase/UC-005-longterm-recommend.md](usecase/UC-005-longterm-recommend.md) |
| UC-006 | AI 자동 매매 — 추론·승인·실행 | P1 | AI | [usecase/UC-006-ai-auto-approval.md](usecase/UC-006-ai-auto-approval.md) |
| UC-007 | RNN 학습 데이터 수집·학습 | P1 | AI/ML | [usecase/UC-007-rnn-training-data.md](usecase/UC-007-rnn-training-data.md) |
| UC-008 | 손익·투자·매매 이력 관리 | P0 | 공통 | [usecase/UC-008-pnl-history.md](usecase/UC-008-pnl-history.md) |
| UC-009 | 다원 시장 정보 수집·표시 | P1 | 공통 | [usecase/UC-009-multi-source-data.md](usecase/UC-009-multi-source-data.md) |
| UC-010 | Android 기능 패리티·승인 푸시 | P1 | 공통 | [usecase/UC-010-android-parity.md](usecase/UC-010-android-parity.md) |
| UC-011 | RiskGuard 및 실전 안전장치 | P0 | 공통 | [usecase/UC-011-risk-guard.md](usecase/UC-011-risk-guard.md) |
| UC-012 | 뉴스·공시·시장 맥락 | P2 | 공통 | [usecase/UC-012-news-disclosure.md](usecase/UC-012-news-disclosure.md) |

**우선순위**: P0 = MVP 차단, P1 = 제품 차별화, P2 = 보조.

---

## 3. UC ↔ 화면(IA) 매핑

| 화면 ID | 관련 UC |
|---------|---------|
| SCR-HOME | UC-001, UC-003, UC-008 |
| SCR-QUOTE | UC-003, UC-004 |
| SCR-CHART | UC-003, UC-004 |
| SCR-ORDER | UC-002, UC-004, UC-006 |
| SCR-HISTORY | UC-008 |
| SCR-ML / 자동매매 Model | UC-006, UC-007 |
| SCR-MKTINFO | UC-009, UC-012 |
| Android Shell | UC-010, UC-006 |

출처: [../doc/25-shinhan-ref-hts-ia-requirements-ko.md](../doc/25-shinhan-ref-hts-ia-requirements-ko.md)

---

## 4. UC ↔ ASR 추적 (초안)

| ASR | UC |
|-----|-----|
| ASR-001 실시간성 | UC-003, UC-009 |
| ASR-002 paper/live 안전 | UC-001, UC-011 |
| ASR-003 AI 승인 | UC-006, UC-010 |
| ASR-004 RNN 개인화 | UC-007, UC-006 |
| ASR-005 이력 완전성 | UC-008 |

상세: [asr.md](ASR-001-asr.md)

---

## 5. Phase 2 체크포인트

- [x] 주요 기능 UC 12건 식별
- [x] 각 UC 상세 문서 링크
- [ ] Phase 3 도메인 모델과 1:1 대응 검증
