#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import subprocess
from datetime import datetime
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT_DIR = REPO_ROOT / ".agent-base" / "failure-cases"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Record an agent failure case for harness reinforcement.")
    parser.add_argument("--summary", help="Short summary of the failure case")
    parser.add_argument("--repository", help="Repository name")
    parser.add_argument("--branch", help="Branch name")
    parser.add_argument("--request", help="Original user request")
    parser.add_argument("--expected", help="Expected result")
    parser.add_argument("--actual", help="Actual result")
    parser.add_argument("--mode", choices=["bootstrap", "adoption", "delivery", "incident"], help="Workflow mode")
    parser.add_argument("--workflow-stage", help="Stage such as interview, spec, mapping, generation, handoff, validation, rollout")
    parser.add_argument("--agent-role", help="Primary agent role at failure time")
    parser.add_argument("--upstream-role", help="Upstream role that handed work into the failed step")
    parser.add_argument("--downstream-role", help="Downstream role affected by the failed step")
    parser.add_argument("--failure-type", action="append", default=[], help="Failure type classification")
    parser.add_argument("--root-cause", help="Root cause summary")
    parser.add_argument(
        "--root-cause-layer",
        action="append",
        default=[],
        help="Harness layer such as docs, prompts, templates, scripts, checklists, tools, role-assignment",
    )
    parser.add_argument("--affected-area", action="append", default=[], help="Harness area to reinforce")
    parser.add_argument("--validation", help="Validation plan or verification result")
    parser.add_argument("--follow-up", action="append", default=[], help="Follow-up items")
    parser.add_argument("--output-dir", default=str(DEFAULT_OUTPUT_DIR), help="Directory where reports will be stored")
    parser.add_argument("--format", choices=["json", "md", "both"], default="both", help="Output format")
    parser.add_argument("--interactive", action="store_true", help="Prompt for missing values interactively")
    return parser.parse_args()


def git_current_branch() -> str:
    result = subprocess.run(
        ["git", "rev-parse", "--abbrev-ref", "HEAD"],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        return ""
    return result.stdout.strip()


def ask(label: str, current: str = "", allow_blank: bool = False) -> str:
    if current:
        return current
    while True:
        value = input(f"{label}: ").strip()
        if value or allow_blank:
            return value


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return slug or "agent-failure"


def render_markdown(payload: dict) -> str:
    lines = [
        f"# Agent Failure Report: {payload['summary']}",
        "",
        f"- Timestamp: `{payload['timestamp']}`",
        f"- Repository: `{payload['repository']}`",
        f"- Branch: `{payload['branch']}`",
        f"- Mode: `{payload['mode'] or '-'}`",
        f"- Workflow stage: `{payload['workflowStage'] or '-'}`",
        f"- Agent role: `{payload['agentRole'] or '-'}`",
        f"- Upstream role: `{payload['upstreamRole'] or '-'}`",
        f"- Downstream role: `{payload['downstreamRole'] or '-'}`",
        "",
        "## Request",
        "",
        payload["request"] or "-",
        "",
        "## Expected",
        "",
        payload["expected"] or "-",
        "",
        "## Actual",
        "",
        payload["actual"] or "-",
        "",
        "## Failure Types",
        "",
    ]
    if payload["failureTypes"]:
        lines.extend([f"- {item}" for item in payload["failureTypes"]])
    else:
        lines.append("- -")
    lines.extend(
        [
            "",
            "## Root Cause",
            "",
            payload["rootCause"] or "-",
            "",
            "## Root Cause Layers",
            "",
        ]
    )
    if payload["rootCauseLayers"]:
        lines.extend([f"- {item}" for item in payload["rootCauseLayers"]])
    else:
        lines.append("- -")
    lines.extend(
        [
            "",
            "## Affected Harness Areas",
            "",
        ]
    )
    if payload["affectedAreas"]:
        lines.extend([f"- {item}" for item in payload["affectedAreas"]])
    else:
        lines.append("- -")
    lines.extend(
        [
            "",
            "## Validation",
            "",
            payload["validation"] or "-",
            "",
            "## Follow-up",
            "",
        ]
    )
    if payload["followUpItems"]:
        lines.extend([f"- {item}" for item in payload["followUpItems"]])
    else:
        lines.append("- -")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    args = parse_args()

    repository = args.repository or REPO_ROOT.name
    branch = args.branch or git_current_branch()

    interactive = args.interactive or not all([args.summary, args.request, args.expected, args.actual])

    summary = ask("Summary", args.summary or "") if interactive else (args.summary or "")
    request = ask("Original request", args.request or "") if interactive else (args.request or "")
    expected = ask("Expected result", args.expected or "") if interactive else (args.expected or "")
    actual = ask("Actual result", args.actual or "") if interactive else (args.actual or "")
    mode = ask("Mode", args.mode or "", allow_blank=True) if interactive else (args.mode or "")
    workflow_stage = (
        ask("Workflow stage", args.workflow_stage or "", allow_blank=True) if interactive else (args.workflow_stage or "")
    )
    agent_role = ask("Agent role", args.agent_role or "", allow_blank=True) if interactive else (args.agent_role or "")
    upstream_role = (
        ask("Upstream role", args.upstream_role or "", allow_blank=True) if interactive else (args.upstream_role or "")
    )
    downstream_role = (
        ask("Downstream role", args.downstream_role or "", allow_blank=True) if interactive else (args.downstream_role or "")
    )
    root_cause = ask("Root cause", args.root_cause or "", allow_blank=True) if interactive else (args.root_cause or "")
    validation = ask("Validation", args.validation or "", allow_blank=True) if interactive else (args.validation or "")

    timestamp = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
    file_stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    output_dir = Path(args.output_dir).resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    stem = f"{file_stamp}-{slugify(summary)}"

    payload = {
        "timestamp": timestamp,
        "repository": repository,
        "branch": branch,
        "summary": summary,
        "request": request,
        "expected": expected,
        "actual": actual,
        "mode": mode,
        "workflowStage": workflow_stage,
        "agentRole": agent_role,
        "upstreamRole": upstream_role,
        "downstreamRole": downstream_role,
        "failureTypes": args.failure_type,
        "rootCause": root_cause,
        "rootCauseLayers": args.root_cause_layer,
        "affectedAreas": args.affected_area,
        "validation": validation,
        "followUpItems": args.follow_up,
    }

    written: list[str] = []
    if args.format in {"json", "both"}:
        json_path = output_dir / f"{stem}.json"
        json_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        written.append(str(json_path))
    if args.format in {"md", "both"}:
        md_path = output_dir / f"{stem}.md"
        md_path.write_text(render_markdown(payload), encoding="utf-8")
        written.append(str(md_path))

    print(json.dumps({"written": written}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
