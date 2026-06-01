# QS-013 — 시세 신선도·WS 폴백

| TraceID | QS-013 |
|---------|--------|

## 자극

장중 WS가 10s 단절된다.

## 응답

- 3s 내 REST 폴링 전환
- UI `as_of`·연결 상태 배지
- live 주문: `as_of` > 5s 이면 **차단**(RG-07)

## 허용 기대

- 폴백 전환 ≤ 3s (정상망)
- stale live 주문 시도 **0건**

## 측정

- 통합: mock WS drop
- E2E: paper에서 stale inject → 주문 버튼 비활성
