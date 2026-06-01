# UC-002 — HTS형 수동 주문

| 항목 | 내용 |
|------|------|
| TraceID | UC-002 |
| 우선순위 | P0 |
| 모드 | `MODE_MANUAL` |
| 액터 | Investor, KIS |

## 목적

종목·가격·수량을 입력해 매수/매도 주문을 제출하고 결과를 기록한다.

## 사전 조건

- UC-001 성공(연결됨).
- 종목 코드 유효.

## 사후 조건

- KIS에 주문 요청 전송(또는 검증 실패로 미전송).
- EventStore에 `order_request` / `order_response` 기록.
- 활동 패널에 요약 표시.

## 기본 흐름

1. Investor가 `매매·주문` 탭에서 종목·호가/지정가·수량 입력.
2. (선택) `시세 반영` 으로 현재가 채움.
3. Investor가 매수 또는 매도 클릭.
4. 시스템이 `OrderValidator` 로 수량·가격·상품코드 검증.
5. `profile=live` 이면 **RiskGuard** 확인 대화상자.
6. `OrderService` → KIS TR 호출.
7. 응답 파싱·감사 로그·UI 피드백.

## 대안 흐름

**A1 — 금액 기준 주문**

1. 금액 입력 → 시스템이 현재가로 수량 환산(내림).
2. 3번으로 합류.

**A2 — paper 모드**

- 5번 확인 생략(설정으로 optional 유지 가능).

## 예외

| 조건 | 처리 |
|------|------|
| 검증 실패 | KIS 호출 전 차단·메시지 |
| KIS 거부 | `rt_cd` 매핑 메시지 |
| 일일 한도 초과 | RiskGuard 차단 |

## 비기능

- ASR-003, FR-MVP-05, FR-MVP-06
- 주문 UI 경로: 시세 탭에서 ≤2클릭 전환 가능

## 추적

- [../doc/11-hts-ui-and-features-ko.md](../../doc/11-hts-ui-and-features-ko.md) §매매
