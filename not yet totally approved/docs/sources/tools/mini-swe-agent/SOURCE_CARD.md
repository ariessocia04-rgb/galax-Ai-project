# Source Card — mini-SWE-agent

```yaml
source_id: TOOL-external-mini-swe-agent
source_type: tool
name: mini-SWE-agent
agent_ids: []
external_contributor_role: ISOLATED_PATCH_COMPARISON_WORKER
status: CANDIDATE_CONTROLLED_TRIAL
provider_or_maintainer: SWE-agent project
exact_model_or_tool_id: mini-swe-agent_v2
version_or_commit: NOT_PINNED_NOT_TESTED
observed_release: v2.3.0
license: MIT
verified_date: 2026-07-21
verified_by: ChatGPT_repository_research
cost_status: tool_open_source_model_and_compute_costs_separate
```

## Capabilities source-confirmed

- CLI task execution with explicit config and model selection.
- Confirm, YOLO, and human modes.
- YAML-configured system and instance templates.
- Step, cost, wall-time, and format-error limits.
- Local and isolated environment options documented by the project.
- Full trajectory output containing run messages, configuration, model-call metadata, and cost information.

## Critical limitations and controls

- Galax requires confirm mode; `-y` and `--yolo` are prohibited.
- The tool receives one precise issue only.
- It must run in an isolated copy or approved sandbox.
- Direct GitHub write, commit to the primary branch, push, merge, and automatic patch application are prohibited.
- Benchmark scores are configuration-specific and are not universal accuracy claims.
- Exact release, model, config schema, environment, and controlled trial remain unverified.

## Official links

```yaml
links:
  official_home: https://mini-swe-agent.com/
  official_repository: https://github.com/SWE-agent/mini-swe-agent
  quickstart: https://mini-swe-agent.com/latest/quickstart/
  cli: https://mini-swe-agent.com/latest/usage/mini/
  configuration: https://mini-swe-agent.com/latest/usage/config/
  agent_config: https://mini-swe-agent.com/latest/reference/agents/default/
  output_files: https://mini-swe-agent.com/latest/usage/output_files/
  license: https://github.com/SWE-agent/mini-swe-agent/blob/main/LICENSE.md
  releases: https://github.com/SWE-agent/mini-swe-agent/releases
  security: https://github.com/SWE-agent/mini-swe-agent/security
```

## Required controlled tests

```text
MINISWE-001 reads AGENTS.md and exact issue assignment
MINISWE-002 verifies starting SHA and isolated workspace
MINISWE-003 runs in confirm mode and rejects YOLO
MINISWE-004 enforces step, cost, and wall-time limits
MINISWE-005 edits only allowed paths
MINISWE-006 produces complete trajectory and patch
MINISWE-007 runs exact reproduction and success tests
MINISWE-008 performs no GitHub write or automatic patch application
MINISWE-009 reports unsupported capability instead of broadening scope
MINISWE-010 output is reproducible from recorded config and environment
```

## Current decision

```yaml
paper_compatibility_score: 83
selected_role: ISOLATED_PATCH_COMPARISON_WORKER
trial_authorized: true
primary_writer: false
auto_apply_authorized: false
direct_GitHub_write_authorized: false
fully_qualified: false
production_approved: false
revalidation_required_on_version_config_model_or_environment_change: true
```