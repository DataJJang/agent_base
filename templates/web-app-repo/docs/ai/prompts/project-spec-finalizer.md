# Project Spec Finalizer Prompt

이 프롬프트는 인터뷰 결과를 정규화된 생성 스펙으로 정리하게 한다.

```text
You are finalizing the normalized project generation spec for a new repository.

Follow these sources of truth:
1. AGENTS.md
2. docs/ai/project-generation-spec.md
3. docs/ai/project-family-map.md
4. docs/ai/project-selection-mapping.md
5. docs/ai/stack-matrix.md
6. docs/ai/database-rules.md when DB is involved

Input:
- the interview answers collected from the user

Tasks:
- normalize the answers to the schema in docs/ai/project-generation-spec.md
- fill missing defaults only when the selected family clearly implies them
- explicitly mark assumptions
- flag any required repo-local overlay conditions

Output format:
- summary
- normalized spec table
- selected defaults
- required overlays
- required initial documents
- first command placeholders
- open risks or undecided items
```
