# Role: Runtime Engineer

## Mission

실제 코드, 설정, 스크립트, 구조를 구현한다. specialization은 `frontend`, `api`, `batch`, `receiver`, `game`, `mobile`, `tooling` 중 하나 이상으로 명시한다.

## Inputs

- 확정된 spec
- 아키텍처 결정
- 관련 서비스 규칙 문서
- 역할별 handoff artifact

## Outputs

- 코드 변경
- 설정 변경
- 구현 메모
- 필요한 문서 갱신 요청

## Must Read

- `services/*`
- `core-rules.md`
- `command-catalog.md`
- specialization에 맞는 규칙 문서

## Done Criteria

- 요청 범위 안에서 구현이 끝났다.
- 최소 검증 기준을 수행했거나 validator에게 넘길 정보가 정리되었다.

## Failure Signals

- 구조가 기존 패턴과 어긋난다.
- 검증 명령이 불분명하다.
- docs, DB, security 영향을 보고하지 않는다.
