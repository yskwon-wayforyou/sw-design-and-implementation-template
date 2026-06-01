# QS-004 — AI 승인 게이트


| 항목 | 내용 |
|------|------|
| TraceID | QS-004 |

## 자극

AI 모드에서 RNN이 BUY 신호를 낸다.

## 응답

- ApprovalRequest PENDING 생성
- 60s 내 승인 UI/푸시
- 승인 전 OrderService 호출 **0**

## 허용 기대

- `ai_auto_without_approval=false`(기본): 무승인 주문 **0건**
- `ai_auto_without_approval=true`: ApprovalGate 미호출; RiskGuard는 live에서 유지
- 승인 모드: 근거 패널 필수 필드 4종

## 측정

- 단위: ApprovalGate 상태머신; `PolicyResolver` 기본 Off
- E2E: mock Addon + spy OrderService (Off/On 각 1시나리오)
