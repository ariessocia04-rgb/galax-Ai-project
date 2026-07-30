# Compatibility Redirect — CODE RED and New-Chat Continuity Guide

**Status:** `COMPATIBILITY_REDIRECT`  
**Previous role:** canonical conversation-length continuity protocol  
**Canonical protocol:** `docs/operations/CODE_RED.md`  
**Current exact handoff guide:** `docs/operations/GALAX_NEW_CHAT_CONTINUITY_GUIDE_2026-07-27.md`  
**Latest exact checkpoint:** `docs/operations/checkpoints/GALAX_LENGTH_CHECKPOINT_2026-07-27_CREWAI_COMPATIBILITY_AUDIT.md`  
**Do not use this file alone as the source of truth.**

The owner renamed the Galax continuity and recovery protocol to:

```text
CODE RED
```

Every repository-aware AI or human that reaches this file must immediately read, in this order:

```text
README.md
→ AGENTS.md
→ docs/operations/CODE_RED.md
→ docs/operations/GALAX_NEW_CHAT_CONTINUITY_GUIDE_2026-07-27.md
→ docs/operations/checkpoints/GALAX_LENGTH_CHECKPOINT_2026-07-27_CREWAI_COMPATIBILITY_AUDIT.md
→ the active assignment, pull requests, issues, branch heads, and newest continuity comments
```

`CODE_RED.md` defines the canonical recovery protocol. The dated continuity guide records the material work completed from the beginning. The latest checkpoint records the newest exact stop point and safe resume action. Live GitHub state must still be verified because no checkpoint grants authority or freezes future branch movement.

Legacy and current trigger phrases all route to this procedure:

```text
CODE RED
length chat problem
chat length problem
conversation length problem
continue exact Galax flow
operation length problem solve
operatiion length problem solve
backread the repo because the chat is full
new chat continuation
where did we stop
resume the latest Galax work
```

## Mandatory response to a length problem

On any trigger above, the new chat must:

```text
stop relying on remembered chat fragments
→ verify repository access
→ verify the current research, implementation, plan, and continuity branch HEAD SHAs
→ read CODE RED completely
→ read the current new-chat continuity guide completely
→ read the latest exact checkpoint completely
→ inspect active Draft PRs and assignment issues
→ separate remote-proven facts from reported local-only facts
→ reconstruct completed, rejected, active, blocked, and pending work
→ determine the exact stop point and exact next safe action
→ return GALAX_NEW_CHAT_CONTINUATION_RECEIPT_V1
→ continue only when repository evidence and authorization agree
```

Do not ask the owner to repeat repository history when repository access exists. Do not create another plan merely because the conversation changed. Do not repeat completed work.

## Current dual-track stop point

The latest checkpoint separates two independent work tracks:

```yaml
Track_A_Cline_Issue_9:
  exact_stop_point: WAITING_FOR_CLINE_EXECUTION_READINESS_RECEIPT_V1
  Cline_execution_proven: false

Track_B_ChatGPT_CrewAI_compatibility_audit:
  exact_stop_point: SOURCE_LEVEL_AUDIT_PAUSED_BEFORE_EXACT_ONE_LLM_CALL_PROOF
  overall_verdict: IN_PROGRESS_CANNOT_CLAIM_100_PERCENT_YET
```

A new chat must not confuse the active Cline assignment with the separately requested factual CrewAI compatibility audit.

## Owner standing checkpoint directive

When the owner explicitly indicates that the current conversation or task will stop, pause, continue later, move to a new chat, or has reached a conversation-length problem, the active AI must enter `SAVE_CURRENT_TASK_CHECKPOINT` mode before starting or resuming another assignment.

The checkpoint must record exact observable evidence without guessing:

```yaml
SAVE_CURRENT_TASK_CHECKPOINT_V1:
  recorded_at_utc:
  active_assignment_id:
  active_contributor:
  active_mode:
  repository:
  branch:
  starting_sha:
  current_sha_or_worktree_state:
  last_completed_actual_action:
  successfully_saved_files: []
  displayed_but_not_executed_actions: []
  rejected_actions: []
  pending_human_approval:
  actions_that_must_not_be_repeated: []
  validation_status:
  commit_status:
  push_status:
  pull_request_status:
  exact_stop_point:
  exact_safe_resume_action:
  prohibited_resume_actions: []
```

Checkpoint rules:

1. Distinguish proposed, displayed, approved, executed, saved, committed, pushed, reviewed, and accepted.
2. Never treat a displayed patch as a saved edit.
3. Never treat an active issue as proof that its contributor started.
4. Never repeat an already completed or saved action.
5. Never restore or reuse rejected work.
6. Preserve the exact assignment ID, branch, starting SHA, and allowed scope.
7. A continuity checkpoint grants no edit, validation, commit, push, merge, deployment, reviewer-trigger, or new-assignment authority.
8. Store the durable checkpoint in the active GitHub issue or PR when tracked-file mutation is not separately authorized.
9. Update CODE RED only through a separately authorized bounded repository change.
10. Resume only from the exact recorded safe action after verifying live repository state.

Capability boundary:

```yaml
silent_chat_close_event_available: false
background_inactivity_trigger_available: false
explicit_stop_or_length_message_trigger: required
controlled_stage_boundary_checkpoint: required
```

The AI cannot detect a silent browser close or user inactivity when no message is received. Checkpoint behavior therefore starts from an explicit owner message or a controlled stage reaching a human-approval boundary.

This redirect is retained because older repository documents, prompts, issues, and conversations may still reference the old path.

Do not delete it until:

```text
all inbound references are inventoried
→ every active reference is migrated to CODE RED, the current continuity guide, and the latest checkpoint
→ historical evidence is preserved
→ link and repository checks pass
→ the human owner explicitly authorizes removal
→ deletion is recorded in CODE RED
```
