# Project Selection Mapping

## 1. 목적

이 문서는 인터뷰에서 선택한 값이 어떤 템플릿, 문서, 명령, 초기 산출물로 이어지는지 정의한다.

## 2. 기본 매핑 규칙

- `projectFamily`가 최상위 템플릿 선택 기준이다.
- 생성기는 `projectFamily`로 기본 템플릿을 고르고, 언어/프레임워크 조합으로 scaffold profile을 고른다.
- `runtimeRole[]`는 서비스 규칙 문서와 추가 템플릿 오버레이 선택 기준이다.
- `repositoryMode`는 생성기 출력의 한계와 후속 오버레이 범위를 결정한다.
- `projectNature`, `deploymentType`, `datastore`, `cache`는 생성해야 할 문서 종류를 제한하거나 확장한다.
- `production` 또는 외부 사용자 대상이면 운영/배포/보안 문서는 필수다.

## 3. 패밀리별 기본 템플릿 매핑

| projectFamily | 기본 템플릿 | 기본 문서 세트 | 기본 명령 기준 |
| --- | --- | --- | --- |
| `game` | `templates/game-repo` | bootstrap, build-guide, test-plan, ops or deployment when needed | engine build, validation, smoke |
| `web-app` | `templates/web-app-repo` | bootstrap, build-guide, test-plan | npm build, UI smoke |
| `pwa` | `templates/pwa-repo` | bootstrap, build-guide, test-plan, deployment-checklist | npm build, offline and install smoke |
| `mobile-app` | `templates/mobile-app-repo` | bootstrap, build-guide, test-plan, deployment-checklist | app build, device smoke |
| `backend-service` | `templates/backend-service-repo` | bootstrap, build-guide, test-plan, deployment-checklist, operations-manual | gradle compile and test, API smoke |
| `batch-worker` | `templates/batch-worker-repo` | bootstrap, build-guide, test-plan, operations-manual | gradle compile and test, job smoke |
| `receiver-integration` | `templates/receiver-integration-repo` | bootstrap, build-guide, test-plan, operations-manual | gradle compile and test, payload smoke |
| `mockup-local` | `templates/mockup-local-repo` | bootstrap, build-guide, test-plan | local preview and walkthrough |
| `library-tooling` | `templates/library-tooling-repo` | bootstrap, build-guide, test-plan | package build and sample invocation |

## 3.1 기본 scaffold profile 매핑

| projectFamily | language / framework | scaffold profile | 지원 수준 |
| --- | --- | --- | --- |
| `web-app` | `TypeScript + React` | `web-react-vite` | supported |
| `pwa` | `TypeScript + React` | `pwa-react-vite` | supported |
| `mockup-local` | 경량 정적 mockup | `mockup-local-static` | supported |
| `backend-service` | `Java + Spring Boot` | `java-spring-service` | supported |
| `batch-worker` | `Java + Spring Boot` | `java-spring-batch` | supported |
| `receiver-integration` | `Java + Spring Boot` | `java-spring-receiver` | supported |
| `library-tooling` | `TypeScript` | `typescript-library-tooling` | supported |
| `library-tooling` | `Java` | `java-library-tooling` | supported |
| `game` | `C# + Unity` | `unity-game` | structure-only |
| `mobile-app` | `Dart + Flutter` | `flutter-mobile` | structure-only |

## 4. 하위 역할 추가 매핑

- `runtimeRole`에 `api`가 있으면 `services/api.md`를 읽고 API 계약, validation, security 기준을 추가한다.
- `runtimeRole`에 `batch`가 있으면 `services/batch.md`를 읽고 scheduler, job, mapper, SQL 기준을 추가한다.
- `runtimeRole`에 `receiver`가 있으면 `services/receiver.md`를 읽고 ingress, parser, publish, diagnostics 기준을 추가한다.
- `runtimeRole`에 `frontend`가 있으면 `services/frontend.md`를 읽고 route, state, i18n, UI smoke 기준을 추가한다.

## 5. 문서 세트 확장 규칙

- `datastore != 없음`이면 `database-rules.md`와 `checklists/database-change.md`를 포함한다.
- `deploymentType != local-only`이면 `deployment-checklist`를 생성한다.
- `projectNature == production`이면 `operations-manual`, `release-and-rollback`, `quality-gates` 검토를 필수로 한다.
- `cache != 없음`이면 config와 deploy-check 문서에 cache 의존성을 명시한다.
- `securityProfile != 없음`이면 보안 baseline과 인증 방식 문서를 같이 만든다.

## 6. 생성기 출력 규칙

- 생성기는 `templates/<family>-repo`를 먼저 복사한다.
- `repositoryMode`가 `monorepo` 또는 `multi-repo`여도 v1 생성기는 샘플 저장소 1개만 만든다.
- 이후 지원되는 scaffold profile이 있으면 코드와 설정 skeleton을 추가한다.
- scaffold profile이 `structure-only`면 실행 가능한 전체 기능 대신 최소 디렉토리와 엔트리 파일만 만든다.
- 생성기는 최소 아래 산출물을 만든다.
  - root `README.md`
  - `.agent-base/project-generation-spec.json`
  - `.agent-base/generation-manifest.json`
  - family-appropriate scaffold files
- 지원되지 않는 스택 조합이면 docs template만 생성하고 `TODO_UNSUPPORTED_SCAFFOLD.md`를 남긴다.
