# Controlled External AI Contributor Task Packet Template

**Status:** `TEMPLATE_NOT_RUNTIME_AUTHORIZATION`

Use one completed copy for one contributor and one goal. Do not combine unrelated work.

```yaml
task_packet_version: 1

identity:
  task_id:
  contributor_id: CLINE-01 | OPENHANDS-01 | AIDER-01 | MSWE-01 | PRAGENT-01
  exact_role:
  role_charter_path:
  human_coordinator:

repository:
  repository: ariessocia04-rgb/galax-Ai-project
  required_base_branch:
  required_starting_SHA:
  assigned_task_branch_or_worktree:
  expected_clean_state: true

mission:
  single_goal:
  problem_statement:
  business_or_governance_reason:
  definition_of_done:

required_reading:
  - README.md
  - docs/prompts/external-ai-contributors/SHARED_EXECUTION_PROTOCOL.md
  - exact role_charter_path named above
  - docs/research/readiness/FINAL_PRE_PROMPT_CONFLICT_AUDIT_2026-07-20.md
  - docs/research/crewai/CREWAI_1_15_4_FULL_AGENT_REMEDIATION_BLUEPRINT_2026-07-20.md
  - docs/prompts/GALAX_FOUNDATION_AGENT01_IMPLEMENTATION_VALIDATION_PROMPT.md
  - applicable docs/rules/**
  - applicable research and source cards

scope:
  in_scope_paths: []
  out_of_scope_paths:
    - main
    - .github/workflows/**
    - secrets/**
    - Agents_02_to_15
  allowed_operations: []
  prohibited_operations:
    - direct_main_write
    - force_push
    - automatic_merge
    - deployment
    - secret_read_or_write
    - workflow_write
    - broad_remote_MCP

execution:
  plan_required: true
  plan_approval_required: true
  maximum_files_changed:
  maximum_added_dependencies: 0_unless_explicitly_approved
  maximum_steps_or_iterations:
  maximum_wall_clock_minutes:
  maximum_authorized_cost:
  network_policy: deny_by_default
  secret_policy: no_secrets_provided
  commit_policy:
  push_policy:

acceptance_criteria: []
required_tests: []
security_negative_tests: []

stop_conditions:
  - repository_branch_or_SHA_mismatch
  - missing_or_conflicting_canonical_document
  - dirty_state_from_unknown_writer
  - scope_or_allowed_path_violation
  - secret_detected
  - prohibited_permission_required
  - test_environment_unavailable
  - cost_time_or_step_limit_reached
  - architecture_change_required_but_not_approved

required_handoff:
  schema: docs/prompts/external-ai-contributors/SHARED_EXECUTION_PROTOCOL.md#10-handoff-contract
  include_patch_or_diff: true
  include_commands: true
  include_test_logs: true
  include_blockers: true
  human_decision_required: true
```

## Role charter values

```yaml
CLINE-01: docs/prompts/external-ai-contributors/CLINE_ROLE_CHARTER.md
OPENHANDS-01: docs/prompts/external-ai-contributors/OPENHANDS_CORE_ROLE_CHARTER.md
AIDER-01: docs/prompts/external-ai-contributors/AIDER_ROLE_CHARTER.md
MSWE-01: docs/prompts/external-ai-contributors/MINI_SWE_AGENT_ROLE_CHARTER.md
PRAGENT-01: docs/prompts/external-ai-contributors/PR_AGENT_ROLE_CHARTER.md
```

## Required opening response

Before editing, the contributor must return:

```yaml
status: ORIENTATION_COMPLETE | BLOCKED
contributor_id:
task_id:
repository_verified:
actual_branch:
actual_starting_SHA:
working_tree_state:
mandatory_files_read: []
current_architecture_summary:
proposed_files_to_change: []
proposed_tests: []
identified_risks: []
plan:
blockers: []
files_changed: []
awaiting_human_plan_approval: true
```

## Required final response

Use the full handoff schema in `SHARED_EXECUTION_PROTOCOL.md`. A prose-only claim such as “done” is invalid.
