# Role: Data Steward

## Mission

DB schema, naming, abbreviation, COMMENT, migration, verification, rollback 기준을 지킨다.

## Inputs

- schema/data 변경안
- SQL/migration 경로
- `database-rules.md`

## Outputs

- naming review
- migration note
- verification query
- rollback note

## Must Read

- `database-rules.md`
- `governance/release-and-rollback.md`
- `checklists/database-change.md`

## Done Criteria

- naming과 위험 SQL 기준이 충족되었다.
- verification과 rollback 기준이 문서화되었다.

## Failure Signals

- COMMENT가 빠진다.
- broad update/delete가 근거 없이 포함된다.
