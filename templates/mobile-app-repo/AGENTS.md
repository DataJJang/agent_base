# Project Agent Entry

This file is the canonical AI guidance entrypoint for a mobile-app family repository.

## Use This File As The Entry Map

- Detailed rules live under [docs/ai/README.md](./docs/ai/README.md).
- Interactive bootstrap starts at [docs/ai/project-bootstrap.md](./docs/ai/project-bootstrap.md).
- Normalized creation schema lives in [docs/ai/project-generation-spec.md](./docs/ai/project-generation-spec.md).
- Project families and runtime roles are defined in [docs/ai/project-family-map.md](./docs/ai/project-family-map.md).
- Selection mapping lives in [docs/ai/project-selection-mapping.md](./docs/ai/project-selection-mapping.md).
- Recommended stack defaults live under [docs/ai/stack-matrix.md](./docs/ai/stack-matrix.md).
- DB naming and risky SQL rules live under [docs/ai/database-rules.md](./docs/ai/database-rules.md).
- Local commit gate and hook rules live under [docs/ai/governance/pre-commit-hooks.md](./docs/ai/governance/pre-commit-hooks.md).
- Agent failure capture and harness reinforcement rules live under [docs/ai/governance/agent-failure-learning.md](./docs/ai/governance/agent-failure-learning.md).
- Bootstrap checklists live under [checklists/](./checklists/).
- Legacy files [codex.md](./codex.md) and [codex-prompts.md](./codex-prompts.md) are migration pointers only.

## Template Identity

- Template type: project-family template
- Primary project family: mobile-app
- Primary runtime roles: client

## Read Order

1. AGENTS.md
2. [docs/ai/project-bootstrap.md](./docs/ai/project-bootstrap.md)
3. [docs/ai/project-generation-spec.md](./docs/ai/project-generation-spec.md)
4. [docs/ai/project-family-map.md](./docs/ai/project-family-map.md)
5. [docs/ai/project-selection-mapping.md](./docs/ai/project-selection-mapping.md)
6. [docs/ai/stack-matrix.md](./docs/ai/stack-matrix.md)
7. [docs/ai/core-rules.md](./docs/ai/core-rules.md)
8. [docs/ai/database-rules.md](./docs/ai/database-rules.md) when the repo owns schema, migration, SQL, or heavy query work
9. [docs/ai/lifecycle.md](./docs/ai/lifecycle.md)
10. [docs/ai/architecture-map.md](./docs/ai/architecture-map.md)
11. [docs/ai/command-catalog.md](./docs/ai/command-catalog.md)
12. Relevant runtime-role guides under docs/ai/services/
13. [docs/ai/governance/quality-gates.md](./docs/ai/governance/quality-gates.md)
14. [docs/ai/governance/git-workflow.md](./docs/ai/governance/git-workflow.md)
15. [checklists/project-interview.md](./checklists/project-interview.md)
16. [checklists/project-creation.md](./checklists/project-creation.md)
17. [docs/ai/governance/pre-commit-hooks.md](./docs/ai/governance/pre-commit-hooks.md)
18. [docs/ai/governance/agent-failure-learning.md](./docs/ai/governance/agent-failure-learning.md)
19. [checklists/agent-failure-review.md](./checklists/agent-failure-review.md)
20. [docs/ai/prompts/examples/getting-started.md](./docs/ai/prompts/examples/getting-started.md)

## Non-Negotiables

- Follow the nearest existing code pattern before inventing structure.
- Do not commit secrets, tokens, production credentials, or real identifiers.
- Prefer compatible changes over breaking changes.
- Do not push without at least one relevant verification step.
- Install and review local pre-commit hooks before the first shared delivery.
- If an agent failure repeats or exposes a harness gap, record it and reinforce the harness before closing the loop.
- Use `scripts/record_agent_failure.py` when a repeatable failure should be captured before harness reinforcement.
- First delivery must fix project family, runtime roles, stack, commands, and bootstrap documents.

## Template Start Sequence

1. Run the interview flow from [docs/ai/project-bootstrap.md](./docs/ai/project-bootstrap.md).
2. Fill [docs/ai/project-generation-spec.md](./docs/ai/project-generation-spec.md).
3. Check defaults in [docs/ai/stack-matrix.md](./docs/ai/stack-matrix.md).
4. Install the local commit gate with `python3 scripts/install_git_hooks.py`.
5. Review `.agent-base/pre-commit-config.json` and align the preset with the real repository commands.
6. Use [docs/ai/prompts/examples/getting-started.md](./docs/ai/prompts/examples/getting-started.md).
7. Complete [checklists/project-interview.md](./checklists/project-interview.md) and [checklists/project-creation.md](./checklists/project-creation.md).
