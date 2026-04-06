# Evaluation And Drift

## 1. 목적

이 문서는 AI 규약과 실제 저장소 상태가 어긋날 때 어떤 순서로 갱신하고 평가할지 정의한다.

## 2. 드리프트 유형

- 코드 구조가 규약과 달라진 경우
- build, compile, test 명령이 바뀐 경우
- 운영 문서와 실제 배포 절차가 달라진 경우
- 템플릿 복제본이 `source/`와 달라진 경우
- 도구 adapter가 canonical 규칙과 충돌하는 경우
- 같은 agent failure가 반복되는데도 규약, prompt, template, script가 강화되지 않은 경우

## 3. 갱신 우선순위

1. 실제 코드와 설정 확인
2. `source/docs/ai/*` 갱신
3. `source/AGENTS.md` 및 adapter 갱신
4. `templates/*` 동기화
5. adoption / maintenance 체크리스트 갱신
6. 실패 케이스가 있으면 `agent-failure-learning.md`와 `checklists/agent-failure-review.md`에 따라 환류

## 4. 평가 기준

- 규칙이 실제 저장소 구조를 설명하는가
- build/test/운영 절차가 현재와 일치하는가
- 서비스별 템플릿이 불필요한 파일 없이 최소 구성을 유지하는가
- 도구별 adapter가 canonical과 충돌하지 않는가
- 문서만 읽고 새 작업자가 의사결정 가능한가
- 반복 실패가 pre-commit gate, prompt, template, script, checklist 강화로 연결되고 있는가

## 5. 정기 점검 권장

- 분기별 1회 템플릿 유효성 검토
- 큰 구조 변경 후 즉시 `source/`와 `templates/*` 동기화
- 새 AI 도구 도입 시 compatibility 문서 검토
- 새 배포 방식 도입 시 lifecycle, release-and-rollback 갱신
- 반복 agent failure가 생기면 월간 단위로 failure pattern을 묶어 강화 우선순위를 재평가
