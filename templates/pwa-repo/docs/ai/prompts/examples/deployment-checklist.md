# Deployment Checklist Example Prompt

```text
Create a deployment checklist for the following project change.

Repository: my-batch-service
Branch: dev
Scope: initial dev deployment checklist for batch service bootstrap
Target environments: dev
Relevant code paths:
- build.gradle
- src/main/resources/application.yml
Relevant config and docs:
- docs/runbook.md
- docs/ai/governance/release-and-rollback.md
- docs/sql/001_init.sql
Out of scope:
- production deployment execution

Requirements:
- Follow AGENTS.md, docs/ai/lifecycle.md, and docs/ai/governance/release-and-rollback.md.
- Include prerequisite config, DB migration order, deployment sequence, smoke checks, and rollback trigger conditions.
- Explicitly call out secrets or environment variables that must be set outside code.

Output format:
- Purpose
- Preconditions
- Deployment order
- Required checks before deployment
- Post-deployment smoke validation
- Rollback triggers and notes
```
