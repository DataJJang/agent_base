# API Service Master Prompt

적용 기준 문서:

- [`AGENTS.md`](../../../AGENTS.md)
- [`docs/ai/core-rules.md`](../core-rules.md)
- [`docs/ai/database-rules.md`](../database-rules.md)
- [`docs/ai/services/api.md`](../services/api.md)
- [`docs/ai/governance/quality-gates.md`](../governance/quality-gates.md)
- [`docs/ai/governance/release-and-rollback.md`](../governance/release-and-rollback.md)

## Prompt Template

```text
You are preparing an API-service deliverable for the target repository.

Follow these sources of truth in order:
1. AGENTS.md
2. docs/ai/core-rules.md
3. docs/ai/database-rules.md when schema, query, or migration is involved
4. docs/ai/services/api.md
5. docs/ai/governance/quality-gates.md
6. docs/ai/governance/release-and-rollback.md
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

Create a {{OUTPUT_TYPE}} for this API service work.

Requirements:
- Respect current controller/service/model/repository/query-repository boundaries.
- Call out request and response contract impact.
- Distinguish JPA, Querydsl, and native query or repository changes.
- Include validation and exception-handling expectations.
- Include environment or profile impact when config changes are involved.
- Include DB migration, naming, COMMENT, verification query, and rollback considerations if the change touches schema or query behavior.
- Explicitly identify any risky SQL or data-correction work.
- Include minimum verification steps:
  - compile
  - automated tests if present
  - target API smoke scenario
- Explicitly list assumptions and manual checks.

Output format:
- Purpose
- Scope
- API and data contract impact
- Detailed work items
- Validation plan
- Deployment and rollback notes
- Risks and open questions
```

## Best Use Cases

- API 변경 영향도 분석
- 운영 매뉴얼 또는 점검 항목 작성
- 배포 체크리스트 작성
- DB/설정/API 계약이 함께 바뀌는 작업 정리
