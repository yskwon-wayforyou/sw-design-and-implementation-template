# 후보 구조 평가

| 항목 | 내용 |
|------|------|
| TraceID | DEC-002 |
| 버전 | 0.2 |
| 입력 | [CAT-001](../candidate/CAT-001-candidates.md) · [CND-001~006](../candidate/README.md) (도식·보완 설계 v0.2) |

---

## 후보별 평가

| 후보 ID | TraceID (문서) | 제목 | QA 만족 | 장점 | 단점 | 결정 | 평가 근거 |
|---------|----------------|------|---------|------|------|------|-----------|
| CA-PERF-B | CND-004 | Desktop WS + REST 폴백 | 실시간 ↑ | 저지연·Tier A | WS 연결 관리 | **채택** | QS-001·NFR-T-01 충족; REST-only(CA-PERF-A)는 폴백으로만 부분 채택 |
| CA-PERF-A | CND-004 | REST 폴링만 | 실시간 ↓ | 단순 | 지연 큼 | 폴백만 | 단독 채택 시 HTS 체감 미달 |
| CA-PERF-C | CND-004 | SyncHub 시세 델타 | Android 실시간 | 맥북·폰 일관 | 호스트 의존 | **채택** (mobile) | QS-010·012; Android는 Hub 경유 보조 |
| CA-SEC-A+C | CND-005 | RiskGuard + ApprovalGate | 안전 5/5 | 경계 명확 | 코드량 | **채택** | QS-002~004; OPA(CA-SEC-B) 대비 유지보수 적합 ([DEC-001](DEC-001-decisions.md) X-04) |
| CA-SEC-B | CND-005 | OPA/Cedar 외부 정책 | — | 유연 | 솔로 과도 | **기각** | 개인 앱 규모·운영 부담 |
| CA-ML-A | CND-003 | LSTM BC RNN | 재현·설명 | 구현 현실적 | 수익 미보장 | **채택** | ADR-002·UC-007; QS-008, 011 |
| CA-ML-B | CND-003 | Transformer | — | 표현력 | 데이터·설명 | **기각** v1 | [DEC-001](DEC-001-decisions.md) X-02 |
| CA-AND-B | CND-001 | SyncHub on macOS | 보안·패리티 | 키·로직 집중 | 맥북 필요 | **채택** | ADR-001·007; QS-010, 012, 017 |
| CA-AND-A | CND-001 | Android 독립 KIS | — | 맥 없이 동작 | 키 분산·평문 리스크 | **기각** | ADR-006으로 **암호화 내장**은 별도; 상용 평문 분산(X-01) 기각 |
| CA-MOD-B | CND-002 | `trading_modes` 패키지 | 변경용이 | 모드 경계 | 리팩터 비용 | **채택** | ADR-003·005; QS 유지보수 |
| CA-MOD-A | CND-002 | GUI 비대화 | — | 단기 빠름 | 결합도 | **기각** | 장기 유지보수 |
| CA-MOD-C | CND-002 | MSA 분리 | — | — | 오버헤드 | **기각** | [DEC-001](DEC-001-decisions.md) X-03 |

---

## 품질 속성 만족도 (채택 조합)

| QA | 만족도 | 평가 근거 |
|----|--------|-----------|
| 안전 | **높음** | RiskGuard(RG-01~09) + ApprovalGate(기본 On 승인) → QS-002~004, 013 |
| 보안 | **높음** | `secrets.enc`·Hub 토큰·감사 → QS-009, 017~018; [SEC-001](../security/SEC-001-threat-model-and-controls.md) |
| 실시간 | **중~높음** | WS+REST; HTS 100%·틱 단위 **비보장** 명시 ([SYS-001](../SYS-001-system.md) C-04) |
| 신뢰성 | **중~높음** | 401·CB·멱등(상용 QS-015~016); v1 구현 예정 |
| AI | **중** | BC+RNN; paper 검증·무승인 기본 Off → QS-004, 011, 020 |
| Android | **중** | SyncHub 패리티; 네이티브 HTS 성능 아님 (C-07) |

---

## QEV-001과의 연결

후보 채택 결과는 품질 시나리오 선정으로 내려간다 → [QEV-001](../quality/QEV-001-evaluations.md).

**다음**: [DEC-001-decisions.md](DEC-001-decisions.md)
