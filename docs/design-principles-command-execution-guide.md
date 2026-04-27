# 설계 커맨드 실행 순서·에이전트 지시 가이드

**목적**: `.cursor/commands/design-principles/*` 커맨드를 **전부 한 번씩** 활용해, 단위 프로젝트(예: `services/my-api/`)의 **`docs/`** 아래에 정돈된 설계·아키텍처 산출물을 만든다.  
**근거 워크플로**: [`.cursor/rules/design-principles/workflow.md`](../.cursor/rules/design-principles/workflow.md) Phase 1~8.  
**산출 위치**: [design-principles-architecture-under-docs.mdc](../.cursor/rules/design-principles-architecture-under-docs.mdc) — 본문 설계는 **`{단위 루트}/docs/`** 만 사용한다(`spec/` 등 병렬 최상위 금지).

---

## 1. 일반적인 설계·아키텍처 문서가 갖추면 좋은 순서 (독자 관점)

독자가 **한 번에 맥락을 잡도록** 아래 순서로 최종 패키지를 구성하는 것을 권장한다. (파일명은 프로젝트에 맞게 조정; 선택으로 `DESIGN-INTEGRATED.md` 허브를 `docs/`에 둔다.)

| 순서 | 독자가 얻는 것 | 대표 산출물(관례) |
|------|----------------|-------------------|
| 1 | **왜 이 시스템인가** — 목적·경계·In/Out | `system.md` |
| 2 | **무엇을 위해** — 비즈니스 목표·이해관계자 | `business.md` |
| 3 | **무엇을 할 수 있는가** — 기능·UC 목록 | `usecases.md` → `usecase/UC-*.md` |
| 4 | **내부가 어떻게 나뉘는가** — 컴포넌트·책임 | `domain/model.md` |
| 5 | **얼마나 좋아야 하는가** — 품질·시나리오·우선순위 | `quality/scenarios.md`, (선택) `qualities.md` |
| 6 | **무슨 기술을 쓸지** — 후보·비교·선택 | `candidate/candidates.md`, `candidate/solutions.md`, **ADR** |
| 7 | **어떻게 배포·운영하는가** | `deployment.md` |
| 8 | **구조 한 장** — 인터페이스·비기능·뷰 | `architecture.md` |
| 9 | **결정의 근거** — 채택/기각 | `adr/*`, (선택) `decision/*` |
| 10 | **통합 허브**(선택) | `DESIGN-INTEGRATED.md` |

**시각 자료**: 절이 무거우면 `.cursor/agents/doc-image-designer.md`에 “이 절의 한 줄 목표 + 배치”를 지시해 Mermaid·이미지 브리프를 넣는다.  
**제출용 PDF**: `.cursor/agents/design-pdf-publisher.md`로 매니페스트·검수 후보낸다.

---

## 2. Phase ↔ 커맨드 대응 (요약)

| Phase | 주제 | 해당 커맨드(아래 표 번호 구간) |
|-------|------|----------------------------------|
| 1 | 시스템·비즈니스 | ①② |
| 2 | UC | ③④ |
| 3 | 도메인 | ⑤ |
| 4 | 품질 | ⑥⑦⑧⑨ |
| 5 | 후보(성능·변경용이·MSA·솔루션·프레임워크·패키지) | ⑩⑪⑫⑬⑭⑮ |
| 6 | 후보 평가·모듈·배포 초안 | ⑯⑰⑱ |
| 7 | 구조 명세 통합 | ⑲ |
| 8 | 구조 분석·평가 | ⑳㉑ |
| 구현 준비 | 작업 배정·코드 | ㉒㉓ |

---

## 3. 커맨드 전체 실행 순서 (23개, 전후 관계 반영)

**공통 전제**: Cursor에서 **단위 프로젝트 루트**(예: 모노레포의 `services/foo/`)를 작업 디렉터리로 두고, 각 커맨드 실행 시 에이전트에게 **같은 루트의 `docs/`** 에만 쓰라고 명시한다.

---

### ① `/design-principles/define-system`

| 항목 | 내용 |
|------|------|
| **선행** | 없음 |
| **에이전트 지시(예시)** | “`system-definer` 역할로 본 프로젝트의 목적·경계(In/Out)·주요 액터·제약을 정리해 `docs/system.md`에만 작성한다. 다른 파일은 수정하지 않는다.” |
| **산출** | `docs/system.md` |
| **후행** | ② |

