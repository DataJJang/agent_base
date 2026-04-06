# Git Workflow

## 1. 목적

이 문서는 프로젝트 저장소 전반에서 기본으로 따를 Git 커밋 규약, 브랜치 전략, PR 작성 기준, merge 전략을 정의한다.

저장소별로 별도 규칙이 명시되어 있으면 그 규칙이 우선한다. 별도 규칙이 없으면 이 문서를 기본값으로 적용한다.

## 2. 기본 원칙

- 보호 브랜치에는 직접 push 하지 않는다.
- 작업은 짧은 생명주기의 topic branch에서 진행한다.
- 커밋은 작고 단일한 의도를 가져야 한다.
- 첫 공유 커밋 전에는 저장소 로컬 pre-commit hook를 설치한다.
- merge 전에 최소 1개 이상의 검증 결과를 확보한다.
- force push는 개인 작업 브랜치에서만 제한적으로 사용한다.
- 운영 브랜치와 통합 브랜치 이력은 가능하면 읽기 쉽게 유지한다.

## 3. 브랜치 전략

### 장기 브랜치

- 저장소에 `dev` 브랜치가 있으면 기본 통합 브랜치로 본다.
- 저장소에 `main` 또는 `master`가 있으면 운영 릴리즈 기준 브랜치로 본다.
- 저장소에 장기 브랜치가 1개뿐이면 해당 브랜치를 통합 및 릴리즈 기준 브랜치로 본다.

### 단기 브랜치

브랜치명은 아래 패턴을 기본값으로 사용한다.

- `feature/<domain>-<topic>`
- `fix/<domain>-<topic>`
- `hotfix/<domain>-<topic>`
- `refactor/<domain>-<topic>`
- `chore/<domain>-<topic>`
- `docs/<domain>-<topic>`
- `test/<domain>-<topic>`

예시:

- `feature/telegram-template-preview`
- `fix/ops-alert-room-link`
- `hotfix/batch-dispatch-timeout`

### 브랜치명 규칙

- 짧고 의미 있는 영어 소문자 kebab-case를 사용한다.
- 개인 이름, 날짜만 있는 이름, 의미 없는 번호만 있는 이름은 피한다.
- 하나의 브랜치에는 하나의 목적만 담는다.

## 4. 커밋 메시지 규약

### 기본 형식

```text
<type>: <summary>
```

또는 scope가 유의미할 때는 아래 형식을 사용한다.

```text
<type>(<scope>): <summary>
```

예시:

- `feat: add telegram room quick send`
- `fix(ops-alert): resolve room project names from biz info`
- `docs: add telegram operations manual`
- `refactor(telegram): use back buttons on detail pages`

### 권장 type

- `feat`: 기능 추가
- `fix`: 버그 수정
- `refactor`: 동작 보존 리팩터링
- `docs`: 문서 변경
- `test`: 테스트 추가 또는 수정
- `chore`: 잡무성 변경, 설정 정리, 비기능성 수정
- `build`: 빌드, 의존성, gradle, npm, packaging 변경
- `ci`: CI/CD 파이프라인 변경
- `perf`: 성능 개선

### summary 규칙

- 현재형 동사로 시작한다.
- 72자 이내를 권장한다.
- 마침표를 붙이지 않는다.
- 추상적인 표현보다 결과가 드러나게 쓴다.
- “update files”, “fix issue” 같은 모호한 문구는 피한다.

### 커밋 분리 규칙

- 기능 추가와 리팩터링은 분리한다.
- 코드 변경과 문서 보강은 가능하면 분리한다.
- 포맷 변경만 있는 경우 별도 커밋으로 분리한다.
- secret 제거, 이력 정리 같은 민감 조치는 별도 커밋으로 분리한다.

## 5. 커밋 본문 템플릿

본문이 필요한 경우 아래 템플릿을 사용한다.

```text
<type>(<scope>): <summary>

Why:
- 변경 이유

What:
- 주요 변경 사항

Validation:
- 수행한 검증
```

릴리즈 영향이나 운영 위험이 크면 아래를 추가한다.

```text
Rollback:
- 롤백 또는 우회 방법
```

