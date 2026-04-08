# Version And Provenance

## 목적

이 문서는 `harness-foundry` 자체 버전과, generated repository가 어떤 baseline에서 나왔는지 추적하는 기준을 정의한다.

## Maintainer Baseline

- 루트 `VERSION`
  - 현재 foundry baseline을 나타내는 working semver
- 루트 `CHANGELOG.md`
  - `Unreleased`, `Added`, `Changed`, `Fixed`, `Migration Notes` 중심으로 유지
- 추천 tag 형식
  - `vX.Y.Z`

공개 릴리스가 아직 많지 않더라도, generated repository provenance는 `VERSION`을 기준으로 먼저 남긴다.

## Generated Repository Provenance

generator는 `.agent-base/generation-manifest.json`에 아래를 남긴다.

- `foundryVersion`
  - generator 실행 시점의 root `VERSION`
- `templateVersion`
  - 현재는 foundry baseline과 같은 값을 사용한다
- `foundryCommit`
  - git metadata를 읽을 수 있으면 full commit hash
- `foundryCommitShort`
  - 짧은 commit hash
- `foundryTag`
  - 현재 commit이 tag와 정확히 일치하면 그 tag
- `latestKnownTag`
  - 가장 최근에 찾은 tag
- `foundryDirty`
  - 생성 시점에 foundry worktree에 미커밋 변경이 있었는지 여부
- `generatedAtUtc`
  - 생성 시간

generated repo에서는 `.agent-base/generation-manifest.json`을 provenance source of truth로 본다.

## 운영 원칙

- baseline 업그레이드는 `VERSION`과 `CHANGELOG.md`를 같이 갱신한다.
- breaking change가 있으면 `Migration Notes`를 비워 두지 않는다.
- generated repo issue를 볼 때는 먼저 `foundryVersion`, `foundryCommit`, `foundryDirty`를 같이 확인한다.
- 로컬 실험 상태에서 생성한 repo라면 `foundryDirty = true`일 수 있으므로, 재현성 판단 시 이를 감안한다.

## AI / Tool Usage

- AI가 generated repo를 점검할 때는 `AGENTS.md`, `.agent-base/context-manifest.json`과 함께 `.agent-base/generation-manifest.json`도 먼저 읽는 편이 좋다.
- `scripts/show_start_path.py`는 starter path와 함께 foundry provenance도 표시한다.
