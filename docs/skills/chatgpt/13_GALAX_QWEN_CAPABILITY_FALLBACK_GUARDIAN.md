```yaml
skill_reference: $galax-qwen-capability-fallback-guardian
skill_id: GALAX-SKILL-13
native_plugin_skill: false
custom_GPT_knowledge_file: true
```

# Skill 13: Galax Qwen Capability Fallback Guardian

## 1. Purpose

Skill 13 controls a **Qwen Code fallback for one already-authorized bounded Galax objective only when the current Cline execution path has a verified tool/capability failure and Qwen's exact replacement capability is currently proven**.

Qwen is not a general replacement for Cline. Cline remains the default repository executor whenever Cline is capable.

This skill exists to prevent repeated Cline loops where the problem is not the Galax code or test itself, but the executor/tool path, such as:

- the current Cline toolset explicitly lacks the required local edit/write mechanism;
- the same bounded command/output observation path repeatedly fails to expose stdout, stderr, exit code, or process state;
- a read-only remote GitHub evidence step is required, the current Cline route lacks or fails that exact access path, and Qwen's own read-only GitHub MCP path is proven live.

Skill 13 never overrides the permanent CrewAI remediation immutable set.

## 2. Highest-priority permanent remediation precheck

Canonical permanent lock:

```text
docs/rules/GALAX_CREWAI_REMEDIATION_BLUEPRINT_FOCUS_LOCK_2026-08-09.md
```

Permanent protected set:

```yaml
PERMANENT_CREWAI_REMEDIATION_SET:
  - docs/research/crewai/CREWAI_1_15_4_FULL_AGENT_REMEDIATION_BLUEPRINT_2026-07-20.md
  - docs/rules/GALAX_CREWAI_REMEDIATION_BLUEPRINT_FOCUS_LOCK_2026-08-09.md
  - docs/plan/FOUNDATION_AGENT01_FLOW_EXECUTION_CONTRACT_2026-07-21.md
```

If a proposed Qwen fallback would directly or indirectly edit, rewrite, delete, rename, move, reformat, replace, supersede, reinterpret, weaken, unlock, or alter the technical meaning of this set:

```text
BLOCKED_PERMANENT_CREWAI_REMEDIATION_LOCK
```

and no Qwen task may be emitted.

Allowed interaction with the permanent set remains read/check/non-mutating validation only. Skill 13 cannot create a Qwen exception to this rule.

## 3. Activation boundary

A Qwen fallback candidate exists only for the **same bounded objective** that Cline could not complete because of an executor/tool capability problem.

At least one of these must be proven:

```yaml
CLINE_CAPABILITY_FAILURE_CLASS:
  EXPLICIT_TOOL_ABSENCE:
    examples:
      - current_Cline_toolset_has_no_required_edit_or_write_tool
      - required_execution_or_observation_tool_is_not_available_in_current_Cline_session
    minimum_failures_required: 1

  REPEATED_SAME_CLASS_TOOL_FAILURE:
    examples:
      - command_output_remains_unobservable
      - stdout_stderr_or_exit_code_cannot_be_recovered
      - process_state_cannot_be_observed_through_current_Cline_path
    minimum_material_failures_required: 2
    same_bounded_goal_required: true
    no_material_repository_state_change_between_failures: true

  CLINE_REMOTE_EVIDENCE_PATH_UNAVAILABLE:
    examples:
      - exact_read_only_GitHub_or_MCP_evidence_path_is_missing_or_has_failed
    minimum_failures_required: 1_when_capability_absence_is_explicit_otherwise_2
```

An ordinary error is not enough.

Do NOT route to Qwen merely because:

- a test failed;
- the code is incorrect;
- Cline produced a bad patch that can be corrected normally;
- Human Owner permission is missing;
- credentials are missing;
- branch/SHA/scope is mismatched;
- the task would touch `LOCKED_ACCEPTED` work without authority;
- the requested action is commit, push, merge, or deploy;
- the current problem is a permanent remediation mutation request;
- the task is simply difficult or long.

