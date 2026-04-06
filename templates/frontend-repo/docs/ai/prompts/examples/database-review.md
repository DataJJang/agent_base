# Database Review Prompt Example

```text
Create a database change review for the following project work item.

Repository: my-repository
Branch: dev
Scope: review a schema and data change before implementation or deployment
Target environments: dev, stg
Relevant code paths:
- src/main/java
- src/main/resources/mapper
Relevant SQL and docs:
- docs/sql/001_init.sql
- db/migration/009_add_new_table.sql
- docs/ai/database-rules.md
- checklists/database-change.md
Out of scope:
- production execution of the SQL itself

Requirements:
- Follow AGENTS.md, docs/ai/core-rules.md, docs/ai/database-rules.md, docs/ai/governance/release-and-rollback.md, and checklists/database-change.md.
- Review new or changed table names, column names, abbreviations, constraints, indexes, and COMMENT coverage.
- Explicitly identify any risky SQL such as DROP, TRUNCATE, broad UPDATE, broad DELETE, or irreversible ALTER.
- Call out migration ordering, rollback or backup strategy, and required verification queries.
- Distinguish confirmed facts from assumptions.

Output format:
- Purpose
- Scope
- Naming and abbreviation review
- Schema and constraint review
- COMMENT and migration review
- Risky SQL review
- Rollback and verification query plan
- Open questions
```
