# QS-015 — 주문 멱등성

| TraceID | QS-015 |
|---------|--------|

## 자극

네트워크 타임아웃 후 동일 주문 재시도.

## 응답

- 동일 `client_order_id` 재전송
- KIS 중복 또는 로컬 RG-08 거부
- 감사 1건의 최종 상태

## 허용 기대

- 이중 체결 **0건**
- UI에 단일 주문 상태

## 측정

- mock: 첫 요청 timeout, 재시도 success
- audit duplicate count = 0
