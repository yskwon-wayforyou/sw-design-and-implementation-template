# 후보 구조 평가

| 후보 | QA 만족 | 장점 | 단점 | 결정 |
|------|---------|------|------|------|
| TraceID | DEC-002 |
| CA-PERF-B (WS+REST) | 실시간 ↑ | 저지연 | 연결 관리 | **채택** (desktop) |
| CA-PERF-A (REST only) | 실시간 ↓ | 단순 | 지연 | 폴백으로 부분 채택 |
| CA-PERF-C (SyncHub 델타) | Android 실시간 | 일관성 | 맥북 의존 | **채택** (mobile) |
| CA-SEC-A+C | 안전 5/5 | 명확 경계 | 코드량 | **채택** |
| CA-SEC-B OPA | — | — | 과도 | **기각** |
| CA-ML-A LSTM BC | 재현·설명 | 구현 현실적 | 수익 미보장 | **채택** |
| CA-ML-B Transformer | — | — | 데이터·설명 | **기각** v1 |
| CA-AND-B SyncHub | 보안·패리티 | 키 단일 | 호스트 필요 | **채택** |
| CA-AND-A 모바일 KIS | — | 독립 | 키 분산 | **기각** |
| CA-MOD-B trading_modes | 변경용이 | 리팩터 비용 | — | **채택** |
| CA-MOD-A GUI 비대 | — | 단기 빠름 | 유지보수 | **기각** |
| CA-MOD-C MSA | — | — | 오버헤드 | **기각** |

## 품질 속성 만족도 (채택 조합)

| QA | 만족도 | 근거 |
|----|--------|------|
| 안전 | 높음 | RiskGuard + ApprovalGate |
| 보안 | 높음 | 볼트 단일·SyncHub 토큰 |
| 실시간 | 중~높음 | WS; HTS 100% 아님 명시 |
| AI | 중 | BC+RNN; paper 검증 |
| Android | 중 | SyncHub 패리티 |

**다음**: [decisions.md](DEC-001-decisions.md)