---

### ② `/design-principles/analyze-business`

| 항목 | 내용 |
|------|------|
| **선행** | ① |
| **에이전트 지시** | “`business-analyzer`로 `system.md`와 정렬되는 비즈니스 목표·드라이버·이해관계자를 `docs/business.md`에 작성한다.” |
| **산출** | `docs/business.md` |
| **후행** | ③ |

---

### ③ `/design-principles/extract-usecases`

| 항목 | 내용 |
|------|------|
| **선행** | ①② |
| **에이전트 지시** | “`usecase-extractor`로 `system.md`·`business.md`에서 UC 목록·ID·우선순위를 `docs/usecases.md`에 정리한다.” |
| **산출** | `docs/usecases.md` |
| **후행** | ④ |

---

### ④ `/design-principles/specify-usecase`

| 항목 | 내용 |
|------|------|
| **선행** | ③ |
| **에이전트 지시** | “`usecase-specifier`로 `usecases.md`의 **주요 UC마다** `docs/usecase/UC-*.md`를 작성한다. 액터·전제/사후·기본/대안 흐름을 빠짐없이 넣는다.” |
| **산출** | `docs/usecase/*.md` |
| **후행** | ⑤ |

---

### ⑤ `/design-principles/design-domain`

| 항목 | 내용 |
|------|------|
| **선행** | ④ (③ 최소) |
| **에이전트 지시** | “`domain-modeler`로 UC와 연결된 논리 컴포넌트·책임·데이터 흐름을 `docs/domain/model.md`에 통합한다. (프로젝트가 `domain/UC-*.md`를 쓰면 그다음 통합 단계를 명시한다.)” |
| **산출** | `docs/domain/model.md` |
| **후행** | ⑥ |

---

### ⑥ `/design-principles/elicit-scenarios`

| 항목 | 내용 |
|------|------|
| **선행** | ①②③ |
| **에이전트 지시** | “`quality-elicitor`로 품질 시나리오(식별자·속성·측정 힌트)를 `docs/quality/scenarios.md`에 도출한다.” |
| **산출** | `docs/quality/scenarios.md` |
| **후행** | ⑦(선택) → ⑧ |

---

### ⑦ `/design-principles/specify-scenario`

| 항목 | 내용 |
|------|------|
| **선행** | ⑥ |
| **에이전트 지시** | “`quality-specifier`로 `scenarios.md`에서 뽑은 **중요 시나리오**를 `docs/quality/QS-*.md`로 상세화한다. 생략 시 `scenarios.md`에 흡수했다고 한 줄 남긴다.” |
| **산출** | `docs/quality/QS-*.md`(선택) |
| **후행** | ⑧ |

---

### ⑧ `/design-principles/evaluate-scenarios`

| 항목 | 내용 |
|------|------|
| **선행** | ⑥ (⑦ 선택) |
| **에이전트 지시** | “`quality-evaluator`로 시나리오별 중요도·난이도·영향을 평가해 `docs/quality/evaluations.md` 또는 프로젝트 관례 파일에 기록한다.” |
| **산출** | `docs/quality/evaluations.md` 등 |
| **후행** | ⑨ |

---

### ⑨ `/design-principles/select-scenarios`

| 항목 | 내용 |
|------|------|
| **선행** | ⑧ |
| **에이전트 지시** | “`quality-selector`로 회귀·SLO에 넣을 우선 시나리오를 고른 뒤 `docs/qualities.md`에 반영한다(프로젝트가 `selected-scenarios.md`만 쓰면 그 파일로 대체 가능—일관되게 한 곳만 정본으로).” |
| **산출** | `docs/qualities.md` 또는 동등 |
| **후행** | ⑩~⑮(병렬 가능하나 아래는 순차 권장) |

---

### ⑩ `/design-principles/design-performance`

| 항목 | 내용 |
|------|------|
| **선행** | ⑤⑨ |
| **에이전트 지시** | “`performance-architect`로 성능 관련 품질 목표에 맞는 **후보 구조**를 `docs/candidate/` 이하(예: `QS-*` 또는 요약 절)에 작성한다.” |
| **산출** | `docs/candidate/*`(성능) |
| **후행** | ⑯ 전 `candidates.md` 정리 시 병합 |

