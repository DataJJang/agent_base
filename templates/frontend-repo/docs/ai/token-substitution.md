# Token Substitution

## 1. 목적

이 문서는 생성기가 scaffold와 문서 안의 placeholder를 어떤 규칙으로 실제 값으로 치환하는지 정의한다.

## 2. 기본 규칙

- 토큰 형식은 `__TOKEN_NAME__`을 사용한다.
- 생성기는 파일명, 디렉토리명, 파일 내용 안의 토큰을 모두 치환한다.
- 치환 값은 `project-generation-spec`과 생성기 내부 파생 규칙에서 계산한다.
- 지원되지 않는 값은 빈 문자열로 두지 않고 가능한 기본값을 계산하거나 명시적 오류를 낸다.

## 3. 기본 토큰

| 토큰 | 의미 |
| --- | --- |
| `__REPOSITORY_NAME__` | `repositoryName` |
| `__PROJECT_NAME__` | `projectName` |
| `__PROJECT_FAMILY__` | `projectFamily` |
| `__PROJECT_PURPOSE__` | `projectPurpose` |
| `__PROJECT_NATURE__` | `projectNature` |
| `__LANGUAGE__` | `language` |
| `__FRAMEWORK__` | `framework` |
| `__RUNTIME_VERSION__` | `runtimeVersion` |
| `__BUILD_TOOL__` | `buildTool` |
| `__TEST_TOOL__` | `testTool` |
| `__DATASTORE__` | `datastore` |
| `__CACHE__` | `cache` |
| `__DEPLOYMENT_TYPE__` | `deploymentType` |
| `__STARTUP_MODE__` | `startupMode` |
| `__LOGGING_MODE__` | `loggingMode` |
| `__SECURITY_PROFILE__` | `securityProfile` |
| `__PACKAGE_NAME__` | `packageName` |
| `__PACKAGE_PATH__` | `packageName`을 path로 치환한 값 |
| `__MAIN_CLASS_NAME__` | 생성기가 계산한 대표 진입 클래스명 |
| `__TARGET_ENVIRONMENTS__` | `targetEnvironments`를 쉼표 문자열로 정리한 값 |
| `__TARGET_OS__` | `targetOs`를 쉼표 문자열로 정리한 값 |
| `__RUNTIME_ROLES__` | `runtimeRoles`를 쉼표 문자열로 정리한 값 |
| `__EXTERNAL_INTEGRATIONS__` | `externalIntegrations`를 쉼표 문자열로 정리한 값 |

## 4. 파생 규칙

- `__PACKAGE_PATH__`는 `com.example.sample` -> `com/example/sample`으로 바꾼다.
- `__PACKAGE_PATH__`와 다른 토큰은 파일 내용뿐 아니라 파일명과 디렉토리명에도 사용할 수 있다.
- `__MAIN_CLASS_NAME__`는 `projectName` 또는 `repositoryName`을 PascalCase로 정리한 뒤 family에 맞는 suffix를 붙인다.
  - backend-service: `Application`
  - batch-worker: `BatchApplication`
  - receiver-integration: `ReceiverApplication`
  - library-tooling java: `ToolingApplication`
- `targetEnvironments`, `targetOs`, `runtimeRoles`, `externalIntegrations`는 문자열 배열이면 쉼표 기준 문자열도 같이 만든다.

## 5. 예외 처리

- Java 계열인데 `packageName`이 없으면 오류로 본다.
- 지원되지 않는 scaffold 조합이면 code scaffold는 생략하고 문서만 생성한다.
- unsupported scaffold일 때도 토큰 치환은 가능한 문서 범위에서 수행한다.
