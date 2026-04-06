# Scaffold Planning Prompt

이 프롬프트는 확정된 generation spec을 기준으로 초기 저장소 구조와 첫 산출물 계획을 세우게 한다.

```text
You are planning the initial scaffold for a new repository.

Follow these sources of truth:
1. AGENTS.md
2. docs/ai/project-selection-mapping.md
3. docs/ai/stack-matrix.md
4. docs/ai/command-catalog.md
5. docs/ai/document-routing.md
6. docs/ai/governance/quality-gates.md
7. docs/ai/database-rules.md when DB exists

Input:
- the normalized project generation spec

Tasks:
- choose the correct base template
- list repo-local overlays that are required
- identify the first documents to generate
- define the first build, compile, test, smoke, and deploy-check commands
- identify what a future scaffold engine would need to generate first

Output format:
- selected template
- directory and document plan
- first commands
- first prompts to run
- initial verification plan
- risks and follow-up items
```
