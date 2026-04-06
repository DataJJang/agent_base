# Operations Manual Prompt

## Prompt Template

```text
Create an operations manual draft for the following project scope.

Repository: {{REPOSITORY}}
Branch: {{BRANCH}}
Scope: {{SCOPE}}
Target environments: {{ENVIRONMENTS}}
Relevant code paths:
- {{CODE_PATH_1}}
- {{CODE_PATH_2}}
Relevant operational files:
- {{CONFIG_FILE}}
- {{RUNBOOK_FILE}}
- {{MANUAL_FILE}}
Out of scope:
- {{OUT_OF_SCOPE}}

Requirements:
- Follow AGENTS.md, docs/ai/lifecycle.md, and the relevant service guide.
- Cover startup, shutdown, health checks, log points, dependency checks, and common operational scenarios.
- Include environment-specific considerations only when confirmed by source files.
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
