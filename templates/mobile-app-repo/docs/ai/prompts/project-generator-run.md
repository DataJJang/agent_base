# Project Generator Run Prompt

이 프롬프트는 확정된 generation spec을 실제 생성기 실행 입력으로 정리하게 한다.

```text
You are preparing the final project generator execution package.

Follow these sources of truth:
1. AGENTS.md
2. docs/ai/project-generation-spec.md
3. docs/ai/project-selection-mapping.md
4. docs/ai/project-generator.md
5. docs/ai/token-substitution.md

Input:
- the confirmed project interview result
- the normalized generation spec
- the intended output root directory

Tasks:
- validate that the spec is generator-ready
- produce the final JSON payload for the generator
- identify which template and scaffold profile should be selected
- list any unsupported stack caveats
- provide the exact generator command to run

Output format:
- summary
- final generator JSON
- selected template
- selected scaffold profile
- exact command
- risks or follow-up items
```
