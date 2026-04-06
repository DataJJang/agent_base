# Project Generator Run Example

```text
Prepare the final generator execution package for a new repository.

Follow these sources of truth:
1. AGENTS.md
2. docs/ai/project-generation-spec.md
3. docs/ai/project-selection-mapping.md
4. docs/ai/project-generator.md
5. docs/ai/token-substitution.md

Repository: sample-backend-service
Branch: dev
Output root: /tmp/generated-projects
Scope: finalize the confirmed backend-service spec and produce a runnable generator command
Target environments: local, dev, stg
Out of scope:
- business feature implementation

Return:
- final generator JSON
- selected template and scaffold profile
- exact python command
- unsupported or follow-up items
```
