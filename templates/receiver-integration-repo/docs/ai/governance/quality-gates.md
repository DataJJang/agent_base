# Quality Gates

## 1. 목적

이 문서는 팀 레벨 품질 일관성을 유지하기 위한 최소 품질 게이트를 정의한다.

## 2. Definition of Done

작업은 아래를 만족해야 완료로 본다.

- 코드가 저장소 규칙에 맞다
- 필요한 설정 반영 여부가 검토되었다
- DB 영향이 있으면 naming, COMMENT, migration, verification, rollback 문서가 검토되었다
- 관련 문서가 갱신되었거나 생략 이유가 있다
- 저장소 로컬 pre-commit gate 설치 여부가 확인되었다
- 최소 1개 이상의 검증이 수행되었다
- 미검증 항목이 보고되었다

## 3. 최소 검증 기준

- Frontend: build 또는 test
- API 서비스: compile 또는 test
- Batch: compile 또는 test
- Receiver: compile 또는 test

DB schema 또는 data change가 있으면 verification query 또는 영향 범위 확인까지 포함한다.

## 3-1. 역할 기반 완료 기준

- `orchestrator`
  - 역할 배정, 순서, handoff 기준이 문서화되었다.
- `runtime-engineer`
  - 구현과 설정 변경이 요청 범위 안에 있고 최소 검증이 수행되었다.
- `data-steward`
  - naming, abbreviation, COMMENT, migration, verification, rollback note가 확인되었다.
- `security-reviewer`
  - 인증, secret, logging, 위험 작업 제약이 검토되었다.
- `qa-validator`
  - build/compile/test/smoke 중 적절한 검증과 미검증 항목 보고가 있다.
- `docs-operator`
  - README, command-catalog, runbook, manual, checklist 중 필요한 문서가 갱신되었다.
- `release-manager`
  - rollout/rollback/운영 점검 기준이 필요한 변경이면 관련 note가 있다.
- `legacy-analyst`
  - 기존 저장소의 실제 명령, 프레임워크, 운영 제약, docs gap이 inventory로 정리되었다.
- `migration-planner`
  - 전환 전략, 단계, parity 목표, cutover/rollback 기준이 문서화되었다.
- `compatibility-reviewer`
  - 목표 스택과 현재 스택의 호환성, breaking point, exception이 정리되었다.

## 4. 검증 레벨

- Level 1: build, compile, test
- Level 2: smoke validation
- Level 3: stage validation
- Level 4: 운영 반영 전 검증

변경 영향이 커질수록 더 높은 레벨을 검토한다.

## 4-1. Brownfield / Migration Gate

기존 저장소를 adoption 또는 migration할 때는 아래가 추가로 필요하다.

- repository inventory가 있다
- adoption spec 또는 migration manifest가 있다
- parity requirement가 정의되었다
- compatibility risk와 legacy exception이 분류되었다
- cutover 또는 rollback note가 있다
- before/after validation 방법이 정의되었다

## 5. 리뷰 기준

리뷰 시 아래를 본다.

- 요청 범위와 변경 범위가 일치하는가
- 기존 패턴을 따르는가
- API, DB, 설정, 문서 영향이 빠지지 않았는가
- DB naming, abbreviation, COMMENT, constraint가 기준과 맞는가
- 민감정보나 운영 위험이 없는가
- 위험 SQL 또는 irreversible change가 포함되는가
- 롤백 또는 우회 방안이 필요한 변경인가
- 검증 결과가 충분한가

## 6. 최종 보고 형식

가능한 경우 아래를 함께 남긴다.

- 변경 요약
- build 성공 여부
- compile 성공 여부
- test 성공 여부
- pre-commit hook 실행 여부
- DB verification query 또는 수동 확인 결과
- 미실행 검증과 이유
- 운영 영향 또는 배포 주의점

## 7. 커밋 전 체크리스트

- [ ] 요청 범위 밖 파일을 건드리지 않았는가
- [ ] 민감정보가 포함되지 않았는가
- [ ] build, compile, test 중 최소 1개 이상 수행했는가
- [ ] 저장소에서 pre-commit hook를 설치했고, 필요한 경우 한 번 이상 실행해봤는가
- [ ] 문서 동반 수정이 필요한지 확인했는가
- [ ] schema/data change가 있으면 `database-rules.md`와 `checklists/database-change.md`를 확인했는가
- [ ] 결과 보고에 미검증 항목을 적을 준비가 되었는가

Git 커밋, 브랜치, PR, merge 기본 규칙은 [`git-workflow.md`](./git-workflow.md)를 따른다.
역할 기반 handoff는 `checklists/agent-handoff.md`와 `checklists/agent-completion-review.md`를 같이 사용한다.