## 4. Qwen capability proof gate

Official product documentation can prove that a Qwen feature exists in the product, but it does not prove that the feature is working in the Human Owner's current installation.

Before fallback execution, the exact required local Qwen capability must be classified as:

```text
CURRENT_TOOL_CAPABILITY_PROVEN
```

Required proof depends on the fallback class.

```yaml
QWEN_CAPABILITY_PROOF:
  local_edit_write:
    prove_current_Qwen_tools_include:
      - edit_or_equivalent
      - write_file_or_equivalent_when_creation_is_required

  validation_output_capture:
    prove_current_Qwen_tools_include:
      - run_shell_command_or_equivalent
    prove_execution_result_can_report:
      - stdout
      - stderr
      - exit_code

  long_running_process_observation:
    prove_current_Qwen_tools_include_one_safe_supported_path:
      - monitor
      - managed_background_shell_plus_task_status_output

  read_only_GitHub_MCP:
    prove_Qwen_itself_recognizes_GitHub_MCP: true
    prove_Qwen_native_MCP_call_path: true
    prove_GitHub_MCP_read_only_behavior: true
    standalone_MCP_binary_test_alone_is_sufficient: false
```

If the exact current Qwen capability is not proven:

```text
BLOCKED_QWEN_CAPABILITY_NOT_PROVEN
```

Do not infer capability from installation, configuration text, old chat memory, or standalone helper scripts alone.

## 5. Allowed fallback classes

Skill 13 initially permits only these classes.

### A. Local file edit/write fallback

Use only when Cline's current tool path has a verified edit/write capability blocker and there is already an exact authorized target and approved content/diff.

```yaml
QWEN_LOCAL_EDIT_WRITE_FALLBACK:
  exact_target_files_required: true
  exact_change_or_approved_diff_required: true
  Human_Owner_ACT_authorization_required: true
  simultaneous_Cline_writer: prohibited
  helper_or_temp_file_creation: prohibited_unless_separately_authorized
  unrelated_file_change: prohibited
  automatic_validation_after_edit: prohibited
  git_stage_commit_push: prohibited
  stop_after_exact_save_and_evidence: true
```

Qwen must not redesign or broaden an already-approved correction simply because Qwen is the fallback writer.

### B. Validation/output capture fallback

Use when Cline could not obtain reliable command/output evidence for an already-authorized exact validation command.

```yaml
QWEN_VALIDATION_OUTPUT_CAPTURE_FALLBACK:
  exact_command_required: true
  exact_working_directory_required: true
  separate_Human_Owner_VALIDATION_authorization_required: true
  automatic_retry: prohibited
  automatic_fix: prohibited
  file_edit_during_validation: prohibited
  capture_required:
    - exact_command
    - working_directory
    - stdout
    - stderr
    - exit_code
    - termination_or_signal_state_when_available
  stop_after_evidence_capture: true
```

A Qwen validation PASS does not authorize commit, push, another test suite, Ruff, formatting, or a code correction.

### C. Long-running process observation fallback

Use only to observe an already-authorized long-running command/process when the Cline path cannot furnish observable evidence.

```yaml
QWEN_LONG_RUNNING_OBSERVATION_FALLBACK:
  launch_new_process_only_if_exact_launch_was_separately_authorized: true
  attach_or_monitor_when_supported: preferred
  process_mutation_beyond_stop_control: prohibited
  source_edit: prohibited
  automatic_restart: prohibited
  evidence_required:
    - process_or_task_identity
    - observable_output
    - completion_or_running_state
    - exit_or_stop_state_when_available
```

### D. Read-only GitHub MCP evidence fallback

Use only when remote GitHub evidence is required and Qwen's own GitHub MCP path has been proven read-only and operational.

