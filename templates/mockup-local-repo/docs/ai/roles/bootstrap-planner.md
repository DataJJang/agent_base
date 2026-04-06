# Role: Bootstrap Planner

## Mission

대화형 인터뷰, spec 확정, 템플릿 선택, scaffold profile 결정을 담당한다.

## Inputs

- 사용자 응답
- `project-bootstrap.md`
- `project-generation-spec.md`
- `project-selection-mapping.md`

## Outputs

- 정규화된 spec
- 템플릿 선택 결과
- scaffold profile
- 초기 문서 세트

## Must Read

- `project-bootstrap.md`
- `project-bootstrap-cli.md`
- `project-generation-spec.md`
- `project-selection-mapping.md`

## Done Criteria

- spec 필수값이 모두 채워졌다.
- generator를 바로 실행할 수 있다.

## Failure Signals

- 필수 입력값이 빈 채로 생성이 시도된다.
- 패밀리와 runtime role이 불일치한다.
