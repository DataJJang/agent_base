# Batch Service Master Prompt

적용 기준 문서:

- [`AGENTS.md`](../../../AGENTS.md)
- [`docs/ai/core-rules.md`](../core-rules.md)
- [`docs/ai/database-rules.md`](../database-rules.md)
- [`docs/ai/services/batch.md`](../services/batch.md)
- [`docs/ai/lifecycle.md`](../lifecycle.md)
- [`docs/ai/governance/quality-gates.md`](../governance/quality-gates.md)

## Prompt Template

```text
You are preparing a batch-service deliverable for the target repository.

Follow these sources of truth in order:
1. AGENTS.md
2. docs/ai/core-rules.md
3. docs/ai/database-rules.md when schema, seed, backfill, or mapper SQL is involved
4. docs/ai/services/batch.md
5. docs/ai/lifecycle.md
6. docs/ai/governance/quality-gates.md
7. The repository-specific files listed below

Repository: {{REPOSITORY}}
Branch: {{BRANCH}}
Goal: {{GOAL}}
Scope: {{SCOPE}}
Target environments: {{ENVIRONMENTS}}
Relevant code paths:
- {{CODE_PATH_1}}
- {{CODE_PATH_2}}
Relevant config and docs:
- {{CONFIG_PATH_1}}
- {{SQL_PATH_1}}
- {{DOC_PATH_1}}
Out of scope:
- {{OUT_OF_SCOPE}}

Create a {{OUTPUT_TYPE}} for this batch work.

Requirements:
- Respect current job, service, model, mapper, XML, and SQL-document structure.
- Consider scheduler timing, retry, idempotency, and operational observability.
- If DDL, seed, backfill, or migration is involved, call out naming, COMMENT, deployment ordering, verification query, and rollback constraints.
- If the work affects external integrations, include dependency and failure-mode notes.
- Explicitly identify any risky SQL or data-correction work.
- Include minimum verification steps:
  - compile
  - relevant automated tests
  - query or mapper regression check
  - job flow or trigger smoke validation
- Explicitly identify operational follow-ups such as runbook or deployment-checklist updates.

Output format:
- Purpose
- Scope
- Job and data flow impact
- Detailed work items
- Validation plan
- Operational considerations
- Risks and follow-ups
```

## Best Use Cases

- 신규 배치 잡 설계/점검 문서
- 배치 운영 매뉴얼 초안
- 스케줄러/재시도/이력 테이블 영향도 분석
- SQL 및 배포 순서 체크리스트 생성
