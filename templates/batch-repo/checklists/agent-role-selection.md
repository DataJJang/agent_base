# Agent Role Selection Checklist

- [ ] 프로젝트 패밀리와 runtime role이 확정되었는가
- [ ] `orchestrator`를 둘지 여부가 결정되었는가
- [ ] 구현 주 담당 역할이 지정되었는가
- [ ] `qa-validator`가 지정되었는가
- [ ] `docs-operator`가 지정되었는가
- [ ] DB 영향이 있으면 `data-steward`가 지정되었는가
- [ ] 보안 영향이 있으면 `security-reviewer`가 지정되었는가
- [ ] 배포/운영 영향이 있으면 `release-manager`가 필요한지 검토했는가
- [ ] 반복 실패나 harness 강화가 예상되면 `failure-curator`를 지정했는가
- [ ] 필수 역할과 optional 역할을 구분했는가
- [ ] 각 역할의 입력과 출력이 정리되었는가
