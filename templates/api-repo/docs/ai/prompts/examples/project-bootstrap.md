# Project Bootstrap Example Prompt

아래 예시는 새 저장소를 시작할 때 바로 복사해 사용할 수 있는 범용 bootstrap 프롬프트다.

```text
Run an interactive project bootstrap interview for a new repository.

Follow these sources of truth in order:
1. AGENTS.md
2. docs/ai/project-bootstrap.md
3. docs/ai/project-generation-spec.md
4. docs/ai/project-family-map.md
5. docs/ai/project-selection-mapping.md
6. docs/ai/stack-matrix.md
7. docs/ai/governance/quality-gates.md

Repository: my-new-project
Branch: dev
Goal: create the initial bootstrap guide and first-document set for a new repository
Scope: repository initialization, family decision, stack decision, command catalog, first validation, and required operating documents
Target environments: local, dev
Relevant code paths:
- repo root only
Relevant config and docs:
- docs/ai/command-catalog.md
- docs/ai/governance/release-and-rollback.md
Out of scope:
- concrete business logic implementation
- production deployment execution

Tasks:
- ask the user for all required choices in the order defined by docs/ai/project-bootstrap.md
- recommend defaults based on the selected project family
- produce a normalized project generation spec
- identify the base template and first prompt sequence

Requirements:
- do not skip projectFamily, projectNature, runtimeRole, language, framework, datastore, cache, deploymentType, startupMode, loggingMode, targetOs, or securityProfile
- define the first build, compile, test, smoke, and deploy-check commands
- state which repo-local overlay docs are mandatory if the stack differs from the default
- Include the first document set to create:
  - build guide
  - test plan
  - deployment checklist
  - operations manual or runbook if needed
- include validation and unverified items

Output format:
- Purpose
- Interview summary
- Normalized project generation spec
- Required repository files and docs
- Selected template and overlays
- First commands to run
- First prompt sequence
- Validation plan
- Risks and follow-ups
```
