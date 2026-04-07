# Project Agent Entry

This file is the canonical AI guidance entrypoint for a project repository template.

## Use This File As The Entry Map

- Canonical guidance starts here.
- Detailed rules live under [`docs/ai/README.md`](./docs/ai/README.md).
- Agent role definitions live under [`docs/ai/roles/README.md`](./docs/ai/roles/README.md).
- Interactive repository bootstrap starts at [`docs/ai/project-bootstrap.md`](./docs/ai/project-bootstrap.md).
- Existing repository adoption starts at [`docs/ai/project-adoption.md`](./docs/ai/project-adoption.md).
- The recommended executable wrapper for bootstrap is [`docs/ai/project-bootstrap-cli.md`](./docs/ai/project-bootstrap-cli.md) and `source/scripts/project_bootstrap_cli.py`.
- The normalized creation schema lives in [`docs/ai/project-generation-spec.md`](./docs/ai/project-generation-spec.md).
- The normalized adoption schema lives in [`docs/ai/adoption-spec.md`](./docs/ai/adoption-spec.md).
- Project families and runtime roles are defined in [`docs/ai/project-family-map.md`](./docs/ai/project-family-map.md).
- Project selection to template and output mapping lives in [`docs/ai/project-selection-mapping.md`](./docs/ai/project-selection-mapping.md).
- Generator usage and scaffold support live in [`docs/ai/project-generator.md`](./docs/ai/project-generator.md).
- Token substitution rules live in [`docs/ai/token-substitution.md`](./docs/ai/token-substitution.md).
- Recommended stack and version defaults live in [`docs/ai/stack-matrix.md`](./docs/ai/stack-matrix.md).
- Database naming, schema, and risky SQL rules live under [`docs/ai/database-rules.md`](./docs/ai/database-rules.md).
- Local commit gate and hook rules live under [`docs/ai/governance/pre-commit-hooks.md`](./docs/ai/governance/pre-commit-hooks.md).
- Agent failure capture and harness reinforcement rules live under [`docs/ai/governance/agent-failure-learning.md`](./docs/ai/governance/agent-failure-learning.md).
- Failure recording helper script lives at `scripts/record_agent_failure.py`.
- Repository inventory helper script lives at `scripts/analyze_repository.py`.
- Failure summary helper script lives at `scripts/summarize_failures.py`.
- Prompt templates live under [`docs/ai/prompts/README.md`](./docs/ai/prompts/README.md).
- Role-specific prompt templates live under [`docs/ai/prompts/roles/README.md`](./docs/ai/prompts/roles/README.md).
- Repository bootstrap checklists live under [`checklists/`](./checklists/).
- Legacy files [`codex.md`](./codex.md) and [`codex-prompts.md`](./codex-prompts.md) are migration pointers only.

## Project Families Supported By This Template

- `game`
- `web-app`
- `pwa`
- `mobile-app`
- `backend-service`
- `batch-worker`
- `receiver-integration`
- `mockup-local`
- `library-tooling`

## Runtime Roles Used As Secondary Architecture Labels

- `frontend`
- `api`
- `batch`
- `receiver`
- `client`
- `tooling`
- `worker`

## Agentic Roles Supported By This Template

- `orchestrator`
- `product-analyst`
- `solution-architect`
- `bootstrap-planner`
- `runtime-engineer`
- `data-steward`
- `security-reviewer`
- `qa-validator`
- `docs-operator`
- `release-manager`
- `failure-curator`
- `legacy-analyst`
- `migration-planner`
- `compatibility-reviewer`
- `refactor-guardian`
- `cutover-manager`

## Read Order

