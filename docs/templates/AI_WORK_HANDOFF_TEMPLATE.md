# AI Work Handoff Template

Copy this template to:

```text
docs/handoff/chat-history/YYYY-MM-DD_<task-id>_<sequence>.md
```

Do not overwrite an earlier handoff record.

```yaml
handoff_version: 1
created_at_utc:
repository: ariessocia04-rgb/galax-Ai-project
conversation_or_session_id: optional_reference_only

repository_state:
  active_branch:
  required_base_branch:
  required_base_sha:
  last_verified_remote_head_sha:
  branch_descends_from_required_base: UNKNOWN_REQUIRES_VERIFICATION
  working_tree_state: CLEAN | DIRTY | UNKNOWN_REMOTE_ONLY
  task_lock_status: ACTIVE | RELEASED | EXPIRED | BLOCKED | NONE

assignment:
  current_scope:
  current_task_id:
  selected_writer_or_reviewer:
  exact_role:
  allowed_paths: []
  protected_paths: []
  acceptance_tests: []
  security_negative_tests: []
  prohibited_actions: []

context_retrieved:
  canonical_documents_read: []
  exact_prompt_or_task_packet:
  source_records_used: []

work_state:
  completed_work: []
  requirements_remaining: []
  files_added_or_changed: []
  files_untracked: []
  commits_created: []
  pull_request:
  commands_or_tools_used: []

evidence:
  tests_run:
    - command:
      result:
      evidence:
  tests_not_run: []
  lint_result:
  type_check_result:
  security_test_result:
  diff_reviewed: false
  external_evidence_ids: []

truth_and_risk:
  claims_not_yet_proven: []
  known_failures: []
  known_blockers: []
  security_observations: []
  unauthorized_operations_attempted: []
  secrets_exposed: false
  quota_or_capacity_state:
  cost_observed:

continuation:
  exact_next_safe_action:
  stop_conditions_still_active: []
  human_decision_required:
  new_chat_bootstrap_prompt_path: docs/templates/CHATGPT_NEW_CHAT_BOOTSTRAP_PROMPT.md
  current_context_pointer_to_update: docs/handoff/CURRENT_CHAT_CONTEXT.md
```

## Validation rules

```text
- Do not guess missing values.
- Use UNKNOWN_REQUIRES_VERIFICATION when evidence is absent.
- Do not claim a test passed without command output or trusted CI evidence.
- Do not claim a branch or SHA without querying GitHub or the actual checkout.
- Do not transfer write ownership while the previous task lock remains active.
- Do not include API keys, tokens, passwords, cookies, or secret values.
- Do not write private chain-of-thought; record decisions, actions, evidence, blockers, and next steps.
```
