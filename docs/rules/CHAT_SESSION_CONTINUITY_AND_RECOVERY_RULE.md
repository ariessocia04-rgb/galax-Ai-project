# Chat Session Continuity and Recovery Rule

**Status:** `MANDATORY_CONTINUITY_RULE_DRAFT`  
**Applies to:** ChatGPT, Jules, Codex, Cline, OpenHands, Aider, mini-SWE-agent, PR-Agent, Antigravity, and any future repository-aware development contributor.  
**Does not authorize:** implementation, runtime activation, repository write access, merge, deployment, or activation of Agents 02–15.

## 1. Trigger condition

This protocol applies when any conversation or tool session is interrupted, including:

```text
You've reached the maximum length for this conversation, but you can keep talking by starting a new chat
```

It also applies to:

- provider quota exhaustion;
- browser or application closure;
- model switching;
- tool disconnection;
- agent crash or timeout;
- a new contributor taking over an authorized task;
- any uncertainty about the current branch, SHA, files, tests, or next action.

## 2. Core continuity rule

```text
The repository is the source of truth.
Chat memory, copied prose, platform summaries, and model recollection are advisory only.
```

A new session must assume it has no reliable access to the complete previous conversation. It must recover state from the repository and verify that state against Git before continuing.

No contributor may continue work from a prose-only statement such as:

```text
Continue where we stopped.
Use the previous context.
You already know the project.
```

The minimum valid continuation chain is:

```text
repository
→ canonical README and rules
→ active-work pointer
→ latest structured checkpoint
→ exact branch and SHA verification
→ task-lock and allowed-path verification
→ test/evidence review
→ human-confirmed resume action
```

## 3. Canonical paths

Every new session must use these paths:

```yaml
entry_point: README.md
continuity_index: docs/continuity/README.md
continuity_rule: docs/rules/CHAT_SESSION_CONTINUITY_AND_RECOVERY_RULE.md
active_work_pointer: docs/state/ACTIVE_WORK_POINTER.yaml
checkpoint_template: docs/templates/CHAT_SESSION_CHECKPOINT_TEMPLATE.yaml
new_chat_prompt: docs/prompts/NEW_CHAT_REPOSITORY_RECOVERY_PROMPT.md
```

The active-work pointer must identify the current task and the exact latest checkpoint path. The pointer is not permission to start implementation.

## 4. Mandatory proactive checkpointing

A contributor must not wait for the platform to show a conversation-length warning. A checkpoint is required:

1. after repository and branch verification;
2. after every approved plan;
3. after every meaningful implementation stage;
4. after every commit or published branch change;
5. after tests or security checks;
6. before a long research or implementation response;
7. before switching models, tools, or contributors;
8. when quota or context is becoming limited;
9. immediately before stopping, pausing, or handing off;
10. after any failure that changes the safe next action.

Recommended repository path:

```text
docs/handoffs/<task-id>/checkpoints/<UTC-timestamp>-<contributor-id>.yaml
```

The stable pointer for the latest checkpoint is:

```text
docs/handoffs/<task-id>/LATEST.yaml
```

A checkpoint may be committed only on the task's authorized branch. It must never be written directly to `main`.

## 5. Checkpoint completeness gate

A checkpoint is invalid unless it contains all required fields from:

```text
docs/templates/CHAT_SESSION_CHECKPOINT_TEMPLATE.yaml
```

At minimum it must record:

- repository owner/name;
- task ID and canonical goal;
- contributor and exact assigned role;
- required base branch and base SHA;
- current branch and current full SHA;
- working-tree state;
- active task-lock status;
- allowed and protected paths;
- canonical documents read;
- files changed and untracked files;
- commands and tools used;
- tests run with actual results;
- decisions made with evidence;
- unresolved blockers and risks;
- quota/cost/context state;
- prohibited actions attempted;
- exact next safe action;
- actions that remain prohibited;
- checkpoint integrity hash when implemented.

Missing branch, SHA, allowed paths, tests, or next action produces:

```yaml
status: BLOCKED_CHECKPOINT_INCOMPLETE
```

## 6. New-chat recovery sequence

The new session must execute this order exactly.

### Stage 0 — No-change orientation

Before editing anything:

1. confirm the connected repository is `ariessocia04-rgb/galax-Ai-project`;
2. read `README.md` completely;
3. read this continuity rule;
4. read `docs/continuity/README.md`;
5. read `docs/state/ACTIVE_WORK_POINTER.yaml`;
6. read the checkpoint referenced by the pointer;
7. read all required canonical files listed in that checkpoint;
8. inspect the exact current branch and full HEAD SHA;
9. inspect repository status and changed files;
10. compare the observed state with the checkpoint.

