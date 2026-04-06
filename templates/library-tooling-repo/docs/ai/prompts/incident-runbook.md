# Incident Runbook Prompt

## Prompt Template

```text
Create an incident runbook draft for the following project component or flow.

Repository: {{REPOSITORY}}
Branch: {{BRANCH}}
Scope: {{SCOPE}}
Target environments: {{ENVIRONMENTS}}
Relevant code and config paths:
- {{CODE_PATH_1}}
- {{CONFIG_FILE}}
Reference docs:
- {{RUNBOOK_FILE}}
- {{MANUAL_FILE}}
Out of scope:
- {{OUT_OF_SCOPE}}

Requirements:
- Follow AGENTS.md, docs/ai/lifecycle.md, and the relevant service guide.
- Focus on symptoms, first checks, likely failure categories, evidence to collect, short-term mitigation, and escalation points.
- Distinguish infrastructure failure, config error, data issue, code bug, and external dependency failure.
- Include log locations, key tables or queues, and restart or retry cautions when confirmed.
- Explicitly list what should not be done during first response.

Output format:
- Incident scope
- Observable symptoms
- First-response checklist
- Evidence collection
- Likely causes
- Safe mitigations
- Escalation criteria
- Post-incident follow-ups
```
