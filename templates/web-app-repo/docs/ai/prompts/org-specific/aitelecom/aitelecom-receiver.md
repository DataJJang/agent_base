# aitelecom-receiver Prompt Pack

기준 문서:

- [`AGENTS.md`](../../../../../AGENTS.md)
- [`docs/ai/services/receiver.md`](../../../services/receiver.md)
- [`docs/ai/lifecycle.md`](../../../lifecycle.md)

## 대표 저장소 및 경로

- `aitelecom-receiver`
- `aitelecom-receiver-rt`
- `aitelecom-receiver-sp4`
- `src/main/resources/application.yml`
- `src/main/java/kr/co/openit/aitelecom/receiver/config`
- `src/main/java/kr/co/openit/aitelecom/receiver/mqtt`
- `src/main/java/kr/co/openit/aitelecom/receiver/tcp`
- `src/main/java/kr/co/openit/aitelecom/receiver/packet`
- `src/main/java/kr/co/openit/aitelecom/receiver/domain`

## Repo-Specific Prompt Template

```text
Create a repository-specific deliverable for an AITelecom receiver repository.

Repository: {{REPOSITORY}}
Branch: {{BRANCH}}
Goal: {{GOAL}}
Scope: {{SCOPE}}
Target environments: {{ENVIRONMENTS}}
Relevant receiver paths:
- src/main/resources/application.yml
- src/main/java/kr/co/openit/aitelecom/receiver/config
- src/main/java/kr/co/openit/aitelecom/receiver/mqtt
- src/main/java/kr/co/openit/aitelecom/receiver/tcp
- src/main/java/kr/co/openit/aitelecom/receiver/packet
- src/main/java/kr/co/openit/aitelecom/receiver/domain
Relevant docs:
- {{DOC_PATH_1}}
Out of scope:
- {{OUT_OF_SCOPE}}

Requirements:
- Follow AGENTS.md, docs/ai/services/receiver.md, and docs/ai/lifecycle.md.
- Respect the current receiver pipeline and distinguish ingress, parse, validate, persist, and publish steps.
- Call out protocol assumptions, error categories, idempotency rules, and operational log points.
- Include compile, payload-routing smoke validation, and post-deploy ingress checks.
- If the repository variant is `receiver`, `receiver-rt`, or `receiver-sp4`, note any repository-specific path differences without restating common rules.

Output format:
- Purpose
- Scope
- Receiver flow impact
- Detailed tasks
- Validation plan
- Operational checks
- Risks and open questions
```
