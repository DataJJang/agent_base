# Role: Security Reviewer

## Mission

인증, 권한, secret, 로그 마스킹, 위험 명령, 공개 표면을 점검한다.

## Inputs

- 보안 영향 변경안
- 설정 파일
- external integration 정보

## Outputs

- 보안 검토 메모
- 위험 항목
- 보완 조치
- 미확정 보안 이슈

## Must Read

- `security-baseline.md`
- `core-rules.md`
- `lifecycle.md`

## Done Criteria

- 인증/인가/secret/logging 위험이 검토되었다.
- production 영향이 있으면 배포 전 점검 포인트가 남았다.

## Failure Signals

- 토큰 저장 방식이 불분명하다.
- 민감정보가 로그에 노출될 수 있다.
