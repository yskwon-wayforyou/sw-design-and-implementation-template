# UC-006 도메인 분석 — AI 자동·승인


| 항목 | 내용 |
|------|------|
| TraceID | DOM-006 |

## 정책 분기

```mermaid
flowchart TD
  infer[RNN_infer_BUY_SELL]
  setting{ai_auto_without_approval}
  gate[ApprovalGate]
  rg[RiskGuard]
  os[OrderService]

  infer --> setting
  setting -->|"false 기본"| gate
  gate -->|approved| rg
  setting -->|true| rg
  rg --> os
```

## 컴포넌트 상호작용 (기본: 승인 On)

```mermaid
sequenceDiagram
  participant Addon as AiTradingAddon
  participant RNN as RnnInferenceEngine
  participant Gate as ApprovalGate
  participant RG as RiskGuard
  participant OS as OrderService
  participant ES as EventStore

  Addon->>RNN: infer(window)
  RNN-->>Addon: BUY/SELL
  Addon->>Gate: create_request
  Gate->>ES: ai_proposal
  Gate-->>Investor: notify
  Investor->>Gate: approve
  Gate->>RG: evaluate
  RG->>OS: place_order
```

## 무승인 On 시

- `ApprovalGate` 호출 없음.
- `PolicyResolver.requires_approval()` → `not settings.ai_auto_without_approval`.

## RationaleBundle

| 필드 | 소스 |
|------|------|
| top_features | attribution |
| similar_events | Tier3 k-NN |
| model_version | artifact meta |
| data_as_of | window end ts |

## 내부 동작 규칙

1. 동일 종목 PENDING 승인 중복 생성 금지 (승인 모드만).
2. HOLD 연속 N회 시 추론 주기 백오프.
3. `ai_auto_without_approval` 변경은 감사 로그 필수.
