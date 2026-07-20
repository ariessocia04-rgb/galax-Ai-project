# Galax External AI Development Contributors

**Status:** `DESIGNATED_NOT_INSTALLED_NOT_ACTIVATED`  
**Branch:** `research/ai-qualification-framework`

## Purpose

This directory is the human-readable roster for the controlled external AI development team supporting the Galax Governance Foundation and Agent 01. These tools operate outside the CrewAI runtime and do not increase the active Galax production-agent count.

## Final designated roster

```yaml
CLINE-01:
  product: Cline
  role: Supervised Primary Implementation Engineer
  score: 86
  canonical_charter: ../../prompts/external-ai-contributors/CLINE_ROLE_CHARTER.md

OPENHANDS-01:
  product: OpenHands Core
  role: Docker-Isolated Fallback and Reproduction Engineer
  score: 84
  canonical_charter: ../../prompts/external-ai-contributors/OPENHANDS_CORE_ROLE_CHARTER.md

MSWE-01:
  product: mini-SWE-agent
  role: Isolated Independent Patch and Trajectory Analyst
  score: 83
  canonical_charter: ../../prompts/external-ai-contributors/MINI_SWE_AGENT_ROLE_CHARTER.md

AIDER-01:
  product: Aider
  role: Surgical Test and Lint Repair Specialist
  score: 82
  canonical_charter: ../../prompts/external-ai-contributors/AIDER_ROLE_CHARTER.md

PRAGENT-01:
  product: PR-Agent
  role: Read-Only Pull Request Quality Reviewer
  score: 82
  canonical_charter: ../../prompts/external-ai-contributors/PR_AGENT_ROLE_CHARTER.md
```

The scores are Galax paper-compatibility scores, not universal accuracy percentages. Every contributor remains blocked from activation until its exact controlled trial passes.

## Canonical reading order

1. `../../prompts/external-ai-contributors/README.md`
2. `../../prompts/external-ai-contributors/SHARED_EXECUTION_PROTOCOL.md`
3. The exact selected contributor charter.
4. `../../plan/EXTERNAL_AI_CONTRIBUTOR_WORK_ASSIGNMENT_PLAN.md`
5. `../../prompts/external-ai-contributors/CONTROLLED_TASK_PACKET_TEMPLATE.md`
6. `../../research/ai-tools/AI_CONTRIBUTOR_COMMAND_DESIGN_SURVEY_2026-07-21.md`
7. `../../research/ai-tools/AI_DEVELOPMENT_CONTRIBUTOR_FINAL_QUALIFICATION_REVIEW_V3_2026-07-21.md`

The individual charters contain the professional background, goal, exact designated work, operating configuration, mandatory start command, prohibited work, success criteria, and failure remedy. They are the canonical role commands.

## Operational sequence

```text
Human issues one completed task packet
        ↓
CLINE-01 plans and implements
        ↓
AIDER-01 may fix one exact reproducible failure after Cline stops
        ↓
MSWE-01 may produce an isolated comparison patch
        ↓
OPENHANDS-01 may reproduce or replace a stopped writer when explicitly activated
        ↓
PRAGENT-01 reviews a stable draft PR read-only
        ↓
Human accepts, returns, or stops
```

## Non-negotiable restrictions

```yaml
one_active_source_writer: required
parallel_overlapping_writers: prohibited
direct_main_write: prohibited
force_push: prohibited
automatic_merge: prohibited
deployment: prohibited
workflow_or_secret_write: prohibited
generic_MCP_catalog: prohibited
Agents_02_to_15: disabled
```

## Current activation status

```yaml
roles_defined: true
work_packages_defined: true
canonical_commands_defined_in_individual_charters: true
tools_installed_by_repository: false
credentials_added: false
MCP_connections_added: false
controlled_trials_passed: false
repository_write_access_granted: false
runtime_activation: false
```
