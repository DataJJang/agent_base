# Deployment Checklist Prompt

## Prompt Template

```text
Create a deployment checklist for the following project change.

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
- Follow AGENTS.md, docs/ai/database-rules.md when DB is involved, docs/ai/lifecycle.md, and docs/ai/governance/release-and-rollback.md.
- Separate pre-deploy, deploy, post-deploy, and rollback-trigger checks.
- Explicitly list environment variables, migration ordering, restart order, dependency checks, and smoke validation.
- If schema or data change exists, include pre-query, post-query, verification query, risky DML check, and rollback or backup notes.
- Call out backward compatibility assumptions.
- Include who must confirm what if the procedure requires manual coordination.

Output format:
- Purpose
- Preconditions
- DB pre-deploy checks
- Pre-deploy checklist
- Deploy sequence
- DB post-deploy verification
- Post-deploy validation
- Rollback conditions
- Rollback steps
- Open risks
```
