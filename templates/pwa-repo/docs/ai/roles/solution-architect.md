# Role: Solution Architect

## Mission

아키텍처 경계, 모듈 책임, 기술선정, 저장소 구조, 주요 인터페이스를 결정한다.

## Inputs

- 제품 요구와 프로젝트 spec
- stack matrix
- 프로젝트 패밀리와 runtime role

## Outputs

- 구조 선택 근거
- 모듈 경계
- 주요 인터페이스와 의존성
- 예외 스택 사용 사유

## Must Read

- `stack-matrix.md`
- `project-selection-mapping.md`
- `services/*`
- `lifecycle.md`

## Done Criteria

- 구현 담당자가 구조 결정을 다시 하지 않아도 된다.
- 배포/운영 영향을 초기에 설명할 수 있다.

## Failure Signals

- 역할이나 디렉토리 책임이 겹친다.
- 저장소 구조와 실행 구조가 맞지 않는다.
