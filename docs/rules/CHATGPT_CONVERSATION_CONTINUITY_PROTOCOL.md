# ChatGPT Conversation Continuity and Recovery Protocol

**Status:** `MANDATORY_REPOSITORY_CONTINUITY_RULE`  
**Applies to:** ChatGPT, Codex, Jules, Cline, OpenHands, Aider, mini-SWE-agent, PR-Agent, Antigravity, and any future repository-aware assistant.  
**Purpose:** Preserve exact project state when a conversation reaches its maximum length, becomes unavailable, is restarted, or moves to another AI tool.

## 1. Core rule

```text
Conversation memory is helpful context, but it is never the canonical project state.
The repository, exact branch, exact commit SHA, task packet, test evidence, and written handoff are canonical.
```

A new chat must not continue implementation from remembered summaries alone. It must reconstruct the task from repository evidence before planning, editing, testing, reviewing, or creating branches.

## 2. Official ChatGPT continuity option

OpenAI Projects can keep related chats, files, and project instructions together and are suitable for long-running work. However, Galax still requires a repository checkpoint because project memory does not replace branch, SHA, diff, test, and authorization verification.

Official references:

- https://help.openai.com/en/articles/10169521-projects-in-chatgpt
- https://help.openai.com/en/articles/7996703

## 3. Trigger conditions

Create or refresh the repository handoff immediately when any of these happens:

```text
- ChatGPT displays that the conversation reached maximum length;
- the chat is very long, slow, frozen, or unreliable;
- the user plans to start a new chat;
- the active AI reaches token, task, credit, or quota limits;
- work is moved to Jules, Codex, Cline, OpenHands, Aider, mini-SWE-agent, PR-Agent, or another assistant;
- the active writer stops, fails, is cancelled, or changes;
- the task scope, branch, base SHA, permissions, model, provider, or tool changes materially.
```

## 4. Canonical continuity paths

```text
docs/handoff/CURRENT_CHAT_CONTEXT.md
  Human-readable current project and task pointer.

docs/handoff/chat-history/YYYY-MM-DD_<task-id>_<sequence>.md
  Immutable detailed handoff record for a stopped or replaced conversation.

docs/templates/CHATGPT_NEW_CHAT_BOOTSTRAP_PROMPT.md
  Paste-ready prompt for the next ChatGPT conversation.

docs/templates/AI_WORK_HANDOFF_TEMPLATE.md
  Structured handoff schema for any AI contributor.
```

`CURRENT_CHAT_CONTEXT.md` is a pointer, not historical evidence. Previous records under `chat-history/` must not be overwritten.

## 5. Required handoff fields

Every conversation handoff must record:

```yaml
handoff_version: 1
created_at_utc:
repository: ariessocia04-rgb/galax-Ai-project
conversation_or_session_id: optional_reference_only
active_branch:
required_base_branch:
required_base_sha:
last_verified_remote_head_sha:
working_tree_state: CLEAN | DIRTY | UNKNOWN_REMOTE_ONLY
current_scope:
current_task_id:
selected_writer_or_reviewer:
task_lock_status:
canonical_documents_read: []
completed_work: []
files_added_or_changed: []
commits_created: []
commands_or_tools_used: []
tests_run: []
tests_not_run: []
claims_not_yet_proven: []
known_blockers: []
quota_or_capacity_state:
prohibited_actions_reminder: []
exact_next_safe_action:
new_chat_bootstrap_prompt_path: docs/templates/CHATGPT_NEW_CHAT_BOOTSTRAP_PROMPT.md
human_decision_required:
```

Unknown values must be written as `UNKNOWN_REQUIRES_VERIFICATION`; they must never be guessed.

## 6. New-chat reconstruction sequence

The next chat must perform this sequence and stop before editing:

