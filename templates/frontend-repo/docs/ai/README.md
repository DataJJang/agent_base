# Project AI Docs

이 디렉토리는 프로젝트 생성과 저장소 운영 규칙을 정의하는 상세 system of record다.

루트 진입점은 [`AGENTS.md`](../../AGENTS.md)다.

## 문서 맵

- [`architecture-map.md`](./architecture-map.md)
  - 어떤 문서가 어떤 사실의 system of record인지 정리
- [`command-catalog.md`](./command-catalog.md)
  - build, compile, test, smoke, deploy-check 명령과 기록 위치 기준
- [`core-rules.md`](./core-rules.md)
  - 공통 코딩, 데이터, 로깅, 검증, 문서화 규칙
- [`database-rules.md`](./database-rules.md)
  - 테이블, 컬럼, 약어, constraint, COMMENT, migration, 위험 SQL 기준
- [`project-bootstrap.md`](./project-bootstrap.md)
  - 새 저장소를 대화형 인터뷰로 어떻게 생성하고 첫 프롬프트를 어떻게 실행할지 정의
- [`project-adoption.md`](./project-adoption.md)
  - 기존 저장소를 inventory, adoption spec, migration plan으로 온보딩하는 절차 정의
- [`project-bootstrap-cli.md`](./project-bootstrap-cli.md)
  - 대화형 인터뷰를 실제 CLI로 실행해 spec 저장과 generator 호출까지 묶는 방법 정의
- [`project-generation-spec.md`](./project-generation-spec.md)
  - 새 저장소 생성 시 반드시 채워야 할 정규화 입력값과 산출 구조 정의
- [`adoption-spec.md`](./adoption-spec.md)
  - 기존 저장소 adoption/migration 시 채워야 할 정규화 입력값 정의
- [`project-family-map.md`](./project-family-map.md)
  - 프로젝트 패밀리와 하위 런타임 역할의 관계 정의
- [`project-selection-mapping.md`](./project-selection-mapping.md)
  - 선택값이 어떤 템플릿, 문서, 명령, 초기 산출물로 이어지는지 정의
- [`repository-inventory.md`](./repository-inventory.md)
  - 기존 저장소에서 먼저 추출해야 하는 사실, 명령, 위험 요소 정의
- [`migration-strategy.md`](./migration-strategy.md)
  - phased, shadow, dual-run, big-bang 같은 전환 전략 선택 기준 정의
- [`compatibility-matrix.md`](./compatibility-matrix.md)
  - 현재 스택과 목표 스택의 호환성, 예외, breaking point 정리
- [`legacy-exception-policy.md`](./legacy-exception-policy.md)
  - 당장 못 바꾸는 legacy 예외를 문서화하고 만료시키는 기준 정의
- [`parity-validation.md`](./parity-validation.md)
  - 기존 동작과 새 구조의 기능/계약/데이터 동등성 검증 기준 정의
- [`roles/README.md`](./roles/README.md)
  - agentic engineering에서 쓰는 역할군, 책임, handoff 기준 정의
- [`project-generator.md`](./project-generator.md)
  - 정규화된 spec으로 실제 샘플 프로젝트를 생성하는 절차와 지원 범위 정의
- [`token-substitution.md`](./token-substitution.md)
  - 생성 시 placeholder를 어떤 규칙으로 치환하는지 정의
- [`stack-matrix.md`](./stack-matrix.md)
  - 프로젝트 패밀리별 권장 언어, 프레임워크, 런타임, 버전 기준
- [`lifecycle.md`](./lifecycle.md)
  - 구축, 운영, 배포, 릴리즈, 롤백, 운영 점검
- [`document-routing.md`](./document-routing.md)
  - 어떤 내용을 어떤 문서에 둘지 결정하는 기준
- [`services/frontend.md`](./services/frontend.md)
- [`services/api.md`](./services/api.md)
- [`services/batch.md`](./services/batch.md)
- [`services/receiver.md`](./services/receiver.md)
- [`governance/quality-gates.md`](./governance/quality-gates.md)
  - Definition of Done, 리뷰 기준, 검증 기준, 보고 형식
- [`governance/git-workflow.md`](./governance/git-workflow.md)
  - 커밋 메시지 규약, 브랜치 전략, PR 기준, merge 전략
- [`governance/pre-commit-hooks.md`](./governance/pre-commit-hooks.md)
  - 저장 전 자동 검사, hook 설치, repo-local gate 설정 기준
- [`governance/agent-failure-learning.md`](./governance/agent-failure-learning.md)
  - 실패 케이스 수집, 재발 방지, harness 강화 환류 기준
