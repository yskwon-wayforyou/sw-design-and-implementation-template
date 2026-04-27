# 소프트웨어 설계·구현 가이드 (Cursor 템플릿)

이 저장소는 **설계 방법론**을 Cursor의 **Rules · Commands · Skills**로 묶어, 새 제품·서비스를 **문서(`docs/`) → 구조 → 코드** 순으로 진행할 때 재사용하기 위한 **템플릿**이다.

---

## 1. 템플릿에 포함된 것

| 경로 | 역할 |
|------|------|
| `.cursor/commands/design-principles/` | 단계별 설계 커맨드 (`/design-principles/...`) |
| `.cursor/rules/design-principles/` | 워크플로·에이전트 역할 RULE (`workflow.md`, `*-architect/RULE.md` 등) |
| `.cursor/rules/*.mdc` | 산출 위치(`docs/`), 필수 산출물, 배포 문서 목차, 전역 vs 프로젝트 룰, 협업 원칙 등 |
| `.cursor/skills/` | ADR 작성, 폴더 단위 설명 문서 패키징 |
| `docs/design-principles-command-execution-guide.md` | 커맨드 **①~㉓** 실행 순서·에이전트 지시 예시 |

---

## 2. 새 저장소(또는 기존 모노레포)에 적용하는 방법

### 2.1 이 템플릿을 복사할 위치

- **단일 제품 저장소**: 저장소 루트에 `.cursor`를 그대로 두거나, 이 템플릿의 `.cursor` 내용을 **대상 저장소 루트 `.cursor/`**에 복사한다.
- **모노레포**: **단위 프로젝트 루트**(예: `services/billing-api/`)마다 `docs/`와 함께 쓸 계획이면, **그 루트**에 `.cursor`를 복사하거나, 루트 `.cursor`를 공유하되 커맨드 실행 시 **작업 디렉터리**를 항상 해당 단위 루트로 맞춘다.

### 2.2 VS Code / Cursor 설정

단위 프로젝트의 설계 산출 경로를 에디터에 알려 준다.

1. `.vscode/settings.json`에 다음을 넣는다(경로는 단위 루트에 맞게 수정).

```json
{
  "designPrinciples.architectureDirectory": "docs"
}
```

모노레포에서 단위가 `services/foo`이면 값은 `"services/foo/docs"`처럼 **해당 모듈의 `docs` 폴더**로 둔다.

2. 설계 본문은 **`{단위 루트}/docs/`** 에만 둔다. `spec/` 등 **문서용 병렬 최상위 폴더를 새로 만들지 않는다**([`design-principles-architecture-under-docs.mdc`](.cursor/rules/design-principles-architecture-under-docs.mdc)).

---

## 3. 단계별 진행 — 설계(Phase 1~8)

아래는 **권장 순서**이다. 상세 지시문·산출 파일명은 [`docs/design-principles-command-execution-guide.md`](docs/design-principles-command-execution-guide.md)를 정본으로 한다.

### Phase 개요

```mermaid
flowchart LR
  P1[1 시스템·비즈니스]
  P2[2 유스케이스]
  P3[3 도메인]
  P4[4 품질]
  P5[5 후보·기술]
  P6[6 평가·모듈·배포]
  P7[7 구조 통합]
  P8[8 분석·평가]
  Impl[구현]
  P1 --> P2 --> P3 --> P4 --> P5 --> P6 --> P7 --> P8 --> Impl
```

### 3.1 Phase 1 — 시스템·비즈니스

| 단계 | 커맨드(예) | 산출 |
|------|------------|------|
| ① | `/design-principles/define-system` | `docs/system.md` |
| ② | `/design-principles/analyze-business` | `docs/business.md` |

### 3.2 Phase 2 — 유스케이스

| 단계 | 커맨드 | 산출 |
|------|--------|------|
| ③ | `/design-principles/extract-usecases` | `docs/usecases.md` |
| ④ | `/design-principles/specify-usecase` | `docs/usecase/UC-*.md` |

### 3.3 Phase 3 — 도메인

| 단계 | 커맨드 | 산출 |
|------|--------|------|
| ⑤ | `/design-principles/design-domain` | `docs/domain/model.md` |

### 3.4 Phase 4 — 품질

