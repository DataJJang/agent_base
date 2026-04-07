#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Analyze an existing repository and emit a lightweight inventory.")
    parser.add_argument("--repo", default=".", help="Target repository root")
    parser.add_argument("--output", help="Output path for repository inventory JSON")
    return parser.parse_args()


def exists(root: Path, relative: str) -> bool:
    return (root / relative).exists()


def analyze(root: Path) -> dict:
    build_files = [
        path
        for path in [
            "package.json",
            "build.gradle",
            "build.gradle.kts",
            "pom.xml",
            "pubspec.yaml",
            "Packages/manifest.json",
        ]
        if exists(root, path)
    ]
    config_files = [
        path
        for path in [
            "src/main/resources/application.yml",
            "src/main/resources/application.yaml",
            ".env",
            ".env.local",
            "docker-compose.yml",
        ]
        if exists(root, path)
    ]
    doc_files = [
        path
        for path in [
            "README.md",
            "AGENTS.md",
            "docs/ai/README.md",
            "docs/runbook.md",
            "docs/deployment-checklist.md",
        ]
        if exists(root, path)
    ]

    languages = []
    if exists(root, "package.json"):
        languages.append("TypeScript/JavaScript")
    if exists(root, "build.gradle") or exists(root, "build.gradle.kts") or exists(root, "pom.xml"):
        languages.append("Java/Kotlin")
    if exists(root, "pubspec.yaml"):
        languages.append("Dart")
    if exists(root, "Packages/manifest.json"):
        languages.append("C#")

    frameworks = []
    if exists(root, "package.json"):
        frameworks.append("node-app")
    if exists(root, "build.gradle") or exists(root, "build.gradle.kts"):
        frameworks.append("gradle-app")
    if exists(root, "pubspec.yaml"):
        frameworks.append("flutter")
    if exists(root, "Packages/manifest.json"):
        frameworks.append("unity")

    return {
        "repositoryRoot": str(root.resolve()),
        "buildFiles": build_files,
        "configFiles": config_files,
        "docFiles": doc_files,
        "detectedLanguages": languages,
        "detectedFrameworkHints": frameworks,
        "needsManualReview": [
            "real build/test/smoke commands",
            "deployment order",
            "DB ownership and migration path",
            "secret injection and environment policy",
        ],
    }


def main() -> int:
    args = parse_args()
    root = Path(args.repo).resolve()
    inventory = analyze(root)
    output = Path(args.output).resolve() if args.output else root / ".agent-base" / "repository-inventory.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(inventory, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({"inventory": str(output)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
