# Receiver Master Prompt

적용 기준 문서:

- [`AGENTS.md`](../../../AGENTS.md)
- [`docs/ai/core-rules.md`](../core-rules.md)
- [`docs/ai/database-rules.md`](../database-rules.md)
- [`docs/ai/services/receiver.md`](../services/receiver.md)
- [`docs/ai/lifecycle.md`](../lifecycle.md)
- [`docs/ai/governance/quality-gates.md`](../governance/quality-gates.md)

## Prompt Template

```text
You are preparing a receiver-service deliverable for the target repository.

Follow these sources of truth in order:
1. AGENTS.md
2. docs/ai/core-rules.md
3. docs/ai/database-rules.md when persistence, migration, seed, or query work is involved
4. docs/ai/services/receiver.md
5. docs/ai/lifecycle.md
6. docs/ai/governance/quality-gates.md
7. The repository-specific files listed below

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

Create a {{OUTPUT_TYPE}} for this receiver work.

Requirements:
- Respect the current ingress -> parser/decoder -> handler/service -> publish/store pipeline.
- Identify protocol assumptions, payload validation rules, idempotency requirements, and failure handling.
- Include MQTT, TCP, persistence, and downstream publishing impact when relevant.
- If the work touches persistence, include DB naming, migration, verification query, and rollback expectations.
- Separate parse failures, business validation failures, and infrastructure failures.
- Include minimum verification steps:
  - compile
  - automated tests if present
  - payload parsing or routing smoke validation
  - logging and failure-path review
- Explicitly list operational checks after deploy, including ingress, logs, DB writes, and publish behavior.

Output format:
- Purpose
- Scope
- Receiver flow impact
- Detailed work items
- Validation plan
- Operational checks
- Risks and open questions
```

## Best Use Cases

- 수신 파이프라인 영향도 분석
- 프로토콜 변경 대응 문서
- 장애 대응서 초안
- 수신 서비스 배포 체크리스트 작성
