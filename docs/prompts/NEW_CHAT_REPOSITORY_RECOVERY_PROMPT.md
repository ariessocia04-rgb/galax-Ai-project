# New Chat Repository Recovery Prompt

**Status:** `PASTE_READY_NO_CHANGE_RECOVERY_PROMPT`  
**Default behavior:** inspect and verify only; do not edit.

Paste the prompt below into a new ChatGPT, Jules, Codex, Cline, OpenHands, Antigravity, or other repository-aware session after a chat-length, quota, crash, or handoff interruption.

---

You are resuming an existing Galax AI project task after a conversation or tool-session interruption.

Repository:

```text
ariessocia04-rgb/galax-Ai-project
```

Your first responsibility is deterministic repository-state recovery. Do not rely on prior chat memory, platform summaries, or assumptions. The repository is the source of truth.

## Mandatory no-change recovery procedure

Before editing, creating, deleting, committing, pushing, opening a PR, running implementation commands, or changing any configuration:

1. Confirm that the connected repository is exactly:

   ```text
   ariessocia04-rgb/galax-Ai-project
   ```

2. Read `README.md` completely.

3. Read:

   ```text
   docs/continuity/README.md
   docs/rules/CHAT_SESSION_CONTINUITY_AND_RECOVERY_RULE.md
   docs/state/ACTIVE_WORK_POINTER.yaml
   docs/templates/CHAT_SESSION_CHECKPOINT_TEMPLATE.yaml
   ```

4. From `docs/state/ACTIVE_WORK_POINTER.yaml`, retrieve the exact current:

   ```yaml
   task_id:
   required_branch:
   required_base_sha:
   latest_checkpoint_path:
   required_reading:
   selected_contributor:
   selected_role:
   task_lock_status:
   allowed_paths:
   prohibited_actions:
   ```

5. Read the exact checkpoint referenced by `latest_checkpoint_path`.

6. Read every canonical document listed in the pointer and checkpoint. Do not claim a file was read unless it was actually retrieved.

7. Inspect and report the actual repository state:

   ```text
   repository owner/name
   actual checked-out or selected branch
   complete 40-character HEAD SHA
   required base SHA relationship
   current changed files
   current untracked files
   active task-lock owner
   latest available checkpoint
   ```

8. Compare expected versus actual:

   ```yaml
   repository_match:
   branch_match:
   base_sha_match:
   checkpoint_sha_match:
   task_lock_match:
   selected_contributor_match:
   allowed_paths_match:
   current_diff_within_scope:
   tests_and_evidence_available:
   newer_checkpoint_exists:
   ```

9. Apply the repository authority order:

   ```text
   exact Git and repository evidence
   → README current readiness
   → current mandatory rules
   → active-work pointer
   → latest valid structured checkpoint
   → current task packet and task lock
   → current qualification/implementation records
   → older historical records
   → chat text or model memory
   ```

10. Do not use `main` as a fallback when the pointer or checkpoint requires another branch.

## Required stop conditions

Stop without changing files when any of these occur:

```text
wrong repository
wrong branch
missing or different full SHA
missing active-work pointer
missing or incomplete checkpoint
newer checkpoint not yet reviewed
active writer lock owned by another contributor
diff outside allowed paths
canonical records conflict
required implementation authorization missing
required test evidence missing
unknown repository state
```

Return the matching status:

```yaml
READY_TO_CONTINUE:
BLOCKED_CONTEXT_MISMATCH:
BLOCKED_CHECKPOINT_INCOMPLETE:
BLOCKED_TASK_LOCK_CONFLICT:
BLOCKED_STALE_CHECKPOINT:
COMPLETED_NO_CONTINUATION_REQUIRED:
```

`READY_TO_CONTINUE` does not authorize source changes. It authorizes only a recovery report for human review.

## Prohibited actions during recovery

Do not:

- modify files;
- create a new branch;
- commit or push;
- open, merge, or close a PR;
- reset, rebase, cherry-pick, or force-push;
- install dependencies;
- run scripts that modify the repository;
- activate an LLM profile;
- activate CrewAI planning, reasoning, memory, delegation, or parallel agents;
- expose secrets;
- enable Agents 02–15;
- infer missing facts;
- restart the task from `main`;
- continue implementation before human confirmation.

## Required recovery report

Return only this structure:

```yaml
recovery_report_version: 1
repository:
requested_task_id:
active_pointer_path: docs/state/ACTIVE_WORK_POINTER.yaml
latest_checkpoint_path:

expected:
  branch:
  base_sha:
  checkpoint_head_sha:
  selected_contributor:
  selected_role:
  task_lock_status:
  allowed_paths: []

actual:
  repository:
  branch:
  head_sha:
  working_tree_clean:
  modified_files: []
  untracked_files: []
  active_task_lock_owner:

verification:
  README_read:
  continuity_rule_read:
  active_pointer_read:
  latest_checkpoint_read:
  canonical_documents_read: []
  missing_documents: []
  repository_match:
  branch_match:
  sha_match:
  task_lock_match:
  scope_match:
  newer_checkpoint_found:
  files_changed_during_recovery: []

status:
blockers: []
exact_safe_remedy:
next_safe_action:
human_approval_required: true
```

If any value cannot be verified, use:

```text
UNKNOWN_NOT_VERIFIED
```

Never invent a value.

Stop after returning the recovery report.

---

## Owner shortcut

The owner can start a new chat with only this message:

```text
Continue the Galax task using the repository continuity protocol.
Repository: ariessocia04-rgb/galax-Ai-project
Read and execute:
docs/prompts/NEW_CHAT_REPOSITORY_RECOVERY_PROMPT.md
Do not edit anything until the repository, active-work pointer, latest checkpoint, branch, full SHA, task lock, and allowed paths are verified.
```
