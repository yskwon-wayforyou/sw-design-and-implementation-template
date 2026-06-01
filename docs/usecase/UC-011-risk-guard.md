# UC-011 — RiskGuard 및 실전 안전장치


| 항목 | 내용 |
|------|------|
| TraceID | UC-011 |

| 우선순위 | P0 |

## 목적

실계좌·AI·자동화 경로에서 오주문·한도 초과·프로필 오류를 차단한다.

## 규칙 (v1 + 상용)

| ID | 규칙 |
|----|------|
| RG-01 | live 주문 전 확인 대화상자 |
| RG-02 | paper URL/키 혼선 기동 거부 |
| RG-03 | (선택) 일일 주문 금액/횟수 한도 |
| RG-04 | AI: 기본 승인 필수 |
| RG-05 | Addon 직접 OrderService 호출 금지 |
| RG-06 | `AST_DISABLE_LIVE` / `live_trading_enabled=false` 존중 |
| RG-07 | live + 시세 stale(기본 `as_of` > 5s) → **DENY** |
| RG-08 | 동일 `client_order_id` 중복 → **DENY** |
| RG-09 | KIS Circuit **OPEN** → 주문 **DENY**(fail-fast) |

상세: [ARC-004](../architecture/ARC-004-resilience-security-crosscut.md), [QLT-002](../QLT-002-commercial-quality-baseline.md)

## 기본 흐름

1. 주문·AI 실행 요청이 `RiskGuard.evaluate(context)` 진입.
2. 규칙 체인 실행 → `ALLOW` | `DENY` | `CONFIRM`.
3. CONFIRM 시 UI; DENY 시 로그.

## 추적

- NFR-01, NFR-02, ASR-002~004, ASR-015~022
