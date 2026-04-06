# Project Agent Entry

This file is the canonical AI guidance entrypoint for a project repository template.

## Use This File As The Entry Map

- Canonical guidance starts here.
- Detailed rules live under [`docs/ai/README.md`](./docs/ai/README.md).
- Interactive repository bootstrap starts at [`docs/ai/project-bootstrap.md`](./docs/ai/project-bootstrap.md).
- The recommended executable wrapper for bootstrap is [`docs/ai/project-bootstrap-cli.md`](./docs/ai/project-bootstrap-cli.md) and `source/scripts/project_bootstrap_cli.py`.
- The normalized creation schema lives in [`docs/ai/project-generation-spec.md`](./docs/ai/project-generation-spec.md).
- Project families and runtime roles are defined in [`docs/ai/project-family-map.md`](./docs/ai/project-family-map.md).
- Project selection to template and output mapping lives in [`docs/ai/project-selection-mapping.md`](./docs/ai/project-selection-mapping.md).
- Generator usage and scaffold support live in [`docs/ai/project-generator.md`](./docs/ai/project-generator.md).
- Token substitution rules live in [`docs/ai/token-substitution.md`](./docs/ai/token-substitution.md).
- Recommended stack and version defaults live in [`docs/ai/stack-matrix.md`](./docs/ai/stack-matrix.md).
- Database naming, schema, and risky SQL rules live under [`docs/ai/database-rules.md`](./docs/ai/database-rules.md).
- Local commit gate and hook rules live under [`docs/ai/governance/pre-commit-hooks.md`](./docs/ai/governance/pre-commit-hooks.md).
- Agent failure capture and harness reinforcement rules live under [`docs/ai/governance/agent-failure-learning.md`](./docs/ai/governance/agent-failure-learning.md).
- Failure recording helper script lives at `scripts/record_agent_failure.py`.
- Prompt templates live under [`docs/ai/prompts/README.md`](./docs/ai/prompts/README.md).
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

## Read Order

1. This `AGENTS.md`
2. [`docs/ai/project-bootstrap.md`](./docs/ai/project-bootstrap.md) when starting or adopting a repository
3. [`docs/ai/project-bootstrap-cli.md`](./docs/ai/project-bootstrap-cli.md)
4. [`docs/ai/project-generation-spec.md`](./docs/ai/project-generation-spec.md)
5. [`docs/ai/project-family-map.md`](./docs/ai/project-family-map.md)
6. [`docs/ai/project-selection-mapping.md`](./docs/ai/project-selection-mapping.md)
7. [`docs/ai/project-generator.md`](./docs/ai/project-generator.md)
8. [`docs/ai/token-substitution.md`](./docs/ai/token-substitution.md)
9. [`docs/ai/stack-matrix.md`](./docs/ai/stack-matrix.md)
10. [`docs/ai/core-rules.md`](./docs/ai/core-rules.md)
11. [`docs/ai/database-rules.md`](./docs/ai/database-rules.md) when the repo owns schema, migration, SQL, or heavy query work
12. [`docs/ai/lifecycle.md`](./docs/ai/lifecycle.md)
13. [`docs/ai/architecture-map.md`](./docs/ai/architecture-map.md)
14. [`docs/ai/command-catalog.md`](./docs/ai/command-catalog.md)
15. The relevant runtime-role guide under `docs/ai/services/`
16. [`docs/ai/governance/quality-gates.md`](./docs/ai/governance/quality-gates.md)
17. [`docs/ai/governance/git-workflow.md`](./docs/ai/governance/git-workflow.md) when branch, commit, PR, or merge behavior matters
18. [`docs/ai/governance/pre-commit-hooks.md`](./docs/ai/governance/pre-commit-hooks.md) before enabling local commit gates
19. [`docs/ai/governance/agent-failure-learning.md`](./docs/ai/governance/agent-failure-learning.md) when repeated mistakes expose harness gaps
20. [`docs/ai/document-routing.md`](./docs/ai/document-routing.md) when documentation changes are involved
21. [`checklists/project-interview.md`](./checklists/project-interview.md) when the repository is still in discovery or bootstrap
22. [`checklists/database-change.md`](./checklists/database-change.md) when schema, migration, seed, or data-correction work is involved
23. [`checklists/agent-failure-review.md`](./checklists/agent-failure-review.md) when a failure case should be reinforced into the harness

## Non-Negotiables

- Follow the nearest existing code pattern before inventing structure.
- Do not commit secrets, tokens, real identifiers, or production credentials.
- Prefer compatible changes over breaking changes.
- Update code, config, DB, docs, and validation together when the change spans them.
- Do not run destructive DB commands without explicit approval, rollback or backup notes, and verification queries.
- Do not push without at least one relevant verification step.
- Install and review local pre-commit hooks before the first shared delivery.
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
10. [`checklists/project-interview.md`](./checklists/project-interview.md)
11. [`checklists/project-creation.md`](./checklists/project-creation.md)
12. [`docs/ai/governance/pre-commit-hooks.md`](./docs/ai/governance/pre-commit-hooks.md)
13. [`docs/ai/prompts/examples/README.md`](./docs/ai/prompts/examples/README.md)

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

## Quality Gate Reminder

Before completion, confirm:

- project family and runtime roles are explicitly fixed
- build, compile, or test was run
- unverified items are explicitly listed
- rollout or operational risk is called out when relevant
- related docs are updated or intentionally deferred with reason
- schema or data work uses [`docs/ai/database-rules.md`](./docs/ai/database-rules.md) and [`checklists/database-change.md`](./checklists/database-change.md)
- first-repository work uses [`checklists/first-delivery.md`](./checklists/first-delivery.md) before the first shared delivery
