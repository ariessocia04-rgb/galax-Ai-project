# Compatibility Redirect — CODE RED

**Status:** `COMPATIBILITY_REDIRECT`  
**Previous role:** canonical conversation-length continuity protocol  
**Canonical replacement:** `docs/operations/CODE_RED.md`  
**Do not use this file as the current source of truth.**

The owner renamed the Galax continuity and recovery protocol to:

```text
CODE RED
```

Every repository-aware AI or human that reaches this file must immediately read:

```text
docs/operations/CODE_RED.md
```

and follow its complete repository reconstruction, action ledger, status, cleanup, accepted-work protection, CrewAI compatibility, and next-action rules.

Legacy trigger phrases remain recognized and route to CODE RED:

```text
length chat problem
chat length problem
conversation length problem
continue exact Galax flow
operation length problem solve
operatiion length problem solve
```

## Owner standing checkpoint directive

When the owner explicitly indicates that the current conversation or task will stop, pause, continue later, move to a new chat, or has reached a conversation-length problem, the active AI must enter `SAVE_CURRENT_TASK_CHECKPOINT` mode before starting or resuming another assignment.

The checkpoint must record the exact current evidence without guessing:

```yaml
active_assignment_id:
active_mode:
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
```

Checkpoint rules:

1. Distinguish proposed, displayed, approved, executed, successfully saved, rejected, and pending actions.
2. Never treat a displayed patch as a saved edit.
3. Never repeat an already completed or already saved action.
4. Never restore or reuse a rejected patch.
5. Preserve the active assignment ID and strict scope.
6. A continuity checkpoint does not authorize file edits, validation, commit, push, merge, deployment, pull-request mutation, or a new assignment.
7. Store the durable checkpoint in the repository continuity record designated by `docs/operations/CODE_RED.md`; when tracked-file mutation is not separately authorized, record it in the active GitHub continuity issue instead and defer the CODE RED file update to a separate bounded assignment.
8. Resume only from the exact recorded safe action after human authorization.

Capability boundary:

```yaml
silent_chat_close_event_available: false
background_inactivity_trigger_available: false
explicit_stop_or_length_message_trigger: required
stage_boundary_checkpoint_when_context_is_active: required
```

The AI cannot detect a silent browser close or user inactivity event when no message is received. Therefore, the automatic checkpoint behavior applies when the owner sends a stop, pause, continue-later, new-chat, or length-problem instruction, or when an active controlled stage reaches a human-approval boundary during the conversation.

This redirect is retained temporarily because older repository documents, prompts, issues, and conversations may still reference the old path.

Do not delete this redirect until:

```text
all inbound references are inventoried
→ every active reference is migrated to docs/operations/CODE_RED.md
→ historical evidence is preserved
→ link and repository checks pass
→ the human owner explicitly authorizes removal
→ the deletion is recorded in CODE RED
```
