# aitelecom-backend Prompt Pack

기준 문서:

- [`AGENTS.md`](../../../../../AGENTS.md)
- [`docs/ai/services/api.md`](../../../services/api.md)
- [`docs/ai/governance/release-and-rollback.md`](../../../governance/release-and-rollback.md)

## 대표 경로

- `build.gradle`
- `src/main/resources/application.yml`
- `src/main/java/.../api`
- `src/main/java/.../domain`
- `src/main/java/.../common`

## Repo-Specific Prompt Template

```text
Create a repository-specific deliverable for aitelecom-backend.

Repository: aitelecom-backend
Branch: {{BRANCH}}
Goal: {{GOAL}}
Scope: {{SCOPE}}
Target environments: {{ENVIRONMENTS}}
Relevant backend paths:
- src/main/java/kr/co/openit/aitelecom/backend/api/{{DOMAIN}}
- src/main/java/kr/co/openit/aitelecom/backend/domain
- src/main/resources/application.yml
- {{SQL_PATH_1}}
Relevant docs:
- {{DOC_PATH_1}}
Out of scope:
- {{OUT_OF_SCOPE}}

Requirements:
- Follow AGENTS.md, docs/ai/services/api.md, and docs/ai/governance/release-and-rollback.md.
- Respect controller, service, model, repository, and query-repository responsibilities.
- Include DB, config, security, validation, exception, and rollback considerations if affected.
- Include Java compile and relevant API smoke verification in the validation plan.
- Call out manual follow-up when runtime infra or secrets are required.

Output format:
- Purpose
- Scope
- API and data impact
- Detailed tasks
- Validation plan
- Deployment and rollback notes
- Risks and open questions
```
