# UC-006 — AI 자동 매매: 추론·승인·실행


| 항목 | 내용 |
|------|------|
| TraceID | UC-006 |

| 모드 | `MODE_AI` |
| 우선순위 | P1 |

## 목적

개인화 RNN이 매매 타이밍을 제안한다. **기본**은 매수·매도 직전 사용자 승인 후 실행한다. 설정에서 **승인 없이 자동**을 켤 수 있으나 **기본은 끔(Off)**.

## 사전 조건

- 배포된 RNN 아티팩트 존재 (`artifacts/models/rnn_personal/...`).
- UC-001 연결.
- `gui_settings.ai_auto_without_approval` — 기본 **`false`**.

## 기본 흐름 (승인 필요 — 기본)

**조건**: `ai_auto_without_approval == false`

1. `AiTradingAddon` 이 주기(예: 1분) 또는 이벤트(시세 갱신)마다 피처 윈도우 구성.
2. `RnnInferenceEngine` → `action ∈ {BUY, SELL, HOLD}` + `confidence` + `attribution_vector`.
3. HOLD면 종료; BUY/SELL이면 `ApprovalRequest` 생성(근거 패널 포함).
4. **ApprovalGate** — 데스크톱 모달 + Android 푸시(UC-010); TTL 기본 60s (`ai_approval_ttl_sec`).
5. Investor: 승인 / 거부 / 만료.
6. 승인 시 → RiskGuard(live 확인 포함) → OrderService.
7. EventStore: `ai_proposal`, `ai_approval`, `order_*`.

## 대안 흐름

**A1 — 승인 없이 자동 (설정 On)**

**조건**: `ai_auto_without_approval == true`

1. 1~2번 동일.
2. BUY/SELL 시 **ApprovalGate 생략**.
3. EventStore: `ai_proposal`, `ai_auto_executed` (승인 생략 사유: 설정).
4. RiskGuard → OrderService (live는 RG-01 확인 대화상자 **유지**).

**A2 — 설정을 On으로 바꿀 때**

1. UI 경고: 「승인 없이 주문됩니다」.
2. 확인 시 저장 + `ai_policy_change` 감사 이벤트.

## 근거 패널 (ASR-005)

승인 모드(기본)에서 필수. 무승인 On일 때는 주문 **직전 알림**(선택)에 동일 요약 제공 권장.

| 필드 | 설명 |
|------|------|
| 신뢰도 | softmax 확률 |
| 유사 과거 패턴 | Tier3 최근 k건 유사도 |
| 피처 기여 | 상위 3 피처 이름·값 |
| 데이터 시각 | 피처 스냅샷 UTC |

## 예외

- 모델 로드 실패 → AI 모드 비활성 배너.
- 승인 모드에서 TTL 만료 → `expired`, 주문 없음.

## 비기능

- ASR-004 (기본 Off), ASR-005, ASR-009
- 승인 요청 → UI 표시 ≤ 2s (로컬)

## 추적

- [design-owner-feedback.md](../FBK-001-design-owner-feedback.md), [ADR-004](../adr/ADR-004-ai-auto-without-approval-setting.md)