No file changes are permitted during Stage 0.

### Stage 1 — Deterministic state comparison

The new session must compare:

```yaml
expected_repository_vs_actual:
expected_branch_vs_actual:
expected_base_SHA_vs_actual:
checkpoint_current_SHA_vs_actual_HEAD:
expected_writer_vs_requesting_writer:
allowed_paths_vs_current_diff:
task_lock_vs_current_session:
reported_tests_vs_available_evidence:
latest_checkpoint_vs_any_newer_checkpoint:
```

### Stage 2 — Resume decision

Only one result is allowed:

```yaml
READY_TO_CONTINUE:
  meaning: repository, branch, SHA, lock, scope, and checkpoint all match

BLOCKED_CONTEXT_MISMATCH:
  meaning: one or more required facts differ

BLOCKED_CHECKPOINT_INCOMPLETE:
  meaning: required continuation evidence is missing

BLOCKED_TASK_LOCK_CONFLICT:
  meaning: another writer still owns the task or overlapping paths

BLOCKED_STALE_CHECKPOINT:
  meaning: repository history moved after the recorded checkpoint without an authorized handoff

COMPLETED_NO_CONTINUATION_REQUIRED:
  meaning: checkpoint and repository show the assigned task is already complete
```

When blocked, the contributor must make no changes and report the exact mismatch and safe remedy.

### Stage 3 — Human-confirmed continuation

Even when the result is `READY_TO_CONTINUE`, the new session must first return a concise recovery report and wait for human approval before source-writing work.

Exception: a separately authorized automation may continue only when its exact task contract explicitly permits automatic resume and all deterministic gates pass. No such automatic resume is currently authorized for Galax.

## 7. Priority order when records conflict

When two records disagree, use this priority:

```text
current repository evidence and exact Git state
→ README current readiness
→ current mandatory rules
→ active-work pointer
→ latest valid structured checkpoint
→ current task packet and task lock
→ current qualification/implementation records
→ older handoffs and historical research
→ chat text or model memory
```

A newer timestamp alone does not override a higher-priority canonical rule.

## 8. Anti-hallucination and anti-drift rules

A resumed contributor must not:

- invent a branch, SHA, commit, file, test, or tool result;
- claim it read a file that it did not retrieve;
- infer completion from a plan or scaffold;
- treat a conversation summary as implementation evidence;
- recreate missing work from memory without repository proof;
- restart the task from `main` when another base branch is required;
- silently choose another model, provider, tool, or architecture;
- widen allowed paths;
- continue while another writer lock is active;
- copy secrets or full private chat transcripts into the repository;
- merge, deploy, force-push, or activate Agents 02–15.

Unknown information must be recorded as:

```yaml
value: UNKNOWN_NOT_VERIFIED
```

not guessed.

## 9. Minimal new-chat message for the owner

When a chat reaches its maximum length, the owner starts a new chat and pastes only:

```text
Continue the Galax task using the repository continuity protocol.
Repository: ariessocia04-rgb/galax-Ai-project
Read and execute:
docs/prompts/NEW_CHAT_REPOSITORY_RECOVERY_PROMPT.md
Do not edit anything until the repository, active-work pointer, latest checkpoint, branch, full SHA, task lock, and allowed paths are verified.
```

The owner should not need to paste the entire old conversation.

## 10. Session closing requirement

Before a contributor intentionally ends a session, it must provide and, when authorized, persist this result:

```yaml
session_close_status:
checkpoint_path:
repository:
branch:
current_SHA:
working_tree_clean:
task_lock_status:
files_changed: []
tests_completed: []
blockers: []
next_safe_action:
resume_prompt_path: docs/prompts/NEW_CHAT_REPOSITORY_RECOVERY_PROMPT.md
```

A session that cannot persist a checkpoint must return the completed checkpoint body to the owner so it can be saved by an authorized repository contributor.

## 11. Security and privacy

Checkpoints must contain evidence references, hashes, paths, and redacted diagnostics—not:

- API keys;
- access tokens;
- passwords;
- `.env` values;
- private keys;
- cookies or session credentials;
- full confidential chat transcripts;
- unnecessary private repository content.

Secret detection must run before committing a checkpoint when implementation tooling exists.

## 12. Current authorization state

```yaml
continuity_documentation_authorized: true
automatic_resume_authorized: false
candidate_repository_write_authorized: false
merge_authorized: false
deployment_authorized: false
Agents_02_to_15_enabled: false
```
