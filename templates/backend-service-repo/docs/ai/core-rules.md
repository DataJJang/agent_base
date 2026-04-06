# Project Core Rules

## 1. 목적

이 문서는 여러 저장소에 공통으로 적용할 수 있는 핵심 개발 규칙을 정리한다.

## 2. 최우선 원칙

### 기존 패턴 우선

- 같은 메뉴, 같은 도메인, 같은 책임의 기존 파일을 먼저 찾는다.
- 새 구조를 만들기 전에 기존 구조 확장이 가능한지 먼저 본다.
- 이상적인 구조보다 현재 저장소에서 반복되는 구조를 우선한다.

### 범위 밖 변경 금지

- 불필요한 리팩터링 금지
- 무관한 이름 변경 금지
- 무관한 포맷 정리 금지
- 무관한 의존성 변경 금지

### 공통 자산 중복 금지

- 타입, 상수, 모델, shared UI, query 레이어, SQL 문서를 먼저 찾는다.
- 같은 의미의 구조를 다른 이름으로 다시 만들지 않는다.

### 하위 호환 우선

- API는 필드 제거보다 optional 추가를 우선 검토한다.
- DB는 nullable, default, migration 순서를 함께 본다.
- soft delete, audit 컬럼, 공통 코드 체계를 깨지 않는다.

### 민감정보 커밋 금지

- 토큰
- 비밀번호
- 실운영 URL
- 실제 Chat ID
- API key
- 운영 DB 접속 정보
- 평문 secret

### 위험한 DB 명령 기본 금지

- destructive DDL 또는 대량 DML은 승인, rollback 또는 backup 메모, verification query 없이 실행하지 않는다.
- DB 작업은 [`database-rules.md`](./database-rules.md)를 source of truth로 본다.

### Git 작업 기본 규칙

- 작업 브랜치, 커밋, PR, 머지는 저장소에 별도 규칙이 없으면 [`governance/git-workflow.md`](./governance/git-workflow.md)를 따른다.
- 하나의 커밋에는 하나의 의도만 담는다.
- 기능 변경, 리팩터링, 포맷 정리, 문서 정리를 한 커밋에 섞지 않는다.
- 공유 브랜치에 직접 force push 하지 않는다.
- 보호 브랜치에는 직접 push 하지 않고 PR 또는 merge request를 우선한다.

## 3. 구조와 네이밍

### 저장소/모듈명

- 저장소명은 역할이 드러나야 한다.
- `admin`, `backend`, `service-api`, `batch`, `receiver` suffix를 유지한다.
- 모듈명은 기술보다 책임 기준으로 짓는다.

### 파일명

#### Frontend

- `XxxListPage.tsx`
- `XxxDetailPage.tsx`
- `XxxRegistrationPage.tsx`
- `XxxModifyPage.tsx`
- `XxxShared.tsx`
- `xxxApi.ts`

#### API 서비스

- `XxxController.java`
- `XxxService.java`
- `XxxSearchVo.java`
- `XxxUpsertVo.java`
- `XxxVo.java`
- `XxxQueryRepository.java`
- `*Inf`, `*Hst`

#### Batch

- `XxxJob.java`
- `XxxService.java`
- `XxxMapper.java`, `I*Mapper.java`
- 기능별 XML mapper
- 순번 기반 migration SQL

#### Receiver

- `XxxController.java`, `Handler.java`
- `XxxService.java`
- `Parser.java`, `Decoder.java`
- `XxxPublisher.java`
- `XxxConfig.java`
- `*Utils.java`

## 4. 코드와 데이터 규칙

### API 계약

- 목록, 상세, 등록, 수정, 삭제의 기본 패턴을 유지한다.
- 요청과 응답은 model 또는 VO로 명시한다.
- 검색 API는 search model 또는 query parameter 구조를 분명히 한다.
- 페이징 목록은 `pageNo`, `pageSize`를 우선 사용한다.

### validation과 예외 처리

- 형식 검증은 controller 또는 request model 근처에서 처리한다.
- 비즈니스 유효성 검증은 service에서 처리한다.
- 사용자 메시지와 내부 로그 메시지를 구분한다.

### DB와 migration

- 신규 테이블, 신규 컬럼, 신규 코드값은 migration과 기준 SQL 문서 둘 다 반영 여부를 검토한다.
- DB naming, abbreviation, COMMENT, constraint, 위험 SQL은 [`database-rules.md`](./database-rules.md)를 따른다.
- DDL 변경 시 COMMENT와 문서 표를 함께 갱신한다.
- soft delete가 있는 경우 `DEL_YN` 조건을 일관되게 적용한다.
- audit 컬럼은 운영성 테이블에서 우선 검토한다.
- schema/data change가 있으면 [`../../checklists/database-change.md`](../../checklists/database-change.md)를 함께 확인한다.

## 5. 프레임워크 규칙

### JPA

- 단순 CRUD는 `JpaRepository`를 우선 사용한다.
- soft delete 조건을 조회 시 누락하지 않는다.

### Querydsl

- 페이징, 검색, 복합 조회는 Querydsl custom repository 패턴을 우선 사용한다.
- Projection 필드명은 응답 모델과 맞춘다.

### Native SQL / Query Repository

- 집계가 복잡하거나 DB 의존 로직이 강하면 `QueryRepository`로 분리한다.
- `SELECT *`는 사용하지 않는다.
- alias는 응답 모델 필드명 기준으로 맞춘다.

### MyBatis

- XML namespace는 인터페이스 FQCN과 일치시킨다.
- XML `id`는 인터페이스 메서드명과 일치시킨다.
- `SELECT *`는 금지한다.
- 컬럼은 한 줄에 하나씩 정렬하고 의미 단위로 조건을 묶는다.

### Receiver 파이프라인

- ingress, parser/decoder, service, publish 경계를 분리한다.
- payload normalize 없이 business 로직으로 직접 전달하지 않는다.
- 수신 실패, 파싱 실패, business 실패, 발행 실패를 구분한다.

## 6. 로깅 규칙

- 로그에 민감정보를 그대로 남기지 않는다.
- placeholder logging을 우선 사용한다.
- API는 요청 식별과 결과 수준으로 로깅한다.
- Batch는 잡 시작, 종료, 실패를 추적 가능하게 남긴다.
- Receiver는 ingress 로그와 business 로그를 구분하고 payload dump를 기본 금지한다.
- Frontend 커밋 코드에 불필요한 `console.log`를 남기지 않는다.

## 7. 검증 규칙

- 검증 없이 push하지 않는다.
- 최소 `build`, `compile`, `test` 중 1개 이상 수행한다.
- 미검증 항목은 이유를 명시한다.
- schema/data change는 naming, COMMENT, migration, rollback, verification query까지 검토한다.

### 최소 검증 기준

- Frontend: build 또는 test
- API 서비스: compile 또는 test
- Batch: compile 또는 test
- Receiver: compile 또는 test

## 8. 문서화 규칙

아래 항목이 바뀌면 문서 동반 수정 여부를 검토한다.

- API 계약
- DB 스키마, migration, seed, data correction
- 운영 설정
- 외부 연동
- 배포 순서
- 검증 절차
- 화면 사용 흐름

문서 종류 분기는 [`document-routing.md`](./document-routing.md)를 따른다.

Git 전략, 커밋 템플릿, 브랜치/머지 기준은 [`governance/git-workflow.md`](./governance/git-workflow.md)를 따른다.
