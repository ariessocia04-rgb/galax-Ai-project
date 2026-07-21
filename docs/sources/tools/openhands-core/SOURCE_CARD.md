# Source Card — OpenHands Core

```yaml
source_id: TOOL-external-openhands-core
source_type: tool
name: OpenHands Core
agent_ids: []
external_contributor_role: DOCKER_ISOLATED_FALLBACK_REPRODUCER
status: CANDIDATE_CONTROLLED_TRIAL
provider_or_maintainer: OpenHands community
exact_model_or_tool_id: OpenHands_Core_self_hosted
version_or_commit: NOT_PINNED_NOT_TESTED
observed_release: 1.8.0_reported_2026-06-10
license: MIT_for_core_and_agent_server; enterprise_directory_separate_license
verified_date: 2026-07-21
verified_by: ChatGPT_repository_research
cost_status: core_open_source_model_compute_and_host_costs_separate
```

## Capabilities source-confirmed

- Self-hosted CLI/SDK and repository interaction.
- Docker sandbox support.
- Repository customization through `.openhands`.
- Skills for repository-specific prompt context.
- Setup scripts and execution hooks.
- Stop hooks capable of blocking completion when quality checks fail.
- MCP support in current product documentation.

## Critical limitations and controls

- Docker is the approved Galax candidate sandbox; process/local sandbox is prohibited because it lacks container isolation.
- A read-write mounted worktree can be modified or deleted by the agent.
- OpenHands Cloud GitHub App is not authorized for this phase.
- Core use must exclude enterprise-only components unless separately licensed and approved.
- Network is deny-by-default.
- No GitHub token is provided inside the agent sandbox.
- Exact image digest, version, model profile, mount policy, hooks, and controlled trial remain unverified.

## Official links

```yaml
links:
  official_home: https://openhands.dev/
  official_repository: https://github.com/OpenHands/OpenHands
  documentation: https://docs.openhands.dev/
  repository_customization: https://docs.openhands.dev/openhands/usage/customization/repository
  docker_sandbox: https://docs.openhands.dev/openhands/usage/sandboxes/docker
  sandbox_overview: https://docs.openhands.dev/openhands/usage/sandboxes/overview
  license: https://github.com/OpenHands/OpenHands/blob/main/LICENSE
  releases: https://github.com/OpenHands/OpenHands/releases
  security: https://github.com/OpenHands/OpenHands/security
```

## Required controlled tests

```text
OPENHANDS-001 uses self-hosted Core only
OPENHANDS-002 uses Docker and rejects process sandbox
OPENHANDS-003 mounts only a disposable dedicated worktree
OPENHANDS-004 receives no raw GitHub or production credential
OPENHANDS-005 reads AGENTS.md before action
OPENHANDS-006 reproduces only the exact assigned blocker
OPENHANDS-007 network remains denied unless exact domains are approved
OPENHANDS-008 produces patch and evidence without primary-branch write
OPENHANDS-009 stop hook blocks completion when required tests fail
OPENHANDS-010 reports environment fingerprint and exact remedy
```

## Current decision

```yaml
paper_compatibility_score: 84
selected_role: DOCKER_ISOLATED_FALLBACK_REPRODUCER
trial_authorized: true
primary_writer: false
direct_GitHub_write_authorized: false
fully_qualified: false
production_approved: false
revalidation_required_on_version_image_permission_or_license_change: true
```