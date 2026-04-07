# Migration Strategy

## 1. 목적

기존 저장소를 전환할 때 어떤 전략을 쓸지 결정하는 기준을 정의한다.

## 2. 전략 유형

- `big-bang`
  - 한 번에 전환한다. 범위가 작고 rollback이 쉬울 때만 쓴다.
- `phased`
  - 기능 또는 계층 단위로 점진 전환한다.
- `shadow`
  - 새 경로를 병행 구동하고 결과를 비교한다.
- `dual-run`
  - 기존/신규를 일정 기간 함께 실행한다.
- `strangler`
  - 일부 경로만 새 시스템으로 우회시켜 점진 분리한다.

## 3. 선택 기준

- API contract가 민감하면 `shadow`, `dual-run`, `phased`를 우선 검토한다.
- DB schema를 크게 바꾸면 rollback과 data correction 계획이 없으면 `big-bang`을 피한다.
- 운영 문서와 observability가 약하면 작은 단계로 쪼갠다.

## 4. 필수 note

- cutover 조건
- rollback 조건
- before/after validation
- 운영자 확인 포인트
