# QS-021 — 음성·자연어 매매 안전

| TraceID | QS-021 |
|---------|--------|
| 우선순위 | **Must** (live·paper 주문 경로) |
| UC | [UC-013](../usecase/UC-013-voice-nl-trading-android.md) |
| ADR | [ADR-011](../adr/ADR-011-android-voice-nl-trading.md) |

## 시나리오

| ID | 제목 | 자극 | 환경 | 응답 | ASR |
|----|------|------|------|------|-----|
| QS-021-N1 | 명확 매수 | 「005930 10주 매수」 | paper | 확인 화면 → 체결 | ASR-023 |
| QS-021-B1 | 최소 수량 | 1주 | paper | 성공 | |
| QS-021-A1 | 모호 종목 | 「삼성」 | — | clarify, 주문 없음 | |
| QS-021-A2 | 낮은 신뢰도 | 잡음 문장 | — | 재입력 | |
| QS-021-E1 | 확인 없이 execute API | confirm 생략 POST | — | 403 | |
| QS-021-E2 | live stale | confirm 시 as_of>5s | live | RG-07 | |

## 허용치

- **확인 화면 생략 API**: **0건**
- parse → execute **TTL**: 120s
- confidence execute 임계: **≥0.6**
- 금지 즉시실행 키워드: 전량, all in, 비밀번호

## 검증

- 시나리오 `tests/scenario/uc_013_voice_nl/`
- Hub 통합: confirm 없이 `/nl/confirm` → 403
