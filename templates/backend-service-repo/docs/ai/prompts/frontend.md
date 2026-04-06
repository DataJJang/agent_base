# Frontend Master Prompt

적용 기준 문서:

- [`AGENTS.md`](../../../AGENTS.md)
- [`docs/ai/core-rules.md`](../core-rules.md)
- [`docs/ai/services/frontend.md`](../services/frontend.md)
- [`docs/ai/governance/quality-gates.md`](../governance/quality-gates.md)

## Prompt Template

```text
You are preparing a frontend-focused deliverable for the target repository.

Follow these sources of truth in order:
1. AGENTS.md
2. docs/ai/core-rules.md
3. docs/ai/services/frontend.md
4. docs/ai/governance/quality-gates.md
5. The repository-specific files listed below

Repository: {{REPOSITORY}}
Branch: {{BRANCH}}
Goal: {{GOAL}}
Scope: {{SCOPE}}
Target environments: {{ENVIRONMENTS}}
Relevant code paths:
- {{CODE_PATH_1}}
- {{CODE_PATH_2}}
Relevant config and docs:
- {{CONFIG_PATH_1}}
- {{DOC_PATH_1}}
Out of scope:
- {{OUT_OF_SCOPE}}

Create a {{OUTPUT_TYPE}} for this frontend work.

Requirements:
- Use the existing page structure and naming rules.
- Consider route, menu, API binding, type changes, i18n keys, shared component impact, and screen flow together.
- Call out required companion changes such as types, i18n, API normalization, and detail/list/register/modify pages.
- Separate confirmed facts from assumptions.
- Include validation steps at minimum:
  - build
  - type or compile validation if applicable
  - major screen smoke check
- Explicitly list any items that still require manual verification.

Output format:
- Purpose
- Scope
- Impacted files or areas
- Detailed tasks
- Validation plan
- Risks and follow-ups
```

## Best Use Cases

- 새로운 관리자 화면 설계안 작성
- 기존 화면 변경 영향도 분석
- 프론트 운영/사용자 매뉴얼 초안 생성
- 프론트 smoke test 체크리스트 생성
