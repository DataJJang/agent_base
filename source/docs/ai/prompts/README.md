# Project AI Prompt Library

이 디렉토리는 프로젝트 생성, 문서 생성, 영향도 분석, 운영 가이드 정리, 테스트 계획 수립에 재사용하는 AI 작업지시 템플릿을 담는다.

규칙 기준 문서는 [`AGENTS.md`](../../../AGENTS.md) 와 [`docs/ai/README.md`](../README.md) 다.

## 사용 원칙

- 프롬프트를 쓰기 전에 `AGENTS.md`와 관련 서비스 규칙 문서를 먼저 읽는다.
- schema, migration, seed, data correction이 있으면 `docs/ai/database-rules.md`를 같이 읽는다.
- 산출물은 항상 현재 코드, 설정, SQL, 문서를 근거로 작성하게 지시한다.
- 프롬프트에는 포함 범위와 제외 범위를 모두 적는다.
- 검증 기준, 미검증 항목, 운영 영향도를 반드시 출력하게 한다.
- 실제 토큰, 실운영 URL, 실계정 정보는 프롬프트에 넣지 않는다.

## 공통 입력 구조

모든 프롬프트는 아래 항목을 가능한 한 채워 넣는다.

- 대상 저장소 또는 저장소명
- 대상 브랜치
- 작업 목적
- 기능 또는 도메인 범위
- 대상 환경: `local`, `dev`, `stg`, `prd`
- 관련 코드 경로
- 관련 설정 파일 경로
- 관련 SQL / migration 경로
- 관련 문서 경로
- 제외 범위
- 산출물 형식
- 검증 기준

## 읽는 순서

1. 프로젝트 bootstrap 인터뷰 계열 프롬프트
2. 프로젝트 패밀리 또는 런타임 역할별 마스터 프롬프트
3. 산출물 유형별 프롬프트
4. 필요 시 저장소 또는 조직 특화 프롬프트
5. `examples/` 아래 복사형 실행 예시

## 새 프로젝트 시작 시 권장 프롬프트 순서

1. [`project-bootstrap-interview.md`](./project-bootstrap-interview.md)로 대화형 인터뷰를 진행한다.
2. [`project-spec-finalizer.md`](./project-spec-finalizer.md)로 인터뷰 결과를 정규화된 spec으로 확정한다.
3. [`scaffold-planning.md`](./scaffold-planning.md)으로 템플릿, 구조, 첫 산출물 계획을 만든다.
4. [`project-generator-run.md`](./project-generator-run.md)으로 generator 실행 패키지를 정리한다.
5. 필요한 경우 런타임 역할별 마스터 프롬프트를 추가로 사용한다.
6. `build-guide.md`를 이용해 첫 로컬 구축 문서를 만든다.
7. `test-plan.md`로 첫 검증 계획을 만든다.
8. DB를 소유하는 저장소면 `examples/database-review.md` 또는 `impact-analysis.md`를 사용해 DB change 기준을 확정한다.
9. 배포가 필요한 저장소면 `deployment-checklist.md`를 만든다.
10. 운영성 기능이면 `operations-manual.md`와 `impact-analysis.md`를 추가한다.
11. 실패 케이스가 생기면 `agent-failure-review.md`와 `scripts/record_agent_failure.py`로 환류를 시작한다.

## 프로젝트 생성 프롬프트

- [`project-bootstrap-interview.md`](./project-bootstrap-interview.md)
- [`project-spec-finalizer.md`](./project-spec-finalizer.md)
- [`scaffold-planning.md`](./scaffold-planning.md)
- [`project-generator-run.md`](./project-generator-run.md)

## 런타임 역할별 마스터 프롬프트

- [`frontend.md`](./frontend.md)
- [`api.md`](./api.md)
- [`batch.md`](./batch.md)
- [`receiver.md`](./receiver.md)

## 산출물 유형별 프롬프트

- [`build-guide.md`](./build-guide.md)
- [`operations-manual.md`](./operations-manual.md)
- [`deployment-checklist.md`](./deployment-checklist.md)
- [`test-plan.md`](./test-plan.md)
- [`incident-runbook.md`](./incident-runbook.md)
- [`impact-analysis.md`](./impact-analysis.md)
- [`agent-failure-review.md`](./agent-failure-review.md)

## 조직 또는 저장소 특화 프롬프트

이 패키지는 필요하면 조직 특화 prompt pack을 추가해 확장할 수 있다. 기본 배포본에서는 공통 생성/운영 프롬프트를 중심으로 사용하고, 조직 전용 pack은 optional overlay로만 사용한다.

- [`org-specific/README.md`](./org-specific/README.md)
- [`org-specific/aitelecom/README.md`](./org-specific/aitelecom/README.md)

## 실행 예시

- [`examples/README.md`](./examples/README.md)
- [`examples/getting-started.md`](./examples/getting-started.md)
- [`examples/project-bootstrap.md`](./examples/project-bootstrap.md)
- [`examples/project-generator-run.md`](./examples/project-generator-run.md)
- [`examples/game-bootstrap.md`](./examples/game-bootstrap.md)
- [`examples/pwa-bootstrap.md`](./examples/pwa-bootstrap.md)
- [`examples/mobile-app-bootstrap.md`](./examples/mobile-app-bootstrap.md)
- [`examples/mockup-local-bootstrap.md`](./examples/mockup-local-bootstrap.md)
- [`examples/backend-service-bootstrap.md`](./examples/backend-service-bootstrap.md)
- [`examples/operations-manual.md`](./examples/operations-manual.md)
- [`examples/deployment-checklist.md`](./examples/deployment-checklist.md)
- [`examples/test-plan.md`](./examples/test-plan.md)
- [`examples/impact-analysis.md`](./examples/impact-analysis.md)
- [`examples/database-review.md`](./examples/database-review.md)
- [`examples/agent-failure-review.md`](./examples/agent-failure-review.md)

## 권장 출력 공통 형식

- 목적
- 범위
- 근거 파일
- 핵심 결정 사항
- 세부 작업 항목
- 검증 계획
- 운영 영향
- 미확정/추가 확인 필요 항목
