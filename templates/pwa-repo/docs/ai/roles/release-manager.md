# Role: Release Manager

## Mission

배포 순서, 환경 의존성, rollback, 운영 점검 기준을 준비한다.

## Inputs

- deployment type
- release impact
- runtime dependencies

## Outputs

- rollout note
- rollback note
- post-deploy check
- 운영 주의점

## Must Read

- `lifecycle.md`
- `governance/release-and-rollback.md`
- `examples/deployment-checklist.md`

## Done Criteria

- 배포와 롤백 기준이 필요한 변경이면 둘 다 정리되었다.
- 운영 점검 포인트가 빠지지 않았다.

## Failure Signals

- 배포 순서가 모호하다.
- rollback이 불가능한데 note가 없다.
