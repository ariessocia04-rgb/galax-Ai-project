# Galax Conversation and Agent Continuity

**Status:** `REPOSITORY_CONTINUITY_ENTRY_POINT`  
**Branch created for this documentation:** `research/ai-qualification-framework`  
**Runtime activation:** prohibited.

## Purpose

This directory provides a deterministic recovery path when a ChatGPT conversation, coding-agent session, provider quota, browser session, or development handoff is interrupted.

The continuity system prevents a new session from guessing what happened in an old conversation.

## Recovery path

```text
README.md
→ docs/continuity/README.md
→ docs/rules/CHAT_SESSION_CONTINUITY_AND_RECOVERY_RULE.md
→ docs/state/ACTIVE_WORK_POINTER.yaml
→ checkpoint referenced by the pointer
→ exact branch and SHA verification
→ canonical task documents
→ no-change recovery report
→ human approval
→ authorized continuation
```

## Canonical continuity files

| Purpose | Path |
|---|---|
| Mandatory rules | `docs/rules/CHAT_SESSION_CONTINUITY_AND_RECOVERY_RULE.md` |
| Active task pointer | `docs/state/ACTIVE_WORK_POINTER.yaml` |
| Structured checkpoint template | `docs/templates/CHAT_SESSION_CHECKPOINT_TEMPLATE.yaml` |
| Paste-ready new-chat recovery prompt | `docs/prompts/NEW_CHAT_REPOSITORY_RECOVERY_PROMPT.md` |
| Per-task checkpoints | `docs/handoffs/<task-id>/checkpoints/` |
| Stable latest checkpoint | `docs/handoffs/<task-id>/LATEST.yaml` |

## Owner action after the chat-limit message

When the platform displays a message such as:

```text
You've reached the maximum length for this conversation, but you can keep talking by starting a new chat
```

start a new chat and paste:

```text
Continue the Galax task using the repository continuity protocol.
Repository: ariessocia04-rgb/galax-Ai-project
Read and execute:
docs/prompts/NEW_CHAT_REPOSITORY_RECOVERY_PROMPT.md
Do not edit anything until the repository, active-work pointer, latest checkpoint, branch, full SHA, task lock, and allowed paths are verified.
```

The complete old conversation should not be required. The new session must reconstruct the authorized state from the repository.

## Accuracy controls

A valid recovery requires:

```yaml
repository_verified: true
branch_verified: true
full_SHA_verified: true
latest_checkpoint_verified: true
task_lock_verified: true
allowed_paths_verified: true
canonical_documents_read: true
files_changed_during_recovery: []
human_approval_before_resume: true
```

If any control cannot be verified, the session must stop with a blocked status instead of filling gaps from memory.

## Checkpoint discipline

Do not wait for the chat to reach its limit. Create or refresh a checkpoint after every major stage, commit, test batch, failure, provider/tool switch, or intentional pause.

A checkpoint is evidence of state, not proof that the implementation is correct.

## Current restrictions

```yaml
automatic_resume: false
direct_main_write: prohibited
force_push: prohibited
automatic_merge: prohibited
merge: prohibited
deployment: prohibited
Agents_02_to_15: disabled
```
