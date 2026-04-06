# Impact Analysis Prompt

## Prompt Template

```text
Create an impact analysis for the following project change.

Repository: {{REPOSITORY}}
Branch: {{BRANCH}}
Scope: {{SCOPE}}
Target environments: {{ENVIRONMENTS}}
Relevant code paths:
- {{CODE_PATH_1}}
- {{CODE_PATH_2}}
Relevant config, SQL, and docs:
- {{CONFIG_FILE}}
- {{SQL_FILE}}
- {{DOC_FILE}}
Out of scope:
- {{OUT_OF_SCOPE}}

Requirements:
- Follow AGENTS.md, docs/ai/core-rules.md, docs/ai/database-rules.md when DB is involved, docs/ai/lifecycle.md, and the relevant service guide.
- Separate direct impact from indirect or potential impact.
- Cover code, config, DB, external integrations, docs, deployment sequence, rollback, and operations.
- If schema or data change exists, review naming, abbreviation, COMMENT, migration ordering, risky SQL, and verification query requirements.
- Distinguish confirmed facts from inferred risks.
- Include minimum required validation and recommended follow-up documents.

Output format:
- Purpose
- Scope
- Direct impact
- Indirect impact
- Schema and data change impact
- Risky SQL and rollback impact
- Operational and deployment impact
- Validation requirements
- Open questions
```
