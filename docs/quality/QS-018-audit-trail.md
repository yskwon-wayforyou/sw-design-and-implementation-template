# QS-018 — 금전 감사 추적

| TraceID | QS-018 |
|---------|--------|

## 자극

live 주문 제출·승인·체결·거부 전 경로.

## 응답

- `audit_events` append-only 레코드
- `trace_id`로 UI→OrderService→kis_core 상관
- DELETE/UPDATE 트리거 거부

## 허용 기대

- 금전 액션 audit 커버리지 **100%**
- 로그에 app_secret **0건**

## 측정

- E2E spy audit repository
- DB 트리거 단위 테스트
