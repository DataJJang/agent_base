# aitelecom-batch Prompt Pack

기준 문서:

- [`AGENTS.md`](../../../../../AGENTS.md)
- [`docs/ai/services/batch.md`](../../../services/batch.md)
- [`docs/ai/lifecycle.md`](../../../lifecycle.md)

## 대표 경로

- `build.gradle`
- `src/main/resources/application.yml`
- `src/main/java/.../jobs`
- `src/main/resources/mapper`
- `ops-alerting-v1`

## Repo-Specific Prompt Template

```text
Create a repository-specific deliverable for aitelecom-batch.

Repository: aitelecom-batch
Branch: {{BRANCH}}
Goal: {{GOAL}}
Scope: {{SCOPE}}
Target environments: {{ENVIRONMENTS}}
Relevant batch paths:
- src/main/java/kr/co/openit/aitelecom/batch/jobs
- src/main/java/kr/co/openit/aitelecom/batch/{{DOMAIN}}
- src/main/resources/mapper
- ops-alerting-v1/sql
- src/main/resources/application.yml
Relevant docs:
- ops-alerting-v1/runbook.md
- ops-alerting-v1/deployment-checklist.md
- ops-alerting-v1/local-dev-validation.md
- {{DOC_PATH_1}}
Out of scope:
- {{OUT_OF_SCOPE}}

Requirements:
- Follow AGENTS.md, docs/ai/services/batch.md, and docs/ai/lifecycle.md.
- Include job registration, trigger behavior, mapper and SQL impact, log points, history or audit table impact, and operational sequencing.
- If schema changes exist, include migration ordering and comment or document update requirements.
- Include compile, relevant tests, and job-flow smoke validation.
- Explicitly call out unverified external dependency checks.

Output format:
- Purpose
- Scope
- Batch flow impact
- Detailed tasks
- Validation plan
- Operational and deployment notes
- Risks and follow-ups
```