- `scripts/record_agent_failure.py`
  - 실패 케이스를 `.agent-base/failure-cases/`에 JSON/Markdown으로 적재하는 helper
- `scripts/analyze_repository.py`
  - 기존 저장소에서 build/test/config/docs/runtime inventory를 추출하는 helper
- `scripts/summarize_failures.py`
  - failure-cases를 집계해 반복 실패 패턴을 요약하는 helper
- [`governance/release-and-rollback.md`](./governance/release-and-rollback.md)
  - 배포/롤백 상세 판단 기준
- [`governance/evaluation-and-drift.md`](./governance/evaluation-and-drift.md)
  - 규약 드리프트 감지, 갱신 절차, 정기 점검 기준
- [`tools/compatibility.md`](./tools/compatibility.md)
  - AGENTS, CLAUDE, GEMINI, Copilot, Cursor, Windsurf 호환 전략
- [`tools/windsurf.md`](./tools/windsurf.md)
  - Windsurf용 변환 가이드
- [`prompts/README.md`](./prompts/README.md)
  - 문서 생성 및 프로젝트 생성용 AI 프롬프트 라이브러리
- [`prompts/roles/README.md`](./prompts/roles/README.md)
  - 역할별 agent prompt template 라이브러리
- `../../checklists/`
  - 프로젝트 생성, 첫 전달, DB 변경 체크리스트
- `../../checklists/agent-role-selection.md`
  - 프로젝트별 필요한 agent 역할과 optional 역할을 고르는 체크리스트
- `../../checklists/agent-handoff.md`
  - 역할 간 handoff artifact와 미해결 이슈를 넘기는 체크리스트
- `../../checklists/agent-completion-review.md`
  - 역할 기반 작업 종료 전 완료 기준을 점검하는 체크리스트
- `../../checklists/agent-failure-review.md`
  - 실패 케이스를 규약, prompt, template, script 강화로 연결하는 체크리스트
- `examples/`
  - 산출물 샘플 출력
  - [`examples/ai-test-bootstrap-sequence.md`](./examples/ai-test-bootstrap-sequence.md)
    - 실제 `ai-test` 게임 프로젝트를 인터뷰로 생성한 흐름 예시

## 사용 순서

1. `AGENTS.md`
2. `docs/ai/project-bootstrap.md`
3. `docs/ai/project-bootstrap-cli.md`
4. `docs/ai/project-generation-spec.md`
5. 필요 시 `docs/ai/project-adoption.md`, `docs/ai/adoption-spec.md`
6. `docs/ai/project-family-map.md`
7. `docs/ai/project-selection-mapping.md`
8. `docs/ai/roles/README.md`
9. `docs/ai/project-generator.md`
10. `docs/ai/token-substitution.md`
11. `docs/ai/stack-matrix.md`
12. `docs/ai/architecture-map.md`
13. `docs/ai/core-rules.md`
14. 필요 시 `docs/ai/database-rules.md`
15. `docs/ai/lifecycle.md`
16. brownfield면 `docs/ai/repository-inventory.md`, `docs/ai/migration-strategy.md`, `docs/ai/parity-validation.md`
17. 런타임 역할별 상세 규칙
18. `docs/ai/governance/quality-gates.md`
19. `docs/ai/governance/pre-commit-hooks.md`
20. 필요 시 `docs/ai/governance/agent-failure-learning.md`
21. 필요 시 `docs/ai/prompts/roles/*`
22. 필요 시 `docs/ai/document-routing.md`, `docs/ai/prompts/*`, `checklists/*`

## 기본 원칙

- 이 디렉토리의 문서는 상세 규칙 문서다.
- 저장소별 개별 규약은 이 상세 문서를 바탕으로 오버레이 방식으로 만든다.
- 루트 엔트리 파일은 짧게 유지하고, 긴 규칙은 여기에서 관리한다.
- DB를 소유하는 저장소는 `database-rules.md`를 schema system of record로 삼는다.
- 상위 분류는 `서비스 유형`이 아니라 `프로젝트 패밀리`다.
- `frontend`, `api`, `batch`, `receiver`는 상위 패밀리가 아니라 하위 런타임 역할이다.
- agentic engineering에서는 역할을 분리하되, 한 사람 또는 한 agent가 여러 역할을 겸할 수 있다.
- 다만 `orchestrator`, `qa-validator`, `docs-operator` 책임은 최종 전달 전 누락되면 안 된다.
- pre-commit hook는 빠른 local gate이고, 상세 검증은 `command-catalog.md`와 `quality-gates.md`가 맡는다.
- agent failure는 회고로 끝내지 않고 `governance/agent-failure-learning.md`와 `checklists/agent-failure-review.md`를 통해 문서, prompt, template, script 강화로 환류한다.
