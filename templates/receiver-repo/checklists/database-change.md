# Database Change Checklist

## 1. Naming

- [ ] 신규 테이블명이 현재 prefix, domain, suffix 규칙과 맞는가
- [ ] 신규 컬럼명이 `*_CD`, `*_NM`, `*_VAL`, `*_YN`, `*_DTMT` 등 공통 패턴과 맞는가
- [ ] 신규 약어가 4자 기본 기준과 맞는가
- [ ] 기존 의미와 다른 약어를 새로 만들지 않았는가
- [ ] PK, FK, UK, IDX 이름이 목적과 테이블을 드러내는가

## 2. COMMENT 및 문서

- [ ] 테이블 COMMENT가 작성되었는가
- [ ] 컬럼 COMMENT가 작성되었는가
- [ ] 논리명/물리명/타입 표가 함께 갱신되었는가
- [ ] 관련 runbook, deployment-checklist, validation guide 갱신 여부를 확인했는가

## 3. Migration 및 호환성

- [ ] 신규 설치본과 운영 migration을 함께 검토했는가
- [ ] nullable, default, backfill 순서를 검토했는가
- [ ] data correction 또는 seed가 별도 파일로 분리되어야 하는가
- [ ] rollback이 가능한가
- [ ] irreversible change 여부를 표시했는가

## 4. 위험 SQL

- [ ] `DROP`, `TRUNCATE`, broad `UPDATE`, broad `DELETE`가 포함되는가
- [ ] 위험 SQL이 있다면 환경, 영향 범위, backup 또는 rollback 메모가 있는가
- [ ] pre-query, post-query, verification query가 준비되었는가
- [ ] 운영 또는 공유 환경 직접 수정 여부를 명시했는가

## 5. 검증

- [ ] row count 또는 영향 범위를 사전에 확인했는가
- [ ] migration 적용 후 검증 쿼리를 준비했는가
- [ ] 관련 compile/test/smoke 항목을 정리했는가
- [ ] 미검증 항목과 이유를 명시했는가
