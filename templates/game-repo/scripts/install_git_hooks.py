#!/usr/bin/env python3
from __future__ import annotations

import os
import stat
import subprocess
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
HOOK_PATH = REPO_ROOT / ".githooks" / "pre-commit"


def main() -> int:
    if not HOOK_PATH.exists():
        raise SystemExit(f"Missing hook file: {HOOK_PATH}")

    current_mode = HOOK_PATH.stat().st_mode
    HOOK_PATH.chmod(current_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)

    subprocess.run(
        ["git", "config", "core.hooksPath", ".githooks"],
        cwd=REPO_ROOT,
        check=True,
    )

    print("Installed git hooks:")
    print("- core.hooksPath = .githooks")
    print(f"- executable hook = {HOOK_PATH}")
    print("Next:")
    print("- review .agent-base/pre-commit-config.json")
    print("- run python3 scripts/precommit_check.py --dry-run")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
