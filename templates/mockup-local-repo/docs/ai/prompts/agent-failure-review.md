# Agent Failure Review Prompt

이 프롬프트는 Agent 실패 사례를 정리하고 하네스 구조 보강 포인트를 찾게 한다.

```text
Create an agent failure review for the following case.

Follow these sources of truth:
1. AGENTS.md
2. docs/ai/governance/agent-failure-learning.md
3. docs/ai/governance/evaluation-and-drift.md
4. docs/ai/governance/quality-gates.md
5. checklists/agent-failure-review.md

Input:
- repository and branch
- original user request
- expected result
- actual result
- changed files or attempted commands
- validation that failed or was skipped

Tasks:
- classify the failure type
- identify root cause
- identify where the harness must be strengthened
- propose the minimum document, prompt, template, or script changes
- define how to verify the fix

Output format:
- summary
- expected vs actual
- failure type
- root cause
- affected harness areas
- concrete fixes
- validation plan
- follow-up items
```
