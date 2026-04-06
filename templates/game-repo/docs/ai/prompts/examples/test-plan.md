# Test Plan Example Prompt

```text
Create a test and validation plan for the following project change.

Repository: my-batch-service
Branch: dev
Scope: initial validation plan for a new batch repository
Target environments: local, dev
Relevant code paths:
- src/main/java/com/example/jobs
- src/main/java/com/example/service
Relevant test, config, and docs:
- src/test/java
- src/main/resources/application.yml
- docs/ai/governance/quality-gates.md
Out of scope:
- long-running production volume test

Requirements:
- Follow AGENTS.md and docs/ai/governance/quality-gates.md.
- Cover compile, unit test, mapper regression, job smoke validation, and manual verification.
- Explicitly state what cannot be validated in the current environment.

Output format:
- Purpose
- Scope
- Test layers and rationale
- Detailed test cases
- Required commands or procedures
- Expected results
- Risks and unverified items
```
