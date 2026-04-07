# Legacy Exception Policy

## 1. 목적

기존 프로젝트에서 당장 바꾸지 못하는 예외를 통제된 방식으로 남기기 위한 기준이다.

## 2. 예외로 허용할 수 있는 항목

- framework upgrade를 막는 특정 라이브러리
- 운영상 즉시 변경이 어려운 배포 순서
- 단기 유지가 필요한 legacy auth 또는 legacy screen
- 문서화되지 않았지만 현재 운영이 의존하는 step

## 3. 예외 기록 필드

- 예외 항목
- 유지 이유
- 영향 범위
- 만료 목표 시점
- 제거 조건
- owner role

## 4. 금지

- 이유 없는 “레거시라서 유지”
- 만료 시점 없는 상시 예외
- rollback 없이 irreversible change 강행
