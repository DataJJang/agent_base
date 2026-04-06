# Windsurf Guidance

Windsurf는 `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`처럼 단일 canonical 파일 전략보다 workspace rules나 editor-integrated rules를 쓰는 경우가 많다.

이 템플릿에서는 Windsurf 전용 canonical 파일을 만들지 않는다.
대신 아래 순서로 변환해 사용한다.

## 변환 순서

1. `AGENTS.md`를 읽고 핵심 엔트리 규칙을 가져온다.
2. `docs/ai/README.md`에서 필요한 상세 규칙 문서를 찾는다.
3. 현재 작업과 관련된 서비스 문서와 품질 게이트만 발췌한다.
4. Windsurf workspace rules에는 짧은 규칙만 넣고, 긴 규칙은 docs 링크로 유지한다.

## 포함해야 할 최소 내용

- 기존 패턴 우선
- 민감정보 커밋 금지
- 검증 없이 완료 금지
- 관련 서비스 문서 위치
- 관련 품질 게이트 문서 위치

## 포함하지 말아야 할 내용

- 전체 정책 문서 복붙
- 길고 중복된 운영 절차
- 코드베이스와 무관한 일반론
