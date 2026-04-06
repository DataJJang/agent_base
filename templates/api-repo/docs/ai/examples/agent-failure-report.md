# Example Output: Agent Failure Report

이 예시는 `scripts/record_agent_failure.py`로 만든 기본 기록을 사람이 보강하는 형태의 샘플이다.

## Purpose

새 프로젝트 bootstrap 과정에서 잘못된 템플릿을 선택한 실패 케이스를 정리한다.

## Expected

- `backend-service` 프로젝트에 API 중심 템플릿이 선택되어야 했다.

## Actual

- `web-app` 템플릿이 선택되어 command-catalog와 build 명령이 틀리게 생성되었다.

## Failure Type

- project selection mapping 규칙 부족
- prompt 예시 부족

## Root Cause

- `projectFamily`와 `runtimeRole`의 우선순위가 문서상 분명하지 않았다.

## Fix Location

- `docs/ai/project-selection-mapping.md`
- `docs/ai/prompts/examples/project-bootstrap.md`
- `checklists/project-interview.md`

## Prevention

- family 우선, role 보조 규칙을 문서에 명시한다.
- bootstrap 예시에 잘못된 family/role 조합 확인 단계를 추가한다.

## Validation

- 같은 입력으로 다시 인터뷰했을 때 `backend-service-repo`가 선택되는지 확인한다.