```yaml
QWEN_GITHUB_MCP_FALLBACK:
  allowed:
    - repository_metadata_read
    - file_read
    - code_search
    - branch_status_read
    - commit_status_read
    - diff_or_compare_read
    - PR_issue_metadata_read
  prohibited:
    - create_or_update_file
    - delete_file
    - create_branch
    - create_or_update_issue
    - create_or_update_PR
    - review_or_comment_write
    - commit
    - push
    - merge
    - repository_setting_change
  required_mode: READ_ONLY
```

## 6. Mandatory fallback gate

Before issuing a Qwen task, return:

```yaml
GALAX_QWEN_CAPABILITY_FALLBACK_GATE_V1:
  repository: ariessocia04-rgb/galax-Ai-project
  Human_Owner_request:
  current_assignment:
  same_bounded_objective_as_failed_Cline_task: true | false
  current_branch_or_workspace:
  current_HEAD_SHA:

  permanent_CrewAI_remediation_collision: true | false
  LOCKED_ACCEPTED_conflict: true | false
  simultaneous_writer_risk: true | false

  Cline_default_executor: true
  Cline_failure_class:
  Cline_capability_failure_proven: true | false
  Cline_failure_evidence: []
  repeated_failure_count:
  material_state_change_between_failures: true | false

  proposed_Qwen_fallback_class:
  Qwen_exact_capability_required: []
  Qwen_current_tool_capability_proven: true | false
  Qwen_capability_evidence: []

  Human_Owner_authorized_exact_fallback_stage: true | false
  exact_allowed_files: []
  exact_allowed_command:
  exact_allowed_remote_reads: []
  exact_stop_condition:

  gate_result:
    PASS_QWEN_CAPABILITY_FALLBACK |
    BLOCKED_PERMANENT_CREWAI_REMEDIATION_LOCK |
    BLOCKED_CLINE_CAPABILITY_FAILURE_NOT_PROVEN |
    BLOCKED_CLINE_STILL_CAPABLE |
    BLOCKED_QWEN_CAPABILITY_NOT_PROVEN |
    BLOCKED_OWNER_AUTHORIZATION_REQUIRED |
    BLOCKED_LOCK_CONFLICT |
    BLOCKED_SIMULTANEOUS_WRITER_RISK |
    BLOCKED_SCOPE_EXPANSION
```

If Cline is currently capable of the exact action, result must be:

```text
BLOCKED_CLINE_STILL_CAPABLE
```

Skill 13 must not be used merely to prefer Qwen or compare models.

## 7. Qwen task packaging

For an allowed Qwen fallback, ChatGPT must choose the exact session/mode and present this header outside the Qwen prompt:

```text
QWEN SESSION: NEW | STAY
QWEN MODE: PLAN | ACT | VALIDATE | REVIEW
CANONICAL MODE: PLAN_ONLY | ACT_BOUNDED | VALIDATION_ONLY | REVIEW_ONLY
OWNER ACTION: <one exact plain-language action>
DO NOT: <exact prohibitions>
EXPECTED QWEN STOP: <exact stop point>
AFTER QWEN STOPS: <exact evidence/result to return to ChatGPT>
QWEN PROMPT REQUIRED: YES | NO
```

Mode mapping:

```yaml
PLAN: PLAN_ONLY
ACT: ACT_BOUNDED
VALIDATE: VALIDATION_ONLY
REVIEW: REVIEW_ONLY
```

Qwen GIT mode does not exist under Skill 13 because commit/push/merge are prohibited.

Use `STAY` only for the same bounded Qwen fallback assignment. Use `NEW` for a new fallback assignment or when prior Qwen context is stale/conflicting. Do not ask the Human Owner to choose the mode/session.

## 8. Writer isolation

Qwen and Cline must not mutate the same Galax worktree at the same time.

Before an ACT_BOUNDED Qwen local write:

```yaml
writer_isolation:
  Cline_mutation_task_active: false
  Qwen_mutation_task_active: false_before_start
  one_writer_only: required
  current_branch_HEAD_and_worktree_state_captured: required
```

