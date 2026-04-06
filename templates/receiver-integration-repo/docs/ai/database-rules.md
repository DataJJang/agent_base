# Database Rules

## 1. 목적

이 문서는 프로젝트 저장소에서 Database 스키마, 테이블, 컬럼, migration, COMMENT, 위험 SQL을 어떻게 다룰지 정의한다.

## 2. 기본 원칙

- 새 스키마는 현재 조직 또는 제품군에서 이미 검증된 SQL 패턴을 우선 따른다.
- 기존 레거시 이름은 정책만으로 일괄 rename 하지 않는다.
- 신규 테이블, 신규 컬럼, 신규 code value는 naming, COMMENT, migration, verification query를 함께 본다.
- 물리명은 기본적으로 대문자 snake case를 사용한다.
- DB 규칙을 어기는 예외는 repo-local 문서에 근거를 남긴다.

## 3. 테이블 네이밍 규칙

### 기본 구조

- 기본 구조는 `[SYSTEM_PREFIX]_[DOMAIN]_[ENTITY]_[SUFFIX]` 형태를 우선 사용한다.
- 전사 또는 제품군 prefix가 있으면 그것을 일관되게 사용한다.
  - 예: `AIT_`
- 도메인 prefix는 현재 자산과 맞춘다.
  - 예: `AIT_OPS_`, `PAY_`, `AUTH_`
- suffix는 해당 조직 또는 제품군에서 이미 쓰는 패턴을 우선 사용한다.
  - `INF`: 관리, 정의, 기준, 설정성 정보
  - `HST`: 이력, 로그, append 성 데이터

### 예시

- `AIT_OPS_ALRM_RULE_INF`
- `AIT_OPS_ALRM_ROOM_INF`
- `AIT_OPS_ALRM_DLVY_HST`

### 금지 또는 제한

- 화면 이름, 메뉴 이름, 구현 클래스 이름을 그대로 테이블명으로 쓰지 않는다.
- 같은 의미에 `TABLE`, `LIST`, `DATA` 같은 무의미 suffix를 붙이지 않는다.
- 동일 책임인데 `INF`, `MST`, `TB`, `TABLE`을 혼용하지 않는다.

## 4. 컬럼 네이밍 규칙

### 기본 규칙

- surrogate PK는 기본적으로 `SERL_NO`를 우선 검토한다.
- FK는 부모 테이블의 키 의미를 그대로 따른다.
  - 예: `ROOM_SERL_NO`, `ALRM_EVT_SERL_NO`
- 코드는 `*_CD`
- 이름은 `*_NM`
- 값은 `*_VAL`
- 본문/내용은 `*_CTT`
- 여부 플래그는 `*_YN`
- 일시는 `*_DTMT`
- 날짜는 `*_DT`
- 시간은 `*_TM`
- 개수는 `*_CNT`
- 응답 코드는 `RESP_CD`처럼 현재 공통 의미를 따른다.
- 정렬 또는 순서는 `ORD_NO` 같은 현재 공통 패턴을 우선 사용한다.

### 일관성 규칙

- 같은 의미에 `*_NAME`과 `*_NM`을 혼용하지 않는다.
- 같은 의미에 `*_CODE`와 `*_CD`를 혼용하지 않는다.
- 같은 의미에 `*_VALUE`와 `*_VAL`을 혼용하지 않는다.
- FK 컬럼명은 참조 대상을 유추할 수 있어야 한다.

## 5. 약어 규칙

### 기본값

- 새로 만드는 의미 약어는 4자 이내를 강한 기본값으로 한다.
- 단, 업계 표준 약어 또는 기존 조직 자산에서 널리 쓰는 약어는 예외를 허용한다.
- 읽기 어려운 약어를 만들 바에는 더 명확한 이름 또는 문서화된 예외를 사용한다.

### 현재 canonical 약어 예시

| 의미 | 권장 약어 |
| --- | --- |
| Alarm | `ALRM` |
| Template | `TMPT` |
| Scope | `SCOP` |
| Recipient | `RCPT` |
| Schedule | `SCHD` |
| Delivery | `DLVY` |
| Serial | `SERL` |
| Event | `EVT` |
| Response | `RESP` |
| Register | `REG` |
| Modify | `MOD` |
| History | `HST` |
| Information | `INF` |
| Severity | `SEV` |
| Result | `RSLT` |
| Language | `LANG` |

