# ADR-011: Android 음성·자연어(NL) 매매 명령

| 상태 | Accepted |
|------|----------|
| TraceID | ADR-011 |
| 날짜 | 2026-06-02 |
| UC | [UC-013](../usecase/UC-013-voice-nl-trading-android.md) |

## Context

Android에서 **음성** 또는 **자연어 텍스트**로 매매 의도를 입력한다. AI RNN(UC-006)과 달리 **사용자 발화의 명시적 해석**이며, 오인·악의 입력에 대한 안전장치가 필요하다.

## Decision

| 항목 | 결정 |
|------|------|
| 플랫폼 | **Android 우선**; macOS는 v1.1 동일 API 재사용 가능 |
| ASR | **Android `SpeechRecognizer` 온디바이스** 1차; 클라우드 ASR은 설정 Off·v2 |
| NLU v1 | **규칙+슬롯** 한국어 패턴 (`trading_modes/nl_command/`) |
| NLU v2 | FinGPT/소형 LLM **의도 JSON** (선택, Hub 배치) — [ADR-010](ADR-010-open-ml-data-and-crossmodal-training.md) |
| 실행 경로 | `ParsedTradeIntent` → **확인 화면 필수** → `OrderService` (UC-002 동일) |
| AI 모드 | 음성/NL은 **RNN 자동 실행 대체 아님**; `propose` 경로와 분리 |
| Hub | `POST /nl/parse`, `POST /nl/confirm` — [INT-001](../implementation/INT-001-module-interfaces.md) |
| 감사 | `nl_parse`, `nl_confirm`, `voice_metadata` (전사문 **기본 미저장**) |
| live | RiskGuard + **읽어주기(TTS) 확인** 권장 |

## Options considered

1. **음성 → 즉시 주문** — 기각 (오인 체결)
2. **규칙 NLU + 확인** — **채택 v1**
3. **전면 LLM 에이전트** — v2; 승인·확인 유지
4. **iOS 동시** — 범위 밖

## Consequences

- `RECORD_AUDIO` 권한·프라이버시 고지
- UC-010 패리티 체크리스트에 음성/NL 항목 추가
- [QS-021](../quality/QS-021-voice-nl-safety.md) Must

## Links

- [UI-006](../ui/UI-006-android-voice-nl.md)
- [DOM-013](../domain/DOM-013-voice-nl-domain.md)