After Qwen stops, ChatGPT reviews the exact evidence before any Cline continuation is prepared.

## 9. Consequential-stage separation

```text
QWEN PLAN ≠ QWEN ACT
QWEN ACT ≠ QWEN VALIDATION
QWEN VALIDATION ≠ COMMIT
```

Skill 13 never authorizes Qwen to commit or push.

If Qwen creates an authorized local edit that later becomes commit-eligible, normal Galax routing resumes. Cline remains the normal Git executor when capable, with separate Human Owner COMMIT and PUSH authorization.

## 10. Failure and no-loop rule

If Qwen also fails the same capability stage:

```yaml
QWEN_FALLBACK_FAILURE:
  automatic_retry: prohibited
  automatic_return_to_Cline: prohibited
  automatic_second_fallback_executor: prohibited
  report_exact_blocker: required
  preserve_all_successful_prior_evidence: required
```

Do not create an executor ping-pong loop.

## 11. Evidence review

Every Qwen result returns to ChatGPT for bounded evidence review before another stage.

Required receipt:

```yaml
GALAX_QWEN_CAPABILITY_FALLBACK_RESULT_V1:
  assignment:
  fallback_class:
  execution_mechanism:
  starting_branch_or_workspace:
  starting_HEAD_SHA:
  files_created: []
  files_modified: []
  files_deleted: []
  commands_run: []
  stdout_captured:
  stderr_captured:
  exit_code:
  remote_reads: []
  Git_write_operations: []
  permanent_CrewAI_remediation_set_changed: false
  LOCKED_ACCEPTED_changed: false
  unrelated_changes_detected: []
  exact_stop_condition_met: true | false
  status: PASS | CHANGES_REQUIRED | BLOCKED
```

Local Qwen evidence does not become remote GitHub proof unless the remote state is separately read and verified.

## 12. Known Galax evidence class motivating this skill

Repository continuity evidence has already recorded executor-path blockers including:

```yaml
historical_examples:
  Assignment_060:
    blocker: Cline_toolset_has_no_native_file_edit_or_write_tool
    result: approved_diff_remained_unsaved_until_alternative_writer_mechanisms_were_investigated

  Failure_2_full_suite_recovery:
    blocker: BLOCKED_VALIDATION_OUTPUT_STILL_UNOBSERVABLE
    known_missing_evidence:
      - full_suite_stdout_stderr
      - full_suite_exit_code
      - original_pytest_process_state
```

These examples justify the fallback category. They do not automatically authorize Qwen on future tasks; the live gate still applies every time.

## 13. Strict prohibitions

```yaml
replace_Cline_by_default: prohibited
route_every_Cline_error_to_Qwen: prohibited
Qwen_without_current_capability_proof: prohibited
Qwen_commit: prohibited
Qwen_push: prohibited
Qwen_merge: prohibited
Qwen_deploy: prohibited
Qwen_force_push: prohibited
Qwen_secret_mutation: prohibited
Qwen_dependency_change_without_separate_future_authority: prohibited
Qwen_workflow_change: prohibited
Qwen_permanent_remediation_mutation: prohibited
simultaneous_Cline_Qwen_writers: prohibited
automatic_retry_loop: prohibited
automatic_scope_expansion: prohibited
```

## 14. Final contract

```text
Cline capable of exact bounded action
→ Cline remains executor.

Cline exact tool/capability failure proven
+ same bounded objective preserved
+ Qwen exact current capability proven
+ no permanent-lock/LOCKED_ACCEPTED/simultaneous-writer conflict
+ Human Owner authorizes the exact fallback stage
→ Skill 13 may package one bounded Qwen fallback.

Qwen completes fallback stage
→ STOP
→ ChatGPT reviews evidence
→ normal Galax routing resumes only after Human Owner controls the next consequential stage.

Permanent CrewAI remediation mutation/unlock
→ BLOCKED_PERMANENT_CREWAI_REMEDIATION_LOCK
→ no Qwen fallback.
```
