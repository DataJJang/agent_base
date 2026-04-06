# Release And Rollback Rules

## 1. 릴리즈 영향도

아래 중 하나라도 있으면 릴리즈 영향도를 명시한다.

- API 계약 변경
- DB 스키마 변경
- seed, backfill, data correction
- 외부 연동 변경
- 배치 스케줄 또는 receiver ingress 변경
- 운영 토큰 또는 권한 변경

## 2. DB 변경 분류

DB change는 아래로 나눠서 본다.

- compatible schema change
  - nullable column 추가, optional index 추가 등
- non-compatible schema change
  - 컬럼 삭제, 타입 축소, unique 강화 등
- data correction
  - 운영 데이터 정정, mass update, cleanup
- irreversible change
  - rollback이 어려운 DDL 또는 대량 DML

## 3. 배포 순서 기준

- DB 선반영이 필요한지 먼저 판단한다.
- backward compatible 여부를 먼저 본다.
- feature toggle 또는 enable flag가 있으면 우선 활용을 검토한다.
- inter-service dependency가 있으면 호출 순서와 readiness를 함께 본다.
- schema/data change가 있으면 pre-query, post-query, verification query를 같이 준비한다.

## 4. 위험 SQL 기준

### 금지 기본값

- `DROP DATABASE`
- `DROP TABLE`
- `TRUNCATE TABLE`
- restrictive `WHERE` 없는 `DELETE`
- restrictive `WHERE` 없는 `UPDATE`
- 영향 범위 설명 없는 data-loss `ALTER`

### 제한적 허용

- 대량 backfill
- data correction
- irreversible DDL
- shared, stg, prd 같은 운영성 환경 직접 수정

### 제한적 허용 시 필수 메모

- 대상 환경
- 예상 row count 또는 영향 범위
- rollback 또는 backup 전략
- verification query
- 관련 문서 또는 change note

## 5. 롤백 기준

배포 전에 아래를 정한다.

- 어떤 증상이 나면 롤백하는가
- 코드만 롤백 가능한가
- DB migration까지 되돌려야 하는가
- 임시 우회 설정이 있는가
- 데이터 정합성 확인 쿼리가 무엇인가

## 6. 권장 롤백 전략

- 하위 호환이 없는 스키마 변경은 단계 배포를 우선 검토한다.
- 완전 롤백이 어려운 운영성 기능은 disable flag를 먼저 준비한다.
- DB 선반영이 있으면 롤백 순서를 문서로 남긴다.
- irreversible change는 rollback 대신 stop condition과 post-check를 더 명확히 적는다.

## 7. 체크리스트

- [ ] migration 선반영 여부를 결정했는가
- [ ] 배포 순서를 정했는가
- [ ] rollback trigger를 정의했는가
- [ ] rollback 시 데이터 정합성 문제가 없는가
- [ ] stage 또는 운영 유사 검증을 했는가
- [ ] 위험 SQL 포함 여부를 검토했는가
- [ ] verification query를 준비했는가
- [ ] backup 또는 우회 전략을 문서화했는가
