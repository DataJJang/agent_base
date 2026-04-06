# Impact Analysis Example Prompt

```text
Create an impact analysis for the following project work item.

Repository: my-batch-service
Branch: dev
Scope: repository bootstrap and first delivery setup for a new batch service
Target environments: local, dev
Relevant code paths:
- build.gradle
- src/main/java/com/example
Relevant config and docs:
- src/main/resources/application.yml
- docs/ai/project-generation-spec.md
- docs/ai/governance/release-and-rollback.md
Out of scope:
- business feature implementation

Requirements:
- Follow AGENTS.md, docs/ai/core-rules.md, docs/ai/lifecycle.md, and docs/ai/services/batch.md.
- Cover code, config, DB, docs, deployment order, rollback concerns, and operational follow-ups.
- Distinguish immediate bootstrap work from later feature work.

Output format:
- Purpose
- Scope
- Affected areas
- Risks
- Validation needs
- Operational and documentation follow-ups
```
