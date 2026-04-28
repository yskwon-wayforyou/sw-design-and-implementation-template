# SW 설계·구현 템플릿 (Cursor)

설계 활동을 **Cursor Rules · Commands · Skills**로 표준화해, 새 소프트웨어를 **`docs/` 기반 설계 → 구현**까지 같은 패턴으로 진행하기 위한 **재사용 템플릿** 저장소이다.

**GitHub**: [yskwon-wayforyou/sw-design-and-implementation-template](https://github.com/yskwon-wayforyou/sw-design-and-implementation-template)

## 빠른 시작

1. 이 저장소를 **새 프로젝트에 복제**하거나, `.cursor/` 전체와 `docs/`·루트 가이드를 필요한 경로에 복사한다.  
2. [`sw_design_and_implementation_guide.md`](./sw_design_and_implementation_guide.md)를 연다.  
3. 단위 프로젝트 루트에 `docs/`를 만들고, VS Code `designPrinciples.architectureDirectory`를 그 `docs`에 맞춘다(예: `"docs"` 또는 `"services/foo/docs"`).  
4. Cursor에서 `/design-principles/define-system`부터 [`docs/design-principles-command-execution-guide.md`](./docs/design-principles-command-execution-guide.md)의 순서대로 커맨드를 실행한다.

## AI·ML 설계 트랙 (선택)

학습·추론·LLM·RAG·에이전트가 **제품 경계**에 들어가면:

- 방법론 정본: [`docs/ai_sw_design_methodology.md`](./docs/ai_sw_design_methodology.md)  
- Agent Notebook 전 주기: [`docs/agent-notebook/ai_sw_design_full_stack_workflow.aanb`](./docs/agent-notebook/ai_sw_design_full_stack_workflow.aanb) (일반 노트북과 동일 ①~㉓, 브리프·품질 Phase 보강)  
- 스킬: [`.cursor/skills/ai-specialist-system-design/SKILL.md`](./.cursor/skills/ai-specialist-system-design/SKILL.md)

일반 소프트웨어만 다룰 때는 기존 순서와 [`docs/agent-notebook/design-principles-full-stack-workflow.aanb`](./docs/agent-notebook/design-principles-full-stack-workflow.aanb)로 충분하다.

## 포함 내용

- **Commands**: `.cursor/commands/design-principles/*` · 상용 보조: `.cursor/commands/productization/*`  
- **Rules**: `.cursor/rules/design-principles/**` + 공통 `.mdc`(예: `design-principles-ai-system-quality`, `persist-docs-each-prompt`)  
- **Skills**: `adr-authoring`, `folder-based-explanation-docs`, `ai-specialist-system-design`, `python-qt6-commercial-app`(샘플용)  
- **실행 순서 정본**: `docs/design-principles-command-execution-guide.md`  
- **샘플**: [`samples/README.md`](./samples/README.md)

라이선스·기여 정책은 저장소 소유자가 추가하면 된다.