### 추가 규칙

- 같은 의미에 여러 약어를 혼용하지 않는다.
  - 예: `ALM`, `ALRM` 혼용 금지
- 예외를 허용한 약어는 해당 저장소 문서에 남긴다.
- 기존 legacy 약어는 즉시 교체 대상이 아니라 신규 변경 시 일관성 유지 대상으로 본다.

## 6. Constraint / Index 네이밍 규칙

- PK: `PK_<TABLE_NAME>` 또는 DB 기본 PK 이름 사용 시에도 DDL 가독성을 해치지 않게 유지한다.
- FK: `FK_<CHILD_TABLE>_<PARENT_HINT>`
- UK: `UK_<TABLE_NAME>_<KEY_PURPOSE>`
- IDX: `IDX_<TABLE_NAME>_<KEY_PURPOSE>`

### 규칙

- constraint와 index 이름에는 반드시 테이블명을 포함한다.
- anonymous index나 목적이 드러나지 않는 이름은 피한다.
- `KEY_PURPOSE`는 너무 길지 않게 핵심 컬럼 묶음을 드러내는 수준으로 쓴다.

## 7. Audit / Soft Delete 규칙

### 관리성 테이블

다음을 우선 검토한다.

- `REG_ID`
- `REG_DTMT`
- `MOD_ID`
- `MOD_DTMT`
- `DEL_YN`
- 필요 시 `USE_YN`

### 이력성 테이블

- append-only 이력이면 `REG_DTMT` 중심으로 설계할 수 있다.
- 이력이 수정될 가능성이 있으면 `MOD_*`도 추가한다.
- soft delete가 필요 없는 append-only 이력에 `DEL_YN`을 기계적으로 넣지 않는다.

## 8. COMMENT 규칙

- 테이블 COMMENT는 필수다.
- 컬럼 COMMENT는 필수다.
- 논리명 표와 SQL COMMENT는 같이 갱신한다.
- 신규 테이블/컬럼이 생기면 기준 SQL 문서의 논리명, 물리명, 타입 표도 함께 반영한다.

## 9. Migration 규칙

- 신규 설치본과 운영 migration은 함께 검토한다.
- 파일명은 순번 + 목적 중심으로 짓는다.
  - 예: `009_add_room_link.sql`
- DDL, seed, backfill은 위험도가 다르면 분리한다.
- schema change에는 verification query와 rollback note를 같이 남긴다.
- 기존 데이터 영향이 있으면 nullable/default/backfill 순서를 명시한다.

## 10. 위험 SQL 규칙

### 금지 기본값

다음은 명시적 승인과 안전 근거 없이는 금지다.

- `DROP DATABASE`
- `DROP TABLE`
- `TRUNCATE TABLE`
- restrictive `WHERE` 없는 `DELETE`
- restrictive `WHERE` 없는 `UPDATE`
- 데이터 유실성 `ALTER`를 근거 없이 직접 수행
- 검증 범위 없이 `SET FOREIGN_KEY_CHECKS=0` 등 안전장치 비활성화

### 제한적 허용 대상

아래는 문서화된 조건을 만족할 때만 제한적으로 허용한다.

- 대량 backfill
- 데이터 정정 DML
- irreversible DDL
- 운영 또는 공유 환경 대상 직접 수정

### 제한적 허용 시 필수 조건

- 대상 환경을 명시한다.
- 실행 전 row count 또는 영향 범위를 확인한다.
- pre-query와 post-query를 준비한다.
- rollback 또는 backup 전략을 명시한다.
- change note 또는 관련 문서에 남긴다.

## 11. 필수 동반 문서

DB schema, migration, seed, backfill, data correction이 있으면 아래를 함께 본다.

- [`core-rules.md`](./core-rules.md)
- [`lifecycle.md`](./lifecycle.md)
- [`governance/release-and-rollback.md`](./governance/release-and-rollback.md)
- [`governance/quality-gates.md`](./governance/quality-gates.md)
- [`../../checklists/database-change.md`](../../checklists/database-change.md)
