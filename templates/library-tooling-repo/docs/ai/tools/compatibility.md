# Tool Compatibility Strategy

## 1. Canonical Strategy

이 규약 패키지의 canonical entry file은 `AGENTS.md`다.

상세 규약은 `docs/ai/`가 system of record다.

## 2. Tool Mapping

| Tool | Preferred file | Recommended strategy |
| --- | --- | --- |
| Codex / OpenAI agent tools | `AGENTS.md` | Canonical |
| Claude Code | `CLAUDE.md` | `AGENTS.md` import + short Claude note |
| Gemini CLI | `GEMINI.md` | `AGENTS.md`를 참조하는 adapter |
| GitHub Copilot | `.github/copilot-instructions.md` | Condensed instructions + `AGENTS.md` pointer |
| Cursor | `.cursor/rules/*` | Scoped rules derived from canonical docs |
| Windsurf | workspace rules | Canonical docs를 바탕으로 변환 |

## 3. Why This Structure

- `AGENTS.md`는 벤더 중립적이다.
- Claude는 `CLAUDE.md`를 공식 memory 파일로 읽는다.
- Gemini는 `GEMINI.md`를 기본 context 파일로 사용한다.
- Copilot은 `.github/copilot-instructions.md`를 공식 지원한다.
- Cursor는 `.cursor/rules`를 공식 규칙 체계로 쓴다.

따라서 canonical은 하나로 두고, 각 도구는 어댑터 파일로 맞추는 것이 가장 안정적이다.

## 4. Maintenance Rule

- 공통 규칙은 `AGENTS.md`와 `docs/ai/`만 갱신한다.
- 도구별 파일은 가능한 한 짧고 파생형으로 유지한다.
- 도구별 파일이 canonical보다 길어지기 시작하면 구조가 잘못된 것으로 본다.
