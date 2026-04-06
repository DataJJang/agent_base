# Project Lifecycle Rules

## 1. 목적

이 문서는 구축, 운영, 배포, 릴리즈, 롤백, 운영 점검을 팀 공통 기준으로 정리한다.

## 2. 구축

새 기능 또는 새 서비스는 아래 묶음으로 본다.

- 코드
- 설정
- DB
- 문서
- 외부 연동
- 검증

어느 하나라도 빠지면 구축 완료로 보지 않는다.

### 구축 체크리스트

- [ ] 코드만 바꾸는 작업인지, 설정과 DB가 함께 필요한 작업인지 구분했는가
- [ ] 신규 설정 키, 신규 테이블, 신규 컬럼, 신규 코드값이 있는가
- [ ] DB를 소유하는 저장소면 [`database-rules.md`](./database-rules.md)를 검토했는가
- [ ] migration, seed, backfill, verification query가 필요한가
- [ ] 외부 연동 또는 토큰 의존성이 있는가
- [ ] 필요한 문서 세트를 식별했는가
- [ ] local, dev, stg, prd 반영 순서를 생각했는가

## 3. 운영

운영 관점에서는 기능 자체보다 아래가 확인 가능해야 한다.

- 기동 여부
- 핵심 로그
- 핵심 적재 테이블
- 외부 연동 성공/실패
- 재시도 또는 누락 여부
- 장애 1차 확인 포인트

운영 절차가 길어지면 runbook으로 분리하고, 이 문서에는 상위 기준만 남긴다.

## 4. 배포

배포는 아래 4단계로 본다.

1. 사전 조건 확인
2. 반영
3. smoke validation
4. 배포 후 운영 점검

### 배포 전 공통 확인

- 대상 브랜치와 커밋
- 관련 `application.yml` 또는 env 키
- DB migration, seed, backfill 필요 여부
- 외부 의존 서비스 가용성
- backward compatibility
- feature toggle 또는 enable flag
- smoke validation 대상
- rollback 조건
- DB pre-check query와 post-check query 준비 여부
- 위험 DML 또는 irreversible DDL 포함 여부

### 배포 직후 공통 확인

- 프로세스 기동 성공
- 시작 로그 이상 여부
- health endpoint 또는 대표 API
- 핵심 화면 진입
- 핵심 DB 적재
- 핵심 scheduler 또는 수신 기능 동작
- schema/data change가 있으면 verification query 결과 확인

## 5. 환경 매트릭스

환경별 차이는 아래 축으로 분리해 문서화한다.

- profile
- datasource
- MQTT, Redis, 외부 API
- 토큰 및 secret
- 배치 enable 여부
- 모니터링, actuator, prometheus

환경 구분:

- `local`: 개발 편의, 단일 검증
- `dev`: 개발 통합 검증
- `stg`: 운영 유사 검증
- `prd`: 실제 운영

## 6. 릴리즈

아래 중 하나라도 있으면 릴리즈 영향도를 명시한다.

- API 계약 변경
- DB 스키마 변경
- data correction 또는 backfill
- 외부 연동 변경
- 배치 스케줄 또는 receiver ingress 변경
- 운영 토큰 또는 권한 변경

## 7. 롤백

배포 전에 아래를 정한다.

- 어떤 증상이 나면 롤백하는가
- 코드만 롤백 가능한가
- DB migration까지 되돌려야 하는가
- backward compatible 상태인가
- 임시 우회 설정이 있는가
- irreversible DDL 또는 data correction이 있는가

### 롤백 체크리스트

- [ ] migration 선반영 여부를 결정했는가
- [ ] 배포 순서를 정했는가
- [ ] rollback trigger를 정의했는가
- [ ] rollback 시 데이터 정합성 문제가 없는가
- [ ] stage 또는 운영 유사 검증을 했는가
- [ ] DB rollback 또는 backup 전략이 명시되었는가

상세 규칙은 [`governance/release-and-rollback.md`](./governance/release-and-rollback.md)를 따른다.

## 8. 운영 점검

### 공통 점검 항목

- 기동 로그
- error 로그 급증 여부
- 핵심 테이블 적재
- 외부 연동 성공/실패
- 큐, scheduler, 수신 루프 정체 여부
- 재시도 또는 dead-letter 여부
- schema/data change가 있으면 verification query 결과

### 프로젝트 패밀리 또는 런타임 역할별 운영 포인트

#### Frontend

- route 진입 가능 여부
- 메뉴 노출 여부
- build 산출물 반영 여부
- 정적 리소스 캐시 이슈 여부

#### API 서비스

- 주요 API 응답
- config 및 security 영향
- DB 적재/조회
- 예외 응답 및 권한 처리

#### Batch

- scheduler 실행 여부
- job 시작/종료 로그
- history 적재
- 실패 재시도, dead-letter, cleanup

#### Receiver

- ingress 수신 여부
- parser 또는 decoder 오류 여부
- publish 또는 저장 성공 여부
- 연속 수신 중 누락/중복/프로토콜 오류 여부

## 9. 테스트 단계 구분

다음을 서로 다른 레이어로 본다.

- `build/compile/test`
  - 코드 수준 정합성
- `smoke validation`
  - 배포 직후 핵심 기능 1~2개 확인
- `stage validation`
  - 운영 유사 환경에서 외부 연동 포함 검증
- `운영 반영 전 검증`
  - 배포 순서, 롤백 조건, 운영 점검 항목, verification query까지 포함한 최종 확인
