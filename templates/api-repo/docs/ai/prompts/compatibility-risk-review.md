# Compatibility Risk Review Prompt

먼저 아래 문서를 읽는다.

1. `AGENTS.md`
2. `docs/ai/context-profiles.md`
3. `docs/ai/start-adoption.md`
4. `docs/ai/compatibility-matrix.md`
5. `docs/ai/legacy-exception-policy.md`

현재 스택과 목표 스택을 비교해 compatibility matrix를 작성하고, breaking point와 legacy exception 후보를 분류하라.

반드시 포함:

- compatible / compatible-with-note / breaking / unknown
- 고위험 구간
- core role로 해결 가능한 항목 vs extended role 검토가 필요한 항목
- 추가 확인 필요 항목