```text
1. Identify repository and intended branch from the user's message.
2. Read README.md completely.
3. Read AGENTS.md completely.
4. Read docs/handoff/CURRENT_CHAT_CONTEXT.md.
5. Read the referenced immutable chat-history handoff, if present.
6. Read all applicable docs/rules files.
7. Read the exact task packet, role charter, plan, and authorized prompt.
8. Query the current remote branch head SHA.
9. Compare branch, SHA, scope, task lock, files, and pending work against the handoff.
10. Inspect relevant diffs, commits, PRs, test logs, and evidence.
11. Return a RECONSTRUCTION_REPORT.
12. Wait for human confirmation when any mismatch or ambiguity exists.
13. Only then begin the separately authorized task.
```

## 7. Required reconstruction report

```yaml
status: CONTEXT_VERIFIED | BLOCKED_CONTEXT_MISMATCH | BLOCKED_INSUFFICIENT_EVIDENCE
repository:
requested_branch:
actual_branch:
actual_remote_head_sha:
required_base_sha_matched:
readme_read:
agents_md_read:
current_handoff_read:
immutable_handoff_read:
canonical_documents_read: []
task_packet_found:
task_lock_status:
current_scope:
completed_work_confirmed: []
pending_work_confirmed: []
files_or_commits_requiring_review: []
contradictions_or_stale_records: []
files_changed_during_reconstruction: []
next_safe_action:
```

During reconstruction, `files_changed_during_reconstruction` must remain empty.

## 8. Mismatch handling

Stop with `BLOCKED_CONTEXT_MISMATCH` when any of these is true:

```text
- selected repository is wrong;
- actual branch differs from the required branch;
- required base SHA cannot be proved;
- branch was created from main when another base was required;
- handoff and repository disagree about completed work;
- another writer has an active overlapping task lock;
- required files, tests, logs, commits, or evidence are missing;
- the new chat attempts to restart instead of continue from verified state;
- the new chat proposes merge, deployment, force push, direct-main write, or Agents 02–15 activation.
```

Required response:

```yaml
status: BLOCKED_CONTEXT_MISMATCH
expected:
actual:
evidence:
safe_recovery_steps: []
files_changed: []
```

## 9. No-memory-only rule

Prohibited statements unless verified from the repository or current external source:

```text
"I remember the branch."
"The previous chat already completed it."
"The tests passed before."
"The prompt was approved."
"The ZIP was uploaded."
"The agent is qualified."
"Nothing changed since the last chat."
```

The assistant may say that a prior summary suggests something, but must label it `UNVERIFIED_UNTIL_REPOSITORY_CHECK`.

## 10. ChatGPT Project recommendation

For the user-facing workflow:

```text
1. Keep Galax conversations inside one ChatGPT Project when available.
2. Add project instructions pointing to README.md, AGENTS.md, and this protocol.
3. Start a new chat inside the same project when the prior conversation is too long.
4. Paste the bootstrap prompt from docs/templates/CHATGPT_NEW_CHAT_BOOTSTRAP_PROMPT.md.
5. Still require repository reconstruction before work.
```

Project memory is convenience; Git evidence is authority.

## 11. Handoff update ownership

```yaml
active_writer:
  must_write_handoff_before_stop: true
reviewer:
  may_append_review_findings: true
  may_not_rewrite_writer_history: true
human_owner:
  may_correct_handoff:
    only_with_reason_and_evidence: true
new_AI:
  may_not_overwrite_previous_handoff: true
  must_create_new_sequence_record: true
```

## 12. Current Galax restrictions preserved across chats

```yaml
current_scope: Governance_Foundation_and_Agent_01_only
Agents_02_to_15: disabled
direct_main_write: prohibited
force_push: prohibited
automatic_merge: prohibited
deployment: prohibited
one_active_source_writer_per_task: required
overlapping_parallel_writers: prohibited
reviewer_source_write: prohibited
account_rotation_to_evade_quota: prohibited
claims_without_evidence: prohibited
```

## 13. Success definition

Conversation recovery is successful only when:

```yaml
repository_verified: true
branch_verified: true
remote_head_sha_recorded: true
base_relationship_verified: true
canonical_rules_read: true
task_packet_verified: true
task_lock_verified: true
completed_and_pending_work_reconciled: true
files_changed_before_authorization: 0
human_mismatch_decision_recorded_when_required: true
```

This protocol preserves continuity. It does not itself authorize implementation, credentials, repository writes, merge, deployment, or runtime activation.
