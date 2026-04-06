# Project Copilot Instructions

Use [`AGENTS.md`](../AGENTS.md) as the canonical repo-wide AI entrypoint.

## Repository-Wide Rules

- Follow the nearest existing code pattern before adding new structure.
- For new repositories or major reshapes, resolve `projectFamily`, `projectNature`, and `runtimeRole[]` first.
- Keep changes scoped to the requested task.
- Do not commit secrets, tokens, production URLs, or real chat IDs.
- Preserve compatibility when touching API contracts or DB schema.
- Update docs when code, config, DB, validation, or rollout behavior changes.

## Where To Look

- Detailed rules: [`docs/ai/README.md`](../docs/ai/README.md)
- Bootstrap flow: [`docs/ai/project-bootstrap.md`](../docs/ai/project-bootstrap.md)
- Selection model: [`docs/ai/project-generation-spec.md`](../docs/ai/project-generation-spec.md), [`docs/ai/project-family-map.md`](../docs/ai/project-family-map.md), [`docs/ai/project-selection-mapping.md`](../docs/ai/project-selection-mapping.md)
- Quality gates: [`docs/ai/governance/quality-gates.md`](../docs/ai/governance/quality-gates.md)
- Prompt templates: [`docs/ai/prompts/README.md`](../docs/ai/prompts/README.md)
- Path-specific instructions: `./instructions/*.instructions.md`