---

### ⑪ `/design-principles/design-modifiability`

| 항목 | 내용 |
|------|------|
| **선행** | ⑤⑨ |
| **에이전트 지시** | “`modifiability-architect`로 변경 용이성 관점 후보를 `docs/candidate/`에 추가한다.” |
| **산출** | `docs/candidate/*` |
| **후행** | ⑯ |

---

### ⑫ `/design-principles/design-msa`

| 항목 | 내용 |
|------|------|
| **선행** | ⑤⑨ |
| **에이전트 지시** | “`msa-architect`로 서비스 분할·통합 관점의 후보(단일 모놀리스 vs 다중 서비스)를 비교하고 `docs/candidate/` 또는 `docs/msa-notes.md`에 맞게 기록한다.” |
| **산출** | 후보 메모·`candidate/` |
| **후행** | ⑯ |

---

### ⑬ `/design-principles/select-solutions`

| 항목 | 내용 |
|------|------|
| **선행** | ⑤⑨, 후보 초안(⑩⑪⑫ 중 일부) 권장 |
| **에이전트 지시** | “`solution-architect`로 DB·캐시·메시징 등 **기술 솔루션** 후보를 비교하고 `docs/candidate/solutions.md`·`docs/candidate/candidates.md`를 갱신한다. 구체 코드는 쓰지 않는다.” |
| **산출** | `docs/candidate/solutions.md`, `candidates.md`, `CA-*.md` |
| **후행** | ⑯ |

---

### ⑭ `/design-principles/select-frameworks`

| 항목 | 내용 |
|------|------|
| **선행** | ⑤⑨, ⑬ 권장 |
| **에이전트 지시** | “`framework-architect`로 런타임·웹 프레임워크 후보를 비교하고, 채택 방향을 `docs/frameworks.md` 또는 ADR 후보로 정리한다.” |
| **산출** | `docs/frameworks.md` 등 |
| **후행** | ⑮ 또는 ⑯ |

---

### ⑮ `/design-principles/design-packages`

| 항목 | 내용 |
|------|------|
| **선행** | ⑤, ⑭ 권장 |
| **에이전트 지시** | “`package-architect`로 패키지·레이어 후보를 `docs/packages.md` 또는 `docs/candidate/`에 명세한다.” |
| **산출** | `docs/packages.md` 등 |
| **후행** | ⑯ |

---

### ⑯ `/design-principles/evaluate-candidates`

| 항목 | 내용 |
|------|------|
| **선행** | ⑩~⑮로 `docs/candidate/candidates.md`가 채워져 있어야 함 |
| **에이전트 지시** | “`candidate-evaluator`로 `candidate/candidates.md`의 후보를 평가해 `docs/decision/evaluations.md`에 장단점·만족도를 적고, 상충 시 비교 결론을 낸다. (ADR로만 고정한 프로젝트는 ‘ADR 인덱스와 매핑’으로 대체 가능하다고 명시한다.)” |
| **산출** | `docs/decision/evaluations.md` |
| **후행** | `decision/decisions.md` 수동 정리 또는 ADR 채택 후 ⑰ |

---

### ⑰ `/design-principles/integrate-deployment`

| 항목 | 내용 |
|------|------|
| **선행** | ⑯에서 채택 방향이 보일 것(또는 기존 ADR) |
| **에이전트 지시** | “`system-architect`로 배치·런타임·데이터 볼륨을 `docs/deployment.md`에 쓴다. 커맨드 기본 경로가 `architecture/deployment.md`이면 **본 프로젝트 규칙에 맞게 `docs/deployment.md`로** 맞춘다.” |
| **산출** | `docs/deployment.md` |
| **후행** | ⑱ |

---

### ⑱ `/design-principles/integrate-module`

| 항목 | 내용 |
|------|------|
| **선행** | ⑯⑰ |
| **에이전트 지시** | “`module-architect`로 채택 구조를 반영한 모듈·레이어·의존성을 `docs/module.md` 또는 `docs/module-integration.md` 등 **단일 정본 파일**에 적는다.” |
| **산출** | `docs/module.md` 등 |
| **후행** | ⑲ |

---

### ⑲ `/design-principles/specify-architecture`

