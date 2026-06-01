# AI 품질 프로파일 — YSTrading

| 항목 | 값 |
|------|-----|
| TraceID | AIQ-001 |
| 응용 유형 | **개인화 의사결정 지원 + 조건부 자동 실행** (고영향: 금전) |
| 고영향 | **예** — live 주문 연결 |
| 필수 QA | 안전(ASR-004), 설명가능성(ASR-005), 데이터품질(Tier), 재현성(NFR-04) |
| 침묵 실패 | HOLD만 반복·저신뢰 제안 미표시 |

## Trade-off

| 축 | 선택 | 이유 |
|----|------|------|
| 수익 vs 안전 | **안전 우선** | 승인 게이트·paper 학습 |
| 자동화 vs 통제 | 승인 기본; 무승인은 설정 On(기본 Off) | 오너 피드백 2026-06-02 |
| 복잡 모델 vs 설명 | RNN + attribution | 근거 패널 |
| 실시간 추론 vs 정확 | 1분 주기 + 이벤트 트리거 | API 한도 |

## 검증

- paper 백테스트 PnL (참고, 보장 없음)
- 승인률·거부율·만료율 대시보드
- 데이터 드리프트: feature 분포 KS 검정(월 1회 배치)
- **상용**: stale 시세 시 infer/주문 차단; `data_hash` 게이트 ([QS-013](quality/QS-013-stale-quote-and-fallback.md), [QS-020](quality/QS-020-ml-data-integrity.md))
- live AI 릴리스: [QLT-002](QLT-002-commercial-quality-baseline.md) §4 게이트 G1~G5

## 관련

- UC-006, UC-007, QS-004, QS-011, QS-020
- [QLT-001](QLT-001-qualities.md), [QLT-002](QLT-002-commercial-quality-baseline.md)
- [SEC-001](security/SEC-001-threat-model-and-controls.md) §8
