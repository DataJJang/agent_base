# Operations Manual Example Prompt

```text
Create an operations manual draft for the following project scope.

Repository: my-batch-service
Branch: dev
Scope: initial batch operation guide for job scheduling and execution history verification
Target environments: dev
Relevant code paths:
- src/main/java/com/example/jobs
- src/main/java/com/example/service
Relevant operational files:
- src/main/resources/application.yml
- docs/runbook.md
- docs/manual/batch-operations.md
Out of scope:
- production incident casebook

Requirements:
- Follow AGENTS.md, docs/ai/lifecycle.md, and docs/ai/services/batch.md.
- Cover startup, shutdown, scheduler enable flags, core logs, history tables, and dependency checks.
- Distinguish operator tasks from developer tasks.
- Include known limitations and manual verification items.

Output format:
- Purpose
- Scope
- Architecture and dependencies
- Operating procedure
- Health and verification checks
- Failure symptoms and first response
- Notes and follow-ups
```
