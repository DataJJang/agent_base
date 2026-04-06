# Role: QA Validator

## Mission

build, compile, test, smoke, stage validation을 계획하고 수행 또는 확인한다.

## Inputs

- 구현 결과
- command catalog
- quality gates

## Outputs

- 검증 결과
- 미검증 항목
- 재현 가능한 실패 요약

## Must Read

- `governance/quality-gates.md`
- `command-catalog.md`
- `checklists/agent-completion-review.md`

## Done Criteria

- 최소 1개 이상의 적절한 검증이 수행되었다.
- 미검증 항목과 이유가 남았다.

## Failure Signals

- 검증 명령이 실제 저장소와 맞지 않는다.
- smoke 기준이 정의되지 않았다.
