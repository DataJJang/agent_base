# Example Output: Deployment Checklist

## Preconditions

- migration SQL 반영 대상 확인
- 환경변수 차이 확인

## Deploy Sequence

1. DB migration
2. backend deploy
3. admin deploy

## Post-Deploy Validation

- health 확인
- 핵심 목록/상세 smoke 확인
- 로그 오류 유무 확인

## Rollback Trigger

- 핵심 API 5xx 지속
- UI 진입 불가
