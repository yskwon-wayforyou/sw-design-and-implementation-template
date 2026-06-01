# 후보 구조 — 보안·안전 (QS-002~004, 009)


| 항목 | 내용 |
|------|------|
| TraceID | CND-005 |

## 후보 A: RiskGuard 단일 모듈 (현행 확장)

- 규칙 체인 인터페이스 `RiskRule`
- OrderService 진입 전 필수

## 후보 B: 정책 엔진 OPA/Cedar 외부

- **기각 후보**: 개인 앱 과도

## 후보 C: AI ApprovalGate 별도 서비스

- `ApprovalGate` 상태머신 + EventStore
- OrderService와 분리

## 권고

- **A + C** 채택: RiskGuard(주문) + ApprovalGate(AI)
