# Agent Failure Learning

## 1. 목적

이 문서는 Agent가 실패한 케이스를 수집하고, 하네스 구조를 강화하는 환류 절차를 정의한다.

## 2. Agent 실패로 보는 경우

- 잘못된 파일이나 계층을 수정한 경우
- 요청 범위를 벗어난 과도한 변경을 한 경우
- 필요한 검증을 누락한 경우
- 위험 명령 또는 위험 SQL을 제어 없이 시도한 경우
- 역할을 잘못 배정했거나 필수 specialist handoff를 생략한 경우
- upstream/downstream handoff artifact가 부족해 같은 판단을 반복한 경우
- 문서, 규칙, 템플릿, prompt가 부족해서 같은 질문이 반복되는 경우
- 지원되지 않는 스택인데도 unsupported 사실을 분명히 알리지 못한 경우
- 같은 오류를 팀이 반복적으로 재경험하는 경우

## 3. 실패 케이스 기록 항목

- 저장소명 / 브랜치
- agent 역할
- upstream 역할 / downstream 역할
- 작업 요청 요약
- 기대 결과
- 실제 결과
- 영향 범위
- 실패 유형
  - 규칙 부족
  - 문서 드리프트
  - prompt 부족
  - template 부족
  - scaffold 부족
  - validation 부족
  - 도구 한계
- 재현 방법
- root cause
- 고쳐야 할 위치
  - `AGENTS.md`
  - `docs/ai/*`
  - `prompts/*`
  - `templates/*`
  - `scripts/*`
  - `checklists/*`
- 고쳐야 할 역할 체계
  - role assignment
  - role prompt
  - handoff checklist
- 예방 조치
- 검증 방법

## 4. 강화 우선순위

1. 위험한 실패
   - destructive action, secret 노출, 운영 영향 누락
2. 반복 실패
   - 같은 질문, 같은 누락, 같은 잘못된 선택 반복
3. 생산성 실패
   - 문서가 부족해서 bootstrap 또는 delivery가 매번 길어지는 경우

## 5. 환류 절차

1. 실패 케이스를 기록한다.
2. root cause를 분류한다.
3. 고칠 문서, 프롬프트, 템플릿, 스크립트, 역할 배정 규칙을 지정한다.
4. `source/`를 먼저 수정한다.
5. `templates/*`를 동기화한다.
6. 같은 실패가 재현되지 않는지 예시 또는 dry-run으로 확인한다.
7. `maintenance.md`와 `evaluation-and-drift.md` 기준으로 장기 반영 여부를 검토한다.

## 6. 기록 저장 위치와 스크립트

- 기본 저장 위치: `.agent-base/failure-cases/`
- 기본 기록 스크립트: `python3 scripts/record_agent_failure.py`

예시:

```bash
python3 scripts/record_agent_failure.py \
  --summary "wrong template selected during bootstrap" \
  --request "create a backend service project" \
  --expected "backend-service template should be selected" \
  --actual "web-app template was selected" \
  --failure-type template \
  --failure-type prompt \
  --affected-area docs/ai/project-selection-mapping.md \
  --affected-area docs/ai/prompts/examples/project-bootstrap.md \
  --validation "rerun bootstrap with the same input and confirm backend-service mapping"
```

## 7. 최소 산출물

- failure note 또는 retrospective
- 수정된 규칙 또는 prompt
- 필요한 template 또는 script 수정
- 필요한 role prompt 또는 handoff checklist 수정
- 재검증 결과

## 8. 추천 주기

- 실패 발생 즉시 triage
- 주간 또는 스프린트 단위로 반복 실패 묶음 정리
- 분기별로 실패 패턴을 다시 분류해 공통 규칙에 승격할지 검토
