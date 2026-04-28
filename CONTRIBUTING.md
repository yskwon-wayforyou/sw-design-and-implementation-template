# 기여 안내

이 저장소는 **설계·구현 워크플로 템플릿**이다. 변경 시 아래를 지킨다. 라이선스는 루트 [LICENSE](./LICENSE)를 본다.

## 원칙

1. **설계 본문 산출물**은 템플릿이 아니라 **각 제품 프로젝트의 `docs/`** 에만 둔다. 이 저장소에는 방법론·룰·커맨드·가이드·샘플만 넣는다.
2. 경로·용어는 [`.cursor/rules/design-principles-architecture-under-docs.mdc`](.cursor/rules/design-principles-architecture-under-docs.mdc)와 [design-principles-project-deliverables](.cursor/rules/design-principles-project-deliverables.mdc)와 맞춘다.
3. Agent Notebook(`.aanb`)을 바꿀 때는 [docs/design-principles-command-execution-guide.md](docs/design-principles-command-execution-guide.md)의 단계 번호·선행 관계와 **모순 없게** 갱신한다.

## PR 전 체크

- [ ] `docs/design-principles-command-execution-guide.md` §6 체크리스트와 어긋나지 않는가  
- [ ] 노트북 전 주기 실행 시 `docs/DESIGN-INTEGRATED.md`, `docs/architect-overview.md`가 **㉑A**로 생성되도록 유지되는가  
- [ ] 불필요한 제품명·내부 URL이 루트 규칙에 새지 않았는가 ([design-rules-scope-global-vs-project](.cursor/rules/design-rules-scope-global-vs-project.mdc))

## 이슈·질문

저장소 소유자 정책에 따라 이슈 트래커 또는 내부 채널을 사용한다.
