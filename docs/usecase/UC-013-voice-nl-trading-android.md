# UC-013 — Android 음성·자연어 매매 명령

| 항목 | 내용 |
|------|------|
| TraceID | UC-013 |
| 우선순위 | **P1** |
| 플랫폼 | Android (SyncHub 경유); macOS v1.1 동일 API |
| ADR | [ADR-011](../adr/ADR-011-android-voice-nl-trading.md) |
| 관련 | UC-002, UC-010, UC-011, UC-006(분리) |

## 목적

투자자가 **말하거나 문장으로 입력**한 매매 의도를 시스템이 해석하고, **확인 후** 기존 주문 파이프라인으로 체결한다. AI 자동매매(UC-006)와 **별개**이다.

## 액터

Investor, SyncHub, `NlCommandService`, OrderService, RiskGuard, (선택) Android ASR/TTS

## 사전 조건

- UC-001 연결(paper 또는 live).
- UC-010 SyncHub 세션 유효 (`X-Session-Token`).
- Android: 마이크 권한(음성 시) 또는 텍스트 입력.

## 사후 조건

- 해석·확인·주문 결과가 EventStore에 기록(`nl_*`, `order_*`).
- `correlation_id` 단일 체인.

## 기본 흐름 (해피패스)

1. Investor가 **주문** 탭에서 마이크 또는 텍스트창에 「삼성전자 10주 시장가 매수」 입력.
2. (음성) Android ASR → **텍스트**만 Hub로 전송 (**음성 파일 미전송** 기본).
3. `POST /nl/parse` → `NlCommandService` 규칙/슬롯 파싱.
4. 시스템이 **확인 화면**(SCR-AND-NL-CONFIRM)에 종목·방향·수량·가격·예상 금액 표시.
5. Investor **확인** 탭.
6. `profile=live` → RiskGuard + (권장) TTS 읽기 확인.
7. `POST /nl/confirm` → `OrderService.submit` (UC-002).
8. 결과 토스트·감사.

```mermaid
sequenceDiagram
  participant And as Android
  participant Hub as ast_mobile
  participant NL as NlCommandService
  participant RG as RiskGuard
  participant OS as OrderService

  And->>And: ASR to text optional
  And->>Hub: POST nl parse text
  Hub->>NL: parse
  NL-->>And: intent preview requires_confirm
  And->>And: SCR-AND-NL-CONFIRM user OK
  And->>Hub: POST nl confirm intent_id
  Hub->>RG: evaluate
  RG->>OS: submit_order
  OS-->>And: result
```

## 대안 흐름

| ID | 조건 | 처리 |
|----|------|------|
| A1 | 종목 모호 「삼성」 | `clarification` 응답·후보 목록 UI |
| A2 | 수량/가격 누락 | 슬롯 질문 「몇 주?」 |
| A3 | paper | live 확인 생략 가능(설정); **확인 화면은 유지** |
| A4 | Hub 오프라인 | ADR-006 폰 단독 시 동일 NL 로컬(구현 v1.1) |
| A5 | 「취소」 발화 | parse → `CANCEL` intent, 주문 없음 |

## 예외

| 조건 | 처리 |
|------|------|
| 신뢰도 < 0.6 | 주문 금지·재입력 요청 |
| RG deny | 이유 표시·주문 없음 |
| stale quote (live) | RG-07 |
| 금지 패턴 「전량」「모두」「비밀번호」 | parse 거부 |

## 비기능

- [QS-021](../quality/QS-021-voice-nl-safety.md)
- ASR-023 (신규)
- ASR-012 일반 용어 확인 화면
- 전사문 저장: 기본 **Off** ([DAT-003](../data/DAT-003-data-schemas.md))

## UC-006과의 경계

| | UC-006 AI | UC-013 음성/NL |
|--|-----------|----------------|
| 트리거 | RNN/주기 | 사용자 발화 |
| 승인 | ApprovalGate(기본) | **확인 화면**(필수) |
| 근거 | 모델 attribution | 파싱 슬롯·원문(화면 only) |

## 추적

- [UI-006](../ui/UI-006-android-voice-nl.md)
- [DOM-013](../domain/DOM-013-voice-nl-domain.md)
