# Getting Started Prompt

```text
Run an interactive project bootstrap interview for a new repository.

Follow these sources of truth in order:
1. AGENTS.md
2. docs/ai/project-bootstrap.md
3. docs/ai/project-generation-spec.md
4. docs/ai/project-family-map.md
5. docs/ai/project-selection-mapping.md
6. docs/ai/project-generator.md
7. docs/ai/stack-matrix.md
8. docs/ai/governance/quality-gates.md

Repository: sample-new-project
Branch: dev
Goal: bootstrap a new repository and generate the first scaffold-ready specification
Scope: repository initialization, family decision, stack decision, generator execution package, command catalog, and first validation
Target environments: local, dev
Out of scope:
- concrete business implementation

Tasks:
- ask the user for all required bootstrap choices in the fixed order
- recommend defaults based on the selected project family
- produce a normalized project generation spec
- identify the base template, overlays, first commands, and first prompt sequence
- prepare the exact generator command if the stack is supported

Output format:
- Purpose
- Interview summary
- Normalized project generation spec
- Selected template and scaffold profile
- First commands to run
- First prompt sequence
- Validation plan
- Risks and follow-ups
```
