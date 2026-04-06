# agent_base

`agent_base`는 새 프로젝트를 시작하거나 기존 저장소에 AI 작업 규칙을 이식할 때 사용하는 `프로젝트 생성 킷 + 규칙 템플릿 패키지`다. 이 패키지는 대화형 bootstrap, scaffold 생성, pre-commit gate, 실패 학습 루프를 함께 제공한다.

이 패키지는 다음 세 가지를 함께 제공한다.

- 대화형 프로젝트 생성 절차
- 실제 터미널 대화형 bootstrap CLI
- 프로젝트 패밀리와 런타임 역할 기준의 규칙 문서
- 실제 샘플 저장소를 별도 디렉토리에 만들어보는 generator와 scaffold
- 저장 전 자동 검사를 위한 pre-commit hook pack
- agent failure를 기록하고 harness 강화로 환류하는 collector와 규약

## 무엇을 할 수 있나

- 새 프로젝트를 시작할 때 인터뷰 형식으로 생성 spec을 확정한다.
- 선택한 프로젝트 패밀리에 맞는 템플릿과 초기 문서 세트를 고른다.
- 지원되는 언어/프레임워크 조합이면 최소 실행 가능한 샘플 저장소를 생성한다.
- 생성된 저장소 안에 `AGENTS.md`, `docs/ai/*`, 체크리스트, prompt 예시를 같이 넣어 첫 build/test/문서화까지 이어갈 수 있게 한다.

## 패키지 구조

- `source/`
  - canonical authoring source
  - generator, scaffold, 공통 규칙, prompt, 예시가 여기서 관리된다
- `templates/`
  - 실제 저장소 루트에 바로 복사할 수 있는 완성형 템플릿
  - 프로젝트 패밀리 템플릿과 런타임 역할 템플릿이 함께 있다
- `checklists/`
  - 도입, 유지보수, 드리프트 점검용 체크리스트

## 시작 순서

1. [`source/AGENTS.md`](./source/AGENTS.md)를 읽는다.
2. [`source/docs/ai/project-bootstrap.md`](./source/docs/ai/project-bootstrap.md)로 인터뷰 절차를 따른다.
3. 가능하면 [`source/docs/ai/project-bootstrap-cli.md`](./source/docs/ai/project-bootstrap-cli.md)와 `source/scripts/project_bootstrap_cli.py`로 인터뷰와 spec 생성을 한 번에 수행한다.
4. [`source/docs/ai/project-generation-spec.md`](./source/docs/ai/project-generation-spec.md)로 생성 spec을 검토한다.
5. [`source/docs/ai/project-family-map.md`](./source/docs/ai/project-family-map.md)과 [`source/docs/ai/project-selection-mapping.md`](./source/docs/ai/project-selection-mapping.md)으로 적합한 템플릿과 runtime role을 정한다.
6. [`source/docs/ai/stack-matrix.md`](./source/docs/ai/stack-matrix.md), [`source/docs/ai/database-rules.md`](./source/docs/ai/database-rules.md)를 기준으로 기술 스택과 DB 기준을 확정한다.
7. [`source/docs/ai/project-generator.md`](./source/docs/ai/project-generator.md)와 [`source/docs/ai/token-substitution.md`](./source/docs/ai/token-substitution.md)를 읽고 generator를 실행한다.
8. 생성된 샘플 저장소 안에서 `python3 scripts/install_git_hooks.py`를 실행한다.
9. 생성된 샘플 저장소 안에서 `.agent-base/pre-commit-config.json`의 preset profile을 실제 명령 체계에 맞게 보정한다.
10. 생성된 샘플 저장소 안에서 `command-catalog`, `architecture-map`, `project-creation`, `first-delivery`를 실제 프로젝트에 맞게 보정한다.

## 프로젝트 패밀리 템플릿

- `game-repo`
- `web-app-repo`
- `pwa-repo`
- `mobile-app-repo`
- `backend-service-repo`
- `batch-worker-repo`
- `receiver-integration-repo`
- `mockup-local-repo`
- `library-tooling-repo`

## 런타임 역할 템플릿

- `frontend-repo`
- `api-repo`
- `batch-repo`
- `receiver-repo`

이 역할 템플릿은 상위 프로젝트 패밀리를 대체하지 않는다. 생성 후 저장소에 추가 규칙을 얹거나 역할별 오버레이를 구성할 때 사용한다.

## 실제 생성 예시

```bash
python3 ./source/scripts/project_bootstrap_cli.py \
  --output-root /tmp/generated-projects \
  --force
```

이 명령은 대화형 인터뷰를 진행한 뒤 `/tmp/generated-projects/<repositoryName>` 형태의 샘플 저장소를 만든다.

## 핵심 원칙

- canonical entry file은 항상 `AGENTS.md`
- 상세 규칙 system of record는 `docs/ai/`
- 생성은 `인터뷰 -> spec -> mapping -> generator -> 보정 -> 첫 검증` 순서로 진행
- 언어, 프레임워크, 런타임, DB 규칙은 문서 기준으로 먼저 확정
- 템플릿 복사 후에는 반드시 repo-local 명령과 환경 설정으로 보정
- 템플릿 복사 후에는 local pre-commit hook와 실패 학습 루프를 저장소 운영 기준에 맞게 활성화
- 규칙 변경은 `source/`를 먼저 수정하고 `templates/*`를 다시 동기화

## 이 패키지가 다루지 않는 것

- 실제 비즈니스 기능 구현
- 완전 자동 스캐폴딩 엔진
- 조직 고유 배포 파이프라인의 세부 절차

이런 항목은 생성된 저장소 안에서 repo-local overlay 문서나 추가 스크립트로 확장한다.
