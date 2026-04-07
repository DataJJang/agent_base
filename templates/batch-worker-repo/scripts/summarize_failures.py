#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Summarize failure cases recorded under .agent-base/failure-cases.")
    parser.add_argument("--root", default=".", help="Repository root")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = Path(args.root).resolve()
    failure_dir = root / ".agent-base" / "failure-cases"
    failure_types: Counter[str] = Counter()
    roles: Counter[str] = Counter()
    total = 0

    if failure_dir.exists():
        for path in sorted(failure_dir.glob("*.json")):
            total += 1
            try:
                payload = json.loads(path.read_text(encoding="utf-8"))
            except json.JSONDecodeError:
                failure_types["invalid-json"] += 1
                continue
            for item in payload.get("failureTypes", []):
                failure_types[item] += 1
            role = payload.get("agentRole")
            if role:
                roles[role] += 1

    summary = {
        "failureDirectory": str(failure_dir),
        "totalCases": total,
        "failureTypes": failure_types.most_common(),
        "agentRoles": roles.most_common(),
    }
    print(json.dumps(summary, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