| 항목 | 내용 |
|------|------|
| **선행** | ①~⑱의 관련 산출이 존재할 것 |
| **에이전트 지시** | “`architecture-specifier`로 **`docs/architecture-specification.md`**(종합 구조 설계서)에 시스템 개요·요약·최종 구조·주요 다이어그램·비기능·제약을 **한 문서로 통합**한다. [`architecture.md`](./architecture.md)는 구조·CRUD·모듈 경계 **정본**으로 두고, 본 산출에서는 중복 서술을 최소화하며 UC·품질·후보·배포·모듈·ADR·`validation.md`는 **교차 참조**한다.” |
| **산출** | `docs/architecture-specification.md` |
| **후행** | ⑳ — 여기서 `doc-image-designer`로 그림 보강 가능 |

---

### ⑳ `/design-principles/analyze-architecture`

| 항목 | 내용 |
|------|------|
| **선행** | ⑲ |
| **에이전트 지시** | “`architecture-analyzer`로 `architecture.md`에서 구조적 의사결정을 추출해 `docs/architecture-analysis.md` 또는 `docs/evaluation/decisions.md` 관례 경로에 정리한다.” |
| **산출** | 분석 노트 |
| **후행** | ㉑ |

---

### ㉑ `/design-principles/evaluate-architecture`

| 항목 | 내용 |
|------|------|
| **선행** | ⑳, 품질 산출(⑥~⑨) |
| **에이전트 지시** | “`architecture-evaluator`로 구조 결정이 품질 시나리오를 만족하는지 갭을 `docs/architecture-evaluation.md`에 적고, 미충족 시 ADR 또는 로드맵 항목으로 연결한다.” |
| **산출** | `docs/architecture-evaluation.md` 등 |
| **후행** | ㉒ |

---

### ㉒ `/design-principles/assign-worker`

| 항목 | 내용 |
|------|------|
| **선행** | ⑲⑰⑱ |
| **에이전트 지시** | “`work-assigner`로 모듈·경로별 담당과 상태를 `docs/work-assignments.md`에 두고, 구현 저장소 루트에 **`AGENTS.md`** 가 필요하면 생성한다(설계 본문은 여전히 `docs/`만).” |
| **산출** | `docs/work-assignments.md`, (선택) `AGENTS.md` |
| **후행** | ㉓ |

---

### ㉓ `/design-principles/generate-code`

| 항목 | 내용 |
|------|------|
| **선행** | ㉒, 모듈·배포 명세가 있을 것 |
| **에이전트 지시** | “`code-generator`로 **설계에 허가된 모듈만** 스캐폴딩한다. 설계 문서와 다른 추측 구현은 금지. 산출은 소스 트리이며 `docs/` 밖이다.” |
| **산출** | 소스 코드 |
| **후행** | 없음(또는 CI·리뷰 루프) |

---

## 4. 병렬로 줄일 수 있는 구간

- **⑩⑪⑫**: 서로 다른 품질 관점 후보 — 인력이 나뉘면 병렬 실행 후 **한 번에 `candidate/candidates.md`를 합친다**.  
- **④**: UC별 `usecase-specifier` 병렬 가능.  
- **⑦**: QS 파일 병렬 가능.

---

## 5. 산출물 정리 시 (참고)

- 통합 허브(선택): `docs/DESIGN-INTEGRATED.md` — ⑲ 이후 **허브에 링크·상태 표**를 갱신하면 “최종 패키지” 읽기 순서와 맞는다.  
- 기술 솔루션 후보: `docs/candidate/solutions.md` — ⑬의 결과물.  
- 배포: `docs/deployment.md`(⑰와 경로 정렬).  
- ADR이 `decision/decisions.md` 역할을 대신하는 경우 ⑯ 산출을 **ADR 목록과 매핑 표**로 대체해도 된다.

---

## 6. 체크리스트 (한 사이클 종료 시)

- [ ] `docs/` 아래에 §1 표의 **독자 순서**로 읽을 수 있는가?  
- [ ] `workflow.md` Phase 1~8에 해당하는 산출이 **빈 칸 없이 링크**되는가?  
- [ ] 위 **①~㉓ 커맨드를 모두** 실행·기록(로그 또는 PR 설명)했는가?  
- [ ] 제출용 PDF가 필요하면 `design-pdf-publisher`로 **전수 검수** 후 저장했는가?
