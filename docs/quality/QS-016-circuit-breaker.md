# QS-016 — KIS Circuit Breaker

| TraceID | QS-016 |
|---------|--------|

## 자극

KIS REST가 60s 내 5xx 5회 연속.

## 응답

- CB → OPEN 30s
- 주문 즉시 거부 + 사유 코드
- 30s 후 HALF_OPEN probe (paper)

## 허용 기대

- OPEN 중 추가 KIS 호출 **최소화**(storm 방지)
- 사용자 메시지 명확

## 측정

- 단위: 상태 전이
- mock 5xx 시퀀스
