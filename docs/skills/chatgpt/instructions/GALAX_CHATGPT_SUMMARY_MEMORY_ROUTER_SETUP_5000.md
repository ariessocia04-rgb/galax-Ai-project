# Galax ChatGPT Summary Memory and Router Setup

```yaml
status: ACTIVE_CANONICAL_CHATGPT_CONTEXT_SETUP
repository: ariessocia04-rgb/galax-Ai-project
router_ref: docs/chatgpt-skill-router-2026-08-02
router_path: docs/skills/chatgpt/00_GALAX_SKILL_ROUTER_MANAGER.md
character_count_contract: EXACTLY_5000_CHARACTERS
Galax_runtime_effect: none
source_or_tests_effect: none
final_authority: Human_Owner
```

## Purpose

This compact recovery memory is for any ChatGPT account or chat authorized to work on Galax AI. It prevents new, resumed, shared, or replacement chats from guessing where work stopped.

The repository is the source of truth. Chat memory only tells ChatGPT where to look. When pasted text, remembered context, or old summaries conflict with current repository evidence, the repository wins.

## Required startup

```text
fetch the canonical router from the exact repository, ref, and path
-> classify the Galax request
-> select exactly one primary $galax-* alias
-> resolve it through GALAX_REPOSITORY_SKILL_REGISTRY_V1
-> fetch the exact mapped Markdown skill from the same ref
-> load no more than two required dependency skills
-> read only minimum authoritative evidence
-> return one bounded result
-> stop
```

Do not require a native plugin when the mapped repository file is accessible. Do not load all skills, scan the full repository, invent a path, or continue automatically.

## Canonical routing

```yaml
REPOSITORY_STATE: $galax-repository-state-scope-guardian
CLINE_PROMPT: $galax-strict-cline-prompt-guardian
EVIDENCE_REVIEW: $galax-evidence-validation-acceptance-guardian
DRAFT_PR_REVIEW: $galax-draft-pr-exact-diff-reviewer
CONTINUITY_OR_ACHIEVEMENT: $galax-continuity-achievement-guardian
LOCKED_ARTIFACT: $galax-locked-artifact-guardian
CLEANUP_AUDIT: $galax-repository-cleanup-auditor
```

## Source-of-truth order

```text
README.md
-> AGENTS.md
-> docs/operations/CODE_RED.md
-> active contracts, plans, and rules required by the task
-> exact assignment, branch, SHA, PR, issue, test, diff, or receipt
-> latest checkpoint and achievement record when relevant
-> current GitHub evidence
-> historical records
-> old chat memory or summaries
```

A plan, issue description, PR description, or summary is not proof that a command, edit, test, commit, push, merge, or deployment happened.

## Evidence classes

```yaml
REMOTE_PROVEN: verified in current GitHub evidence
HUMAN_OWNER_PROVIDED_CLINE_EVIDENCE: exact local output, diff, command result, or receipt supplied by the owner
REPORTED_LOCAL_NOT_REMOTE_PROOF: local claim not visible remotely
UNKNOWN_OR_CONFLICTING: missing, stale, inconsistent, or insufficient evidence
```

Local Cline edit not committed or pushed is invisible to GitHub. Without an exact receipt, do not guess whether it exists, was saved, passed, or failed.

## No-guessing contract

ChatGPT must not guess the active branch, HEAD SHA, assignment, stop point, pending failure, completed test, accepted artifact, permission, or next action. Missing evidence must produce the smallest factual blocker:

```text
BLOCKED_REPOSITORY_ACCESS_REQUIRED
BLOCKED_ROUTER_OR_SKILL_UNAVAILABLE
BLOCKED_REPOSITORY_STATE_MISMATCH
BLOCKED_LOCAL_STATE_UNVERIFIED
BLOCKED_MISSING_EVIDENCE
BLOCKED_SCOPE_TOO_BROAD
BLOCKED_HUMAN_AUTHORIZATION_REQUIRED
```

A blocker must name the missing repository, ref, path, evidence, or authority. Never block only because an alias is not a native plugin after its mapped file was fetched.

## Work control

Use one task, one objective, one mode, and one stop condition. Investigation, save, validation, correction, commit, push, PR review, merge, and deployment are separate stages unless a live rule authorizes an exact combination.

Only one contributor may write to the same active worktree or files. Two ChatGPT chats may exist, but only one should actively control Cline. Another chat remains read-only unless it has separate authorized scope.

Human Owner-accepted work is LOCKED_ACCEPTED. Do not rerun, rewrite, restore, rename, delete, refactor, or broadly clean it without exact authorization.

## Summary-memory fields

```yaml
repository:
router_ref:
router_path:
current_project_phase:
verified_branch_and_SHA:
last_completed_actual_action:
completed_and_LOCKED_ACCEPTED_work:
pending_or_unproven_work:
current_exact_stop_point:
one_next_safe_action:
actions_not_to_repeat:
important_blockers:
```

Keep current facts, history, achievements, pending work, and local-only reports separate. Never store hidden chain-of-thought, credentials, API keys, private tokens, or unsupported completion claims.

## Final rule

```text
Memory tells ChatGPT where to look.
The router decides what to load.
The repository proves what is true.
The selected skill limits the task.
The Human Owner authorizes consequential action.
ChatGPT returns one bounded result and stops.
```

Another account needs its own GitHub authorization and Project instructions. This file does not prove any connection or automation is active.
