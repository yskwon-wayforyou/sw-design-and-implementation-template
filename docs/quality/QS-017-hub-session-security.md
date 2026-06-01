# QS-017 — SyncHub 세션 보안

| TraceID | QS-017 |
|---------|--------|

## 자극

LAN에서 토큰 없이 `POST /orders` 호출.

## 응답

- HTTP 401
- audit `hub_auth_fail`
- rate limit 초과 시 429

## 허용 기대

- 무토큰 주문 성공 **0건**
- 페어링 후 토큰으로만 성공

## 측정

- contract: Hub API matrix
- 토큰 만료·재페어링 시나리오
