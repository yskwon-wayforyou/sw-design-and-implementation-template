---
name: ai-specialist-system-design
description: AI 전문가(SWO) 관점의 시스템 설계—추론·운영 이중 품질, 가드레일, 침묵하는 실패, 데이터 품질, 응용 유형별 QA 우선순위. WHEN AI 시스템 설계, LLM RAG 에이전트, MLOps 품질, 고영향 AI, 공정성 프라이버시 설명가능성, silent failure, 품질 trade-off, AI 품질 속성.
---

# AI 전문가(SWO) 시스템 설계 스킬

## 언제 쓰는가

- `system.md`·`business.md`에 **학습·추론·RAG·에이전트·온디바이스 AI** 등이 등장한다.
- 품질 논의가 **공정성·프라이버시·설명 용이성·강건성·제어 가능성** 등 AI 특화 속성으로 확장되어야 한다.
- **고영향 AI**(채용·금융·의료·안전 필수) 규제·준법과 성능의 균형을 설계 문서에 남겨야 한다.

## 반드시 읽을 룰·문서

1. `.cursor/rules/design-principles-ai-system-quality.mdc` — AI 품질 속성 정의·산출 연계.
2. `docs/ai_sw_design_methodology.md` — 본 스킬의 개념 정본(강의 자료와 정렬된 요약).
3. 기존 설계 룰: `design-principles-project-deliverables.mdc`, `design-principles-persist-docs-each-prompt.mdc`.

## 설계 시 체크리스트 (요약)

| 구분 | 해야 할 일 |
|------|------------|
| 범위 식별 | 추론 파이프라인(데이터 준비→입력 가드레일→서빙→출력 가드레일→운영)과 개발 파이프라인(학습·등록·평가)을 `system.md` 또는 `architecture.md`에 명시 |
| 품질 이중 초점 | **추론 중심 QA**(기능 정확성·강건성·프라이버시·공정성·수행 효율성)와 **운영 중심 QA**(기능 적응성·제어 가능성·설명 용이성)를 `quality/scenarios.md` Utility Tree에 **루트 분기**로 넣는다 |
| 데이터 품질 | 라벨·분포·드리프트·편향 완화가 **별도 QS**로 측정 가능하게 잡히는지 확인 |
| 침묵하는 실패 | 확률적 오류·과신·드리프트·물리/도메인 규칙 위반이 **로그 없이** 통과하지 않도록 모니터링·가드레일·휴먼 인 더 루프를 시나리오화 |
| 응용 유형 | 하이퍼퍼스널라이제이션·인지/지각·생성형·예측·에이전트 등 **유형별 QA 우선순위**를 `docs/ai_quality_profile.md`(선택) 또는 `qualities.md` 서두에 한 표로 고정 |
| Trade-off | 정확도↔공정성·정확도↔프라이버시·정확도↔설명성·품질 강화↔수행 효율성 충돌 시 **완화 전략**(XAI, PETs, 압축, 임계 재조정 등)을 ADR 후보로 남긴다 |
| 전 주기 마무리(㉑A) | `DESIGN-INTEGRATED.md`·`architect-overview.md`에 AI 산출·가드레일·품질 표가 링크되는지 확인 |

## 에이전트 매핑

- `quality-elicitor` — Utility Tree에 AI 분기·데이터 품질·silent failure 시나리오 포함.
- `quality-specifier` — 확률 출력·가드레일·드리프트 측정을 환경-동작-측정으로 명세.
- `quality-selector` — 준법·안전 NFR 잠금 후 QA 우선순위; 응용 유형 표 반영.
- `quality-evaluator` — salient failure 노출도·모니터링 커버리지를 평가 축에 추가.

## 금지·주의

- 강의 PDF 원문을 저장소에 **복제·전부 인용**하지 않는다. 개념은 `docs/ai_sw_design_methodology.md`에 **요약·재구성**만 한다.
- 제품별 데이터·모델 가중치는 **고객 `docs/`**에만 둔다.
