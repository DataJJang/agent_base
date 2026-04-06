# aitelecom-service-api Prompt Pack

기준 문서:

- [`AGENTS.md`](../../../../../AGENTS.md)
- [`docs/ai/services/api.md`](../../../services/api.md)
- [`docs/ai/governance/release-and-rollback.md`](../../../governance/release-and-rollback.md)

## 대표 경로

- `build.gradle`
- `src/main/resources/application.yml`
- `src/main/java/.../api`
- `src/main/java/.../common`

## Repo-Specific Prompt Template

```text
Create a repository-specific deliverable for aitelecom-service-api.

Repository: aitelecom-service-api
Branch: {{BRANCH}}
Goal: {{GOAL}}
Scope: {{SCOPE}}
Target environments: {{ENVIRONMENTS}}
Relevant API paths:
- src/main/java/kr/co/openit/aitelecom/service/api/{{DOMAIN}}
- src/main/resources/application.yml
- {{SQL_PATH_1}}
Relevant docs:
- {{DOC_PATH_1}}
Out of scope:
- {{OUT_OF_SCOPE}}

Requirements:
- Follow AGENTS.md and docs/ai/services/api.md.
- Treat this repository as an API service with the same core structure rules as backend, but call out any service-api-specific public contract concerns.
- Include controller, service, model, repository, config, validation, and deployment impact when relevant.
- Include compile and API verification in the validation plan.
- Clearly distinguish confirmed contract changes from assumptions.

Output format:
- Purpose
- Scope
- Service contract impact
- Detailed tasks
- Validation plan
- Deployment notes
- Risks and open questions
```
