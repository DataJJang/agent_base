# Agent Failure Review Example Prompt

```text
Create an agent failure review for the following case.

Follow these sources of truth:
1. AGENTS.md
2. docs/ai/governance/agent-failure-learning.md
3. docs/ai/governance/evaluation-and-drift.md
4. docs/ai/governance/quality-gates.md
5. checklists/agent-failure-review.md

Repository: my-backend-service
Branch: dev
Scope: wrong template and command set selected during bootstrap
Expected result:
- backend-service template should be selected
- gradle-based command-catalog should be generated
Actual result:
- web-app template was selected
- npm-based commands were suggested
Relevant files:
- docs/ai/project-selection-mapping.md
- docs/ai/prompts/examples/project-bootstrap.md
- checklists/project-interview.md
Out of scope:
- business feature implementation

Return:
- failure classification
- root cause
- affected harness documents
- concrete reinforcement actions
- validation plan
```
