# External AI Development Contributor Role Package

**Branch:** `research/ai-qualification-framework`  
**Status:** `DESIGNATED_ROLES_RESEARCH_ONLY_NOT_ACTIVATED`  
**Applies to:** Cline, OpenHands Core, Aider, mini-SWE-agent, and PR-Agent.

## Purpose

This package converts the qualification decisions into exact, professional, repository-first role charters, task inputs, and work assignments. It does not install, activate, authenticate, grant repository write access, merge, deploy, or enable Galax Agents 02–15.

## Canonical reading order

1. `../../../README.md`
2. `../../rules/AI_DEVELOPMENT_CONTRIBUTOR_QUALIFICATION_GATE.md`
3. `../../research/ai-tools/AI_DEVELOPMENT_CONTRIBUTOR_FINAL_QUALIFICATION_REVIEW_V3_2026-07-21.md`
4. `../../research/ai-tools/AI_CONTRIBUTOR_COMMAND_DESIGN_SURVEY_2026-07-21.md`
5. `../../plan/AI_DEVELOPMENT_CONTRIBUTOR_COORDINATION_PLAN_DRAFT.md`
6. `../../plan/EXTERNAL_AI_CONTRIBUTOR_WORK_ASSIGNMENT_PLAN.md`
7. `SHARED_EXECUTION_PROTOCOL.md`
8. `CONTROLLED_TASK_PACKET_TEMPLATE.md`
9. The exact role charter for the selected contributor.

## Designated roles

```yaml
Cline:
  contributor_id: CLINE-01
  role: SUPERVISED_PRIMARY_IMPLEMENTER
  may_write_source: only_after_controlled_trial_and_on_authorized_task_branch
  charter: CLINE_ROLE_CHARTER.md

OpenHands_Core:
  contributor_id: OPENHANDS-01
  role: DOCKER_ISOLATED_FALLBACK_IMPLEMENTER
  may_write_source: only_after_primary_writer_stops
  charter: OPENHANDS_CORE_ROLE_CHARTER.md

Aider:
  contributor_id: AIDER-01
  role: SURGICAL_FIX_AND_TEST_REPAIR_SPECIALIST
  may_write_source: only_for_one_reproducible_failure
  charter: AIDER_ROLE_CHARTER.md

mini_SWE_agent:
  contributor_id: MSWE-01
  role: ISOLATED_PATCH_COMPARISON_WORKER
  may_write_source: isolated_copy_only
  direct_repository_write: prohibited
  charter: MINI_SWE_AGENT_ROLE_CHARTER.md

PR_Agent:
  contributor_id: PRAGENT-01
  role: READ_ONLY_PR_REVIEWER
  source_write: prohibited
  merge: prohibited
  charter: PR_AGENT_ROLE_CHARTER.md
```

## Canonical files

- `SHARED_EXECUTION_PROTOCOL.md` — shared operating, safety, test, stop, handoff, and MCP rules.
- `CONTROLLED_TASK_PACKET_TEMPLATE.md` — mandatory completed input for one contributor and one goal.
- `CLINE_ROLE_CHARTER.md` — professional background, exact role, start command, restrictions, success, and remedy.
- `OPENHANDS_CORE_ROLE_CHARTER.md` — Docker fallback/reproduction role and isolation controls.
- `AIDER_ROLE_CHARTER.md` — exact surgical repair role and minimal-context workflow.
- `MINI_SWE_AGENT_ROLE_CHARTER.md` — isolated patch-comparison and trajectory role.
- `PR_AGENT_ROLE_CHARTER.md` — read-only stable PR review role.
- `../../plan/EXTERNAL_AI_CONTRIBUTOR_WORK_ASSIGNMENT_PLAN.md` — exact Agent 01 work packages and ownership transitions.

## Activation sequence

```text
paper qualification
→ complete controlled task packet
→ controlled role trial
→ security-negative tests
→ quota/cost observation
→ human decision record
→ conditional approval for one exact role
```

No tool may skip directly from a role charter to repository write access.

## Current authorization

```yaml
role_designation_documented: true
professional_commands_documented: true
work_packages_documented: true
installation_authorized: false
credentials_authorized: false
live_trial_authorized: false
repository_write_authorized: false
MCP_mesh_authorized: false
merge_authorized: false
deployment_authorized: false
Agents_02_to_15_enabled: false
```