| 단계 | 커맨드 | 산출 |
|------|--------|------|
| ⑥ | `/design-principles/elicit-scenarios` | `docs/quality/scenarios.md` |
| ⑦~⑨ | `specify-scenario`, `select-scenarios`, `evaluate-scenarios` | 품질 상세·선정·평가 노트 |

### 3.5 Phase 5 — 후보·아키텍처 관점

병렬 가능한 구간이 많다. 후보 표는 `docs/candidate/` 등에 모은 뒤 한 번에 정리한다.

- ⑩ `evaluate-candidates` — ⑭ `select-frameworks` — ⑮ `design-packages` — MSA/성능/변경용이 등(가이드 표 참고).

### 3.6 Phase 6 — 평가·모듈·배포 초안

- ⑯ `evaluate-candidates` / 결정 기록  
- ⑰ `integrate-deployment` → `docs/deployment.md`  
- ⑱ `integrate-module` → `docs/module-integration.md` 등

### 3.7 Phase 7 — 구조 명세 통합

- ⑲ `/design-principles/specify-architecture` → **`docs/architecture-specification.md`**(종합 한 장) + 기존 `docs/architecture.md`와 역할 분담(가이드 ⑲절).

### 3.8 Phase 8 — 구조 분석·평가

- ⑳ `analyze-architecture` → `docs/architecture-analysis.md` 등  
- ㉑ `evaluate-architecture` → `docs/architecture-evaluation.md` 등

### 3.9 설계 마무리 체크

`docs/design-principles-command-execution-guide.md` **§6 체크리스트**를 실행한다.

---

## 4. 구현 단계(설계 이후)

설계 산출이 갖춰진 뒤에는 다음을 권장한다.

| 순서 | 활동 | 비고 |
|------|--------|------|
| 1 | **작업 분해** | `/design-principles/assign-worker` — `docs/work-assignments.md` 등 |
| 2 | **TDD** | 설계의 TC·시나리오에 맞춰 실패 테스트부터 추가 |
| 3 | **코드 스캐폴드** | `/design-principles/generate-code` — **설계에서 허가된 모듈만** 최소 구현 |
| 4 | **검증** | `docs/validation.md` 같은 **설계 대비 구현** 표를 프로젝트에 두고 갱신 |
| 5 | **CI** | `go test`, `pytest`, 빌드 등 저장소 표준에 맞게 고정 |

협업 규칙은 루트 [`collaborative-design-first.mdc`](.cursor/rules/collaborative-design-first.mdc)를 따른다(불명확하면 구현으로 들어가지 않기, 모듈 단위 허가 등).

---

## 5. ADR·설명 문서 스킬

- 구조적 결정 기록: [`.cursor/skills/adr-authoring/SKILL.md`](.cursor/skills/adr-authoring/SKILL.md)  
- 이해용 폴더 구조·Mermaid: [`.cursor/skills/folder-based-explanation-docs/SKILL.md`](.cursor/skills/folder-based-explanation-docs/SKILL.md)

---

## 6. 이 템플릿 저장소 자체를 고칠 때

- **방법론만** 바꾸는 변경은 `.cursor/`와 본 가이드에 반영한다.  
- **특정 제품명·경로**가 룰에 새어 들어가면 [`design-rules-scope-global-vs-project.mdc`](.cursor/rules/design-rules-scope-global-vs-project.mdc)에 따라 **제품 쪽 `.cursor` 또는 `docs/`**로 옮긴다.

---

## 7. 관련 파일

| 파일 | 용도 |
|------|------|
| [README.md](README.md) | 템플릿 소개·복사 방법 요약 |
| [docs/design-principles-command-execution-guide.md](docs/design-principles-command-execution-guide.md) | 커맨드 23개 전후관계·에이전트 지시문 |
| [.cursor/rules/design-principles/workflow.md](.cursor/rules/design-principles/workflow.md) | Phase 1~8 정의 |

---

*본 가이드는 템플릿 저장소의 진입 문서다. 제품별 세부 내용은 각 프로젝트의 `docs/`에만 둔다.*

---

## 8. 이 템플릿의 Git 원격

- **저장소**: [https://github.com/yskwon-wayforyou/sw-design-and-implementation-template](https://github.com/yskwon-wayforyou/sw-design-and-implementation-template)

```bash
git clone https://github.com/yskwon-wayforyou/sw-design-and-implementation-template.git
```