1. This `AGENTS.md`
2. [`docs/ai/project-bootstrap.md`](./docs/ai/project-bootstrap.md) when starting or adopting a repository
3. [`docs/ai/project-bootstrap-cli.md`](./docs/ai/project-bootstrap-cli.md)
4. [`docs/ai/project-adoption.md`](./docs/ai/project-adoption.md) when working with an existing repository
5. [`docs/ai/project-generation-spec.md`](./docs/ai/project-generation-spec.md)
6. [`docs/ai/adoption-spec.md`](./docs/ai/adoption-spec.md)
7. [`docs/ai/project-family-map.md`](./docs/ai/project-family-map.md)
8. [`docs/ai/project-selection-mapping.md`](./docs/ai/project-selection-mapping.md)
9. [`docs/ai/roles/README.md`](./docs/ai/roles/README.md)
10. [`docs/ai/project-generator.md`](./docs/ai/project-generator.md)
11. [`docs/ai/token-substitution.md`](./docs/ai/token-substitution.md)
12. [`docs/ai/stack-matrix.md`](./docs/ai/stack-matrix.md)
13. [`docs/ai/core-rules.md`](./docs/ai/core-rules.md)
14. [`docs/ai/database-rules.md`](./docs/ai/database-rules.md) when the repo owns schema, migration, SQL, or heavy query work
15. [`docs/ai/lifecycle.md`](./docs/ai/lifecycle.md)
16. [`docs/ai/architecture-map.md`](./docs/ai/architecture-map.md)
17. [`docs/ai/repository-inventory.md`](./docs/ai/repository-inventory.md) when discovering an existing repository
18. [`docs/ai/migration-strategy.md`](./docs/ai/migration-strategy.md) when planning conversion or cutover
19. [`docs/ai/command-catalog.md`](./docs/ai/command-catalog.md)
20. The relevant runtime-role guide under `docs/ai/services/`
21. [`docs/ai/governance/quality-gates.md`](./docs/ai/governance/quality-gates.md)
22. [`docs/ai/governance/git-workflow.md`](./docs/ai/governance/git-workflow.md) when branch, commit, PR, or merge behavior matters
23. [`docs/ai/governance/pre-commit-hooks.md`](./docs/ai/governance/pre-commit-hooks.md) before enabling local commit gates
24. [`docs/ai/governance/agent-failure-learning.md`](./docs/ai/governance/agent-failure-learning.md) when repeated mistakes expose harness gaps
25. [`docs/ai/document-routing.md`](./docs/ai/document-routing.md) when documentation changes are involved
26. [`docs/ai/prompts/roles/README.md`](./docs/ai/prompts/roles/README.md)
27. [`checklists/project-interview.md`](./checklists/project-interview.md) when the repository is still in discovery or bootstrap
28. [`checklists/project-adoption.md`](./checklists/project-adoption.md) when a brownfield repository is being onboarded
29. [`checklists/agent-role-selection.md`](./checklists/agent-role-selection.md) when multi-agent execution or specialist handoff matters
30. [`checklists/agent-handoff.md`](./checklists/agent-handoff.md) when work moves between specialized agents
31. [`checklists/database-change.md`](./checklists/database-change.md) when schema, migration, seed, or data-correction work is involved
32. [`checklists/agent-failure-review.md`](./checklists/agent-failure-review.md) when a failure case should be reinforced into the harness

## Non-Negotiables

- Follow the nearest existing code pattern before inventing structure.
- Do not commit secrets, tokens, real identifiers, or production credentials.
- Prefer compatible changes over breaking changes.
- Update code, config, DB, docs, and validation together when the change spans them.
- Do not run destructive DB commands without explicit approval, rollback or backup notes, and verification queries.
- Do not push without at least one relevant verification step.
- Install and review local pre-commit hooks before the first shared delivery.
- Role-heavy changes must explicitly assign an orchestrator, implementation owner, validator, and documentation owner.
- DB-owning changes must involve `data-steward` responsibilities even if one person or one agent wears multiple hats.
- Production-significant security changes must include `security-reviewer` output before completion.
- If an agent failure repeats or exposes a harness gap, record it and reinforce the harness before closing the loop.
- New repository work must resolve project family, runtime roles, stack, commands, and documentation responsibilities before the first shared delivery.

## Where To Find Commands

