# Adoption Repository Inventory Prompt

기존 저장소 온보딩을 위한 inventory를 작성한다.

먼저 아래 문서를 읽는다.

1. `AGENTS.md`
2. `docs/ai/context-profiles.md`
3. `docs/ai/start-adoption.md`
4. `docs/ai/project-adoption.md`
5. `docs/ai/repository-inventory.md`
6. `docs/ai/project-selection-mapping.md`

현재 저장소의 언어, 프레임워크, build/test 명령, 환경설정 위치, DB/cache/외부 연동, 문서 갭, 운영 위험 구간을 inventory 형식으로 정리하라.

규칙:

- bootstrap 문맥과 혼합하지 않는다.
- 실제 저장소에 존재하는 파일, 설정, 명령만 근거로 쓴다.
- core roles와 extended roles를 구분해 추천한다.

출력:

- repository inventory
- command catalog draft
- docs gap
- recommended core roles
- recommended extended roles
