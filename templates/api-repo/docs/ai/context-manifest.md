# Context Manifest

이 문서는 생성기나 저장소 overlay가 남기는 `.agent-base/context-manifest.json`의 의미를 정의한다.

## 목적

- 새 저장소에서 어떤 문서를 먼저 읽어야 하는지 빠르게 알려준다.
- fast path와 deep path를 기계적으로 남겨 entry layer 과적재를 줄인다.
- core roles와 extended roles를 생성 시점 기준으로 고정해 handoff의 출발점으로 쓴다.

## 기본 항목

- `mode`
  - `bootstrap` 또는 이후 확장 가능한 다른 모드
- `projectFamily`
- `runtimeRoles`
- `fastPathDocs`
- `deepPathDocs`
- `coreRoles`
- `extendedRoles`
- `roleSpecializations`
- `contextBudget`

## 사용 원칙

- 저장소를 처음 열면 먼저 `fastPathDocs`만 읽는다.
- deep path 문서는 schema ownership, migration, rollout, repeated failure 같은 조건이 생길 때만 추가한다.
- `coreRoles`를 먼저 확정하고, `extendedRoles`는 필요 조건이 생겼을 때만 실제 실행 흐름에 넣는다.
- repo-local overlay가 생기면 context manifest도 함께 갱신한다.

## 생성 시점

- `generate_project.py`는 샘플 저장소 생성 시 `.agent-base/context-manifest.json`을 같이 만든다.
- 이후 저장소 담당자는 `command-catalog.md`, `architecture-map.md`, repo-local 예외를 보정한 뒤 필요하면 manifest를 수동 갱신한다.