- Web and app-style repositories usually define commands in `package.json`, `pubspec.yaml`, lock files, or repo-local bootstrap manifests.
- Java repositories usually define commands in `build.gradle`.
- Unity repositories usually define runtime and editor automation through Unity version docs, project settings, and repo-local scripts.
- Environment and profile keys usually live in `src/main/resources/application.yml`, `.env*`, platform config files, or repo-local environment docs.
- DB change verification queries and migration command notes belong in [`docs/ai/command-catalog.md`](./docs/ai/command-catalog.md).
- Pre-commit gate installation and repo-local hook behavior belong in [`docs/ai/governance/pre-commit-hooks.md`](./docs/ai/governance/pre-commit-hooks.md).
- Failure case storage and reinforcement workflow belong in [`docs/ai/governance/agent-failure-learning.md`](./docs/ai/governance/agent-failure-learning.md).
- If the repo has additional runbooks or validation guides, record them in [`docs/ai/command-catalog.md`](./docs/ai/command-catalog.md).
- If the repo is new, fix the first build, compile, test, smoke, and deploy-check commands before the first PR.

## When Starting A New Repository

Read these in order:

1. [`docs/ai/project-bootstrap.md`](./docs/ai/project-bootstrap.md)
2. [`docs/ai/project-bootstrap-cli.md`](./docs/ai/project-bootstrap-cli.md)
3. [`docs/ai/project-generation-spec.md`](./docs/ai/project-generation-spec.md)
4. [`docs/ai/project-family-map.md`](./docs/ai/project-family-map.md)
5. [`docs/ai/project-selection-mapping.md`](./docs/ai/project-selection-mapping.md)
6. [`docs/ai/project-generator.md`](./docs/ai/project-generator.md)
7. [`docs/ai/token-substitution.md`](./docs/ai/token-substitution.md)
8. [`docs/ai/stack-matrix.md`](./docs/ai/stack-matrix.md)
9. [`docs/ai/database-rules.md`](./docs/ai/database-rules.md) if the repo owns schema, migration, seed, or query-heavy persistence
10. [`docs/ai/roles/README.md`](./docs/ai/roles/README.md)
11. [`checklists/project-interview.md`](./checklists/project-interview.md)
12. [`checklists/agent-role-selection.md`](./checklists/agent-role-selection.md)
13. [`checklists/project-creation.md`](./checklists/project-creation.md)
14. [`docs/ai/governance/pre-commit-hooks.md`](./docs/ai/governance/pre-commit-hooks.md)
15. [`docs/ai/prompts/examples/README.md`](./docs/ai/prompts/examples/README.md)

## When Docs Must Be Updated

Check [`docs/ai/document-routing.md`](./docs/ai/document-routing.md) when any of the following changes:

- project family or runtime-role assumptions
- API contract
- DB schema, migration, seed, naming exception, or data-correction query
- operational settings
- deployment order
- validation procedure
- user-facing workflow
- incident response or rollback behavior
- agent role assignment or handoff model

## Tool Adapters

- Claude Code: [`CLAUDE.md`](./CLAUDE.md)
- Gemini CLI: [`GEMINI.md`](./GEMINI.md)
- GitHub Copilot: [`.github/copilot-instructions.md`](./.github/copilot-instructions.md)
- Cursor: [`.cursor/rules/00-base.mdc`](./.cursor/rules/00-base.mdc)
- Windsurf guidance: [`docs/ai/tools/windsurf.md`](./docs/ai/tools/windsurf.md)

## Prompts

Use [`docs/ai/prompts/README.md`](./docs/ai/prompts/README.md) for:

- interactive project bootstrap interview
- project spec finalization
- scaffold planning
- project generator execution
- build guides
- operations manuals
- deployment checklists
- test and validation plans
- incident runbooks
- impact analysis
- database change review examples
- project-family bootstrap prompt examples
- role-specific specialist prompts

## Quality Gate Reminder

Before completion, confirm:

- project family and runtime roles are explicitly fixed
- build, compile, or test was run
- unverified items are explicitly listed
- rollout or operational risk is called out when relevant
- related docs are updated or intentionally deferred with reason
- schema or data work uses [`docs/ai/database-rules.md`](./docs/ai/database-rules.md) and [`checklists/database-change.md`](./checklists/database-change.md)
- first-repository work uses [`checklists/first-delivery.md`](./checklists/first-delivery.md) before the first shared delivery
- specialist-agent flows use [`checklists/agent-role-selection.md`](./checklists/agent-role-selection.md) and [`checklists/agent-handoff.md`](./checklists/agent-handoff.md)
- existing-repository onboarding starts with `scripts/analyze_repository.py`, `docs/ai/project-adoption.md`, and [`checklists/project-adoption.md`](./checklists/project-adoption.md)