## 6. 저장 전 Local Gate

- 커밋 전에 [`pre-commit-hooks.md`](./pre-commit-hooks.md)를 기준으로 local pre-commit gate를 설치한다.
- hook는 빠른 반복 검증만 맡고, 상세 검증은 `quality-gates.md`와 `command-catalog.md`를 따른다.
- hook가 실패하면 코드를 고치거나, repo-local hook 설정과 명령 카탈로그를 먼저 일치시킨다.
- 같은 유형의 commit 직전 실패가 반복되면 `agent-failure-learning.md` 기준으로 문서, template, script 보강이 필요한지 검토한다.

## 6. PR 작성 규칙

PR 또는 merge request에는 아래를 가능한 한 포함한다.

- 목적
- 변경 범위
- 핵심 변경 사항
- API 영향
- DB 영향
- 설정 영향
- 문서 영향
- 검증 결과
- 미검증 항목
- 운영 영향 또는 배포 주의점

UI 변경이면 스크린샷 또는 화면 설명을 포함한다.

## 7. Merge 전략

### 기본 전략

- 기본 merge 전략은 `squash merge`를 권장한다.
- 이유는 작은 topic branch의 다수 커밋을 읽기 쉬운 단위로 정리하기 위함이다.

### 예외 전략

- 장기적으로 브랜치 이력을 보존해야 하는 release branch는 `merge commit`을 허용할 수 있다.
- 단일 커밋 자체가 이미 충분히 정리되어 있고 이력을 그대로 보존할 가치가 있으면 `rebase and merge`를 허용할 수 있다.

### 병합 전 정리 규칙

- topic branch는 대상 브랜치 기준으로 최신화한다.
- 충돌 해결은 가능하면 topic branch에서 먼저 수행한다.
- 공유 브랜치에 merge commit을 쌓아 최신화하는 방식보다, topic branch rebase 또는 명시적 동기화를 우선 검토한다.

## 8. Rebase / Force Push 규칙

- 개인 topic branch에서는 rebase를 허용한다.
- 이미 리뷰가 진행 중인 브랜치에서 history를 크게 바꾸는 force push는 팀에 알리고 수행한다.
- `dev`, `main`, `master` 등 공유 브랜치에는 force push 하지 않는다.
- 충돌 해결 목적의 rebase는 허용하되, 커밋 의미가 흐려지지 않게 한다.

## 9. 릴리즈와 핫픽스 흐름

### 일반 기능

- `feature/*` 또는 `fix/*` 브랜치에서 작업한다.
- 통합 브랜치가 있으면 우선 `dev`로 병합한다.
- 운영 릴리즈는 `dev -> main/master` 또는 저장소별 릴리즈 절차를 따른다.

### 핫픽스

- 운영 브랜치 기준으로 `hotfix/*` 브랜치를 만든다.
- 긴급 수정 후 운영 브랜치에 반영한다.
- 이후 동일 변경을 통합 브랜치에도 반드시 정방향 반영한다.
- 상황에 따라 merge, cherry-pick, 재작업 중 하나를 택하되 중복 반영 여부를 확인한다.

## 10. 리뷰 체크리스트

- [ ] 브랜치 목적이 명확한가
- [ ] 커밋 메시지가 규칙을 따르는가
- [ ] 변경 범위가 요청 범위를 넘지 않는가
- [ ] API/DB/설정/문서 영향이 빠지지 않았는가
- [ ] 민감정보가 없는가
- [ ] 검증 결과와 미검증 항목이 분명한가
- [ ] merge 후 롤백 또는 우회 방안이 필요한 변경인가

## 11. 빠른 기준 요약

- 저장소별 규칙이 없으면 `dev`를 통합 브랜치, `main/master`를 릴리즈 기준 브랜치로 본다.
- topic branch는 `feature`, `fix`, `hotfix`, `refactor`, `docs`, `test`, `chore` prefix를 사용한다.
- 커밋 메시지는 `type: summary` 또는 `type(scope): summary` 형식을 따른다.
- 기본 merge 전략은 `squash merge`다.
- 공유 브랜치 force push는 금지한다.
