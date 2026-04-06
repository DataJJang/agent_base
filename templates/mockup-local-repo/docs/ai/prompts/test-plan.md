# Test Plan Prompt

## Prompt Template

```text
Create a test and validation plan for the following project change.

Repository: {{REPOSITORY}}
Branch: {{BRANCH}}
Scope: {{SCOPE}}
Target environments: {{ENVIRONMENTS}}
Relevant code paths:
- {{CODE_PATH_1}}
- {{CODE_PATH_2}}
Relevant test, config, and docs:
- {{TEST_PATH_1}}
- {{CONFIG_FILE}}
- {{DOC_FILE}}
Out of scope:
- {{OUT_OF_SCOPE}}

Requirements:
- Follow AGENTS.md and docs/ai/governance/quality-gates.md.
- Cover unit, integration, regression, smoke, and manual validation as applicable.
- Map tests to impacted layers: UI, API, batch, receiver, DB, external integration.
- Distinguish required automated checks from manual verification.
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
