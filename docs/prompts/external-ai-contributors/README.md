# External AI Development Contributor Role Package

**Branch:** `research/ai-qualification-framework`  
**Status:** `DESIGNATED_ROLES_RESEARCH_ONLY_NOT_ACTIVATED`  
**Applies to:** Cline, OpenHands Core, Aider, mini-SWE-agent, and PR-Agent.

## Purpose

This package converts the qualification decisions into exact, professional, repository-first role charters and task commands. It does not install, activate, authenticate, grant repository write access, merge, deploy, or enable Galax Agents 02–15.

## Required reading order

1. `../../../README.md`
2. `../../rules/AI_DEVELOPMENT_CONTRIBUTOR_QUALIFICATION_GATE.md`
3. `../../research/ai-tools/AI_DEVELOPMENT_CONTRIBUTOR_FINAL_QUALIFICATION_REVIEW_V3_2026-07-21.md`
4. `../../plan/AI_DEVELOPMENT_CONTRIBUTOR_COORDINATION_PLAN_DRAFT.md`
5. `SHARED_EXECUTION_PROTOCOL.md`
6. The exact role charter for the selected contributor.

## Designated roles

```yaml
Cline:
  role: SUPERVISED_PRIMARY_IMPLEMENTER
  may_write_source: only_on_authorized_task_branch

OpenHands_Core:
  role: DOCKER_ISOLATED_FALLBACK_IMPLEMENTER
  may_write_source: only_after_primary_writer_stops

Aider:
  role: SURGICAL_FIX_AND_TEST_REPAIR_SPECIALIST
  may_write_source: only_for_one_reproducible_failure

mini_SWE_agent:
  role: ISOLATED_PATCH_COMPARISON_WORKER
  may_write_source: isolated_copy_only
  direct_repository_write: prohibited

PR_Agent:
  role: READ_ONLY_PR_REVIEWER
  source_write: prohibited
  merge: prohibited
```

## Files

- `SHARED_EXECUTION_PROTOCOL.md`
- `CLINE_ROLE_CHARTER.md`
- `OPENHANDS_CORE_ROLE_CHARTER.md`
- `AIDER_ROLE_CHARTER.md`
- `MINI_SWE_AGENT_ROLE_CHARTER.md`
- `PR_AGENT_ROLE_CHARTER.md`

## Current authorization

```yaml
role_designation_documented: true
installation_authorized: false
credentials_authorized: false
live_trial_authorized: false
repository_write_authorized: false
MCP_mesh_authorized: false
merge_authorized: false
deployment_authorized: false
Agents_02_to_15_enabled: false
```
