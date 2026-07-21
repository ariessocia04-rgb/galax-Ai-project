# ChatGPT New-Chat Bootstrap Prompt

Use this prompt when the prior ChatGPT conversation reaches maximum length, becomes unreliable, or must continue in a new chat.

```text
Continue the Galax AI project from repository evidence, not from assumed chat memory.

Repository:
ariessocia04-rgb/galax-Ai-project

MANDATORY CONTEXT-RECONSTRUCTION MODE

Do not edit files, create branches, commit, push, open a PR, merge, deploy, enable an LLM, or activate Agents 02–15 during this reconstruction step.

Read in this exact order:

1. README.md
2. AGENTS.md
3. docs/rules/CHATGPT_CONVERSATION_CONTINUITY_PROTOCOL.md
4. docs/handoff/CURRENT_CHAT_CONTEXT.md
5. the immutable chat-history handoff referenced by CURRENT_CHAT_CONTEXT.md, if one is listed
6. all applicable files under docs/rules/
7. the exact current plan, task packet, role charter, research record, and authorized prompt referenced by the handoff

Then verify from GitHub or the actual repository checkout:

- exact repository owner/name;
- selected branch;
- complete remote HEAD SHA;
- required base branch and base SHA;
- whether the branch is descended from the required base;
- current changed files and commits;
- active task lock and selected writer/reviewer;
- tests and evidence actually present;
- completed work versus pending work;
- contradictions, stale records, missing files, or unsupported claims.

Never use main as a fallback when another branch or SHA is required.
Never trust a previous-chat statement unless repository evidence confirms it.
Unknown facts must be reported as UNKNOWN_REQUIRES_VERIFICATION.

Return only this reconstruction report:

status: CONTEXT_VERIFIED | BLOCKED_CONTEXT_MISMATCH | BLOCKED_INSUFFICIENT_EVIDENCE
repository:
requested_branch:
actual_branch:
actual_remote_head_sha:
required_base_branch:
required_base_sha:
required_base_relationship_verified:
readme_read:
agents_md_read:
continuity_protocol_read:
current_handoff_read:
immutable_handoff_read:
canonical_documents_read: []
task_packet_found:
active_task_id:
selected_writer_or_reviewer:
task_lock_status:
current_scope:
completed_work_confirmed: []
pending_work_confirmed: []
files_and_commits_reviewed: []
tests_and_evidence_confirmed: []
claims_still_unverified: []
contradictions_or_stale_records: []
files_changed_during_reconstruction: []
blockers: []
next_safe_action:

Required restrictions:

- files_changed_during_reconstruction must be [];
- do not restart completed work;
- do not create an implementation branch from main;
- do not activate Agents 02–15;
- do not merge or deploy;
- do not conceal uncertainty;
- stop when branch, SHA, scope, lock, or evidence does not match.

After returning the report, wait for the human owner to approve the next task.
```

## User reminder

Start the new chat inside the same ChatGPT Project when available, then paste the prompt above. The repository reconstruction remains mandatory even when Project memory is available.
